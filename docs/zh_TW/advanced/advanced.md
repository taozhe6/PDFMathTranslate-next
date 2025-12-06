[**高級選項**](./introduction.md) > **高級選項** _(current)_

---

<h3 id="目錄">目錄</h3>

- [#### 命令行參數](#命令行參數)
- [#### 速率限制配置指南](#速率限制配置指南)
- [#### 部分翻譯](#部分翻譯)
- [#### 指定來源與目標語言](#指定來源與目標語言)
- [#### 使用例外進行翻譯](#使用例外進行翻譯)
- [#### 自訂提示詞](#自訂提示詞)
- [#### 自定義配置](#自定義配置)
- [#### 跳過清理](#跳過清理)
- [#### 翻譯快取](#翻譯快取)
- [#### 部署為公共服務](#部署為公共服務)
- [#### 驗證與歡迎頁面](#驗證與歡迎頁面)
- [#### 詞彙表支持](#詞彙表支持)

---

#### 命令行參數

在命令行中執行翻譯命令，在當前工作目錄中生成翻譯後的文檔 `example-mono.pdf` 和雙語文檔 `example-dual.pdf`。使用 Google 作為默認翻譯服務。更多支持的翻譯服務可以在 [這裡](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services) 找到。

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

在以下表格中，我們列出所有高級選項供參考：

##### 參數

| 選項                          | 功能                                                                               | 範例                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | 要處理的輸入 PDF 檔案                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `--output`                      | 輸出文件的目錄                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| `--<Services>`                  | 使用 [**特定服務**](./Documentation-of-Translation-Services.md) 進行翻譯 | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| `--help`, `-h`                  | 顯示幫助訊息並退出                                                              | `pdf2zh_next -h`                                                                                                      |
| `--config-file`                 | 配置檔案的路徑                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| `--report-interval`             | 進度報告間隔（秒）                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--debug`                       | 使用除錯日誌等級                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--gui`                         | 與 GUI 互動                                                                       | `pdf2zh_next --gui`                                                                                                   |
| `--warmup`                      | 僅下載並驗證所需資源後退出                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| `--generate-offline-assets`     | 在指定目錄中生成離線資源包                              | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| `--restore-offline-assets`      | 從指定目錄恢復離線資源包                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| `--version`                     | 顯示版本後退出                                                                  | `pdf2zh_next --version`                                                                                               |
| `--pages`                       | 部分文件翻譯                                                            | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
| `--lang-in`                     | 來源語言代碼                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| `--lang-out`                    | 目標語言代碼                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| `--min-text-length`             | 最小翻譯文字長度                                                        | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| `--rpc-doclayout`               | 用於文件版面分析的 RPC 服務主機地址                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| `--qps`                         | 翻譯服務的 QPS 限制                                                       | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| `--ignore-cache`                | 忽略翻譯快取                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--custom-system-prompt`        | 用於翻譯的自定義系統提示詞。適用於 Qwen 3 中的 `/no_think`                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--glossaries`                  | 詞彙表文件列表。                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| `--save-auto-extracted-glossary`| 儲存自動擷取的詞彙表                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| `--pool-max-workers`            | 翻譯池的最大工作線程數。如果未設置，將使用 qps 作為工作線程數 | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| `--term-qps`                    | 術語提取翻譯服務的 QPS 限制。如果未設置，將遵循 qps。         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| `--term-pool-max-workers`       | 術語提取翻譯池的最大工作線程數。如果未設置或為 0，將遵循 pool_max_workers。 | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| `--no-auto-extract-glossary`    | 禁用自動提取詞彙表                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--primary-font-family`         | 覆蓋翻譯文字的主要字型系列。選項：'serif' 表示襯線字型，'sans-serif' 表示無襯線字型，'script' 表示手寫/斜體字型。若未指定，則根據原始文字屬性使用自動字型選擇。 | `pdf2zh_next example.pdf --primary-font-family serif` |
| `--no-dual`                     | 不輸出雙語 PDF 文件                                                       | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--no-mono`                     | 不輸出單語種 PDF 文件                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| `--formular-font-pattern`       | 用於識別公式文字的字型模式                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| `--formular-char-pattern`       | 用於識別公式文本的字符模式                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| `--split-short-lines`           | 強制將短行拆分為不同段落                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| `--short-line-split-factor`     | 短行分割閾值因子                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| `--skip-clean`                  | 跳過 PDF 清理步驟                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| `--dual-translate-first`        | 在雙 PDF 模式下將翻譯後的頁面放在前面                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--disable-rich-text-translate` | 禁用富文本翻譯                                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| `--enhance-compatibility`       | 啟用所有相容性增強選項                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| `--use-alternating-pages-dual`  | 使用交替頁面模式處理雙語 PDF                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| `--watermark-output-mode`       | PDF 文件的浮水印輸出模式                                                     | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        |
| `--max-pages-per-part`          | 分割翻譯時每個部分的最大頁數                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| `--translate-table-text`        | 翻譯表格文字（實驗性功能）                                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| `--skip-scanned-detection`      | 跳過掃描檢測                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| `--ocr-workaround`              | 強制將翻譯後的文字設為黑色並添加白色背景                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| `--auto-enable-ocr-workaround`  | 啟用自動 OCR 解決方案。如果檢測到文件為重度掃描文件，將嘗試啟用 OCR 處理並跳過進一步的掃描檢測。詳情請參閱文檔。（預設值：False） | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| `--only-include-translated-page`| 僅在輸出 PDF 中包含已翻譯的頁面。僅在使用 --pages 時有效。  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| `--no-merge-alternating-line-numbers` | 停用合併帶有行號的文件中的交替行號與文字段落 | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| `--no-remove-non-formula-lines` | 禁用移除段落區域內的非公式行                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| `--non-formula-line-iou-threshold` | 設定識別非公式行的 IoU 閾值 (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       |
| `--figure-table-protection-threshold` | 設定圖形和表格的保護閾值 (0.0-1.0)。圖形/表格內的線條將不會被處理 | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        |
| `--skip-formula-offset-calculation` | 在處理過程中跳過公式偏移量計算          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### GUI 參數

| 選項                          | 功能                               | 範例                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | 啟用分享模式                    | `pdf2zh_next --gui --share`                     |
| `--auth-file`                   | 驗證檔案的路徑        | `pdf2zh_next --gui --auth-file /path`           |
| `--welcome-page`                | 歡迎頁面 HTML 檔案的路徑          | `pdf2zh_next --gui --welcome-page /path`        |
| `--enabled-services`            | 啟用的翻譯服務           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | 禁用 GUI 敏感輸入            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
| `--disable-config-auto-save`    | 禁用自動配置保存 | `pdf2zh_next --gui --disable-config-auto-save`  |
| `--server-port`                 | WebUI 端口                             | `pdf2zh_next --gui --server-port 7860`          |
| `--ui-lang`                     | UI 語言                            | `pdf2zh_next --gui --ui-lang zh`                |

[⬆️ 回到頂部](#toc)

---

#### 速率限制配置指南

在使用翻譯服務時，適當的速率限制配置對於避免 API 錯誤和優化效能至關重要。本指南解釋如何根據不同的上游服務限制來配置 `--qps` 和 `--pool-max-worker` 參數。

> [!TIP]
>
> 建議 `pool_size` 不要超過 1000。如果通過以下方法計算出的 `pool_size` 超過 1000，請使用 1000。

##### RPM（每分鐘請求數）速率限制

當上游服務有 RPM 限制時，請使用以下計算方式：

**計算公式：**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> 係數 10 是一個經驗係數，在大多數情況下通常效果良好。

**範例：**
如果您的翻譯服務限制為 600 RPM：
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
如果您的翻譯服務允許 50 個並發連接：
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### 最佳實踐

> [!TIP]
> - 始終從保守值開始，並在需要時逐漸增加
> - 監控您的服務響應時間和錯誤率
> - 不同的服務可能需要不同的優化策略
> - 在設定這些參數時，請考慮您的具體使用情境和文件大小


[⬆️ 回到頂部](#toc)

---

#### 部分翻譯

使用 `--pages` 參數來翻譯文件的一部分。

- 如果頁碼是連續的，你可以這樣寫：

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` 包含第 25 頁之後的所有頁面。如果您的文件有 100 頁，這相當於 `25-100`。
> 
> 同樣地，`-25` 包含第 25 頁之前的所有頁面，這相當於 `1-25`。

- 如果頁面不是連續的，你可以使用逗號 `,` 來分隔它們。

例如，如果您想要翻譯第一頁和第三頁，可以使用以下命令：

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- 如果頁面包含連續與非連續範圍，你也可以用逗號連接它們，像這樣：

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

此命令將翻譯第一頁、第三頁、第 10 到 20 頁，以及從第 25 頁開始的所有頁面。

[⬆️ 回到頂部](#目錄)

---

#### 指定來源與目標語言

請參閱 [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages)、[DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ 回到頂部](#toc)

---

#### 使用例外進行翻譯

使用正則表達式指定需要保留的公式字體和字元：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

預設保留 `Latex`、`Mono`、`Code`、`Italic`、`Symbol` 與 `Math` 字體：

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ 回到頂部](#toc)

---

#### 自訂提示詞

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/pull/637). -->

自訂翻譯系統提示詞。主要用於在提示詞中添加 Qwen 3 的 `/no_think` 指令。

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ 回到頂部](#toc)

---

#### 自定義配置

有多種方式可以修改和導入配置文件。

> [!NOTE]
> **配置檔案層級**
>
> 當使用不同方法修改同一參數時，軟體將按照以下優先順序套用變更。
>
> 較高優先順序的修改將覆蓋較低優先順序的修改。
>
> **cli/gui > env > 使用者配置檔案 > 預設配置檔案**

- 透過 **命令行參數** 修改配置

對於大多數情況，您可以直接通過命令行參數傳遞所需的設定。更多資訊請參閱 [命令行參數](#cmd)。

例如，如果您想要啟用 GUI 視窗，可以使用以下命令：

```bash
pdf2zh_next --gui
```

- 透過 **環境變數** 修改配置

您可以將命令行參數中的 `--` 替換為 `PDF2ZH_`，使用 `=` 連接參數，並將 `-` 替換為 `_` 作為環境變量。

例如，如果您想要啟用 GUI 視窗，可以使用以下命令：

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- 使用者指定的 **配置檔案**

您可以使用以下命令行參數指定配置檔案：

```bash
pdf2zh_next --config-file '/path/config.toml'
```

如果您不確定配置文件的格式，請參考下面描述的默認配置文件。

- **預設配置文件**

預設的設定檔位於 `~/.config/pdf2zh`。
請勿修改 `default` 目錄中的設定檔。
強烈建議參考此設定檔的內容，並使用**使用者指定設定檔**來實作您自己的設定檔。

> [!TIP]
> - 預設情況下，pdf2zh 2.0 每次在 GUI 中點擊翻譯按鈕時，會自動將當前配置保存到 `~/.config/pdf2zh/config.v3.toml`。此配置文件將在下次啟動時預設加載。
> - `default` 目錄中的配置文件由程序自動生成。您可以複製它們進行修改，但請不要直接修改它們。
> - 配置文件中可能包含 "v2"、"v3" 等版本號。這些是**配置文件的版本號**，**並非** pdf2zh 本身的版本號。


[⬆️ 回到頂部](#toc)

---

#### 跳過清理

當此參數設為 True 時，將跳過 PDF 清理步驟，這可以提高兼容性並避免一些字體處理問題。

用法：

```bash
pdf2zh_next example.pdf --skip-clean
```

或使用環境變數：

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> 當啟用 `--enhance-compatibility` 時，跳過清理會自動啟用。

---

#### 翻譯快取

PDFMathTranslate 會快取已翻譯的文字，以提高速度並避免對相同內容進行不必要的 API 呼叫。您可以使用 `--ignore-cache` 選項來忽略翻譯快取並強制重新翻譯。

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ 回到頂部](#toc)

---

#### 部署為公共服務

當在公共服務上部署 pdf2zh GUI 時，您應按照以下說明修改配置檔案。

> [!WARNING]
>
> 本項目未經過專業的安全審計，可能存在安全漏洞。請在部署到公共網絡前評估風險並採取必要的安全措施。


> [!TIP]
> - 公開部署時，應同時啟用 `disable_gui_sensitive_input` 和 `disable_config_auto_save`。
> - 使用*英文逗號* <kbd>,</kbd> 分隔不同的可用服務。

一個可用的配置如下：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ 回到頂部](#toc)

---

#### 驗證與歡迎頁面

當使用驗證與歡迎頁面來指定哪些用戶可以使用 Web UI 並自定義登錄頁面時：

範例 auth.txt
每行包含兩個元素，用戶名和密碼，以逗號分隔。

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

example welcome.html

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
> 僅當驗證檔案不為空白時，歡迎頁面才會生效。
> 如果驗證檔案為空白，則不會進行任何驗證。 :)

一個可用的配置如下：

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ 回到頂部](#toc)

---

#### 詞彙表支持

PDFMathTranslate 支持詞彙表。詞彙表文件應為 `csv` 文件。
文件包含三列。這是一個演示用的詞彙表文件：

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

您現在可以上傳自己的詞彙表檔案。上傳檔案後，您可以點擊檔案名稱來查看它們，內容會顯示在下方。

[⬆️ 回到頂部](#目錄)

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>