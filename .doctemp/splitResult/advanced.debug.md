<!-- CHUNK ID: chunk_DDD39913  CHUNK TYPE: paragraph START_LINE:1 -->
[**Advanced**](./introduction.md) > **Advanced** _(current)_

<!-- CHUNK ID: h_rule_8268bba0  CHUNK TYPE: h_rule START_LINE:3 -->
---

<!-- CHUNK ID: chunk_D9B293FF  CHUNK TYPE: paragraph START_LINE:5 -->
<h3 id="toc">Table of Contents</h3>

<!-- CHUNK ID: chunk_F0A2B12C  CHUNK TYPE: list START_LINE:7 -->
- [Command Line Args](#command-line-args)
- [Rate Limiting Configuration Guide](#rate-limiting-configuration-guide)
- [Partial translation](#partial-translation)
- [Specify source and target languages](#specify-source-and-target-languages)
- [Translate wih exceptions](#translate-wih-exceptions)
- [Custom prompt](#custom-prompt)
- [Custom configuration](#custom-configuration)
- [Skip clean](#skip-clean)
- [Translation cache](#translation-cache)
- [Deployment as a public services](#deployment-as-a-public-services)
- [Authentication and welcome page](#authentication-and-welcome-page)
- [Glossary Support](#glossary-support)

<!-- CHUNK ID: h_rule_4f9c9a70  CHUNK TYPE: h_rule START_LINE:20 -->
---

<!-- CHUNK ID: chunk_3BF1A9B5  CHUNK TYPE: header START_LINE:22 -->
#### Command Line Args

<!-- CHUNK ID: chunk_A2860DDF  CHUNK TYPE: paragraph START_LINE:24 -->
Execute the translation command in the command line to generate the translated document `example-mono.pdf` and the bilingual document `example-dual.pdf` in the current working directory. Use Google as the default translation service. More support translation services can find [HERE](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<!-- CHUNK ID: chunk_B6CD1E39  CHUNK TYPE: image START_LINE:26 -->
<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

<!-- CHUNK ID: chunk_B3EB591F  CHUNK TYPE: paragraph START_LINE:28 -->
In the following table, we list all advanced options for reference:

<!-- CHUNK ID: chunk_A2A42E6B  CHUNK TYPE: header START_LINE:30 -->
##### Args

<!-- CHUNK ID: chunk_BBEC0B84  CHUNK TYPE: longtable_head START_LINE:32 -->
| Option                          | Function                                                                               | Example                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Input PDF files to process                                                              | `pdf2zh_next example.pdf`                                                                                             |
<!-- CHUNK ID: chunk_DE6EE671  CHUNK TYPE: longtable_content START_LINE:35 -->
| `--output`                      | Output directory for files                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
<!-- CHUNK ID: chunk_2B98CF3B  CHUNK TYPE: longtable_content START_LINE:36 -->
| `--<Services>`                  | Use [**specific service**](./Documentation-of-Translation-Services.md) for translation | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
<!-- CHUNK ID: chunk_9D0BEC24  CHUNK TYPE: longtable_content START_LINE:37 -->
| `--help`, `-h`                  | Show help message and exit                                                              | `pdf2zh_next -h`                                                                                                      |
<!-- CHUNK ID: chunk_52F525D9  CHUNK TYPE: longtable_content START_LINE:38 -->
| `--config-file`                 | Path to the configuration file                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
<!-- CHUNK ID: chunk_A3B72E30  CHUNK TYPE: longtable_content START_LINE:39 -->
| `--report-interval`             | Progress report interval in seconds                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
<!-- CHUNK ID: chunk_681FB271  CHUNK TYPE: longtable_content START_LINE:40 -->
| `--debug`                       | Use debug logging level                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
<!-- CHUNK ID: chunk_0F2C1928  CHUNK TYPE: longtable_content START_LINE:41 -->
| `--gui`                         | Interact with GUI                                                                       | `pdf2zh_next --gui`                                                                                                   |
<!-- CHUNK ID: chunk_3165C2A9  CHUNK TYPE: longtable_content START_LINE:42 -->
| `--warmup`                      | Only download and verify required assets then exit                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
<!-- CHUNK ID: chunk_8D4A4094  CHUNK TYPE: longtable_content START_LINE:43 -->
| `--generate-offline-assets`     | Generate offline assets package in the specified directory                              | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
<!-- CHUNK ID: chunk_FDB3A2AC  CHUNK TYPE: longtable_content START_LINE:44 -->
| `--restore-offline-assets`      | Restore offline assets package from the specified directory                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
<!-- CHUNK ID: chunk_A9512419  CHUNK TYPE: longtable_content START_LINE:45 -->
| `--version`                     | Show version then exit                                                                  | `pdf2zh_next --version`                                                                                               |
<!-- CHUNK ID: chunk_F75A4DB9  CHUNK TYPE: longtable_content START_LINE:46 -->
| `--pages`                       | Partial document translation                                                            | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
<!-- CHUNK ID: chunk_694D0450  CHUNK TYPE: longtable_content START_LINE:47 -->
| `--lang-in`                     | Source language code                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                |
<!-- CHUNK ID: chunk_CEDB686F  CHUNK TYPE: longtable_content START_LINE:48 -->
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
<!-- CHUNK ID: chunk_E3F565CB  CHUNK TYPE: longtable_content START_LINE:49 -->
| `--min-text-length`             | Minimum text length to translate                                                        | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
<!-- CHUNK ID: chunk_6483EDCD  CHUNK TYPE: longtable_content START_LINE:50 -->
| `--rpc-doclayout`               | RPC service host address for document layout analysis                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
<!-- CHUNK ID: chunk_4331C67D  CHUNK TYPE: longtable_content START_LINE:51 -->
| `--qps`                         | QPS limit for translation service                                                       | `pdf2zh_next example.pdf --qps 200`                                                                                   |
<!-- CHUNK ID: chunk_4A87E333  CHUNK TYPE: longtable_content START_LINE:52 -->
| `--ignore-cache`                | Ignore translation cache                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
<!-- CHUNK ID: chunk_3DCF93F4  CHUNK TYPE: longtable_content START_LINE:53 -->
| `--custom-system-prompt`        | Custom system prompt for translation. Used for `/no_think` in Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
<!-- CHUNK ID: chunk_6BBAD367  CHUNK TYPE: longtable_content START_LINE:54 -->
| `--glossaries`                  | Glossary file list.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
<!-- CHUNK ID: chunk_80C69F3E  CHUNK TYPE: longtable_content START_LINE:55 -->
| `--save-auto-extracted-glossary`| save automatically extracted glossary                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
<!-- CHUNK ID: chunk_A884E4C7  CHUNK TYPE: longtable_content START_LINE:56 -->
| `--pool-max-workers`            | Maximum number of workers for translation pool. If not set, will use qps as the number of workers | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
<!-- CHUNK ID: chunk_9855EBF1  CHUNK TYPE: longtable_content START_LINE:57 -->
| `--term-qps`                    | QPS limit for term extraction translation service. If not set, will follow qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
<!-- CHUNK ID: chunk_C006E91B  CHUNK TYPE: longtable_content START_LINE:58 -->
| `--term-pool-max-workers`       | Maximum number of workers for term extraction translation pool. If not set or 0, will follow pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
<!-- CHUNK ID: chunk_57DBEFAD  CHUNK TYPE: longtable_content START_LINE:59 -->
| `--no-auto-extract-glossary`    | Disable auto extract glossary                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
<!-- CHUNK ID: chunk_AEAB36FD  CHUNK TYPE: longtable_content START_LINE:60 -->
| `--primary-font-family`         | Override primary font family for translated text. Choices: 'serif' for serif fonts, 'sans-serif' for sans-serif fonts, 'script' for script/italic fonts. If not specified, uses automatic font selection based on original text properties. | `pdf2zh_next example.pdf --primary-font-family serif` |
<!-- CHUNK ID: chunk_313C0250  CHUNK TYPE: longtable_content START_LINE:61 -->
| `--no-dual`                     | Do not output bilingual PDF files                                                       | `pdf2zh_next example.pdf --no-dual`                                                                                   |
<!-- CHUNK ID: chunk_F01ADA4A  CHUNK TYPE: longtable_content START_LINE:62 -->
| `--no-mono`                     | Do not output monolingual PDF files                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
<!-- CHUNK ID: chunk_CE4B67DB  CHUNK TYPE: longtable_content START_LINE:63 -->
| `--formular-font-pattern`       | Font pattern to identify formula text                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
<!-- CHUNK ID: chunk_751A0C21  CHUNK TYPE: longtable_content START_LINE:64 -->
| `--formular-char-pattern`       | Character pattern to identify formula text                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
<!-- CHUNK ID: chunk_AB421930  CHUNK TYPE: longtable_content START_LINE:65 -->
| `--split-short-lines`           | Force split short lines into different paragraphs                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
<!-- CHUNK ID: chunk_89EE9309  CHUNK TYPE: longtable_content START_LINE:66 -->
| `--short-line-split-factor`     | Split threshold factor for short lines                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
<!-- CHUNK ID: chunk_EE138D1A  CHUNK TYPE: longtable_content START_LINE:67 -->
| `--skip-clean`                  | Skip PDF cleaning step                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
<!-- CHUNK ID: chunk_63121590  CHUNK TYPE: longtable_content START_LINE:68 -->
| `--dual-translate-first`        | Put translated pages first in dual PDF mode                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
<!-- CHUNK ID: chunk_30F3E646  CHUNK TYPE: longtable_content START_LINE:69 -->
| `--disable-rich-text-translate` | Disable rich text translation                                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
<!-- CHUNK ID: chunk_A3203F6A  CHUNK TYPE: longtable_content START_LINE:70 -->
| `--enhance-compatibility`       | Enable all compatibility enhancement options                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
<!-- CHUNK ID: chunk_DF7A3C7D  CHUNK TYPE: longtable_content START_LINE:71 -->
| `--use-alternating-pages-dual`  | Use alternating pages mode for dual PDF                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
<!-- CHUNK ID: chunk_B35D3C0C  CHUNK TYPE: longtable_content START_LINE:72 -->
| `--watermark-output-mode`       | Watermark output mode for PDF files                                                     | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        |
<!-- CHUNK ID: chunk_53A9759F  CHUNK TYPE: longtable_content START_LINE:73 -->
| `--max-pages-per-part`          | Maximum pages per part for split translation                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
<!-- CHUNK ID: chunk_0CA60CFA  CHUNK TYPE: longtable_content START_LINE:74 -->
| `--translate-table-text`        | Translate table text (experimental)                                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
<!-- CHUNK ID: chunk_1336591D  CHUNK TYPE: longtable_content START_LINE:75 -->
| `--skip-scanned-detection`      | Skip scanned detection                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
<!-- CHUNK ID: chunk_EBAC01C5  CHUNK TYPE: longtable_content START_LINE:76 -->
| `--ocr-workaround`              | Force translated text to be black and add white background                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
<!-- CHUNK ID: chunk_04D70854  CHUNK TYPE: longtable_content START_LINE:77 -->
| `--auto-enable-ocr-workaround`  | Enable automatic OCR workaround. If a document is detected as heavily scanned, this will attempt to enable OCR processing and skip further scan detection. See documentation for details. (default: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
<!-- CHUNK ID: chunk_DB9F7803  CHUNK TYPE: longtable_content START_LINE:78 -->
| `--only-include-translated-page`| Only include translated pages in the output PDF. Effective only when --pages is used.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
<!-- CHUNK ID: chunk_F59B12F3  CHUNK TYPE: longtable_content START_LINE:79 -->
| `--no-merge-alternating-line-numbers` | Disable merging of alternating line numbers and text paragraphs in documents with line numbers | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
<!-- CHUNK ID: chunk_144034ED  CHUNK TYPE: longtable_content START_LINE:80 -->
| `--no-remove-non-formula-lines` | Disable removal of non-formula lines within paragraph areas                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
<!-- CHUNK ID: chunk_F487963F  CHUNK TYPE: longtable_content START_LINE:81 -->
| `--non-formula-line-iou-threshold` | Set IoU threshold for identifying non-formula lines (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       |
<!-- CHUNK ID: chunk_F56B7BA4  CHUNK TYPE: longtable_content START_LINE:82 -->
| `--figure-table-protection-threshold` | Set protection threshold for figures and tables (0.0-1.0). Lines within figures/tables will not be processed | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        |
<!-- CHUNK ID: chunk_8D0C4079  CHUNK TYPE: longtable_content START_LINE:83 -->
| `--skip-formula-offset-calculation` | Skip formula offset calculation during processing          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


<!-- CHUNK ID: chunk_140EFE95  CHUNK TYPE: header START_LINE:86 -->
##### GUI Args

<!-- CHUNK ID: chunk_3E7D5666  CHUNK TYPE: longtable_head START_LINE:88 -->
| Option                          | Function                               | Example                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Enable sharing mode                    | `pdf2zh_next --gui --share`                     |
<!-- CHUNK ID: chunk_69EC4DA6  CHUNK TYPE: longtable_content START_LINE:91 -->
| `--auth-file`                   | Path to the authentication file        | `pdf2zh_next --gui --auth-file /path`           |
<!-- CHUNK ID: chunk_7C537E64  CHUNK TYPE: longtable_content START_LINE:92 -->
| `--welcome-page`                | Path to the welcome html file          | `pdf2zh_next --gui --welcome-page /path`        |
<!-- CHUNK ID: chunk_FEFD024F  CHUNK TYPE: longtable_content START_LINE:93 -->
| `--enabled-services`            | Enabled translation services           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` |
<!-- CHUNK ID: chunk_82368AEC  CHUNK TYPE: longtable_content START_LINE:94 -->
| `--disable-gui-sensitive-input` | Disable GUI sensitive input            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
<!-- CHUNK ID: chunk_EDCAC052  CHUNK TYPE: longtable_content START_LINE:95 -->
| `--disable-config-auto-save`    | Disable automatic configuration saving | `pdf2zh_next --gui --disable-config-auto-save`  |
<!-- CHUNK ID: chunk_D406105F  CHUNK TYPE: longtable_content START_LINE:96 -->
| `--server-port`                 | WebUI Port                             | `pdf2zh_next --gui --server-port 7860`          |
<!-- CHUNK ID: chunk_854DF91F  CHUNK TYPE: longtable_content START_LINE:97 -->
| `--ui-lang`                     | UI language                            | `pdf2zh_next --gui --ui-lang zh`                |

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:99 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_60043796  CHUNK TYPE: h_rule START_LINE:101 -->
---

<!-- CHUNK ID: chunk_E0DC0651  CHUNK TYPE: header START_LINE:103 -->
#### Rate Limiting Configuration Guide

<!-- CHUNK ID: chunk_23D405EC  CHUNK TYPE: paragraph START_LINE:105 -->
When using translation services, proper rate limiting configuration is crucial to avoid API errors and optimize performance. This guide explains how to configure `--qps` and `--pool-max-worker` parameters based on different upstream service limitations.

<!-- CHUNK ID: chunk_742CD289  CHUNK TYPE: blockquote START_LINE:107 -->
> [!TIP]
>
> It is recommended that the pool_size does not exceed 1000. If the pool_size calculated by the following method exceeds 1000, please use 1000.

<!-- CHUNK ID: chunk_F9E5B2E2  CHUNK TYPE: header START_LINE:111 -->
##### RPM (Requests Per Minute) Rate Limiting

<!-- CHUNK ID: chunk_CDE1A5D3  CHUNK TYPE: paragraph START_LINE:113 -->
When the upstream service has RPM limitations, use the following calculation:

**Calculation Formula:**
<!-- CHUNK ID: chunk_D293CCA3  CHUNK TYPE: list START_LINE:116 -->
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

<!-- CHUNK ID: chunk_1C383BEE  CHUNK TYPE: blockquote START_LINE:119 -->
> [!NOTE]
> The factor of 10 is an empirical coefficient that generally works well for most scenarios.

<!-- CHUNK ID: chunk_AB49073F  CHUNK TYPE: paragraph START_LINE:122 -->
**Example:**
If your translation service has a limit of 600 RPM:
<!-- CHUNK ID: chunk_131B05E6  CHUNK TYPE: list START_LINE:124 -->
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

<!-- CHUNK ID: chunk_D4EF62BC  CHUNK TYPE: code_block START_LINE:127 -->
```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

<!-- CHUNK ID: chunk_C7673CDB  CHUNK TYPE: header START_LINE:131 -->
##### Concurrent Connection Limiting

<!-- CHUNK ID: chunk_62AE5A6C  CHUNK TYPE: paragraph START_LINE:133 -->
When the upstream service has concurrent connection limitations (like GLM official service), use this approach:

**Calculation Formula:**
<!-- CHUNK ID: chunk_B095EF50  CHUNK TYPE: list START_LINE:136 -->
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

<!-- CHUNK ID: chunk_1616A330  CHUNK TYPE: paragraph START_LINE:139 -->
**Example:**
If your translation service allows 50 concurrent connections:
<!-- CHUNK ID: chunk_1D19FB94  CHUNK TYPE: list START_LINE:141 -->
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

<!-- CHUNK ID: chunk_DB872698  CHUNK TYPE: code_block START_LINE:144 -->
```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

<!-- CHUNK ID: chunk_4C0D79DD  CHUNK TYPE: header START_LINE:148 -->
##### Best Practices

<!-- CHUNK ID: chunk_60A6D664  CHUNK TYPE: blockquote START_LINE:150 -->
> [!TIP]
> - Always start with conservative values and gradually increase if needed
> - Monitor your service's response times and error rates
> - Different services may require different optimization strategies
> - Consider your specific use case and document size when setting these parameters


<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:157 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_53cb14ca  CHUNK TYPE: h_rule START_LINE:159 -->
---

<!-- CHUNK ID: chunk_ADC018D0  CHUNK TYPE: header START_LINE:161 -->
#### Partial translation

<!-- CHUNK ID: chunk_A7D2451C  CHUNK TYPE: paragraph START_LINE:163 -->
Use the `--pages` parameter to translate a portion of a document.

<!-- CHUNK ID: chunk_C04AFE09  CHUNK TYPE: list START_LINE:165 -->
- If the page numbers are consecutive, you can write it like this:

<!-- CHUNK ID: chunk_037196E3  CHUNK TYPE: code_block START_LINE:167 -->
```bash
pdf2zh_next example.pdf --pages 1-3
```

<!-- CHUNK ID: chunk_02CC256B  CHUNK TYPE: code_block START_LINE:171 -->
```bash
pdf2zh_next example.pdf --pages 25-
```

<!-- CHUNK ID: chunk_773EEC89  CHUNK TYPE: blockquote START_LINE:175 -->
> [!TIP]
> `25-` includes all pages after page 25. If your document has 100 pages, this is equivalent to `25-100`.
> 
> Similarly, `-25` includes all pages before page 25, which is equivalent to `1-25`.

<!-- CHUNK ID: chunk_1A89F075  CHUNK TYPE: list START_LINE:180 -->
- If the pages are not consecutive, you can use a comma `,` to separate them.

<!-- CHUNK ID: chunk_046E7E79  CHUNK TYPE: paragraph START_LINE:182 -->
For example, if you want to translate the first and third pages, you can use the following command:

<!-- CHUNK ID: chunk_7FBB71F3  CHUNK TYPE: code_block START_LINE:184 -->
```bash
pdf2zh_next example.pdf --pages "1,3"
```

<!-- CHUNK ID: chunk_376C9855  CHUNK TYPE: list START_LINE:188 -->
- If the pages include both consecutive and non-consecutive ranges, you can also connect them with a comma, like this:

<!-- CHUNK ID: chunk_DE0F06A2  CHUNK TYPE: code_block START_LINE:190 -->
```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

<!-- CHUNK ID: chunk_16D6BA70  CHUNK TYPE: paragraph START_LINE:194 -->
This command will translate the first page, the third page, pages 10-20, and all pages from 25 to the end.


[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_c55a47b4  CHUNK TYPE: h_rule START_LINE:199 -->
---

<!-- CHUNK ID: chunk_482C5F18  CHUNK TYPE: header START_LINE:201 -->
#### Specify source and target languages

<!-- CHUNK ID: chunk_3E16227B  CHUNK TYPE: paragraph START_LINE:203 -->
See [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

<!-- CHUNK ID: chunk_CE426311  CHUNK TYPE: code_block START_LINE:205 -->
```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:209 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_4469a613  CHUNK TYPE: h_rule START_LINE:211 -->
---

<!-- CHUNK ID: chunk_EA41DE52  CHUNK TYPE: header START_LINE:213 -->
#### Translate wih exceptions

<!-- CHUNK ID: chunk_6BAF2E56  CHUNK TYPE: paragraph START_LINE:215 -->
Use regex to specify formula fonts and characters that need to be preserved:

<!-- CHUNK ID: chunk_8D6F2147  CHUNK TYPE: code_block START_LINE:217 -->
```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

<!-- CHUNK ID: chunk_8FEF09F4  CHUNK TYPE: paragraph START_LINE:221 -->
Preserve `Latex`, `Mono`, `Code`, `Italic`, `Symbol` and `Math` fonts by default:

<!-- CHUNK ID: chunk_ACAC9383  CHUNK TYPE: code_block START_LINE:223 -->
```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:227 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_48128847  CHUNK TYPE: h_rule START_LINE:229 -->
---

<!-- CHUNK ID: chunk_37A13558  CHUNK TYPE: header START_LINE:231 -->
#### Custom prompt

<!-- CHUNK ID: chunk_54E57534  CHUNK TYPE: html_comment START_LINE:233 -->
<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/pull/637). -->

<!-- CHUNK ID: chunk_5F141742  CHUNK TYPE: paragraph START_LINE:235 -->
Custom system prompt for translation. It is mainly used to add the '/no_think' instruction of Qwen 3 in the prompt.

<!-- CHUNK ID: chunk_4E347A0E  CHUNK TYPE: code_block START_LINE:237 -->
```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:241 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_fb0c24b1  CHUNK TYPE: h_rule START_LINE:243 -->
---

<!-- CHUNK ID: chunk_1EC5A9B5  CHUNK TYPE: header START_LINE:245 -->
#### Custom configuration

<!-- CHUNK ID: chunk_754794E1  CHUNK TYPE: paragraph START_LINE:247 -->
There are multiple ways to modify and import the configuration file.

<!-- CHUNK ID: chunk_B9BF8271  CHUNK TYPE: blockquote START_LINE:249 -->
> [!NOTE]
> **Configuration File Hierarchy**
>
> When modifying the same parameter using different methods, the software will apply changes according to the priority order below. 
>
> Higher-ranked modifications will override lower-ranked ones.
>
> **cli/gui > env > user config file > default config file**

<!-- CHUNK ID: chunk_06B261DE  CHUNK TYPE: list START_LINE:258 -->
- Modifying Configuration via **Command Line Arguments**

<!-- CHUNK ID: chunk_4579F74D  CHUNK TYPE: paragraph START_LINE:260 -->
For most cases, you can directly pass your desired settings through command line arguments. Please refer to [Command Line Args](#cmd) for more information.

For example, if you want to enable a GUI window, you can use the following command:

<!-- CHUNK ID: chunk_9668B90D  CHUNK TYPE: code_block START_LINE:264 -->
```bash
pdf2zh_next --gui
```

<!-- CHUNK ID: chunk_85CC4581  CHUNK TYPE: list START_LINE:268 -->
- Modifying Configuration via **Environment Variables**

<!-- CHUNK ID: chunk_A3573A4C  CHUNK TYPE: paragraph START_LINE:270 -->
You can replace the `--` in command line arguments with `PDF2ZH_`, connect parameters using `=`, and replace `-` with `_` as environment variables.

For example, if you want to enable a GUI window, you can use the following command:

<!-- CHUNK ID: chunk_5A8D89BB  CHUNK TYPE: code_block START_LINE:274 -->
```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<!-- CHUNK ID: chunk_9DD1EEE0  CHUNK TYPE: image START_LINE:278 -->
<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

<!-- CHUNK ID: chunk_11A0D60E  CHUNK TYPE: list START_LINE:280 -->
- User-Specified **Configuration File**

<!-- CHUNK ID: chunk_9EE9DFB5  CHUNK TYPE: paragraph START_LINE:282 -->
You can specify a configuration file using the command line argument below:

<!-- CHUNK ID: chunk_3B8259C7  CHUNK TYPE: code_block START_LINE:284 -->
```bash
pdf2zh_next --config-file '/path/config.toml'
```

<!-- CHUNK ID: chunk_FC4FBE9E  CHUNK TYPE: paragraph START_LINE:288 -->
If you are unsure about the config file format, please refer to the default configuration file described below.

<!-- CHUNK ID: chunk_A4C0C077  CHUNK TYPE: list START_LINE:290 -->
- **Default Configuration File**

<!-- CHUNK ID: chunk_B17D9FE3  CHUNK TYPE: paragraph START_LINE:292 -->
The default configuration file is located at `~/.config/pdf2zh`. 
Please do not modify the configuration files in the `default` directory. 
It is strongly recommended to refer to this configuration file's content and use **User-Specified Configuration File** to implement your own configuration file.

<!-- CHUNK ID: chunk_15DFB8EE  CHUNK TYPE: blockquote START_LINE:296 -->
> [!TIP]
> - By default, pdf2zh 2.0 automatically saves the current configuration to `~/.config/pdf2zh/config.v3.toml` each time you click the translate button in the GUI. This configuration file will be loaded by default on the next startup.
> - The configuration files in the `default` directory are automatically generated by the program. You can copy them for modification, but please do not modify them directly.
> - Configuration files may include version numbers such as "v2", "v3", etc. These are **configuration file version numbers**, **not** the version number of pdf2zh itself.


<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:302 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_18b4b4d3  CHUNK TYPE: h_rule START_LINE:304 -->
---

<!-- CHUNK ID: chunk_870EBD0C  CHUNK TYPE: header START_LINE:306 -->
#### Skip clean

<!-- CHUNK ID: chunk_012D63A3  CHUNK TYPE: paragraph START_LINE:308 -->
When this parameter is set to True, the PDF cleaning step will be skipped, which can improve compatibility and avoid some font processing issues.

Usage:

<!-- CHUNK ID: chunk_56748FCD  CHUNK TYPE: code_block START_LINE:312 -->
```bash
pdf2zh_next example.pdf --skip-clean
```

<!-- CHUNK ID: chunk_1078AA87  CHUNK TYPE: paragraph START_LINE:316 -->
Or using environment variables:

<!-- CHUNK ID: chunk_C147F788  CHUNK TYPE: code_block START_LINE:318 -->
```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

<!-- CHUNK ID: chunk_E510ADDB  CHUNK TYPE: blockquote START_LINE:322 -->
> [!TIP]
> When `--enhance-compatibility` is enabled, Skip clean is automatically enabled.

<!-- CHUNK ID: h_rule_068fd2f7  CHUNK TYPE: h_rule START_LINE:325 -->
---

<!-- CHUNK ID: chunk_A35603CF  CHUNK TYPE: header START_LINE:327 -->
#### Translation cache

<!-- CHUNK ID: chunk_F8D49E02  CHUNK TYPE: paragraph START_LINE:329 -->
PDFMathTranslate caches translated texts to increase speed and avoid unnecessary API calls for same contents. You can use `--ignore-cache` option to ignore translation cache and force retranslation.

<!-- CHUNK ID: chunk_D7B6C013  CHUNK TYPE: code_block START_LINE:331 -->
```bash
pdf2zh_next example.pdf --ignore-cache
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:335 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_85c7ddf7  CHUNK TYPE: h_rule START_LINE:337 -->
---

<!-- CHUNK ID: chunk_05080CDF  CHUNK TYPE: header START_LINE:339 -->
#### Deployment as a public services

<!-- CHUNK ID: chunk_A72BDF82  CHUNK TYPE: paragraph START_LINE:341 -->
When deploying a pdf2zh GUI on public services, you should modify the configuration file as described below.

<!-- CHUNK ID: chunk_41166DB8  CHUNK TYPE: blockquote START_LINE:343 -->
> [!WARNING]
>
> This project has not been professionally audited for security, and may contain security vulnerabilities. Please evaluate the risks and take necessary security measures before deploying on public networks.


> [!TIP]
> - When deploying publicly, both disable_gui_sensitive_input and disable_config_auto_save should be enabled.
> - Separate different available services with *English commas* <kbd>,</kbd> .

<!-- CHUNK ID: chunk_F2D0AEC1  CHUNK TYPE: paragraph START_LINE:352 -->
A usable configuration is as follows:

<!-- CHUNK ID: chunk_12A9803B  CHUNK TYPE: code_block START_LINE:354 -->
```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:364 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_dd52a23a  CHUNK TYPE: h_rule START_LINE:366 -->
---

<!-- CHUNK ID: chunk_E255AB78  CHUNK TYPE: header START_LINE:368 -->
#### Authentication and welcome page

<!-- CHUNK ID: chunk_1A5EEA9C  CHUNK TYPE: paragraph START_LINE:370 -->
When using Authentication and welcome page to specify which user to use Web UI and custom the login page:

example auth.txt
Each line contains two elements, username, and password, separated by a comma.

<!-- CHUNK ID: chunk_B865D3B8  CHUNK TYPE: code_block START_LINE:375 -->
```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

<!-- CHUNK ID: chunk_0CEA118C  CHUNK TYPE: paragraph START_LINE:383 -->
example welcome.html

<!-- CHUNK ID: chunk_0FC66A15  CHUNK TYPE: code_block START_LINE:385 -->
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

<!-- CHUNK ID: chunk_40E12FA3  CHUNK TYPE: blockquote START_LINE:398 -->
> [!NOTE]
> welcome page will work if only authentication file is not blank.
> If authentication file is blank, there will be no authentication. :)

<!-- CHUNK ID: chunk_F2D0AEC1  CHUNK TYPE: paragraph START_LINE:402 -->
A usable configuration is as follows:

<!-- CHUNK ID: chunk_39D7C203  CHUNK TYPE: code_block START_LINE:404 -->
```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

<!-- CHUNK ID: chunk_F1B6ECA2  CHUNK TYPE: paragraph START_LINE:413 -->
[⬆️ Back to top](#toc)

<!-- CHUNK ID: h_rule_4616fb87  CHUNK TYPE: h_rule START_LINE:415 -->
---

<!-- CHUNK ID: chunk_4A9C44BF  CHUNK TYPE: header START_LINE:417 -->
#### Glossary Support

<!-- CHUNK ID: chunk_65580DD5  CHUNK TYPE: paragraph START_LINE:419 -->
PDFMathTranslate supports the glossary table. The glossary tables file should be `csv` file.
There are three columns in file. Here is a demo glossary file:

<!-- CHUNK ID: chunk_2403CA4A  CHUNK TYPE: table START_LINE:422 -->
| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 自动 ML  | zh-CN   |
| a,a    | a       | zh-CN   |
| "      | "       | zh-CN   |


<!-- CHUNK ID: chunk_598725B0  CHUNK TYPE: paragraph START_LINE:429 -->
For CLI user:
You can use multiple files for glossary. And different files should be split by `,`.

<!-- CHUNK ID: chunk_332A0BF8  CHUNK TYPE: code_block START_LINE:432 -->
```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

<!-- CHUNK ID: chunk_B3174CBC  CHUNK TYPE: paragraph START_LINE:436 -->
For WebUI user:

You can upload your own glossary file now. After you uploaded the file, you can check them by click their name and the content shows below.

[⬆️ Back to top](#toc)
