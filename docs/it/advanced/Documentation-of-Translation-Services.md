[**Opzioni avanzate**](./introduction.md) > **Documentazione dei servizi di traduzione** _(attuale)_

---

### Visualizzazione dei servizi di traduzione disponibili tramite Riga di comando

È possibile verificare i servizi di traduzione disponibili e il loro utilizzo stampando il messaggio di aiuto nella Riga di comando.

```bash
pdf2zh_next -h
```

txt
pdf2zh translate [OPTIONS] [FILE]...

  Translate a PDF file.

Options:
  --target-language TEXT         Target language code.  [required]
  --source-language TEXT         Source language code.  [default: auto]
  --translation-service TEXT     Translation service to use.  [default: auto]
  --translation-service-key TEXT
                                  Translation service API key.
  --translation-service-url TEXT
                                  Translation service API URL.
  --translation-service-model TEXT
                                  Translation service model.
  --translation-engine TEXT      Translation engine to use.  [default: auto]
  --translation-engine-key TEXT  Translation engine API key.
  --translation-engine-url TEXT  Translation engine API URL.
  --translation-engine-model TEXT
                                  Translation engine model.
  --ocr-engine TEXT              OCR engine to use.  [default: auto]
  --ocr-engine-key TEXT          OCR engine API key.
  --ocr-engine-url TEXT          OCR engine API URL.
  --ocr-engine-model TEXT        OCR engine model.
  --concurrency INTEGER          Number of concurrent translation tasks.
                                 [default: 4]
  --retry INTEGER                Number of retries for translation tasks.
                                 [default: 3]
  --timeout INTEGER              Timeout for translation tasks in seconds.
                                 [default: 60]
  --output-format TEXT           Output format.  [default: pdf]
  --output-dir TEXT              Output directory.  [default: .]
  --output-filename TEXT         Output filename.
  --output-options TEXT          Output options.
  --config-file TEXT             Configuration file.
  --quiet                        Suppress output.
  --verbose                      Verbose output.
  --version                      Show the version and exit.
  --help                         Show this message and exit.
```

---

### it(ISO 639-1 code)

Alla fine del messaggio di aiuto, puoi visualizzare informazioni dettagliate sui diversi servizi di traduzione.

```txt
pdf2zh translate [OPZIONI] [FILE]...

  Traduce un file PDF.

Opzioni:
  --target-language TESTO         Codice della lingua di destinazione.  [obbligatorio]
  --source-language TESTO         Codice della lingua di origine.  [predefinito: auto]
  --translation-service TESTO     Servizio di traduzione da utilizzare.  [predefinito: auto]
  --translation-service-key TESTO
                                  Chiave API del servizio di traduzione.
  --translation-service-url TESTO
                                  URL API del servizio di traduzione.
  --translation-service-model TESTO
                                  Modello del servizio di traduzione.
  --translation-engine TESTO      Motore di traduzione da utilizzare.  [predefinito: auto]
  --translation-engine-key TESTO  Chiave API del motore di traduzione.
  --translation-engine-url TESTO  URL API del motore di traduzione.
  --translation-engine-model TESTO
                                  Modello del motore di traduzione.
  --ocr-engine TESTO              Motore OCR da utilizzare.  [predefinito: auto]
  --ocr-engine-key TESTO          Chiave API del motore OCR.
  --ocr-engine-url TESTO          URL API del motore OCR.
  --ocr-engine-model TESTO        Modello del motore OCR.
  --concurrency INTERO            Numero di attività di traduzione concorrenti.
                                 [predefinito: 4]
  --retry INTERO                  Numero di tentativi per le attività di traduzione.
                                 [predefinito: 3]
  --timeout INTERO                Timeout per le attività di traduzione in secondi.
                                 [predefinito: 60]
  --output-format TESTO           Formato di output.  [predefinito: pdf]
  --output-dir TESTO              Directory di output.  [predefinito: .]
  --output-filename TESTO         Nome del file di output.
  --output-options TESTO          Opzioni di output.
  --config-file TESTO             File di configurazione.
  --quiet                         Sopprime l'output.
  --verbose                       Output dettagliato.
  --version                       Mostra la versione ed esce.
  --help                          Mostra questo messaggio ed esce.


