[**高級選項**](./introduction.md) > **翻譯服務文檔** _(current)_

---

### 通過命令行查看可用的翻譯服務

您可以通過在命令行中打印幫助訊息來確認可用的翻譯服務及其使用方法。

```bash
pdf2zh_next -h
```

Example:

```bash
$ pdf2zh --help
...
Translation Services:
- OpenAI: GPT-4o-mini, GPT-4o, GPT-4
- Google: gemini-1.5-flash-8b, gemini-1.5-flash, gemini-1.5-pro
- Anthropic: claude-3-5-sonnet, claude-3-haiku
- DeepSeek: deepseek-chat, deepseek-reasoning
- Moonshot: moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k
- ZhipuAI: glm-4-flash, glm-4-plus, glm-4-air, glm-4-airx, glm-4v-plus, glm-4
- 01.ai: yi-large, yi-large-turbo, yi-large-preview
- Minimax: abab6.5s-chat, abab6.5-chat
- Microsoft Azure: gpt-4o-mini, gpt-4o, gpt-4-turbo, gpt-4
- Ollama: llama3.2-vision:latest, llama3.2:latest, llama3.2:3b, llama3.1:latest, llama3.1:8b, llama3.1:70b, llama3:latest, llama3:8b, llama3:70b, qwen2.5-vl:latest, qwen2.5-vl:7b, qwen2.5:latest, qwen2.5:72b, qwen2.5:32b, qwen2.5:14b, qwen2.5:7b, qwen2.5:3b, qwen2.5:1.5b, qwen2.5:0.5b, gemma2:latest, gemma2:27b, gemma2:9b, gemma2:2b, deepseek-v3:latest, deepseek-v3:67b, deepseek-coder-v2-lite:latest, deepseek-coder-v2-lite:16b
- vLLM: llama3.2-vision:latest, llama3.2:latest, llama3.2:3b, llama3.1:latest, llama3.1:8b, llama3.1:70b, llama3:latest, llama3:8b, llama3:70b, qwen2.5-vl:latest, qwen2.5-vl:7b, qwen2.5:latest, qwen2.5:72b, qwen2.5:32b, qwen2.5:14b, qwen2.5:7b, qwen2.5:3b, qwen2.5:1.5b, qwen2.5:0.5b, gemma2:latest, gemma2:27b, gemma2:9b, gemma2:2b, deepseek-v3:latest, deepseek-v3:67b, deepseek-coder-v2-lite:latest, deepseek-coder-v2-lite:16b
- LM Studio: llama3.2-vision:latest, llama3.2:latest, llama3.2:3b, llama3.1:latest, llama3.1:8b, llama3.1:70b, llama3:latest, llama3:8b, llama3:70b, qwen2.5-vl:latest, qwen2.5-vl:7b, qwen2.5:latest, qwen2.5:72b, qwen2.5:32b, qwen2.5:14b, qwen2.5:7b, qwen2.5:3b, qwen2.5:1.5b, qwen2.5:0.5b, gemma2:latest, gemma2:27b, gemma2:9b, gemma2:2b, deepseek-v3:latest, deepseek-v3:67b, deepseek-coder-v2-lite:latest, deepseek-coder-v2-lite:16b
```

在說明訊息的結尾，您可以查看不同翻譯服務的詳細資訊。

範例：

