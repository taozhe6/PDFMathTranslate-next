[**高级选项**](./introduction.md) > **高级选项** _(当前)_

---

<h3 id="目录">目录</h3>

- [命令行参数](#命令行参数)
- [限流配置指南](#限流配置指南)
- [部分翻译](#部分翻译)
- [指定源语言和目标语言](#指定源语言和目标语言)
- [带例外的翻译](#带例外的翻译)
- [自定义提示词](#自定义提示词)
- [自定义配置](#自定义配置)
- [跳过清理](#跳过清理)
- [翻译缓存](#翻译缓存)
- [部署为公共服务](#部署为公共服务)
- [认证与欢迎页](#认证与欢迎页)
- [术语表支持](#术语表支持)

---

#### 命令行参数

在命令行中执行翻译命令，在当前工作目录下生成翻译后的文档 `example-mono.pdf` 和双语文档 `example-dual.pdf`。默认使用 Google 作为翻译服务。更多支持的翻译服务可在 [HERE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services) 找到。

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

在下表中，我们列出了所有高级选项以供参考：

##### 参数

| `output-dir`                    | Directory to save translated PDF files                                                   | `pdf2zh_next -o ./translated example.pdf`                                                                             |
| `input-dir`                     | Directory containing PDF files to process                                                | `pdf2zh_next -i ./pdfs`                                                                                               |
| `output-filename`                | Filename of the translated PDF                                                           | `pdf2zh_next -o ./translated/translated.pdf example.pdf`                                                               |
| `language`                       | Target language for translation                                                          | `pdf2zh_next -l zh example.pdf`                                                                                       |
| `api-key`                        | API key for the translation service                                                      | `pdf2zh_next --api-key YOUR_API_KEY example.pdf`                                                                      |
| `api-base`                       | Base URL for the translation API                                                         | `pdf2zh_next --api-base https://api.openai.com/v1 example.pdf`                                                         |
| `model`                          | Model to use for translation                                                             | `pdf2zh_next --model gpt-4o-mini example.pdf`                                                                         |
| `translator`                     | Translation service to use                                                               | `pdf2zh_next --translator openai example.pdf`                                                                         |
| `concurrency`                    | Number of concurrent translation requests                                                 | `pdf2zh_next --concurrency 5 example.pdf`                                                                             |
| `retry-attempts`                 | Number of retry attempts for failed requests                                             | `pdf2zh_next --retry-attempts 3 example.pdf`                                                                          |
| `retry-delay`                    | Delay between retry attempts in seconds                                                  | `pdf2zh_next --retry-delay 10 example.pdf`                                                                            |
| `timeout`                        | Timeout for each translation request in seconds                                          | `pdf2zh_next --timeout 60 example.pdf`                                                                                |
| `max-tokens`                     | Maximum tokens per translation request                                                   | `pdf2zh_next --max-tokens 1000 example.pdf`                                                                           |
| `proxy`                          | Proxy server to use for requests                                                         | `pdf2zh_next --proxy http://proxy.example.com:8080 example.pdf`                                                        |
| `cache-dir`                      | Directory to cache translation results                                                   | `pdf2zh_next --cache-dir ./cache example.pdf`                                                                         |
| `no-cache`                       | Disable caching of translation results                                                   | `pdf2zh_next --no-cache example.pdf`                                                                                  |
| `ignore-cache`                   | Ignore existing cache and retranslate                                                    | `pdf2zh_next --ignore-cache example.pdf`                                                                              |
| `resume`                         | Resume from the last interrupted translation                                            | `pdf2zh_next --resume example.pdf`                                                                                    |
| `checkpoint-interval`            | Interval (in pages) to save translation progress                                         | `pdf2zh_next --checkpoint-interval 10 example.pdf`                                                                    |
| `translation-only`               | Only perform translation without generating PDF                                          | `pdf2zh_next --translation-only example.pdf`                                                                          |
| `pdf-only`                       | Only generate PDF from existing translation cache                                        | `pdf2zh_next --pdf-only example.pdf`                                                                                  |
| `force`                          | Force overwrite existing files                                                           | `pdf2zh_next --force example.pdf`                                                                                     |
| `pages`                          | Specific pages to translate (e.g., 1-5, 8, 11-13)                                        | `pdf2zh_next --pages 1-5 example.pdf`                                                                                 |
| `ocr`                            | Enable OCR for image-based PDFs                                                          | `pdf2zh_next --ocr example.pdf`                                                                                       |
| `ocr-language`                   | Language for OCR                                                                         | `pdf2zh_next --ocr-language eng example.pdf`                                                                          |
| `ignore-existing`                | Skip files that already have a translated version                                        | `pdf2zh_next --ignore-existing example.pdf`                                                                           |
| `version`                        | Show version information                                                                 | `pdf2zh_next --version`                                                                                               |
| `help`                           | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| 选项                          | 功能                                                                               | 示例                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | 要处理的输入 PDF 文件                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `output-dir`                    | 保存翻译后 PDF 文件的目录                                                   | `pdf2zh_next -o ./translated example.pdf`                                                                             |
| `input-dir`                     | 包含要处理的 PDF 文件的目录                                                | `pdf2zh_next -i ./pdfs`                                                                                               |
| `output-filename`                | 翻译后 PDF 的文件名                                                           | `pdf2zh_next -o ./translated/translated.pdf example.pdf`                                                               |
| `language`                       | 翻译的目标语言                                                          | `pdf2zh_next -l zh example.pdf`                                                                                       |
| `api-key`                        | 翻译服务的 API 密钥                                                      | `pdf2zh_next --api-key YOUR_API_KEY example.pdf`                                                                      |
| `api-base`                       | 翻译 API 的基础 URL                                                         | `pdf2zh_next --api-base https://api.openai.com/v1 example.pdf`                                                         |
| `model`                          | 用于翻译的模型                                                             | `pdf2zh_next --model gpt-4o-mini example.pdf`                                                                         |
| `translator`                     | 要使用的翻译服务                                                               | `pdf2zh_next --translator openai example.pdf`                                                                         |
| `concurrency`                    | 并发翻译请求的数量                                                 | `pdf2zh_next --concurrency 5 example.pdf`                                                                             |
| `retry-attempts`                 | 失败请求的重试次数                                             | `pdf2zh_next --retry-attempts 3 example.pdf`                                                                          |
| `retry-delay`                    | 重试尝试之间的延迟（秒）                                                  | `pdf2zh_next --retry-delay 10 example.pdf`                                                                            |
| `timeout`                        | 每个翻译请求的超时时间（秒）                                          | `pdf2zh_next --timeout 60 example.pdf`                                                                                |
| `max-tokens`                     | 每个翻译请求的最大令牌数                                                   | `pdf2zh_next --max-tokens 1000 example.pdf`                                                                           |
| `proxy`                          | 用于请求的代理服务器                                                         | `pdf2zh_next --proxy http://proxy.example.com:8080 example.pdf`                                                        |
| `cache-dir`                      | 缓存翻译结果的目录                                                   | `pdf2zh_next --cache-dir ./cache example.pdf`                                                                         |
| `no-cache`                       | 禁用翻译结果的缓存                                                   | `pdf2zh_next --no-cache example.pdf`                                                                                  |
| `ignore-cache`                   | 忽略现有缓存并重新翻译                                                    | `pdf2zh_next --ignore-cache example.pdf`                                                                              |
| `resume`                         | 从上次中断的翻译处恢复                                            | `pdf2zh_next --resume example.pdf`                                                                                    |
| `checkpoint-interval`            | 保存翻译进度的间隔（按页数）                                         | `pdf2zh_next --checkpoint-interval 10 example.pdf`                                                                    |
| `translation-only`               | 仅执行翻译而不生成 PDF                                          | `pdf2zh_next --translation-only example.pdf`                                                                          |
| `pdf-only`                       | 仅从现有翻译缓存生成 PDF                                        | `pdf2zh_next --pdf-only example.pdf`                                                                                  |
| `force`                          | 强制覆盖现有文件                                                           | `pdf2zh_next --force example.pdf`                                                                                     |
| `pages`                          | 要翻译的特定页面（例如：1-5, 8, 11-13）                                        | `pdf2zh_next --pages 1-5 example.pdf`                                                                                 |
| `ocr`                            | 为基于图像的 PDF 启用 OCR                                                          | `pdf2zh_next --ocr example.pdf`                                                                                       |
| `ocr-language`                   | OCR 的语言                                                                         | `pdf2zh_next --ocr-language eng example.pdf`                                                                          |
| `ignore-existing`                | 跳过已有翻译版本的文件                                        | `pdf2zh_next --ignore-existing example.pdf`                                                                           |
| `version`                        | 显示版本信息                                                                 | `pdf2zh_next --version`                                                                                               |
| `help`                           | 显示帮助消息                                                                       | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-suffix`               | Suffix added to the output file name                                                    | `pdf2zh_next example.pdf --output-suffix _zh`                                                                         |
| `-o`                            | Alias for `--output`                                                                    | `pdf2zh_next example.pdf -o /outputpath`                                                                              |
| `--output-type`                 | Output file type, can be `pdf` or `text`                                                | `pdf2zh_next example.pdf --output-type text`                                                                          |
| `--output-format`               | Format of the output file, can be `markdown` or `text` (only when output type is text)  | `pdf2zh_next example.pdf --output-format markdown --output-type text`                                                 |
| `--output-encoding`             | Output file encoding, default is `utf-8`                                                | `pdf2zh_next example.pdf --output-encoding gbk`                                                                       |
| `--output-ocr`                  | Whether to output the OCR result, default is `false`                                    | `pdf2zh_next example.pdf --output-ocr true`                                                                           |
| `--output-ocr-format`           | Format of the OCR result, can be `json` or `text`                                       | `pdf2zh_next example.pdf --output-ocr-format json`                                                                    |
| `--output-ocr-encoding`         | OCR result encoding, default is `utf-8`                                                 | `pdf2zh_next example.pdf --output-ocr-encoding gbk`                                                                   |
| `--output-ocr-suffix`           | Suffix added to the OCR output file name                                                | `pdf2zh_next example.pdf --output-ocr-suffix _ocr`                                                                    |
| `--output-ocr-only`             | Whether to only output the OCR result, default is `false`                               | `pdf2zh_next example.pdf --output-ocr-only true`                                                                      |
| `--output-ocr-only-format`      | Format of the OCR only output, can be `json` or `text`                                  | `pdf2zh_next example.pdf --output-ocr-only-format json`                                                               |
| `--output-ocr-only-encoding`    | OCR only output encoding, default is `utf-8`                                            | `pdf2zh_next example.pdf --output-ocr-only-encoding gbk`                                                              |
| `--output-ocr-only-suffix`      | Suffix added to the OCR only output file name                                           | `pdf2zh_next example.pdf --output-ocr-only-suffix _ocr`                                                               |

---

### TRANSLATION RESULT

| `--output`                      | 输出文件的目录                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-suffix`               | 添加到输出文件名的后缀                                                    | `pdf2zh_next example.pdf --output-suffix _zh`                                                                         |
| `-o`                            | `--output` 的别名                                                                    | `pdf2zh_next example.pdf -o /outputpath`                                                                              |
| `--output-type`                 | 输出文件类型，可以是 `pdf` 或 `text`                                                | `pdf2zh_next example.pdf --output-type text`                                                                          |
| `--output-format`               | 输出文件的格式，可以是 `markdown` 或 `text`（仅当输出类型为 `text` 时）  | `pdf2zh_next example.pdf --output-format markdown --output-type text`                                                 |
| `--output-encoding`             | 输出文件编码，默认为 `utf-8`                                                | `pdf2zh_next example.pdf --output-encoding gbk`                                                                       |
| `--output-ocr`                  | 是否输出 OCR 结果，默认为 `false`                                    | `pdf2zh_next example.pdf --output-ocr true`                                                                           |
| `--output-ocr-format`           | OCR 结果的格式，可以是 `json` 或 `text`                                       | `pdf2zh_next example.pdf --output-ocr-format json`                                                                    |
| `--output-ocr-encoding`         | OCR 结果编码，默认为 `utf-8`                                                 | `pdf2zh_next example.pdf --output-ocr-encoding gbk`                                                                   |
| `--output-ocr-suffix`           | 添加到 OCR 输出文件名的后缀                                                | `pdf2zh_next example.pdf --output-ocr-suffix _ocr`                                                                    |
| `--output-ocr-only`             | 是否仅输出 OCR 结果，默认为 `false`                               | `pdf2zh_next example.pdf --output-ocr-only true`                                                                      |
| `--output-ocr-only-format`      | 仅 OCR 输出的格式，可以是 `json` 或 `text`                                  | `pdf2zh_next example.pdf --output-ocr-only-format json`                                                               |
| `--output-ocr-only-encoding`    | 仅 OCR 输出编码，默认为 `utf-8`                                            | `pdf2zh_next example.pdf --output-ocr-only-encoding gbk`                                                              |
| `--output-ocr-only-suffix`      | 添加到仅 OCR 输出文件名的后缀                                           | `pdf2zh_next example.pdf --output-ocr-only-suffix _ocr`                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>`-`<model>`        | Use [**specific model**](./Documentation-of-Translation-Services.md) for translation   | `pdf2zh_next example.pdf --openai-gpt-4o`<br>`pdf2zh_next example.pdf --deepseek-deepseek-chat`                       |
| `--<Services>`-`<api-key>`      | Set the API key for the service                                                       | `pdf2zh_next example.pdf --openai-api-key <your key>`<br>`pdf2zh_next example.pdf --deepseek-api-key <your key>`       |
| `--<Services>`-`<api-base>`     | Set the API base URL for the service                                                  | `pdf2zh_next example.pdf --openai-api-base <base url>`<br>`pdf2zh_next example.pdf --deepseek-api-base <base url>`     |
| `--<Services>`-`<api-version>`  | Set the API version for the service                                                   | `pdf2zh_next example.pdf --azure-api-version <version>`                                                               |

---

### OUTPUT

| `--<Services>`                  | 使用 [**特定服务**](./Documentation-of-Translation-Services.md) 进行翻译 | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>`-`<model>`        | 使用 [**特定模型**](./Documentation-of-Translation-Services.md) 进行翻译   | `pdf2zh_next example.pdf --openai-gpt-4o`<br>`pdf2zh_next example.pdf --deepseek-deepseek-chat`                       |
| `--<Services>`-`<api-key>`      | 设置服务的 API 密钥                                                       | `pdf2zh_next example.pdf --openai-api-key <your key>`<br>`pdf2zh_next example.pdf --deepseek-api-key <your key>`       |
| `--<Services>`-`<api-base>`     | 设置服务的 API 基础 URL                                                  | `pdf2zh_next example.pdf --openai-api-base <base url>`<br>`pdf2zh_next example.pdf --deepseek-api-base <base url>`     |
| `--<Services>`-`<api-version>`  | 设置服务的 API 版本                                                   | `pdf2zh_next example.pdf --azure-api-version <version>`                                                               |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--version`, `-v`               | Show version and exit                                                                    | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | **Required**. Input file path.                                                           | `pdf2zh_next -i input.pdf`                                                                                            |
| `--output`, `-o`                | **Required**. Output file path.                                                          | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `--source-lang`, `-s`           | Source language. Default is `auto`.                                                      | `pdf2zh_next -i input.pdf -o output.pdf -s en`                                                                        |
| `--target-lang`, `-t`           | Target language. Default is `zh`.                                                        | `pdf2zh_next -i input.pdf -o output.pdf -t zh`                                                                        |
| `--translator`, `-tr`           | Translation service. Default is `aliyun`.                                                | `pdf2zh_next -i input.pdf -o output.pdf -tr aliyun`                                                                   |
| `--translator-args`, `-tr-args` | Arguments for translation service.                                                       | `pdf2zh_next -i input.pdf -o output.pdf -tr aliyun -tr-args '{"access_key_id": "xxx", "access_key_secret": "xxx"}'`   |
| `--translator-config`, `-tr-cfg` | Config file for translation service.                                                     | `pdf2zh_next -i input.pdf -o output.pdf -tr aliyun -tr-cfg config.json`                                               |
| `--ocr`, `-ocr`                 | OCR service. Default is `auto`.                                                          | `pdf2zh_next -i input.pdf -o output.pdf -ocr auto`                                                                    |
| `--ocr-args`, `-ocr-args`       | Arguments for OCR service.                                                               | `pdf2zh_next -i input.pdf -o output.pdf -ocr auto -ocr-args '{"access_key_id": "xxx", "access_key_secret": "xxx"}'`   |
| `--ocr-config`, `-ocr-cfg`      | Config file for OCR service.                                                             | `pdf2zh_next -i input.pdf -o output.pdf -ocr auto -ocr-cfg config.json`                                               |
| `--parallel`, `-p`              | Number of parallel translations. Default is `4`.                                         | `pdf2zh_next -i input.pdf -o output.pdf -p 8`                                                                         |
| `--batch-size`, `-b`            | Number of pages per batch. Default is `10`.                                              | `pdf2zh_next -i input.pdf -o output.pdf -b 20`                                                                        |
| `--timeout`, `-to`              | Timeout for translation service in seconds. Default is `30`.                             | `pdf2zh_next -i input.pdf -o output.pdf -to 60`                                                                       |
| `--retry`, `-r`                 | Number of retries for translation service. Default is `3`.                               | `pdf2zh_next -i input.pdf -o output.pdf -r 5`                                                                         |
| `--log-level`, `-l`             | Log level. Default is `info`.                                                            | `pdf2zh_next -i input.pdf -o output.pdf -l debug`                                                                     |
| `--log-file`, `-lf`             | Log file path.                                                                           | `pdf2zh_next -i input.pdf -o output.pdf -lf log.txt`                                                                  |
| `--config`, `-c`                | Config file path.                                                                        | `pdf2zh_next -i input.pdf -o output.pdf -c config.json`                                                               |
| `--no-cache`, `-nc`             | Disable cache.                                                                           | `pdf2zh_next -i input.pdf -o output.pdf -nc`                                                                          |
| `--cache-dir`, `-cd`            | Cache directory. Default is `./.cache`.                                                  | `pdf2zh_next -i input.pdf -o output.pdf -cd /tmp/cache`                                                               |
| `--cache-ttl`, `-ct`            | Cache TTL in seconds. Default is `86400` (1 day).                                        | `pdf2zh_next -i input.pdf -o output.pdf -ct 3600`                                                                     |
| `--force`, `-f`                 | Force translation even if output file exists.                                            | `pdf2zh_next -i input.pdf -o output.pdf -f`                                                                           |
| `--dry-run`, `-dr`              | Dry run without actual translation.                                                      | `pdf2zh_next -i input.pdf -o output.pdf -dr`                                                                          |
| `--verbose`, `-vb`              | Verbose output.                                                                          | `pdf2zh_next -i input.pdf -o output.pdf -vb`                                                                          |
| `--quiet`, `-q`                 | Quiet mode.                                                                              | `pdf2zh_next -i input.pdf -o output.pdf -q`                                                                           |
| `--yes`, `-y`                   | Auto confirm all prompts.                                                                | `pdf2zh_next -i input.pdf -o output.pdf -y`                                                                           |
| `--no`, `-n`                    | Auto deny all prompts.                                                                   | `pdf2zh_next -i input.pdf -o output.pdf -n`                                                                           |
| `--help-translator`, `-htr`     | Show help for translation service.                                                       | `pdf2zh_next -htr aliyun`                                                                                             |
| `--help-ocr`, `-hocr`           | Show help for OCR service.                                                               | `pdf2zh_next -hocr auto`                                                                                              |
| `--list-translators`, `-ltr`    | List available translation services.                                                     | `pdf2zh_next -ltr`                                                                                                    |
| `--list-ocr`, `-locr`           | List available OCR services.                                                             | `pdf2zh_next -locr`                                                                                                   |
| `--list-languages`, `-ll`       | List supported languages.                                                                | `pdf2zh_next -ll`                                                                                                     |
| `--update`, `-u`                | Update to the latest version.                                                            | `pdf2zh_next -u`                                                                                                      |
| `--self-update`, `-su`          | Self update.                                                                             | `pdf2zh_next -su`                                                                                                     |
| `--uninstall`, `-un`            | Uninstall pdf2zh.                                                                        | `pdf2zh_next -un`                                                                                                     |
| `--install`, `-in`              | Install pdf2zh.                                                                          | `pdf2zh_next -in`                                                                                                     |
| `--check`, `-chk`               | Check installation.                                                                      | `pdf2zh_next -chk`                                                                                                    |
| `--doctor`, `-doc`              | Diagnose and fix common issues.                                                          | `pdf2zh_next -doc`                                                                                                    |
| `--bug-report`, `-br`           | Generate bug report.                                                                     | `pdf2zh_next -br`                                                                                                     |
| `--feedback`, `-fb`             | Send feedback.                                                                           | `pdf2zh_next -fb`                                                                                                     |
| `--donate`, `-d`                | Donate to the project.                                                                   | `pdf2zh_next -d`                                                                                                      |
| `--sponsor`, `-sp`              | Sponsor the project.                                                                     | `pdf2zh_next -sp`                                                                                                      |

---

### TRANSLATION RESULT

| `--help`, `-h`                  | 显示帮助信息并退出                                                                      | `pdf2zh_next -h`                                                                                                      |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--version`, `-v`               | 显示版本并退出                                                                          | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | **必填**。输入文件路径。                                                                | `pdf2zh_next -i input.pdf`                                                                                            |
| `--output`, `-o`                | **必填**。输出文件路径。                                                                | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `--source-lang`, `-s`           | 源语言。默认为 `auto`。                                                                 | `pdf2zh_next -i input.pdf -o output.pdf -s en`                                                                        |
| `--target-lang`, `-t`           | 目标语言。默认为 `zh`。                                                                 | `pdf2zh_next -i input.pdf -o output.pdf -t zh`                                                                        |
| `--translator`, `-tr`           | 翻译服务。默认为 `aliyun`。                                                             | `pdf2zh_next -i input.pdf -o output.pdf -tr aliyun`                                                                   |
| `--translator-args`, `-tr-args` | 翻译服务的参数。                                                                        | `pdf2zh_next -i input.pdf -o output.pdf -tr aliyun -tr-args '{"access_key_id": "xxx", "access_key_secret": "xxx"}'`   |
| `--translator-config`, `-tr-cfg` | 翻译服务的配置文件。                                                                    | `pdf2zh_next -i input.pdf -o output.pdf -tr aliyun -tr-cfg config.json`                                               |
| `--ocr`, `-ocr`                 | OCR 服务。默认为 `auto`。                                                               | `pdf2zh_next -i input.pdf -o output.pdf -ocr auto`                                                                    |
| `--ocr-args`, `-ocr-args`       | OCR 服务的参数。                                                                        | `pdf2zh_next -i input.pdf -o output.pdf -ocr auto -ocr-args '{"access_key_id": "xxx", "access_key_secret": "xxx"}'`   |
| `--ocr-config`, `-ocr-cfg`      | OCR 服务的配置文件。                                                                    | `pdf2zh_next -i input.pdf -o output.pdf -ocr auto -ocr-cfg config.json`                                               |
| `--parallel`, `-p`              | 并行翻译数量。默认为 `4`。                                                              | `pdf2zh_next -i input.pdf -o output.pdf -p 8`                                                                         |
| `--batch-size`, `-b`            | 每批处理的页数。默认为 `10`。                                                           | `pdf2zh_next -i input.pdf -o output.pdf -b 20`                                                                        |
| `--timeout`, `-to`              | 翻译服务的超时时间（秒）。默认为 `30`。                                                 | `pdf2zh_next -i input.pdf -o output.pdf -to 60`                                                                       |
| `--retry`, `-r`                 | 翻译服务的重试次数。默认为 `3`。                                                        | `pdf2zh_next -i input.pdf -o output.pdf -r 5`                                                                         |
| `--log-level`, `-l`             | 日志级别。默认为 `info`。                                                               | `pdf2zh_next -i input.pdf -o output.pdf -l debug`                                                                     |
| `--log-file`, `-lf`             | 日志文件路径。                                                                          | `pdf2zh_next -i input.pdf -o output.pdf -lf log.txt`                                                                  |
| `--config`, `-c`                | 配置文件路径。                                                                          | `pdf2zh_next -i input.pdf -o output.pdf -c config.json`                                                               |
| `--no-cache`, `-nc`             | 禁用缓存。                                                                              | `pdf2zh_next -i input.pdf -o output.pdf -nc`                                                                          |
| `--cache-dir`, `-cd`            | 缓存目录。默认为 `./.cache`。                                                           | `pdf2zh_next -i input.pdf -o output.pdf -cd /tmp/cache`                                                               |
| `--cache-ttl`, `-ct`            | 缓存 TTL（秒）。默认为 `86400`（1 天）。                                                | `pdf2zh_next -i input.pdf -o output.pdf -ct 3600`                                                                     |
| `--force`, `-f`                 | 即使输出文件已存在也强制翻译。                                                          | `pdf2zh_next -极速翻译 -i input.pdf -o output.pdf -f`                                                                           |
| `--dry-run`, `-极速翻译`              | 不进行实际翻译的试运行。                                                      | `pdf2zh_next -i input.pdf -o output.pdf -极速翻译`                                                                          |
| `--verbose`, `-vb`              | 详细输出。                                                                              | `pdf2zh_next -i input.pdf -o output.pdf -vb`                                                                          |
| `--quiet`, `-q`                 | 静默模式。                                                                              | `pdf2zh_next -i input.pdf -o output.pdf -q`                                                                           |
| `--yes`, `-y`                   | 自动确认所有提示。                                                                      | `pdf 极速翻译 -i input.pdf -o output.pdf -y`                                                                           |
| `--no`, `-n`                    | 自动拒绝所有提示。                                                                      | `pdf2zh_next -i input.pdf -o output.pdf -n`                                                                           |
| `--help-translator`, `-htr`     | 显示翻译服务的帮助信息。                                                                | `pdf2zh_next -htr aliyun`                                                                                             |
| `--help-ocr`, `-hocr`           | 显示 OCR 服务的帮助信息。                                                               | `pdf2zh_next -hocr auto`                                                                                              |
| `--list-translators`, `-l 极速翻译`    | 列出可用的翻译服务。                                                     | `pdf2zh_next -ltr`                                                                                                    |
| `--list-ocr`, `-locr`           | 列出可用的 OCR 服务。                                                                   | `pdf2zh_next -locr`                                                                                                   |
| `--list-languages`, `-ll`       | 列出支持的语言。                                                                        | `pdf2zh_next -ll`                                                                                                     |
| `--update`, `-u`                | 更新到最新版本。                                                                        | `pdf2zh_next -u`                                                                                                      |
| `--self-update`, `-su`          | 自我更新。                                                                              | `pdf2zh_next -su`                                                                                                     |
| `--uninstall`, `-un`            | 卸载 pdf2zh。                                                                           | `pdf2zh_next -un`                                                                                                     |
| `--install`, `-in`              | 安装 pdf2zh。                                                                           | `pdf2zh_next -in`                                                                                                     |
| `--check`, `-chk`               | 检查安装。                                                                              | `pdf2zh_next -chk 极速翻译`                                                                                                    |
| `--doctor`, `-doc`              | 诊断并修复常见问题。                                                                    | `pdf2zh_next -doc`                                                                                                    |
| `--bug-report`, `-br`           | 生成错误报告。                                                                          | `pdf2zh_next -br`                                                                                                     |
| `--feedback`, `-fb`             | 发送反馈。                                                                              | `pdf2zh_next -fb`                                                                                                     |
| `--donate`, `-d`                | 向项目捐赠。                                                                            | `pdf2zh_next -d`                                                                                                      |
| `--sponsor`, `-sp`              | 赞助项目。                                                                              | `pdf2zh_next -sp`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--config`                      | Same as `--config-file`                                                                 | `pdf2zh_next --config /path/to/config/config.toml`                                                                    |
| `--debug`                       | Enable debug mode, which outputs more detailed information                              | `pdf2zh_next --debug`                                                                                                 |
| `--dry-run`                     | Perform a dry run without actually translating any files                                | `pdf2zh_next --dry-run`                                                                                               |
| `--help`, `-h`                  | Show help information                                                                   | `pdf2zh_next --help`                                                                                                  |
| `--output-dir`                  | Specify the output directory for the translated files                                   | `pdf2zh_next --output-dir /path/to/output`                                                                            |
| `--output-file`                 | Specify the output file path                                                            | `pdf2zh_next --output-file /path/to/output/translated_file.pdf`                                                       |
| `--output-prefix`               | Add a prefix to the output file name                                                    | `pdf2zh_next --output-prefix "translated_"`                                                                           |
| `--output-suffix`               | Add a suffix to the output file name                                                    | `pdf2zh_next --output-suffix "_translated"`                                                                           |
| `--overwrite`                   | Overwrite existing files without prompting                                              | `pdf2zh_next --overwrite`                                                                                             |
| `--quiet`, `-q`                 | Run in quiet mode, suppressing non-essential output                                     | `pdf2zh_next --quiet`                                                                                                 |
| `--version`, `-v`               | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `--yes`, `-y`                   | Automatically answer yes to all prompts                                                 | `pdf2zh_next --yes`                                                                                                   |

---

### TRANSLATION RESULT

| `--config-file`                 | 配置文件路径                                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--config`                      | 与 `--config-file` 相同                                                                 | `pdf2zh_next --config /path/to/config/config.toml`                                                                    |
| `--debug`                       | 启用调试模式，输出更详细的信息                                                          | `pdf2zh_next --debug`                                                                                                 |
| `--dry-run`                     | 执行试运行，不实际翻译任何文件                                                          | `pdf2zh_next --dry-run`                                                                                               |
| `--help`, `-h`                  | 显示帮助信息                                                                            | `pdf2zh_next --help`                                                                                                  |
| `--output-dir`                  | 指定翻译后文件的输出目录                                                                | `pdf2zh_next --output-dir /path/to/output`                                                                            |
| `--output-file`                 | 指定输出文件路径                                                                        | `pdf2zh_next --output-file /path/to/output/translated_file.pdf`                                                       |
| `--output-prefix`               | 在输出文件名前添加前缀                                                                  | `pdf2zh_next --output-prefix "translated_"`                                                                           |
| `--output-suffix`               | 在输出文件名后添加后缀                                                                  | `pdf2zh_next --output-suffix "_translated"`                                                                           |
| `--overwrite`                   | 不提示直接覆盖现有文件                                                                  | `pdf2zh_next --overwrite`                                                                                             |
| `--quiet`, `-q`                 | 以静默模式运行，抑制非必要输出                                                          | `pdf2zh_next --quiet`                                                                                                 |
| `--version`, `-v`               | 显示版本信息                                                                            | `pdf2zh_next --version`                                                                                               |
| `--yes`, `-y`                   | 自动对所有提示回答“是”                                                                  | `pdf2zh_next --yes`                                                                                                   |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--report-interval`             | 进度报告间隔（秒）                                                                      | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--report-interval`             | 进度报告间隔（秒）                                                                      | `pdf2zh_next example.pdf --report-interval 5`                                                                         |

---

### OUTPUT

| `--report-interval`             | 进度报告间隔（秒）                                                                      | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--report-interval`             | 进度报告间隔（秒）                                                                      | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--report-interval`             | 进度报告间隔（秒）                                                                      | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--verbose`                     | Use verbose logging level                                                               | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--log-level`                   | Set the log level. Choices: `debug`, `info`, `warning`, `error`, `critical`             | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | Log to a file instead of stdout                                                         | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `-v`, `--version`               | Show the version and exit                                                               | `pdf2zh_next -v`                                                                                                      |
| `-h`, `--help`                  | Show this help message and exit                                                         | `pdf2zh_next -h`                                                                                                      |

---

### OUTPUT

| `--debug`                       | 使用调试日志级别                                                                        | `pdf2zh_next example.pdf --debug`                                                                                     |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--verbose`                     | 使用详细日志级别                                                                        | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--log-level`                   | 设置日志级别。选项：`debug`、`info`、`warning`、`error`、`critical`                     | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | 将日志输出到文件而非标准输出                                                            | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `-v`, `--version`               | 显示版本信息并退出                                                                      | `pdf2zh_next -v`                                                                                                      |
| `-h`, `--help`                  | 显示帮助信息并退出                                                                      | `pdf2zh_next -h`                                                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--webui`                       | Start webui server                                                                      | `pdf2zh_next --webui`                                                                                                 | 
| `--port <port>`                 | Specify the port for the webui server. Default is `7860`                                 | `pdf2zh_next --webui --port 7861`                                                                                     | 
| `--host <host>`                 | Specify the host for the webui server. Default is `127.0.0.1`                           | `pdf2zh_next --webui --host 0.0.0.0`                                                                                  | 
| `--share`                       | Create a public link for the webui server (using Gradio share)                           | `pdf2zh_next --webui --share`                                                                                         | 
| `--auth <username:password>`    | Set username and password for webui access (comma-separated for multiple users)         | `pdf2zh_next --webui --auth "user1:pass1,user2:pass2"`                                                                | 
| `--ssl-keyfile <path>`          | Specify the path to the SSL key file for HTTPS                                           | `pdf2zh_next --webui --ssl-keyfile key.pem`                                                                           | 
| `--ssl-certfile <path>`         | Specify the path to the SSL certificate file for HTTPS                                   | `pdf2zh_next --webui --ssl-certfile cert.pem`                                                                         | 

---

### OUTPUT

| `--gui`                         | 与 GUI 交互                                                                             | `pdf2zh_next --gui`                                                                                                   | 
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--webui`                       | 启动 webui 服务器                                                                       | `pdf2zh_next --webui`                                                                                                 | 
| `--port <port>`                 | 指定 webui 服务器的端口。默认为 `7860`                                                  | `pdf2zh_next --webui --port 7861`                                                                                     | 
| `--host <host>`                 | 指定 webui 服务器的主机。默认为 `127.0.0.1`                                             | `pdf2zh_next --webui --host 0.0.0.0`                                                                                  | 
| `--share`                       | 为 webui 服务器创建公共链接（使用 Gradio share）                                        | `pdf2zh_next --webui --share`                                                                                         | 
| `--auth <username:password>`    | 设置 webui 访问的用户名和密码（多个用户用逗号分隔）                                     | `pdf2zh_next --webui --auth "user1:pass1,user2:pass2"`                                                                | 
| `--ssl-keyfile <path>`          | 指定 HTTPS 的 SSL 密钥文件路径                                                          | `pdf2zh_next --webui --ssl-keyfile key.pem`                                                                           | 
| `--ssl-certfile <path>`         | 指定 HTTPS 的 SSL 证书文件路径                                                          | `pdf2zh_next --webui --ssl-certfile cert.pem`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--download-only`               | Only download required assets then exit                                                 | `pdf2zh_next example.pdf --download-only`                                                                             |
| `--output-dir <output-dir>`     | Specify the output directory, default is `./output`                                     | `pdf2zh_next example.pdf --output-dir ./my_output`                                                                    |
| `--output-name <output-name>`   | Specify the output name, default is `{input_name}_translated.pdf`                       | `pdf2zh_next example.pdf --output-name my_translation.pdf`                                                            |
| `--output-format <format>`      | Specify the output format, choices are `pdf`, `markdown`, `html`, `json`, default `pdf` | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--target-lang <lang-code>`     | Specify the target language, default is `zh`                                           | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--engine <engine>`             | Specify the translation engine, default is `openai`                                     | `pdf2zh_next example.pdf --engine openai`                                                                             |
| `--model <model>`               | Specify the model for the translation engine                                            | `pdf2zh_next example.pdf --engine openai --model gpt-4o`                                                              |
| `--api-key <api-key>`           | Specify the API key for the translation engine                                          | `pdf2zh_next example.pdf --engine openai --api-key sk-...`                                                            |
| `--api-base <api-base>`         | Specify the API base URL for the translation engine                                     | `pdf2zh_next example.pdf --engine openai --api-base https://api.openai.com/v1`                                        |
| `--proxy <proxy>`               | Specify the proxy for the translation engine                                            | `pdf2zh_next example.pdf --engine openai --proxy http://127.0.0.1:7890`                                               |
| `--max-concurrent-requests`     | Maximum concurrent requests for translation, default is `3`                             | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 |
| `--max-tokens-per-request`      | Maximum tokens per request for translation, default is `4096`                          | `pdf2zh_next example.pdf --max-tokens-per-request 2048`                                                               |
| `--ocr`                         | Enable OCR for better text extraction, default is `false`                              | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-engine <ocr-engine>`     | Specify the OCR engine, choices are `paddle`, `tesseract`, default `paddle`             | `pdf2zh_next example.pdf --ocr --ocr-engine tesseract`                                                                |
| `--ocr-lang <ocr-lang>`         | Specify the OCR language, default is `en`                                               | `pdf2zh_next example.pdf --ocr --ocr-lang ja`                                                                         |
| `--ocr-dpi <dpi>`               | Specify the OCR DPI, default is `300`                                                   | `pdf2zh_next example.pdf --ocr --ocr-dpi 150`                                                                        |
| `--ocr-timeout <timeout>`       | Specify the OCR timeout in seconds, default is `30`                                     | `pdf2zh_next example.pdf --ocr --ocr-timeout 60`                                                                      |
| `--ocr-max-workers`             | Maximum workers for OCR, default is `4`                                                 | `pdf2zh_next example.pdf --ocr --ocr-max-workers 8`                                                                   |
| `--font <font>`                 | Specify the font for the output PDF, default is `Noto Sans CJK SC`                      | `pdf2zh_next example.pdf --font "Source Han Sans CN"`                                                                 |
| `--font-size <font-size>`       | Specify the font size for the output PDF, default is `10`                               | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing <line-spacing>` | Specify the line spacing for the output PDF, default is `1.2`                           | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--margin <margin>`             | Specify the margin for the output PDF, default is `72`                                   | `pdf2zh_next example.pdf --margin 36`                                                                                 |
| `--page-size <page-size>`       | Specify the page size for the output PDF, default is `A4`                               | `pdf2zh_next example.pdf --page-size Letter`                                                                          |
| `--retry <retry>`               | Specify the number of retries for failed requests, default is `3`                       | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--retry-delay <retry-delay>`   | Specify the delay between retries in seconds, default is `1`                             | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |
| `--timeout <timeout>`           | Specify the timeout for each request in seconds, default is `30`                        | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--verbose`                     | Enable verbose logging                                                                  | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | Show the version number and exit                                                        | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show this help message and exit                                                         | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT

| `--warmup`                      | 仅下载并验证所需资源后退出                                                 | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--download-only`               | 仅下载所需资源后退出                                                       | `pdf2zh_next example.pdf --download-only`                                                                             |
| `--output-dir <output-dir>`     | 指定输出目录，默认为 `./output`                                            | `pdf2zh_next example.pdf --output-dir ./my_output`                                                                    |
| `--output-name <output-name>`   | 指定输出文件名，默认为 `{input_name}_translated.pdf`                       | `pdf2zh_next example.pdf --output-name my_translation.pdf`                                                            |
| `--output-format <format>`      | 指定输出格式，可选值为 `pdf`、`markdown`、`html`、`json`，默认为 `pdf`      | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--target-lang <lang-code>`     | 指定目标语言，默认为 `zh`                                                  | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--engine <engine>`             | 指定翻译引擎，默认为 `openai`                                              | `pdf2zh_next example.pdf --engine openai`                                                                             |
| `--model <model>`               | 指定翻译引擎使用的模型                                                     | `pdf2zh_next example.pdf --engine openai --model gpt-4o`                                                              |
| `--api-key <api-key>`           | 指定翻译引擎的 API 密钥                                                    | `pdf2zh_next example.pdf --engine openai --api-key sk-...`                                                            |
| `--api-base <api-base>`         | 指定翻译引擎的 API 基础 URL                                                | `pdf2zh_next example.pdf --engine openai --api-base https://api.openai.com/v1`                                        |
| `--proxy <proxy>`               | 指定翻译引擎使用的代理                                                     | `pdf2zh_next example.pdf --engine openai --proxy http://127.0.0.1:7890`                                               |
| `--max-concurrent-requests`     | 翻译的最大并发请求数，默认为 `3`                                           | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 |
| `--max-tokens-per-request`      | 每次翻译请求的最大 token 数，默认为 `4096`                                 | `pdf2zh_next example.pdf --max-tokens-per-request 2048`                                                               |
| `--ocr`                         | 启用 OCR 以改善文本提取效果，默认为 `false`                                | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-engine <ocr-engine>`     | 指定 OCR 引擎，可选值为 `paddle`、`tesseract`，默认为 `paddle`             | `pdf2zh_next example.pdf --ocr --ocr-engine tesseract`                                                                |
| `--ocr-lang <ocr-lang>`         | 指定 OCR 语言，默认为 `en`                                                 | `pdf2zh_next example.pdf --ocr --ocr-lang ja`                                                                         |
| `--ocr-dpi <dpi>`               | 指定 OCR 的 DPI，默认为 `300`                                              | `pdf2zh_next example.pdf --ocr --ocr-dpi 150`                                                                        |
| `--ocr-timeout <timeout>`       | 指定 OCR 的超时时间（秒），默认为 `30`                                     | `pdf2zh_next example.pdf --ocr --ocr-timeout 60`                                                                      |
| `--ocr-max-workers`             | OCR 的最大工作线程数，默认为 `4`                                           | `pdf2zh_next example.pdf --ocr --ocr-max-workers 8`                                                                   |
| `--font <font>`                 | 指定输出 PDF 的字体，默认为 `Noto Sans CJK SC`                             | `pdf2zh_next example.pdf --font "Source Han Sans CN"`                                                                 |
| `--font-size <font-size>`       | 指定输出 PDF 的字体大小，默认为 `10`                                       | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing <line-spacing>` | 指定输出 PDF 的行间距，默认为 `1.2`                                        | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--margin <margin>`             | 指定输出 PDF 的页边距，默认为 `72`                                         | `pdf2zh_next example.pdf --margin 36`                                                                                 |
| `--page-size <page-size>`       | 指定输出 PDF 的页面大小，默认为 `A4`                                       | `pdf2zh_next example.pdf --page-size Letter`                                                                          |
| `--retry <retry>`               | 指定失败请求的重试次数，默认为 `3`                                         | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--retry-delay <retry-delay>`   | 指定重试之间的延迟时间（秒），默认为 `1`                                   | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |
| `--timeout <timeout>`           | 指定每个请求的超时时间（秒），默认为 `30`                                  | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--verbose`                     | 启用详细日志记录                                                           | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | 显示版本号并退出                                                           | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 显示此帮助信息并退出                                                       | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`, `-o`            | Specify the output directory for the generated files                                    | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-filename`             | Specify the output filename for the generated files                                     | `pdf2zh_next example.pdf --output-filename my_output`                                                                 |
| `--output-format`               | Specify the output format for the generated files (default: `pdf`)                      | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--output-language`, `-l`       | Specify the output language for the generated files (default: `zh`)                     | `pdf2zh_next example.pdf --output-language en`                                                                        |
| `--output-ocr-language`, `-ol`  | Specify the output OCR language for the generated files (default: `zh`)                 | `pdf2zh_next example.pdf --output-ocr-language en`                                                                    |
| `--output-ocr-engine`           | Specify the output OCR engine for the generated files (default: `easyocr`)              | `pdf2zh_next example.pdf --output-ocr-engine paddleocr`                                                               |
| `--output-translation-service`  | Specify the output translation service for the generated files (default: `google`)      | `pdf2zh_next example.pdf --output-translation-service deepl`                                                          |
| `--output-translation-key`      | Specify the output translation key for the generated files (optional)                   | `pdf2zh_next example.pdf --output-translation-key YOUR_API_KEY`                                                       |
| `--output-translation-region`   | Specify the output translation region for the generated files (optional)                | `pdf2zh_next example.pdf --output-translation-region eastus`                                                          |
| `--output-translation-endpoint` | Specify the output translation endpoint for the generated files (optional)              | `pdf2zh_next example.pdf --output-translation-endpoint https://api.cognitive.microsofttranslator.com`                 |
| `--output-translation-model`    | Specify the output translation model for the generated files (optional)                 | `pdf2zh_next example.pdf --output-translation-model gpt-4`                                                            |
| `--output-translation-prompt`   | Specify the output translation prompt for the generated files (optional)                | `pdf2zh_next example.pdf --output-translation-prompt "You are a helpful assistant that translates text to Chinese."`  |
| `--output-translation-timeout`  | Specify the output translation timeout for the generated files (optional)               | `pdf2zh_next example.pdf --output-translation-timeout 30`                                                             |
| `--output-translation-retry`    | Specify the output translation retry times for the generated files (optional)           | `pdf2zh_next example.pdf --output-translation-retry 3`                                                                |
| `--output-translation-backoff`  | Specify the output translation backoff factor for the generated files (optional)        | `pdf2zh_next example.pdf --output-translation-backoff 2`                                                              |
| `--output-translation-max-tokens` | Specify the output translation max tokens for the generated files (optional)            | `pdf2zh_next example.pdf --output-translation-max-tokens 4096`                                                        |
| `--output-translation-temperature` | Specify the output translation temperature for the generated files (optional)           | `pdf2zh_next example.pdf --output-translation-temperature 0.7`                                                        |
| `--output-translation-top-p`    | Specify the output translation top p for the generated files (optional)                 | `pdf2zh_next example.pdf --output-translation-top-p 0.9`                                                              |
| `--output-translation-frequency-penalty` | Specify the output translation frequency penalty for the generated files (optional) | `pdf2zh_next example.pdf --output-translation-frequency-penalty 0.5`                                                  |
| `--output-translation-presence-penalty` | Specify the output translation presence penalty for the generated files (optional)   | `pdf2zh_next example.pdf --output-translation-presence-penalty 0.5`                                                   |
| `--output-translation-stop`     | Specify the output translation stop sequences for the generated files (optional)        | `pdf2zh_next example.pdf --output-translation-stop "。\n"`                                                            |
| `--output-translation-logprobs` | Specify the output translation logprobs for the generated files (optional)             | `pdf2zh_next example.pdf --output-translation-logprobs 5`                                                             |
| `--output-translation-echo`     | Specify the output translation echo for the generated files (optional)                 | `pdf2zh_next example.pdf --output-translation-echo true`                                                              |
| `--output-translation-n`        | Specify the output translation n for the generated files (optional)                    | `pdf2zh_next example.pdf --output-translation-n 1`                                                                    |
| `--output-translation-stream`   | Specify the output translation stream for the generated files (optional)               | `pdf2zh_next example.pdf --output-translation-stream false`                                                           |
| `--output-translation-suffix`   | Specify the output translation suffix for the generated files (optional)               | `pdf2zh_next example.pdf --output-translation-suffix " (translated)"`                                                 |
| `--output-translation-user`     | Specify the output translation user for the generated files (optional)                 | `pdf2zh_next example.pdf --output-translation-user "user-123"`                                                        |
| `--output-translation-encoding` | Specify the output translation encoding for the generated files (optional)             | `pdf2zh_next example.pdf --output-translation-encoding utf-8`                                                         |
| `--output-translation-format`   | Specify the output translation format for the generated files (optional)               | `pdf2zh_next example.pdf --output-translation-format text`                                                            |
| `--output-translation-style`    | Specify the output translation style for the generated files (optional)                | `pdf2zh_next example.pdf --output-translation-style formal`                                                           |
| `--output-translation-profile`  | Specify the output translation profile for the generated files (optional)              | `pdf2zh_next example.pdf --output-translation-profile technical`                                                      |
| `--output-translation-glossary` | Specify the output translation glossary for the generated files (optional)             | `pdf2zh_next example.pdf --output-translation-glossary /path/to/glossary.json`                                        |
| `--output-translation-context`  | Specify the output translation context for the generated files (optional)              | `pdf2zh_next example.pdf --output-translation-context "This is a technical document."`                                |
| `--output-translation-domain`   | Specify the output translation domain for the generated files (optional)               | `pdf2zh_next example.pdf --output-translation-domain IT`                                                              |
| `--output-translation-category` | Specify the output translation category for the generated files (optional)             | `pdf2zh_next example.pdf --output-translation-category general`                                                       |

---

### OUTPUT

| `--generate-offline-assets`     | 在指定目录中生成离线资源包                                                                      | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`, `-o`            | 指定生成文件的输出目录                                                                          | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-filename`             | 指定生成文件的输出文件名                                                                        | `pdf2zh_next example.pdf --output-filename my_output`                                                                 |
| `--output-format`               | 指定生成文件的输出格式（默认：`pdf`）                                                            | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--output-language`, `-l`       | 指定生成文件的输出语言（默认：`zh`）                                                            | `pdf2zh_next example.pdf --output-language en`                                                                        |
| `--output-ocr-language`, `-ol`  | 指定生成文件的输出 OCR 语言（默认：`zh`）                                                        | `pdf2zh_next example.pdf --output-ocr-language en`                                                                    |
| `--output-ocr-engine`           | 指定生成文件的输出 OCR 引擎（默认：`easyocr`）                                                   | `pdf2zh_next example.pdf --output-ocr-engine paddleocr`                                                               |
| `--output-translation-service`  | 指定生成文件的输出翻译服务（默认：`google`）                                                     | `pdf2zh_next example.pdf --output-translation-service deepl`                                                          |
| `--output-translation-key`      | 指定生成文件的输出翻译密钥（可选）                                                              | `pdf2zh_next example.pdf --output-translation-key YOUR_API_KEY`                                                       |
| `--output-translation-region`   | 指定生成文件的输出翻译区域（可选）                                                              | `pdf2zh_next example.pdf --output-translation-region eastus`                                                          |
| `--output-translation-endpoint` | 指定生成文件的输出翻译端点（可选）                                                              | `pdf2zh_next example.pdf --output-translation-endpoint https://api.cognitive.microsofttranslator.com`                 |
| `--output-translation-model`    | 指定生成文件的输出翻译模型（可选）                                                              | `pdf2zh_next example.pdf --output-translation-model gpt-4`                                                            |
| `--output-translation-prompt`   | 指定生成文件的输出翻译提示（可选）                                                              | `pdf2zh_next example.pdf --output-translation-prompt "You are a helpful assistant that translates text to Chinese."`  |
| `--output-translation-timeout`  | 指定生成文件的输出翻译超时时间（可选）                                                          | `pdf2zh_next example.pdf --output-translation-timeout 30`                                                             |
| `--output-translation-retry`    | 指定生成文件的输出翻译重试次数（可选）                                                          | `pdf2zh_next example.pdf --output-translation-retry 3`                                                                |
| `--output-translation-backoff`  | 指定生成文件的输出翻译退避因子（可选）                                                          | `pdf2zh_next example.pdf --output-translation-backoff 2`                                                              |
| `--output-translation-max-tokens` | 指定生成文件的输出翻译最大令牌数（可选）                                                        | `pdf2zh_next example.pdf --output-translation-max-tokens 4096`                                                        |
| `--output-translation-temperature` | 指定生成文件的输出翻译温度（可选）                                                              | `pdf2zh_next example.pdf --output-translation-temperature 0.7`                                                        |
| `--output-translation-top-p`    | 指定生成文件的输出翻译 top p（可选）                                                            | `pdf2zh_next example.pdf --output-translation-top-p 0.9`                                                              |
| `--output-translation-frequency-penalty` | 指定生成文件的输出翻译频率惩罚（可选）                                                  | `pdf2zh_next example.pdf --output-translation-frequency-penalty 0.5`                                                  |
| `--output-translation-presence-penalty` | 指定生成文件的输出翻译存在惩罚（可选）                                                    | `pdf2zh_next example.pdf --output-translation-presence-penalty 0.5`                                                   |
| `--output-translation-stop`     | 指定生成文件的输出翻译停止序列（可选）                                                          | `pdf2zh_next example.pdf --output-translation-stop "。\n"`                                                            |
| `--output-translation-logprobs` | 指定生成文件的输出翻译对数概率（可选）                                                          | `pdf2zh_next example.pdf --output-translation-logprobs 5`                                                             |
| `--output-translation-echo`     | 指定生成文件的输出翻译回显（可选）                                                              | `pdf2zh_next example.pdf --output-translation-echo true`                                                              |
| `--output-translation-n`        | 指定生成文件的输出翻译 n（可选）                                                                | `pdf2zh_next example.pdf --output-translation-n 1`                                                                    |
| `--output-translation-stream`   | 指定生成文件的输出翻译流（可选）                                                                | `pdf2zh_next example.pdf --output-translation-stream false`                                                           |
| `--output-translation-suffix`   | 指定生成文件的输出翻译后缀（可选）                                                              | `pdf2zh_next example.pdf --output-translation-suffix " (translated)"`                                                 |
| `--output-translation-user`     | 指定生成文件的输出翻译用户（可选）                                                              | `pdf2zh_next example.pdf --output-translation-user "user-123"`                                                        |
| `--output-translation-encoding` | 指定生成文件的输出翻译编码（可选）                                                              | `pdf2zh_next example.pdf --output-translation-encoding utf-8`                                                         |
| `--output-translation-format`   | 指定生成文件的输出翻译格式（可选）                                                              | `pdf2zh_next example.pdf --output-translation-format text`                                                            |
| `--output-translation-style`    | 指定生成文件的输出翻译风格（可选）                                                              | `pdf2zh_next example.pdf --output-translation-style formal`                                                           |
| `--output-translation-profile`  | 指定生成文件的输出翻译配置文件（可选）                                                          | `pdf2zh_next example.pdf --output-translation-profile technical`                                                      |
| `--output-translation-glossary` | 指定生成文件的输出翻译术语表（可选）                                                            | `pdf2zh_next example.pdf --output-translation-glossary /path/to/glossary.json`                                        |
| `--output-translation-context`  | 指定生成文件的输出翻译上下文（可选）                                                            | `pdf2zh_next example.pdf --output-translation-context "This is a technical document."`                                |
| `--output-translation-domain`   | 指定生成文件的输出翻译领域（可选）                                                              | `pdf2zh_next example.pdf --output-translation-domain IT`                                                              |
| `--output-translation-category` | 指定生成文件的输出翻译类别（可选）                                                              | `pdf2zh_next example.pdf --output-translation-category general`                                                       |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--restore-offline-assets-only` | Only restore offline assets package from the specified directory, and exit the program   | `pdf2zh_next example.pdf --restore-offline-assets-only /path`                                                         |
| `--offline-assets-dir`          | Specify the directory to store offline assets                                            | `pdf2zh_next example.pdf --offline-assets-dir /path/to/offline_assets`                                               |
| `--save-offline-assets`         | Save offline assets package to the specified directory                                   | `pdf2zh_next example.pdf --save-offline-assets /path`                                                                 |
| `--save-offline-assets-only`    | Only save offline assets package to the specified directory, and exit the program        | `pdf2zh_next example.pdf --save-offline-assets-only /path`                                                            |
| `--offline`                     | Enable offline mode, which will use local assets only                                    | `pdf2zh_next example.pdf --offline`                                                                                   |

---

### OUTPUT

| `--restore-offline-assets`      | 从指定目录恢复离线资源包                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--restore-offline-assets-only` | 仅从指定目录恢复离线资源包，然后退出程序   | `pdf2zh_next example.pdf --restore-offline-assets-only /path`                                                         |
| `--offline-assets-dir`          | 指定存储离线资源的目录                                            | `pdf2zh_next example.pdf --offline-assets-dir /path/to/offline_assets`                                               |
| `--save-offline-assets`         | 将离线资源包保存到指定目录                                   | `pdf2zh_next example.pdf --save-offline-assets /path`                                                                 |
| `--save-offline-assets-only`    | 仅将离线资源包保存到指定目录，然后退出程序        | `pdf2zh_next example.pdf --save-offline-assets-only /path`                                                            |
| `--offline`                     | 启用离线模式，仅使用本地资源                                    | `pdf2zh_next example.pdf --offline`                                                                                   |
---

### OUTPUT

| `--version`                     | 显示版本号后退出                                                                  | `pdf2zh_next --version`                                                                                               |
Translate only pages 1,2,3,5, and all pages after page 5. The page numbers are separated by commas, and ranges can be specified using `-`. |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `--output`                      | Specify the output file name                                                            | `pdf2zh_next example.pdf --output example_zh.pdf`                                                                     | Specify the output file name. If not specified, the default output file name is `{original_name}_zh.pdf`.                                  |
| `--output-dir`                  | Specify the output directory                                                            | `pdf2zh_next example.pdf --output-dir ./output`                                                                       | Specify the output directory. If not specified, the default output directory is the same as the input file.                                |
| `--engine`                      | Specify the translation engine                                                          | `pdf2zh_next example.pdf --engine aliyun`                                                                             | Specify the translation engine. If not specified, the default engine is `aliyun`.                                                          |
| `--lang`                        | Specify the target language                                                             | `pdf2zh_next example.pdf --lang ja`                                                                                   | Specify the target language. If not specified, the default target language is `zh`.                                                        |
| `--api-key`                     | Specify the API key for the translation engine                                          | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      | Specify the API key for the translation engine. If not specified, the program will try to read the API key from the environment variable. |
| `--api-secret`                  | Specify the API secret for the translation engine                                       | `pdf2zh_next example.pdf --api-secret YOUR_API_SECRET`                                                                | Specify the API secret for the translation engine. If not specified, the program will try to read the API secret from the environment variable. |
| `--api-region`                  | Specify the API region for the translation engine                                       | `pdf2zh_next example.pdf --api-region YOUR_API_REGION`                                                                | Specify the API region for the translation engine. If not specified, the program will try to read the API region from the environment variable. |
| `--api-base-url`                | Specify the API base URL for the translation engine                                     | `pdf2zh_next example.pdf --api-base-url YOUR_API_BASE_URL`                                                            | Specify the API base URL for the translation engine. If not specified, the program will use the default API base URL.                      |
| `--api-version`                 | Specify the API version for the translation engine                                      | `pdf2zh_next example.pdf --api-version YOUR_API_VERSION`                                                              | Specify the API version for the translation engine. If not specified, the program will use the default API version.                        |
| `--api-model`                   | Specify the API model for the translation engine                                        | `pdf2zh_next example.pdf --api-model YOUR_API_MODEL`                                                                  | Specify the API model for the translation engine. If not specified, the program will use the default API model.                            |
| `--concurrency`                 | Specify the number of concurrent translation requests                                   | `pdf2zh_next example.pdf --concurrency 10`                                                                            | Specify the number of concurrent translation requests. If not specified, the default value is 5.                                            |
| `--timeout`                     | Specify the timeout for each translation request                                        | `pdf2zh_next example.pdf --timeout 30`                                                                                | Specify the timeout for each translation request. If not specified, the default value is 30 seconds.                                       |
| `--retry`                       | Specify the number of retries for failed translation requests                           | `pdf2zh_next example.pdf --retry 3`                                                                                   | Specify the number of retries for failed translation requests. If not specified, the default value is 3.                                   |
| `--retry-delay`                 | Specify the delay between retries                                                       | `pdf2zh_next example.pdf --retry-delay 1`                                                                             | Specify the delay between retries. If not specified, the default value is 1 second.                                                         |
| `--no-cache`                    | Disable caching of translation results                                                  | `pdf2zh_next example.pdf --no-cache`                                                                                  | Disable caching of translation results. If not specified, the program will cache translation results by default.                            |
| `--cache-dir`                   | Specify the cache directory                                                             | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         | Specify the cache directory. If not specified, the default cache directory is `~/.cache/pdf2zh_next`.                                      |
| `--cache-ttl`                   | Specify the cache time-to-live                                                          | `pdf2zh_next example.pdf --cache-ttl 3600`                                                                            | Specify the cache time-to-live. If not specified, the default value is 3600 seconds (1 hour).                                                |
| `--dry-run`                     | Perform a dry run without actually translating the document                             | `pdf2zh_next example.pdf --dry-run`                                                                                   | Perform a dry run without actually translating the document.                                                                               |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   | Enable verbose output.                                                                                                                     |
| `--version`                     | Show the version of the program                                                         | `pdf2zh_next --version`                                                                                               | Show the version of the program.                                                                                                           |
| `--help`                        | Show the help message                                                                   | `pdf2zh_next --help`                                                                                                  | Show the help message.                                                                                                                     |

---

### TRANSLATION RESULT

| `--pages`                       | 部分文档翻译                                                              | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | 仅翻译第 1、2、3、5 页以及第 5 页之后的所有页面。页码以逗号分隔，可以使用 `-` 指定范围。 |
| ------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `--output`                      | 指定输出文件名                                                            | `pdf2zh_next example.pdf --output example_zh.pdf`                                                                     | 指定输出文件名。如果未指定，默认输出文件名为 `{original_name}_zh.pdf`。                  |
| `--output-dir`                  | 指定输出目录                                                              | `pdf2zh_next example.pdf --output-dir ./output`                                                                       | 指定输出目录。如果未指定，默认输出目录与输入文件相同。                                    |
| `--engine`                      | 指定翻译引擎                                                              | `pdf2zh_next example.pdf --engine aliyun`                                                                             | 指定翻译引擎。如果未指定，默认引擎为 `aliyun`。                                          |
| `--lang`                        | 指定目标语言                                                              | `pdf2zh_next example.pdf --lang ja`                                                                                   | 指定目标语言。如果未指定，默认目标语言为 `zh`。                                          |
| `--api-key`                     | 指定翻译引擎的 API 密钥                                                   | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      | 指定翻译引擎的 API 密钥。如果未指定，程序将尝试从环境变量中读取 API 密钥。               |
| `--api-secret`                  | 指定翻译引擎的 API 密钥                                                   | `pdf2zh_next example.pdf --api-secret YOUR_API_SECRET`                                                                | 指定翻译引擎的 API 密钥。如果未指定，程序将尝试从环境变量中读取 API 密钥。               |
| `--api-region`                  | 指定翻译引擎的 API 区域                                                   | `pdf2zh_next example.pdf --api-region YOUR_API_REGION`                                                                | 指定翻译引擎的 API 区域。如果未指定，程序将尝试从环境变量中读取 API 区域。               |
| `--api-base-url`                | 指定翻译引擎的 API 基础 URL                                               | `pdf2zh_next example.pdf --api-base-url YOUR_API_BASE_URL`                                                            | 指定翻译引擎的 API 基础 URL。如果未指定，程序将使用默认的 API 基础 URL。                 |
| `--api-version`                 | 指定翻译引擎的 API 版本                                                   | `pdf2zh_next example.pdf --api-version YOUR_API_VERSION`                                                              | 指定翻译引擎的 API 版本。如果未指定，程序将使用默认的 API 版本。                         |
| `--api-model`                   | 指定翻译引擎的 API 模型                                                   | `pdf2zh_next example.pdf --api-model YOUR_API_MODEL`                                                                  | 指定翻译引擎的 API 模型。如果未指定，程序将使用默认的 API 模型。                         |
| `--concurrency`                 | 指定并发翻译请求的数量                                                    | `pdf2zh_next example.pdf --concurrency 10`                                                                            | 指定并发翻译请求的数量。如果未指定，默认值为 5。                                         |
| `--timeout`                     | 指定每个翻译请求的超时时间                                                | `pdf2zh_next example.pdf --timeout 30`                                                                                | 指定每个翻译请求的超时时间。如果未指定，默认值为 30 秒。                                 |
| `--retry`                       | 指定失败翻译请求的重试次数                                                | `pdf2zh_next example.pdf --retry 3`                                                                                   | 指定失败翻译请求的重试次数。如果未指定，默认值为 3。                                     |
| `--retry-delay`                 | 指定重试之间的延迟                                                        | `pdf2zh_next example.pdf --retry-delay 1`                                                                             | 指定重试之间的延迟。如果未指定，默认值为 1 秒。                                          |
| `--no-cache`                    | 禁用翻译结果的缓存                                                        | `pdf2zh_next example.pdf --no-cache`                                                                                  | 禁用翻译结果的缓存。如果未指定，程序默认会缓存翻译结果。                                 |
| `--cache-dir`                   | 指定缓存目录                                                              | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         | 指定缓存目录。如果未指定，默认缓存目录为 `~/.cache/pdf2zh_next`。                        |
| `--cache-ttl`                   | 指定缓存的生存时间                                                        | `pdf2zh_next example.pdf --cache-ttl 3600`                                                                            | 指定缓存的生存时间。如果未指定，默认值为 3600 秒（1 小时）。                             |
| `--dry-run`                     | 执行试运行而不实际翻译文档                                                | `pdf2zh_next example.pdf --dry-run`                                                                                   | 执行试运行而不实际翻译文档。                                                             |
| `--verbose`                     | 启用详细输出                                                              | `pdf2zh_next example.pdf --verbose`                                                                                   | 启用详细输出。                                                                           |
| `--version`                     | 显示程序版本                                                              | `pdf2zh_next --version`                                                                                               | 显示程序版本。                                                                           |
| `--help`                        | 显示帮助信息                                                              | `pdf2zh_next --help`                                                                                                  | 显示帮助信息。                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               |
| `--translator`                  | Translation service to use                                                              | `pdf2zh_next example.pdf --translator aliyun`                                                                         |
| `--translator-config`           | Path to the translator configuration file                                               | `pdf2zh_next example.pdf --translator-config ./config/translator.json`                                                |
| `--translator-config-json`      | Translator configuration in JSON format                                                 | `pdf2zh_next example.pdf --translator-config-json '{"translator": "aliyun", "config": {"access_key_id": "xxx", "access_key_secret": "xxx"}}'` |
| `--translator-config-base64`    | Base64 encoded translator configuration                                                 | `pdf2zh_next example.pdf --translator-config-base64 "eyJ0cmFuc2xhdG9yIjogImFsaXl1biIsICJjb25maWciOiB7ImFjY2Vzc19rZXlfaWQiOiAieHh4IiwgImFjY2Vzc19rZXlfc2VjcmV0IjogInh4eCJ9fQ=="` |
| `--translator-options`          | Additional options for the translator                                                   | `pdf2zh_next example.pdf --translator-options '{"key": "value"}'`                                                     |
| `--translator-options-base64`   | Base64 encoded additional options for the translator                                    | `pdf2zh_next example.pdf --translator-options-base64 "eyJrZXkiOiAidmFsdWUifQ=="`                                      |
| `--translator-options-json`     | Additional options for the translator in JSON format                                    | `pdf2zh_next example.pdf --translator-options-json '{"key": "value"}'`                                                |

---

### OUTPUT

| `--lang-in`                     | 源语言代码                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | 目标语言代码                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               |
| `--translator`                  | 使用的翻译服务                                                              | `pdf2zh_next example.pdf --translator aliyun`                                                                         |
| `--translator-config`           | 翻译器配置文件路径                                               | `pdf2zh_next example.pdf --translator-config ./config/translator.json`                                                |
| `--translator-config-json`      | JSON 格式的翻译器配置                                                 | `pdf2zh_next example.pdf --translator-config-json '{"translator": "aliyun", "config": {"access_key_id": "xxx", "access_key_secret": "xxx"}}'` |
| `--translator-config-base64`    | Base64 编码的翻译器配置                                                 | `pdf2zh_next example.pdf --translator-config-base64 "eyJ0cmFuc2xhdG9yIjogImFsaXl1biIsICJjb25maWciOiB7ImFjY2Vzc19rZXlfaWQiOiAieHh4IiwgImFjY2Vzc19rZXlfc2VjcmV0IjogInh4eCJ9fQ=="` |
| `--translator-options`          | 翻译器的附加选项                                                   | `pdf2zh_next example.pdf --translator-options '{"key": "value"}'`                                                     |
| `--translator-options-base64`   | Base64 编码的翻译器附加选项                                    | `pdf2zh_next example.pdf --translator-options-base64 "eyJrZXkiOiAidmFsdWUifQ=="`                                      |
| `--translator-options-json`     | JSON 格式的翻译器附加选项                                    | `pdf2zh_next example.pdf --translator-options-json '{"key": "value"}'`                                                |
[Language Code](https://pdf2zh-next.com/getting-started/LANGUAGE_CODE.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--translator`                  | Translation service                                                                     | `pdf2zh_next example.pdf --translator aliyun`                                                                         | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-api-key`          | API key for the translation service                                                     | `pdf2zh_next example.pdf --translator aliyun --translator-api-key YOUR_API_KEY`                                       | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-api-endpoint`     | API endpoint for the translation service                                                | `pdf2zh_next example.pdf --translator aliyun --translator-api-endpoint YOUR_API_ENDPOINT`                             | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-api-region`       | API region for the translation service                                                  | `pdf2zh_next example.pdf --translator aliyun --translator-api-region YOUR_API_REGION`                                  | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-model`            | Model name for the translation service                                                  | `pdf2zh_next example.pdf --translator siliconflow --translator-model YOUR_MODEL_NAME`                                 | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-api-version`      | API version for the translation service                                                 | `pdf2zh_next example.pdf --translator azure --translator-api-version YOUR_API_VERSION`                                | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-extra-params`     | Extra parameters for the translation service                                            | `pdf2zh_next example.pdf --translator openai --translator-extra-params '{"temperature": 0.7}'`                        | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-timeout`          | Timeout for the translation service (seconds)                                           | `pdf2zh_next example.pdf --translator aliyun --translator-timeout 30`                                                 | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-max-retries`      | Maximum retries for the translation service                                             | `pdf2zh_next example.pdf --translator aliyun --translator-max-retries 3`                                              | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-retry-delay`      | Delay between retries for the translation service (seconds)                             | `pdf2zh_next example.pdf --translator aliyun --translator-retry-delay 2`                                              | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-retry-max-delay`  | Maximum delay between retries for the translation service (seconds)                     | `pdf2zh_next example.pdf --translator aliyun --translator-retry-max-delay 10`                                         | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-retry-backoff`    | Backoff factor for retries for the translation service                                   | `pdf2zh_next example.pdf --translator aliyun --translator-retry-backoff 2`                                            | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-retry-on`         | HTTP status codes to retry on for the translation service                               | `pdf2zh_next example.pdf --translator aliyun --translator-retry-on 429,500,502,503,504`                               | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |
| `--translator-retry-on-exception` | Whether to retry on exception for the translation service                               | `pdf2zh_next example.pdf --translator aliyun --translator-retry-on-exception`                                         | [Documentation of Translation Services](https://pdf2zh-next.com/translator/) |

---

### OUTPUT

| `--lang-out`                    | 目标语言代码                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            | [语言代码](https://pdf2zh-next.com/getting-started/LANGUAGE_CODE.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--translator`                  | 翻译服务                                                                     | `pdf2zh_next example.pdf --translator aliyun`                                                                         | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-api-key`          | 翻译服务的 API 密钥                                                     | `pdf2zh_next example.pdf --translator aliyun --translator-api-key YOUR_API_KEY`                                       | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-api-endpoint`     | 翻译服务的 API 端点                                                | `pdf2zh_next example.pdf --translator aliyun --translator-api-endpoint YOUR_API_ENDPOINT`                             | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-api-region`       | 翻译服务的 API 区域                                                  | `pdf2zh_next example.pdf --translator aliyun --translator-api-region YOUR_API_REGION`                                  | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-model`            | 翻译服务的模型名称                                                  | `pdf2zh_next example.pdf --translator siliconflow --translator-model YOUR_MODEL_NAME`                                 | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-api-version`      | 翻译服务的 API 版本                                                 | `pdf2zh_next example.pdf --translator azure --translator-api-version YOUR_API_VERSION`                                | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-extra-params`     | 翻译服务的额外参数                                            | `pdf2zh_next example.pdf --translator openai --translator-extra-params '{"temperature": 0.7}'`                        | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-timeout`          | 翻译服务的超时时间（秒）                                           | `pdf2zh_next example.pdf --translator aliyun --translator-timeout 30`                                                 | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-max-retries`      | 翻译服务的最大重试次数                                             | `pdf2zh_next example.pdf --translator aliyun --translator-max-retries 3`                                              | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-retry-delay`      | 翻译服务重试之间的延迟时间（秒）                             | `pdf2zh_next example.pdf --translator aliyun --translator-retry-delay 2`                                              | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-retry-max-delay`  | 翻译服务重试之间的最大延迟时间（秒）                     | `pdf2zh_next example.pdf --translator aliyun --translator-retry-max-delay 10`                                         | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-retry-backoff`    | 翻译服务重试的退避因子                                   | `pdf2zh_next example.pdf --translator aliyun --translator-retry-backoff 2`                                            | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-retry-on`         | 翻译服务重试的 HTTP 状态码                               | `pdf2zh_next example.pdf --translator aliyun --translator-retry-on 429,500,502,503,504`                               | [翻译服务文档](https://pdf2zh-next.com/translator/) |
| `--translator-retry-on-exception` | 是否在翻译服务异常时重试                               | `pdf2zh_next example.pdf --translator aliyun --translator-retry-on-exception`                                         | [翻译服务文档](https://pdf2zh-next.com/translator/) |
5                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `--max-text-length`             | Maximum text length to translate                                                        | `pdf2zh_next example.pdf --max-text-length 500`                                                                       | 500                                                                                              |
| `--min-text-ratio`              | Minimum text ratio to translate                                                         | `pdf2zh_next example.pdf --min-text-ratio 0.5`                                                                        | 0.5                                                                                              |
| `--max-text-ratio`              | Maximum text ratio to translate                                                         | `pdf2zh_next example.pdf --max-text-ratio 0.8`                                                                        | 0.8                                                                                              |
| `--remove-text-ratio-below`     | Remove text with ratio below this value                                                 | `pdf2zh_next example.pdf --remove-text-ratio-below 0.1`                                                               | 0.1                                                                                              |
| `--remove-text-ratio-above`     | Remove text with ratio above this value                                                 | `pdf2zh_next example.pdf --remove-text-ratio-above 0.9`                                                               | 0.9                                                                                              |
| `--remove-text-length-below`    | Remove text with length below this value                                                | `pdf2zh_next example.pdf --remove-text-length-below 10`                                                               | 10                                                                                               |
| `--remove-text-length-above`    | Remove text with length above this value                                                | `pdf2zh_next example.pdf --remove-text-length-above 1000`                                                             | 1000                                                                                             |
| `--remove-text-regex`           | Remove text matching regex                                                              | `pdf2zh_next example.pdf --remove-text-regex "^[0-9]+$"`                                                              | "^[0-9]+$"                                                                                       |
| `--remove-text-contains`       | Remove text containing the specified string                                             | `pdf2zh_next example.pdf --remove-text-contains "copyright"`                                                           | "copyright"                                                                                      |
| `--remove-text-equals`         | Remove text exactly matching the specified string                                        | `pdf2zh_next example.pdf --remove-text-equals "Appendix"`                                                              | "Appendix"                                                                                       |
| `--remove-text-startswith`      | Remove text starting with the specified string                                          | `pdf2zh_next example.pdf --remove-text-startswith "Chapter"`                                                           | "Chapter"                                                                                        |
| `--remove-text-endswith`        | Remove text ending with the specified string                                            | `pdf2zh_next example.pdf --remove-text-endswith "References"`                                                           | "References"                                                                                     |
| `--remove-text-in-pages`        | Remove text in specified pages (comma-separated page numbers or ranges, e.g., "1,3,5-7") | `pdf2zh_next example.pdf --remove-text-in-pages "1,3,5-7"`                                                            | "1,3,5-7"                                                                                        |
| `--keep-text-regex`             | Keep text matching regex (overrides remove filters)                                      | `pdf2zh_next example.pdf --keep-text-regex "^Figure [0-9]+:"`                                                          | "^Figure [0-9]+:"                                                                                |
| `--keep-text-contains`         | Keep text containing the specified string (overrides remove filters)                     | `pdf2zh_next example.pdf --keep-text-contains "important"`                                                             | "important"                                                                                      |
| `--keep-text-equals`           | Keep text exactly matching the specified string (overrides remove filters)               | `pdf2zh_next example.pdf --keep-text-equals "Abstract"`                                                               | "Abstract"                                                                                       |
| `--keep-text-startswith`        | Keep text starting with the specified string (overrides remove filters)                  | `pdf2zh_next example.pdf --keep-text-startswith "Section"`                                                            | "Section"                                                                                        |
| `--keep-text-endswith`          | Keep text ending with the specified string (overrides remove filters)                    | `pdf2zh_next example.pdf --keep-text-endswith "Conclusion"`                                                           | "Conclusion"                                                                                     |
| `--keep-text-in-pages`          | Keep text in specified pages (comma-separated page numbers or ranges, e.g., "2,4,8-10") | `pdf2zh_next example.pdf --keep-text-in-pages "2,4,8-10"`                                                            | "2,4,8-10"                                                                                       |
| `--translate-text-regex`        | Only translate text matching regex                                                       | `pdf2zh_next example.pdf --translate-text-regex "^[A-Za-z ]+$"`                                                       | "^[A-Za-z ]+$"                                                                                   |
| `--translate-text-contains`     | Only translate text containing the specified string                                      | `pdf2zh_next example.pdf --translate-text-contains "method"`                                                           | "method"                                                                                         |
| `--translate-text-equals`       | Only translate text exactly matching the specified string                                | `pdf2zh_next example.pdf --translate-text-equals "Introduction"`                                                      | "Introduction"                                                                                   |
| `--translate-text-startswith`   | Only translate text starting with the specified string                                   | `pdf2zh_next example.pdf --translate-text-startswith "Result"`                                                         | "Result"                                                                                         |
| `--translate-text-endswith`     | Only translate text ending with the specified string                                     | `pdf2zh_next example.pdf --translate-text-endswith "Analysis"`                                                         | "Analysis"                                                                                       |
| `--translate-text-in-pages`     | Only translate text in specified pages (comma-separated page numbers or ranges)          | `pdf2zh_next example.pdf --translate-text-in-pages "1-3,5"`                                                           | "1-3,5"                                                                                          |
| `--skip-text-regex`             | Skip translating text matching regex                                                     | `pdf2zh_next example.pdf --skip-text-regex "^[0-9.]+$"`                                                               | "^[0-9.]+$"                                                                                      |
| `--skip-text-contains`          | Skip translating text containing the specified string                                    | `pdf2zh_next example.pdf --skip-text-contains "equation"`                                                              | "equation"                                                                                       |
| `--skip-text-equals`            | Skip translating text exactly matching the specified string                               | `pdf2zh_next example.pdf --skip-text-equals "Appendix"`                                                               | "Appendix"                                                                                       |
| `--skip-text-startswith`        | Skip translating text starting with the specified string                                 | `pdf2zh_next example.pdf --skip-text-startswith "Table"`                                                              | "Table"                                                                                          |
| `--skip-text-endswith`          | Skip translating text ending with the specified string                                   | `pdf2zh_next example.pdf --skip-text-endswith "References"`                                                            | "References"                                                                                     |
| `--skip-text-in-pages`          | Skip translating text in specified pages (comma-separated page numbers or ranges)        | `pdf2zh_next example.pdf --skip-text-in-pages "4,6-8"`                                                                | "4,6-8"                                                                                          |

---

### OUTPUT

| `--min-text-length`             | 最小翻译文本长度                                                       | `pdf2zh_next example.pdf --min-text-length 5`                                                                         | 5                                                                                                |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `--max-text-length`             | 最大翻译文本长度                                                       | `pdf2zh_next example.pdf --max-text-length 500`                                                                       | 500                                                                                              |
| `--min-text-ratio`              | 最小文本比例以进行翻译                                                   | `pdf2zh_next example.pdf --min-text-ratio 0.5`                                                                        | 0.5                                                                                              |
| `--max-text-ratio`              | 最大文本比例以进行翻译                                                   | `pdf2zh_next example.pdf --max-text-ratio 0.8`                                                                        | 0.8                                                                                              |
| `--remove-text-ratio-below`     | 移除比例低于此值的文本                                                 | `pdf2zh_next example.pdf --remove-text-ratio-below 0.1`                                                               | 0.1                                                                                              |
| `--remove-text-ratio-above`     | 移除比例高于此值的文本                                                 | `pdf2zh_next example.pdf --remove-text-ratio-above 0.9`                                                               | 0.9                                                                                              |
| `--remove-text-length-below`    | 移除长度低于此值的文本                                                | `pdf2zh_next example.pdf --remove-text-length-below 10`                                                               | 10                                                                                               |
| `--remove-text-length-above`    | 移除长度高于此值的文本                                                | `pdf2zh_next example.pdf --remove-text-length-above 1000`                                                             | 1000                                                                                             |
| `--remove-text-regex`           | 移除匹配正则表达式的文本                                                              | `pdf2zh_next example.pdf --remove-text-regex "^[0-9]+$"`                                                              | "^[0-9]+$"                                                                                       |
| `--remove-text-contains`       | 移除包含指定字符串的文本                                             | `pdf2zh_next example.pdf --remove-text-contains "copyright"`                                                           | "copyright"                                                                                      |
| `--remove-text-equals`         | 移除完全匹配指定字符串的文本                                        | `pdf2zh_next example.pdf --remove-text-equals "Appendix"`                                                              | "Appendix"                                                                                       |
| `--remove-text-startswith`      | 移除以指定字符串开头的文本                                          | `pdf2zh_next example.pdf --remove-text-startswith "Chapter"`                                                           | "Chapter"                                                                                        |
| `--remove-text-endswith`        | 移除以指定字符串结尾的文本                                            | `pdf2zh_next example.pdf --remove-text-endswith "References"`                                                           | "References"                                                                                     |
| `--remove-text-in-pages`        | 移除指定页面中的文本（逗号分隔的页码或范围，例如 "1,3,5-7"） | `pdf2zh_next example.pdf --remove-text-in-pages "1,3,5-7"`                                                            | "1,3,5-7"                                                                                        |
| `--keep-text-regex`             | 保留匹配正则表达式的文本（覆盖移除过滤器）                                      | `pdf2zh_next example.pdf --keep-text-regex "^Figure [0-9]+:"`                                                          | "^Figure [0-9]+:"                                                                                |
| `--keep-text-contains`         | 保留包含指定字符串的文本（覆盖移除过滤器）                     | `pdf2zh_next example.pdf --keep-text-contains "important"`                                                             | "important"                                                                                      |
| `--keep-text-equals`           | 保留完全匹配指定字符串的文本（覆盖移除过滤器）               | `pdf2zh_next example.pdf --keep-text-equals "Abstract"`                                                               | "Abstract"                                                                                       |
| `--keep-text-startswith`        | 保留以指定字符串开头的文本（覆盖移除过滤器）                  | `pdf2zh_next example.pdf --keep-text-startswith "Section"`                                                            | "Section"                                                                                        |
| `--keep-text-endswith`          | 保留以指定字符串结尾的文本（覆盖移除过滤器）                    | `pdf2zh_next example.pdf --keep-text-endswith "Conclusion"`                                                           | "Conclusion"                                                                                     |
| `--keep-text-in-pages`          | 保留指定页面中的文本（逗号分隔的页码或范围，例如 "2,4,8-10"） | `pdf2zh_next example.pdf --keep-text-in-pages "2,4,8-10"`                                                            | "2,4,8-10"                                                                                       |
| `--translate-text-regex`        | 仅翻译匹配正则表达式的文本                                                       | `pdf2zh_next example.pdf --translate-text-regex "^[A-Za-z ]+$"`                                                       | "^[A-Za-z ]+$"                                                                                   |
| `--translate-text-contains`     | 仅翻译包含指定字符串的文本                                      | `pdf2zh_next example.pdf --translate-text-contains "method"`                                                           | "method"                                                                                         |
| `--translate-text-equals`       | 仅翻译完全匹配指定字符串的文本                                | `pdf2zh_next example.pdf --translate-text-equals "Introduction"`                                                      | "Introduction"                                                                                   |
| `--translate-text-startswith`   | 仅翻译以指定字符串开头的文本                                   | `pdf2zh_next example.pdf --translate-text-startswith "Result"`                                                         | "Result"                                                                                         |
| `--translate-text-endswith`     | 仅翻译以指定字符串结尾的文本                                     | `pdf2zh_next example.pdf --translate-text-endswith "Analysis"`                                                         | "Analysis"                                                                                       |
| `--translate-text-in-pages`     | 仅翻译指定页面中的文本（逗号分隔的页码或范围）          | `pdf2zh_next example.pdf --translate-text-in-pages "1-3,5"`                                                           | "1-3,5"                                                                                          |
| `--skip-text-regex`             | 跳过翻译匹配正则表达式的文本                                                     | `pdf2zh_next example.pdf --skip-text-regex "^[0-9.]+$"`                                                               | "^[0-9.]+$"                                                                                      |
| `--skip-text-contains`          | 跳过翻译包含指定字符串的文本                                    | `pdf2zh_next example.pdf --skip-text-contains "equation"`                                                              | "equation"                                                                                       |
| `--skip-text-equals`            | 跳过翻译完全匹配指定字符串的文本                               | `pdf2zh_next example.pdf --skip-text-equals "Appendix"`                                                               | "Appendix"                                                                                       |
| `--skip-text-startswith`        | 跳过翻译以指定字符串开头的文本                                 | `pdf2zh_next example.pdf --skip-text-startswith "Table"`                                                              | "Table"                                                                                          |
| `--skip-text-endswith`          | 跳过翻译以指定字符串结尾的文本                                   | `pdf2zh_next example.pdf --skip-text-endswith "References"`                                                            | "References"                                                                                     |
| `--skip-text-in-pages`          | 跳过翻译指定页面中的文本（逗号分隔的页码或范围）        | `pdf2zh_next example.pdf --skip-text-in-pages "4,6-8"`                                                                | "4,6-8"                                                                                          |
`http://127.0.0.1:8000` |
| `--rpc-ocr`                     | RPC service host address for OCR                                                         | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8000`                                                             | `http://127.0.0.1:8000` |
| `--rpc-translate`               | RPC service host address for translation                                                 | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8000`                                                       | `http://127.0.0.1:8000` |
| `--rpc-doclayout-args`          | Additional arguments for document layout analysis RPC service                            | `pdf2zh_next example.pdf --rpc-doclayout-args '{"model_name": "doclaynet"}'`                                          | `{}`                    |
| `--rpc-ocr-args`                | Additional arguments for OCR RPC service                                                 | `pdf2zh_next example.pdf --rpc-ocr-args '{"det": "DB", "rec": "SVTR"}',`                                              | `{}`                    |
| `--rpc-translate-args`          | Additional arguments for translation RPC service                                         | `pdf2zh_next example.pdf --rpc-translate-args '{"provider": "openai", "model": "gpt-4o", "api_key": "sk-..."}'`       | `{}`                    |
| `--rpc-doclayout-timeout`       | Timeout for document layout analysis RPC service (seconds)                               | `pdf2zh_next example.pdf --rpc-doclayout-timeout 600`                                                                 | `600`                   |
| `--rpc-ocr-timeout`             | Timeout for OCR RPC service (seconds)                                                    | `pdf2zh_next example.pdf --rpc-ocr-timeout 600`                                                                       | `600`                   |
| `--rpc-translate-timeout`       | Timeout for translation RPC service (seconds)                                            | `pdf2zh_next example.pdf --rpc-translate-timeout 600`                                                                 | `600`                   |
| `--rpc-doclayout-request-timeout` | Request timeout for document layout analysis RPC service (seconds)                       | `pdf2zh_next example.pdf --rpc-doclayout-request-timeout 60`                                                          | `60`                    |
| `--rpc-ocr-request-timeout`     | Request timeout for OCR RPC service (seconds)                                            | `pdf2zh_next example.pdf --rpc-ocr-request-timeout 60`                                                                | `60`                    |
| `--rpc-translate-request-timeout` | Request timeout for translation RPC service (seconds)                                    | `pdf2zh_next example.pdf --rpc-translate-request-timeout 60`                                                          | `60`                    |
| `--rpc-doclayout-batch-size`    | Batch size for document layout analysis RPC service                                      | `pdf2zh_next example.pdf --rpc-doclayout-batch-size 32`                                                               | `32`                    |
| `--rpc-ocr-batch-size`          | Batch size for OCR RPC service                                                           | `pdf2zh_next example.pdf --rpc-ocr-batch-size 32`                                                                     | `32`                    |
| `--rpc-translate-batch-size`    | Batch size for translation RPC service                                                   | `pdf2zh_next example.pdf --rpc-translate-batch-size 32`                                                               | `32`                    |

---

### OUTPUT

| `--rpc-doclayout`               | 文档布局分析的 RPC 服务主机地址                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       | `http://127.0.0.1:8000` |
| `--rpc-ocr`                     | OCR 的 RPC 服务主机地址                                                         | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8000`                                                             | `http://127.0.0.1:8000` |
| `--rpc-translate`               | 翻译的 RPC 服务主机地址                                                 | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8000`                                                       | `http://127.0.0.1:8000` |
| `--rpc-doclayout-args`          | 文档布局分析 RPC 服务的附加参数                            | `pdf2zh_next example.pdf --rpc-doclayout-args '{"model_name": "doclaynet"}'`                                          | `{}`                    |
| `--rpc-ocr-args`                | OCR RPC 服务的附加参数                                                 | `pdf2zh_next example.pdf --rpc-ocr-args '{"det": "DB", "rec": "SVTR"}',`                                              | `{}`                    |
| `--rpc-translate-args`          | 翻译 RPC 服务的附加参数                                         | `pdf2zh_next example.pdf --rpc-translate-args '{"provider": "openai", "model": "gpt-4o", "api_key": "sk-..."}'`       | `{}`                    |
| `--rpc-doclayout-timeout`       | 文档布局分析 RPC 服务的超时时间（秒）                               | `pdf2zh_next example.pdf --rpc-doclayout-timeout 600`                                                                 | `600`                   |
| `--rpc-ocr-timeout`             | OCR RPC 服务的超时时间（秒）                                                    | `pdf2zh_next example.pdf --rpc-ocr-timeout 600`                                                                       | `600`                   |
| `--rpc-translate-timeout`       | 翻译 RPC 服务的超时时间（秒）                                            | `pdf2zh_next example.pdf --rpc-translate-timeout 600`                                                                 | `600`                   |
| `--rpc-doclayout-request-timeout` | 文档布局分析 RPC 服务的请求超时时间（秒）                       | `pdf2zh_next example.pdf --rpc-doclayout-request-timeout 60`                                                          | `60`                    |
| `--rpc-ocr-request-timeout`     | OCR RPC 服务的请求超时时间（秒）                                            | `pdf2zh_next example.pdf --rpc-ocr-request-timeout 60`                                                                | `60`                    |
| `--rpc-translate-request-timeout` | 翻译 RPC 服务的请求超时时间（秒）                                    | `pdf2zh_next example.pdf --rpc-translate-request-timeout 60`                                                          | `60`                    |
| `--rpc-doclayout-batch-size`    | 文档布局分析 RPC 服务的批处理大小                                      | `pdf2zh_next example.pdf --rpc-doclayout-batch-size 32`                                                               | `32`                    |
| `--rpc-ocr-batch-size`          | OCR RPC 服务的批处理大小                                                           | `pdf2zh_next example.pdf --rpc-ocr-batch-size 32`                                                                     | `32`                    |
| `--rpc-translate-batch-size`    | 翻译 RPC 服务的批处理大小                                                   | `pdf2zh_next example.pdf --rpc-translate-batch-size 32`                                                               | `32`                    |
---

### OUTPUT

| `--qps`                         | 翻译服务的 QPS 限制                                                                    | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ignore-cache-translation`    | Ignore translation cache only, but use layout cache (if exists)                         | `pdf2zh_next example.pdf --ignore-cache-translation`                                                                  |
| `--ignore-cache-layout`         | Ignore layout cache only, but use translation cache (if exists)                         | `pdf2zh_next example.pdf --ignore-cache-layout`                                                                       |
| `--ignore-cache-ocr`            | Ignore OCR cache only, but use other cache (if exists)                                  | `pdf2zh_next example.pdf --ignore-cache-ocr`                                                                          |
| `--ignore-cache-all`            | Ignore all cache (including translation, layout, and OCR cache)                         | `pdf2zh_next example.pdf --ignore-cache-all`                                                                          |
| `--force-refresh-layout`        | Force refresh layout cache (re-analyze the layout of the PDF)                           | `pdf2zh_next example.pdf --force-refresh-layout`                                                                      |
| `--force-refresh-ocr`           | Force refresh OCR cache (re-OCR the PDF)                                                | `pdf2zh_next example.pdf --force-refresh-ocr`                                                                         |
| `--force-refresh-translation`   | Force refresh translation cache (re-translate the text)                                 | `pdf2zh_next example.pdf --force-refresh-translation`                                                                 |
| `--force-refresh-all`           | Force refresh all cache (re-analyze layout, re-OCR, and re-translate)                   | `pdf2zh_next example.pdf --force-refresh-all`                                                                         |

---

### TRANSLATION RESULT

| `--ignore-cache`                | 忽略翻译缓存                                                                             | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ignore-cache-translation`    | 仅忽略翻译缓存，但使用布局缓存（如果存在）                                                 | `pdf2zh_next example.pdf --ignore-cache-translation`                                                                  |
| `--ignore-cache-layout`         | 仅忽略布局缓存，但使用翻译缓存（如果存在）                                                 | `pdf2zh_next example.pdf --ignore-cache-layout`                                                                       |
| `--ignore-cache-ocr`            | 仅忽略 OCR 缓存，但使用其他缓存（如果存在）                                                | `pdf2zh_next example.pdf --ignore-cache-ocr`                                                                          |
| `--ignore-cache-all`            | 忽略所有缓存（包括翻译、布局和 OCR 缓存）                                                  | `pdf2zh_next example.pdf --ignore-cache-all`                                                                          |
| `--force-refresh-layout`        | 强制刷新布局缓存（重新分析 PDF 的布局）                                                    | `pdf2zh_next example.pdf --force-refresh-layout`                                                                      |
| `--force-refresh-ocr`           | 强制刷新 OCR 缓存（重新对 PDF 进行 OCR）                                                   | `pdf2zh_next example.pdf --force-refresh-ocr`                                                                         |
| `--force-refresh-translation`   | 强制刷新翻译缓存（重新翻译文本）                                                           | `pdf2zh_next example.pdf --force-refresh-translation`                                                                 |
| `--force-refresh-all`           | 强制刷新所有缓存（重新分析布局、重新 OCR 和重新翻译）                                       | `pdf2zh_next example.pdf --force-refresh-all`                                                                         |

| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--glossaries_auto_detect`      | Whether to automatically detect glossary files in the current directory.                 | `pdf2zh_next example.pdf --glossaries_auto_detect`                                                                    |
| `--glossaries_auto_detect_path` | The path to automatically detect glossary files.                                        | `pdf2zh_next example.pdf --glossaries_auto_detect_path "./glossaries"`                                                |
| `--glossaries_auto_detect_ext`  | The file extensions to automatically detect glossary files.                             | `pdf2zh_next example.pdf --glossaries_auto_detect_ext "csv,txt"`                                                      |
| `--glossaries_auto_detect_mode` | The mode to automatically detect glossary files. Options: `union`, `intersection`.      | `pdf2zh_next example.pdf --glossaries_auto_detect_mode "union"`                                                       |
| `--glossaries_auto_detect_name` | The name pattern to automatically detect glossary files. Supports wildcards (`*`).       | `pdf2zh_next example.pdf --glossaries_auto_detect_name "*glossary*"`                                                  |
| `--glossaries_auto_detect_depth`| The depth to automatically detect glossary files.                                       | `pdf2zh_next example.pdf --glossaries_auto_detect_depth 2`                                                            |

---

### TRANSLATION RESULT

| `--glossaries`                  | 术语表文件列表。                                                                        | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--glossaries_auto_detect`      | 是否自动检测当前目录中的术语表文件。                                                    | `pdf2zh_next example.pdf --glossaries_auto_detect`                                                                    |
| `--glossaries_auto_detect_path` | 自动检测术语表文件的路径。                                                              | `pdf2zh_next example.pdf --glossaries_auto_detect_path "./glossaries"`                                                |
| `--glossaries_auto_detect_ext`  | 自动检测术语表文件的扩展名。                                                            | `pdf2zh_next example.pdf --glossaries_auto_detect_ext "csv,txt"`                                                      |
| `--glossaries_auto_detect_mode` | 自动检测术语表文件的模式。选项：`union`（并集）、`intersection`（交集）。               | `pdf2zh_next example.pdf --glossaries_auto_detect_mode "union"`                                                       |
| `--glossaries_auto_detect_name` | 自动检测术语表文件的名称模式。支持通配符（`*`）。                                       | `pdf2zh_next example.pdf --glossaries_auto_detect_name "*glossary*"`                                                  |
| `--glossaries_auto_detect_depth`| 自动检测术语表文件的深度。                                                              | `pdf2zh_next example.pdf --glossaries_auto_detect_depth 2`                                                            |
`glossary`                                                               |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `--save-glossary`               | save the glossary after translation                                                    | `pdf2zh_next example.pdf --save-glossary`                                                                             | `glossary`                                                               |
| `--save-raw-glossary`           | save the raw glossary after translation                                                | `pdf2zh_next example.pdf --save-raw-glossary`                                                                         | `glossary`                                                               |

---

### OUTPUT

| `--save-auto-extracted-glossary`| 保存自动提取的术语表                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              | `glossary`                                                               |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `--save-glossary`               | 保存翻译后的术语表                                                    | `pdf2zh_next example.pdf --save-glossary`                                                                             | `glossary`                                                               |
| `--save-raw-glossary`           | 保存翻译后的原始术语表                                                | `pdf2zh_next example.pdf --save-raw-glossary`                                                                         | `glossary`                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-workers-per-second` | Maximum number of workers per second for translation pool. If not set, will use qps / 10          | `pdf2zh_next example.pdf --pool-max-workers-per-second 10`                                                |

---

### OUTPUT

| `--pool-max-workers`            | 翻译池的最大工作线程数。如果未设置，将使用 qps 作为工作线程数 | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-workers-per-second` | 翻译池每秒最大工作线程数。如果未设置，将使用 qps / 10          | `pdf2zh_next example.pdf --pool-max-workers-per-second 10`                                                |
`float`       |
| `--term-api-key`                | API key for term extraction translation service. If not set, will follow `--api-key`.   | `pdf2zh_next example.pdf --term-api-key YOUR_API_KEY`                                                                 | `string`      |
| `--term-base-url`               | Base URL for term extraction translation service. If not set, will follow `--base-url`. | `pdf2zh_next example.pdf --term-base-url https://api.openai.com/v1`                                                   | `string`      |
| `--term-model`                  | Model for term extraction translation service. If not set, will follow `--model`.       | `pdf2zh_next example.pdf --term-model gpt-4o-mini`                                                                    | `string`      |
| `--term-system-prompt`          | System prompt for term extraction translation service.                                  | `pdf2zh_next example.pdf --term-system-prompt "You are a helpful assistant to extract terms from text."`               | `string`      |
| `--term-max-tokens`             | Max tokens for term extraction translation service.                                     | `pdf2zh_next example.pdf --term-max-tokens 1000`                                                                      | `integer`     |
| `--term-temperature`            | Temperature for term extraction translation service.                                    | `pdf2zh_next example.pdf --term-temperature 0.7`                                                                      | `float`       |
| `--term-top-p`                  | Top p for term extraction translation service.                                          | `pdf2zh_next example.pdf --term-top-p 0.9`                                                                            | `float`       |
| `--term-presence-penalty`       | Presence penalty for term extraction translation service.                               | `pdf2zh_next example.pdf --term-presence-penalty 0.0`                                                                 | `float`       |
| `--term-frequency-penalty`      | Frequency penalty for term extraction translation service.                              | `pdf2zh_next example.pdf --term-frequency-penalty 0.0`                                                                | `float`       |
| `--term-timeout`                | Timeout for term extraction translation service.                                        | `pdf2zh_next example.pdf --term-timeout 30`                                                                           | `integer`     |
| `--term-request-timeout`        | Request timeout for term extraction translation service.                                | `pdf2zh_next example.pdf --term-request-timeout 30`                                                                   | `integer`     |
| `--term-max-retries`            | Max retries for term extraction translation service.                                    | `pdf2zh_next example.pdf --term-max-retries 3`                                                                        | `integer`     |
| `--term-retry-min-wait`         | Min wait time for retries for term extraction translation service.                      | `pdf2zh_next example.pdf --term-retry-min-wait 1`                                                                     | `integer`     |
| `--term-retry-max-wait`         | Max wait time for retries for term extraction translation service.                      | `pdf2zh_next example.pdf --term-retry-max-wait 10`                                                                    | `integer`     |
| `--term-organization`           | Organization for term extraction translation service.                                   | `pdf2zh_next example.pdf --term-organization YOUR_ORG_ID`                                                             | `string`      |
| `--term-project`                | Project for term extraction translation service.                                        | `pdf2zh_next example.pdf --term-project YOUR_PROJECT_ID`                                                              | `string`      |
| `--term-extra-body`             | Extra body for term extraction translation service.                                     | `pdf2zh_next example.pdf --term-extra-body '{"key": "value"}'`                                                        | `string`      |
| `--term-extra-headers`          | Extra headers for term extraction translation service.                                  | `pdf2zh_next example.pdf --term-extra-headers '{"X-Custom-Header": "value"}'`                                         | `string`      |
| `--term-extra-query`            | Extra query for term extraction translation service.                                    | `pdf2zh_next example.pdf --term-extra-query '{"custom_param": "value"}'`                                              | `string`      |

---

### TRANSLATED TEXT

| `--term-qps`                    | 术语提取翻译服务的 QPS 限制。如果未设置，将遵循 qps。                                   | `pdf2zh_next example.pdf --term-qps 20`                                                                               | `float`       |
| `--term-api-key`                | 术语提取翻译服务的 API 密钥。如果未设置，将遵循 `--api-key`。                           | `pdf2zh_next example.pdf --term-api-key YOUR_API_KEY`                                                                 | `string`      |
| `--term-base-url`               | 术语提取翻译服务的基础 URL。如果未设置，将遵循 `--base-url`。                           | `pdf2zh_next example.pdf --term-base-url https://api.openai.com/v1`                                                   | `string`      |
| `--term-model`                  | 术语提取翻译服务的模型。如果未设置，将遵循 `--model`。                                  | `pdf2zh_next example.pdf --term-model gpt-4o-mini`                                                                    | `string`      |
| `--term-system-prompt`          | 术语提取翻译服务的系统提示。                                                           | `pdf2zh_next example.pdf --term-system-prompt "You are a helpful assistant to extract terms from text."`               | `string`      |
| `--term-max-tokens`             | 术语提取翻译服务的最大 token 数。                                                      | `pdf2zh_next example.pdf --term-max-tokens 1000`                                                                      | `integer`     |
| `--term-temperature`            | 术语提取翻译服务的温度参数。                                                           | `pdf2zh_next example.pdf --term-temperature 0.7`                                                                      | `float`       |
| `--term-top-p`                  | 术语提取翻译服务的 top p 参数。                                                        | `pdf2zh_next example.pdf --term-top-p 0.9`                                                                            | `float`       |
| `--term-presence-penalty`       | 术语提取翻译服务的存在惩罚参数。                                                       | `pdf2zh_next example.pdf --term-presence-penalty 0.0`                                                                 | `float`       |
| `--term-frequency-penalty`      | 术语提取翻译服务的频率惩罚参数。                                                       | `pdf2zh_next example.pdf --term-frequency-penalty 0.0`                                                                | `float`       |
| `--term-timeout`                | 术语提取翻译服务的超时时间。                                                           | `pdf2zh_next example.pdf --term-timeout 30`                                                                           | `integer`     |
| `--term-request-timeout`        | 术语提取翻译服务的请求超时时间。                                                       | `pdf2zh_next example.pdf --term-request-timeout 30`                                                                   | `integer`     |
| `--term-max-retries`            | 术语提取翻译服务的最大重试次数。                                                       | `pdf2zh_next example.pdf --term-max-retries 3`                                                                        | `integer`     |
| `--term-retry-min-wait`         | 术语提取翻译服务重试的最小等待时间。                                                   | `pdf2zh_next example.pdf --term-retry-min-wait 1`                                                                     | `integer`     |
| `--term-retry-max-wait`         | 术语提取翻译服务重试的最大等待时间。                                                   | `pdf2zh_next example.pdf --term-retry-max-wait 10`                                                                    | `integer`     |
| `--term-organization`           | 术语提取翻译服务的组织。                                                               | `pdf2zh_next example.pdf --term-organization YOUR_ORG_ID`                                                             | `string`      |
| `--term-project`                | 术语提取翻译服务的项目。                                                               | `pdf2zh_next example.pdf --term-project YOUR_PROJECT_ID`                                                              | `string`      |
| `--term-extra-body`             | 术语提取翻译服务的额外请求体。                                                         | `pdf2zh_next example.pdf --term-extra-body '{"key": "value"}'`                                                        | `string`      |
| `--term-extra-headers`          | 术语提取翻译服务的额外请求头。                                                         | `pdf2zh_next example.pdf --term-extra-headers '{"X-Custom-Header": "value"}'`                                         | `string`      |
| `--term-extra-query`            | 术语提取翻译服务的额外查询参数。                                                       | `pdf2zh_next example.pdf --term-extra-query '{"custom_param": "value"}'`                                              | `string`      |

| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary <path>`             | Use a custom glossary file                                                              | `pdf2zh_next example.pdf --glossary custom_glossary.txt`                                                              |
| `--glossary-merge-strategy`     | Strategy for merging glossaries: `overwrite`, `combine` or `smart` (default: `smart`)   | `pdf2zh_next example.pdf --glossary custom_glossary.txt --glossary-merge-strategy overwrite`                          |
| `--glossary-min-freq <number>`  | Minimum frequency for a term to be included in the auto-extracted glossary (default: 3) | `pdf2zh_next example.pdf --glossary-min-freq 5`                                                                       |

---

### OUTPUT

| `--no-auto-extract-glossary`    | 禁用自动提取术语表                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary <path>`             | 使用自定义术语表文件                                                              | `pdf2zh_next example.pdf --glossary custom_glossary.txt`                                                              |
| `--glossary-merge-strategy`     | 术语表合并策略：`overwrite`、`combine` 或 `smart`（默认：`smart`）   | `pdf2zh_next example.pdf --glossary custom_glossary.txt --glossary-merge-strategy overwrite`                          |
| `--glossary-min-freq <number>`  | 自动提取术语表中包含术语的最小频率（默认：3） | `pdf2zh_next example.pdf --glossary-min-freq 5`                                                                       |
| `--secondary-font-family`       | Override secondary font family for translated text. Choices: 'serif' for serif fonts, 'sans-serif' for sans-serif fonts, 'script' for script/italic fonts. If not specified, uses automatic font selection based on original text properties. | `pdf2zh_next example.pdf --secondary-font-family script` |
| `--font-size-multiplier`        | Font size multiplier for translated text. Values less than 1.0 make text smaller, greater than 1.0 make text larger. | `pdf2zh_next example.pdf --font-size-multiplier 0.9` |
| `--line-spacing-multiplier`     | Line spacing multiplier for translated text. Values less than 1.0 make lines closer, greater than 1.0 make lines more spaced. | `pdf2zh_next example.pdf --line-spacing-multiplier 1.1` |
| `--char-spacing-multiplier`     | Character spacing multiplier for translated text. Values less than 1.0 make characters closer, greater than 1.0 make characters more spaced. | `pdf2zh_next example.pdf --char-spacing-multiplier 1.05` |
| `--word-spacing-multiplier`     | Word spacing multiplier for translated text. Values less than 1.0 make words closer, greater than 1.0 make words more spaced. | `pdf2zh_next example.pdf --word-spacing-multiplier 1.05` |
| `--font-family-mapping`         | Custom font family mapping in JSON format. Maps original font families to target font families. | `pdf2zh_next example.pdf --font-family-mapping '{"Arial": "SimHei", "Times New Roman": "SimSun"}'` |

---

### TRANSLATION

| `--primary-font-family`         | 覆盖翻译文本的主字体族。选项：'serif' 表示衬线字体，'sans-serif' 表示无衬线字体，'script' 表示手写体/斜体字体。如果未指定，则根据原始文本属性自动选择字体。 | `pdf2zh_next example.pdf --primary-font-family serif` |
| `--secondary-font-family`       | 覆盖翻译文本的次字体族。选项：'serif' 表示衬线字体，'sans-serif' 表示无衬线字体，'script' 表示手写体/斜体字体。如果未指定，则根据原始文本属性自动选择字体。 | `pdf2zh_next example.pdf --secondary-font-family script` |
| `--font-size-multiplier`        | 翻译文本的字体大小乘数。小于 1.0 的值会使文本变小，大于 1.0 的值会使文本变大。 | `pdf2zh_next example.pdf --font-size-multiplier 0.9` |
| `--line-spacing-multiplier`     | 翻译文本的行间距乘数。小于 1.0 的值会使行距更近，大于 1.0 的值会使行距更宽。 | `pdf2zh_next example.pdf --line-spacing-multiplier 1.1` |
| `--char-spacing-multiplier`     | 翻译文本的字符间距乘数。小于 1.0 的值会使字符更近，大于 1.0 的值会使字符更宽。 | `pdf2zh_next example.pdf --char-spacing-multiplier 1.05` |
| `--word-spacing-multiplier`     | 翻译文本的单词间距乘数。小于 1.0 的值会使单词更近，大于 1.0 的值会使单词更宽。 | `pdf2zh_next example.pdf --word-spacing-multiplier 1.05` |
| `--font-family-mapping`         | 以 JSON 格式自定义字体族映射。将原始字体族映射到目标字体族。 | `pdf2zh_next example.pdf --font-family-mapping '{"Arial": "SimHei", "Times New Roman": "SimSun"}'` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--translate-annotations`       | Translate annotations (such as text boxes, comments, etc.)                             | `pdf2zh_next example.pdf --translate-annotations`                                                                     |
| `--translate-bookmarks`         | Translate bookmarks                                                                    | `pdf2zh_next example.pdf --translate-bookmarks`                                                                       |
| `--translate-metadata`          | Translate metadata                                                                      | `pdf2zh_next example.pdf --translate-metadata`                                                                        |
| `--translate-outlines`          | Translate outlines                                                                      | `pdf2zh_next example.pdf --translate-outlines`                                                                        |
| `--language`                    | Specify the target language. Default: `zh`                                             | `pdf2zh_next example.pdf --language ja`                                                                               |
| `--source-language`             | Specify the source language. Default: `auto`                                           | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--translator`                  | Specify the translation service provider. Default: `openai`                             | `pdf2zh_next example.pdf --translator aliyun`                                                                         |
| `--translator-args`             | Pass additional arguments to the translation service provider                           | `pdf2zh_next example.pdf --translator openai --translator-args '{"model": "gpt-4-turbo", "api_key": "your-api-key"}'` |
| `--translator-args-base64`      | Pass additional arguments to the translation service provider in base64 encoded format | `pdf2zh_next example.pdf --translator openai --translator-args-base64 "eyJtb2RlbCI6ICJncHQtNC10dXJibyJ9"`              |
| `--translator-args-file`        | Pass additional arguments to the translation service provider via a JSON file          | `pdf2zh_next example.pdf --translator openai --translator-args-file args.json`                                         |
| `--webui`                       | Start the web interface                                                                | `pdf2zh_next --webui`                                                                                                 |
| `--webui-port`                  | Specify the port for the web interface. Default: `5000`                                | `pdf2zh_next --webui --webui-port 8080`                                                                               |
| `--webui-host`                  | Specify the host for the web interface. Default: `127.0.0.1`                           | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                            |
| `--webui-no-browser`            | Do not automatically open the browser                                                  | `pdf2zh_next --webui --webui-no-browser`                                                                              |
| `--webui-debug`                 | Enable debug mode for the web interface                                                | `pdf2zh_next --webui --webui-debug`                                                                                   |
| `--webui-reload`                | Enable auto-reload for the web interface                                               | `pdf2zh_next --webui --webui-reload`                                                                                  |
| `--webui-worker`                | Number of web interface workers. Default: `1`                                          | `pdf2zh_next --webui --webui-worker 4`                                                                                |
| `--version`                     | Show the version and exit                                                              | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show this help message and exit                                                        | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT

| `--no-dual`                     | 不输出双语 PDF 文件                                                                     | `pdf2zh_next example.pdf --no-dual`                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--translate-annotations`       | 翻译注释（如文本框、评论等）                                                            | `pdf2zh_next example.pdf --translate-annotations`                                                                     |
| `--translate-bookmarks`         | 翻译书签                                                                                | `pdf2zh_next example.pdf --translate-bookmarks`                                                                       |
| `--translate-metadata`          | 翻译元数据                                                                              | `pdf2zh_next example.pdf --translate-metadata`                                                                        |
| `--translate-outlines`          | 翻译大纲                                                                                | `pdf2zh_next example.pdf --translate-outlines`                                                                        |
| `--language`                    | 指定目标语言。默认：`zh`                                                                | `pdf2zh_next example.pdf --language ja`                                                                               |
| `--source-language`             | 指定源语言。默认：`auto`                                                                | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--translator`                  | 指定翻译服务提供商。默认：`openai`                                                      | `pdf2zh_next example.pdf --translator aliyun`                                                                         |
| `--translator-args`             | 向翻译服务提供商传递额外参数                                                            | `pdf2zh_next example.pdf --translator openai --translator-args '{"model": "gpt-4-turbo", "api_key": "your-api-key"}'` |
| `--translator-args-base64`      | 以 base64 编码格式向翻译服务提供商传递额外参数                                          | `pdf2zh_next example.pdf --translator openai --translator-args-base64 "eyJtb2RlbCI6ICJncHQtNC10dXJibyJ9"`              |
| `--translator-args-file`        | 通过 JSON 文件向翻译服务提供商传递额外参数                                              | `pdf2zh_next example.pdf --translator openai --translator-args-file args.json`                                         |
| `--webui`                       | 启动 Web 界面                                                                           | `pdf2zh_next --webui`                                                                                                 |
| `--webui-port`                  | 指定 Web 界面的端口。默认：`5000`                                                       | `pdf2zh_next --webui --webui-port 8080`                                                                               |
| `--webui-host`                  | 指定 Web 界面的主机。默认：`127.0.0.1`                                                  | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                            |
| `--webui-no-browser`            | 不自动打开浏览器                                                                        | `pdf2zh_next --webui --webui-no-browser`                                                                              |
| `--webui-debug`                 | 启用 Web 界面的调试模式                                                                 | `pdf2zh_next --webui --webui-debug`                                                                                   |
| `--webui-reload`                | 启用 Web 界面的自动重新加载                                                             | `pdf2zh_next --webui --webui-reload`                                                                                  |
| `--webui-worker`                | Web 界面的工作进程数。默认：`1`                                                         | `pdf2zh_next --webui --webui-worker 4`                                                                                |
| `--version`                     | 显示版本信息并退出                                                                      | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 显示此帮助信息并退出                                                                    | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-dual`                     | Do not output dual-column PDF files                                                     | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--no-html`                     | Do not output HTML files                                                                | `pdf2zh_next example.pdf --no-html`                                                                                   |
| `--no-markdown`                 | Do not output Markdown files                                                            | `pdf2zh_next example.pdf --no-markdown`                                                                               |
| `--no-pdf`                      | Do not output PDF files (implies `--no-mono --no-dual`)                                 | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--output-dir <dir>`            | Specify the output directory                                                           | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-filename <filename>`  | Specify the output filename (without extension)                                        | `pdf2zh_next example.pdf --output-filename translated`                                                                |
| `--overwrite`                   | Overwrite existing files                                                               | `pdf2zh_next example.pdf --overwrite`                                                                                 |
| `--preserve-original-layout`    | Preserve the original PDF layout (may affect translation quality)                      | `pdf2zh_next example.pdf --preserve-original-layout`                                                                  |
| `--quiet`                       | Suppress all output except errors                                                       | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `--source-lang <lang>`          | Source language code (default: auto)                                                   | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--target-lang <lang>`          | Target language code (default: zh)                                                     | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--translator <translator>`     | Translation service (default: aliyun)                                                  | `pdf2zh_next example.pdf --translator aliyun`                                                                         |
| `--translator-options <options>` | Additional options for the translation service (as JSON)                               | `pdf2zh_next example.pdf --translator-options '{"key": "your-api-key"}'`                                              |
| `--version`                     | Show version information                                                               | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message                                                                      | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT LANGUAGE

zh

---

### OUTPUT

| `--no-mono`                     | 不输出单语 PDF 文件                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-dual`                     | 不输出双栏 PDF 文件                                                     | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--no-html`                     | 不输出 HTML 文件                                                                 | `pdf2zh_next example.pdf --no-html`                                                                                   |
| `--no-markdown`                 | 不输出 Markdown 文件                                                             | `pdf2zh_next example.pdf --no-markdown`                                                                               |
| `--no-pdf`                      | 不输出 PDF 文件 (隐含 `--no-mono --no-dual`)                                 | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--output-dir <dir>`            | 指定输出目录                                                           | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-filename <filename>`  | 指定输出文件名 (不含扩展名)                                        | `pdf2zh_next example.pdf --output-filename translated`                                                                |
| `--overwrite`                   | 覆盖现有文件                                                               | `pdf2zh_next example.pdf --overwrite`                                                                                 |
| `--preserve-original-layout`    | 保留原始 PDF 布局 (可能影响翻译质量)                      | `pdf2zh_next example.pdf --preserve-original-layout`                                                                  |
| `--quiet`                       | 抑制除错误外的所有输出                                                       | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `--source-lang <lang>`          | 源语言代码 (默认值：auto)                                                   | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--target-lang <lang>`          | 目标语言代码 (默认值：zh)                                                     | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--translator <translator>`     | 翻译服务 (默认值：aliyun)                                                  | `pdf2zh_next example.pdf --translator aliyun`                                                                         |
| `--translator-options <options>` | 翻译服务的附加选项 (JSON 格式)                               | `pdf2zh_next example.pdf --translator-options '{"key": "your-api-key"}'`                                              |
| `--version`                     | 显示版本信息                                                               | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 显示帮助信息                                                                      | `pdf2zh_next --help`                                                                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--formular-font-size-threshold` | Font size threshold to identify formula text (in pt)                                   | `pdf2zh_next example.pdf --formular-font-size-threshold 10`                                                            |
| `--formular-font-color-threshold` | Font color threshold to identify formula text (in RGB hex, e.g. `#000000` for black)    | `pdf2zh_next example.pdf --formular-font-color-threshold "#000000"`                                                    |
| `--formular-ocr`                | Enable OCR for formulas to improve recognition                                          | `pdf2zh_next example.pdf --formular-ocr`                                                                               |
| `--formular-ocr-dpi`            | DPI setting for formula OCR (default: 300)                                             | `pdf2zh_next example.pdf --formular-ocr-dpi 300`                                                                       |
| `--formular-ocr-lang`           | Language for formula OCR (default: `eng`)                                              | `pdf2zh_next example.pdf --formular-ocr-lang eng`                                                                      |

---

### TRANSLATION RESULT

| `--formular-font-pattern`       | 用于识别公式文本的字体模式                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--formular-font-size-threshold` | 用于识别公式文本的字体大小阈值（单位：磅）                                   | `pdf2zh_next example.pdf --formular-font-size-threshold 10`                                                            |
| `--formular-font-color-threshold` | 用于识别公式文本的字体颜色阈值（RGB 十六进制，例如 `#000000` 表示黑色）    | `pdf2zh_next example.pdf --formular-font-color-threshold "#000000"`                                                    |
| `--formular-ocr`                | 启用公式的 OCR 以提高识别率                                          | `pdf2zh_next example.pdf --formular-ocr`                                                                               |
| `--formular-ocr-dpi`            | 公式 OCR 的 DPI 设置（默认：300）                                             | `pdf2zh_next example.pdf --formular-ocr-dpi 300`                                                                       |
| `--formular-ocr-lang`           | 公式 OCR 的语言（默认：`eng`）                                              | `pdf2zh_next example.pdf --formular-ocr-lang eng`                                                                      |
`--formular-char-pattern ".*"`                                                                                                                                                                                                                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--formular-char-pattern-regex` | Whether to use regex for formular-char-pattern (default: false)                        | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-regex true`                           | `--formular-char-pattern-regex false`                                                                                                                                                                                                                                                       |
| `--formular-char-pattern-ignorecase` | Whether to ignore case when matching formular-char-pattern (default: false)           | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-ignorecase true`                      | `--formular-char-pattern-ignorecase false`                                                                                                                                                                                                                                                  |
| `--formular-char-pattern-invert` | Whether to invert the matching of formular-char-pattern (default: false)               | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-invert true`                          | `--formular-char-pattern-invert false`                                                                                                                                                                                                                                                      |
| `--formular-char-pattern-wholeword` | Whether to match whole words only for formular-char-pattern (default: false)           | `pdf2zh_next example.pdf --formular-char-pattern "MS" --formular-char-pattern-wholeword true`                         | `--formular-char-pattern-wholeword false`                                                                                                                                                                                                                                                   |
| `--formular-char-pattern-multiline` | Whether to match multiline for formular-char-pattern (default: false)                  | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-multiline true`                       | `--formular-char-pattern-multiline false`                                                                                                                                                                                                                                                   |

---

### OUTPUT

| `--formular-char-pattern`       | 用于识别公式文本的字符模式                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            | `--formular-char-pattern ".*"`                                                                                                                                                                                                                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--formular-char-pattern-regex` | 是否对 formular-char-pattern 使用正则表达式（默认值：false）                        | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-regex true`                           | `--formular-char-pattern-regex false`                                                                                                                                                                                                                                                       |
| `--formular-char-pattern-ignorecase` | 匹配 formular-char-pattern 时是否忽略大小写（默认值：false）           | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-ignorecase true`                      | `--formular-char-pattern-ignorecase false`                                                                                                                                                                                                                                                  |
| `--formular-char-pattern-invert` | 是否反转 formular-char-pattern 的匹配（默认值：false）               | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-invert true`                          | `--formular-char-pattern-invert false`                                                                                                                                                                                                                                                      |
| `--formular-char-pattern-wholeword` | 是否仅匹配 formular-char-pattern 的完整单词（默认值：false）           | `pdf2zh_next example.pdf --formular-char-pattern "MS" --formular-char-pattern-wholeword true`                         | `--formular-char-pattern-wholeword false`                                                                                                                                                                                                                                                   |
| `--formular-char-pattern-multiline` | 是否对 formular-char-pattern 进行多行匹配（默认值：false）                  | `pdf2zh_next example.pdf --formular-char-pattern "MS.*" --formular-char-pattern-multiline true`                       | `--formular-char-pattern-multiline false`                                                                                                                                                                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-split-short-lines`        | Disable splitting short lines into different paragraphs                                 | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--line-split-length`           | The maximum number of characters in a line that will be considered as a short line       | `pdf2zh_next example.pdf --line-split-length 20`                                                                      |
| `--line-split-max-lines`        | The maximum number of short lines that can be merged into a paragraph                    | `pdf2zh_next example.pdf --line-split-max-lines 5`                                                                    |
| `--line-split-min-lines`        | The minimum number of short lines that can be merged into a paragraph                    | `pdf2zh_next example.pdf --line-split-min-lines 2`                                                                    |

---

### TRANSLATION RESULT

| `--split-short-lines`           | 强制将短行拆分为不同的段落                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-split-short-lines`        | 禁用将短行拆分为不同的段落                                 | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--line-split-length`           | 一行中将被视为短行的最大字符数       | `pdf2zh_next example.pdf --line-split-length 20`                                                                      |
| `--line-split-max-lines`        | 可以合并为一个段落的短行最大数量                    | `pdf2zh_next example.pdf --line-split-max-lines 5`                                                                    |
| `--line-split-min-lines`        | 可以合并为一个段落的短行最小数量                    | `pdf2zh_next example.pdf --line-split-min-lines 2`                                                                    |
---

### OUTPUT

| `--short-line-split-factor`     | 短行分割阈值因子                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | Skip OCR step                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-layout`                 | Skip layout analysis step                                                               | `pdf2zh_next example.pdf --skip-layout`                                                                               |
| `--skip-html`                   | Skip HTML generation step                                                               | `pdf2zh_next example.pdf --skip-html`                                                                                 |
| `--skip-pdf`                    | Skip PDF generation step                                                               | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--skip-all`                    | Skip all steps except for the first step (PDF parsing)                                 | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--only-clean`                  | Only perform PDF cleaning step                                                         | `pdf2zh_next example.pdf --only-clean`                                                                                |
| `--only-translate`              | Only perform translation step                                                          | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--only-ocr`                    | Only perform OCR step                                                                  | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-layout`                 | Only perform layout analysis step                                                      | `pdf2zh_next example.pdf --only-layout`                                                                               |
| `--only-html`                   | Only perform HTML generation step                                                      | `pdf2zh_next example.pdf --only-html`                                                                                 |
| `--only-pdf`                    | Only perform PDF generation step                                                      | `pdf2zh_next example.pdf --only-pdf`                                                                                  |

---

### OUTPUT

| `--skip-clean`                  | 跳过 PDF 清理步骤                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | 跳过翻译步骤                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | 跳过 OCR 步骤                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-layout`                 | 跳过布局分析步骤                                                               | `pdf2zh_next example.pdf --skip-layout`                                                                               |
| `--skip-html`                   | 跳过 HTML 生成步骤                                                               | `pdf2zh_next example.pdf --skip-html`                                                                                 |
| `--skip-pdf`                    | 跳过 PDF 生成步骤                                                               | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--skip-all`                    | 跳过除第一步（PDF 解析）外的所有步骤                                 | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--only-clean`                  | 仅执行 PDF 清理步骤                                                         | `pdf2zh_next example.pdf --only-clean`                                                                                |
| `--only-translate`              | 仅执行翻译步骤                                                          | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--only-ocr`                    | 仅执行 OCR 步骤                                                                  | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-layout`                 | 仅执行布局分析步骤                                                      | `pdf2zh_next example.pdf --only-layout`                                                                               |
| `--only-html`                   | 仅执行 HTML 生成步骤                                                      | `pdf2zh_next example.pdf --only-html`                                                                                 |
| `--only-pdf`                    | 仅执行 PDF 生成步骤                                                      | `pdf2zh_next example.pdf --only-pdf`                                                                                  |
| `--dual-keep-first`             | Put original pages first in dual PDF mode                                               | `pdf2zh_next example.pdf --dual-keep-first`                                                                           |
| `--dual-remove-original`        | Remove original pages in dual PDF mode                                                   | `pdf2zh_next example.pdf --dual-remove-original`                                                                      |
| `--dual-remove-translated`      | Remove translated pages in dual PDF mode                                                 | `pdf2zh_next example.pdf --dual-remove-translated`                                                                    |
| `--dual-remove-both`            | Remove both original and translated pages in dual PDF mode (useful for manual creation) | `pdf2zh_next example.pdf --dual-remove-both`                                                                          |
| `--dual-only-translated`        | Only include translated pages in dual PDF mode                                           | `pdf2zh_next example.pdf --dual-only-translated`                                                                      |
| `--dual-only-original`          | Only include original pages in dual PDF mode                                             | `pdf2zh_next example.pdf --dual-only-original`                                                                        |

---

### OUTPUT

| `--dual-translate-first`        | 在双页 PDF 模式下将翻译后的页面放在前面                                       | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-keep-first`             | 在双页 PDF 模式下将原始页面放在前面                                           | `pdf2zh_next example.pdf --dual-keep-first`                                                                           |
| `--dual-remove-original`        | 在双页 PDF 模式下移除原始页面                                                 | `pdf2zh_next example.pdf --dual-remove-original`                                                                      |
| `--dual-remove-translated`      | 在双页 PDF 模式下移除翻译后的页面                                             | `pdf2zh_next example.pdf --dual-remove-translated`                                                                    |
| `--dual-remove-both`            | 在双页 PDF 模式下同时移除原始页面和翻译后的页面（适用于手动创建场景）           | `pdf2zh_next example.pdf --dual-remove-both`                                                                          |
| `--dual-only-translated`        | 在双页 PDF 模式下仅包含翻译后的页面                                           | `pdf2zh_next example.pdf --dual-only-translated`                                                                      |
| `--dual-only-original`          | 在双页 PDF 模式下仅包含原始页面                                               | `pdf2zh_next example.pdf --dual-only-original`                                                                        |
If the rich text translation is not working correctly, you can use this option to disable it.                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |

---

### TRANSLATION RESULT

| `--disable-rich-text-translate` | 禁用富文本翻译                                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               | 如果富文本翻译无法正常工作，可以使用此选项禁用它。                   |
[Documentation of Translation Services](https://pdf2zh-next.com/translation-services.html#enhance-compatibility) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `--enhance-context`             | Enable context enhancement options                                                      | `pdf2zh_next example.pdf --enhance-context`                                                                           | [Documentation of Translation Services](https://pdf2zh-next.com/translation-services.html#enhance-context)       |
| `--enhance-math`                | Enable math enhancement options                                                         | `pdf2zh_next example.pdf --enhance-math`                                                                              | [Documentation of Translation Services](https://pdf2zh-next.com/translation-services.html#enhance-math)          |
| `--enhance-table`               | Enable table enhancement options                                                        | `pdf2zh_next example.pdf --enhance-table`                                                                             | [Documentation of Translation Services](https://pdf2zh-next.com/translation-services.html#enhance-table)         |
| `--enhance-text`                | Enable text enhancement options                                                         | `pdf2zh_next example.pdf --enhance-text`                                                                              | [Documentation of Translation Services](https://pdf2zh-next.com/translation-services.html#enhance-text)          |
| `--enhance-translation-quality` | Enable translation quality enhancement options                                          | `pdf2zh_next example.pdf --enhance-translation-quality`                                                               | [Documentation of Translation Services](https://pdf2zh-next.com/translation-services.html#enhance-translation-quality) |
| `-f`, `--force`                 | Force overwrite existing output file                                                    | `pdf2zh_next example.pdf -f`                                                                                          | [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html#force-overwrite)                          |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next -h`                                                                                                      | [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html#help)                                     |
| `--lang`                        | Set the target language for translation (default: `zh`)                                 | `pdf2zh_next example.pdf --lang en`                                                                                   | [Supported Languages](https://pdf2zh-next.com/translation-services.html#supported-languages)                    |
| `--log-level`                   | Set the log level (default: `info`)                                                     | `pdf2zh_next example.pdf --log-level debug`                                                                           | [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html#log-level)                                |
| `-o`, `--output`                | Specify the output file path                                                            | `pdf2zh_next example.pdf -o output.pdf`                                                                               | [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output)                                   |
| `--open`                        | Automatically open the output file after translation                                    | `pdf2zh_next example.pdf --open`                                                                                      | [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html#open)                                     |
| `-s`, `--service`               | Specify the translation service to use (default: `openai`)                              | `pdf2zh_next example.pdf -s aliyun`                                                                                   | [Translation Services](https://pdf2zh-next.com/translation-services.html)                                       |
| `-t`, `--target`                | Set the target language for translation (default: `zh`)                                 | `pdf2zh_next example.pdf -t en`                                                                                       | [Supported Languages](https://pdf2zh-next.com/translation-services.html#supported-languages)                    |
| `-v`, `--version`               | Show the version of pdf2zh and exit                                                     | `pdf2zh_next -v`                                                                                                      | [Command Line](https://pdf2zh-next.com/getting-started/USAGE_cli.html#version)                                  |


---

### OUTPUT

| `--enhance-compatibility`       | 启用所有兼容性增强选项                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     | [翻译服务文档](https://pdf2zh-next.com/translation-services.html#enhance-compatibility) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `--enhance-context`             | 启用上下文增强选项                                                      | `pdf2zh_next example.pdf --enhance-context`                                                                           | [翻译服务文档](https://pdf2zh-next.com/translation-services.html#enhance-context)       |
| `--enhance-math`                | 启用数学公式增强选项                                                         | `pdf2zh_next example.pdf --enhance-math`                                                                              | [翻译服务文档](https://pdf2zh-next.com/translation-services.html#enhance-math)          |
| `--enhance-table`               | 启用表格增强选项                                                        | `pdf2zh_next example.pdf --enhance-table`                                                                             | [翻译服务文档](https://pdf2zh-next.com/translation-services.html#enhance-table)         |
| `--enhance-text`                | 启用文本增强选项                                                         | `pdf2zh_next example.pdf --enhance-text`                                                                              | [翻译服务文档](https://pdf2zh-next.com/translation-services.html#enhance-text)          |
| `--enhance-translation-quality` | 启用翻译质量增强选项                                          | `pdf2zh_next example.pdf --enhance-translation-quality`                                                               | [翻译服务文档](https://pdf2zh-next.com/translation-services.html#enhance-translation-quality) |
| `-f`, `--force`                 | 强制覆盖现有输出文件                                                    | `pdf2zh_next example.pdf -f`                                                                                          | [命令行](https://pdf2zh-next.com/getting-started/USAGE_cli.html#force-overwrite)                          |
| `-h`, `--help`                  | 显示帮助信息并退出                                                              | `pdf2zh_next -h`                                                                                                      | [命令行](https://pdf2zh-next.com/getting-started/USAGE_cli.html#help)                                     |
| `--lang`                        | 设置翻译目标语言（默认：`zh`）                                 | `pdf2zh_next example.pdf --lang en`                                                                                   | [支持的语言](https://pdf2zh-next.com/translation-services.html#supported-languages)                    |
| `--log-level`                   | 设置日志级别（默认：`info`）                                                     | `pdf2zh_next example.pdf --log-level debug`                                                                           | [命令行](https://pdf2zh-next.com/getting-started/USAGE_cli.html#log-level)                                |
| `-o`, `--output`                | 指定输出文件路径                                                            | `pdf2zh_next example.pdf -o output.pdf`                                                                               | [命令行](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output)                                   |
| `--open`                        | 翻译完成后自动打开输出文件                                    | `pdf2zh_next example.pdf --open`                                                                                      | [命令行](https://pdf2zh-next.com/getting-started/USAGE_cli.html#open)                                     |
| `-s`, `--service`               | 指定使用的翻译服务（默认：`openai`）                              | `pdf2zh_next example.pdf -s aliyun`                                                                                   | [翻译服务](https://pdf2zh-next.com/translation-services.html)                                       |
| `-t`, `--target`                | 设置翻译目标语言（默认：`zh`）                                 | `pdf2zh_next example.pdf -t en`                                                                                       | [支持的语言](https://pdf2zh-next.com/translation-services.html#supported-languages)                    |
| `-v`, `--version`               | 显示 pdf2zh 版本并退出                                                     | `pdf2zh_next -v`                                                                                                      | [命令行](https://pdf2zh-next.com/getting-started/USAGE_cli.html#version)                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-separate-pages`          | Use separate pages mode                                                                 | `pdf2zh_next example.pdf --use-separate-pages`                                                                        |
| `--use-single-page`             | Use single page mode (default)                                                          | `pdf2zh_next example.pdf --use-single-page`                                                                           |
| `--use-columns`                 | Use columns mode                                                                        | `pdf2zh_next example.pdf --use-columns`                                                                               |
| `--use-columns-js`              | Use columns mode with JavaScript                                                        | `pdf2zh_next example.pdf --use-columns-js`                                                                            |
| `--use-overlay`                 | Use overlay mode                                                                        | `pdf2zh_next example.pdf --use-overlay`                                                                               |
| `--use-overlay-js`              | Use overlay mode with JavaScript                                                        | `pdf2zh_next example.pdf --use-overlay-js`                                                                            |
| `--use-immersive-translate`     | Use Immersive Translate mode                                                            | `pdf2zh_next example.pdf --use-immersive-translate`                                                                   |

---

### OUTPUT

| `--use-alternating-pages-dual`  | 为双栏 PDF 使用交替页面模式                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | 为单栏 PDF 使用交替页面模式                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-separate-pages`          | 使用分离页面模式                                                                 | `pdf2zh_next example.pdf --use-separate-pages`                                                                        |
| `--use-single-page`             | 使用单页模式（默认）                                                          | `pdf2zh_next example.pdf --use-single-page`                                                                           |
| `--use-columns`                 | 使用列模式                                                                        | `pdf2zh_next example.pdf --use-columns`                                                                               |
| `--use-columns-js`              | 使用带 JavaScript 的列模式                                                        | `pdf2zh_next example.pdf --use-columns-js`                                                                            |
| `--use-overlay`                 | 使用覆盖模式                                                                        | `pdf2zh_next example.pdf --use-overlay`                                                                               |
| `--use-overlay-js`              | 使用带 JavaScript 的覆盖模式                                                        | `pdf2zh_next example.pdf --use-overlay-js`                                                                            |
| `--use-immersive-translate`     | 使用沉浸式翻译模式                                                            | `pdf2zh_next example.pdf --use-immersive-translate`                                                                   |
`no_watermark` | `no_watermark`, `watermark`, `watermark_only` |

---

### OUTPUT

| `--watermark-output-mode`       | PDF 文件的水印输出模式                                                     | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `no_watermark` | `no_watermark`, `watermark`, `watermark_only` |
`50`                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `--max-concurrent-parts`        | Maximum concurrent parts for translation                                                | `pdf2zh_next example.pdf --max-concurrent-parts 2`                                                                    | `2`                                                          |
| `--max-concurrent-requests`     | Maximum concurrent requests for translation                                            | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 | `5`                                                          |
| `--max-retries`                 | Maximum retries for translation requests                                               | `pdf2zh_next example.pdf --max-retries 3`                                                                             | `3`                                                          |
| `--retry-delay`                 | Delay in seconds between retries                                                        | `pdf2zh_next example.pdf --retry-delay 2`                                                                             | `2`                                                          |
| `--request-timeout`             | Timeout in seconds for each translation request                                         | `pdf2zh_next example.pdf --request-timeout 30`                                                                        | `30`                                                         |
| `--ocr-timeout`                 | Timeout in seconds for OCR processing                                                   | `pdf2zh_next example.pdf --ocr-timeout 60`                                                                            | `60`                                                         |
| `--translator-timeout`          | Timeout in seconds for translation processing                                           | `pdf2zh_next example.pdf --translator-timeout 30`                                                                     | `30`                                                         |
| `--ocr-retries`                 | Maximum retries for OCR processing                                                      | `pdf2zh_next example.pdf --ocr-retries 3`                                                                             | `3`                                                          |
| `--translator-retries`          | Maximum retries for translation processing                                              | `pdf2zh_next example.pdf --translator-retries 3`                                                                      | `3`                                                          |
| `--ocr-retry-delay`             | Delay in seconds between OCR retries                                                    | `pdf2zh_next example.pdf --ocr-retry-delay 2`                                                                         | `2`                                                          |
| `--translator-retry-delay`      | Delay in seconds between translation retries                                            | `pdf2zh_next example.pdf --translator-retry-delay 2`                                                                  | `2`                                                          |
| `--ocr-concurrent-requests`     | Maximum concurrent requests for OCR processing                                           | `pdf2zh_next example.pdf --ocr-concurrent-requests 5`                                                                  | `5`                                                          |
| `--translator-concurrent-requests` | Maximum concurrent requests for translation processing                                   | `pdf2zh_next example.pdf --translator-concurrent-requests 5`                                                           | `5`                                                          |
| `--ocr-concurrent-timeout`      | Timeout in seconds for OCR concurrent processing                                        | `pdf2zh_next example.pdf --ocr-concurrent-timeout 60`                                                                 | `60`                                                         |
| `--translator-concurrent-timeout` | Timeout in seconds for translation concurrent processing                                | `pdf2zh_next example.pdf --translator-concurrent-timeout 30`                                                          | `30`                                                         |

---

### OUTPUT

| `--max-pages-per-part`          | 每部分翻译的最大页数                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     | `50`                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `--max-concurrent-parts`        | 翻译的最大并发部分数                                                | `pdf2zh_next example.pdf --max-concurrent-parts 2`                                                                    | `2`                                                          |
| `--max-concurrent-requests`     | 翻译的最大并发请求数                                            | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 | `5`                                                          |
| `--max-retries`                 | 翻译请求的最大重试次数                                               | `pdf2zh_next example.pdf --max-retries 3`                                                                             | `3`                                                          |
| `--retry-delay`                 | 重试之间的延迟（秒）                                                        | `pdf2zh_next example.pdf --retry-delay 2`                                                                             | `2`                                                          |
| `--request-timeout`             | 每个翻译请求的超时时间（秒）                                         | `pdf2zh_next example.pdf --request-timeout 30`                                                                        | `30`                                                         |
| `--ocr-timeout`                 | OCR 处理的超时时间（秒）                                                   | `pdf2zh_next example.pdf --ocr-timeout 60`                                                                            | `60`                                                         |
| `--translator-timeout`          | 翻译处理的超时时间（秒）                                           | `pdf2zh_next example.pdf --translator-timeout 30`                                                                     | `30`                                                         |
| `--ocr-retries`                 | OCR 处理的最大重试次数                                                      | `pdf2zh_next example.pdf --ocr-retries 3`                                                                             | `3`                                                          |
| `--translator-retries`          | 翻译处理的最大重试次数                                              | `pdf2zh_next example.pdf --translator-retries 3`                                                                      | `3`                                                          |
| `--ocr-retry-delay`             | OCR 重试之间的延迟（秒）                                                    | `pdf2zh_next example.pdf --ocr-retry-delay 2`                                                                         | `2`                                                          |
| `--translator-retry-delay`      | 翻译重试之间的延迟（秒）                                            | `pdf2zh_next example.pdf --translator-retry-delay 2`                                                                  | `2`                                                          |
| `--ocr-concurrent-requests`     | OCR 处理的最大并发请求数                                           | `pdf2zh_next example.pdf --ocr-concurrent-requests 5`                                                                  | `5`                                                          |
| `--translator-concurrent-requests` | 翻译处理的最大并发请求数                                   | `pdf2zh_next example.pdf --translator-concurrent-requests 5`                                                           | `5`                                                          |
| `--ocr-concurrent-timeout`      | OCR 并发处理的超时时间（秒）                                        | `pdf2zh_next example.pdf --ocr-concurrent-timeout 60`                                                                 | `60`                                                         |
| `--translator-concurrent-timeout` | 翻译并发处理的超时时间（秒）                                | `pdf2zh_next example.pdf --translator-concurrent-timeout 30`                                                          | `30`                                                         |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Method to translate table text (experimental)                                           | `pdf2zh_next example.pdf --translate-table-text-method "translate"`                                                   |
| `--translate-table-text-prompt` | Prompt to translate table text (experimental)                                            | `pdf2zh_next example.pdf --translate-table-text-prompt "Translate the following table into Chinese, keep the format"` |
| `--translate-table-text-model`  | Model to translate table text (experimental)                                             | `pdf2zh_next example.pdf --translate-table-text-model "gpt-4o"`                                                       |
| `--translate-table-text-api`    | API to translate table text (experimental)                                               | `pdf2zh_next example.pdf --translate-table-text-api "openai"`                                                         |
| `--translate-table-text-key`    | API key to translate table text (experimental)                                            | `pdf2zh_next example.pdf --translate-table-text-key "sk-..."`                                                         |
| `--translate-table-text-url`    | API URL to translate table text (experimental)                                            | `pdf2zh_next example.pdf --translate-table-text-url "https://api.openai.com/v1/chat/completions"`                     |
| `--translate-table-text-proxy`  | Proxy to translate table text (experimental)                                              | `pdf2zh_next example.pdf --translate-table-text-proxy "http://127.0.0.1:7890"`                                       |

---

### TRANSLATION RESULT

| `--translate-table-text`        | 翻译表格文本（实验性功能）                                                               | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | 翻译表格文本的方法（实验性功能）                                                           | `pdf2zh_next example.pdf --translate-table-text-method "translate"`                                                   |
| `--translate-table-text-prompt` | 翻译表格文本的提示词（实验性功能）                                                        | `pdf2zh_next example.pdf --translate-table-text-prompt "Translate the following table into Chinese, keep the format"` |
| `--translate-table-text-model`  | 翻译表格文本的模型（实验性功能）                                                           | `pdf2zh_next example.pdf --translate-table-text-model "gpt-4o"`                                                       |
| `--translate-table-text-api`    | 翻译表格文本的 API（实验性功能）                                                           | `pdf2zh_next example.pdf --translate-table-text-api "openai"`                                                         |
| `--translate-table-text-key`    | 翻译表格文本的 API 密钥（实验性功能）                                                      | `pdf2zh_next example.pdf --translate-table-text-key "sk-..."`                                                         |
| `--translate-table-text-url`    | 翻译表格文本的 API URL（实验性功能）                                                       | `pdf2zh_next example.pdf --translate-table-text-url "https://api.openai.com/v1/chat/completions"`                     |
| `--translate-table-text-proxy`  | 翻译表格文本的代理（实验性功能）                                                           | `pdf2zh_next example.pdf --translate-table-text-proxy "http://127.0.0.1:7890"`                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection-force` | Force skip scanned detection                                                            | `pdf2zh_next example.pdf --skip-scanned-detection-force`                                                              |
| `--skip-scanned-detection-threshold` | Threshold for scanned detection (default: 0.5)                                         | `pdf2zh_next example.pdf --skip-scanned-detection-threshold 0.3`                                                      |
| `--skip-scanned-detection-method` | Method for scanned detection (default: `"mixed"`)                                      | `pdf2zh_next example.pdf --skip-scanned-detection-method "mixed"`                                                      |
| `--skip-scanned-detection-method` | Available methods: `"mixed"`, `"ocr"`, `"layout"`                                      | `pdf2zh_next example.pdf --skip-scanned-detection-method "ocr"`                                                        |

---

### OUTPUT

| `--skip-scanned-detection`      | 跳过扫描检测                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection-force` | 强制跳过扫描检测                                                            | `pdf2zh_next example.pdf --skip-scanned-detection-force`                                                              |
| `--skip-scanned-detection-threshold` | 扫描检测阈值 (默认：0.5)                                         | `pdf2zh_next example.pdf --skip-scanned-detection-threshold 0.3`                                                      |
| `--skip-scanned-detection-method` | 扫描检测方法 (默认：`"mixed"`)                                      | `pdf2zh_next example.pdf --skip-scanned-detection-method "mixed"`                                                      |
| `--skip-scanned-detection-method` | 可用方法：`"mixed"`, `"ocr"`, `"layout"`                                      | `pdf2zh_next example.pdf --skip-scanned-detection-method "ocr"`                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-background`   | Background color for OCR workaround, default is white                                   | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-background "#ff0000"`                                      |
| `--ocr-workaround-foreground`   | Foreground color for OCR workaround, default is black                                   | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-foreground "#00ff00"`                                      |
| `--ocr-workaround-font`         | Font for OCR workaround, default is "Arial"                                             | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font "SimHei"`                                              |
| `--ocr-workaround-font-size`    | Font size for OCR workaround, default is 12                                             | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-size 16`                                              |
| `--ocr-workaround-line-spacing` | Line spacing for OCR workaround, default is 1.0                                         | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-line-spacing 1.5`                                          |

---

### TRANSLATION RESULT

| `--ocr-workaround`              | 强制将翻译后的文本设置为黑色并添加白色背景                                            | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-background`   | OCR 修复的背景颜色，默认为白色                                                          | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-background "#ff0000"`                                      |
| `--ocr-workaround-foreground`   | OCR 修复的前景颜色，默认为黑色                                                          | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-foreground "#00ff00"`                                      |
| `--ocr-workaround-font`         | OCR 修复的字体，默认为 "Arial"                                                          | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font "SimHei"`                                              |
| `--ocr-workaround-font-size`    | OCR 修复的字体大小，默认为 12                                                            | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-size 16`                                              |
| `--ocr-workaround-line-spacing` | OCR 修复的行间距，默认为 1.0                                                            | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-line-spacing 1.5`                                          |
---

### TRANSLATION RESULT

| `--auto-enable-ocr-workaround`  | 启用自动 OCR 临时解决方案。如果检测到文档为重度扫描件，将尝试启用 OCR 处理并跳过进一步的扫描检测。详情请参阅文档。（默认值：False） | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
|---------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--page-range-mode`             | Set the page range mode. Options: `pdf` or `ocr`. Default: `pdf`.                     | `pdf2zh_next example.pdf --pages 1-5 --page-range-mode ocr`                                                           |
| `--output`                      | Set the output PDF file path.                                                         | `pdf2zh_next example.pdf --output example_translated.pdf`                                                             |
| `--verbose`                     | Enable verbose output.                                                                | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--debug`                       | Enable debug output.                                                                  | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Show help message and exit.                                                           | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Show version and exit.                                                                | `pdf2zh_next --version`                                                                                               |

---

### TRANSLATED TEXT

| `--only-include-translated-page` | 仅在输出 PDF 中包含已翻译的页面。仅在使用了 `--pages` 参数时生效。 | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page` |
|---------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------|
| `--page-range-mode`             | 设置页面范围模式。选项：`pdf` 或 `ocr`。默认值：`pdf`。          | `pdf2zh_next example.pdf --pages 1-5 --page-range-mode ocr`         |
| `--output`                      | 设置输出 PDF 文件的路径。                                       | `pdf2zh_next example.pdf --output example_translated.pdf`           |
| `--verbose`                     | 启用详细输出。                                                  | `pdf2zh_next example.pdf --verbose`                                 |
| `--debug`                       | 启用调试输出。                                                  | `pdf2zh_next example.pdf --debug`                                   |
| `--help`                        | 显示帮助信息并退出。                                            | `pdf2zh_next --help`                                                |
| `--version`                     | 显示版本信息并退出。                                            | `pdf2zh_next --version`                                             |
`false` |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------- |

---

### TRANSLATION RESULT

| `--no-merge-alternating-line-numbers` | 禁用合并带有行号的文档中的交替行号和文本段落 | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                | `false` |
| -------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------- |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-formula-lines` | 禁用移除段落区域内的非公式行                                                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |

---

### OUTPUT

| `--no-remove-non-formula-lines` | 禁用移除段落区域内的非公式行 | `pdf2zh_next example.pdf --no-remove-non-formula-lines` |
`0.85` |
| `--non-formula-line-iou-threshold` | 设置用于识别非公式行的 IoU 阈值 (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.85` |

---

### OUTPUT

| `--non-formula-line-iou-threshold` | 设置用于识别非公式行的 IoU 阈值 (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.85` |
0.9      |
| `--figure-table-protection-off`       | Disable figure and table protection                                                                          | `pdf2zh_next example.pdf --figure-table-protection-off`                                                     |          |

---

### OUTPUT

| `--figure-table-protection-threshold` | 设置图表保护阈值（0.0-1.0）。图表内的行将不会被处理 | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95` | 0.9      |
| `--figure-table-protection-off`       | 禁用图表保护                                      | `pdf2zh_next example.pdf --figure-table-protection-off`          |          |
---

### OUTPUT

| `--skip-formula-offset-calculation` | 在处理过程中跳过公式偏移计算          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### GUI 参数

| `--server-name <server-name>`   | Set server name                        | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--server-port <server-port>`   | Set server port                        | `pdf2zh_next --gui --server-port 8080`          |
| `--auth <username:password>`    | Set username and password              | `pdf2zh_next --gui --auth admin:password`       |
| `--ssl-keyfile <ssl-keyfile>`   | Set SSL key file                       | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile <ssl-certfile>` | Set SSL certificate file               | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
| `--ssl-keyfile-password`        | Set SSL key file password              | `pdf2zh_next --gui --ssl-keyfile-password pass` |

---

### TRANSLATED TEXT

| 选项                          | 功能                                   | 示例                                               |
| ----------------------------- | -------------------------------------- | -------------------------------------------------- |
| `--share`                       | 启用共享模式                           | `pdf2zh_next --gui --share`                        |
| `--server-name <server-name>`   | 设置服务器名称                         | `pdf2zh_next --gui --server-name 0.0.0.0`          |
| `--server-port <server-port>`   | 设置服务器端口                         | `pdf2zh_next --gui --server-port 8080`             |
| `--auth <username:password>`    | 设置用户名和密码                       | `pdf2zh_next --gui --auth admin:password`          |
| `--ssl-keyfile <ssl-keyfile>`   | 设置 SSL 密钥文件                      | `pdf2zh_next --gui --ssl-keyfile key.pem`          |
| `--ssl-certfile <ssl-certfile>` | 设置 SSL 证书文件                      | `pdf2zh_next --gui --ssl-certfile cert.pem`        |
| `--ssl-keyfile-password`        | 设置 SSL 密钥文件密码                  | `pdf2zh_next --gui --ssl-keyfile-password pass`    |
|
|---------------------------------|----------------------------------------|-------------------------------------------------|--|
| `--auto-close`                  | Automatically close the window after the task is completed. | `pdf2zh_next --gui --auto-close`                |  |
| `--auto-open`                   | Automatically open the output directory after the task is completed. | `pdf2zh_next --gui --auto-open`                 |  |
| `--auto-start`                  | Automatically start the task after the window is opened. | `pdf2zh_next --gui --auto-start`                |  |
| `--debug`                       | Enable debug mode.                     | `pdf2zh_next --gui --debug`                     |  |
| `--help`                        | Show help message.                     | `pdf2zh_next --gui --help`                      |  |
| `--host`                        | The host address to listen on.         | `pdf2zh_next --gui --host 0.0.0.0`              |  |
| `--log-level`                   | Set the log level.                     | `pdf2zh_next --gui --log-level debug`           |  |
| `--log-path`                    | Path to the log file.                  | `pdf2zh_next --gui --log-path /path/to/log.txt` |  |
| `--no-browser`                  | Do not open the browser automatically. | `pdf2zh_next --gui --no-browser`                |  |
| `--port`                        | The port to listen on.                 | `pdf2zh_next --gui --port 8080`                 |  |
| `--show`                        | Show the window.                       | `pdf2zh_next --gui --show`                      |  |
| `--version`                     | Show the version.                      | `pdf2zh_next --gui --version`                   |  |

---

### TRANSLATED TEXT

| `--auth-file`                   | 认证文件的路径                     | `pdf2zh_next --gui --auth-file /path`           |  |
|---------------------------------|------------------------------------|-------------------------------------------------|--|
| `--auto-close`                  | 任务完成后自动关闭窗口             | `pdf2zh_next --gui --auto-close`                |  |
| `--auto-open`                   | 任务完成后自动打开输出目录         | `pdf2zh_next --gui --auto-open`                 |  |
| `--auto-start`                  | 窗口打开后自动开始任务             | `pdf2zh_next --gui --auto-start`                |  |
| `--debug`                       | 启用调试模式                       | `pdf2zh_next --gui --debug`                     |  |
| `--help`                        | 显示帮助信息                       | `pdf2zh_next --gui --help`                      |  |
| `--host`                        | 监听的 host 地址                   | `pdf2zh_next --gui --host 0.0.0.0`              |  |
| `--log-level`                   | 设置日志级别                       | `pdf2zh_next --gui --log-level debug`           |  |
| `--log-path`                    | 日志文件的路径                     | `pdf2zh_next --gui --log-path /path/to/log.txt` |  |
| `--no-browser`                  | 不自动打开浏览器                   | `pdf2zh_next --gui --no-browser`                |  |
| `--port`                        | 监听的端口                         | `pdf2zh_next --gui --port 8080`                 |  |
| `--show`                        | 显示窗口                           | `pdf2zh_next --gui --show`                      |  |
| `--version`                     | 显示版本信息                       | `pdf2zh_next --gui --version`                   |  |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--config-file-path`            | Path to the config file                | `pdf2zh_next --gui --config-file-path /path`    |
| `--log-file-path`               | Path to the log file                   | `pdf2zh_next --gui --log-file-path /path`       |
| `--window-theme`                | Set the window theme                   | `pdf2zh_next --gui --window-theme dark`         |
| `--window-theme-mode`           | Set the window theme mode              | `pdf2zh_next --gui --window-theme-mode system`  |
| `--window-color-override`       | Set the window color override          | `pdf2zh_next --gui --window-color-override red` |

---

### OUTPUT

| `--welcome-page`                | 欢迎页面的 HTML 文件路径               | `pdf2zh_next --gui --welcome-page /path`        |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--config-file-path`            | 配置文件路径                           | `pdf2zh_next --gui --config-file-path /path`    |
| `--log-file-path`               | 日志文件路径                           | `pdf2zh_next --gui --log-file-path /path`       |
| `--window-theme`                | 设置窗口主题                           | `pdf2zh_next --gui --window-theme dark`         |
| `--window-theme-mode`           | 设置窗口主题模式                       | `pdf2zh_next --gui --window-theme-mode system`  |
| `--window-color-override`       | 设置窗口颜色覆盖                       | `pdf2zh_next --gui --window-color-override red` |
Enable Bing and OpenAI translation services in GUI mode. |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Bing"`       | Disable Bing translation service in GUI mode.            |
| `--service-config`              | Configuration for translation services | `pdf2zh_next --gui --service-config OpenAI.key=sk-...` | Set OpenAI API key in GUI mode.                          |
| `--service-config`              | Configuration for translation services | `pdf2zh_next --gui --service-config Bing.cookie=...` | Set Bing cookie in GUI mode.                             |
| `--service-config`              | Configuration for translation services | `pdf2zh_next --gui --service-config Aliyun.access_key_id=...` | Set Aliyun access key ID in GUI mode.                    |
| `--service-config`              | Configuration for translation services | `pdf2zh_next --gui --service-config Aliyun.access_key_secret=...` | Set Aliyun access key secret in GUI mode.                |
| `--service-config`              | Configuration for translation services | `pdf2zh_next --gui --service-config SiliconFlow.key=...` | Set SiliconFlow API key in GUI mode.                     |

---

### OUTPUT

| `--enabled-services`            | 启用的翻译服务           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | 在 GUI 模式下启用 Bing 和 OpenAI 翻译服务。 |
| ------------------------------- | ------------------------ | ---------------------------------------------------- | ------------------------------------------- |
| `--disabled-services`           | 禁用的翻译服务          | `pdf2zh_next --gui --disabled-services "Bing"`       | 在 GUI 模式下禁用 Bing 翻译服务。            |
| `--service-config`              | 翻译服务的配置 | `pdf2zh_next --gui --service-config OpenAI.key=sk-...` | 在 GUI 模式下设置 OpenAI API 密钥。                          |
| `--service-config`              | 翻译服务的配置 | `pdf2zh_next --gui --service-config Bing.cookie=...` | 在 GUI 模式下设置 Bing cookie。                             |
| `--service-config`              | 翻译服务的配置 | `pdf2zh_next --gui --service-config Aliyun.access_key_id=...` | 在 GUI 模式下设置 阿里云 访问密钥 ID。                    |
| `--service-config`              | 翻译服务的配置 | `pdf2zh_next --gui --service-config Aliyun.access_key_secret=...` | 在 GUI 模式下设置 阿里云 访问密钥密钥。                |
| `--service-config`              | 翻译服务的配置 | `pdf2zh_next --gui --service-config SiliconFlow.key=...` | 在 GUI 模式下设置 SiliconFlow API 密钥。                     |
| ------------------------------- | -------------------------------------- | ------------------------------------------------- |
| `--disable-gui-close-warning`   | Disable GUI close confirmation warning | `pdf2zh_next --gui --disable-gui-close-warning`   |
| `--disable-gui-save-warning`    | Disable GUI save confirmation warning  | `pdf2zh_next --gui --disable-gui-save-warning`    |

---

### OUTPUT

| `--disable-gui-sensitive-input` | 禁用 GUI 敏感输入            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
| ------------------------------- | ---------------------------- | ------------------------------------------------- |
| `--disable-gui-close-warning`   | 禁用 GUI 关闭确认警告        | `pdf2zh_next --gui --disable-gui-close-warning`   |
| `--disable-gui-save-warning`    | 禁用 GUI 保存确认警告        | `pdf2zh_next --gui --disable-gui-save-warning`    |
`false` | `boolean` |
|---------------------------------|----------------------------------------|-------------------------------------------------|---------|-----------|
| `--disable-gpu`                 | Disable GPU acceleration               | `pdf2zh_next --gui --disable-gpu`               | `false` | `boolean` |
| `--disable-update-check`        | Disable update check                   | `pdf2zh_next --gui --disable-update-check`      | `false` | `boolean` |
| `--disable-web-security`        | Disable web security                   | `pdf2zh_next --gui --disable-web-security`      | `false` | `boolean` |
| `--disable-zy`                  | Disable ZY translation                 | `pdf2zh_next --disable-zy`                      | `false` | `boolean` |
| `--enable-logging`              | Enable logging                         | `pdf2zh_next --gui --enable-logging`            | `false` | `boolean` |
| `--enable-unsafe-content`       | Enable unsafe content                  | `pdf2zh_next --gui --enable-unsafe-content`     | `false` | `boolean` |
| `--force-device-scale-factor`   | Force device scale factor              | `pdf2zh_next --gui --force-device-scale-factor=1.5` | `1.0`   | `number`  |
| `--proxy-server`                | Proxy server                           | `pdf2zh_next --gui --proxy-server="http://127.0.0.1:7890"` | `""`    | `string`  |
| `--user-data-dir`               | User data directory                    | `pdf2zh_next --gui --user-data-dir="./data"`    | `""`    | `string`  |

---

### TRANSLATION RESULT

| `--disable-config-auto-save`    | 禁用自动保存配置 | `pdf2zh_next --gui --disable-config-auto-save`  | `false` | `boolean` |
|---------------------------------|------------------|-------------------------------------------------|---------|-----------|
| `--disable-gpu`                 | 禁用 GPU 加速    | `pdf2zh_next --gui --disable-gpu`               | `false` | `boolean` |
| `--disable-update-check`        | 禁用更新检查     | `pdf2zh_next --gui --disable-update-check`      | `false` | `boolean` |
| `--disable-web-security`        | 禁用网页安全     | `pdf2zh_next --gui --disable-web-security`      | `false` | `boolean` |
| `--disable-zy`                  | 禁用 ZY 翻译     | `pdf2zh_next --disable-zy`                      | `false` | `boolean` |
| `--enable-logging`              | 启用日志记录     | `pdf2zh_next --gui --enable-logging`            | `false` | `boolean` |
| `--enable-unsafe-content`       | 启用不安全内容   | `pdf2zh_next --gui --enable-unsafe-content`     | `false` | `boolean` |
| `--force-device-scale-factor`   | 强制设备缩放因子 | `pdf2zh_next --gui --force-device-scale-factor=1.5` | `1.0`   | `number`  |
| `--proxy-server`                | 代理服务器       | `pdf2zh_next --gui --proxy-server="http://127.0.0.1:7890"` | `""`    | `string`  |
| `--user-data-dir`               | 用户数据目录     | `pdf2zh_next --gui --user-data-dir="./data"`    | `""`    | `string`  |
---

### OUTPUT

| `--server-port`                 | WebUI 端口                             | `pdf2zh_next --gui --server-port 7860`          |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--model`                       | Model name                             | `pdf2zh_next --model gpt-4o-mini`               |
| `--api-key`                     | API key                                | `pdf2zh_next --api-key sk-...`                  |
| `--base-url`                    | API base URL                           | `pdf2zh_next --base-url https://api.openai.com` |
| `--proxy`                       | API proxy                              | `pdf2zh_next --proxy http://127.0.0.1:7890`     |
| `--output-dir`                  | Output directory                       | `pdf2zh_next --output-dir ./output`             |
| `--doc-type`                    | Document type                          | `pdf2zh_next --doc-type paper`                  |
| `--doc-lang`                    | Document language                      | `pdf2zh_next --doc-lang en`                     |
| `--target-lang`                 | Target language                        | `pdf2zh_next --target-lang zh`                  |
| `--font`                        | Font family                            | `pdf2zh_next --font "Noto Sans SC"`             |
| `--font-size`                   | Font size                              | `pdf2zh_next --font-size 16`                    |
| `--line-spacing`                | Line spacing                           | `pdf2zh_next --line-spacing 1.5`                |
| `--page-margin`                 | Page margin                            | `pdf2zh_next --page-margin 2cm`                 |
| `--title-font-size`             | Title font size                        | `pdf2zh_next --title-font-size 20`              |
| `--heading1-font-size`          | Heading 1 font size                    | `pdf2zh_next --heading1-font-size 18`           |
| `--heading2-font-size`          | Heading 2 font size                    | `pdf2zh_next --heading2-font-size 16`           |
| `--heading3-font-size`          | Heading 3 font size                    | `pdf2zh_next --heading3-font-size 14`           |
| `--paragraph-spacing`           | Paragraph spacing                      | `pdf2zh_next --paragraph-spacing 12pt`          |
| `--image-dpi`                   | Image DPI                              | `pdf2zh_next --image-dpi 300`                   |
| `--image-quality`               | Image quality                          | `pdf2zh_next --image-quality 95`                |
| `--max-concurrent`              | Max concurrent requests                | `pdf2zh_next --max-concurrent 5`                |
| `--request-interval`            | Request interval (ms)                  | `pdf2zh_next --request-interval 1000`           |
| `--timeout`                     | Request timeout (s)                    | `pdf2zh_next --timeout 60`                      |
| `--retry-attempts`              | Retry attempts                         | `pdf2zh_next --retry-attempts 3`                |
| `--retry-delay`                 | Retry delay (ms)                       | `pdf2zh_next --retry-delay 2000`                |
| `--cache-dir`                   | Cache directory                        | `pdf2zh_next --cache-dir ./cache`               |
| `--cache-ttl`                   | Cache TTL (hours)                      | `pdf2zh_next --cache-ttl 24`                    |
| `--log-level`                   | Log level                              | `pdf2zh_next --log-level info`                  |
| `--log-file`                    | Log file path                          | `pdf2zh_next --log-file ./logs/app.log`         |
| `--config`                      | Config file path                       | `pdf2zh_next --config ./config.yaml`            |
| `--version`                     | Show version                           | `pdf2zh_next --version`                         |
| `--help`                        | Show help                              | `pdf2zh_next --help`                            |

---

### TRANSLATION RESULT

| `--ui-lang`                     | UI 语言                                | `pdf2zh_next --gui --ui-lang zh`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--model`                       | 模型名称                               | `pdf2zh_next --model gpt-4o-mini`               |
| `--api-key`                     | API 密钥                               | `pdf2zh_next --api-key sk-...`                  |
| `--base-url`                    | API 基础 URL                           | `pdf2zh_next --base-url https://api.openai.com` |
| `--proxy`                       | API 代理                               | `pdf2zh_next --proxy http://127.0.0.1:7890`     |
| `--output-dir`                  | 输出目录                               | `pdf2zh_next --output-dir ./output`             |
| `--doc-type`                    | 文档类型                               | `pdf2zh_next --doc-type paper`                  |
| `--doc-lang`                    | 文档语言                               | `pdf2zh_next --doc-lang en`                     |
| `--target-lang`                 | 目标语言                               | `pdf2zh_next --target-lang zh`                  |
| `--font`                        | 字体族                                 | `pdf2zh_next --font "Noto Sans SC"`             |
| `--font-size`                   | 字体大小                               | `pdf2zh_next --font-size 16`                    |
| `--line-spacing`                | 行间距                                 | `pdf2zh_next --line-spacing 1.5`                |
| `--page-margin`                 | 页面边距                               | `pdf2zh_next --page-margin 2cm`                 |
| `--title-font-size`             | 标题字体大小                           | `pdf2zh_next --title-font-size 20`              |
| `--heading1-font-size`          | 一级标题字体大小                       | `pdf2zh_next --heading1-font-size 18`           |
| `--heading2-font-size`          | 二级标题字体大小                       | `pdf2zh_next --heading2-font-size 16`           |
| `--heading3-font-size`          | 三级标题字体大小                       | `pdf2zh_next --heading3-font-size 14`           |
| `--paragraph-spacing`           | 段落间距                               | `pdf2zh_next --paragraph-spacing 12pt`          |
| `--image-dpi`                   | 图像 DPI                               | `pdf2zh_next --image-dpi 300`                   |
| `--image-quality`               | 图像质量                               | `pdf2zh_next --image-quality 95`                |
| `--max-concurrent`              | 最大并发请求数                         | `pdf2zh_next --max-concurrent 5`                |
| `--request-interval`            | 请求间隔（毫秒）                       | `pdf2zh_next --request-interval 1000`           |
| `--timeout`                     | 请求超时（秒）                         | `pdf2zh_next --timeout 60`                      |
| `--retry-attempts`              | 重试次数                               | `pdf2zh_next --retry-attempts 3`                |
| `--retry-delay`                 | 重试延迟（毫秒）                       | `pdf2zh_next --retry-delay 2000`                |
| `--cache-dir`                   | 缓存目录                               | `pdf2zh_next --cache-dir ./cache`               |
| `--cache-ttl`                   | 缓存 TTL（小时）                       | `pdf2zh_next --cache-ttl 24`                    |
| `--log-level`                   | 日志级别                               | `pdf2zh_next --log-level info`                  |
| `--log-file`                    | 日志文件路径                           | `pdf2zh_next --log-file ./logs/app.log`         |
| `--config`                      | 配置文件路径                           | `pdf2zh_next --config ./config.yaml`            |
| `--version`                     | 显示版本                               | `pdf2zh_next --version`                         |
| `--help`                        | 显示帮助                               | `pdf2zh_next --help`                            |

[⬆️ 返回顶部](#目录)

---

#### 速率限制配置指南

在使用翻译服务时，合理的速率限制配置对于避免 API 错误和优化性能至关重要。本指南将根据不同的上游服务限制，讲解如何配置 `--qps` 和 `--pool-max-worker` 参数。

> [!TIP]
>
> 建议 `pool_size` 不要超过 1000。如果通过以下方法计算出的 `pool_size` 超过 1000，请使用 1000。

##### RPM（每分钟请求数）速率限制

当上游服务有 RPM 限制时，使用以下计算方式：

**计算公式：**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> 系数 10 是一个经验值，在大多数场景下都能良好适用。

**示例：**
如果您的翻译服务限制为 600 RPM：
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### 并发连接限制

当上游服务存在并发连接限制（如 GLM 官方服务）时，可采用以下方法：

**计算公式：**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**示例：**
如果您的翻译服务允许 50 个并发连接：
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### 最佳实践

> [!TIP]
> - 始终从保守值开始，必要时逐步增加
> - 监控服务的响应时间和错误率
> - 不同服务可能需要不同的优化策略
> - 设置这些参数时，请考虑您的具体用例和文档大小


[⬆️ 返回顶部](#目录)

---

#### 部分翻译

使用 `--pages` 参数翻译文档的一部分。

- 如果页码是连续的，可以这样书写：

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` 包含第 25 页之后的所有页面。如果您的文档有 100 页，这相当于 `25-100`。
> 
> 类似地，`-25` 包含第 25 页之前的所有页面，相当于 `1-25`。

- 如果页面不连续，可以使用逗号 `,` 进行分隔。

例如，如果你想翻译第一页和第三页，可以使用以下命令：

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- 如果页面同时包含连续和非连续范围，也可以用逗号连接，例如：

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

该命令将翻译第一页、第三页、第 10 至 20 页以及从第 25 页开始的所有页面。


[⬆️ 返回顶部](#目录)

---

#### 指定源语言和目标语言

请参阅 [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages)、[DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ 返回顶部](#目录)

---

#### 翻译时排除例外

使用正则表达式指定需要保留的公式字体和字符：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

默认保留 `Latex`、`Mono`、`Code`、`Italic`、`Symbol` 和 `Math` 字体：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ 返回顶部](#目录)

---

#### 自定义提示

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

自定义翻译系统提示词。主要用于在提示词中添加 Qwen 3 的 `/no_think` 指令。

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ 返回顶部](#目录)

---

#### 自定义配置

有多种方式可以修改和导入配置文件。

> [!NOTE]
> **配置文件层级**
>
> 当通过不同方式修改同一参数时，软件将按照以下优先级顺序应用变更。
>
> 更高优先级的修改会覆盖较低优先级的配置。
>
> **命令行/图形界面 > 环境变量 > 用户配置文件 > 默认配置文件**

- 通过**命令行参数**修改配置

在大多数情况下，您可以直接通过命令行参数传递所需的设置。更多信息请参阅 [命令行参数](#命令行参数)。

例如，如果您想启用 GUI 窗口，可以使用以下命令：

```bash
pdf2zh_next --gui
```

- 通过 **环境变量** 修改配置

你可以将命令行参数中的 `--` 替换为 `PDF2ZH_`，使用 `=` 连接参数，并将 `-` 替换为 `_` 作为环境变量。

例如，如果你想启用 GUI 窗口，可以使用以下命令：

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- 用户指定的 **配置文件**

您可以使用以下命令行参数指定配置文件：

```bash
pdf2zh_next --config-file '/path/config.toml'
```

如果您不确定配置文件格式，请参考下方描述的默认配置文件。

- **默认配置文件**

默认配置文件位于 `~/.config/pdf2zh`。  
请勿修改 `default` 目录中的配置文件。  
强烈建议参考此配置文件的内容，并使用**自定义配置**来实现您自己的配置文件。

> [!TIP]
> - 默认情况下，pdf2zh 2.0 每次在 GUI 中点击翻译按钮时，会自动将当前配置保存到 `~/.config/pdf2zh/config.v3.toml`。该配置文件将在下次启动时默认加载。
> - `default` 目录中的配置文件由程序自动生成。您可以复制它们进行修改，但请勿直接修改。
> - 配置文件中可能包含 "v2"、"v3" 等版本号。这些是**配置文件版本号**，**并非** pdf2zh 本身的版本号。


[⬆️ 返回顶部](#目录)

---

#### 跳过清理

当此参数设为 True 时，将跳过 PDF 清理步骤，这可以提高兼容性并避免一些字体处理问题。

用法：

```bash
pdf2zh_next example.pdf --skip-clean
```

或者使用环境变量：

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> 当启用 `--enhance-compatibility` 时，跳过清理会自动启用。

---

#### 翻译缓存

PDFMathTranslate 会缓存已翻译的文本以提高速度，并避免对相同内容进行不必要的 API 调用。你可以使用 `--ignore-cache` 选项来忽略翻译缓存并强制重新翻译。

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ 返回顶部](#目录)

---

#### 部署为公共服务

在公共服务上部署 pdf2zh GUI 时，您应按照以下说明修改配置文件。

> [!WARNING]
>
> 本项目尚未经过专业安全审计，可能存在安全漏洞。请在公共网络部署前评估风险并采取必要的安全措施。


> [!TIP]
> - 公开部署时，应同时启用 `disable_gui_sensitive_input` 和 `disable_config_auto_save` 选项。
> - 使用*英文逗号* <kbd>,</kbd> 分隔不同的可用服务。

可用的配置如下：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ 返回顶部](#目录)

---

#### 认证与欢迎页面

当使用认证与欢迎页面来指定哪些用户可以使用 Web UI 并自定义登录页面时：

示例 auth.txt  
每行包含两个元素，用户名和密码，以逗号分隔。

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

示例 welcome.html

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
> 欢迎页面仅在认证文件不为空时生效。
> 如果认证文件为空，则不会进行认证。 :)

可用的配置如下：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ 返回顶部](#目录)

---

#### 术语表支持

PDFMathTranslate 支持术语表功能。术语表文件应为 `csv` 格式。  
文件包含三列数据，以下是示例术语表文件：

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自动 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


对于 CLI 用户：
你可以使用多个文件作为术语表。不同文件之间应以 `,` 分隔。

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

对于 WebUI 用户：

您现在可以上传自己的术语表文件了。上传文件后，可以通过点击文件名查看其内容，内容将显示在下方。

[⬆️ 返回顶部](#目录)

<div align="right"> 
<h6><small>本页面的部分内容由 GPT 翻译，可能包含错误。</small></h6>