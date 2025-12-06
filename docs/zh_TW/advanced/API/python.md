> [!NOTE]
> 本文檔可能包含 AI 生成的內容。雖然我們力求準確，但仍可能存在不準確之處。請通過以下方式報告任何問題：
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - 社區貢獻（歡迎提交 PR！）

## Python API: do_translate_async_stream

### 概述
- `do_translate_async_stream` 是底層的非同步入口點，用於翻譯單個 `PDF` 並產生一個事件串流（進度/錯誤/完成）。
- 它適用於構建您自己的 `UI` 或 `CLI`，在這些場景中您需要即時進度並對結果擁有完全控制權。
- 它接受一個經過驗證的 `SettingsModel` 和一個檔案路徑，並返回一個字典事件的非同步產生器。

### 簽名
- 導入：`from pdf2zh_next.high_level import do_translate_async_stream`
- 呼叫：`async for event in do_translate_async_stream(settings, file): ...`
- 參數：
  - settings: SettingsModel。必須是有效的；該函數將呼叫 `settings.validate_settings()`。
  - file: str | pathlib.Path。要翻譯的單個 PDF 檔案。必須存在。

注意：

- `settings.basic.input_files` 在此函數中被忽略；僅翻譯給定的 `file`。
- 如果 `settings.basic.debug` 為 True，翻譯在主進程中運行；否則在子進程中運行。兩種情況的事件模式是相同的。

### 事件串流合約
非同步產生器會產生以下類型的 JSON 類字典事件：

- 階段摘要事件：`stage_summary`（可選，可能最先出現）
  - 欄位
    - `type`："stage_summary"
    - `stages`：物件列表 `{ "name": str, "percent": float }`，描述估計的工作分配
    - `part_index`：對於此摘要事件可能為 0
    - `total_parts`：總部分數（>= 1）

- 進度事件：`progress_start`、`progress_update`、`progress_end`
  - 通用欄位
    - `type`：上述之一
    - `stage`：人類可讀的階段名稱（例如："解析 PDF 並建立中間表示"、"翻譯段落"、"儲存 PDF"）
    - `stage_progress`：[0, 100] 內的浮點數，表示當前階段的進度
    - `overall_progress`：[0, 100] 內的浮點數，表示整體進度
    - `part_index`：當前部分索引（對於進度事件通常基於 1）
    - `total_parts`：總部分數（>= 1）。大型文件可能會自動分割。
    - `stage_current`：階段內的當前步驟
    - `stage_total`：階段內的總步驟數

- 完成事件：`finish`
  - 欄位
    - `type`："finish"
    - `translate_result`：一個提供最終輸出的**物件**（注意：不是字典，而是類別實例）
      - `original_pdf_path`：輸入 PDF 的路徑
      - `mono_pdf_path`：單語翻譯 PDF 的路徑（或 None）
      - `dual_pdf_path`：雙語翻譯 PDF 的路徑（或 None）
      - `no_watermark_mono_pdf_path`：無浮水印的單語輸出路徑（如果已產生），否則為 None
      - `no_watermark_dual_pdf_path`：無浮水印的雙語輸出路徑（如果已產生），否則為 None
      - `auto_extracted_glossary_path`：自動擷取的術語表 CSV 路徑（或 None）
      - `total_seconds`：經過的秒數（浮點數）
      - `peak_memory_usage`：翻譯期間的近似峰值記憶體使用量（浮點數；實作依賴的單位）

- 錯誤事件：`error`
  - 欄位
    - `type`："error"
    - `error`：人類可讀的錯誤訊息
    - `error_type`：其中之一為 `BabeldocError`、`SubprocessError`、`IPCError`、`SubprocessCrashError` 等。
    - `details`：可選的詳細資訊（例如，原始錯誤或追溯資訊）

重要行為：
- 在進度開始之前，可能會發出一個可選的 `stage_summary`。
- 在某些失敗情況下，生成器將首先產生一個 `error` 事件，然後引發一個源自 `TranslationError` 的異常。您應該同時檢查錯誤事件並準備好捕獲異常。
- `progress_update` 事件可能會重複出現相同的值；必要時，消費者應進行去抖動處理。
- 當您收到 `finish` 事件時，請停止消費串流。

### 最小使用範例（非同步）
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

### 取消
您可以取消消耗串流的任務。取消操作會傳播到底層的翻譯過程。

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

### 事件形狀示例
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

進度事件（範例）：
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

完成事件（範例）：
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

錯誤事件（範例）：
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### 注意事項與最佳實踐
- 始終處理來自生成器的錯誤事件和異常。
- 在 `finish` 事件時中斷循環，以避免不必要的工作。
- 在調用前確保 `file` 存在且 `settings.validate_settings()` 通過驗證。
- 大型文件可能會被拆分；使用 `part_index/total_parts` 和 `overall_progress` 來驅動您的用戶界面。
- 如果您的用戶界面對重複、相同的更新敏感，請對 `progress_update` 進行防抖處理。
- `report_interval` (SettingsModel)：僅控制 `progress_update` 事件的發射速率。它不影響 `stage_summary`、`progress_start`、`progress_end` 或 `finish`。默認值為 0.1 秒，允許的最小值為 0.05 秒。根據進度監控邏輯，當 `stage_total <= 3` 時，更新不受 `report_interval` 的限制。

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>