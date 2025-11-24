[**고급 옵션**](./introduction.md) > **번역 서비스 문서** _(현재)_

---

### 명령줄에서 사용 가능한 번역 서비스 확인하기

명령줄에서 도움말 메시지를 출력하여 사용 가능한 번역 서비스와 그 사용법을 확인할 수 있습니다.

```bash
pdf2zh_next -h
```

- [Google Cloud Translation](https://cloud.google.com/translate): Google's cloud translation service.
- [Baidu Translate](https://fanyi.baidu.com/): Baidu's translation service.
- [Alibaba Cloud Machine Translation](https://www.alibabacloud.com/product/machine-translation): Alibaba Cloud's machine translation service.

---

### OUTPUT

도움말 메시지의 끝에서 다양한 번역 서비스에 대한 자세한 정보를 확인할 수 있습니다.

- [Google Cloud Translation](https://cloud.google.com/translate): Google 의 클라우드 번역 서비스입니다.
- [Baidu Translate](https://fanyi.baidu.com/): Baidu 의 번역 서비스입니다.
- [Alibaba Cloud Machine Translation](https://www.alibabacloud.com/product/machine-translation): Alibaba Cloud 의 기계 번역 서비스입니다.


---

pdf2zh supports multiple translation engines, including:
- **OpenAI** (GPT-3.5, GPT-4)
- **Azure OpenAI** (GPT-3.5, GPT-4)
- **DeepSeek** (DeepSeek-V3)
- **Google Gemini** (Gemini-Pro)
- **Claude** (Claude-3)
- **Ollama** (Llama3, Qwen2, etc.)
- **Open Source Models** (via API Server)

!!! note "Note"
    We recommend using **OpenAI** or **Azure OpenAI** for the best experience. Other engines may have varying performance.

### How to Choose a Translation Engine
1. **OpenAI**: The most stable and recommended option.
2. **Azure OpenAI**: Suitable for enterprise users who need Azure integration.
3. **DeepSeek**: A cost-effective alternative with good performance.
4. **Google Gemini**: Good performance but may have usage restrictions in some regions.
5. **Claude**: High-quality translations but slower speed.
6. **Ollama**: For users who want to run models locally.
7. **Open Source Models**: For advanced users who want to use self-hosted models.

### Configuration Steps
1. **Set API Key**: Configure the API key for your chosen engine.
2. **Select Model**: Choose the appropriate model for your needs.
3. **Adjust Parameters**: Fine-tune parameters like temperature and max tokens.

For detailed configuration instructions, refer to the [Usage](USAGE.md) documentation.

---

### OUTPUT

### 번역 엔진 지원 정책
pdf2zh 는 다음과 같은 여러 번역 엔진을 지원합니다:
- **OpenAI** (GPT-3.5, GPT-4)
- **Azure OpenAI** (GPT-3.5, GPT-4)
- **DeepSeek** (DeepSeek-V3)
- **Google Gemini** (Gemini-Pro)
- **Claude** (Claude-3)
- **Ollama** (Llama3, Qwen2 등)
- **오픈소스 모델** (API 서버를 통해)

!!! note "참고"
    최상의 경험을 위해 **OpenAI** 또는 **Azure OpenAI** 사용을 권장합니다. 다른 엔진은 성능이 다를 수 있습니다.

### 번역 엔진 선택 방법
1. **OpenAI**: 가장 안정적이며 권장되는 옵션입니다.
2. **Azure OpenAI**: Azure 통합이 필요한 기업 사용자에게 적합합니다.
3. **DeepSeek**: 좋은 성능을 가진 비용 효율적인 대안입니다.
4. **Google Gemini**: 좋은 성능이지만 일부 지역에서 사용 제한이 있을 수 있습니다.
5. **Claude**: 높은 품질의 번역이지만 속도가 느립니다.
6. **Ollama**: 로컬에서 모델을 실행하려는 사용자를 위한 옵션입니다.
7. **오픈소스 모델**: 자체 호스팅 모델을 사용하려는 고급 사용자를 위한 옵션입니다.

### 구성 단계
1. **API 키 설정**: 선택한 엔진의 API 키를 구성합니다.
2. **모델 선택**: 필요에 맞는 적절한 모델을 선택합니다.
3. **매개변수 조정**: temperature 및 max tokens 와 같은 매개변수를 미세 조정합니다.

자세한 구성 지침은 [사용법](USAGE.md) 문서를 참조하세요.

- **Google Translate**: `google` (Free)
- **DeepL**: `deepl` (Free/Paid)
- **OpenAI**: `openai` (Paid)
- **Azure**: `azure` (Paid)

#### Tier 2 (Community Support)
- **Gemini**: `gemini` (Free/Paid)
- **Claude**: `claude` (Free/Paid)
- **DeepSeek**: `deepseek` (Free/Paid)
- **Moonshot**: `moonshot` (Free/Paid)
- **Ollama**: `ollama` (Free)
- **Volcengine**: `volcengine` (Free/Paid)
- **Aliyun**: `aliyun` (Free/Paid)
- **Tencent**: `tencent` (Free/Paid)
- **Baidu**: `baidu` (Free/Paid)
- **Youdao**: `youdao` (Free/Paid)

#### Tier 3 (Experimental)
- **NiuTrans**: `niutrans` (Free)
- **GPT-SoVITS**: `gptsovits` (Experimental)

---

### OUTPUT

#### 1 단계 (공식 지원)
- **Google Translate**: `google` (무료)
- **DeepL**: `deepl` (무료/유료)
- **OpenAI**: `openai` (유료)
- **Azure**: `azure` (유료)

#### 2 단계 (커뮤니티 지원)
- **Gemini**: `gemini` (무료/유료)
- **Claude**: `claude` (무료/유료)
- **DeepSeek**: `deepseek` (무료/유료)
- **Moonshot**: `moonshot` (무료/유료)
- **Ollama**: `ollama` (무료)
- **Volcengine**: `volcengine` (무료/유료)
- **Aliyun**: `aliyun` (무료/유료)
- **Tencent**: `tencent` (무료/유료)
- **Baidu**: `baidu` (무료/유료)
- **Youdao**: `youdao` (무료/유료)

#### 3 단계 (실험적)
- **NiuTrans**: `niutrans` (무료)
- **GPT-SoVITS**: `gptsovits` (실험적)

- [**Google Translate**](https://translate.google.com/): Google's free online translation service.
- [**DeepL**](https://www.deepl.com/translator): DeepL's high-quality translation service.
- [**OpenAI**](https://openai.com/): OpenAI's GPT models.
- [**Azure**](https://azure.microsoft.com/): Microsoft Azure's OpenAI service.

---

### OUTPUT

**1 단계 번역 엔진**은 프로젝트 관리자에 의해 직접 유지됩니다. 관리자들은 **이 프로젝트를 정기적으로 사용하지는 않지만**, GitHub 이슈를 통해 문제를 파악할 것입니다. 이러한 엔진 중 하나라도 문제가 발생하면, 관리자들은 안정성과 신뢰성을 보장하기 위해 가능한 한 빨리 수정할 것입니다.

현재 지원되는 1 단계 번역 엔진은 다음과 같습니다:

- [**Google Translate**](https://translate.google.com/): Google 의 무료 온라인 번역 서비스.
- [**DeepL**](https://www.deepl.com/translator): DeepL 의 고품질 번역 서비스.
- [**OpenAI**](https://openai.com/): OpenAI 의 GPT 모델.
- [**Azure**](https://azure.microsoft.com/): Microsoft Azure 의 OpenAI 서비스.
8. NvidiaNim
9. Azure
10. Ollama
11. DeepL
12. Google
13. Gemini
14. Claude
15. Volcengine
16. Tencent
17. Baidu
18. Youdao
19. Moonshot
20. NiuTrans
21. GPT-SoVITS
22. ArgosTranslate
23. OpenNMT
24. MarianNMT
25. EasyNMT

---

### OUTPUT

1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible
8. NvidiaNim
9. Azure
10. Ollama
11. DeepL
12. Google
13. Gemini
14. Claude
15. Volcengine
16. Tencent
17. Baidu
18. Youdao
19. Moonshot
20. NiuTrans
21. GPT-SoVITS
22. ArgosTranslate
23. OpenNMT
24. MarianNMT
25. EasyNMT

- [DeepL](https://www.deepl.com/translator)
- [Yandex Translate](https://translate.yandex.com/)
- [Bing Translator](https://www.bing.com/translator)
- [Baidu Translate](https://fanyi.baidu.com/)
- [Tencent Translate](https://fanyi.qq.com/)
- [Alibaba Translate](https://translate.alibaba.com/)
- [Youdao Translate](https://fanyi.youdao.com/)
- [Naver Papago](https://papago.naver.com/)
- [Google Translate](https://translate.google.com/)

#### Tier 3 (No Support)
- [Argos Translate](https://github.com/argosopentech/argos-translate)
- [OpenNMT](https://opennmt.net/)
- [MarianNMT](https://marian-nmt.github.io/)
- [EasyNMT](https://github.com/UKPLab/EasyNMT)

---

### OUTPUT LANGUAGE

ko

---

Let's go.

- #### Tier 2 (Community Support): - [DeepL](https://www.deepl.com/translator)
- [Yandex Translate](https://translate.yandex.com/)
- [Bing Translator](https://www.bing.com/translator)
- [Baidu Translate](https://fanyi.baidu.com/)
- [Tencent Translate](https://fanyi.qq.com/)
- [Alibaba Translate](https://translate.alibaba.com/)
- [Youdao Translate](https://fanyi.youdao.com/)
- [Naver Papago](https://papago.naver.com/)
- [Google Translate](https://translate.google.com/)

#### Tier 3 (No Support)
- [Argos Translate](https://github.com/argosopentech/argos-translate)
- [OpenNMT](https://opennmt.net/)
- [MarianNMT](https://marian-nmt.github.io/)
- [EasyNMT](https://github.com/UKPLab/EasyNMT)

---

### OUTPUT LANGUAGE

ko

---

Let's go.

**2 단계 번역 엔진**은 커뮤니티에서 유지보수 및 지원됩니다.  
이러한 엔진에 문제가 발생할 경우, 프로젝트 관리자들은 직접 수정을 제공하지 않습니다. 대신 관련 이슈에 `help wanted` 라벨을 붙이고 기여자들의 풀 리퀘스트를 통해 문제 해결을 도와줄 것을 환영합니다.

프로그램에서 지원되지만 1 단계에 명시적으로 나열되지 않은 모든 엔진은 2 단계 번역 엔진으로 간주됩니다.
- #### 2 단계 (커뮤니티 지원): - [DeepL](https://www.deepl.com/translator)
- [Yandex Translate](https://translate.yandex.com/)
- [Bing Translator](https://www.bing.com/translator)
- [Baidu Translate](https://fanyi.baidu.com/)
- [Tencent Translate](https://fanyi.qq.com/)
- [Alibaba Translate](https://translate.alibaba.com/)
- [Youdao Translate](https://fanyi.youdao.com/)
- [Naver Papago](https://papago.naver.com/)
- [Google Translate](https://translate.google.com/)

#### 3 단계 (지원 없음)
- [Argos Translate](https://github.com/argosopentech/argos-translate)
- [OpenNMT](https://opennmt.net/)
- [MarianNMT](https://marian-nmt.github.io/)
- [EasyNMT](https://github.com/UKPLab/EasyNMT)

> [!WARNING]  
> These engines are not maintained anymore. If you want to use them, please use an older version of pdf2zh.

- [**Google Cloud Translation**](https://cloud.google.com/translate): Google's cloud translation service.
- [**Baidu Translate**](https://fanyi.baidu.com/): Baidu's translation service.
- [**Alibaba Cloud Machine Translation**](https://www.alibabacloud.com/product/machine-translation): Alibaba Cloud's machine translation service.

---

### OUTPUT LANGUAGE

ko

- **Google Cloud Translation** (deprecated in v0.7.0)
- **Baidu Translate** (deprecated in v0.7.0)
- **Alibaba Cloud Machine Translation** (deprecated in v0.7.0)

> [!WARNING]
> These engines are no longer maintained. If you need to use them, please use an older version of pdf2zh.

---

### OUTPUT

다음 번역 엔진들은 **더 이상 사용되지 않으며**(deprecated) 유지보수나 지원이 중단되었습니다:
- **Google Cloud Translation** (v0.7.0 에서 deprecated)
- **Baidu Translate** (v0.7.0 에서 deprecated)
- **Alibaba Cloud Machine Translation** (v0.7.0 에서 deprecated)

> [!WARNING]
> 이러한 엔진들은 더 이상 유지보수되지 않습니다. 사용해야 하는 경우 이전 버전의 pdf2zh 를 사용하세요.

3. DeepL
4. OpenAI
5. Azure
6. Gemini
7. Claude
8. DeepSeek
9. Moonshot
10. Ollama
11. Volcengine
12. Aliyun
13. Tencent
14. Baidu
15. Youdao
16. NiuTrans
17. GPT-SoVITS

---

### OUTPUT

1. Bing
2. Google
3. DeepL
4. OpenAI
5. Azure
6. Gemini
7. Claude
8. DeepSeek
9. Moonshot
10. Ollama
11. Volcengine
12. Aliyun
13. Tencent
14. Baidu
15. Youdao
16. NiuTrans
17. GPT-SoVITS

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>