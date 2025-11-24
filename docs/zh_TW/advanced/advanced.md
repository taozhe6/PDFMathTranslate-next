[**高級選項**](./introduction.md) > **高級選項** _(目前頁面)_

---

<h3 id="目錄">目錄</h3>

- [命令行參數](#命令行參數)
- [速率限制配置指南](#速率限制配置指南)
- [部分翻譯](#部分翻譯)
- [指定源語言與目標語言](#指定源語言與目標語言)
- [帶例外條件的翻譯](#帶例外條件的翻譯)
- [自定義提示詞](#自定義提示詞)
- [自定義配置](#自定義配置)
- [跳過清理](#跳過清理)
- [翻譯緩存](#翻譯緩存)
- [部署為公共服務](#部署為公共服務)
- [認證與歡迎頁面](#認證與歡迎頁面)
- [術語表支持](#術語表支持)

---

#### 命令行參數

在命令行中執行翻譯指令，於當前工作目錄下生成翻譯後的文檔 `example-mono.pdf` 與雙語文檔 `example-dual.pdf`。預設使用 Google 作為翻譯服務。更多支援的翻譯服務可查閱 [HERE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services)。

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

在以下表格中，我們列出所有高級選項以供參考：

##### 參數

| `output-folder`                 | Output folder for translated files                                                      | `pdf2zh_next example.pdf --output-folder /path/to/output`                                                              |
| `output-filename`               | Output filename (without extension)                                                     | `pdf2zh_next example.pdf --output-filename my_translated_file`                                                         |
| `output-format`                 | Output file formats (markdown, docx, pdf, tex)                                          | `pdf2zh_next example.pdf --output-format markdown pdf`                                                                 |
| `language-pair`                 | Language pair (e.g., en-zh)                                                             | `pdf2zh_next example.pdf --language-pair en-zh`                                                                       |
| `translation-service`           | Translation service (openai, azure, aliyun, siliconflow, gemini, deepseek)              | `pdf2zh_next example.pdf --translation-service openai`                                                                |
| `model`                         | Model name for the translation service                                                  | `pdf2zh_next example.pdf --model gpt-4o`                                                                              |
| `api-key`                       | API key for the translation service                                                     | `pdf2zh_next example.pdf --api-key sk-xxx`                                                                            |
| `api-base`                      | Custom API base URL                                                                     | `pdf2zh_next example.pdf --api-base https://api.openai.com/v1`                                                        |
| `concurrency`                   | Number of concurrent translation requests (default: 4)                                  | `pdf2zh_next example.pdf --concurrency 10`                                                                            |
| `max-requests-per-minute`       | Maximum requests per minute (default: varies by service)                                | `pdf2zh_next example.pdf --max-requests-per-minute 100`                                                               |
| `batch-size`                    | Number of pages to process in each batch (default: 10)                                  | `pdf2zh_next example.pdf --batch-size 20`                                                                             |
| `math-mode`                     | Math translation mode (formula, hybrid, text)                                           | `pdf2zh_next example.pdf --math-mode formula`                                                                         |
| `formula-detection-method`      | Formula detection method (ml, rule)                                                     | `pdf2zh_next example.pdf --formula-detection-method ml`                                                               |
| `formula-translation-method`    | Formula translation method (native, hybrid)                                             | `pdf2zh_next example.pdf --formula-translation-method hybrid`                                                          |
| `keep-formula`                  | Keep original formula text in translation                                               | `pdf2zh_next example.pdf --keep-formula`                                                                              |
| `glossary`                      | Glossary file for translation                                                           | `pdf2zh_next example.pdf --glossary my_glossary.txt`                                                                  |
| `glossary-strategy`             | Glossary matching strategy (fuzzy, exact)                                               | `pdf2zh_next example.pdf --glossary-strategy fuzzy`                                                                   |
| `context-window`                | Context window size for translation                                                     | `pdf2zh_next example.pdf --context-window 5`                                                                          |
| `context-method`                | Context method (none, previous, all)                                                    | `pdf2zh_next example.pdf --context-method previous`                                                                   |
| `no-table`                      | Skip table translation                                                                  | `pdf2zh_next example.pdf --no-table`                                                                                  |
| `table-translation-method`      | Table translation method (markdown, text)                                               | `pdf2zh_next example.pdf --table-translation-method markdown`                                                         |
| `no-text-split`                 | Disable text splitting                                                                  | `pdf2zh_next example.pdf --no-text-split`                                                                             |
| `split-method`                  | Text split method (sentence, paragraph, page)                                           | `pdf2zh_next example.pdf --split-method sentence`                                                                     |
| `split-length`                  | Maximum length for text splitting                                                       | `pdf2zh_next example.pdf --split-length 1000`                                                                         |
| `split-overlap`                 | Overlap length for text splitting                                                       | `pdf2zh_next example.pdf --split-overlap 50`                                                                          |
| `no-cache`                      | Disable translation cache                                                               | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `cache-dir`                     | Cache directory                                                                         | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `cache-version`                 | Cache version (for cache invalidation)                                                  | `pdf2zh_next example.pdf --cache-version 2`                                                                           |
| `resume`                        | Resume from last interruption                                                           | `pdf2zh_next example.pdf --resume`                                                                                    |
| `config`                        | Configuration file                                                                      | `pdf2zh_next example.pdf --config config.yaml`                                                                        |
| `log-level`                     | Log level (debug, info, warning, error)                                                 | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `progress`                      | Show progress bar                                                                       | `pdf2zh_next example.pdf --progress`                                                                                  |
| `version`                       | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `help`                          | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| 選項                          | 功能                                                                               | 範例                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | 要處理的輸入 PDF 文件                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `output-folder`                 | 翻譯文件的輸出資料夾                                                      | `pdf2zh_next example.pdf --output-folder /path/to/output`                                                              |
| `output-filename`               | 輸出文件名（不包含副檔名）                                                     | `pdf2zh_next example.pdf --output-filename my_translated_file`                                                         |
| `output-format`                 | 輸出文件格式（markdown、docx、pdf、tex）                                          | `pdf2zh_next example.pdf --output-format markdown pdf`                                                                 |
| `language-pair`                 | 語言對（例如：en-zh）                                                             | `pdf2zh_next example.pdf --language-pair en-zh`                                                                       |
| `translation-service`           | 翻譯服務（openai、azure、aliyun、siliconflow、gemini、deepseek）              | `pdf2zh_next example.pdf --translation-service openai`                                                                |
| `model`                         | 翻譯服務的模型名稱                                                  | `pdf2zh_next example.pdf --model gpt-4o`                                                                              |
| `api-key`                       | 翻譯服務的 API 金鑰                                                     | `pdf2zh_next example.pdf --api-key sk-xxx`                                                                            |
| `api-base`                      | 自定義 API 基礎 URL                                                                     | `pdf2zh_next example.pdf --api-base https://api.openai.com/v1`                                                        |
| `concurrency`                   | 並發翻譯請求的數量（預設：4）                                  | `pdf2zh_next example.pdf --concurrency 10`                                                                            |
| `max-requests-per-minute`       | 每分鐘最大請求數（預設：因服務而異）                                | `pdf2zh_next example.pdf --max-requests-per-minute 100`                                                               |
| `batch-size`                    | 每個批次處理的頁數（預設：10）                                  | `pdf2zh_next example.pdf --batch-size 20`                                                                             |
| `math-mode`                     | 數學翻譯模式（formula、hybrid、text）                                           | `pdf2zh_next example.pdf --math-mode formula`                                                                         |
| `formula-detection-method`      | 公式檢測方法（ml、rule）                                                     | `pdf2zh_next example.pdf --formula-detection-method ml`                                                               |
| `formula-translation-method`    | 公式翻譯方法（native、hybrid）                                             | `pdf2zh_next example.pdf --formula-translation-method hybrid`                                                          |
| `keep-formula`                  | 在翻譯中保留原始公式文本                                               | `pdf2zh_next example.pdf --keep-formula`                                                                              |
| `glossary`                      | 翻譯的術語表文件                                                           | `pdf2zh_next example.pdf --glossary my_glossary.txt`                                                                  |
| `glossary-strategy`             | 術語表匹配策略（fuzzy、exact）                                               | `pdf2zh_next example.pdf --glossary-strategy fuzzy`                                                                   |
| `context-window`                | 翻譯的上下文窗口大小                                                     | `pdf2zh_next example.pdf --context-window 5`                                                                          |
| `context-method`                | 上下文方法（none、previous、all）                                                    | `pdf2zh_next example.pdf --context-method previous`                                                                   |
| `no-table`                      | 跳過表格翻譯                                                                  | `pdf2zh_next example.pdf --no-table`                                                                                  |
| `table-translation-method`      | 表格翻譯方法（markdown、text）                                               | `pdf2zh_next example.pdf --table-translation-method markdown`                                                         |
| `no-text-split`                 | 禁用文本分割                                                                  | `pdf2zh_next example.pdf --no-text-split`                                                                             |
| `split-method`                  | 文本分割方法（sentence、paragraph、page）                                           | `pdf2zh_next example.pdf --split-method sentence`                                                                     |
| `split-length`                  | 文本分割的最大長度                                                       | `pdf2zh_next example.pdf --split-length 1000`                                                                         |
| `split-overlap`                 | 文本分割的重疊長度                                                       | `pdf2zh_next example.pdf --split-overlap 50`                                                                          |
| `no-cache`                      | 禁用翻譯快取                                                               | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `cache-dir`                     | 快取目錄                                                                         | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `cache-version`                 | 快取版本（用於快取失效）                                                  | `pdf2zh_next example.pdf --cache-version 2`                                                                           |
| `resume`                        | 從上次中斷處恢復                                                           | `pdf2zh_next example.pdf --resume`                                                                                    |
| `config`                        | 設定檔                                                                      | `pdf2zh_next example.pdf --config config.yaml`                                                                        |
| `log-level`                     | 日誌級別（debug、info、warning、error）                                                 | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `progress`                      | 顯示進度條                                                                       | `pdf2zh_next example.pdf --progress`                                                                                  |
| `version`                       | 顯示版本資訊                                                                | `pdf2zh_next --version`                                                                                               |
| `help`                          | 顯示幫助訊息                                                                       | `pdf2zh_next --help`                                                                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `-o`                            | Alias of `--output`                                                                     | `pdf2zh_next example.pdf -o /outputpath`                                                                              |
| `--output-name`                 | Output filename (without extension)                                                     | `pdf2zh_next example.pdf --output-name example-translated`                                                            |
| `--output-format`               | Output format, supports `pdf`, `docx`, `doc`, `txt`, `json`                             | `pdf2zh_next example.pdf --output-format docx`                                                                        |
| `--output-language`             | Output language code, default is `zh`, support for `zh`, `en`, `ja`, `ko`, `de`, `fr`   | `pdf2zh_next example.pdf --output-language en`                                                                        |
| `--output-layout`               | Output layout, supports `single-column`, `two-column`                                   | `pdf2zh_next example.pdf --output-layout two-column`                                                                  |
| `--output-image-ocr`            | Whether to perform OCR on images in the output file, default is `false`                 | `pdf2zh_next example.pdf --output-image-ocr true`                                                                     |
| `--output-image-ocr-language`   | Language code for image OCR, default is `zh`, support for `zh`, `en`, `ja`, `ko`, `de`, `fr` | `pdf2zh_next example.pdf --output-image-ocr-language en`                                                              |
| `--output-image-ocr-whisper`    | Whether to use Whisper for image OCR, default is `false`                                | `pdf2zh_next example.pdf --output-image-ocr-whisper true`                                                             |
| `--output-image-ocr-whisper-model` | Whisper model for image OCR, default is `base`                                          | `pdf2zh_next example.pdf --output-image-ocr-whisper-model large`                                                      |
| `--output-image-ocr-whisper-language` | Language code for Whisper image OCR, default is `zh`, support for `zh`, `en`, `ja`, `ko`, `de`, `fr` | `pdf2zh_next example.pdf --output-image-ocr-whisper-language en`                                                      |
| `--output-image-ocr-whisper-prompt` | Prompt for Whisper image OCR, default is `""`                                           | `pdf2zh_next example.pdf --output-image-ocr-whisper-prompt "Translate the following text to English"`                 |

---

### OUTPUT

| `--output`                      | 輸出檔案目錄                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| :------------------------------ | :------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `-o`                            | `--output` 的別名                                                         | `pdf2zh_next example.pdf -o /outputpath`                                                                              |
| `--output-name`                 | 輸出檔案名稱（不含副檔名）                                                | `pdf2zh_next example.pdf --output-name example-translated`                                                            |
| `--output-format`               | 輸出格式，支援 `pdf`、`docx`、`doc`、`txt`、`json`                        | `pdf2zh_next example.pdf --output-format docx`                                                                        |
| `--output-language`             | 輸出語言代碼，預設為 `zh`，支援 `zh`、`en`、`ja`、`ko`、`de`、`fr`        | `pdf2zh_next example.pdf --output-language en`                                                                        |
| `--output-layout`               | 輸出佈局，支援 `single-column`、`two-column`                              | `pdf2zh_next example.pdf --output-layout two-column`                                                                  |
| `--output-image-ocr`            | 是否對輸出檔案中的圖像執行 OCR，預設為 `false`                            | `pdf2zh_next example.pdf --output-image-ocr true`                                                                     |
| `--output-image-ocr-language`   | 圖像 OCR 的語言代碼，預設為 `zh`，支援 `zh`、`en`、`ja`、`ko`、`de`、`fr` | `pdf2zh_next example.pdf --output-image-ocr-language en`                                                              |
| `--output-image-ocr-whisper`    | 是否使用 Whisper 進行圖像 OCR，預設為 `false`                             | `pdf2zh_next example.pdf --output-image-ocr-whisper true`                                                             |
| `--output-image-ocr-whisper-model` | 圖像 OCR 的 Whisper 模型，預設為 `base`                                   | `pdf2zh_next example.pdf --output-image-ocr-whisper-model large`                                                      |
| `--output-image-ocr-whisper-language` | Whisper 圖像 OCR 的語言代碼，預設為 `zh`，支援 `zh`、`en`、`ja`、`ko`、`de`、`fr` | `pdf2zh_next example.pdf --output-image-ocr-whisper-language en`                                                      |
| `--output-image-ocr-whisper-prompt` | Whisper 圖像 OCR 的提示詞，預設為 `""`                                    | `pdf2zh_next example.pdf --output-image-ocr-whisper-prompt "Translate the following text to English"`                 |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-l`, `--language`              | Set the [**target language**](./Supported-Languages.md)                                | `pdf2zh_next example.pdf -l zh_TW`<br>`pdf2zh_next example.pdf --language zh_TW`                                      |
| `-o`, `--output`                | Set the **output path** of the translated file                                         | `pdf2zh_next example.pdf -o example_translated.pdf`<br>`pdf2zh_next example.pdf --output example_translated.pdf`       |
| `-p`, `--proxy`                 | Set the **proxy** for the translation service                                          | `pdf2zh_next example.pdf -p http://127.0.0.1:7890`<br>`pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`         |
| `-t`, `--template`              | Set the **template** for the translated document                                       | `pdf2zh_next example.pdf -t academic`<br>`pdf2zh_next example.pdf --template academic`                                |
| `-k`, `--key`                   | Set the **API key** for the translation service                                        | `pdf2zh_next example.pdf -k sk-xxxx`<br>`pdf2zh_next example.pdf --key sk-xxxx`                                       |
| `-v`, `--version`               | Show the **version** of pdf2zh                                                         | `pdf2zh_next -v`<br>`pdf2zh_next --version`                                                                           |
| `-h`, `--help`                  | Show the **help** message                                                              | `pdf2zh_next -h`<br>`pdf2zh_next --help`                                                                              |

---

### TRANSLATION RESULT

| `--<服務>`                  | 使用 [**特定服務**](./Documentation-of-Translation-Services.md) 進行翻譯 | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| -------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-l`, `--language`         | 設定 [**目標語言**](./Supported-Languages.md)                           | `pdf2zh_next example.pdf -l zh_TW`<br>`pdf2zh_next example.pdf --language zh_TW`                                      |
| `-o`, `--output`           | 設定翻譯檔案的**輸出路徑**                                             | `pdf2zh_next example.pdf -o example_translated.pdf`<br>`pdf2zh_next example.pdf --output example_translated.pdf`       |
| `-p`, `--proxy`            | 為翻譯服務設定**代理**                                                 | `pdf2zh_next example.pdf -p http://127.0.0.1:7890`<br>`pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`         |
| `-t`, `--template`         | 設定翻譯文件的**模板**                                                 | `pdf2zh_next example.pdf -t academic`<br>`pdf2zh_next example.pdf --template academic`                                |
| `-k`, `--key`              | 設定翻譯服務的 **API 金鑰**                                            | `pdf2zh_next example.pdf -k sk-xxxx`<br>`pdf2zh_next example.pdf --key sk-xxxx`                                       |
| `-v`, `--version`          | 顯示 pdf2zh 的**版本**                                                 | `pdf2zh_next -v`<br>`pdf2zh_next --version`                                                                           |
| `-h`, `--help`             | 顯示**幫助**訊息                                                       | `pdf2zh_next -h`<br>`pdf2zh_next --help`                                                                              |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--version`, `-v`               | Show version and exit                                                                    | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | Input file path or directory path.                                                       | `pdf2zh_next -i input.pdf`                                                                                            |
| `--output`, `-o`                | Output file path or directory path.                                                      | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `--lang`, `-l`                  | Target language code. Default: `zh`                                                      | `pdf2zh_next -i input.pdf -l ja`                                                                                      |
| `--config`, `-c`                | Configuration file path.                                                                 | `pdf2zh_next -i input.pdf -c config.json`                                                                             |
| `--service`                     | Translation service. Default: `openai`                                                   | `pdf2zh_next -i input.pdf --service aliyun`                                                                           |
| `--model`                       | Model name. Default: `gpt-3.5-turbo`                                                     | `pdf2zh_next -i input.pdf --model gpt-4`                                                                              |
| `--key`                         | API key for translation service.                                                         | `pdf2zh_next -i input.pdf --key sk-xxx`                                                                               |
| `--url`                         | API endpoint for translation service.                                                    | `pdf2zh_next -i input.pdf --url https://api.openai.com/v1/chat/completions`                                           |
| `--timeout`                     | Timeout for API requests in seconds. Default: `60`                                       | `pdf2zh_next -i input.pdf --timeout 120`                                                                              |
| `--retry`                       | Number of retries for API requests. Default: `3`                                         | `pdf2zh_next -i input.pdf --retry 5`                                                                                  |
| `--concurrency`                 | Number of concurrent requests. Default: `5`                                              | `pdf2zh_next -i input.pdf --concurrency 10`                                                                           |
| `--batch-size`                  | Number of texts to translate in a single request. Default: `10`                          | `pdf2zh_next -i input.pdf --batch-size 20`                                                                            |
| `--max-tokens`                  | Maximum number of tokens in a single request. Default: `4096`                            | `pdf2zh_next -i input.pdf --max-tokens 8192`                                                                          |
| `--temperature`                 | Temperature for text generation. Default: `0.1`                                          | `pdf2zh_next -i input.pdf --temperature 0.5`                                                                          |
| `--top-p`                       | Top-p for text generation. Default: `1.0`                                                | `pdf2zh_next -i input.pdf --top-p 0.9`                                                                                |
| `--presence-penalty`            | Presence penalty for text generation. Default: `0.0`                                     | `pdf2zh_next -i input.pdf --presence-penalty 0.1`                                                                     |
| `--frequency-penalty`           | Frequency penalty for text generation. Default: `0.0`                                    | `pdf2zh_next -i input.pdf --frequency-penalty 0.1`                                                                    |
| `--system-prompt`               | System prompt for translation.                                                           | `pdf2zh_next -i input.pdf --system-prompt "You are a helpful assistant."`                                              |
| `--user-prompt`                 | User prompt for translation.                                                             | `pdf2zh_next -i input.pdf --user-prompt "Translate the following text to {lang}:"`                                     |
| `--no-cache`                    | Disable cache.                                                                           | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir`                   | Cache directory path. Default: `./cache`                                                 | `pdf2zh_next -i input.pdf --cache-dir ./my_cache`                                                                     |
| `--log-level`                   | Log level. Default: `INFO`                                                               | `pdf2zh_next -i input.pdf --log-level DEBUG`                                                                          |
| `--log-file`                    | Log file path.                                                                           | `pdf2zh_next -i input.pdf --log-file ./log.txt`                                                                       |
| `--quiet`, `-q`                 | Disable all output.                                                                      | `pdf2zh_next -i input.pdf -q`                                                                                         |
| `--force`, `-f`                 | Force overwrite output file.                                                             | `pdf2zh_next -i input.pdf -o output.pdf -f`                                                                           |
| `--dry-run`                     | Dry run without actual translation.                                                      | `pdf2zh_next -i input.pdf --dry-run`                                                                                  |
| `--list-services`               | List available translation services.                                                     | `pdf2zh_next --list-services`                                                                                         |
| `--list-models`                 | List available models for a service.                                                     | `pdf2zh_next --list-models --service openai`                                                                          |
| `--list-languages`              | List supported languages.                                                                | `pdf2zh_next --list-languages`                                                                                        |
| `--check-update`                | Check for updates.                                                                       | `pdf2zh_next --check-update`                                                                                          |
| `--update`                      | Update to the latest version.                                                            | `pdf2zh_next --update`                                                                                                |
| `--uninstall`                   | Uninstall pdf2zh.                                                                        | `pdf2zh_next --uninstall`                                                                                             |

---

### OUTPUT

| `--help`, `-h`                  | 顯示幫助訊息並退出                                                              | `pdf2zh_next -h`                                                                                                      |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--version`, `-v`               | 顯示版本並退出                                                                    | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | 輸入檔案路徑或目錄路徑。                                                       | `pdf2zh_next -i input.pdf`                                                                                            |
| `--output`, `-o`                | 輸出檔案路徑或目錄路徑。                                                      | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `--lang`, `-l`                  | 目標語言代碼。預設：`zh`                                                      | `pdf2zh_next -i input.pdf -l ja`                                                                                      |
| `--config`, `-c`                | 配置檔案路徑。                                                                 | `pdf2zh_next -i input.pdf -c config.json`                                                                             |
| `--service`                     | 翻譯服務。預設：`openai`                                                   | `pdf2zh_next -i input.pdf --service aliyun`                                                                           |
| `--model`                       | 模型名稱。預設：`gpt-3.5-turbo`                                                     | `pdf2zh_next -i input.pdf --model gpt-4`                                                                              |
| `--key`                         | 翻譯服務的 API 金鑰。                                                         | `pdf2zh_next -i input.pdf --key sk-xxx`                                                                               |
| `--url`                         | 翻譯服務的 API 端點。                                                    | `pdf2zh_next -i input.pdf --url https://api.openai.com/v1/chat/completions`                                           |
| `--timeout`                     | API 請求的超時時間（秒）。預設：`60`                                       | `pdf2zh_next -i input.pdf --timeout 120`                                                                              |
| `--retry`                       | API 請求的重試次數。預設：`3`                                         | `pdf2zh_next -i input.pdf --retry 5`                                                                                  |
| `--concurrency`                 | 並發請求數量。預設：`5`                                              | `pdf2zh_next -i input.pdf --concurrency 10`                                                                           |
| `--batch-size`                  | 單次請求中翻譯的文字數量。預設：`10`                          | `pdf2zh_next -i input.pdf --batch-size 20`                                                                            |
| `--max-tokens`                  | 單次請求中的最大 token 數量。預設：`4096`                            | `pdf2zh_next -i input.pdf --max-tokens 8192`                                                                          |
| `--temperature`                 | 文字生成的溫度。預設：`0.1`                                          | `pdf2zh_next -i input.pdf --temperature 0.5`                                                                          |
| `--top-p`                       | 文字生成的 Top-p。預設：`1.0`                                                | `pdf2zh_next -i input.pdf --top-p 0.9`                                                                                |
| `--presence-penalty`            | 文字生成的存在懲罰。預設：`0.0`                                     | `pdf2zh_next -i input.pdf --presence-penalty 0.1`                                                                     |
| `--frequency-penalty`           | 文字生成的頻率懲罰。預設：`0.0`                                    | `pdf2zh_next -i input.pdf --frequency-penalty 0.1`                                                                    |
| `--system-prompt`               | 翻譯的系統提示。                                                           | `pdf2zh_next -i input.pdf --system-prompt "You are a helpful assistant."`                                              |
| `--user-prompt`                 | 翻譯的使用者提示。                                                             | `pdf2zh_next -i input.pdf --user-prompt "Translate the following text to {lang}:"`                                     |
| `--no-cache`                    | 停用快取。                                                                           | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir`                   | 快取目錄路徑。預設：`./cache`                                                 | `pdf2zh_next -i input.pdf --cache-dir ./my_cache`                                                                     |
| `--log-level`                   | 日誌級別。預設：`INFO`                                                               | `pdf2zh_next -i input.pdf --log-level DEBUG`                                                                          |
| `--log-file`                    | 日誌檔案路徑。                                                                           | `pdf2zh_next -i input.pdf --log-file ./log.txt`                                                                       |
| `--quiet`, `-q`                 | 停用所有輸出。                                                                      | `pdf2zh_next -i input.pdf -q`                                                                                         |
| `--force`, `-f`                 | 強制覆寫輸出檔案。                                                             | `pdf2zh_next -i input.pdf -o output.pdf -f`                                                                           |
| `--dry-run`                     | 模擬執行，不進行實際翻譯。                                                      | `pdf2zh_next -i input.pdf --dry-run`                                                                                  |
| `--list-services`               | 列出可用的翻譯服務。                                                     | `pdf2zh_next --list-services`                                                                                         |
| `--list-models`                 | 列出某個服務的可用模型。                                                     | `pdf2zh_next --list-models --service openai`                                                                          |
| `--list-languages`              | 列出支持的語言。                                                                | `pdf2zh_next --list-languages`                                                                                        |
| `--check-update`                | 檢查更新。                                                                       | `pdf2zh_next --check-update`                                                                                          |
| `--update`                      | 更新至最新版本。                                                            | `pdf2zh_next --update`                                                                                                |
| `--uninstall`                   | 解除安裝 pdf2zh。                                                                        | `pdf2zh_next --uninstall`                                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`, `-o`            | The directory where the output files will be saved                                     | `pdf2zh_next --output-dir /path/to/output` <br> `pdf2zh_next -o /path/to/output`                                       |
| `--model`                       | Specifies the model to use for translation                                              | `pdf2zh_next --model "gpt-4o-mini"`                                                                                    |
| `--translator`                  | Specifies the translation service to use                                                | `pdf2zh_next --translator "openai"`                                                                                    |
| `--source-lang`                 | Source language of the PDF file                                                         | `pdf2zh_next --source-lang "en"`                                                                                       |
| `--target-lang`                 | Target language for translation                                                         | `pdf2zh_next --target-lang "zh"`                                                                                       |
| `--api-key`                     | Your API key for the translation service                                                | `pdf2zh_next --api-key "your-api-key-here"`                                                                            |
| `--api-base`                    | The base URL for the API (if using a custom endpoint)                                   | `pdf2zh_next --api-base "https://your-custom-endpoint.com"`                                                            |
| `--batch-size`                  | Number of pages to process in a single batch (default: 10)                              | `pdf2zh_next --batch-size 5`                                                                                           |
| `--concurrent-requests`         | Number of concurrent requests to the translation service (default: 5)                   | `pdf2zh_next --concurrent-requests 10`                                                                                 |
| `--timeout`                     | Timeout in seconds for each translation request (default: 60)                          | `pdf2zh_next --timeout 120`                                                                                            |
| `--max-retries`                 | Maximum number of retries for failed requests (default: 3)                              | `pdf2zh_next --max-retries 5`                                                                                          |
| `--retry-delay`                 | Delay in seconds between retries (default: 1)                                          | `pdf2zh_next --retry-delay 2`                                                                                          |
| `--proxy`                       | Proxy server to use for requests                                                        | `pdf2zh_next --proxy "http://proxy-server.com:8080"`                                                                   |
| `--no-cache`                    | Disable caching of translation results                                                 | `pdf2zh_next --no-cache`                                                                                               |
| `--cache-dir`                   | Directory to store cache files (default: system cache directory)                        | `pdf2zh_next --cache-dir /path/to/cache`                                                                               |
| `--log-level`                   | Log level (debug, info, warning, error, critical) (default: info)                       | `pdf2zh_next --log-level debug`                                                                                        |
| `--log-file`                    | File to write logs to (default: stdout)                                               | `pdf2zh_next --log-file /path/to/logfile.log`                                                                          |
| `--help`, `-h`                  | Show help message and exit                                                             | `pdf2zh_next --help` <br> `pdf2zh_next -h`                                                                             |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next --version` <br> `pdf2zh_next -v`                                                                          |

---

### OUTPUT

| `--config-file`                 | 設定文件的路徑                                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`, `-o`            | 輸出文件保存的目錄                                                                      | `pdf2zh_next --output-dir /path/to/output` <br> `pdf2zh_next -o /path/to/output`                                       |
| `--model`                       | 指定用於翻譯的模型                                                                      | `pdf2zh_next --model "gpt-4o-mini"`                                                                                    |
| `--translator`                  | 指定使用的翻譯服務                                                                      | `pdf2zh_next --translator "openai"`                                                                                    |
| `--source-lang`                 | PDF 文件的源語言                                                                        | `pdf2zh_next --source-lang "en"`                                                                                       |
| `--target-lang`                 | 翻譯的目標語言                                                                          | `pdf2zh_next --target-lang "zh"`                                                                                       |
| `--api-key`                     | 翻譯服務的 API 金鑰                                                                     | `pdf2zh_next --api-key "your-api-key-here"`                                                                            |
| `--api-base`                    | API 的基礎 URL（如果使用自定義端點）                                                     | `pdf2zh_next --api-base "https://your-custom-endpoint.com"`                                                            |
| `--batch-size`                  | 單一批次處理的頁數（默認：10）                                                           | `pdf2zh_next --batch-size 5`                                                                                           |
| `--concurrent-requests`         | 向翻譯服務發送的並發請求數（默認：5）                                                    | `pdf2zh_next --concurrent-requests 10`                                                                                 |
| `--timeout`                     | 每個翻譯請求的超時時間（秒）（默認：60）                                                 | `pdf2zh_next --timeout 120`                                                                                            |
| `--max-retries`                 | 失敗請求的最大重試次數（默認：3）                                                        | `pdf2zh_next --max-retries 5`                                                                                          |
| `--retry-delay`                 | 重試之間的延遲時間（秒）（默認：1）                                                      | `pdf2zh_next --retry-delay 2`                                                                                          |
| `--proxy`                       | 用於請求的代理服務器                                                                    | `pdf2zh_next --proxy "http://proxy-server.com:8080"`                                                                   |
| `--no-cache`                    | 禁用翻譯結果的緩存                                                                      | `pdf2zh_next --no-cache`                                                                                               |
| `--cache-dir`                   | 存儲緩存文件的目錄（默認：系統緩存目錄）                                                 | `pdf2zh_next --cache-dir /path/to/cache`                                                                               |
| `--log-level`                   | 日誌級別（debug、info、warning、error、critical）（默認：info）                          | `pdf2zh_next --log-level debug`                                                                                        |
| `--log-file`                    | 寫入日誌的文件（默認：stdout）                                                          | `pdf2zh_next --log-file /path/to/logfile.log`                                                                          |
| `--help`, `-h`                  | 顯示幫助信息並退出                                                                      | `pdf2zh_next --help` <br> `pdf2zh_next -h`                                                                             |
| `--version`, `-v`               | 顯示版本並退出                                                                          | `pdf2zh_next --version` <br> `pdf2zh_next -v`                                                                          |
`5`                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `--report-interval-0`           | Disable progress report                                                                 | `pdf2zh_next example.pdf --report-interval-0`                                                                         | `0`                                                              |
| `--retry-count`                 | Number of retries on failure                                                            | `pdf2zh_next example.pdf --retry-count 3`                                                                             | `3`                                                              |
| `--retry-interval`              | Interval between retries in seconds                                                      | `pdf2zh_next example.pdf --retry-interval 10`                                                                         | `10`                                                             |
| `--retry-interval-multiplier`   | Multiplier for retry interval (exponential backoff)                                     | `pdf2zh_next example.pdf --retry-interval-multiplier 2`                                                               | `2`                                                              |
| `--retry-interval-max`          | Maximum retry interval in seconds                                                        | `pdf2zh_next example.pdf --retry-interval-max 60`                                                                     | `60`                                                             |
| `--retry-interval-min`          | Minimum retry interval in seconds                                                        | `pdf2zh_next example.pdf --retry-interval-min 1`                                                                      | `1`                                                              |

---

### OUTPUT

| `--report-interval`             | 進度報告間隔（秒）                                                                         | `pdf2zh_next example.pdf --report-interval 5`                                                                         | `5`                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `--report-interval-0`           | 禁用進度報告                                                                               | `pdf2zh_next example.pdf --report-interval-0`                                                                         | `0`                                                              |
| `--retry-count`                 | 失敗重試次數                                                                               | `pdf2zh_next example.pdf --retry-count 3`                                                                             | `3`                                                              |
| `--retry-interval`              | 重試間隔（秒）                                                                             | `pdf2zh_next example.pdf --retry-interval 10`                                                                         | `10`                                                             |
| `--retry-interval-multiplier`   | 重試間隔倍數（指數退避）                                                                     | `pdf2zh_next example.pdf --retry-interval-multiplier 2`                                                               | `2`                                                              |
| `--retry-interval-max`          | 最大重試間隔（秒）                                                                         | `pdf2zh_next example.pdf --retry-interval-max 60`                                                                     | `60`                                                             |
| `--retry-interval-min`          | 最小重試間隔（秒）                                                                         | `pdf2zh_next example.pdf --retry-interval-min 1`                                                                      | `1`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-level`                   | Set logging level (`debug`, `info`, `warning`, `error`, `critical`)                     | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | Log to a file                                                                           | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--log-format`                  | Set log format (`text`, `json`)                                                         | `pdf2zh_next example.pdf --log-format json`                                                                           |
| `--log-rotate`                  | Enable log rotation                                                                     | `pdf2zh_next example.pdf --log-rotate`                                                                                |
| `--log-rotate-max-bytes`        | Maximum size of log file before rotation (default: `10485760`)                          | `pdf2zh_next example.pdf --log-rotate-max-bytes 20971520`                                                             |
| `--log-rotate-backup-count`     | Number of backup logs to keep (default: `5`)                                            | `pdf2zh_next example.pdf --log-rotate-backup-count 10`                                                                |
| `--log-rotate-compress`         | Compress rotated logs                                                                   | `pdf2zh_next example.pdf --log-rotate-compress`                                                                       |
| `--log-rotate-when`             | When to rotate logs (`S`, `M`, `H`, `D`, `midnight`, `W0`-`W6`) (default: `D`)          | `pdf2zh_next example.pdf --log-rotate-when H`                                                                         |
| `--log-rotate-interval`         | Interval for log rotation (default: `1`)                                                | `pdf2zh_next example.pdf --log-rotate-interval 2`                                                                     |
| `--log-rotate-at-time`          | Time to rotate logs (default: `00:00`)                                                  | `pdf2zh_next example.pdf --log-rotate-at-time 12:00`                                                                  |

---

### OUTPUT

| `--debug`                       | 使用除錯日誌等級                                                                        | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-level`                   | 設定日誌等級 (`debug`, `info`, `warning`, `error`, `critical`)                          | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | 將日誌輸出至檔案                                                                        | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--log-format`                  | 設定日誌格式 (`text`, `json`)                                                           | `pdf2zh_next example.pdf --log-format json`                                                                           |
| `--log-rotate`                  | 啟用日誌輪替                                                                            | `pdf2zh_next example.pdf --log-rotate`                                                                                |
| `--log-rotate-max-bytes`        | 日誌檔案輪替前的最大大小（預設：`10485760`）                                            | `pdf2zh_next example.pdf --log-rotate-max-bytes 20971520`                                                             |
| `--log-rotate-backup-count`     | 保留的備份日誌數量（預設：`5`）                                                         | `pdf2zh_next example.pdf --log-rotate-backup-count 10`                                                                |
| `--log-rotate-compress`         | 壓縮輪替後的日誌                                                                        | `pdf2zh_next example.pdf --log-rotate-compress`                                                                       |
| `--log-rotate-when`             | 日誌輪替時機 (`S`, `M`, `H`, `D`, `midnight`, `W0`-`W6`)（預設：`D`）                   | `pdf2zh_next example.pdf --log-rotate-when H`                                                                         |
| `--log-rotate-interval`         | 日誌輪替間隔（預設：`1`）                                                               | `pdf2zh_next example.pdf --log-rotate-interval 2`                                                                     |
| `--log-rotate-at-time`          | 日誌輪替時間（預設：`00:00`）                                                           | `pdf2zh_next example.pdf --log-rotate-at-time 12:00`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Show program's version number and exit                                                   | `pdf2zh_next --version`                                                                                               |
| `--config`                      | Show config file path and exit                                                          | `pdf2zh_next --config`                                                                                                |
| `--show-default-config`         | Show default config and exit                                                            | `pdf2zh_next --show-default-config`                                                                                   |
| `--input` or `-i`               | Input file or directory                                                                 | `pdf2zh_next --input ./paper.pdf`                                                                                     |
| `--output` or `-o`              | Output file or directory                                                                | `pdf2zh_next --output ./paper_zh.pdf`                                                                                 |
| `--source-lang`                 | Source language code (default: `auto`)                                                  | `pdf2zh_next --source-lang en`                                                                                        |
| `--target-lang`                 | Target language code (default: `zh-Hans`)                                              | `pdf2zh_next --target-lang zh-Hant`                                                                                   |
| `--translator`                  | Translator service (default: `openai`)<br>Available: `openai`, `aliyun`, `siliconflow` | `pdf2zh_next --translator aliyun`                                                                                     |
| `--translate-only`              | Only translate, do not process PDF                                                      | `pdf2zh_next --translate-only`                                                                                        |
| `--process-only`                | Only process PDF, do not translate                                                      | `pdf2zh_next --process-only`                                                                                          |
| `--force`                       | Force overwrite output file                                                             | `pdf2zh_next --force`                                                                                                 |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next --no-cache`                                                                                              |
| `--log-level`                   | Log level (default: `INFO`)<br>Available: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | `pdf2zh_next --log-level DEBUG`                                                                                       |
| `--log-file`                    | Log file path                                                                           | `pdf2zh_next --log-file ./log.txt`                                                                                    |
| `--proxy`                       | Proxy URL                                                                               | `pdf2zh_next --proxy http://127.0.0.1:7890`                                                                           |
| `--openai-api-key`              | OpenAI API key                                                                          | `pdf2zh_next --openai-api-key sk-...`                                                                                 |
| `--openai-base-url`             | OpenAI base URL                                                                         | `pdf2zh_next --openai-base-url https://api.example.com/v1`                                                            |
| `--openai-model`                | OpenAI model (default: `gpt-4o`)                                                        | `pdf2zh_next --openai-model gpt-4o-mini`                                                                              |
| `--aliyun-access-key-id`        | Aliyun access key ID                                                                    | `pdf2zh_next --aliyun-access-key-id ...`                                                                              |
| `--aliyun-access-key-secret`    | Aliyun access key secret                                                                | `pdf2zh_next --aliyun-access-key-secret ...`                                                                          |
| `--siliconflow-api-key`         | SiliconFlow API key                                                                     | `pdf2zh_next --siliconflow-api-key ...`                                                                               |
| `--siliconflow-base-url`        | SiliconFlow base URL (default: `https://api.siliconflow.cn/v1`)                         | `pdf2zh_next --siliconflow-base-url https://api.siliconflow.cn/v1`                                                    |
| `--siliconflow-model`           | SiliconFlow model (default: `DeepSeek/DeepSeek-V3`)                                     | `pdf2zh_next --siliconflow-model DeepSeek/DeepSeek-V3`                                                                |

---

### OUTPUT

| `--gui`                         | 與 GUI 互動                                                                             | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--help`                        | 顯示幫助訊息並退出                                                                      | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | 顯示程式版本號並退出                                                                    | `pdf2zh_next --version`                                                                                               |
| `--config`                      | 顯示設定檔路徑並退出                                                                    | `pdf2zh_next --config`                                                                                                |
| `--show-default-config`         | 顯示預設設定並退出                                                                      | `pdf2zh_next --show-default-config`                                                                                   |
| `--input` 或 `-i`               | 輸入檔案或目錄                                                                          | `pdf2zh_next --input ./paper.pdf`                                                                                     |
| `--output` 或 `-o`              | 輸出檔案或目錄                                                                          | `pdf2zh_next --output ./paper_zh.pdf`                                                                                 |
| `--source-lang`                 | 來源語言代碼 (預設：`auto`)                                                             | `pdf2zh_next --source-lang en`                                                                                        |
| `--target-lang`                 | 目標語言代碼 (預設：`zh-Hans`)                                                          | `pdf2zh_next --target-lang zh-Hant`                                                                                   |
| `--translator`                  | 翻譯服務 (預設：`openai`)<br>可用：`openai`, `aliyun`, `siliconflow`                  | `pdf2zh_next --translator aliyun`                                                                                     |
| `--translate-only`              | 僅翻譯，不處理 PDF                                                                      | `pdf2zh_next --translate-only`                                                                                        |
| `--process-only`                | 僅處理 PDF, 不翻譯                                                                      | `pdf2zh_next --process-only`                                                                                          |
| `--force`                       | 強制覆蓋輸出檔案                                                                        | `pdf2zh_next --force`                                                                                                 |
| `--no-cache`                    | 停用快取                                                                                | `pdf2zh_next --no-cache`                                                                                              |
| `--log-level`                   | 日誌等級 (預設：`INFO`)<br>可用：`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`      | `pdf2zh_next --log-level DEBUG`                                                                                       |
| `--log-file`                    | 日誌檔案路徑                                                                            | `pdf2zh_next --log-file ./log.txt`                                                                                    |
| `--proxy`                       | 代理 URL                                                                               | `pdf2zh_next --proxy http://127.0.0.1:7890`                                                                           |
| `--openai-api-key`              | OpenAI API 金鑰                                                                         | `pdf2zh_next --openai-api-key sk-...`                                                                                 |
| `--openai-base-url`             | OpenAI 基礎 URL                                                                         | `pdf2zh_next --openai-base-url https://api.example.com/v1`                                                            |
| `--openai-model`                | OpenAI 模型 (預設：`gpt-4o`)                                                            | `pdf2zh_next --openai-model gpt-4o-mini`                                                                              |
| `--aliyun-access-key-id`        | 阿里雲存取金鑰 ID                                                                       | `pdf2zh_next --aliyun-access-key-id ...`                                                                              |
| `--aliyun-access-key-secret`    | 阿里雲存取金鑰密碼                                                                      | `pdf2zh_next --aliyun-access-key-secret ...`                                                                          |
| `--siliconflow-api-key`         | SiliconFlow API 金鑰                                                                    | `pdf2zh_next --siliconflow-api-key ...`                                                                               |
| `--siliconflow-base-url`        | SiliconFlow 基礎 URL (預設：`https://api.siliconflow.cn/v1`)                            | `pdf2zh_next --siliconflow-base-url https://api.siliconflow.cn/v1`                                                    |
| `--siliconflow-model`           | SiliconFlow 模型 (預設：`DeepSeek/DeepSeek-V3`)                                          | `pdf2zh_next --siliconflow-model DeepSeek/DeepSeek-V3`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                   |
| `--cache-dir <dir>`             | Specify cache directory                                                                | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          |
| `--model-dir <dir>`             | Specify model directory                                                                 | `pdf2zh_next example.pdf --model-dir ./models`                                                                         |
| `--model <model>`               | Specify model to use                                                                    | `pdf2zh_next example.pdf --model siliconflow/DeepSeek-R1-Distill-Qwen-1.5B`                                           |
| `--model-type <type>`           | Specify model type                                                                      | `pdf2zh_next example.pdf --model-type siliconflow`                                                                     |
| `--model-revision <revision>`   | Specify model revision                                                                  | `pdf2zh_next example.pdf --model-revision main`                                                                        |
| `--model-trust-remote-code`     | Trust remote code when loading model                                                    | `pdf2zh_next example.pdf --model-trust-remote-code`                                                                    |
| `--model-tokenizer <tokenizer>` | Specify tokenizer to use                                                                | `pdf2zh_next example.pdf --model-tokenizer Qwen/Qwen2-7B-Instruct`                                                     |
| `--model-tokenizer-revision <revision>` | Specify tokenizer revision                                                              | `pdf2zh_next example.pdf --model-tokenizer-revision main`                                                              |
| `--model-tokenizer-trust-remote-code` | Trust remote code when loading tokenizer                                                | `pdf2zh_next example.pdf --model-tokenizer-trust-remote-code`                                                          |
| `--device <device>`             | Specify device to use                                                                   | `pdf2zh_next example.pdf --device cuda`                                                                                |
| `--device-id <id>`              | Specify device id to use                                                                | `pdf2zh_next example.pdf --device-id 0`                                                                                |
| `--dtype <dtype>`               | Specify dtype to use                                                                    | `pdf2zh_next example.pdf --dtype bfloat16`                                                                             |
| `--batch-size <size>`           | Specify batch size                                                                      | `pdf2zh_next example.pdf --batch-size 16`                                                                              |
| `--max-concurrent <number>`     | Specify max concurrent tasks                                                            | `pdf2zh_next example.pdf --max-concurrent 4`                                                                          |
| `--max-retry <number>`          | Specify max retry times                                                                 | `pdf2zh_next example.pdf --max-retry 3`                                                                                |
| `--timeout <seconds>`           | Specify timeout for each request                                                        | `pdf2zh_next example.pdf --timeout 30`                                                                                 |
| `--proxy <proxy>`               | Specify proxy to use                                                                    | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--api-key <key>`               | Specify API key                                                                         | `pdf2zh_next example.pdf --api-key sk-xxxxxx`                                                                          |
| `--api-base <url>`              | Specify API base URL                                                                    | `pdf2zh_next example.pdf --api-base https://api.siliconflow.cn/v1`                                                     |
| `--api-org <org>`               | Specify API organization                                                                | `pdf2zh_next example.pdf --api-org org-xxxxxx`                                                                         |
| `--api-project <project>`       | Specify API project                                                                     | `pdf2zh_next example.pdf --api-project proj-xxxxxx`                                                                    |
| `--api-model <model>`           | Specify API model                                                                       | `pdf2zh_next example.pdf --api-model DeepSeek-R1-Distill-Qwen-1.5B`                                                    |
| `--api-max-tokens <tokens>`     | Specify API max tokens                                                                  | `pdf2zh_next example.pdf --api-max-tokens 4096`                                                                        |
| `--api-temperature <temperature>` | Specify API temperature                                                                 | `pdf2zh_next example.pdf --api-temperature 0.1`                                                                       |
| `--api-top-p <top-p>`           | Specify API top p                                                                       | `pdf2zh_next example.pdf --api-top-p 0.9`                                                                              |
| `--api-frequency-penalty <penalty>` | Specify API frequency penalty                                                         | `pdf2zh_next example.pdf --api-frequency-penalty 0`                                                                   |
| `--api-presence-penalty <penalty>` | Specify API presence penalty                                                           | `pdf2zh_next example.pdf --api-presence-penalty 0`                                                                     |
| `--api-stop <stop>`             | Specify API stop sequences                                                              | `pdf2zh_next example.pdf --api-stop "<\|im_end\|>"`                                                                   |
| `--api-extra-args <json>`       | Specify extra API arguments                                                             | `pdf2zh_next example.pdf --api-extra-args '{"seed": 123}'`                                                             |
| `--translator <translator>`     | Specify translator to use                                                               | `pdf2zh_next example.pdf --translator aliyun`                                                                          |
| `--translator-args <json>`      | Specify extra translator arguments                                                      | `pdf2zh_next example.pdf --translator-args '{"key": "value"}'`                                                         |
| `--source-lang <lang>`          | Specify source language                                                                 | `pdf2zh_next example.pdf --source-lang en`                                                                             |
| `--target-lang <lang>`          | Specify target language                                                                 | `pdf2zh_next example.pdf --target-lang zh`                                                                             |
| `--format <format>`             | Specify output format                                                                   | `pdf2zh_next example.pdf --format markdown`                                                                            |
| `--output <file>`               | Specify output file                                                                     | `pdf2zh_next example.pdf --output example_translated.md`                                                               |
| `--output-dir <dir>`            | Specify output directory                                                                | `pdf2zh_next example.pdf --output-dir ./output`                                                                        |
| `--overwrite`                   | Overwrite output file if exists                                                         | `pdf2zh_next example.pdf --overwrite`                                                                                  |
| `--no-backup`                   | Disable backup                                                                          | `pdf2zh_next example.pdf --no-backup`                                                                                  |
| `--backup-dir <dir>`            | Specify backup directory                                                                | `pdf2zh_next example.pdf --backup-dir ./backup`                                                                        |
| `--backup-format <format>`      | Specify backup format                                                                   | `pdf2zh_next example.pdf --backup-format pdf`                                                                          |
| `--log-level <level>`           | Specify log level                                                                       | `pdf2zh_next example.pdf --log-level info`                                                                             |
| `--log-file <file>`             | Specify log file                                                                        | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                         |
| `--no-progress`                 | Disable progress bar                                                                    | `pdf2zh_next example.pdf --no-progress`                                                                                |
| `--yes`                         | Skip confirmation prompts                                                               | `pdf2zh_next example.pdf --yes`                                                                                        |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Show help and exit                                                                      | `pdf2zh_next --help`                                                                                                   |

---

### OUTPUT

| `--warmup`                      | 僅下載並驗證所需資源後退出                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-cache`                    | 禁用緩存                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                   |
| `--cache-dir <dir>`             | 指定緩存目錄                                                                | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          |
| `--model-dir <dir>`             | 指定模型目錄                                                                 | `pdf2zh_next example.pdf --model-dir ./models`                                                                          |
| `--model <model>`               | 指定使用的模型                                                                    | `pdf2zh_next example.pdf --model siliconflow/DeepSeek-R1-Distill-Qwen-1.5B`                                           |
| `--model-type <type>`           | 指定模型類型                                                                      | `pdf2zh_next example.pdf --model-type siliconflow`                                                                     |
| `--model-revision <revision>`   | 指定模型版本                                                                  | `pdf2zh_next example.pdf --model-revision main`                                                                        |
| `--model-trust-remote-code`     | 加載模型時信任遠端代碼                                                    | `pdf2zh_next example.pdf --model-trust-remote-code`                                                                    |
| `--model-tokenizer <tokenizer>` | 指定使用的分詞器                                                                | `pdf2zh_next example.pdf --model-tokenizer Qwen/Qwen2-7B-Instruct`                                                     |
| `--model-tokenizer-revision <revision>` | 指定分詞器版本                                                              | `pdf2zh_next example.pdf --model-tokenizer-revision main`                                                              |
| `--model-tokenizer-trust-remote-code` | 加載分詞器時信任遠端代碼                                                | `pdf2zh_next example.pdf --model-tokenizer-trust-remote-code`                                                          |
| `--device <device>`             | 指定使用的設備                                                                   | `pdf2zh_next example.pdf --device cuda`                                                                                |
| `--device-id <id>`              | 指定使用的設備 ID                                                                | `pdf2zh_next example.pdf --device-id 0`                                                                                |
| `--dtype <dtype>`               | 指定使用的數據類型                                                                    | `pdf2zh_next example.pdf --dtype bfloat16`                                                                             |
| `--batch-size <size>`           | 指定批次大小                                                                      | `pdf2zh_next example.pdf --batch-size 16`                                                                              |
| `--max-concurrent <number>`     | 指定最大併發任務數                                                            | `pdf2zh_next example.pdf --max-concurrent 4`                                                                          |
| `--max-retry <number>`          | 指定最大重試次數                                                                 | `pdf2zh_next example.pdf --max-retry 3`                                                                                |
| `--timeout <seconds>`           | 指定每個請求的超時時間                                                        | `pdf2zh_next example.pdf --timeout 30`                                                                                 |
| `--proxy <proxy>`               | 指定使用的代理                                                                    | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--api-key <key>`               | 指定 API 金鑰                                                                         | `pdf2zh_next example.pdf --api-key sk-xxxxxx`                                                                          |
| `--api-base <url>`              | 指定 API 基礎 URL                                                                    | `pdf2zh_next example.pdf --api-base https://api.siliconflow.cn/v1`                                                     |
| `--api-org <org>`               | 指定 API 組織                                                                | `pdf2zh_next example.pdf --api-org org-xxxxxx`                                                                         |
| `--api-project <project>`       | 指定 API 專案                                                                     | `pdf2zh_next example.pdf --api-project proj-xxxxxx`                                                                    |
| `--api-model <model>`           | 指定 API 模型                                                                       | `pdf2zh_next example.pdf --api-model DeepSeek-R1-Distill-Qwen-1.5B`                                                    |
| `--api-max-tokens <tokens>`     | 指定 API 最大令牌數                                                                  | `pdf2zh_next example.pdf --api-max-tokens 4096`                                                                        |
| `--api-temperature <temperature>` | 指定 API 溫度                                                                 | `pdf2zh_next example.pdf --api-temperature 0.1`                                                                       |
| `--api-top-p <top-p>`           | 指定 API top p 值                                                                       | `pdf2zh_next example.pdf --api-top-p 0.9`                                                                              |
| `--api-frequency-penalty <penalty>` | 指定 API 頻率懲罰                                                         | `pdf2zh_next example.pdf --api-frequency-penalty 0`                                                                   |
| `--api-presence-penalty <penalty>` | 指定 API 存在懲罰                                                           | `pdf2zh_next example.pdf --api-presence-penalty 0`                                                                     |
| `--api-stop <stop>`             | 指定 API 停止序列                                                              | `pdf2zh_next example.pdf --api-stop "<\|im_end\|>"`                                                                   |
| `--api-extra-args <json>`       | 指定額外的 API 參數                                                             | `pdf2zh_next example.pdf --api-extra-args '{"seed": 123}'`                                                             |
| `--translator <translator>`     | 指定使用的翻譯器                                                               | `pdf2zh_next example.pdf --translator aliyun`                                                                          |
| `--translator-args <json>`      | 指定額外的翻譯器參數                                                      | `pdf2zh_next example.pdf --translator-args '{"key": "value"}'`                                                         |
| `--source-lang <lang>`          | 指定源語言                                                                 | `pdf2zh_next example.pdf --source-lang en`                                                                             |
| `--target-lang <lang>`          | 指定目標語言                                                                 | `pdf2zh_next example.pdf --target-lang zh`                                                                             |
| `--format <format>`             | 指定輸出格式                                                                   | `pdf2zh_next example.pdf --format markdown`                                                                            |
| `--output <file>`               | 指定輸出檔案                                                                     | `pdf2zh_next example.pdf --output example_translated.md`                                                               |
| `--output-dir <dir>`            | 指定輸出目錄                                                                | `pdf2zh_next example.pdf --output-dir ./output`                                                                        |
| `--overwrite`                   | 如果輸出檔案存在則覆寫                                                         | `pdf2zh_next example.pdf --overwrite`                                                                                  |
| `--no-backup`                   | 禁用備份                                                                          | `pdf2zh_next example.pdf --no-backup`                                                                                  |
| `--backup-dir <dir>`            | 指定備份目錄                                                                | `pdf2zh_next example.pdf --backup-dir ./backup`                                                                        |
| `--backup-format <format>`      | 指定備份格式                                                                   | `pdf2zh_next example.pdf --backup-format pdf`                                                                          |
| `--log-level <level>`           | 指定日誌等級                                                                       | `pdf2zh_next example.pdf --log-level info`                                                                             |
| `--log-file <file>`             | 指定日誌檔案                                                                        | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                         |
| `--no-progress`                 | 禁用進度條                                                                    | `pdf2zh_next example.pdf --no-progress`                                                                                |
| `--yes`                         | 跳過確認提示                                                               | `pdf2zh_next example.pdf --yes`                                                                                        |
| `--version`                     | 顯示版本並退出                                                                   | `pdf2zh_next --version`                                                                                                |
| `--help`                        | 顯示幫助並退出                                                                      | `pdf2zh_next --help`                                                                                                   |
| :------------------------------ | :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-path`         | Use the offline assets package from the specified directory                              | `pdf2zh_next example.pdf --offline-assets-path /path`                                                                 |
| `--offline-assets-version`      | The version of the offline assets package, default is `latest`                           | `pdf2zh_next example.pdf --offline-assets-path /path --offline-assets-version 1.0.0`                                  |
| `--offline-assets-keep-zip`     | Keep the downloaded zip file of the offline assets package after extraction, default is `false` | `pdf2zh_next example.pdf --offline-assets-path /path --offline-assets-keep-zip true`                                  |

---

### OUTPUT

| `--generate-offline-assets`     | 在指定目錄中生成離線資源包                                                              | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| :------------------------------ | :--------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-path`         | 使用指定目錄中的離線資源包                                                              | `pdf2zh_next example.pdf --offline-assets-path /path`                                                                 |
| `--offline-assets-version`      | 離線資源包的版本，默認為 `latest`                                                       | `pdf2zh_next example.pdf --offline-assets-path /path --offline-assets-version 1.0.0`                                  |
| `--offline-assets-keep-zip`     | 在解壓後保留離線資源包的壓縮文件，默認為 `false`                                         | `pdf2zh_next example.pdf --offline-assets-path /path --offline-assets-keep-zip true`                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--restore-offline-assets-only` | Restore offline assets package from the specified directory without performing any task | `pdf2zh_next --restore-offline-assets-only /path`                                                                     |

---

### TRANSLATION RESULT

| `--restore-offline-assets`      | 從指定目錄恢復離線資源包                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--restore-offline-assets-only` | 僅從指定目錄恢復離線資源包，不執行任何任務 | `pdf2zh_next --restore-offline-assets-only /path`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--help`                        | Show this message and exit                                                              | `pdf2zh_next --help`                                                                                                  |
| `-i`, `--input`                 | Input file path                                                                         | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output`                | Output file path                                                                        | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-s`, `--service`               | Translation service, default to `google`                                                | `pdf2zh_next -i input.pdf -s google`                                                                                  |
| `--source-lang`, `--src-lang`   | Source language, default to `auto`                                                      | `pdf2zh_next -i input.pdf --src-lang en`                                                                              |
| `--target-lang`, `--tgt-lang`   | Target language, default to `zh-CN`                                                     | `pdf2zh_next -i input.pdf --tgt-lang zh-TW`                                                                           |
| `--api-key`                     | API key for translation service                                                         | `pdf2zh_next -i input.pdf -s openai --api-key sk-xxxx`                                                                |
| `--api-base`                    | API base URL for translation service, only for OpenAI compatible APIs                   | `pdf2zh_next -i input.pdf -s openai --api-base https://api.siliconflow.cn/v1`                                         |
| `--model`                       | Model name for translation service, only for OpenAI compatible APIs                     | `pdf2zh_next -i input.pdf -s openai --model gpt-3.5-turbo`                                                            |
| `--proxy`                       | Proxy URL, only for `google` and `deepl` services                                       | `pdf2zh_next -i input.pdf -s google --proxy http://127.0.0.1:1080`                                                    |
| `--concurrency`                 | Number of concurrent requests, default to 4                                             | `pdf2zh_next -i input.pdf --concurrency 8`                                                                            |
| `--batch-size`                  | Number of paragraphs per request, default to 10                                         | `pdf2zh_next -i input.pdf --batch-size 20`                                                                            |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir`                   | Cache directory, default to `.cache` in the current directory                           | `pdf2zh_next -i input.pdf --cache-dir /tmp/cache`                                                                     |
| `--log-level`                   | Log level, default to `INFO`                                                            | `pdf2zh_next -i input.pdf --log-level DEBUG`                                                                          |
| `--log-file`                    | Log file path                                                                           | `pdf2zh_next -i input.pdf --log-file log.txt`                                                                         |
| `--timeout`                     | Timeout for each request in seconds, default to 30                                      | `pdf2zh_next -i input.pdf --timeout 60`                                                                               |
| `--retry`                       | Number of retries for each request, default to 3                                        | `pdf2zh_next -i input.pdf --retry 5`                                                                                  |
| `--retry-delay`                 | Delay between retries in seconds, default to 1                                          | `pdf2zh_next -i input.pdf --retry-delay 2`                                                                            |
| `--max-requests`                | Maximum number of requests per minute, default to 60                                    | `pdf2zh_next -i input.pdf --max-requests 100`                                                                         |
| `--dry-run`                     | Dry run, only show the number of paragraphs to be translated                            | `pdf2zh_next -i input.pdf --dry-run`                                                                                  |
| `--force`                       | Force translation even if the output file already exists                                | `pdf2zh_next -i input.pdf --force`                                                                                    |
| `--no-backup`                   | Do not backup the original file                                                         | `pdf2zh_next -i input.pdf --no-backup`                                                                                |
| `--backup-dir`                  | Backup directory, default to `.backup` in the current directory                         | `pdf2zh_next -i input.pdf --backup-dir /tmp/backup`                                                                   |
| `--no-color`                    | Disable colored output                                                                  | `pdf2zh_next -i input.pdf --no-color`                                                                                 |
| `--config`                      | Path to config file                                                                     | `pdf2zh_next -i input.pdf --config config.toml`                                                                       |
| `--list-services`               | List available translation services                                                     | `pdf2zh_next --list-services`                                                                                         |
| `--list-languages`              | List supported languages for a translation service                                      | `pdf2zh_next --list-languages`                                                                                        |
| `--list-models`                 | List supported models for a translation service, only for OpenAI compatible APIs        | `pdf2zh_next --list-models`                                                                                           |
| `--list-formats`                | List supported input and output formats                                                 | `pdf2zh_next --list-formats`                                                                                          |

---

### TRANSLATED TEXT

| `--version`                     | 顯示版本後退出                                                                          | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--help`                        | 顯示此訊息並退出                                                                        | `pdf2zh_next --help`                                                                                                  |
| `-i`, `--input`                 | 輸入檔案路徑                                                                            | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output`                | 輸出檔案路徑                                                                            | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-s`, `--service`               | 翻譯服務，預設為 `google`                                                               | `pdf2zh_next -i input.pdf -s google`                                                                                  |
| `--source-lang`, `--src-lang`   | 來源語言，預設為 `auto`                                                                 | `pdf2zh_next -i input.pdf --src-lang en`                                                                              |
| `--target-lang`, `--tgt-lang`   | 目標語言，預設為 `zh-CN`                                                                | `pdf2zh_next -i input.pdf --tgt-lang zh-TW`                                                                           |
| `--api-key`                     | 翻譯服務的 API 金鑰                                                                     | `pdf2zh_next -i input.pdf -s openai --api-key sk-xxxx`                                                                |
| `--api-base`                    | 翻譯服務的 API 基礎 URL，僅適用於 OpenAI 相容的 API                                     | `pdf2zh_next -i input.pdf -s openai --api-base https://api.siliconflow.cn/v1`                                         |
| `--model`                       | 翻譯服務的模型名稱，僅適用於 OpenAI 相容的 API                                          | `pdf2zh_next -i input.pdf -s openai --model gpt-3.5-turbo`                                                            |
| `--proxy`                       | 代理 URL，僅適用於 `google` 和 `deepl` 服務                                             | `pdf2zh_next -i input.pdf -s google --proxy http://127.0.0.1:1080`                                                    |
| `--concurrency`                 | 併發請求數量，預設為 4                                                                  | `pdf2zh_next -i input.pdf --concurrency 8`                                                                            |
| `--batch-size`                  | 每個請求的段落數量，預設為 10                                                           | `pdf2zh_next -i input.pdf --batch-size 20`                                                                            |
| `--no-cache`                    | 停用快取                                                                                | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir`                   | 快取目錄，預設為當前目錄中的 `.cache`                                                   | `pdf2zh_next -i input.pdf --cache-dir /tmp/cache`                                                                     |
| `--log-level`                   | 日誌級別，預設為 `INFO`                                                                 | `pdf2zh_next -i input.pdf --log-level DEBUG`                                                                          |
| `--log-file`                    | 日誌檔案路徑                                                                            | `pdf2zh_next -i input.pdf --log-file log.txt`                                                                         |
| `--timeout`                     | 每個請求的超時時間（秒），預設為 30                                                     | `pdf2zh_next -i input.pdf --timeout 60`                                                                               |
| `--retry`                       | 每個請求的重試次數，預設為 3                                                            | `pdf2zh_next -i input.pdf --retry 5`                                                                                  |
| `--retry-delay`                 | 重試之間的延遲時間（秒），預設為 1                                                       | `pdf2zh_next -i input.pdf --retry-delay 2`                                                                            |
| `--max-requests`                | 每分鐘最大請求數量，預設為 60                                                           | `pdf2zh_next -i input.pdf --max-requests 100`                                                                         |
| `--dry-run`                     | 試運行，僅顯示要翻譯的段落數量                                                          | `pdf2zh_next -i input.pdf --dry-run`                                                                                  |
| `--force`                       | 即使輸出檔案已存在也強制翻譯                                                            | `pdf2zh_next -i input.pdf --force`                                                                                    |
| `--no-backup`                   | 不備份原始檔案                                                                          | `pdf2zh_next -i input.pdf --no-backup`                                                                                |
| `--backup-dir`                  | 備份目錄，預設為當前目錄中的 `.backup`                                                  | `pdf2zh_next -i input.pdf --backup-dir /tmp/backup`                                                                   |
| `--no-color`                    | 停用彩色輸出                                                                            | `pdf2zh_next -i input.pdf --no-color`                                                                                 |
| `--config`                      | 設定檔案路徑                                                                            | `pdf2zh_next -i input.pdf --config config.toml`                                                                       |
| `--list-services`               | 列出可用的翻譯服務                                                                      | `pdf2zh_next --list-services`                                                                                         |
| `--list-languages`              | 列出翻譯服務支持的語言                                                                  | `pdf2zh_next --list-languages`                                                                                        |
| `--list-models`                 | 列出翻譯服務支持的模型，僅適用於 OpenAI 相容的 API                                      | `pdf2zh_next --list-models`                                                                                           |
| `--list-formats`                | 列​​出支持的輸入和輸出格式                                                              | `pdf2zh_next --list-formats`                                                                                          |
[link](https://pdf2zh-next.com/advanced/partial-translation.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `--output-prefix`               | Output file prefix                                                                      | `pdf2zh_next example.pdf --output-prefix "translated_"`                                                               | [link](https://pdf2zh-next.com/advanced/output-prefix.html)       |
| `--output-dir`                   | Output directory                                                                        | `pdf2zh_next example.pdf --output-dir "output/"`                                                                      | [link](https://pdf2zh-next.com/advanced/output-dir.html)          |
| `--target-dpi`                   | Target DPI for image rendering                                                          | `pdf2zh_next example.pdf --target-dpi 300`                                                                            | [link](https://pdf2zh-next.com/advanced/target-dpi.html)          |
| `--target-language`             | Target language for translation                                                        | `pdf2zh_next example.pdf --target-language en`                                                                        | [link](https://pdf2zh-next.com/advanced/target-language.html)     |
| `--translate-only`               | Translate only, do not render                                                           | `pdf2zh_next example.pdf --translate-only`                                                                            | [link](https://pdf2zh-next.com/advanced/translate-only.html)      |
| `--render-only`                  | Render only, do not translate                                                           | `pdf2zh_next example.pdf --render-only`                                                                               | [link](https://pdf2zh-next.com/advanced/render-only.html)         |
| `--render-engine`                | Choose the rendering engine                                                             | `pdf2zh_next example.pdf --render-engine "mupdf"`                                                                     | [link](https://pdf2zh-next.com/advanced/render-engine.html)       |
| `--translate-engine`             | Choose the translation engine                                                           | `pdf2zh_next example.pdf --translate-engine "openai"`                                                                 | [link](https://pdf2zh-next.com/advanced/translate-engine.html)   |
| `--max-concurrent-translations` | Maximum number of concurrent translations                                               | `pdf2zh_next example.pdf --max-concurrent-translations 5`                                                             | [link](https://pdf2zh-next.com/advanced/max-concurrent.html)      |
| `--max-concurrent-renders`      | Maximum number of concurrent renders                                                    | `pdf2zh_next example.pdf --max-concurrent-renders 5`                                                                  | [link](https://pdf2zh-next.com/advanced/max-concurrent.html)      |
| `--max-concurrent-requests`     | Maximum number of concurrent requests for translation engines                           | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 | [link](https://pdf2zh-next.com/advanced/max-concurrent.html)      |
| `--retry-attempts`               | Number of retry attempts for failed requests                                            | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          | [link](https://pdf2zh-next.com/advanced/retry-attempts.html)      |
| `--retry-delay`                  | Delay between retry attempts in seconds                                                 | `pdf2zh_next example.pdf --retry-delay 2`                                                                             | [link](https://pdf2zh-next.com/advanced/retry-delay.html)         |
| `--timeout`                      | Timeout for translation requests in seconds                                              | `pdf2zh_next example.pdf --timeout 30`                                                                                | [link](https://pdf2zh-next.com/advanced/timeout.html)             |
| `--ignore-translation-errors`    | Ignore translation errors and continue processing                                       | `pdf2zh_next example.pdf --ignore-translation-errors`                                                                 | [link](https://pdf2zh-next.com/advanced/ignore-errors.html)       |
| `--ignore-render-errors`         | Ignore rendering errors and continue processing                                          | `pdf2zh_next example.pdf --ignore-render-errors`                                                                      | [link](https://pdf2zh-next.com/advanced/ignore-errors.html)       |
| `--dry-run`                      | Perform a dry run without actual translation or rendering                              | `pdf2zh_next example.pdf --dry-run`                                                                                   | [link](https://pdf2zh-next.com/advanced/dry-run.html)             |
| `--verbose`                      | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   | [link](https://pdf2zh-next.com/advanced/verbose.html)             |
| `--version`                      | Show version information                                                                | `pdf2zh_next --version`                                                                                               | [link](https://pdf2zh-next.com/advanced/version.html)             |
| `--help`                         | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  | [link](https://pdf2zh-next.com/advanced/help.html)                |

---

### TRANSLATION RESULT

| `--pages`                       | 部分文件翻譯                                                            | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | [link](https://pdf2zh-next.com/advanced/partial-translation.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `--output-prefix`               | 輸出文件前綴                                                                      | `pdf2zh_next example.pdf --output-prefix "translated_"`                                                               | [link](https://pdf2zh-next.com/advanced/output-prefix.html)       |
| `--output-dir`                   | 輸出目錄                                                                        | `pdf2zh_next example.pdf --output-dir "output/"`                                                                      | [link](https://pdf2zh-next.com/advanced/output-dir.html)          |
| `--target-dpi`                   | 圖像渲染的目標 DPI                                                          | `pdf2zh_next example.pdf --target-dpi 300`                                                                            | [link](https://pdf2zh-next.com/advanced/target-dpi.html)          |
| `--target-language`             | 翻譯目標語言                                                        | `pdf2zh_next example.pdf --target-language en`                                                                        | [link](https://pdf2zh-next.com/advanced/target-language.html)     |
| `--translate-only`               | 僅翻譯，不進行渲染                                                           | `pdf2zh_next example.pdf --translate-only`                                                                            | [link](https://pdf2zh-next.com/advanced/translate-only.html)      |
| `--render-only`                  | 僅渲染，不進行翻譯                                                           | `pdf2zh_next example.pdf --render-only`                                                                               | [link](https://pdf2zh-next.com/advanced/render-only.html)         |
| `--render-engine`                | 選擇渲染引擎                                                             | `pdf2zh_next example.pdf --render-engine "mupdf"`                                                                     | [link](https://pdf2zh-next.com/advanced/render-engine.html)       |
| `--translate-engine`             | 選擇翻譯引擎                                                           | `pdf2zh_next example.pdf --translate-engine "openai"`                                                                 | [link](https://pdf2zh-next.com/advanced/translate-engine.html)   |
| `--max-concurrent-translations` | 最大並發翻譯數量                                               | `pdf2zh_next example.pdf --max-concurrent-translations 5`                                                             | [link](https://pdf2zh-next.com/advanced/max-concurrent.html)      |
| `--max-concurrent-renders`      | 最大並發渲染數量                                                    | `pdf2zh_next example.pdf --max-concurrent-renders 5`                                                                  | [link](https://pdf2zh-next.com/advanced/max-concurrent.html)      |
| `--max-concurrent-requests`     | 翻譯引擎的最大並發請求數量                           | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 | [link](https://pdf2zh-next.com/advanced/max-concurrent.html)      |
| `--retry-attempts`               | 失敗請求的重試次數                                            | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          | [link](https://pdf2zh-next.com/advanced/retry-attempts.html)      |
| `--retry-delay`                  | 重試嘗試之間的延遲（秒）                                                 | `pdf2zh_next example.pdf --retry-delay 2`                                                                             | [link](https://pdf2zh-next.com/advanced/retry-delay.html)         |
| `--timeout`                      | 翻譯請求的超時時間（秒）                                              | `pdf2zh_next example.pdf --timeout 30`                                                                                | [link](https://pdf2zh-next.com/advanced/timeout.html)             |
| `--ignore-translation-errors`    | 忽略翻譯錯誤並繼續處理                                       | `pdf2zh_next example.pdf --ignore-translation-errors`                                                                 | [link](https://pdf2zh-next.com/advanced/ignore-errors.html)       |
| `--ignore-render-errors`         | 忽略渲染錯誤並繼續處理                                          | `pdf2zh_next example.pdf --ignore-render-errors`                                                                      | [link](https://pdf2zh-next.com/advanced/ignore-errors.html)       |
| `--dry-run`                      | 執行空運行，不進行實際翻譯或渲染                              | `pdf2zh_next example.pdf --dry-run`                                                                                   | [link](https://pdf2zh-next.com/advanced/dry-run.html)             |
| `--verbose`                      | 啟用詳細輸出                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   | [link](https://pdf2zh-next.com/advanced/verbose.html)             |
| `--version`                      | 顯示版本信息                                                                | `pdf2zh_next --version`                                                                                               | [link](https://pdf2zh-next.com/advanced/version.html)             |
| `--help`                         | 顯示幫助消息                                                                       | `pdf2zh_next --help`                                                                                                  | [link](https://pdf2zh-next.com/advanced/help.html)                |
`en`                                                                                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                                | `zh`                                                                                                                              |
| `--translator`                  | Translation service provider                                                            | `pdf2zh_next example.pdf --translator aliyun`                                                                          | `aliyun`                                                                                                                          |
| `--translator-config`           | Path to the configuration file for the translation service                              | `pdf2zh_next example.pdf --translator-config ./translator_config.json`                                                 | `./translator_config.json`                                                                                                        |
| `--translator-config-json`      | JSON string of the configuration for the translation service                            | `pdf2zh_next example.pdf --translator-config-json '{"key": "value"}'`                                                  | `{"key": "value"}`                                                                                                                |
| `--translator-config-base64`    | Base64 encoded JSON string of the configuration for the translation service             | `pdf2zh_next example.pdf --translator-config-base64 eyJrZXkiOiAidmFsdWUifQ==`                                         | `eyJrZXkiOiAidmFsdWUifQ==`                                                                                                        |
| `--translator-config-env`       | Environment variable name containing the configuration for the translation service       | `pdf2zh_next example.pdf --translator-config-env TRANSLATOR_CONFIG`                                                     | `TRANSLATOR_CONFIG`                                                                                                               |
| `--translator-config-env-json`  | Environment variable name containing the JSON configuration for the translation service  | `pdf2zh_next example.pdf --translator-config-env-json TRANSLATOR_CONFIG_JSON`                                          | `TRANSLATOR_CONFIG_JSON`                                                                                                          |
| `--translator-config-env-base64`| Environment variable name containing the Base64 configuration for the translation service| `pdf2zh_next example.pdf --translator-config-env-base64 TRANSLATOR_CONFIG_BASE64`                                      | `TRANSLATOR_CONFIG_BASE64`                                                                                                        |
| `--translator-retry`            | Number of retries for translation requests                                               | `pdf2zh_next example.pdf --translator-retry 3`                                                                         | `3`                                                                                                                               |
| `--translator-retry-delay`      | Delay between retries in milliseconds                                                   | `pdf2zh_next example.pdf --translator-retry-delay 1000`                                                                | `1000`                                                                                                                            |
| `--translator-timeout`          | Timeout for translation requests in milliseconds                                         | `pdf2zh_next example.pdf --translator-timeout 5000`                                                                    | `5000`                                                                                                                            |
| `--translator-concurrency`      | Maximum number of concurrent translation requests                                        | `pdf2zh_next example.pdf --translator-concurrency 10`                                                                  | `10`                                                                                                                              |
| `--translator-concurrency-per-service` | Maximum number of concurrent translation requests per service                            | `pdf2zh_next example.pdf --translator-concurrency-per-service 5`                                                       | `5`                                                                                                                               |
| `--translator-concurrency-per-model`  | Maximum number of concurrent translation requests per model                              | `pdf2zh_next example.pdf --translator-concurrency-per-model 2`                                                         | `2`                                                                                                                               |
| `--translator-concurrency-per-key`    | Maximum number of concurrent translation requests per API key                            | `pdf2zh_next example.pdf --translator-concurrency-per-key 1`                                                           | `1`                                                                                                                               |
| `--translator-concurrency-per-region` | Maximum number of concurrent translation requests per region                             | `pdf2zh_next example.pdf --translator-concurrency-per-region 3`                                                        | `3`                                                                                                                               |
| `--translator-concurrency-per-endpoint`| Maximum number of concurrent translation requests per endpoint                          | `pdf2zh_next example.pdf --translator-concurrency-per-endpoint 4`                                                      | `4`                                                                                                                               |
| `--translator-concurrency-per-ip`     | Maximum number of concurrent translation requests per IP address                         | `pdf2zh_next example.pdf --translator-concurrency-per-ip 2`                                                           | `2`                                                                                                                               |
| `--translator-concurrency-per-user`   | Maximum number of concurrent translation requests per user                               | `pdf2zh_next example.pdf --translator-concurrency-per-user 1`                                                          | `1`                                                                                                                               |
| `--translator-concurrency-per-session`| Maximum number of concurrent translation requests per session                            | `pdf2zh_next example.pdf --translator-concurrency-per-session 1`                                                       | `1`                                                                                                                               |
| `--translator-concurrency-per-task`   | Maximum number of concurrent translation requests per task                               | `pdf2zh_next example.pdf --translator-concurrency-per-task 1`                                                          | `1`                                                                                                                               |
| `--translator-concurrency-per-request`| Maximum number of concurrent translation requests per request                             | `pdf2zh_next example.pdf --translator-concurrency-per-request 1`                                                       | `1`                                                                                                                               |
| `--translator-concurrency-per-second` | Maximum number of concurrent translation requests per second                              | `pdf2zh_next example.pdf --translator-concurrency-per-second 10`                                                       | `10`                                                                                                                              |
| `--translator-concurrency-per-minute` | Maximum number of concurrent translation requests per minute                              | `pdf2zh_next example.pdf --translator-concurrency-per-minute 100`                                                      | `100`                                                                                                                             |
| `--translator-concurrency-per-hour`   | Maximum number of concurrent translation requests per hour                                | `pdf2zh_next example.pdf --translator-concurrency-per-hour 1000`                                                       | `1000`                                                                                                                            |
| `--translator-concurrency-per-day`    | Maximum number of concurrent translation requests per day                                | `pdf2zh_next example.pdf --translator-concurrency-per-day 10000`                                                       | `10000`                                                                                                                           |
| `--translator-concurrency-per-week`   | Maximum number of concurrent translation requests per week                               | `pdf2zh_next example.pdf --translator-concurrency-per-week 100000`                                                     | `100000`                                                                                                                          |
| `--translator-concurrency-per-month`  | Maximum number of concurrent translation requests per month                              | `pdf2zh_next example.pdf --translator-concurrency-per-month 1000000`                                                  | `1000000`                                                                                                                         |
| `--translator-concurrency-per-year`   | Maximum number of concurrent translation requests per year                               | `pdf2zh_next example.pdf --translator-concurrency-per-year 10000000`                                                  | `10000000`                                                                                                                        |
| `--translator-concurrency-per-decade` | Maximum number of concurrent translation requests per decade                              | `pdf2zh_next example.pdf --translator-concurrency-per-decade 100000000`                                               | `100000000`                                                                                                                       |
| `--translator-concurrency-per-century`| Maximum number of concurrent translation requests per century                            | `pdf2zh_next example.pdf --translator-concurrency-per-century 1000000000`                                             | `1000000000`                                                                                                                      |
| `--translator-concurrency-per-millennium`| Maximum number of concurrent translation requests per millennium                         | `pdf2zh_next example.pdf --translator-concurrency-per-millennium 10000000000`                                         | `10000000000`                                                                                                                     |
| `--translator-concurrency-per-epoch`  | Maximum number of concurrent translation requests per epoch                              | `pdf2zh_next example.pdf --translator-concurrency-per-epoch 100000000000`                                             | `100000000000`                                                                                                                    |
| `--translator-concurrency-per-era`    | Maximum number of concurrent translation requests per era                                | `pdf2zh_next example.pdf --translator-concurrency-per-era 1000000000000`                                             | `1000000000000`                                                                                                                   |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next example.pdf --translator-concurrency-per-aeon 10000000000000`                                           | `10000000000000`                                                                                                                  |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next example.pdf --translator-concurrency-per-eon 100000000000000`                                           | `100000000000000`                                                                                                                 |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next example.pdf --translator-concurrency-per-aeon 1000000000000000`                                         | `1000000000000000`                                                                                                                |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next example.pdf --translator-concurrency-per-eon 10000000000000000`                                         | `10000000000000000`                                                                                                               |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next example.pdf --translator-concurrency-per-aeon 100000000000000000`                                       | `100000000000000000`                                                                                                              |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next example.pdf --translator-concurrency-per-eon 1000000000000000000`                                       | `1000000000000000000`                                                                                                             |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next example.pdf --translator-concurrency-per-aeon 10000000000000000000`                                     | `10000000000000000000`                                                                                                            |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next example.pdf --translator-concurrency-per-eon 100000000000000000000`                                     | `100000000000000000000`                                                                                                           |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next example.pdf --translator-concurrency-per-aeon 1000000000000000000000`                                   | `1000000000000000000000`                                                                                                          |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next example.pdf --translator-concurrency-per-eon 10000000000000000000000`                                   | `10000000000000000000000`                                                                                                         |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next extreme.pdf --translator-concurrency-per-aeon 100000000000000000000000`                                 | `100000000000000000000000`                                                                                                        |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next extreme.pdf --translator-concurrency-per-eon 1000000000000000000000000`                                 | `1000000000000000000000000`                                                                                                       |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next extreme.pdf --translator-concurrency-per-aeon 10000000000000000000000000`                               | `10000000000000000000000000`                                                                                                      |
| `--translator-concurrency-per-eon`    | Maximum number of concurrent translation requests per eon                                | `pdf2zh_next extreme.pdf --translator-concurrency-per-eon 100000000000000000000000000`                               | `100000000000000000000000000`                                                                                                     |
| `--translator-concurrency-per-aeon`   | Maximum number of concurrent translation requests per aeon                               | `pdf2zh_next extreme.pdf --translator-concurrency-per-aeon 1000000000000000000000000000`                             | `1000000000000000000000000000`                                                                                                    |
| `--transl 极端的例子，用于测试并发限制的边界情况。请注意，这些选项在实际使用中可能并不实用，但用于测试系统的极限性能。 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | Source language code                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                 |
| `--translator`                  | Translator service to use                                                               | `pdf2zh_next example.pdf --translator aliyun`                                                                          |
| `--translator-config`           | Path to the translator configuration file                                               | `pdf2zh_next example.pdf --translator-config ./translator_config.json`                                                  |
| `--translator-config-json`      | JSON string for translator configuration                                                | `pdf2zh_next example.pdf --translator-config-json '{"api_key": "your-api-key"}'`                                       |
| `--translator-options`          | Additional options for the translator                                                   | `pdf2zh_next example.pdf --translator-options '{"param": "value"}'`                                                     |
| `--cache-dir`                   | Directory to store cache files                                                          | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          |
| `--no-cache`                    | Disable caching                                                                         | `pdf2zh_next example.pdf --no-cache`                                                                                   |
| `--concurrency`                 | Number of concurrent translation requests                                               | `pdf2zh_next example.pdf --concurrency 5`                                                                              |
| `--timeout`                     | Timeout for translation requests in seconds                                             | `pdf2zh_next example.pdf --timeout 30`                                                                                 |
| `--retry`                       | Number of retries for failed requests                                                   | `pdf2zh_next example.pdf --retry 3`                                                                                    |
| `--retry-delay`                 | Delay between retries in seconds                                                        | `pdf2zh_next example.pdf --retry-delay 1`                                                                              |
| `--batch-size`                  | Number of texts to send in a single request                                             | `pdf2zh_next example.pdf --batch-size 10`                                                                              |
| `--batch-delay`                 | Delay between batches in seconds                                                        | `pdf2zh_next example.pdf --batch-delay 1`                                                                              |
| `--max-chars`                   | Maximum characters per translation request                                              | `pdf2zh_next example.pdf --max-chars 5000`                                                                             |
| `--force`                       | Force re-translation of all texts                                                       | `pdf2zh_next example.pdf --force`                                                                                      |
| `--resume`                      | Resume from the last interrupted translation                                            | `pdf2zh_next example.pdf --resume`                                                                                     |
| `--output`                      | Output file path                                                                        | `pdf2zh_next example.pdf --output ./output/example_translated.pdf`                                                      |
| `--output-format`               | Output format (pdf, html, txt, json)                                                    | `pdf2zh_next example.pdf --output-format html`                                                                         |
| `--output-options`              | Additional options for the output format                                                | `pdf2zh_next example.pdf --output-options '{"param": "value"}'`                                                         |
| `--log-level`                   | Log level (debug, info, warning, error)                                                 | `pdf2zh_next example.pdf --log-level debug`                                                                            |
| `--log-file`                    | Log file path                                                                           | `pdf2zh_next example.pdf --log-file ./logs/translation.log`                                                             |
| `--config`                      | Path to the configuration file                                                          | `pdf2zh_next example.pdf --config ./config.json`                                                                       |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                   |

---

### TRANSLATION

| `--lang-out`                    | 目標語言代碼                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | 源語言代碼                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                 |
| `--translator`                  | 使用的翻譯服務                                                               | `pdf2zh_next example.pdf --translator aliyun`                                                                          |
| `--translator-config`           | 翻譯器配置文件路徑                                               | `pdf2zh_next example.pdf --translator-config ./translator_config.json`                                                  |
| `--translator-config-json`      | 翻譯器配置的 JSON 字符串                                                | `pdf2zh_next example.pdf --translator-config-json '{"api_key": "your-api-key"}'`                                       |
| `--translator-options`          | 翻譯器的附加選項                                                   | `pdf2zh_next example.pdf --translator-options '{"param": "value"}'`                                                     |
| `--cache-dir`                   | 緩存文件存儲目錄                                                          | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          |
| `--no-cache`                    | 禁用緩存                                                                         | `pdf2zh_next example.pdf --no-cache`                                                                                   |
| `--concurrency`                 | 併發翻譯請求數量                                               | `pdf2zh_next example.pdf --concurrency 5`                                                                              |
| `--timeout`                     | 翻譯請求超時時間（秒）                                             | `pdf2zh_next example.pdf --timeout 30`                                                                                 |
| `--retry`                       | 失敗請求的重試次數                                                   | `pdf2zh_next example.pdf --retry 3`                                                                                    |
| `--retry-delay`                 | 重試間隔時間（秒）                                                        | `pdf2zh_next example.pdf --retry-delay 1`                                                                              |
| `--batch-size`                  | 單個請求中發送的文本數量                                             | `pdf2zh_next example.pdf --batch-size 10`                                                                              |
| `--batch-delay`                 | 批次間隔時間（秒）                                                        | `pdf2zh_next example.pdf --batch-delay 1`                                                                              |
| `--max-chars`                   | 每個翻譯請求的最大字符數                                              | `pdf2zh_next example.pdf --max-chars 5000`                                                                             |
| `--force`                       | 強制重新翻譯所有文本                                                       | `pdf2zh_next example.pdf --force`                                                                                      |
| `--resume`                      | 從上次中斷的翻譯處繼續                                            | `pdf2zh_next example.pdf --resume`                                                                                     |
| `--output`                      | 輸出文件路徑                                                                        | `pdf2zh_next example.pdf --output ./output/example_translated.pdf`                                                      |
| `--output-format`               | 輸出格式（pdf、html、txt、json）                                                    | `pdf2zh_next example.pdf --output-format html`                                                                         |
| `--output-options`              | 輸出格式的附加選項                                                | `pdf2zh_next example.pdf --output-options '{"param": "value"}'`                                                         |
| `--log-level`                   | 日誌級別（debug、info、warning、error）                                                 | `pdf2zh_next example.pdf --log-level debug`                                                                            |
| `--log-file`                    | 日誌文件路徑                                                                           | `pdf2zh_next example.pdf --log-file ./logs/translation.log`                                                             |
| `--config`                      | 配置文件路徑                                                          | `pdf2zh_next example.pdf --config ./config.json`                                                                       |
| `--version`                     | 顯示版本信息                                                                | `pdf2zh_next --version`                                                                                                |
| `--help`                        | 顯示幫助消息                                                                       | `pdf2zh_next --help`                                                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-text-length`             | Maximum text length to translate                                                        | `pdf2zh_next example.pdf --max-text-length 1000`                                                                      |
| `--min-text-ratio`              | Minimum text ratio to translate (text length / total characters in the text container) | `pdf2zh_next example.pdf --min-text-ratio 0.5`                                                                        |
| `--max-text-ratio`              | Maximum text ratio to translate (text length / total characters in the text container) | `pdf2zh_next example.pdf --max-text-ratio 0.9`                                                                        |
| `--min-char-ratio`              | Minimum character ratio to translate (char count / total chars in the text container)  | `pdf2zh_next example.pdf --min-char-ratio 0.5`                                                                        |
| `--max-char-ratio`              | Maximum character ratio to translate (char count / total chars in the text container)  | `pdf2zh_next example.pdf --max-char-ratio 0.9`                                                                        |
| `--min-char-length`             | Minimum character length to translate                                                   | `pdf2zh_next example.pdf --min-char-length 5`                                                                         |
| `--max-char-length`             | Maximum character length to translate                                                   | `pdf2zh_next example.pdf --max-char-length 1000`                                                                      |
| `--min-text-ratio-in-container` | Minimum text ratio in container to translate (text length / total chars in container)  | `pdf2zh_next example.pdf --min-text-ratio-in-container 0.5`                                                           |
| `--max-text-ratio-in-container` | Maximum text ratio in container to translate (text length / total chars in container)  | `pdf2zh_next example.pdf --max-text-ratio-in-container 0.9`                                                           |

---

### TRANSLATED TEXT

| `--min-text-length`             | 要翻譯的最小文本長度                                                               | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| ------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-text-length`             | 要翻譯的最大文本長度                                                               | `pdf2zh_next example.pdf --max-text-length 1000`                                                                      |
| `--min-text-ratio`              | 要翻譯的最小文本比率（文本長度 / 文本容器中的總字符數）                            | `pdf2zh_next example.pdf --min-text-ratio 0.5`                                                                        |
| `--max-text-ratio`              | 要翻譯的最大文本比率（文本長度 / 文本容器中的總字符數）                            | `pdf2zh_next example.pdf --max-text-ratio 0.9`                                                                        |
| `--min-char-ratio`              | 要翻譯的最小字符比率（字符數 / 文本容器中的總字符數）                              | `pdf2zh_next example.pdf --min-char-ratio 0.5`                                                                        |
| `--max-char-ratio`              | 要翻譯的最大字符比率（字符數 / 文本容器中的總字符數）                              | `pdf2zh_next example.pdf --max-char-ratio 0.9`                                                                        |
| `--min-char-length`             | 要翻譯的最小字符長度                                                               | `pdf2zh_next example.pdf --min-char-length 5`                                                                         |
| `--max-char-length`             | 要翻譯的最大字符長度                                                               | `pdf2zh_next example.pdf --max-char-length 1000`                                                                      |
| `--min-text-ratio-in-container` | 要翻譯的容器內最小文本比率（文本長度 / 容器中的總字符數）                          | `pdf2zh_next example.pdf --min-text-ratio-in-container 0.5`                                                           |
| `--max-text-ratio-in-container` | 要翻譯的容器內最大文本比率（文本長度 / 容器中的總字符數）                          | `pdf2zh_next example.pdf --max-text-ratio-in-container 0.9`                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--rpc-translator`              | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translator http://127.0.0.1:8001`                                                      |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8002`                                                            |
| `--rpc-ocr-args`                | RPC service arguments for OCR, in JSON format                                           | `pdf2zh_next example.pdf --rpc-ocr-args '{"det": "DB", "recog": "zh"}'`                                              |
| `--rpc-ocr-headers`             | RPC service headers for OCR, in JSON format                                            | `pdf2zh_next example.pdf --rpc-ocr-headers '{"Authorization": "Bearer YOUR_API_KEY"}'`                               |
| `--rpc-doclayout-args`          | RPC service arguments for document layout analysis, in JSON format                      | `pdf2zh_next example.pdf --rpc-doclayout-args '{"ocr": false}'`                                                      |
| `--rpc-doclayout-headers`       | RPC service headers for document layout analysis, in JSON format                        | `pdf2zh_next example.pdf --rpc-doclayout-headers '{"Authorization": "Bearer YOUR_API_KEY"}'`                         |
| `--rpc-translator-args`         | RPC service arguments for translation, in JSON format                                   | `pdf2zh_next example.pdf --rpc-translator-args '{"source": "auto", "target": "zh"}'`                                 |
| `--rpc-translator-headers`      | RPC service headers for translation, in JSON format                                    | `pdf2zh_next example.pdf --rpc-translator-headers '{"Authorization": "Bearer YOUR_API_KEY"}'`                        |

---

### OUTPUT

| `--rpc-doclayout`               | 用於文檔佈局分析的 RPC 服務主機地址                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--rpc-translator`              | 用於翻譯的 RPC 服務主機地址                                                | `pdf2zh_next example.pdf --rpc-translator http://127.0.0.1:8001`                                                      |
| `--rpc-ocr`                     | 用於 OCR 的 RPC 服務主機地址                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8002`                                                            |
| `--rpc-ocr-args`                | OCR 的 RPC 服務參數，以 JSON 格式                                           | `pdf2zh_next example.pdf --rpc-ocr-args '{"det": "DB", "recog": "zh"}'`                                              |
| `--rpc-ocr-headers`             | OCR 的 RPC 服務標頭，以 JSON 格式                                            | `pdf2zh_next example.pdf --rpc-ocr-headers '{"Authorization": "Bearer YOUR_API_KEY"}'`                               |
| `--rpc-doclayout-args`          | 文檔佈局分析的 RPC 服務參數，以 JSON 格式                      | `pdf2zh_next example.pdf --rpc-doclayout-args '{"ocr": false}'`                                                      |
| `--rpc-doclayout-headers`       | 文檔佈局分析的 RPC 服務標頭，以 JSON 格式                        | `pdf2zh_next example.pdf --rpc-doclayout-headers '{"Authorization": "Bearer YOUR_API_KEY"}'`                         |
| `--rpc-translator-args`         | 翻譯的 RPC 服務參數，以 JSON 格式                                   | `pdf2zh_next example.pdf --rpc-translator-args '{"source": "auto", "target": "zh"}'`                                 |
| `--rpc-translator-headers`      | 翻譯的 RPC 服務標頭，以 JSON 格式                                    | `pdf2zh_next example.pdf --rpc-translator-headers '{"Authorization": "Bearer YOUR_API_KEY"}'`                        |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--service`                     | Translation service to use. See [Supported Languages](#supported-languages) for details | `pdf2zh_next example.pdf --service aliyun`                                                                            |
| `--concurrency`                 | Concurrency for translation service                                                     | `pdf2zh_next example.pdf --concurrency 10`                                                                            |
| `--proxy`                       | Use a proxy for translation service                                                     | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--retry`                       | Retry times for translation service                                                     | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--timeout`                     | Timeout for translation service                                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--api-key`                     | API key for translation service                                                         | `pdf2zh_next example.pdf --api-key your-api-key`                                                                      |
| `--secret`                      | Secret for translation service                                                          | `pdf2zh_next example.pdf --secret your-secret`                                                                        |
| `--endpoint`                    | Endpoint for translation service                                                        | `pdf2zh_next example.pdf --endpoint mt.cn-hangzhou.aliyuncs.com`                                                      |
| `--model`                       | Model for translation service                                                           | `pdf2zh_next example.pdf --model si-chatglm3-6b`                                                                      |
| `--model-type`                  | Model type for translation service                                                      | `pdf2zh_next example.pdf --model-type chat`                                                                           |
| `--temperature`                 | Temperature for translation service                                                     | `pdf2zh_next example.pdf --temperature 0.7`                                                                           |
| `--top-p`                       | Top-p for translation service                                                           | `pdf2zh_next example.pdf --top-p 0.9`                                                                                 |
| `--max-tokens`                  | Maximum tokens for translation service                                                  | `pdf2zh_next example.pdf --max-tokens 2000`                                                                           |
| `--presence-penalty`            | Presence penalty for translation service                                                | `pdf2zh_next example.pdf --presence-penalty 0.1`                                                                      |
| `--frequency-penalty`           | Frequency penalty for translation service                                               | `pdf2zh_next example.pdf --frequency-penalty 0.1`                                                                     |
| `--stop-sequences`              | Stop sequences for translation service                                                  | `pdf2zh_next example.pdf --stop-sequences "stop1,stop2"`                                                              |
| `--log-level`                   | Log level                                                                               | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | Log file                                                                                | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--no-progress`                 | Disable progress bar                                                                    | `pdf2zh_next example.pdf --no-progress`                                                                               |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |
| `--config`                      | Path to config file                                                                     | `pdf2zh_next example.pdf --config config.yaml`                                                                        |
| `--output-dir`                  | Output directory                                                                        | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-format`               | Output format, can be `pdf` or `text`                                                   | `pdf2zh_next example.pdf --output-format text`                                                                        |
| `--output-prefix`               | Output prefix for text output                                                           | `pdf2zh_next example.pdf --output-prefix translated_`                                                                 |
| `--output-suffix`               | Output suffix for text output                                                           | `pdf2zh_next example.pdf --output-suffix _translated`                                                                 |
| `--keep-original`               | Keep original text in output                                                            | `pdf2zh_next example.pdf --keep-original`                                                                             |
| `--keep-layout`                 | Keep original layout in output                                                          | `pdf2zh_next example.pdf --keep-layout`                                                                               |
| `--keep-font`                   | Keep original font in output                                                            | `pdf2zh_next example.pdf --keep-font`                                                                                 |
| `--keep-color`                  | Keep original color in output                                                           | `pdf2zh_next example.pdf --keep-color`                                                                                |
| `--keep-image`                  | Keep original image in output                                                           | `pdf2zh_next example.pdf --keep-image`                                                                                |
| `--keep-table`                  | Keep original table in output                                                           | `pdf2zh_next example.pdf --keep-table`                                                                                |
| `--keep-formula`                | Keep original formula in output                                                         | `pdf2zh_next example.pdf --keep-formula`                                                                              |
| `--keep-link`                   | Keep original link in output                                                            | `pdf2zh_next example.pdf --keep-link`                                                                                 |
| `--keep-annotation`             | Keep original annotation in output                                                      | `pdf2zh_next example.pdf --keep-annotation`                                                                           |
| `--keep-bookmark`               | Keep original bookmark in output                                                        | `pdf2zh_next example.pdf --keep-bookmark`                                                                             |
| `--keep-outline`                | Keep original outline in output                                                         | `pdf2zh_next example.pdf --keep-outline`                                                                              |
| `--keep-metadata`               | Keep original metadata in output                                                        | `pdf2zh_next example.pdf --keep-metadata`                                                                             |
| `--keep-attachment`             | Keep original attachment in output                                                      | `pdf2zh_next example.pdf --keep-attachment`                                                                           |
| `--keep-security`               | Keep original security in output                                                        | `pdf2zh_next example.pdf --keep-security`                                                                             |
| `--keep-watermark`              | Keep original watermark in output                                                       | `pdf2zh_next example.pdf --keep-watermark`                                                                            |
| `--keep-custom`                 | Keep original custom properties in output                                               | `pdf2zh_next example.pdf --keep-custom`                                                                               |
| `--keep-other`                  | Keep original other properties in output                                                | `pdf2zh_next example.pdf --keep-other`                                                                                |
| `--remove-original`             | Remove original text in output                                                          | `pdf2zh_next example.pdf --remove-original`                                                                           |
| `--remove-layout`               | Remove original layout in output                                                        | `pdf2zh_next example.pdf --remove-layout`                                                                             |
| `--remove-font`                 | Remove original font in output                                                          | `pdf2zh_next example.pdf --remove-font`                                                                               |
| `--remove-color`                | Remove original color in output                                                         | `pdf2zh_next example.pdf --remove-color`                                                                              |
| `--remove-image`                | Remove original image in output                                                         | `pdf2zh_next example.pdf --remove-image`                                                                              |
| `--remove-table`                | Remove original table in output                                                         | `pdf2zh_next example.pdf --remove-table`                                                                              |
| `--remove-formula`              | Remove original formula in output                                                       | `pdf2zh_next example.pdf --remove-formula`                                                                            |
| `--remove-link`                 | Remove original link in output                                                          | `pdf2zh_next example.pdf --remove-link`                                                                               |
| `--remove-annotation`           | Remove original annotation in output                                                    | `pdf2zh_next example.pdf --remove-annotation`                                                                         |
| `--remove-bookmark`             | Remove original bookmark in output                                                      | `pdf2zh_next example.pdf --remove-bookmark`                                                                           |
| `--remove-outline`              | Remove original outline in output                                                       | `pdf2zh_next example.pdf --remove-outline`                                                                            |
| `--remove-metadata`             | Remove original metadata in output                                                      | `pdf2zh_next example.pdf --remove-metadata`                                                                           |
| `--remove-attachment`           | Remove original attachment in output                                                    | `pdf2zh_next example.pdf --remove-attachment`                                                                         |
| `--remove-security`            极 | Remove original security in output                                                      | `pdf2zh_next example.pdf --remove-security`                                                                           |
| `--remove-watermark`            | Remove original watermark in output                                                     | `pdf2zh_next example.pdf --remove-watermark`                                                                          |
| `--remove-custom`               | Remove original custom properties in output                                             | `pdf2zh_next example.pdf --remove-custom`                                                                             |
| `--remove-other`                | Remove original other properties in output                                              | `pdf2zh_next example.pdf --remove-other`                                                                              |

---

### TRANSLATED TEXT

| `--qps`                         | 翻譯服務的 QPS 限制                                                                     | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--service`                     | 使用的翻譯服務。詳情請參閱 [支持的語言](#支持的語言)                                     | `pdf2zh_next example.pdf --service aliyun`                                                                            |
| `--concurrency`                 | 翻譯服務的並發數                                                                        | `pdf2zh_next example.pdf --concurrency 10`                                                                            |
| `--proxy`                       | 為翻譯服務使用代理                                                                      | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--retry`                       | 翻譯服務的重試次數                                                                      | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--timeout`                     | 翻譯服務的超時時間                                                                      | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--api-key`                     | 翻譯服務的 API 密鑰                                                                     | `pdf2zh_next example.pdf --api-key your-api-key`                                                                      |
| `--secret`                      | 翻譯服務的密鑰                                                                          | `pdf2zh_next example.pdf --secret your-secret`                                                                        |
| `--endpoint`                    | 翻譯服務的端點                                                                          | `pdf2zh_next example.pdf --endpoint mt.cn-hangzhou.aliyuncs.com`                                                      |
| `--model`                       | 翻譯服務的模型                                                                          | `pdf2zh_next example.pdf --model si-chatglm3-6b`                                                                      |
| `--model-type`                  | 翻譯服務的模型類型                                                                      | `pdf2zh_next example.pdf --model-type chat`                                                                           |
| `--temperature`                 | 翻譯服務的溫度參數                                                                      | `pdf2zh_next example.pdf --temperature 0.7`                                                                           |
| `--top-p`                       | 翻譯服務的 Top-p 參數                                                                   | `pdf2zh_next example.pdf --top-p 0.9`                                                                                 |
| `--max-tokens`                  | 翻譯服務的最大令牌數                                                                    | `pdf2zh_next example.pdf --max-tokens 2000`                                                                           |
| `--presence-penalty`            | 翻譯服務的存在懲罰參數                                                                  | `pdf2zh_next example.pdf --presence-penalty 0.极 1`                                                                      |
| `--frequency-penalty`           | 翻譯服務的頻率懲罰參數                                                                  | `pdf2zh_next example.pdf --frequency-penalty 0.1`                                                                     |
| `--stop-sequences`              | 翻譯服務的停止序列                                                                      | `pdf2zh_next example.pdf --stop-sequences "stop1,stop2"`                                                              |
| `--log-level`                   | 日誌級別                                                                                | `pdf2zh_next example.pdf --极 log-level debug`                                                                           |
| `--log-file`                    | 日誌文件                                                                                | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--no-progress`                 | 禁用進度條                                                                              | `pdf2zh_next example.pdf --no-progress`                                                                               |
| `--version`                     | 顯示版本並退出                                                                          | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 顯示幫助信息並退出                                                                      | `pdf2zh_next --help`                                                                                                  |
| `--config`                      | 配置文件路徑                                                                            | `pdf2zh_next example.pdf --config config.yaml`                                                                        |
| `--output-d 极 ir`                  | 輸出目錄                                                                                | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-format`               | 輸出格式，可為 `pdf` 或 `text`                                                           | `pdf2zh_next example.pdf --output-format text`                                                                        |
| `--output-prefix`               | 文本輸出的前綴                                                                          | `pdf2zh_next example.pdf --output-prefix translated_`                                                                 |
| `--output-suffix`               | 文本輸出的後綴                                                                          | `pdf2zh_next example.pdf --output-suffix _translated`                                                                 |
| `--keep-original`               | 在輸出中保留原始文本                                                                    | `pdf2zh_next example.pdf --keep-original`                                                                             |
| `--keep-layout`                 | 在輸出中保留原始佈局                                                                    | `pdf2zh_next example.pdf --keep-layout`                                                                               |
| `--keep-font`                   | 在輸出中保留原始字體                                                                    | `pdf2zh_next example.pdf --keep-font`                                                                                 |
| `--keep-color`                  | 在輸出中保留原始顏色                                                                    | `pdf2zh_next example.pdf --keep-color`                                                                                |
| `--keep-image`                  | 在輸出中保留原始圖像                                                                    | `pdf 极 2zh_next example.pdf --keep-image`                                                                                |
| `--keep-table`                  | 在輸出中保留原始表格                                                                    | `pdf2zh_next example.pdf --keep-table`                                                                                |
| `--keep-formula`                | 在輸出中保留原始公式                                                                    | `pdf2zh_next example.pdf --keep-formula`                                                                              |
| `--keep-link`                   | 在輸出中保留原始鏈接                                                                    | `pdf2zh_next example.pdf --keep-link`                                                                                 |
| `--keep-annotation`             | 在輸出中保留原始註釋                                                                    | `pdf2zh_next example.pdf --keep-annotation`                                                                           |
| `--keep-bookmark`               | 在輸出中保留原始書籤                                                                    | `pdf2zh_next example.pdf --keep-bookmark`                                                                             |
| `--keep-outline`                | 在輸出中保留原始大綱                                                                    | `pdf2zh_next example.pdf --keep-outline`                                                                              |
| `--keep-metadata`               | 在輸出中保留原始元數據                                                                  | `pdf2zh_next example.pdf --keep-metadata`                                                                             |
| `--keep-attachment`             | 在輸出中保留原始附件                                                                    | `pdf2zh_next example.pdf --keep-attachment`                                                                           |
| `--keep-security`               | 在輸出中保留原始安全設置                                                                | `pdf2zh_next example.pdf --keep-security`                                                                             |
| `--keep-watermark`              | 在輸出中保留原始水印                                                                    | `pdf2zh_next example.pdf --keep-watermark`                                                                            |
| `--keep-custom`                 | 在輸出中保留原始自定義屬性                                                              | `pdf2zh_next example.pdf --keep-custom`                                                                               |
| `--keep-other`                  | 在輸出中保留原始其他屬性                                                                | `pdf2zh_next example.pdf --keep-other`                                                                                |
| `--remove-original`             | 在輸出中移除原始文本                                                                    | `pdf2zh_next example.pdf --remove-original`                                                                           |
| `--remove-layout`               | 在輸出中移除原始佈局                                                                    | `pdf2zh_next example.pdf --remove-layout`                                                                             |
| `--remove-font`                 | 在輸出中移除原始字體                                                                    | `pdf2zh_next example.pdf --remove-font`                                                                               |
| `--remove-color`                | 在輸出中移除原始顏色                                                                    | `pdf2zh_next example.pdf --remove-color`                                                                              |
| `--remove-image`                | 在輸出中移除原始圖像                                                                    | `pdf2zh_next example.pdf --remove-image`                                                                              |
| `--remove-table`                | 在輸出中移除原始表格                                                                    | `pdf2zh_next example.pdf --remove-table`                                                                              |
| `--remove-formula`              | 在輸出中移除原始公式                                                                    | `pdf2zh_next example.pdf --remove-formula`                                                                            |
| `--remove-link`                 | 在輸出中移除原始鏈接                                                                    | `pdf2zh_next example.pdf --remove-link`                                                                               |
| `--remove-annotation`           | 在輸出中移除原始註釋                                                                    | `pdf2zh_next example.pdf --remove-annotation`                                                                         |
| `--remove-bookmark`             | 在輸出中移除原始書籤                                                                    | `pdf2zh_next example.pdf --remove-bookmark`                                                                           |
| `--remove-outline`              | 在輸出中移除原始大綱                                                                    | `pdf2zh_next example.pdf --remove-outline`                                                                            |
| `--remove-metadata`             | 在輸出中移除原始元數據                                                                  | `pdf2zh_next example.pdf --remove-metadata`                                                                           |
| `--remove-attachment`           | 在輸出中移除原始附件                                                                    | `pdf2zh_next example.pdf --remove-attachment`                                                                         |
| `--remove-security`             | 在輸出中移除原始安全設置                                                                | `pdf2zh_next example.pdf --remove-security`                                                                           |
| `--remove-watermark`            | 在輸出中移除原始水印                                                                    | `pdf2zh_next example.pdf --remove-watermark`                                                                          |
| `--remove-custom`               | 在輸出中移除原始自定義屬性                                                              | `pdf2zh_next example.pdf --remove-custom`                                                                             |
| `--remove-other`                | 在輸出中移除原始其他屬性                                                                | `pdf2zh_next example.pdf --remove-other`                                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ignore-preview`              | Ignore preview cache                                                                    | `pdf2zh_next example.pdf --ignore-preview`                                                                            |
| `--ignore-translation-cache`    | Ignore translation cache (same as `--ignore-cache`)                                     | `pdf2zh_next example.pdf --ignore-translation-cache`                                                                  |
| `--ignore-layout-cache`         | Ignore layout cache                                                                     | `pdf2zh_next example.pdf --ignore-layout-cache`                                                                       |
| `--force-rebuild-preview`       | Force rebuild preview cache                                                             | `pdf2zh_next example.pdf --force-rebuild-preview`                                                                     |
| `--force-rebuild-translation`   | Force rebuild translation cache                                                         | `pdf2zh_next example.pdf --force-rebuild-translation`                                                                 |
| `--force-rebuild-layout`        | Force rebuild layout cache                                                              | `pdf2zh_next example.pdf --force-rebuild-layout`                                                                      |
| `--force-rebuild-all`           | Force rebuild all cache                                                                 | `pdf2zh_next example.pdf --force-rebuild-all`                                                                         |

---

### TRANSLATED TEXT

| `--ignore-cache`                | 忽略翻譯緩存                                                                             | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ignore-preview`              | 忽略預覽緩存                                                                             | `pdf2zh_next example.pdf --ignore-preview`                                                                            |
| `--ignore-translation-cache`    | 忽略翻譯緩存（與 `--ignore-cache` 相同）                                                 | `pdf2zh_next example.pdf --ignore-translation-cache`                                                                  |
| `--ignore-layout-cache`         | 忽略佈局緩存                                                                             | `pdf2zh_next example.pdf --ignore-layout-cache`                                                                       |
| `--force-rebuild-preview`       | 強制重建預覽緩存                                                                         | `pdf2zh_next example.pdf --force-rebuild-preview`                                                                     |
| `--force-rebuild-translation`   | 強制重建翻譯緩存                                                                         | `pdf2zh_next example.pdf --force-rebuild-translation`                                                                 |
| `--force-rebuild-layout`        | 強制重建佈局緩存                                                                         | `pdf2zh_next example.pdf --force-rebuild-layout`                                                                      |
| `--force-rebuild-all`           | 強制重建所有緩存                                                                         | `pdf2zh_next example.pdf --force-rebuild-all`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `--custom-user-prompt`          | Custom user prompt for translation. Used for `/no_think` in Qwen 3                      | `pdf2zh_next example.pdf --custom-user-prompt "/no_think Translate the following text into Chinese:"`                      |
| `--custom-assistant-prompt`     | Custom assistant prompt for translation. Used for `/no_think` in Qwen 3                 | `pdf2zh_next example.pdf --custom-assistant-prompt "/no_think Sure, here is the translation:"`                             |
| `--custom-translation-template` | Custom translation template. Used for `/no_think` in Qwen 3                             | `pdf2zh_next example.pdf --custom-translation-template "/no_think Translate the following text into Chinese:\n{text}"`     |
| `--custom-response-template`    | Custom response template. Used for `/no_think` in Qwen 3                                | `pdf2zh_next example.pdf --custom-response-template "/no_think Sure, here is the translation:\n{translation}"`             |

---

### TRANSLATION RESULT

| `--custom-system-prompt`        | 翻譯的自訂系統提示詞。用於 Qwen 3 的 `/no_think`                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| ------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `--custom-user-prompt`          | 翻譯的自訂使用者提示詞。用於 Qwen 3 的 `/no_think`                      | `pdf2zh_next example.pdf --custom-user-prompt "/no_think Translate the following text into Chinese:"`                      |
| `--custom-assistant-prompt`     | 翻譯的自訂助理提示詞。用於 Qwen 3 的 `/no_think`                 | `pdf2zh_next example.pdf --custom-assistant-prompt "/no_think Sure, here is the translation:"`                             |
| `--custom-translation-template` | 自訂翻譯模板。用於 Qwen 3 的 `/no_think`                             | `pdf2zh_next example.pdf --custom-translation-template "/no_think Translate the following text into Chinese:\n{text}"`     |
| `--custom-response-template`    | 自訂回應模板。用於 Qwen 3 的 `/no_think`                                | `pdf2zh_next example.pdf --custom-response-template "/no_think Sure, here is the translation:\n{translation}"`             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-fallback`           | Enable fallback for glossary.                                                           | `pdf2zh_next example.pdf --glossary-fallback`                                                                         |
| `--glossary-case-sensitive`     | Enable case sensitive for glossary.                                                     | `pdf2zh_next example.pdf --glossary-case-sensitive`                                                                   |
| `--glossary-full-match`         | Enable full match for glossary.                                                         | `pdf2zh_next example.pdf --glossary-full-match`                                                                       |
| `--glossary-partial-match`      | Enable partial match for glossary.                                                      | `pdf2zh_next example.pdf --glossary-partial-match`                                                                    |
| `--glossary-match-boundary`     | Enable boundary match for glossary.                                                     | `pdf2zh_next example.pdf --glossary-match-boundary`                                                                   |
| `--glossary-ignore-punctuation` | Enable ignore punctuation for glossary.                                                 | `pdf2zh_next example.pdf --glossary-ignore-punctuation`                                                               |
| `--glossary-ignore-whitespace`  | Enable ignore whitespace for glossary.                                                  | `pdf2zh_next example.pdf --glossary-ignore-whitespace`                                                                |
| `--glossary-ignore-case`        | Enable ignore case for glossary.                                                        | `pdf2zh_next example.pdf --glossary-ignore-case`                                                                      |
| `--glossary-format`             | Glossary format.                                                                        | `pdf2zh_next example.pdf --glossary-format "csv"`                                                                     |
| `--glossary-encoding`           | Glossary encoding.                                                                      | `pdf2zh_next example.pdf --glossary-encoding "utf-8"`                                                                 |
| `--glossary-separator`          | Glossary separator.                                                                     | `pdf2zh_next example.pdf --glossary-separator ","`                                                                    |
| `--glossary-quotechar`          | Glossary quotechar.                                                                     | `pdf2zh_next example.pdf --glossary-quotechar "\""`                                                                   |
| `--glossary-skip-lines`         | How many lines to skip in the glossary file.                                            | `pdf2zh_next example.pdf --glossary-skip-lines 1`                                                                     |
| `--glossary-fields`             | Which fields to use in the glossary file.                                               | `pdf2zh_next example.pdf --glossary-fields "0,1"`                                                                     |
| `--glossary-source-field`       | Which field is the source text in the glossary file.                                    | `pdf2zh_next example.pdf --glossary-source-field 0`                                                                   |
| `--glossary-target-field`       | Which field is the target text in the glossary file.                                    | `pdf2zh_next example.pdf --glossary-target-field 1`                                                                   |
| `--glossary-comment-prefix`     | Lines starting with this string will be treated as comments and ignored in glossary file | `pdf2zh_next example.pdf --glossary-comment-prefix "#"`                                                               |

---

### TRANSLATION RESULT

| `--glossaries`                  | 術語表文件列表。                                                                        | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-fallback`           | 啟用術語表後備機制。                                                                    | `pdf2zh_next example.pdf --glossary-fallback`                                                                         |
| `--glossary-case-sensitive`     | 啟用術語表大小寫敏感。                                                                  | `pdf2zh_next example.pdf --glossary-case-sensitive`                                                                   |
| `--glossary-full-match`         | 啟用術語表完全匹配。                                                                    | `pdf2zh_next example.pdf --glossary-full-match`                                                                       |
| `--glossary-partial-match`      | 啟用術語表部分匹配。                                                                    | `pdf2zh_next example.pdf --glossary-partial-match`                                                                    |
| `--glossary-match-boundary`     | 啟用術語表邊界匹配。                                                                    | `pdf2zh_next example.pdf --glossary-match-boundary`                                                                   |
| `--glossary-ignore-punctuation` | 啟用術語表忽略標點符號。                                                                | `pdf2zh_next example.pdf --glossary-ignore-punctuation`                                                               |
| `--glossary-ignore-whitespace`  | 啟用術語表忽略空白字符。                                                                | `pdf2zh_next example.pdf --glossary-ignore-whitespace`                                                                |
| `--glossary-ignore-case`        | 啟用術語表忽略大小寫。                                                                  | `pdf2zh_next example.pdf --glossary-ignore-case`                                                                      |
| `--glossary-format`             | 術語表格式。                                                                            | `pdf2zh_next example.pdf --glossary-format "csv"`                                                                     |
| `--glossary-encoding`           | 術語表編碼。                                                                            | `pdf2zh_next example.pdf --glossary-encoding "utf-8"`                                                                 |
| `--glossary-separator`          | 術語表分隔符。                                                                          | `pdf2zh_next example.pdf --glossary-separator ","`                                                                    |
| `--glossary-quotechar`          | 術語表引用符。                                                                          | `pdf2zh_next example.pdf --glossary-quotechar "\""`                                                                   |
| `--glossary-skip-lines`         | 在術語表文件中跳過的行數。                                                              | `pdf2zh_next example.pdf --glossary-skip-lines 1`                                                                     |
| `--glossary-fields`             | 在術語表文件中使用的字段。                                                              | `pdf2zh_next example.pdf --glossary-fields "0,1"`                                                                     |
| `--glossary-source-field`       | 術語表文件中源文本的字段。                                                              | `pdf2zh_next example.pdf --glossary-source-field 0`                                                                   |
| `--glossary-target-field`       | 術語表文件中目標文本的字段。                                                            | `pdf2zh_next example.pdf --glossary-target-field 1`                                                                   |
| `--glossary-comment-prefix`     | 在術語表文件中，以該字符串開頭的行將被視為註釋並忽略。                                  | `pdf2zh_next example.pdf --glossary-comment-prefix "#"`                                                               |
`./example.pdf.glossary.json`                                                                                          |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `--use-glossary`                | use glossary to improve translation quality                                             | `pdf2zh_next example.pdf --use-glossary ./example.glossary.json`                                                      |                                                                                                                        |
| `--save-auto-extracted-glossary-path` | specify the path to save the automatically extracted glossary                          | `pdf2zh_next example.pdf --save-auto-extracted-glossary --save-auto-extracted-glossary-path ./my-glossary.json`       | `./my-glossary.json`                                                                                                   |
| `--save-glossary-template`      | save a glossary template for user to fill in                                            | `pdf2zh_next example.pdf --save-glossary-template`                                                                    | `./example.pdf.glossary.template.json`                                                                                 |
| `--save-glossary-template-path` | specify the path to save the glossary template                                          | `pdf2zh_next example.pdf --save-glossary-template --save-glossary-template-path ./my-glossary-template.json`           | `./my-glossary-template.json`                                                                                          |

---

### OUTPUT

| `--save-auto-extracted-glossary`| 保存自動提取的詞彙表                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              | `./example.pdf.glossary.json`                                                                                          |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| `--use-glossary`                | 使用詞彙表提高翻譯質量                                             | `pdf2zh_next example.pdf --use-glossary ./example.glossary.json`                                                      |                                                                                                                        |
| `--save-auto-extracted-glossary-path` | 指定保存自動提取詞彙表的路徑                          | `pdf2zh_next example.pdf --save-auto-extracted-glossary --save-auto-extracted-glossary-path ./my-glossary.json`       | `./my-glossary.json`                                                                                                   |
| `--save-glossary-template`      | 保存一個詞彙表模板供用戶填寫                                            | `pdf2zh_next example.pdf --save-glossary-template`                                                                    | `./example.pdf.glossary.template.json`                                                                                 |
| `--save-glossary-template-path` | 指定保存詞彙表模板的路徑                                          | `pdf2zh_next example.pdf --save-glossary-template --save-glossary-template-path ./my-glossary-template.json`           | `./my-glossary-template.json`                                                                                          |
|---------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `--pool-max-workers-per-service` | Maximum number of workers for translation pool per service. If not set, will use qps as the number of workers | `pdf2zh_next example.pdf --pool-max-workers-per-service 100`                                               |
| `--pool-max-qps`                | Maximum qps for translation pool. If not set, will use the default value 100                      | `pdf2zh_next example.pdf --pool-max-qps 100`                                                               |
| `--pool-max-qps-per-service`    | Maximum qps for translation pool per service. If not set, will use the default value 100          | `pdf2zh_next example.pdf --pool-max-qps-per-service 100`                                                   |
| `--pool-max-queue-size`         | Maximum queue size for translation pool. If not set, will use the default value 1000              | `pdf2zh_next example.pdf --pool-max-queue-size 1000`                                                       |

---

### OUTPUT

| `--pool-max-workers`            | 翻譯池的最大工作進程數。如果未設置，將使用 qps 作為工作進程數 | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
|---------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| `--pool-max-workers-per-service` | 每個服務的翻譯池最大工作進程數。如果未設置，將使用 qps 作為工作進程數 | `pdf2zh_next example.pdf --pool-max-workers-per-service 100`                                               |
| `--pool-max-qps`                | 翻譯池的最大 qps。如果未設置，將使用默認值 100                      | `pdf2zh_next example.pdf --pool-max-qps 100`                                                               |
| `--pool-max-qps-per-service`    | 每個服務的翻譯池最大 qps。如果未設置，將使用默認值 100          | `pdf2zh_next example.pdf --pool-max-qps-per-service 100`                                                   |
| `--pool-max-queue-size`         | 翻譯池的最大隊列大小。如果未設置，將使用默認值 1000              | `pdf2zh_next example.pdf --pool-max-queue-size 1000`                                                       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-t, --term_service`            | Term extraction translation service. If not set, it will use the same service as `--service`. | `pdf2zh_next example.pdf -t aliyun`                                                                                   |
| `--term_lang`                   | Term extraction language code. If not set, it will use the same as `--lang`.            | `pdf2zh_next example.pdf --term_lang en`                                                                              |
| `--term_glossary`               | Term extraction glossary. If not set, it will use the same as `--glossary`.             | `pdf2zh_next example.pdf --term_glossary example_glossary.txt`                                                        |

---

### TRANSLATION RESULT

| `--term-qps`                    | 術語抽取翻譯服務的 QPS 限制。如果未設置，將遵循 qps。         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-t, --term_service`            | 術語抽取翻譯服務。如果未設置，將使用與 `--service` 相同的服務。 | `pdf2zh_next example.pdf -t aliyun`                                                                                   |
| `--term_lang`                   | 術語抽取語言代碼。如果未設置，將使用與 `--lang` 相同的代碼。            | `pdf2zh_next example.pdf --term_lang en`                                                                              |
| `--term_glossary`               | 術語抽取詞彙表。如果未設置，將使用與 `--glossary` 相同的詞彙表。             | `pdf2zh_next example.pdf --term_glossary example_glossary.txt`                                                        |
---

### OUTPUT

| `--term-pool-max-workers`       | 術語提取翻譯池的最大工作進程數。如果未設置或為 0，將遵循 pool_max_workers。 | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--auto-extract-glossary`       | Enable auto extract glossary (default)                                                  | `pdf2zh_next example.pdf --auto-extract-glossary`                                                                     |
| `--glossary <path_to_glossary>` | Specify a glossary file to use                                                          | `pdf2zh_next example.pdf --glossary ./my-glossary.txt`                                                                |
| `--glossary-offset <number>`    | Set the offset for glossary extraction. This option only works when auto extract is on. | `pdf2zh_next example.pdf --glossary-offset 100`                                                                       |
| `--glossary-limit <number>`     | Set the limit for glossary extraction. This option only works when auto extract is on.  | `pdf2zh_next example.pdf --glossary-limit 100`                                                                        |
| `--no-glossary`                 | Disable glossary usage                                                                  | `pdf2zh_next example.pdf --no-glossary`                                                                               |
| `--glossary`                    | Enable glossary usage (default)                                                         | `pdf2zh_next example.pdf --glossary`                                                                                  |
| `--glossary-threshold <number>` | Set the threshold for glossary extraction. This option only works when auto extract is on. | `pdf2zh_next example.pdf --glossary-threshold 0.5`                                                                  |

---

### TRANSLATION RESULT

| `--no-auto-extract-glossary`    | 禁用自動提取詞彙表                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--auto-extract-glossary`       | 啟用自動提取詞彙表（預設）                                                  | `pdf2zh_next example.pdf --auto-extract-glossary`                                                                     |
| `--glossary <path_to_glossary>` | 指定要使用的詞彙表文件                                                          | `pdf2zh_next example.pdf --glossary ./my-glossary.txt`                                                                |
| `--glossary-offset <number>`    | 設置詞彙表提取的偏移量。此選項僅在啟用自動提取時有效。 | `pdf2zh_next example.pdf --glossary-offset 100`                                                                       |
| `--glossary-limit <number>`     | 設置詞彙表提取的限制數量。此選項僅在啟用自動提取時有效。  | `pdf2zh_next example.pdf --glossary-limit 100`                                                                        |
| `--no-glossary`                 | 禁用詞彙表使用                                                                  | `pdf2zh_next example.pdf --no-glossary`                                                                               |
| `--glossary`                    | 啟用詞彙表使用（預設）                                                         | `pdf2zh_next example.pdf --glossary`                                                                                  |
| `--glossary-threshold <number>` | 設置詞彙表提取的閾值。此選項僅在啟用自動提取時有效。 | `pdf2zh_next example.pdf --glossary-threshold 0.5`                                                                  |

| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-image`                    | Do not translate images                                                                 | `pdf2zh_next example.pdf --no-image`                                                                                  |
| `--no-text`                     | Do not translate text                                                                   | `pdf2zh_next example.pdf --no-text`                                                                                   |
| `--only-translate`              | Only translate the specified pages                                                      | `pdf2zh_next example.pdf --only-translate 1-5,10`                                                                     |
| `--only-ocr`                    | Only OCR the specified pages                                                            | `pdf2zh_next example.pdf --only-ocr 1-5,10`                                                                           |
| `--only-format`                 | Only format the specified pages                                                         | `pdf2zh_next example.pdf --only-format 1-5,10`                                                                        |
| `--only-extract`                | Only extract the specified pages                                                        | `pdf2zh_next example.pdf --only-extract 1-5,10`                                                                       |
| `--only-translate-ocr`          | Only translate and OCR the specified pages                                              | `pdf2zh_next example.pdf --only-translate-ocr 1-5,10`                                                                 |
| `--only-translate-format`       | Only translate and format the specified pages                                           | `pdf2zh_next example.pdf --only-translate-format 1-5,10`                                                              |
| `--only-ocr-format`             | Only OCR and format the specified pages                                                 | `pdf2zh_next example.pdf --only-ocr-format 1-5,10`                                                                    |
| `--only-translate-ocr-format`   | Only translate, OCR and format the specified pages                                      | `pdf2zh_next example.pdf --only-translate-ocr-format 1-5,10`                                                          |
| `--no-translate`                | Do not translate the specified pages                                                    | `pdf2zh_next example.pdf --no-translate 1-5,10`                                                                       |
| `--no-ocr`                      | Do not OCR the specified pages                                                          | `pdf2zh_next example.pdf --no-ocr 1-5,10`                                                                             |
| `--no-format`                   | Do not format the specified pages                                                       | `pdf2zh_next example.pdf --no-format 1-5,10`                                                                          |
| `--no-extract`                  | Do not extract the specified pages                                                      | `pdf2zh_next example.pdf --no-extract 1-5,10`                                                                         |
| `--no-translate-ocr`            | Do not translate and OCR the specified pages                                            | `pdf2zh_next example.pdf --no-translate-ocr 1-5,10`                                                                   |
| `--no-translate-format`         | Do not translate and format the specified pages                                         | `pdf2zh_next example.pdf --no-translate-format 1-5,10`                                                                |
| `--no-ocr-format`               | Do not OCR and format the specified pages                                               | `pdf2zh_next example.pdf --no-ocr-format 1-5,10`                                                                      |
| `--no-translate-ocr-format`     | Do not translate, OCR and format the specified pages                                    | `pdf2zh_next example.pdf --no-translate-ocr-format 1-5,10`                                                            |
| `--no-translate-ocr-format-all` | Do not translate, OCR and format all pages                                              | `pdf2zh_next example.pdf --no-translate-ocr-format-all`                                                               |
| `--no-translate-ocr-all`        | Do not translate and OCR all pages                                                      | `pdf2zh_next example.pdf --no-translate-ocr-all`                                                                      |
| `--no-translate-format-all`     | Do not translate and format all pages                                                   | `pdf2zh_next example.pdf --no-translate-format-all`                                                                   |
| `--no-ocr-format-all`           | Do not OCR and format all pages                                                         | `pdf2zh_next example.pdf --no-ocr-format-all`                                                                         |
| `--no-translate-all`            | Do not translate all pages                                                              | `pdf2zh_next example.pdf --no-translate-all`                                                                          |
| `--no-ocr-all`                  | Do not OCR all pages                                                                    | `pdf2zh_next example.pdf --no-ocr-all`                                                                                |
| `--no-format-all`               | Do not format all pages                                                                 | `pdf2zh_next example.pdf --no-format-all`                                                                             |
| `--no-extract-all`              | Do not extract all pages                                                                | `pdf2zh_next example.pdf --no-extract-all`                                                                            |

---

### OUTPUT

| `--no-dual`                     | 不輸出雙語 `PDF` 文件                                                             | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-image`                    | 不翻譯圖片                                                                        | `pdf2zh_next example.pdf --no-image`                                                                                  |
| `--no-text`                     | 不翻譯文字                                                                        | `pdf2zh_next example.pdf --no-text`                                                                                   |
| `--only-translate`              | 僅翻譯指定的頁面                                                                  | `pdf2zh_next example.pdf --only-translate 1-5,10`                                                                     |
| `--only-ocr`                    | 僅對指定的頁面進行 `OCR`                                                           | `pdf2zh_next example.pdf --only-ocr 1-5,10`                                                                           |
| `--only-format`                 | 僅格式化指定的頁面                                                                | `pdf2zh_next example.pdf --only-format 1-5,10`                                                                        |
| `--only-extract`                | 僅提取指定的頁面                                                                  | `pdf2zh_next example.pdf --only-extract 1-5,10`                                                                       |
| `--only-translate-ocr`          | 僅翻譯和對指定的頁面進行 `OCR`                                                     | `pdf2zh_next example.pdf --only-translate-ocr 1-5,10`                                                                 |
| `--only-translate-format`       | 僅翻譯和格式化指定的頁面                                                          | `pdf2zh_next example.pdf --only-translate-format 1-5,10`                                                              |
| `--only-ocr-format`             | 僅對指定的頁面進行 `OCR` 和格式化                                                  | `pdf2zh_next example.pdf --only-ocr-format 1-5,10`                                                                    |
| `--only-translate-ocr-format`   | 僅翻譯、對指定的頁面進行 `OCR` 和格式化                                            | `pdf2zh_next example.pdf --only-translate-ocr-format 1-5,10`                                                          |
| `--no-translate`                | 不翻譯指定的頁面                                                                  | `pdf2zh_next example.pdf --no-translate 1-5,10`                                                                       |
| `--no-ocr`                      | 不對指定的頁面進行 `OCR`                                                           | `pdf2zh_next example.pdf --no-ocr 1-5,10`                                                                             |
| `--no-format`                   | 不格式化指定的頁面                                                                | `pdf2zh_next example.pdf --no-format 1-5,10`                                                                          |
| `--no-extract`                  | 不提取指定的頁面                                                                  | `pdf2zh_next example.pdf --no-extract 1-5,10`                                                                         |
| `--no-translate-ocr`            | 不翻譯和對指定的頁面進行 `OCR`                                                     | `pdf2zh_next example.pdf --no-translate-ocr 1-5,10`                                                                   |
| `--no-translate-format`         | 不翻譯和格式化指定的頁面                                                          | `pdf2zh_next example.pdf --no-translate-format 1-5,10`                                                                |
| `--no-ocr-format`               | 不對指定的頁面進行 `OCR` 和格式化                                                  | `pdf2zh_next example.pdf --no-ocr-format 1-5,10`                                                                      |
| `--no-translate-ocr-format`     | 不翻譯、對指定的頁面進行 `OCR` 和格式化                                            | `pdf2zh_next example.pdf --no-translate-ocr-format 1-5,10`                                                            |
| `--no-translate-ocr-format-all` | 不翻譯、對所有頁面進行 `OCR` 和格式化                                              | `pdf2zh_next example.pdf --no-translate-ocr-format-all`                                                               |
| `--no-translate-ocr-all`        | 不翻譯和對所有頁面進行 `OCR`                                                       | `pdf2zh_next example.pdf --no-translate-ocr-all`                                                                      |
| `--no-translate-format-all`     | 不翻譯和格式化所有頁面                                                            | `pdf2zh_next example.pdf --no-translate-format-all`                                                                   |
| `--no-ocr-format-all`           | 不對所有頁面進行 `OCR` 和格式化                                                    | `pdf2zh_next example.pdf --no-ocr-format-all`                                                                         |
| `--no-translate-all`            | 不翻譯所有頁面                                                                    | `pdf2zh_next example.pdf --no-translate-all`                                                                          |
| `--no-ocr-all`                  | 不對所有頁面進行 `OCR`                                                             | `pdf2zh_next example.pdf --no-ocr-all`                                                                                |
| `--no-format-all`               | 不格式化所有頁面                                                                  | `pdf2zh_next example.pdf --no-format-all`                                                                             |
| `--no-extract-all`              | 不提取所有頁面                                                                    | `pdf2zh_next example.pdf --no-extract-all`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-mono-pdf`                 | Same as `--no-mono`                                                                     | `pdf2zh_next example.pdf --no-mono-pdf`                                                                               |
| `-s`, `--skip`                  | Skip the files that have already been translated                                        | `pdf2zh_next example.pdf -s`                                                                                          |
| `--skip-translated`             | Same as `--skip`                                                                        | `pdf2zh_next example.pdf --skip-translated`                                                                           |
| `-d`, `--debug`                 | Enable debug mode                                                                        | `pdf2zh_next example.pdf -d`                                                                                          |
| `--debug-mode`                  | Same as `--debug`                                                                       | `pdf2zh_next example.pdf --debug-mode`                                                                               |
| `-v`, `--version`               | Show the version of the program                                                         | `pdf2zh_next -v`                                                                                                      |
| `--version-info`                | Same as `--version`                                                                     | `pdf2zh_next --version-info`                                                                                          |

---

### OUTPUT

| `--no-mono`                     | 不輸出單語種 PDF 文件                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-mono-pdf`                 | 同 `--no-mono`                                                                     | `pdf2zh_next example.pdf --no-mono-pdf`                                                                               |
| `-s`, `--skip`                  | 跳過已經翻譯的文件                                        | `pdf2zh_next example.pdf -s`                                                                                          |
| `--skip-translated`             | 同 `--skip`                                                                        | `pdf2zh_next example.pdf --skip-translated`                                                                           |
| `-d`, `--debug`                 | 啟用調試模式                                                                        | `pdf2zh_next example.pdf -d`                                                                                          |
| `--debug-mode`                  | 同 `--debug`                                                                       | `pdf2zh_next example.pdf --debug-mode`                                                                               |
| `-v`, `--version`               | 顯示程序版本                                                         | `pdf2zh_next -v`                                                                                                      |
| `--version-info`                | 同 `--version`                                                                     | `pdf2zh_next --version-info`                                                                                          |
|
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--|
| `--formular-font-size-threshold`| Font size threshold to identify formula text. Default: `0`                              | `pdf2zh_next example.pdf --formular-font-size-threshold 13`                                                           |  |
| `--formular-font-size-ratio`    | Font size ratio to identify formula text. Default: `0.8`                                | `pdf2zh_next example.pdf --formular-font-size-ratio 0.9`                                                              |  |
| `--formular-font-color`         | Font color to identify formula text. Default: `#000000`                                 | `pdf2zh_next example.pdf --formular-font-color "#000000"`                                                             |  |
| `--formular-font-color-tolerance` | Tolerance for font color to identify formula text. Default: `0`                         | `pdf2zh_next example.pdf --formular-font-color-tolerance 0`                                                           |  |
| `--formular-font-style`         | Font style to identify formula text. Default: `normal`                                  | `pdf2zh_next example.pdf --formular-font-style "normal"`                                                              |  |
| `--formular-font-weight`        | Font weight to identify formula text. Default: `normal`                                 | `pdf2zh_next example.pdf --formular-font-weight "normal"`                                                             |  |
| `--formular-font-family`        | Font family to identify formula text. Default: `null`                                   | `pdf2zh_next example.pdf --formular-font-family "Arial"`                                                              |  |
| `--formular-font-family-pattern`| Font family pattern to identify formula text. Default: `null`                           | `pdf2zh_next example.pdf --formular-font-family-pattern "(Arial.*)"`                                                  |  |
| `--formular-font-family-exclude`| Font family exclude pattern to identify formula text. Default: `null`                   | `pdf2zh_next example.pdf --formular-font-family-exclude "(Arial.*)"`                                                  |  |
| `--formular-font-family-exclude-pattern` | Font family exclude pattern to identify formula text. Default: `null`             | `pdf2zh_next example.pdf --formular-font-family-exclude-pattern "(Arial.*)"`                                          |  |
| `--formular-font-family-include`| Font family include pattern to identify formula text. Default: `null`                   | `pdf2zh_next example.pdf --formular-font-family-include "(Arial.*)"`                                                  |  |
| `--formular-font-family-include-pattern` | Font family include pattern to identify formula text. Default: `null`             | `pdf2zh_next example.pdf --formular-font-family-include-pattern "(Arial.*)"`                                          |  |
| `--formular-font-family-exclude-list` | Font family exclude list to identify formula text. Default: `[]`                  | `pdf2zh_next example.pdf --formular-font-family-exclude-list "Arial" "Times"`                                         |  |
| `--formular-font-family-include-list` | Font family include list to identify formula text. Default: `[]`                  | `pdf2zh_next example.pdf --formular-font-family-include-list "Arial" "Times"`                                         |  |
| `--formular-font-family-exclude-file` | Font family exclude file to identify formula text. Default: `null`                | `pdf2zh_next example.pdf --formular-font-family-exclude-file "exclude.txt"`                                           |  |
| `--formular-font-family-include-file` | Font family include file to identify formula text. Default: `null`                | `pdf2zh_next example.pdf --formular-font-family-include-file "include.txt"`                                           |  |
| `--formular-font-family-exclude-file-pattern` | Font family exclude file pattern to identify formula text. Default: `null` | `pdf2zh_next example.pdf --formular-font-family-exclude-file-pattern "exclude.txt"`                                   |  |
| `--formular-font-family-include-file-pattern` | Font family include file pattern to identify formula text. Default: `null` | `pdf2zh_next example.pdf --formular-font-family-include-file-pattern "include.txt"`                                   |  |
| `--formular-font-family-exclude-file-list` | Font family exclude file list to identify formula text. Default: `[]`      | `pdf2zh_next example.pdf --formular-font-family-exclude-file-list "exclude.txt" "exclude2.txt"`                       |  |
| `--formular-font-family-include-file-list` | Font family include file list to identify formula text. Default: `[]`      | `pdf2zh_next example.pdf --formular-font-family-include-file-list "include.txt" "include2.txt"`                       |  |
| `--formular-font-family-exclude-file-file` | Font family exclude file file to identify formula text. Default: `null`    | `pdf2zh_next example.pdf --formular-font-family-exclude-file-file "exclude.txt"`                                      |  |
| `--formular-font-family-include-file-file` | Font family include file file to identify formula text. Default: `null`    | `pdf2zh_next example.pdf --formular-font-family-include-file-file "include.txt"`                                      |  |
| `--formular-font-family-exclude-file-file-pattern` | Font family exclude file file pattern to identify formula text. Default: `null` | `pdf2zh_next example.pdf --formular-font-family-exclude-file-file-pattern "exclude.txt"`                              |  |
| `--formular-font-family-include-file-file-pattern` | Font family include file file pattern to identify formula text. Default: `null` | `pdf2zh_next example.pdf --formular-font-family-include-file-file-pattern "include.txt"`                              |  |
| `--formular-font-family-exclude-file-file-list` | Font family exclude file file list to identify formula text. Default: `[]` | `pdf2zh_next example.pdf --formular-font-family-exclude-file-file-list "exclude.txt" "exclude2.txt"`                  |  |
| `--formular-font-family-include-file-file-list` | Font family include file file list to identify formula text. Default: `[]` | `pdf2zh_next example.pdf --formular-font-family-include-file-file-list "include.txt" "include2.txt"`                  |  |

---

### TRANSLATION RESULT

| `--formular-font-pattern`       | 用於識別公式文字的字體模式                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--|
| `--formular-font-size-threshold`| 用於識別公式文字的字體大小閾值。預設值：`0`                              | `pdf2zh_next example.pdf --formular-font-size-threshold 13`                                                           |  |
| `--formular-font-size-ratio`    | 用於識別公式文字的字體大小比例。預設值：`0.8`                                | `pdf2zh_next example.pdf --formular-font-size-ratio 0.9`                                                              |  |
| `--formular-font-color`         | 用於識別公式文字的字體顏色。預設值：`#000000`                                 | `pdf2zh_next example.pdf --formular-font-color "#000000"`                                                             |  |
| `--formular-font-color-tolerance` | 用於識別公式文字的字體顏色容差。預設值：`0`                         | `pdf2zh_next example.pdf --formular-font-color-tolerance 0`                                                           |  |
| `--formular-font-style`         | 用於識別公式文字的字體樣式。預設值：`normal`                                  | `pdf2zh_next example.pdf --formular-font-style "normal"`                                                              |  |
| `--formular-font-weight`        | 用於識別公式文字的字體粗細。預設值：`normal`                                 | `pdf2zh_next example.pdf --formular-font-weight "normal"`                                                             |  |
| `--formular-font-family`        | 用於識別公式文字的字體系列。預設值：`null`                                   | `pdf2zh_next example.pdf --formular-font-family "Arial"`                                                              |  |
| `--formular-font-family-pattern`| 用於識別公式文字的字體系列模式。預設值：`null`                           | `pdf2zh_next example.pdf --formular-font-family-pattern "(Arial.*)"`                                                  |  |
| `--formular-font-family-exclude`| 用於識別公式文字的字體系列排除模式。預設值：`null`                   | `pdf2zh_next example.pdf --formular-font-family-exclude "(
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-replacement`   | Replacement string for formula text                                                     | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replacement "**$1**"`                        |
| `--formular-pattern`            | Pattern to identify formula regions                                                      | `pdf2zh_next example.pdf --formular-pattern "(?s)(?<=\\n)(\\$\\$.*?\\$\\$)(?=\\n)"`                                    |
| `--formular-replacement`        | Replacement string for formula regions                                                   | `pdf2zh_next example.pdf --formular-pattern "(?s)(?<=\\n)(\\$\\$.*?\\$\\$)(?=\\n)" --formular-replacement "\n```math\n$1\n```\n"` |
| `--formular-remove-pattern`     | Pattern to remove from formula regions                                                   | `pdf2zh_next example.pdf --formular-remove-pattern "\\\\begin\\{align\\*\\}"`                                          |
| `--formular-remove-replacement` | Replacement string for removal patterns (usually empty)                                 | `pdf2zh_next example.pdf --formular-remove-pattern "\\\\begin\\{align\\*\\}" --formular-remove-replacement ""`         |

---

### TRANSLATION RESULT

| `--formular-char-pattern`       | 用於識別公式文本的字符模式                                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-replacement`   | 公式文本的替換字符串                                                                    | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replacement "**$1**"`                        |
| `--formular-pattern`            | 用於識別公式區域的模式                                                                  | `pdf2zh_next example.pdf --formular-pattern "(?s)(?<=\\n)(\\$\\$.*?\\$\\$)(?=\\n)"`                                    |
| `--formular-replacement`        | 公式區域的替換字符串                                                                    | `pdf2zh_next example.pdf --formular-pattern "(?s)(?<=\\n)(\\$\\$.*?\\$\\$)(?=\\n)" --formular-replacement "\n```math\n$1\n```\n"` |
| `--formular-remove-pattern`     | 要從公式區域中移除的模式                                                                | `pdf2zh_next example.pdf --formular-remove-pattern "\\\\begin\\{align\\*\\}"`                                          |
| `--formular-remove-replacement` | 用於移除模式的替換字符串（通常為空）                                                    | `pdf2zh_next example.pdf --formular-remove-pattern "\\\\begin\\{align\\*\\}" --formular-remove-replacement ""`         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | Threshold for splitting short lines (default: `0.5`)                                    | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-threshold 0.3`                                      |
| `--split-short-lines-min-len`   | Minimum length of a line to be considered for splitting (default: `5`)                  | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-len 10`                                         |
| `--split-short-lines-max-len`   | Maximum length of a line to be considered for splitting (default: `100`)                | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-len 50`                                         |
| `--split-short-lines-min-ratio` | Minimum ratio of line length to page width for splitting (default: `0.1`)               | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-ratio 0.2`                                      |
| `--split-short-lines-max-ratio` | Maximum ratio of line length to page width for splitting (default: `0.9`)               | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-ratio 0.8`                                      |
| `--split-short-lines-min-gap`   | Minimum gap between lines to be considered for splitting (default: `0.1`)              | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-gap 0.2`                                        |
| `--split-short-lines-max-gap`   | Maximum gap between lines to be considered for splitting (default: `0.9`)              | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-gap 0.8`                                        |
| `--split-short-lines-min-overlap` | Minimum overlap between lines to be considered for splitting (default: `0.1`)         | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-overlap 0.2`                                    |
| `--split-short-lines-max-overlap` | Maximum overlap between lines to be considered for splitting (default: `0.9`)         | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-overlap 0.8`                                    |

---

### OUTPUT

| `--split-short-lines`           | 強制將短行拆分為不同段落                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | 拆分短行的閾值（預設值：`0.5`）                                    | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-threshold 0.3`                                      |
| `--split-short-lines-min-len`   | 要考慮拆分的最小行長度（預設值：`5`）                  | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-len 10`                                         |
| `--split-short-lines-max-len`   | 要考慮拆分的最大行長度（預設值：`100`）                | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-len 50`                                         |
| `--split-short-lines-min-ratio` | 要考慮拆分的行長與頁面寬度的最小比例（預設值：`0.1`）               | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-ratio 0.2`                                      |
| `--split-short-lines-max-ratio` | 要考慮拆分的行長與頁面寬度的最大比例（預設值：`0.9`）               | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-ratio 0.8`                                      |
| `--split-short-lines-min-gap`   | 要考慮拆分的行間最小間距（預設值：`0.1`）              | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-gap 0.2`                                        |
| `--split-short-lines-max-gap`   | 要考慮拆分的行間最大間距（預設值：`0.9`）              | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-gap 0.8`                                        |
| `--split-short-lines-min-overlap` | 要考慮拆分的行間最小重疊（預設值：`0.1`）         | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-min-overlap 0.2`                                    |
| `--split-short-lines-max-overlap` | 要考慮拆分的行間最大重疊（預設值：`0.9`）         | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-max-overlap 0.8`                                    |

| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-ocr`                    | Skip OCR step                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-format`                 | Skip format step                                                                        | `pdf2zh_next example.pdf --skip-format`                                                                               |
| `--skip-html`                   | Skip HTML generation step                                                               | `pdf2zh_next example.pdf --skip-html`                                                                                 |
| `--skip-pdf`                    | Skip PDF generation step                                                                | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--no-clean`                    | Same as `--skip-clean`                                                                  | `pdf2zh_next example.pdf --no-clean`                                                                                  |
| `--no-ocr`                      | Same as `--skip-ocr`                                                                    | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--no-translate`                | Same as `--skip-translate`                                                              | `pdf2zh_next example.pdf --no-translate`                                                                              |
| `--no-format`                   | Same as `--skip-format`                                                                 | `pdf2zh_next example.pdf --no-format`                                                                                 |
| `--no-html`                     | Same as `--skip-html`                                                                   | `pdf2zh_next example.pdf --no-html`                                                                                   |
| `--no-pdf`                      | Same as `--skip-pdf`                                                                    | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--clean-only`                  | Only run PDF cleaning step                                                              | `pdf2zh_next example.pdf --clean-only`                                                                                |
| `--ocr-only`                    | Only run OCR step                                                                       | `pdf2zh_next example.pdf --ocr-only`                                                                                  |
| `--translate-only`              | Only run translation step                                                               | `pdf2zh_next example.pdf --translate-only`                                                                            |
| `--format-only`                 | Only run format step                                                                    | `pdf2zh_next example.pdf --format-only`                                                                               |
| `--html-only`                   | Only run HTML generation step                                                           | `pdf2zh_next example.pdf --html-only`                                                                                 |
| `--pdf-only`                    | Only run PDF generation step                                                            | `pdf2zh_next example.pdf --pdf-only`                                                                                  |
| `--clean-and-ocr-only`          | Only run PDF cleaning and OCR steps                                                     | `pdf2zh_next example.pdf --clean-and-ocr-only`                                                                        |
| `--ocr-and-translate-only`      | Only run OCR and translation steps                                                      | `pdf2zh_next example.pdf --ocr-and-translate-only`                                                                    |
| `--translate-and-format-only`   | Only run translation and format steps                                                   | `pdf2zh_next example.pdf --translate-and-format-only`                                                                 |
| `--format-and-html-only`        | Only run format and HTML generation steps                                               | `pdf2zh_next example.pdf --format-and-html-only`                                                                      |
| `--html-and-pdf-only`           | Only run HTML and PDF generation steps                                                  | `pdf2zh_next example.pdf --html-and-pdf-only`                                                                         |
| `--clean-ocr-translate-only`    | Only run PDF cleaning, OCR and translation steps                                        | `pdf2zh_next example.pdf --clean-ocr-translate-only`                                                                  |
| `--ocr-translate-format-only`   | Only run OCR, translation and format steps                                              | `pdf2zh_next example.pdf --ocr-translate-format-only`                                                                 |
| `--translate-format-html-only`  | Only run translation, format and HTML generation steps                                  | `pdf2zh_next example.pdf --translate-format-html-only`                                                                |
| `--format-html-pdf-only`        | Only run format, HTML and PDF generation steps                                          | `pdf2zh_next example.pdf --format-html-pdf-only`                                                                      |
| `--clean-ocr-translate-format`  | Only run PDF cleaning, OCR, translation and format steps                                | `pdf2zh_next example.pdf --clean-ocr-translate-format`                                                                |
| `--ocr-translate-format-html`   | Only run OCR, translation, format and HTML generation steps                             | `pdf2zh_next example.pdf --ocr-translate-format-html`                                                                 |
| `--translate-format-html-pdf`   | Only run translation, format, HTML and PDF generation steps                             | `pdf2zh_next example.pdf --translate-format-html-pdf`                                                                 |
| `--clean-ocr-translate-format-html` | Only run PDF cleaning, OCR, translation, format and HTML generation steps             | `pdf2zh_next example.pdf --clean-ocr-translate-format-html`                                                           |
| `--ocr-translate-format-html-pdf` | Only run OCR, translation, format, HTML and PDF generation steps                      | `pdf2zh_next example.pdf --ocr-translate-format-html-pdf`                                                             |

---

### OUTPUT

| `--skip-clean`                  | 跳過 PDF 清理步驟                                                                      | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-ocr`                    | 跳過 OCR 步驟                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-translate`              | 跳過翻譯步驟                                                                           | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-format`                 | 跳過格式調整步驟                                                                        | `pdf2zh_next example.pdf --skip-format`                                                                               |
| `--skip-html`                   | 跳過 HTML 生成步驟                                                               | `pdf2zh_next example.pdf --skip-html`                                                                                 |
| `--skip-pdf`                    | 跳過 PDF 生成步驟                                                                | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--no-clean`                    | 與 `--skip-clean` 相同                                                                  | `pdf2zh_next example.pdf --no-clean`                                                                                  |
| `--no-ocr`                      | 與 `--skip-ocr` 相同                                                                    | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--no-translate`                | 與 `--skip-translate` 相同                                                              | `pdf2zh_next example.pdf --no-translate`                                                                              |
| `--no-format`                   | 與 `--skip-format` 相同                                                                 | `pdf2zh_next example.pdf --no-format`                                                                                 |
| `--no-html`                     | 與 `--skip-html` 相同                                                                   | `pdf2zh_next example.pdf --no-html`                                                                                   |
| `--no-pdf`                      | 與 `--skip-pdf` 相同                                                                    | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--clean-only`                  | 僅執行 PDF 清理步驟                                                              | `pdf2zh_next example.pdf --clean-only`                                                                                |
| `--ocr-only`                    | 僅執行 OCR 步驟                                                                       | `pdf2zh_next example.pdf --ocr-only`                                                                                  |
| `--translate-only`              | 僅執行翻譯步驟                                                               | `pdf2zh_next example.pdf --translate-only`                                                                            |
| `--format-only`                 | 僅執行格式調整步驟                                                                    | `pdf2zh_next example.pdf --format-only`                                                                               |
| `--html-only`                   | 僅執行 HTML 生成步驟                                                           | `pdf2zh_next example.pdf --html-only`                                                                                 |
| `--pdf-only`                    | 僅執行 PDF 生成步驟                                                            | `pdf2zh_next example.pdf --pdf-only`                                                                                  |
| `--clean-and-ocr-only`          | 僅執行 PDF 清理和 OCR 步驟                                                     | `pdf2zh_next example.pdf --clean-and-ocr-only`                                                                        |
| `--ocr-and-translate-only`      | 僅執行 OCR 和翻譯步驟                                                      | `pdf2zh_next example.pdf --ocr-and-translate-only`                                                                    |
| `--translate-and-format-only`   | 僅執行翻譯和格式調整步驟                                                   | `pdf2zh_next example.pdf --translate-and-format-only`                                                                 |
| `--format-and-html-only`        | 僅執行格式調整和 HTML 生成步驟                                               | `pdf2zh_next example.pdf --format-and-html-only`                                                                      |
| `--html-and-pdf-only`           | 僅執行 HTML 和 PDF 生成步驟                                                  | `pdf2zh_next example.pdf --html-and-pdf-only`                                                                         |
| `--clean-ocr-translate-only`    | 僅執行 PDF 清理、OCR 和翻譯步驟                                        | `pdf2zh_next example.pdf --clean-ocr-translate-only`                                                                  |
| `--ocr-translate-format-only`   | 僅執行 OCR、翻譯和格式調整步驟                                              | `pdf2zh_next example.pdf --ocr-translate-format-only`                                                                 |
| `--translate-format-html-only`  | 僅執行翻譯、格式調整和 HTML 生成步驟                                  | `pdf2zh_next example.pdf --translate-format-html-only`                                                                |
| `--format-html-pdf-only`        | 僅執行格式調整、HTML 和 PDF 生成步驟                                          | `pdf2zh_next example.pdf --format-html-pdf-only`                                                                      |
| `--clean-ocr-translate-format`  | 僅執行 PDF 清理、OCR、翻譯和格式調整步驟                                | `pdf2zh_next example.pdf --clean-ocr-translate-format`                                                                |
| `--ocr-translate-format-html`   | 僅執行 OCR、翻譯、格式調整和 HTML 生成步驟                             | `pdf2zh_next example.pdf --ocr-translate-format-html`                                                                 |
| `--translate-format-html-pdf`   | 僅執行翻譯、格式調整、HTML 和 PDF 生成步驟                             | `pdf2zh_next example.pdf --translate-format-html-pdf`                                                                 |
| `--clean-ocr-translate-format-html` | 僅執行 PDF 清理、OCR、翻譯、格式調整和 HTML 生成步驟             | `pdf2zh_next example.pdf --clean-ocr-translate-format-html`                                                           |
| `--ocr-translate-format-html-pdf` | 僅執行 OCR、翻譯、格式調整、HTML 和 PDF 生成步驟                      | `pdf2zh_next example.pdf --ocr-translate-format-html-pdf`                                                             |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--dual-translate-first-ratio`  | Ratio of translated pages in dual PDF mode, defaults to 0.5                            | `pdf2zh_next example.pdf --dual-translate-first-ratio 0.3`                                                            |

---

### OUTPUT

| `--dual-translate-first`        | 在雙 PDF 模式下，將翻譯後的頁面放在前面                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--dual-translate-first-ratio`  | 雙 PDF 模式下翻譯頁面的比例，預設為 0.5                            | `pdf2zh_next example.pdf --dual-translate-first-ratio 0.3`                                                            |

`false`         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------- |
| `--enhance-compatibility-ocr`   | Enable OCR for images in PDFs to improve text extraction accuracy                       | `pdf2zh_next example.pdf --enhance-compatibility-ocr`                                                                 | `false`         |
| `--enhance-compatibility-merge` | Merge text blocks that are split across multiple lines to improve text extraction       | `pdf2zh_next example.pdf --enhance-compatibility-merge`                                                               | `false`         |
| `--enhance-compatibility-fonts` | Use font information to improve text extraction accuracy                                | `pdf2zh_next example.pdf --enhance-compatibility-fonts`                                                               | `false`         |

---

### OUTPUT

| `--enhance-compatibility`       | 啟用所有兼容性增強選項                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     | `false`         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------- |
| `--enhance-compatibility-ocr`   | 啟用 PDF 中圖片的 OCR 功能以提高文字提取準確度                       | `pdf2zh_next example.pdf --enhance-compatibility-ocr`                                                                 | `false`         |
| `--enhance-compatibility-merge` | 合併跨越多行的文字區塊以改善文字提取       | `pdf2zh_next example.pdf --enhance-compatibility-merge`                                                               | `false`         |
| `--enhance-compatibility-fonts` | 使用字型資訊以提高文字提取準確度                                | `pdf2zh_next example.pdf --enhance-compatibility-fonts`                                                               | `false`         |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | 
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              | 
| `--use-dual-pdf`                | Use dual PDF mode                                                                       | `pdf2zh_next example.pdf --use-dual-pdf`                                                                              | 
| `--use-single-pdf`              | Use single PDF mode                                                                     | `pdf2zh_next example.pdf --use-single-pdf`                                                                            | 
| `--use-html`                    | Use HTML mode                                                                           | `pdf2zh_next example.pdf --use-html`                                                                                  | 
| `--use-html-para`               | Use HTML mode and split by paragraph                                                    | `pdf2zh_next example.pdf --use-html-para`                                                                             | 
| `--use-html-para-translate`     | Use HTML mode, split by paragraph, and translate                                        | `pdf2zh_next example.pdf --use-html-para-translate`                                                                   | 
| `--use-html-translate`          | Use HTML mode and translate                                                             | `pdf2zh_next example.pdf --use-html-translate`                                                                        | 
| `--use-html-translate-para`     | Use HTML mode, translate, and split by paragraph                                        | `pdf2zh_next example.pdf --use-html-translate-para`                                                                   | 
| `--use-html-translate-para-doc` | Use HTML mode, translate, split by paragraph, and merge into a single document          | `pdf2zh_next example.pdf --use-html-translate-para-doc`                                                               | 
| `--use-html-translate-para-pdf` | Use HTML mode, translate, split by paragraph, and merge into a single PDF               | `pdf2zh_next example.pdf --use-html-translate-para-pdf`                                                               | 
| `--use-html-translate-para-txt` | Use HTML mode, translate, split by paragraph, and merge into a single text file         | `pdf2zh_next example.pdf --use-html-translate-para-txt`                                                               | 
| `--use-html-translate-pdf`      | Use HTML mode, translate, and merge into a single PDF                                   | `pdf2zh_next example.pdf --use-html-translate-pdf`                                                                    | 
| `--use-html-translate-txt`      | Use HTML mode, translate, and merge into a single text file                             | `pdf2zh_next example.pdf --use-html-translate-txt`                                                                    | 
| `--use-para`                    | Use paragraph mode                                                                      | `pdf2zh_next example.pdf --use-para`                                                                                  | 
| `--use-para-translate`          | Use paragraph mode and translate                                                        | `pdf2zh_next example.pdf --use-para-translate`                                                                        | 
| `--use-para-translate-doc`      | Use paragraph mode, translate, and merge into a single document                         | `pdf2zh_next example.pdf --use-para-translate-doc`                                                                    | 
| `--use-para-translate-pdf`      | Use paragraph mode, translate, and merge into a single PDF                              | `pdf2zh_next example.pdf --use-para-translate-pdf`                                                                    | 
| `--use-para-translate-txt`      | Use paragraph mode, translate, and merge into a single text file                        | `pdf2zh_next example.pdf --use-para-translate-txt`                                                                    | 
| `--use-translate`               | Use translate mode                                                                      | `pdf2zh_next example.pdf --use-translate`                                                                             | 
| `--use-translate-doc`           | Use translate mode and merge into a single document                                     | `pdf2zh_next example.pdf --use-translate-doc`                                                                         | 
| `--use-translate-pdf`           | Use translate mode and merge into a single PDF                                          | `pdf2zh_next example.pdf --use-translate-pdf`                                                                         | 
| `--use-translate-txt`           | Use translate mode and merge into a single text file                                    | `pdf2zh_next example.pdf --use-translate-txt`                                                                         | 

---

### OUTPUT

| `--use-alternating-pages-dual`  | 對雙頁 PDF 使用交替頁面模式                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                | 
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- | 
| `--use-alternating-pages-single` | 對單頁 PDF 使用交替頁面模式                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              | 
| `--use-dual-pdf`                | 使用雙頁 PDF 模式                                                                       | `pdf2zh_next example.pdf --use-dual-pdf`                                                                              | 
| `--use-single-pdf`              | 使用單頁 PDF 模式                                                                     | `pdf2zh_next example.pdf --use-single-pdf`                                                                            | 
| `--use-html`                    | 使用 HTML 模式                                                                           | `pdf2zh_next example.pdf --use-html`                                                                                  | 
| `--use-html-para`               | 使用 HTML 模式並按段落分割                                                    | `pdf2zh_next example.pdf --use-html-para`                                                                             | 
| `--use-html-para-translate`     | 使用 HTML 模式、按段落分割並翻譯                                        | `pdf2zh_next example.pdf --use-html-para-translate`                                                                   | 
| `--use-html-translate`          | 使用 HTML 模式並翻譯                                                             | `pdf2zh_next example.pdf --use-html-translate`                                                                        | 
| `--use-html-translate-para`     | 使用 HTML 模式、翻譯並按段落分割                                        | `pdf2zh_next example.pdf --use-html-translate-para`                                                                   | 
| `--use-html-translate-para-doc` | 使用 HTML 模式、翻譯、按段落分割並合併為單一文檔          | `pdf2zh_next example.pdf --use-html-translate-para-doc`                                                               | 
| `--use-html-translate-para-pdf` | 使用 HTML 模式、翻譯、按段落分割並合併為單一 PDF               | `pdf2zh_next example.pdf --use-html-translate-para-pdf`                                                               | 
| `--use-html-translate-para-txt` | 使用 HTML 模式、翻譯、按段落分割並合併為單一文字檔         | `pdf2zh_next example.pdf --use-html-translate-para-txt`                                                               | 
| `--use-html-translate-pdf`      | 使用 HTML 模式、翻譯並合併為單一 PDF                                   | `pdf2zh_next example.pdf --use-html-translate-pdf`                                                                    | 
| `--use-html-translate-txt`      | 使用 HTML 模式、翻譯並合併為單一文字檔                             | `pdf2zh_next example.pdf --use-html-translate-txt`                                                                    | 
| `--use-para`                    | 使用段落模式                                                                      | `pdf2zh_next example.pdf --use-para`                                                                                  | 
| `--use-para-translate`          | 使用段落模式並翻譯                                                        | `pdf2zh_next example.pdf --use-para-translate`                                                                        | 
| `--use-para-translate-doc`      | 使用段落模式、翻譯並合併為單一文檔                         | `pdf2zh_next example.pdf --use-para-translate-doc`                                                                    | 
| `--use-para-translate-pdf`      | 使用段落模式、翻譯並合併為單一 PDF                              | `pdf2zh_next example.pdf --use-para-translate-pdf`                                                                    | 
| `--use-para-translate-txt`      | 使用段落模式、翻譯並合併為單一文字檔                        | `pdf2zh_next example.pdf --use-para-translate-txt`                                                                    | 
| `--use-translate`               | 使用翻譯模式                                                                      | `pdf2zh_next example.pdf --use-translate`                                                                             | 
| `--use-translate-doc`           | 使用翻譯模式並合併為單一文檔                                     | `pdf2zh_next example.pdf --use-translate-doc`                                                                         | 
| `--use-translate-pdf`           | 使用翻譯模式並合併為單一 PDF                                          | `pdf2zh_next example.pdf --use-translate-pdf`                                                                         | 
| `--use-translate-txt`           | 使用翻譯模式並合併為單一文字檔                                    | `pdf2zh_next example.pdf --use-translate-txt`                                                                         |
`no_watermark` | `no_watermark`, `watermark`, `watermark_light` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------|

---

### TRANSLATED TEXT

| `--watermark-output-mode`       | PDF 檔案的水印輸出模式                                                                  | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `no_watermark` | `no_watermark`, `watermark`, `watermark_light` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------|
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-tokens-per-part`         | Maximum tokens per part for split translation                                           | `pdf2zh_next example.pdf --max-tokens-per-part 1000`                                                                  |
| `--max-characters-per-part`     | Maximum characters per part for split translation (for non-OpenAI models)               | `pdf2zh_next example.pdf --max-characters-per-part 2000`                                                              |
| `--max-workers`                 | Maximum number of concurrent workers for translation                                    | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--max-retries`                 | Maximum number of retries for failed translations                                       | `pdf2zh_next example.pdf --max-retries 3`                                                                             |
| `--request-timeout`             | Timeout in seconds for each translation request                                         | `pdf2zh_next example.pdf --request-timeout 60`                                                                        |
| `--request-interval`            | Interval in seconds between translation requests                                        | `pdf2zh_next example.pdf --request-interval 1`                                                                        |
| `--token-buffer-size`           | Buffer size for tokens to avoid exceeding limits                                        | `pdf2zh_next example.pdf --token-buffer-size 100`                                                                     |
| `--character-buffer-size`       | Buffer size for characters to avoid exceeding limits (for non-OpenAI models)            | `pdf2zh_next example.pdf --character-buffer-size 100`                                                                 |

---

### TRANSLATION

| `--max-pages-per-part`          | 拆分翻譯時每個部分的最大頁數                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-tokens-per-part`         | 拆分翻譯時每個部分的最大 token 數量                                           | `pdf2zh_next example.pdf --max-tokens-per-part 1000`                                                                  |
| `--max-characters-per-part`     | 拆分翻譯時每個部分的最大字符數（適用於非 OpenAI 模型）               | `pdf2zh_next example.pdf --max-characters-per-part 2000`                                                              |
| `--max-workers`                 | 併發翻譯的最大工作線程數                                    | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--max-retries`                 | 翻譯失敗時的最大重試次數                                       | `pdf2zh_next example.pdf --max-retries 3`                                                                             |
| `--request-timeout`             | 每個翻譯請求的超時時間（秒）                                         | `pdf2zh_next example.pdf --request-timeout 60`                                                                        |
| `--request-interval`            | 翻譯請求之間的間隔時間（秒）                                        | `pdf2zh_next example.pdf --request-interval 1`                                                                        |
| `--token-buffer-size`           | 用於避免超出限制的 token 緩衝區大小                                        | `pdf2zh_next example.pdf --token-buffer-size 100`                                                                     |
| `--character-buffer-size`       | 用於避免超出限制的字符緩衝區大小（適用於非 OpenAI 模型）            | `pdf2zh_next example.pdf --character-buffer-size 100`                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Method to translate table text, `row` or `col` (experimental)                           | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method row`                                     |
| `--translate-table-text-max`    | Maximum number of characters per cell for table text translation (experimental)         | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-max 100`                                        |
| `--translate-table-text-min`    | Minimum number of characters per cell for table text translation (experimental)         | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-min 10`                                        |
| `--translate-table-text-skip`   | Skip table text translation if the table has more than this number of rows (experimental) | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-skip 10`                                       |

---

### OUTPUT

| `--translate-table-text`        | 翻譯表格文字（實驗性功能）                                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | 翻譯表格文字的方法，`row` 或 `col`（實驗性功能）                           | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method row`                                     |
| `--translate-table-text-max`    | 表格文字翻譯時每個儲存格的最大字元數（實驗性功能）         | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-max 100`                                        |
| `--translate-table-text-min`    | 表格文字翻譯時每個儲存格的最小字元數（實驗性功能）         | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-min 10`                                        |
| `--translate-table-text-skip`   | 如果表格的行數超過此數值，則跳過表格文字翻譯（實驗性功能） | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-skip 10`                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection=true` | Skip scanned detection                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               |
| `--skip-scanned-detection=true` | Skip scanned detection                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               |
| `--skip-scanned-detection=false`| Enable scanned detection                                                                | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              |
| `--skip-scanned-detection=false`| Enable scanned detection                                                                | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              |

---

### TRANSLATION RESULT

| `--skip-scanned-detection`      | 跳過掃描檢測                                                                          | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection=true` | 跳過掃描檢測                                                                          | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               |
| `--skip-scanned-detection=true` | 跳過掃描檢測                                                                          | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               |
| `--skip-scanned-detection=false`| 啟用掃描檢測                                                                          | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              |
| `--skip-scanned-detection=false`| 啟用掃描檢測                                                                          | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              |
`false` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------|
| `--output-dir <output_dir>`     | Specify the output directory                                                           | `pdf2zh_next example.pdf --output-dir ./output`                                                                       | `./`    |
| `--output-name <output_name>`   | Specify the output filename                                                            | `pdf2zh_next example.pdf --output-name example_translated.pdf`                                                        | `null`  |
| `--overwrite`                   | Overwrite the output file if it exists                                                 | `pdf2zh_next example.pdf --overwrite`                                                                                 | `false` |
| `--page-range <page_range>`     | Specify the page range to translate, e.g. `1,3-5,7`                                    | `pdf2zh_next example.pdf --page-range 1,3-5,7`                                                                        | `null`  |
| `--proxy <proxy>`               | Specify a proxy to use for the translation service                                     | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               | `null`  |
| `--render-mode <render_mode>`   | Specify the render mode, can be `auto`, `vector`, `raster`                             | `pdf2zh_next example.pdf --render-mode raster`                                                                        | `auto`  |
| `--skip-figure`                 | Skip translating figures                                                               | `pdf2zh_next example.pdf --skip-figure`                                                                               | `false` |
| `--skip-table`                  | Skip translating tables                                                                | `pdf2zh_next example.pdf --skip-table`                                                                                | `false` |
| `--source-lang <source_lang>`   | Specify the source language                                                            | `pdf2zh_next example.pdf --source-lang en`                                                                            | `auto`  |
| `--target-lang <target_lang>`   | Specify the target language                                                            | `pdf2zh_next example.pdf --target-lang zh-CN`                                                                         | `zh-CN` |
| `--threads <threads>`           | Specify the number of threads to use                                                   | `pdf2zh_next example.pdf --threads 4`                                                                                 | `1`     |
| `--timeout <timeout>`           | Specify the timeout for each translation request in seconds                            | `pdf2zh_next example.pdf --timeout 30`                                                                                | `10`    |
| `--translation-service <service>` | Specify the translation service to use, can be `openai`, `google`, `deepl`, `youdao` | `pdf2zh_next example.pdf --translation-service google`                                                                | `openai`|
| `--translation-service-api-key <key>` | Specify the API key for the translation service                                    | `pdf2zh_next example.pdf --translation-service-api-key sk-xxxx`                                                        | `null`  |
| `--translation-service-base-url <url>` | Specify the base URL for the translation service                                   | `pdf2zh_next example.pdf --translation-service-base-url https://api.openai.com/v1`                                    | `null`  |

---

### TRANSLATION RESULT

| `--ocr-workaround`              | 強制將翻譯後的文字設為黑色並添加白色背景                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            | `false` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------|
| `--output-dir <output_dir>`     | 指定輸出目錄                                                           | `pdf2zh_next example.pdf --output-dir ./output`                                                                       | `./`    |
| `--output-name <output_name>`   | 指定輸出文件名                                                           | `pdf2zh_next example.pdf --output-name example_translated.pdf`                                                        | `null`  |
| `--overwrite`                   | 如果輸出文件已存在則覆蓋                                                 | `pdf2zh_next example.pdf --overwrite`                                                                                 | `false` |
| `--page-range <page_range>`     | 指定要翻譯的頁面範圍，例如 `1,3-5,7`                                    | `pdf2zh_next example.pdf --page-range 1,3-5,7`                                                                        | `null`  |
| `--proxy <proxy>`               | 指定用於翻譯服務的代理伺服器                                     | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               | `null`  |
| `--render-mode <render_mode>`   | 指定渲染模式，可選 `auto`、`vector`、`raster`                             | `pdf2zh_next example.pdf --render-mode raster`                                                                        | `auto`  |
| `--skip-figure`                 | 跳過翻譯圖形                                                               | `pdf2zh_next example.pdf --skip-figure`                                                                               | `false` |
| `--skip-table`                  | 跳過翻譯表格                                                                | `pdf2zh_next example.pdf --skip-table`                                                                                | `false` |
| `--source-lang <source_lang>`   | 指定源語言                                                            | `pdf2zh_next example.pdf --source-lang en`                                                                            | `auto`  |
| `--target-lang <target_lang>`   | 指定目標語言                                                            | `pdf2zh_next example.pdf --target-lang zh-CN`                                                                         | `zh-CN` |
| `--threads <threads>`           | 指定使用的執行緒數量                                                   | `pdf2zh_next example.pdf --threads 4`                                                                                 | `1`     |
| `--timeout <timeout>`           | 指定每個翻譯請求的超時時間（秒）                            | `pdf2zh_next example.pdf --timeout 30`                                                                                | `10`    |
| `--translation-service <service>` | 指定要使用的翻譯服務，可選 `openai`、`google`、`deepl`、`youdao` | `pdf2zh_next example.pdf --translation-service google`                                                                | `openai`|
| `--translation-service-api-key <key>` | 指定翻譯服務的 API 金鑰                                    | `pdf2zh_next example.pdf --translation-service-api-key sk-xxxx`                                                        | `null`  |
| `--translation-service-base-url <url>` | 指定翻譯服務的基礎 URL                                   | `pdf2zh_next example.pdf --translation-service-base-url https://api.openai.com/v1`                                    | `null`  |
---

### OUTPUT

| `--auto-enable-ocr-workaround`  | 啟用自動 OCR 解決方案。如果檢測到文檔為重度掃描，將嘗試啟用 OCR 處理並跳過後續的掃描檢測。詳情請參閱文檔。（預設：False） | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
`false`            |
|---------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------|
| `--add-original-pdf`            | Add the original PDF to the output PDF.                                               | `pdf2zh_next example.pdf --add-original-pdf`                                                                          | `false`            |
| `--split-pdf`                   | Split the PDF into single pages before translation                                    | `pdf2zh_next example.pdf --split-pdf`                                                                                 | `false`            |
| `--split-size`                  | Split the PDF into chunks of specified size (in MB) before translation                | `pdf2zh_next example.pdf --split-size 10`                                                                             | `10`               |
| `--merge-pdf`                   | Merge the translated PDFs after translation                                          | `pdf2zh_next example.pdf --merge-pdf`                                                                                 | `false`            |
| `--ocr`                         | Use OCR to extract text from the PDF                                                  | `pdf2zh_next example.pdf --ocr`                                                                                       | `false`            |
| `--ocr-language`                | Language for OCR. See [Supported Languages](#supported-languages) for more details.   | `pdf2zh_next example.pdf --ocr-language eng`                                                                          | `eng`              |
| `--ocr-engine`                  | OCR engine to use. Currently only `tesseract` is supported.                           | `pdf2zh_next example.pdf --ocr-engine tesseract`                                                                      | `tesseract`        |
| `--ocr-dpi`                     | DPI for OCR. Higher DPI may improve accuracy but will increase processing time.       | `pdf2zh_next example.pdf --ocr-dpi 300`                                                                               | `300`              |
| `--ocr-timeout`                 | Timeout for OCR in seconds.                                                           | `pdf2zh_next example.pdf --ocr-timeout 60`                                                                            | `60`               |
| `--output`                      | Output file path.                                                                     | `pdf2zh_next example.pdf --output example_zh.pdf`                                                                     | `{filename}_zh.pdf`|
| `--output-format`               | Output format. Currently only `pdf` is supported.                                     | `pdf2zh_next example.pdf --output-format pdf`                                                                         | `pdf`              |
| `--output-dir`                  | Output directory.                                                                     | `pdf2zh_next example.pdf --output-dir ./output`                                                                       | `./`               |
| `--output-prefix`               | Output file prefix.                                                                   | `pdf2zh_next example.pdf --output-prefix translated_`                                                                 | `""`               |
| `--output-suffix`               | Output file suffix.                                                                   | `pdf2zh_next example.pdf --output-suffix _zh`                                                                         | `_zh`              |
| `--log-level`                   | Log level.                                                                            | `pdf2zh_next example.pdf --log-level info`                                                                            | `info`             |
| `--log-file`                    | Log file path.                                                                        | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                        | `""`               |
| `--config`                      | Path to the configuration file.                                                       | `pdf2zh_next example.pdf --config ./config.yaml`                                                                      | `""`               |
| `--version`                     | Show version information.                                                             | `pdf2zh_next --version`                                                                                               | `false`            |
| `--help`                        | Show help message.                                                                    | `pdf2zh_next --help`                                                                                                  | `false`            |

---

### TRANSLATION

| `--only-include-translated-page` | 僅在輸出 PDF 中包含已翻譯的頁面。僅在 --pages 使用時有效。 | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page` | `false` |
|----------------------------------|-----------------------------------------------------------|---------------------------------------------------------------------|---------|
| `--add-original-pdf`             | 將原始 PDF 添加到輸出 PDF 中。                             | `pdf2zh_next example.pdf --add-original-pdf`                        | `false` |
| `--split-pdf`                    | 在翻譯前將 PDF 拆分為單頁。                                | `pdf2zh_next example.pdf --split-pdf`                               | `false` |
| `--split-size`                   | 在翻譯前將 PDF 拆分為指定大小（單位：MB）的塊。            | `pdf2zh_next example.pdf --split-size 10`                           | `10`    |
| `--merge-pdf`                    | 在翻譯後合併已翻譯的 PDF。                                 | `pdf2zh_next example.pdf --merge-pdf`                               | `false` |
| `--ocr`                          | 使用 OCR 從 PDF 中提取文字。                               | `pdf2zh_next example.pdf --ocr`                                     | `false` |
| `--ocr-language`                 | OCR 使用的語言。詳情請參閱 [支持的語言](#支持的語言)。     | `pdf2zh_next example.pdf --ocr-language eng`                        | `eng`   |
| `--ocr-engine`                   | 使用的 OCR 引擎。目前僅支持 `tesseract`。                  | `pdf2zh_next example.pdf --ocr-engine tesseract`                    | `tesseract` |
| `--ocr-dpi`                      | OCR 的 DPI。較高的 DPI 可能會提高準確性，但會增加處理時間。 | `pdf2zh_next example.pdf --ocr-dpi 300`                             | `300`   |
| `--ocr-timeout`                  | OCR 的超時時間（單位：秒）。                               | `pdf2zh_next example.pdf --ocr-timeout 60`                          | `60`    |
| `--output`                       | 輸出檔案路徑。                                             | `pdf2zh_next example.pdf --output example_zh.pdf`                   | `{filename}_zh.pdf` |
| `--output-format`                | 輸出格式。目前僅支持 `pdf`。                               | `pdf2zh_next example.pdf --output-format pdf`                       | `pdf`   |
| `--output-dir`                   | 輸出目錄。                                                 | `pdf2zh_next example.pdf --output-dir ./output`                     | `./`    |
| `--output-prefix`                | 輸出檔案前綴。                                             | `pdf2zh_next example.pdf --output-prefix translated_`               | `""`    |
| `--output-suffix`                | 輸出檔案後綴。                                             | `pdf2zh_next example.pdf --output-suffix _zh`                       | `_zh`   |
| `--log-level`                    | 日誌級別。                                                 | `pdf2zh_next example.pdf --log-level info`                          | `info`  |
| `--log-file`                     | 日誌檔案路徑。                                             | `pdf2zh_next example.pdf --log-file ./log.txt`                      | `""`    |
| `--config`                       | 設定檔案的路徑。                                           | `pdf2zh_next example.pdf --config ./config.yaml`                    | `""`    |
| `--version`                      | 顯示版本資訊。                                             | `pdf2zh_next --version`                                             | `false` |
| `--help`                         | 顯示幫助訊息。                                             | `pdf2zh_next --help`                                                | `false` |

| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-formula-lines` | 禁用移除段落區域內的非公式行                                                              | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |

---

### OUTPUT

| `--no-remove-non-formula-lines` | 禁用移除段落區域內的非公式行                                                              | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-formula-lines` | 禁用移除段落區域內的非公式行                                                              | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
`0.85`    |
| `--formula-line-iou-threshold`     | Set IoU threshold for identifying formula lines (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                           | `0.85`    |
| `--table-line-iou-threshold`       | Set IoU threshold for identifying table lines (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                             | `0.85`    |
| `--is-table-line-iou-threshold`    | Set IoU threshold for determining if a line is a table line (0.0-1.0)              | `pdf2zh_next example.pdf --is-table-line-iou-threshold 0.85`                                                          | `0.85`    |
| `--table-cell-iou-threshold`       | Set IoU threshold for identifying table cells (0.0-1.0)                            | `pdf2zh_next example.pdf --table-cell-iou-threshold 0.85`                                                             | `0.85`    |
| `--table-cell-merge-threshold`     | Set threshold for merging table cells (0.0-1.0)                                    | `pdf2zh_next example.pdf --table-cell-merge-threshold 0.85`                                                           | `0.85`    |
| `--table-cell-merge-max-height`    | Set maximum height for merging table cells (in pixels)                             | `pdf2zh_next example.pdf --table-cell-merge-max-height 50`                                                            | `20`      |

---

### OUTPUT

| `--non-formula-line-iou-threshold` | 設定用於識別非公式行的 IoU 閾值 (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.85`    |
| `--formula-line-iou-threshold`     | 設定用於識別公式行的 IoU 閾值 (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                           | `0.85`    |
| `--table-line-iou-threshold`       | 設定用於識別表格行的 IoU 閾值 (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                             | `0.85`    |
| `--is-table-line-iou-threshold`    | 設定用於判斷一行是否為表格行的 IoU 閾值 (0.0-1.0)              | `pdf2zh_next example.pdf --is-table-line-iou-threshold 0.85`                                                          | `0.85`    |
| `--table-cell-iou-threshold`       | 設定用於識別表格儲存格的 IoU 閾值 (0.0-1.0)                            | `pdf2zh_next example.pdf --table-cell-iou-threshold 0.85`                                                             | `0.85`    |
| `--table-cell-merge-threshold`     | 設定用於合併表格儲存格的閾值 (0.0-1.0)                                    | `pdf2zh_next example.pdf --table-cell-merge-threshold 0.85`                                                           | `0.85`    |
| `--table-cell-merge-max-height`    | 設定合併表格儲存格的最大高度 (像素)                             | `pdf2zh_next example.pdf --table-cell-merge-max-height 50`                                                            | `20`      |
`0.95`            |
| `--figure-table-protection-method`    | Method to protect figures and tables: "ocr" or "mask"                                                      | `pdf2zh_next example.pdf --figure-table-protection-method ocr`                                           | `ocr`             |
| `--figure-table-ocr-whitelist`        | Whitelist of characters allowed in figure/table OCR                                                        | `pdf2zh_next example.pdf --figure-table-ocr-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`           | `""` (empty)      |
| `--figure-table-ocr-blacklist`        | Blacklist of characters not allowed in figure/table OCR                                                    | `pdf2zh_next example.pdf --figure-table-ocr-blacklist "!@#$%^&*()"`                                      | `""` (empty)      |
| `--figure-table-mask-color`           | Color used to mask protected figures and tables                                                            | `pdf2zh_next example.pdf --figure-table-mask-color "#FF0000"`                                             | `"#FF0000"` (red) |

---

### OUTPUT

| `--figure-table-protection-threshold` | 設定圖表和表格的保護閾值 (0.0-1.0)。圖表/表格內的文字將不會被處理 | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        | `0.95`            |
| `--figure-table-protection-method`    | 保護圖表和表格的方法："ocr" 或 "mask"                              | `pdf2zh_next example.pdf --figure-table-protection-method ocr`                                           | `ocr`             |
| `--figure-table-ocr-whitelist`        | 圖表/表格 OCR 中允許的字元白名單                                   | `pdf2zh_next example.pdf --figure-table-ocr-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`           | `""` (空)         |
| `--figure-table-ocr-blacklist`        | 圖表/表格 OCR 中不允許的字元黑名單                                 | `pdf2zh_next example.pdf --figure-table-ocr-blacklist "!@#$%^&*()"`                                      | `""` (空)         |
| `--figure-table-mask-color`           | 用於遮罩受保護圖表和表格的顏色                                     | `pdf2zh_next example.pdf --figure-table-mask-color "#FF0000"`                                             | `"#FF0000"` (紅色) |
---

### TRANSLATION RESULT

| `--skip-formula-offset-calculation` | 在處理過程中跳過公式偏移量計算          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### 圖形界面參數

| `--server-name`                 | Specify server name                    | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--server-port`                 | Specify server port                    | `pdf2zh_next --gui --server-port 7861`          |
| `--concurrency-count`           | Number of concurrent threads           | `pdf2zh_next --gui --concurrency-count 10`      |
| `--auth`                        | Set authentication                     | `pdf2zh_next --gui --auth username:password`    |
| `--auth-message`                | Custom authentication message          | `pdf2zh_next --gui --auth-message "請輸入帳號密碼"` |
| `--ssl-keyfile`                 | Path to SSL key file                   | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | Path to SSL certificate file           | `pdf2zh_next --gui --ssl-certfile cert.pem`     |

---

### TRANSLATION RESULT

| 選項                          | 功能                               | 範例                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | 啟用分享模式                    | `pdf2zh_next --gui --share`                     |
| `--server-name`                 | 指定伺服器名稱                    | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--server-port`                 | 指定伺服器連接埠                    | `pdf2zh_next --gui --server-port 7861`          |
| `--concurrency-count`           | 並行執行緒數量           | `pdf2zh_next --gui --concurrency-count 10`      |
| `--auth`                        | 設定驗證                     | `pdf2zh_next --gui --auth username:password`    |
| `--auth-message`                | 自訂驗證訊息          | `pdf2zh_next --gui --auth-message "請輸入帳號密碼"` |
| `--ssl-keyfile`                 | SSL 金鑰檔案路徑                   | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | SSL 憑證檔案路徑           | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
Optional, default is `~/.pdf2zh/auth.json` |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ------------------------------------------ |
| `--auth-type`                   | Authentication type                    | `pdf2zh_next --gui --auth-type aliyun`          | Optional, default is `aliyun`              |
| `--auth-key`                    | Authentication key                     | `pdf2zh_next --gui --auth-key your_key`         | Optional, default is read from auth file   |
| `--auth-secret`                 | Authentication secret                  | `pdf2zh_next --gui --auth-secret your_secret`   | Optional, default is read from auth file   |
| `--auth-endpoint`               | Authentication endpoint                | `pdf2zh_next --gui --auth-endpoint your_domain` | Optional, default is read from auth file   |
| `--auth-region`                 | Authentication region                  | `pdf2zh_next --gui --auth-region your_region`   | Optional, default is read from auth file   |
| `--auth-custom-url`             | Custom authentication URL              | `pdf2zh_next --gui --auth-custom-url your_url`  | Optional, default is read from auth file   |
| `--auth-custom-method`          | Custom authentication method           | `pdf2zh_next --gui --auth-custom-method POST`   | Optional, default is read from auth file   |
| `--auth-custom-headers`         | Custom authentication headers          | `pdf2zh_next --gui --auth-custom-headers '{}'`  | Optional, default is read from auth file   |
| `--auth-custom-payload`         | Custom authentication payload          | `pdf2zh_next --gui --auth-custom-payload '{}'`  | Optional, default is read from auth file   |
| `--auth-custom-response-path`   | Custom authentication response path    | `pdf2zh_next --gui --auth-custom-response-path` | Optional, default is read from auth file   |

---

### OUTPUT

| `--auth-file`                   | 身份驗證文件的路徑                     | `pdf2zh_next --gui --auth-file /path`           | 可選，默認為 `~/.pdf2zh/auth.json`         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ------------------------------------------ |
| `--auth-type`                   | 身份驗證類型                           | `pdf2zh_next --gui --auth-type aliyun`          | 可選，默認為 `aliyun`                      |
| `--auth-key`                    | 身份驗證密鑰                           | `pdf2zh_next --gui --auth-key your_key`         | 可選，默認從身份驗證文件中讀取             |
| `--auth-secret`                 | 身份驗證密鑰                           | `pdf2zh_next --gui --auth-secret your_secret`   | 可選，默認從身份驗證文件中讀取             |
| `--auth-endpoint`               | 身份驗證端點                           | `pdf2zh_next --gui --auth-endpoint your_domain` | 可選，默認從身份驗證文件中讀取             |
| `--auth-region`                 | 身份驗證區域                           | `pdf2zh_next --gui --auth-region your_region`   | 可選，默認從身份驗證文件中讀取             |
| `--auth-custom-url`             | 自定義身份驗證 URL                     | `pdf2zh_next --gui --auth-custom-url your_url`  | 可選，默認從身份驗證文件中讀取             |
| `--auth-custom-method`          | 自定義身份驗證方法                     | `pdf2zh_next --gui --auth-custom-method POST`   | 可選，默認從身份驗證文件中讀取             |
| `--auth-custom-headers`         | 自定義身份驗證標頭                     | `pdf2zh_next --gui --auth-custom-headers '{}'`  | 可選，默認從身份驗證文件中讀取             |
| `--auth-custom-payload`         | 自定義身份驗證負載                     | `pdf2zh_next --gui --auth-custom-payload '{}'`  | 可選，默認從身份驗證文件中讀取             |
| `--auth-custom-response-path`   | 自定義身份驗證響應路徑                 | `pdf2zh_next --gui --auth-custom-response-path` | 可選，默認從身份驗證文件中讀取             |
---

### OUTPUT

| `--welcome-page`                | 歡迎頁面的 HTML 文件路徑          | `pdf2zh_next --gui --welcome-page /path`        |
Enable `Bing` and `OpenAI` service only. |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ---------------------------------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Bing"`       | Disable `Bing` service only.             |
| `--service-order`               | Service priority order                 | `pdf2zh_next --gui --service-order "OpenAI,Bing"`    | Try `OpenAI` first, then `Bing`.         |
| `--service-settings-file`       | Service settings file                  | `pdf2zh_next --gui --service-settings-file ./my.json`| Use custom service settings.             |
| `--service-config`              | Service config                         | `pdf2zh_next --gui --service-config OpenAI.apikey=sk-xxx` | Set `OpenAI` API key to `sk-xxx`.        |
| `--service-config`              | Service config                         | `pdf2zh_next --gui --service-config Aliyun.access_key_id=xxx` | Set `Aliyun` access key id to `xxx`.     |
| `--service-config`              | Service config                         | `pdf2zh_next --gui --service-config SiliconFlow.apikey=xxx` | Set `SiliconFlow` API key to `xxx`.      |

---

### RESPONSE

| `--enabled-services`            | 啟用的翻譯服務           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | 僅啟用 `Bing` 和 `OpenAI` 服務。 |
| ------------------------------- | ------------------------ | ---------------------------------------------------- | -------------------------------- |
| `--disabled-services`           | 停用的翻譯服務          | `pdf2zh_next --gui --disabled-services "Bing"`       | 僅停用 `Bing` 服務。             |
| `--service-order`               | 服務優先順序                 | `pdf2zh_next --gui --service-order "OpenAI,Bing"`    | 先嘗試 `OpenAI`，然後 `Bing`。         |
| `--service-settings-file`       | 服務設定檔                  | `pdf2zh_next --gui --service-settings-file ./my.json`| 使用自訂服務設定。             |
| `--service-config`              | 服務配置                         | `pdf2zh_next --gui --service-config OpenAI.apikey=sk-xxx` | 將 `OpenAI` API 金鑰設為 `sk-xxx`。        |
| `--service-config`              | 服務配置                         | `pdf2zh_next --gui --service-config Aliyun.access_key_id=xxx` | 將 `Aliyun` 存取金鑰 ID 設為 `xxx`。     |
| `--service-config`              | 服務配置                         | `pdf2zh_next --gui --service-config SiliconFlow.apikey=xxx` | 將 `SiliconFlow` API 金鑰設為 `xxx`。      |
Disable GUI sensitive input for the WebUI. |
|---------------------------------|----------------------------------------|---------------------------------------------------|--------------------------------------------|
| `--enable-gui-sensitive-input`  | Enable GUI sensitive input             | `pdf2zh_next --gui --enable-gui-sensitive-input`  | Enable GUI sensitive input for the WebUI.  |
| `--gui`                         | Launch WebUI                           | `pdf2zh_next --gui`                               | Launch the WebUI.                          |

---

### OUTPUT

| `--disable-gui-sensitive-input` | 禁用 GUI 敏感輸入            | `pdf2zh_next --gui --disable-gui-sensitive-input` | 為 WebUI 禁用 GUI 敏感輸入。 |
|---------------------------------|----------------------------------------|---------------------------------------------------|--------------------------------------------|
| `--enable-gui-sensitive-input`  | 啟用 GUI 敏感輸入             | `pdf2zh_next --gui --enable-gui-sensitive-input`  | 為 WebUI 啟用 GUI 敏感輸入。  |
| `--gui`                         | 啟動 WebUI                           | `pdf2zh_next --gui`                               | 啟動 WebUI。                          |
`false` |
| `--disable-ocr`                 | Disable OCR functionality               | `pdf2zh_next --disable-ocr`                     | `false` |
| `--disable-translation`         | Disable translation functionality       | `pdf2zh_next --disable-translation`             | `false` |
| `--disable-vectorization`       | Disable vectorization functionality     | `pdf2zh_next --disable-vectorization`           | `false` |
| `--disable-vectorization-cache` | Disable vectorization cache             | `pdf2zh_next --disable-vectorization-cache`     | `false` |
| `--enable-ocr`                  | Enable OCR functionality                | `pdf2zh_next --enable-ocr`                      | `false` |
| `--enable-translation`          | Enable translation functionality        | `pdf2zh_next --enable-translation`              | `false` |
| `--enable-vectorization`        | Enable vectorization functionality      | `pdf2zh_next --enable-vectorization`            | `false` |
| `--enable-vectorization-cache`  | Enable vectorization cache              | `pdf2zh_next --enable-vectorization-cache`      | `false` |
| `--gui`                         | Launch the GUI                          | `pdf2zh_next --gui`                             | `false` |
| `--help`                        | Show help message                       | `pdf2zh_next --help`                            |         |
| `--input`                       | Input file path                         | `pdf2zh_next --input example.pdf`               |         |
| `--log-level`                   | Set log level                           | `pdf2zh_next --log-level debug`                 | `info`  |
| `--output`                      | Output file path                        | `pdf2zh_next --output example_zh.pdf`           |         |
| `--output-dir`                  | Output directory                        | `pdf2zh_next --output-dir ./output`             |         |
| `--prompt`                      | Prompt text for translation             | `pdf2zh_next --prompt "Translate to Chinese"`   |         |
| `--prompt-ocr`                  | Prompt text for OCR                     | `pdf2zh_next --prompt-ocr "OCR this image"`     |         |
| `--prompt-vectorization`        | Prompt text for vectorization           | `pdf2zh_next --prompt-vectorization "Summarize"`|         |
| `--service`                     | Translation service to use              | `pdf2zh_next --service openai`                  | `openai`|
| `--target-language`             | Target language for translation         | `pdf2zh_next --target-language zh`              | `zh`    |
| `--version`                     | Show version information                | `pdf2zh_next --version`                         |         |

---

### TRANSLATION RESULT

| `--disable-config-auto-save`    | 禁用自動配置保存 | `pdf2zh_next --gui --disable-config-auto-save`  | `false` |
| `--disable-ocr`                 | 禁用 OCR 功能 | `pdf2zh_next --disable-ocr`                     | `false` |
| `--disable-translation`         | 禁用翻譯功能 | `pdf2zh_next --disable-translation`             | `false` |
| `--disable-vectorization`       | 禁用向量化功能 | `pdf2zh_next --disable-vectorization`           | `false` |
| `--disable-vectorization-cache` | 禁用向量化緩存 | `pdf2zh_next --disable-vectorization-cache`     | `false` |
| `--enable-ocr`                  | 啟用 OCR 功能 | `pdf2zh_next --enable-ocr`                      | `false` |
| `--enable-translation`          | 啟用翻譯功能 | `pdf2zh_next --enable-translation`              | `false` |
| `--enable-vectorization`        | 啟用向量化功能 | `pdf2zh_next --enable-vectorization`            | `false` |
| `--enable-vectorization-cache`  | 啟用向量化緩存 | `pdf2zh_next --enable-vectorization-cache`      | `false` |
| `--gui`                         | 啟動 GUI | `pdf2zh_next --gui`                             | `false` |
| `--help`                        | 顯示幫助訊息 | `pdf2zh_next --help`                            |         |
| `--input`                       | 輸入文件路徑 | `pdf2zh_next --input example.pdf`               |         |
| `--log-level`                   | 設置日誌級別 | `pdf2zh_next --log-level debug`                 | `info`  |
| `--output`                      | 輸出文件路徑 | `pdf2zh_next --output example_zh.pdf`           |         |
| `--output-dir`                  | 輸出目錄 | `pdf2zh_next --output-dir ./output`             |         |
| `--prompt`                      | 翻譯提示文本 | `pdf2zh_next --prompt "Translate to Chinese"`   |         |
| `--prompt-ocr`                  | OCR 提示文本 | `pdf2zh_next --prompt-ocr "OCR this image"`     |         |
| `--prompt-vectorization`        | 向量化提示文本 | `pdf2zh_next --prompt-vectorization "Summarize"`|         |
| `--service`                     | 使用的翻譯服務 | `pdf2zh_next --service openai`                  | `openai`|
| `--target-language`             | 翻譯目標語言 | `pdf2zh_next --target-language zh`              | `zh`    |
| `--version`                     | 顯示版本資訊 | `pdf2zh_next --version`                         |         |
`7860`                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ------------------------------ |
| `--server-name`                 | WebUI Host                             | `pdf2zh_next --gui --server-name 0.0.0.0`       | `0.0.0.0`                      |
| `--concurrency-count`           | Number of concurrent tasks             | `pdf2zh_next --gui --concurrency-count 4`       | `4`                            |
| `--server-headless`             | Run WebUI in headless mode             | `pdf2zh_next --gui --server-headless`           | `False`                        |
| `--share`                       | Create a public link                   | `pdf2zh_next --gui --share`                     | `False`                        |
| `--auth`                        | Set username and password              | `pdf2zh_next --gui --auth user pass`            | `None`                         |
| `--auth-message`                | Custom auth message                    | `pdf2zh_next --gui --auth-message "hello"`      | `None`                         |
| `--ssl-keyfile`                 | SSL key file path                      | `pdf2zh_next --gui --ssl-keyfile key.pem`       | `None`                         |
| `--ssl-certfile`                | SSL certificate file path              | `pdf2zh_next --gui --ssl-certfile cert.pem`     | `None`                         |
| `--ssl-keyfile-password`        | SSL key file password                  | `pdf2zh_next --gui --ssl-keyfile-password pass` | `None`                         |
| `--ssl-version`                 | SSL version                            | `pdf2zh_next --gui --ssl-version 2`             | `None`                         |
| `--max-file-size`               | Max file size (MB)                     | `pdf2zh_next --gui --max-file-size 100`         | `100`                          |
| `--max-files`                   | Max number of files                    | `pdf2zh_next --gui --max-files 20`              | `20`                           |
| `--allowed-path`                | Allowed upload paths                   | `pdf2zh_next --gui --allowed-path /path/to/dir` | `None`                         |
| `--blocking-cross-origin`       | Block cross-origin requests            | `pdf2zh_next --gui --blocking-cross-origin`     | `False`                        |
| `--show-error`                  | Show error in the WebUI                | `pdf2zh_next --gui --show-error`                | `False`                        |
| `--prevent-thread-lock`         | Prevent thread lock in WebUI           | `pdf2zh_next --gui --prevent-thread-lock`       | `False`                        |
| `--favicon-path`                | Path to custom favicon                 | `pdf2zh_next --gui --favicon-path favicon.ico`  | `None`                         |
| `--show-api`                    | Show API docs                          | `pdf2zh_next --gui --show-api`                  | `True`                         |
| `--mode`                        | WebUI mode                             | `pdf2zh_next --gui --mode full`                 | `full`                         |
| `--root-path`                   | Root path for the app                  | `pdf2zh_next --gui --root-path /app`            | `None`                         |
| `--app-kwargs`                  | Additional app kwargs                  | `pdf2zh_next --gui --app-kwargs '{"title":""}'` | `{}`                           |
| `--gradio-kwargs`               | Additional gradio kwargs              | `pdf2zh_next --gui --gradio-kwargs '{}'`        | `{}`                           |

---

### OUTPUT

| `--server-port`                 | WebUI 端口                             | `pdf2zh_next --gui --server-port 7860`          | `7860`                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ------------------------------ |
| `--server-name`                 | WebUI 主機                             | `pdf2zh_next --gui --server-name 0.0.0.0`       | `0.0.0.0`                      |
| `--concurrency-count`           | 併發任務數量                           | `pdf2zh_next --gui --concurrency-count 4`       | `4`                            |
| `--server-headless`             | 以無頭模式運行 WebUI                    | `pdf2zh_next --gui --server-headless`           | `False`                        |
| `--share`                       | 創建公共鏈接                           | `pdf2zh_next --gui --share`                     | `False`                        |
| `--auth`                        | 設置用戶名和密碼                       | `pdf2zh_next --gui --auth user pass`            | `None`                         |
| `--auth-message`                | 自定義認證消息                         | `pdf2zh_next --gui --auth-message "hello"`      | `None`                         |
| `--ssl-keyfile`                 | SSL 密鑰文件路徑                       | `pdf2zh_next --gui --ssl-keyfile key.pem`       | `None`                         |
| `--ssl-certfile`                | SSL 證書文件路徑                       | `pdf2zh_next --gui --ssl-certfile cert.pem`     | `None`                         |
| `--ssl-keyfile-password`        | SSL 密鑰文件密碼                       | `pdf2zh_next --gui --ssl-keyfile-password pass` | `None`                         |
| `--ssl-version`                 | SSL 版本                               | `pdf2zh_next --gui --ssl-version 2`             | `None`                         |
| `--max-file-size`               | 最大文件大小 (MB)                      | `pdf2zh_next --gui --max-file-size 100`         | `100`                          |
| `--max-files`                   | 最大文件數量                           | `pdf2zh_next --gui --max-files 20`              | `20`                           |
| `--allowed-path`                | 允許上傳的路徑                         | `pdf2zh_next --gui --allowed-path /path/to/dir` | `None`                         |
| `--blocking-cross-origin`       | 阻止跨域請求                           | `pdf2zh_next --gui --blocking-cross-origin`     | `False`                        |
| `--show-error`                  | 在 WebUI 中顯示錯誤                    | `pdf2zh_next --gui --show-error`                | `False`                        |
| `--prevent-thread-lock`         | 防止 WebUI 中的線程鎖定                | `pdf2zh_next --gui --prevent-thread-lock`       | `False`                        |
| `--favicon-path`                | 自定義網站圖標路徑                     | `pdf2zh_next --gui --favicon-path favicon.ico`  | `None`                         |
| `--show-api`                    | 顯示 API 文檔                          | `pdf2zh_next --gui --show-api`                  | `True`                         |
| `--mode`                        | WebUI 模式                             | `pdf2zh_next --gui --mode full`                 | `full`                         |
| `--root-path`                   | 應用程序的根路徑                       | `pdf2zh_next --gui --root-path /app`            | `None`                         |
| `--app-kwargs`                  | 額外的應用程序參數                     | `pdf2zh_next --gui --app-kwargs '{"title":""}'` | `{}`                           |
| `--gradio-kwargs`               | 額外的 gradio 參數                     | `pdf2zh_next --gui --gradio-kwargs '{}'`        | `{}`                           |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--ui-lang`                     | UI 語言                                | `pdf2zh_next --gui --ui-lang zh`                |

---

### OUTPUT

| `--ui-lang`                     | UI 語言                                | `pdf2zh_next --gui --ui-lang zh`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--ui-lang`                     | UI 語言                                | `pdf2zh_next --gui --ui-lang zh`                |

[⬆️ 返回頂部](#目錄)

---

#### 速率限制配置指南

在使用翻譯服務時，適當的速率限制配置對於避免 API 錯誤和優化性能至關重要。本指南解釋如何根據不同的上游服務限制來配置 `--qps` 和 `--pool-max-worker` 參數。

> [!TIP]
>
> 建議 `pool_size` 不要超過 1000。如果通過以下方法計算出的 `pool_size` 超過 1000，請使用 1000。

##### RPM（每分鐘請求數）速率限制

當上游服務有 RPM 限制時，請使用以下計算方式：

**計算公式：**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> 係數 10 是一個經驗係數，在大多數情況下都能良好運作。

**範例：**
如果您的翻譯服務有 600 RPM 的限制：
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### 並發連接限制

當上游服務有並發連接限制（如 GLM 官方服務）時，使用此方法：

**計算公式：**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**範例：**
若您的翻譯服務允許 50 個並發連接：
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### 最佳實踐

> [!TIP]
> - 始終從保守值開始，並根據需要逐步增加
> - 監控服務的響應時間和錯誤率
> - 不同的服務可能需要不同的優化策略
> - 設置這些參數時，請考慮您的具體使用案例和文件大小


[⬆️ 返回頂部](#目錄)

---

#### 部分翻譯

使用 `--pages` 參數來翻譯文件的一部分。

- 如果頁碼是連續的，可以這樣寫：

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` 包含第 25 頁之後的所有頁面。如果您的文件有 100 頁，這等同於 `25-100`。
> 
> 同理，`-25` 包含第 25 頁之前的所有頁面，等同於 `1-25`。

- 如果頁面不是連續的，可以使用逗號 `,` 分隔它們。

例如，如果您想翻譯第一頁和第三頁，可以使用以下命令：

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- 如果頁面包含連續與非連續範圍，你也可以用逗號連接它們，像這樣：

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

這個命令將翻譯第一頁、第三頁、第 10 至 20 頁，以及從第 25 頁開始的所有頁面。

[⬆️ 回到頂部](#目錄)

---

#### 指定來源與目標語言

請參閱 [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages)、[DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ 返回頂部](#目錄)

---

#### 翻譯例外情況

使用正則表達式指定需要保留的公式字體與字元：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

預設保留 `Latex`、`Mono`、`Code`、`Italic`、`Symbol` 與 `Math` 字體：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ 返回頂部](#目錄)

---

#### 自訂提示

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

自訂翻譯系統提示。主要用於在提示中加入 Qwen 3 的 `/no_think` 指令。

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ 返回頂部](#目錄)

---

#### 自訂配置

有多種方式可以修改並導入設定檔。

> [!NOTE]
> **設定檔層級**
>
> 當使用不同方法修改相同參數時，軟體會依照以下優先順序套用變更。
>
> 較高優先順序的修改會覆蓋較低優先順序的設定。
>
> **命令行/圖形界面 > 環境變數 > 使用者設定檔 > 預設設定檔**

- 透過 **命令行參數** 修改配置

在大多數情況下，您可以直接通過命令行參數傳遞所需的設定。更多資訊請參考 [命令行參數](#命令行參數)。

例如，如果您想啟用圖形界面窗口，可以使用以下命令：

```bash
pdf2zh_next --gui
```

- 透過 **環境變數** 修改配置

你可以將命令列參數中的 `--` 替換為 `PDF2ZH_`，使用 `=` 連接參數，並將 `-` 替換為 `_` 作為環境變數。

例如，如果你想啟用圖形界面視窗，可以使用以下命令：

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- 使用者指定的 **設定檔**

您可以使用以下命令行參數指定配置檔案：

```bash
pdf2zh_next --config-file '/path/config.toml'
```

如果您不確定配置文件的格式，請參考下方描述的默認配置文件。

- **預設配置文件**

預設的設定檔位於 `~/.config/pdf2zh`。  
請勿修改 `default` 目錄中的設定檔。  
強烈建議參考此設定檔的內容，並使用 **自訂配置** 來實現您自己的設定檔。

> [!TIP]
> - 預設情況下，pdf2zh 2.0 每次在圖形界面中點擊翻譯按鈕時，會自動將當前配置保存到 `~/.config/pdf2zh/config.v3.toml`。此配置文件將在下次啟動時自動載入。
> - `default` 目錄中的配置文件由程序自動生成。您可以複製它們進行修改，但請勿直接修改這些文件。
> - 配置文件中可能包含 "v2"、"v3" 等版本號。這些是**配置文件的版本號**，**並非** pdf2zh 本身的版本號。


[⬆️ 返回頂部](#目錄)

---

#### 跳過清理

當此參數設為 True 時，將跳過 PDF 清理步驟，這能提升相容性並避免一些字體處理問題。

使用方法：

```bash
pdf2zh_next example.pdf --skip-clean
```

或者使用環境變數：

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> 當啟用 `--enhance-compatibility` 時，跳過清理會自動啟用。

---

#### 翻譯快取

PDFMathTranslate 會快取已翻譯的文字，以提高速度並避免對相同內容進行不必要的 API 呼叫。你可以使用 `--ignore-cache` 選項來忽略翻譯快取並強制重新翻譯。

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ 返回頂部](#目錄)

---

#### 部署為公共服務

在將 pdf2zh GUI 部署為公共服務時，您應按照以下說明修改配置檔案。

> [!WARNING]
>
> 本專案尚未經過專業安全審計，可能包含安全漏洞。請在部署至公共網絡前評估風險並採取必要的安全措施。


> [!TIP]
> - 公開部署時，應同時啟用 `disable_gui_sensitive_input` 和 `disable_config_auto_save` 選項。
> - 使用 *英文逗號* <kbd>,</kbd> 分隔不同的可用服務。

一個可用的配置如下：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ 返回頂部](#目錄)

---

#### 驗證與歡迎頁面

當使用驗證與歡迎頁面來指定哪些用戶可以使用 Web UI 並自訂登入頁面時：

範例 auth.txt
每行包含兩個元素，用戶名和密碼，以逗號分隔。

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

範例 welcome.html

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
> 歡迎頁面僅在驗證檔案不為空白時才會運作。
> 若驗證檔案為空白，則不會進行驗證。 :)

一個可用的配置如下：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ 返回頂部](#目錄)

---

#### 詞彙表支援

PDFMathTranslate 支援詞彙表功能。詞彙表檔案應為 `csv` 格式。  
檔案中包含三欄，以下是一個示範詞彙表檔案：

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自動 ML  | zh-TW   |
| a,a    | a       | zh-TW   |
| "      | "       | zh-TW   |


對於 CLI 使用者：
您可以使用多個檔案作為詞彙表。不同檔案應以 `,` 分隔。

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

對於 WebUI 使用者：

您現在可以上傳自己的詞彙表檔案。上傳檔案後，您可以點擊檔案名稱來查看內容，內容會顯示在下方。

[⬆️ 回到頂部](#目錄)

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>