<div align="center">

<img src="./docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="タイトル">PDFMathTranslate</h2>

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

PDF 科学論文の翻訳と二言語比較。 [BabelDOC](https://github.com/funstory-ai/BabelDOC) に基づいています。さらに、このプロジェクトは BabelDOC を呼び出して PDF 翻訳を実行するための公式リファレンス実装でもあります。

- 📊 数式、チャート、目次、注釈を保持 _([プレビュー](#プレビュー))_。
- 🌐 [複数言語](https://pdf2zh-next.com/supported_languages.html) をサポートし、多様な [翻訳サービス](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html) に対応。
- 🤖 [コマンドラインツール](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)、[インタラクティブユーザーインターフェース](https://pdf2zh-next.com/getting-started/USAGE_webui.html)、[Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) を提供。

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> このプロジェクトは [AGPL v3](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/LICENSE) ライセンスの下で「現状のまま」提供されており、プログラムの品質および性能について一切の保証はありません。**プログラムの品質および性能に関する全てのリスクはあなたが負担します。** プログラムに欠陥があることが判明した場合、必要な全てのサービス、修理、または修正費用はあなたの責任となります。
>
> メンテナの限られたエネルギーにより、いかなる形式の使用支援や問題解決も提供しません。関連する Issue は直接クローズされます！（プロジェクトのドキュメントを改善する Pull Request は歓迎します。Issue テンプレートに従ったバグ報告や友好的な Issue はこの影響を受けません）


詳細な貢献方法については、[貢献ガイド](https://pdf2zh-next.com/community/Contribution-Guide.html) をご参照ください。

<h2 id="preview">プレビュー</h2>

<div align="center">
<!-- <img src="./docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="demo">オンラインサービス 🌟</h2>

以下のいずれかのサービスを使用して、アプリケーションをお試しいただけます：

- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 無料利用枠が利用可能です。詳細はページのよくある質問セクションをご参照ください。

<h2 id="インストール">インストールと使い方</h2>

### インストール

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>Windows ユーザーにおすすめ</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>Linux ユーザーにおすすめ</small>
3. [**uv** (Python パッケージマネージャー)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>macOS ユーザーにおすすめ</small>

---

### 使い方

1. [**WebUI** の使い方](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [**Zotero プラグイン** の使い方](https://github.com/guaguastandup/zotero-pdf2zh) (サードパーティ製プログラム)
3. [**コマンドライン** の使い方](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

異なるユースケースに対応するため、当プログラムには複数の使用方法が用意されています。詳細については [こちらのページ](./getting-started/getting-started.md) をご覧ください。

<h2 id="usage">高度なオプション</h2>

各オプションの詳細な説明については、[高度な使い方](https://pdf2zh-next.com/advanced/advanced.html) のドキュメントで全オプション一覧をご確認ください。

<h2 id="downstream">二次開発（API）</h2>

<!-- <!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about: -->

- [Python API](./docs/ja/advanced/API/python.md)、他の Python プログラムで本プログラムを使用する方法
<!-- - [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="langcode">言語コード</h2>

必要な言語に翻訳するためのコードがわからない場合は、[こちらのドキュメント](https://pdf2zh-next.com/advanced/Language-Codes.html) を確認してください。

<h2 id="acknowledgement">謝辞</h2>

- [Immersive Translation](https://immersivetranslate.com) は、このプロジェクトの積極的な貢献者向けに月間 Pro メンバーシップ交換コードをスポンサー提供しています。詳細は以下をご覧ください：[CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- [SiliconFlow](https://siliconflow.cn) は、大規模言語モデル（LLM）を活用して、このプロジェクトに無料の翻訳サービスを提供しています。

- 1.x バージョン：[Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- バックエンド：[BabelDOC](https://github.com/funstory-ai/BabelDOC)

- PDF ライブラリ：[PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- PDF 解析：[Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- PDF プレビュー：[Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- レイアウト解析：[DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- PDF 標準：[PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- 多言語フォント：[BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets) を参照

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Rich logging with multiprocessing](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- ドキュメントの国際化（i18n）には [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/) を使用


<h2 id="conduct">コードを提出する前に</h2>

pdf2zh をより良くするために、貢献者の積極的な参加を歓迎します。コードを提出する準備が整う前に、[行動規範](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) と [貢献ガイド](https://pdf2zh-next.com/community/Contribution-Guide.html) を参照してください。

<h2 id="contrib">貢献者</h2>

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
<h6><small>このページの一部のコンテンツは GPT によって翻訳されており、エラーが含まれている可能性があります。</small></h6>