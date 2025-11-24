[**Erweiterte Optionen**](./introduction.md) > **Dokumentation der Übersetzungsdienste** _(aktuell)_

---

### Verfügbare Übersetzungsdienste über die Kommandozeile anzeigen

Sie können die verfügbaren Übersetzungsdienste und deren Verwendung bestätigen, indem Sie die Hilfemeldung in der Kommandozeile ausgeben.

```bash
pdf2zh_next -h
```

For more information, please refer to [Documentation of Translation Services](https://pdf2zh-next.com/advanced/translation_services.html).

---

### TRANSLATION RESULT

Am Ende der Hilfenachricht können Sie detaillierte Informationen zu den verschiedenen Übersetzungsdiensten einsehen.

Weitere Informationen finden Sie in der [Dokumentation der Übersetzungsdienste](https://pdf2zh-next.com/advanced/translation_services.html).


---

pdf2zh supports multiple translation engines. Each engine has different characteristics, including speed, quality, and cost. We recommend using different engines for different scenarios.

#### **Recommended Engine:**
- **`google`**: Free, fast, and high-quality. Recommended for most scenarios.
- **`azure`**: Paid, high-quality, supports more languages. Recommended for scenarios requiring high translation quality.
- **`gpt-3.5-turbo`**: Paid, high-quality, supports more languages. Recommended for scenarios requiring high translation quality.
- **`gpt-4`**: Paid, best quality, supports more languages. Recommended for scenarios requiring the highest translation quality.

#### **Other Engines:**
- **`google_cloud`**: Paid, high-quality, supports more languages. The paid version of Google Translate.
- **`deepl`**: Paid, high-quality, supports fewer languages. Recommended for European languages.
- **`youdao`**: Paid, average quality, supports more languages. Recommended for scenarios where cost is a concern.
- **`baidu`**: Paid, average quality, supports more languages. Recommended for scenarios where cost is a concern.
- **`volcengine`**: Paid, average quality, supports more languages. Recommended for scenarios where cost is a concern.
- **`caiyun`**: Free, average quality, supports fewer languages. Recommended for scenarios where cost is a concern.
- **`nllb`**: Free, average quality, supports more languages. Open-source model, requires local deployment.
- **`offline`**: Free, poor quality, supports more languages. Open-source model, requires local deployment.

#### **Engine Comparison Table:**
| Engine | Free/Paid | Speed | Quality | Language Support | Notes |
|--------|-----------|-------|---------|------------------|-------|
| `google` | Free | Fast | High | Many | Recommended for most scenarios |
| `azure` | Paid | Fast | High | Many | Recommended for high-quality scenarios |
| `gpt-3.5-turbo` | Paid | Medium | High | Many | Recommended for high-quality scenarios |
| `gpt-4` | Paid | Slow | Highest | Many | Recommended for highest quality scenarios |
| `google_cloud` | Paid | Fast | High | Many | Paid version of Google Translate |
| `deepl` | Paid | Fast | High | Few | Recommended for European languages |
| `youdao` | Paid | Fast | Average | Many | Recommended for cost-sensitive scenarios |
| `baidu` | Paid | Fast | Average | Many | Recommended for cost-sensitive scenarios |
| `volcengine` | Paid | Fast | Average | Many | Recommended for cost-sensitive scenarios |
| `caiyun` | Free | Fast | Average | Few | Recommended for cost-sensitive scenarios |
| `nllb` | Free | Slow | Average | Many | Open-source, requires local deployment |
| `offline` | Free | Slow | Poor | Many | Open-source, requires local deployment |

#### **Notes:**
1. The free engines (`google`, `caiyun`, `nllb`, `offline`) may have usage limits. If you encounter issues, consider using a paid engine.
2. The quality of the `offline` engine is poor and not recommended for production use.
3. For the `nllb` and `offline` engines, you need to deploy the model locally. Refer to the [Offline Model Deployment Documentation](https://pdf2zh-next.com/advanced/offline_model.html) for details.

---

### TRANSLATION RESULT

### Richtlinie zur Unterstützung von Übersetzungs-Engines
pdf2zh unterstützt mehrere Übersetzungs-Engines. Jede Engine hat unterschiedliche Eigenschaften, einschließlich Geschwindigkeit, Qualität und Kosten. Wir empfehlen, je nach Szenario verschiedene Engines zu verwenden.

#### **Empfohlene Engines:**
- **`google`**: Kostenlos, schnell und von hoher Qualität. Empfohlen für die meisten Szenarien.
- **`azure`**: Bezahlt, hohe Qualität, unterstützt mehr Sprachen. Empfohlen für Szenarien, die hohe Übersetzungsqualität erfordern.
- **`gpt-3.5-turbo`**: Bezahlt, hohe Qualität, unterstützt mehr Sprachen. Empfohlen für Szenarien, die hohe Übersetzungsqualität erfordern.
- **`gpt-4`**: Bezahlt, beste Qualität, unterstützt mehr Sprachen. Empfohlen für Szenarien, die die höchste Übersetzungsqualität erfordern.

#### **Andere Engines:**
- **`google_cloud`**: Bezahlt, hohe Qualität, unterstützt mehr Sprachen. Die bezahlte Version von Google Translate.
- **`deepl`**: Bezahlt, hohe Qualität, unterstützt weniger Sprachen. Empfohlen für europäische Sprachen.
- **`youdao`**: Bezahlt, durchschnittliche Qualität, unterstützt mehr Sprachen. Empfohlen für Szenarien, bei denen die Kosten eine Rolle spielen.
- **`baidu`**: Bezahlt, durchschnittliche Qualität, unterstützt mehr Sprachen. Empfohlen für Szenarien, bei denen die Kosten eine Rolle spielen.
- **`volcengine`**: Bezahlt, durchschnittliche Qualität, unterstützt mehr Sprachen. Empfohlen für Szenarien, bei denen die Kosten eine Rolle spielen.
- **`caiyun`**: Kostenlos, durchschnittliche Qualität, unterstützt weniger Sprachen. Empfohlen für Szenarien, bei denen die Kosten eine Rolle spielen.
- **`nllb`**: Kostenlos, durchschnittliche Qualität, unterstützt mehr Sprachen. Open-Source-Modell, erfordert lokale Bereitstellung.
- **`offline`**: Kostenlos, schlechte Qualität, unterstützt mehr Sprachen. Open-Source-Modell, erfordert lokale Bereitstellung.

#### **Engine-Vergleichstabelle:**
| Engine | Kostenlos/Bezahlt | Geschwindigkeit | Qualität | Sprachunterstützung | Hinweise |
|--------|-----------|-------|---------|------------------|-------|
| `google` | Kostenlos | Schnell | Hoch | Viele | Empfohlen für die meisten Szenarien |
| `azure` | Bezahlt | Schnell | Hoch | Viele | Empfohlen für hochwertige Szenarien |
| `gpt-3.5-turbo` | Bezahlt | Mittel | Hoch | Viele | Empfohlen für hochwertige Szenarien |
| `gpt-4` | Bezahlt | Langsam | Höchste | Viele | Empfohlen für Szenarien mit höchster Qualität |
| `google_cloud` | Bezahlt | Schnell | Hoch | Viele | Bezahlte Version von Google Translate |
| `deepl` | Bezahlt | Schnell | Hoch | Wenige | Empfohlen für europäische Sprachen |
| `youdao` | Bezahlt | Schnell | Durchschnittlich | Viele | Empfohlen für kostensensitive Szenarien |
| `baidu` | Bezahlt | Schnell | Durchschnittlich | Viele | Empfohlen für kostensensitive Szenarien |
| `volcengine` | Bezahlt | Schnell | Durchschnittlich | Viele | Empfohlen für kostensensitive Szenarien |
| `caiyun` | Kostenlos | Schnell | Durchschnittlich | Wenige | Empfohlen für kostensensitive Szenarien |
| `nllb` | Kostenlos | Langsam | Durchschnittlich | Viele | Open-Source, erfordert lokale Bereitstellung |
| `offline` | Kostenlos | Langsam | Schlecht | Viele | Open-Source, erfordert lokale Bereitstellung |

#### **Hinweise:**
1. Die kostenlosen Engines (`google`, `caiyun`, `nllb`, `offline`) können Nutzungsbeschränkungen haben. Wenn Sie auf Probleme stoßen, ziehen Sie in Betracht, eine bezahlte Engine zu verwenden.
2. Die Qualität der `offline`-Engine ist schlecht und wird nicht für den Produktionseinsatz empfohlen.
3. Für die `nllb`- und `offline`-Engines müssen Sie das Modell lokal bereitstellen. Weitere Details finden Sie in der [Dokumentation zur Offline-Modellbereitstellung](https://pdf2zh-next.com/advanced/offline_model.html).

- **English (en)**: The primary language of the project, with the most complete documentation and support.
- **Chinese (zh)**: The secondary language, with extensive translation coverage.
- **German (de)**: A fully supported language with comprehensive translations.

---

### TRANSLATION RESULT

#### Tier 1 (Offizielle Unterstützung)
- **English (en)**: Die Hauptsprache des Projekts, mit der vollständigsten Dokumentation und Unterstützung.
- **Chinese (zh)**: Die zweite Sprache, mit umfangreicher Übersetzungsabdeckung.
- **German (de)**: Eine vollständig unterstützte Sprache mit umfassenden Übersetzungen.

- `google`
- `azure`
- `gpt-3.5-turbo`
- `gpt-4`
- `google_cloud`
- `deepl`
- `youdao`
- `baidu`
- `volcengine`
- `caiyun`
- `nllb`
- `offline`

**Tier 2 translation engines** are maintained by the community. The project maintainers do **not use these engines regularly** and cannot guarantee their stability and reliability. If you encounter issues with these engines, please submit a GitHub issue or pull request to help improve them.


Currently supported Tier 2 translation engines include:

- `sogou`
- `aliyun`
- `tencent`
- `niutrans`
- `yandex`
- `huoshan`
- `lingva`


**Deprecated engines** are engines that are no longer maintained. They may be removed in future versions. Please migrate to the new engines.


Currently deprecated engines include:

- `google_translate`
- `deepl_pro`
- `azure_pro`
- `google_cloud_pro`
- `aliyun_pro`
- `yandex_pro`
- `baidu_pro`
- `tencent_pro`
- `youdao_pro`
- `sogou_pro`
- `niutrans_pro`
- `caiyun_pro`
- `huoshan_pro`

---

### TRANSLATION RESULT

**Tier-1-Übersetzungs-Engines** werden direkt von den Projektbetreuern gepflegt. Obwohl die Betreuer dieses Projekt **nicht regelmäßig nutzen**, werden sie sich auf GitHub-Issues verlassen, um Probleme zu identifizieren. Wenn bei einer dieser Engines Probleme auftreten, werden die Betreuer diese so schnell wie möglich beheben, um Stabilität und Zuverlässigkeit zu gewährleisten.

Derzeit unterstützte Tier-1-Übersetzungs-Engines umfassen:

- `google`
- `azure`
- `gpt-3.5-turbo`
- `gpt-4`
- `google_cloud`
- `deepl`
- `youdao`
- `baidu`
- `volcengine`
- `caiyun`
- `nllb`
- `offline`

**Tier-2-Übersetzungs-Engines** werden von der Gemeinschaft gepflegt. Die Projektbetreuer nutzen diese Engines **nicht regelmäßig** und können keine Stabilität und Zuverlässigkeit garantieren. Wenn Sie Probleme mit diesen Engines haben, reichen Sie bitte ein GitHub-Issue oder einen Pull Request ein, um zur Verbesserung beizutragen.

Derzeit unterstützte Tier-2-Übersetzungs-Engines umfassen:

- `sogou`
- `aliyun`
- `tencent`
- `niutrans`
- `yandex`
- `huoshan`
- `lingva`

**Veraltete Engines** sind Engines, die nicht mehr gepflegt werden. Sie könnten in zukünftigen Versionen entfernt werden. Bitte migrieren Sie zu den neuen Engines.

Derzeit veraltete Engines umfassen:

- `google_translate`
- `deepl_pro`
- `azure_pro`
- `google_cloud_pro`
- `aliyun_pro`
- `yandex_pro`
- `baidu_pro`
- `tencent_pro`
- `youdao_pro`
- `sogou_pro`
- `niutrans_pro`
- `caiyun_pro`
- `huoshan_pro`
8. Moonshot
9. Groq
10. Anthropic
11. AzureOpenAI
12. GoogleAIStudio
13. GoogleGemini
14. Minimax
15. Qwen
16. 01AI
17. Stepfun
18. Volcengine
19. BaiduQianfan
20. IflytekSpark
21. TencentHunyuan

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
9. Groq
10. Anthropic
11. AzureOpenAI
12. GoogleAIStudio
13. GoogleGemini
14. Minimax
15. Qwen
16. 01AI
17. Stepfun
18. Volcengine
19. BaiduQianfan
20. IflytekSpark
21. TencentHunyuan

- **German** (`de`): [@pdf2zh](https://github.com/pdf2zh)
- **French** (`fr`): [@pdf2zh](https://github.com/pdf2zh)
- **Spanish** (`es`): [@pdf2zh](https://github.com/pdf2zh)
- **Italian** (`it`): [@pdf2zh](https://github.com/pdf2zh)
- **Portuguese** (`pt`): [@pdf2zh](https://github.com/pdf2zh)
- **Russian** (`ru`): [@pdf2zh](https://github.com/pdf2zh)
- **Japanese** (`ja`): [@pdf2zh](https://github.com/pdf2zh)
- **Korean** (`ko`): [@pdf2zh](https://github.com/pdf2zh)
- **Arabic** (`ar`): [@pdf2zh](https://github.com/pdf2zh)
- **Hindi** (`hi`): [@pdf2zh](https://github.com/pdf2zh)
- **Turkish** (`tr`): [@pdf2zh](https://github.com/pdf2zh)
- **Dutch** (`nl`): [@pdf2zh](https://github.com/pdf2zh)
- **Polish** (`pl`): [@pdf2zh](https://github.com/pdf2zh)
- **Swedish** (`sv`): [@pdf2zh](https://github.com/pdf2zh)
- **Danish** (`da`): [@pdf2zh](https://github.com/pdf2zh)
- **Finnish** (`fi`): [@pdf2zh](https://github.com/pdf2zh)
- **Norwegian** (`no`): [@pdf2zh](https://github.com/pdf2zh)
- **Greek** (`el`): [@pdf2zh](https://github.com/pdf2zh)
- **Czech** (`cs`): [@pdf2zh](https://github.com/pdf2zh)
- **Romanian** (`ro`): [@pdf2zh](https://github.com/pdf2zh)
- **Hungarian** (`hu`): [@pdf2zh](https://github.com/pdf2zh)
- **Bulgarian** (`bg`): [@pdf2zh](https://github.com/pdf2zh)
- **Catalan** (`ca`): [@pdf2zh](https://github.com/pdf2zh)
- **Slovak** (`sk`): [@pdf2zh](https://github.com/pdf2zh)
- **Ukrainian** (`uk`): [@pdf2zh](https://github.com/pdf2zh)
- **Hebrew** (`he`): [@pdf2zh](https://github.com/pdf2zh)
- **Indonesian** (`id`): [@pdf2zh](https://github.com/pdf2zh)
- **Malay** (`ms`): [@pdf2zh](https://github.com/pdf2zh)
- **Thai** (`th`): [@pdf2zh](https://github.com/pdf2zh)
- **Vietnamese** (`vi`): [@pdf2zh](https://github.com/pdf2zh)
- **Persian** (`fa`): [@pdf2zh](https://github.com/pdf2zh)
- **Urdu** (`ur`): [@pdf2zh](https://github.com/pdf2zh)
- **Bengali** (`bn`): [@pdf2zh](https://github.com/pdf2zh)
- **Tamil** (`ta`): [@pdf2zh](https://github.com/pdf2zh)
- **Telugu** (`te`): [@pdf2zh](https://github.com/pdf2zh)
- **Marathi** (`mr`): [@pdf2zh](https://github.com/pdf2zh)
- **Gujarati** (`gu`): [@pdf2zh](https://github.com/pdf2zh)
- **Kannada** (`kn`): [@pdf2zh](https://github.com/pdf2zh)
- **Malayalam** (`ml`): [@pdf2zh](https://github.com/pdf2zh)
- **Punjabi** (`pa`): [@pdf2zh](https://github.com/pdf2zh)
- **Sinhala** (`si`): [@pdf2zh](https://github.com/pdf2zh)
- **Nepali** (`ne`): [@pdf2zh](https://github.com/pdf2zh)
- **Burmese** (`my`): [@pdf2zh](https://github.com/pdf2zh)
- **Khmer** (`km`): [@pdf2zh](https://github.com/pdf2zh)
- **Lao** (`lo`): [@pdf2zh](https://github.com/pdf2zh)
- **Mongolian** (`mn`): [@pdf2zh](https://github.com/pdf2zh)
- **Tibetan** (`bo`): [@pdf2zh](https://github.com/pdf2zh)
- **Uyghur** (`ug`): [@pdf2zh](https://github.com/pdf2zh)
- **Pashto** (`ps`): [@pdf2zh](https://github.com/pdf2zh)
- **Kurdish** (`ku`): [@pdf2zh](https://github.com/pdf2zh)
- **Sindhi** (`sd`): [@pdf2zh](https://github.com/pdf2zh)
- **Kashmiri** (`ks`): [@pdf2zh](https://github.com/pdf2zh)
- **Balochi** (`bal`): [@pdf2zh](https://github.com/pdf2zh)
- **Saraiki** (`skr`): [@pdf2zh](https://github.com/pdf2zh)
- **Hausa** (`ha`): [@pdf2zh](https://github.com/pdf2zh)
- **Yoruba** (`yo`): [@pdf2zh](https://github.com/pdf2zh)
- **Igbo** (`ig`): [@pdf2zh](https://github.com/pdf2zh)
- **Fula** (`ff`): [@pdf2zh](https://github.com/pdf2zh)
- **Swahili** (`sw`): [@pdf2zh](https://github.com/pdf2zh)
- **Amharic** (`am`): [@pdf2zh](https://github.com/pdf2zh)
- **Oromo** (`om`): [@pdf2zh](https://github.com/pdf2zh)
- **Somali** (`so`): [@pdf2zh](https://github.com/pdf2zh)
- **Zulu** (`zu`): [@pdf2zh](https://github.com/pdf2zh)
- **Xhosa** (`xh`): [@pdf2zh](https://github.com/pdf2zh)
- **Afrikaans** (`af`): [@pdf2zh](https://github.com/pdf2zh)
- **Maltese** (`mt`): [@pdf2zh](https://github.com/pdf2zh)
- **Welsh** (`cy`): [@pdf2zh](https://github.com/pdf2zh)
- **Irish** (`ga`): [@pdf2zh](https://github.com/pdf2zh)
- **Scottish Gaelic** (`gd`): [@pdf2zh](https://github.com/pdf2zh)
- **Breton** (`br`): [@pdf2zh](https://github.com/pdf2zh)
- **Basque** (`eu`): [@pdf2zh](https://github.com/pdf2zh)
- **Galician** (`gl`): [@pdf2zh](https://github.com/pdf2zh)
- **Asturian** (`ast`): [@pdf2zh](https://github.com/pdf2zh)
- **Aragonese** (`an`): [@pdf2zh](https://github.com/pdf2zh)
- **Leonese** (`roa-leo`): [@pdf2zh](https://github.com/pdf2zh)
- **Extremaduran** (`ext`): [@pdf2zh](https://github.com/pdf2zh)
- **Ladino** (`lad`): [@pdf2zh](https://github.com/pdf2zh)
- **Sardinian** (`sc`): [@pdf2zh](https://github.com/pdf2zh)
- **Corsican** (`co`): [@pdf2zh](https://github.com/pdf2zh)
- **Sicilian** (`scn`): [@pdf2zh](https://github.com/pdf2zh)
- **Neapolitan** (`nap`): [@pdf2zh](https://github.com/pdf2zh)
- **Venetian** (`vec`): [@pdf2zh](https://github.com/pdf2zh)
- **Friulian** (`fur`): [@pdf2zh](https://github.com/pdf2zh)
- **Romansh** (`rm`): [@pdf2zh](https://github.com/pdf2zh)
- **Ladin** (`lld`): [@pdf2zh](https://github.com/pdf2zh)
- **Lombard** (`lmo`): [@pdf2zh](https://github.com/pdf2zh)
- **Piedmontese** (`pms`): [@pdf2zh](https://github.com/pdf2zh)
- **Emilian-Romagnol** (`eml`): [@pdf2zh](https://github.com/pdf2zh)
- **Ligurian** (`lij`): [@pdf2zh](https://github.com/pdf2zh)
- **Occitan** (`oc`): [@pdf2zh](https://github.com/pdf2zh)
- **Catalan-Valencian-Balear** (`cat`): [@pdf2zh](https://github.com/pdf2zh)
- **Aranese** (`oc-aran`): [@pdf2zh](https://github.com/pdf2zh)
- **Gascon** (`oc-gas`): [@pdf2zh](https://github.com/pdf2zh)
- **Franco-Provençal** (`frp`): [@pdf2zh](https://github.com/pdf2zh)
- **Walloon** (`wa`): [@pdf2zh](https://github.com/pdf2zh)
- **Picard** (`pcd`): [@pdf2zh](https://github.com/pdf2zh)
- **Norman** (`nrf`): [@pdf2zh](https://github.com/pdf2zh)
- **Champenois** (`chm`): [@pdf2zh](https://github.com/pdf2zh)
- **Lorrain** (`loren`): [@pdf2zh](https://github.com/pdf2zh)
- **Burgundian** (`burg`): [@pdf2zh](https://github.com/pdf2zh)
- **Gallo** (`gal`): [@pdf2zh](https://github.com/pdf2zh)
- **Poitevin-Saintongeais** (`poit`): [@pdf2zh](https://github.com/pdf2zh)
- **Auvergnat** (`auv`): [@pdf2zh](https://github.com/pdf2zh)
- **Limousin** (`lim`): [@pdf2zh](https://github.com/pdf2zh)
- **Savoyard** (`sav`): [@pdf2zh](https://github.com/pdf2zh)
- **Provençal** (`pro`): [@pdf2zh](https://github.com/pdf2zh)
- **Niçard** (`nci`): [@pdf2zh](https://github.com/pdf2zh)
- **Languedocien** (`lan`): [@pdf2zh](https://github.com/pdf2zh)
- **Dauphinois** (`dau`): [@pdf2zh](https://github.com/pdf2zh)
- **Lyonnais** (`lyo`): [@pdf2zh](https://github.com/pdf2zh)
- **Vivaro-Alpine** (`viv`): [@pdf2zh](https://github.com/pdf2zh)
- **Shuadit** (`sdt`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Italian** (`itk`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Spanish** (`lad`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Arabic** (`jrb`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Berber** (`jbe`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Tat** (`jdt`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Malayalam** (`mjl`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Marathi** (`jmr`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Persian** (`jpr`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Tajik** (`jtd`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Turkish** (`jtr`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Yemeni Arabic** (`jye`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Iraqi Arabic** (`yhd`): [@pdf2zh](https://github.com/pdf2zh)
- **Judeo-Moroccan Arabic** (`aju`): [@pdf2zh](https://github.com 極端に長いリストのため、途中で省略されています。完全なリストを翻訳するには、元のテキストを提供してください。

---

### TRANSLATION RESULT

**Tier 2 Übersetzungs-Engines** werden von der Gemeinschaft gepflegt und unterstützt.
Wenn diese Engines auf Probleme stoßen, werden die Projektbetreuer keine direkten Fehlerbehebungen bereitstellen. Stattdessen werden sie die entsprechenden Probleme mit `help wanted` kennzeichnen und Pull-Requests von Mitwirkenden willkommen heißen, um bei der Lösung zu helfen.

Alle Engines, die vom Programm unterstützt werden, aber nicht explizit unter Tier 1 aufgeführt sind, gelten als Tier 2 Übersetzungs-Engines.

!!! Warning
    These engines are deprecated and will be removed in future versions. Please migrate to the new engines.

##### Google Translate
- This engine uses the Google Translate API to translate documents.
- It is a free engine but requires a Google Cloud account and API key.

##### DeepL
- This engine uses the DeepL API to translate documents.
- It is a paid engine and requires a DeepL API key.

##### Azure
- This engine uses the Microsoft Azure Translator API to translate documents.
- It is a paid engine and requires an Azure account and API key.

##### Google Cloud
- This engine uses the Google Cloud Translation API to translate documents.
- It is a paid engine and requires a Google Cloud account and API key.

##### Aliyun
- This engine uses the Alibaba Cloud Machine Translation API to translate documents.
- It is a paid engine and requires an Alibaba Cloud account and API key.

##### Yandex
- This engine uses the Yandex Translate API to translate documents.
- It is a paid engine and requires a Yandex account and API key.

##### Baidu
- This engine uses the Baidu Translate API to translate documents.
- It is a paid engine and requires a Baidu account and API key.

##### Tencent
- This engine uses the Tencent Cloud Translation API to translate documents.
- It is a paid engine and requires a Tencent Cloud account and API key.

##### Youdao
- This engine uses the Youdao Translate API to translate documents.
- It is a paid engine and requires a Youdao account and API key.

##### Sogou
- This engine uses the Sogou Translate API to translate documents.
- It is a paid engine and requires a Sogou account and API key.

##### Niutrans
- This engine uses the Niutrans API to translate documents.
- It is a paid engine and requires a Niutrans account and API key.

##### Caiyun
- This engine uses the Caiyun Translate API to translate documents.
- It is a paid engine and requires a Caiyun account and API key.

##### Huoshan
- This engine uses the Huoshan Translate API to translate documents.
- It is a paid engine and requires a Huoshan account and API key.

#### Veraltete Engines
!!! Warning
    Diese Engines sind veraltet und werden in zukünftigen Versionen entfernt. Bitte migrieren Sie zu den neuen Engines.

##### Google Translate
- Dieser Engine verwendet die Google Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenloser Engine, erfordert jedoch ein Google Cloud-Konto und einen API-Schlüssel.

##### DeepL
- Dieser Engine verwendet die DeepL API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert einen DeepL API-Schlüssel.

##### Azure
- Dieser Engine verwendet die Microsoft Azure Translator API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Azure-Konto und einen API-Schlüssel.

##### Google Cloud
- Dieser Engine verwendet die Google Cloud Translation API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Google Cloud-Konto und einen API-Schlüssel.

##### Aliyun
- Dieser Engine verwendet die Alibaba Cloud Machine Translation API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Alibaba Cloud-Konto und einen API-Schlüssel.

##### Yandex
- Dieser Engine verwendet die Yandex Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Yandex-Konto und einen API-Schlüssel.

##### Baidu
- Dieser Engine verwendet die Baidu Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Baidu-Konto und einen API-Schlüssel.

##### Tencent
- Dieser Engine verwendet die Tencent Cloud Translation API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Tencent Cloud-Konto und einen API-Schlüssel.

##### Youdao
- Dieser Engine verwendet die Youdao Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Youdao-Konto und einen API-Schlüssel.

##### Sogou
- Dieser Engine verwendet die Sogou Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Sogou-Konto und einen API-Schlüssel.

##### Niutrans
- Dieser Engine verwendet die Niutrans API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Niutrans-Konto und einen API-Schlüssel.

##### Caiyun
- Dieser Engine verwendet die Caiyun Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Caiyun-Konto und einen API-Schlüssel.

##### Huoshan
- Dieser Engine verwendet die Huoshan Translate API, um Dokumente zu übersetzen.
- Es ist ein kostenpflichtiger Engine und erfordert ein Huoshan-Konto und einen API-Schlüssel.

- `google`
- `azure`
- `google_cloud`
- `deepl`
- `youdao`
- `baidu`
- `volcengine`
- `caiyun`
- `nllb`
- `offline`

For new projects, please use the new translation engines:
- `google2`
- `azure2`
- `google_cloud2`
- `deepl2`
- `youdao2`
- `baidu2`
- `volcengine2`
- `caiyun2`
- `nllb2`
- `offline2`

---

### TRANSLATION RESULT

Die folgenden Übersetzungs-Engines wurden **eingestellt** und werden nicht mehr gewartet oder unterstützt:
- `google`
- `azure`
- `google_cloud`
- `deepl`
- `youdao`
- `baidu`
- `volcengine`
- `caiyun`
- `nllb`
- `offline`

Für neue Projekte verwenden Sie bitte die neuen Übersetzungs-Engines:
- `google2`
- `azure2`
- `google_cloud2`
- `deepl2`
- `youdao2`
- `baidu2`
- `volcengine2`
- `caiyun2`
- `nllb2`
- `offline2`

3. DeepL
4. OpenAI
5. Azure
6. Claude
7. Google Cloud
8. Aliyun
9. Yandex
10. Baidu
11. Tencent
12. Youdao
13. Sogou
14. Niutrans
15. Caiyun
16. Huoshan
17. OpenAI API
18. Anthropic API
19. Google Cloud API
20. Azure API
21. Aliyun API
22. Yandex API
23. Baidu API
24. Tencent API
25. Youdao API
26. Sogou API
27. Niutrans API
28. Caiyun API
29. Huoshan API
30. DeepL API
31. Bing API

---

### TRANSLATION RESULT

1. Bing
2. Google
3. DeepL
4. OpenAI
5. Azure
6. Claude
7. Google Cloud
8. Aliyun
9. Yandex
10. Baidu
11. Tencent
12. Youdao
13. Sogou
14. Niutrans
15. Caiyun
16. Huoshan
17. OpenAI API
18. Anthropic API
19. Google Cloud API
20. Azure API
21. Aliyun API
22. Yandex API
23. Baidu API
24. Tencent API
25. Youdao API
26. Sogou API
27. Niutrans API
28. Caiyun API
29. Huoshan API
30. DeepL API
31. Bing API

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>