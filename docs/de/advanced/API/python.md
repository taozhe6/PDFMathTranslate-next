> [!NOTE]
> Diese Dokumentation kann KI-generierte Inhalte enthalten. Obwohl wir auf Genauigkeit achten, kann es zu Ungenauigkeiten kommen. Bitte melden Sie etwaige Probleme über:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Gemeinschaftsbeiträge (PRs sind willkommen!)

## Python API: do_translate_async_stream

### Übersicht
- do_translate_async_stream ist der Low-Level-Async-Einstiegspunkt, der eine einzelne PDF übersetzt und einen Stream von Ereignissen (Fortschritt/Fehler/Fertigstellung) liefert.
- Es eignet sich zum Erstellen Ihrer eigenen Benutzeroberfläche oder Kommandozeile, bei der Sie Echtzeit-Fortschritt und volle Kontrolle über die Ergebnisse wünschen.
- Es akzeptiert ein validiertes SettingsModel und einen Dateipfad und gibt einen asynchronen Generator von Dict-Ereignissen zurück.

### Signatur
- Import: `from pdf2zh_next.high_level import do_translate_async_stream`
- Aufruf: `async for event in do_translate_async_stream(settings, file): ...`
- Parameter:
  - settings: SettingsModel. Muss gültig sein; die Funktion ruft `settings.validate_settings()` auf.
  - file: str | pathlib.Path. Die einzelne zu übersetzende PDF. Muss existieren.

Hinweis:

- `settings.basic.input_files` wird von dieser Funktion ignoriert; nur die angegebene `file` wird übersetzt.
- Wenn `settings.basic.debug` True ist, läuft die Übersetzung im Hauptprozess; andernfalls läuft sie in einem Unterprozess. Das Ereignisschema ist für beide identisch.

### Event-Stream-Vertrag
Der asynchrone Generator liefert JSON-ähnliche Dict-Ereignisse mit den folgenden Typen:

-   Stufenzusammenfassungsereignis: `stage_summary` (optional, kann zuerst erscheinen)
    -   Felder
        -   `type`: "stage_summary"
        -   `stages`: Liste von Objekten `{ "name": str, "percent": float }`, die die geschätzte Arbeitsverteilung beschreiben
        -   `part_index`: kann für dieses Zusammenfassungsereignis 0 sein
        -   `total_parts`: Gesamtzahl der Teile (>= 1)

-   Fortschrittsereignisse: `progress_start`, `progress_update`, `progress_end`
    -   Gemeinsame Felder
        -   `type`: einer der oben genannten
        -   `stage`: menschenlesbarer Stufenname (z. B. "PDF parsen und Zwischendarstellung erstellen", "Absätze übersetzen", "PDF speichern")
        -   `stage_progress`: Float in [0, 100], der den Fortschritt innerhalb der aktuellen Stufe anzeigt
        -   `overall_progress`: Float in [0, 100], der den Gesamtfortschritt anzeigt
        -   `part_index`: aktueller Teilindex (typischerweise 1-basiert für Fortschrittsereignisse)
        -   `total_parts`: Gesamtzahl der Teile (>= 1). Große Dokumente können automatisch aufgeteilt werden.
        -   `stage_current`: aktueller Schritt innerhalb der Stufe
        -   `stage_total`: Gesamtschritte innerhalb der Stufe

-   Abschlussereignis: `finish`
    -   Felder
        -   `type`: "finish"
        -   `translate_result`: ein **Objekt**, das die endgültigen Ausgaben bereitstellt (HINWEIS: kein Wörterbuch, sondern eine Klasseninstanz)
            -   `original_pdf_path`: Pfad zur Eingabe-PDF
            -   `mono_pdf_path`: Pfad zur einsprachig übersetzten PDF (oder None)
            -   `dual_pdf_path`: Pfad zur zweisprachig übersetzten PDF (oder None)
            -   `no_watermark_mono_pdf_path`: Pfad zur einsprachigen Ausgabe ohne Wasserzeichen (falls erstellt), sonst None
            -   `no_watermark_dual_pdf_path`: Pfad zur zweisprachigen Ausgabe ohne Wasserzeichen (falls erstellt), sonst None
            -   `auto_extracted_glossary_path`: Pfad zur automatisch extrahierten Glossar-CSV (oder None)
            -   `total_seconds`: verstrichene Sekunden (Float)
            -   `peak_memory_usage`: ungefährer Spitzenspeicherverbrauch während der Übersetzung (Float; implementierungsabhängige Einheiten)

-   Fehlerereignis: `error`
    -   Felder
        -   `type`: "error"
        -   `error`: menschenlesbare Fehlermeldung
        -   `error_type`: einer von `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
        -   `details`: optionale Details (z. B. ursprünglicher Fehler oder Traceback)

Wichtiges Verhalten:
- Ein optionales `stage_summary` kann ausgegeben werden, bevor der Fortschritt beginnt.
- Bei bestimmten Fehlern wird der Generator zuerst ein `error`-Ereignis liefern und dann eine Ausnahme auslösen, die von `TranslationError` abgeleitet ist. Sie sollten sowohl auf Fehlerereignisse prüfen als auch darauf vorbereitet sein, Ausnahmen abzufangen.
- `progress_update`-Ereignisse können sich mit identischen Werten wiederholen; Verbraucher sollten bei Bedarf entprellen.
- Beenden Sie den Verbrauch des Streams, wenn Sie ein `finish`-Ereignis erhalten.

### Minimales Verwendungsbeispiel (Async)
```python
import asyncio
from pathlib import Path
from pdf2zh_next.high_level import do_translate_async_stream

