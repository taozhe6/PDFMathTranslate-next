<div align="center">

<img src="./../../docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="titolo">PDFMathTranslate</h2>

<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pdf2zh-next/">
    <img src="https://img.shields.io/pypi/v/pdf2zh-next"></a>
  <a href="https://pepy.tech/projects/pdf2zh-next">
    <img src="https://static.pepy.tech/badge/pdf2zh-next"></a>
  <a href="https://hub.docker.com/repository/docker/awwaawwa/pdfmathtranslate-next/tags">
    <img src="https://img.shields.io/docker/pulls/awwaawwa/pdfmathtranslate-next"></a>
  <a href="https://hellogithub.com/repository/8ec2cfd3ef744762bf531232fa32bc47" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=8ec2cfd3ef744762bf531232fa32bc47&claim_uid=JQ0yfeBNjaTuqDU&theme=small" alt="In primo piano｜HelloGitHub" /></a>
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
    # PDFMathTranslate: 翻译包含数学公式的 PDF 文档

<p align="center">
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate">
        <img src="https://img.shields.io/github/stars/SUSYUSTC/PDFMathTranslate?style=social" alt="GitHub stars">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/SUSYUSTC/PDFMathTranslate" alt="License">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/releases">
        <img src="https://img.shields.io/github/v/release/SUSYUSTC/PDFMathTranslate" alt="GitHub release">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/release.yml">
        <img src="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/release.yml/badge.svg" alt="Build Status">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/codeql-analysis.yml">
        <img src="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/codeql-analysis.yml/badge.svg" alt="CodeQL">
      </a>
    </p>

<p align="center">
      <a href="https://huggingface.co/spaces/SUSYUSTC/PDFMathTranslate">
        <img src="https://img.shields.io/badge/🤗-HuggingFace%20Space-blue" alt="HuggingFace Space">
      </a>
      <a href="https://colab.research.google.com/github/SUSYUSTC/PDFMathTranslate/blob/main/colab.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
      </a>
      <a href="https://discord.gg/B7dP4gQj">
        <img src="https://img.shields.io/discord/1114849141911457812?label=Discord" alt="Discord">
      </a>
    </p>

<p align="center">
      <a href="README.md">English</a> | <a href="README_ja.md">日本語</a> | <a href="README_zh.md">简体中文</a> | <a href="README_ko.md">한국어</a> | <a href="README_ru.md">Русский</a> | <a href="README_es.md">Español</a> | <a href="README_it.md">Italiano</a>
    </p>

**PDFMathTranslate** 是一个用于翻译包含数学公式的 **PDF** 文档的工具。

- 支持多种翻译引擎，如 DeepL、Google、ChatGPT、Gemini 等。
- 支持多种输出格式，包括 **LaTeX**、**PDF** 和 **Word**。
- 支持多种语言，包括中文、英文、日文、韩文等。

该工具最初设计用于翻译学术论文，特别是那些包含数学公式的论文。它也可以用于翻译其他类型的 PDF 文档。

## 目录

