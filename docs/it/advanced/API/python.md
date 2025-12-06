> [!NOTE]
> Questa documentazione potrebbe contenere contenuti generati dall'IA. Sebbene ci impegniamo per l'accuratezza, potrebbero esserci delle imprecisioni. Si prega di segnalare eventuali problemi tramite:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Contributo della comunità (PR sono benvenuti!)

## Python API: do_translate_async_stream

### Panoramica
- do_translate_async_stream è il punto di ingresso asincrono di basso livello che traduce un singolo PDF e restituisce un flusso di eventi (progresso/errore/fine).
- È adatto per costruire la propria UI o CLI in cui si desidera un progresso in tempo reale e il controllo completo sui risultati.
- Accetta un SettingsModel validato e un percorso del file e restituisce un generatore asincrono di eventi dict.

### Firma
- Import: `from pdf2zh_next.high_level import do_translate_async_stream`
- Chiamata: `async for event in do_translate_async_stream(settings, file): ...`
- Parametri:
  - settings: SettingsModel. Deve essere valido; la funzione chiamerà `settings.validate_settings()`.
  - file: str | pathlib.Path. Il singolo PDF da tradurre. Deve esistere.

NOTE

- `settings.basic.input_files` viene ignorato da questa funzione; viene tradotto solo il `file` specificato.
- Se `settings.basic.debug` è True, la traduzione viene eseguita nel processo principale; altrimenti viene eseguita in un sottoprocesso. Lo schema degli eventi è identico in entrambi i casi.

### Contratto del flusso di eventi
Il generatore asincrono produce eventi di tipo dict simili a JSON con i seguenti tipi:

- Evento di riepilogo fase: `stage_summary` (opzionale, può apparire per primo)
  - Campi
    - `type`: "stage_summary"
    - `stages`: lista di oggetti `{ "name": str, "percent": float }` che descrivono la distribuzione stimata del lavoro
    - `part_index`: può essere 0 per questo evento di riepilogo
    - `total_parts`: numero totale di parti (>= 1)

- Eventi di avanzamento: `progress_start`, `progress_update`, `progress_end`
  - Campi comuni
    - `type`: uno dei precedenti
    - `stage`: nome della fase leggibile dall'uomo (ad es. "Analizza PDF e Crea Rappresentazione Intermedia", "Traduci Paragrafi", "Salva PDF")
    - `stage_progress`: float in [0, 100] che indica l'avanzamento all'interno della fase corrente
    - `overall_progress`: float in [0, 100] che indica l'avanzamento complessivo
    - `part_index`: indice della parte corrente (tipicamente basato su 1 per gli eventi di avanzamento)
    - `total_parts`: numero totale di parti (>= 1). Documenti di grandi dimensioni possono essere suddivisi automaticamente.
    - `stage_current`: passo corrente all'interno della fase
    - `stage_total`: passi totali all'interno della fase

- Evento di completamento: `finish`
  - Campi
    - `type`: "finish"
    - `translate_result`: un **oggetto** che fornisce gli output finali (NOTA: non un dizionario, ma un'istanza di classe)
      - `original_pdf_path`: Percorso del PDF di input
      - `mono_pdf_path`: Percorso del PDF tradotto monolingue (o None)
      - `dual_pdf_path`: Percorso del PDF tradotto bilingue (o None)
      - `no_watermark_mono_pdf_path`: Percorso dell'output monolingue senza filigrana (se prodotto), altrimenti None
      - `no_watermark_dual_pdf_path`: Percorso dell'output bilingue senza filigrana (se prodotto), altrimenti None
      - `auto_extracted_glossary_path`: Percorso del glossario CSV estratto automaticamente (o None)
      - `total_seconds`: secondi trascorsi (float)
      - `peak_memory_usage`: utilizzo approssimativo della memoria di picco durante la traduzione (float; unità dipendenti dall'implementazione)

- Evento di errore: `error`
  - Campi
    - `type`: "error"
    - `error`: messaggio di errore leggibile dall'uomo
    - `error_type`: uno tra `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, ecc.
    - `details`: dettagli opzionali (ad es. errore originale o traceback)

Comportamento importante:
- Un `stage_summary` opzionale può essere emesso prima che il progresso inizi.
- In caso di determinati fallimenti, il generatore emetterà prima un evento `error` e poi solleverà un'eccezione derivata da `TranslationError`. Dovresti sia controllare la presenza di eventi di errore che essere pronto a catturare le eccezioni.
- Gli eventi `progress_update` possono ripetersi con valori identici; i consumatori dovrebbero eseguire il debounce se necessario.
- Interrompi il consumo del flusso quando ricevi un evento `finish`.

### Esempio di utilizzo minimo (Async)
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

### Annullamento
Puoi annullare l'attività consumando il flusso. L'annullamento viene propagato al processo di traduzione sottostante.

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

### Forme di Evento di Esempio
Riepilogo dello stage evento (esempio):
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

Progress event (esempio):
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

Finish event (esempio):
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

Evento di errore (esempio):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Note e migliori pratiche
- Gestire sempre sia gli eventi di errore che le eccezioni dal generatore.
- Interrompere il ciclo su `finish` per evitare lavoro non necessario.
- Assicurarsi che il `file` esista e che `settings.validate_settings()` passi prima della chiamata.
- I documenti di grandi dimensioni potrebbero essere divisi; utilizzare `part_index/total_parts` e `overall_progress` per guidare la tua UI.
- Debounce `progress_update` se la tua UI è sensibile a ripetuti aggiornamenti identici.
- `report_interval` (SettingsModel): controlla solo la frequenza di emissione degli eventi `progress_update`. Non influisce su `stage_summary`, `progress_start`, `progress_end` o `finish`. Il valore predefinito è 0.1s e il minimo consentito è 0.05s. Come da logica del monitor di avanzamento, quando `stage_total <= 3`, gli aggiornamenti non sono limitati da `report_interval`.

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>