```bash
$ pdf2zh --help
...
翻譯服務：
- OpenAI：GPT-4o-mini、GPT-4o、GPT-4
- Google：gemini-1.5-flash-8b、gemini-1.5-flash、gemini-1.5-pro
- Anthropic：claude-3-5-sonnet、claude-3-haiku
- DeepSeek：deepseek-chat、deepseek-reasoning
- Moonshot：moonshot-v1-8k、moonshot-v1-32k、moonshot-v1-128k
- ZhipuAI：glm-4-flash、glm-4-plus、glm-4-air、glm-4-airx、glm-4v-plus、glm-4
- 01.ai：yi-large、yi-large-turbo、yi-large-preview
- Minimax：abab6.5s-chat、abab6.5-chat
- Microsoft Azure：gpt-4o-mini、gpt-4o、gpt-4-turbo、gpt-4
- Ollama：llama3.2-vision:latest、llama3.2:latest、llama3.2:3b、llama3.1:latest、llama3.1:8b、llama3.1:70b、llama3:latest、llama3:8b、llama3:70b、qwen2.5-vl:latest、qwen2.5-vl:7b、qwen2.5:latest、qwen2.5:72b、qwen2.5:32b、qwen2.5:14b、qwen2.5:7b、qwen2.5:3b、qwen2.5:1.5b、qwen2.5:0.5b、gemma2:latest、gemma2:27b、gemma2:9b、gemma2:2b、deepseek-v3:latest、deepseek-v3:67b、deepseek-coder-v2-lite:latest、deepseek-coder-v2-lite:16b
- vLLM：llama3.2-vision:latest、llama3.2:latest、llama3.2:3b、llama3.1:latest、llama3.1:8b、llama3.1:70b、llama3:latest、llama3:8b、llama3:70b、qwen2.5-vl:latest、qwen2.5-vl:7b、qwen2.5:latest、qwen2.5:72b、qwen2.5:32b、qwen2.5:14b、qwen2.5:7b、qwen2.5:3b、qwen2.5:1.5b、qwen2.5:0.5b、gemma2:latest、gemma2:27b、gemma2:9b、gemma2:2b、deepseek-v3:latest、deepseek-v3:67b、deepseek-coder-v2-lite:latest、deepseek-coder-v2-lite:16b
- LM Studio：llama3.2-vision:latest、llama3.2:latest、llama3.2:3b、llama3.1:latest、llama3.1:8b、llama3.1:70b、llama3:latest、llama3:8b、llama3:70b、qwen2.5-vl:latest、qwen2.5-vl:7b、qwen2.5:latest、qwen2.5:72b、qwen2.5:32b、qwen2.5:14b、qwen2.5:7b、qwen2.5:3b、qwen2.5:1.5b、qwen2.5:0.5b、gemma2:latest、gemma2:27b、gemma2:9b、gemma2:2b、deepseek-v3:latest、deepseek-v3:67b、deepseek-coder-v2-lite:latest、deepseek-coder-v2-lite:16b
```


---

pdf2zh supports multiple translation engines, including:

- **OpenAI**: OpenAI's GPT series models, such as GPT-4o, GPT-4-turbo, etc.
- **DeepSeek**: DeepSeek's models, such as DeepSeek-V3.
- **Azure**: Azure OpenAI service.
- **Ollama**: Local models deployed via Ollama.
- **Gemini**: Google's Gemini series models.
- **Claude**: Anthropic's Claude series models.
- **SiliconCloud**: SiliconCloud's models.
- **SiliconFlow**: SiliconFlow's models.
- **Moonshot**: Moonshot AI's models.
- **Zhipu**: Zhipu AI's models.
- **StepFun**: StepFun's models.
- **Minimax**: Minimax's models.
- **Volcengine**: Volcengine's models.
- **Tencent**: Tencent's models.
- **Aliyun**: Alibaba Cloud's models.
- **Baidu**: Baidu's models.
- **Hunyuan**: Tencent Hunyuan's models.
- **DeepL**: DeepL's translation service.
- **Google**: Google's translation service.
- **Youdao**: Youdao's translation service.
- **Baidu Translate**: Baidu's translation service.
- **Volcengine Translate**: Volcengine's translation service.

!!! note "Note"
    Some engines may require specific API keys or configurations. Please refer to the respective engine's documentation for setup instructions.

---

### TRANSLATION RESULT

### 翻譯引擎支持政策
pdf2zh 支援多種翻譯引擎，包括：

