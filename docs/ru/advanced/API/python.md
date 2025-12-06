> [!NOTE]
> Эта документация может содержать контент, созданный искусственным интеллектом. Хотя мы стремимся к точности, могут быть неточности. Пожалуйста, сообщайте о любых проблемах через:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Вклад сообщества (PR приветствуются!)

## Python API: do_translate_async_stream

### Обзор
- do_translate_async_stream — это низкоуровневая асинхронная точка входа, которая переводит один PDF-файл и генерирует поток событий (прогресс/ошибка/завершение).
- Она подходит для создания собственного пользовательского интерфейса или интерфейса командной строки, где требуется прогресс в реальном времени и полный контроль над результатами.
- Она принимает проверенную SettingsModel и путь к файлу и возвращает асинхронный генератор событий в виде словарей.

### Подпись
- Импорт: `from pdf2zh_next.high_level import do_translate_async_stream`
- Вызов: `async for event in do_translate_async_stream(settings, file): ...`
- Параметры:
  - settings: SettingsModel. Должен быть валидным; функция вызовет `settings.validate_settings()`.
  - file: str | pathlib.Path. Единичный PDF-файл для перевода. Должен существовать.

Примечание:

- `settings.basic.input_files` игнорируется этой функцией; переводится только указанный `file`.
- Если `settings.basic.debug` имеет значение True, перевод выполняется в основном процессе; в противном случае он выполняется в подпроцессе. Схема событий идентична в обоих случаях.

### Контракт потока событий
Асинхронный генератор возвращает события в виде словарей, похожих на JSON, со следующими типами:

- Событие сводки этапов: `stage_summary` (опционально, может появиться первым)
  - Поля
    - `type`: "stage_summary"
    - `stages`: список объектов `{ "name": str, "percent": float }`, описывающих предполагаемое распределение работы
    - `part_index`: может быть 0 для этого сводного события
    - `total_parts`: общее количество частей (>= 1)

- События прогресса: `progress_start`, `progress_update`, `progress_end`
  - Общие поля
    - `type`: один из вышеперечисленных
    - `stage`: читаемое человеком название этапа (например, "Разбор PDF и создание промежуточного представления", "Перевод абзацев", "Сохранение PDF")
    - `stage_progress`: число с плавающей точкой в [0, 100], указывающее прогресс в текущем этапе
    - `overall_progress`: число с плавающей точкой в [0, 100], указывающее общий прогресс
    - `part_index`: индекс текущей части (обычно начинается с 1 для событий прогресса)
    - `total_parts`: общее количество частей (>= 1). Большие документы могут быть разделены автоматически.
    - `stage_current`: текущий шаг в рамках этапа
    - `stage_total`: общее количество шагов в рамках этапа

- Событие завершения: `finish`
  - Поля
    - `type`: "finish"
    - `translate_result`: **объект**, предоставляющий финальные результаты (ПРИМЕЧАНИЕ: не словарь, а экземпляр класса)
      - `original_pdf_path`: Путь к исходному PDF
      - `mono_pdf_path`: Путь к переведенному одностраничному PDF (или None)
      - `dual_pdf_path`: Путь к переведенному двуязычному PDF (или None)
      - `no_watermark_mono_pdf_path`: Путь к одностраничному выводу без водяного знака (если создан), иначе None
      - `no_watermark_dual_pdf_path`: Путь к двуязычному выводу без водяного знака (если создан), иначе None
      - `auto_extracted_glossary_path`: Путь к автоматически извлеченному глоссарию CSV (или None)
      - `total_seconds`: затраченные секунды (число с плавающей точкой)
      - `peak_memory_usage`: приблизительное пиковое использование памяти во время перевода (число с плавающей точкой; единицы измерения зависят от реализации)

- Событие ошибки: `error`
  - Поля
    - `type`: "error"
    - `error`: читаемое человеком сообщение об ошибке
    - `error_type`: один из `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError` и т.д.
    - `details`: опциональные детали (например, исходная ошибка или трассировка стека)

Важное поведение:
- Необязательный `stage_summary` может быть выдан до начала прогресса.
- При определенных сбоях генератор сначала выдаст событие `error`, а затем вызовет исключение, производное от `TranslationError`. Вам следует как проверять наличие событий ошибок, так и быть готовым перехватывать исключения.
- События `progress_update` могут повторяться с одинаковыми значениями; потребители должны устранять дребезг, если это необходимо.
- Прекратите потреблять поток, когда получите событие `finish`.

### Минимальный пример использования (Асинхронный)
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

### Отмена
Вы можете отменить задачу, потребляющую поток. Отмена распространяется на базовый процесс перевода.

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

### Примеры форм событий
Сводное событие этапа (пример):
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

Событие прогресса (пример):
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

Событие завершения (пример):
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

Событие ошибки (пример):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Примечания и рекомендации
- Всегда обрабатывайте как события ошибок, так и исключения из генератора.
- Прерывайте цикл при событии `finish`, чтобы избежать ненужной работы.
- Убедитесь, что `file` существует и `settings.validate_settings()` проходит успешно перед вызовом.
- Большие документы могут быть разделены; используйте `part_index/total_parts` и `overall_progress` для управления вашим пользовательским интерфейсом.
- Дебаунсируйте `progress_update`, если ваш пользовательский интерфейс чувствителен к повторяющимся, идентичным обновлениям.
- `report_interval` (SettingsModel): управляет только частотой генерации событий `progress_update`. Он не влияет на `stage_summary`, `progress_start`, `progress_end` или `finish`. По умолчанию 0.1с, минимально допустимое значение — 0.05с. Согласно логике монитора прогресса, когда `stage_total <= 3`, обновления не регулируются `report_interval`.

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>