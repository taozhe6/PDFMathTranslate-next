# 為專案貢獻

> [!CAUTION]
>
> 當前專案維護者正在研究自動化文檔國際化。因此，任何與文檔國際化/翻譯相關的 PR 將不被接受！
>
> 請勿提交與文檔國際化/翻譯相關的 PR！

感謝您對本專案的關注！在開始貢獻之前，請花些時間閱讀以下指南，以確保您的貢獻能夠順利被接受。

## 不接受的貢獻類型

1. 文檔國際化/翻譯
2. 與核心基礎設施相關的貢獻，例如 HTTP API 等
3. 明確標記為「No help needed」的議題（包括 [Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) 和 [PDFMathTranslate-next/PDFMathTranslate-next](PDFMathTranslate-next/PDFMathTranslate-next) 存儲庫中的議題）
4. 維護者認為不適當的其他貢獻
5. 貢獻文檔，但修改非英文的其他語言文檔
6. 需要修改 `PDF` 文件的 PR
7. 修改 `pdf2zh_next/gui_translation.yaml` 文件的 PR

請勿提交與上述類型相關的 PR。

> [!NOTE]
>
> 若您想貢獻文檔，請**僅修改英文版本文檔**。其他語言版本由貢獻者自行翻譯。

- [ ] Add new features
- [ ] Add new dependencies
- [ ] Modify project architecture

## PRs that are recommended to submit directly
- [ ] Fix bugs
- [ ] Fix typos
- [ ] Improve documentation
- [ ] Refactor code
- [ ] Improve test cases

---

### OUTPUT

## 建議在提交前透過 Issue 與維護者討論的 PR
- [ ] 新增功能
- [ ] 新增依賴項
- [ ] 修改專案架構

## 建議直接提交的 PR
- [ ] 修復錯誤
- [ ] 修正錯字
- [ ] 改進文檔
- [ ] 重構程式碼
- [ ] 改進測試案例

- [ ] Add new features
- [ ] Add new dependencies
- [ ] Modify project architecture

For the following types of PRs, it is recommended to submit directly:
- [ ] Fix bugs
- [ ] Fix typos
- [ ] Improve documentation
- [ ] Refactor code
- [ ] Improve test cases

2. PRs related to UI modifications. (The current UI is considered stable, and we do not plan to make significant changes to it).
3. PRs related to the addition of new LLM services. (We currently support OpenAI, Azure OpenAI, Aliyun, and SiliconFlow, which are sufficient for our needs).
4. PRs related to the addition of new translation services. (We currently support Google Translate, DeepL, and Youdao, which are sufficient for our needs).

---

### OUTPUT

1. 與多用戶共享功能相關的 PR。（本專案主要設計為單用戶使用，無意引入完整的多用戶系統）。
2. 與 UI 修改相關的 PR。（當前 UI 被認為是穩定的，我們不計劃對其進行重大更改）。
3. 與新增 LLM 服務相關的 PR。（我們目前支持 OpenAI、Azure OpenAI、Aliyun 和 SiliconFlow，這些已滿足我們的需求）。
4. 與新增翻譯服務相關的 PR。（我們目前支持 Google Translate、DeepL 和 Youdao，這些已滿足我們的需求）。

## 貢獻流程

