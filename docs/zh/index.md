<div align="center">

<img src="./docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="标题">PDFMathTranslate</h2>

<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pdf2zh-next/">
    <img src="https://img.shields.io/pypi/v/pdf2zh-next"></a>
  <a href="https://pepy.tech/projects/pdf2zh-next">
    <img src="https://static.pepy.tech/badge/pdf2zh-next"></a>
  <a href="https://hub.docker.com/repository/docker/awwaawwa/pdfmathtranslate-next/tags">
    <img src="https://img.shields.io/docker/pulls/awwaawwa/pdfmathtranslate-next"></a>
  <!-- <a href="https://gitcode.com/PDFMathTranslate-next/PDFMathTranslate-next/overview">
    <img src="https://gitcode.com/PDFMathTranslate-next/PDFMathTranslate-next/star/badge.svg"></a> -->
  <!-- <a href="https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97-Online%20Demo-FF9E0D"></a> -->
  <!-- <a href="https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate"> -->
    <!-- <img src="https://img.shields.io/badge/ModelScope-Demo-blue"></a> -->
  <!-- <a href="https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/pulls">
    <img src="https://img.shields.io/badge/contributions-welcome-green"></a> -->
  <a href="https://t.me/+Z9_SgnxmsmA5NzBl">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white"></a>
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/PDFMathTranslate-next/PDFMathTranslate-next"></a>
  <a href="https://hosted.weblate.org/engage/pdfmathtranslate-next/">
    <img src="https://hosted.weblate.org/widget/pdfmathtranslate-next/svg-badge.svg" alt="translation status" /></a>
    <a href="https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<a href="https://trendshift.io/repositories/12424" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12424" alt="Byaidu%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

PDF 科学论文翻译与双语对照。基于 [BabelDOC](https://github.com/funstory-ai/BabelDOC)。此外，本项目也是调用 BabelDOC 执行 PDF 翻译的官方参考实现。

- 📊 保留公式、图表、目录和注释 _([预览](#预览))_。
- 🌐 支持 [多种语言](https://pdf2zh-next.com/supported_languages.html)，以及多样化的 [翻译服务](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html)。
- 🤖 提供 [命令行工具](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)、[交互式用户界面](https://pdf2zh-next.com/getting-started/USAGE_webui.html) 和 [Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html)

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> 本项目基于 [AGPL v3](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/LICENSE) 许可证"按原样"提供，对程序的质量和性能不作任何保证。**程序质量和性能的全部风险由您承担。** 如果程序被发现存在缺陷，您将承担所有必要的服务、维修或更正费用。
>
> 由于维护者精力有限，我们不提供任何形式的使用协助或问题解答。相关问题将被直接关闭！（欢迎提交改进项目文档的拉取请求；遵循问题模板的 Bug 报告或友好讨论不受此影响）


有关如何贡献的详细信息，请查阅 [贡献指南](https://pdf2zh-next.com/community/Contribution-Guide.html)。

<h2 id="预览">预览</h2>

<div align="center">
<!-- <img src="./docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="demo">在线服务 🌟</h2>

您可以通过以下任一服务试用我们的应用程序：

- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 提供免费使用额度；详情请参阅页面上的常见问题部分。

<h2 id="install">如何安装与使用</h2>

### 如何安装

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>推荐用于 Windows</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>推荐用于 Linux</small>
3. [**uv** (a Python package manager)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>推荐用于 macOS</small>

---

### 如何使用

1. [使用 **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [使用 **Zotero 插件**](https://github.com/guaguastandup/zotero-pdf2zh)（第三方程序）
3. [使用 **命令行**](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

针对不同的使用场景，我们提供了多种使用程序的方法。更多信息请查看 [此页面](./getting-started/getting-started.md)。

<h2 id="usage">高级选项</h2>

有关详细说明，请参阅我们的 [高级用法](https://pdf2zh-next.com/advanced/advanced.html) 文档，以获取每个选项的完整列表。

<h2 id="downstream">二次开发 (APIs)</h2>

<!-- <!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about: -->

- [Python API](./docs/zh/advanced/API/python.md)，如何在其他 Python 程序中使用该程序
<!-- - [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="langcode">语言代码</h2>

如果您不知道需要使用什么代码来翻译成您需要的语言，请查阅 [此文档](https://pdf2zh-next.com/advanced/Language-Codes.html)

<h2 id="acknowledgement">致谢</h2>

- [Immersive Translation](https://immersivetranslate.com) 为该项目活跃贡献者提供月度 Pro 会员兑换码赞助，详情请见：[CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- [SiliconFlow](https://siliconflow.cn) 为本项目提供基于大语言模型（LLM）的免费翻译服务。

- 1.x 版本：[Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- 后端：[BabelDOC](https://github.com/funstory-ai/BabelDOC)

- PDF 库：[PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- PDF 解析：[Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- PDF 预览：[Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- 布局解析：[DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- PDF 标准：[PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- 多语言字体：请参阅 [BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets)

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Rich logging with multiprocessing](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- 文档国际化使用 [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/)


<h2 id="conduct">提交代码之前</h2>

我们欢迎贡献者积极参与，让 pdf2zh 变得更好。在您准备提交代码之前，请参阅我们的 [行为准则](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) 和 [贡献指南](https://pdf2zh-next.com/community/Contribution-Guide.html)。

<h2 id="contrib">贡献者</h2>

<!-- <a href="https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a> -->

<!-- ![Alt](https://repobeats.axiom.co/api/embed/45529651750579e099960950f757449a410477ad.svg "Repobeats analytics image") -->

<h2 id="star_hist">Star History</h2>

<a href="https://star-history.com/#PDFMathTranslate-next/PDFMathTranslate-next&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date"/>
 </picture>
</a>

<div align="right"> 
<h6><small>本页面的部分内容由 GPT 翻译，可能包含错误。</small></h6>