# 為專案貢獻

> [!CAUTION]
>
> 當前專案維護者正在研究自動化文檔國際化。因此，任何與文檔國際化/翻譯相關的 PR 將不被接受！
>
> 請不要提交與文檔國際化/翻譯相關的 PR！

感謝您對本專案的關注！在開始貢獻之前，請花一些時間閱讀以下指南，以確保您的貢獻能夠順利被接受。

## 不接受貢獻的類型

1. 文檔國際化/翻譯
2. 與核心基礎設施相關的貢獻，例如 HTTP API 等。
3. 明確標記為「無需幫助」的 Issue（包括 [Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) 和 [PDFMathTranslate-next/PDFMathTranslate-next](PDFMathTranslate-next/PDFMathTranslate-next) 倉庫中的 Issue）。
4. 維護者認為不適當的其他貢獻。
5. 貢獻文檔，但修改非英文語言的文檔。
6. 需要修改 PDF 檔案的 PR。
7. 修改 `pdf2zh_next/gui_translation.yaml` 檔案的 PR。

請勿提交與上述類型相關的 PR。

> [!NOTE]
>
> 如果您想貢獻文檔，請**僅修改文檔的英文版本**。其他語言版本由貢獻者自行翻譯。

## 建議在提交前透過 Issue 與維護者討論的 PR 類型

對於以下類型的 PR，建議在提交前先與維護者討論：

1. 與多用戶共享功能相關的 PR。（本專案主要設計為單用戶使用，無意引入完整的多用戶系統）。

## 貢獻流程

1. Fork 此儲存庫並在本地端克隆它。
2. 建立一個新分支：`git checkout -b feature/<feature-name>`。
3. 進行開發並確保您的程式碼符合要求。
4. 提交您的程式碼：
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. 推送至您的儲存庫：`git push origin feature/<feature-name>`。
6. 在 GitHub 上建立一個 PR，提供詳細的描述，並向 [@awwaawwa](https://github.com/awwaawwa) 請求審查。
7. 確保所有自動化檢查都通過。

> [!TIP]
>
> 您不需要等到開發完全完成才創建 PR。提前創建 PR 可以讓我們審查您的實現並提供建議。
>
> 如果您對源代碼或相關事宜有任何疑問，請通過 aw@funstory.ai 聯繫維護者。
>
> 2.0 版本的資源文件與 [BabelDOC](https://github.com/funstory-ai/BabelDOC) 共享。下載相關資源的代碼位於 BabelDOC 中。如果您想添加新的資源文件，請通過 aw@funstory.ai 聯繫 BabelDOC 維護者。

## 基本要求

<h4 id="sop">1. 工作流程</h4>

   - 請從 `main` 分支進行 fork，並在您 fork 的分支上進行開發。
   - 提交 Pull Request (PR) 時，請提供您所做更改的詳細說明。
   - 如果您的 PR 未通過自動化檢查（顯示為 `checks failed` 和紅色叉號），請查看對應的 `details` 並修改您的提交，以確保新的 PR 通過所有檢查。


<h4 id="dev&test">2. 開發與測試</h4>

   - 使用命令 `pip install -e .` 進行開發和測試。


<h4 id="format">3. 程式碼格式化</h4>

   - 配置 `pre-commit` 工具並啟用 `black` 和 `flake8` 進行代碼格式化。


<h4 id="requpdate">4. 依賴更新</h4>

   - 如果您引入了新的依賴項，請及時更新 `pyproject.toml` 文件中的依賴項列表。


<h4 id="docupdate">5. 文檔更新</h4>

   - 如果您添加了新的命令行選項，請相應地更新所有語言版本的 `README.md` 文件中的命令行選項列表。


<h4 id="commitmsg">6. 提交訊息</h4>

   - 使用 [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)，例如：`feat(translator): add openai`。


<h4 id="codestyle">7. 編碼風格</h4>

   - 確保您提交的程式碼符合基本的編碼風格標準。
   - 變數命名請使用 snake_case 或 camelCase。


<h4 id="doctypo">8. 文檔格式</h4>

   - 對於 `README.md` 的格式，請遵循 [中文文案排版指北](https://github.com/sparanoid/chinese-copywriting-guidelines)。
   - 確保英文和中文文檔始終保持最新；其他語言文檔的更新是可選的。

## 添加翻譯引擎

1. 在 `pdf2zh/config/translate_engine_model.py` 檔案中新增一個翻譯器配置類別。
2. 在同一個檔案中，將新的翻譯器配置類別的實例添加到 `TRANSLATION_ENGINE_SETTING_TYPE` 類型別名中。
3. 在 `pdf2zh/translator/translator_impl` 資料夾中新增翻譯器的實作類別。

> [!NOTE]
>
> 本專案不打算支援任何 RPS（每秒請求數）低於 4 的翻譯引擎。請勿提交對此類引擎的支援。
> 以下類型的翻譯器也將不會被整合：
> - 已被上游維護者停止維護的翻譯器（例如 deeplx）
> - 依賴項龐大的翻譯器（例如依賴於 pytorch 的翻譯器）
> - 不穩定的翻譯器
> - 基於逆向工程 API 的翻譯器
>
> 當您不確定某個翻譯器是否符合要求時，可以發送一個 issue 與維護者討論。

## 專案結構

- **config 資料夾**：配置系統。
- **translator 資料夾**：翻譯器相關實現。
- **gui.py**：提供 GUI 介面。
- **const.py**：一些常數。
- **main.py**：提供命令行工具。
- **high_level.py**：基於 BabelDOC 的高階介面。
- **http_api.py**：提供 HTTP API（未啟動）。

向 AI 詢問以了解專案：[DeepWiki](https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next)

## 聯繫我們

如果您有任何問題，請透過 Issue 提交回饋或加入我們的 Telegram 群組。感謝您的貢獻！

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) 為本專案的活躍貢獻者贊助每月 Pro 會員碼。詳情請見：[BabelDOC/PDFMathTranslate 貢獻者獎勵規則](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>