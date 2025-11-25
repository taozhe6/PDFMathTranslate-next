<div align="center">

<img src="./docs/images/banner.png" width="320px"  alt="banner"/>

<h2 id="заголовок">PDFMathTranslate</h2>

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
    <a href="https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next"><img src="https://deepwiki.com/badge.svg" alt="Спроси DeepWiki"></a>
</p>

<a href="https://trendshift.io/repositories/12424" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12424" alt="Byaidu%2FPDFMathTranslate | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

Перевод научных статей в формате PDF и двуязычное сравнение. Основано на [BabelDOC](https://github.com/funstory-ai/BabelDOC). Кроме того, этот проект также является официальной эталонной реализацией для вызова BabelDOC для выполнения перевода PDF.

- 📊 Сохранение формул, диаграмм, оглавления и аннотаций _([предварительный просмотр](#предварительный-просмотр))_.
- 🌐 Поддержка [множества языков](https://pdf2zh-next.com/supported_languages.html) и разнообразных [служб перевода](https://pdf2zh-next.com/advanced/Documentation-of-Translation-Services.html).
- 🤖 Предоставляет [инструмент командной строки](https://pdf2zh-next.com/getting-started/USAGE_commandline.html), [интерактивный пользовательский интерфейс](https://pdf2zh-next.com/getting-started/USAGE_webui.html) и [Docker](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html)

<!-- Feel free to provide feedback in [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues) or [Telegram Group](https://t.me/+Z9_SgnxmsmA5NzBl). -->

> [!WARNING]
>
> Этот проект предоставляется «как есть» по лицензии [AGPL v3](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/LICENSE), и никаких гарантий относительно качества и производительности программы не предоставляется. **Весь риск, связанный с качеством и производительностью программы, лежит на вас.** Если программа окажется дефектной, вы будете нести ответственность за все необходимые расходы на обслуживание, ремонт или исправление.
>
> В связи с ограниченными ресурсами сопровождающих мы не предоставляем никакой помощи в использовании или решении проблем. Соответствующие вопросы будут закрыты напрямую! (Приветствуются пул-реквесты для улучшения документации проекта; на ошибки или дружелюбные вопросы, следующие шаблону вопроса, это не распространяется)


Для получения подробной информации о том, как внести свой вклад, обратитесь к [Руководству по внесению вклада](https://pdf2zh-next.com/community/Contribution-Guide.html).

<h2 id="предпросмотр">Предпросмотр</h2>

<div align="center">
<!-- <img src="./docs/images/preview.gif" width="80%"  alt="preview"/> -->
<img src="https://s.immersivetranslate.com/assets/r2-uploads/images/babeldoc-preview.png" width="80%"/>
</div>

<h2 id="демо">Онлайн-сервис 🌟</h2>

Вы можете опробовать наше приложение, используя любой из следующих сервисов:

- [Immersive Translate - BabelDOC](https://app.immersivetranslate.com/babel-doc/) Доступна бесплатная квота использования; подробности смотрите в разделе FAQ на странице.

<h2 id="установка">Установка и использование</h2>

### Установка

1. [**Windows EXE**](https://pdf2zh-next.com/getting-started/INSTALLATION_winexe.html) <small>Рекомендуется для Windows</small>
2. [**Docker**](https://pdf2zh-next.com/getting-started/INSTALLATION_docker.html) <small>Рекомендуется для Linux</small>
3. [**uv** (менеджер пакетов Python)](https://pdf2zh-next.com/getting-started/INSTALLATION_uv.html) <small>Рекомендуется для macOS</small>

---

### Использование

1. [Использование **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
2. [Использование **Плагина Zotero**](https://github.com/guaguastandup/zotero-pdf2zh) (Сторонняя программа)
3. [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_commandline.html)

Для различных случаев использования мы предоставляем различные методы работы с нашей программой. Подробнее смотрите на [этой странице](./getting-started/getting-started.md).

<h2 id="usage">Расширенные параметры</h2>

Подробные объяснения смотрите в нашем документе о [Расширенном использовании](https://pdf2zh-next.com/advanced/advanced.html) для получения полного списка каждой опции.

<h2 id="downstream">Вторичная разработка (API)</h2>

<!-- <!-- For downstream applications, please refer to our document about [API Details](./docs/APIS.md) for futher information about: -->

- [Python API](./docs/ru/advanced/API/python.md), как использовать программу в других программах на Python
<!-- - [HTTP API](./docs/APIS.md#api-http), how to communicate with a server with the program installed -->

<h2 id="кодязыка">Код языка</h2>

Если вы не знаете, какой код использовать для перевода на нужный вам язык, ознакомьтесь с [этой документацией](https://pdf2zh-next.com/advanced/Language-Codes.html)

<h2 id="благодарности">Благодарности</h2>

- [Immersive Translation](https://immersivetranslate.com) спонсирует ежемесячные коды для активации Pro-подписки для активных участников этого проекта, подробности см. в: [CONTRIBUTOR_REWARD.md](https://github.com/funstory-ai/BabelDOC/blob/main/docs/CONTRIBUTOR_REWARD.md)

- [SiliconFlow](https://siliconflow.cn) предоставляет бесплатный сервис перевода для этого проекта, работающий на основе больших языковых моделей (LLM).

- Версия 1.x: [Byaidu/PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)


- Бэкенд: [BabelDOC](https://github.com/funstory-ai/BabelDOC)

- Библиотека для работы с PDF: [PyMuPDF](https://github.com/pymupdf/PyMuPDF)

- Парсинг PDF: [Pdfminer.six](https://github.com/pdfminer/pdfminer.six)

- Предпросмотр PDF: [Gradio PDF](https://github.com/freddyaboulton/gradio-pdf)

- Анализ макета: [DocLayout-YOLO](https://github.com/opendatalab/DocLayout-YOLO)

- Стандарты PDF: [PDF Explained](https://zxyle.github.io/PDF-Explained/), [PDF Cheat Sheets](https://pdfa.org/resource/pdf-cheat-sheets/)

- Многоязычные шрифты: см. [BabelDOC-Assets](https://github.com/funstory-ai/BabelDOC-Assets)

- [Asynchronize](https://github.com/multimeric/Asynchronize/tree/master?tab=readme-ov-file)

- [Расширенное логирование с использованием многопроцессорности](https://github.com/SebastianGrans/Rich-multiprocess-logging/tree/main)

- Интернационализация документации с использованием [Weblate](https://hosted.weblate.org/projects/pdfmathtranslate-next/)


<h2 id="conduct">Перед отправкой кода</h2>

Мы приветствуем активное участие участников, чтобы сделать pdf2zh лучше. Прежде чем вы будете готовы отправить свой код, пожалуйста, ознакомьтесь с нашим [Кодексом поведения](https://pdf2zh-next.com/community/CODE_OF_CONDUCT.html) и [Руководством по внесению вклада](https://pdf2zh-next.com/community/Contribution-Guide.html).

<h2 id="contrib">Участники</h2>

<!-- <a href="https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/graphs/contributors">
  <img src="https://opencollective.com/PDFMathTranslate/contributors.svg?width=890&button=false" />
</a> -->

<!-- ![Alt](https://repobeats.axiom.co/api/embed/45529651750579e099960950f757449a410477ad.svg "Repobeats analytics image") -->

<h2 id="star_hist">История звезд</h2>

<a href="https://star-history.com/#PDFMathTranslate-next/PDFMathTranslate-next&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=PDFMathTranslate-next/PDFMathTranslate-next&type=Date"/>
 </picture>
</a>

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>