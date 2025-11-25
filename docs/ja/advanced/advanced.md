[**高度な設定**](./introduction.md) > **高度な設定** _(現在)_

---

<h3 id="目次">目次</h3>

- [コマンドライン引数](#コマンドライン引数)
- [レート制限設定ガイド](#レート制限設定ガイド)
- [部分翻訳](#部分翻訳)
- [ソース言語とターゲット言語の指定](#ソース言語とターゲット言語の指定)
- [例外付き翻訳](#例外付き翻訳)
- [カスタムプロンプト](#カスタムプロンプト)
- [カスタム設定](#カスタム設定)
- [クリーン処理のスキップ](#クリーン処理のスキップ)
- [翻訳キャッシュ](#翻訳キャッシュ)
- [公開サービスとしてのデプロイ](#公開サービスとしてのデプロイ)
- [認証とウェルカムページ](#認証とウェルカムページ)
- [用語集サポート](#用語集サポート)

---

#### コマンドライン引数

コマンドラインで翻訳コマンドを実行し、現在の作業ディレクトリに翻訳済みドキュメント `example-mono.pdf` とバイリンガルドキュメント `example-dual.pdf` を生成します。デフォルトの翻訳サービスとして Google を使用します。その他のサポート翻訳サービスは [HERE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services) で確認できます。

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

以下の表に、すべての高度なオプションを参考として記載します：

##### 引数

| `output-dir`                    | Output directory for translated PDF files                                               | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `engine`                        | Translation engine to use (`google`, `google_free`, `deepl`, `openai`, `gemini`, `azure`, `claude`, `youdao`, `baidu`, `tencent`, `ali`, `volcengine`, `ollama`, `groq`) | `pdf2zh_next example.pdf --engine google`                                                                             |
| `source-lang`                   | Source language of the PDF                                                              | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `target-lang`                   | Target language for translation                                                         | `pdf2zh_next example.pdf --target-lang zh`                                                                            |
| `pages`                         | Specific pages to translate (e.g., 1-5, 8, 11-13)                                       | `pdf2zh_next example.pdf --pages 1-5`                                                                                 |
| `ocr`                           | Enable OCR for image-based PDFs                                                         | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `ocr-lang`                      | Language for OCR engine                                                                 | `pdf2zh_next example.pdf --ocr-lang en`                                                                               |
| `parallel`                      | Number of parallel translation tasks                                                    | `pdf2zh_next example.pdf --parallel 5`                                                                                |
| `retry`                         | Number of retries for failed translations                                               | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `timeout`                       | Timeout for each translation request in seconds                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `api-key`                       | API key for translation service                                                         | `pdf2zh_next example.pdf --engine openai --api-key YOUR_API_KEY`                                                       |
| `api-base`                      | Custom API base URL                                                                     | `pdf2zh_next example.pdf --engine openai --api-base https://api.openai.com/v1`                                         |
| `model`                         | Model name for AI translation engines                                                   | `pdf2zh_next example.pdf --engine openai --model gpt-4`                                                               |
| `formula-detection`             | Strategy for formula detection (`none`, `ml`, `rule`)                                   | `pdf2zh_next example.pdf --formula-detection ml`                                                                      |
| `formula-translation`           | Strategy for formula translation (`ignore`, `translate`, `ignore_all`)                  | `pdf2zh_next example.pdf --formula-translation ignore`                                                                |
| `glossary`                      | Glossary file for translation                                                           | `pdf2zh_next example.pdf --glossary glossary.txt`                                                                     |
| `highlight-color`               | Color for highlighting translations                                                     | `pdf2zh_next example.pdf --highlight-color yellow`                                                                    |
| `highlight-opacity`             | Opacity for highlight overlay (0-1)                                                     | `pdf2zh_next example.pdf --highlight-opacity 0.3`                                                                     |
| `highlight-position`            | Position for highlight text (`original`, `below`, `above`, `right`)                     | `pdf2zh_next example.pdf --highlight-position below`                                                                  |
| `line-break`                    | Strategy for line break handling (`auto`, `preserve`, `single`)                         | `pdf2zh_next example.pdf --line-break preserve`                                                                       |
| `font-family`                   | Font family for translated text                                                         | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `font-size`                     | Font size for translated text                                                           | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `bold`                          | Make translated text bold                                                               | `pdf2zh_next example.pdf --bold`                                                                                      |
| `italic`                        | Make translated text italic                                                             | `pdf2zh_next example.pdf --italic`                                                                                    |
| `remove-original`                | Remove original text after translation                                                  | `pdf2zh_next example.pdf --remove-original`                                                                           |
| `config`                        | Path to configuration file                                                              | `pdf2zh_next example.pdf --config config.json`                                                                        |
| `version`                       | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `help`                          | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| オプション                     | 機能                                                                                   | 例                                                                                                                   |
| ------------------------------ | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                  | 処理する入力 PDF ファイル                                                               | `pdf2zh_next example.pdf`                                                                                             |
| `output-dir`                   | 翻訳された PDF ファイルの出力ディレクトリ                                                | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `engine`                       | 使用する翻訳エンジン（`google`、`google_free`、`deepl`、`openai`、`gemini`、`azure`、`claude`、`youdao`、`baidu`、`tencent`、`ali`、`volcengine`、`ollama`、`groq`） | `pdf2zh_next example.pdf --engine google`                                                                             |
| `source-lang`                  | PDF の原文言語                                                                          | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `target-lang`                  | 翻訳対象の言語                                                                          | `pdf2zh_next example.pdf --target-lang zh`                                                                            |
| `pages`                        | 翻訳する特定のページ（例：1-5、8、11-13）                                                | `pdf2zh_next example.pdf --pages 1-5`                                                                                 |
| `ocr`                          | 画像ベースの PDF に対して OCR を有効化                                                    | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `ocr-lang`                     | OCR エンジンの言語                                                                      | `pdf2zh_next example.pdf --ocr-lang en`                                                                               |
| `parallel`                     | 並列翻訳タスクの数                                                                      | `pdf2zh_next example.pdf --parallel 5`                                                                                |
| `retry`                        | 失敗した翻訳のリトライ回数                                                              | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `timeout`                      | 各翻訳リクエストのタイムアウト（秒）                                                    | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `api-key`                      | 翻訳サービスの API キー                                                                 | `pdf2zh_next example.pdf --engine openai --api-key YOUR_API_KEY`                                                       |
| `api-base`                     | カスタム API ベース URL                                                                 | `pdf2zh_next example.pdf --engine openai --api-base https://api.openai.com/v1`                                         |
| `model`                        | AI 翻訳エンジンのモデル名                                                                | `pdf2zh_next example.pdf --engine openai --model gpt-4`                                                               |
| `formula-detection`            | 数式検出の戦略（`none`、`ml`、`rule`）                                                   | `pdf2zh_next example.pdf --formula-detection ml`                                                                      |
| `formula-translation`          | 数式翻訳の戦略（`ignore`、`translate`、`ignore_all`）                                    | `pdf2zh_next example.pdf --formula-translation ignore`                                                                |
| `glossary`                     | 翻訳用の用語集ファイル                                                                  | `pdf2zh_next example.pdf --glossary glossary.txt`                                                                     |
| `highlight-color`              | 翻訳テキストのハイライト色                                                              | `pdf2zh_next example.pdf --highlight-color yellow`                                                                    |
| `highlight-opacity`            | ハイライトオーバーレイの不透明度（0-1）                                                  | `pdf2zh_next example.pdf --highlight-opacity 0.3`                                                                     |
| `highlight-position`           | ハイライトテキストの位置（`original`、`below`、`above`、`right`）                        | `pdf2zh_next example.pdf --highlight-position below`                                                                  |
| `line-break`                   | 改行処理の戦略（`auto`、`preserve`、`single`）                                           | `pdf2zh_next example.pdf --line-break preserve`                                                                       |
| `font-family`                  | 翻訳テキストのフォントファミリー                                                        | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `font-size`                    | 翻訳テキストのフォントサイズ                                                            | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `bold`                         | 翻訳テキストを太字にする                                                                | `pdf2zh_next example.pdf --bold`                                                                                      |
| `italic`                       | 翻訳テキストを斜体にする                                                                | `pdf2zh_next example.pdf --italic`                                                                                    |
| `remove-original`              | 翻訳後に原文を削除する                                                                  | `pdf2zh_next example.pdf --remove-original`                                                                           |
| `config`                       | 設定ファイルのパス                                                                      | `pdf2zh_next example.pdf --config config.json`                                                                        |
| `version`                      | バージョン情報を表示する                                                                | `pdf2zh_next --version`                                                                                               |
| `help`                         | ヘルプメッセージを表示する                                                              | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--engine`                      | Translation engine to use. See [Translation Services](docs/TRANSLATION_SERVICES.md) for more. | `pdf2zh_next example.pdf --engine deepl`                                                                              |
| `--lang`                        | Language code of target language. See [Supported Languages](docs/SUPPORTED_LANGUAGES.md) for more. | `pdf2zh_next example.pdf --lang ja`                                                                                   |
| `--cache-dir`                   | Directory to store cache files                                                          | `pdf2zh_next example.pdf --cache-dir /cachepath`                                                                      |
| `--config`                      | Path to config file                                                                     | `pdf2zh_next example.pdf --config /configpath/config.yaml`                                                            |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--no-ocr`                      | Disable OCR                                                                             | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--force-ocr`                   | Force OCR even if text is detected                                                      | `pdf2zh_next example.pdf --force-ocr`                                                                                 |
| `--only-ocr`                    | Only perform OCR without translation                                                    | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-translate`              | Only perform translation without OCR                                                    | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--font-size`                   | Font size for output PDF (pt)                                                           | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--font-family`                 | Font family for output PDF                                                              | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `--line-spacing`                | Line spacing for output PDF                                                             | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--margin`                      | Page margin for output PDF (mm)                                                         | `pdf2zh_next example.pdf --margin 20`                                                                                 |
| `--render-mode`                 | Render mode for OCR. Options: `auto`, `hi_res`, `fast`                                  | `pdf2zh_next example.pdf --render-mode hi_res`                                                                        |
| `--target-pages`                | Target pages to process. Example: `1-3,5,7-9`                                           | `pdf2zh_next example.pdf --target-pages 1-3,5,7-9`                                                                    |
| `--workers`                     | Number of workers for parallel processing                                               | `pdf2zh_next example.pdf --workers 4`                                                                                 |
| `--timeout`                     | Timeout for each translation request (seconds)                                          | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry`                       | Number of retries for failed requests                                                   | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--verbose`                     | Enable verbose logging                                                                  | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--output`                      | ファイルの出力ディレクトリ                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--engine`                      | 使用する翻訳エンジン。詳細は [翻訳サービス](docs/TRANSLATION_SERVICES.md) を参照。 | `pdf2zh_next example.pdf --engine deepl`                                                                              |
| `--lang`                        | ターゲット言語の言語コード。詳細は [サポート言語](docs/SUPPORTED_LANGUAGES.md) を参照。 | `pdf2zh_next example.pdf --lang ja`                                                                                   |
| `--cache-dir`                   | キャッシュファイルの保存ディレクトリ                                                          | `pdf2zh_next example.pdf --cache-dir /cachepath`                                                                      |
| `--config`                      | 設定ファイルのパス                                                                     | `pdf2zh_next example.pdf --config /configpath/config.yaml`                                                            |
| `--no-cache`                    | キャッシュを無効にする                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--no-ocr`                      | OCR を無効にする                                                                             | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--force-ocr`                   | テキストが検出されても強制的に OCR を実行                                                      | `pdf2zh_next example.pdf --force-ocr`                                                                                 |
| `--only-ocr`                    | 翻訳を行わず OCR のみを実行                                                    | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-translate`              | OCR を行わず翻訳のみを実行                                                                            | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--font-size`                   | 出力 PDF のフォントサイズ（pt）                                                           | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--font-family`                 | 出力 PDF のフォントファミリー                                                              | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `--line-spacing`                | 出力 PDF の行間隔                                                             | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--margin`                      | 出力 PDF のページ余白（mm）                                                         | `pdf2zh_next example.pdf --margin 20`                                                                                 |
| `--render-mode`                 | OCR のレンダリングモード。オプション：`auto`、`hi_res`、`fast`                                  | `pdf2zh_next example.pdf --render-mode hi_res`                                                                        |
| `--target-pages`                | 処理対象のページ。例：`1-3,5,7-9`                                           | `pdf2zh_next example.pdf --target-pages 1-3,5,7-9`                                                                    |
| `--workers`                     | 並列処理のワーカー数                                               | `pdf2zh_next example.pdf --workers 4`                                                                                 |
| `--timeout`                     | 各翻訳リクエストのタイムアウト（秒）                                          | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry`                       | 失敗したリクエストの再試行回数                                                   | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--verbose`                     | 詳細ログを有効にする                                                                  | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | バージョンを表示して終了                                                                   | `pdf2zh_next --version`                                                                                               |
| `--help`                        | ヘルプメッセージを表示して終了                                                              | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-model`            | Model to use for translation                                                            | `pdf2zh_next example.pdf --openai --openai-model gpt-4o`<br>`pdf2zh_next example.pdf --deepseek --deepseek-model deepseek-chat` |
| `--<Services>-api-key`          | API Key                                                                                 | `pdf2zh_next example.pdf --openai --openai-api-key <your-api-key>`                                                    |
| `--<Services>-api-base`         | API Base URL (Optional)                                                                  | `pdf2zh_next example.pdf --openai --openai-api-base <your-api-base>`                                                  |
| `--<Services>-prompt`           | Prompt to use for translation (Optional)                                                | `pdf2zh_next example.pdf --openai --openai-prompt <your-prompt>`                                                      |
| `--<Services>-temperature`      | Temperature for translation (Optional)                                                  | `pdf2zh_next example.pdf --openai --openai-temperature 0.1`                                                          |
| `--<Services>-max-tokens`       | Max tokens for translation (Optional)                                                   | `pdf2zh_next example.pdf --openai --openai-max-tokens 1000`                                                           |
| `--<Services>-timeout`          | Timeout for translation (Optional)                                                      | `pdf2zh_next example.pdf --openai --openai-timeout 100`                                                               |
| `--<Services>-retry`            | Retry times for translation (Optional)                                                  | `pdf2zh_next example.pdf --openai --openai-retry 3`                                                                   |
| `--<Services>-proxy`            | Proxy for translation (Optional)                                                        | `pdf2zh_next example.pdf --openai --openai-proxy http://127.0.0.1:7890`                                              |
| `--<Services>-organization`     | Organization for translation (Optional)                                                 | `pdf2zh_next example.pdf --openai --openai-organization <your-organization>`                                          |
| `--<Services>-project`          | Project for translation (Optional)                                                       | `pdf2zh_next example.pdf --openai --openai-project <your-project>`                                                    |
| `--<Services>-extra-args`       | Extra arguments for translation (Optional)                                              | `pdf2zh_next example.pdf --openai --openai-extra-args '{"top_p": 0.9}'`                                               |
| `--<Services>-extra-headers`    | Extra headers for translation (Optional)                                                | `pdf2zh_next example.pdf --openai --openai-extra-headers '{"X-Custom-Header": "value"}'`                             |

---

### OUTPUT

| `--<Services>`                  | [**特定のサービス**](./Documentation-of-Translation-Services.md) を使用して翻訳する | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-model`            | 翻訳に使用するモデル                                                            | `pdf2zh_next example.pdf --openai --openai-model gpt-4o`<br>`pdf2zh_next example.pdf --deepseek --deepseek-model deepseek-chat` |
| `--<Services>-api-key`          | API キー                                                                                 | `pdf2zh_next example.pdf --openai --openai-api-key <your-api-key>`                                                    |
| `--<Services>-api-base`         | API ベース URL（オプション）                                                                  | `pdf2zh_next example.pdf --openai --openai-api-base <your-api-base>`                                                  |
| `--<Services>-prompt`           | 翻訳に使用するプロンプト（オプション）                                                | `pdf2zh_next example.pdf --openai --openai-prompt <your-prompt>`                                                      |
| `--<Services>-temperature`      | 翻訳の温度（オプション）                                                  | `pdf2zh_next example.pdf --openai --openai-temperature 0.1`                                                          |
| `--<Services>-max-tokens`       | 翻訳の最大トークン数（オプション）                                                   | `pdf2zh_next example.pdf --openai --openai-max-tokens 1000`                                                           |
| `--<Services>-timeout`          | 翻訳のタイムアウト（オプション）                                                      | `pdf2zh_next example.pdf --openai --openai-timeout 100`                                                               |
| `--<Services>-retry`            | 翻訳の再試行回数（オプション）                                                  | `pdf2zh_next example.pdf --openai --openai-retry 3`                                                                   |
| `--<Services>-proxy`            | 翻訳用のプロキシ（オプション）                                                        | `pdf2zh_next example.pdf --openai --openai-proxy http://127.0.0.1:7890`                                              |
| `--<Services>-organization`     | 翻訳用の組織（オプション）                                                 | `pdf2zh_next example.pdf --openai --openai-organization <your-organization>`                                          |
| `--<Services>-project`          | 翻訳用のプロジェクト（オプション）                                                       | `pdf2zh_next example.pdf --openai --openai-project <your-project>`                                                    |
| `--<Services>-extra-args`       | 翻訳用の追加引数（オプション）                                              | `pdf2zh_next example.pdf --openai --openai-extra-args '{"top_p": 0.9}'`                                               |
| `--<Services>-extra-headers`    | 翻訳用の追加ヘッダー（オプション）                                                | `pdf2zh_next example.pdf --openai --openai-extra-headers '{"X-Custom-Header": "value"}'`                             |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | Input PDF file path                                                                     | `pdf2zh_next --input ./example.pdf`                                                                                   |
| `--output`, `-o`                | Output PDF file path                                                                    | `pdf2zh_next --input ./example.pdf --output ./example_translated.pdf`                                                 |
| `--target-lang`, `-tl`          | Target language code                                                                    | `pdf2zh_next --input ./example.pdf --target-lang ja`                                                                  |
| `--source-lang`, `-sl`          | Source language code (optional)                                                         | `pdf2zh_next --input ./example.pdf --target-lang ja --source-lang en`                                                 |
| `--translator`, `-t`            | Translation service, default: `google`                                                  | `pdf2zh_next --input ./example.pdf --translator google`                                                               |
| `--translator-config`, `-tc`    | Translation service configuration, in JSON format                                       | `pdf2zh_next --input ./example.pdf --translator-config '{"api_key": "your_api_key"}'`                                 |
| `--translator-args`, `-ta`      | Translation service additional arguments, in JSON format                                | `pdf2zh_next --input ./example.pdf --translator-args '{"timeout": 10}'`                                               |
| `--ocr`, `-ocr`                 | Enable OCR for image-based PDFs                                                         | `pdf2zh_next --input ./example.pdf --ocr`                                                                             |
| `--ocr-config`, `-oc`           | OCR configuration, in JSON format                                                       | `pdf2zh_next --input ./example.pdf --ocr-config '{"lang": "eng+chi_sim"}'`                                            |
| `--concurrency`, `-c`           | Number of concurrent translation tasks, default: 4                                      | `pdf2zh_next --input ./example.pdf --concurrency 8`                                                                   |
| `--timeout`, `-to`              | Translation timeout in seconds, default: 30                                             | `pdf2zh_next --input ./example.pdf --timeout 60`                                                                      |
| `--retry`, `-r`                 | Number of retries for failed translations, default: 3                                   | `pdf2zh_next --input ./example.pdf --retry 5`                                                                         |
| `--log-level`, `-ll`            | Log level: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, default: `INFO`             | `pdf2zh_next --input ./example.pdf --log-level DEBUG`                                                                 |
| `--log-file`, `-lf`             | Log file path                                                                           | `pdf2zh_next --input ./example.pdf --log-file ./translation.log`                                                      |
| `--config`, `-cfg`              | Configuration file path                                                                 | `pdf2zh_next --config ./config.json`                                                                                  |
| `--dry-run`, `-dr`              | Perform a dry run without actual translation                                            | `pdf2zh_next --input ./example.pdf --dry-run`                                                                         |
| `--force`, `-f`                 | Force overwrite output file if it exists                                                | `pdf2zh_next --input ./example.pdf --output ./example_translated.pdf --force`                                         |
| `--no-backup`, `-nb`            | Do not create backup of original PDF                                                    | `pdf2zh_next --input ./example.pdf --no-backup`                                                                       |
| `--page-range`, `-pr`           | Page range to translate (e.g., "1-5,8,10-15")                                           | `pdf2zh_next --input ./example.pdf --page-range "1-5"`                                                                |
| `--exclude-pages`, `-ep`        | Pages to exclude from translation (e.g., "1,3,5")                                       | `pdf2zh_next --input ./example.pdf --exclude-pages "1,3,5"`                                                           |
| `--only-text`, `-ot`            | Only translate text, skip equations and tables                                          | `pdf2zh_next --input ./example.pdf --only-text`                                                                       |
| `--no-equations`, `-ne`         | Skip translation of equations                                                           | `pdf2zh_next --input ./example.pdf --no-equations`                                                                    |
| `--no-tables`, `-nt`            | Skip translation of tables                                                              | `pdf2zh_next --input ./example.pdf --no-tables`                                                                       |
| `--font`, `-font`               | Font to use for translated text                                                         | `pdf2zh_next --input ./example.pdf --font "Noto Sans CJK SC"`                                                         |
| `--font-size`, `-fs`            | Font size for translated text                                                           | `pdf2zh_next --input ./example.pdf --font-size 12`                                                                    |
| `--color`, `-color`             | Color for translated text                                                               | `pdf2zh_next --input ./example.pdf --color "#333333"`                                                                 |
| `--line-spacing`, `-ls`         | Line spacing for translated text                                                        | `pdf2zh_next --input ./example.pdf --line-spacing 1.5`                                                                |
| `--margin`, `-margin`           | Margin around translated text                                                           | `pdf2zh_next --input ./example.pdf --margin 10`                                                                       |
| `--align`, `-align`             | Text alignment: `left`, `center`, `right`, `justify`, default: `left`                   | `pdf2zh_next --input ./example.pdf --align justify`                                                                   |
| `--position`, `-pos`            | Text position: `original`, `above`, `below`, `left`, `right`, default: `original`       | `pdf2zh_next --input ./example.pdf --position below`                                                                  |
| `--opacity`, `-op`              | Opacity of translated text (0-100), default: 100                                        | `pdf2zh_next --input ./example.pdf --opacity 80`                                                                      |
| `--background`, `-bg`           | Background color for translated text                                                    | `pdf2zh_next --input ./example.pdf --background "#FFFF00"`                                                            |
| `--border`, `-border`           | Border around translated text                                                           | `pdf2zh_next --input ./example.pdf --border "1px solid #000000"`                                                      |
| `--border-radius`, `-br`        | Border radius for translated text boxes                                                 | `pdf2zh_next --input ./example.pdf --border-radius 5`                                                                 |
| `--shadow`, `-shadow`           | Shadow for translated text boxes                                                        | `pdf2zh_next --input ./example.pdf --shadow "2px 2px 5px rgba(0,0,0,0.3)"`                                           |
| `--rotate`, `-rotate`           | Rotate translated text (degrees)                                                        | `pdf2zh_next --input ./example.pdf --rotate 5`                                                                        |
| `--scale`, `-scale`             | Scale translated text                                                                   | `pdf2zh_next --input ./example.pdf --scale 1.2`                                                                       |
| `--custom-css`, `-css`          | Custom CSS for translated text                                                          | `pdf2zh_next --input ./example.pdf --custom-css "font-weight: bold; text-decoration: underline;"`                     |
| `--preserve-formatting`, `-pf`  | Preserve original formatting as much as possible                                        | `pdf2zh_next --input ./example.pdf --preserve-formatting`                                                             |
| `--min-confidence`, `-mc`       | Minimum confidence threshold for OCR (0-100), default: 80                               | `pdf2zh_next --input ./example.pdf --min-confidence 90`                                                               |
| `--dpi`, `-dpi`                 | DPI for OCR processing, default: 300                                                    | `pdf2zh_next --input ./example.pdf --dpi 600`                                                                         |
| `--preprocess`, `-pp`           | Preprocess images before OCR                                                            | `pdf2zh_next --input ./example.pdf --preprocess`                                                                      |
| `--preprocess-config`, `-pc`    | Preprocessing configuration, in JSON format                                             | `pdf2zh_next --input ./example.pdf --preprocess-config '{"denoise": true, "deskew": true}'`                           |
| `--postprocess`, `-pop`         | Postprocess translated text                                                             | `pdf2zh_next --input ./example.pdf --postprocess`                                                                     |
| `--postprocess-config`, `-poc`  | Postprocessing configuration, in JSON format                                            | `pdf2zh_next --input ./example.pdf --postprocess-config '{"fix_punctuation": true, "fix_spaces": true}'`              |
| `--glossary`, `-gl`             | Glossary file path for custom translations                                              | `pdf2zh_next --input ./example.pdf --glossary ./glossary.txt`                                                         |
| `--glossary-mode`, `-gm`        | Glossary mode: `prefer`, `only`, `avoid`, default: `prefer`                             | `pdf2zh_next --input ./example.pdf --glossary-mode only`                                                              |
| `--cache`, `-cache`             | Enable translation cache                                                                | `pdf2zh_next --input ./example.pdf --cache`                                                                           |
| `--cache-dir`, `-cd`            | Cache directory path                                                                    | `pdf2zh_next --input ./example.pdf --cache-dir ./cache`                                                               |
| `--cache-ttl`, `-ct`            | Cache time-to-live in seconds, default: 2592000 (30 days)                               | `pdf2zh_next --input ./example.pdf --cache-ttl 604800`                                                                |
| `--no-cache`, `-nc`             | Disable translation cache                                                               | `pdf2zh_next --input ./example.pdf --no-cache`                                                                        |
| `--clean-cache`, `-cc`          | Clean translation cache                                                                 | `pdf2zh_next --clean-cache`                                                                                           |
| `--list-translators`, `-lt`     | List available translation services                                                     | `pdf2zh_next --list-translators`                                                                                      |
| `--list-languages`, `-llang`    | List supported languages                                                                | `pdf2zh_next --list-languages`                                                                                        |
| `--list-fonts`, `-lf`           | List available fonts                                                                    | `pdf2zh_next --list-fonts`                                                                                            |
| `--check-update`, `-cu`         | Check for updates                                                                       | `pdf2zh_next --check-update`                                                                                          |
| `--update`, `-u`                | Update to the latest version                                                            | `pdf2zh_next --update`                                                                                                |
| `--verbose`, `-vb`              | Verbose output                                                                          | `pdf2zh_next --input ./example.pdf --verbose`                                                                         |
| `--quiet`, `-q`                 | Quiet mode, only show errors                                                            | `pdf2zh_next --input ./example.pdf --quiet`                                                                           |
| `--yes`, `-y`                   | Answer yes to all prompts                                                               | `pdf2zh_next --input ./example.pdf --yes`                                                                             |
| `--no`, `-n`                    | Answer no to all prompts                                                                | `pdf2zh_next --input ./example.pdf --no`                                                                              |
| `--progress`, `-p`              | Show progress bar                                                                       | `pdf2zh_next --input ./example.pdf --progress`                                                                        |
| `--no-progress`, `-np`          | Hide progress bar                                                                       | `pdf2zh_next --input ./example.pdf --no-progress`                                                                     |
| `--stats`, `-stats`             | Show translation statistics                                                             | `pdf2zh_next --input ./example.pdf --stats`                                                                           |
| `--debug`, `-dbg`               | Enable debug mode                                                                       | `pdf2zh_next --input ./example.pdf --debug`                                                                           |
| `--profile`, `-prof`            | Enable profiling                                                                        | `pdf2zh_next --input ./example.pdf --profile`                                                                         |
| `--profile-output`, `-po`       | Profile output file path                                                                | `pdf2zh_next --input ./example.pdf --profile-output ./profile.txt`                                                    |
| `--benchmark`, `-bm`            | Run benchmark tests                                                                     | `pdf2zh_next --benchmark`                                                                                             |
| `--test`, `-test`               | Run tests                                                                               | `pdf2zh_next --test`                                                                                                  |
| `--validate`, `-val`            | Validate configuration                                                                  | `pdf2zh_next --validate`                                                                                              |
| `--init`, `-init`               | Initialize configuration file                                                           | `pdf2zh_next --init`                                                                                                  |
| `--reset`, `-reset`             | Reset configuration to defaults                                                         | `pdf2zh_next --reset`                                                                                                 |
| `--env`, `-env`                 | Environment variables file path                                                         | `pdf2zh_next --env .env`                                                                                              |
| `--docker`, `-docker`           | Run in Docker container                                                                 | `pdf2zh_next --docker`                                                                                                |
| `--docker-image`, `-di`         | Docker image name                                                                       | `pdf2zh_next --docker-image pdf2zh-next`                                                                              |
| `--docker-args`, `-da`          | Docker additional arguments                                                             | `pdf2zh_next --docker-args "--rm -v $(pwd):/app"`                                                                     |
| `--api`, `-api`                 | Start API server                                                                        | `pdf2zh_next --api`                                                                                                   |
| `--api-host`, `-ah`             | API server host, default: `127.0.0.1`                                                   | `pdf2zh_next --api --api-host 0.0.0.0`                                                                                |
| `--api-port`, `-ap`             | API server port, default: `8000`                                                        | `pdf2zh_next --api --api-port 8080`                                                                                   |
| `--api-workers`, `-aw`          | API server workers, default: `4`                                                        | `pdf2zh_next --api --api-workers 8`                                                                                   |
| `--api-docs`, `-ad`             | Enable API documentation                                                                | `pdf2zh_next --api --api-docs`                                                                                        |
| `--api-reload`, `-ar`           | Enable API auto-reload                                                                  | `pdf2zh_next --api --api-reload`                                                                                      |
| `--webui`, `-webui`             | Start WebUI server                                                                      | `pdf2zh_next --webui`                                                                                                 |
| `--webui-host`, `-wh`           | WebUI server host, default: `127.0.0.1`                                                 | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                            |
| `--webui-port`, `-wp`           | WebUI server port, default: `8000`                                                      | `pdf2zh_next --webui --webui-port 8080`                                                                               |
| `--webui-workers`, `-ww`        | WebUI server workers, default: `4`                                                      | `pdf2zh_next --webui --webui-workers 8`                                                                               |
| `--webui-reload`, `-wr`         | Enable WebUI auto-reload                                                                | `pdf2zh_next --webui --webui-reload`                                                                                  |
| `--webui-theme`, `-wt`          | WebUI theme: `light`, `dark`, `auto`, default: `auto`                                   | `pdf2zh_next --webui --webui-theme dark`                                                                              |
| `--webui-lang`, `-wl`           | WebUI language code                                                                     | `pdf2zh_next --webui --webui-lang ja`                                                                                 |
| `--batch`, `-batch`             | Batch process multiple PDF files                                                        | `pdf2zh_next --batch ./pdfs/*.pdf`                                                                                    |
| `--batch-input-dir`, `-bid`     | Batch input directory                                                                   | `pdf2zh_next --batch-input-dir ./pdfs`                                                                                |
| `--batch-output-dir`, `-bod`    | Batch output directory                                                                  | `pdf2zh_next --batch-input-dir ./pdfs --batch-output-dir ./translated`                                                |
| `--batch-pattern`, `-bp`        | Batch file pattern                                                                      | `pdf2zh_next --batch-input-dir ./pdfs --batch-pattern "*.pdf"`                                                        |
| `--batch-recursive`, `-br`      | Process batch recursively                                                               | `pdf2zh_next --batch-input-dir ./pdfs --batch-recursive`                                                              |
| `--batch-concurrency`, `-bc`    | Batch concurrency level, default: 2                                                     | `pdf2zh_next --batch-input-dir ./pdfs --batch-concurrency 4`                                                          |
| `--batch-timeout`, `-bt`        | Batch timeout per file in seconds, default: 300                                         | `pdf2zh_next --batch-input-dir ./pdfs --batch-timeout 600`                                                            |
| `--batch-retry`, `-bret`        | Batch retries per file, default: 2                                                      | `pdf2zh_next --batch-input-dir ./pdfs --batch-retry 3`                                                                |
| `--batch-skip-existing`, `-bse` | Skip existing files in batch processing                                                 | `pdf2zh_next --batch-input-dir ./pdfs --batch-skip-existing`                                                          |
| `--batch-overwrite`, `-bo`      | Overwrite existing files in batch processing                                            | `pdf2zh_next --batch-input-dir ./pdfs --batch-overwrite`                                                              |
| `--batch-rename`, `-brn`        | Rename pattern for batch output                                                         | `pdf2zh_next --batch-input-dir ./pdfs --batch-rename "{name}_translated.{ext}"`                                       |
| `--batch-report`, `-brep`       | Generate batch report                                                                   | `pdf2zh_next --batch-input-dir ./pdfs --batch-report`                                                                 |
| `--batch-report-format`, `-brf` | Batch report format: `json`, `csv`, `txt`, `html`, default: `json`                      | `pdf2zh_next --batch-input-dir ./pdfs --batch-report-format csv`                                                      |
| `--batch-report-output`, `-bro` | Batch report output file path                                                           | `pdf2zh_next --batch-input-dir ./pdfs --batch-report-output ./batch_report.json`                                      |
| `--watch`, `-watch`             | Watch directory for new PDF files                                                       | `pdf2zh_next --watch ./pdfs`                                                                                          |
| `--watch-interval`, `-wi`       | Watch interval in seconds, default: 60                                                  | `pdf2zh_next --watch ./pdfs --watch-interval 30`                                                                      |
| `--watch-recursive`, `-wr`      | Watch recursively                                                                       | `pdf2zh_next --watch ./pdfs --watch-recursive`                                                                        |
| `--watch-pattern`, `-wp`        | Watch file pattern                                                                      | `pdf2zh_next --watch ./pdfs --watch-pattern "*.pdf"`                                                                  |
| `--watch-command`, `-wc`        | Command to execute when new file is detected                                            | `pdf2zh_next --watch ./pdfs --watch-command "echo New file: {file}"`                                                  |
| `--watch-output-dir`, `-wod`    | Watch output directory                                                                  | `pdf2zh_next --watch ./pdfs --watch-output-dir ./translated`                                                          |
| `--watch-overwrite`, `-wo`      | Overwrite existing files in watch mode                                                  | `pdf2zh_next --watch ./pdfs --watch-overwrite`                                                                        |
| `--watch-rename`, `-wrn`        | Rename pattern for watch output                                                         | `pdf2zh_next --watch ./pdfs --watch-rename "{name}_translated.{ext}"`                                                 |
| `--daemon`, `-d`                | Run as daemon                                                                           | `pdf2zh_next --daemon`                                                                                                |
| `--pid`, `-pid`                 | PID file path                                                                           | `pdf2zh_next --daemon --pid ./pdf2zh.pid`                                                                             |
| `--log`, `-log`                 | Log file path for daemon mode                                                           | `pdf2zh_next --daemon --log ./pdf2zh.log`                                                                             |
| `--stop`, `-stop`               | Stop daemon                                                                             | `pdf2zh_next --stop`                                                                                                  |
| `--restart`, `-restart`         | Restart daemon                                                                          | `pdf2zh_next --restart`                                                                                               |
| `--status`, `-status`           | Check daemon status                                                                     | `pdf2zh_next --status`                                                                                                |
| `--user`, `-user`               | User to run daemon as                                                                   | `pdf2zh_next --daemon --user nobody`                                                                                  |
| `--group`, `-group`             | Group to run daemon as                                                                  | `pdf2zh_next --daemon --group nogroup`                                                                                |
| `--umask`, `-umask`             | Umask for daemon                                                                        | `pdf2zh_next --daemon --umask 022`                                                                                    |
| `--chdir`, `-chdir`             | Change directory for daemon                                                             | `pdf2zh_next --daemon --chdir /var/lib/pdf2zh`                                                                        |
| `--no-chdir`, `-ncd`            | Do not change directory for daemon                                                      | `pdf2zh_next --daemon --no-chdir`                                                                                     |
| `--no-close`, `-ncl`            | Do not close file descriptors for daemon                                                | `pdf2zh_next --daemon --no-close`                                                                                     |
| `--no-umask`, `-num`            | Do not set umask for daemon                                                             | `pdf2zh_next --daemon --no-umask`                                                                                     |
| `--no-setsid`, `-nsd`            | Do not call setsid() for daemon                                                         | `pdf2zh_next --daemon --no-setsid`                                                                                    |
| `--help-all`, `-ha`             | Show all help including advanced options                                                | `pdf2zh_next --help-all`                                                                                              |
| `--help-short`, `-hs`           | Show short help                                                                         | `pdf2zh_next --help-short`                                                                                            |
| `--help-json`, `-hj`            | Show help in JSON format                                                                | `pdf2zh_next --help-json`                                                                                             |
| `--help-md`, `-hmd`             | Show help in Markdown format                                                            | `pdf2zh_next --help-md`                                                                                               |
| `--help-man`, `-hman`           | Show help in man page format                                                            | `pdf2zh_next --help-man`                                                                                              |
| `--help-rst`, `-hrst`           | Show help in reStructuredText format                                                    | `pdf2zh_next --help-rst`                                                                                              |
| `--help-xml`, `-hxml`           | Show help in XML format                                                                 | `pdf2zh_next --help-xml`                                                                                              |
| `--help-yaml`, `-hyaml`         | Show help in YAML format                                                                | `pdf2zh_next --help-yaml`                                                                                             |
| `--help-html`, `-hhtml`         | Show help in HTML format                                                                | `pdf2zh_next --help-html`                                                                                             |
| `--help-text`, `-htxt`          | Show help in plain text format                                                          | `pdf2zh_next --help-text`                                                                                             |
| `--help-usage`, `-hu`           | Show usage examples                                                                     | `pdf2zh_next --help-usage`                                                                                            |
| `--help-verbose`, `-hv`         | Show verbose help                                                                       | `pdf2zh_next --help-verbose`                                                                                          |
| `--help-debug`, `-hdbg`         | Show debug help                                                                         | `pdf2zh_next --help-debug`                                                                                            |
| `--help-api`, `-hapi`           | Show API help                                                                           | `pdf2zh_next --help-api`                                                                                              |
| `--help-webui`, `-hwebui`       | Show WebUI help                                                                         | `pdf2zh_next --help-webui`                                                                                            |
| `--help-batch`, `-hbatch`       | Show batch help                                                                         | `pdf2zh_next --help-batch`                                                                                            |
| `--help-watch`, `-hwatch`       | Show watch help                                                                         |极速 pdf2zh_next --help-watch`                                                                                          |
| `--help-daemon`, `-hdaemon`     | Show daemon help                                                                        | `pdf2zh_next --help-daemon`                                                                                           |
| `--help-config`, `-hcfg`        | Show configuration help                                                                 | `极速 pdf2zh_next --help-config`                                                                                       |
| `--help-translator`, `-ht`      | Show translator help                                                                    | `pdf2zh_next --help-translator`                                                                                       |
| `--help-ocr`, `-hocr`           | Show OCR help                                                                           | `pdf2zh_next --help-ocr`                                                                                              |
| `--help-font`, `-hfont`         | Show font help                                                                          | `pdf2 极速 zh_next --help-font`                                                                                         |
| `--help-style`, `-hstyle`       | Show style help                                                                         | `pdf2zh_next --help-style`                                                                                            |
| `--help-cache`, `-hcache`       | Show cache help                                                                         | `pdf2zh_next --help-cache`                                                                                            |
| `--help-glossary`, `-hgl`       | Show glossary help                                                                      | `pdf2zh_next --help-glossary`                                                                                         |
| `--help-preprocess`, `-hpp`     | Show preprocessing help                                                                 | `pdf2zh_next --help-preprocess`                                                                                       |
| `--help-postprocess`, `-hpop`   | Show postprocessing help                                                                | `pdf2zh_next --help-postprocess`                                                                                      |
| `--help-benchmark`, `-hbm`      | Show benchmark help                                                                     | `pdf2zh_next --极速 help-benchmark`                                                                                    |
| `--help-test`, `-htest`         | Show test help                                                                          | `pdf2zh_next --help-test`                                                                                             |
| `--help-profile`, `-hprof`      | Show profile help                                                                       | `pdf2zh_next --help-profile`                                                                                          |
| `--help-docker`, `-hdocker`     | Show Docker help                                                                        | `pdf2zh_next --help-docker`                                                                                           |
| `--help-env`, `-henv`           | Show environment help                                                                   | `pdf2zh_next --help-env`                                                                                              |
| `--help-version`, `-hver`       | Show version help                                                                       | `pdf2zh_next --help-version`                                                                                          |
| `--help-license`, `-hlic`       | Show license help                                                                       | `pdf2zh_next --help-license`                                                                                          |
| `--help-contrib`, `-hcontrib`   | Show contribution help                                                                  | `pdf2zh_next --help-contrib`                                                                                          |
| `--help-community`, `-hcomm`    | Show community help                                                                     | `pdf2zh_next --help-community`                                                                                        |
| `--help-faq`, `-hfaq`           | Show FAQ help                                                                           | `pdf2zh_next --help-faq`                                                                                              |
| `--help-troubleshoot`, `-hts`   | Show troubleshooting help                                                               | `pdf2zh_next --help-troubleshoot`                                                                                     |
| `--help-security`, `-hsec`      | Show security help                                                                      | `pdf2zh_next --help-security`                                                                                         |
| `--help-privacy`, `-hpriv`      | Show privacy help                                                                       | `pdf2zh_next --help-privacy`                                                                                          |
| `--help-performance`, `-hperf`  | Show performance help                                                                   | `pdf2zh_next --help-performance`                                                                                      |
| `--help-compatibility`, `-hcomp` | Show compatibility help                                                                 | `pdf2zh_next --help-compatibility`                                                                                    |
| `--help-limitations`, `-hlim`   | Show limitations help                                                                   | `pdf2zh_next --help-limitations`                                                                                      |
| `--help-known-issues`, `-hki`   | Show known issues help                                                                  | `pdf2zh_next --help-known-issues`                                                                                     |
| `--help-changelog`, `-hcl`      | Show changelog help                                                                     | `pdf2zh_next --help-changelog`                                                                                        |
| `--help-roadmap`, `-hroad`      | Show roadmap help                                                                极速                                                                 | `pdf2zh_next --help-roadmap`                                                                                          |
| `--help-support`, `-hsupp`      | Show support help                                                                       | `pdf2zh_next --help-support`                                                                                          |
| `--help-donate`, `-hdon`        | Show donate help                                                                        | `pdf2zh_next --help-donate`                                                                                           |
| `--help-contact`, `-hcont`      | Show contact help                                                                       | `pdf2zh_next --help-contact`                                                                                          |
| `--help-about`, `-habout`       | Show about help                                                                         | `pdf2zh_next --help-about`                                                                                            |

---

### OUTPUT

| `--help`, `-h`                  | ヘルプメッセージを表示して終了                                                              | `pdf2zh_next -h`                                                                                                      |
| :------------------------------ | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | バージョンを表示して終了                                                                   | `pdf2zh_next -极速 v`                                                                                                      |
| `--input`, `-i`                 | 入力 PDF ファイルパス                                                                     | `pdf2zh_next --input ./example.pdf`                                                                                   |
| `--output`, `-o`                | 出力 PDF ファイルパス                                                                    | `pdf2zh_next --input ./example.pdf --output ./example_translated.pdf`                                                 |
| `--target-lang`, `-tl`          | ターゲット言語コード                                                                    | `pdf2zh_next --input ./example.pdf --target-lang ja`                                                                  |
| `--source-lang`, `-极速 sl`          | ソース言語コード（オプション）                                                         | `pdf2zh_next --input ./example.pdf --target-lang ja --source-lang en`                                                 |
| `--translator`, `-t`            | 翻訳サービス、デフォルト：`google`                                                  | `pdf2zh_next --input ./example.pdf --translator google`                                                               |
| `--translator-config`, `-tc`    | 翻訳サービス設定、JSON 形式                                       | `pdf2zh_next --input ./example.pdf --translator-config '{"api_key": "your_api_key"}'`                                 |
| `--translator-args`, `-ta`      | 翻訳サービス追加引数、JSON 形式                                | `pdf2zh_next --input ./example.pdf --translator-args '{"timeout": 10}'`                                               |
| `--ocr`, `-ocr`                 | 画像ベース PDF の OCR を有効化                                                         | `pdf2zh_next --input ./example.pdf --ocr`                                                                             |
| `--ocr-config`, `-oc`           | OCR 設定、JSON 形式                                                       | `pdf2zh_next --input ./example.pdf --ocr-config '{"lang": "eng+chi_sim"}'`                                            |
| `--concurrency`, `-c`           | 並列翻訳タスク数、デフォルト：4                                      | `pdf2zh_next --input ./example.pdf --concurrency 8`                                                                   |
| `--timeout`, `-to`              | 翻訳タイムアウト（秒）、デフォルト：30                                             | `pdf2zh_next --input ./example.pdf --timeout 60`                                                                      |
| `--retry`, `-r`                 | 失敗した翻訳の再試行回数、デフォルト：3                                   | `pdf2zh_next --input ./example.pdf --retry 5`                                                                         |
| `--log-level`, `-ll`            | ログレベル：`DEBUG`、`INFO`、`WARNING`、`ERROR`、`CRITICAL`、デフォルト：`INFO`             | `pdf2zh_next --input ./example.pdf --log-level DEBUG`                                                                 |
| `--log-file`, `-lf`             | ログファイルパス                                                                           | `pdf2zh_next --input ./example.pdf --极速 log-file ./translation.log`                                                      |
| `--config`, `-cfg`              | 設定ファイルパス                                                                 | `pdf2zh_next --config ./config.json`                                                                                  |
| `极速--dry-run`, `-dr`              | 実際の翻訳を行わないドライランを実行                                            | `pdf2zh_next --input ./example.pdf --dry-run`                                                                         |
| `--force`, `-f`                 | 出力ファイルが存在する場合に強制上書き                                                | `pdf2zh_next --input ./example.pdf --output ./example_translated.pdf --force`                                         |
| `--no-backup`, `-nb`            | 元の PDF のバックアップを作成しない                                                    | `pdf2zh_next --input ./example.pdf --no-backup`                                                                       |
| `--page-range`, `-pr`           | 翻訳するページ範囲（例："1-5,8,10-15"）                                           | `pdf2zh_next --input ./example.pdf --page-range "1-5"`                                                                |
| `--exclude-pages`, `-ep`        | 翻訳から除外するページ（例："1,3,5"）                                       | `pdf2zh_next --input ./example.pdf --exclude-pages "1,3,5"`                                                           |
| `--only-text`, `-ot`            | テキストのみ翻訳、数式と表をスキップ                                          | `pdf2zh_next --input ./example.pdf --only-text`                                                                       |
| `--no-equations`, `-ne`         | 数式の翻訳をスキップ                                                           | `pdf2zh_next --input ./example.pdf --no-equations`                                                                    |
| `--no-tables`, `-nt`            | 表の翻訳をスキップ                                                              | `pdf2zh_next --input ./example.pdf --no-tables`                                                                       |
| `--font`, `-font`               | 翻訳テキストに使用するフォント                                                         | `pdf2zh_next --input ./example.pdf --font "Noto Sans CJK SC"`                                                         |
| `--font-size`, `-fs`            | 翻訳テキストのフォントサイズ                                                           | `pdf2zh_next --input ./example.pdf --font-size 12`                                                                    |
| `--color`, `-color`             | 翻訳テキストの色                                                               | `pdf2zh_next --input ./example.pdf --color "#333333"`                                                                 |
| `--line-spacing`, `-ls`         | 翻訳テキストの行間                                                        | `pdf 极速 2zh_next --input ./example.pdf --line-spacing 1.5`                                                                |
| `--margin`, `-margin`           | 翻訳テキスト周囲の余白                                                           | `pdf2zh_next --input ./example.pdf --margin 10`                                                                       |
| `--align`, `-align`             | テキスト配置：`left`、`center`、`right`、`justify`、デフォルト：`left`                   | `pdf2zh_next --input ./example.pdf --align justify`                                                                   |
| `--position`, `-pos`            | テキスト位置：`original`、`above`、`below`、`left`、`right`、デフォルト：`original`       | `pdf2zh_next --input ./example.pdf --position below`                                                                  |
| `--opacity`, `-op`              | 翻訳テキストの不透明度（0-100）、デフォルト：100                                        | `pdf2zh_next --input ./example.pdf --opacity 80`                                                                      |
| `--background`, `-bg`           | 翻訳テキストの背景色                                                    | `pdf2zh_next --input ./example.pdf --background "#FFFF00"`                                                            |
| `--border`, `-border`           | 翻訳テキスト周囲のボーダー                                                           | `pdf2zh_next --input ./example.pdf --border "1px solid #000000"`                                                      |
| `--border-radius`, `-br`        | 翻訳テキストボックスのボーダー半径                                                 | `pdf2zh_next --input ./example.pdf --border-radius 5`                                                                 |
| `--shadow`, `-shadow`           | 翻訳テキストボックスのシャドウ                                                        | `pdf2zh_next --input ./example.pdf --shadow "2px 2px 5px rgba(0,0,0,0.3)"`                                           |
| `--rotate`, `-rotate`           | 翻訳テキストの回転（度）                                                        | `pdf2zh_next --input ./example.pdf --rotate 5`                                                                        |
| `--scale`, `-scale`             | 翻訳テキストのスケール                                                                   | `pdf2zh_next --input ./example.pdf --scale 1.极速 2`                                                                       |
| `--custom-css`, `-css`          | 翻訳テキストのカスタム CSS                                                          | `pdf2zh 极速_next --input ./example.pdf --custom-css "font-weight: bold; text-decoration: underline;"`                     |
| `--preserve-formatting`, `-极速 pf`  | 元のフォーマットを可能な限り保持                                        | `pdf2zh_next --input ./example.pdf --preserve-formatting`                                                             |
| `--min-confidence`, `-mc`       | OCR の最小信頼度閾値（0-100）、デフォルト：80                               | `pdf2zh_next --input ./example.pdf --min-confidence 90`                                                               |
| `--dpi`, `-d 极速 pi`                 | OCR 処理の DPI、デフォルト：300                                                    | `pdf2zh_next --input ./example.pdf --dpi 600`                                                                         |
| `--preprocess`, `-pp`           | OCR 前に画像を前処理                                                            | `pdf2zh_next --input ./example.pdf --preprocess`                                                                      |
| `--preprocess-config`, `-pc`    | 前処理設定、JSON 格式                                             | `pdf2zh_next --input ./example.pdf --preprocess-config '{"denoise": true, "deskew": true}'`                           |
| `--postprocess`, `-pop`         | 翻訳テキストを後処理                                                             | `pdf2zh_next --input ./example.pdf --postprocess`                                                                     |
| `--postprocess-config`, `-poc`  | 後処理設定、JSON 格式                                            | `pdf2zh_next --input ./example.pdf --postprocess-config '{"fix_punctuation": true, "fix_spaces": true}'`              |
| `--glossary`, `-gl`             | カスタム翻訳用の用語集ファイルパス                                              | `pdf2zh_next --input ./example.pdf --glossary ./glossary.txt`                                                         |
| `--glossary-mode`, `-gm`        | 用語集モード：`prefer`、`only`、`avoid`、デフォルト：`prefer`                             | `pdf2zh_next --input ./example.pdf --glossary-mode only`                                                              |
| `--cache`, `-cache`             | 翻訳キャッシュを有効化                                                                | `pdf2zh_next --input ./example.pdf --cache`                                                                           |
| `--cache-dir`, `-cd`            | キャッシュディレクトリパス                                                                    | `pdf2zh_next --input ./example.pdf --cache-dir ./cache`                                                               |
| `--cache-ttl`, `-ct`            | キャッシュの有効期限（秒）、デフォルト：2592000（30 日）                               | `pdf2zh_next --input ./example.pdf --cache-tt 极速 l 604800`                                                                |
| `--no-cache`, `-nc`             | 翻訳キャッシュを無効化                                                               | `pdf2zh_next --input ./example.pdf --no-cache`                                                                        |
| `--clean-cache`, `-cc`          | 翻訳キャッシュをクリーン                                                                 | `pdf2zh_next --clean-cache`                                                                                           |
| `--list-translators`, `-lt`     | 利用可能な翻訳サービスを一覧表示                                                     | `pdf2zh_next --list-translators`                                                                                      |
| `--list-languages`, `-llang`    | サポート言語を一覧表示                                                                | `pdf2zh_next --list-languages`                                                                                        |
| `--list-fonts`, `-lf`           | 利用可能なフォントを一覧表示                                                                    | `pdf2zh_next --list-fonts`                                                                                            |
| `--check-update`, `-cu`         | アップデートをチェック                                                                       | `pdf2zh_next --check-update`                                                                                          |
| `--update`, `-u`                | 最新バージョンにアップデート                                                            | `pdf2zh_next --update`                                                                                                |
| `--verbose`, `-vb`              | 詳細出力                                                                          | `pdf2zh_next --input ./example.pdf --verbose`                                                                         |
| `--quiet`, `-q`                 | サイレントモード、エラーのみ表示                                                            | `pdf2zh_next --input ./example.pdf --quiet`                                                                           |
| `--yes`, `-y`                   | すべてのプロンプトに「はい」と回答                                                               | `pdf2zh_next --input ./example.pdf --yes`                                                                             |
| `--no`, `-n`                    | すべてのプロンプトに「いいえ」と回答                                                                | `pdf2zh_next --input ./example.pdf --no`                                                                              |
| `--progress`, `-p`              | プログレスバーを表示                                                                       | `pdf2zh_next --input ./example.pdf --progress`                                                                        |
| `--no-progress`, `-np`          | プログレスバーを非表示                                                                       | `pdf2zh_next --input ./example.pdf --no-progress`                                                                     |
| `--stats`, `-stats`             | 翻訳統計を表示                                                             | `pdf2zh_next --input ./example.pdf --stats`                                                                           |
| `--debug`, `-dbg`               | デバッグモードを有効化                                                                       | `pdf2zh_next --input ./example.pdf --debug`                                                                           |
| `--profile`, `-prof`            | プロファイリングを有効化                                                                        | `pdf2zh_next --input ./example.pdf --profile`                                                                         |
| `--profile-output`, `-po`       | プロファイル出力ファイルパス                                                                | `pdf2zh_next --input ./example.pdf --profile-output ./profile.txt`                                                    |
| `--benchmark`, `-bm`            | ベンチマークテストを実行                                                                     | `pdf2zh_next --benchmark`                                                                                             |
| `--test`, `-test`               | テストを実行                                                                               | `pdf2zh_next --test`                                                                                                  |
| `--validate`, `-val`            | 設定を検証                                                                  | `pdf2zh_next --validate`                                                                                              |
| `--init`, `-init`               | 設定ファイルを初期化                                                           | `pdf2zh_next --极速 init`                                                                                                  |
| `--reset`, `-reset`             | 設定をデフォルトにリセット                                                         | `pdf2zh_next --reset`                                                                                                 |
| `--env`, `-env`                 | 環境変数ファイルパス                                                         | `pdf2zh_next --env .env`                                                                                              |
| `--docker`, `-docker`           | Docker コンテナで実行                                                                 | `pdf2zh_next --docker`                                                                                                |
| `--docker-image`, `-di`         | Docker イメージ名                                                                       | `pdf2zh_next --docker-image pdf2zh-next`                                                                              |
| `--docker-args`, `-da`          | Docker 追加引数                                                             | `pdf2zh_next --docker-args "--rm -v $(pwd):/app"`                                                                     |
| `--api`, `-api`                 | API サーバーを起動                                                                        | `pdf2zh_next --api`                                                                                                   |
| `--api-host`, `-ah`             | API サーバーホスト、デフォルト：`127.0.0.1`                                                   | `pdf2zh_next --api --api-host 0.0.0.0`                                                                                |
| `--api-port`, `-ap`             | API サーバーポート、デフォルト：`8000`                                                        | `pdf2zh_next --api --api-port 8080`                                                                                   |
| `--api-workers`, `-aw`          | API サーバーワーカー数、デフォルト：`4`                                                        | `pdf2zh_next --api --api-workers 8`                                                                                   |
| `--api-docs`, `-ad`             | API ドキュメントを有効化                                                                | `pdf2zh_next --api --api-docs 极速`                                                                                        |
| `--api-reload`, `-ar`           | API 自動リロードを有効化                                                                  | `pdf2zh_next --api --api-reload`                                                                                      |
| `--webui`, `-webui`             | WebUI サーバーを起動                                                                      | `pdf2zh_next --webui`                                                                                                 |
| `--webui-host`, `-wh`           | WebUI サーバーホスト、デフォルト：`127.0.0.1`                                                 | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                            |
| `--webui-port`, `-wp`           | WebUI サーバーポート、デフォルト：`8000`                                                      | `pdf2zh_next --webui --webui-port 8080`                                                                               |
| `--webui-workers`, `-ww`        | WebUI サーバーワーカー数、デフォルト：`4`                                                      | `pdf2zh_next --webui --webui-workers 8`                                                                               |
| `--web 极速 ui-reload`, `-wr`         | WebUI 自動リロードを有効化                                                                | `pdf2zh_next --webui --webui-reload`                                                                                  |
| `--webui-theme`, `-wt`          | WebUI テーマ：`light`、`dark`、`auto`、デフォルト：`auto`                                   | `pdf2zh_next --webui --webui-theme dark`                                                                              |
| `--webui-lang`, `-wl`           | WebUI 言語コード                                                                     | `pdf2zh_next --webui --webui-lang ja`                                                                                 |
| `--batch`, `-batch`             | 複数 PDF ファイルをバッチ処理                                                        | `pdf2zh_next --batch ./pdfs/*.pdf`                                                                                    |
| `--batch-input-dir`, `-bid`     | バッチ入力ディレクトリ                                                                   | `pdf2zh_next --batch-input-dir ./pdf 极速 s`                                                                                |
| `--batch-output-dir`, `-bod`    | バッチ出力ディレクトリ                                                                  | `pdf2zh_next --batch-input-dir ./pdfs --batch-output-dir ./translated`                                                |
| `--batch-pattern`, `-bp`        | バッチファイルパターン                                                                      | `pdf2zh_next --batch-input-dir ./pdfs --batch-pattern "*.pdf"`                                                        |
| `--batch-recursive`, `-br`      | バッチを再帰的に処理                                                               | `pdf2zh_next --batch-input-dir ./pdfs --batch-recursive`                                                              |
| `--batch-concurrency`, `-bc`    | バッチ並列レベル、デフォルト：2                                                     | `pdf2zh_next --batch-input-dir ./pdfs --batch-concurrency 4`                                                          |
| `--batch-timeout`, `-bt`        | ファイルごとのバッチタイムアウト（秒）、デフォルト：300                                         | `pdf2zh_next --batch-input-dir ./pdfs --batch-timeout 600`                                                            |
| `--batch-retry`, `-bret`        | ファイルごとのバッチ再試行回数、デフォルト：2                                                      | `pdf2zh_next --batch-input-dir ./pdfs --batch-retry 3`                                                                |
| `--batch-skip-existing`, `-bse` | バッチ処理で既存ファイルをスキップ                                                 | `pdf2zh_next --batch-input-dir ./pdfs --batch-skip-existing`                                                          |
| `--batch-overwrite`, `-bo`      | バッチ処理で既存ファイルを上書き                                            | `pdf2zh_next --batch-input-dir ./pdfs --batch-overwrite`                                                              |
| `--batch-rename`, `-brn`        | バッチ出力の名前変更パターン                                                         | `pdf2zh_next --batch-input-dir ./pdfs --batch-rename "{name}_translated.{ext}"`                                       |
| `--batch-report`, `-brep`       | バッチレポートを生成                                                                   | `pdf2zh_next --batch-input-dir ./pdfs --batch-report`                                                                 |
| `--batch-report-format`, `-br 极速 f` | バッチレポート形式：`json`、`csv` 极速、`txt`、`html`、デフォルト：`json`                      | `pdf2zh_next --batch-input-dir ./pdfs --batch-report-format csv`                                                      |
| `--batch-report-output`, `-bro` | バッチレポート出力ファイルパス                                                           | `pdf2zh_next --batch-input-dir ./pdfs --batch-report-output ./batch_report.json`                                      |
| `--watch`, `-watch`             | 新しい PDF ファイル用にディレクトリを監視                                                       | `pdf2zh_next --watch ./pdfs`                                                                                          |
| `--watch-interval`, `-wi`       | 監視間隔（秒）、デフォルト：60                                                  | `pdf2zh_next --watch ./pdfs --watch-interval 30`                                                                      |
| `--watch-recursive`, `-wr`      | 再帰的に監視                                                                       | `pdf2zh_next --watch ./pdfs --watch-recursive`                                                                        |
| `--watch-pattern`, `-wp`        | 監視ファイルパターン                                                                      | `pdf2zh_next --watch ./pdfs --watch-pattern "*.pdf"`                                                                  |
| `--watch-command`, `-wc`        | 新しいファイルが検出されたときに実行するコマンド                                            | `pdf2zh_next --watch ./pdfs --watch-command "echo New file: {file}"`                                                  |
| `--watch-output-dir`, `-wod`    | 監視出力ディレクトリ                                                                  | `pdf2zh_next --watch ./pdfs --watch-output-dir ./translated`                                                          |
| `--watch-overwrite`, `-wo`      | 監視モードで既存ファイルを上書き                                                  | `pdf2zh_next --watch ./pdfs --watch-overwrite`                                                                        |
| `--watch-rename`, `-wrn`        | 監視出力の名前変更パターン                                                         | `pdf2zh_next --watch ./pdfs --watch-rename "{name}_translated.{ext}"`                                                 |
| `--daemon`, `-d`                | デーモンとして実行                                                                           | `pdf2zh_next --daemon`                                                                                                |
| `--pid`, `-pid`                 | PID ファイルパス                                                                           | `pdf2zh_next --daemon --pid ./pdf2zh.pid`                                                                             |
| `--log`, `-log`                 | デーモンモード用のログファイルパス                                                           | `pdf2zh_next --daemon --log ./pdf2zh.log`                                                                             |
| `--stop`, `-极速 stop`               | デーモンを停止                                                                             | `pdf2zh_next --stop`                                                                                                  |
| `--restart`, `-restart`         | デーモンを再起動                                                                          | `pdf2zh_next --restart`                                                                                               |
| `--status`, `-status`           | デーモンステータスをチェック                                                                     | `pdf2zh_next --status`                                                                                                |
| `--user`, `-user`               | デーモンを実行するユーザー                                                                   | `pdf2zh_next --daemon --user nobody`                                                                                  |
| `--group`, `-group`             | デーモンを実行するグループ                                                                  | `pdf2zh_next --daemon --group nogroup`                                                                                |
| `--umask`, `-umask`             | デーモンの umask                                                                        | `pdf2zh_next --daemon --umask 022`                                                                极速                    |
| `--chdir`, `-chdir`             | デーモンのディレクトリ変更                                                             | `pdf2zh_next --daemon --chdir /var/lib/pdf2zh`                                                                        |
| `--no-chdir`, `-ncd`            | デーモンのディレクトリ変更を行わない                                                      | `pdf2zh_next --daemon --no-chdir`                                                                                     |
| `--no-close`, `-ncl`            | デーモンのファイル記述子を閉じない                                                | `pdf2zh_next --daemon --no-close`                                                                                     |
| `--no-umask`, `-num`            | デーモンの umask を設定しない                                                             | `pdf2zh_next --daemon --no-umask`                                                                                     |
| `--no-setsid`, `-nsd`            | デーモンの setsid() を呼び出さない                                                         | `pdf2zh_next --daemon --no-setsid`                                                                                    |
| `--help-all`, `-ha`             | 高度なオプションを含むすべてのヘルプを表示                                                | `pdf2zh_next --help-all`                                                                                              |
| `--help-short`, `-hs`           | 短いヘルプを表示                                                                         | `pdf2zh_next --help-short`                                                                                            |
| `--help-json`, `-hj`            | JSON 形式でヘルプを表示                                                                | `pdf2zh_next --help-json`                                                                                             |
| `--help-md`, `-hmd`             | Markdown 形式でヘルプを表示                                                            | `pdf2zh_next --help-md`                                                                                               |
| `--help-man`, `-hman`           | man ページ形式でヘルプを表示                                                            | `pdf2zh_next --help-man`                                                                                              |
| `--help-rst`, `-hrst`           | reStructuredText 形式でヘルプを表示                                                    | `pdf2zh_next --help-rst`                                                                                              |
| `--help-xml`, `-hxml`           | XML 形式でヘルプを表示                                                                 | `pdf2zh_next --help-xml`                                                                                              |
| `--help-yaml`, `-hyaml`         | YAML 形式でヘルプを表示                                                                | `pdf2zh_next --help-yaml`                                                                                             |
| `--help-html`, `-hhtml`         | HTML 形式でヘルプを表示                                                                | `pdf2zh_next --help-html`                                                                                             |
| `--help-text`, `-htxt`          | プレーンテキスト形式でヘルプを表示                                                          | `pdf2zh_next --help-text`                                                                                             |
| `--help-usage`, `-hu`           | 使用例を表示                                                                     | `pdf2zh_next --help-usage`                                                                                            |
| `--help-verbose`, `-hv`         | 詳細なヘルプを表示                                                                       | `pdf2zh_next --help-verbose`                                                                                          |
| `--help-debug`, `-hdb 极速 g`         | デバッグヘルプを表示                                                                         | `pdf2zh_next --help-debug`                                                                                            |
| `--help-api`, `-hapi`           | API ヘルプを表示                                                                           | `pdf2zh_next --help-api`                                                                                              |
| `--help-webui`, `-hwebui`       | WebUI ヘルプを显示                                                                         | `pdf2zh_next --help-webui`                                                                                            |
| `--help-batch`, `-hbatch`       | バッチヘルプを显示                                                                         | `pdf2zh_next --help-batch`                                                                                            |
| `--help-watch`, `-hwatch`       | 監視ヘルプを显示                                                                         | `pdf2zh_next --help-watch`                                                                                          |
| `--help-daemon`, `-hdaemon`     | デーモンヘルプを显示                                                                        | `pdf2zh_next --help-daemon`                                                                                           |
| `--help-config`, `-hcfg`        | 設定ヘルプを显示                                                                 | `pdf2zh_next --help-config`                                                                                       |
| `--help-translator`, `-ht`      | 翻訳ヘルプを显示                                                                    | `pdf2zh_next --help-translator`                                                                                       |
| `--help-ocr`, `-hocr`           | OCR ヘルプを显示                                                                           | `pdf2zh_next --help-ocr`                                                                                              |
| `--help-font`, `-hfont`         | フォントヘルプを显示                                                                          | `pdf2zh_next --help-font`                                                                                         |
| `--help-style`, `-hstyle`       | スタイルヘルプを显示                                                                         | `pdf2zh_next --help-style`                                                                                            |
| `--help-cache`, `-hcache`       | キャッシュヘルプを显示                                                                         | `pdf2zh_next --help-cache`                                                                                            |
| `--help-glossary`, `-hgl`       | 用語集ヘルプを显示                                                                      | `pdf2zh_next --help-glossary`                                                                                         |
| `--help-preprocess`, `-hpp`     | 前処理ヘルプを显示                                                                 | `pdf2zh_next --help-preprocess`                                                                                       |
| `--help-postprocess`, `-hpop`   | 後処理ヘルプを显示                                                                | `pdf2zh_next --help-postprocess`                                                                                      |
| `--help-benchmark`, `-hbm`      | ベンチマークヘルプを显示                                                                     | `pdf2zh_next --help-benchmark`                                                                                    |
| `--help-test`, `-htest`         | テストヘルプを显示                                                                          | `pdf2zh_next --help-test`                                                                                             |
| `--help-profile`, `-hprof`      | プロファイルヘルプを显示                                                                       | `pdf2zh_next --help-profile`                                                                                          |
| `--help-docker`, `-hdocker`     | Docker ヘルプを显示                                                                        | `pdf2zh_next --help-docker`                                                                                           |
| `--help-en 极速 v`, `-henv`           | 環境ヘルプを显示                                                                   | `pdf2zh_next --help-env`                                                                                              |
| `--help-version`, `-hver`       | バージョンヘルプを显示                                                                       | `pdf2zh_next --help-version`                                                                                          |
| `--help-license`, `-hlic` 极速       | ライセンスヘルプを显示                                                                       | `pdf2zh_next --help-license`                                                                                          |
| `--help-contrib`, `-hcontrib`   | 貢献ヘルプを显示                                                                  | `pdf2zh_next --help-contrib`                                                                                          |
| `--help-community`, `-hcomm`    | コミュニティヘルプを显示                                                                     | `pdf2zh_next --help-community`                                                                                        |
| `--help-faq`, `-hfaq`           | FAQ ヘルプを显示                                                                           | `pdf2zh_next --help-faq`                                                                                              |
| `--help-troubleshoot`, `-hts`   | トラブルシューティングヘルプを显示                                                               | `pdf2zh_next --help-troubleshoot`                                                                                     |
| `--help-security`, `-hsec`      | セキュリティヘルプを显示                                                                      | `pdf2zh_next --help-security`                                                                                         |
| `--help-privacy`, `-hpriv`      | プライバシーヘルプを显示                                                                       | `pdf2zh_next --help-privacy`                                                                                          |
| `--help-performance`, `-hperf`  | パフォーマンスヘルプを显示                                                                   | `pdf2zh_next --help-performance`                                                                                      |
| `--help-compatibility`, `-hcomp` | 互換性ヘルプを显示                                                                 | `pdf2zh_next --help-compatibility`                                                                                    |
| `--help-limitations`, `-hlim`   | 制限事項ヘルプを显示                                                                   | `pdf2zh_next --help-limitations`                                                                                      |
| `--help-known-issues`, `-hki`   | 既知の問題ヘルプを显示                                                                  | `pdf2zh_next --help-known-issues`                                                                                     |
| `--help-changelog`, `-h 极速 cl`      | 変更履歴ヘルプを显示                                                                     | `pdf2zh_next --help-changelog`                                                                                        |
| `--help-roadmap`, `-hroad`      | ロードマップヘルプを显示                                                                极速                                                                 | `pdf2zh_next --help-roadmap`                                                                                          |
| `--help-support`, `-hsupp`      | サポートヘルプを显示                                                                       | `pdf2zh_next --help-support`                                                                                          |
| `--help-donate`, `-hdon`        | 寄付ヘルプを显示                                                                        | `pdf2zh_next --help-donate`                                                                                           |
| `--help-contact`, `-hcont`      | 連絡先ヘルプを显示                                                                       | `pdf2zh_next --help-contact`                                                                                          |
| `--help-about`, `-habout`       | 概要ヘルプを显示                                                                         | `pdf2zh_next --help-about`                                                                                            |
`None`  |
| `--output-dir`                  | Directory to save the output file                                                       | `pdf2zh_next --output-dir /path/to/output`                                                                            | `None`  |
| `--output-filename`             | Name of the output file                                                                 | `pdf2zh_next --output-filename output.pdf`                                                                            | `None`  |
| `--keep-original-order`         | Keep the original page order of the PDF                                                 | `pdf2zh_next --keep-original-order`                                                                                   | `false` |
| `--disable-translation`         | Disable translation                                                                     | `pdf2zh_next --disable-translation`                                                                                   | `false` |
| `--disable-math`                | Disable math translation                                                                | `pdf2zh_next --disable-math`                                                                                          | `false` |
| `--disable-figure`              | Disable figure translation                                                              | `pdf2zh_next --disable-figure`                                                                                        | `false` |
| `--disable-table`               | Disable table translation                                                               | `pdf2zh_next --disable-table`                                                                                         | `false` |
| `--disable-algorithm`           | Disable algorithm translation                                                           | `pdf2zh_next --disable-algorithm`                                                                                     | `false` |
| `--disable-caption`             | Disable caption translation                                                             | `pdf2zh_next --disable-caption`                                                                                       | `false` |
| `--disable-reference`           | Disable reference translation                                                           | `pdf2zh_next --disable-reference`                                                                                     | `false` |
| `--disable-citation`            | Disable citation translation                                                            | `pdf2zh_next --disable-citation`                                                                                      | `false` |
| `--disable-bib`                 | Disable bibliography translation                                                        | `pdf2zh_next --disable-bib`                                                                                           | `false` |
| `--disable-abstract`            | Disable abstract translation                                                            | `pdf2zh_next --disable-abstract`                                                                                      | `false` |
| `--disable-title`               | Disable title translation                                                               | `pdf2zh_next --disable-title`                                                                                         | `false` |
| `--disable-section`             | Disable section translation                                                             | `pdf2zh_next --disable-section`                                                                                       | `false` |
| `--disable-paragraph`           | Disable paragraph translation                                                           | `pdf2zh_next --disable-paragraph`                                                                                     | `false` |
| `--disable-footnote`            | Disable footnote translation                                                            | `pdf2zh_next --disable-footnote`                                                                                      | `false` |
| `--disable-quote`               | Disable quote translation                                                               | `pdf2zh_next --disable-quote`                                                                                         | `false` |
| `--disable-itemize`             | Disable itemize translation                                                             | `pdf2zh_next --disable-itemize`                                                                                       | `false` |
| `--disable-enumerate`           | Disable enumerate translation                                                           | `pdf2zh_next --disable-enumerate`                                                                                     | `false` |
| `--disable-unknown`             | Disable unknown translation                                                             | `pdf2zh_next --disable-unknown`                                                                                       | `false` |
| `--disable-other`               | Disable other translation                                                               | `pdf2zh_next --disable-other`                                                                                         | `false` |
| `--disable-merge`               | Disable merging of translated text                                                      | `pdf2zh_next --disable-merge`                                                                                         | `false` |
| `--disable-ocr`                 | Disable OCR                                                                             | `pdf2zh_next --disable-ocr`                                                                                           | `false` |
| `--translation-service`         | Translation service to use                                                              | `pdf2zh_next --translation-service google`                                                                            | `None`  |
| `--translation-service-config`  | Path to the translation service config file                                             | `pdf2zh_next --translation-service-config /path/to/config/translation.toml`                                           | `None`  |
| `--source-lang`                 | Source language                                                                         | `pdf2zh_next --source-lang en`                                                                                        | `auto`  |
| `--target-lang`                 | Target language                                                                         | `pdf2zh_next --target-lang zh`                                                                                        | `zh`    |
| `--math-translator`             | Math translator to use                                                                  | `pdf2zh_next --math-translator google`                                                                                | `google`|
| `--math-translator-config`      | Path to the math translator config file                                                 | `pdf2zh_next --math-translator-config /path/to/config/math.toml`                                                      | `None`  |
| `--ocr-service`                 | OCR service to use                                                                      | `pdf2zh_next --ocr-service tesseract`                                                                                 | `tesseract` |
| `--ocr-service-config`          | Path to the OCR service config file                                                     | `pdf2zh_next --ocr-service-config /path/to/config/ocr.toml`                                                           | `None`  |
| `--concurrency-limit`           | Maximum number of concurrent translation tasks                                          | `pdf2zh_next --concurrency-limit 10`                                                                                  | `5`     |
| `--timeout`                     | Timeout for each translation task in seconds                                            | `pdf2zh_next --timeout 30`                                                                                            | `30`    |
| `--retry-attempts`              | Number of retry attempts for failed translation tasks                                   | `pdf2zh_next --retry-attempts 3`                                                                                      | `3`     |
| `--retry-delay`                 | Delay between retry attempts in seconds                                                 | `pdf2zh_next --retry-delay 1`                                                                                         | `1`     |
| `--log-level`                   | Log level                                                                               | `pdf2zh_next --log-level info`                                                                                        | `info`  |
| `--log-file`                    | Path to the log file                                                                    | `pdf2zh_next --log-file /path/to/log/file.log`                                                                        | `None`  |
| `--cache-dir`                   | Directory to store cache files                                                          | `pdf2zh_next --cache-dir /path/to/cache`                                                                              | `None`  |
| `--cache-ttl`                   | Time to live for cache entries in seconds                                               | `pdf2zh_next --cache-ttl 3600`                                                                                        | `3600`  |
| `--cache-size`                  | Maximum size of the cache in megabytes                                                  | `pdf2zh_next --cache-size 100`                                                                                        | `100`   |
| `--cache-disabled`              | Disable cache                                                                           | `pdf2zh_next --cache-disabled`                                                                                        | `false` |
| `--dry-run`                     | Perform a dry run without actually translating                                          | `pdf2zh_next --dry-run`                                                                                               | `false` |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               | `false` |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  | `false` |
`5`                               |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `--report-file`                 | File to write progress reports to                                                       | `pdf2zh_next example.pdf --report-file /tmp/progress.txt`                                                             | `/tmp/progress.txt`               |
| `--report-format`               | Format of progress reports (`json` or `text`)                                           | `pdf2zh_next example.pdf --report-format json`                                                                        | `text`                            |
| `--no-progress`                 | Disable progress reporting                                                              | `pdf2zh_next example.pdf --no-progress`                                                                               | `false`                           |
| `--progress`                    | Enable progress reporting (default)                                                     | `pdf2zh_next example.pdf --progress`                                                                                  | `true`                            |

---

### TRANSLATION RESULT

| `--report-interval`             | 進捗レポートの間隔（秒単位）                                                   | `pdf2zh_next example.pdf --report-interval 5`                                                                         | `5`                               |
|---------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `--report-file`                 | 進捗レポートを書き込むファイル                                                   | `pdf2zh_next example.pdf --report-file /tmp/progress.txt`                                                             | `/tmp/progress.txt`               |
| `--report-format`               | 進捗レポートのフォーマット（`json` または `text`）                              | `pdf2zh_next example.pdf --report-format json`                                                                        | `text`                            |
| `--no-progress`                 | 進捗レポートを無効にする                                                         | `pdf2zh_next example.pdf --no-progress`                                                                               | `false`                           |
| `--progress`                    | 進捗レポートを有効にする（デフォルト）                                           | `pdf2zh_next example.pdf --progress`                                                                                  | `true`                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-to-file`                 | Log to file instead of stdout                                                           | `pdf2zh_next example.pdf --log-to-file`                                                                               |
| `--log-file`                    | Specify the log file path                                                               | `pdf2zh_next example.pdf --log-to-file --log-file ./log.txt`                                                          |
| `--disable-log-timestamp`       | Disable timestamp in log                                                                | `pdf2zh_next example.pdf --disable-log-timestamp`                                                                     |
| `--log-format`                  | Log format (`default` or `json`)                                                        | `pdf2zh_next example.pdf --log-format json`                                                                           |

---

### OUTPUT

| `--debug`                       | デバッグログレベルを使用する                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-to-file`                 | 標準出力の代わりにファイルにログを記録する                                                           | `pdf2zh_next example.pdf --log-to-file`                                                                               |
| `--log-file`                    | ログファイルのパスを指定する                                                               | `pdf2zh_next example.pdf --log-to-file --log-file ./log.txt`                                                          |
| `--disable-log-timestamp`       | ログのタイムスタンプを無効にする                                                                | `pdf2zh_next example.pdf --disable-log-timestamp`                                                                     |
| `--log-format`                  | ログフォーマット（`default` または `json`）                                                        | `pdf2zh_next example.pdf --log-format json`                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`                     | Show the version number and exit                                                        | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show this message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION

| `--gui`                         | GUI で操作                                                                              | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`                     | バージョン番号を表示して終了                                                              | `pdf2zh_next --version`                                                                                               |
| `--help`                        | このメッセージを表示して終了                                                              | `pdf2zh_next --help`                                                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-m`<br/>`--model`              | Specify the translation model. The default model is `google`                            | `pdf2zh_next example.pdf -m google`<br/>`pdf2zh_next example.pdf --model google`                                      |
| `-t`<br/>`--target-language`    | Specify the target language. The default target language is `zh`                        | `pdf2zh_next example.pdf -t ja`<br/>`pdf2zh_next example.pdf --target-language ja`                                    |
| `-s`<br/>`--source-language`    | Specify the source language. The default source language is `auto`                      | `pdf2zh_next example.pdf -s en`<br/>`pdf2zh_next example.pdf --source-language en`                                    |
| `-p`<br/>`--provider`           | Specify the translation provider. The default provider is `google`                      | `pdf2zh_next example.pdf -p google`<br/>`pdf2zh_next example.pdf --provider google`                                   |
| `-k`<br/>`--api-key`            | Specify the API key for the translation provider                                        | `pdf2zh_next example.pdf -k <API_KEY>`<br/>`pdf2zh_next example.pdf --api-key <API_KEY>`                              |
| `-c`<br/>`--config`             | Specify the path to a configuration file                                                | `pdf2zh_next example.pdf -c config.toml`<br/>`pdf2zh_next example.pdf --config config.toml`                           |
| `-o`<br/>`--output`             | Specify the output file path                                                            | `pdf2zh_next example.pdf -o output.pdf`<br/>`pdf2zh_next example.pdf --output output.pdf`                             |
| `-f`<br/>`--force`              | Force overwrite the output file if it already exists                                    | `pdf2zh_next example.pdf -o output.pdf -f`<br/>`pdf2zh_next example.pdf --output output.pdf --force`                  |
| `-v`<br/>`--verbose`            | Enable verbose output                                                                   | `pdf2zh_next example.pdf -v`<br/>`pdf2zh_next example.pdf --verbose`                                                  |
| `-h`<br/>`--help`               | Show help message and exit                                                              | `pdf2zh_next -h`<br/>`pdf2zh_next --help`                                                                            |
| `-V`<br/>`--version`            | Show version information and exit                                                       | `pdf2zh_next -V`<br/>`pdf2zh_next --version`                                                                         |

---

### OUTPUT

| `--warmup`                      | 必要なアセットをダウンロードして検証した後に終了します                                     | `pdf2zh_next example.pdf --warmup`                                                                                    |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-m`<br/>`--model`              | 翻訳モデルを指定します。デフォルトのモデルは `google` です                                 | `pdf2zh_next example.pdf -m google`<br/>`pdf2zh_next example.pdf --model google`                                      |
| `-t`<br/>`--target-language`    | ターゲット言語を指定します。デフォルトのターゲット言語は `zh` です                         | `pdf2zh_next example.pdf -t ja`<br/>`pdf2zh_next example.pdf --target-language ja`                                    |
| `-s`<br/>`--source-language`    | ソース言語を指定します。デフォルトのソース言語は `auto` です                               | `pdf2zh_next example.pdf -s en`<br/>`pdf2zh_next example.pdf --source-language en`                                    |
| `-p`<br/>`--provider`           | 翻訳プロバイダーを指定します。デフォルトのプロバイダーは `google` です                     | `pdf2zh_next example.pdf -p google`<br/>`pdf2zh_next example.pdf --provider google`                                   |
| `-k`<br/>`--api-key`            | 翻訳プロバイダーの API キーを指定します                                                    | `pdf2zh_next example.pdf -k <API_KEY>`<br/>`pdf2zh_next example.pdf --api-key <API_KEY>`                              |
| `-c`<br/>`--config`             | 設定ファイルへのパスを指定します                                                           | `pdf2zh_next example.pdf -c config.toml`<br/>`pdf2zh_next example.pdf --config config.toml`                           |
| `-o`<br/>`--output`             | 出力ファイルのパスを指定します                                                             | `pdf2zh_next example.pdf -o output.pdf`<br/>`pdf2zh_next example.pdf --output output.pdf`                             |
| `-f`<br/>`--force`              | 出力ファイルが既に存在する場合、強制的に上書きします                                       | `pdf2zh_next example.pdf -o output.pdf -f`<br/>`pdf2zh_next example.pdf --output output.pdf --force`                  |
| `-v`<br/>`--verbose`            | 詳細な出力を有効にします                                                                   | `pdf2zh_next example.pdf -v`<br/>`pdf2zh_next example.pdf --verbose`                                                  |
| `-h`<br/>`--help`               | ヘルプメッセージを表示して終了します                                                       | `pdf2zh_next -h`<br/>`pdf2zh_next --help`                                                                            |
| `-V`<br/>`--version`            | バージョン情報を表示して終了します                                                         | `pdf2zh_next -V`<br/>`pdf2zh_next --version`                                                                         |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--offline-mode`                | Enable offline mode, translate using offline assets                                     | `pdf2zh_next example.pdf --offline-mode`                                                                              |
| `--custom-offline-assets`       | Specify custom offline assets directory                                                 | `pdf2zh_next example.pdf --custom-offline-assets /path/to/assets`                                                      |
| `--ocr`                         | Enable OCR for better text extraction (when text extraction is poor)                    | `pdf2zh_next example.pdf --ocr`                                                                                        |
| `--ocr-language`                | Specify OCR language (e.g., `eng`, `chi_sim`)                                           | `pdf2zh_next example.pdf --ocr-language chi_sim`                                                                      |
| `--ocr-pdf`                     | Enable OCR for entire PDF (use when PDF is image-based)                                 | `pdf2zh_next example.pdf --ocr-pdf`                                                                                    |
| `--ocr-offline`                 | Enable offline OCR mode                                                                 | `pdf2zh_next example.pdf --ocr-offline`                                                                                |
| `--ocr-offline-data-dir`        | Specify offline OCR data directory                                                      | `pdf2zh_next example.pdf --ocr-offline-data-dir /path/to/tessdata`                                                     |
| `--ocr-method`                  | Specify OCR method (`tesseract`, `paddleocr`)                                           | `pdf2zh_next example.pdf --ocr-method paddleocr`                                                                       |
| `--ocr-pdf-method`              | Specify OCR PDF method (`ocrmypdf`, `paddleocr`)                                        | `pdf2zh_next example.pdf --ocr-pdf-method paddleocr`                                                                   |
| `--ocr-pdf-force-ocr`           | Force OCR for all pages (even if they contain text)                                     | `pdf2zh_next example.pdf --ocr-pdf-force-ocr`                                                                          |
| `--ocr-pdf-skip-text`           | Skip OCR for pages that already contain text                                            | `pdf2zh_next example.pdf --ocr-pdf-skip-text`                                                                          |
| `--ocr-pdf-language`            | Specify OCR PDF language (e.g., `eng`, `chi_sim`)                                       | `pdf2zh_next example.pdf --ocr-pdf-language chi_sim`                                                                   |
| `--ocr-pdf-deskew`              | Deskew pages before OCR                                                                 | `pdf2zh_next example.pdf --ocr-pdf-deskew`                                                                             |
| `--ocr-pdf-clean`               | Clean pages before OCR                                                                  | `pdf2zh_next example.pdf --ocr-pdf-clean`                                                                              |
| `--ocr-pdf-remove-background`   | Remove background from pages before OCR                                                 | `pdf2zh_next example.pdf --ocr-pdf-remove-background`                                                                  |
| `--ocr-pdf-rotate-pages`        | Automatically rotate pages                                                              | `pdf2zh_next example.pdf --ocr-pdf-rotate-pages`                                                                       |
| `--ocr-pdf-rotate-pages-threshold` | Threshold for page rotation (default: `14.0`)                                        | `pdf2zh_next example.pdf --ocr-pdf-rotate-pages-threshold 10.0`                                                        |
| `--ocr-pdf-skip-big`            | Skip pages larger than specified size (default: `50MB`)                                 | `pdf2zh_next example.pdf --ocr-pdf-skip-big 100MB`                                                                     |
| `--ocr-pdf-optimize`            | Optimize PDF after OCR                                                                  | `pdf2zh_next example.pdf --ocr-pdf-optimize`                                                                           |
| `--ocr-pdf-force-ocr`           | Force OCR for all pages (even if they contain text)                                     | `pdf2zh_next example.pdf --ocr-pdf-force-ocr`                                                                          |
| `--ocr-pdf-skip-text`           | Skip OCR for pages that already contain text                                            | `pdf2zh_next example.pdf --ocr-pdf-skip-text`                                                                          |
| `--ocr-pdf-jpg-quality`         | JPG quality for OCR (default: `90`)                                                     | `pdf2zh_next example.pdf --ocr-pdf-jpg-quality 95`                                                                     |
| `--ocr-pdf-png-quality`         | PNG quality for OCR (default: `90`)                                                     | `pdf2zh_next example.pdf --ocr-pdf-png-quality 95`                                                                     |
| `--ocr-pdf-jpg-quality`         | JPG quality for OCR (default: `90`)                                                     | `pdf2zh_next example.pdf --ocr-pdf-jpg-quality 95`                                                                     |

---

### TRANSLATION

| `--generate-offline-assets`     | 指定されたディレクトリにオフラインアセットパッケージを生成する                              | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--offline-mode`                | オフラインンモードを有効にし、オフラインアセットを使用して翻訳する                             | `pdf2zh_next example.pdf --offline-mode`                                                                              |
| `--custom-offline-assets`       | カスタムオフラインアセットディレクトリを指定する                                                 | `pdf2zh_next example.pdf --custom-offline-assets /path/to/assets`                                                      |
| `--ocr`                         | テキスト抽出が不十分な場合に OCR を有効にしてテキスト抽出を改善する                    | `pdf2zh_next example.pdf --ocr`                                                                                        |
| `--ocr-language`                | OCR 言語を指定する（例：`eng`、`chi_sim`）                                           | `pdf2zh_next example.pdf --ocr-language chi_sim`                                                                      |
| `--ocr-pdf`                     | PDF 全体に OCR を適用する（画像ベースの PDF の場合に使用）                                 | `pdf2zh_next example.pdf --ocr-pdf`                                                                                    |
| `--ocr-offline`                 | オフライン OCR モードを有効にする                                                                 | `pdf2zh_next example.pdf --ocr-offline`                                                                                |
| `--ocr-offline-data-dir`        | オフライン OCR データディレクトリを指定する                                                      | `pdf2zh_next example.pdf --ocr-offline-data-dir /path/to/tessdata`                                                     |
| `--ocr-method`                  | OCR メソッドを指定する（`tesseract`、`paddleocr`）                                           | `pdf2zh_next example.pdf --ocr-method paddleocr`                                                                       |
| `--ocr-pdf-method`              | OCR PDF メソッドを指定する（`ocrmypdf`、`paddleocr`）                                        | `pdf2zh_next example.pdf --ocr-pdf-method paddleocr`                                                                   |
| `--ocr-pdf-force-ocr`           | すべてのページに強制的に OCR を適用する（テキストが含まれている場合でも）                                     | `pdf2zh_next example.pdf --ocr-pdf-force-ocr`                                                                          |
| `--ocr-pdf-skip-text`           | すでにテキストが含まれているページの OCR をスキップする                                            | `pdf2zh_next example.pdf --ocr-pdf-skip-text`                                                                          |
| `--ocr-pdf-language`            | OCR PDF 言語を指定する（例：`eng`、`chi_sim`）                                       | `pdf2zh_next example.pdf --ocr-pdf-language chi_sim`                                                                   |
| `--ocr-pdf-deskew`              | OCR 前にページの傾きを補正する                                                                 | `pdf2zh_next example.pdf --ocr-pdf-deskew`                                                                             |
| `--ocr-pdf-clean`               | OCR 前にページをクリーンアップする                                                                  | `pdf2zh_next example.pdf --ocr-pdf-clean`                                                                              |
| `--ocr-pdf-remove-background`   | OCR 前にページから背景を削除する                                                 | `pdf2zh_next example.pdf --ocr-pdf-remove-background`                                                                  |
| `--ocr-pdf-rotate-pages`        | ページを自動的に回転させる                                                              | `pdf2zh_next example.pdf --ocr-pdf-rotate-pages`                                                                       |
| `--ocr-pdf-rotate-pages-threshold` | ページ回転の閾値（デフォルト：`14.0`）                                        | `pdf2zh_next example.pdf --ocr-pdf-rotate-pages-threshold 10.0`                                                        |
| `--ocr-pdf-skip-big`            | 指定されたサイズより大きいページをスキップする（デフォルト：`50MB`）                                 | `pdf2zh_next example.pdf --ocr-pdf-skip-big 100MB`                                                                     |
| `--ocr-pdf-optimize`            | OCR 後に PDF を最適化する                                                                  | `pdf2zh_next example.pdf --ocr-pdf-optimize`                                                                           |
| `--ocr-pdf-force-ocr`           | すべてのページに強制的に OCR を適用する（テキストが含まれている場合でも）                                     | `pdf2zh_next example.pdf --ocr-pdf-force-ocr`                                                                          |
| `--ocr-pdf-skip-text`           | すでにテキストが含まれているページの OCR をスキップする                                            | `pdf2zh_next example.pdf --ocr-pdf-skip-text`                                                                          |
| `--ocr-pdf-jpg-quality`         | OCR 用の JPG 品質（デフォルト：`90`）                                                     | `pdf2zh_next example.pdf --ocr-pdf-jpg-quality 95`                                                                     |
| `--ocr-pdf-png-quality`         | OCR 用の PNG 品質（デフォルト：`90`）                                                     | `pdf2zh_next example.pdf --ocr-pdf-png-quality 95`                                                                     |
| `--ocr-pdf-jpg-quality`         | OCR 用の JPG 品質（デフォルト：`90`）                                                     | `pdf2zh_next example.pdf --ocr-pdf-jpg-quality 95`                                                                     |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-path`         | Path to offline assets directory                                                         | `pdf2zh_next example.pdf --offline-assets-path /path`                                                                 |
| `--offline-assets-download`     | Download offline assets to the specified directory                                       | `pdf2zh_next example.pdf --offline-assets-download /path`                                                              |
| `--offline-assets-check`        | Check if offline assets are available                                                    | `pdf2zh_next example.pdf --offline-assets-check`                                                                      |
| `--offline-assets-update`       | Update offline assets to the latest version                                              | `pdf2zh_next example.pdf --offline-assets-update`                                                                     |
| `--offline-assets-clear`        | Clear offline assets cache                                                               | `pdf2zh_next example.pdf --offline-assets-clear`                                                                      |

---

### TRANSLATION

| `--restore-offline-assets`      | 指定されたディレクトリからオフラインアセットパッケージを復元する                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-path`         | オフラインアセットディレクトリへのパス                                                         | `pdf2zh_next example.pdf --offline-assets-path /path`                                                                 |
| `--offline-assets-download`     | 指定されたディレクトリにオフラインアセットをダウンロードする                                       | `pdf2zh_next example.pdf --offline-assets-download /path`                                                              |
| `--offline-assets-check`        | オフラインアセットが利用可能かどうかを確認する                                                    | `pdf2zh_next example.pdf --offline-assets-check`                                                                      |
| `--offline-assets-update`       | オフラインアセットを最新バージョンに更新する                                                      | `pdf2zh_next example.pdf --offline-assets-update`                                                                     |
| `--offline-assets-clear`        | オフラインアセットキャッシュをクリアする                                                               | `pdf2zh_next example.pdf --offline-assets-clear`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-i`, `--input`                 | The path of the input file or directory.                                                 | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output`                | The path of the output file or directory.                                                | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-f`, `--force`                 | Force overwrite the output file if it exists.                                            | `pdf2zh_next -i input.pdf -o output.pdf -f`                                                                           |
| `-l`, `--language`              | The target language for translation.                                                     | `pdf2zh_next -i input.pdf -l ja`                                                                                      |
| `-t`, `--translator`            | The translator service to use, such as Google, OpenAI, etc.                              | `pdf2zh_next -i input.pdf -t google`                                                                                  |
| `--api-key`                     | The API key for the translator service.                                                  | `pdf2zh_next -i input.pdf -t openai --api-key YOUR_OPENAI_API_KEY`                                                    |
| `--model`                       | The model to use for the translator service.                                             | `pdf2zh_next -i input.pdf -t openai --model gpt-4o`                                                                  |
| `--base-url`                    | The base URL for the translator service.                                                 | `pdf2zh_next -i input.pdf -t openai --base-url https://api.openai.com/v1`                                             |
| `--proxy`                       | The proxy to use for the translator service.                                             | `pdf2zh_next -i input.pdf -t google --proxy http://127.0.0.1:7890`                                                   |
| `-p`, `--preserve-formatting`   | Preserve the original formatting of the text.                                            | `pdf2zh_next -i input.pdf -p`                                                                                         |
| `-c`, `--concurrency`           | The number of concurrent requests to the translator service.                             | `pdf2zh_next -i input.pdf -c 10`                                                                                      |
| `-s`, `--size-limit`            | The size limit for each request to the translator service, in tokens.                    | `pdf2zh_next -i input.pdf -s 1000`                                                                                    |
| `--timeout`                     | The timeout for each request to the translator service, in seconds.                      | `pdf2zh_next -i input.pdf --timeout 10`                                                                               |
| `--retry`                       | The number of retries for each request to the translator service.                         | `pdf2zh_next -i input.pdf --retry 3`                                                                                  |
| `--retry-delay`                 | The delay between retries for each request to the translator service, in seconds.        | `pdf2zh_next -i input.pdf --retry-delay 1`                                                                            |
| `--no-cache`                    | Disable the cache for the translator service.                                            | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir`                   | The directory to store the cache for the translator service.                            | `pdf2zh_next -i input.pdf --cache-dir ./cache`                                                                        |
| `--log-level`                   | The log level for the application.                                                       | `pdf2zh_next -i input.pdf --log-level debug`                                                                          |
| `--log-file`                    | The file to store the logs for the application.                                          | `pdf2zh_next -i input.pdf --log-file ./log.txt`                                                                      |
| `--config`                      | The path to the configuration file.                                                       | `pdf2zh_next -i input.pdf --config ./config.yaml`                                                                     |
| `-h`, `--help`                  | Show this help message and exit.                                                         | `pdf2zh_next -h`                                                                                                      |

---

### OUTPUT

| `--version`                     | バージョンを表示して終了                                                                 | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-i`, `--input`                 | 入力ファイルまたはディレクトリのパス。                                                    | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output`                | 出力ファイルまたはディレクトリのパス。                                                    | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-f`, `--force`                 | 出力ファイルが存在する場合、強制的に上書きする。                                           | `pdf2zh_next -i input.pdf -o output.pdf -f`                                                                           |
| `-l`, `--language`              | 翻訳の対象言語。                                                                         | `pdf2zh_next -i input.pdf -l ja`                                                                                      |
| `-t`, `--translator`            | 使用する翻訳サービス（Google、OpenAI など）。                                             | `pdf2zh_next -i input.pdf -t google`                                                                                  |
| `--api-key`                     | 翻訳サービスの API キー。                                                                 | `pdf2zh_next -i input.pdf -t openai --api-key YOUR_OPENAI_API_KEY`                                                    |
| `--model`                       | 翻訳サービスで使用するモデル。                                                            | `pdf2zh_next -i input.pdf -t openai --model gpt-4o`                                                                  |
| `--base-url`                    | 翻訳サービスのベース URL。                                                                | `pdf2zh_next -i input.pdf -t openai --base-url https://api.openai.com/v1`                                             |
| `--proxy`                       | 翻訳サービスで使用するプロキシ。                                                          | `pdf2zh_next -i input.pdf -t google --proxy http://127.0.0.1:7890`                                                   |
| `-p`, `--preserve-formatting`   | テキストの元の書式を保持する。                                                            | `pdf2zh_next -i input.pdf -p`                                                                                         |
| `-c`, `--concurrency`           | 翻訳サービスへの同時リクエスト数。                                                        | `pdf2zh_next -i input.pdf -c 10`                                                                                      |
| `-s`, `--size-limit`            | 翻訳サービスへの各リクエストのサイズ制限（トークン単位）。                                | `pdf2zh_next -i input.pdf -s 1000`                                                                                    |
| `--timeout`                     | 翻訳サービスへの各リクエストのタイムアウト（秒単位）。                                     | `pdf2zh_next -i input.pdf --timeout 10`                                                                               |
| `--retry`                       | 翻訳サービスへの各リクエストのリトライ回数。                                               | `pdf2zh_next -i input.pdf --retry 3`                                                                                  |
| `--retry-delay`                 | 翻訳サービスへの各リクエストのリトライ間隔（秒単位）。                                     | `pdf2zh_next -i input.pdf --retry-delay 1`                                                                            |
| `--no-cache`                    | 翻訳サービスのキャッシュを無効にする。                                                    | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir`                   | 翻訳サービスのキャッシュを保存するディレクトリ。                                           | `pdf2zh_next -i input.pdf --cache-dir ./cache`                                                                        |
| `--log-level`                   | アプリケーションのログレベル。                                                            | `pdf2zh_next -i input.pdf --log-level debug`                                                                          |
| `--log-file`                    | アプリケーションのログを保存するファイル。                                                 | `pdf2zh_next -i input.pdf --log-file ./log.txt`                                                                      |
| `--config`                      | 設定ファイルのパス。                                                                     | `pdf2zh_next -i input.pdf --config ./config.yaml`                                                                     |
| `-h`, `--help`                  | このヘルプメッセージを表示して終了。                                                      | `pdf2zh_next -h`                                                                                                      |
`--pages` オプションを使用すると、翻訳するページを指定できます。ページ範囲は `1,2,1-,-3,3-5` のように指定します。 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `--output`                      | Specify the output file name                                                            | `pdf2zh_next example.pdf --output example_translated.pdf`                                                              | 出力ファイル名を指定します。                                                                                    |
| `--output-type`                 | Specify the output file type                                                            | `pdf2zh_next example.pdf --output-type docx`                                                                           | 出力ファイルの種類を指定します。サポートされている形式は `pdf`、`docx`、`txt`、`markdown` です。               |
| `--model`                       | Specify the translation model                                                           | `pdf2zh_next example.pdf --model gpt-4o`                                                                               | 翻訳モデルを指定します。デフォルトは `gpt-4o` です。                                                            |
| `--source-language`             | Specify the source language                                                             | `pdf2zh_next example.pdf --source-language en`                                                                         | ソース言語を指定します。デフォルトは `auto` です。                                                              |
| `--target-language`             | Specify the target language                                                             | `pdf2zh_next example.pdf --target-language zh`                                                                         | ターゲット言語を指定します。デフォルトは `zh` です。                                                            |
| `--proxy`                       | Specify the proxy server address                                                        | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | プロキシサーバーのアドレスを指定します。                                                                        |
| `--api-key`                     | Specify the API key                                                                     | `pdf2zh_next example.pdf --api-key sk-xxxxxx`                                                                          | API キーを指定します。                                                                                          |
| `--api-base`                    | Specify the API base URL                                                                | `pdf2zh_next example.pdf --api-base https://api.openai.com`                                                            | API ベース URL を指定します。                                                                                   |
| `--retry`                       | Specify the number of retries for failed translations                                   | `pdf2zh_next example.pdf --retry 5`                                                                                    | 翻訳失敗時のリトライ回数を指定します。デフォルトは `3` です。                                                   |
| `--timeout`                     | Specify the timeout for each translation request                                         | `pdf2zh_next example.pdf --timeout 300`                                                                                | 各翻訳リクエストのタイムアウトを秒単位で指定します。デフォルトは `300` です。                                    |
| `--concurrent`                  | Specify the number of concurrent translation requests                                   | `pdf2zh_next example.pdf --concurrent 5`                                                                                | 同時翻訳リクエスト数を指定します。デフォルトは `3` です。                                                        |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                   | キャッシュを無効にします。                                                                                      |
| `--cache-dir`                   | Specify the cache directory                                                             | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          | キャッシュディレクトリを指定します。デフォルトは `./cache` です。                                                |
| `--log-level`                   | Specify the log level                                                                   | `pdf2zh_next example.pdf --log-level debug`                                                                            | ログレベルを指定します。オプションは `debug`、`info`、`warning`、`error` です。デフォルトは `info` です。       |
| `--help`                        | Show help information                                                                   | `pdf2zh_next --help`                                                                                                   | ヘルプ情報を表示します。                                                                                        |

---

### TRANSLATION RESULT

| `--pages`                       | 部分的な文書翻訳                                                             | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | `--pages` オプションを使用すると、翻訳するページを指定できます。ページ範囲は `1,2,1-,-3,3-5` のように指定します。 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `--output`                      | 出力ファイル名を指定                                                              | `pdf2zh_next example.pdf --output example_translated.pdf`                                                              | 出力ファイル名を指定します。                                                                                    |
| `--output-type`                 | 出力ファイルの種類を指定                                                            | `pdf2zh_next example.pdf --output-type docx`                                                                           | 出力ファイルの種類を指定します。サポートされている形式は `pdf`、`docx`、`txt`、`markdown` です。               |
| `--model`                       | 翻訳モデルを指定                                                           | `pdf2zh_next example.pdf --model gpt-4o`                                                                               | 翻訳モデルを指定します。デフォルトは `gpt-4o` です。                                                            |
| `--source-language`             | ソース言語を指定                                                             | `pdf2zh_next example.pdf --source-language en`                                                                         | ソース言語を指定します。デフォルトは `auto` です。                                                              |
| `--target-language`             | ターゲット言語を指定                                                             | `pdf2zh_next example.pdf --target-language zh`                                                                         | ターゲット言語を指定します。デフォルトは `zh` です。                                                            |
| `--proxy`                       | プロキシサーバーのアドレスを指定                                                        | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | プロキシサーバーのアドレスを指定します。                                                                        |
| `--api-key`                     | API キーを指定                                                                     | `pdf2zh_next example.pdf --api-key sk-xxxxxx`                                                                          | API キーを指定します。                                                                                          |
| `--api-base`                    | API ベース URL を指定                                                                | `pdf2zh_next example.pdf --api-base https://api.openai.com`                                                            | API ベース URL を指定します。                                                                                   |
| `--retry`                       | 翻訳失敗時のリトライ回数を指定                                   | `pdf2zh_next example.pdf --retry 5`                                                                                    | 翻訳失敗時のリトライ回数を指定します。デフォルトは `3` です。                                                   |
| `--timeout`                     | 各翻訳リクエストのタイムアウトを秒単位で指定                                         | `pdf2zh_next example.pdf --timeout 300`                                                                                | 各翻訳リクエストのタイムアウトを秒単位で指定します。デフォルトは `300` です。                                    |
| `--concurrent`                  | 同時翻訳リクエスト数を指定                                   | `pdf2zh_next example.pdf --concurrent 5`                                                                                | 同時翻訳リクエスト数を指定します。デフォルトは `3` です。                                                        |
| `--no-cache`                    | キャッシュを無効にします                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                   | キャッシュを無効にします。                                                                                      |
| `--cache-dir`                   | キャッシュディレクトリを指定                                                             | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          | キャッシュディレクトリを指定します。デフォルトは `./cache` です。                                                |
| `--log-level`                   | ログレベルを指定                                                                   | `pdf2zh_next example.pdf --log-level debug`                                                                            | ログレベルを指定します。オプションは `debug`、`info`、`warning`、`error` です。デフォルトは `info` です。       |
| `--help`                        | ヘルプ情報を表示                                                                   | `pdf2zh_next --help`                                                                                                   | ヘルプ情報を表示します。                                                                                        |
`auto`, `en`, `zh`, ... |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               | `en`, `zh`, `ja`, ...   |
| `--translator`                  | Translation service name                                                                | `pdf2zh_next example.pdf --translator google`                                                                         | `google`, `openai`, ... |
| `--model`                       | Model name used by the translation service                                              | `pdf2zh_next example.pdf --translator openai --model gpt-4o-mini`                                                     | `gpt-4o-mini`, ...      |
| `--api-key`                     | API key for the translation service                                                     | `pdf2zh_next example.pdf --translator openai --api-key YOUR_API_KEY`                                                  |                         |
| `--api-base`                    | API base URL for the translation service                                                | `pdf2zh_next example.pdf --translator openai --api-base https://api.example.com`                                      |                         |
| `--context-window`              | Context window size for the translation model (in tokens)                               | `pdf2zh_next example.pdf --translator openai --context-window 4096`                                                   |                         |
| `--max-tokens`                  | Maximum tokens per request for the translation model                                    | `pdf2zh_next example.pdf --translator openai --max-tokens 2048`                                                       |                         |
| `--batch-size`                  | Number of sentences processed in one batch                                              | `pdf2zh_next example.pdf --batch-size 10`                                                                             |                         |
| `--batch-delay`                 | Delay between batch requests (in seconds)                                               | `pdf2zh_next example.pdf --batch-delay 1`                                                                             |                         |
| `--concurrent-requests`         | Number of concurrent requests for translation                                           | `pdf2zh_next example.pdf --concurrent-requests 3`                                                                     |                         |
| `--retry-attempts`              | Number of retry attempts for failed requests                                            | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          |                         |
| `--retry-delay`                 | Delay between retry attempts (in seconds)                                               | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |                         |
| `--timeout`                     | Timeout for each request (in seconds)                                                   | `pdf2zh_next example.pdf --timeout 30`                                                                                |                         |
| `--output`                      | Output file path                                                                        | `pdf2zh_next example.pdf --output example_translated.pdf`                                                             |                         |
| `--output-format`               | Output format                                                                           | `pdf2zh_next example.pdf --output-format pdf`                                                                         | `pdf`, `markdown`       |
| `--output-layout`               | Output layout                                                                           | `pdf2zh_next example.pdf --output-layout single-column`                                                               | `single-column`, `two-columns`, `original` |
| `--font-family`                 | Font family for the output PDF                                                          | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |                         |
| `--font-size`                   | Font size for the output PDF                                                            | `pdf2zh_next example.pdf --font-size 12`                                                                              |                         |
| `--line-spacing`                | Line spacing for the output PDF                                                         | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |                         |
| `--margin`                      | Margin size for the output PDF (in points)                                              | `pdf2zh_next example.pdf --margin 72`                                                                                 |                         |
| `--color-scheme`                | Color scheme for the output PDF                                                         | `pdf2zh_next example.pdf --color-scheme light`                                                                        | `light`, `dark`         |
| `--target-audience`             | Target audience for translation                                                         | `pdf2zh_next example.pdf --target-audience general`                                                                   | `general`, `academic`, `technical`, `business` |
| `--formality`                   | Formality level for translation                                                         | `pdf2zh_next example.pdf --formality formal`                                                                          | `formal`, `informal`    |
| `--glossary`                    | Glossary file path for custom translations                                              | `pdf2zh_next example.pdf --glossary glossary.txt`                                                                     |                         |
| `--exclude-elements`            | Elements to exclude from translation                                                    | `pdf2zh_next example.pdf --exclude-elements "code,table"`                                                             |                         |
| `--include-elements`            | Elements to include in translation                                                      | `pdf2zh_next example.pdf --include-elements "text,list"`                                                              |                         |
| `--preserve-formatting`         | Preserve original formatting in translation                                             | `pdf2zh_next example.pdf --preserve-formatting`                                                                       |                         |
| `--preserve-links`              | Preserve hyperlinks in translation                                                      | `pdf2zh_next example.pdf --preserve-links`                                                                            |                         |
| `--preserve-images`             | Preserve images in translation                                                          | `pdf2zh_next example.pdf --preserve-images`                                                                           |                         |
| `--preserve-tables`             | Preserve tables in translation                                                          | `pdf2zh_next example.pdf --preserve-tables`                                                                           |                         |
| `--debug`                       | Enable debug mode                                                                       | `pdf2zh_next example.pdf --debug`                                                                                     |                         |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   |                         |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |                         |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |                         |

---

### OUTPUT

| `--lang-in`                     | ソース言語コード                                                                        | `pdf2zh_next example.pdf --lang-in en`                                                                                | `auto`, `en`, `zh`, ... |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--lang-out`                    | ターゲット言語コード                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               | `en`, `zh`, `ja`, ...   |
| `--translator`                  | 翻訳サービス名                                                                          | `pdf2zh_next example.pdf --translator google`                                                                         | `google`, `openai`, ... |
| `--model`                       | 翻訳サービスで使用するモデル名                                                          | `pdf2zh_next example.pdf --translator openai --model gpt-4o-mini`                                                     | `gpt-4o-mini`, ...      |
| `--api-key`                     | 翻訳サービスの API キー                                                                 | `pdf2zh_next example.pdf --translator openai --api-key YOUR_API_KEY`                                                  |                         |
| `--api-base`                    | 翻訳サービスの API ベース URL                                                           | `pdf2zh_next example.pdf --translator openai --api-base https://api.example.com`                                      |                         |
| `--context-window`              | 翻訳モデルのコンテキストウィンドウサイズ（トークン単位）                                | `pdf2zh_next example.pdf --translator openai --context-window 4096`                                                   |                         |
| `--max-tokens`                  | 翻訳モデルのリクエストごとの最大トークン数                                              | `pdf2zh_next example.pdf --translator openai --max-tokens 2048`                                                       |                         |
| `--batch-size`                  | 1 バッチで処理する文の数                                                                | `pdf2zh_next example.pdf --batch-size 10`                                                                             |                         |
| `--batch-delay`                 | バッチリクエスト間の遅延（秒単位）                                                      | `pdf2zh_next example.pdf --batch-delay 1`                                                                             |                         |
| `--concurrent-requests`         | 翻訳の同時リクエスト数                                                                  | `pdf2zh_next example.pdf --concurrent-requests 3`                                                                     |                         |
| `--retry-attempts`              | 失敗したリクエストの再試行回数                                                          | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          |                         |
| `--retry-delay`                 | 再試行間の遅延（秒単位）                                                                | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |                         |
| `--timeout`                     | 各リクエストのタイムアウト（秒単位）                                                    | `pdf2zh_next example.pdf --timeout 30`                                                                                |                         |
| `--output`                      | 出力ファイルパス                                                                        | `pdf2zh_next example.pdf --output example_translated.pdf`                                                             |                         |
| `--output-format`               | 出力フォーマット                                                                        | `pdf2zh_next example.pdf --output-format pdf`                                                                         | `pdf`, `markdown`       |
| `--output-layout`               | 出力レイアウト                                                                          | `pdf2zh_next example.pdf --output-layout single-column`                                                               | `single-column`, `two-columns`, `original` |
| `--font-family`                 | 出力 PDF のフォントファミリー                                                           | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |                         |
| `--font-size`                   | 出力 PDF のフォントサイズ                                                               | `pdf2zh_next example.pdf --font-size 12`                                                                              |                         |
| `--line-spacing`                | 出力 PDF の行間                                                                         | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |                         |
| `--margin`                      | 出力 PDF の余白サイズ（ポイント単位）                                                   | `pdf2zh_next example.pdf --margin 72`                                                                                 |                         |
| `--color-scheme`                | 出力 PDF のカラースキーム                                                               | `pdf2zh_next example.pdf --color-scheme light`                                                                        | `light`, `dark`         |
| `--target-audience`             | 翻訳のターゲットオーディエンス                                                          | `pdf2zh_next example.pdf --target-audience general`                                                                   | `general`, `academic`, `technical`, `business` |
| `--formality`                   | 翻訳のフォーマリティレベル                                                              | `pdf2zh_next example.pdf --formality formal`                                                                          | `formal`, `informal`    |
| `--glossary`                    | カスタム翻訳用の用語集ファイルパス                                                      | `pdf2zh_next example.pdf --glossary glossary.txt`                                                                     |                         |
| `--exclude-elements`            | 翻訳から除外する要素                                                                    | `pdf2zh_next example.pdf --exclude-elements "code,table"`                                                             |                         |
| `--include-elements`            | 翻訳に含める要素                                                                        | `pdf2zh_next example.pdf --include-elements "text,list"`                                                              |                         |
| `--preserve-formatting`         | 翻訳で元のフォーマットを保持する                                                        | `pdf2zh_next example.pdf --preserve-formatting`                                                                       |                         |
| `--preserve-links`              | 翻訳でハイパーリンクを保持する                                                          | `pdf2zh_next example.pdf --preserve-links`                                                                            |                         |
| `--preserve-images`             | 翻訳で画像を保持する                                                                    | `pdf2zh_next example.pdf --preserve-images`                                                                           |                         |
| `--preserve-tables`             | 翻訳でテーブルを保持する                                                                | `pdf2zh_next example.pdf --preserve-tables`                                                                           |                         |
| `--debug`                       | デバッグモードを有効にする                                                              | `pdf2zh_next example.pdf --debug`                                                                                     |                         |
| `--verbose`                     | 詳細な出力を有効にする                                                                  | `pdf2zh_next example.pdf --verbose`                                                                                   |                         |
| `--version`                     | バージョン情報を表示する                                                                | `pdf2zh_next --version`                                                                                               |                         |
| `--help`                        | ヘルプメッセージを表示する                                                              | `pdf2zh_next --help`                                                                                                  |                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | Source language code                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN --lang-in en`                                                                |
| `--service`                     | Translation service, default is `google`                                                | `pdf2zh_next example.pdf --lang-out zh-CN --service google`                                                             |
| `--translator-args`             | Additional arguments for the translator, in JSON format                                 | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args '{"timeout": 10, "proxies": {"https": "localhost:7890"}}'` |
| `--translator-args-proxy-https` | Shortcut for setting HTTPS proxy for translator                                         | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-proxy-https localhost:7890`                                |
| `--translator-args-proxy-http`  | Shortcut for setting HTTP proxy for translator                                          | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-proxy-http localhost:7890`                                 |
| `--translator-args-timeout`     | Shortcut for setting timeout for translator                                             | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-timeout 10`                                                 |
| `--translator-args-fallback`    | Fallback service when primary service fails, default is `google`                        | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-fallback google`                                            |
| `--translator-args-retries`     | Number of retries for translation requests, default is 3                                | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-retries 5`                                                  |
| `--translator-args-delay`       | Delay between retries in seconds, default is 1                                          | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-delay 2`                                                    |
| `--translator-args-verbose`     | Enable verbose logging for translator, default is false                                 | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-verbose`                                                    |
| `--translator-args-raise-error` | Raise error when translation fails, default is false                                    | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-raise-error`                                                |

---

### TRANSLATION RESULT

| `--lang-out`                    | ターゲット言語コード                                                                     | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | ソース言語コード                                                                         | `pdf2zh_next example.pdf --lang-out zh-CN --lang-in en`                                                                |
| `--service`                     | 翻訳サービス、デフォルトは `google`                                                       | `pdf2zh_next example.pdf --lang-out zh-CN --service google`                                                             |
| `--translator-args`             | 翻訳機用の追加引数、JSON 形式で指定                                                        | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args '{"timeout": 10, "proxies": {"https": "localhost:7890"}}'` |
| `--translator-args-proxy-https` | 翻訳機用 HTTPS プロキシ設定のショートカット                                                 | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-proxy-https localhost:7890`                                |
| `--translator-args-proxy-http`  | 翻訳機用 HTTP プロキシ設定のショートカット                                                  | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-proxy-http localhost:7890`                                 |
| `--translator-args-timeout`     | 翻訳機用タイムアウト設定のショートカット                                                    | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-timeout 10`                                                 |
| `--translator-args-fallback`    | プライマリサービスが失敗した際のフォールバックサービス、デフォルトは `google`               | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-fallback google`                                            |
| `--translator-args-retries`     | 翻訳リクエストのリトライ回数、デフォルトは 3                                               | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-retries 5`                                                  |
| `--translator-args-delay`       | リトライ間の遅延（秒）、デフォルトは 1                                                     | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-delay 2`                                                    |
| `--translator-args-verbose`     | 翻訳機用詳細ログ出力の有効化、デフォルトは false                                           | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-verbose`                                                    |
| `--translator-args-raise-error` | 翻訳失敗時にエラーを発生させる、デフォルトは false                                         | `pdf2zh_next example.pdf --lang-out zh-CN --translator-args-raise-error`                                                |
| `--min-text-length`             | 翻訳する最小テキスト長                                                        | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| `--rpc-ocr`                     | RPC service host address for OCR                                                       | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8000`                                                             |
| `--rpc-translate`               | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8000`                                                       |

---

### OUTPUT

| `--rpc-doclayout`               | 文書レイアウト分析のための RPC サービスホストアドレス                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| `--rpc-ocr`                     | OCR のための RPC サービスホストアドレス                                                 | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8000`                                                             |
| `--rpc-translate`               | 翻訳のための RPC サービスホストアドレス                                                  | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8000`                                                       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--proxy`                       | Use proxy for translation service                                                       | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--no-merge`                    | Do not merge the text blocks after translation, which may result in more accurate layout | `pdf2zh_next example.pdf --no-merge`                                                                                  |
| `--no-ocr`                      | Do not perform OCR on the PDF, only translate the existing text                         | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--ocr-lang`                    | Specify the OCR language, default is `eng` (English)                                    | `pdf2zh_next example.pdf --ocr-lang jpn`                                                                              |
| `--ocr-dpi`                     | Specify the DPI for OCR, default is `300`                                               | `pdf2zh_next example.pdf --ocr-dpi 600`                                                                               |
| `--ocr-timeout`                 | Specify the timeout for OCR in seconds, default is `600`                                | `pdf2zh_next example.pdf --ocr-timeout 1200`                                                                          |
| `--ocr-max-workers`             | Specify the maximum number of workers for OCR, default is `4`                           | `pdf2zh_next example.pdf --ocr-max-workers 8`                                                                         |
| `--ocr-engine`                  | Specify the OCR engine, `easyocr` or `tesseract`, default is `easyocr`                  | `pdf2zh_next example.pdf --ocr-engine tesseract`                                                                      |
| `--cache-dir`                   | Specify the cache directory                                                             | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--force`                       | Force overwrite existing output file                                                    | `pdf2zh_next example.pdf --force`                                                                                     |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help information                                                                   | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATED TEXT

| `--qps`                         | 翻訳サービスの QPS 制限                                                                 | `pdf2zh_next example.pdf --qps 200`                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--proxy`                       | 翻訳サービスにプロキシを使用                                                             | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--no-merge`                    | 翻訳後にテキストブロックを結合しない（より正確なレイアウトが得られる可能性があります）       | `pdf2zh_next example.pdf --no-merge`                                                                                  |
| `--no-ocr`                      | PDF に対して OCR を実行せず、既存のテキストのみを翻訳                                    | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--ocr-lang`                    | OCR の言語を指定（デフォルトは `eng`（英語））                                           | `pdf2zh_next example.pdf --ocr-lang jpn`                                                                              |
| `--ocr-dpi`                     | OCR の DPI を指定（デフォルトは `300`）                                                  | `pdf2zh_next example.pdf --ocr-dpi 600`                                                                               |
| `--ocr-timeout`                 | OCR のタイムアウトを秒単位で指定（デフォルトは `600`）                                   | `pdf2zh_next example.pdf --ocr-timeout 1200`                                                                          |
| `--ocr-max-workers`             | OCR の最大ワーカー数を指定（デフォルトは `4`）                                           | `pdf2zh_next example.pdf --ocr-max-workers 8`                                                                         |
| `--ocr-engine`                  | OCR エンジンを指定（`easyocr` または `tesseract`、デフォルトは `easyocr`）               | `pdf2zh_next example.pdf --ocr-engine tesseract`                                                                      |
| `--cache-dir`                   | キャッシュディレクトリを指定                                                             | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `--no-cache`                    | キャッシュを無効化                                                                       | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--force`                       | 既存の出力ファイルを強制的に上書き                                                         | `pdf2zh_next example.pdf --force`                                                                                     |
| `--version`                     | バージョン情報を表示                                                                     | `pdf2zh_next --version`                                                                                               |
| `--help`                        | ヘルプ情報を表示                                                                         | `pdf2zh_next --help`                                                                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--ignore-translated`           | Ignore translated text                                                                  | `pdf2zh_next example.pdf --ignore-translated`                                                                         |
| `--ignore-math`                 | Ignore math formulas                                                                    | `pdf2zh_next example.pdf --ignore-math`                                                                               |
| `--ignore-figure`               | Ignore figures                                                                          | `pdf2zh_next example.pdf --ignore-figure`                                                                             |
| `--ignore-table`                | Ignore tables                                                                           | `pdf2zh_next example.pdf --ignore-table`                                                                              |
| `--ignore-code`                 | Ignore code blocks                                                                      | `pdf2zh_next example.pdf --ignore-code`                                                                               |
| `--ignore-text`                 | Ignore text                                                                             | `pdf2zh_next example.pdf --ignore-text`                                                                               |
| `--ignore-title`                | Ignore titles                                                                           | `pdf2zh_next example.pdf --ignore-title`                                                                              |
| `--ignore-footnote`             | Ignore footnotes                                                                        | `pdf2zh_next example.pdf --ignore-footnote`                                                                           |
| `--ignore-page-number`          | Ignore page numbers                                                                     | `pdf2zh_next example.pdf --ignore-page-number`                                                                        |
| `--ignore-reference`            | Ignore references                                                                       | `pdf2zh_next example.pdf --ignore-reference`                                                                          |
| `--ignore-bib`                  | Ignore bibliography                                                                     | `pdf2zh_next example.pdf --ignore-bib`                                                                                |
| `--ignore-abstract`             | Ignore abstract                                                                         | `pdf2zh_next example.pdf --ignore-abstract`                                                                           |
| `--ignore-author`               | Ignore author names                                                                     | `pdf2zh_next example.pdf --ignore-author`                                                                             |
| `--ignore-date`                 | Ignore dates                                                                            | `pdf2zh_next example.pdf --ignore-date`                                                                               |
| `--ignore-email`                | Ignore emails                                                                           | `pdf2zh_next example.pdf --ignore-email`                                                                              |
| `--ignore-url`                  | Ignore URLs                                                                             | `pdf2zh_next example.pdf --ignore-url`                                                                                |
| `--ignore-phone`                | Ignore phone numbers                                                                    | `pdf2zh_next example.pdf --ignore-phone`                                                                              |
| `--ignore-address`              | Ignore addresses                                                                        | `pdf2zh_next example.pdf --ignore-address`                                                                            |
| `--ignore-postcode`             | Ignore postcodes                                                                        | `pdf2zh_next example.pdf --ignore-postcode`                                                                           |
| `--ignore-country`              | Ignore countries                                                                        | `pdf2zh_next example.pdf --ignore-country`                                                                            |
| `--ignore-currency`             | Ignore currencies                                                                       | `pdf2zh_next example.pdf --ignore-currency`                                                                           |
| `--ignore-other`                | Ignore other content                                                                    | `pdf2zh_next example.pdf --ignore-other`                                                                              |
| `--ignore-custom`               | Ignore custom content                                                                   | `pdf2zh_next example.pdf --ignore-custom`                                                                             |
| `--ignore-all`                  | Ignore all content                                                                      | `pdf2zh_next example.pdf --ignore-all`                                                                                |
| `--ignore-none`                 | Ignore nothing                                                                          | `pdf2zh_next example.pdf --ignore-none`                                                                               |
| `--ignore-list`                 | Ignore list of content                                                                  | `pdf2zh_next example.pdf --ignore-list cache,math,figure,table,code,text,title,footnote,page-number,reference,bib,abstract,author,date,email,url,phone,address,postcode,country,currency,other,custom` |

---

### OUTPUT

| `--ignore-cache`                | 翻訳キャッシュを無視                                                                     | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| :------------------------------ | :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--ignore-translated`           | 翻訳済みテキストを無視                                                                   | `pdf2zh_next example.pdf --ignore-translated`                                                                         |
| `--ignore-math`                 | 数式を無視                                                                               | `pdf2zh_next example.pdf --ignore-math`                                                                               |
| `--ignore-figure`               | 図を無視                                                                                 | `pdf2zh_next example.pdf --ignore-figure`                                                                             |
| `--ignore-table`                | 表を無視                                                                                 | `pdf2zh_next example.pdf --ignore-table`                                                                              |
| `--ignore-code`                 | コードブロックを無視                                                                     | `pdf2zh_next example.pdf --ignore-code`                                                                               |
| `--ignore-text`                 | テキストを無視                                                                           | `pdf2zh_next example.pdf --ignore-text`                                                                               |
| `--ignore-title`                | タイトルを無視                                                                           | `pdf2zh_next example.pdf --ignore-title`                                                                              |
| `--ignore-footnote`             | 脚注を無視                                                                               | `pdf2zh_next example.pdf --ignore-footnote`                                                                           |
| `--ignore-page-number`          | ページ番号を無視                                                                         | `pdf2zh_next example.pdf --ignore-page-number`                                                                        |
| `--ignore-reference`            | 参考文献を無視                                                                           | `pdf2zh_next example.pdf --ignore-reference`                                                                          |
| `--ignore-bib`                  | 参考文献リストを無視                                                                     | `pdf2zh_next example.pdf --ignore-bib`                                                                                |
| `--ignore-abstract`             | 要約を無視                                                                               | `pdf2zh_next example.pdf --ignore-abstract`                                                                           |
| `--ignore-author`               | 著者名を無視                                                                             | `pdf2zh_next example.pdf --ignore-author`                                                                             |
| `--ignore-date`                 | 日付を無視                                                                               | `pdf2zh_next example.pdf --ignore-date`                                                                               |
| `--ignore-email`                | メールアドレスを無視                                                                     | `pdf2zh_next example.pdf --ignore-email`                                                                              |
| `--ignore-url`                  | URL を無視                                                                               | `pdf2zh_next example.pdf --ignore-url`                                                                                |
| `--ignore-phone`                | 電話番号を無視                                                                           | `pdf2zh_next example.pdf --ignore-phone`                                                                              |
| `--ignore-address`              | 住所を無視                                                                               | `pdf2zh_next example.pdf --ignore-address`                                                                            |
| `--ignore-postcode`             | 郵便番号を無視                                                                           | `pdf2zh_next example.pdf --ignore-postcode`                                                                           |
| `--ignore-country`              | 国名を無視                                                                               | `pdf2zh_next example.pdf --ignore-country`                                                                            |
| `--ignore-currency`             | 通貨を無視                                                                               | `pdf2zh_next example.pdf --ignore-currency`                                                                           |
| `--ignore-other`                | その他のコンテンツを無視                                                                 | `pdf2zh_next example.pdf --ignore-other`                                                                              |
| `--ignore-custom`               | カスタムコンテンツを無視                                                                 | `pdf2zh_next example.pdf --ignore-custom`                                                                             |
| `--ignore-all`                  | すべてのコンテンツを無視                                                                 | `pdf2zh_next example.pdf --ignore-all`                                                                                |
| `--ignore-none`                 | 何も無視しない                                                                           | `pdf2zh_next example.pdf --ignore-none`                                                                               |
| `--ignore-list`                 | 無視するコンテンツのリスト                                                               | `pdf2zh_next example.pdf --ignore-list cache,math,figure,table,code,text,title,footnote,page-number,reference,bib,abstract,author,date,email,url,phone,address,postcode,country,currency,other,custom` |
---

### OUTPUT

| `--custom-system-prompt`        | 翻訳用のカスタムシステムプロンプト。Qwen 3 の `/no_think` で使用されます                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-fallback`           | Fallback to original text if no match found in glossary.                                | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fallback`                                            |
| `--glossary-case-sensitive`     | Enable case-sensitive matching for glossary entries.                                    | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-case-sensitive`                                      |
| `--glossary-whole-words`        | Match only whole words in glossary entries.                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-whole-words`                                         |
| `--glossary-fuzzy`              | Enable fuzzy matching for glossary entries.                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy`                                               |
| `--glossary-fuzzy-threshold`    | Set the similarity threshold for fuzzy matching (0.0-1.0). Default is 0.8.              | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-threshold 0.9`                |
| `--glossary-fuzzy-max-candidates` | Set the maximum number of candidate matches for fuzzy matching. Default is 10.          | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-max-candidates 5`             |
| `--glossary-fuzzy-max-edit-distance` | Set the maximum edit distance for fuzzy matching. Default is 3.                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-max-edit-distance 2`          |
| `--glossary-fuzzy-min-length`   | Set the minimum length of words to apply fuzzy matching. Default is 3.                  | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-min-length 4`                 |
| `--glossary-fuzzy-prefix`       | Require matching prefix for fuzzy matching.                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-prefix`                       |
| `--glossary-fuzzy-suffix`       | Require matching suffix for fuzzy matching.                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-suffix`                       |

---

### TRANSLATION RESULT

| `--glossaries`                  | 用語集ファイルのリスト。                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-fallback`           | 用語集で一致するものが見つからない場合、元のテキストにフォールバックします。                                | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fallback`                                            |
| `--glossary-case-sensitive`     | 用語集エントリの大文字と小文字を区別したマッチングを有効にします。                                    | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-case-sensitive`                                      |
| `--glossary-whole-words`        | 用語集エントリで完全一致する単語のみをマッチングします。                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-whole-words`                                         |
| `--glossary-fuzzy`              | 用語集エントリのあいまいマッチングを有効にします。                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy`                                               |
| `--glossary-fuzzy-threshold`    | あいまいマッチングの類似度閾値を設定します（0.0 ～ 1.0）。デフォルトは 0.8。              | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-threshold 0.9`                |
| `--glossary-fuzzy-max-candidates` | あいまいマッチングの候補マッチの最大数を設定します。デフォルトは 10。          | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-max-candidates 5`             |
| `--glossary-fuzzy-max-edit-distance` | あいまいマッチングの最大編集距離を設定します。デフォルトは 3。                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-max-edit-distance 2`          |
| `--glossary-fuzzy-min-length`   | あいまいマッチングを適用する単語の最小長を設定します。デフォルトは 3。                  | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-min-length 4`                 |
| `--glossary-fuzzy-prefix`       | あいまいマッチングで接頭辞の一致を要求します。                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-prefix`                       |
| `--glossary-fuzzy-suffix`       | あいまいマッチングで接尾辞の一致を要求します。                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-fuzzy --glossary-fuzzy-suffix`                       |
---

### OUTPUT

| `--save-auto-extracted-glossary`| 自動的に抽出された用語集を保存する                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-workers-per-service` | Maximum number of workers for each translation service. If not set, will use `--pool-max-workers` | `pdf2zh_next example.pdf --pool-max-workers 100 --pool-max-workers-per-service 20`                         |
| `--pool-qps`                     | QPS (Queries Per Second) for translation pool. If not set, will use `10`                          | `pdf2zh_next example.pdf --pool-qps 10`                                                                    |
| `--pool-qps-per-service`         | QPS for each translation service. If not set, will use `--pool-qps`                               | `pdf2zh_next example.pdf --pool-qps 10 --pool-qps-per-service 5`                                           |
| `--pool-max-retries`             | Maximum retries for each translation request. If not set, will use `3`                            | `pdf2zh_next example.pdf --pool-max-retries 5`                                                             |
| `--pool-timeout`                 | Timeout for each translation request in seconds. If not set, will use `10`                        | `pdf2zh_next example.pdf --pool-timeout 30`                                                                |
| `--pool-proxy`                   | Proxy for translation pool. If not set, will use system proxy or no proxy                         | `pdf2zh_next example.pdf --pool-proxy "http://127.0.0.1:7890"`                                             |
| `--pool-proxy-per-service`       | Proxy for each translation service. If not set, will use `--pool-proxy`                           | `pdf2zh_next example.pdf --pool-proxy "http://127.0.0.1:7890" --pool-proxy-per-service "socks5://127.0.0.1:7891"` |

---

### OUTPUT

| `--pool-max-workers`            | 翻訳プールの最大ワーカー数。設定されていない場合、qps がワーカー数として使用されます | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-workers-per-service` | 各翻訳サービスの最大ワーカー数。設定されていない場合、`--pool-max-workers` が使用されます | `pdf2zh_next example.pdf --pool-max-workers 100 --pool-max-workers-per-service 20`                         |
| `--pool-qps`                     | 翻訳プールの QPS（1 秒あたりのクエリ数）。設定されていない場合、`10` が使用されます                          | `pdf2zh_next example.pdf --pool-qps 10`                                                                    |
| `--pool-qps-per-service`         | 各翻訳サービスの QPS。設定されていない場合、`--pool-qps` が使用されます                               | `pdf2zh_next example.pdf --pool-qps 10 --pool-qps-per-service 5`                                           |
| `--pool-max-retries`             | 各翻訳リクエストの最大リトライ回数。設定されていない場合、`3` が使用されます                            | `pdf2zh_next example.pdf --pool-max-retries 5`                                                             |
| `--pool-timeout`                 | 各翻訳リクエストのタイムアウト（秒単位）。設定されていない場合、`10` が使用されます                        | `pdf2zh_next example.pdf --pool-timeout 30`                                                                |
| `--pool-proxy`                   | 翻訳プールのプロキシ。設定されていない場合、システムプロキシまたはプロキシなしが使用されます                         | `pdf2zh_next example.pdf --pool-proxy "http://127.0.0.1:7890"`                                             |
| `--pool-proxy-per-service`       | 各翻訳サービスのプロキシ。設定されていない場合、`--pool-proxy` が使用されます                           | `pdf2zh_next example.pdf --pool-proxy "http://127.0.0.1:7890" --pool-proxy-per-service "socks5://127.0.0.1:7891"` |
---

Let's begin.
| `--term-pool-max-workers`       | 用語抽出翻訳プールの最大ワーカー数。設定されていないか 0 の場合、pool_max_workers に従います。 | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
---

### TRANSLATION RESULT

| `--no-auto-extract-glossary`    | 自動用語抽出を無効にする                                                               | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| `--secondary-font-family`       | Override secondary font family for translated text. Choices are the same as `--primary-font-family`. If not specified, uses automatic font selection based on original text properties.                                               | `pdf2zh_next example.pdf --secondary-font-family serif` |
| `--font-family-mapping`         | Custom font family mapping rules in JSON format. Example: `'{"Times New Roman": "Source Han Serif", "Arial": "Source Han Sans"}'`                                                                                                      | `pdf2zh_next example.pdf --font-family-mapping '{"Times New Roman": "Source Han Serif", "Arial": "Source Han Sans"}'` |
| `--target-language`             | Target language code for translation. Default: `ja`. See [Supported Languages](supported-languages.md) for available options.                                                                                                          | `pdf2zh_next example.pdf --target-language zh-CN`      |
| `--service`                     | Translation service to use. Default: `google`. See [Documentation of Translation Services](translation-services.md) for available services.                                                                                            | `pdf2zh_next example.pdf --service openai`             |
| `--proxy`                       | Proxy URL for translation service requests. Example: `http://127.0.0.1:7890`                                                                                                                                                          | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890` |
| `--api-key`                     | API key for translation service (if required).                                                                                                                                                                                         | `pdf2zh_next example.pdf --service openai --api-key YOUR_API_KEY` |
| `--model`                       | Model name for translation service (if configurable).                                                                                                                                                                                  | `pdf2zh_next example.pdf --service openai --model gpt-4` |
| `--max-concurrent-requests`     | Maximum number of concurrent translation requests. Default: `10`.                                                                                                                                                                      | `pdf2zh_next example.pdf --max-concurrent-requests 20` |
| `--request-timeout`             | Timeout in seconds for each translation request. Default: `30`.                                                                                                                                                                        | `pdf2zh_next example.pdf --request-timeout 60`         |
| `--retry-attempts`              | Number of retry attempts for failed translation requests. Default: `3`.                                                                                                                                                                | `pdf2zh_next example.pdf --retry-attempts 5`           |
| `--retry-delay`                 | Delay in seconds between retry attempts. Default: `2`.                                                                                                                                                                                 | `pdf2zh_next example.pdf --retry-delay 5`              |
| `--batch-size`                  | Number of text segments to process in each translation batch. Default: `50`.                                                                                                                                                           | `pdf2zh_next example.pdf --batch-size 100`             |
| `--translation-cache`           | Enable or disable translation caching. Default: `true`.                                                                                                                                                                                | `pdf2zh_next example.pdf --translation-cache false`    |

---

### OUTPUT

| `--primary-font-family`         | 翻訳テキストのプライマリフォントファミリーを上書きします。選択肢：セリフフォントには「serif」、サンセリフフォントには「sans-serif」、スクリプト／イタリックフォントには「script」。指定しない場合、元のテキストプロパティに基づいて自動フォント選択を使用します。 | `pdf2zh_next example.pdf --primary-font-family serif` |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| `--secondary-font-family`       | 翻訳テキストのセカンダリフォントファミリーを上書きします。選択肢は `--primary-font-family` と同じです。指定しない場合、元のテキストプロパティに基づいて自動フォント選択を使用します。                                               | `pdf2zh_next example.pdf --secondary-font-family serif` |
| `--font-family-mapping`         | JSON 形式のカスタムフォントファミリーマッピングルール。例：`'{"Times New Roman": "Source Han Serif", "Arial": "Source Han Sans"}'`                                                                                                      | `pdf2zh_next example.pdf --font-family-mapping '{"Times New Roman": "Source Han Serif", "Arial": "Source Han Sans"}'` |
| `--target-language`             | 翻訳のターゲット言語コード。デフォルト：`ja`。利用可能なオプションについては [サポート言語](supported-languages.md) を参照してください。                                                                                                          | `pdf2zh_next example.pdf --target-language zh-CN`      |
| `--service`                     | 使用する翻訳サービス。デフォルト：`google`。利用可能なサービスについては [翻訳サービスドキュメント](translation-services.md) を参照してください。                                                                                            | `pdf2zh_next example.pdf --service openai`             |
| `--proxy`                       | 翻訳サービスリクエスト用のプロキシ URL。例：`http://127.0.0.1:7890`                                                                                                                                                          | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890` |
| `--api-key`                     | 翻訳サービスの API キー（必要な場合）。                                                                                                                                                                                         | `pdf2zh_next example.pdf --service openai --api-key YOUR_API_KEY` |
| `--model`                       | 翻訳サービスのモデル名（設定可能な場合）。                                                                                                                                                                                  | `pdf2zh_next example.pdf --service openai --model gpt-4` |
| `--max-concurrent-requests`     | 同時翻訳リクエストの最大数。デフォルト：`10`。                                                                                                                                                                      | `pdf2zh_next example.pdf --max-concurrent-requests 20` |
| `--request-timeout`             | 各翻訳リクエストのタイムアウト（秒）。デフォルト：`30`。                                                                                                                                                                        | `pdf2zh_next example.pdf --request-timeout 60`         |
| `--retry-attempts`              | 失敗した翻訳リクエストの再試行回数。デフォルト：`3`。                                                                                                                                                                | `pdf2zh_next example.pdf --retry-attempts 5`           |
| `--retry-delay`                 | 再試行間の遅延（秒）。デフォルト：`2`。                                                                                                                                                                                 | `pdf2zh_next example.pdf --retry-delay 5`              |
| `--batch-size`                  | 各翻訳バッチで処理するテキストセグメントの数。デフォルト：`50`。                                                                                                                                                           | `pdf2zh_next example.pdf --batch-size 100`             |
| `--translation-cache`           | 翻訳キャッシュを有効または無効にします。デフォルト：`true`。                                                                                                                                                                                | `pdf2zh_next example.pdf --translation-cache false`    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output <path>`               | Specify the output file path                                                            | `pdf2zh_next example.pdf --output translated.pdf`                                                                     |
| `--page-range <start> [<end>]`  | Specify the page range to translate (e.g., 1-5, 8, 11-13)                               | `pdf2zh_next example.pdf --page-range 1-5`                                                                            |
| `--remove-original`             | Remove the original PDF file after translation                                          | `pdf2zh_next example.pdf --remove-original`                                                                           |
| `--service <service>`           | Specify the translation service to use (e.g., google, deepl, openai)                    | `pdf2zh_next example.pdf --service deepl`                                                                             |
| `--target-lang <lang>`          | Specify the target language (e.g., zh, ja, en)                                          | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `--workers <num>`               | Specify the number of concurrent workers for translation (default: 3)                   | `pdf2zh_next example.pdf --workers 5`                                                                                 |
| `--yes`                         | Skip all confirmation prompts                                                           | `pdf2zh_next example.pdf --yes`                                                                                       |

---

### TRANSLATED TEXT

| `--no-dual`                     | バイリンガル PDF ファイルを出力しない                                                       | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output <path>`               | 出力ファイルのパスを指定する                                                            | `pdf2zh_next example.pdf --output translated.pdf`                                                                     |
| `--page-range <start> [<end>]`  | 翻訳するページ範囲を指定する（例：1-5, 8, 11-13）                               | `pdf2zh_next example.pdf --page-range 1-5`                                                                            |
| `--remove-original`             | 翻訳後に元の PDF ファイルを削除する                                          | `pdf2zh_next example.pdf --remove-original`                                                                           |
| `--service <service>`           | 使用する翻訳サービスを指定する（例：google, deepl, openai）                    | `pdf2zh_next example.pdf --service deepl`                                                                             |
| `--target-lang <lang>`          | ターゲット言語を指定する（例：zh, ja, en）                                          | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--version`                     | バージョン情報を表示する                                                                | `pdf2zh_next --version`                                                                                               |
| `--workers <num>`               | 翻訳用の同時実行ワーカー数を指定する（デフォルト：3）                   | `pdf2zh_next example.pdf --workers 5`                                                                                 |
| `--yes`                         | すべての確認プロンプトをスキップする                                                           | `pdf2zh_next example.pdf --yes`                                                                                       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-bilingual`                | Do not output bilingual PDF files                                                       | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--no-mono --no-bilingual`      | Do not output any PDF files, only output markdown files                                 | `pdf2zh_next example.pdf --no-mono --no-bilingual`                                                                    |
| `--only-translated-md`          | Only output the translated markdown files, do not output the original markdown files    | `pdf2zh_next example.pdf --only-translated-md`                                                                        |
| `--only-original-md`            | Only output the original markdown files, do not output the translated markdown files    | `pdf2zh_next example.pdf --only-original-md`                                                                          |
| `--only-original-md --no-mono --no-bilingual` | Only output the original markdown files, do not output any PDF files and translated markdown files | `pdf2zh_next example.pdf --only-original-md --no-mono --no-bilingual`                                                 |

---

### TRANSLATION RESULT

| `--no-mono`                     | 単一言語 PDF ファイルを出力しない                                                       | `pdf2zh_next example.pdf --no-mono`                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-bilingual`                | 二言語対訳 PDF ファイルを出力しない                                                     | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--no-mono --no-bilingual`      | PDF ファイルを出力せず、マークダウン ファイルのみを出力する                             | `pdf2zh_next example.pdf --no-mono --no-bilingual`                                                                    |
| `--only-translated-md`          | 翻訳済みマークダウン ファイルのみを出力し、元のマークダウン ファイルは出力しない         | `pdf2zh_next example.pdf --only-translated-md`                                                                        |
| `--only-original-md`            | 元のマークダウン ファイルのみを出力し、翻訳済みマークダウン ファイルは出力しない         | `pdf2zh_next example.pdf --only-original-md`                                                                          |
| `--only-original-md --no-mono --no-bilingual` | 元のマークダウン ファイルのみを出力し、PDF ファイルと翻訳済みマークダウン ファイルは出力しない | `pdf2zh_next example.pdf --only-original-md --no-mono --no-bilingual`                                                 |
`(MS.*)`          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `--formular-font-patterns-file` | Path to a file containing multiple font patterns, one per line, for identifying formula | `pdf2zh_next example.pdf --formular-font-patterns-file formular_patterns.txt`                                         | `formular_patterns.txt` |

---

### OUTPUT

| `--formular-font-pattern`       | 数式テキストを識別するためのフォントパターン                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            | `(MS.*)`          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `--formular-font-patterns-file` | 数式を識別するための複数のフォントパターンを含むファイルへのパス。1 行に 1 つのパターン。 | `pdf2zh_next example.pdf --formular-font-patterns-file formular_patterns.txt`                                         | `formular_patterns.txt` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-replace`       | Replacement for formula text                                                            | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "\\boxed{\\1}"`                     |
| `--formular-char-replace-first` | Replace only the first occurrence of formula text                                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "\\boxed{\\1}" --formular-char-replace-first` |
| `--formular-char-replace-all`   | Replace all occurrences of formula text (default)                                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "\\boxed{\\1}" --formular-char-replace-all`   |
| `--formular-char-replace-html`  | Use HTML tags instead of LaTeX for formula text replacement. This option is for WebUI.  | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "<span class='formula'>\\1</span>" --formular-char-replace-html` |

---

### TRANSLATION RESULT

| `--formular-char-pattern`       | 数式テキストを識別する文字パターン                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-replace`       | 数式テキストの置換                                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "\\boxed{\\1}"`                     |
| `--formular-char-replace-first` | 数式テキストの最初の出現のみ置換                                                 | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "\\boxed{\\1}" --formular-char-replace-first` |
| `--formular-char-replace-all`   | 数式テキストのすべての出現を置換（デフォルト）                                     | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "\\boxed{\\1}" --formular-char-replace-all`   |
| `--formular-char-replace-html`  | 数式テキストの置換に LaTeX の代わりに HTML タグを使用します。このオプションは WebUI 用です。 | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "<span class='formula'>\\1</span>" --formular-char-replace-html` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | Set the threshold for splitting short lines (default: 10)                               | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-threshold 15`                                        |
| `--no-split-short-lines`        | Disable splitting short lines                                                           | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--ignore-short-lines`          | Ignore short lines                                                                      | `pdf2zh_next example.pdf --ignore-short-lines`                                                                        |
| `--ignore-short-lines-threshold`| Set the threshold for ignoring short lines (default: 10)                                | `pdf2zh_next example.pdf --ignore-short-lines --ignore-short-lines-threshold 15`                                      |

---

### OUTPUT

| `--split-short-lines`           | 短い行を強制的に別の段落に分割                                   | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | 短い行を分割する閾値を設定（デフォルト：10）                       | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-threshold 15`                                        |
| `--no-split-short-lines`        | 短い行の分割を無効化                                               | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--ignore-short-lines`          | 短い行を無視                                                       | `pdf2zh_next example.pdf --ignore-short-lines`                                                                        |
| `--ignore-short-lines-threshold`| 短い行を無視する閾値を設定（デフォルト：10）                       | `pdf2zh_next example.pdf --ignore-short-lines --ignore-short-lines-threshold 15`                                      |
`1.0`                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `--short-line-split-min-length` | Minimum character count for short lines                                                 | `pdf2zh_next example.pdf --short-line-split-min-length 10`                                                            | `5`                                                   |
| `--short-line-split-max-length` | Maximum character count for short lines                                                 | `pdf2zh_next example.pdf --short-line-split-max-length 100`                                                           | `100`                                                 |
| `--short-line-merge-factor`     | Merge threshold factor for short lines                                                  | `pdf2zh_next example.pdf --short-line-merge-factor 1.2`                                                               | `1.0`                                                 |
| `--short-line-merge-min-length` | Minimum character count for short lines to be merged                                    | `pdf2zh_next example.pdf --short-line-merge-min-length 10`                                                            | `5`                                                   |
| `--short-line-merge-max-length` | Maximum character count for short lines to be merged                                    | `pdf2zh_next example.pdf --short-line-merge-max-length 100`                                                           | `100`                                                 |
| `--short-line-merge-same-line`  | Whether to merge short lines that are on the same line                                  | `pdf2zh_next example.pdf --short-line-merge-same-line`                                                                | `false`                                               |
| `--short-line-merge-next-line`  | Whether to merge short lines with the next line                                         | `pdf2zh_next example.pdf --short-line-merge-next-line`                                                                | `false`                                               |
| `--short-line-merge-prev-line`  | Whether to merge short lines with the previous line                                     | `pdf2zh_next example.pdf --short-line-merge-prev-line`                                                                | `false`                                               |
| `--short-line-merge-same-font`  | Whether to merge short lines with the same font                                         | `pdf2zh_next example.pdf --short-line-merge-same-font`                                                                | `false`                                               |
| `--short-line-merge-same-size`  | Whether to merge short lines with the same font size                                    | `pdf2zh_next example.pdf --short-line-merge-same-size`                                                                | `false`                                               |
| `--short-line-merge-same-color` | Whether to merge short lines with the same color                                        | `pdf2zh_next example.pdf --short-line-merge-same-color`                                                               | `false`                                               |
| `--short-line-merge-same-style` | Whether to merge short lines with the same style                                        | `pdf2zh_next example.pdf --short-line-merge-same-style`                                                               | `false`                                               |
| `--short-line-merge-same-align` | Whether to merge short lines with the same alignment                                    | `pdf2zh_next example.pdf --short-line-merge-same-align`                                                               | `false`                                               |
| `--short-line-merge-same-indent` | Whether to merge short lines with the same indent                                       | `pdf2zh_next example.pdf --short-line-merge-same-indent`                                                              | `false`                                               |
| `--short-line-merge-same-spacing` | Whether to merge short lines with the same line spacing                                 | `pdf2zh_next example.pdf --short-line-merge-same-spacing`                                                             | `false`                                               |
| `--short-line-merge-same-margin` | Whether to merge short lines with the same margin                                       | `pdf2zh_next example.pdf --short-line-merge-same-margin`                                                              | `false`                                               |
| `--short-line-merge-same-padding` | Whether to merge short lines with the same padding                                      | `pdf2zh_next example.pdf --short-line-merge-same-padding`                                                             | `false`                                               |
| `--short-line-merge-same-border` | Whether to merge short lines with the same border                                       | `pdf2zh_next example.pdf --short-line-merge-same-border`                                                              | `false`                                               |
| `--short-line-merge-same-background` | Whether to merge short lines with the same background                                   | `pdf2zh_next example.pdf --short-line-merge-same-background`                                                          | `false`                                               |
| `--short-line-merge-same-other` | Whether to merge short lines with the same other attributes                             | `pdf2zh_next example.pdf --short-line-merge-same-other`                                                               | `false`                                               |

---

### TRANSLATION RESULT

| `--short-line-split-factor`     | 短い行の分割しきい値係数                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               | `1.0`                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `--short-line-split-min-length` | 短い行の最小文字数                                                 | `pdf2zh_next example.pdf --short-line-split-min-length 10`                                                            | `5`                                                   |
| `--short-line-split-max-length` | 短い行の最大文字数                                                 | `pdf2zh_next example.pdf --short-line-split-max-length 100`                                                           | `100`                                                 |
| `--short-line-merge-factor`     | 短い行のマージしきい値係数                                                  | `pdf2zh_next example.pdf --short-line-merge-factor 1.2`                                                               | `1.0`                                                 |
| `--short-line-merge-min-length` | マージされる短い行の最小文字数                                    | `pdf2zh_next example.pdf --short-line-merge-min-length 10`                                                            | `5`                                                   |
| `--short-line-merge-max-length` | マージされる短い行の最大文字数                                    | `pdf2zh_next example.pdf --short-line-merge-max-length 100`                                                           | `100`                                                 |
| `--short-line-merge-same-line`  | 同じ行にある短い行をマージするかどうか                                  | `pdf2zh_next example.pdf --short-line-merge-same-line`                                                                | `false`                                               |
| `--short-line-merge-next-line`  | 短い行を次の行とマージするかどうか                                         | `pdf2zh_next example.pdf --short-line-merge-next-line`                                                                | `false`                                               |
| `--short-line-merge-prev-line`  | 短い行を前の行とマージするかどうか                                     | `pdf2zh_next example.pdf --short-line-merge-prev-line`                                                                | `false`                                               |
| `--short-line-merge-same-font`  | 同じフォントの短い行をマージするかどうか                                         | `pdf2zh_next example.pdf --short-line-merge-same-font`                                                                | `false`                                               |
| `--short-line-merge-same-size`  | 同じフォントサイズの短い行をマージするかどうか                                    | `pdf2zh_next example.pdf --short-line-merge-same-size`                                                                | `false`                                               |
| `--short-line-merge-same-color` | 同じ色の短い行をマージするかどうか                                        | `pdf2zh_next example.pdf --short-line-merge-same-color`                                                               | `false`                                               |
| `--short-line-merge-same-style` | 同じスタイルの短い行をマージするかどうか                                        | `pdf2zh_next example.pdf --short-line-merge-same-style`                                                               | `false`                                               |
| `--short-line-merge-same-align` | 同じ配置の短い行をマージするかどうか                                    | `pdf2zh_next example.pdf --short-line-merge-same-align`                                                               | `false`                                               |
| `--short-line-merge-same-indent` | 同じインデントの短い行をマージするかどうか                                       | `pdf2zh_next example.pdf --short-line-merge-same-indent`                                                              | `false`                                               |
| `--short-line-merge-same-spacing` | 同じ行間隔の短い行をマージするかどうか                                 | `pdf2zh_next example.pdf --short-line-merge-same-spacing`                                                             | `false`                                               |
| `--short-line-merge-same-margin` | 同じマージンの短い行をマージするかどうか                                       | `pdf2zh_next example.pdf --short-line-merge-same-margin`                                                              | `false`                                               |
| `--short-line-merge-same-padding` | 同じパディングの短い行をマージするかどうか                                      | `pdf2zh_next example.pdf --short-line-merge-same-padding`                                                             | `false`                                               |
| `--short-line-merge-same-border` | 同じ境界線の短い行をマージするかどうか                                       | `pdf2zh_next example.pdf --short-line-merge-same-border`                                                              | `false`                                               |
| `--short-line-merge-same-background` | 同じ背景の短い行をマージするかどうか                                   | `pdf2zh_next example.pdf --short-line-merge-same-background`                                                          | `false`                                               |
| `--short-line-merge-same-other` | 同じ他の属性の短い行をマージするかどうか                             | `pdf2zh_next example.pdf --short-line-merge-same-other`                                                               | `false`                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | Skip OCR step                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-reconstruct`            | Skip PDF reconstruction step                                                            | `pdf2zh_next example.pdf --skip-reconstruct`                                                                          |
| `--keep-translation-in-pdf`     | Keep translation text in PDF (for debugging)                                            | `pdf2zh_next example.pdf --keep-translation-in-pdf`                                                                   |
| `--save-json`                   | Save translation results to JSON file (for debugging)                                  | `pdf2zh_next example.pdf --save-json`                                                                                |
| `--save-json-path <path>`       | Specify path to save JSON file                                                          | `pdf2zh_next example.pdf --save-json-path ./translation.json`                                                         |
| `--skip-pdf2image`              | Skip PDF to image conversion (use existing images)                                     | `pdf2zh_next example.pdf --skip-pdf2image`                                                                            |
| `--skip-image2pdf`              | Skip image to PDF conversion (use existing PDF)                                          | `pdf2zh_next example.pdf --skip-image2pdf`                                                                            |
| `--skip-image-clean`            | Skip image cleaning step                                                                | `pdf2zh_next example.pdf --skip-image-clean`                                                                          |
| `--skip-image-ocr`              | Skip image OCR step                                                                     | `pdf2zh_next example.pdf --skip-image-ocr`                                                                            |
| `--skip-image-translate`        | Skip image translation step                                                             | `pdf2zh_next example.pdf --skip-image-translate`                                                                      |
| `--skip-image-reconstruct`      | Skip image reconstruction step                                                          | `pdf2zh_next example.pdf --skip-image-reconstruct`                                                                    |
| `--skip-image-save`             | Skip image saving step                                                                  | `pdf2zh_next example.pdf --skip-image-save`                                                                           |
| `--skip-image-merge`            | Skip image merging step                                                                 | `pdf2zh_next example.pdf --skip-image-merge`                                                                          |
| `--skip-image-split`            | Skip image splitting step                                                               | `pdf2zh_next example.pdf --skip-image-split`                                                                          |
| `--skip-image-resize`           | Skip image resizing step                                                                | `pdf2zh_next example.pdf --skip-image-resize`                                                                         |
| `--skip-image-rotate`           | Skip image rotation step                                                                | `pdf2zh_next example.pdf --skip-image-rotate`                                                                         |
| `--skip-image-flip`             | Skip image flipping step                                                                | `pdf2zh_next example.pdf --skip-image-flip`                                                                            |
| `--skip-image-crop`             | Skip image cropping step                                                                | `pdf2zh_next example.pdf --skip-image-crop`                                                                           |
| `--skip-image-blur`             | Skip image blurring step                                                                | `pdf2zh_next example.pdf --skip-image-blur`                                                                            |
| `--skip-image-sharpen`          | Skip image sharpening step                                                              | `pdf2zh_next example.pdf --skip-image-sharpen`                                                                        |
| `--skip-image-denoise`          | Skip image denoising step                                                               | `pdf2zh_next example.pdf --skip-image-denoise`                                                                        |
| `--skip-image-enhance`          | Skip image enhancement step                                                             | `pdf2zh_next example.pdf --skip-image-enhance`                                                                        |
| `--skip-image-compress`         | Skip image compression step                                                             | `pdf2zh_next example.pdf --skip-image-compress`                                                                       |
| `--skip-image-convert`          | Skip image format conversion step                                                       | `pdf2zh_next example.pdf --skip-image-convert`                                                                        |
| `--skip-image-watermark`        | Skip image watermarking step                                                            | `pdf2zh_next example.pdf --skip-image-watermark`                                                                      |
| `--skip-image-border`           | Skip image border adding step                                                          | `pdf2zh_next example.pdf --skip-image-border`                                                                          |
| `--skip-image-shadow`           | Skip image shadow adding step                                                          | `pdf2zh_next example.pdf --skip-image-shadow`                                                                         |
| `--skip-image-text`             | Skip image text adding step                                                            | `pdf2zh_next example.pdf --skip-image-text`                                                                            |
| `--skip-image-shape`            | Skip image shape adding step                                                           | `pdf2zh_next example.pdf --skip-image-shape`                                                                          |
| `--skip-image-filter`           | Skip image filter applying step                                                        | `pdf2zh_next example.pdf --skip-image-filter`                                                                         |
| `--skip-image-mask`             | Skip image masking step                                                                | `pdf2zh_next example.pdf --skip-image-mask`                                                                            |
| `--skip-image-blend`            | Skip image blending step                                                               | `pdf2zh_next example.pdf --skip-image-blend`                                                                          |
| `--skip-image-composite`        | Skip image compositing step                                                            | `pdf2zh_next example.pdf --skip-image-composite`                                                                      |
| `--skip-image-draw`             | Skip image drawing step                                                                | `pdf2zh_next example.pdf --skip-image-draw`                                                                           |
| `--skip-image-paint`            | Skip image painting step                                                               | `pdf2zh_next example.pdf --skip-image-paint`                                                                          |
| `--skip-image-fill`             | Skip image filling step                                                                | `pdf2zh_next example.pdf --skip-image-fill`                                                                            |
| `--skip-image-stroke`           | Skip image stroking step                                                               | `pdf2zh_next example.pdf --skip-image-stroke`                                                                         |
| `--skip-image-gradient`         | Skip image gradient applying step                                                      | `pdf2zh_next example.pdf --skip-image-gradient`                                                                       |
| `--skip-image-pattern`          | Skip image pattern applying step                                                       | `pdf2zh_next example.pdf --skip-image-pattern`                                                                        |
| `--skip-image-clip`             | Skip image clipping step                                                               | `pdf2zh_next example.pdf --skip-image-clip`                                                                            |
| `--skip-image-path`             | Skip image path drawing step                                                           | `pdf2zh_next example.pdf --skip-image-path`                                                                            |
| `--skip-image-transform`        | Skip image transformation step                                                          | `pdf2zh_next example.pdf --skip-image-transform`                                                                      |
| `--skip-image-affine`           | Skip image affine transformation step                                                  | `pdf2zh_next example.pdf --skip-image-affine`                                                                         |
| `--skip-image-perspective`      | Skip image perspective transformation step                                               | `pdf2zh_next example.pdf --skip-image-perspective`                                                                    |
| `--skip-image-warp`             | Skip image warping step                                                                | `pdf2zh_next example.pdf --skip-image-warp`                                                                           |
| `--skip-image-morph`            | Skip image morphing step                                                               | `pdf2zh_next example.pdf --skip-image-morph`                                                                          |
| `--skip-image-deform`           | Skip image deforming step                                                              | `pdf2zh_next example.pdf --skip-image-deform`                                                                         |
| `--skip-image-render`           | Skip image rendering step                                                              | `pdf2zh_next example.pdf --skip-image-render`                                                                         |
| `--skip-image-display`          | Skip image display step                                                                | `pdf2zh_next example.pdf --skip-image-display`                                                                        |
| `--skip-image-save`             | Skip image saving step                                                                  | `pdf2zh_next example.pdf --skip-image-save`                                                                           |
| `--skip-image-load`             | Skip image loading step                                                                | `pdf2zh_next example.pdf --skip-image-load`                                                                            |
| `--skip-image-export`           | Skip image exporting step                                                              | `pdf2zh_next example.pdf --skip-image-export`                                                                         |
| `--skip-image-import`           | Skip image importing step                                                              | `pdf2zh_next example.pdf --skip-image-import`                                                                         |
| `--skip-image-copy`             | Skip image copying step                                                                | `pdf2zh_next example.pdf --skip-image-copy`                                                                            |
| `--skip-image-paste`            | Skip image pasting step                                                               | `pdf2zh_next example.pdf --skip-image-paste`                                                                          |
| `--skip-image-cut`              | Skip image cutting step                                                               | `pdf2zh_next example.pdf --skip-image-cut`                                                                            |
| `--skip-image-clear`            | Skip image clearing step                                                              | `pdf2zh_next example.pdf --skip-image-clear`                                                                          |
| `--skip-image-undocumented`     | Skip undocumented image processing steps                                               | `pdf2zh_next example.pdf --skip-image-undocumented`                                                                   |

---

### OUTPUT

| `--skip-clean`                  | PDF クリーニングステップをスキップ                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | 翻訳ステップをスキップ                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | OCR ステップをスキップ                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-reconstruct`            | PDF 再構築ステップをスキップ                                                            | `pdf2zh_next example.pdf --skip-reconstruct`                                                                          |
| `--keep-translation-in-pdf`     | 翻訳テキストを PDF に保持（デバッグ用）                                            | `pdf2zh_next example.pdf --keep-translation-in-pdf`                                                                   |
| `--save-json`                   | 翻訳結果を JSON ファイルに保存（デバッグ用）                                  | `pdf2zh_next example.pdf --save-json`                                                                                |
| `--save-json-path <path>`       | JSON ファイルの保存パスを指定                                                          | `pdf2zh_next example.pdf --save-json-path ./translation.json`                                                         |
| `--skip-pdf2image`              | PDF から画像への変換をスキップ（既存の画像を使用）                                     | `pdf2zh_next example.pdf --skip-pdf2image`                                                                            |
| `--skip-image2pdf`              | 画像から PDF への変換をスキップ（既存の PDF を使用）                                          | `pdf2zh_next example.pdf --skip-image2pdf`                                                                            |
| `--skip-image-clean`            | 画像クリーニングステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-clean`                                                                          |
| `--skip-image-ocr`              | 画像 OCR ステップをスキップ                                                                     | `pdf2zh_next example.pdf --skip-image-ocr`                                                                            |
| `--skip-image-translate`        | 画像翻訳ステップをスキップ                                                             | `pdf2zh_next example.pdf --skip-image-translate`                                                                      |
| `--skip-image-reconstruct`      | 画像再構築ステップをスキップ                                                          | `pdf2zh_next example.pdf --skip-image-reconstruct`                                                                    |
| `--skip-image-save`             | 画像保存ステップをスキップ                                                                  | `pdf2zh_next example.pdf --skip-image-save`                                                                           |
| `--skip-image-merge`            | 画像結合ステップをスキップ                                                                 | `pdf2zh_next example.pdf --skip-image-merge`                                                                          |
| `--skip-image-split`            | 画像分割ステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-split`                                                                          |
| `--skip-image-resize`           | 画像リサイズステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-resize`                                                                         |
| `--skip-image-rotate`           | 画像回転ステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-rotate`                                                                         |
| `--skip-image-flip`             | 画像反転ステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-flip`                                                                            |
| `--skip-image-crop`             | 画像クロップステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-crop`                                                                           |
| `--skip-image-blur`             | 画像ぼかしステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-blur`                                                                            |
| `--skip-image-sharpen`          | 画像シャープニングステップをスキップ                                                              | `pdf2zh_next example.pdf --skip-image-sharpen`                                                                        |
| `--skip-image-denoise`          | 画像ノイズ除去ステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-denoise`                                                                        |
| `--skip-image-enhance`          | 画像強調ステップをスキップ                                                             | `pdf2zh_next example.pdf --skip-image-enhance`                                                                        |
| `--skip-image-compress`         | 画像圧縮ステップをスキップ                                                             | `pdf2zh_next example.pdf --skip-image-compress`                                                                       |
| `--skip-image-convert`          | 画像フォーマット変換ステップをスキップ                                                       | `pdf2zh_next example.pdf --skip-image-convert`                                                                        |
| `--skip-image-watermark`        | 画像透かしステップをスキップ                                                            | `pdf2zh_next example.pdf --skip-image-watermark`                                                                      |
| `--skip-image-border`           | 画像ボーダー追加ステップをスキップ                                                          | `pdf2zh_next example.pdf --skip-image-border`                                                                          |
| `--skip-image-shadow`           | 画像シャドウ追加ステップをスキップ                                                          | `pdf2zh_next example.pdf --skip-image-shadow`                                                                         |
| `--skip-image-text`             | 画像テキスト追加ステップをスキップ                                                            | `pdf2zh_next example.pdf --skip-image-text`                                                                            |
| `--skip-image-shape`            | 画像シェイプ追加ステップをスキップ                                                           | `pdf2zh_next example.pdf --skip-image-shape`                                                                          |
| `--skip-image-filter`           | 画像フィルター適用ステップをスキップ                                                        | `pdf2zh_next example.pdf --skip-image-filter`                                                                         |
| `--skip-image-mask`             | 画像マスキングステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-mask`                                                                            |
| `--skip-image-blend`            | 画像ブレンドステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-blend`                                                                          |
| `--skip-image-composite`        | 画像合成ステップをスキップ                                                            | `pdf2zh_next example.pdf --skip-image-composite`                                                                      |
| `--skip-image-draw`             | 画像描画ステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-draw`                                                                           |
| `--skip-image-paint`            | 画像ペイントステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-paint`                                                                          |
| `--skip-image-fill`             | 画像塗りつぶしステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-fill`                                                                            |
| `--skip-image-stroke`           | 画像ストロークステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-stroke`                                                                         |
| `--skip-image-gradient`         | 画像グラデーション適用ステップをスキップ                                                      | `pdf2zh_next example.pdf --skip-image-gradient`                                                                       |
| `--skip-image-pattern`          | 画像パターン適用ステップをスキップ                                                       | `pdf2zh_next example.pdf --skip-image-pattern`                                                                        |
| `--skip-image-clip`             | 画像クリッピングステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-clip`                                                                            |
| `--skip-image-path`             | 画像パス描画ステップをスキップ                                                           | `pdf2zh_next example.pdf --skip-image-path`                                                                            |
| `--skip-image-transform`        | 画像変換ステップをスキップ                                                          | `pdf2zh_next example.pdf --skip-image-transform`                                                                      |
| `--skip-image-affine`           | 画像アフィン変換ステップをスキップ                                                  | `pdf2zh_next example.pdf --skip-image-affine`                                                                         |
| `--skip-image-perspective`      | 画像透視変換ステップをスキップ                                               | `pdf2zh_next example.pdf --skip-image-perspective`                                                                    |
| `--skip-image-warp`             | 画像ワープステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-warp`                                                                           |
| `--skip-image-morph`            | 画像モーフィングステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-morph`                                                                          |
| `--skip-image-deform`           | 画像変形ステップをスキップ                                                              | `pdf2zh_next example.pdf --skip-image-deform`                                                                         |
| `--skip-image-render`           | 画像レンダリングステップをスキップ                                                              | `pdf2zh_next example.pdf --skip-image-render`                                                                         |
| `--skip-image-display`          | 画像表示ステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-display`                                                                        |
| `--skip-image-save`             | 画像保存ステップをスキップ                                                                  | `pdf2zh_next example.pdf --skip-image-save`                                                                           |
| `--skip-image-load`             | 画像読み込みステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-load`                                                                            |
| `--skip-image-export`           | 画像エクスポートステップをスキップ                                                              | `pdf2zh_next example.pdf --skip-image-export`                                                                         |
| `--skip-image-import`           | 画像インポートステップをスキップ                                                              | `pdf2zh_next example.pdf --skip-image-import`                                                                         |
| `--skip-image-copy`             | 画像コピーステップをスキップ                                                                | `pdf2zh_next example.pdf --skip-image-copy`                                                                            |
| `--skip-image-paste`            | 画像ペーストステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-paste`                                                                          |
| `--skip-image-cut`              | 画像カットステップをスキップ                                                               | `pdf2zh_next example.pdf --skip-image-cut`                                                                            |
| `--skip-image-clear`            | 画像クリアステップをスキップ                                                              | `pdf2zh_next example.pdf --skip-image-clear`                                                                          |
| `--skip-image-undocumented`     | 非公式の画像処理ステップをスキップ                                               | `pdf2zh_next example.pdf --skip-image-undocumented`                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-first`        | デュアル PDF モードで翻訳されたページを先に配置する                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-first`        | デュアル PDF モードで翻訳されたページを先に配置する                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |

---

### OUTPUT

| `--dual-translate-first`        | デュアル PDF モードで翻訳されたページを先に配置する                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-first`        | デュアル PDF モードで翻訳されたページを先に配置する                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-first`        | デュアル PDF モードで翻訳されたページを先に配置する                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-rich-text-latex`     | Disable rich text LaTeX translation                                                     | `pdf2zh_next example.pdf --disable-rich-text-latex`                                                                   |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next -h`                                                                                                      |
| `-V`, `--version`               | Show version and exit                                                                   | `pdf2zh_next -V`                                                                                                      |

---

### TRANSLATION RESULT

| `--disable-rich-text-translate` | リッチテキストの翻訳を無効にする                                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-rich-text-latex`     | リッチテキストの LaTeX 翻訳を無効にする                                                     | `pdf2zh_next example.pdf --disable-rich-text-latex`                                                                   |
| `-h`, `--help`                  | ヘルプメッセージを表示して終了する                                                              | `pdf2zh_next -h`                                                                                                      |
| `-V`, `--version`               | バージョンを表示して終了する                                                                   | `pdf2zh_next -V`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-split` | Enable compatibility enhancement: Split large blocks of text to avoid exceeding the API | `pdf2zh_next example.pdf --enhance-compatibility-split`                                                               |
| `--enhance-compatibility-merge` | Enable compatibility enhancement: Merge small blocks of text to reduce API calls        | `pdf2zh_next example.pdf --enhance-compatibility-merge`                                                               |
| `--enhance-compatibility-retry` | Enable compatibility enhancement: Retry when an API call fails                          | `pdf2zh_next example.pdf --enhance-compatibility-retry`                                                               |
| `--enhance-compatibility-queue` | Enable compatibility enhancement: Queue API calls to avoid exceeding rate limits        | `pdf2zh_next example.pdf --enhance-compatibility-queue`                                                               |
| `--enhance-compatibility-all`   | Enable all compatibility enhancement options                                            | `pdf2zh_next example.pdf --enhance-compatibility-all`                                                                 |
| `--enhance-compatibility-none`  | Disable all compatibility enhancement options                                           | `pdf2zh_next example.pdf --enhance-compatibility-none`                                                                |

---

### OUTPUT

| `--enhance-compatibility`       | すべての互換性向上オプションを有効にする                                                                 | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-split` | 互換性向上：API の上限を超えないように大きなテキストブロックを分割する                                   | `pdf2zh_next example.pdf --enhance-compatibility-split`                                                               |
| `--enhance-compatibility-merge` | 互換性向上：API 呼び出しを減らすために小さなテキストブロックをマージする                                 | `pdf2zh_next example.pdf --enhance-compatibility-merge`                                                               |
| `--enhance-compatibility-retry` | 互換性向上：API 呼び出しが失敗した場合に再試行する                                                       | `pdf2zh_next example.pdf --enhance-compatibility-retry`                                                               |
| `--enhance-compatibility-queue` | 互換性向上：レート制限を超えないように API 呼び出しをキューイングする                                    | `pdf2zh_next example.pdf --enhance-compatibility-queue`                                                               |
| `--enhance-compatibility-all`   | すべての互換性向上オプションを有効にする                                                                 | `pdf2zh_next example.pdf --enhance-compatibility-all`                                                                 |
| `--enhance-compatibility-none`  | すべての互換性向上オプションを無効にする                                                                 | `pdf2zh_next example.pdf --enhance-compatibility-none`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-columns-dual`            | Use columns mode for dual PDF                                                           | `pdf2zh_next example.pdf --use-columns-dual`                                                                          |
| `--use-columns-single`          | Use columns mode for single PDF                                                         | `pdf2zh_next example.pdf --use-columns-single`                                                                        |
| `--use-immersive-translate`     | Use [Immersive Translate](https://github.com/immersive-translate/immersive-translate) | `pdf2zh_next example.pdf --use-immersive-translate`                                                                   |
| `--use-llm`                     | Use LLM for translation (default is `gpt-4o-mini`)                                      | `pdf2zh_next example.pdf --use-llm`                                                                                   |

---

### TRANSLATION RESULT

| `--use-alternating-pages-dual`  | デュアル PDF 用に交互ページモードを使用する                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | シングル PDF 用に交互ページモードを使用する                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-columns-dual`            | デュアル PDF 用にカラムモードを使用する                                                           | `pdf2zh_next example.pdf --use-columns-dual`                                                                          |
| `--use-columns-single`          | シングル PDF 用にカラムモードを使用する                                                         | `pdf2zh_next example.pdf --use-columns-single`                                                                        |
| `--use-immersive-translate`     | [Immersive Translate](https://github.com/immersive-translate/immersive-translate) を使用する | `pdf2zh_next example.pdf --use-immersive-translate`                                                                   |
| `--use-llm`                     | 翻訳に LLM を使用する（デフォルトは `gpt-4o-mini`）                                      | `pdf2zh_next example.pdf --use-llm`                                                                                   |
`watermark` `no_watermark` `watermark_only` | `watermark` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|-------------|
| `--watermark-text`              | Watermark text for PDF files                                                            | `pdf2zh_next example.pdf --watermark-text "Hello World"`                                                              | string                                      | `pdf2zh`    |
| `--watermark-font-family`       | Font family for watermark text                                                          | `pdf2zh_next example.pdf --watermark-font-family "Helvetica"`                                                         | string                                      | `Helvetica` |
| `--watermark-font-size`         | Font size for watermark text                                                            | `pdf2zh_next example.pdf --watermark-font-size 30`                                                                   | number                                      | `30`        |
| `--watermark-opacity`           | Opacity for watermark text                                                              | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                    | number between 0 and 1                      | `0.5`       |
| `--watermark-rotation`          | Rotation angle for watermark text                                                       | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                    | number                                      | `45`        |
| `--watermark-color`             | Color for watermark text                                                                | `pdf2zh_next example.pdf --watermark-color "#FF0000"`                                                                | RGB hex value                               | `#FF0000`   |
| `--watermark-position`          | Position for watermark text                                                             | `pdf2zh_next example.pdf --watermark-position "center"`                                                              | `center` `top_left` `top_right` `bottom_left` `bottom_right` | `center`    |
| `--watermark-x`                 | X coordinate for watermark text                                                         | `pdf2zh_next example.pdf --watermark-x 100`                                                                          | number                                      | `100`       |
| `--watermark-y`                 | Y coordinate for watermark text                                                         | `pdf2zh_next example.pdf --watermark-y 100`                                                                          | number                                      | `100`       |

---

### OUTPUT

| `--watermark-output-mode`       | PDF ファイルの透かし出力モード                                                     | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `watermark` `no_watermark` `watermark_only` | `watermark` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------|-------------|
| `--watermark-text`              | PDF ファイルの透かしテキスト                                                            | `pdf2zh_next example.pdf --watermark-text "Hello World"`                                                              | string                                      | `pdf2zh`    |
| `--watermark-font-family`       | 透かしテキストのフォントファミリー                                                          | `pdf2zh_next example.pdf --watermark-font-family "Helvetica"`                                                         | string                                      | `Helvetica` |
| `--watermark-font-size`         | 透かしテキストのフォントサイズ                                                            | `pdf2zh_next example.pdf --watermark-font-size 30`                                                                   | number                                      | `30`        |
| `--watermark-opacity`           | 透かしテキストの不透明度                                                              | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                    | 0 から 1 の間の数値                      | `0.5`       |
| `--watermark-rotation`          | 透かしテキストの回転角度                                                       | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                    | number                                      | `45`        |
| `--watermark-color`             | 透かしテキストの色                                                                | `pdf2zh_next example.pdf --watermark-color "#FF0000"`                                                                | RGB 16 進値                               | `#FF0000`   |
| `--watermark-position`          | 透かしテキストの位置                                                             | `pdf2zh_next example.pdf --watermark-position "center"`                                                              | `center` `top_left` `top_right` `bottom_left` `bottom_right` | `center`    |
| `--watermark-x`                 | 透かしテキストの X 座標                                                         | `pdf2zh_next example.pdf --watermark-x 100`                                                                          | number                                      | `100`       |
| `--watermark-y`                 | 透かしテキストの Y 座標                                                         | `pdf2zh_next example.pdf --watermark-y 100`                                                                          | number                                      | `100`       |
`50`     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------- |
| `--api-endpoint`                | API endpoint for translation service                                                    | `pdf2zh_next example.pdf --api-endpoint https://api.example.com/translate`                                            | `None`   |
| `--api-key`                     | API key for translation service                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      | `None`   |
| `--model`                       | Model name for translation service                                                      | `pdf2zh_next example.pdf --model gpt-4`                                                                               | `None`   |
| `--prompt-template`             | Custom prompt template for translation                                                  | `pdf2zh_next example.pdf --prompt-template "Translate the following text from {src_lang} to {tgt_lang}:"`             | `None`   |
| `--timeout`                     | Timeout for each translation request in seconds                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                | `30`     |
| `--max-retries`                 | Maximum retries for each translation request                                            | `pdf2zh_next example.pdf --max-retries 3`                                                                             | `3`      |
| `--request-interval`            | Interval between requests in seconds                                                    | `pdf2zh_next example.pdf --request-interval 1`                                                                        | `1`      |
| `--ignore-translated-parts`     | Ignore already translated parts and only translate untranslated parts                   | `pdf2zh_next example.pdf --ignore-translated-parts`                                                                   | `False`  |
| `--no-cache`                    | Disable caching of translation results                                                  | `pdf2zh_next example.pdf --no-cache`                                                                                  | `False`  |
| `--cache-dir`                   | Directory to store cache files                                                          | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         | `./cache`|
| `--log-level`                   | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)                                       | `pdf2zh_next example.pdf --log-level INFO`                                                                            | `INFO`   |
| `--log-file`                    | File to write logs to                                                                   | `pdf2zh_next example.pdf --log-file translation.log`                                                                  | `None`   |
| `--no-progress-bar`             | Disable progress bar                                                                    | `pdf2zh_next example.pdf --no-progress-bar`                                                                           | `False`  |
| `--dry-run`                     | Perform a dry run without actual translation                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   | `False`  |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               | `None`   |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  | `None`   |

---

### TRANSLATION RESULT

| `--max-pages-per-part`          | 分割翻訳におけるパートごとの最大ページ数                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     | `50`     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------- |
| `--api-endpoint`                | 翻訳サービスの API エンドポイント                                                    | `pdf2zh_next example.pdf --api-endpoint https://api.example.com/translate`                                            | `None`   |
| `--api-key`                     | 翻訳サービスの API キー                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      | `None`   |
| `--model`                       | 翻訳サービスのモデル名                                                      | `pdf2zh_next example.pdf --model gpt-4`                                                                               | `None`   |
| `--prompt-template`             | 翻訳用のカスタムプロンプトテンプレート                                                  | `pdf2zh_next example.pdf --prompt-template "Translate the following text from {src_lang} to {tgt_lang}:"`             | `None`   |
| `--timeout`                     | 各翻訳リクエストのタイムアウト（秒単位）                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                | `30`     |
| `--max-retries`                 | 各翻訳リクエストの最大リトライ回数                                            | `pdf2zh_next example.pdf --max-retries 3`                                                                             | `3`      |
| `--request-interval`            | リクエスト間の間隔（秒単位）                                                    | `pdf2zh_next example.pdf --request-interval 1`                                                                        | `1`      |
| `--ignore-translated-parts`     | 既に翻訳済みのパートを無視し、未翻訳のパートのみを翻訳する                   | `pdf2zh_next example.pdf --ignore-translated-parts`                                                                   | `False`  |
| `--no-cache`                    | 翻訳結果のキャッシュを無効にする                                                  | `pdf2zh_next example.pdf --no-cache`                                                                                  | `False`  |
| `--cache-dir`                   | キャッシュファイルを保存するディレクトリ                                                          | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         | `./cache`|
| `--log-level`                   | ログレベル（DEBUG、INFO、WARNING、ERROR、CRITICAL）                                       | `pdf2zh_next example.pdf --log-level INFO`                                                                            | `INFO`   |
| `--log-file`                    | ログを書き込むファイル                                                                   | `pdf2zh_next example.pdf --log-file translation.log`                                                                  | `None`   |
| `--no-progress-bar`             | プログレスバーを無効にする                                                                    | `pdf2zh_next example.pdf --no-progress-bar`                                                                           | `False`  |
| `--dry-run`                     | 実際の翻訳を行わずにドライランを実行する                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   | `False`  |
| `--version`                     | バージョンを表示して終了                                                                   | `pdf2zh_next --version`                                                                                               | `None`   |
| `--help`                        | ヘルプメッセージを表示して終了                                                              | `pdf2zh_next --help`                                                                                                  | `None`   |
---

### OUTPUT

| `--translate-table-text`        | テーブルテキストを翻訳する（実験的機能）                                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--skip-scanned-detect`         | Same as `--skip-scanned-detection`                                                      | `pdf2zh_next example.pdf --skip-scanned-detect`                                                                       |
| `--skip-scanned`                | Same as `--skip-scanned-detection`                                                      | `pdf2zh_next example.pdf --skip-scanned`                                                                              |
| `--scanned-detection-threshold` | Threshold for scanned detection, default `0.5`                                         | `pdf2zh_next example.pdf --scanned-detection-threshold 0.3`                                                           |
| `-t`, `--threshold`             | Same as `--scanned-detection-threshold`                                                 | `pdf2zh_next example.pdf -t 0.3`                                                                                      |

---

### OUTPUT

| `--skip-scanned-detection`      | スキャン文書検出をスキップ                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--skip-scanned-detect`         | `--skip-scanned-detection` と同じ                                                      | `pdf2zh_next example.pdf --skip-scanned-detect`                                                                       |
| `--skip-scanned`                | `--skip-scanned-detection` と同じ                                                      | `pdf2zh_next example.pdf --skip-scanned`                                                                              |
| `--scanned-detection-threshold` | スキャン文書検出の閾値、デフォルトは `0.5`                                         | `pdf2zh_next example.pdf --scanned-detection-threshold 0.3`                                                           |
| `-t`, `--threshold`             | `--scanned-detection-threshold` と同じ                                                 | `pdf2zh_next example.pdf -t 0.3`                                                                                      |
[!NOTE] This option may not be compatible with all PDF readers and may result in poor display of some PDFs. |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `--proxy`                       | Use a proxy for network requests                                                        | `pdf2zh_next example.pdf --proxy http://127.0.0.1:8080`                                                               |                                                                                                             |
| `--proxy-username`              | Proxy username (if required)                                                            | `pdf2zh_next example.pdf --proxy http://127.0.0.1:8080 --proxy-username username`                                     |                                                                                                             |
| `--proxy-password`              | Proxy password (if required)                                                            | `pdf2zh_next example.pdf --proxy http://127.0.0.1:8080 --proxy-password password`                                     |                                                                                                             |

---

### RESPONSE

| `--ocr-workaround`              | 翻訳されたテキストを強制的に黒色にし、白い背景を追加する                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                               | [!NOTE] このオプションはすべての PDF リーダーと互換性がない場合があり、一部の PDF の表示が不十分になる可能性があります。 |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `--proxy`                       | ネットワークリクエストにプロキシを使用する                                                | `pdf2zh_next example.pdf --proxy http://127.0.0.1:8080`                                                               |                                                                                                             |
| `--proxy-username`              | プロキシユーザー名（必要な場合）                                                          | `pdf2zh_next example.pdf --proxy http://127.0.0.1:8080 --proxy-username username`                                     |                                                                                                             |
| `--proxy-password`              | プロキシパスワード（必要な場合）                                                          | `pdf2zh_next example.pdf --proxy http://127.0.0.1:8080 --proxy-password password`                                     |                                                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--enable-ocr-workaround`       | Enable OCR workaround for scanned documents. This will force OCR processing even if the document is not detected as scanned. See documentation for details. (default: False)                         | `pdf2zh_next example.pdf --enable-ocr-workaround`                          |
| `--disable-ocr-workaround`      | Disable OCR workaround for scanned documents. This will skip OCR processing even if the document is detected as scanned. See documentation for details. (default: False)                             | `pdf2zh_next example.pdf --disable-ocr-workaround`                         |

---

### TRANSLATION

| `--auto-enable-ocr-workaround`  | 自動 OCR 回避策を有効にします。文書がスキャンが多用されていると検出された場合、OCR 処理を有効にし、さらなるスキャン検出をスキップしようとします。詳細はドキュメントを参照してください。（デフォルト：False） | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--enable-ocr-workaround`       | スキャン文書に対する OCR 回避策を有効にします。文書がスキャンされていると検出されない場合でも、OCR 処理を強制的に実行します。詳細はドキュメントを参照してください。（デフォルト：False）                         | `pdf2zh_next example.pdf --enable-ocr-workaround`                          |
| `--disable-ocr-workaround`      | スキャン文書に対する OCR 回避策を無効にします。文書がスキャンされていると検出された場合でも、OCR 処理をスキップします。詳細はドキュメントを参照してください。（デフォルト：False）                             | `pdf2zh_next example.pdf --disable-ocr-workaround`                         |
| `--only-include-translated-page`| 出力 PDF に翻訳済みページのみを含める。--pages が使用された場合のみ有効。  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| `--no-merge-alternating-line-numbers` | 行番号付き文書における行番号とテキスト段落の交互マージを無効化 | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-remove-non-inline-lines`  | Disable removal of non-inline formula lines within paragraph areas                      | `pdf2zh_next example.pdf --no-remove-non-inline-lines`                                                                |
| `--no-remove-non-display-lines` | Disable removal of non-display formula lines within paragraph areas                     | `pdf2zh_next example.pdf --no-remove-non-display-lines`                                                               |
| `--no-remove-lines`             | Disable all line removal operations within paragraph areas. Equivalent to enabling all three options above. | `pdf2zh_next example.pdf --no-remove-lines`                                                                           |

---

### TRANSLATED TEXT

| `--no-remove-non-formula-lines` | 段落エリア内の非数式行の除去を無効化する                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-remove-non-inline-lines`  | 段落エリア内の非インライン数式行の除去を無効化する                      | `pdf2zh_next example.pdf --no-remove-non-inline-lines`                                                                |
| `--no-remove-non-display-lines` | 段落エリア内の非ディスプレイ数式行の除去を無効化する                     | `pdf2zh_next example.pdf --no-remove-non-display-lines`                                                               |
| `--no-remove-lines`             | 段落エリア内のすべての行除去操作を無効化する。上記の 3 つのオプションをすべて有効にすることと同等。 | `pdf2zh_next example.pdf --no-remove-lines`                                                                           |
`0.8`       |
| `--non-formula-line-ignore-gap`    | Set maximum gap to ignore between non-formula lines (px)                           | `pdf2zh_next example.pdf --non-formula-line-ignore-gap 10`                                                            | `5`         |
| `--non-formula-line-ignore-length` | Set minimum length to ignore for non-formula lines (px)                            | `pdf2zh_next example.pdf --non-formula-line-ignore-length 20`                                                         | `10`        |

---

### OUTPUT

| `--non-formula-line-iou-threshold` | 非数式行を識別するための IoU 閾値を設定 (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.8`       |
| `--non-formula-line-ignore-gap`    | 非数式行間で無視する最大ギャップを設定 (px)                           | `pdf2zh_next example.pdf --non-formula-line-ignore-gap 10`                                                            | `5`         |
| `--non-formula-line-ignore-length` | 非数式行で無視する最小の長さを設定 (px)                            | `pdf2zh_next example.pdf --non-formula-line-ignore-length 20`                                                         | `10`        |
`0.9`                  |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------- |
| `--ocr`                               | Force OCR processing for all pages                                                                          | `pdf2zh_next example.pdf --ocr`                                                                           | `False`                |
| `--ocr-only`                          | Only perform OCR without translation                                                                        | `pdf2zh_next example.pdf --ocr-only`                                                                      | `False`                |
| `--no-ocr`                            | Disable OCR processing                                                                                      | `pdf2zh_next example.pdf --no-ocr`                                                                        | `False`                |
| `--ocr-method`                        | Specify OCR method (e.g., 'tesseract', 'paddle')                                                            | `pdf2zh_next example.pdf --ocr-method paddle`                                                             | `tesseract`            |
| `--ocr-lang`                          | Specify OCR language (e.g., 'chi_sim', 'jpn')                                                               | `pdf2zh_next example.pdf --ocr-lang chi_sim`                                                              | `chi_sim+eng`          |
| `--ocr-dpi`                           | Set DPI for OCR processing                                                                                  | `pdf2zh_next example.pdf --ocr-dpi 300`                                                                   | `300`                  |
| `--ocr-pages`                         | Specify pages for OCR processing (e.g., '1-5,8,10-15')                                                      | `pdf2zh_next example.pdf --ocr-pages 1-5,8,10-15`                                                         | `None` (all pages)     |
| `--ocr-timeout`                       | Set timeout for OCR processing (seconds)                                                                    | `pdf2zh_next example.pdf --ocr-timeout 120`                                                               | `120`                  |
| `--ocr-retry`                         | Number of retries for OCR processing                                                                        | `pdf2zh_next example.pdf --ocr-retry 3`                                                                   | `3`                    |
| `--ocr-skip-text`                     | Skip OCR for pages with existing text                                                                       | `pdf2zh_next example.pdf --ocr-skip-text`                                                                 | `False`                |
| `--ocr-engine`                        | Choose OCR engine ('tesseract' or 'paddle')                                                                 | `pdf2zh_next example.pdf --ocr-engine paddle`                                                             | `tesseract`            |
| `--ocr-paddle-lang`                   | Language for PaddleOCR (e.g., 'ch', 'en', 'japan')                                                          | `pdf2zh_next example.pdf --ocr-paddle-lang ch`                                                            | `ch`                   |
| `--ocr-tesseract-lang`                | Language for TesseractOCR (e.g., 'chi_sim', 'jpn')                                                          | `pdf2zh_next example.pdf --ocr-tesseract-lang chi_sim`                                                    | `chi_sim+eng`          |
| `--ocr-tesseract-cmd`                 | Path to tesseract command                                                                                   | `pdf2zh_next example.pdf --ocr-tesseract-cmd /usr/bin/tesseract`                                          | `tesseract`            |
| `--ocr-paddle-cmd`                    | Path to paddleocr command                                                                                   | `pdf2zh_next example.pdf --ocr-paddle-cmd /usr/bin/paddleocr`                                             | `paddleocr`            |
| `--ocr-paddle-model`                  | Model for PaddleOCR ('ocr' or 'structure')                                                                  | `pdf2zh_next example.pdf --ocr-paddle-model structure`                                                    | `structure`            |
| `--ocr-paddle-layout`                 | Use layout analysis for PaddleOCR                                                                           | `pdf2zh_next example.pdf --ocr-paddle-layout`                                                             | `False`                |
| `--ocr-paddle-lang`                   | Language for PaddleOCR (e.g., 'ch', 'en', 'japan')                                                          | `pdf2zh_next example.pdf --ocr-paddle-lang ch`                                                            | `ch`                   |
| `--ocr-paddle-whitelist`              | Whitelist characters for PaddleOCR                                                                          | `pdf2zh_next example.pdf --ocr-paddle-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`                   | `None`                 |
| `--ocr-paddle-blacklist`              | Blacklist characters for PaddleOCR                                                                          | `pdf2zh_next example.pdf --ocr-paddle-blacklist "!@#$%^&*()"`                                             | `None`                 |
| `--ocr-tesseract-psm`                 | Page segmentation mode for TesseractOCR (0-13)                                                              | `pdf2zh_next example.pdf --ocr-tesseract-psm 6`                                                           | `6`                    |
| `--ocr-tesseract-oem`                 | OCR Engine mode for TesseractOCR (0-3)                                                                      | `pdf2zh_next example.pdf --ocr-tesseract-oem 3`                                                           | `3`                    |
| `--ocr-tesseract-whitelist`           | Whitelist characters for TesseractOCR                                                                       | `pdf2zh_next example.pdf --ocr-tesseract-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`                | `None`                 |
| `--ocr-tesseract-blacklist`           | Blacklist characters for TesseractOCR                                                                       | `pdf2zh_next example.pdf --ocr-tesseract-blacklist "!@#$%^&*()"`                                          | `None`                 |
| `--ocr-tesseract-config`              | Additional config for TesseractOCR                                                                          | `pdf2zh_next example.pdf --ocr-tesseract-config "tessedit_char_whitelist=0123456789"`                     | `None`                 |
| `--ocr-tesseract-timeout`             | Timeout for TesseractOCR (seconds)                                                                          | `pdf2zh_next example.pdf --ocr-tesseract-timeout 60`                                                      | `60`                   |
| `--ocr-tesseract-retry`               | Number of retries for TesseractOCR                                                                          | `pdf2zh_next example.pdf --ocr-tesseract-retry 3`                                                         | `3`                    |
| `--ocr-paddle-timeout`                | Timeout for PaddleOCR (seconds)                                                                             | `pdf2zh_next example.pdf --ocr-paddle-timeout 60`                                                         | `60`                   |
| `--ocr-paddle-retry`                  | Number of retries for PaddleOCR                                                                             | `pdf2zh_next example.pdf --ocr-paddle-retry 3`                                                            | `3`                    |

---

### TRANSLATION RESULT

| `--figure-table-protection-threshold` | 図表の保護閾値を設定（0.0-1.0）。図表内の行は処理されません                                                                             | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        | `0.9`                  |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------- |
| `--ocr`                               | 全ページに対して OCR 処理を強制実行                                                                                                     | `pdf2zh_next example.pdf --ocr`                                                                           | `False`                |
| `--ocr-only`                          | 翻訳を行わず、OCR のみを実行                                                                                                            | `pdf2zh_next example.pdf --ocr-only`                                                                      | `False`                |
| `--no-ocr`                            | OCR 処理を無効化                                                                                                                        | `pdf2zh_next example.pdf --no-ocr`                                                                        | `False`                |
| `--ocr-method`                        | OCR メソッドを指定（例：`tesseract`、`paddle`）                                                                                         | `pdf2zh_next example.pdf --ocr-method paddle`                                                             | `tesseract`            |
| `--ocr-lang`                          | OCR 言語を指定（例：`chi_sim`、`jpn`）                                                                                                  | `pdf2zh_next example.pdf --ocr-lang chi_sim`                                                              | `chi_sim+eng`          |
| `--ocr-dpi`                           | OCR 処理の DPI を設定                                                                                                                   | `pdf2zh_next example.pdf --ocr-dpi 300`                                                                   | `300`                  |
| `--ocr-pages`                         | OCR 処理を行うページを指定（例：`1-5,8,10-15`）                                                                                         | `pdf2zh_next example.pdf --ocr-pages 1-5,8,10-15`                                                         | `None`（全ページ）       |
| `--ocr-timeout`                       | OCR 処理のタイムアウトを設定（秒）                                                                                                      | `pdf2zh_next example.pdf --ocr-timeout 120`                                                               | `120`                  |
| `--ocr-retry`                         | OCR 処理のリトライ回数を設定                                                                                                            | `pdf2zh_next example.pdf --ocr-retry 3`                                                                   | `3`                    |
| `--ocr-skip-text`                     | 既存のテキストがあるページの OCR をスキップ                                                                                             | `pdf2zh_next example.pdf --ocr-skip-text`                                                                 | `False`                |
| `--ocr-engine`                        | OCR エンジンを選択（`tesseract` または `paddle`）                                                                                       | `pdf2zh_next example.pdf --ocr-engine paddle`                                                             | `tesseract`            |
| `--ocr-paddle-lang`                   | PaddleOCR の言語を指定（例：`ch`、`en`、`japan`）                                                                                       | `pdf2zh_next example.pdf --ocr-paddle-lang ch`                                                            | `ch`                   |
| `--ocr-tesseract-lang`                | TesseractOCR の言語を指定（例：`chi_sim`、`jpn`）                                                                                       | `pdf2zh_next example.pdf --ocr-tesseract-lang chi_sim`                                                    | `chi_sim+eng`          |
| `--ocr-tesseract-cmd`                 | tesseract コマンドへのパスを指定                                                                                                        | `pdf2zh_next example.pdf --ocr-tesseract-cmd /usr/bin/tesseract`                                          | `tesseract`            |
| `--ocr-paddle-cmd`                    | paddleocr コマンドへのパスを指定                                                                                                        | `pdf2zh_next example.pdf --ocr-paddle-cmd /usr/bin/paddleocr`                                             | `paddleocr`            |
| `--ocr-paddle-model`                  | PaddleOCR のモデルを指定（`ocr` または `structure`）                                                                                    | `pdf2zh_next example.pdf --ocr-paddle-model structure`                                                    | `structure`            |
| `--ocr-paddle-layout`                 | PaddleOCR でレイアウト解析を使用                                                                                                        | `pdf2zh_next example.pdf --ocr-paddle-layout`                                                             | `False`                |
| `--ocr-paddle-lang`                   | PaddleOCR の言語を指定（例：`ch`、`en`、`japan`）                                                                                       | `pdf2zh_next example.pdf --ocr-paddle-lang ch`                                                            | `ch`                   |
| `--ocr-paddle-whitelist`              | PaddleOCR のホワイトリスト文字を指定                                                                                                    | `pdf2zh_next example.pdf --ocr-paddle-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`                   | `None`                 |
| `--ocr-paddle-blacklist`              | PaddleOCR のブラックリスト文字を指定                                                                                                    | `pdf2zh_next example.pdf --ocr-paddle-blacklist "!@#$%^&*()"`                                             | `None`                 |
| `--ocr-tesseract-psm`                 | TesseractOCR のページ分割モードを指定（0-13）                                                                                           | `pdf2zh_next example.pdf --ocr-tesseract-psm 6`                                                           | `6`                    |
| `--ocr-tesseract-oem`                 | TesseractOCR の OCR エンジンモードを指定（0-3）                                                                                         | `pdf2zh_next example.pdf --ocr-tesseract-oem 3`                                                           | `3`                    |
| `--ocr-tesseract-whitelist`           | TesseractOCR のホワイトリスト文字を指定                                                                                                 | `pdf2zh_next example.pdf --ocr-tesseract-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`                | `None`                 |
| `--ocr-tesseract-blacklist`           | TesseractOCR のブラックリスト文字を指定                                                                                                 | `pdf2zh_next example.pdf --ocr-tesseract-blacklist "!@#$%^&*()"`                                          | `None`                 |
| `--ocr-tesseract-config`              | TesseractOCR の追加設定を指定                                                                                                           | `pdf2zh_next example.pdf --ocr-tesseract-config "tessedit_char_whitelist=0123456789"`                     | `None`                 |
| `--ocr-tesseract-timeout`             | TesseractOCR のタイムアウトを設定（秒）                                                                                                 | `pdf2zh_next example.pdf --ocr-tesseract-timeout 60`                                                      | `60`                   |
| `--ocr-tesseract-retry`               | TesseractOCR のリトライ回数を設定                                                                                                       | `pdf2zh_next example.pdf --ocr-tesseract-retry 3`                                                         | `3`                    |
| `--ocr-paddle-timeout`                | PaddleOCR のタイムアウトを設定（秒）                                                                                                    | `pdf2zh_next example.pdf --ocr-paddle-timeout 60`                                                         | `60`                   |
| `--ocr-paddle-retry`                  | PaddleOCR のリトライ回数を設定                                                                                                          | `pdf2zh_next example.pdf --ocr-paddle-retry 3`                                                            | `3`                    |
---

### OUTPUT

| `--skip-formula-offset-calculation` | 処理中に数式のオフセット計算をスキップする          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### GUI 引数

| `--server_name`                 | Set server name                        | `pdf2zh_next --gui --server_name 0.0.0.0`       |
| `--server_port`                 | Set server port                        | `pdf2zh_next --gui --server_port 7860`          |
| `--auth`                        | Set authentication                     | `pdf2zh_next --gui --auth username:password`   |
| `--ssl_keyfile`                 | Set SSL keyfile                        | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile`                | Set SSL certfile                       | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--concurrency-count`           | Set concurrency count                  | `pdf2zh_next --gui --concurrency-count 10`      |
| `--max-file-size`               | Set max file size                      | `pdf2zh_next --gui --max-file-size 100`         |
| `--allowed-paths`               | Set allowed paths                      | `pdf2zh_next --gui --allowed-paths /path/to/dir`|
| `--theme`                       | Set theme                              | `pdf2zh_next --gui --theme dark`                |
| `--show-error`                  | Show error                             | `pdf2zh_next --gui --show-error`                |
| `--debug`                       | Enable debug mode                      | `pdf2zh_next --gui --debug`                     |

---

### TRANSLATION

| オプション                          | 機能                               | 例                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | 共有モードを有効にする                    | `pdf2zh_next --gui --share`                     |
| `--server_name`                 | サーバー名を設定する                        | `pdf2zh_next --gui --server_name 0.0.0.0`       |
| `--server_port`                 | サーバーポートを設定する                        | `pdf2zh_next --gui --server_port 7860`          |
| `--auth`                        | 認証を設定する                     | `pdf2zh_next --gui --auth username:password`   |
| `--ssl_keyfile`                 | SSL キーファイルを設定する                        | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile`                | SSL 証明書ファイルを設定する                       | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--concurrency-count`           | 同時実行数を設定する                  | `pdf2zh_next --gui --concurrency-count 10`      |
| `--max-file-size`               | 最大ファイルサイズを設定する                      | `pdf2zh_next --gui --max-file-size 100`         |
| `--allowed-paths`               | 許可されたパスを設定する                      | `pdf2zh_next --gui --allowed-paths /path/to/dir`|
| `--theme`                       | テーマを設定する                              | `pdf2zh_next --gui --theme dark`                |
| `--show-error`                  | エラーを表示する                             | `pdf2zh_next --gui --show-error`                |
| `--debug`                       | デバッグモードを有効にする                      | `pdf2zh_next --gui --debug`                     |
If you have a large number of API keys, you can store them in a file and use this parameter to specify the path to that file. The format of the file should be one API key per line. |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--auth-str`                    | Authentication string                  | `pdf2zh_next --gui --auth-str "key1,key2,key3"` | Directly input the API keys, separated by commas.                                                                                                                                 |
| `--auth-env`                    | Environment variable name              | `pdf2zh_next --gui --auth-env MY_API_KEYS`      | Read API keys from an environment variable. The format should be a string of keys separated by commas.                                                                             |
| `--auth-command`                | Command to retrieve auth keys          | `pdf2zh_next --gui --auth-command "command"`    | Execute a command to retrieve the API keys. The command's output should be a string of keys separated by commas.                                                                   |
| `--auth-command-env`            | Environment variable for auth command  | `pdf2zh_next --gui --auth-command-env VAR_NAME` | Set an environment variable for the auth command.                                                                                                                                 |
| `--auth-command-timeout`        | Timeout for auth command (seconds)     | `pdf2zh_next --gui --auth-command-timeout 10`   | Set the timeout for the auth command execution. Default is 10 seconds.                                                                                                            |
| `--auth-retry-count`            | Number of retries for auth command     | `pdf2zh_next --gui --auth-retry-count 3`        | Number of times to retry the auth command if it fails. Default is 3.                                                                                                              |
| `--auth-retry-interval`         | Interval between retries (seconds)     | `pdf2zh_next --gui --auth-retry-interval 5`     | Interval between retries for the auth command. Default is 5 seconds.                                                                                                              |

---

### TRANSLATED TEXT

| `--auth-file`                   | 認証ファイルのパス                     | `pdf2zh_next --gui --auth-file /path`           | 大量の API キーがある場合、それらをファイルに保存し、このパラメータを使用してそのファイルのパスを指定できます。ファイルの形式は、1 行に 1 つの API キーを記述する必要があります。 |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--auth-str`                    | 認証文字列                             | `pdf2zh_next --gui --auth-str "key1,key2,key3"` | API キーを直接入力し、カンマで区切ります。                                                                                                                                         |
| `--auth-env`                    | 環境変数名                             | `pdf2zh_next --gui --auth-env MY_API_KEYS`      | 環境変数から API キーを読み取ります。形式は、カンマで区切られたキーの文字列である必要があります。                                                                                   |
| `--auth-command`                | 認証キーを取得するコマンド             | `pdf2zh_next --gui --auth-command "command"`    | API キーを取得するコマンドを実行します。コマンドの出力は、カンマで区切られたキーの文字列である必要があります。                                                                      |
| `--auth-command-env`            | 認証コマンドの環境変数                 | `pdf2zh_next --gui --auth-command-env VAR_NAME` | 認証コマンドの環境変数を設定します。                                                                                                                                               |
| `--auth-command-timeout`        | 認証コマンドのタイムアウト（秒）       | `pdf2zh_next --gui --auth-command-timeout 10`   | 認証コマンド実行のタイムアウトを設定します。デフォルトは 10 秒です。                                                                                                               |
| `--auth-retry-count`            | 認証コマンドの再試行回数               | `pdf2zh_next --gui --auth-retry-count 3`        | 認証コマンドが失敗した場合の再試行回数。デフォルトは 3 回です。                                                                                                                    |
| `--auth-retry-interval`         | 再試行間隔（秒）                       | `pdf2zh_next --gui --auth-retry-interval 5`     | 認証コマンドの再試行間隔。デフォルトは 5 秒です。                                                                                                                                  |
[Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html) |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------- |
| `--help`                        | Print help                             | `pdf2zh_next --help`                            | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html) |

---

### OUTPUT

| `--welcome-page`                | ウェルカム HTML ファイルのパス          | `pdf2zh_next --gui --welcome-page /path`        | [**WebUI** の使い方](https://pdf2zh-next.com/getting-started/USAGE_webui.html) |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------------------- |
| `--help`                        | ヘルプを表示                             | `pdf2zh_next --help`                            | [**コマンドライン** の使い方](https://pdf2zh-next.com/getting-started/USAGE_cli.html) |
Enable `Bing` and `OpenAI` translation services. |
|---------------------------------|----------------------------------------|-----------------------------------------------------|--------------------------------------------------|
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Bing"`      | Disable `Bing` translation service.              |
| `--target-language`             | Target language                        | `pdf2zh_next --gui --target-language "ja"`          | Set target language to Japanese.                 |
| `--source-language`             | Source language                        | `pdf2zh_next --gui --source-language "en"`          | Set source language to English.                  |
| `--proxy`                       | Proxy server                           | `pdf2zh_next --gui --proxy "http://127.0.0.1:7890"` | Set proxy server address.                        |
| `--timeout`                     | Request timeout (seconds)              | `pdf2zh_next --gui --timeout 30`                    | Set request timeout to 30 seconds.               |
| `--retry-attempts`              | Number of retry attempts               | `pdf2zh_next --gui --retry-attempts 3`              | Set retry attempts to 3 times.                   |
| `--retry-delay`                 | Retry delay (seconds)                  | `pdf2zh_next --gui --retry-delay 5`                 | Set retry delay to 5 seconds.                    |
| `--max-workers`                 | Maximum number of workers              | `pdf2zh_next --gui --max-workers 5`                 | Set maximum workers to 5.                        |
| `--chunk-size`                  | Chunk size for translation             | `pdf2zh_next --gui --chunk-size 1000`               | Set chunk size to 1000 characters.               |
| `--batch-size`                  | Batch size for translation             | `pdf2zh_next --gui --batch-size 10`                 | Set batch size to 10 chunks.                     |
| `--output-format`               | Output format                          | `pdf2zh_next --gui --output-format "markdown"`      | Set output format to markdown.                   |
| `--output-dir`                  | Output directory                       | `pdf2zh_next --gui --output-dir "./output"`         | Set output directory to "./output".              |
| `--log-level`                   | Log level                              | `pdf2zh_next --gui --log-level "INFO"`              | Set log level to INFO.                           |
| `--log-file`                    | Log file path                          | `pdf2zh_next --gui --log-file "./app.log"`          | Set log file path to "./app.log".                |
| `--config`                      | Configuration file path                | `pdf2zh_next --gui --config "./config.json"`        | Load configuration from "./config.json".         |
| `--no-gui`                      | Disable GUI (run in CLI mode)          | `pdf2zh_next --no-gui`                               | Run in command line mode.                        |
| `--version`                     | Show version information               | `pdf2zh_next --version`                              | Display version information.                     |
| `--help`                        | Show help information                  | `pdf2zh_next --help`                                 | Display help information.                        |

---

### TRANSLATION RESULT

| `--enabled-services`            | 有効化する翻訳サービス                 | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | `Bing` と `OpenAI` の翻訳サービスを有効化します。 |
|---------------------------------|----------------------------------------|-----------------------------------------------------|--------------------------------------------------|
| `--disabled-services`           | 無効化する翻訳サービス                 | `pdf2zh_next --gui --disabled-services "Bing"`      | `Bing` の翻訳サービスを無効化します。             |
| `--target-language`             | ターゲット言語                         | `pdf2zh_next --gui --target-language "ja"`          | ターゲット言語を日本語に設定します。             |
| `--source-language`             | ソース言語                             | `pdf2zh_next --gui --source-language "en"`          | ソース言語を英語に設定します。                   |
| `--proxy`                       | プロキシサーサーバー                       | `pdf2zh_next --gui --proxy "http://127.0.0.1:7890"` | プロキシサーサーバーのアドレスを設定します。         |
| `--timeout`                     | リクエストタイムアウト（秒）           | `pdf2zh_next --gui --timeout 30`                    | リクエストタイムアウトを 30 秒に設定します。     |
| `--retry-attempts`              | リトライ試行回数                       | `pdf2zh_next --gui --retry-attempts 3`              | リトライ試行回数を 3 回に設定します。            |
| `--retry-delay`                 | リトライ遅延（秒）                     | `pdf2zh_next --gui --retry-delay 5`                 | リトライ遅延を 5 秒に設定します。                |
| `--max-workers`                 | 最大ワーカー数                         | `pdf2zh_next --gui --max-workers 5`                 | 最大ワーカー数を 5 に設定します。                |
| `--chunk-size`                  | 翻訳用のチャンクサイズ                 | `pdf2zh_next --gui --chunk-size 1000`               | チャンクサイズを 1000 文字に設定します。         |
| `--batch-size`                  | 翻訳用のバッチサイズ                   | `pdf2zh_next --gui --batch-size 10`                 | バッチサイズを 10 チャンクに設定します。         |
| `--output-format`               | 出力フォーマット                       | `pdf2zh_next --gui --output-format "markdown"`      | 出力フォーマットをマークダウンに設定します。     |
| `--output-dir`                  | 出力ディレクトリ                       | `pdf2zh_next --gui --output-dir "./output"`         | 出力ディレクトリを「`./output`」に設定します。   |
| `--log-level`                   | ログレベル                             | `pdf2zh_next --gui --log-level "INFO"`              | ログレベルを `INFO` に設定します。               |
| `--log-file`                    | ログファイルパス                       | `pdf2zh_next --gui --log-file "./app.log"`          | ログファイルパスを「`./app.log`」に設定します。  |
| `--config`                      | 設定ファイルパス                       | `pdf2zh_next --gui --config "./config.json"`        | 「`./config.json`」から設定を読み込みます。      |
| `--no-gui`                      | GUI を無効化（CLI モードで実行）       | `pdf2zh_next --no-gui`                               | コマンドラインモードで実行します。               |
| `--version`                     | バージョン情報を表示                   | `pdf2zh_next --version`                              | バージョン情報を表示します。                     |
| `--help`                        | ヘルプ情報を表示                       | `pdf2zh_next --help`                                 | ヘルプ情報を表示します。                         |
- |

---

### OUTPUT

| `--disable-gui-sensitive-input` | GUI のセンシティブ入力を無効にする           | `pdf2zh_next --gui --disable-gui-sensitive-input` | - |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--disable-config`              | Disable configuration file loading     | `pdf2zh_next --gui --disable-config`            |

---

### OUTPUT

| `--disable-config-auto-save`    | 自動設定保存を無効にする | `pdf2zh_next --gui --disable-config-auto-save`  | 
|---------------------------------|--------------------------|-------------------------------------------------|
| `--disable-config`              | 設定ファイルの読み込みを無効にする | `pdf2zh_next --gui --disable-config`            |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | WebUI Host                             | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--share`                       | Enable Public Network Access           | `pdf2zh_next --gui --share`                     |
| `--auth USERNAME:PASSWORD`      | Set Username and Password              | `pdf2zh_next --gui --auth admin:admin123`       |
| `--auth USERNAME:PASSWORD_FILE` | Set Username and Password from a File  | `pdf2zh_next --gui --auth admin:password.txt`   |
| `--ssl-keyfile KEYFILE_PATH`    | SSL Key File Path                      | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile CERTFILE_PATH`  | SSL Certificate File Path              | `pdf2zh_next --gui --ssl-certfile cert.pem`     |

---

### TRANSLATION

| `--server-port`                 | WebUI ポート                           | `pdf2zh_next --gui --server-port 7860`          |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | WebUI ホスト                           | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--share`                       | パブリックネットワークアクセスを有効化 | `pdf2zh_next --gui --share`                     |
| `--auth USERNAME:PASSWORD`      | ユーザー名とパスワードを設定           | `pdf2zh_next --gui --auth admin:admin123`       |
| `--auth USERNAME:PASSWORD_FILE` | ファイルからユーザー名とパスワードを設定 | `pdf2zh_next --gui --auth admin:password.txt`   |
| `--ssl-keyfile KEYFILE_PATH`    | SSL キーファイルのパス                 | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile CERTFILE_PATH`  | SSL 証明書ファイルのパス               | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--model`                       | Model name                             | `pdf2zh_next --gui --model gpt-4o`              |
| `--api-key`                     | API key                                | `pdf2zh_next --gui --api-key sk-...`            |
| `--base-url`                    | API base URL                           | `pdf2zh_next --gui --base-url https://api.openai.com` |
| `--translation-service`         | Translation service                    | `pdf2zh_next --gui --translation-service azure` |
| `--region`                      | Region                                 | `pdf2zh_next --gui --region eastasia`           |
| `--concurrent-limit`            | Concurrent request limit               | `pdf2zh_next --gui --concurrent-limit 10`       |
| `--timeout`                     | Request timeout (seconds)              | `pdf2zh_next --gui --timeout 60`                |
| `--retry-attempts`              | Retry attempts                         | `pdf2zh_next --gui --retry-attempts 3`          |
| `--retry-delay`                 | Retry delay (seconds)                  | `pdf2zh_next --gui --retry-delay 2`             |
| `--http-proxy`                  | HTTP proxy                             | `pdf2zh_next --gui --http-proxy http://127.0.0.1:7890` |
| `--socks-proxy`                 | SOCKS proxy                            | `pdf2zh_next --gui --socks-proxy socks5://127.0.0.1:7891` |
| `--log-level`                   | Log level (DEBUG/INFO/WARNING/ERROR)   | `pdf2zh_next --gui --log-level DEBUG`           |
| `--log-file`                    | Log file path                          | `pdf2zh_next --gui --log-file ./app.log`        |
| `--config-file`                 | Config file path                       | `pdf2zh_next --gui --config-file ./config.json` |
| `--cache-dir`                   | Cache directory                        | `pdf2zh_next --gui --cache-dir ./cache`         |
| `--theme`                       | Theme (light/dark/auto)                | `pdf2zh_next --gui --theme dark`                |

---

### TRANSLATED TEXT

| `--ui-lang`                     | UI 言語                                | `pdf2zh_next --gui --ui-lang zh`                |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--model`                       | モデル名                               | `pdf2zh_next --gui --model gpt-4o`              |
| `--api-key`                     | API キー                              | `pdf2zh_next --gui --api-key sk-...`            |
| `--base-url`                    | API ベース URL                         | `pdf2zh_next --gui --base-url https://api.openai.com` |
| `--translation-service`         | 翻訳サービス                           | `pdf2zh_next --gui --translation-service azure` |
| `--region`                      | リージョン                             | `pdf2zh_next --gui --region eastasia`           |
| `--concurrent-limit`            | 同時リクエスト制限                     | `pdf2zh_next --gui --concurrent-limit 10`       |
| `--timeout`                     | リクエストタイムアウト（秒）           | `pdf2zh_next --gui --timeout 60`                |
| `--retry-attempts`              | リトライ試行回数                       | `pdf2zh_next --gui --retry-attempts 3`          |
| `--retry-delay`                 | リトライ遅延（秒）                     | `pdf2zh_next --gui --retry-delay 2`             |
| `--http-proxy`                  | HTTP プロキシ                         | `pdf2zh_next --gui --http-proxy http://127.0.0.1:7890` |
| `--socks-proxy`                 | SOCKS プロキシ                        | `pdf2zh_next --gui --socks-proxy socks5://127.0.0.1:7891` |
| `--log-level`                   | ログレベル（DEBUG/INFO/WARNING/ERROR） | `pdf2zh_next --gui --log-level DEBUG`           |
| `--log-file`                    | ログファイルパス                       | `pdf2zh_next --gui --log-file ./app.log`        |
| `--config-file`                 | 設定ファイルパス                       | `pdf2zh_next --gui --config-file ./config.json` |
| `--cache-dir`                   | キャッシュディレクトリ                 | `pdf2zh_next --gui --cache-dir ./cache`         |
| `--theme`                       | テーマ（light/dark/auto）              | `pdf2zh_next --gui --theme dark`                |

[⬆️ トップに戻る](#toc)

---

#### レート制限設定ガイド

翻訳サービスを利用する際、適切なレート制限設定は API エラーを回避し、パフォーマンスを最適化するために重要です。このガイドでは、異なる上流サービスの制限に基づいて `--qps` と `--pool-max-worker` パラメータを設定する方法を説明します。

> [!TIP]
>
> pool_size は 1000 を超えないことが推奨されます。以下の方法で計算された pool_size が 1000 を超える場合は、1000 を使用してください。

##### RPM (リクエスト毎分) レート制限

上流サービスに RPM 制限がある場合、以下の計算式を使用します：

**計算式：**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> 10 という係数は、ほとんどのシナリオでうまく機能する経験的な係数です。

**例：**
翻訳サービスの制限が 600 RPM の場合：
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### 同時接続制限

上流サービスに同時接続制限がある場合（GLM 公式サービスなど）、この方法を使用します：

**計算式：**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**例：**
翻訳サービスが 50 の同時接続を許可している場合：
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### ベストプラクティス

> [!TIP]
> - 常に控えめな値から始め、必要に応じて徐々に増やしてください
> - サービスの応答時間とエラーレートを監視してください
> - サービスによって最適化戦略が異なる場合があります
> - これらのパラメータを設定する際は、具体的なユースケースとドキュメントサイズを考慮してください


[⬆️ トップに戻る](#toc)

---

#### 部分翻訳

`--pages` パラメータを使用して、ドキュメントの一部を翻訳します。

- ページ番号が連続している場合、以下のように記述できます：

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` は 25 ページ以降のすべてのページを含みます。ドキュメントが 100 ページある場合、これは `25-100` と同じです。
> 
> 同様に、`-25` は 25 ページより前のすべてのページを含み、これは `1-25` と同じです。

- ページが連続していない場合は、カンマ `,` を使用して区切ることができます。

例えば、最初と 3 ページ目を翻訳したい場合、次のコマンドを使用できます：

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- ページに連続した範囲と非連続した範囲の両方が含まれている場合、以下のようにカンマで接続することもできます：

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

このコマンドは、最初のページ、3 ページ目、10～20 ページ、および 25 ページから最後までのすべてのページを翻訳します。


[⬆️ トップに戻る](#toc)

---

#### ソース言語とターゲット言語の指定

[Google 言語コード](https://developers.google.com/admin-sdk/directory/v1/languages)、[DeepL 言語コード](https://developers.deepl.com/docs/resources/supported-languages) を参照してください

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ トップに戻る](#toc)

---

#### 例外付きで翻訳する

正規表現を使用して、保持する必要がある数式フォントと文字を指定します：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

デフォルトで `Latex`、`Mono`、`Code`、`Italic`、`Symbol`、`Math` フォントを保持します：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ トップに戻る](#toc)

---

#### カスタムプロンプト

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

翻訳用のカスタムシステムプロンプト。主に Qwen 3 の `/no_think` 命令をプロンプトに追加するために使用されます。

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ トップに戻る](#toc)

---

#### カスタム設定

設定ファイルを変更およびインポートする方法は複数あります。

> [!NOTE]
> **設定ファイルの階層**
>
> 同じパラメータを異なる方法で変更する場合、ソフトウェアは以下の優先順位に従って変更を適用します。
>
> 上位の変更は下位の変更を上書きします。
>
> **cli/gui > env > ユーザー設定ファイル > デフォルト設定ファイル**

- **コマンドライン引数** を介した設定の変更

ほとんどの場合、コマンドライン引数を通じて希望の設定を直接渡すことができます。詳細については、[コマンドライン引数](#cmd) を参照してください。

例えば、GUI ウィンドウを有効にしたい場合は、次のコマンドを使用できます：

```bash
pdf2zh_next --gui
```

- **環境変数** を介した設定の変更

コマンドライン引数の `--` を `PDF2ZH_` に置き換え、パラメータを `=` で接続し、`-` を `_` に置き換えて環境変数として使用できます。

例えば、GUI ウィンドウを有効にする場合は、以下のコマンドを使用できます：

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- ユーザー指定の **設定ファイル**

以下のコマンドライン引数を使用して設定ファイルを指定できます：

```bash
pdf2zh_next --config-file '/path/config.toml'
```

設定ファイルの形式が分からない場合は、以下のデフォルト設定ファイルを参照してください。

- **デフォルト設定ファイル**

デフォルトの設定ファイルは `~/.config/pdf2zh` にあります。  
`default` ディレクトリ内の設定ファイルは変更しないでください。  
この設定ファイルの内容を参照し、**ユーザー指定の設定ファイル**を使用して独自の設定ファイルを実装することを強くお勧めします。

> [!TIP]
> - デフォルトでは、pdf2zh 2.0 は GUI で翻訳ボタンをクリックするたびに現在の設定を `~/.config/pdf2zh/config.v3.toml` に自動的に保存します。この設定ファイルは次回起動時にデフォルトで読み込まれます。
> - `default` ディレクトリ内の設定ファイルはプログラムによって自動生成されます。修正のためにコピーすることは可能ですが、直接編集しないでください。
> - 設定ファイルには「v2」「v3」などのバージョン番号が含まれる場合があります。これらは**設定ファイルのバージョン番号**であり、pdf2zh 自体のバージョン番号**ではありません**。


[⬆️ トップに戻る](#toc)

---

#### クリーンをスキップ

このパラメータが True に設定されている場合、PDF のクリーンアップステップがスキップされ、互換性が向上し、一部のフォント処理の問題を回避できます。

使い方：

```bash
pdf2zh_next example.pdf --skip-clean
```

または環境変数を使用する：

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> `--enhance-compatibility` が有効な場合、クリーンをスキップは自動的に有効になります。

---

#### 翻訳キャッシュ

PDFMathTranslate は翻訳済みのテキストをキャッシュし、同じ内容に対する不要な API 呼び出しを避けつつ速度を向上させます。`--ignore-cache` オプションを使用すると、翻訳キャッシュを無視して強制的に再翻訳を行うことができます。

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ トップに戻る](#toc)

---

#### 公開サービスとしてのデプロイ

公開サービスで pdf2zh GUI をデプロイする場合、以下のように設定ファイルを変更する必要があります。

> [!WARNING]
>
> このプロジェクトはセキュリティに関する専門的な監査を受けておらず、セキュリティ上の脆弱性が含まれている可能性があります。パブリックネットワークにデプロイする前に、リスクを評価し、必要なセキュリティ対策を講じてください。


> [!TIP]
> - 公開デプロイ時には、`disable_gui_sensitive_input` と `disable_config_auto_save` の両方を有効にする必要があります。
> - 利用可能な異なるサービスは *英語のカンマ* <kbd>,</kbd> で区切ってください。

以下の設定が利用可能です：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ トップに戻る](#toc)

---

#### 認証とウェルカムページ

認証とウェルカムページを使用して、どのユーザーが Web UI を使用し、ログインページをカスタマイズするかを指定する場合：

例 auth.txt
各行には、ユーザー名とパスワードの 2 つの要素が含まれており、カンマで区切られています。

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

例 welcome.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my simple HTML page.</p>
</body>
</html>
```

> [!NOTE]
> 認証ファイルが空白でない場合のみ、ウェルカムページが機能します。
> 認証ファイルが空白の場合、認証は行われません。 :)

以下の設定が利用可能です：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ トップに戻る](#toc)

---

#### 用語集サポート

PDFMathTranslate は用語集テーブルをサポートしています。用語集テーブルファイルは `csv` ファイルである必要があります。
ファイルには 3 つの列があります。以下はデモ用の用語集ファイルです：

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自動 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


CLI ユーザー向け：
用語集に複数のファイルを使用できます。異なるファイルは `,` で区切る必要があります。

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

WebUI ユーザー向け：

独自の用語集ファイルをアップロードできるようになりました。ファイルをアップロードした後、名前をクリックして内容を確認できます。内容は下に表示されます。

[⬆️ トップに戻る](#toc)

<div align="right"> 
<h6><small>このページの一部のコンテンツは GPT によって翻訳されており、エラーが含まれている可能性があります。</small></h6>