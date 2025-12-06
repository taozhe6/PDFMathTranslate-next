> [!NOTE]
> このドキュメントには AI 生成コンテンツが含まれている可能性があります。正確性を心がけていますが、不正確な点があるかもしれません。問題があれば以下から報告してください：
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - コミュニティ貢献（プルリクエスト歓迎！）

## Python API: do_translate_async_stream

### 概要
- do_translate_async_stream は、単一の PDF を翻訳し、イベント（進捗状況／エラー／完了）のストリームを生成する低レベルの非同期エントリーポイントです。
- リアルタイムの進捗状況と結果の完全な制御を望む独自の UI または CLI を構築する場合に適しています。
- 検証済みの SettingsModel とファイルパスを受け取り、dict イベントの非同期ジェネレータを返します。

### 署名
- インポート：`from pdf2zh_next.high_level import do_translate_async_stream`
- 呼び出し：`async for event in do_translate_async_stream(settings, file): ...`
- パラメータ：
  - settings: SettingsModel。有効である必要があります。関数は `settings.validate_settings()` を呼び出します。
  - file: str | pathlib.Path。翻訳する単一の PDF ファイル。存在する必要があります。

注記：

- `settings.basic.input_files` はこの関数では無視され、指定された `file` のみが翻訳されます。
- `settings.basic.debug` が True の場合、翻訳はメインプロセスで実行されます。それ以外の場合はサブプロセスで実行されます。どちらの場合もイベントスキーマは同一です。

### イベントストリーム契約
非同期ジェネレータは以下のタイプの JSON ライクな辞書イベントを生成します：

- ステージ概要イベント：`stage_summary`（オプション、最初に表示される場合があります）
  - フィールド
    - `type`: "stage_summary"
    - `stages`: 推定作業配分を記述するオブジェクト `{ "name": str, "percent": float }` のリスト
    - `part_index`: この概要イベントでは 0 になる場合があります
    - `total_parts`: パートの総数（>= 1）

- 進捗イベント：`progress_start`、`progress_update`、`progress_end`
  - 共通フィールド
    - `type`: 上記のいずれか
    - `stage`: 人間が読めるステージ名（例：「PDF の解析と中間表現の作成」、「段落の翻訳」、「PDF の保存」）
    - `stage_progress`: 現在のステージ内の進捗を示す [0, 100] の浮動小数点数
    - `overall_progress`: 全体の進捗を示す [0, 100] の浮動小数点数
    - `part_index`: 現在のパートインデックス（進捗イベントでは通常 1 から始まる）
    - `total_parts`: パートの総数（>= 1）。大きな文書は自動的に分割される場合があります。
    - `stage_current`: ステージ内の現在のステップ
    - `stage_total`: ステージ内の総ステップ数

- 終了イベント：`finish`
  - フィールド
    - `type`: "finish"
    - `translate_result`: 最終出力を提供する**オブジェクト**（注：辞書ではなく、クラスインスタンスです）
      - `original_pdf_path`: 入力 PDF へのパス
      - `mono_pdf_path`: 単一言語翻訳 PDF へのパス（または None）
      - `dual_pdf_path`: 二言語翻訳 PDF へのパス（または None）
      - `no_watermark_mono_pdf_path`: 透かしなしの単一言語出力へのパス（生成された場合）、それ以外は None
      - `no_watermark_dual_pdf_path`: 透かしなしの二言語出力へのパス（生成された場合）、それ以外は None
      - `auto_extracted_glossary_path`: 自動抽出された用語集 CSV へのパス（または None）
      - `total_seconds`: 経過秒数（浮動小数点数）
      - `peak_memory_usage`: 翻訳中の概算ピークメモリ使用量（浮動小数点数；実装依存の単位）

- エラーイベント：`error`
  - フィールド
    - `type`: "error"
    - `error`: 人間が読めるエラーメッセージ
    - `error_type`: `BabeldocError`、`SubprocessError`、`IPCError`、`SubprocessCrashError` などのいずれか
    - `details`: オプションの詳細（例：元のエラーまたはトレースバック）

重要な動作：
- 進行が開始される前に、オプションの `stage_summary` が出力される場合があります。
- 特定の障害が発生した場合、ジェネレーターは最初に `error` イベントを yield し、その後 `TranslationError` から派生した例外を発生させます。エラーイベントをチェックするとともに、例外をキャッチする準備も行う必要があります。
- `progress_update` イベントは同じ値で繰り返される場合があります。必要に応じて、コンシューマー側でデバウンス処理を実施してください。
- `finish` イベントを受信したら、ストリームの消費を停止してください。

### 最小限の使用例（非同期）
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

### キャンセル
ストリームを消費するタスクをキャンセルできます。キャンセルは基盤となる翻訳プロセスに伝播されます。

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

### イベント形状の例
ステージサマリーイベント（例）：
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

Progress イベント（例）：
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

エラーイベント（例）：
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### 注意点とベストプラクティス
- ジェネレーターからのエラーイベントと例外の両方を常に処理してください。
- 不要な作業を避けるために、`finish` でループを抜けてください。
- 呼び出す前に、`file` が存在し、`settings.validate_settings()` が通過することを確認してください。
- 大きな文書は分割される可能性があります。UI を駆動するために `part_index/total_parts` と `overall_progress` を使用してください。
- UI が繰り返しの同一更新に敏感な場合は、`progress_update` をデバウンスしてください。
- `report_interval` (SettingsModel): `progress_update` イベントの送出頻度のみを制御します。`stage_summary`、`progress_start`、`progress_end`、または `finish` には影響しません。デフォルトは 0.1 秒で、最小許容値は 0.05 秒です。進捗モニターのロジックに従い、`stage_total <= 3` の場合、更新は `report_interval` によって調整されません。

<div align="right"> 
<h6><small>このページの一部のコンテンツは GPT によって翻訳されており、エラーが含まれている可能性があります。</small></h6>