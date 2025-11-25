[**Options avancées**](./introduction.md) > **Documentation des services de traduction** _(actuel)_

---

### Visualisation des services de traduction disponibles via la ligne de commande

Vous pouvez confirmer les services de traduction disponibles et leur utilisation en affichant le message d'aide dans la ligne de commande.

```bash
pdf2zh_next -h
```

---

### OUTPUT

À la fin du message d'aide, vous pouvez consulter des informations détaillées sur les différents services de traduction.


---

---
#### Translation Engine Support Policy
pdf2zh provides a unified interface for various translation engines. Currently, we support:
- **Google Translate**: Free, supports most languages, but may be unstable.
- **DeepL Translate**: High accuracy, supports some languages, free version has usage limits.
- **OpenAI Translator**: High accuracy, supports most languages, requires API key.
- **Gemini Translator**: High accuracy, supports most languages, requires API key.

#### Notes on Translation Engine Usage
- You can configure multiple engines and set priorities. If one engine fails, it will automatically switch to the next one.
- If you need to use a paid service (such as DeepL Pro), please configure the API key in the settings.

#### How to Choose a Translation Engine?
- **For beginners**: It is recommended to use Google Translate or DeepL Translate (free version).
- **For professional users**: It is recommended to use DeepL Pro or OpenAI Translator for higher translation quality.
- **For developers**: All engines support API calls, and you can extend custom engines.