- **OpenAI**：OpenAI 的 GPT 系列模型，例如 GPT-4o、GPT-4-turbo 等。
- **DeepSeek**：DeepSeek 的模型，例如 DeepSeek-V3。
- **Azure**：Azure OpenAI 服務。
- **Ollama**：透過 Ollama 部署的本地模型。
- **Gemini**：Google 的 Gemini 系列模型。
- **Claude**：Anthropic 的 Claude 系列模型。
- **SiliconCloud**：SiliconCloud 的模型。
- **SiliconFlow**：SiliconFlow 的模型。
- **Moonshot**：Moonshot AI 的模型。
- **Zhipu**：智譜 AI 的模型。
- **StepFun**：階躍星辰的模型。
- **Minimax**：Minimax 的模型。
- **Volcengine**：火山引擎的模型。
- **Tencent**：騰訊的模型。
- **Aliyun**：阿里雲的模型。
- **Baidu**：百度的模型。
- **Hunyuan**：騰訊混元的模型。
- **DeepL**：DeepL 的翻譯服務。
- **Google**：Google 的翻譯服務。
- **Youdao**：有道翻譯的服務。
- **Baidu Translate**：百度翻譯的服務。
- **Volcengine Translate**：火山翻譯的服務。

!!! note "注意"
    部分引擎可能需要特定的 API 金鑰或配置。請參考相應引擎的文檔以獲取設定說明。

> [!NOTE]
> These providers are officially supported and guaranteed to be compatible with the latest version of pdf2zh.

- **OpenAI** (GPT-4o-mini, GPT-4o, GPT-4): The most powerful and reliable choice.
- **Google** (Gemini-1.5-flash-8b, Gemini-1.5-flash, Gemini-1.5-pro): A strong alternative to OpenAI.
- **Anthropic** (Claude-3-5-Sonnet, Claude-3-Haiku): Excellent for longer contexts.

#### Tier 2 (Community Support)
> [!WARNING]
> These providers are supported by the community. They may not be fully compatible with the latest version of pdf2zh.

- **DeepSeek**: A cost-effective option with good performance.
- **Moonshot**: Known for handling long contexts well.
- **ZhipuAI**: Popular in the Chinese market.

#### Tier 3 (Experimental)
> [!CAUTION]
> These providers are experimental and may not work reliably.

- **01.ai**: Emerging provider with potential.
- **Minimax**: Still under development.
- **Microsoft Azure**: Azure OpenAI Service.

#### Tier 4 (Self-hosted)
> [!TIP]
> Run your own model for maximum control and privacy.

- **Ollama**: Easy local deployment of open-source models.
- **vLLM**: High-performance inference for large models.
- **LM Studio**: User-friendly local model management.

---

### TRANSLATION RESULT

#### Tier 1（官方支持）
> [!NOTE]
> 這些提供商受到官方支持，並保證與 pdf2zh 的最新版本兼容。

- **OpenAI**（GPT-4o-mini、GPT-4o、GPT-4）：最強大且可靠的選擇。
- **Google**（Gemini-1.5-flash-8b、Gemini-1.5-flash、Gemini-1.5-pro）：OpenAI 的強力替代方案。
- **Anthropic**（Claude-3-5-Sonnet、Claude-3-Haiku）：非常適合處理較長的上下文。

#### Tier 2（社區支持）
> [!WARNING]
> 這些提供商由社區支持。它們可能不完全兼容 pdf2zh 的最新版本。

- **DeepSeek**：一個性價比高且性能良好的選項。
- **Moonshot**：以良好處理長上下文而聞名。
- **ZhipuAI**：在中文市場中很受歡迎。

#### Tier 3（實驗性）
> [!CAUTION]
> 這些提供商是實驗性的，可能無法可靠運作。

- **01.ai**：具有潛力的新興提供商。
- **Minimax**：仍在開發中。
- **Microsoft Azure**：Azure OpenAI 服務。

#### Tier 4（自託管）
> [!TIP]
> 運行您自己的模型以獲得最大的控制權和隱私。