# Assume you already have a valid SettingsModel instance named `settings`
# and a PDF file path

async def translate_one(settings, pdf_path: str | Path):
    try:
        async for event in do_translate_async_stream(settings, pdf_path):
            etype = event.get("type")

            if etype == "stage_summary":
                # Optional pre-flight summary of stages
                stages = event.get("stages", [])
                print("Stage summary:", ", ".join(f"{s['name']}:{s['percent']:.2f}" for s in stages))

            elif etype in {"progress_start", "progress_update", "progress_end"}:
                stage = event.get("stage")
                stage_prog = event.get("stage_progress")  # 0..100
                overall = event.get("overall_progress")  # 0..100
                part_i = event.get("part_index")
                part_n = event.get("total_parts")
                print(f"[{etype}] {stage} | stage {stage_prog:.1f}% | overall {overall:.1f}% (part {part_i}/{part_n})")

            elif etype == "error":
                # You will also get a raised exception after this yield
                print("[error]", event.get("error"), event.get("error_type"))

            elif etype == "finish":
                result = event["translate_result"]
                print("Done in", getattr(result, "total_seconds", None), "s")
                print("Mono:", getattr(result, "mono_pdf_path", None))
                print("Dual:", getattr(result, "dual_pdf_path", None))
                print("No-watermark Mono:", getattr(result, "no_watermark_mono_pdf_path", None))
                print("No-watermark Dual:", getattr(result, "no_watermark_dual_pdf_path", None))
                print("Glossary:", getattr(result, "auto_extracted_glossary_path", None))
                print("Peak memory:", getattr(result, "peak_memory_usage", None))
                break

    except Exception as exc:
        # Catch exceptions raised by the stream after an error event
        print("Translation failed:", exc)

# asyncio.run(translate_one(settings, "/path/to/file.pdf"))
```

### Stornierung
Sie können die Aufgabe abbrechen, die den Stream verbraucht. Die Stornierung wird an den zugrunde liegenden Übersetzungsprozess weitergegeben.

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream

async def cancellable(settings, pdf):
    task = asyncio.create_task(_consume(settings, pdf))
    await asyncio.sleep(1.0)  # let it start
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Cancelled")

async def _consume(settings, pdf):
    async for event in do_translate_async_stream(settings, pdf):
        if event["type"] == "finish":
            break
```

### Beispielhafte Ereignisformen
Stadiumszusammenfassungsereignis (Beispiel):
```json
{
  "type": "stage_summary",
  "stages": [
    {"name": "Parse PDF and Create Intermediate Representation", "percent": 0.1086},
    {"name": "DetectScannedFile", "percent": 0.0188},
    {"name": "Parse Page Layout", "percent": 0.1079}
    // ... more stages ...
  ],
  "part_index": 0,
  "total_parts": 1
}
```

Progress-Ereignis (Beispiel):
```json
{
  "type": "progress_update",
  "stage": "Translate Paragraphs",
  "stage_progress": 2.04,
  "stage_current": 1,
  "stage_total": 49,
  "overall_progress": 53.44,
  "part_index": 1,
  "total_parts": 1
}
```

Finish-Ereignis (Beispiel):
```json
{
  "type": "finish",
  "translate_result": {
    "original_pdf_path": "pdf2zh_files/<session>/table.pdf",
    "mono_pdf_path": "pdf2zh_files/<session>/table.zh-CN.mono.pdf",
    "dual_pdf_path": "pdf2zh_files/<session>/table.zh-CN.dual.pdf",
    "no_watermark_mono_pdf_path": "pdf2zh_files/<session>/table.no_watermark.zh-CN.mono.pdf",
    "no_watermark_dual_pdf_path": "pdf2zh_files/<session>/table.no_watermark.zh-CN.dual.pdf",
    "auto_extracted_glossary_path": "pdf2zh_files/<session>/table.zh-CN.glossary.csv",
    "total_seconds": 42.83,
    "peak_memory_usage": 4651.55
  }
}
```

Fehlerereignis (Beispiel):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Hinweise & Best Practices
-   Sowohl Fehlerereignisse als auch Ausnahmen vom Generator müssen immer behandelt werden.
-   Unterbrechen Sie die Schleife bei `finish`, um unnötige Arbeit zu vermeiden.
-   Stellen Sie sicher, dass die `file` existiert und `settings.validate_settings()` erfolgreich ist, bevor Sie die Funktion aufrufen.
-   Große Dokumente können aufgeteilt werden; verwenden Sie `part_index/total_parts` und `overall_progress`, um Ihre Benutzeroberfläche zu steuern.
-   Entprellen Sie `progress_update`, wenn Ihre Benutzeroberfläche empfindlich auf wiederholte, identische Aktualisierungen reagiert.
-   `report_interval` (SettingsModel): Steuert nur die Ausgaberate von `progress_update`-Ereignissen. Es beeinflusst nicht `stage_summary`, `progress_start`, `progress_end` oder `finish`. Der Standardwert ist 0,1s und das zulässige Minimum ist 0,05s. Gemäß der Fortschrittsmonitor-Logik werden bei `stage_total <= 3` Aktualisierungen nicht durch `report_interval` gedrosselt.

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>