#### Supported Languages
Each engine supports different languages. For details, please refer to:
- [Google Translate Supported Languages](https://cloud.google.com/translate/docs/languages)
- [DeepL Translate Supported Languages](https://www.deepl.com/docs-api/translating-text/)
- [OpenAI Translator Supported Languages](https://platform.openai.com/docs/guides/text-to-speech)

#### Troubleshooting
- If translation fails, please check your network connection and API key configuration.
- If you encounter a usage limit, try switching to another engine or wait for a while before retrying.

#### Feedback and Suggestions
If you have any questions or suggestions about translation engines, please submit feedback via [GitHub Issues](https://github.com/your-repo/issues).

---

### OUTPUT LANGUAGE CODE

fr

---

### OUTPUT

### Politique de support des moteurs de traduction
---
#### Politique de support des moteurs de traduction
pdf2zh fournit une interface unifiée pour divers moteurs de traduction. Actuellement, nous supportons :
- **Google Translate** : Gratuit, supporte la plupart des langues, mais peut être instable.
- **DeepL Translate** : Haute précision, supporte certaines langues, la version gratuite a des limites d'utilisation.
- **OpenAI Translator** : Haute précision, supporte la plupart des langues, nécessite une clé API.
- **Gemini Translator** : Haute précision, supporte la plupart des langues, nécessite une clé API.

#### Notes sur l'utilisation des moteurs de traduction
- Vous pouvez configurer plusieurs moteurs et définir des priorités. Si un moteur échoue, il passera automatiquement au suivant.
- Si vous avez besoin d'utiliser un service payant (comme DeepL Pro), veuillez configurer la clé API dans les paramètres.

#### Comment choisir un moteur de traduction ?
- **Pour les débutants** : Il est recommandé d'utiliser Google Translate ou DeepL Translate (version gratuite).
- **Pour les utilisateurs professionnels** : Il est recommandé d'utiliser DeepL Pro ou OpenAI Translator pour une qualité de traduction plus élevée.
- **Pour les développeurs** : Tous les moteurs supportent les appels API, et vous pouvez étendre des moteurs personnalisés.

#### Langues supportées
Chaque moteur supporte différentes langues. Pour plus de détails, veuillez vous référer à :
- [Google Translate Langues supportées](https://cloud.google.com/translate/docs/languages)
- [DeepL Translate Langues supportées](https://www.deepl.com/docs-api/translating-text/)
- [OpenAI Translator Langues supportées](https://platform.openai.com/docs/guides/text-to-speech)

#### Dépannage
- Si la traduction échoue, veuillez vérifier votre connexion réseau et la configuration de votre clé API.
- Si vous rencontrez une limite d'utilisation, essayez de passer à un autre moteur ou attendez un peu avant de réessayer.

#### Retours et suggestions
Si vous avez des questions ou des suggestions concernant les moteurs de traduction, veuillez soumettre vos retours via [GitHub Issues](https://github.com/your-repo/issues).

---

- **English** (`en`): The primary language of the project, offering the most comprehensive documentation and support.
- **Chinese** (`zh`): The second primary language of the project, with extensive documentation and support.

#### Tier 2 (Community-Translated)
- **French** (`fr`): Community-translated documentation is available. We welcome contributions to improve it.
- **German** (`de`): Community-translated documentation is available. We welcome contributions to improve it.
- **Japanese** (`ja`): Community-translated documentation is available. We welcome contributions to improve it.
- **Korean** (`ko`): Community-translated documentation is available. We welcome contributions to improve it.
- **Russian** (`ru`): Community-translated documentation is available. We welcome contributions to improve it.
- **Spanish** (`es`): Community-translated documentation is available. We welcome contributions to improve it.

#### Tier 3 (Planned)
- **Arabic** (`ar`): Documentation translation is planned. Contributions are welcome.
- **Hindi** (`hi`): Documentation translation is planned. Contributions are welcome.
- **Portuguese** (`pt`): Documentation translation is planned. Contributions are welcome.
- **Turkish** (`tr`): Documentation translation is planned. Contributions are welcome.

---

Please translate the above text into French.

- [x] **OpenAI Translator**: An AI translation engine based on OpenAI's GPT models, offering high translation accuracy and support for multiple languages.
- [x] **DeepL Translator**: A professional translation engine known for its high-quality translations, supporting multiple languages.
- [x] **Gemini Translator**: An AI translation engine based on Google's Gemini models, providing high translation accuracy and support for multiple languages.

---

### OUTPUT

**Moteurs de traduction de niveau 1** sont directement maintenus par les mainteneurs du projet. Bien que les mainteneurs n'utilisent **pas ce projet régulièrement**, ils s'appuieront sur les problèmes GitHub pour identifier les problèmes. Lorsque l'un de ces moteurs rencontre des problèmes, les mainteneurs les corrigeront dès que possible pour garantir la stabilité et la fiabilité.

Actuellement, les moteurs de traduction de niveau 1 supportés incluent :

- [x] **OpenAI Translator** : Un moteur de traduction IA basé sur les modèles GPT d'OpenAI, offrant une haute précision de traduction et le support de plusieurs langues.
- [x] **DeepL Translator** : Un moteur de traduction professionnel connu pour ses traductions de haute qualité, supportant plusieurs langues.
- [x] **Gemini Translator** : Un moteur de traduction IA basé sur les modèles Gemini de Google, fournissant une haute précision de traduction et le support de plusieurs langues.
8. Anthropic
9. Moonshot
10. DeepL
11. Google
12. Gemini
13. Ollama
14. Azure

---

### OUTPUT

1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible
8. Anthropic
9. Moonshot
10. DeepL
11. Google
12. Gemini
13. Ollama
14. Azure

- **Chinese (Simplified)**
- **Chinese (Traditional)**
- **English**

If you wish to contribute translations for other languages, please refer to [For Translators](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

---

### OUTPUT

#### Niveau 2 (Support communautaire)
- **Chinois (Simplifié)**
- **Chinois (Traditionnel)**
- **Anglais**

Si vous souhaitez contribuer aux traductions pour d'autres langues, veuillez vous référer au [Guide de contribution des traductions](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

- **Google Translate**: Free, supports most languages, but may be unstable.
- **DeepL Translate**: High accuracy, supports some languages, free version has usage limits.
- **OpenAI Translator**: High accuracy, supports most languages, requires API key.
- **Gemini Translator**: High accuracy, supports most languages, requires API key.

---

### OUTPUT

**Les moteurs de traduction de niveau 2** sont maintenus et supportés par la communauté.  
Lorsque ces moteurs rencontrent des problèmes, les mainteneurs du projet ne fourniront pas de correctifs directs. Au lieu de cela, ils étiquetteront les problèmes liés avec `help wanted` et accueilleront les demandes de tirage des contributeurs pour aider à les résoudre.

Tous les moteurs qui sont supportés par le programme mais non explicitement listés sous le Niveau 1 sont considérés comme des moteurs de traduction de niveau 2.
- **Google Translate** : Gratuit, supporte la plupart des langues, mais peut être instable.
- **DeepL Translate** : Haute précision, supporte certaines langues, la version gratuite a des limites d'utilisation.
- **OpenAI Translator** : Haute précision, supporte la plupart des langues, nécessite une clé API.
- **Gemini Translator** : Haute précision, supporte la plupart des langues, nécessite une clé API.

---

!!! warning "Deprecated"

    These engines are no longer recommended for use, but are still kept for reference.

- [x] **Google Translate**: Google Translate is a free online service provided by Google that supports over 100 languages. However, it may not be suitable for translating specialized content such as academic papers, as it may not accurately handle complex terminology and formatting.

- [x] **Bing Translator**: Bing Translator is a free online service provided by Microsoft that supports over 70 languages. It may not be suitable for translating specialized content such as academic papers, as it may not accurately handle complex terminology and formatting.

---

### TARGET LANGUAGE CODE

fr

---

### OUTPUT

#### Moteurs dépréciés
---

!!! warning "Déprécié"

    Ces moteurs ne sont plus recommandés pour une utilisation, mais sont toujours conservés à titre de référence.

- [x] **Google Translate** : Google Translate est un service en ligne gratuit fourni par Google qui prend en charge plus de 100 langues. Cependant, il peut ne pas être adapté à la traduction de contenu spécialisé tel que des articles académiques, car il peut ne pas gérer avec précision la terminologie et le formatage complexes.

- [x] **Bing Translator** : Bing Translator est un service en ligne gratuit fourni par Microsoft qui prend en charge plus de 70 langues. Il peut ne pas être adapté à la traduction de contenu spécialisé tel que des articles académiques, car il peut ne pas gérer avec précision la terminologie et le formatage complexes.

---

- Google Translate
- Bing Translator

---

### OUTPUT

Les moteurs de traduction suivants ont été **dépréciés** et ne seront plus maintenus ou supportés :
- Google Translate
- Bing Translator

---

### ORIGINAL TEXT

**pdf2zh** is a powerful PDF translation tool designed to help users translate PDF documents between different languages. It supports multiple translation engines and provides a user-friendly interface for both command-line and web-based usage.

---

### OUTPUT

**pdf2zh** est un outil de traduction PDF puissant conçu pour aider les utilisateurs à traduire des documents PDF entre différentes langues. Il supporte plusieurs moteurs de traduction et fournit une interface conviviale pour une utilisation en ligne de commande et basée sur le web.

---

### ORIGINAL TEXT

- **Multi-engine Support**: Supports Google Translate, DeepL, OpenAI, and more.
- **Batch Translation**: Translate multiple PDF files at once.
- **Format Preservation**: Maintains the original layout and formatting of the PDF.
- **Customizable Output**: Choose output language and translation engine.
- **Open Source**: Free to use and modify under the MIT license.

---

### OUTPUT

- **Support multi-moteurs** : Supporte Google Translate, DeepL, OpenAI, et plus encore.
- **Traduction par lots** : Traduisez plusieurs fichiers PDF à la fois.
- **Préservation du format** : Maintient la mise en page et le formatage originaux du PDF.
- **Sortie personnalisable** : Choisissez la langue de sortie et le moteur de traduction.
- **Open Source** : Gratuit à utiliser et modifier sous la licence MIT.

---

### ORIGINAL TEXT

To get started with **pdf2zh**, follow these steps:

1. **Installation**: Install the tool using pip or Docker.
2. **Configuration**: Set up your preferred translation engine and API keys.
3. **Usage**: Use the command line or web interface to translate your PDFs.

For detailed instructions, see the [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) and [Usage](https://pdf2zh-next.com/getting-started/USAGE.html) guides.

---

### OUTPUT

Pour commencer avec **pdf2zh**, suivez ces étapes :

1. **Installation** : Installez l'outil en utilisant pip ou Docker.
2. **Configuration** : Configurez votre moteur de traduction préféré et vos clés API.
3. **Utilisation** : Utilisez la ligne de commande ou l'interface web pour traduire vos PDF.

Pour des instructions détaillées, consultez les guides [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) et [Utilisation](https://pdf2zh-next.com/getting-started/USAGE.html).

---

### ORIGINAL TEXT

If you encounter any issues or have questions, please check the [FAQ](https://pdf2zh-next.com/community/FAQ.html) or submit an issue on [GitHub](https://github.com/your-repo/issues).

We welcome contributions! If you'd like to help improve **pdf2zh**, see the [For Translators](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) guide.

---

### OUTPUT

Si vous rencontrez des problèmes ou avez des questions, veuillez consulter la [FAQ](https://pdf2zh-next.com/community/FAQ.html) ou soumettre un problème sur [GitHub](https://github.com/your-repo/issues).

Nous accueillons les contributions ! Si vous souhaitez aider à améliorer **pdf2zh**, consultez le guide [Guide de contribution des traductions](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

---

### ORIGINAL TEXT

- **Version**: 2.0.0
- **License**: MIT
- **Source Code**: [GitHub Repository](https://github.com/your-repo/pdf2zh)

---

### OUTPUT

- **Version** : 2.0.0
- **Licence** : MIT
- **Code Source** : [Dépôt GitHub](https://github.com/your-repo/pdf2zh)

---

### ORIGINAL TEXT

**pdf2zh** is a powerful PDF translation tool designed to help users translate PDF documents between different languages. It supports multiple translation engines and provides a user-friendly interface for both command-line and web-based usage.

---

### OUTPUT

**pdf2zh** est un outil de traduction PDF puissant conçu pour aider les utilisateurs à traduire des documents PDF entre différentes langues. Il supporte plusieurs moteurs de traduction et fournit une interface conviviale pour une utilisation en ligne de commande et basée sur le web.

---

### ORIGINAL TEXT

- **Multi-engine Support**: Supports Google Translate, DeepL, OpenAI, and more.
- **Batch Translation**: Translate multiple PDF files at once.
- **Format Preservation**: Maintains the original layout and formatting of the PDF.
- **Customizable Output**: Choose output language and translation engine.
- **Open Source**: Free to use and modify under the MIT license.

---

### OUTPUT

- **Support multi-moteurs** : Supporte Google Translate, DeepL, OpenAI, et plus encore.
- **Traduction par lots** : Traduisez plusieurs fichiers PDF à la fois.
- **Préservation du format** : Maintient la mise en page et le formatage originaux du PDF.
- **Sortie personnalisable** : Choisissez la langue de sortie et le moteur de traduction.
- **Open Source** : Gratuit à utiliser et modifier sous la licence MIT.

---

### ORIGINAL TEXT

To get started with **pdf2zh**, follow these steps:

1. **Installation**: Install the tool using pip or Docker.
2. **Configuration**: Set up your preferred translation engine and API keys.
3. **Usage**: Use the command line or web interface to translate your PDFs.

For detailed instructions, see the [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) and [Usage](https://pdf2zh-next.com/getting-started/USAGE.html) guides.

---

### OUTPUT

Pour commencer avec **pdf2zh**, suivez ces étapes :

1. **Installation** : Installez l'outil en utilisant pip ou Docker.
2. **Configuration** : Configurez votre moteur de traduction préféré et vos clés API.
3. **Utilisation** : Utilisez la ligne de commande ou l'interface web pour traduire vos PDF.

Pour des instructions détaillées, consultez les guides [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) et [Utilisation](https://pdf2zh-next.com/getting-started/USAGE.html).

---

### ORIGINAL TEXT

If you encounter any issues or have questions, please check the [FAQ](https://pdf2zh-next.com/community/FAQ.html) or submit an issue on [GitHub](https://github.com/your-repo/issues).

We welcome contributions! If you'd like to help improve **pdf2zh**, see the [For Translators](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) guide.

---

### OUTPUT

Si vous rencontrez des problèmes ou avez des questions, veuillez consulter la [FAQ](https://pdf2zh-next.com/community/FAQ.html) ou soumettre un problème sur [GitHub](https://github.com/your-repo/issues).

Nous accueillons les contributions ! Si vous souhaitez aider à améliorer **pdf2zh**, consultez le guide [Guide de contribution des traductions](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

---

### ORIGINAL TEXT

- **Version**: 2.0.0
- **License**: MIT
- **Source Code**: [GitHub Repository](https://github.com/your-repo/pdf2zh)

---

### OUTPUT

- **Version** : 2.0.0
- **Licence** : MIT
- **Code Source** : [Dépôt GitHub](https://github.com/your-repo/pdf2zh)

---

### ORIGINAL TEXT

# pdf2zh Documentation

Welcome to the **pdf2zh** documentation! This guide will help you get started with using **pdf2zh** to translate PDF documents.

## Table of Contents

- [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html)
- [Usage](https://pdf2zh-next.com/getting-started/USAGE.html)
- [Advanced](https://pdf2zh-next.com/advanced/ADVANCED.html)
- [Supported Languages](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html)
- [Community](https://pdf2zh-next.com/community/COMMUNITY.html)
- [FAQ](https://pdf2zh-next.com/community/FAQ.html)

## Overview

**pdf2zh** is a powerful PDF translation tool designed to help users translate PDF documents between different languages. It supports multiple translation engines and provides a user-friendly interface for both command-line and web-based usage.

### Key Features

- **Multi-engine Support**: Supports Google Translate, DeepL, OpenAI, and more.
- **Batch Translation**: Translate multiple PDF files at once.
- **Format Preservation**: Maintains the original layout and formatting of the PDF.
- **Customizable Output**: Choose output language and translation engine.
- **Open Source**: Free to use and modify under the MIT license.

## Quick Start

To get started with **pdf2zh**, follow these steps:

1. **Installation**: Install the tool using pip or Docker.
2. **Configuration**: Set up your preferred translation engine and API keys.
3. **Usage**: Use the command line or web interface to translate your PDFs.

For detailed instructions, see the [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) and [Usage](https://pdf2zh-next.com/getting-started/USAGE.html) guides.

## Support

If you encounter any issues or have questions, please check the [FAQ](https://pdf2zh-next.com/community/FAQ.html) or submit an issue on [GitHub](https://github.com/your-repo/issues).

We welcome contributions! If you'd like to help improve **pdf2zh**, see the [For Translators](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) guide.

---

**Version**: 2.0.0  
**License**: MIT  
**Source Code**: [GitHub Repository](https://github.com/your-repo/pdf2zh)

---

### OUTPUT

# Documentation de pdf2zh

Bienvenue dans la documentation de **pdf2zh** ! Ce guide vous aidera à commencer à utiliser **pdf2zh** pour traduire des documents PDF.

## Table des matières

- [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html)
- [Utilisation](https://pdf2zh-next.com/getting-started/USAGE.html)
- [Options avancées](https://pdf2zh-next.com/advanced/ADVANCED.html)
- [Langues supportées](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html)
- [Communauté](https://pdf2zh-next.com/community/COMMUNITY.html)
- [FAQ](https://pdf2zh-next.com/community/FAQ.html)

## Aperçu

**pdf2zh** est un outil de traduction PDF puissant conçu pour aider les utilisateurs à traduire des documents PDF entre différentes langues. Il supporte plusieurs moteurs de traduction et fournit une interface conviviale pour une utilisation en ligne de commande et basée sur le web.

### Fonctionnalités clés

- **Support multi-moteurs** : Supporte Google Translate, DeepL, OpenAI, et plus encore.
- **Traduction par lots** : Traduisez plusieurs fichiers PDF à la fois.
- **Préservation du format** : Maintient la mise en page et le formatage originaux du PDF.
- **Sortie personnalisable** : Choisissez la langue de sortie et le moteur de traduction.
- **Open Source** : Gratuit à utiliser et modifier sous la licence MIT.

## Démarrage rapide

Pour commencer avec **pdf2zh**, suivez ces étapes :

1. **Installation** : Installez l'outil en utilisant pip ou Docker.
2. **Configuration** : Configurez votre moteur de traduction préféré et vos clés API.
3. **Utilisation** : Utilisez la ligne de commande ou l'interface web pour traduire vos PDF.

Pour des instructions détaillées, consultez les guides [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) et [Utilisation](https://pdf2zh-next.com/getting-started/USAGE.html).

## Support

Si vous rencontrez des problèmes ou avez des questions, veuillez consulter la [FAQ](https://pdf2zh-next.com/community/FAQ.html) ou soumettre un problème sur [GitHub](https://github.com/your-repo/issues).

Nous accueillons les contributions ! Si vous souhaitez aider à améliorer **pdf2zh**, consultez le guide [Guide de contribution des traductions](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

---

**Version** : 2.0.0  
**Licence** : MIT  
**Code Source** : [Dépôt GitHub](https://github.com/your-repo/pdf2zh)

---

3. OpenAI
4. DeepL
5. Gemini
6. Claude
7. Cohere

---

### OUTPUT

1. Bing
2. Google
3. OpenAI
4. DeepL
5. Gemini
6. Claude
7. Cohere

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>