- **Ollama**：輕鬆本地部署開源模型。
- **vLLM**：針對大型模型的高性能推理。
- **LM Studio**：用戶友好的本地模型管理。

- **OpenAI**: OpenAI's GPT series models, such as GPT-4o, GPT-4-turbo, etc.
- **Google**: Google's Gemini series models, such as Gemini-1.5-flash, Gemini-1.5-pro, etc.
- **Anthropic**: Anthropic's Claude series models, such as Claude-3-5-Sonnet, Claude-3-Haiku, etc.
- **DeepSeek**: DeepSeek's models, such as DeepSeek-V3.
- **Ollama**: Local models deployed via Ollama.
- **OpenAI Compatible**: Any OpenAI-compatible API endpoint.

**Tier 2 translation engines** are maintained by the community. The project maintainers do not use these engines and do not guarantee their stability. If you encounter any issues, you can submit a PR to fix them.

Currently supported Tier 2 translation engines include:

- **Moonshot**: Moonshot AI's models.
- **Zhipu**: Zhipu AI's models.
- **StepFun**: StepFun's models.
- **Minimax**: Minimax's models.
- **Volcengine**: Volcengine's models.
- **Tencent**: Tencent's models.
- **Aliyun**: Alibaba Cloud's models.
- **Baidu**: Baidu's models.
- **Hunyuan**: Tencent Hunyuan's models.
- **DeepL**: DeepL's translation service.
- **Google Translate**: Google's translation service.
- **Youdao**: Youdao's translation service.
- **Baidu Translate**: Baidu's translation service.
- **Volcengine Translate**: Volcengine's translation service.
- **SiliconCloud**: SiliconCloud's models.
- **SiliconFlow**: SiliconFlow's models.

**Tier 3 translation engines** are experimental and may not work reliably. They are provided for testing purposes only.

Currently supported Tier 3 translation engines include:

- **01.ai**: 01.ai's models.
- **Microsoft Azure**: Azure OpenAI service.

---

### zh_TW TRANSLATION

**第一層級翻譯引擎**由專案維護者直接維護。儘管維護者**不經常使用此專案**，他們將依賴 GitHub 問題來識別問題。當這些引擎遇到問題時，維護者將盡快修復它們以確保穩定性和可靠性。

目前支援的第一層級翻譯引擎包括：

- **OpenAI**：OpenAI 的 GPT 系列模型，例如 GPT-4o、GPT-4-turbo 等。
- **Google**：Google 的 Gemini 系列模型，例如 Gemini-1.5-flash、Gemini-1.5-pro 等。
- **Anthropic**：Anthropic 的 Claude 系列模型，例如 Claude-3-5-Sonnet、Claude-3-Haiku 等。
- **DeepSeek**：DeepSeek 的模型，例如 DeepSeek-V3。
- **Ollama**：透過 Ollama 部署的本地模型。
- **OpenAI Compatible**：任何與 OpenAI 相容的 API 端點。

**第二層級翻譯引擎**由社區維護。專案維護者不使用這些引擎，也不保證其穩定性。如果您遇到任何問題，可以提交 PR 來修復它們。

目前支援的第二層級翻譯引擎包括：

- **Moonshot**：Moonshot AI 的模型。
- **Zhipu**：智譜 AI 的模型。
- **StepFun**：階躍星辰的模型。
- **Minimax**：Minimax 的模型。
- **Volcengine**：火山引擎的模型。
- **Tencent**：騰訊的模型。
- **Aliyun**：阿里雲的模型。
- **Baidu**：百度的模型。
- **Hunyuan**：騰訊混元的模型。
- **DeepL**：DeepL 的翻譯服務。
- **Google Translate**：Google 的翻譯服務。
- **Youdao**：有道翻譯的服務。
- **Baidu Translate**：百度翻譯的服務。
- **Volcengine Translate**：火山翻譯的服務。
- **SiliconCloud**：SiliconCloud 的模型。
- **SiliconFlow**：SiliconFlow 的模型。