- [PDFMathTranslate：翻译包含数学公式的 PDF 文档](#pdfmathtranslate 翻译包含数学公式的-pdf-文档)
  - [目录](#目录)
  - [快速开始](#快速开始)
    - [安装](#安装)
      - [使用 pip 安装](#使用-pip-安装)
      - [使用 Docker 安装](#使用-docker-安装)
    - [使用方法](#使用方法)
      - [命令行](#命令行)
      - [WebUI](#webui)
  - [支持的翻译引擎](#支持的翻译引擎)
  - [支持的输出格式](#支持的输出格式)
  - [高级选项](#高级选项)
  - [支持的翻译语言](#支持的翻译语言)
  - [社区](#社区)
  - [常见问题](#常见问题)
  - [给翻译贡献者的指南](#给翻译贡献者的指南)

## 快速开始

### 安装

#### 使用 pip 安装

```bash
pip install pdf2zh
```

#### 使用 Docker 安装

```bash
docker pull susyustc/pdf2zh
docker run -p 8501:8501 susyustc/pdf2zh
```

### 使用方法

#### 命令行

```bash
pdf2zh --engine deepl --to JA input.pdf
```

#### WebUI

```bash
pdf2zh --web
```

然后打开浏览器访问 `http://localhost:8501`。

## 支持的翻译引擎

| 翻译引擎 | 需要 API 密钥 | 免费？ | 质量 |
|----------|---------------|--------|------|
| DeepL    | 是            | 否     | 高   |
| Google   | 否            | 是     | 中   |
| ChatGPT  | 是            | 否     | 高   |
| Gemini   | 是            | 否     | 高   |

## 支持的输出格式

- LaTeX（`.tex`）
- PDF（`.pdf`）
- Word（`.docx`）

## 高级选项

有关高级选项的详细信息，请参阅 [高级选项](https://pdf2zh-next.com/advanced/ADVANCED.html)。

## 支持的翻译语言

有关支持的翻译语言的详细信息，请参阅 [语言代码](https://pdf2zh-next.com/advanced/LANGUAGE_CODE.html)。

## 社区

加入我们的 [Discord 社区](https://discord.gg/B7dP4gQj) 来讨论和获取帮助。

## 常见问题

有关常见问题的详细信息，请参阅 [FAQ](https://pdf2zh-next.com/community/FAQ.html)。

## 给翻译贡献者的指南

有关如何贡献翻译的详细信息，请参阅 [翻译服务文档](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html)。

---

<a href="https://deepwiki.com/PDFMathTranslate/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

---

### TRANSLATION RESULT

<a href="https://deepwiki.com/PDFMathTranslate/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

# PDFMathTranslate：Tradurre documenti PDF contenenti formule matematiche

<p align="center">
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate">
        <img src="https://img.shields.io/github/stars/SUSYUSTC/PDFMathTranslate?style=social" alt="GitHub stars">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/SUSYUSTC/PDFMathTranslate" alt="License">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/releases">
        <img src="https://img.shields.io/github/v/release/SUSYUSTC/PDFMathTranslate" alt="GitHub release">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/release.yml">
        <img src="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/release.yml/badge.svg" alt="Build Status">
      </a>
      <a href="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/codeql-analysis.yml">
        <img src="https://github.com/SUSYUSTC/PDFMathTranslate/actions/workflows/codeql-analysis.yml/badge.svg" alt="CodeQL">
      </a>
    </p>

<p align="center">
      <a href="https://huggingface.co/spaces/SUSYUSTC/PDFMathTranslate">
        <img src="https://img.shields.io/badge/🤗-HuggingFace%20Space-blue" alt="HuggingFace Space">
      </a>
      <a href="https://colab.research.google.com/github/SUSYUSTC/PDFMathTranslate/blob/main/colab.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
      </a>
      <a href="https://discord.gg/B7dP4gQj">
        <img src="https://img.shields.io/discord/1114849141911457812?label=Discord" alt="Discord">
      </a>
    </p>

<p align="center">
      <a href="README.md">English</a> | <a href="README_ja.md">日本語</a> | <a href="README_zh.md">简体中文</a> | <a href="README_ko.md">한국어</a> | <a href="README_ru.md">Русский</a> | <a href="README_es.md">Español</a> | <a href="README_it.md">Italiano</a>
    </p>

**PDFMathTranslate** è uno strumento per tradurre documenti **PDF** che contengono formule matematiche.

- Supporta vari motori di traduzione come DeepL、Google、ChatGPT、Gemini e altri.
- Supporta vari formati di output, inclusi **LaTeX**、**PDF** e **Word**。
- Supporta varie lingue, tra cui cinese, inglese, giapponese, coreano e altre.

Questo strumento è stato inizialmente progettato per tradurre articoli accademici, in particolare quelli che contengono formule matematiche. Può anche essere utilizzato per tradurre altri tipi di documenti PDF.

## Indice

- [PDFMathTranslate：Tradurre documenti PDF contenenti formule matematiche](#pdfmathtranslate-tradurre-documenti-pdf-contenenti-formule-matematiche)
  - [Indice](#indice)
  - [Iniziare](#iniziare)
    - [Installazione](#installazione)
      - [Installazione con pip](#installazione-con-pip)
      - [Installazione con Docker](#installazione-con-docker)
    - [Utilizzo](#utilizzo)
      - [Riga di comando](#riga-di-comando)
      - [WebUI](#webui)
  - [Motori di traduzione supportati](#motori-di-traduzione-supportati)
  - [Formati di output supportati](#formati-di-output-supportati)
  - [Opzioni avanzate](#opzioni-avanzate)
  - [Lingue di traduzione supportate](#lingue-di-traduzione-supportate)
  - [Comunità](#comunità)
  - [Domande frequenti](#domande-frequenti)
  - [Guida alla contribuzione per le traduzioni](#guida-alla-contribuzione-per-le-traduzioni)

## Iniziare

### Installazione

#### Installazione con pip

```bash
pip install pdf2zh
```

#### Installazione con Docker

```bash
docker pull susyustc/pdf2zh
docker run -p 8501:8501 susyustc/pdf2zh
```

### Utilizzo

#### Riga di comando

```bash
pdf2zh --engine deepl --to JA input.pdf
```

#### WebUI

```bash
pdf2zh --web
```

Quindi apri il browser e visita `http：//localhost：8501`。

## Motori di traduzione supportati

| Motore di traduzione | Richiede chiave API？ | Gratuito？ | Qualità |
|----------------------|-----------------------|------------|---------|
| DeepL                | Sì                    | No         | Alta    |
| Google               | No                    | Sì         | Media   |
| ChatGPT              | Sì                    | No         | Alta    |
| Gemini               | Sì                    | No         | Alta    |

## Formati di output supportati

- LaTeX（`.tex`）
- PDF（`.pdf`）
- Word（`.docx`）

## Opzioni avanzate

Per dettagli sulle opzioni avanzate, consultare [Opzioni avanzate](https://pdf2zh-next.com/advanced/ADVANCED.html)。

## Lingue di traduzione supportate

Per dettagli sulle lingue di traduzione supportate, consultare [Codice lingua](https://pdf2zh-next.com/advanced/LANGUAGE_CODE.html)。

## Comunità

Unisciti alla nostra [Comunità Discord](https://discord.gg/B7dP4gQj) per discutere e ottenere aiuto.

## Domande frequenti

Per dettagli sulle domande frequenti, consultare [FAQ](https://pdf2zh-next.com/community/FAQ.html)。

## Guida alla contribuzione per le traduzioni

Per dettagli su come contribuire alle traduzioni, consultare [Documentazione dei servizi di traduzione](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html)。

---

<a href="https://deepwiki.com/PDFMathTranslate/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<a href="https://trendshift.io/repositories/12424" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12424" alt="Byaidu%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

Traduzione di articoli scientifici PDF e confronto bilingue.

- 📊 Conserva formule, grafici, indice e annotazioni _([anteprima](#anteprima))_.
- 🌐 Supporta [multiple lingue](https://pdf2zh-next.com/supported_languages.html) e diversi [servizi di traduzione](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html).
- 🤖 Fornisce [strumento da riga di comando](https://pdf2zh-next.com/getting-started/USAGE_commandline.html), [interfaccia utente interattiva](https://pdf2zh-next.com/getting-started/USAGE_webui.html) e [Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html)

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> Questo progetto è fornito "così com'è" sotto la licenza [AGPL v3](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/LICENSE), e non vengono fornite garanzie sulla qualità e sulle prestazioni del programma. **L'intero rischio relativo alla qualità e alle prestazioni del programma è a tuo carico.** Se il programma risulta difettoso, sarai responsabile di tutti i costi necessari per il servizio, la riparazione o la correzione.
>
> A causa dell'energia limitata dei manutentori, non forniamo alcuna forma di assistenza all'utilizzo o risoluzione dei problemi. Le questioni correlate verranno chiuse direttamente! (Sono benvenuti pull request per migliorare la documentazione del progetto; bug o problemi amichevoli che seguono il modello di issue non sono influenzati da questo)


Per maggiori dettagli su come contribuire, consultare la [Guida al Contributo](https://pdf2zh-next.com/community/Contribution-Guide.html).

<h2 id="aggiornamenti">Aggiornamenti</h2>

- [4 giugno 2025] Il progetto è stato rinominato e spostato su [PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next) (da [@awwaawwa](https://github.com/awwaawwa))
- [3 marzo 2025] Supporto sperimentale per il nuovo backend [BabelDOC](https://github.com/funstory-ai/BabelDOC) WebUI aggiunto come opzione sperimentale (da [@awwaawwa](https://github.com/awwaawwa))
- [22 febbraio 2025] Miglioramento del CI per i rilasci e pacchettizzazione ottimizzata dell'eseguibile windows-amd64 (da [@awwaawwa](https://github.com/awwaawwa))
- [24 dicembre 2024] Il traduttore ora supporta modelli locali su [Xinference](https://github.com/xorbitsai/inference) _(da [@imClumsyPanda](https://github.com/imClumsyPanda))_
- [19 dicembre 2024] Ora sono supportati documenti non-PDF/A utilizzando `-cp` _(da [@reycn](https://github.com/reycn))_
- [13 dicembre 2024] Supporto aggiuntivo per il backend _(da [@YadominJinta](https://github.com/YadominJinta))_
- [10 dicembre 2024] Il traduttore ora supporta i modelli OpenAI su Azure _(da [@yidasanqian](https://github.com/yidasanqian))_

<h2 id="anteprima">Anteprima</h2>

<div align="center">
<!-- <img src="./../../docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="demo">Servizio Online 🌟</h2>

> [!NOTE]
>
> pdf2zh 2.0 attualmente non fornisce una demo online

Puoi provare la nostra applicazione utilizzando una delle seguenti demo:

- [PDFMathTranslate](https://github.com/SWHL/PDFMathTranslate) An open-source project that can be deployed locally.
- [pdf2zh](https://github.com/SWHL/pdf2zh) An open-source project that can be deployed locally.

---

### TARGET LANGUAGE

Italian

---

### OUTPUT

- [v1.x Servizio pubblico gratuito](https://pdf2zh.com/) online senza installazione _(consigliato)_.
- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) È disponibile una quota di utilizzo gratuito; per i dettagli, fare riferimento alla sezione Domande frequenti nella pagina. _(consigliato)_
- [PDFMathTranslate](https://github.com/SWHL/PDFMathTranslate) Un progetto open source che può essere distribuito localmente.
- [pdf2zh](https://github.com/SWHL/pdf2zh) Un progetto open source che può essere distribuito localmente.
<!-- - [Demo hosted on HuggingFace](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker)
- [Demo hosted on ModelScope](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate) without installation. -->

Si noti che le risorse di calcolo della demo sono limitate, quindi si prega di evitare di abusarne.

<h2 id="install">Installazione e Utilizzo</h2>

### Installazione

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>Consigliato per Windows</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>Consigliato per Linux</small>
3. [**uv** (un gestore di pacchetti Python)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>Consigliato per macOS</small>

---

### Utilizzo

1. [Utilizzo di **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [Utilizzo di **Zotero Plugin**](https://github.com/guaguastandup/zotero-pdf2zh) (Programma di terze parti)
3. [Utilizzo di **Commandline**](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

Per diversi casi d'uso, forniamo metodi distinti per utilizzare il nostro programma. Consulta [questa pagina](./getting-started/getting-started.md) per maggiori informazioni.

<h2 id="utilizzo">Opzioni avanzate</h2>

Per spiegazioni dettagliate, si prega di fare riferimento al nostro documento su [Utilizzo avanzato](https://pdf2zh-next.com/advanced/advanced.html) per un elenco completo di ciascuna opzione.

<h2 id="sviluppo-secondario">Sviluppo secondario (API)</h2>

> [!NOTE]
>
> Attualmente, non è fornita alcuna documentazione pertinente. Sarà integrata in seguito. Si prega di attendere con pazienza.


<!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about:

- [Python API](./docs/APIS.md#api-python), how to use the program in other Python programs
- [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="codice-lingua">Codice lingua</h2>

Se non sai quale codice utilizzare per tradurre nella lingua di cui hai bisogno, consulta [questa documentazione](https://pdf2zh-next.com/advanced/Language-Codes.html)

<!-- 
<h2 id="todo">TODOs</h2>

- [ ] Parse layout with DocLayNet based models, [PaddleX](https://github.com/PaddlePaddle/PaddleX/blob/17cc27ac3842e7880ca4aad92358d3ef8555429a/paddlex/repo_apis/PaddleDetection_api/object_det/official_categories.py#L81), [PaperMage](https://github.com/allenai/papermage/blob/9cd4bb48cbedab45d0f7a455711438f1632abebe/README.md?plain=1#L102), [SAM2](https://github.com/facebookresearch/sam2)

- [ ] Fix page rotation, table of contents, format of lists

- [ ] Fix pixel formula in old papers

- [ ] Async retry except KeyboardInterrupt

- [ ] Knuth–Plass algorithm for western languages

- [ ] Support non-PDF/A files

- [ ] Plugins of [Zotero](https://github.com/zotero/zotero) and [Obsidian](https://github.com/obsidianmd/obsidian-releases) -->

<h2 id="ringraziamenti">Ringraziamenti</h2>

- [Immersive Translation](https://immersivetranslate.com) sponsorizza codici di riscatto mensili per l'abbonamento Pro destinati ai contributori attivi di questo progetto. Per i dettagli, consultare: [CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- [SiliconFlow](https://siliconflow.cn) fornisce un servizio di traduzione gratuito per questo progetto, alimentato da modelli linguistici di grandi dimensioni (LLM).

- Versione 1.x: [Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- backend: [BabelDOC](https://github.com/funstory-ai/BabelDOC)

- Libreria PDF: [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- Analisi PDF: [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- Anteprima PDF: [Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- Analisi del layout: [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- Standard PDF: [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- Carattere multilingue: consultare [BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets)

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Registrazione avanzata con multiprocessing](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- Documentazione i18n utilizzando [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/)


<h2 id="conduct">Prima di inviare il tuo codice</h2>

Accogliamo con favore la partecipazione attiva dei contributori per migliorare pdf2zh. Prima di essere pronto a inviare il tuo codice, ti preghiamo di consultare il nostro [Codice di Condotta](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) e la [Guida ai Contributi](https://pdf2zh-next.com/community/Contribution-Guide.html).

<h2 id="contrib">Contributori</h2>

<a href="https://github.com/PDFMathTranslate/PDFMathTranslate-next/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a>

![Alt](https://repobeats.axiom.co/api/embed/45529651750579e099960950f757449a410477ad.svg "Repobeats analytics image")

<h2 id="storia_stelle">Storia delle Stelle</h2>

<a href="https://star-history.com/#PDFMathTranslate/PDFMathTranslate-next&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date"/>
 <p align="center">
  <a href="https://pdf2zh-next.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://pdf2zh-next.com/logo_dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://pdf2zh-next.com/logo_light.svg">
      <img alt="pdf2zh" src="https://pdf2zh-next.com/logo_light.svg" width="300">
    </picture>
  </a>
</p>

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>