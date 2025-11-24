<div align="center">

<img src="./../../docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="제목">PDFMathTranslate</h2>

<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pdf2zh-next/">
    <img src="https://img.shields.io/pypi/v/pdf2zh-next"></a>
  <a href="https://pepy.tech/projects/pdf2zh-next">
    <img src="https://static.pepy.tech/badge/pdf2zh-next"></a>
  <a href="https://hub.docker.com/repository/docker/awwaawwa/pdfmathtranslate-next/tags">
    <img src="https://img.shields.io/docker/pulls/awwaawwa/pdfmathtranslate-next"></a>
  <a href="https://hellogithub.com/repository/8ec2cfd3ef744762bf531232fa32bc47" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=8ec2cfd3ef744762bf531232fa32bc47&claim_uid=JQ0yfeBNjaTuqDU&theme=small" alt="추천｜HelloGitHub" /></a>
  <!-- <a href="https://gitcode.com/PDFMathTranslate/PDFMathTranslate-next/overview">
    <img src="https://gitcode.com/PDFMathTranslate/PDFMathTranslate-next/star/badge.svg"></a> -->
  <!-- <a href="https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97-Online%20Demo-FF9E0D"></a> -->
  <!-- <a href="https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate"> -->
    <!-- <img src="https://img.shields.io/badge/ModelScope-Demo-blue"></a> -->
  <!-- <a href="https://github.com/PDFMathTranslate/PDFMathTranslate-next/pulls">
    <img src="https://img.shields.io/badge/contributions-welcome-green"></a> -->
  <a href="https://t.me/+Z9_SgnxmsmA5NzBl">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white"></a>
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/PDFMathTranslate/PDFMathTranslate-next"></a>
  <a href="https://hosted.weblate.org/engage/pdfmathtranslate-next/">
    <img src="https://hosted.weblate.org/widget/pdfmathtranslate-next/svg-badge.svg" alt="translation status" /></a>
    The next generation of `PDFMathTranslate` - `pdf2zh-next` is a powerful tool designed to extract text and mathematical formulas from PDF files and translate them into the desired language. It supports a variety of translation services, including OpenAI, Azure, Google, DeepSeek, and DeepL, ensuring high-quality translations for academic and technical documents.

## Features

- **Accurate Text Extraction**: Utilize `pdfplumber` and `pymupdf` to extract text and mathematical formulas from PDF files with high precision.
- **Multi-Translation Service Support**: Choose from OpenAI, Azure, Google, DeepSeek, and DeepL for translations.
- **Flexible Output Options**: Generate translated documents in Markdown, LaTeX, or PDF format.
- **Customizable Translation**: Select specific pages or page ranges for translation, and customize the output language.
- **Batch Processing**: Translate multiple PDF files in one go with batch processing capabilities.

## Installation

You can install `pdf2zh-next` using pip:

```bash
pip install pdf2zh-next
```

For more detailed installation instructions, including how to set up the necessary API keys, please refer to the [Installation](./getting-started/INSTALLATION.md) guide.

## Quick Start

To get started with `pdf2zh-next`, you can use the Command Line Interface (CLI) or the WebUI.

### Using Command Line

1. **Set your API key** (required for translation services):

    ```bash
    pdf2zh config --api-key <your-api-key> --service <service-name>
    ```

    Replace `<your-api-key>` with your actual API key and `<service-name>` with the desired translation service (e.g., `openai`, `azure`, `google`, `deepseek`, `deepl`).

2. **Translate a PDF file**:

    ```bash
    pdf2zh translate --input <path-to-pdf> --output <path-to-output> --target-lang <language-code>
    ```

    Replace `<path-to-pdf>` with the path to your PDF file, `<path-to-output>` with the desired output path, and `<language-code>` with the target language code (e.g., `zh` for Chinese, `ja` for Japanese).

For more examples and advanced usage, check out the [Command Line](./getting-started/USAGE_cli.md) documentation.

### Using WebUI

For a more interactive experience, you can use the WebUI:

1. **Start the WebUI server**:

    ```bash
    pdf2zh webui
    ```

2. **Open your browser** and navigate to `http://localhost:7860` to access the WebUI.

3. **Upload your PDF file**, configure the translation settings, and start the translation process.

For detailed instructions on using the WebUI, visit the [WebUI](./getting-started/USAGE_webui.md) guide.

## Documentation