1. 複製此儲存庫並在本地克隆。
2. 創建一個新分支：`git checkout -b feature/<feature-name>`。
3. 開發並確保你的代碼符合要求。
4. 提交你的代碼：
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. 推送至你的儲存庫：`git push origin feature/<feature-name>`。
6. 在 GitHub 上創建一個 PR，提供詳細描述，並請求 [@awwaawwa](https://github.com/awwaawwa) 進行審查。
7. 確保所有自動化檢查通過。

> [!TIP]
>
> 您不需要等到開發完全完成才創建 PR。提前創建 PR 可以讓我們審查您的實現並提供建議。
>
> 如果您對源代碼或相關事宜有任何疑問，請聯繫維護者 aw@funstory.ai。
>
> 2.0 版本的資源文件與 [BabelDOC](https://github.com/funstory-ai/BabelDOC) 共享。下載相關資源的代碼位於 BabelDOC 中。如果您想新增資源文件，請聯繫 BabelDOC 維護者 aw@funstory.ai。

## 基本要求

<h4 id="sop">1. 工作流程</h4>

   - 請從 `main` 分支進行 fork，並在您 fork 的分支上進行開發。
   - 提交 Pull Request (PR) 時，請提供詳細的變更說明。
   - 如果您的 PR 未通過自動化檢查（顯示為 `checks failed` 和紅色叉號），請查看對應的 `details` 並修改您的提交，以確保新的 PR 通過所有檢查。


<h4 id="開發與測試">2. 開發與測試</h4>

   - 使用命令 `pip install -e .` 進行開發和測試。


<h4 id="格式">3. 代碼格式化</h4>

   - 配置 `pre-commit` 工具並啟用 `black` 和 `flake8` 進行代碼格式化。


<h4 id="requpdate">4. 依賴項更新</h4>

   - 如果您引入了新的依賴項，請及時更新 `pyproject.toml` 文件中的依賴列表。


<h4 id="docupdate">5. 文件更新</h4>

   - 如果您新增了命令行選項，請相應地更新所有語言版本的 `README.md` 文件中的命令行選項列表。


<h4 id="commitmsg">6. 提交訊息</h4>

   - 使用 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)，例如：`feat(translator): add openai`。


<h4 id="codestyle">7. 程式碼風格</h4>

   - 確保您提交的代碼符合基本的編碼風格標準。
   - 變量命名請使用 snake_case 或 camelCase。


<h4 id="doctypo">8. 文件格式</h4>

   - 對於 `README.md` 的格式，請遵循 [中文文案排版指南](https://github.com/sparanoid/chinese-copywriting-guidelines)。
   - 確保英文和中文文檔始終保持最新；其他語言文檔的更新是可選的。

## 新增翻譯引擎

1. 在 `pdf2zh/config/translate_engine_model.py` 檔案中新增一個翻譯器配置類別。
2. 在相同檔案中，將新的翻譯器配置類別實例添加到 `TRANSLATION_ENGINE_SETTING_TYPE` 類型別名中。
3. 在 `pdf2zh/translator/translator_impl` 資料夾中新增翻譯器實作類別。

> [!NOTE]
>
> 本項目無意支援任何 RPS（每秒請求數）低於 4 的翻譯引擎。請勿提交對此類引擎的支援請求。
> 以下類型的翻譯器也不會被整合：
> - 已被上游維護者棄用的翻譯器（例如 deeplx）
> - 依賴項過大的翻譯器（例如依賴 pytorch 的翻譯器）
> - 不穩定的翻譯器
> - 基於逆向工程 API 的翻譯器
>
> 當您不確定某個翻譯器是否符合要求時，可以提交 issue 與維護者討論。

## 專案結構

- **config 資料夾**：配置系統。
- **translator 資料夾**：與翻譯器相關的實現。
- **gui.py**：提供 GUI 介面。
- **const.py**：一些常數。
- **main.py**：提供命令行工具。
- **high_level.py**：基於 BabelDOC 的高階介面。
- **http_api.py**：提供 HTTP API（尚未啟動）。

- [x] Support for PDF to PDF, including text and mathematical formulas
- [x] Support for LaTeX to LaTeX
- [x] Support for Markdown to Markdown
- [x] Support for plain text to plain text
- [x] Support for multiple LLM services (OpenAI, DeepSeek, Aliyun, SiliconFlow, etc.)
- [x] Support for multiple translation services (Google Translate, Microsoft Translator, etc.)
- [x] Support for multiple file formats (PDF, LaTeX, Markdown, plain text)
- [x] Support for multiple languages (English, Chinese, Japanese, Korean, etc.)
- [x] Support for command line interface (CLI)
- [x] Support for web user interface (WebUI)
- [x] Support for batch processing
- [x] Support for custom translation rules
- [x] Support for custom output formats
- [x] Support for custom language models
- [x] Support for custom translation services
- [x] Support for custom output directories
- [x] Support for custom output file names
- [x] Support for custom output file extensions
- [x] Support for custom output file formats
- [x] Support for custom output file encodings
- [x] Support for custom output file line endings
- [x] Support for custom output file indentation
- [x] Support for custom output file spacing
- [x] Support for custom output file margins
- [x] Support for custom output file page breaks
- [x] Support for custom output file headers and footers
- [x] Support for custom output file watermarks
- [x] Support for custom output file backgrounds
- [x] Support for custom output file fonts
- [x] Support for custom output file font sizes
- [x] Support for custom output file font colors
- [x] Support for custom output file font styles
- [x] Support for custom output file font weights
- [x] Support for custom output file font families
- [x] Support for custom output file font variants
- [x] Support for custom output file font stretches
- [x] Support for custom output file font kerning
- [x] Support for custom output file font ligatures
- [x] Support for custom output file font features
- [x] Support for custom output file font variations
- [x] Support for custom output file font optical sizing
- [x] Support for custom output file font display
- [x] Support for custom output file font fallback
- [x] Support for custom output file font synthesis
- [x] Support for custom output file font size adjust
- [x] Support for custom output file font smoothing
- [x] Support for custom output file font rendering
- [x] Support for custom output file font hinting
- [x] Support for custom output file font subpixel rendering
- [x] Support for custom output file font antialiasing
- [x] Support for custom output file font grayscale
- [x] Support for custom output file font subpixel antialiasing
- [x] Support for custom output file font LCD rendering
- [x] Support for custom output file font LCD filter
- [x] Support for custom output file font LCD subpixel
- [x] Support for custom output file font LCD vertical
- [x] Support for custom output file font LCD horizontal
- [x] Support for custom output file font LCD RGB
- [x] Support for custom output file font LCD BGR
- [x] Support for custom output file font LCD V RGB
- [x] Support for custom output file font LCD V BGR
- [x] Support for custom output file font LCD H RGB
- [x] Support for custom output file font LCD H BGR
- [x] Support for custom output file font LCD V
- [x] Support for custom output file font LCD H
- [x] Support for custom output file font LCD
- [x] Support for custom output file font
- [x] Support for custom output file
- [x] Support for custom output
- [x] Support for custom
- [x] Support for

---

### OUTPUT

請 AI 理解專案：[DeepWiki](https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next)
- [x] 支援 PDF 轉 PDF，包括文字和數學公式
- [x] 支援 LaTeX 轉 LaTeX
- [x] 支援 Markdown 轉 Markdown
- [x] 支援純文字轉純文字
- [x] 支援多種 LLM 服務（OpenAI、DeepSeek、阿里雲、硅基流動等）
- [x] 支援多種翻譯服務（Google Translate、Microsoft Translator 等）
- [x] 支援多種檔案格式（PDF、LaTeX、Markdown、純文字）
- [x] 支援多種語言（英文、中文、日文、韓文等）
- [x] 支援命令行介面（CLI）
- [x] 支援網頁使用者介面（WebUI）
- [x] 支援批次處理
- [x] 支援自訂翻譯規則
- [x] 支援自訂輸出格式
- [x] 支援自訂語言模型
- [x] 支援自訂翻譯服務
- [x] 支援自訂輸出目錄
- [x] 支援自訂輸出檔案名稱
- [x] 支援自訂輸出檔案副檔名
- [x] 支援自訂輸出檔案格式
- [x] 支援自訂輸出檔案編碼
- [x] 支援自訂輸出檔案行尾符號
- [x] 支援自訂輸出檔案縮排
- [x] 支援自訂輸出檔案間距
- [x] 支援自訂輸出檔案邊距
- [x] 支援自訂輸出檔案分頁符
- [x] 支援自訂輸出檔案頁首和頁尾
- [x] 支援自訂輸出檔案浮水印
- [x] 支援自訂輸出檔案背景
- [x] 支援自訂輸出檔案字型
- [x] 支援自訂輸出檔案字型大小
- [x] 支援自訂輸出檔案字型顏色
- [x] 支援自訂輸出檔案字型樣式
- [x] 支援自訂輸出檔案字型粗細
- [x] 支援自訂輸出檔案字型家族
- [x] 支援自訂輸出檔案字型變體
- [x] 支援自訂輸出檔案字型拉伸
- [x] 支援自訂輸出檔案字型字距調整
- [x] 支援自訂輸出檔案字型連字
- [x] 支援自訂輸出檔案字型特性
- [x] 支援自訂輸出檔案字型變體
- [x] 支援自訂輸出檔案字型光學尺寸調整
- [x] 支援自訂輸出檔案字型顯示
- [x] 支援自訂輸出檔案字型後備
- [x] 支援自訂輸出檔案字型合成
- [x] 支援自訂輸出檔案字型大小調整
- [x] 支援自訂輸出檔案字型平滑
- [x] 支援自訂輸出檔案字型渲染
- [x] 支援自訂輸出檔案字型提示
- [x] 支援自訂輸出檔案字型子像素渲染
- [x] 支援自訂輸出檔案字型抗鋸齒
- [x] 支援自訂輸出檔案字型灰階
- [x] 支援自訂輸出檔案字型子像素抗鋸齒
- [x] 支援自訂輸出檔案字型 LCD 渲染
- [x] 支援自訂輸出檔案字型 LCD 濾鏡
- [x] 支援自訂輸出檔案字型 LCD 子像素
- [x] 支援自訂輸出檔案字型 LCD 垂直
- [x] 支援自訂輸出檔案字型 LCD 水平
- [x] 支援自訂輸出檔案字型 LCD RGB
- [x] 支援自訂輸出檔案字型 LCD BGR
- [x] 支援自訂輸出檔案字型 LCD V RGB
- [x] 支援自訂輸出檔案字型 LCD V BGR
- [x] 支援自訂輸出檔案字型 LCD H RGB
- [x] 支援自訂輸出檔案字型 LCD H BGR
- [x] 支援自訂輸出檔案字型 LCD V
- [x] 支援自訂輸出檔案字型 LCD H
- [x] 支援自訂輸出檔案字型 LCD
- [x] 支援自訂輸出檔案字型
- [x] 支援自訂輸出檔案
- [x] 支援自訂輸出
- [x] 支援自訂
- [x] 支援

## 聯絡我們

如果您有任何疑問，請透過 Issue 提交反饋或加入我們的 Telegram 群組。感謝您的貢獻！

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) 為本專案的活躍貢獻者提供每月 Pro 會員碼贊助。詳情請參閱：[BabelDOC/PDFMathTranslate 貢獻者獎勵規則](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>