---

- OCR: [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- Translation: [Google Translate](https://translate.google.com), [Deepl](https://www.deepl.com/translator), [Gemini](https://deepmind.google/technologies/gemini/), [ChatGPT](https://chat.openai.com), [Ollama](https://ollama.ai/), [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [OpenAI](https://openai.com), [Claude](https://www.anthropic.com), [Moonshot](https://moonshot.cn), [ZhiPuAI](https://www.zhipuai.cn), [Qwen](https://qwenlm.github.io), [DeepSeek](https://www.deepseek.com), [VolcEngine](https://www.volcengine.com/product/machine-translation), [Youdao](https://ai.youdao.com), [Baidu](https://fanyi.baidu.com), [Tencent](https://fanyi.qq.com), [Aliyun](https://www.aliyun.com/product/ai/machine_trans), [Huoshan](https://www.volcengine.com/product/machine-translation), [Sogou](https://fanyi.sogou.com), [Caiyun](https://fanyi.caiyunapp.com), [Niutrans](https://niutrans.com), [Bing](https://www.bing.com/translator), [Bing Microsoft Translator](https://www.bing.com/translator), [Yandex](https://translate.yandex.com)

---

### TRANSLATION

### Politica di supporto dei motori di traduzione
- OCR: [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- Traduzione: [Google Translate](https://translate.google.com), [Deepl](https://www.deepl.com/translator), [Gemini](https://deepmind.google/technologies/gemini/), [ChatGPT](https://chat.openai.com), [Ollama](https://ollama.ai/), [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [OpenAI](https://openai.com), [Claude](https://www.anthropic.com), [Moonshot](https://moonshot.cn), [ZhiPuAI](https://www.zhipuai.cn), [Qwen](https://qwenlm.github.io), [DeepSeek](https://www.deepseek.com), [VolcEngine](https://www.volcengine.com/product/machine-translation), [Youdao](https://ai.youdao.com), [Baidu](https://fanyi.baidu.com), [Tencent](https://fanyi.qq.com), [Aliyun](https://www.aliyun.com/product/ai/machine_trans), [Huoshan](https://www.volcengine.com/product/machine-translation), [Sogou](https://fanyi.sogou.com), [Caiyun](https://fanyi.caiyunapp.com), [Niutrans](https://niutrans.com), [Bing](https://www.bing.com/translator), [Bing Microsoft Translator](https://www.bing.com/translator), [Yandex](https://translate.yandex.com)

- [Google](https://cloud.google.com/translate/docs/languages)
- [Azure](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)
- [Amazon](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)
- [DeepL](https://www.deepl.com/docs-api/translate-text/translate-text/)

#### Tier 2 (Community Support)
- [Argos](https://argosopentech.github.io/argos-translate/docs/supported-languages)
- [Baidu](https://fanyi-api.baidu.com/doc/21)
- [Tencent](https://cloud.tencent.com/document/product/551/7376)
- [Youdao](https://ai.youdao.com/DOCSIRMA/html/trans/api/wbfy/index.html)
- [Aliyun](https://help.aliyun.com/zh/machine-translation/support/supported-languages-and-codes)
- [Volcengine](https://www.volcengine.com/docs/4640/1308717)
- [Sogou](https://deepi.sogou.com/docs/fanyiLanguageSupport)
- [Niutrans](https://niutrans.com/documents/contents/trans_text#languageList)

---

### it(ISO 639-1 code)

#### Livello 1 (Supporto ufficiale)
- [Google](https://cloud.google.com/translate/docs/languages)
- [Azure](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)
- [Amazon](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)
- [DeepL](https://www.deepl.com/docs-api/translate-text/translate-text/)

#### Livello 2 (Supporto della comunità)
- [Argos](https://argosopentech.github.io/argos-translate/docs/supported-languages)
- [Baidu](https://fanyi-api.baidu.com/doc/21)
- [Tencent](https://cloud.tencent.com/document/product/551/7376)
- [Youdao](https://ai.youdao.com/DOCSIRMA/html/trans/api/wbfy/index.html)
- [Aliyun](https://help.aliyun.com/zh/machine-translation/support/supported-languages-and-codes)
- [Volcengine](https://www.volcengine.com/docs/4640/1308717)
- [Sogou](https://deepi.sogou.com/docs/fanyiLanguageSupport)
- [Niutrans](https://niutrans.com/documents/contents/trans_text#languageList)

- **Google**: [Google](https://cloud.google.com/translate/docs/languages)
- **Azure**: [Azure](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)
- **Amazon**: [Amazon](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)
- **DeepL**: [DeepL](https://www.deepl.com/docs-api/translate-text/translate-text/)

**Tier 2 translation engines** are maintained by the community. The project maintainers do **not use** these engines and cannot guarantee their stability. If you encounter any issues, please submit a Pull Request to fix them.


Currently supported Tier 2 translation engines include:

- **Argos**: [Argos](https://argosopentech.github.io/argos-translate/docs/supported-languages)
- **Baidu**: [Baidu](https://fanyi-api.baidu.com/doc/21)
- **Tencent**: [Tencent](https://cloud.tencent.com/document/product/551/7376)
- **Youdao**: [Youdao](https://ai.youdao.com/DOCSIRMA/html/trans/api/wbfy/index.html)
- **Aliyun**: [Aliyun](https://help.aliyun.com/zh/machine-translation/support/supported-languages-and-codes)
- **Volcengine**: [Volcengine](https://www.volcengine.com/docs/4640/1308717)
- **Sogou**: [Sogou](https://deepi.sogou.com/docs/fanyiLanguageSupport)
- **Niutrans**: [Niutrans](https://niutrans.com/documents/contents/trans_text#languageList)

If you are a user of a Tier 2 engine and encounter issues, please submit a Pull Request to fix them. The maintainers will review and merge it as soon as possible.


If you are a user of a Tier 2 engine and want to promote it to Tier 1, please contact the maintainers. The maintainers will consider promoting it to Tier 1 if the engine is stable and reliable.

I motori di traduzione di **Livello 1** sono mantenuti direttamente dai manutentori del progetto. Sebbene i manutentori **non utilizzino regolarmente questo progetto**, si affideranno ai problemi di GitHub per identificare i problemi. Quando uno qualsiasi di questi motori incontra problemi, i manutentori li risolveranno il prima possibile per garantire stabilità e affidabilità.

Attualmente, i motori di traduzione di Livello 1 supportati includono:

- **Google**: [Google](https://cloud.google.com/translate/docs/languages)
- **Azure**: [Azure](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)
- **Amazon**: [Amazon](https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html)
- **DeepL**: [DeepL](https://www.deepl.com/docs-api/translate-text/translate-text/)

I motori di traduzione di **Livello 2** sono mantenuti dalla comunità. I manutentori del progetto **non utilizzano** questi motori e non possono garantirne la stabilità. Se incontri problemi, si prega di inviare una Pull Request per risolverli.

Attualmente, i motori di traduzione di Livello 2 supportati includono:

- **Argos**: [Argos](https://argosopentech.github.io/argos-translate/docs/supported-languages)
- **Baidu**: [Baidu](https://fanyi-api.baidu.com/doc/21)
- **Tencent**: [Tencent](https://cloud.tencent.com/document/product/551/7376)
- **Youdao**: [Youdao](https://ai.youdao.com/DOCSIRMA/html/trans/api/wbfy/index.html)
- **Aliyun**: [Aliyun](https://help.aliyun.com/zh/machine-translation/support/supported-languages-and-codes)
- **Volcengine**: [Volcengine](https://www.volcengine.com/docs/4640/1308717)
- **Sogou**: [Sogou](https://deepi.sogou.com/docs/fanyiLanguageSupport)
- **Niutrans**: [Niutrans](https://niutrans.com/documents/contents/trans_text#languageList)

Se sei un utente di un motore di Livello 2 e incontri problemi, si prega di inviare una Pull Request per risolverli. I manutentori la revisioneranno e la uniranno il prima possibile.

Se sei un utente di un motore di Livello 2 e desideri promuoverlo a Livello 1, si prega di contattare i manutentori. I manutentori valuteranno di promuoverlo a Livello 1 se il motore è stabile e affidabile.
8. AzureOpenAI
9. Ollama
10. LocalAI
11. Gemini
12. Claude
13. Moonshot
14. BaiduWenxin
15. Hunyuan
16. Doubao
17. Minimax
18. Step
19. Iflyrec
20. IflytekSpark
21. 01AI
22. Grok
23. Coze
24. Mistral
25. Anthropic
26. GoogleTranslate
27. AzureAITranslator
28. AmazonTranslate
29. DeepL
30. AliyunMachineTranslation
31. TencentMachineTranslation
32. VolcengineMachineTranslation
33. Niutrans
34. BaiduTranslate
35. YoudaoTranslate
36. SogouTranslate
37. CaiyunTranslate
38. ArgosTranslate
39. BingMicrosoftTranslator
40. YandexTranslate
41. PaddleOCR
42. EasyOCR

---

### it(ISO 639-1 code)

1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible
8. AzureOpenAI
9. Ollama
10. LocalAI
11. Gemini
12. Claude
13. Moonshot
14. BaiduWenxin
15. Hunyuan
16. Doubao
17. Minimax
18. Step
19. Iflyrec
20. IflytekSpark
21. 01AI
22. Grok
23. Coze
24. Mistral
25. Anthropic
26. GoogleTranslate
27. AzureAITranslator
28. AmazonTranslate
29. DeepL
30. AliyunMachineTranslation
31. TencentMachineTranslation
32. VolcengineMachineTranslation
33. Niutrans
34. BaiduTranslate
35. YoudaoTranslate
36. SogouTranslate
37. CaiyunTranslate
38. ArgosTranslate
39. BingMicrosoftTranslator
40. YandexTranslate
41. PaddleOCR
42. EasyOCR

- **DeepL**: [DeepL](https://www.deepl.com/) is a high-quality translation service that supports multiple languages. It offers both free and paid plans. The free plan has a limit of 500,000 characters per month. For more details, refer to the [DeepL documentation](https://www.deepl.com/docs-api).
- **Google Translate**: [Google Translate](https://translate.google.com/) is a widely used translation service. It offers a free tier with a limit of 500,000 characters per month. For more details, refer to the [Google Cloud Translation documentation](https://cloud.google.com/translate/docs).

---

### TARGET LANGUAGE

it

- #### Tier 2 (Community Support): - **DeepL**: [DeepL](https://www.deepl.com/) is a high-quality translation service that supports multiple languages. It offers both free and paid plans. The free plan has a limit of 500,000 characters per month. For more details, refer to the [DeepL documentation](https://www.deepl.com/docs-api).
- **Google Translate**: [Google Translate](https://translate.google.com/) is a widely used translation service. It offers a free tier with a limit of 500,000 characters per month. For more details, refer to the [Google Cloud Translation documentation](https://cloud.google.com/translate/docs).

---

I motori di traduzione di **Livello 2** sono mantenuti e supportati dalla comunità.  
Quando questi motori incontrano problemi, i maintainer del progetto non forniranno correzioni dirette. Invece, etichetteranno le issue correlate con `help wanted` e accoglieranno pull request dai contributori per aiutare a risolverle.

Tutti i motori supportati dal programma ma non esplicitamente elencati sotto il Livello 1 sono considerati motori di traduzione di Livello 2.

- [!WARNING] Deprecated Engines
  The following engines are deprecated and will be removed in the future. Please use the [Recommended Engines](#recommended-engines) instead.

##### Google Translate (Free)
- **API**: `google`
- **Status**: Deprecated
- **Reason**: The free version of Google Translate API is no longer maintained and may be unstable.

##### Baidu Translate (Free)
- **API**: `baidu`
- **Status**: Deprecated
- **Reason**: The free version of Baidu Translate API has been discontinued.

##### Youdao Translate (Free)
- **API**: `youdao`
- **Status**: Deprecated
- **Reason**: The free version of Youdao Translate API is no longer available.

##### Caiyun Translate (Free)
- **API**: `caiyun`
- **Status**: Deprecated
- **Reason**: The free version of Caiyun Translate API has been discontinued.

#### Recommended Engines
- [!NOTE] Recommended Engines
  The following engines are recommended for use. They are stable and provide good translation quality.

##### Google Translate (Paid)
- **API**: `google`
- **Status**: Recommended
- **Reason**: The paid version of Google Translate API is stable and provides high-quality translations.

##### DeepSeek Translate (Free)
- **API**: `deepseek`
- **Status**: Recommended
- **Reason**: DeepSeek Translate provides high-quality translations and is free to use.

##### OpenAI (GPT)
- **API**: `openai`
- **Status**: Recommended
- **Reason**: OpenAI's GPT models provide high-quality translations but require an API key.

##### Azure AI Translator
- **API**: `azure`
- **Status**: Recommended
- **Reason**: Azure AI Translator is a stable and reliable translation service.

##### DeepL Translate
- **API**: `deepl`
- **Status**: Recommended
- **Reason**: DeepL Translate is known for its high-quality translations.

##### Aliyun Machine Translation
- **API**: `aliyun`
- **Status**: Recommended
- **Reason**: Aliyun Machine Translation is a stable and reliable translation service.

##### Tencent Machine Translation
- **API**: `tencent`
- **Status**: Recommended
- **Reason**: Tencent Machine Translation is a stable and reliable translation service.

##### Volcengine Machine Translation
- **API**: `volcengine`
- **Status**: Recommended
- **Reason**: Volcengine Machine Translation is a stable and reliable translation service.

##### Niutrans Machine Translation
- **API**: `niutrans`
- **Status**: Recommended
- **Reason**: Niutrans Machine Translation is a stable and reliable translation service.

#### Other Engines
- [!NOTE] Other Engines
  The following engines are available but may not be as stable or provide as high quality translations as the recommended engines.

##### ChatGPT (Free)
- **API**: `chatgpt`
- **Status**: Experimental
- **Reason**: The free version of ChatGPT may be unstable and has usage limitations.

##### Gemini (Free)
- **API**: `gemini`
- **Status**: Experimental
- **Reason**: The free version of Gemini may be unstable and has usage limitations.

##### Hunyuan (Free)
- **API**: `hunyuan`
- **Status**: Experimental
- **Reason**: The free version of Hunyuan may be unstable and has usage limitations.

##### Minimax (Free)
- **API**: `minimax`
- **Status**: Experimental
- **Reason**: The free version of Minimax may be unstable and has usage limitations.

##### Step (Free)
- **API**: `step`
- **Status**: Experimental
- **Reason**: The free version of Step may be unstable and has usage limitations.

##### Iflyrec (Free)
- **API**: `iflyrec`
- **Status**: Experimental
- **Reason**: The free version of Iflyrec may be unstable and has usage limitations.

##### Iflytek Spark (Free)
- **API**: `iflytekSpark`
- **Status**: Experimental
- **Reason**: The free version of Iflytek Spark may be unstable and has usage limitations.

##### Baidu Wenxin (Free)
- **API**: `baiduWenxin`
- **Status**: Experimental
- **Reason**: The free version of Baidu Wenxin may be unstable and has usage limitations.

##### Zhipu AI (Free)
- **API**: `zhipu`
- **Status**: Experimental
- **Reason**: The free version of Zhipu AI may be unstable and has usage limitations.

##### Moonshot (Free)
- **API**: `moonshot`
- **Status**: Experimental
- **Reason**: The free version of Moonshot may be unstable and has usage limitations.

##### 01.AI (Free)
- **API**: `zeroOneAI`
- **Status**: Experimental
- **Reason**: The free version of 01.AI may be unstable and has usage limitations.

##### Grok (Free)
- **API**: `grok`
- **Status**: Experimental
- **Reason**: The free version of Grok may be unstable and has usage limitations.

##### Coze (Free)
- **API**: `coze`
- **Status**: Experimental
- **Reason**: The free version of Coze may be unstable and has usage limitations.

##### Doubao (Free)
- **API**: `doubao`
- **Status**: Experimental
- **Reason**: The free version of Doubao may be unstable and has usage limitations.

##### Mistral (Free)
- **API**: `mistral`
- **Status**: Experimental
- **Reason**: The free version of Mistral may be unstable and has usage limitations.

##### Anthropic (Free)
- **API**: `anthropic`
- **Status**: Experimental
- **Reason**: The free version of Anthropic may be unstable and has usage limitations.

##### Ollama (Local)
- **API**: `ollama`
- **Status**: Experimental
- **Reason**: Ollama is a local deployment solution that requires manual model deployment and may have performance issues.

##### Local Model (Local)
- **API**: `local`
- **Status**: Experimental
- **Reason**: Local models require manual deployment and may have performance issues.

---

Now, I will translate the provided text into Italian, following all the specified rules.

#### Motori deprecati
- [!WARNING] Motori deprecati
  I seguenti motori sono deprecati e verranno rimossi in futuro. Si prega di utilizzare invece i [Motori consigliati](#motori-consigliati).

##### Google Translate (Gratuito)
- **API**: `google`
- **Stato**: Deprecato
- **Motivo**: La versione gratuita dell'API di Google Translate non è più mantenuta e potrebbe essere instabile.

##### Baidu Translate (Gratuito)
- **API**: `baidu`
- **Stato**: Deprecato
- **Motivo**: La versione gratuita dell'API di Baidu Translate è stata dismessa.

##### Youdao Translate (Gratuito)
- **API**: `youdao`
- **Stato**: Deprecato
- **Motivo**: La versione gratuita dell'API di Youdao Translate non è più disponibile.

##### Caiyun Translate (Gratuito)
- **API**: `caiyun`
- **Stato**: Deprecato
- **Motivo**: La versione gratuita dell'API di Caiyun Translate è stata dismessa.

#### Motori consigliati
- [!NOTE] Motori consigliati
  I seguenti motori sono consigliati per l'uso. Sono stabili e forniscono una buona qualità di traduzione.

##### Google Translate (A pagamento)
- **API**: `google`
- **Stato**: Consigliato
- **Motivo**: La versione a pagamento dell'API di Google Translate è stabile e fornisce traduzioni di alta qualità.

##### DeepSeek Translate (Gratuito)
- **API**: `deepseek`
- **Stato**: Consigliato
- **Motivo**: DeepSeek Translate fornisce traduzioni di alta qualità ed è gratuito.

##### OpenAI (GPT)
- **API**: `openai`
- **Stato**: Consigliato
- **Motivo**: I modelli GPT di OpenAI forniscono traduzioni di alta qualità ma richiedono una chiave API.

##### Azure AI Translator
- **API**: `azure`
- **Stato**: Consigliato
- **Motivo**: Azure AI Translator è un servizio di traduzione stabile e affidabile.

##### DeepL Translate
- **API**: `deepl`
- **Stato**: Consigliato
- **Motivo**: DeepL Translate è noto per le sue traduzioni di alta qualità.

##### Aliyun Machine Translation
- **API**: `aliyun`
- **Stato**: Consigliato
- **Motivo**: Aliyun Machine Translation è un servizio di traduzione stabile e affidabile.

##### Tencent Machine Translation
- **API**: `tencent`
- **Stato**: Consigliato
- **Motivo**: Tencent Machine Translation è un servizio di traduzione stabile e affidabile.

##### Volcengine Machine Translation
- **API**: `volcengine`
- **Stato**: Consigliato
- **Motivo**: Volcengine Machine Translation è un servizio di traduzione stabile e affidabile.

##### Niutrans Machine Translation
- **API**: `niutrans`
- **Stato**: Consigliato
- **Motivo**: Niutrans Machine Translation è un servizio di traduzione stabile e affidabile.

#### Altri motori
- [!NOTE] Altri motori
  I seguenti motori sono disponibili ma potrebbero non essere così stabili o fornire traduzioni di qualità elevata come i motori consigliati.

##### ChatGPT (Gratuito)
- **API**: `chatgpt`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di ChatGPT potrebbe essere instabile e ha limitazioni d'uso.

##### Gemini (Gratuito)
- **API**: `gemini`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Gemini potrebbe essere instabile e ha limitazioni d'uso.

##### Hunyuan (Gratuito)
- **API**: `hunyuan`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Hunyuan potrebbe essere instabile e ha limitazioni d'uso.

##### Minimax (Gratuito)
- **API**: `minimax`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Minimax potrebbe essere instabile e ha limitazioni d'uso.

##### Step (Gratuito)
- **API**: `step`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Step potrebbe essere instabile e ha limitazioni d'use.

##### Iflyrec (Gratuito)
- **API**: `iflyrec`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Iflyrec potrebbe essere instabile e ha limitazioni d'uso.

##### Iflytek Spark (Gratuito)
- **API**: `iflytekSpark`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Iflytek Spark potrebbe essere instabile e ha limitazioni d'uso.

##### Baidu Wenxin (Gratuito)
- **API**: `baiduWenxin`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Baidu Wenxin potrebbe essere instabile e ha limitazioni d'uso.

##### Zhipu AI (Gratuito)
- **API**: `zhipu`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Zhipu AI potrebbe essere instabile e ha limitazioni d'uso.

##### Moonshot (Gratuito)
- **API**: `moonshot`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Moonshot potrebbe essere instabile e ha limitazioni d'uso.

##### 01.AI (Gratuito)
- **API**: `zeroOneAI`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di 01.AI potrebbe essere instabile e ha limitazioni d'uso.

##### Grok (Gratuito)
- **API**: `grok`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Grok potrebbe essere instabile e ha limitazioni d'uso.

##### Coze (Gratuito)
- **API**: `coze`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Coze potrebbe essere instabile e ha limitazioni d'uso.

##### Doubao (Gratuito)
- **API**: `doubao`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Doubao potrebbe essere instabile e ha limitazioni d'uso.

##### Mistral (Gratuito)
- **API**: `mistral`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Mistral potrebbe essere instabile e ha limitazioni d'uso.

##### Anthropic (Gratuito)
- **API**: `anthropic`
- **Stato**: Sperimentale
- **Motivo**: La versione gratuita di Anthropic potrebbe essere instabile e ha limitazioni d'uso.

##### Ollama (Locale)
- **API**: `ollama`
- **Stato**: Sperimentale
- **Motivo**: Ollama è una soluzione di deployment locale che richiede il deployment manuale del modello e potrebbe avere problemi di prestazioni.

##### Modello locale (Locale)
- **API**: `local`
- **Stato**: Sperimentale
- **Motivo**: I modelli locali richiedono il deployment manuale e potrebbero avere problemi di prestazioni.

- `google` (free version)
- `baidu` (free version)
- `youdao` (free version)
- `caiyun` (free version)

Please use the [recommended engines](#recommended-engines) instead.

### Recommended Engines

The following engines are recommended for use:

- `google` (paid version): Stable and high-quality translations.
- `deepseek`: Free and high-quality translations.
- `openai`: High-quality translations but requires an API key.
- `azure`: Stable and reliable.
- `deepl`: High-quality translations.
- `aliyun`: Stable and reliable.
- `tencent`: Stable and reliable.
- `volcengine`: Stable and reliable.
- `niutrans`: Stable and reliable.

### Other Engines

The following engines are available but may not be as stable or provide as high quality translations:

- `chatgpt` (free version): May be unstable and has usage limitations.
- `gemini` (free version): May be unstable and has usage limitations.
- `hunyuan` (free version): May be unstable and has usage limitations.
- `minimax` (free version): May be unstable and has usage limitations.
- `step` (free version): May be unstable and has usage limitations.
- `iflyrec` (free version): May be unstable and has usage limitations.
- `iflytekSpark` (free version): May be unstable and has usage limitations.
- `baiduWenxin` (free version): May be unstable and has usage limitations.
- `zhipu` (free version): May be unstable and has usage limitations.
- `moonshot` (free version): May be unstable and has usage limitations.
- `zeroOneAI` (free version): May be unstable and has usage limitations.
- `grok` (free version): May be unstable and has usage limitations.
- `coze` (free version): May be unstable and has usage limitations.
- `doubao` (free version): May be unstable and has usage limitations.
- `mistral` (free version): May be unstable and has usage limitations.
- `anthropic` (free version): May be unstable and has usage limitations.
- `ollama`: Local deployment solution that requires manual model deployment and may have performance issues.
- `local`: Local models require manual deployment and may have performance issues.

---

I seguenti motori di traduzione sono stati **deprecati** e non saranno più mantenuti o supportati:
- `google` (versione gratuita)
- `baidu` (versione gratuita)
- `youdao` (versione gratuita)
- `caiyun` (versione gratuita)

Si prega di utilizzare invece i [motori consigliati](#motori-consigliati).

### Motori consigliati

I seguenti motori sono consigliati per l'uso:

- `google` (versione a pagamento): Traduzioni stabili e di alta qualità.
- `deepseek`: Traduzioni gratuite e di alta qualità.
- `openai`: Traduzioni di alta qualità ma richiede una chiave API.
- `azure`: Stabile e affidabile.
- `deepl`: Traduzioni di alta qualità.
- `aliyun`: Stabile e affidabile.
- `tencent`: Stabile e affidabile.
- `volcengine`: Stabile e affidabile.
- `niutrans`: Stabile e affidabile.

### Altri motori

I seguenti motori sono disponibili ma potrebbero non essere così stabili o fornire traduzioni di qualità elevata:

- `chatgpt` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `gemini` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `hunyuan` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `minimax` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `step` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `iflyrec` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `iflytekSpark` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `baiduWenxin` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `zhipu` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `moonshot` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `zeroOneAI` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `grok` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `coze` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `doubao` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `mistral` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `anthropic` (versione gratuita): Potrebbe essere instabile e ha limitazioni d'uso.
- `ollama`: Soluzione di deployment locale che richiede il deployment manuale del modello e potrebbe avere problemi di prestazioni.
- `local`: I modelli locali richiedono il deployment manuale e potrebbero avere problemi di prestazioni.

3. Azure
4. Amazon
5. DeepL
6. Argos
7. Baidu
8. Tencent
9. Youdao
10. Aliyun
11. Volcengine
12. Sogou
13. Niutrans
14. DeepSeek
15. OpenAI
16. ChatGPT
17. Gemini
18. Hunyuan
19. Minimax
20. Step
21. Iflyrec
22. IflytekSpark
23. BaiduWenxin
24. Zhipu
25. Moonshot
26. zeroOneAI
27. Grok
28. Coze
29. Doubao
30. Mistral
31. Anthropic
32. Ollama
33. Local

---

Now, I will translate the provided list of terms into Italian. Since these are proper names or specific terms, they should generally remain unchanged, but I will ensure they are presented correctly in the context.

1. Bing
2. Google
3. Azure
4. Amazon
5. DeepL
6. Argos
7. Baidu
8. Tencent
9. Youdao
10. Aliyun
11. Volcengine
12. Sogou
13. Niutrans
14. DeepSeek
15. OpenAI
16. ChatGPT
17. Gemini
18. Hunyuan
19. Minimax
20. Step
21. Iflyrec
22. IflytekSpark
23. BaiduWenxin
24. Zhipu
25. Moonshot
26. zeroOneAI
27. Grok
28. Coze
29. Doubao
30. Mistral
31. Anthropic
32. Ollama
33. Local

Note: Since the bypass list includes terms that should remain unchanged, and the original text is a list of proper names, I have kept them as is.

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>