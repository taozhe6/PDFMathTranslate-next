<div align="center">

<img src="./docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="titre">PDFMathTranslate</h2>

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

Traduction d'articles scientifiques PDF et comparaison bilingue. Basé sur [BabelDOC](https://github.com/funstory-ai/BabelDOC). De plus, ce projet est également l'implémentation de référence officielle pour appeler BabelDOC afin d'effectuer la traduction PDF.

- 📊 Préserve les formules, les graphiques, la table des matières et les annotations _([aperçu](#aperçu))_.
- 🌐 Prend en charge [plusieurs langues](https://pdf2zh-next.com/supported_languages.html) et divers [services de traduction](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html).
- 🤖 Fournit un [outil en ligne de commande](https://pdf2zh-next.com/getting-started/USAGE_commandline.html), une [interface utilisateur interactive](https://pdf2zh-next.com/getting-started/USAGE_webui.html) et [Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html)

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> Ce projet est fourni "tel quel" sous la licence [AGPL v3](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/LICENSE), et aucune garantie n'est fournie quant à la qualité et aux performances du programme. **L'intégralité du risque concernant la qualité et les performances du programme est supportée par vous.** Si le programme s'avère défectueux, vous serez responsable de tous les coûts nécessaires de service, de réparation ou de correction.
>
> En raison de l'énergie limitée des mainteneurs, nous ne fournissons aucune forme d'assistance à l'utilisation ou de résolution de problèmes. Les problèmes liés seront fermés directement ! (Les pull requests pour améliorer la documentation du projet sont les bienvenues ; les bugs ou les problèmes amicaux qui suivent le modèle de problème ne sont pas affectés par cela)


Pour plus de détails sur la manière de contribuer, veuillez consulter le [Guide de contribution](https://pdf2zh-next.com/community/Contribution-Guide.html).

<h2 id="preview">Aperçu</h2>

<div align="center">
<!-- <img src="./docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="demo">Service en Ligne 🌟</h2>

Vous pouvez essayer notre application en utilisant l'un des services suivants :

- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) Un quota d'utilisation gratuit est disponible ; veuillez consulter la section FAQ de la page pour plus de détails.

<h2 id="install">Installation et Utilisation</h2>

### Installation

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>Recommandé pour Windows</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>Recommandé pour Linux</small>
3. [**uv** (un gestionnaire de paquets Python)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>Recommandé pour macOS</small>

---

### Utilisation

1. [Utilisation de **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [Utilisation du **Plugin Zotero**](https://github.com/guaguastandup/zotero-pdf2zh) (Programme tiers)
3. [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

Pour différents cas d'utilisation, nous fournissons des méthodes distinctes pour utiliser notre programme. Consultez [cette page](./getting-started/getting-started.md) pour plus d'informations.

<h2 id="usage">Options avancées</h2>

Pour des explications détaillées, veuillez vous référer à notre document sur [l'Utilisation avancée](https://pdf2zh-next.com/advanced/advanced.html) pour une liste complète de chaque option.

<h2 id="downstream">Développement secondaire (APIs)</h2>

<!-- <!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about: -->

- [API Python](./docs/fr/advanced/API/python.md), comment utiliser le programme dans d'autres programmes Python
<!-- - [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="langcode">Code de langue</h2>

Si vous ne savez pas quel code utiliser pour traduire dans la langue dont vous avez besoin, consultez [cette documentation](https://pdf2zh-next.com/advanced/Language-Codes.html)

<h2 id="acknowledgement">Remerciements</h2>

- [Immersive Translation](https://immersivetranslate.com) sponsorise des codes de rédemption d'abonnement Pro mensuels pour les contributeurs actifs de ce projet, voir les détails à : [CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- [SiliconFlow](https://siliconflow.cn) fournit un service de traduction gratuit pour ce projet, alimenté par de grands modèles de langage (LLM).

- Version 1.x : [Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- backend : [BabelDOC](https://github.com/funstory-ai/BabelDOC)

- Bibliothèque PDF : [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- Analyse PDF : [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- Aperçu PDF : [Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- Analyse de mise en page : [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- Normes PDF : [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- Police multilingue : voir [BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets)

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Journalisation Rich avec multiprocessing](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- Documentation i18n utilisant [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/)


<h2 id="conduite">Avant de soumettre votre code</h2>

Nous accueillons favorablement la participation active des contributeurs pour améliorer pdf2zh. Avant de soumettre votre code, veuillez consulter notre [Code de Conduite](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) et notre [Guide de Contribution](https://pdf2zh-next.com/community/Contribution-Guide.html).

<h2 id="contributeurs">Contributeurs</h2>

<!-- <a href="https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a> -->

<!-- ![Alt](https://repobeats.axiom.co/api/embed/45529651750579e099960950f757449a410477ad.svg "Repobeats analytics image") -->

<h2 id="historique_étoiles">Historique des étoiles</h2>

<a href="https://star-history.com/#PDFMathTranslate-next/PDFMathTranslate-next&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date"/>
 </picture>
</a>

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>