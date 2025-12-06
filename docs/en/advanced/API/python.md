> [!NOTE]
> This documentation may contain AI-generated content. While we strive for accuracy, there might be inaccuracies. Please report any issues via:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Community contribution (PRs welcome!)

## Python API: do_translate_async_stream

### Overview
- do_translate_async_stream is the low-level async entrypoint that translates a single PDF and yields a stream of events (progress/error/finish).
- It is suitable for building your own UI or CLI where you want real-time progress and full control over results.
- It accepts a validated SettingsModel and a file path and returns an async generator of dict events.

### Signature
- Import: `from pdf2zh_next.high_level import do_translate_async_stream`
- Call: `async for event in do_translate_async_stream(settings, file): ...`
- Parameters:
  - settings: SettingsModel. Must be valid; the function will call `settings.validate_settings()`.
  - file: str | pathlib.Path. The single PDF to translate. Must exist.

Note:

- `settings.basic.input_files` is ignored by this function; only the given `file` is translated.
- If `settings.basic.debug` is True, translation runs in the main process; otherwise it runs in a subprocess. Event schema is identical for both.

### Event Stream Contract
The async generator yields JSON-like dict events with the following types:

- Stage summary event: `stage_summary` (optional, may appear first)
  - Fields
    - `type`: "stage_summary"
    - `stages`: list of objects `{ "name": str, "percent": float }` describing the estimated work distribution
    - `part_index`: may be 0 for this summary event
    - `total_parts`: total number of parts (>= 1)

- Progress events: `progress_start`, `progress_update`, `progress_end`
  - Common fields
    - `type`: one of the above
    - `stage`: human-readable stage name (e.g., "Parse PDF and Create Intermediate Representation", "Translate Paragraphs", "Save PDF")
    - `stage_progress`: float in [0, 100] indicating progress within the current stage
    - `overall_progress`: float in [0, 100] indicating overall progress
    - `part_index`: current part index (typically 1-based for progress events)
    - `total_parts`: total number of parts (>= 1). Large documents may be split automatically.
    - `stage_current`: current step within the stage
    - `stage_total`: total steps within the stage

- Finish event: `finish`
  - Fields
    - `type`: "finish"
    - `translate_result`: an **object** providing final outputs (NOTE: not a dictionary, but a class instance)
      - `original_pdf_path`: Path to the input PDF
      - `mono_pdf_path`: Path to the monolingual translated PDF (or None)
      - `dual_pdf_path`: Path to the bilingual translated PDF (or None)
      - `no_watermark_mono_pdf_path`: Path to monolingual output without watermark (if produced), otherwise None
      - `no_watermark_dual_pdf_path`: Path to bilingual output without watermark (if produced), otherwise None
      - `auto_extracted_glossary_path`: Path to auto-extracted glossary CSV (or None)
      - `total_seconds`: elapsed seconds (float)
      - `peak_memory_usage`: approximate peak memory usage during translation (float; implementation-dependent units)

- Error event: `error`
  - Fields
    - `type`: "error"
    - `error`: human-readable error message
    - `error_type`: one of `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details`: optional details (e.g., original error or traceback)

Important behavior:
- An optional `stage_summary` may be emitted before progress begins.
- On certain failures, the generator will first yield an `error` event and then raise an exception derived from `TranslationError`. You should both check for error events and be prepared to catch exceptions.
- `progress_update` events may repeat with identical values; consumers should debounce if necessary.
- Stop consuming the stream when you receive a `finish` event.

### Minimal Usage Example (Async)
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

### Cancellation
You can cancel the task consuming the stream. Cancellation is propagated to the underlying translation process.

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

### Example Event Shapes
Stage summary event (example):
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

Progress event (example):
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

Finish event (example):
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

Error event (example):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Notes & Best Practices
- Always handle both error events and exceptions from the generator.
- Break the loop on `finish` to avoid unnecessary work.
- Ensure the `file` exists and `settings.validate_settings()` passes before calling.
- Large documents may be split; use `part_index/total_parts` and `overall_progress` to drive your UI.
- Debounce `progress_update` if your UI is sensitive to repeated, identical updates.
- `report_interval` (SettingsModel): controls only the emission rate of `progress_update` events. It does not affect `stage_summary`, `progress_start`, `progress_end`, or `finish`. Default is 0.1s and the minimum allowed is 0.05s. As per the progress monitor logic, when `stage_total <= 3`, updates are not throttled by `report_interval`.

