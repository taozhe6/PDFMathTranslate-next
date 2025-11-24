<div align="center">

<img src="./../../docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="タイトル">PDFMathTranslate</h2>

<p>
  <!-- PyPI -->
  <a href="https://pypi.org/project/pdf2zh-next/">
    <img src="https://img.shields.io/pypi/v/pdf2zh-next"></a>
  <a href="https://pepy.tech/projects/pdf2zh-next">
    <img src="https://static.pepy.tech/badge/pdf2zh-next"></a>
  <a href="https://hub.docker.com/repository/docker/awwaawwa/pdfmathtranslate-next/tags">
    <img src="https://img.shields.io/docker/pulls/awwaawwa/pdfmathtranslate-next"></a>
  <a href="https://hellogithub.com/repository/8ec2cfd3ef744762bf531232fa32bc47" target="_blank"><img src="https://api.hellogithub.com/v1/widgets/recommend.svg?rid=8ec2cfd3ef744762bf531232fa32bc47&claim_uid=JQ0yfeBNjaTuqDU&theme=small" alt="おすすめ｜HelloGitHub" /></a>
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
    ## PDFMathTranslate
    
    [English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)
    
    `PDFMathTranslate` is a tool that converts PDF files containing mathematical formulas into translations in any language, preserving the original formatting and formulas. It supports both command-line and web interface usage.
    
    ## Features
    
    - **Accurate Translation**: Accurately translates text and mathematical formulas in PDF files.
    - **Format Preservation**: Maintains the original layout and format of the PDF.
    - **Multiple Translation Services**: Supports various translation services including DeepL, Google, OpenAI, and more.
    - **Command Line and Web Interface**: Provides both command-line tools and a web interface for easy use.
    - **Batch Processing**: Supports batch processing of multiple PDF files.
    
    ## Installation
    
    ### Using pip
    
    ```bash
    pip install pdf2zh
    ```
    
    ### Using Docker
    
    ```bash
    docker pull nabenabe0928/pdf2zh:latest
    ```
    
    For more installation methods, please refer to the [Installation Guide](https://pdf2zh-next.com/getting-started/INSTALLATION.html).
    
    ## Usage
    
    ### Command Line
    
    ```bash
    pdf2zh --input input.pdf --output output.pdf --to ja
    ```
    
    For more command-line options, please refer to the [Command Line Usage Guide](https://pdf2zh-next.com/getting-started/USAGE_cli.html).
    
    ### Web Interface
    
    Start the web interface with the following command:
    
    ```bash
    pdf2zh --web
    ```
    
    Then open your browser and visit `http://localhost:7860`.
    
    For more details on using the web interface, please refer to the [Web Interface Usage Guide](https://pdf2zh-next.com/getting-started/USAGE_webui.html).
    
    ## Supported Languages
    
    `PDFMathTranslate` supports translation into multiple languages. For the list of supported languages and their corresponding language codes, please refer to the [Supported Languages](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html) documentation.
    
    ## Documentation
    
    For detailed documentation, please visit [PDFMathTranslate Documentation](https://pdf2zh-next.com).
    
    ## Community and Support
    
    - **FAQ**: For common questions and solutions, please refer to the [FAQ](https://pdf2zh-next.com/community/FAQ.html).
    - **Discord**: Join our [Discord community](https://discord.gg/Gm8P5gvTz8) for discussions and support.
    - **GitHub Issues**: If you encounter any issues, please submit them on [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues).
    
    ## Contributing
    
    We welcome contributions! If you are interested in contributing, please refer to our [Contribution Guide](https://pdf2zh-next.com/community/CONTRIBUTING.html).
    
    ## License
    
    This project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.
    
    ## Acknowledgments
    
    - This project is inspired by [Immersive Translate](https://immersivetranslate.com/).
    - Thanks to all contributors and users for their support and feedback.

---

### TRANSLATED TEXT

<a href="https://deepwiki.com/PDFMathTranslate/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

## PDFMathTranslate

[English](README.md) | [中文](README_zh.md) | [日本語](README_ja.md) | [한국어](README_ko.md)

`PDFMathTranslate` は、数学的な数式を含む `PDF` ファイルを任意の言語に翻訳し、元の書式と数式を保持するツールです。コマンドラインとウェブインターフェースの両方の使用方法をサポートしています。

## 特徴

- **正確な翻訳**：`PDF` ファイル内のテキストと数学的式を正確に翻訳します。
- **書式の保持**：`PDF` の元のレイアウトと書式を維持します。
- **複数の翻訳サービス**：DeepL、Google、OpenAI など、さまざまな翻訳サービスをサポートします。
- **コマンドラインとウェブインターフェース**：使いやすいコマンドラインツールとウェブインターフェースの両方を提供します。
- **バッチ処理**：複数の `PDF` ファイルのバッチ処理をサポートします。

## インストール

### pip を使用する

```bash
pip install pdf2zh
```

### Docker を使用する

```bash
docker pull nabenabe0928/pdf2zh:latest
```

その他のインストール方法については、[インストールガイド](https://pdf2zh-next.com/getting-started/INSTALLATION.html) を参照してください。

## 使い方

### コマンドライン

```bash
pdf2zh --input input.pdf --output output.pdf --to ja
```

コマンドラインオプションの詳細については、[コマンドライン使用ガイド](https://pdf2zh-next.com/getting-started/USAGE_cli.html) を参照してください。

### ウェブインターフェース

以下のコマンドでウェブインターフェースを起動します：

```bash
pdf2zh --web
```

その後、ブラウザを開き `http://localhost:7860` にアクセスしてください。

ウェブインターフェースの使用に関する詳細は、[ウェブインターフェース使用ガイド](https://pdf2zh-next.com/getting-started/USAGE_webui.html) を参照してください。

## サポート言語

`PDFMathTranslate` は、複数の言語への翻訳をサポートしています。サポートされている言語とそれに対応する言語コードのリストについては、[サポート言語](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html) ドキュメントを参照してください。

## ドキュメント

詳細なドキュメントについては、[PDFMathTranslate ドキュメント](https://pdf2zh-next.com) をご覧ください。

## コミュニティとサポート

- **よくある質問**：よくある質問と解決策については、[よくある質問](https://pdf2zh-next.com/community/FAQ.html) を参照してください。
- **Discord**：[Discord コミュニティ](https://discord.gg/Gm8P5gvTz8) に参加して、ディスカッションとサポートを受けられます。
- **GitHub Issues**：問題が発生した場合は、[GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues) に提出してください。

## 貢献

貢献を歓迎します！貢献に興味がある場合は、[貢献ガイド](https://pdf2zh-next.com/community/CONTRIBUTING.html) を参照してください。

## ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については、[LICENSE](LICENSE) ファイルを参照してください。

## 謝辞

- このプロジェクトは [Immersive Translate](https://immersivetranslate.com/) に触発されています。
- すべての貢献者とユーザーのサポートとフィードバックに感謝します。

<a href="https://trendshift.io/repositories/12424" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12424" alt="Byaidu%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

PDF 科学論文の翻訳とバイリンガル比較。

- 📊 数式、チャート、目次、注釈を保持 _([プレビュー](#プレビュー))_。
- 🌐 [複数言語](https://pdf2zh-next.com/supported_languages.html) をサポートし、多様な [翻訳サービス](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html) に対応。
- 🤖 [コマンドラインツール](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)、[インタラクティブユーザーインターフェース](https://pdf2zh-next.com/getting-started/USAGE_webui.html)、[Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) を提供。

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> このプロジェクトは [AGPL v3](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/LICENSE) ライセンスのもと「現状のまま」提供されており、プログラムの品質や性能について一切の保証はありません。**プログラムの品質や性能に関するすべてのリスクはあなたが負担します。** プログラムに欠陥が見つかった場合、必要なサービス、修理、または修正にかかる費用はすべてあなたの責任となります。
>
> メンテナーのリソースが限られているため、使用方法のサポートや問題解決のいかなる形式も提供しません。関連する Issue は直接クローズされます！（プロジェクトドキュメントを改善するプルリクエストは歓迎します。Issue テンプレートに従ったバグ報告や友好的な Issue はこの限りではありません）


貢献方法の詳細については、[貢献ガイド](https://pdf2zh-next.com/community/Contribution-Guide.html) をご覧ください。

<h2 id="updates">更新情報</h2>

- [2025 年 6 月 4 日] プロジェクト名が変更され、[PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next) に移動しました（by [@awwaawwa](https://github.com/awwaawwa)）
- [2025 年 3 月 3 日] 新しいバックエンド [BabelDOC](https://github.com/funstory-ai/BabelDOC) の実験的サポートが追加され、WebUI が実験的オプションとして利用可能になりました（by [@awwaawwa](https://github.com/awwaawwa)）
- [2025 年 2 月 22 日] リリース CI が改善され、Windows-amd64 用の exe ファイルが適切にパッケージ化されました（by [@awwaawwa](https://github.com/awwaawwa)）
- [2024 年 12 月 24 日] 翻訳ツールが [Xinference](https://github.com/xorbitsai/inference) 上のローカルモデルをサポートするようになりました（by [@imClumsyPanda](https://github.com/imClumsyPanda)）
- [2024 年 12 月 19 日] `-cp` を使用して非 PDF/A ドキュメントがサポートされるようになりました（by [@reycn](https://github.com/reycn)）
- [2024 年 12 月 13 日] バックエンドの追加サポートが提供されました（by [@YadominJinta](https://github.com/YadominJinta)）
- [2024 年 12 月 10 日] 翻訳ツールが Azure 上の OpenAI モデルをサポートするようになりました（by [@yidasanqian](https://github.com/yidasanqian)）

<h2 id="プレビュー">プレビュー</h2>

<div align="center">
<!-- <img src="./../../docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="demo">オンラインサービス 🌟</h2>

> [!NOTE]
>
> pdf2zh 2.0 は現在オンラインデモを提供していません

以下のデモのいずれかを使用して、私たちのアプリケーションをお試しいただけます：

- [Download the latest release](https://github.com/StardustSky/pdf2zh-next/releases) for offline use.

---

### OUTPUT

- [v1.x パブリック無料サービス](https://pdf2zh.com/) はインストール不要でオンライン利用可能 _(推奨)_。
- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) 無料利用枠あり。詳細はページの FAQ セクションを参照 _(推奨)_
- オフライン利用のためには [最新リリースをダウンロード](https://github.com/StardustSky/pdf2zh-next/releases)
<!-- - [Demo hosted on HuggingFace](https://huggingface.co/spaces/reycn/PDFMathTranslate-Docker)
- [Demo hosted on ModelScope](https://www.modelscope.cn/studios/AI-ModelScope/PDFMathTranslate) without installation. -->

デモの計算リソースは限られているため、乱用は避けてください。

<h2 id="インストール">インストールと使い方</h2>

### インストール

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>Windows におすすめ</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>Linux におすすめ</small>
3. [**uv** (a Python package manager)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>macOS におすすめ</small>

---

### 使い方

1. [**WebUI** の使い方](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [**Zotero プラグイン** の使い方](https://github.com/guaguastandup/zotero-pdf2zh)（サードパーティ製プログラム）
3. [**コマンドライン** の使い方](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

異なる使用ケースに対応するため、当プログラムには複数の利用方法が用意されています。詳細は [このページ](./getting-started/getting-started.md) をご覧ください。

<h2 id="使い方">高度な設定</h2>

各オプションの詳細な説明については、[高度な使い方](https://pdf2zh-next.com/advanced/advanced.html) のドキュメントで完全なリストを参照してください。

<h2 id="二次開発">二次開発（API）</h2>

> [!NOTE]
>
> 現在、関連するドキュメントは提供されていません。後日追加されますので、しばらくお待ちください。


<!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about:

- [Python API](./docs/APIS.md#api-python), how to use the program in other Python programs
- [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="langcode">言語コード</h2>

必要な言語に翻訳するためのコードがわからない場合は、[このドキュメント](https://pdf2zh-next.com/advanced/Language-Codes.html) を確認してください

<!-- 
<h2 id="todo">TODOs</h2>

- [ ] Parse layout with DocLayNet based models, [PaddleX](https://github.com/PaddlePaddle/PaddleX/blob/17cc27ac3842e7880ca4aad92358d3ef8555429a/paddlex/repo_apis/PaddleDetection_api/object_det/official_categories.py#L81), [PaperMage](https://github.com/allenai/papermage/blob/9cd4bb48cbedab45d0f7a455711438f1632abebe/README.md?plain=1#L102), [SAM2](https://github.com/facebookresearch/sam2)

- [ ] Fix page rotation, table of contents, format of lists

- [ ] Fix pixel formula in old papers

- [ ] Async retry except KeyboardInterrupt

- [ ] Knuth–Plass algorithm for western languages

- [ ] Support non-PDF/A files

- [ ] Plugins of [Zotero](https://github.com/zotero/zotero) and [Obsidian](https://github.com/obsidianmd/obsidian-releases) -->

<h2 id="謝辞">謝辞</h2>

- [Immersive Translate](https://immersivetranslate.com) は、このプロジェクトの積極的な貢献者向けに月額 Pro メンバーシップの引き換えコードを提供しています。詳細はこちら：[CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- [SiliconFlow](https://siliconflow.cn) は、大規模言語モデル（LLM）を活用した無料翻訳サービスをこのプロジェクトに提供しています。

- 1.x バージョン：[Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- バックエンド：[BabelDOC](https://github.com/funstory-ai/BabelDOC)

- PDF ライブラリ：[PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- PDF 解析：[Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- PDF プレビュー：[Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- レイアウト解析：[DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- PDF 標準：[PDF Explained](https://zxyle.github.io/PDF-Explained/)、[PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- 多言語フォント：[BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets) を参照

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Rich logging with multiprocessing](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- ドキュメントの国際化（i18n）には [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/) を使用しています


<h2 id="conduct">コードを提出する前に</h2>

pdf2zh をより良くするために、貢献者の積極的な参加を歓迎します。コードを提出する準備が整う前に、[行動規範](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) と [貢献ガイド](https://pdf2zh-next.com/community/Contribution-Guide.html) を参照してください。

<h2 id="contrib">貢献者</h2>

<a href="https://github.com/PDFMathTranslate/PDFMathTranslate-next/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a>

![Alt](https://repobeats.axiom.co/api/embed/45529651750579e099960950f757449a410477ad.svg "Repobeats analytics image")

<h2 id="star_hist">スター履歴</h2>

<a href="https://star-history.com/#PDFMathTranslate/PDFMathTranslate-next&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PDFMathTranslate/PDFMathTranslate-next&type=Date"/>
 </picture>
</a>

<div align="right"> 
<h6><small>このページの一部のコンテンツは GPT によって翻訳されており、エラーが含まれている可能性があります。</small></h6>