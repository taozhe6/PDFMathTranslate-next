> [!NOTE]
> Esta documentación puede contener contenido generado por IA. Aunque nos esforzamos por la precisión, pueden existir inexactitudes. Por favor, reporte cualquier problema a través de:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Contribución de la comunidad (¡PRs son bienvenidas!)

## Python API: do_translate_async_stream

### Resumen
- do_translate_async_stream es el punto de entrada asíncrono de bajo nivel que traduce un único PDF y produce un flujo de eventos (progreso/error/finalización).
- Es adecuado para construir tu propia interfaz de usuario o CLI donde desees progreso en tiempo real y control total sobre los resultados.
- Acepta un SettingsModel validado y una ruta de archivo, y devuelve un generador asíncrono de eventos dict.

### Firma
- Importar: `from pdf2zh_next.high_level import do_translate_async_stream`
- Llamar: `async for event in do_translate_async_stream(settings, file): ...`
- Parámetros:
  - settings: SettingsModel. Debe ser válido; la función llamará a `settings.validate_settings()`.
  - file: str | pathlib.Path. El único PDF a traducir. Debe existir.

Nota:

- `settings.basic.input_files` es ignorado por esta función; solo se traduce el `file` proporcionado.
- Si `settings.basic.debug` es True, la traducción se ejecuta en el proceso principal; de lo contrario, se ejecuta en un subproceso. El esquema de eventos es idéntico en ambos casos.

### Contrato de flujo de eventos
El generador asíncrono produce eventos de tipo dict similares a JSON con los siguientes tipos:

- Evento de resumen de etapa: `stage_summary` (opcional, puede aparecer primero)
  - Campos
    - `type`: "stage_summary"
    - `stages`: lista de objetos `{ "name": str, "percent": float }` que describe la distribución estimada del trabajo
    - `part_index`: puede ser 0 para este evento de resumen
    - `total_parts`: número total de partes (>= 1)

- Eventos de progreso: `progress_start`, `progress_update`, `progress_end`
  - Campos comunes
    - `type`: uno de los anteriores
    - `stage`: nombre de la etapa legible por humanos (por ejemplo, "Analizar PDF y Crear Representación Intermedia", "Traducir Párrafos", "Guardar PDF")
    - `stage_progress`: flotante en [0, 100] que indica el progreso dentro de la etapa actual
    - `overall_progress`: flotante en [0, 100] que indica el progreso general
    - `part_index`: índice de la parte actual (típicamente basado en 1 para eventos de progreso)
    - `total_parts`: número total de partes (>= 1). Los documentos grandes pueden dividirse automáticamente.
    - `stage_current`: paso actual dentro de la etapa
    - `stage_total`: pasos totales dentro de la etapa

- Evento de finalización: `finish`
  - Campos
    - `type`: "finish"
    - `translate_result`: un **objeto** que proporciona las salidas finales (NOTA: no es un diccionario, sino una instancia de clase)
      - `original_pdf_path`: Ruta al PDF de entrada
      - `mono_pdf_path`: Ruta al PDF traducido monolingüe (o None)
      - `dual_pdf_path`: Ruta al PDF traducido bilingüe (o None)
      - `no_watermark_mono_pdf_path`: Ruta a la salida monolingüe sin marca de agua (si se produjo), de lo contrario None
      - `no_watermark_dual_pdf_path`: Ruta a la salida bilingüe sin marca de agua (si se produjo), de lo contrario None
      - `auto_extracted_glossary_path`: Ruta al glosario CSV extraído automáticamente (o None)
      - `total_seconds`: segundos transcurridos (flotante)
      - `peak_memory_usage`: uso máximo aproximado de memoria durante la traducción (flotante; unidades dependientes de la implementación)

- Evento de error: `error`
  - Campos
    - `type`: "error"
    - `error`: mensaje de error legible por humanos
    - `error_type`: uno de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details`: detalles opcionales (por ejemplo, error original o traza de ejecución)

Comportamiento importante:
- Se puede emitir un `stage_summary` opcional antes de que comience el progreso.
- En ciertos fallos, el generador primero producirá un evento `error` y luego lanzará una excepción derivada de `TranslationError`. Debes verificar tanto los eventos de error como estar preparado para capturar excepciones.
- Los eventos `progress_update` pueden repetirse con valores idénticos; los consumidores deben aplicar debounce si es necesario.
- Deja de consumir el flujo cuando recibas un evento `finish`.

### Ejemplo de uso mínimo (Asíncrono)
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

### Cancelación
Puedes cancelar la tarea consumiendo el flujo. La cancelación se propaga al proceso de traducción subyacente.

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

### Formas de eventos de ejemplo
Evento de resumen de etapa (ejemplo):
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

Evento de progreso (ejemplo):
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

Evento de finalización (ejemplo):
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

Evento de error (ejemplo):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Notas y mejores prácticas
-   Maneja siempre tanto los eventos de error como las excepciones del generador.
-   Rompe el bucle en `finish` para evitar trabajo innecesario.
-   Asegúrate de que el `file` exista y que `settings.validate_settings()` pase antes de llamar.
-   Los documentos grandes pueden dividirse; usa `part_index/total_parts` y `overall_progress` para impulsar tu interfaz de usuario.
-   Debounce `progress_update` si tu interfaz de usuario es sensible a actualizaciones repetidas e idénticas.
-   `report_interval` (SettingsModel): controla solo la tasa de emisión de eventos `progress_update`. No afecta a `stage_summary`, `progress_start`, `progress_end` o `finish`. El valor predeterminado es 0.1s y el mínimo permitido es 0.05s. Según la lógica del monitor de progreso, cuando `stage_total <= 3`, las actualizaciones no se limitan por `report_interval`.

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>