For comprehensive documentation, including detailed guides and advanced configuration options, please visit our [documentation site](https://pdf2zh-next.com).

- [Getting Started](https://pdf2zh-next.com/getting-started/)
- [Advanced](https://pdf2zh-next.com/advanced/)
- [Supported Languages](https://pdf2zh-next.com/supported-languages/)
- [Community](https://pdf2zh-next.com/community/)
- [FAQ](https://pdf2zh-next.com/faq/)
- [For Translators](https://pdf2zh-next.com/for-translators/)

## Contributing

We welcome contributions! If you'd like to contribute to `pdf2zh-next`, please check out our [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is built upon the original [PDFMathTranslate](https://github.com/Z-Y-X-1/PDFMathTranslate) by Z-Y-X-1.
- Special thanks to all the contributors and the open-source community for their support.

---

<p align="center">
    Made with  ❤️ by the PDFMathTranslate team
</p>

---

### OUTPUT

<a href="https://deepwiki.com/PDFMathTranslate/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

`PDFMathTranslate` 의 차세대 버전인 `pdf2zh-next` 는 PDF 파일에서  텍스트와 수학 공식을 추출하여 원하는 언어로 번역하는 강력한 도구입니다. OpenAI, Azure, Google, DeepSeek, DeepL 등 다양한 번역 서비스를 지원하여 학술 및 기술 문서의 고품질 번역을 보장합니다.

## 기능

- **정확한  텍스트 추출**: `pdfplumber` 와 `pymupdf` 를 활용하여 PDF 파일에서  텍스트와 수학 공식을 높은 정밀도로 추출합니다.
- **다중 번역 서비스 지원**: OpenAI, Azure, Google, DeepSeek, DeepL 중에서 번역 서비스를 선택할 수 있습니다.
- **유연한 출력 옵션**: 번역된 문서를 Markdown, LaTeX 또는 PDF 형식으로 생성합니다.
- **맞춤형 번역**: 특정 페이지나 페이지 범위를 선택하여 번역하고, 출력 언어를 사용자 정의할 수 있습니다.
- **일괄 처리**: 일괄 처리 기능으로 여러 PDF 파일을 한 번에 번역할 수 있습니다.

## 설치

pip 를 사용하여 `pdf2zh-next` 를 설치할 수 있습니다:

```bash
pip install pdf2zh-next
```

필요한 API 키를 설정하는 방법을 포함한 더 자세한 설치 지침은 [설치](./getting-started/INSTALLATION.md) 가이드를 참조하세요.

## 빠른 시작

`pdf2zh-next` 를 시작하려면 명령줄 인터페이스 (CLI) 나 WebUI 를 사용할 수 있습니다.

### 명령줄 사용

1. **API 키 설정** (번역 서비스에 필요):

    ```bash
    pdf2zh config --api-key <your-api-key> --service <service-name>
    ```

    `<your-api-key>`  를 실제 API 키로, `<service-name>` 을 원하는 번역 서비스 (예: `openai`, `azure`, `google`, `deepseek`, `deepl`) 로 바꾸세요.

2. **PDF 파일 번역**:

    ```bash
    pdf2zh translate --input <path-to-pdf> --output <path-to-output> --target-lang <language-code>
    ```

    `<path-to-pdf>` 를 PDF 파일 경로로, `<path-to-output>`  을 원하는 출력 경로로, `<language-code>` 를 대상 언어 코드 (예: 중국어는 `zh`, 일본어는 `ja`) 로 바꾸세요.

더 많은 예제와 고급 사용법은 [명령줄](./getting-started/USAGE_cli.md) 문서를 확인하세요.

### WebUI 사용

보다 대화형 경험을 원한다면 WebUI 를 사용할 수 있습니다:

1. **WebUI 서버 시작**:

    ```bash
    pdf2zh webui
    ```

2. **브라우저를 열고** `http://localhost:7860`  으로 이동하여 WebUI 에 접속합니다.

3. **PDF 파일을 업로드**하고, 번역 설정을 구성한 후 번역 프로세스를 시작합니다.

WebUI 사용에 대한 자세한 지침은 [WebUI](./getting-started/USAGE_webui.md) 가이드를 방문하세요.

## 문서

자세한 가이드와 고급 구성  옵션을 포함한 포괄적인 문서는 [문서 사이트](https://pdf2zh-next.com) 를 방문하세요.

- [시작하기](https://pdf2zh-next.com/getting-started/)
- [고급 옵션](https://pdf2zh-next.com/advanced/)
- [지원 언어](https://pdf2zh-next.com/supported-languages/)
- [커뮤니티](https://pdf2zh-next.com/community/)
- [자주 묻는 질문](https://pdf2zh-next.com/faq/)
- [문서 번역 기여 가이드](https://pdf2zh-next.com/for-translators/)

## 기여

기여를 환영합니다! `pdf2zh-next` 에 기여하고 싶으시다면 [기여 지침](CONTRIBUTING.md) 을 확인해 주세요.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 감사의 말

- 이 프로젝트는 Z-Y-X-1 의 원본 [PDFMathTranslate](https://github.com/Z-Y-X-1/PDFMathTranslate)  를 기반으로 구축되었습니다.
- 모든 기여자와 오픈소스 커뮤니티의 지원에 특별한 감사를 드립니다.

---

<p align="center">
    PDFMathTranslate  팀이 ❤️  을 담아 만들었습니다.
</p>

---

<a href="https://trendshift.io/repositories/12424" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12424" alt="Byaidu%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

PDF 과학 논문 번역 및 이중 언어 비교.

- 📊 수식, 차트, 목차 및 주석 보존 _([미리보기](#미리보기))_.
- 🌐 [다양한 언어](https://pdf2zh-next.com/supported_languages.html) 및 다양한 [번역 서비스](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html) 지원.
- 🤖 [명령줄 도구](https://pdf2zh-next.com/getting-started/USAGE_commandline.html), [대화형 사용자 인터페이스](https://pdf2zh-next.com/getting-started/USAGE_webui.html), [Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) 제공

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> 이 프로젝트는 [AGPL v3](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/LICENSE) 라이선스 하에 "있는 그대로" 제공되며, 프로그램의 품질과 성능에 대한 어떠한 보증도 제공되지 않습니다. **프로그램의 품질과 성능에 대한 모든 위험은 사용자 본인이 부담합니다.** 프로그램에 결함이 발견될 경우, 필요한 모든 서비스, 수리 또는 수정 비용은 사용자 본인이 책임져야 합니다.
>
> 유지보수 담당자의 제한된 에너지로 인해, 우리는 어떠한 형태의 사용 지원이나 문제 해결도 제공하지 않습니다. 관련 이슈는 즉시 닫힐 것입니다! (프로젝트 문서 개선을 위한 풀 리퀘스트는 환영합니다; 이슈 템플릿을 준수하는 버그 또는 친절한 이슈는 이 정책의 영향을 받지 않습니다)


자세한 기여 방법은 [기여 가이드](https://pdf2zh-next.com/community/Contribution-Guide.html) 를 참조하세요.

<h2 id="업데이트">업데이트</h2>

- [2025 년 6 월 4 일] 프로젝트 이름이 변경되어 [PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next) 로 이동했습니다 (by [@awwaawwa](https://github.com/awwaawwa))
- [2025 년 3 월 3 일] 새로운 백엔드 [BabelDOC](https://github.com/funstory-ai/BabelDOC) WebUI 에 대한 실험적 지원이 추가되었습니다 (by [@awwaawwa](https://github.com/awwaawwa))
- [2025 년 2 월 22 일] 개선된 릴리스 CI 와 잘 패키징된 windows-amd64 exe 가 추가되었습니다 (by [@awwaawwa](https://github.com/awwaawwa))
- [2024 년 12 월 24 일] 번역기가 이제 [Xinference](https://github.com/xorbitsai/inference) 의 로컬 모델을 지원합니다 _(by [@imClumsyPanda](https://github.com/imClumsyPanda))_
- [2024 년 12 월 19 일] `-cp` 를 사용하여 비-PDF/A 문서가 이제 지원됩니다 _(by [@reycn](https://github.com/reycn))_
- [2024 년 12 월 13 일] 추가 백엔드 지원이 추가되었습니다 _(by [@YadominJinta](https://github.com/YadominJinta))_
- [2024 년 12 월 10 일] 번역기가 이제 Azure 의 OpenAI 모델을 지원합니다 _(by [@yidasanqian](https://github.com/yidasanqian))_

<h2 id="미리보기">미리보기</h2>

<div align="center">
<!-- <img src="./../../docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="demo">온라인 서비스 🌟</h2>

> [!NOTE]
>
> pdf2zh 2.0 은 현재 온라인 데모를 제공하지 않습니다

다음 데모 중 하나를 사용하여 저희 애플리케이션을 시험해 볼 수 있습니다:

- [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html) (requires installation)
- [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) (requires installation)
- [Using **API**](https://pdf2zh-next.com/getting-started/USAGE_api.html) (requires installation)

---

### OUTPUT

- [v1.x 공개 무료 서비스](https://pdf2zh.com/) 설치 없이 온라인 사용 가능 _(권장)_
- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 무료 사용량 제공; 자세한 내용은 페이지 내 FAQ 섹션 참조 _(권장)_
- [**WebUI** 사용](https://pdf2zh-next.com/getting-started/USAGE_webui.html) (설치 필요)
- [**명령줄** 사용](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) (설치 필요)
- [**API** 사용](https://pdf2zh-next.com/getting-started/USAGE_api.html) (설치 필요)
<!-- - [Demo hosted on HuggingFace](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker)
- [Demo hosted on ModelScope](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate) without installation. -->

데모의 컴퓨팅 리소스는 제한되어 있으므로 남용하지 않도록 주의해 주세요.

<h2 id="설치">설치 및 사용법</h2>

### 설치

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>Windows 용 추천</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>Linux 용 추천</small>
3. [**uv** (a Python package manager)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>macOS 용 추천</small>

---

### 사용법

1. [**WebUI** 사용](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [**Zotero 플러그인** 사용](https://github.com/guaguastandup/zotero-pdf2zh) (서드파티 프로그램)
3. [**명령줄** 사용](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

다양한 사용 사례에 따라 우리 프로그램을 사용하는 별도의 방법을 제공합니다. 더 많은 정보는 [이 페이지](./getting-started/getting-started.md) 를 확인하세요.

<h2 id="usage">고급 옵션</h2>

자세한 설명은 각 옵션의 전체 목록을 확인하기 위해 [고급 사용법](https://pdf2zh-next.com/advanced/advanced.html) 문서를 참조하세요.

<h2 id="downstream">2 차 개발 (API)</h2>

> [!NOTE]
>
> 현재 관련 문서가 제공되지 않습니다. 나중에 보충될 예정이니, 조금만 기다려 주세요.


<!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about:

- [Python API](./docs/APIS.md#api-python), how to use the program in other Python programs
- [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="langcode">언어 코드</h2>

필요한 언어로 번역하기 위해 어떤 코드를 사용해야 할지 모르겠다면 [이 문서](https://pdf2zh-next.com/advanced/Language-Codes.html) 를 확인하세요.

<!-- 
<h2 id="todo">TODOs</h2>

- [ ] Parse layout with DocLayNet based models, [PaddleX](https://github.com/PaddlePaddle/PaddleX/blob/17cc27ac3842e7880ca4aad92358d3ef8555429a/paddlex/repo_apis/PaddleDetection_api/object_det/official_categories.py#L81), [PaperMage](https://github.com/allenai/papermage/blob/9cd4bb48cbedab45d0f7a455711438f1632abebe/README.md?plain=1#L102), [SAM2](https://github.com/facebookresearch/sam2)

- [ ] Fix page rotation, table of contents, format of lists

- [ ] Fix pixel formula in old papers

- [ ] Async retry except KeyboardInterrupt

- [ ] Knuth–Plass algorithm for western languages

- [ ] Support non-PDF/A files

- [ ] Plugins of [Zotero](https://github.com/zotero/zotero) and [Obsidian](https://github.com/obsidianmd/obsidian-releases) -->

<h2 id="acknowledgement">감사의 말</h2>

- [Immersive Translation](https://immersivetranslate.com) 은 이 프로젝트에 활발히 기여하는 기여자들을 위해 매월 Pro 멤버십 교환 코드를 후원합니다. 자세한 내용은 [CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md) 에서 확인하세요.

- [SiliconFlow](https://siliconflow.cn) 는 이 프로젝트를 위해 대규모 언어 모델 (LLM) 로 구동되는 무료 번역 서비스를 제공합니다.

- 1.x 버전: [Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- 백엔드: [BabelDOC](https://github.com/funstory-ai/BabelDOC)

- PDF 라이브러리: [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- PDF 파싱: [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- PDF 미리보기: [Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- 레이아웃 파싱: [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- PDF 표준: [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- 다국어 폰트: [BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets) 참조

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Rich logging with multiprocessing](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- 문서 국제화 (i18n) 는 [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/) 를 사용합니다.


<h2 id="conduct">코드 제출 전에</h2>

우리는 pdf2zh 를 더 나은 방향으로 발전시키기 위해 기여자들의 적극적인 참여를 환영합니다. 코드를 제출하기 전에 [행동 강령](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) 과 [기여 가이드](https://pdf2zh-next.com/community/Contribution-Guide.html) 를 참고해 주세요.

<h2 id="contrib">기여자</h2>

<a href="https://github.com/PDFMathTranslate/PDFMathTranslate-next/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a>

![Alt](https://repobeats.axiom.co/api/embed/45529651750579e099960950f757449a410477ad.svg "Repobeats analytics image")

<h2 id="star_hist">스타 히스토리</h2>

<a href="https://star-history.com/#PDFMathTranslate/PDFMathTranslate-next&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date"/>
 </picture>
</a>

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>