**第三層級翻譯引擎**是實驗性的，可能無法可靠運作。它們僅供測試用途。

目前支援的第三層級翻譯引擎包括：

- **01.ai**：01.ai 的模型。
- **Microsoft Azure**：Azure OpenAI 服務。
8. Moonshot
9. Anthropic
10. Google
11. Ollama
12. StepFun
13. Minimax
14. Volcengine
15. Tencent
16. Aliyun
17. Baidu
18. Hunyuan
19. DeepL
20. GoogleTranslate
21. Youdao
22. BaiduTranslate
23. VolcengineTranslate

---

### TRANSLATION RESULT

1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible
8. Moonshot
9. Anthropic
10. Google
11. Ollama
12. StepFun
13. Minimax
14. Volcengine
15. Tencent
16. Aliyun
17. Baidu
18. Hunyuan
19. DeepL
20. GoogleTranslate
21. Youdao
22. BaiduTranslate
23. VolcengineTranslate

| Provider | Free? | Quality |
| -------- | ----- | ------- |
| Aliyun | Yes | High |
| SiliconFlow | Yes | High |

---

### zh_TW TRANSLATION

#### 第二層級（社區支援）
| 供應商 | 是否免費？ | 品質 |
| -------- | ----- | ------- |
| Aliyun | 是 | 高 |
| SiliconFlow | 是 | 高 |

You can view the current list of supported engines in [Supported Languages](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html).

!!! warning "Community Support"
    Tier 2 translation engines are maintained by the community. If you encounter issues, please check existing GitHub issues or consider contributing a fix.

---

### OUTPUT

**第二層級翻譯引擎**由社區維護和支持。  
當這些引擎遇到問題時，項目維護者不會直接提供修復。相反，他們會將相關問題標記為 `help wanted`，並歡迎貢獻者提交拉取請求來幫助解決這些問題。

所有被程序支持但未明確列在第一層級下的引擎都被視為第二層級翻譯引擎。
您可以在 [支持的語言](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) 中查看當前支持的引擎列表。

!!! warning "社區支持"
    第二層級翻譯引擎由社區維護。如果您遇到問題，請檢查現有的 GitHub 問題或考慮貢獻修復。

The following engines are deprecated and will be removed in the future:

- [x] OpenAI
- [x] Aliyun
- [x] SiliconFlow

We recommend using the `OpenAI Compatible` engine instead.

---

### OUTPUT

#### 已棄用的引擎
以下引擎已被棄用，將在未來移除：

- [x] OpenAI
- [x] Aliyun
- [x] SiliconFlow

我們建議改用 `OpenAI Compatible` 引擎。

- `azure` (Azure OpenAI)
- `baidu` (Baidu Translate)
- `deepl` (DeepL Translate)
- `google` (Google Translate)
- `volcengine` (Volcengine Translate)
- `youdao` (Youdao Translate)

!!! warning "Important"
    These engines have been removed from the codebase. If you are still using them, please switch to one of the [supported engines](#translation-engine-support-policy).

---

### TRANSLATION RESULT

以下翻譯引擎已被**棄用**，將不再進行維護或支援：
- `azure`（Azure OpenAI）
- `baidu`（百度翻譯）
- `deepl`（DeepL 翻譯）
- `google`（Google 翻譯）
- `volcengine`（火山翻譯）
- `youdao`（有道翻譯）

!!! warning "重要"
    這些引擎已從程式碼庫中移除。如果您仍在使用它們，請切換至 [支援的引擎](#翻譯引擎支援政策)。

3. DeepL
4. Youdao
5. Baidu
6. Volcengine

---

### OUTPUT

1. Bing
2. Google
3. DeepL
4. Youdao
5. Baidu
6. Volcengine

<div align="right"> 
<h6><small>Some content on this page has been translated by GPT and may contain errors.</small></h6>