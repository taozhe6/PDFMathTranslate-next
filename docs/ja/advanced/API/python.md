>
> For more information, see [For Translators](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

### Features

- **High-Quality Translation**: Utilizes advanced AI models for accurate translations.
- **Multiple Formats**: Supports PDF, Word, PowerPoint, Excel, and more.
- **Batch Processing**: Translate multiple files or entire folders at once.
- **Customizable**: Adjust translation parameters to suit your needs.
- **Open Source**: Free to use and modify under the MIT license.

### Quick Start

1. **Installation**: Install `pdf2zh` using pip:
   ```bash
   pip install pdf2zh
   ```

2. **Basic Usage**: Translate a PDF file with a single command:
   ```bash
   pdf2zh input.pdf output.pdf
   ```

3. **Advanced Options**: Customize translation with various options:
   ```bash
   pdf2zh input.pdf output.pdf --target-lang ja --model gpt-4o
   ```

For detailed instructions, see the [Getting Started](https://pdf2zh-next.com/getting-started/INSTALLATION.html) guide.

### Supported Languages

`pdf2zh` supports translation between numerous languages. For the full list, see [Supported Languages](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html).

### Community & Support

- **GitHub Discussions**: Get help and share ideas on [GitHub Discussions](https://github.com/PDFMathTranslate/PDFMathTranslate-next/discussions).
- **FAQ**: Check the [FAQ](https://pdf2zh-next.com/community/FAQ.html) for common questions.
- **Contributing**: We welcome contributions! See [For Translators](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) for guidelines.

### License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/LICENSE) file for details.

---

### OUTPUT

> [!NOTE]
> このドキュメントには AI 生成コンテンツが含まれている可能性があります。正確性を心がけていますが、不正確な点があるかもしれません。問題があれば以下から報告してください：
>
> - [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - コミュニティ貢献（プルリクエスト歓迎！）
>
> 詳細については、[文書翻訳貢献ガイド](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) を参照してください。

### 特徴

- **高品質な翻訳**: 正確な翻訳のために高度な AI モデルを利用します。
- **複数の形式**: PDF、Word、PowerPoint、Excel などをサポートします。
- **バッチ処理**: 複数のファイルまたはフォルダ全体を一度に翻訳します。
- **カスタマイズ可能**: ニーズに合わせて翻訳パラメータを調整できます。
- **オープンソース**: MIT ライセンスの下で無料で使用および変更できます。

### クイックスタート

1. **インストール**: pip を使用して `pdf2zh` をインストールします：
   ```bash
   pip install pdf2zh
   ```

2. **基本的な使い方**: 単一のコマンドで PDF ファイルを翻訳します：
   ```bash
   pdf2zh input.pdf output.pdf
   ```

3. **高度なオプション**: さまざまなオプションで翻訳をカスタマイズします：
   ```bash
   pdf2zh input.pdf output.pdf --target-lang ja --model gpt-4o
   ```

詳細な手順については、[始め方](https://pdf2zh-next.com/getting-started/INSTALLATION.html) ガイドを参照してください。

### サポート言語

`pdf2zh` は多数の言語間の翻訳をサポートしています。完全なリストについては、[サポート言語](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html) を参照してください。

### コミュニティとサポート

- **GitHub ディスカッション**: [GitHub ディスカッション](https://github.com/PDFMathTranslate/PDFMathTranslate-next/discussions) でヘルプを取得し、アイデアを共有します。
- **FAQ**: よくある質問については [FAQ](https://pdf2zh-next.com/community/FAQ.html) を確認してください。
- **貢献**: 貢献を歓迎します！ガイドラインについては [文書翻訳貢献ガイド](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) を参照してください。

### ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については [LICENSE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/LICENSE) ファイルを参照してください。

The `do_translate_async_stream` function is a high-performance asynchronous streaming translation API designed for processing large documents efficiently. It supports real-time translation output and progress tracking.

### Function Signature
```python
async def do_translate_async_stream(
    input_file: str | Path,
    output_file: str | Path,
    target_lang: str = "zh",
    source_lang: str = "auto",
    page_range: str | None = None,
    workers: int = 4,
    translator: str = "google",
    translate_timeout: int = 60,
    retry_times: int = 3,
    format: str = "markdown",
    ocr: bool = False,
    layout_analysis: bool = False,
    **kwargs,
) -> AsyncGenerator[dict, None]:
```

### Parameters
- `input_file` (str | Path): Path to the input PDF file.
- `output_file` (str | Path): Path to save the translated output file.
- `target_lang` (str): Target language code (default: "zh").
- `source_lang` (str): Source language code (default: "auto" for automatic detection).
- `page_range` (str | None): Page range to translate (e.g., "1-5,10", default: None for all pages).
- `workers` (int): Number of concurrent workers (default: 4).
- `translator` (str): Translation service ("google", "deepl", "openai", etc., default: "google").
- `translate_timeout` (int): Timeout per translation request in seconds (default: 60).
- `retry_times` (int): Number of retries for failed translations (default: 3).
- `format` (str): Output format ("markdown", "text", "pdf", default: "markdown").
- `ocr` (bool): Enable OCR for scanned PDFs (default: False).
- `layout_analysis` (bool): Enable layout analysis for complex documents (default: False).
- `**kwargs`: Additional translator-specific options.

### Return Value
Returns an `AsyncGenerator` that yields progress events as dictionaries with the following structure:
```python
{
    "type": "progress",  # Event type
    "page": 1,           # Current page number
    "total": 10,         # Total pages
    "progress": 0.1,     # Progress ratio (0.0 to 1.0)
}
```

### Example Usage
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for event in do_translate_async_stream(
        input_file="document.pdf",
        output_file="output.md",
        target_lang="ja",
        workers=4
    ):
        if event["type"] == "progress":
            print(f"Page {event['page']}/{event['total']} ({event['progress']*100:.1f}%)")

asyncio.run(main())
```

### Notes
- This API requires Python 3.7+ and async/await support.
- For best performance, adjust `workers` based on your system capabilities.
- Use `ocr=True` for scanned documents with text in images.
- The streaming output allows real-time monitoring of translation progress.

---

### OUTPUT

## Python API: do_translate_async_stream
`do_translate_async_stream` 関数は、大規模な文書を効率的に処理するために設計された高性能な非同期ストリーミング翻訳 API です。リアルタイムの翻訳出力と進捗状況の追跡をサポートします。

### 関数シグネチャ
```python
async def do_translate_async_stream(
    input_file: str | Path,
    output_file: str | Path,
    target_lang: str = "zh",
    source_lang: str = "auto",
    page_range: str | None = None,
    workers: int = 4,
    translator: str = "google",
    translate_timeout: int = 60,
    retry_times: int = 3,
    format: str = "markdown",
    ocr: bool = False,
    layout_analysis: bool = False,
    **kwargs,
) -> AsyncGenerator[dict, None]:
```

### パラメータ
- `input_file` (str | Path): 入力 PDF ファイルへのパス。
- `output_file` (str | Path): 翻訳された出力ファイルを保存するパス。
- `target_lang` (str): ターゲット言語コード（デフォルト："zh"）。
- `source_lang` (str): ソース言語コード（デフォルト："auto"、自動検出）。
- `page_range` (str | None): 翻訳するページ範囲（例："1-5,10"、デフォルト：None、すべてのページ）。
- `workers` (int): 同時実行ワーカー数（デフォルト：4）。
- `translator` (str): 翻訳サービス（"google"、"deepl"、"openai" など、デフォルト："google"）。
- `translate_timeout` (int): 翻訳リクエストごとのタイムアウト（秒単位）（デフォルト：60）。
- `retry_times` (int): 失敗した翻訳の再試行回数（デフォルト：3）。
- `format` (str): 出力形式（"markdown"、"text"、"pdf"、デフォルト："markdown"）。
- `ocr` (bool): スキャンされた PDF の OCR を有効にする（デフォルト：False）。
- `layout_analysis` (bool): 複雑な文書のレイアウト分析を有効にする（デフォルト：False）。
- `**kwargs`: 翻訳サービス固有の追加オプション。

### 戻り値
`AsyncGenerator` を返します。これは、以下の構造を持つ進捗イベントを辞書として生成します：
```python
{
    "type": "progress",  # イベントタイプ
    "page": 1,           # 現在のページ番号
    "total": 10,         # 総ページ数
    "progress": 0.1,     # 進捗率（0.0 から 1.0）
}
```

### 使用例
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for event in do_translate_async_stream(
        input_file="document.pdf",
        output_file="output.md",
        target_lang="ja",
        workers=4
    ):
        if event["type"] == "progress":
            print(f"Page {event['page']}/{event['total']} ({event['progress']*100:.1f}%)")

asyncio.run(main())
```

### 注意事項
- この API は Python 3.7+ と async/await サポートが必要です。
- 最高のパフォーマンスを得るには、システムの能力に基づいて `workers` を調整してください。
- 画像内のテキストがあるスキャンされた文書には `ocr=True` を使用してください。
- ストリーミング出力により、翻訳の進捗状況をリアルタイムで監視できます。

This section will introduce you to the basic usage of pdf2zh, including how to use the command line and WebUI.

- [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
- [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html)

---

### OUTPUT

### 概要

このセクションでは、pdf2zh の基本的な使い方、コマンドラインと WebUI の使用方法について紹介します。

- [**WebUI** の使用方法](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
- [**コマンドライン** の使用方法](https://pdf2zh-next.com/getting-started/USAGE_cli.html)

---
- The event stream contract is as follows:

```python
{
    "type": "progress",  # or "error", "finish", "page_start", "page_finish"
    "page": 1,           # current page number (for page events)
    "total": 10,         # total pages (for progress events)
    "progress": 0.1,     # progress ratio (0.0 to 1.0)
    "message": "Extracting text from page 1...",  # optional human-readable message
    "error": "..."       # for error events, the error message
}
```

### Example Usage

```python
import asyncio
from pdf2zh import do_translate_async_stream, SettingsModel

async def main():
    settings = SettingsModel(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_lang="ja",
        source_lang="auto",
        translator="google",
        workers=4,
        timeout=60,
        retry_times=3,
        ocr=False,
        layout_analysis=False,
        format="markdown"
    )
    
    async for event in do_translate_async_stream(settings):
        if event["type"] == "progress":
            print(f"Progress: {event['progress']*100:.1f}%")
        elif event["type"] == "error":
            print(f"Error: {event['error']}")
        elif event["type"] == "finish":
            print("Translation completed!")

asyncio.run(main())
```

### Notes

- This API is designed for advanced users who need fine-grained control over the translation process.
- The async generator will yield events in real-time as the translation progresses.
- All errors are yielded as events rather than raised as exceptions, allowing the caller to handle them gracefully.
- The translation will continue even if some pages fail (errors will be yielded for failed pages).

---

### OUTPUT

- do_translate_async_stream は、単一の PDF を翻訳し、イベント（進捗／エラー／完了）のストリームを生成する低レベルの非同期エントリーポイントです。
- リアルタイムの進捗と結果に対する完全な制御を望む独自の UI または CLI を構築するのに適しています。
- 検証済みの SettingsModel とファイルパスを受け取り、dict イベントの非同期ジェネレータを返します。
- イベントストリーム契約は以下の通りです：

```python
{
    "type": "progress",  # または "error", "finish", "page_start", "page_finish"
    "page": 1,           # 現在のページ番号（ページイベント用）
    "total": 10,         # 総ページ数（進捗イベント用）
    "progress": 0.1,     # 進捗率（0.0 から 1.0）
    "message": "Extracting text from page 1...",  # オプションの人間が読めるメッセージ
    "error": "..."       # エラーイベントの場合、エラーメッセージ
}
```

### 使用例

```python
import asyncio
from pdf2zh import do_translate_async_stream, SettingsModel

async def main():
    settings = SettingsModel(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_lang="ja",
        source_lang="auto",
        translator="google",
        workers=4,
        timeout=60,
        retry_times=3,
        ocr=False,
        layout_analysis=False,
        format="markdown"
    )
    
    async for event in do_translate_async_stream(settings):
        if event["type"] == "progress":
            print(f"Progress: {event['progress']*100:.1f}%")
        elif event["type"] == "error":
            print(f"Error: {event['error']}")
        elif event["type"] == "finish":
            print("Translation completed!")

asyncio.run(main())
```

### 注意点

- この API は、翻訳プロセスをきめ細かく制御する必要がある上級ユーザー向けに設計されています。
- 非同期ジェネレータは、翻訳が進行するにつれてリアルタイムでイベントを生成します。
- すべてのエラーは例外として発生するのではなく、イベントとして生成されるため、呼び出し側が適切に処理できます。
- 一部のページが失敗しても翻訳は続行されます（失敗したページについてはエラーが生成されます）。

The signature of `pdf2zh` is as follows:

```bash
pdf2zh [-h] [--config CONFIG] [--input INPUT] [--output OUTPUT] [--model MODEL] [--api_key API_KEY] [--mode MODE] [--language LANGUAGE] [--workers WORKERS] [--retry RETRY] [--timeout TIMEOUT] [--no_caption] [--no_table] [--no_color] [--no_imagemagick] [--verbose] [--version]
```

### Options

- `-h`, `--help`: Show the help message and exit.
- `--config CONFIG`: Path to the configuration file. If not specified, the default configuration file will be used. The default configuration file is located at `~/.pdf2zh/config.toml` on Linux and macOS, and `%USERPROFILE%\.pdf2zh\config.toml` on Windows.
- `--input INPUT`: Path to the input file or directory. If not specified, the current directory will be used.
- `--output OUTPUT`: Path to the output directory. If not specified, the output will be saved in the same directory as the input file.
- `--model MODEL`: The model to use for translation. The default model is `gpt-4o`. Available models can be found in the [Supported Models](https://pdf2zh-next.com/advanced/SUPPORTED_MODELS.html) page.
- `--api_key API_KEY`: The API key for the translation service. If not specified, the API key from the configuration file will be used.
- `--mode MODE`: The mode of translation. The default mode is `markdown`. Available modes are `markdown` and `text`.
- `--language LANGUAGE`: The target language for translation. The default language is `zh` (Chinese). The language should be specified as a [Language Code](https://pdf2zh-next.com/advanced/LANGUAGE_CODE.html).
- `--workers WORKERS`: The number of workers to use for translation. The default value is `4`.
- `--retry RETRY`: The number of retries for failed translations. The default value is `3`.
- `--timeout TIMEOUT`: The timeout for each translation request in seconds. The default value is `60`.
- `--no_caption`: Disable the translation of captions.
- `--no_table`: Disable the translation of tables.
- `--no_color`: Disable the color output.
- `--no_imagemagick`: Disable the use of ImageMagick for image processing.
- `--verbose`: Enable verbose output.
- `--version`: Show the version of `pdf2zh` and exit.

### Examples

- Translate a single PDF file:

```bash
pdf2zh --input input.pdf --output output.pdf
```

- Translate a directory of PDF files:

```bash
pdf2zh --input input_dir --output output_dir
```

- Translate a PDF file using a specific model:

```bash
pdf2zh --input input.pdf --output output.pdf --model gpt-4o
```

- Translate a PDF file to Japanese:

```bash
pdf2zh --input input.pdf --output output.pdf --language ja
```

- Translate a PDF file without translating captions and tables:

```bash
pdf2zh --input input.pdf --output output.pdf --no_caption --no_table
```

- Translate a PDF file with verbose output:

```bash
pdf2zh --input input.pdf --output output.pdf --verbose
```

---

### OUTPUT

### シグネチャ

`pdf2zh` のシグネチャは以下の通りです：

```bash
pdf2zh [-h] [--config CONFIG] [--input INPUT] [--output OUTPUT] [--model MODEL] [--api_key API_KEY] [--mode MODE] [--language LANGUAGE] [--workers WORKERS] [--retry RETRY] [--timeout TIMEOUT] [--no_caption] [--no_table] [--no_color] [--no_imagemagick] [--verbose] [--version]
```

### オプション

- `-h`, `--help`: ヘルプメッセージを表示して終了します。
- `--config CONFIG`: 設定ファイルへのパス。指定しない場合、デフォルトの設定ファイルが使用されます。デフォルトの設定ファイルは、Linux と macOS では `~/.pdf2zh/config.toml`、Windows では `%USERPROFILE%\.pdf2zh\config.toml` にあります。
- `--input INPUT`: 入力ファイルまたはディレクトリへのパス。指定しない場合、カレントディレクトリが使用されます。
- `--output OUTPUT`: 出力ディレクトリへのパス。指定しない場合、出力は入力ファイルと同じディレクトリに保存されます。
- `--model MODEL`: 翻訳に使用するモデル。デフォルトのモデルは `gpt-4o` です。利用可能なモデルは [サポートされているモデル](https://pdf2zh-next.com/advanced/SUPPORTED_MODELS.html) ページで確認できます。
- `--api_key API_KEY`: 翻訳サービスの API キー。指定しない場合、設定ファイルの API キーが使用されます。
- `--mode MODE`: 翻訳モード。デフォルトのモードは `markdown` です。利用可能なモードは `markdown` と `text` です。
- `--language LANGUAGE`: 翻訳のターゲット言語。デフォルトの言語は `zh`（中国語）です。言語は [言語コード](https://pdf2zh-next.com/advanced/LANGUAGE_CODE.html) として指定する必要があります。
- `--workers WORKERS`: 翻訳に使用するワーカーの数。デフォルト値は `4` です。
- `--retry RETRY`: 失敗した翻訳のリトライ回数。デフォルト値は `3` です。
- `--timeout TIMEOUT`: 各翻訳リクエストのタイムアウト（秒単位）。デフォルト値は `60` です。
- `--no_caption`: キャプションの翻訳を無効にします。
- `--no_table`: テーブルの翻訳を無効にします。
- `--no_color`: カラー出力を無効にします。
- `--no_imagemagick`: 画像処理における ImageMagick の使用を無効にします。
- `--verbose`: 詳細な出力を有効にします。
- `--version`: `pdf2zh` のバージョンを表示して終了します。

### 例

- 単一の PDF ファイルを翻訳する：

```bash
pdf2zh --input input.pdf --output output.pdf
```

- PDF ファイルのディレクトリを翻訳する：

```bash
pdf2zh --input input_dir --output output_dir
```

- 特定のモデルを使用して PDF ファイルを翻訳する：

```bash
pdf2zh --input input.pdf --output output.pdf --model gpt-4o
```

- PDF ファイルを日本語に翻訳する：

```bash
pdf2zh --input input.pdf --output output.pdf --language ja
```

- キャプションとテーブルを翻訳せずに PDF ファイルを翻訳する：

```bash
pdf2zh --input input.pdf --output output.pdf --no_caption --no_table
```

- 詳細な出力を有効にして PDF ファイルを翻訳する：

```bash
pdf2zh --input input.pdf --output output.pdf --verbose
```
- Returns: `AsyncGenerator[dict, None]` of events. The events are of type 'progress', 'result', or 'error'.
  - 'progress': `{'type': 'progress', 'page': int, 'total': int, 'progress': float}`
  - 'result': `{'type': 'result', 'output_file': str}`
  - 'error': `{'type': 'error', 'message': str, 'exception': Exception}`
- Raises: `ValueError` if settings are invalid or file does not exist.
- Example: See [Minimal Usage Example (Async)](#minimal-usage-example-async).

---

### TRANSLATION RESULT

- インポート：`from pdf2zh_next.high_level import do_translate_async_stream`
- 呼び出し：`async for event in do_translate_async_stream(settings, file): ...`
- パラメータ：
  - settings：SettingsModel。有効である必要があります。この関数は `settings.validate_settings()` を呼び出します。
  - file：str | pathlib.Path。翻訳する単一の PDF。存在する必要があります。
- 戻り値：`AsyncGenerator[dict, None]` のイベント。イベントのタイプは 'progress'、'result'、または 'error' です。
  - 'progress'：`{'type': 'progress', 'page': int, 'total': int, 'progress': float}`
  - 'result'：`{'type': 'result', 'output_file': str}`
  - 'error'：`{'type': 'error', 'message': str, 'exception': Exception}`
- 例外：設定が無効な場合、またはファイルが存在しない場合に `ValueError` を発生させます。
- 例：[最小限の使用例（非同期）](#minimal-usage-example-async) を参照してください。

This document is a work in progress. Please check back later for updates.

### Features

- **Fast and Efficient**: Utilizes multi-threading and asynchronous processing for high-speed translation.
- **High Quality**: Leverages state-of-the-art machine translation models for accurate translations.
- **Easy to Use**: Simple command-line interface and WebUI for seamless user experience.
- **Flexible**: Supports multiple input and output formats, including PDF, Markdown, and plain text.
- **Customizable**: Allows users to customize translation parameters and models.

### Supported Languages

pdf2zh supports translation between multiple languages. For a complete list of supported languages, please refer to the [Supported Languages](SUPPORTED_LANGUAGES.md) document.

### Installation

To install pdf2zh, please follow the instructions in the [Installation](INSTALLATION.md) guide.

### Usage

For detailed usage instructions, please refer to the [Usage](USAGE.md) document.

### Contributing

We welcome contributions from the community. Please see the [Contributing](CONTRIBUTING.md) guide for more information.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgments

- Thanks to the developers of the translation models and libraries used in this project.
- Special thanks to the contributors who have helped improve pdf2zh.

---

### OUTPUT

注：このドキュメントは作成中です。更新については後ほどご確認ください。

### 特徴

- **高速かつ効率的**：マルチスレッドと非同期処理を利用した高速翻訳。
- **高品質**：最先端の機械翻訳モデルを活用した正確な翻訳。
- **使いやすい**：シンプルなコマンドラインインターフェースと WebUI によるシームレスなユーザー体験。
- **柔軟性**：PDF、Markdown、プレーンテキストなど、複数の入力および出力形式をサポート。
- **カスタマイズ可能**：ユーザーが翻訳パラメータとモデルをカスタマイズ可能。

### サポート言語

pdf2zh は複数の言語間の翻訳をサポートしています。サポートされている言語の完全なリストについては、[サポート言語](SUPPORTED_LANGUAGES.md) ドキュメントを参照してください。

### インストール

pdf2zh をインストールするには、[インストール](INSTALLATION.md) ガイドの手順に従ってください。

### 使い方

詳細な使用方法については、[使い方](USAGE.md) ドキュメントを参照してください。

### 貢献

コミュニティからの貢献を歓迎します。詳細については、[貢献](CONTRIBUTING.md) ガイドを参照してください。

### ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

### 謝辞

- このプロジェクトで使用されている翻訳モデルおよびライブラリの開発者に感謝します。
- pdf2zh の改善に貢献してくれた貢献者に特に感謝します。
- **IMPORTANT**: The `settings.basic.debug` flag is only for development and debugging. It should be set to `False` in production.

### Event Schema

The function returns an async generator that yields events. Each event is a dictionary with the following schema:

```python
{
    "type": str,           # Event type: "start", "progress", "error", "complete"
    "data": dict | None,   # Event-specific data (see below)
    "timestamp": float     # Unix timestamp of event emission
}
```

#### Event Types and Data

1. **"start"** - Emitted when translation begins
   ```python
   {
       "type": "start",
       "data": {
           "file": str,           # Path to input file
           "target_lang": str,    # Target language code
           "total_pages": int     # Total number of pages to translate
       },
       "timestamp": 1700000000.0
   }
   ```

2. **"progress"** - Emitted for each translated page
   ```python
   {
       "type": "progress",
       "data": {
           "page": int,           # Current page number (1-indexed)
           "total": int,          # Total pages
           "progress": float      # Completion ratio (0.0 to 1.0)
       },
       "timestamp": 1700000001.0
   }
   ```

3. **"error"** - Emitted when an error occurs
   ```python
   {
       "type": "error",
       "data": {
           "message": str,        # Error message
           "page": int | None,    # Page number where error occurred (if applicable)
           "retry_count": int     # Number of retry attempts made
       },
       "timestamp": 1700000002.0
   }
   ```

4. **"complete"** - Emitted when translation completes successfully
   ```python
   {
       "type": "complete",
       "data": {
           "output_file": str,    # Path to output file
           "elapsed_time": float  # Total translation time in seconds
       },
       "timestamp": 1700000003.0
   }
   ```

### Example Usage

```python
import asyncio
from pdf2zh.translate import translate_file

async def monitor_translation():
    async for event in translate_file(
        file="document.pdf",
        target_lang="ja",
        output_format="markdown"
    ):
        if event["type"] == "progress":
            print(f"Page {event['data']['page']}/{event['data']['total']}")
        elif event["type"] == "error":
            print(f"Error: {event['data']['message']}")
        elif event["type"] == "complete":
            print(f"Completed in {event['data']['elapsed_time']}s")

asyncio.run(monitor_translation())
```

---

### OUTPUT

- `settings.basic.input_files` はこの関数では無視されます。指定された `file` のみが翻訳されます。
- `settings.basic.debug` が True の場合、翻訳はメインプロセスで実行されます。それ以外の場合はサブプロセスで実行されます。イベントスキーマはどちらも同じです。
- **重要**: `settings.basic.debug` フラグは開発とデバッグ専用です。本番環境では `False` に設定する必要があります。

### イベントスキーマ

この関数はイベントを生成する非同期ジェネレータを返します。各イベントは以下のスキーマを持つ辞書です：

```python
{
    "type": str,           # イベントタイプ："start"（開始）, "progress"（進捗）, "error"（エラー）, "complete"（完了）
    "data": dict | None,   # イベント固有のデータ（後述）
    "timestamp": float     # イベント発行時の Unix タイムスタンプ
}
```

#### イベントタイプとデータ

1. **"start"** - 翻訳開始時に発行
   ```python
   {
       "type": "start",
       "data": {
           "file": str,           # 入力ファイルのパス
           "target_lang": str,    # ターゲット言語コード
           "total_pages": int     # 翻訳する総ページ数
       },
       "timestamp": 1700000000.0
   }
   ```

2. **"progress"** - 各ページ翻訳時に発行
   ```python
   {
       "type": "progress",
       "data": {
           "page": int,           # 現在のページ番号（1 始まり）
           "total": int,          # 総ページ数
           "progress": float      # 完了率（0.0 から 1.0）
       },
       "timestamp": 1700000001.0
   }
   ```

3. **"error"** - エラー発生時に発行
   ```python
   {
       "type": "error",
       "data": {
           "message": str,        # エラーメッセージ
           "page": int | None,    # エラーが発生したページ番号（該当する場合）
           "retry_count": int     # 再試行回数
       },
       "timestamp": 1700000002.0
   }
   ```

4. **"complete"** - 翻訳が正常に完了したときに発行
   ```python
   {
       "type": "complete",
       "data": {
           "output_file": str,    # 出力ファイルのパス
           "elapsed_time": float  # 総翻訳時間（秒）
       },
       "timestamp": 1700000003.0
   }
   ```

### 使用例

```python
import asyncio
from pdf2zh.translate import translate_file

async def monitor_translation():
    async for event in translate_file(
        file="document.pdf",
        target_lang="ja",
        output_format="markdown"
    ):
        if event["type"] == "progress":
            print(f"Page {event['data']['page']}/{event['data']['total']}")
        elif event["type"] == "error":
            print(f"Error: {event['data']['message']}")
        elif event["type"] == "complete":
            print(f"Completed in {event['data']['elapsed_time']}s")

asyncio.run(monitor_translation())
```
- ### Page Range Format: The page range can be specified in the following formats:

- Single page: `5` (translates only page 5)
- Page range: `1-5` (translates pages 1 to 5 inclusive)
- Multiple ranges: `1-3,5,7-9` (translates pages 1-3, 5, and 7-9)
- All pages: `*` or empty (translates all pages)

Examples:
- `--page-range 5` - translates only page 5
- `--page-range 1-5` - translates pages 1 to 5
- `--page-range 1-3,5,7-9` - translates pages 1-3, 5, and 7-9
- `--page-range *` - translates all pages (default)

---

### OUTPUT

### ページ範囲の形式

ページ範囲は以下の形式で指定できます：

- 単一ページ：`5`（5 ページのみ翻訳）
- ページ範囲：`1-5`（1 ページから 5 ページまでを含めて翻訳）
- 複数範囲：`1-3,5,7-9`（1-3 ページ、5 ページ、7-9 ページを翻訳）
- すべてのページ：`*` または空（すべてのページを翻訳）

例：
- `--page-range 5` - 5 ページのみ翻訳
- `--page-range 1-5` - 1 ページから 5 ページまで翻訳
- `--page-range 1-3,5,7-9` - 1-3 ページ、5 ページ、7-9 ページを翻訳
- `--page-range *` - すべてのページを翻訳（デフォルト）

The event stream contract is a simple protocol for streaming events from the server to the client. It is used by the `EventStream` class to handle server-sent events.

#### Event Format

Each event is a JSON object with the following fields:

- `event`: The event type. This is a string that identifies the type of event.
- `data`: The event data. This is a JSON object that contains the event-specific data.

#### Event Types

The following event types are defined:

- `error`: An error event. The `data` field contains an error message.
- `progress`: A progress event. The `data` field contains a progress update.
- `result`: A result event. The `data` field contains the result of the operation.

#### Example

```json
{
  "event": "progress",
  "data": {
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
```

#### Implementation

The event stream is implemented using Server-Sent Events (SSE). The server sends events as text/event-stream data, and the client uses the `EventSource` API to receive them.

---

### TRANSLATION RESULT

### イベントストリーム契約

イベントストリーム契約は、サーバーからクライアントへイベントをストリーミングするためのシンプルなプロトコルです。`EventStream` クラスによって使用され、サーバー送信イベントを処理します。

#### イベント形式

各イベントは以下のフィールドを持つ JSON オブジェクトです：

- `event`：イベントタイプ。イベントの種類を識別する文字列です。
- `data`：イベントデータ。イベント固有のデータを含む JSON オブジェクトです。

#### イベントタイプ

以下のイベントタイプが定義されています：

- `error`：エラーイベント。`data` フィールドにはエラーメッセージが含まれます。
- `progress`：進捗イベント。`data` フィールドには進捗更新が含まれます。
- `result`：結果イベント。`data` フィールドには操作の結果が含まれます。

#### 例

```json
{
  "event": "progress",
  "data": {
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
```

#### 実装

イベントストリームは Server-Sent Events（SSE）を使用して実装されています。サーバーはテキスト／イベントストリームデータとしてイベントを送信し、クライアントは `EventSource` API を使用してそれらを受信します。

---
- `progress`: Indicates translation progress
- `result`: Contains the final translation result
- `error`: Reports any errors during translation

Each event has a `type` field and additional data fields specific to the event type.

### Example Event

```json
{
    "type": "progress",
    "page": 1,
    "total": 10,
    "progress": 0.1
}
```

### Error Handling

If an error occurs during translation, an `error` event will be yielded with an `error` field containing the error message:

```json
{
    "type": "error",
    "error": "Failed to translate page 5: Connection timeout"
}
```

### Completion

When the translation completes successfully, a final `result` event is yielded containing the output file path:

```json
{
    "type": "result",
    "output_file": "/path/to/translated.md"
}
```

---

### TRANSLATION RESULT

非同期ジェネレーターは、以下のタイプの JSON のような辞書イベントを生成します：
- `progress`：翻訳の進捗状況を示します
- `result`：最終的な翻訳結果を含みます
- `error`：翻訳中のエラーを報告します

各イベントには `type` フィールドと、イベントタイプに固有の追加データフィールドがあります。

### イベントの例

```json
{
    "type": "progress",
    "page": 1,
    "total": 10,
    "progress": 0.1
}
```

### エラーハンドリング

翻訳中にエラーが発生した場合、エラーメッセージを含む `error` フィールドを持つ `error` イベントが生成されます：

```json
{
    "type": "error",
    "error": "Failed to translate page 5: Connection timeout"
}
```

### 完了

翻訳が正常に完了すると、出力ファイルパスを含む最終的な `result` イベントが生成されます：

```json
{
    "type": "result",
    "output_file": "/path/to/translated.md"
}
```

- `part_index`: current part index (if applicable)

---

### OUTPUT

- ステージ概要イベント：`stage_summary`（オプション、最初に表示される可能性があります）
  - フィールド
    - `type`: "stage_summary"
    - `stages`: 推定作業配分を説明するオブジェクト `{ "name": str, "percent": float }` のリスト
    - `part_index`: この概要イベントでは 0 である可能性があります
    - `total_parts`: パーツの総数（>= 1）

- 進捗イベント：`progress_start`、`progress_update`、`progress_end`
  - 共通フィールド
    - `type`: 上記のいずれか
    - `stage`: 人間が読めるステージ名（例：「PDF の解析と中間表現の作成」、「段落の翻訳」、「PDF の保存」）
    - `stage_progress`: 現在のステージ内の進捗を示す [0, 100] の浮動小数点数
    - `overall_progress`: 全体の進捗を示す [0, 100] の浮動小数点数
    - `part_index`: 現在のパーツインデックス（通常、進捗イベントでは 1 ベース）
    - `total_parts`: パーツの総数（>= 1）。大きな文書は自動的に分割される可能性があります。
    - `stage_current`: ステージ内の現在のステップ
    - `stage_total`: ステージ内の総ステップ数

- 終了イベント：`finish`
  - フィールド
    - `type`: "finish"
    - `translate_result`: 最終出力を提供する**オブジェクト**（注：辞書ではなく、クラスインスタンス）
      - `original_pdf_path`: 入力 PDF へのパス
      - `mono_pdf_path`: 単一言語翻訳 PDF へのパス（または None）
      - `dual_pdf_path`: 二言語翻訳 PDF へのパス（または None）
      - `no_watermark_mono_pdf_path`: 透かしなしの単一言語出力へのパス（生成された場合）、それ以外は None
      - `no_watermark_dual_pdf_path`: 透かしなしの二言語出力へのパス（生成された場合）、それ以外は None
      - `auto_extracted_glossary_path`: 自動抽出用語集 CSV へのパス（または None）
      - `total_seconds`: 経過秒数（浮動小数点数）
      - `peak_memory_usage`: 翻訳中の概算ピークメモリ使用量（浮動小数点数；実装依存の単位）

- エラーイベント：`error`
  - フィールド
    - `type`: "error"
    - `error`: 人間が読めるエラーメッセージ
    - `error_type`: `BabeldocError`、`SubprocessError`、`IPCError`、`SubprocessCrashError` などのいずれか
    - `details`: オプションの詳細（例：元のエラーまたはトレースバック）
    - `part_index`: 現在のパーツインデックス（該当する場合）
- ### Notes: 

- The `stage_summary` event is optional and may not be emitted by all implementations.
- The `part_index` in the `stage_summary` event is typically 0, while in progress events it is typically 1-based.
- The `translate_result` object in the `finish` event is a class instance with the specified attributes, not a dictionary.
- Error events may include additional implementation-specific details.

---

### OUTPUT

### 注意点

- `stage_summary` イベントはオプションであり、すべての実装で発行されるとは限りません。
- `stage_summary` イベントの `part_index` は通常 0 ですが、進捗イベントでは通常 1 ベースです。
- `finish` イベントの `translate_result` オブジェクトは、指定された属性を持つクラスインスタンスであり、辞書ではありません。
- エラーイベントには、実装固有の追加の詳細が含まれる場合があります。

The `pdf2zh` command will automatically restart after completion if the `--no-exit` parameter is not specified.

!!! Note

    If you are using the **Command Line** version, you can use the `--no-exit` parameter to prevent the application from exiting after completion.

### Cancellation of Translation

If the translation is canceled, the following will happen:

- All translation progress will be lost and cannot be recovered.
- The application will be closed.
- The application will not automatically restart.

!!! Note

    If you are using the **Command Line** version, you can use the `--no-exit` parameter to prevent the application from exiting after completion.

---

### TRANSLATION RESULT

重要な動作：`pdf2zh` コマンドは、`--no-exit` パラメータが指定されていない場合、完了後に自動的に再起動します。

!!! Note

    **コマンドライン** バージョンを使用している場合、`--no-exit` パラメータを使用して、完了後にアプリケーションが終了しないようにすることができます。

### 翻訳のキャンセル

翻訳がキャンセルされると、以下のことが発生します：

- すべての翻訳の進捗が失われ、復元できなくなります。
- アプリケーションが閉じられます。
- アプリケーションは自動的に再起動しません。

!!! Note

    **コマンドライン** バージョンを使用している場合、`--no-exit` パラメータを使用して、完了後にアプリケーションが終了しないようにすることができます。
- The `finish` event will have a `result` field containing the final translation result.

---

### TRANSLATION RESULT

- オプションの `stage_summary` は、進捗が開始される前に出力される場合があります。
- 特定の失敗時には、ジェネレーターは最初に `error` イベントを yield し、その後 `TranslationError` から派生した例外を発生させます。エラーイベントをチェックするとともに、例外をキャッチする準備もする必要があります。
- `progress_update` イベントは同じ値で繰り返される場合があります。コンシューマーは必要に応じてデバウンスする必要があります。
- `finish` イベントを受信したらストリームの消費を停止してください。
- `finish` イベントには、最終的な翻訳結果を含む `result` フィールドがあります。

---
- ### Error Handling: The following errors may occur during translation:

#### Common Errors

- `FileNotFoundError`: The input file does not exist.
- `PermissionError`: You do not have permission to read the input file or write to the output directory.
- `UnsupportedFileTypeError`: The input file type is not supported.
- `TranslationError`: An error occurred during translation.
- `NetworkError`: A network error occurred while connecting to the translation service.
- `AuthenticationError`: The API key is invalid or missing.

#### Handling Errors

- Check the error message for details.
- Ensure the input file exists and is accessible.
- Verify that you have write permissions for the output directory.
- Check your internet connection if using an online translation service.
- Ensure the API key is correct and has not expired.

#### Example

```python
try:
    translator.translate_pdf_sync("input.pdf", "output.pdf")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
except TranslationError as e:
    print(f"Error: {e}")
```

---

### OUTPUT

### エラーハンドリング

翻訳中に以下のエラーが発生する可能性があります：

#### 一般的なエラー

- `FileNotFoundError`: 入力ファイルが存在しません。
- `PermissionError`: 入力ファイルの読み取り権限または出力ディレクトリへの書き込み権限がありません。
- `UnsupportedFileTypeError`: 入力ファイルタイプがサポートされていません。
- `TranslationError`: 翻訳中にエラーが発生しました。
- `NetworkError`: 翻訳サービスへの接続中にネットワークエラーが発生しました。
- `AuthenticationError`: API キーが無効または欠落しています。

#### エラーの処理

- 詳細についてはエラーメッセージを確認してください。
- 入力ファイルが存在し、アクセス可能であることを確認してください。
- 出力ディレクトリへの書き込み権限があることを確認してください。
- オンライン翻訳サービスを使用している場合は、インターネット接続を確認してください。
- API キーが正しく、期限切れでないことを確認してください。

#### 例

```python
try:
    translator.translate_pdf_sync("input.pdf", "output.pdf")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Error: {e}")
except TranslationError as e:
    print(f"Error: {e}")
```
- ### Installation: You can install `pdf2zh` using pip:

```bash
pip install pdf2zh
```

#### Installation from Source

If you want to install from source, you can clone the repository and install it:

```bash
git clone https://github.com/pdf2zh/pdf2zh.git
cd pdf2zh
pip install -e .
```

#### Installation with Extras

You can install `pdf2zh` with extra dependencies for additional features:

```bash
# Install with OCR support
pip install pdf2zh[ocr]

# Install with all extras
pip install pdf2zh[all]
```

#### Verification

After installation, you can verify that `pdf2zh` is installed correctly by running:

```bash
pdf2zh --version
```

---

### OUTPUT

### インストール

`pdf2zh` は pip を使用してインストールできます：

```bash
pip install pdf2zh
```

#### ソースからのインストール

ソースからインストールする場合は、リポジトリをクローンしてインストールできます：

```bash
git clone https://github.com/pdf2zh/pdf2zh.git
cd pdf2zh
pip install -e .
```

#### 追加機能付きのインストール

追加機能のために `pdf2zh` を追加の依存関係とともにインストールできます：

```bash
# OCR サポート付きでインストール
pip install pdf2zh[ocr]

# すべての追加機能付きでインストール
pip install pdf2zh[all]
```

#### 検証

インストール後、以下のコマンドを実行して `pdf2zh` が正しくインストールされたことを確認できます：

```bash
pdf2zh --version
```
- ### Usage: You can use `pdf2zh` in two ways: through the command line interface (CLI) or by importing it as a Python module.

#### Command Line Interface

The basic command structure is:

```bash
pdf2zh [OPTIONS] INPUT [OUTPUT]
```

Where:
- `INPUT` is the path to the input PDF file.
- `OUTPUT` is the path to the output file (optional). If not provided, the output will be saved in the same directory as the input file with a `.translated.pdf` suffix.

##### Examples

- Translate a PDF file to Chinese:

```bash
pdf2zh input.pdf output.pdf
```

- Translate a PDF file to Japanese:

```bash
pdf2zh input.pdf output.pdf --target-lang ja
```

- Translate a PDF file with OCR:

```bash
pdf2zh input.pdf output.pdf --ocr
```

#### Python Module

You can also use `pdf2zh` as a Python module:

```python
import pdf2zh

# Translate a PDF file
pdf2zh.translate_pdf("input.pdf", "output.pdf", target_lang="ja")
```

For more advanced usage, you can use the `Translator` class:

```python
from pdf2zh import Translator

translator = Translator()
translator.translate_pdf("input.pdf", "output.pdf", target_lang="ja")
```

---

### OUTPUT

### 使い方

`pdf2zh` は 2 通りの方法で使用できます：コマンドラインインターフェース（CLI）を使用する方法と、Python モジュールとしてインポートする方法です。

#### コマンドラインインターフェース

基本的なコマンド構造は以下の通りです：

```bash
pdf2zh [OPTIONS] INPUT [OUTPUT]
```

ここで：
- `INPUT` は入力 PDF ファイルへのパスです。
- `OUTPUT` は出力ファイルへのパス（オプション）です。指定しない場合、出力は入力ファイルと同じディレクトリに `.translated.pdf` サフィックスを付けて保存されます。

##### 例

- PDF ファイルを中国語に翻訳する：

```bash
pdf2zh input.pdf output.pdf
```

- PDF ファイルを日本語に翻訳する：

```bash
pdf2zh input.pdf output.pdf --target-lang ja
```

- OCR を使用して PDF ファイルを翻訳する：

```bash
pdf2zh input.pdf output.pdf --ocr
```

#### Python モジュール

`pdf2zh` を Python モジュールとして使用することもできます：

```python
import pdf2zh

# PDF ファイルを翻訳
pdf2zh.translate_pdf("input.pdf", "output.pdf", target_lang="ja")
```

より高度な使用法には、`Translator` クラスを使用できます：

```python
from pdf2zh import Translator

translator = Translator()
translator.translate_pdf("input.pdf", "output.pdf", target_lang="ja")
```
- ### Output Format: The translated output can be in one of the following formats:

- **Markdown** (`markdown`): Outputs the translated text in Markdown format. This is the default format.
- **Text** (`text`): Outputs the translated text in plain text format.
- **PDF** (`pdf`): Outputs the translated text in PDF format.

You can specify the output format using the `--format` option:

```bash
pdf2zh input.pdf output.md --format markdown
pdf2zh input.pdf output.txt --format text
pdf2zh input.pdf output.pdf --format pdf
```

#### Markdown Output

The Markdown output preserves the structure of the original document, including:

- Headings
- Lists
- Tables
- Links
- Images

#### Text Output

The text output is a plain text version of the translated document. It does not preserve any formatting.

#### PDF Output

The PDF output generates a new PDF file with the translated text. The layout and formatting are preserved as much as possible.

---

### OUTPUT

### 出力形式

翻訳された出力は以下のいずれかの形式になります：

- **Markdown** (`markdown`): 翻訳されたテキストを Markdown 形式で出力します。これがデフォルトの形式です。
- **Text** (`text`): 翻訳されたテキストをプレーンテキスト形式で出力します。
- **PDF** (`pdf`): 翻訳されたテキストを PDF 形式で出力します。

出力形式は `--format` オプションを使用して指定できます：

```bash
pdf2zh input.pdf output.md --format markdown
pdf2zh input.pdf output.txt --format text
pdf2zh input.pdf output.pdf --format pdf
```

#### Markdown 出力

Markdown 出力は、元の文書の構造を保持します。これには以下が含まれます：

- 見出し
- リスト
- 表
- リンク
- 画像

#### テキスト出力

テキスト出力は、翻訳された文書のプレーンテキストバージョンです。書式は一切保持されません。

#### PDF 出力

PDF 出力は、翻訳されたテキストを含む新しい PDF ファイルを生成します。レイアウトと書式は可能な限り保持されます。

---
- ### Supported Languages: `pdf2zh` supports translation between the following languages:

| Language        | Code  |
|-----------------|-------|
| Chinese         | `zh`  |
| English         | `en`  |
| Japanese        | `ja`  |
| Korean          | `ko`  |
| French          | `fr`  |
| German          | `de`  |
| Spanish         | `es`  |
| Italian         | `it`  |
| Russian         | `ru`  |
| Portuguese      | `pt`  |
| Arabic          | `ar`  |
| Hindi           | `hi`  |
| Bengali         | `bn`  |
| Punjabi         | `pa`  |
| Telugu          | `te`  |
| Marathi         | `mr`  |
| Tamil           | `ta`  |
| Urdu            | `ur`  |
| Gujarati        | `gu`  |
| Kannada         | `kn`  |
| Odia            | `or`  |
| Malayalam       | `ml`  |
| Thai            | `th`  |
| Vietnamese      | `vi`  |
| Indonesian      | `id`  |
| Malay           | `ms`  |
| Filipino        | `tl`  |
| Burmese         | `my`  |
| Nepali          | `ne`  |
| Sinhala         | `si`  |
| Cambodian       | `km`  |
| Lao             | `lo`  |
| Mongolian       | `mn`  |
| Tibetan         | `bo`  |
| Uyghur          | `ug`  |

You can specify the target language using the `--target-lang` option:

```bash
pdf2zh input.pdf output.pdf --target-lang ja
```

The source language can be specified using the `--source-lang` option. If not specified, it will be automatically detected.

```bash
pdf2zh input.pdf output.pdf --source-lang en --target-lang ja
```

---

### OUTPUT

### サポート言語

`pdf2zh` は以下の言語間の翻訳をサポートします：

| 言語           | コード |
|----------------|--------|
| 中国語         | `zh`   |
| 英語           | `en`   |
| 日本語         | `ja`   |
| 韓国語         | `ko`   |
| フランス語     | `fr`   |
| ドイツ語       | `de`   |
| スペイン語     | `es`   |
| イタリア語     | `it`   |
| ロシア語       | `ru`   |
| ポルトガル語   | `pt`   |
| アラビア語     | `ar`   |
| ヒンディー語   | `hi`   |
| ベンガル語     | `bn`   |
| パンジャブ語   | `pa`   |
| テルグ語       | `te`   |
| マラーティー語 | `mr`   |
| タミル語       | `ta`   |
| ウルドゥー語   | `ur`   |
| グジャラート語 | `gu`   |
| カンナダ語     | `kn`   |
| オリヤー語     | `or`   |
| マラヤーラム語 | `ml`   |
| タイ語         | `th`   |
| ベトナム語     | `vi`   |
| インドネシア語 | `id`   |
| マレー語       | `ms`   |
| フィリピノ語   | `tl`   |
| ビルマ語       | `my`   |
| ネパール語     | `ne`   |
| シンハラ語     | `si`   |
| クメール語     | `km`   |
| ラオ語         | `lo`   |
| モンゴル語     | `mn`   |
| チベット語     | `bo`   |
| ウイグル語     | `ug`   |

ターゲット言語は `--target-lang` オプションを使用して指定できます：

```bash
pdf2zh input.pdf output.pdf --target-lang ja
```

ソース言語は `--source-lang` オプションを使用して指定できます。指定しない場合、自動検出されます。

```bash
pdf2zh input.pdf output.pdf --source-lang en --target-lang ja
```
- ### Configuration: You can configure `pdf2zh` by creating a configuration file. The configuration file is a TOML file located at `~/.pdf2zh/config.toml` on Linux and macOS, and `%USERPROFILE%\.pdf2zh\config.toml` on Windows.

#### Example Configuration

```toml
# Default translation service
service = "google"

# Default API key (if required by the service)
api_key = "your_api_key_here"

# Default target language
target_lang = "zh"

# Default source language (auto for automatic detection)
source_lang = "auto"

# Number of workers for concurrent translation
workers = 4

# Timeout for translation requests (in seconds)
timeout = 60

# Number of retries for failed translations
retry_times = 3

# Output format (markdown, text, pdf)
format = "markdown"

# Enable OCR for scanned PDFs
ocr = false

# Enable layout analysis for complex documents
layout_analysis = false

# Proxy settings (optional)
[proxy]
http = "http://proxy.example.com:8080"
https = "http://proxy.example.com:8080"

# Translator-specific options (optional)
[translator.google]
# Google Translate API endpoint
endpoint = "https://translation.googleapis.com/language/translate/v2"

[translator.deepl]
# DeepL API endpoint
endpoint = "https://api.deepl.com/v2/translate"

[translator.openai]
# OpenAI API endpoint
endpoint = "https://api.openai.com/v1/chat/completions"
```

#### Command Line Overrides

You can override any configuration option from the command line. For example:

```bash
pdf2zh input.pdf output.pdf --service deepl --api-key YOUR_DEEPL_API_KEY
```

---

### OUTPUT

### 設定

`pdf2zh` は設定ファイルを作成して設定できます。設定ファイルは TOML ファイルで、Linux と macOS では `~/.pdf2zh/config.toml`、Windows では `%USERPROFILE%\.pdf2zh\config.toml` にあります。

#### 設定例

```toml
# デフォルトの翻訳サービス
service = "google"

# デフォルトの API キー（サービスで必要な場合）
api_key = "your_api_key_here"

# デフォルトのターゲット言語
target_lang = "zh"

# デフォルトのソース言語（自動検出の場合は auto）
source_lang = "auto"

# 同時翻訳のためのワーカー数
workers = 4

# 翻訳リクエストのタイムアウト（秒単位）
timeout = 60

# 失敗した翻訳のリトライ回数
retry_times = 3

# 出力形式（markdown、text、pdf）
format = "markdown"

# スキャンされた PDF の OCR を有効化
ocr = false

# 複雑な文書のレイアウト分析を有効化
layout_analysis = false

# プロキシ設定（オプション）
[proxy]
http = "http://proxy.example.com:8080"
https = "http://proxy.example.com:8080"

# 翻訳サービス固有のオプション（オプション）
[translator.google]
# Google Translate API エンドポイント
endpoint = "https://translation.googleapis.com/language/translate/v2"

[translator.deepl]
# DeepL API エンドポイント
endpoint = "https://api.deepl.com/v2/translate"

[translator.openai]
# OpenAI API エンドポイント
endpoint = "https://api.openai.com/v1/chat/completions"
```

#### コマンドラインでの上書き

コマンドラインから任意の設定オプションを上書きできます。例：

```bash
pdf2zh input.pdf output.pdf --service deepl --api-key YOUR_DEEPL_API_KEY
```
- ### Advanced Usage: For advanced users, `pdf2zh` provides additional options and features.

#### Custom Translators

You can create custom translators by implementing the `Translator` interface. Here's an example:

```python
from pdf2zh import Translator

class MyCustomTranslator(Translator):
    async def translate(self, text, source_lang, target_lang):
        # Implement your translation logic here
        return translated_text
```

#### Batch Processing

You can process multiple files in batch mode:

```bash
pdf2zh batch input_dir output_dir --target-lang ja
```

#### Parallel Processing

Use the `--workers` option to specify the number of parallel workers:

```bash
pdf2zh input.pdf output.pdf --workers 8
```

#### Custom Dictionaries

You can use custom dictionaries to improve translation accuracy:

```bash
pdf2zh input.pdf output.pdf --dictionary custom_dict.txt
```

The dictionary file should contain one term per line in the format `source_term target_term`.

#### Logging

Enable verbose logging for debugging:

```bash
pdf2zh input.pdf output.pdf --verbose
```

#### Dry Run

Perform a dry run to see what would be translated without actually translating:

```bash
pdf2zh input.pdf output.pdf --dry-run
```

---

### OUTPUT

### 高度な使い方

上級ユーザー向けに、`pdf2zh` は追加のオプションと機能を提供します。

#### カスタム翻訳機

`Translator` インターフェースを実装することで、カスタム翻訳機を作成できます。以下は例です：

```python
from pdf2zh import Translator

class MyCustomTranslator(Translator):
    async def translate(self, text, source_lang, target_lang):
        # ここに翻訳ロジックを実装
        return translated_text
```

#### バッチ処理

バッチモードで複数のファイルを処理できます：

```bash
pdf2zh batch input_dir output_dir --target-lang ja
```

#### 並列処理

`--workers` オプションを使用して並列ワーカーの数を指定できます：

```bash
pdf2zh input.pdf output.pdf --workers 8
```

#### カスタム辞書

カスタム辞書を使用して翻訳の精度を向上させることができます：

```bash
pdf2zh input.pdf output.pdf --dictionary custom_dict.txt
```

辞書ファイルは 1 行に 1 つの用語を `source_term target_term` の形式で含む必要があります。

#### ロギング

デバッグのために詳細なロギングを有効にします：

```bash
pdf2zh input.pdf output.pdf --verbose
```

#### ドライラン

実際に翻訳せずに何が翻訳されるかを確認するドライランを実行します：

```bash
pdf2zh input.pdf output.pdf --dry-run
```
- ### Performance: `pdf2zh` is designed for high performance and can handle large documents efficiently.

#### Benchmarks

| Document Size | Pages | Time (seconds) |
|---------------|-------|----------------|
| 1 MB          | 10    | 5              |
| 5 MB          | 50    | 25             |
| 10 MB         | 100   | 50             |
| 50 MB         | 500   | 250            |
| 100 MB        | 1000  | 500            |

These benchmarks are based on using the Google Translate API with 4 workers. Your mileage may vary depending on your internet connection and the translation service used.

#### Optimization Tips

- Use the `--workers` option to increase parallelism. The optimal number depends on your system and network conditions.
- For large documents, consider splitting them into smaller parts and translating them separately.
- Use the `--no-ocr` option if your document does not contain scanned text to avoid unnecessary OCR processing.
- Use the `--no-layout-analysis` option if your document has a simple layout to speed up processing.

#### Memory Usage

`pdf2zh` is memory efficient and can handle large documents without excessive memory usage. However, very large documents may require more memory. If you encounter memory issues, try reducing the number of workers or splitting the document.

---

### OUTPUT

### パフォーマンス

`pdf2zh` は高性能を目指して設計されており、大規模な文書を効率的に処理できます。

#### ベンチマーク

| 文書サイズ | ページ数 | 時間（秒） |
|------------|----------|------------|
| 1 MB       | 10       | 5          |
| 5 MB       | 50       | 25         |
| 10 MB      | 100      | 50         |
| 50 MB      | 500      | 250        |
| 100 MB     | 1000     | 500        |

これらのベンチマークは、Google Translate API を 4 ワーカーで使用した場合に基づいています。実際の結果は、インターネット接続と使用する翻訳サービスによって異なる場合があります。

#### 最適化のヒント

- `--workers` オプションを使用して並列性を高めます。最適な数はシステムとネットワークの状態によって異なります。
- 大規模な文書の場合は、文書を小さな部分に分割して個別に翻訳することを検討してください。
- 文書にスキャンされたテキストが含まれていない場合は、不要な OCR 処理を避けるために `--no-ocr` オプションを使用してください。
- 文書のレイアウトが単純な場合は、処理を高速化するために `--no-layout-analysis` オプションを使用してください。

#### メモリ使用量

`pdf2zh` はメモリ効率が良く、過剰なメモリ使用なしで大規模な文書を処理できます。ただし、非常に大きな文書ではより多くのメモリが必要になる場合があります。メモリの問題が発生した場合は、ワーカーの数を減らすか、文書を分割してみてください。
- ### Troubleshooting: If you encounter issues while using `pdf2zh`, here are some common problems and solutions:

#### Common Issues

1. **`FileNotFoundError`: The input file does not exist.**
   - **Solution**: Check the file path and ensure the file exists.

2. **`PermissionError`: Permission denied.**
   - **Solution**: Ensure you have read permission for the input file and write permission for the output directory.

3. **`UnsupportedFileTypeError`: The file type is not supported.**
   - **Solution**: Ensure the input file is a PDF. Other file types are not supported.

4. **`TranslationError`: Translation failed.**
   - **Solution**: Check your internet connection and ensure the translation service is accessible.

5. **`AuthenticationError`: Invalid API key.**
   - **Solution**: Verify your API key and ensure it is correct.

6. **`NetworkError`: Network error occurred.**
   - **Solution**: Check your internet connection and try again.

7. **`OCRProcessingError`: OCR processing failed.**
   - **Solution**: Ensure that the PDF contains text that can be OCRed, or try without OCR.

8. **`LayoutAnalysisError`: Layout analysis failed.**
   - **Solution**: Try without layout analysis if the document has a complex layout.

#### Getting Help

If you cannot resolve the issue, you can:

- Check the [FAQ](FAQ.md) for common questions.
- Open an issue on [GitHub](https://github.com/pdf2zh/pdf2zh/issues).
- Ask for help in the [Community](https://github.com/pdf2zh/pdf2zh/discussions).

---

### OUTPUT

### トラブルシューティング

`pdf2zh` の使用中に問題が発生した場合、以下に一般的な問題と解決策を示します：

#### 一般的な問題

1. **`FileNotFoundError`: 入力ファイルが存在しません。**
   - **解決策**: ファイルパスを確認し、ファイルが存在することを確認してください。

2. **`PermissionError`: 権限がありません。**
   - **解決策**: 入力ファイルの読み取り権限と出力ディレクトリへの書き込み権限があることを確認してください。

3. **`UnsupportedFileTypeError`: ファイルタイプがサポートされていません。**
   - **解決策**: 入力ファイルが PDF であることを確認してください。他のファイルタイプはサポートされていません。

4. **`TranslationError`: 翻訳に失敗しました。**
   - **解決策**: インターネット接続を確認し、翻訳サービスにアクセスできることを確認してください。

5. **`AuthenticationError`: 無効な API キーです。**
   - **解決策**: API キーを確認し、正しいことを確認してください。

6. **`NetworkError`: ネットワークエラーが発生しました。**
   - **解決策**: インターネット接続を確認し、再度お試しください。

7. **`OCRProcessingError`: OCR 処理に失敗しました。**
   - **解決策**: PDF に OCR 可能なテキストが含まれていることを確認するか、OCR なしで試してください。

8. **`LayoutAnalysisError`: レイアウト分析に失敗しました。**
   - **解決策**: 文書のレイアウトが複雑な場合は、レイアウト分析なしで試してください。

#### ヘルプの取得

問題が解決できない場合は、以下のことができます：

- 一般的な質問については [FAQ](FAQ.md) を確認してください。
- [GitHub](https://github.com/pdf2zh/pdf2zh/issues) で issue を開いてください。
- [コミュニティ](https://github.com/pdf2zh/pdf2zh/discussions) でヘルプを求めてください。
- ### FAQ: #### Q: What is `pdf2zh`?

**A**: `pdf2zh` is a tool for translating PDF documents from one language to another. It supports multiple translation services and output formats.

#### Q: How do I install `pdf2zh`?

**A**: You can install `pdf2zh` using pip:

```bash
pip install pdf2zh
```

#### Q: How do I use `pdf2zh`?

**A**: You can use `pdf2zh` via the command line or as a Python module. For example:

```bash
pdf2zh input.pdf output.pdf --target-lang ja
```

#### Q: What languages does `pdf2zh` support?

**A**: `pdf2zh` supports over 30 languages, including Chinese, English, Japanese, Korean, and many others. See the [Supported Languages](SUPPORTED_LANGUAGES.md) page for a complete list.

#### Q: Can I use my own translation service?

**A**: Yes, you can implement a custom translator by extending the `Translator` class.

#### Q: How do I handle large documents?

**A**: For large documents, it is recommended to split them into smaller parts and translate them separately. You can also use the `--workers` option to increase parallelism.

#### Q: What should I do if I encounter an error?

**A**: Check the error message and refer to the [Troubleshooting](TROUBLESHOOTING.md) guide. If the issue persists, open an issue on GitHub.

#### Q: Is `pdf2zh` free to use?

**A**: `pdf2zh` itself is free and open source. However, some translation services may require API keys and have usage costs.

#### Q: Can I contribute to `pdf2zh`?

**A**: Yes! We welcome contributions. Please see the [Contributing](CONTRIBUTING.md) guide for more information.

#### Q: Where can I get help?

**A**: You can ask for help in the [Community](https://github.com/pdf2zh/pdf2zh/discussions) or open an issue on [GitHub](https://github.com/pdf2zh/pdf2zh/issues).

---

### OUTPUT

### よくある質問

#### Q: `pdf2zh` とは何ですか？

**A**: `pdf2zh` は、PDF 文書をある言語から別の言語に翻訳するためのツールです。複数の翻訳サービスと出力形式をサポートしています。

#### Q: `pdf2zh` をインストールするにはどうすればよいですか？

**A**: `pdf2zh` は pip を使用してインストールできます：

```bash
pip install pdf2zh
```

#### Q: `pdf2zh` はどのように使用しますか？

**A**: `pdf2zh` はコマンドラインまたは Python モジュールとして使用できます。例：

```bash
pdf2zh input.pdf output.pdf --target-lang ja
```

#### Q: `pdf2zh` はどの言語をサポートしていますか？

**A**: `pdf2zh` は中国語、英語、日本語、韓国語など 30 以上の言語をサポートしています。完全なリストは [サポート言語](SUPPORTED_LANGUAGES.md) ページを参照してください。

#### Q: 独自の翻訳サービスを使用できますか？

**A**: はい、`Translator` クラスを拡張してカスタム翻訳機を実装できます。

#### Q: 大きな文書はどのように処理すればよいですか？

**A**: 大きな文書の場合は、文書を小さな部分に分割して個別に翻訳することをお勧めします。また、`--workers` オプションを使用して並列性を高めることもできます。

#### Q: エラーが発生した場合はどうすればよいですか？

**A**: エラーメッセージを確認し、[トラブルシューティング](TROUBLESHOOTING.md) ガイドを参照してください。問題が解決しない場合は、GitHub で issue を開いてください。

#### Q: `pdf2zh` は無料で使用できますか？

**A**: `pdf2zh` 自体は無料でオープンソースです。ただし、一部の翻訳サービスでは API キーが必要で、使用コストがかかる場合があります。

#### Q: `pdf2zh` に貢献できますか？

**A**: はい！貢献を歓迎します。詳細については [貢献](CONTRIBUTING.md) ガイドを参照してください。

#### Q: どこでヘルプを得られますか？

**A**: [コミュニティ](https://github.com/pdf2zh/pdf2zh/discussions) でヘルプを求めるか、[GitHub](https://github.com/pdf2zh/pdf2zh/issues) で issue を開いてください。
- ### Contributing: We welcome contributions to `pdf2zh`! Here's how you can help:

#### Ways to Contribute

- **Report Bugs**: If you find a bug, please open an issue on [GitHub](https://github.com/pdf2zh/pdf2zh/issues).
- **Suggest Features**: If you have an idea for a new feature, open an issue to discuss it.
- **Submit Pull Requests**: If you want to contribute code, please submit a pull request.
- **Improve Documentation**: Help us improve the documentation by fixing errors or adding examples.
- **Translate Documentation**: Help translate the documentation into other languages.

#### Development Setup

1. Fork the repository on GitHub.
2. Clone your fork locally:

```bash
git clone https://github.com/your-username/pdf2zh.git
cd pdf2zh
```

3. Install the development dependencies:

```bash
pip install -e .[dev]
```

4. Make your changes and test them.
5. Submit a pull request.

#### Code Style

Please follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.

#### Testing

Run the tests to ensure your changes don't break anything:

```bash
pytest
```

#### Documentation

Documentation is written in Markdown and located in the `docs` directory. Please ensure your changes include updates to the documentation if necessary.

#### Questions?

If you have any questions, feel free to ask in the [Community](https://github.com/pdf2zh/pdf2zh/discussions).

---

### OUTPUT

### 貢献

`pdf2zh` への貢献を歓迎します！以下は貢献する方法です：

#### 貢献方法

- **バグの報告**: バグを見つけた場合は、[GitHub](https://github.com/pdf2zh/pdf2zh/issues) で issue を開いてください。
- **機能の提案**: 新しい機能のアイデアがある場合は、issue を開いて議論してください。
- **プルリクエストの提出**: コードを貢献したい場合は、プルリクエストを提出してください。
- **ドキュメントの改善**: ドキュメントの誤りを修正したり、例を追加したりして、ドキュメントの改善を手伝ってください。
- **ドキュメントの翻訳**: ドキュメントを他の言語に翻訳するのを手伝ってください。

#### 開発環境のセットアップ

1. GitHub でリポジトリをフォークします。
2. フォークをローカルにクローンします：

```bash
git clone https://github.com/your-username/pdf2zh.git
cd pdf2zh
```

3. 開発依存関係をインストールします：

```bash
pip install -e .[dev]
```

4. 変更を加えてテストします。
5. プルリクエストを提出します。

#### コードスタイル

Python コードは [PEP 8](https://www.python.org/dev/peps/pep-0008/) スタイルガイドに従ってください。

#### テスト

変更が何も壊していないことを確認するためにテストを実行します：

```bash
pytest
```

#### ドキュメント

ドキュメントは Markdown で書かれており、`docs` ディレクトリにあります。必要に応じて、変更にドキュメントの更新を含めてください。

#### 質問？

質問がある場合は、[コミュニティ](https://github.com/pdf2zh/pdf2zh/discussions) でお気軽にお尋ねください。
- ### License: `pdf2zh` is released under the MIT License.

#### MIT License

Copyright (c) 2023 pdf2zh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

### OUTPUT

### ライセンス

`pdf2zh` は MIT ライセンスの下でリリースされています。

#### MIT ライセンス

Copyright (c) 2023 pdf2zh

以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も無制限に含まれます。

上記の著作権表示および本許可表示を、ソフトウェアのすべての複製または重要な部分に記載するものとします。

ソフトウェアは「現状のまま」で、明示黙示を問わず、何らの保証もなく提供されます。ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害についての保証も含みますが、それに限定されるものではありません。作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務について何らの責任も負わないものとします。

---
- ### Changelog: #### v1.0.0 (2023-10-01)

- Initial release of `pdf2zh`.
- Support for translating PDF documents.
- Multiple translation services: Google, DeepL, OpenAI.
- Output formats: Markdown, Text, PDF.
- Command line interface and Python API.

#### v1.1.0 (2023-10-15)

- Added support for OCR of scanned PDFs.
- Added layout analysis for complex documents.
- Improved performance with parallel processing.
- Added support for custom dictionaries.
- Added dry run mode.

#### v1.2.0 (2023-11-01)

- Added support for batch processing.
- Added support for more languages.
- Improved error handling and logging.
- Added configuration file support.
- Added progress tracking.

#### v1.3.0 (2023-11-15)

- Added support for custom translators.
- Added support for proxy settings.
- Improved memory efficiency.
- Added more translation services.
- Added community contributions.

#### v1.4.0 (2023-12-01)

- Added support for EPUB and HTML documents.
- Added support for immersive translation.
- Improved documentation.
- Added FAQ and troubleshooting guides.
- Added community discussions.

---

### OUTPUT

### 変更履歴

#### v1.0.0 (2023-10-01)

- `pdf2zh` の初期リリース。
- PDF 文書の翻訳のサポート。
- 複数の翻訳サービス：Google、DeepL、OpenAI。
- 出力形式：Markdown、テキスト、PDF。
- コマンドラインインターフェースと Python API。

#### v1.1.0 (2023-10-15)

- スキャンされた PDF の OCR サポートを追加。
- 複雑な文書のレイアウト分析を追加。
- 並列処理によるパフォーマンスの改善。
- カスタム辞書のサポートを追加。
- ドライランモードを追加。

#### v1.2.0 (2023-11-01)

- バッチ処理のサポートを追加。
- より多くの言語のサポートを追加。
- エラーハンドリングとロギングの改善。
- 設定ファイルのサポートを追加。
- 進捗追跡を追加。

#### v1.3.0 (2023-11-15)

- カスタム翻訳機のサポートを追加。
- プロキシ設定のサポートを追加。
- メモリ効率の改善。
- より多くの翻訳サービスの追加。
- コミュニティ貢献を追加。

#### v1.4.0 (2023-12-01)

- EPUB と HTML 文書のサポートを追加。
- 没入型翻訳のサポートを追加。
- ドキュメントの改善。
- FAQ とトラブルシューティングガイドを追加。
- コミュニティディスカッションを追加。
- ### Acknowledgments: We would like to thank the following projects and individuals for their contributions and inspiration:

#### Projects

- [PDFMiner](https://github.com/pdfminer/pdfminer.six): For PDF text extraction.
- [Google Translate](https://translate.google.com): For translation services.
- [DeepL](https://www.deepl.com): For translation services.
- [OpenAI](https://openai.com): For translation services.
- [Immersive Translate](https://immersivetranslate.com): For inspiration on immersive translation.
- [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate): For handling mathematical formulas.

#### Individuals

- **John Doe**: For initial development and project leadership.
- **Jane Smith**: For documentation and community management.
- **Alice Johnson**: For testing and bug reports.
- **Bob Brown**: For feature suggestions and contributions.

#### Community

Thanks to all the contributors and users of `pdf2zh` for their feedback and support.

---

### OUTPUT

### 謝辞

以下のプロジェクトと個人の貢献とインスピレーションに感謝します：

#### プロジェクト

- [PDFMiner](https://github.com/pdfminer/pdfminer.six): PDF テキスト抽出のために。
- [Google Translate](https://translate.google.com): 翻訳サービスのために。
- [DeepL](https://www.deepl.com): 翻訳サービスのために。
- [OpenAI](https://openai.com): 翻訳サービスのために。
- [Immersive Translate](https://immersivetranslate.com): 没入型翻訳のインスピレーションのために。
- [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate): 数式の処理のために。

#### 個人

- **John Doe**: 初期開発とプロジェクトリーダーシップのために。
- **Jane Smith**: ドキュメントとコミュニティ管理のために。
- **Alice Johnson**: テストとバグ報告のために。
- **Bob Brown**: 機能提案と貢献のために。

#### コミュニティ

`pdf2zh` のすべての貢献者とユーザーのフィードバックとサポートに感謝します。
- ### Community: Join our community to get help, share ideas, and contribute to `pdf2zh`.

#### Discord

Join our Discord server for real-time discussions:

[![Discord](https://img.shields.io/discord/1234567890?label=Discord&logo=discord)](https://discord.gg/pdf2zh)

#### GitHub Discussions

Use GitHub Discussions for longer-form discussions and questions:

[![GitHub Discussions](https://img.shields.io/github/discussions/pdf2zh/pdf2zh?label=Discussions)](https://github.com/pdf2zh/pdf2zh/discussions)

#### GitHub Issues

Report bugs and suggest features using GitHub Issues:

[![GitHub Issues](https://img.shields.io/github/issues/pdf2zh/pdf2zh?label=Issues)](https://github.com/pdf2zh/pdf2zh/issues)

#### Social Media

Follow us on social media for updates:

- Twitter: [@pdf2zh](https://twitter.com/pdf2zh)
- LinkedIn: [pdf2zh](https://www.linkedin.com/company/pdf2zh)

#### Newsletter

Subscribe to our newsletter for updates and announcements:

[Subscribe](https://pdf2zh.com/newsletter)

---

### OUTPUT

### コミュニティ

私たちのコミュニティに参加して、ヘルプを得たり、アイデアを共有したり、`pdf2zh` に貢献したりしましょう。

#### Discord

リアルタイムのディスカッションのために Discord サーバーに参加してください：

[![Discord](https://img.shields.io/discord/1234567890?label=Discord&logo=discord)](https://discord.gg/pdf2zh)

#### GitHub ディスカッション

長めのディスカッションや質問には GitHub ディスカッションを使用してください：

[![GitHub Discussions](https://img.shields.io/github/discussions/pdf2zh/pdf2zh?label=Discussions)](https://github.com/pdf2zh/pdf2zh/discussions)

#### GitHub Issues

バグの報告や機能の提案には GitHub Issues を使用してください：

[![GitHub Issues](https://img.shields.io/github/issues/pdf2zh/pdf2zh?label=Issues)](https://github.com/pdf2zh/pdf2zh/issues)

#### ソーシャルメディア

更新情報はソーシャルメディアでフォローしてください：

- Twitter: [@pdf2zh](https://twitter.com/pdf2zh)
- LinkedIn: [pdf2zh](https://www.linkedin.com/company/pdf2zh)

#### ニュースレター

更新と発表のためにニュースレターを購読してください：

[購読](https://pdf2zh.com/newsletter)
- ### Support: If you need help with `pdf2zh`, there are several ways to get support.

#### Documentation

First, check the documentation:

- [Getting Started](https://pdf2zh.com/getting-started)
- [Usage](https://pdf2zh.com/usage)
- [FAQ](https://pdf2zh.com/faq)
- [Troubleshooting](https://pdf2zh.com/troubleshooting)

#### Community Support

- **Discord**: Join our [Discord server](https://discord.gg/pdf2zh) for real-time help.
- **GitHub Discussions**: Ask questions on [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions).
- **GitHub Issues**: Report bugs on [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues).

#### Paid Support

For paid support and consulting, please contact us at [support@pdf2zh.com](mailto:support@pdf2zh.com).

#### Enterprise Support

For enterprise support, please contact us at [enterprise@pdf2zh.com](mailto:enterprise@pdf2zh.com).

---

### OUTPUT

### サポート

`pdf2zh` についてヘルプが必要な場合、サポートを得る方法がいくつかあります。

#### ドキュメント

まず、ドキュメントを確認してください：

- [始め方](https://pdf2zh.com/getting-started)
- [使い方](https://pdf2zh.com/usage)
- [よくある質問](https://pdf2zh.com/faq)
- [トラブルシューティング](https://pdf2zh.com/troubleshooting)

#### コミュニティサポート

- **Discord**: リアルタイムのヘルプのために [Discord サーバー](https://discord.gg/pdf2zh) に参加してください。
- **GitHub ディスカッション**: [GitHub ディスカッション](https://github.com/pdf2zh/pdf2zh/discussions) で質問してください。
- **GitHub Issues**: [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues) でバグを報告してください。

#### 有料サポート

有料サポートとコンサルティングについては、[support@pdf2zh.com](mailto:support@pdf2zh.com) までご連絡ください。

#### エンタープライズサポート

エンタープライズサポートについては、[enterprise@pdf2zh.com](mailto:enterprise@pdf2zh.com) までご連絡ください。
- ### Privacy: We take your privacy seriously. Here's how we handle your data:

#### Data Collection

- **No Data Collection**: `pdf2zh` does not collect any personal data.
- **Local Processing**: All processing is done locally on your machine. No data is sent to our servers.
- **Translation Services**: When using online translation services (e.g., Google Translate), your data may be sent to their servers. Please refer to their privacy policies for more information.

#### Data Usage

- **No Tracking**: We do not track your usage of `pdf2zh`.
- **No Advertising**: We do not show any advertisements.

#### Data Security

- **Local Storage**: Your files are stored locally and are not accessible to us.
- **Encryption**: We do not encrypt your data, but you can use encryption tools if needed.

#### Third-Party Services

- **Translation Services**: If you use online translation services, your data may be subject to their privacy policies. We recommend reviewing these policies before use.

#### Changes to This Policy

We may update this privacy policy from time to time. The latest version will always be available on our website.

#### Contact

If you have any questions about privacy, please contact us at [privacy@pdf2zh.com](mailto:privacy@pdf2zh.com).

---

### OUTPUT

### プライバシー

私たちはあなたのプライバシーを真剣に考えています。以下はデータの取り扱い方法です：

#### データ収集

- **データ収集なし**: `pdf2zh` は個人データを一切収集しません。
- **ローカル処理**: すべての処理はあなたのマシン上でローカルに行われます。データが私たちのサーバーに送信されることはありません。
- **翻訳サービス**: オンライン翻訳サービス（例：Google Translate）を使用する場合、あなたのデータはそれらのサーバーに送信される可能性があります。詳細についてはそれぞれのプライバシーポリシーを参照してください。

#### データ使用

- **トラッキングなし**: `pdf2zh` の使用状況を追跡することはありません。
- **広告なし**: 広告を表示することはありません。

#### データセキュリティ

- **ローカルストレージ**: あなたのファイルはローカルに保存され、私たちがアクセスすることはできません。
- **暗号化**: データを暗号化することはありませんが、必要に応じて暗号化ツールを使用できます。

#### 第三者サービス

- **翻訳サービス**: オンライン翻訳サービスを使用する場合、あなたのデータはそれらのプライバシーポリシーの対象となる可能性があります。使用前にこれらのポリシーを確認することをお勧めします。

#### ポリシーの変更

このプライバシーポリシーは随時更新される場合があります。最新版は常に私たちのウェブサイトでご覧いただけます。

#### 連絡先

プライバシーに関する質問がある場合は、[privacy@pdf2zh.com](mailto:privacy@pdf2zh.com) までご連絡ください。
- ### Security: We are committed to keeping `pdf2zh` secure. Here are some security considerations:

#### Code Security

- **Code Review**: All code changes are reviewed by multiple developers before being merged.
- **Dependency Scanning**: We regularly scan dependencies for known vulnerabilities.
- **Security Updates**: We promptly apply security updates to dependencies.

#### User Security

- **Local Processing**: All processing is done locally on your machine. No data is sent to our servers.
- **File Permissions**: `pdf2zh` only accesses files you explicitly specify.
- **Network Security**: When using online translation services, ensure you are using a secure connection.

#### Reporting Security Issues

If you discover a security vulnerability in `pdf2zh`, please report it responsibly:

- **Email**: Send details to [security@pdf2zh.com](mailto:security@pdf2zh.com).
- **Disclosure**: We will acknowledge your report and work on a fix. Please do not disclose the vulnerability publicly until it is fixed.

#### Security Best Practices

- **Keep `pdf2zh` Updated**: Always use the latest version of `pdf2zh` to ensure you have the latest security fixes.
- **Use Secure Connections**: When using online translation services, use HTTPS and secure connections.
- **Protect API Keys**: Keep your API keys secure and do not share them publicly.

---

### OUTPUT

### セキュリティ

私たちは `pdf2zh` のセキュリティを維持することに尽力しています。以下はいくつかのセキュリティに関する考慮事項です：

#### コードセキュリティ

- **コードレビュー**: すべてのコード変更は、マージされる前に複数の開発者によってレビューされます。
- **依存関係スキャン**: 既知の脆弱性について依存関係を定期的にスキャンします。
- **セキュリティ更新**: 依存関係へのセキュリティ更新を迅速に適用します。

#### ユーザーセキュリティ

- **ローカル処理**: すべての処理はあなたのマシン上でローカルに行われます。データが私たちのサーバーに送信されることはありません。
- **ファイル権限**: `pdf2zh` は明示的に指定したファイルのみにアクセスします。
- **ネットワークセキュリティ**: オンライン翻訳サービスを使用する場合は、安全な接続を使用していることを確認してください。

#### セキュリティ問題の報告

`pdf2zh` でセキュリティの脆弱性を発見した場合は、責任を持って報告してください：

- **メール**: 詳細を [security@pdf2zh.com](mailto:security@pdf2zh.com) まで送信してください。
- **開示**: 報告を確認し、修正に取り組みます。脆弱性が修正されるまで公に開示しないでください。

#### セキュリティのベストプラクティス

- **`pdf2zh` を最新の状態に保つ**: 最新のセキュリティ修正を確実に入手するために、常に最新バージョンの `pdf2zh` を使用してください。
- **安全な接続を使用する**: オンライン翻訳サービスを使用する場合は、HTTPS と安全な接続を使用してください。
- **API キーを保護する**: API キーを安全に保管し、公開して共有しないでください。
- ### Roadmap: Here's what we're planning for future versions of `pdf2zh`:

#### Short Term (Next 3 Months)

- **v1.5.0**: Add support for more file formats (e.g., DOCX, PPTX).
- **v1.6.0**: Improve OCR accuracy and speed.
- **v1.7.0**: Add more translation services (e.g., Microsoft Translate, Amazon Translate).

#### Medium Term (Next 6 Months)

- **v2.0.0**: Rewrite core for better performance and modularity.
- **v2.1.0**: Add plugin system for extensibility.
- **v2.2.0**: Add desktop GUI application.

#### Long Term (Next 12 Months)

- **v3.0.0**: Add AI-powered translation with custom models.
- **v3.1.0**: Add real-time collaborative translation.
- **v3.2.0**: Add support for voice translation.

#### Ongoing

- **Improve Documentation**: Continuously improve documentation and add more examples.
- **Community Engagement**: Engage with the community and incorporate feedback.
- **Performance Optimization**: Continuously optimize performance and reduce resource usage.

#### Contributing

If you want to contribute to any of these goals, please see the [Contributing](CONTRIBUTING.md) guide.

---

### OUTPUT

### ロードマップ

以下は `pdf2zh` の将来のバージョンに向けた計画です：

#### 短期（今後 3 か月）

- **v1.5.0**: より多くのファイル形式（例：DOCX、PPTX）のサポートを追加。
- **v1.6.0**: OCR の精度と速度を改善。
- **v1.7.0**: より多くの翻訳サービス（例：Microsoft Translate、Amazon Translate）を追加。

#### 中期（今後 6 か月）

- **v2.0.0**: パフォーマンスとモジュール性を向上させるためコアを書き直し。
- **v2.1.0**: 拡張性のためのプラグインシステムを追加。
- **v2.2.0**: デスクトップ GUI アプリケーションを追加。

#### 長期（今後 12 か月）

- **v3.0.0**: カスタムモデルによる AI 駆動の翻訳を追加。
- **v3.1.0**: リアルタイム協調翻訳を追加。
- **v3.2.0**: 音声翻訳のサポートを追加。

#### 継続中

- **ドキュメントの改善**: ドキュメントを継続的に改善し、より多くの例を追加。
- **コミュニティエンゲージメント**: コミュニティと関わり、フィードバックを取り入れる。
- **パフォーマンス最適化**: パフォーマンスを継続的に最適化し、リソース使用量を削減。

#### 貢献

これらの目標のいずれかに貢献したい場合は、[貢献](CONTRIBUTING.md) ガイドを参照してください。

{#minimal-usage-example-async}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # Initialize the translator
    translator = pdf2zh.Translator()

    # Translate a PDF file
    await translator.translate_pdf(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_lang="ja"
    )

asyncio.run(main())
```

### Minimal Usage Example (Sync) {#minimal-usage-example-sync}

```python
from pdf2zh import pdf2zh

# Initialize the translator
translator = pdf2zh.Translator()

# Translate a PDF file
translator.translate_pdf_sync(
    input_pdf="input.pdf",
    output_pdf="output.pdf",
    target_lang="ja"
)
```

### Advanced Usage Example {#advanced-usage-example}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # Initialize the translator with custom options
    translator = pdf2zh.Translator(
        # Specify the translation service
        service="google",
        
        # Set API key (if required)
        api_key="your_api_key_here",
        
        # Set proxy (optional)
        proxies={
            "http": "http://proxy.example.com:8080",
            "https": "http://proxy.example.com:8080",
        },
        
        # Other advanced options
        timeout=30,
        max_retries=3
    )

    # Translate with additional options
    await translator.translate_pdf(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_lang="ja",
        
        # Additional translation options
        source_lang="auto",  # Auto detect source language
        enable_ocr=True,     # Enable OCR for scanned PDFs
        preserve_formatting=True,
        
        # Progress callback (optional)
        progress_callback=lambda current, total: print(f"Progress: {current}/{total}")
    )

asyncio.run(main())
```

### Command Line Usage {#command-line-usage}

```bash
# Basic usage
pdf2zh translate input.pdf output.pdf --target-lang ja

# With additional options
pdf2zh translate input.pdf output.pdf \
    --target-lang ja \
    --service google \
    --api-key YOUR_API_KEY \
    --enable-ocr \
    --preserve-formatting
```

For more detailed usage instructions, see the [Usage](USAGE.md) documentation.

---

### TRANSLATION RESULT

### 最小限の使用例（非同期） {#最小限の使用例（非同期）}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # 翻訳機を初期化
    translator = pdf2zh.Translator()

    # PDF ファイルを翻訳
    await translator.translate_pdf(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_lang="ja"
    )

asyncio.run(main())
```

### 最小限の使用例（同期） {#最小限の使用例（同期）}

```python
from pdf2zh import pdf2zh

# 翻訳機を初期化
translator = pdf2zh.Translator()

# PDF ファイルを翻訳
translator.translate_pdf_sync(
    input_pdf="input.pdf",
    output_pdf="output.pdf",
    target_lang="ja"
)
```

### 高度な使用例 {#高度な使用例}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # カスタムオプションで翻訳機を初期化
    translator = pdf2zh.Translator(
        # 翻訳サービスを指定
        service="google",
        
        # API キーを設定（必要な場合）
        api_key="your_api_key_here",
        
        # プロキシを設定（オプション）
        proxies={
            "http": "http://proxy.example.com:8080",
            "https": "http://proxy.example.com:8080",
        },
        
        # その他の高度なオプション
        timeout=30,
        max_retries=3
    )

    # 追加オプションで翻訳
    await translator.translate_pdf(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_lang="ja",
        
        # 追加の翻訳オプション
        source_lang="auto",  # ソース言語を自動検出
        enable_ocr=True,     # スキャンされた PDF 用に OCR を有効化
        preserve_formatting=True,
        
        # 進捗コールバック（オプション）
        progress_callback=lambda current, total: print(f"Progress: {current}/{total}")
    )

asyncio.run(main())
```

### コマンドライン使用法 {#コマンドライン使用法}

```bash
# 基本的な使用法
pdf2zh translate input.pdf output.pdf --target-lang ja

# 追加オプション付き
pdf2zh translate input.pdf output.pdf \
    --target-lang ja \
    --service google \
    --api-key YOUR_API_KEY \
    --enable-ocr \
    --preserve-formatting
```

より詳細な使用手順については、[使い方](USAGE.md) ドキュメントを参照してください。
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

of Translation

If the translation is canceled, the following will happen:

- All translation progress will be lost and cannot be recovered.
- The application will be closed.
- The application will not automatically restart.

!!! Note

    If you are using the **Command Line** version, you can use the `--no-exit` parameter to prevent the application from exiting after completion.

### Cancellation of Translation

If the translation is canceled, the following will happen:

- All translation progress will be lost and cannot be recovered.
- The application will be closed.
- The application will not automatically restart.

!!! Note

    If you are using the **Command Line** version, you can use the `--no-exit` parameter to prevent the application from exiting after completion.

---

### TRANSLATION RESULT

### 翻訳のキャンセル

翻訳がキャンセルされると、以下のことが発生します：

- すべての翻訳の進捗が失われ、復元できなくなります。
- アプリケーションが閉じられます。
- アプリケーションは自動的に再起動しません。

!!! Note

    **コマンドライン** バージョンを使用している場合、`--no-exit` パラメータを使用して、完了後にアプリケーションが終了しないようにすることができます。

### 翻訳のキャンセル

翻訳がキャンセルされると、以下のことが発生します：

- すべての翻訳の進捗が失われ、復元できなくなります。
- アプリケーションが閉じられます。
- アプリケーションは自動的に再起動しません。

!!! Note

    **コマンドライン** バージョンを使用している場合、`--no-exit` パラメータを使用して、完了後にアプリケーションが終了しないようにすることができます。
- **Cancellation**: If the task consuming the stream is cancelled, the translation process will be cancelled as well.
- **Graceful Shutdown**: The translation process will attempt to shutdown gracefully, but any ongoing work will be lost.

---

### OUTPUT

ストリームを消費するタスクをキャンセルできます。キャンセルは基礎となる翻訳プロセスに伝播します。
- **キャンセル**: ストリームを消費するタスクがキャンセルされると、翻訳プロセスもキャンセルされます。
- **グレースフルシャットダウン**: 翻訳プロセスはグレースフルにシャットダウンを試みますが、進行中の作業はすべて失われます。

---
- ### Example Event Shapes: The following examples illustrate how to use the `EventShape` class to define different event shapes.

#### Example 1: Simple Rectangle

```python
from pdf2zh import EventShape

# Define a rectangle event shape
shape = EventShape(
    shape_type="rectangle",
    x=100,
    y=200,
    width=300,
    height=150,
    color="#FF5733",
    opacity=0.8
)
```

#### Example 2: Circle with Border

```python
from pdf2zh import EventShape

# Define a circle with border
shape = EventShape(
    shape_type="circle",
    x=400,
    y=300,
    radius=50,
    color="#33FF57",
    border_color="#000000",
    border_width=2,
    opacity=0.9
)
```

#### Example 3: Polygon

```python
from pdf2zh import EventShape

# Define a polygon using points
shape = EventShape(
    shape_type="polygon",
    points=[(100, 100), (200, 50), (300, 100), (250, 200), (150, 200)],
    color="#3357FF",
    opacity=0.7
)
```

#### Example 4: Text Box

```python
from pdf2zh import EventShape

# Define a text box
shape = EventShape(
    shape_type="text",
    x=150,
    y=350,
    text="Click Here!",
    font_size=16,
    font_family="Arial",
    color="#FFFFFF",
    background_color="#000000",
    opacity=1.0
)
```

#### Example 5: Custom Path

```python
from pdf2zh import EventShape

# Define a custom path using SVG path syntax
shape = EventShape(
    shape_type="path",
    path_data="M100 100 L200 200 L300 100 Z",
    color="#FF33A6",
    opacity=0.6
)
```

### Notes

- The `EventShape` class provides a flexible way to define various shapes for events.
- All coordinates and dimensions are in pixels.
- Colors can be specified using HEX codes, RGB values, or color names.
- Opacity values range from 0.0 (completely transparent) to 1.0 (completely opaque).

---

### OUTPUT

### イベントシェイプの例

以下の例は、`EventShape` クラスを使用してさまざまなイベントシェイプを定義する方法を示しています。

#### 例 1: シンプルな矩形

```python
from pdf2zh import EventShape

# 矩形のイベントシェイプを定義
shape = EventShape(
    shape_type="rectangle",
    x=100,
    y=200,
    width=300,
    height=150,
    color="#FF5733",
    opacity=0.8
)
```

#### 例 2: 枠線付き円

```python
from pdf2zh import EventShape

# 枠線付き円を定義
shape = EventShape(
    shape_type="circle",
    x=400,
    y=300,
    radius=50,
    color="#33FF57",
    border_color="#000000",
    border_width=2,
    opacity=0.9
)
```

#### 例 3: 多角形

```python
from pdf2zh import EventShape

# ポイントを使用して多角形を定義
shape = EventShape(
    shape_type="polygon",
    points=[(100, 100), (200, 50), (300, 100), (250, 200), (极速赛车开奖直播官网 150, 200)],
    color="#3357FF",
    opacity=0.7
)
```

#### 例 4: テキストボックス

```python
from pdf2zh import EventShape

# テキストボックスを極速赛车开奖直播官网 定義
shape = EventShape(
    shape_type="text",
    x=150,
    y=350,
    text="Click Here!",
    font_size=16,
    font_family="Arial",
    color="#FFFFFF",
    background_color="#000000",
    opacity=1.0
)
```

#### 例 5: カスタムパス

```python
from pdf2zh import EventShape

# SVG パス構文を使用してカスタムパスを定義
shape = EventShape(
    shape_type="path",
    path_data="M100 100 L200 200 L300 100 Z",
    color="#FF33A6",
    opacity=0.6
)
```

### 注意点

- `EventShape` クラスは、イベント用のさまざまなシェイプを定義する柔軟な方法を提供します。
- すべての座標と寸法はピクセル単位です。
- 色は HEX コード、RGB 値、または色名を使用して指定できます。
- 不透明度の値は 0.0（完全に透明）から 1.0（完全に不透明）の範囲です。

---
- ### Notes & Best Practices: #### Notes

- **Translating PDFs with Math**: For PDFs containing mathematical formulas, it is recommended to use [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) for better results.
- **Translating Webpages**: For translating webpages, it is recommended to use [Immersive Translate](https://immersivetranslate.com/) for a better experience.
- **Translating EPUBs**: For translating EPUBs, it is recommended to use [NeoReader](https://www.onyx-international.com.cn/ne 极速赛车开奖直播官网 oreader/) for a better experience.

#### Best Practices

- **Translating Long Documents**: For long documents, it is recommended to split the document into smaller parts and translate them separately to avoid performance issues.
- **Translating Documents with Images**: For documents with images, it is recommended to use the `--image-output-dir` option to save the images separately and then combine them with the translated text.
- **Translating Documents with Tables**: For documents with tables, it is recommended to use the `--table-output-dir` option to save the tables separately and then combine them with the translated text.

---

### OUTPUT

### 注意点とベストプラクティス

#### 注意点

- **数式を含む PDF の翻訳**: 数式を含む PDF を翻訳する場合は、より良い結果を得るために [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) の使用を推奨します。
- **ウェブページの翻訳**: ウェブページを翻訳する場合は、より良い体験のために [Immersive Translate](https://immersivetranslate.com/) の使用を推奨します。
- **EPUB の翻訳**: EPUB を翻訳する場合は、より良い体験のために [NeoReader](https://www.onyx-international.com.cn/neoreader/) の使用を推奨します。

#### ベストプラクティス

- **長文書の翻訳**: 長文書を翻訳する場合は、パフォーマンスの問題を避けるために、文書を小さな部分に分割して個別に翻訳することを推奨します。
- **画像を含む文書の翻訳**: 画像を含む文書を翻訳する場合は、`--image-output-dir` 極速赛车开奖直播官网 オプションを使用して画像を別途保存し、翻訳されたテキストと組み合わせることを推奨します。
- **表を含む文書の翻訳**: 表を含む文書を翻訳する場合は、`--table-output-dir` オプションを使用して表を別途保存し、翻訳されたテキストと組み合わせることを推奨します。

---
- ### Cancellation: of Translation

If the translation is canceled, the following will happen:

- All translation progress will be lost and cannot be recovered.
- The application will be closed.
- The application will not automatically restart.

!!! Note

    If you are using the **Command Line** version, you can use the `--no-exit` parameter to prevent the application from exiting after completion.

### Cancellation of Translation

If the translation is canceled, the following will happen:

- All translation progress will be lost and cannot be recovered.
- The application will be closed.
- The application will not automatically restart.

!!! Note

    If you are using the **Command Line** version, you can use the `--no-exit` parameter to prevent the application from exiting after completion.

---

### OUTPUT

### 翻訳のキャンセル

翻訳がキャンセルされると、以下のことが発生します：

- すべての翻訳の進捗が失われ、復元できなくなります。
- アプリケーションが閉じられます。
- アプリケーションは自動的に再起動しません。

!!! Note

    **コマンドライン** バージョンを使用している場合、`--no-exit` パラメータを使用して、完了後にアプリケーションが終了しないようにすることができます。

### 翻訳のキャンセル

翻訳がキャンセルされると、以下のことが発生します：

- すべての翻訳の進捗が失われ、復元できなくなります。
- アプリケーションが閉じられます。
- アプリケーションは自動的に再起動しません。

!!! Note

    **コマンドライン** バージョンを使用している場合、`--no 极速赛车开奖直播官网-exit` パラメータを使用して、完了後にアプリケーションが極速赛车开奖直播官网終了しないようにすることができます。

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

The following examples illustrate how to use the `EventShape` class to define different event shapes.

#### Example 1: Simple Rectangle

```python
from pdf2zh import EventShape

# Define a rectangle event shape
shape = EventShape(
    shape_type="rectangle",
    x=100,
    y=200,
    width=300,
    height=150,
    color="#FF5733",
    opacity=0.8
)
```

#### Example 2: Circle with Border

```python
from pdf2zh import EventShape

# Define a circle with border
shape = EventShape(
    shape_type="circle",
    x=400,
    y=300,
    radius=50,
    color="#33FF57",
    border_color="#000000",
    border_width=2,
    opacity=0.9
)
```

#### Example 3: Polygon

```python
from pdf2zh import EventShape

# Define a polygon using points
shape = EventShape(
    shape_type="polygon",
    points=[(100, 100), (200, 50), (300, 100), (250, 200), (150, 200)],
    color="#3357FF",
    opacity=0.7
)
```

#### Example 4: Text Box

```python
from pdf2zh import EventShape

# Define a text box
shape = EventShape(
    shape_type="text",
    x=150,
    y=350,
    text="Click Here!",
    font_size=16,
    font_family="Arial",
    color="#FFFFFF",
    background_color="#000000",
    opacity=1.0
)
```

#### Example 5: Custom Path

```python
from pdf2zh import EventShape

# Define a custom path using SVG path syntax
shape = EventShape(
    shape_type="path",
    path_data="M100 100 L200 200 L300 100 Z",
    color="#FF33A6",
    opacity=0.6
)
```

### Notes

- The `EventShape` class provides a flexible way to define various shapes for events.
- All coordinates and dimensions are in pixels.
- Colors can be specified using HEX codes, RGB values, or color names.
- Opacity values range from 0.0 (completely transparent) to 1.0 (completely opaque).

---

### TRANSLATION RESULT

### イベントシェイプの例

以下の例は、`EventShape` クラスを使用してさまざまなイベントシェイプを定義する方法を示しています。

#### 例 1: シンプルな矩形

```python
from pdf2zh import EventShape

# 矩形のイベントシェイプを定義
shape = EventShape(
    shape_type="rectangle",
    x=100,
    y=200,
    width=300,
    height=150,
    color="#FF5733",
    opacity=0.8
)
```

#### 例 2: 枠線付き円

```python
from pdf2zh import EventShape

# 枠線付き円を定義
shape = EventShape(
    shape_type="circle",
    x=400,
    y=300,
    radius=50,
    color="#33FF57",
    border_color="#000000",
    border_width=2,
    opacity=0.9
)
```

#### 例 3: 多角形

```python
from pdf2zh import EventShape

# ポイントを使用して多角形を定義
shape = EventShape(
    shape_type="polygon",
    points=[(100, 100), (200, 50), (300, 100), (250, 200), (150, 200)],
    color="#3357FF",
    opacity=0.7
)
```

#### 例 4: テキストボックス

```python
from pdf2zh import EventShape

# テキストボックスを定義
shape = EventShape(
    shape_type="text",
    x=150,
    y=350,
    text="Click Here!",
    font_size=16,
    font_family="Arial",
    color="#FFFFFF",
    background_color="#000000",
    opacity=1.0
)
```

#### 例 5: カスタムパス

```python
from pdf2zh import EventShape

# SVG パス構文を使用してカスタムパスを定義
shape = EventShape(
    shape_type="path",
    path_data="M100 100 L200 200 L300 100 Z",
    color="#FF33A6",
    opacity=0.6
)
```

### 注意点

- `EventShape` クラスは、イベント用のさまざまなシェイプを定義する柔軟な方法を提供します。
- すべての座標と寸法はピクセル単位です。
- 色は HEX コード、RGB 値、または色名を使用して指定できます。
- 不透明度の値は 0.0（完全に透明）から 1.0（完全に不透明）の範囲です。
```json
{
    "type": "stage_summary",
    "stage": "translation",
    "status": "completed",
    "start_time": "2024-01-01T00:00:00Z",
    "end_time": "2024-01-01T00:05:00Z",
    "duration": 300,
    "pages_processed": 10,
    "pages_total": 10,
    "progress": 1.0
}
```

---

### TRANSLATION RESULT

ステージサマリーイベント（例）：

```json
{
    "type": "stage_summary",
    "stage": "translation",
    "status": "completed",
    "start_time": "2024-01-01T00:00:00Z",
    "end_time": "2024-01-01T00:05:00Z",
    "duration": 300,
    "pages_processed": 10,
    "pages_total": 10,
    "progress": 1.0
}
```

---
- ## Supported Languages: 

The following languages are supported by pdf2zh:

- **Chinese** (`zh`): Simplified Chinese
- **Japanese** (`ja`): Japanese
- **English** (`en`): English
- **Korean** (`ko`): Korean
- **French** (`fr`): French
- **German** (`de`): German
- **Spanish** (`es`): Spanish
- **Italian** (`it`): Italian
- **Russian** (`ru`): Russian
- **Portuguese** (`pt`): Portuguese
- **Arabic** (`ar`): Arabic
- **Hindi** (`hi`): Hindi
- **Turkish** (`tr`): Turkish
- **Dutch** (`nl`): Dutch
- **Polish** (`pl`): Polish
- **Swedish** (`sv`): Swedish
- **Danish** (`da`): Danish
- **Finnish** (`fi`): Finnish
- **Norwegian** (`no`): Norwegian
- **Greek** (`el`): Greek
- **Czech** (`cs`): Czech
- **Romanian** (`ro`): Romanian
- **Hungarian** (`hu`): Hungarian
- **Bulgarian** (`bg`): Bulgarian
- **Catalan** (`ca`): Catalan
- **Ukrainian** (`uk`): Ukrainian
- **Hebrew** (`he`): Hebrew
- **Indonesian** (`id`): Indonesian
- **Malay** (`ms`): Malay
- **Thai** (`th`): Thai
- **Vietnamese** (`vi`): Vietnamese

For a complete list of supported languages and their corresponding language codes, please refer to the [Language Code](LANGUAGE_CODE.md) documentation.

---

### TRANSLATION RESULT

## サポート言語

pdf2zh でサポートされている言語は以下の通りです：

- **中国語** (`zh`)：簡体字中国語
- **日本語** (`ja`)：日本語
- **英語** (`en`)：英語
- **韓国語** (`ko`)：韓国語
- **フランス語** (`fr`)：フランス語
- **ドイツ語** (`de`)：ドイツ語
- **スペイン語** (`es`)：スペイン語
- **イタリア語** (`it`)：イタリア語
- **ロシア語** (`ru`)：ロシア語
- **ポルトガル語** (`pt`)：ポルトガル語
- **アラビア語** (`ar`)：アラビア語
- **ヒンディー語** (`hi`)：ヒンディー語
- **トルコ語** (`tr`)：トルコ語
- **オランダ語** (`nl`)：オランダ語
- **ポーランド語** (`pl`)：ポーランド語
- **スウェーデン語** (`sv`)：スウェーデン語
- **デンマーク語** (`da`)：デンマーク語
- **フィンランド語** (`fi`)：フィンランド語
- **ノルウェー語** (`no`)：ノルウェー語
- **ギリシャ語** (`el`)：ギリシャ語
- **チェコ語** (`cs`)：チェコ語
- **ルーマニア語** (`ro`)：ルーマニア語
- **ハンガリー語** (`hu`)：ハンガリー語
- **ブルガリア語** (`bg`)：ブルガリア語
- **カタロニア語** (`ca`)：カタロニア語
- **ウクライナ語** (`uk`)：ウクライナ語
- **ヘブライ語** (`he`)：ヘブライ語
- **インドネシア語** (`id`)：インドネシア語
- **マレー語** (`ms`)：マレー語
- **タイ語** (`th`)：タイ語
- **ベトナム語** (`vi`)：ベトナム語

サポートされている言語と対応する言語コードの完全なリストについては、[言語コード](LANGUAGE_CODE.md) ドキュメントを参照してください。

---
- ## Supported Languages: 

The following languages are supported by pdf2zh:

- **Chinese** (`zh`): Simplified Chinese
- **Japanese** (`ja`): Japanese
- **English** (`en`): English
- **Korean** (`ko`): Korean
- **French** (`fr`): French
- **German** (`de`): German
- **Spanish** (`es`): Spanish
- **Italian** (`it`): Italian
- **Russian** (`ru`): Russian
- **Portuguese** (`pt`): Portuguese
- **Arabic** (`ar`): Arabic
- **Hindi** (`hi`): Hindi
- **Turkish** (`tr`): Turkish
- **Dutch** (`nl`): Dutch
- **Polish** (`pl`): Polish
- **Swedish** (`sv`): Swedish
- **Danish** (`da`): Danish
- **Finnish** (`fi`): Finnish
- **Norwegian** (`no`): Norwegian
- **Greek** (`el`): Greek
- **Czech** (`cs`): Czech
- **Romanian** (`ro`): Romanian
- **Hungarian** (`hu`): Hungarian
- **Bulgarian** (`bg`): Bulgarian
- **Catalan** (`ca`): Catalan
- **Ukrainian** (`uk`): Ukrainian
- **Hebrew** (`he`): Hebrew
- **Indonesian** (`id`): Indonesian
- **Malay** (`ms`): Malay
- **Thai** (`th`): Thai
- **Vietnamese** (`vi`): Vietnamese

For a complete list of supported languages and their corresponding language codes, please refer to the [Language Code](LANGUAGE_CODE.md) documentation.

---

### TRANSLATION RESULT

## サポート言語

pdf2zh でサポートされている言語は以下の通りです：

- **中国語** (`zh`)：簡体字中国語
- **日本語** (`ja`)：日本語
- **英語** (`en`)：英語
- **韓国語** (`ko`)：韓国語
- **フランス語** (`fr`)：フランス語
- **ドイツ語** (`de`)：ドイツ語
- **スペイン語** (`es`)：スペイン語
- **イタリア語** (`it`)：イタリア語
- **ロシア語** (`ru`)：ロシア語
- **ポルトガル語** (`pt`)：ポルトガル語
- **アラビア語** (`ar`)：アラビア語
- **ヒンディー語** (`hi`)：ヒンディー語
- **トルコ語** (`tr`)：トルコ語
- **オランダ語** (`nl`)：オランダ語
- **ポーランド語** (`pl`)：ポーランド語
- **スウェーデン語** (`sv`)：スウェーデン語
- **デンマーク語** (`da`)：デンマーク語
- **フィンランド語** (`fi`)：フィンランド語
- **ノルウェー語** (`no`)：ノルウェー語
- **ギリシャ語** (`el`)：ギリシャ語
- **チェコ語** (`cs`)：チェコ語
- **ルーマニア語** (`ro`)：ルーマニア語
- **ハンガリー語** (`hu`)：ハンガリー語
- **ブルガリア語** (`bg`)：ブルガリア語
- **カタロニア語** (`ca`)：カタロニア語
- **ウクライナ語** (`uk`)：ウクライナ語
- **ヘブライ語** (`he`)：ヘブライ語
- **インドネシア語** (`id`)：インドネシア語
- **マレー語** (`ms`)：マレー語
- **タイ語** (`th`)：タイ語
- **ベトナム語** (`vi`)：ベトナム語

サポートされている言語と対応する言語コードの完全なリストについては、[言語コード](LANGUAGE_CODE.md) ドキュメントを参照してください。
- ## Community: 

Join our community to get help, share your experiences, and contribute to the project!

- [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions): Ask questions, share ideas, and discuss with other users and developers.
- [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues): Report bugs, request features, and suggest improvements.
- [Discord Server](https://discord.gg/example): Chat with the community in real-time (Note: This is a placeholder link, replace with your actual Discord invite link).
- [Telegram Group](https://t.me/example): Join our Telegram group for quick discussions (Note: This is a placeholder link, replace with your actual Telegram group link).

### Contributing

We welcome contributions from the community! Whether you're fixing a bug, adding a new feature, or improving the documentation, your help is appreciated.

Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

### Code of Conduct

To ensure a welcoming and inclusive community, we adhere to a [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating.

### License

This project is licensed under the [MIT License](LICENSE).

---

### TRANSLATION RESULT

## コミュニティ

私たちのコミュニティに参加して、ヘルプを受けたり、経験を共有したり、プロジェクトに貢献しましょう！

- [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions)：質問をしたり、アイデアを共有したり、他のユーザーや開発者と議論しましょう。
- [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues)：バグを報告したり、機能をリクエストしたり、改善を提案しましょう。
- [Discord サーバー](https://discord.gg/example)：コミュニティとリアルタイムでチャットしましょう（注：これはプレースホルダーリンクです。実際の Discord 招待リンクに置き換えてください）。
- [Telegram グループ](https://t.me/example)：簡単な議論のために私たちの Telegram グループに参加しましょう（注：これはプレースホルダーリンクです。実際の Telegram グループリンクに置き換えてください）。

### 貢献

コミュニティからの貢献を歓迎します！バグを修正する、新機能を追加する、ドキュメントを改善するなど、あなたの助けは感謝されます。

始めるには、[貢献ガイドライン](CONTRIBUTING.md) をお読みください。

### 行動規範

歓迎的で包括的なコミュニティを確保するために、私たちは [行動規範](CODE_OF_CONDUCT.md) を遵守しています。参加する前に必ずお読みください。

### ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) の下でライセンスされています。

---
- ## FAQ: 

### General Questions

#### Q: What is pdf2zh?
A: pdf2zh is a tool for translating PDF documents from one language to another. It supports various translation services and provides both command-line and web interface.

#### Q: Is pdf2zh free to use?
A: The core functionality of pdf2zh is free and open-source. However, some translation services may require API keys with associated costs.

#### Q: What languages are supported?
A: pdf2zh supports over 30 languages including Chinese, Japanese, English, Korean, and many European languages. See [Supported Languages](SUPPORTED_LANGUAGES.md) for complete list.

#### Q: Can I use my own translation service?
A: Yes, pdf2zh supports multiple translation services including Google Translate, DeepL, OpenAI, and others. You can configure your preferred service in the settings.

### Technical Questions

#### Q: How do I install pdf2zh?
A: You can install pdf2zh using pip:
```bash
pip install pdf2zh
```
Or from source:
```bash
git clone https://github.com/pdf2zh/pdf2zh.git
cd pdf2zh
pip install -e .
```

#### Q: How do I use the command line interface?
A: Basic usage:
```bash
pdf2zh translate input.pdf output.pdf --target-lang ja
```
See [Command Line Usage](USAGE_CLI.md) for detailed instructions.

#### Q: How do I use the web interface?
A: After installation, run:
```bash
pdf2zh serve
```
Then open your browser to `http://localhost:8000`.

#### Q: Can I translate scanned PDFs?
A: Yes, pdf2zh supports OCR (Optical Character Recognition) for scanned PDFs. Use the `--ocr` flag in CLI or enable OCR in web interface.

#### Q: What is the maximum file size?
A: The maximum file size depends on your system resources. For large files, consider splitting them into smaller parts.

### Troubleshooting

#### Q: Translation is slow. How can I improve performance?
A: You can:
- Increase the number of workers with `--workers` option
- Use a faster translation service
- Disable OCR if not needed
- Use a more powerful machine

#### Q: I'm getting API errors. What should I do?
A: Check your:
- Internet connection
- API key validity
- Service quotas and limits
- Proxy settings if using corporate network

#### Q: The output formatting is wrong. How to fix?
A: Try:
- Using different output formats (`--format` option)
- Enabling/disabling layout analysis
- Adjusting OCR settings

#### Q: Where can I get more help?
A: Check our:
- [Documentation](https://pdf2zh.com/docs)
- [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues)
- [Community Discord](https://discord.gg/example)

### Advanced Questions

#### Q: Can I customize the translation?
A: Yes, you can:
- Create custom translation rules
- Modify the translation templates
- Add support for new languages
- Integrate with other services

#### Q: Is batch processing supported?
A: Yes, you can process multiple files at once:
```bash
pdf2zh translate *.pdf --output-dir translated/ --target-lang ja
```

#### Q: Can I use pdf2zh in my own projects?
A: Yes, pdf2zh provides a Python API that you can integrate into your applications. See [Python API](API.md) for details.

#### Q: How do I contribute to pdf2zh?
A: We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

---

### TRANSLATION RESULT

## よくある質問

### 一般的な質問

#### Q: pdf2zh とは何ですか？
A: pdf2zh は、PDF 文書をある言語から別の言語に翻訳するためのツールです。さまざまな翻訳サービスをサポートし、コマンドラインと Web インターフェースの両方を提供します。

#### Q: pdf2zh は無料で使用できますか？
A: pdf2zh のコア機能は無料でオープンソースです。ただし、一部の翻訳サービスでは関連するコストがかかる API キーが必要な場合があります。

#### Q: どの言語がサポートされていますか？
A: pdf2zh は中国語、日本語、英語、韓国語、および多くのヨーロッパ言語を含む 30 以上の言語をサポートしています。完全なリストについては [サポート言語](SUPPORTED_LANGUAGES.md) を参照してください。

#### Q: 独自の翻訳サービスを使用できますか？
A: はい、pdf2zh は Google Translate、DeepL、OpenAI などの複数の翻訳サービスをサポートしています。設定で希望のサービスを構成できます。

### 技術的な質問

#### Q: pdf2zh をどのようにインストールしますか？
A: pip を使用して pdf2zh をインストールできます：
```bash
pip install pdf2zh
```
またはソースから：
```bash
git clone https://github.com/pdf2zh/pdf2zh.git
cd pdf2zh
pip install -e .
```

#### Q: コマンドラインインターフェースはどのように使用しますか？
A: 基本的な使用法：
```bash
pdf2zh translate input.pdf output.pdf --target-lang ja
```
詳細な手順については [コマンドラインの使用法](USAGE_CLI.md) を参照してください。

#### Q: Web インターフェースはどのように使用しますか？
A: インストール後、実行します：
```bash
pdf2zh serve
```
その後、ブラウザで `http://localhost:8000` を開きます。

#### Q: スキャンされた PDF を翻訳できますか？
A: はい、pdf2zh はスキャンされた PDF 用の OCR（光学文字認識）をサポートしています。CLI で `--ocr` フラグを使用するか、Web インターフェースで OCR を有効にします。

#### Q: 最大ファイルサイズはどれくらいですか？
A: 最大ファイルサイズはシステムリソースに依存します。大きなファイルの場合は、それらを小さな部分に分割することを検討してください。

### トラブルシューティング

#### Q: 翻訳が遅いです。パフォーマンスを向上させるにはどうすればよいですか？
A: 以下のことができます：
- `--workers` オプションでワーカーの数を増やす
- より高速な翻訳サービスを使用する
- 必要ない場合は OCR を無効にする
- より強力なマシンを使用する

#### Q: API エラーが発生します。どうすればよいですか？
A: 以下を確認してください：
- インターネット接続
- API キーの有効性
- サービスのクォータと制限
- 企業ネットワークを使用している場合のプロキシ設定

#### Q: 出力のフォーマットが間違っています。修正するにはどうすればよいですか？
A: 以下を試してください：
- 異なる出力形式の使用（`--format` オプション）
- レイアウト分析の有効化／無効化
- OCR 設定の調整

#### Q: さらにヘルプはどこで得られますか？
A: 以下を確認してください：
- [ドキュメント](https://pdf2zh.com/docs)
- [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues)
- [コミュニティ Discord](https://discord.gg/example)

### 高度な質問

#### Q: 翻訳をカスタマイズできますか？
A: はい、以下のことができます：
- カスタム翻訳ルールの作成
- 翻訳テンプレートの変更
- 新しい言語のサポートの追加
- 他のサービスとの統合

#### Q: バッチ処理はサポートされていますか？
A: はい、複数のファイルを一度に処理できます：
```bash
pdf2zh translate *.pdf --output-dir translated/ --target-lang ja
```

#### Q: 自分のプロジェクトで pdf2zh を使用できますか？
A: はい、pdf2zh はアプリケーションに統合できる Python API を提供します。詳細は [Python API](API.md) を参照してください。

#### Q: pdf2zh に貢献するにはどうすればよいですか？
A: 貢献を歓迎します！詳細は [貢献ガイド](CONTRIBUTING.md) を参照してください。
- ## For Translators: 

Thank you for your interest in contributing to pdf2zh's translation efforts! This guide will help you get started with translating the documentation and the application itself.

### Getting Started

1. **Fork the Repository**: Start by forking the [pdf2zh repository](https://github.com/pdf2zh/pdf2zh) on GitHub.
2. **Clone Your Fork**: Clone your forked repository to your local machine.
3. **Set Up Development Environment**: Follow the [Installation](INSTALLATION.md) guide to set up your development environment.
4. **Choose What to Translate**: You can translate:
   - Documentation (in the `docs/` directory)
   - Application strings (in the `src/` directory)
   - Website content (in the `website/` directory)

### Translation Guidelines

- **Consistency**: Use consistent terminology across all translations. Refer to the [Glossary](GLOSSARY.md) for standard terms.
- **Formatting**: Maintain the original formatting including Markdown syntax, code blocks, and links.
- **Cultural Appropriateness**: Ensure translations are culturally appropriate and use natural language.
- **Testing**: Test your translations to ensure they work correctly in context.

### Documentation Translation

1. **Find Files**: Documentation files are in the `docs/` directory in Markdown (`.md`) format.
2. **Create Translated Files**: For each language, create a corresponding directory (e.g., `docs/ja/` for Japanese) and place translated files there.
3. **Update Navigation**: Update the navigation configuration to include your translated documents.

### Application Translation

1. **Locale Files**: Application strings are in `src/locales/` directory.
2. **JSON Format**: Translations are in JSON format with key-value pairs.
3. **Add New Language**: To add a new language, create a new JSON file following the existing pattern.

### Submitting Translations

1. **Create a Branch**: Create a new branch for your translation work.
2. **Make Changes**: Make your translation changes in the appropriate files.
3. **Test**: Test your changes to ensure they work correctly.
4. **Submit Pull Request**: Submit a pull request to the main repository.

### Review Process

- All translations will be reviewed by maintainers for quality and consistency.
- You may be asked to make revisions based on feedback.
- Once approved, your translations will be merged into the main repository.

### Resources

- [Glossary](GLOSSARY.md): Standard terminology for consistent translations.
- [Style Guide](STYLE_GUIDE.md): Writing style guidelines for translations.
- [Translation Tools](TOOLS.md): Recommended tools for translation work.

### Need Help?

- Join our [Discord server](https://discord.gg/example) for real-time help.
- Check [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues) for existing translation tasks.
- Contact maintainers through [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions).

Thank you for contributing to making pdf2zh accessible to more users around the world!

---

### TRANSLATION RESULT

## 文書翻訳貢献ガイド

pdf2zh の翻訳作業に貢献することに興味を持っていただきありがとうございます！このガイドは、ドキュメントとアプリケーション自体の翻訳を始めるのに役立ちます。

### 開始方法

1. **リポジトリをフォーク**: まず、GitHub で [pdf2zh リポジトリ](https://github.com/pdf2zh/pdf2zh) をフォークします。
2. **フォークをクローン**: フォークしたリポジトリをローカルマシンにクローンします。
3. **開発環境のセットアップ**: [インストール](INSTALLATION.md) ガイドに従って開発環境をセットアップします。
4. **翻訳するものを選択**: 以下を翻訳できます：
   - ドキュメント（`docs/` ディレクトリ内）
   - アプリケーション文字列（`src/` ディレクトリ内）
   - ウェブサイトコンテンツ（`website/` ディレクトリ内）

### 翻訳ガイドライン

- **一貫性**: すべての翻訳で一貫した用語を使用してください。標準的な用語については [用語集](GLOSSARY.md) を参照してください。
- **フォーマット**: Markdown 構文、コードブロック、リンクを含む元のフォーマットを維持してください。
- **文化的適切さ**: 翻訳が文化的に適切で自然な言語を使用していることを確認してください。
- **テスト**: 翻訳が文脈で正しく機能することをテストしてください。

### ドキュメント翻訳

1. **ファイルを見つける**: ドキュメントファイルは Markdown（`.md`）形式で `docs/` ディレクトリにあります。
2. **翻訳ファイルを作成**: 各言語について、対応するディレクトリ（例：日本語の場合は `docs/ja/`）を作成し、翻訳されたファイルをそこに配置します。
3. **ナビゲーションの更新**: 翻訳されたドキュメントを含めるようにナビゲーション構成を更新します。

### アプリケーション翻訳

1. **ロケールファイル**: アプリケーション文字列は `src/locales/` ディレクトリにあります。
2. **JSON 形式**: 翻訳はキーと値のペアで JSON 形式です。
3. **新しい言語の追加**: 新しい言語を追加するには、既存のパターンに従って新しい JSON ファイルを作成します。

### 翻訳の提出

1. **ブランチを作成**: 翻訳作業用に新しいブランチを作成します。
2. **変更を加える**: 適切なファイルに翻訳の変更を加えます。
3. **テスト**: 変更が正しく機能することをテストします。
4. **プルリクエストを提出**: メインリポジトリにプルリクエストを提出します。

### レビュープロセス

- すべての翻訳は、品質と一貫性についてメンテナーによってレビューされます。
- フィードバックに基づいて修正を求められる場合があります。
- 承認されると、翻訳はメインリポジトリにマージされます。

### リソース

- [用語集](GLOSSARY.md): 一貫した翻訳のための標準用語。
- [スタイルガイド](STYLE_GUIDE.md): 翻訳のための執筆スタイルガイドライン。
- [翻訳ツール](TOOLS.md): 翻訳作業におすすめのツール。

### ヘルプが必要ですか？

- リアルタイムのヘルプには [Discord サーバー](https://discord.gg/example) に参加してください。
- 既存の翻訳タスクについては [GitHub Issues](https://github.com/pdf2zh/pdf2zh/issues) を確認してください。
- [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions) を通じてメンテナーに連絡してください。

世界中のより多くのユーザーが pdf2zh を利用できるように貢献していただきありがとうございます！
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

json
{
    "type": "progress",
    "page": 1,
    "total": 10,
    "progress": 0.1
}
```

---

### TRANSLATION RESULT

進捗イベント（例）：

```json
{
    "type": "progress",
    "page": 1,
    "total": 10,
    "progress": 0.1
}
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

This event is emitted when the translation is completed.

```json
{
  "event": "finish",
  "data": {
    "status": "success",
    "message": "Translation completed successfully"
  }
}
```

Error event (example): This event is emitted when an error occurs during translation.

```json
{
  "event": "error",
  "data": {
    "status": "error",
    "message": "An error occurred during translation"
  }
}
```

Progress event (example): This event is emitted to report the progress of the translation.

```json
{
  "event": "progress",
  "data": {
    "status": "progress",
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
```

---

### TRANSLATION RESULT

完了イベント（例）：このイベントは翻訳が完了したときに発行されます。

```json
{
  "event": "finish",
  "data": {
    "status": "success",
    "message": "Translation completed successfully"
  }
}
```

エラーイベント（例）：このイベントは翻訳中にエラーが発生したときに発行されます。

```json
{
  "event": "error",
  "data": {
    "status": "error",
    "message": "An error occurred during translation"
  }
}
```

進捗イベント（例）：このイベントは翻訳の進捗状況を報告するために発行されます。

```json
{
  "event": "progress",
  "data": {
    "status": "progress",
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
```
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

{
  "event": "error",
  "data": {
    "message": "Failed to translate page 5: Timeout after 60 seconds"
  }
}

Progress event (example): {
  "event": "progress",
  "data": {
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}

Result event (example): {
  "event": "result",
  "data": {
    "output_file": "output.md",
    "total_pages": 20,
    "translated_pages": 20,
    "failed_pages": 0
  }
}

---

### OUTPUT

エラーイベント（例）：{
  "event": "error",
  "data": {
    "message": "Failed to translate page 5: Timeout after 60 seconds"
  }
}

進捗イベント（例）：{
  "event": "progress",
  "data": {
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}

結果イベント（例）：{
  "event": "result",
  "data": {
    "output_file": "output.md",
    "total_pages": 20,
    "translated_pages": 20,
    "failed_pages": 0
  }
}
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

#### Notes

- **Translating PDFs with Math**: For PDFs containing mathematical formulas, it is recommended to use [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) for better results.
- **Translating Webpages**: For translating webpages, it is recommended to use [Immersive Translate](https://immersivetranslate.com/) for a better experience.
- **Translating EPUBs**: For translating EPUBs, it is recommended to use [NeoReader](https://www.onyx-international.com.cn/neoreader/) for a better experience.

#### Best Practices

- **Translating Long Documents**: For long documents, it is recommended to split the document into smaller parts and translate them separately to avoid performance issues.
- **Translating Documents with Images**: For documents with images, it is recommended to use the `--image-output-dir` option to save the images separately and then combine them with the translated text.
- **Translating Documents with Tables**: For documents with tables, it is recommended to use the `--table-output-dir` option to save the tables separately and then combine them with the translated text.

---

### OUTPUT

### 注意点とベストプラクティス

#### 注意点

- **数式を含む PDF の翻訳**: 数式を含む PDF を翻訳する場合は、より良い結果を得るために [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) の使用を推奨します。
- **ウェブページの翻訳**: ウェブページを翻訳する場合は、より良い体験のために [Immersive Translate](https://immersivetranslate.com/) の使用を推奨します。
- **EPUB の翻訳**: EPUB を翻訳する場合は、より良い体験のために [NeoReader](https://www.onyx-international.com.cn/neoreader/) の使用を推奨します。

#### ベストプラクティス

- **長文書の翻訳**: 長文書を翻訳する場合は、パフォーマンスの問題を避けるために、文書を小さな部分に分割して個別に翻訳することを推奨します。
- **画像を含む文書の翻訳**: 画像を含む文書を翻訳する場合は、`--image-output-dir` オプションを使用して画像を別途保存し、翻訳されたテキストと組み合わせることを推奨します。
- **表を含む文書の翻訳**: 表を含む文書を翻訳する場合は、`--table-output-dir` オプションを使用して表を別途保存し、翻訳されたテキストと組み合わせることを推奨します。
---

### TRANSLATION RESULT

- ジェネレータからのエラーイベントと例外の両方を常に処理してください。
- 不必要な作業を避けるために、`finish` でループを抜けてください。
- 呼び出す前に、`file` が存在し、`settings.validate_settings()` が通過することを確認してください。
- 大きな文書は分割される可能性があります。`part_index/total_parts` と `overall_progress` を使用して UI を駆動してください。
- UI が繰り返しの同一の更新に敏感な場合は、`progress_update` をデバウンスしてください。
- `report_interval` (SettingsModel): `progress_update` イベントの送出頻度のみを制御します。`stage_summary`、`progress_start`、`progress_end`、または `finish` には影響しません。デフォルトは 0.1 秒で、最小許容値は 0.05 秒です。進捗監視ロジックに従い、`stage_total <= 3` の場合、更新は `report_interval` によって調整されません。

<div align="right"> 
<h6><small>このページの一部のコンテンツは GPT によって翻訳されており、エラーが含まれている可能性があります。</small></h6>