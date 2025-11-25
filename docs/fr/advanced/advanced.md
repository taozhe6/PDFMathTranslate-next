[**Options avancées**](./introduction.md) > **Options avancées** _(actuel)_

---

<h3 id="toc">Table des matières</h3>

- [Arguments de ligne de commande](#arguments-de-ligne-de-commande)
- [Guide de configuration de la limitation de débit](#guide-de-configuration-de-la-limitation-de-débit)
- [Traduction partielle](#traduction-partielle)
- [Spécifier les langues source et cible](#spécifier-les-langues-source-et-cible)
- [Traduire avec exceptions](#traduire-avec-exceptions)
- [Invite personnalisée](#invite-personnalisée)
- [Configuration personnalisée](#configuration-personnalisée)
- [Ignorer le nettoyage](#ignorer-le-nettoyage)
- [Cache de traduction](#cache-de-traduction)
- [Déploiement en tant que services publics](#déploiement-en-tant-que-services-publics)
- [Authentification et page d'accueil](#authentification-et-page-daccueil)
- [Support de glossaire](#support-de-glossaire)

---

#### Arguments de ligne de commande

Exécutez la commande de traduction dans la ligne de commande pour générer le document traduit `example-mono.pdf` et le document bilingue `example-dual.pdf` dans le répertoire de travail actuel. Utilisez Google comme service de traduction par défaut. Plus de services de traduction supportés peuvent être trouvés [HERE](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

Dans le tableau suivant, nous listons toutes les options avancées pour référence :

##### Arguments

| `output-dir`                    | Output directory for translated PDFs                                                    | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `-l`, `--target-language`       | Target language for translation                                                         | `pdf2zh_next example.pdf -l fr`                                                                                       |
| `-o`, `--output-filename`       | Output filename for the translated PDF                                                  | `pdf2zh_next example.pdf -o translated.pdf`                                                                           |
| `-s`, `--source-language`       | Source language of the PDF (optional)                                                   | `pdf2zh_next example.pdf -s en`                                                                                       |
| `--ocr`                         | Enable OCR for text extraction                                                          | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-language`                | Specify OCR language (requires `--ocr`)                                                 | `pdf2zh_next example.pdf --ocr --ocr-language en`                                                                     |
| `--translate-with`              | Choose translation engine (`google`, `google-cloud`, `openai`, `azure`, `deepl`)        | `pdf2zh_next example.pdf --translate-with openai`                                                                     |
| `--openai-api-key`              | OpenAI API key (requires `--translate-with openai`)                                     | `pdf2zh_next example.pdf --translate-with openai --openai-api-key YOUR_KEY`                                           |
| `--openai-model`                | OpenAI model to use (requires `--translate-with openai`)                                | `pdf2zh_next example.pdf --translate-with openai --openai-model gpt-4`                                                |
| `--azure-key`                   | Azure Translator key (requires `--translate-with azure`)                                | `pdf2zh_next example.pdf --translate-with azure --azure-key YOUR_KEY`                                                 |
| `--azure-region`                | Azure region (requires `--translate-with azure`)                                        | `pdf2zh_next example.pdf --translate-with azure --azure-region eastus`                                                |
| `--deepl-auth-key`              | DeepL authentication key (requires `--translate-with deepl`)                            | `pdf2zh_next example.pdf --translate-with deepl --deepl-auth-key YOUR_KEY`                                            |
| `--google-cloud-credentials`    | Google Cloud credentials JSON file (requires `--translate-with google-cloud`)           | `pdf2zh_next example.pdf --translate-with google-cloud --google-cloud-credentials credentials.json`                   |
| `-c`, `--config-file`           | Path to a configuration file                                                            | `pdf2zh_next example.pdf -c config.json`                                                                              |
| `-v`, `--verbose`               | Enable verbose output                                                                   | `pdf2zh_next example.pdf -v`                                                                                          |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Show help message                                                                       | `pdf2zh_next -h`                                                                                                      |

---

### TRANSLATION

| Option                          | Fonction                                                                               | Exemple                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Fichiers PDF en entrée à traiter                                                         | `pdf2zh_next example.pdf`                                                                                             |
| `output-dir`                    | Répertoire de sortie pour les PDF traduits                                               | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `-l`, `--target-language`       | Langue cible pour la traduction                                                          | `pdf2zh_next example.pdf -l fr`                                                                                       |
| `-o`, `--output-filename`       | Nom de fichier de sortie pour le PDF traduit                                             | `pdf2zh_next example.pdf -o translated.pdf`                                                                           |
| `-s`, `--source-language`       | Langue source du PDF (optionnel)                                                        | `pdf2zh_next example.pdf -s en`                                                                                       |
| `--ocr`                         | Activer l'OCR pour l'extraction de texte                                                 | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-language`                | Spécifier la langue de l'OCR (nécessite `--ocr`)                                         | `pdf2zh_next example.pdf --ocr --ocr-language en`                                                                     |
| `--translate-with`              | Choisir le moteur de traduction (`google`, `google-cloud`, `openai`, `azure`, `deepl`)    | `pdf2zh_next example.pdf --translate-with openai`                                                                     |
| `--openai-api-key`              | Clé API OpenAI (nécessite `--translate-with openai`)                                    | `pdf2zh_next example.pdf --translate-with openai --openai-api-key YOUR_KEY`                                           |
| `--openai-model`                | Modèle OpenAI à utiliser (nécessite `--translate-with openai`)                          | `pdf2zh_next example.pdf --translate-with openai --openai-model gpt-4`                                                |
| `--azure-key`                   | Clé Azure Translator (nécessite `--translate-with azure`)                               | `pdf2zh_next example.pdf --translate-with azure --azure-key YOUR_KEY`                                                 |
| `--azure-region`                | Région Azure (nécessite `--translate-with azure`)                                       | `pdf2zh_next example.pdf --translate-with azure --azure-region eastus`                                                |
| `--deepl-auth-key`              | Clé d'authentification DeepL (nécessite `--translate-with deepl`)                       | `pdf2zh_next example.pdf --translate-with deepl --deepl-auth-key YOUR_KEY`                                            |
| `--google-cloud-credentials`    | Fichier d'identification Google Cloud JSON (nécessite `--translate-with google-cloud`)  | `pdf2zh_next example.pdf --translate-with google-cloud --google-cloud-credentials credentials.json`                   |
| `-c`, `--config-file`           | Chemin vers un fichier de configuration                                                 | `pdf2zh_next example.pdf -c config.json`                                                                              |
| `-v`, `--verbose`               | Activer la sortie détaillée                                                              | `pdf2zh_next example.pdf -v`                                                                                          |
| `--version`                     | Afficher les informations de version                                                    | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Afficher le message d'aide                                                               | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--target-lang`                 | Target language code (default: `zh-CN`)                                                 | `pdf2zh_next example.pdf --target-lang en-US`                                                                         |
| `--source-lang`                 | Source language code (default: `auto`)                                                  | `pdf2zh_next example.pdf --source-lang en-US`                                                                         |
| `--translator`                  | Translator service (default: `google`)                                                  | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-api-key`          | API key for the translator service                                                      | `pdf2zh_next example.pdf --translator deepl --translator-api-key your_deepl_api_key`                                  |
| `--translator-api-url`          | API URL for the translator service                                                      | `pdf2zh_next example.pdf --translator deepl --translator-api-url https://api-free.deepl.com/v2/translate`             |
| `--translator-api-region`       | API region for the translator service                                                   | `pdf2zh_next example.pdf --translator azure --translator-api-region eastus`                                           |
| `--translator-api-model`        | API model for the translator service                                                    | `pdf2zh_next example.pdf --translator openai --translator-api-model gpt-4o`                                           |
| `--translator-api-timeout`      | Timeout in seconds for the translator service (default: 60)                             | `pdf2zh_next example.pdf --translator-api-timeout 120`                                                                |
| `--translator-concurrency-limit`| Concurrency limit for the translator service (default: 10)                              | `pdf2zh_next example.pdf --translator-concurrency-limit 5`                                                            |
| `--translator-request-limit`    | Request limit for the translator service (default: 50)                                  | `pdf2zh_next example.pdf --translator-request-limit 100`                                                              |
| `--translator-request-interval` | Request interval in milliseconds for the translator service (default: 1000)             | `pdf2zh_next example.pdf --translator-request-interval 2000`                                                          |
| `--translator-retry-attempts`   | Retry attempts for the translator service (default: 3)                                  | `pdf2zh_next example.pdf --translator-retry-attempts 5`                                                               |
| `--translator-retry-delay`      | Retry delay in milliseconds for the translator service (default: 1000)                  | `pdf2zh_next example.pdf --translator-retry-delay 2000`                                                               |
| `--translator-save-json`        | Whether to save the translator's response JSON (default: `false`)                       | `pdf2zh_next example.pdf --translator-save-json true`                                                                 |
| `--translator-save-json-path`   | Path to save the translator's response JSON (default: same as output directory)         | `pdf2zh_next example.pdf --translator-save-json true --translator-save-json-path /jsonpath`                           |
| `--translator-proxy`            | Proxy for the translator service                                                        | `pdf2zh_next example.pdf --translator-proxy http://127.0.0.1:7890`                                                    |
| `--translator-proxy-auth`       | Proxy authentication for the translator service                                         | `pdf2zh_next example.pdf --translator-proxy http://127.0.0.1:7890 --translator-proxy-auth username:password`          |
| `--translator-proxy-timeout`    | Proxy timeout in seconds for the translator service (default: 60)                       | `pdf2zh_next example.pdf --translator-proxy-timeout 120`                                                              |
| `--translator-proxy-retry`      | Proxy retry attempts for the translator service (default: 3)                            | `pdf2zh_next example.pdf --translator-proxy-retry 5`                                                                  |
| `--translator-proxy-retry-delay`| Proxy retry delay in milliseconds for the translator service (default: 1000)            | `pdf2zh_next example.pdf --translator-proxy-retry-delay 2000`                                                         |
| `--translator-proxy-save-json`  | Whether to save the proxy's response JSON (default: `false`)                            | `pdf2zh_next example.pdf --translator-proxy-save-json true`                                                           |
| `--translator-proxy-save-json-path` | Path to save the proxy's response JSON (default: same as output directory)          | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-path /jsonpath`               |
| `--translator-proxy-save-json-format` | Format to save the proxy's response JSON (default: `json`)                          | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-format json`                  |
| `--translator-proxy-save-json-indent` | Indent for the proxy's response JSON (default: 2)                                   | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-indent 4`                     |
| `--translator-proxy-save-json-encoding` | Encoding for the proxy's response JSON (default: `utf-8`)                         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-encoding utf-8`               |
| `--translator-proxy-save-json-ensure-ascii` | Whether to ensure ASCII for the proxy's response JSON (default: `false`)         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-ensure-ascii true`            |
| `--translator-proxy-save-json-sort-keys` | Whether to sort keys for the proxy's response JSON (default: `false`)             | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-sort-keys true`               |
| `--translator-proxy-save-json-allow-nan` | Whether to allow NaN for the proxy's response JSON (default: `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-allow-nan true`               |
| `--translator-proxy-save-json-skipkeys` | Whether to skip keys for the proxy's response JSON (default: `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-skipkeys true`                |
| `--translator-proxy-save-json-default` | Default value for the proxy's response JSON (default: `None`)                     | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-default null`                 |
| `--translator-proxy-save-json-check-circular` | Whether to check circular references for the proxy's response JSON (default: `true`) | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-check-circular false`         |
| `--translator-proxy-save-json-separators` | Separators for the proxy's response JSON (default: `(',', ': ')`)                 | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-separators (',', ': ')`       |
| `--translator-proxy-save-json-indent` | Indent for the proxy's response JSON (default: 2)                                   | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-indent 4`                     |
| `--translator-proxy-save-json-encoding` | Encoding for the proxy's response JSON (default: `utf-8`)                         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-encoding utf-8`               |
| `--translator-proxy-save-json-ensure-ascii` | Whether to ensure ASCII for the proxy's response JSON (default: `false`)         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-ensure-ascii true`            |
| `--translator-proxy-save-json-sort-keys` | Whether to sort keys for the proxy's response JSON (default: `false`)             | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-sort-keys true`               |
| `--translator-proxy-save-json-allow-nan` | Whether to allow NaN for the proxy's response JSON (default: `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-allow-nan true`               |
| `--translator-proxy-save-json-skipkeys` | Whether to skip keys for the proxy's response JSON (default: `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-skipkeys true`                |
| `--translator-proxy-save-json-default` | Default value for the proxy's response JSON (default: `None`)                     | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-default null`                 |
| `--translator-proxy-save-json-check-circular` | Whether to check circular references for the proxy's response JSON (default: `true`) | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-check-circular false`         |
| `--translator-proxy 极-save-json-separators` | Separators for the proxy's response JSON (default: `(',', ': ')`)                 | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-separators (',', ': ')`       |

---

### OUTPUT

| `--output`                      | Répertoire de sortie pour les fichiers                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--target-lang`                 | Code de langue cible (par défaut : `zh-CN`)                                                         | `pdf2zh_next example.pdf --target-lang en-US`                                                                         |
| `--source-lang`                 | Code de langue source (par défaut : `auto`)                                                         | `pdf2zh_next example.pdf --source-lang en-US`                                                                         |
| `--translator`                  | Service de traduction (par défaut : `google`)                                                       | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-api-key`          | Clé API pour le service de traduction                                                               | `pdf2zh_next example.pdf --translator deepl --translator-api-key your_deepl_api_key`                                  |
| `--translator-api-url`          | URL de l'API pour le service de traduction                                                          | `pdf2zh_next example.pdf --translator deepl --translator-api-url https://api-free.deepl.com/v2/translate`             |
| `--translator-api-region`       | Région de l'API pour le service de traduction                                                       | `pdf2zh_next example.pdf --translator azure --translator-api-region eastus`                                           |
| `--translator-api-model`        | Modèle de l'API pour le service de traduction                                                       | `pdf2zh_next example.pdf --translator openai --translator-api-model gpt-4o`                                           |
| `--translator-api-timeout`      | Délai d'attente en secondes pour le service de traduction (par défaut : 60)                         | `pdf 极 zh_next example.pdf --translator-api-timeout 120`                                                                |
| `--translator-concurrency-limit`| Limite de concurrence pour le service de traduction (par défaut : 10)                              | `pdf2zh_next example.pdf --translator-concurrency-limit 5`                                                            |
| `--translator-request-limit`    | Limite de requêtes pour le service de traduction (par défaut : 50)                                  | `pdf2zh_next example.pdf --translator-request 极 limit 100`                                                              |
| `--translator-request-interval` | Intervalle de requête en millisecondes pour le service de traduction (par défaut : 1000)             | `pdf2zh_next example.pdf --translator-request-interval 2000`                                                          |
| `--translator-retry-attempts`   | Tentatives de réessai pour le service de traduction (par défaut : 3)                                  | `pdf2zh_next example.pdf --translator-retry-attempts 5`                                                               |
| `--translator-retry-del 极`      | Délai de réessai en millisecondes pour le service de traduction (par défaut : 1000)                  | `pdf2zh_next example.pdf --translator-retry-delay 2000`                                                               |
| `--translator-save-json`        | Indique s'il faut enregistrer le JSON de réponse du traducteur (par défaut : `false`)                       | `pdf2zh_next example.pdf --translator-save-json true`                                                                 |
| `--translator-save-json-path`   | Chemin pour enregistrer le JSON de réponse du traducteur (par défaut : même que le répertoire de sortie)         | `pdf2zh_next example.pdf --translator-save-json true --translator-save-json-path /jsonpath`                           |
| `--translator-proxy`            | Proxy pour le service de traduction                                                        | `pdf2zh_next example.pdf --translator-proxy http://127.0.0.1:7890`                                                    |
| `--translator-proxy-auth`       | Authentification du proxy pour le service de traduction                                         | `pdf2zh_next example.pdf --translator-proxy http://127.0.0.1:7890 --translator-proxy-auth username:password`          |
| `--translator-proxy-timeout`    | Délai d'attente du proxy en secondes pour le service de traduction (par défaut : 60)                       | `pdf2zh_next example.pdf --translator-proxy-timeout 120`                                                              |
| `--translator-proxy-retry`      | Tentatives de réessai du proxy pour le service de traduction (par défault : 3)                            | `pdf2zh_next example.pdf --translator-proxy-retry 5`                                                                  |
| `--translator-proxy-retry-delay`| Délai de réessai du proxy en millisecondes pour le service de traduction (par défaut : 1000)            | `pdf2zh_next example.pdf --translator-proxy-retry-delay 2000`                                                         |
| `--translator-proxy-save-json`  | Indique s'il faut enregistrer le JSON de réponse du proxy (par défaut : `false`)                            | `pdf2zh_next example.pdf --translator-proxy-save-json true`                                                           |
| `--translator-proxy-save-json-path` | Chemin pour enregistrer le JSON de réponse du proxy (par défaut : même que le répertoire de sortie)          | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy 极 save-json-path /jsonpath`               |
| `--translator-proxy-save-json-format` | Format pour enregistrer le JSON de réponse du proxy (par défaut : `json`)                          | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-format json`                  |
| `--translator-proxy-save-json-indent` | Indentation pour le JSON de réponse du proxy (par défaut : 2)                                   | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-indent 4`                     |
| `--translator-proxy-save-json-encoding` | Encodage pour le JSON de réponse du proxy (par défaut : `utf-8`)                         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-encoding utf-8`               |
| `--translator-proxy-save-json-ensure-ascii` | Indique s'il faut garantir l'ASCII pour le JSON de réponse du proxy (par défaut : `false`)         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-ensure-ascii true`            |
| `--translator-proxy-save-json-sort-keys` | Indique s'il faut trier les clés pour le JSON de réponse du proxy (par défaut : `false`)             | `pdf2zh_next example.pdf --translator-proxy-save-极 json true --translator-proxy-save-json-sort-keys true`               |
| `--translator-proxy-save-json-allow-nan` | Indique s'il faut autoriser NaN pour le JSON de réponse du proxy (par défaut : `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-allow-nan true`               |
| `--translator-proxy-save-json-skipkeys` | Indique s'il faut ignorer les clés pour le JSON de réponse du proxy (par défaut : `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-skipkeys true`                |
| `--translator-proxy-save-json-default` | Valeur par défaut pour le JSON de réponse du proxy (par défaut : `None`)                     | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-default null`                 |
| `--translator-proxy-save-json-check-circular` | Indique s'il faut vérifier les références circulaires pour le JSON de réponse du proxy (par défaut : `true`) | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-check-circular false`         |
| `--translator-proxy-save-json-separators` | Séparateurs pour le JSON de réponse du proxy (par défaut : `(',', ': ')`)                 | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-separators (',', ': ')`       |
| `--translator-proxy-save-json-indent` | Indentation pour le JSON de réponse du proxy (par défaut : 2)                                   | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-indent 4`                     |
| `--translator-proxy-save-json-encoding` | Encodage pour le JSON de réponse du proxy (par défaut : `utf-8`)                         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-encoding utf-8 极`               |
| `--translator-proxy-save-json-ensure-ascii` | Indique s'il faut garantir l'ASCII pour le JSON de réponse du proxy (par défaut : `false`)         | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-ensure-ascii true`            |
| `--translator-proxy-save-json-s 极 ort-keys` | Indique s'il faut trier les clés pour le JSON de réponse du proxy (par défaut : `false`)             | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-sort-keys true`               |
| `--translator-proxy-save-json-allow-nan` | Indique s'il faut autoriser NaN pour le JSON de réponse du proxy (par défaut : `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-pro 极 xy-save-json-allow-nan 极 true`               |
| `--translator-proxy-save-json-skipkeys` | Indique s'il faut ignorer les clés pour le JSON de réponse du proxy (par défaut : `false`)              | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-skipkeys true`                |
| `--translator-proxy-save-json-default` | Valeur par défaut pour le JSON de réponse du proxy (par défaut : `None`)                     | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-default null`                 |
| `--translator-proxy-save-json-check-circular` | Indique s'il faut vérifier les références circulaires pour le JSON de réponse du proxy (par défaut : `true`) | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-check-circular false`         |
| `--translator-proxy-save-json-separators` | Séparateurs pour le JSON de réponse du proxy (par défaut : `(',', ': ')`)                 | `pdf2zh_next example.pdf --translator-proxy-save-json true --translator-proxy-save-json-separators (',', ': ')`       |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-<Config>`         | Set [**service config**](./Documentation-of-Translation-Services.md)                   | `pdf2zh_next example.pdf --openai-api-key <your api key>`<br>`pdf2zh_next example.pdf --openai-base-url <your base url>` |
| `--cache-dir <path>`            | Set cache directory for translation results                                            | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--no-cache`                    | Disable cache for translation results                                                  | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--target-lang <language code>` | Set target language, default is `zh`                                                   | `pdf2zh_next example.pdf --target-lang en`                                                                            |

---

### OUTPUT

| `--<Services>`                  | Utiliser un [**service spécifique**](./Documentation-of-Translation-Services.md) pour la traduction | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-<Config>`         | Définir la [**configuration du service**](./Documentation-of-Translation-Services.md)               | `pdf2zh_next example.pdf --openai-api-key <your api key>`<br>`pdf2zh_next example.pdf --openai-base-url <your base url>` |
| `--cache-dir <path>`            | Définir le répertoire de cache pour les résultats de traduction                                     | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--no-cache`                    | Désactiver le cache pour les résultats de traduction                                                | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--target-lang <language code>` | Définir la langue cible, par défaut `zh`                                                            | `pdf2zh_next example.pdf --target-lang en`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | Specify input file or directory                                                         | `pdf2zh_next -i input.pdf`<br>`pdf2zh_next -i ./input_dir`                                                             |
| `--output`, `-o`                | Specify output directory (default: `./output`)                                          | `pdf2zh_next -i input.pdf -o ./output_dir`                                                                            |
| `--target-lang`, `-t`           | Specify target language code (default: `zh`)                                           | `pdf2zh_next -i input.pdf -t ja`                                                                                      |
| `--source-lang`, `-s`           | Specify source language code (default: `auto`)                                          | `pdf2zh_next -i input.pdf -s en`                                                                                      |
| `--translator`, `-tr`           | Specify translator service (default: `google`)                                          | `pdf2zh_next -i input.pdf -tr deepl`                                                                                  |
| `--translator-key`, `-trk`      | Specify translator service API key                                                       | `pdf2zh_next -i input.pdf -tr deepl -trk YOUR_DEEPL_API_KEY`                                                          |
| `--translator-url`, `-tru`      | Specify translator service API URL (for self-hosted services)                           | `pdf2zh_next -i input.pdf -tr openai -tru https://api.openai.com/v1`                                                   |
| `--translator-model`, `-trm`    | Specify translator model (for services that support multiple models)                     | `pdf2zh_next -i input.pdf -tr openai -trm gpt-4`                                                                      |
| `--force`, `-f`                 | Force overwrite existing output files                                                   | `pdf2zh_next -i input.pdf -f`                                                                                         |
| `--verbose`, `-vb`              | Enable verbose output                                                                   | `pdf2zh_next -i input.pdf -vb`                                                                                        |
| `--config`, `-c`                | Specify configuration file path                                                         | `pdf2zh_next -c config.json`                                                                                          |
| `--list-languages`, `-ll`       | List all supported languages                                                            | `pdf2zh_next -ll`                                                                                                     |
| `--list-translators`, `-lt`     | List all supported translator services                                                  | `pdf2zh_next -lt`                                                                                                     |
| `--check-update`, `-cu`         | Check for updates                                                                       | `pdf2zh_next -cu`                                                                                                     |
| `--max-concurrency`, `-mc`      | Maximum number of concurrent translation tasks (default: `5`)                            | `pdf2zh_next -i input.pdf -mc 10`                                                                                     |
| `--timeout`, `-to`              | Timeout for translation requests in seconds (default: `30`)                             | `pdf2zh_next -i input.pdf -to 60`                                                                                     |
| `--retry`, `-r`                 | Number of retries for failed translation requests (default: `3`)                         | `pdf2zh_next -i input.pdf -r 5`                                                                                       |
| `--no-cache`, `-nc`             | Disable translation cache                                                               | `pdf2zh_next -i input.pdf -nc`                                                                                        |
| `--cache-dir`, `-cd`            | Specify cache directory (default: `./cache`)                                             | `pdf2zh_next -i input.pdf -cd ./my_cache`                                                                             |
| `--log-level`, `-l`             | Set log level (`debug`, `info`, `warning`, `error`, `critical`)                          | `pdf2zh_next -i input.pdf -l debug`                                                                                   |
| `--log-file`, `-lf`             | Specify log file path                                                                   | `pdf2zh_next -i input.pdf -lf ./app.log`                                                                              |
| `--dry-run`, `-dr`              | Perform a dry run without actual translation                                            | `pdf2zh_next -i input.pdf -dr`                                                                                        |
| `--batch-size`, `-bs`           | Batch size for processing multiple files (default: `10`)                                | `pdf2zh_next -i ./input_dir -bs 20`                                                                                   |
| `--exclude`, `-e`               | Exclude files matching pattern                                                          | `pdf2zh_next -i ./input_dir -e "*.tmp"`                                                                               |
| `--include`, `-in`              | Include only files matching pattern                                                     | `pdf2zh_next -i ./input_dir -in "*.pdf"`                                                                              |
| `--preserve-layout`, `-pl`      | Preserve original layout as much as possible                                            | `pdf2zh_next -i input.pdf -pl`                                                                                        |
| `--ocr`, `-oc`                  | Enable OCR for scanned PDFs                                                             | `pdf2zh_next -i scanned.pdf -oc`                                                                                      |
| `--ocr-lang`, `-ocl`            | Specify OCR language (default: `auto`)                                                  | `pdf2zh_next -i scanned.pdf -oc -ocl en`                                                                              |
| `--ocr-engine`, `-oce`          | Specify OCR engine (`tesseract`, `easyocr`, default: `tesseract`)                       | `pdf2zh_next -i scanned.pdf -oc -oce easyocr`                                                                         |
| `--format`, `-fmt`              | Output format (`pdf`, `markdown`, `text`, `html`, default: `pdf`)                       | `pdf2zh_next -i input.pdf -fmt markdown`                                                                              |
| `--watermark`, `-wm`            | Add watermark to output PDF                                                             | `pdf2zh_next -i input.pdf -wm "Translated by pdf2zh"`                                                                 |
| `--quality`, `-q`               | Output PDF quality (`low`, `medium`, `high`, default: `medium`)                         | `pdf2zh_next -i input.pdf -q high`                                                                                    |
| `--dpi`, `-d`                   | Output DPI for images (default: `300`)                                                 | `pdf2zh_next -i input.pdf -d 600`                                                                                     |
| `--page-range`, `-pr`           | Specify page range to translate (e.g., `1-5,8,10-15`)                                   | `pdf2zh_next -i input.pdf -pr 1-5,10`                                                                                 |
| `--skip-translated`, `-st`      | Skip pages that have already been translated                                            | `pdf2zh_next -i input.pdf -st`                                                                                        |
| `--resume`, `-rs`               | Resume from last interrupted translation                                                | `pdf2zh_next -i input.pdf -rs`                                                                                        |
| `--cleanup`, `-cl`              | Cleanup temporary files after processing                                                | `pdf2zh_next -i input.pdf -cl`                                                                                        |
| `--no-cleanup`, `-ncl`          | Do not cleanup temporary files                                                          | `pdf2zh_next -i input.pdf -ncl`                                                                                       |
| `--help-translators`, `-ht`     | Show help for translator services                                                       | `pdf2zh_next -ht`                                                                                                     |
| `--help-languages`, `-hl`       | Show help for language codes                                                            | `pdf2zh_next -hl`                                                                                                     |
| `--help-ocr`, `-ho`             | Show help for OCR options                                                               | `pdf2zh_next -ho`                                                                                                     |

---

### OUTPUT

| `--help`, `-h`                  | Afficher le message d'aide et quitter                                                              | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Afficher la version et quitter                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | Spécifier le fichier ou le répertoire d'entrée                                                         | `pdf2zh_next -i input.pdf`<br>`pdf2zh_next -i ./input_dir`                                                             |
| `--output`, `-o`                | Spécifier le répertoire de sortie (par défaut : `./output`)                                          | `pdf2zh_next -i input.pdf -o ./output_dir`                                                                            |
| `--target-lang`, `-t`           | Spécifier le code de langue cible (par défaut : `zh`)                                           | `pdf2zh_next -i input.pdf -t ja`                                                                                      |
| `--source-lang`, `-s`           | Spécifier le code de langue source (par défaut : `auto`)                                          | `pdf2zh_next -i input.pdf -s en`                                                                                      |
| `--translator`, `-tr`           | Spécifier le service de traduction (par défaut : `google`)                                          | `pdf2zh_next -i input.pdf -tr deepl`                                                                                  |
| `--translator-key`, `-trk`      | Spécifier la clé API du service de traduction                                                       | `pdf2zh_next -i input.pdf -tr deepl -trk YOUR_DEEPL_API_KEY`                                                          |
| `--translator-url`, `-tru`      | Spécifier l'URL de l'API du service de traduction (pour les services auto-hébergés)                           | `pdf2zh_next -i input.pdf -tr openai -tru https://api.openai.com/v1`                                                   |
| `--translator-model`, `-trm`    | Spécifier le modèle de traduction (pour les services prenant en charge plusieurs modèles)                     | `pdf2zh_next -i input.pdf -tr openai -trm gpt-4`                                                                      |
| `--force`, `-f`                 | Forcer l'écrasement des fichiers de sortie existants                                                   | `pdf2zh_next -i input.pdf -f`                                                                                         |
| `--verbose`, `-vb`              | Activer la sortie détaillée                                                                   | `pdf2zh_next -i input.pdf -vb`                                                                                        |
| `--config`, `-c`                | Spécifier le chemin du fichier de configuration                                                         | `pdf2zh_next -c config.json`                                                                                          |
| `--list-languages`, `-ll`       | Lister toutes les langues supportées                                                            | `pdf2zh_next -ll`                                                                                                     |
| `--list-translators`, `-lt`     | Lister tous les services de traduction supportés                                                  | `pdf2zh_next -lt`                                                                                                     |
| `--check-update`, `-cu`         | Vérifier les mises à jour                                                                       | `pdf2zh_next -cu`                                                                                                     |
| `--max-concurrency`, `-mc`      | Nombre maximum de tâches de traduction simultanées (par défaut : `5`)                            | `pdf2zh_next -i input.pdf -mc 10`                                                                                     |
| `--timeout`, `-to`              | Délai d'attente pour les requêtes de traduction en secondes (par défaut : `30`)                             | `pdf2zh_next -i input.pdf -to 60`                                                                                     |
| `--retry`, `-r`                 | Nombre de tentatives pour les requêtes de traduction échouées (par défaut : `3`)                         | `pdf2zh_next -i input.pdf -r 5`                                                                                       |
| `--no-cache`, `-nc`             | Désactiver le cache de traduction                                                               | `pdf2zh_next -i input.pdf -nc`                                                                                        |
| `--cache-dir`, `-cd`            | Spécifier le répertoire de cache (par défaut : `./cache`)                                             | `pdf2zh_next -i input.pdf -cd ./my_cache`                                                                             |
| `--log-level`, `-l`             | Définir le niveau de journalisation (`debug`, `info`, `warning`, `error`, `critical`)                          | `pdf2zh_next -i input.pdf -l debug`                                                                                   |
| `--log-file`, `-lf`             | Spécifier le chemin du fichier de journal                                                                   | `pdf2zh_next -i input.pdf -lf ./app.log`                                                                              |
| `--dry-run`, `-dr`              | Effectuer une simulation sans traduction réelle                                            | `pdf2zh_next -i input.pdf -dr`                                                                                        |
| `--batch-size`, `-bs`           | Taille des lots pour le traitement de plusieurs fichiers (par défaut : `10`)                                | `pdf2zh_next -i ./input_dir -bs 20`                                                                                   |
| `--exclude`, `-e`               | Exclure les fichiers correspondant au modèle                                                          | `pdf2zh_next -i ./input_dir -e "*.tmp"`                                                                               |
| `--include`, `-in`              | Inclure uniquement les fichiers correspondant au modèle                                                     | `pdf2zh_next -i ./input_dir -in "*.pdf"`                                                                              |
| `--preserve-layout`, `-pl`      | Préserver la mise en page originale autant que possible                                            | `pdf2zh_next -i input.pdf -pl`                                                                                        |
| `--ocr`, `-oc`                  | Activer la ROC pour les PDF scannés                                                             | `pdf2zh_next -i scanned.pdf -oc`                                                                                      |
| `--ocr-lang`, `-ocl`            | Spécifier la langue de la ROC (par défaut : `auto`)                                                  | `pdf2zh_next -i scanned.pdf -oc -ocl en`                                                                              |
| `--ocr-engine`, `-oce`          | Spécifier le moteur de ROC (`tesseract`, `easyocr`, par défaut : `tesseract`)                       | `pdf2zh_next -i scanned.pdf -oc -oce easyocr`                                                                         |
| `--format`, `-fmt`              | Format de sortie (`pdf`, `markdown`, `text`, `html`, par défaut : `pdf`)                       | `pdf2zh_next -i input.pdf -fmt markdown`                                                                              |
| `--watermark`, `-wm`            | Ajouter un filigrane au PDF de sortie                                                             | `pdf2zh_next -i input.pdf -wm "Translated by pdf2zh"`                                                                 |
| `--quality`, `-q`               | Qualité du PDF de sortie (`low`, `medium`, `high`, par défaut : `medium`)                         | `pdf2zh_next -i input.pdf -q high`                                                                                    |
| `--dpi`, `-d`                   | DPI de sortie pour les images (par défaut : `300`)                                                 | `pdf2zh_next -i input.pdf -d 600`                                                                                     |
| `--page-range`, `-pr`           | Spécifier la plage de pages à traduire (par exemple, `1-5,8,10-15`)                                   | `pdf2zh_next -i input.pdf -pr 1-5,10`                                                                                 |
| `--skip-translated`, `-st`      | Ignorer les pages déjà traduites                                            | `pdf2zh_next -i input.pdf -st`                                                                                        |
| `--resume`, `-rs`               | Reprendre à partir de la dernière traduction interrompue                                                | `pdf2zh_next -i input.pdf -rs`                                                                                        |
| `--cleanup`, `-cl`              | Nettoyer les fichiers temporaires après le traitement                                                | `pdf2zh_next -i input.pdf -cl`                                                                                        |
| `--no-cleanup`, `-ncl`          | Ne pas nettoyer les fichiers temporaires                                                          | `pdf2zh_next -i input.pdf -ncl`                                                                                       |
| `--help-translators`, `-ht`     | Afficher l'aide pour les services de traduction                                                       | `pdf2zh_next -ht`                                                                                                     |
| `--help-languages`, `-hl`       | Afficher l'aide pour les codes de langue                                                            | `pdf2zh_next -hl`                                                                                                     |
| `--help-ocr`, `-ho`             | Afficher l'aide pour les options de ROC                                                               | `pdf2zh_next -ho`                                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--config-file`                 | Chemin vers le fichier de configuration                                                | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| `--lang-source`                 | Source language code                                                                    | `pdf2zh_next --lang-source en`                                                                                        |
| `--lang-target`                 | Target language code                                                                    | `pdf2zh_next --lang-target fr`                                                                                        |
| `--output-dir`                  | Output directory                                                                        | `pdf2zh_next --output-dir /path/to/output/dir`                                                                        |
| `--output-format`               | Output format, `pdf` or `html`                                                          | `pdf2zh_next --output-format html`                                                                                     |
| `--output-prefix`               | Prefix for the output filename                                                          | `pdf2zh_next --output-prefix "translated_"`                                                                            |
| `--output-suffix`               | Suffix for the output filename                                                          | `pdf2zh_next --output-suffix "_fr"`                                                                                    |
| `--api-key`                     | API key for translation service                                                         | `pdf2zh_next --api-key "your-api-key"`                                                                                 |
| `--api-base`                    | API base URL for translation service                                                    | `pdf2zh_next --api-base "https://api.example.com"`                                                                     |
| `--api-model`                   | API model for translation service                                                        | `pdf2zh_next --api-model "gpt-4"`                                                                                      |
| `--api-temperature`             | API temperature for translation service                                                 | `pdf2zh_next --api-temperature 0.7`                                                                                    |
| `--api-max-tokens`              | API max tokens for translation service                                                  | `pdf2zh_next --api-max-tokens 2000`                                                                                    |
| `--retry-attempts`              | Number of retry attempts for API calls                                                  | `pdf2zh_next --retry-attempts 3`                                                                                       |
| `--retry-delay`                 | Delay between retry attempts in milliseconds                                            | `pdf2zh_next --retry-delay 1000`                                                                                       |
| `--timeout`                     | Timeout for API calls in milliseconds                                                   | `pdf2zh_next --timeout 30000`                                                                                          |
| `--concurrency`                 | Number of concurrent API requests                                                       | `pdf2zh_next --concurrency 5`                                                                                          |
| `--batch-size`                  | Number of text segments to process in each API request                                  | `pdf2zh_next --batch-size 10`                                                                                          |
| `--log-level`                   | Log level, `debug`, `info`, `warning`, `error`, or `critical`                           | `pdf2zh_next --log-level info`                                                                                         |
| `--log-file`                    | Path to the log file                                                                    | `pdf2zh_next --log-file /path/to/log/file.log`                                                                         |
| `--cache-dir`                   | Directory for caching translations                                                      | `pdf2zh_next --cache-dir /path/to/cache/dir`                                                                           |
| `--no-cache`                    | Disable caching                                                                         | `pdf2zh_next --no-cache`                                                                                               |
| `--force-retranslate`           | Force retranslation even if cached                                                      | `pdf2zh_next --force-retranslate`                                                                                      |
| `--dry-run`                     | Perform a dry run without actual translation                                            | `pdf2zh_next --dry-run`                                                                                                |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                   |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                |

---

### TRANSLATION RESULT

| `--config-file`                 | Chemin vers le fichier de configuration                                                | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-source`                 | Code de langue source                                                                    | `pdf2zh_next --lang-source en`                                                                                        |
| `--lang-target`                 | Code de langue cible                                                                    | `pdf2zh_next --lang-target fr`                                                                                        |
| `--output-dir`                  | Répertoire de sortie                                                                        | `pdf2zh_next --output-dir /path/to/output/dir`                                                                        |
| `--output-format`               | Format de sortie, `pdf` ou `html`                                                          | `pdf2zh_next --output-format html`                                                                                     |
| `--output-prefix`               | Préfixe pour le nom de fichier de sortie                                                          | `pdf2zh_next --output-prefix "translated_"`                                                                            |
| `--output-suffix`               | Suffixe pour le nom de fichier de sortie                                                          | `pdf2zh_next --output-suffix "_fr"`                                                                                    |
| `--api-key`                     | Clé API pour le service de traduction                                                         | `pdf2zh_next --api-key "your-api-key"`                                                                                 |
| `--api-base`                    | URL de base de l'API pour le service de traduction                                                    | `pdf2zh_next --api-base "https://api.example.com"`                                                                     |
| `--api-model`                   | Modèle d'API pour le service de traduction                                                        | `pdf2zh_next --api-model "gpt-4"`                                                                                      |
| `--api-temperature`             | Température de l'API pour le service de traduction                                                 | `pdf2zh_next --api-temperature 0.7`                                                                                    |
| `--api-max-tokens`              | Nombre maximum de jetons de l'API pour le service de traduction                                                  | `pdf2zh_next --api-max-tokens 2000`                                                                                    |
| `--retry-attempts`              | Nombre de tentatives de réessai pour les appels API                                                  | `pdf2zh_next --retry-attempts 3`                                                                                       |
| `--retry-delay`                 | Délai entre les tentatives de réessai en millisecondes                                            | `pdf2zh_next --retry-delay 1000`                                                                                       |
| `--timeout`                     | Délai d'expiration pour les appels API en millisecondes                                                   | `pdf2zh_next --timeout 30000`                                                                                          |
| `--concurrency`                 | Nombre de requêtes API concurrentes                                                       | `pdf2zh_next --concurrency 5`                                                                                          |
| `--batch-size`                  | Nombre de segments de texte à traiter dans chaque requête API                                  | `pdf2zh_next --batch-size 10`                                                                                          |
| `--log-level`                   | Niveau de journalisation, `debug`, `info`, `warning`, `error`, ou `critical`                           | `pdf2zh_next --log-level info`                                                                                         |
| `--log-file`                    | Chemin vers le fichier de journalisation                                                                    | `pdf2zh_next --log-file /path/to/log/file.log`                                                                         |
| `--cache-dir`                   | Répertoire pour la mise en cache des traductions                                                      | `pdf2zh_next --cache-dir /path/to/cache/dir`                                                                           |
| `--no-cache`                    | Désactiver la mise en cache                                                                         | `pdf2zh_next --no-cache`                                                                                               |
| `--force-retranslate`           | Forcer la retraduction même si mise en cache                                                      | `pdf2zh_next --force-retranslate`                                                                                      |
| `--dry-run`                     | Effectuer une simulation sans traduction réelle                                            | `pdf2zh_next --dry-run`                                                                                                |
| `--help`                        | Afficher le message d'aide                                                                       | `pdf2zh_next --help`                                                                                                   |
| `--version`                     | Afficher les informations de version                                                                | `pdf2zh_next --version`                                                                                                |
`5`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `--concurrency`                 | Number of concurrent translation tasks                                                  | `pdf2zh_next example.pdf --concurrency 5`                                                                             | `5`                                                              |
| `--gpt-request-interval`        | Interval in seconds between requests to GPT API                                         | `pdf2zh_next example.pdf --gpt-request-interval 5`                                                                    | `5`                                                              |
| `--rate-limit`                  | Rate limit for translation requests (requests per minute)                               | `pdf2zh_next example.pdf --rate-limit 60`                                                                             | `60`                                                             |
| `--max-retries`                 | Maximum number of retries for failed translation requests                               | `pdf2zh_next example.pdf --max-retries 5`                                                                             | `5`                                                              |
| `--timeout`                     | Timeout in seconds for each translation request                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                | `30`                                                             |
| `--ignore-errors`               | Continue processing even if translation errors occur                                    | `pdf2zh_next example.pdf --ignore-errors`                                                                             | `false`                                                          |
| `--retry-wait`                  | Wait time in seconds before retrying a failed request                                   | `pdf2zh_next example.pdf --retry-wait 5`                                                                              | `5`                                                              |
| `--batch-size`                  | Number of text segments to process in each batch                                        | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `10`                                                             |
| `--max-requests`                | Maximum number of requests to make (for testing)                                        | `pdf2zh_next example.pdf --max-requests 100`                                                                          | `100`                                                            |
| `--dry-run`                     | Simulate the process without making actual API calls                                    | `pdf2zh_next example.pdf --dry-run`                                                                                   | `false`                                                          |
| `--resume`                      | Resume from the last checkpoint                                                         | `pdf2zh_next example.pdf --resume`                                                                                    | `false`                                                          |
| `--checkpoint-interval`         | Interval in seconds for saving checkpoints                                              | `pdf2zh_next example.pdf --checkpoint-interval 300`                                                                   | `300`                                                            |
| `--log-level`                   | Log level (debug, info, warning, error, critical)                                       | `pdf2zh_next example.pdf --log-level info`                                                                            | `info`                                                           |
| `--log-file`                    | File path to save logs                                                                  | `pdf2zh_next example.pdf --log-file output.log`                                                                       | `output.log`                                                     |
| `--quiet`                       | Suppress all output except errors                                                       | `pdf2zh_next example.pdf --quiet`                                                                                     | `false`                                                          |
| `--version`                     | Show version information and exit                                                       | `pdf2zh_next --version`                                                                                               | `false`                                                          |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  | `false`                                                          |

---

### TRANSLATION RESULT

| `--report-interval`             | Intervalle de rapport de progression en secondes                                        | `pdf2zh_next example.pdf --report-interval 5`                                                                         | `5`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `--concurrency`                 | Nombre de tâches de traduction simultanées                                              | `pdf2zh_next example.pdf --concurrency 5`                                                                             | `5`                                                              |
| `--gpt-request-interval`        | Intervalle en secondes entre les requêtes à l'API GPT                                   | `pdf2zh_next example.pdf --gpt-request-interval 5`                                                                    | `5`                                                              |
| `--rate-limit`                  | Limite de débit pour les requêtes de traduction (requêtes par minute)                   | `pdf2zh_next example.pdf --rate-limit 60`                                                                             | `60`                                                             |
| `--max-retries`                 | Nombre maximum de tentatives pour les requêtes de traduction échouées                   | `pdf2zh_next example.pdf --max-retries 5`                                                                             | `5`                                                              |
| `--timeout`                     | Délai d'attente en secondes pour chaque requête de traduction                           | `pdf2zh_next example.pdf --timeout 30`                                                                                | `30`                                                             |
| `--ignore-errors`               | Continuer le traitement même si des erreurs de traduction se produisent                 | `pdf2zh_next example.pdf --ignore-errors`                                                                             | `false`                                                          |
| `--retry-wait`                  | Temps d'attente en secondes avant de réessayer une requête échouée                      | `pdf2zh_next example.pdf --retry-wait 5`                                                                              | `5`                                                              |
| `--batch-size`                  | Nombre de segments de texte à traiter dans chaque lot                                   | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `10`                                                             |
| `--max-requests`                | Nombre maximum de requêtes à effectuer (pour les tests)                                 | `pdf2zh_next example.pdf --max-requests 100`                                                                          | `100`                                                            |
| `--dry-run`                     | Simuler le processus sans effectuer d'appels API réels                                  | `pdf2zh_next example.pdf --dry-run`                                                                                   | `false`                                                          |
| `--resume`                      | Reprendre à partir du dernier point de contrôle                                         | `pdf2zh_next example.pdf --resume`                                                                                    | `false`                                                          |
| `--checkpoint-interval`         | Intervalle en secondes pour enregistrer les points de contrôle                          | `pdf2zh_next example.pdf --checkpoint-interval 300`                                                                   | `300`                                                            |
| `--log-level`                   | Niveau de journalisation (debug, info, warning, error, critical)                        | `pdf2zh_next example.pdf --log-level info`                                                                            | `info`                                                           |
| `--log-file`                    | Chemin du fichier pour enregistrer les journaux                                         | `pdf2zh_next example.pdf --log-file output.log`                                                                       | `output.log`                                                     |
| `--quiet`                       | Supprimer toute sortie sauf les erreurs                                                 | `pdf2zh_next example.pdf --quiet`                                                                                     | `false`                                                          |
| `--version`                     | Afficher les informations de version et quitter                                         | `pdf2zh_next --version`                                                                                               | `false`                                                          |
| `--help`                        | Afficher le message d'aide et quitter                                                   | `pdf2zh_next --help`                                                                                                  | `false`                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-ocr`                 | Disable OCR                                                                             | `pdf2zh_next example.pdf --disable-ocr`                                                                               |
| `--disable-translate`           | Disable Translate                                                                       | `pdf2zh_next example.pdf --disable-translate`                                                                         |
| `--dry-run`                     | Run without generating files                                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--force-rebuild`               | Force rebuild all pages                                                                 | `pdf2zh_next example.pdf --force-rebuild`                                                                             |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |
| `--language <language_code>`    | Set target language, default is `zh`                                                    | `pdf2zh_next example.pdf --language ja`                                                                               |
| `--log-level <level>`           | Set log level, default is `info`                                                        | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--max-workers <num>`           | Set max workers for OCR and translate, default is `8`                                   | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--only-ocr`                    | Only OCR, skip translate                                                                | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-translate`              | Only translate, skip OCR                                                                | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--output <path>`               | Set output path                                                                         | `pdf2zh_next example.pdf --output ./output/`                                                                          |
| `--page-range <start> [<end>]`  | Set page range to process, e.g. `1-5` or `1,3,5-7`                                      | `pdf2zh_next example.pdf --page-range 1-5` <br> `pdf2zh_next example.pdf --page-range 1,3,5-7`                         |
| `--proxy <proxy_url>`           | Set proxy for requests                                                                  | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--rebuild-failed`              | Rebuild failed pages                                                                    | `pdf2zh_next example.pdf --rebuild-failed`                                                                            |
| `--rebuild-page <page_number>`  | Rebuild specific page                                                                   | `pdf2zh_next example.pdf --rebuild-page 1`                                                                            |
| `--service <service_name>`      | Set translation service, default is `google`                                            | `pdf2zh_next example.pdf --service deepl`                                                                             |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               |

---

### TRANSLATION

| `--debug`                       | Utiliser le niveau de journalisation de débogage                                        | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-ocr`                 | Désactiver l'OCR                                                                        | `pdf2zh_next example.pdf --disable-ocr`                                                                               |
| `--disable-translate`           | Désactiver la traduction                                                                | `pdf2zh_next example.pdf --disable-translate`                                                                         |
| `--dry-run`                     | Exécuter sans générer de fichiers                                                       | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--force-rebuild`               | Forcer la reconstruction de toutes les pages                                            | `pdf2zh_next example.pdf --force-rebuild`                                                                             |
| `--help`                        | Afficher le message d'aide et quitter                                                   | `pdf2zh_next --help`                                                                                                  |
| `--language <language_code>`    | Définir la langue cible, par défaut `zh`                                                | `pdf2zh_next example.pdf --language ja`                                                                               |
| `--log-level <level>`           | Définir le niveau de journalisation, par défaut `info`                                  | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--max-workers <num>`           | Définir le nombre maximum de workers pour l'OCR et la traduction, par défaut `8`        | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--no-cache`                    | Désactiver le cache                                                                     | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--only-ocr`                    | Uniquement l'OCR, ignorer la traduction                                                 | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-translate`              | Uniquement la traduction, ignorer l'OCR                                                 | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--output <path>`               | Définir le chemin de sortie                                                             | `pdf2zh_next example.pdf --output ./output/`                                                                          |
| `--page-range <start> [<end>]`  | Définir la plage de pages à traiter, par ex. `1-5` ou `1,3,5-7`                         | `pdf2zh_next example.pdf --page-range 1-5` <br> `pdf2zh_next example.pdf --page-range 1,3,5-7`                         |
| `--proxy <proxy_url>`           | Définir le proxy pour les requêtes                                                      | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--rebuild-failed`              | Reconstruire les pages échouées                                                         | `pdf2zh_next example.pdf --rebuild-failed`                                                                            |
| `--rebuild-page <page_number>`  | Reconstruire une page spécifique                                                        | `pdf2zh_next example.pdf --rebuild-page 1`                                                                            |
| `--service <service_name>`      | Définir le service de traduction, par défaut `google`                                   | `pdf2zh_next example.pdf --service deepl`                                                                             |
| `--version`                     | Afficher la version et quitter                                                          | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--webui`                       | Interact with WebUI                                                                     | `pdf2zh_next --webui`                                                                                                 |
| `--webui-port`                  | Set the port for WebUI (default: 8000)                                                  | `pdf2zh_next --webui --webui-port 8080`                                                                               |
| `--webui-host`                  | Set the host for WebUI (default: localhost)                                             | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                            |
| `--webui-no-browser`            | Do not open the browser automatically when starting WebUI                               | `pdf2zh_next --webui --webui-no-browser`                                                                              |
| `--webui-queue-concurrency`     | Set the concurrency of the WebUI queue (default: 1)                                     | `pdf2zh_next --webui --webui-queue-concurrency 2`                                                                     |
| `--webui-queue-timeout`         | Set the timeout of the WebUI queue (default: 300)                                       | `pdf2zh_next --webui --webui-queue-timeout 600`                                                                       |
| `--webui-queue-max-size`        | Set the max size of the WebUI queue (default: 100)                                      | `pdf2zh_next --webui --webui-queue-max-size 200`                                                                      |
| `--webui-queue-ttl`             | Set the TTL of the WebUI queue (default: 300)                                           | `pdf2zh_next --webui --webui-queue-ttl 600`                                                                           |

---

### TRANSLATED TEXT

| `--gui`                         | Interagir avec l'interface graphique (GUI)                                              | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--webui`                       | Interagir avec l'interface Web (WebUI)                                                  | `pdf2zh_next --webui`                                                                                                 |
| `--webui-port`                  | Définir le port pour WebUI (par défaut : 8000)                                          | `pdf2zh_next --webui --webui-port 8080`                                                                               |
| `--webui-host`                  | Définir l'hôte pour WebUI (par défaut : localhost)                                      | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                            |
| `--webui-no-browser`            | Ne pas ouvrir automatiquement le navigateur au démarrage de WebUI                       | `pdf2zh_next --webui --webui-no-browser`                                                                              |
| `--webui-queue-concurrency`     | Définir le niveau de concurrence de la file d'attente WebUI (par défaut : 1)            | `pdf2zh_next --webui --webui-queue-concurrency 2`                                                                     |
| `--webui-queue-timeout`         | Définir le délai d'expiration de la file d'attente WebUI (par défaut : 300)             | `pdf2zh_next --webui --webui-queue-timeout 600`                                                                       |
| `--webui-queue-max-size`        | Définir la taille maximale de la file d'attente WebUI (par défaut : 100)                | `pdf2zh_next --webui --webui-queue-max-size 200`                                                                      |
| `--webui-queue-ttl`             | Définir le TTL (durée de vie) de la file d'attente WebUI (par défaut : 300)             | `pdf2zh_next --webui --webui-queue-ttl 600`                                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--download-only`               | Only download required assets then exit                                                 | `pdf2zh_next example.pdf --download-only`                                                                             |
| `--verify-only`                 | Only verify required assets then exit                                                   | `pdf2zh_next example.pdf --verify-only`                                                                               |
| `--download-models`             | Download required models before processing                                              | `pdf2zh_next example.pdf --download-models`                                                                           |
| `--force-download`              | Force download assets even if they exist                                                | `pdf2zh_next example.pdf --force-download`                                                                            |
| `--model-dir <path>`            | Specify model directory, default is `~/.pdf2zh/models`                                  | `pdf2zh_next example.pdf --model-dir ./my_models`                                                                     |
| `--cache-dir <path>`            | Specify cache directory, default is `~/.pdf2zh/cache`                                   | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--output <path>`               | Specify output file path, default is `{original_filename}_translated.{original_format}` | `pdf2zh_next example.pdf --output ./output/translated.pdf`                                                            |
| `--format <format>`             | Output format, default is same as input, support `pdf` and `docx`                       | `pdf2zh_next example.pdf --format docx`                                                                               |
| `--target-language <lang_code>` | Target language code, default is `zh`                                                   | `pdf2zh_next example.pdf --target-language ja`                                                                        |
| `--source-language <lang_code>` | Source language code, default is `auto`                                                 | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--translator <translator>`     | Specify translator, default is `google`                                                 | `pdf2zh_next example.pdf --translator deeplx`                                                                         |
| `--translator-args <json>`      | Arguments for translator, in JSON format                                                | `pdf2zh_next example.pdf --translator-args '{"api_key": "your_api_key"}'`                                             |
| `--ocr <ocr>`                   | Specify OCR engine, default is `paddle`                                                 | `pdf2zh_next example.pdf --ocr easyocr`                                                                               |
| `--ocr-args <json>`             | Arguments for OCR engine, in JSON format                                                | `pdf2zh_next example.pdf --ocr-args '{"lang": ["en", "zh"]}'`                                                         |
| `--concurrency <number>`        | Number of concurrent tasks, default is `4`                                              | `pdf2zh_next example.pdf --concurrency 8`                                                                             |
| `--timeout <seconds>`           | Timeout for each task in seconds, default is `30`                                       | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry <number>`              | Number of retries for failed tasks, default is `3`                                      | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--log-level <level>`           | Log level, default is `info`, support `debug`, `info`, `warning`, `error`               | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file <path>`             | Log file path, default is `stdout`                                                      | `pdf2zh_next example.pdf --log-file ./logs/translation.log`                                                           |
| `--config <path>`               | Configuration file path                                                                 | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `--dry-run`                     | Dry run without actual processing                                                       | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help and exit                                                                      | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATED TEXT

| `--warmup`                      | Télécharge et vérifie uniquement les ressources requises puis quitte                                                               | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--download-only`               | Télécharge uniquement les ressources requises puis quitte                                                                          | `pdf2zh_next example.pdf --download-only`                                                                             |
| `--verify-only`                 | Vérifie uniquement les ressources requises puis quitte                                                                             | `pdf2zh_next example.pdf --verify-only`                                                                               |
| `--download-models`             | Télécharge les modèles requis avant le traitement                                                                                  | `pdf2zh_next example.pdf --download-models`                                                                           |
| `--force-download`              | Force le téléchargement des ressources même si elles existent                                                                      | `pdf2zh_next example.pdf --force-download`                                                                            |
| `--model-dir <path>`            | Spécifie le répertoire des modèles, par défaut `~/.pdf2zh/models`                                                                  | `pdf2zh_next example.pdf --model-dir ./my_models`                                                                     |
| `--cache-dir <path>`            | Spécifie le répertoire de cache, par défaut `~/.pdf2zh/cache`                                                                      | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--output <path>`               | Spécifie le chemin du fichier de sortie, par défaut `{original_filename}_translated.{original_format}`                              | `pdf2zh_next example.pdf --output ./output/translated.pdf`                                                            |
| `--format <format>`             | Format de sortie, par défaut identique à l'entrée, supporte `pdf` et `docx`                                                        | `pdf2zh_next example.pdf --format docx`                                                                               |
| `--target-language <lang_code>` | Code de langue cible, par défaut `zh`                                                                                              | `pdf2zh_next example.pdf --target-language ja`                                                                        |
| `--source-language <lang_code>` | Code de langue source, par défaut `auto`                                                                                           | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--translator <translator>`     | Spécifie le traducteur, par défaut `google`                                                                                        | `pdf2zh_next example.pdf --translator deeplx`                                                                         |
| `--translator-args <json>`      | Arguments pour le traducteur, au format JSON                                                                                       | `pdf2zh_next example.pdf --translator-args '{"api_key": "your_api_key"}'`                                             |
| `--ocr <ocr>`                   | Spécifie le moteur OCR, par défaut `paddle`                                                                                        | `pdf2zh_next example.pdf --ocr easyocr`                                                                               |
| `--ocr-args <json>`             | Arguments pour le moteur OCR, au format JSON                                                                                       | `pdf2zh_next example.pdf --ocr-args '{"lang": ["en", "zh"]}'`                                                         |
| `--concurrency <number>`        | Nombre de tâches concurrentes, par défaut `4`                                                                                      | `pdf2zh_next example.pdf --concurrency 8`                                                                             |
| `--timeout <seconds>`           | Délai d'attente pour chaque tâche en secondes, par défaut `30`                                                                     | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry <number>`              | Nombre de tentatives pour les tâches échouées, par défaut `3`                                                                      | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--log-level <level>`           | Niveau de journalisation, par défaut `info`, supporte `debug`, `info`, `warning`, `error`                                          | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file <path>`             | Chemin du fichier de journal, par défaut `stdout`                                                                                  | `pdf2zh_next example.pdf --log-file ./logs/translation.log`                                                           |
| `--config <path>`               | Chemin du fichier de configuration                                                                                                 | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `--dry-run`                     | Exécution à blanc sans traitement réel                                                                                             | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | Affiche la version et quitte                                                                                                       | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Affiche l'aide et quitte                                                                                                           | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-dir`          | Use offline assets from the specified directory                                          | `pdf2zh_next example.pdf --offline-assets-dir /path`                                                                  |
| `--cache-dir`                   | Cache directory for storing downloaded models and assets                                 | `pdf2zh_next example.pdf --cache-dir /path`                                                                           |
| `--cache`                       | Enable caching of downloaded models and assets (enabled by default)                      | `pdf2zh_next example.pdf --cache`                                                                                     |
| `--no-cache`                    | Disable caching of downloaded models and assets                                          | `pdf2zh_next example.pdf --no-cache`                                                                                  |

---

### TRANSLATION RESULT

| `--generate-offline-assets`     | Générer un package de ressources hors ligne dans le répertoire spécifié                 | `pdf2zh_next example.pdf --generate-offline-assets /chemin`                                                             |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-dir`          | Utiliser les ressources hors ligne depuis le répertoire spécifié                         | `pdf2zh_next example.pdf --offline-assets-dir /chemin`                                                                  |
| `--cache-dir`                   | Répertoire de cache pour stocker les modèles et ressources téléchargés                   | `pdf2zh_next example.pdf --cache-dir /chemin`                                                                           |
| `--cache`                       | Activer la mise en cache des modèles et ressources téléchargés (activé par défaut)       | `pdf2zh_next example.pdf --cache`                                                                                     |
| `--no-cache`                    | Désactiver la mise en cache des modèles et ressources téléchargés                        | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--restore-offline-assets-dir`  | The directory to restore offline assets from, default is `./assets`                     | `pdf2zh_next example.pdf --restore-offline-assets-dir /path/to/assets`                                                |
| `--restore-offline-assets-file` | The offline assets file to restore, default is `assets.zip`                             | `pdf2zh_next example.pdf --restore-offline-assets-file /path/to/assets.zip`                                           |
| `-s`<br>`--source-language`     | The source language of the document. Default is `auto`.                                 | `pdf2zh_next example.pdf -s en`<br>`pdf2zh_next example.pdf --source-language en`                                     |
| `-t`<br>`--target-language`     | The target language to translate to. Default is `zh`.                                   | `pdf2zh_next example.pdf -t ja`<br>`pdf2zh_next example.pdf --target-language ja`                                     |
| `-l`<br>`--language`            | The language of the document. Equivalent to setting both `-s` and `-t` to the same value. | `pdf2zh_next example.pdf -l ja`<br>`pdf2zh_next example.pdf --language ja`                                            |
| `-o`<br>`--output`              | The output file path. Default is `[original_name]_translated.pdf`                       | `pdf2zh_next example.pdf -o translated.pdf`<br>`pdf2zh_next example.pdf --output translated.pdf`                      |
| `-f`<br>`--format`              | The output format. Default is `pdf`.                                                    | `pdf2zh_next example.pdf -f docx`<br>`pdf2zh_next example.pdf --format docx`                                          |
| `-v`<br>`--verbose`             | Enable verbose output.                                                                  | `pdf2zh_next example.pdf -v`<br>`pdf2zh_next example.pdf --verbose`                                                   |
| `-h`<br>`--help`                | Show help message and exit.                                                             | `pdf2zh_next example.pdf -h`<br>`pdf2zh_next example.pdf --help`                                                      |

---

### TRANSLATED TEXT

| `--restore-offline-assets`      | Restaurer le package d'actifs hors ligne à partir du répertoire spécifié                | `pdf2zh_next example.pdf --restore-offline-assets /chemin`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--restore-offline-assets-dir`  | Le répertoire à partir duquel restaurer les actifs hors ligne, par défaut `./assets`    | `pdf2zh_next example.pdf --restore-offline-assets-dir /chemin/vers/assets`                                             |
| `--restore-offline-assets-file` | Le fichier d'actifs hors ligne à restaurer, par défaut `assets.zip`                     | `pdf2zh_next example.pdf --restore-offline-assets-file /chemin/vers/assets.zip`                                        |
| `-s`<br>`--source-language`     | La langue source du document. Par défaut `auto`.                                        | `pdf2zh_next example.pdf -s en`<br>`pdf2zh_next example.pdf --source-language en`                                     |
| `-t`<br>`--target-language`     | La langue cible vers laquelle traduire. Par défaut `zh`.                                | `pdf2zh_next example.pdf -t ja`<br>`pdf2zh_next example.pdf --target-language ja`                                     |
| `-l`<br>`--language`            | La langue du document. Équivalent à définir `-s` et `-t` à la même valeur.              | `pdf2zh_next example.pdf -l ja`<br>`pdf2zh_next example.pdf --language ja`                                            |
| `-o`<br>`--output`              | Le chemin du fichier de sortie. Par défaut `[nom_original]_translated.pdf`              | `pdf2zh_next example.pdf -o translated.pdf`<br>`pdf2zh_next example.pdf --output translated.pdf`                      |
| `-f`<br>`--format`              | Le format de sortie. Par défaut `pdf`.                                                  | `pdf2zh_next example.pdf -f docx`<br>`pdf2zh_next example.pdf --format docx`                                          |
| `-v`<br>`--verbose`             | Activer la sortie détaillée.                                                            | `pdf2zh_next example.pdf -v`<br>`pdf2zh_next example.pdf --verbose`                                                   |
| `-h`<br>`--help`                | Afficher le message d'aide et quitter.                                                  | `pdf2zh_next example.pdf -h`<br>`pdf2zh_next example.pdf --help`                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--help`                        | Show help then exit                                                                     | `pdf2zh_next --help`                                                                                                  |
| `-i`, `--input <input>`         | Input PDF file path (required)                                                          | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output <output>`       | Output directory (required)                                                             | `pdf2zh_next -i input.pdf -o output_directory`                                                                        |
| `-l`, `--lang <lang>`           | Target language code (required). <br>See [Supported Languages](./SUPPORTED_LANG.md)     | `pdf2zh_next -i input.pdf -o out -l fr`                                                                               |
| `-s`, `--service <service>`     | Translation service (required). <br>See [Documentation of Translation Services](./TRANSLATION_SERVICES.md) | `pdf2zh_next -i input.pdf -o out -l fr -s google`                                                                     |
| `--service-key <service_key>`   | Translation service key (optional)                                                      | `pdf2zh_next -i input.pdf -o out -l fr -s google --service-key <your_key>`                                            |
| `--service-url <service_url>`   | Translation service url (optional)                                                      | `pdf2zh_next -i input.pdf -o out -l fr -s google --service-url <your_url>`                                            |
| `--service-region <service_region>` | Translation service region (optional)                                                   | `pdf2zh_next -i input.pdf -o out -l fr -s azure --service-region <your_region>`                                       |
| `--model <model>`               | Model for translation (optional)                                                        | `pdf2zh_next -i input.pdf -o out -l fr -s openai --model gpt-4`                                                       |
| `--math-translator <translator>` | Math translator (optional). <br>Choose from: `PDFMathTranslate`, `simple`               | `pdf2zh_next -i input.pdf -o out -l fr -s google --math-translator PDFMathTranslate`                                  |
| `--math-prompt <prompt>`        | Math prompt (optional)                                                                  | `pdf2zh_next -i input.pdf -o out -l fr -s google --math-prompt <your_prompt>`                                         |
| `--no-text`                     | Skip text translation (optional)                                                        | `pdf2zh_next -i input.pdf -o out -l fr -s google --no-text`                                                           |
| `--no-math`                     | Skip math translation (optional)                                                        | `pdf2zh_next -i input.pdf -o out -l fr -s google --no-math`                                                           |
| `--only-math`                   | Only translate math (optional)                                                          | `pdf2zh_next -i input.pdf -o out -l fr -s google --only-math`                                                         |
| `--workers <workers>`           | Number of workers for translation (optional)                                            | `pdf2zh_next -i input.pdf -o out -l fr -s google --workers 4`                                                         |
| `--timeout <timeout>`           | Timeout for each translation request in seconds (optional)                              | `pdf2zh_next -i input.pdf -o out -l fr -s google --timeout 30`                                                        |
| `--retry <retry>`               | Number of retries for each translation request (optional)                               | `pdf2zh_next -i input.pdf -o out -l fr -s google --retry 3`                                                           |
| `--retry-wait <retry_wait>`     | Wait time between retries in seconds (optional)                                         | `pdf2zh_next -i input.pdf -o out -l fr -s google --retry-wait 1`                                                      |
| `--check`                       | Check translation service without translating (optional)                                | `pdf2zh_next -i input.pdf -o out -l fr -s google --check`                                                             |
| `--verbose`                     | Show verbose output (optional)                                                          | `pdf2zh_next -i input.pdf -o out -l fr -s google --verbose`                                                           |
| `--debug`                       | Show debug output (optional)                                                            | `pdf2zh_next -i input.pdf -o out -l fr -s google --debug`                                                             |

---

### TRANSLATED TEXT

| `--version`                     | Afficher la version puis quitter                                                              | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--help`                        | Afficher l'aide puis quitter                                                                   | `pdf2zh_next --help`                                                                                                  |
| `-i`, `--input <input>`         | Chemin du fichier PDF d'entrée (obligatoire)                                                   | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output <output>`       | Répertoire de sortie (obligatoire)                                                             | `pdf2zh_next -i input.pdf -o output_directory`                                                                        |
| `-l`, `--lang <lang>`           | Code de langue cible (obligatoire). <br>Voir [Langues supportées](./SUPPORTED_LANG.md)         | `pdf2zh_next -i input.pdf -o out -l fr`                                                                               |
| `-s`, `--service <service>`     | Service de traduction (obligatoire). <br>Voir [Documentation des services de traduction](./TRANSLATION_SERVICES.md) | `pdf2zh_next -i input.pdf -o out -l fr -s google`                                                                     |
| `--service-key <service_key>`   | Clé du service de traduction (optionnel)                                                       | `pdf2zh_next -i input.pdf -o out -l fr -s google --service-key <your_key>`                                            |
| `--service-url <service_url>`   | URL du service de traduction (optionnel)                                                       | `pdf2zh_next -i input.pdf -o out -l fr -s google --service-url <your_url>`                                            |
| `--service-region <service_region>` | Région du service de traduction (optionnel)                                                    | `pdf2zh_next -i input.pdf -o out -l fr -s azure --service-region <your_region>`                                       |
| `--model <model>`               | Modèle pour la traduction (optionnel)                                                          | `pdf2zh_next -i input.pdf -o out -l fr -s openai --model gpt-4`                                                       |
| `--math-translator <translator>` | Traducteur mathématique (optionnel). <br>Choix possibles : `PDFMathTranslate`, `simple`        | `pdf2zh_next -i input.pdf -o out -l fr -s google --math-translator PDFMathTranslate`                                  |
| `--math-prompt <prompt>`        | Invite pour les mathématiques (optionnel)                                                      | `pdf2zh_next -i input.pdf -o out -l fr -s google --math-prompt <your_prompt>`                                         |
| `--no-text`                     | Ignorer la traduction du texte (optionnel)                                                     | `pdf2zh_next -i input.pdf -o out -l fr -s google --no-text`                                                           |
| `--no-math`                     | Ignorer la traduction des mathématiques (optionnel)                                            | `pdf2zh_next -i input.pdf -o out -l fr -s google --no-math`                                                           |
| `--only-math`                   | Traduire uniquement les mathématiques (optionnel)                                              | `pdf2zh_next -i input.pdf -o out -l fr -s google --only-math`                                                         |
| `--workers <workers>`           | Nombre de workers pour la traduction (optionnel)                                               | `pdf2zh_next -i input.pdf -o out -l fr -s google --workers 4`                                                         |
| `--timeout <timeout>`           | Délai d'attente pour chaque requête de traduction en secondes (optionnel)                      | `pdf2zh_next -i input.pdf -o out -l fr -s google --timeout 30`                                                        |
| `--retry <retry>`               | Nombre de tentatives pour chaque requête de traduction (optionnel)                             | `pdf2zh_next -i input.pdf -o out -l fr -s google --retry 3`                                                           |
| `--retry-wait <retry_wait>`     | Temps d'attente entre les tentatives en secondes (optionnel)                                   | `pdf2zh_next -i input.pdf -o out -l fr -s google --retry-wait 1`                                                      |
| `--check`                       | Vérifier le service de traduction sans traduire (optionnel)                                    | `pdf2zh_next -i input.pdf -o out -l fr -s google --check`                                                             |
| `--verbose`                     | Afficher une sortie détaillée (optionnel)                                                      | `pdf2zh_next -i input.pdf -o out -l fr -s google --verbose`                                                           |
| `--debug`                       | Afficher une sortie de débogage (optionnel)                                                    | `pdf2zh_next -i input.pdf -o out -l fr -s google --debug`                                                             |
[Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--output`                      | Specify the output file name                                                            | `pdf2zh_next example.pdf --output example-zh.pdf`                                                                      | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--model`                       | Specify the model to use for translation                                                | `pdf2zh_next example.pdf --model gpt-4o`                                                                              | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--target-lang`                 | Specify the target language for translation                                             | `pdf2zh_next example.pdf --target-lang fr`                                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--source-lang`                 | Specify the source language for translation                                             | `pdf2zh_next example.pdf --source-lang en`                                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--api-key`                     | Specify the API key for the translation service                                         | `pdf2zh_next example.pdf --api-key sk-xxxxxx`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--proxy`                       | Specify the proxy for the translation service                                           | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--tokens-per-chunk`            | Specify the number of tokens per chunk for translation                                  | `pdf2zh_next example.pdf --tokens-per-chunk 1024`                                                                      | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--tokens-overlap`              | Specify the number of tokens to overlap between chunks for translation                   | `pdf2zh_next example.pdf --tokens-overlap 50`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--max-concurrent`              | Specify the maximum number of concurrent translations                                   | `pdf2zh_next example.pdf --max-concurrent 5`                                                                            | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--max-retries`                 | Specify the maximum number of retries for translation                                   | `pdf2zh_next example.pdf --max-retries 3`                                                                               | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--timeout`                     | Specify the timeout for translation requests                                            | `pdf2zh_next example.pdf --timeout 30`                                                                                  | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--temperature`                 | Specify the temperature for translation                                                | `pdf2zh_next example.pdf --temperature 0.1`                                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--translate-only`              | Only translate the text without generating a new PDF                                     | `pdf2zh_next example.pdf --translate-only`                                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--webui`                       | Start the web interface                                                                 | `pdf2zh_next --webui`                                                                                                  | [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-port`                  | Specify the port for the web interface                                                  | `pdf2zh_next --webui --webui-port 3000`                                                                                | [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-host`                  | Specify the host for the web interface                                                  | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                             | [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-base-url`              | Specify the base URL for the web interface                                              | `pdf2zh_next --webui --webui-base-url /pdf2zh`                                                                         | [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-no-browser`            | Do not open the browser automatically when starting the web interface                   | `pdf2zh_next --webui --webui-no-browser`                                                                               | [Using **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--version`                     | Display the version of pdf2zh_next                                                      | `pdf2zh_next --version`                                                                                                | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--help`                        | Display the help message                                                                | `pdf2zh_next --help`                                                                                                   | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |

---

### OUTPUT

| `--pages`                       | Traduction partielle du document                                                       | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--output`                      | Spécifier le nom du fichier de sortie                                                   | `pdf2zh_next example.pdf --output example-zh.pdf`                                                                      | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--model`                       | Spécifier le modèle à utiliser pour la traduction                                       | `pdf2zh_next example.pdf --model gpt-4o`                                                                              | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--target-lang`                 | Spécifier la langue cible pour la traduction                                            | `pdf2zh_next example.pdf --target-lang fr`                                                                             | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--source-lang`                 | Spécifier la langue source pour la traduction                                           | `pdf2zh_next example.pdf --source-lang en`                                                                             | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--api-key`                     | Spécifier la clé API pour le service de traduction                                      | `pdf2zh_next example.pdf --api-key sk-xxxxxx`                                                                          | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--proxy`                       | Spécifier le proxy pour le service de traduction                                        | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--tokens-per-chunk`            | Spécifier le nombre de jetons par segment pour la traduction                            | `pdf2zh_next example.pdf --tokens-per-chunk 1024`                                                                      | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--tokens-overlap`              | Spécifier le nombre de jetons à chevaucher entre les segments pour la traduction        | `pdf2zh_next example.pdf --tokens-overlap 50`                                                                          | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--max-concurrent`              | Spécifier le nombre maximum de traductions simultanées                                  | `pdf2zh_next example.pdf --max-concurrent 5`                                                                            | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--max-retries`                 | Spécifier le nombre maximum de tentatives pour la traduction                            | `pdf2zh_next example.pdf --max-retries 3`                                                                               | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--timeout`                     | Spécifier le délai d’attente pour les requêtes de traduction                            | `pdf2zh_next example.pdf --timeout 30`                                                                                  | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--temperature`                 | Spécifier la température pour la traduction                                             | `pdf2zh_next example.pdf --temperature 0.1`                                                                             | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--translate-only`              | Traduire uniquement le texte sans générer un nouveau PDF                                | `pdf2zh_next example.pdf --translate-only`                                                                             | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--webui`                       | Démarrer l’interface web                                                                | `pdf2zh_next --webui`                                                                                                  | [Utilisation de **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-port`                  | Spécifier le port pour l’interface web                                                  | `pdf2zh_next --webui --webui-port 3000`                                                                                | [Utilisation de **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-host`                  | Spécifier l’hôte pour l’interface web                                                   | `pdf2zh_next --webui --webui-host 0.0.0.0`                                                                             | [Utilisation de **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-base-url`              | Spécifier l’URL de base pour l’interface web                                            | `pdf2zh_next --webui --webui-base-url /pdf2zh`                                                                         | [Utilisation de **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--webui-no-browser`            | Ne pas ouvrir automatiquement le navigateur lors du démarrage de l’interface web       | `pdf2zh_next --webui --webui-no-browser`                                                                               | [Utilisation de **WebUI**](https://pdf2zh-next.com/getting-started/USAGE_webui.html)               |
| `--version`                     | Afficher la version de pdf2zh_next                                                     | `pdf2zh_next --version`                                                                                                | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--help`                        | Afficher le message d’aide                                                              | `pdf2zh_next --help`                                                                                                   | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out fr`                                                                               |
| `--output`<br/>`-o`             | Output file path                                                                        | `pdf2zh_next example.pdf -o example_fr.pdf`                                                                           |
| `--engine`                      | Translation engine to use                                                               | `pdf2zh_next example.pdf --engine google`                                                                             |
| `--api-key`                     | API key for translation engine                                                          | `pdf2zh_next example.pdf --engine openai --api-key sk-xxx`                                                            |
| `--model`                       | Model name for OpenAI or Azure                                                          | `pdf2zh_next example.pdf --engine openai --model gpt-4`                                                               |
| `--api-base`                    | API base URL for Azure or other OpenAI-compatible APIs                                  | `pdf2zh_next example.pdf --engine azure --api-base https://xxx.openai.azure.com/`                                     |
| `--api-version`                 | API version for Azure                                                                   | `pdf2zh_next example.pdf --engine azure --api-version 2024-02-01`                                                     |
| `--concurrency`                 | Number of concurrent translation requests                                               | `pdf2zh_next example.pdf --concurrency 5`                                                                             |
| `--timeout`                     | Timeout for each translation request in seconds                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry`                       | Number of retries for failed requests                                                   | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir`                   | Directory to store cache files                                                          | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--log-level`                   | Log level (debug, info, warn, error)                                                   | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--help`<br/>`-h`               | Show help                                                                               | `pdf2zh_next -h`                                                                                                      |
| `--version`<br/>`-v`            | Show version                                                                            | `pdf2zh_next -v`                                                                                                      |
| `--list-engines`                | List all available translation engines                                                  | `pdf2zh_next --list-engines`                                                                                          |
| `--list-languages`              | List all supported languages                                                            | `pdf2zh_next --list-languages`                                                                                        |
| `--check-update`                | Check for updates                                                                       | `pdf2zh_next --check-update`                                                                                          |

---

### TRANSLATION RESULT

| `--lang-in`                     | Code de langue source                                                                   | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Code de langue cible                                                                    | `pdf2zh_next example.pdf --lang-out fr`                                                                               |
| `--output`<br/>`-o`             | Chemin du fichier de sortie                                                             | `pdf2zh_next example.pdf -o example_fr.pdf`                                                                           |
| `--engine`                      | Moteur de traduction à utiliser                                                         | `pdf2zh_next example.pdf --engine google`                                                                             |
| `--api-key`                     | Clé API pour le moteur de traduction                                                    | `pdf2zh_next example.pdf --engine openai --api-key sk-xxx`                                                            |
| `--model`                       | Nom du modèle pour OpenAI ou Azure                                                      | `pdf2zh_next example.pdf --engine openai --model gpt-4`                                                               |
| `--api-base`                    | URL de base de l'API pour Azure ou autres API compatibles OpenAI                        | `pdf2zh_next example.pdf --engine azure --api-base https://xxx.openai.azure.com/`                                     |
| `--api-version`                 | Version de l'API pour Azure                                                             | `pdf2zh_next example.pdf --engine azure --api-version 2024-02-01`                                                     |
| `--concurrency`                 | Nombre de requêtes de traduction simultanées                                            | `pdf2zh_next example.pdf --concurrency 5`                                                                             |
| `--timeout`                     | Délai d'attente pour chaque requête de traduction en secondes                           | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry`                       | Nombre de tentatives pour les requêtes échouées                                         | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--no-cache`                    | Désactiver le cache                                                                     | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir`                   | Répertoire pour stocker les fichiers de cache                                           | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--log-level`                   | Niveau de journalisation (debug, info, warn, error)                                     | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--help`<br/>`-h`               | Afficher l'aide                                                                         | `pdf2zh_next -h`                                                                                                      |
| `--version`<br/>`-v`            | Afficher la version                                                                     | `pdf2zh_next -v`                                                                                                      |
| `--list-engines`                | Lister tous les moteurs de traduction disponibles                                       | `pdf2zh_next --list-engines`                                                                                          |
| `--list-languages`              | Lister toutes les langues supportées                                                    | `pdf2zh_next --list-languages`                                                                                        |
| `--check-update`                | Vérifier les mises à jour                                                               | `pdf2zh_next --check-update`                                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--save-translated-pdf`         | Save the translated PDF                                                                 | `pdf2zh_next example.pdf --save-translated-pdf`                                                                       |
| `--save-translated-text`        | Save the translated text                                                                | `pdf2zh_next example.pdf --save-translated-text`                                                                      |
| `--save-raw-text`               | Save the raw text (without translation)                                                 | `pdf2zh_next example.pdf --save-raw-text`                                                                             |
| `--save-raw-json`               | Save the raw JSON (without translation)                                                 | `pdf2zh_next example.pdf --save-raw-json`                                                                             |
| `--save-markdown`               | Save the markdown text (without translation)                                            | `pdf2zh_next example.pdf --save-markdown`                                                                             |
| `--save-html`                   | Save the HTML text (without translation)                                                | `pdf2zh_next example.pdf --save-html`                                                                                 |
| `--save-translated-html`        | Save the translated HTML text                                                           | `pdf2zh_next example.pdf --save-translated-html`                                                                      |
| `--save-translated-markdown`    | Save the translated markdown text                                                       | `pdf2zh_next example.pdf --save-translated-markdown`                                                                  |
| `--save-json`                   | Save the JSON text (without translation)                                                | `pdf2zh_next example.pdf --save-json`                                                                                 |
| `--save-translated-json`        | Save the translated JSON text                                                           | `pdf2zh_next example.pdf --save-translated-json`                                                                      |
| `--save-pdf-json`               | Save the PDF JSON (without translation)                                                 | `pdf2zh_next example.pdf --save-pdf-json`                                                                             |
| `--save-translated-pdf-json`    | Save the translated PDF JSON                                                            | `pdf2zh_next example.pdf --save-translated-pdf-json`                                                                  |
| `--save-pdf-text`               | Save the PDF text (without translation)                                                 | `pdf2zh_next example.pdf --save-pdf-text`                                                                             |
| `--save-translated-pdf-text`    | Save the translated PDF text                                                            | `pdf2zh_next example.pdf --save-translated-pdf-text`                                                                  |
| `--save-pdf-html`               | Save the PDF HTML (without translation)                                                 | `pdf2zh_next example.pdf --save-pdf-html`                                                                             |
| `--save-translated-pdf-html`    | Save the translated PDF HTML                                                            | `pdf2zh_next example.pdf --save-translated-pdf-html`                                                                  |
| `--save-pdf-markdown`           | Save the PDF markdown (without translation)                                             | `pdf2zh_next example.pdf --save-pdf-markdown`                                                                         |
| `--save-translated-pdf-markdown`| Save the translated PDF markdown                                                        | `pdf2zh_next example.pdf --save-translated-pdf-markdown`                                                              |
| `--save-pdf-json-raw`           | Save the PDF JSON raw (without translation)                                             | `pdf2zh_next example.pdf --save-pdf-json-raw`                                                                         |
| `--save-translated-pdf-json-raw`| Save the translated PDF JSON raw                                                        | `pdf2zh_next example.pdf --save-translated-pdf-json-raw`                                                              |
| `--save-pdf-text-raw`           | Save the PDF text raw (without translation)                                             | `pdf2zh_next example.pdf --save-pdf-text-raw`                                                                         |
| `--save-translated-pdf-text-raw`| Save the translated PDF text raw                                                        | `pdf2zh_next example.pdf --save-translated-pdf-text-raw`                                                              |
| `--save-pdf-html-raw`           | Save the PDF HTML raw (without translation)                                             | `pdf2zh_next example.pdf --save-pdf-html-raw`                                                                         |
| `--save-translated-pdf-html-raw`| Save the translated PDF HTML raw                                                        | `pdf2zh_next example.pdf --save-translated-pdf-html-raw`                                                              |
| `--save-pdf-markdown-raw`       | Save the PDF markdown raw (without translation)                                         | `pdf2zh_next example.pdf --save-pdf-markdown-raw`                                                                     |
| `--save-translated-pdf-markdown-raw`| Save the translated PDF markdown raw                                                 | `pdf2zh_next example.pdf --save-translated-pdf-markdown-raw`                                                          |
| `--save-pdf-json-raw-translated`| Save the PDF JSON raw translated                                                        | `pdf2zh_next example.pdf --save-pdf-json-raw-translated`                                                              |
| `--save-pdf-text-raw-translated`| Save the PDF text raw translated                                                        | `pdf2zh_next example.pdf --save-pdf-text-raw-translated`                                                              |
| `--save-pdf-html-raw-translated`| Save the PDF HTML raw translated                                                        | `pdf2zh_next example.pdf --save-pdf-html-raw-translated`                                                              |
| `--save-pdf-markdown-raw-translated`| Save the PDF markdown raw translated                                                 | `pdf2zh_next example.pdf --save-pdf-markdown-raw-translated`                                                          |
| `--save-pdf-json-translated`    | Save the PDF JSON translated                                                            | `pdf2zh_next example.pdf --save-pdf-json-translated`                                                                  |
| `--save-pdf-text-translated`    | Save the PDF text translated                                                            | `pdf2zh_next example.pdf --save-pdf-text-translated`                                                                  |
| `--save-pdf-html-translated`    | Save the PDF HTML translated                                                            | `pdf2zh_next example.pdf --save-pdf-html-translated`                                                                  |
| `--save-pdf-markdown-translated`| Save the PDF markdown translated                                                        | `pdf2zh_next example.pdf --save-pdf-markdown-translated`                                                              |
| `--save-pdf-json-raw-translated`| Save the PDF JSON raw translated                                                        | `pdf2zh_next example.pdf --save-pdf-json-raw-translated`                                                              |
| `--save-pdf-text-raw-translated`| Save the PDF text raw translated                                                        | `pdf2zh_next example.pdf --save-pdf-text-raw-translated`                                                              |
| `--save-pdf-html-raw-translated`| Save the PDF HTML raw translated                                                        | `pdf2zh_next example.pdf --save-pdf-html-raw-translated`                                                              |
| `--save-pdf-markdown-raw-translated`| Save the PDF markdown raw translated                                                 | `pdf2zh_next example.pdf --save-pdf-markdown-raw-translated`                                                          |

---

### TRANSLATION RESULT

| `--lang-out`                    | Code de langue cible                                                                     | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--save-translated-pdf`         | Enregistrer le PDF traduit                                                              | `pdf2zh_next example.pdf --save-translated-pdf`                                                                       |
| `--save-translated-text`        | Enregistrer le texte traduit                                                            | `pdf2zh_next example.pdf --save-translated-text`                                                                      |
| `--save-raw-text`               | Enregistrer le texte brut (sans traduction)                                             | `pdf2zh_next example.pdf --save-raw-text`                                                                             |
| `--save-raw-json`               | Enregistrer le JSON brut (sans traduction)                                              | `pdf2zh_next example.pdf --save-raw-json`                                                                             |
| `--save-markdown`               | Enregistrer le texte markdown (sans traduction)                                         | `pdf2zh_next example.pdf --save-markdown`                                                                             |
| `--save-html`                   | Enregistrer le texte HTML (sans traduction)                                             | `pdf2zh_next example.pdf --save-html`                                                                                 |
| `--save-translated-html`        | Enregistrer le texte HTML traduit                                                       | `pdf2zh_next example.pdf --save-translated-html`                                                                      |
| `--save-translated-markdown`    | Enregistrer le texte markdown traduit                                                   | `pdf2zh_next example.pdf --save-translated-markdown`                                                                  |
| `--save-json`                   | Enregistrer le texte JSON (sans traduction)                                             | `pdf2zh_next example.pdf --save-json`                                                                                 |
| `--save-translated-json`        | Enregistrer le texte JSON traduit                                                       | `pdf2zh_next example.pdf --save-translated-json`                                                                      |
| `--save-pdf-json`               | Enregistrer le JSON PDF (sans traduction)                                               | `pdf2zh_next example.pdf --save-pdf-json`                                                                             |
| `--save-translated-pdf-json`    | Enregistrer le JSON PDF traduit                                                         | `pdf2zh_next example.pdf --save-translated-pdf-json`                                                                  |
| `--save-pdf-text`               | Enregistrer le texte PDF (sans traduction)                                              | `pdf2zh_next example.pdf --save-pdf-text`                                                                             |
| `--save-translated-pdf-text`    | Enregistrer le texte PDF traduit                                                        | `pdf2zh_next example.pdf --save-translated-pdf-text`                                                                  |
| `--save-pdf-html`               | Enregistrer le HTML PDF (sans traduction)                                               | `pdf2zh_next example.pdf --save-pdf-html`                                                                             |
| `--save-translated-pdf-html`    | Enregistrer le HTML PDF traduit                                                         | `pdf2zh_next example.pdf --save-translated-pdf-html`                                                                  |
| `--save-pdf-markdown`           | Enregistrer le markdown PDF (sans traduction)                                           | `pdf2zh_next example.pdf --save-pdf-markdown`                                                                         |
| `--save-translated-pdf-markdown`| Enregistrer le markdown PDF traduit                                                     | `pdf2zh_next example.pdf --save-translated-pdf-markdown`                                                              |
| `--save-pdf-json-raw`           | Enregistrer le JSON brut PDF (sans traduction)                                          | `pdf2zh_next example.pdf --save-pdf-json-raw`                                                                         |
| `--save-translated-pdf-json-raw`| Enregistrer le JSON brut PDF traduit                                                    | `pdf2zh_next example.pdf --save-translated-pdf-json-raw`                                                              |
| `--save-pdf-text-raw`           | Enregistrer le texte brut PDF (sans traduction)                                         | `pdf2zh_next example.pdf --save-pdf-text-raw`                                                                         |
| `--save-translated-pdf-text-raw`| Enregistrer le texte brut PDF traduit                                                   | `pdf2zh_next example.pdf --save-translated-pdf-text-raw`                                                              |
| `--save-pdf-html-raw`           | Enregistrer le HTML brut PDF (sans traduction)                                          | `pdf2zh_next example.pdf --save-pdf-html-raw`                                                                         |
| `--save-translated-pdf-html-raw`| Enregistrer le HTML brut PDF traduit                                                    | `pdf2zh_next example.pdf --save-translated-pdf-html-raw`                                                              |
| `--save-pdf-markdown-raw`       | Enregistrer le markdown brut PDF (sans traduction)                                      | `pdf2zh_next example.pdf --save-pdf-markdown-raw`                                                                     |
| `--save-translated-pdf-markdown-raw`| Enregistrer le markdown brut PDF traduit                                             | `pdf2zh_next example.pdf --save-translated-pdf-markdown-raw`                                                          |
| `--save-pdf-json-raw-translated`| Enregistrer le JSON brut PDF traduit                                                    | `pdf2zh_next example.pdf --save-pdf-json-raw-translated`                                                              |
| `--save-pdf-text-raw-translated`| Enregistrer le texte brut PDF traduit                                                   | `pdf2zh_next example.pdf --save-pdf-text-raw-translated`                                                              |
| `--save-pdf-html-raw-translated`| Enregistrer le HTML brut PDF traduit                                                    | `pdf2zh_next example.pdf --save-pdf-html-raw-translated`                                                              |
| `--save-pdf-markdown-raw-translated`| Enregistrer le markdown brut PDF traduit                                             | `pdf2zh_next example.pdf --save-pdf-markdown-raw-translated`                                                          |
| `--save-pdf-json-translated`    | Enregistrer le JSON PDF traduit                                                         | `pdf2zh_next example.pdf --save-pdf-json-translated`                                                                  |
| `--save-pdf-text-translated`    | Enregistrer le texte PDF traduit                                                        | `pdf2zh_next example.pdf --save-pdf-text-translated`                                                                  |
| `--save-pdf-html-translated`    | Enregistrer le HTML PDF traduit                                                         | `pdf2zh_next example.pdf --save-pdf-html-translated`                                                                  |
| `--save-pdf-markdown-translated`| Enregistrer le markdown PDF traduit                                                     | `pdf2zh_next example.pdf --save-pdf-markdown-translated`                                                              |
| `--save-pdf-json-raw-translated`| Enregistrer le JSON brut PDF traduit                                                    | `pdf2zh_next example.pdf --save-pdf-json-raw-translated`                                                              |
| `--save-pdf-text-raw-translated`| Enregistrer le texte brut PDF traduit                                                   | `pdf2zh_next example.pdf --save-pdf-text-raw-translated`                                                              |
| `--save-pdf-html-raw-translated`| Enregistrer le HTML brut PDF traduit                                                    | `pdf2zh_next example.pdf --save-pdf-html-raw-translated`                                                              |
| `--save-pdf-markdown-raw-translated`| Enregistrer le markdown brut PDF traduit                                             | `pdf2zh_next example.pdf --save-pdf-markdown-raw-translated`                                                          |
`5`                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `--min-text-ratio`              | Minimum text ratio to translate                                                        | `pdf2zh_next example.pdf --min-text-ratio 0.5`                                                                         | `0.5`                                                               |
| `--translate-words`             | Translate words (e.g., labels in figures)                                              | `pdf2zh_next example.pdf --translate-words`                                                                            | `false`                                                             |
| `--glossaries`                  | Glossaries to use for translation                                                      | `pdf2zh_next example.pdf --glossaries "path/to/glossary1.csv,path/to/glossary2.csv"`                                   | `[]`                                                                |
| `--formula-translation-mode`    | Formula translation mode (`"disabled"`, `"single-line"`, `"multi-line"`)               | `pdf2zh_next example.pdf --formula-translation-mode "single-line"`                                                     | `"single-line"`                                                     |
| `--formula-translation-prompt`  | Custom prompt for formula translation                                                  | `pdf2zh_next example.pdf --formula-translation-prompt "Translate the following formula to Chinese:"`                   | `"Translate the following formula to {target_language}:"`           |
| `--formula-translation-timeout` | Timeout for formula translation (seconds)                                              | `pdf2zh_next example.pdf --formula-translation-timeout 30`                                                             | `30`                                                                |
| `--formula-detection-threshold` | Confidence threshold for formula detection (0-1)                                       | `pdf2zh_next example.pdf --formula-detection-threshold 0.8`                                                            | `0.8`                                                               |
| `--table-translation-mode`      | Table translation mode (`"disabled"`, `"markdown"`, `"text"`)                          | `pdf2zh_next example.pdf --table-translation-mode "markdown"`                                                           | `"markdown"`                                                         |
| `--table-translation-prompt`    | Custom prompt for table translation                                                    | `pdf2zh_next example.pdf --table-translation-prompt "Translate the following table to Chinese:"`                       | `"Translate the following table to {target_language}:"`             |
| `--table-translation-timeout`   | Timeout for table translation (seconds)                                                | `pdf2zh_next example.pdf --table-translation-timeout 30`                                                               | `30`                                                                |
| `--table-detection-threshold`   | Confidence threshold for table detection (0-1)                                         | `pdf2zh_next example.pdf --table-detection-threshold 0.8`                                                              | `0.8`                                                               |
| `--figure-translation-mode`     | Figure translation mode (`"disabled"`, `"single-line"`, `"multi-line"`)               | `pdf2zh_next example.pdf --figure-translation-mode "single-line"`                                                       | `"single-line"`                                                     |
| `--figure-translation-prompt`   | Custom prompt for figure translation                                                   | `pdf2zh_next example.pdf --figure-translation-prompt "Translate the following figure to Chinese:"`                     | `"Translate the following figure to {target_language}:"`           |
| `--figure-translation-timeout`  | Timeout for figure translation (seconds)                                               | `pdf2zh_next example.pdf --figure-translation-timeout 30`                                                              | `30`                                                                |
| `--figure-detection-threshold`  | Confidence threshold for figure detection (0-1)                                        | `pdf2zh_next example.pdf --figure-detection-threshold 0.8`                                                             | `0.8`                                                               |
| `--page-range`                  | Page range to translate (e.g., "1-5,8,10-12")                                          | `pdf2zh_next example.pdf --page-range "1-5,8,10-12"`                                                                   | `"all"`                                                             |
| `--exclude-page-range`          | Page range to exclude from translation (e.g., "1-5,8,10-12")                           | `pdf2zh_next example.pdf --exclude-page-range "1-5,8,10-12"`                                                            | `""`                                                                |
| `--workers`                     | Number of workers for parallel processing                                              | `pdf2zh_next example.pdf --workers 4`                                                                                  | `4`                                                                 |
| `--batch-size`                   | Batch size for translation requests                                                    | `pdf2zh_next example.pdf --batch-size 10`                                                                              | `10`                                                                |
| `--request-timeout`             | Timeout for translation requests (seconds)                                             | `pdf2zh_next example.pdf --request-timeout 30`                                                                         | `30`                                                                |
| `--max-retries`                 | Maximum number of retries for failed requests                                          | `pdf2zh_next example.pdf --max-retries 3`                                                                              | `3`                                                                 |
| `--retry-delay`                 | Delay between retries (seconds)                                                        | `pdf2zh_next example.pdf --retry-delay 1`                                                                              | `1`                                                                 |
| `--cache`                       | Enable caching of translation results                                                  | `pdf2zh_next example.pdf --cache`                                                                                      | `true`                                                              |
| `--cache-dir`                   | Directory for caching translation results                                              | `pdf2zh_next example.pdf --cache-dir "./cache"`                                                                        | `"./cache"`                                                         |
| `--cache-ttl`                   | Time-to-live for cache entries (seconds)                                               | `pdf2zh_next example.pdf --cache-ttl 86400`                                                                            | `86400`                                                             |
| `--dry-run`                     | Perform a dry run without actual translation                                           | `pdf2zh_next example.pdf --dry-run`                                                                                    | `false`                                                             |
| `--verbose`                     | Enable verbose output                                                                  | `pdf2zh_next example.pdf --verbose`                                                                                    | `false`                                                             |
| `--debug`                       | Enable debug output                                                                    | `pdf2zh_next example.pdf --debug`                                                                                      | `false`                                                             |
| `--version`                     | Show version information                                                               | `pdf2zh_next --version`                                                                                                | `false`                                                             |
| `--help`                        | Show help message                                                                      | `pdf2zh_next --help`                                                                                                   | `false`                                                             |

---

### TRANSLATION RESULT

| `--min-text-length`             | Longueur minimale du texte à traduire                                                  | `pdf2zh_next example.pdf --min-text-length 5`                                                                         | `5`                                                                 |
| ------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `--min-text-ratio`              | Ratio minimal du texte à traduire                                                      | `pdf2zh_next example.pdf --min-text-ratio 0.5`                                                                         | `0.5`                                                               |
| `--translate-words`             | Traduire les mots (par exemple, les étiquettes dans les figures)                        | `pdf2zh_next example.pdf --translate-words`                                                                            | `false`                                                             |
| `--glossaries`                  | Glossaires à utiliser pour la traduction                                                | `pdf2zh_next example.pdf --glossaries "path/to/glossary1.csv,path/to/glossary2.csv"`                                   | `[]`                                                                |
| `--formula-translation-mode`    | Mode de traduction des formules (`"disabled"`, `"single-line"`, `"multi-line"`)        | `pdf2zh_next example.pdf --formula-translation-mode "single-line"`                                                     | `"single-line"`                                                     |
| `--formula-translation-prompt`  | Invite personnalisée pour la traduction des formules                                    | `pdf2zh_next example.pdf --formula-translation-prompt "Translate the following formula to Chinese:"`                   | `"Translate the following formula to {target_language}:"`           |
| `--formula-translation-timeout` | Délai d’attente pour la traduction des formules (secondes)                             | `pdf2zh_next example.pdf --formula-translation-timeout 30`                                                             | `30`                                                                |
| `--formula-detection-threshold` | Seuil de confiance pour la détection des formules (0-1)                                 | `pdf2zh_next example.pdf --formula-detection-threshold 0.8`                                                            | `0.8`                                                               |
| `--table-translation-mode`      | Mode de traduction des tableaux (`"disabled"`, `"markdown"`, `"text"`)                  | `pdf2zh_next example.pdf --table-translation-mode "markdown"`                                                           | `"markdown"`                                                         |
| `--table-translation-prompt`    | Invite personnalisée pour la traduction des tableaux                                    | `pdf2zh_next example.pdf --table-translation-prompt "Translate the following table to Chinese:"`                       | `"Translate the following table to {target_language}:"`             |
| `--table-translation-timeout`   | Délai d’attente pour la traduction des tableaux (secondes)                             | `pdf2zh_next example.pdf --table-translation-timeout 30`                                                               | `30`                                                                |
| `--table-detection-threshold`   | Seuil de confiance pour la détection des tableaux (0-1)                                 | `pdf2zh_next example.pdf --table-detection-threshold 0.8`                                                              | `0.8`                                                               |
| `--figure-translation-mode`     | Mode de traduction des figures (`"disabled"`, `"single-line"`, `"multi-line"`)         | `pdf2zh_next example.pdf --figure-translation-mode "single-line"`                                                       | `"single-line"`                                                     |
| `--figure-translation-prompt`   | Invite personnalisée pour la traduction des figures                                     | `pdf2zh_next example.pdf --figure-translation-prompt "Translate the following figure to Chinese:"`                     | `"Translate the following figure to {target_language}:"`           |
| `--figure-translation-timeout`  | Délai d’attente pour la traduction des figures (secondes)                              | `pdf2zh_next example.pdf --figure-translation-timeout 30`                                                              | `30`                                                                |
| `--figure-detection-threshold`  | Seuil de confiance pour la détection des figures (0-1)                                  | `pdf2zh_next example.pdf --figure-detection-threshold 0.8`                                                             | `0.8`                                                               |
| `--page-range`                  | Plage de pages à traduire (par exemple, "1-5,8,10-12")                                 | `pdf2zh_next example.pdf --page-range "1-5,8,10-12"`                                                                   | `"all"`                                                             |
| `--exclude-page-range`          | Plage de pages à exclure de la traduction (par exemple, "1-5,8,10-12")                 | `pdf2zh_next example.pdf --exclude-page-range "1-5,8,10-12"`                                                            | `""`                                                                |
| `--workers`                     | Nombre de travailleurs pour le traitement parallèle                                    | `pdf2zh_next example.pdf --workers 4`                                                                                  | `4`                                                                 |
| `--batch-size`                  | Taille des lots pour les requêtes de traduction                                         | `pdf2zh_next example.pdf --batch-size 10`                                                                              | `10`                                                                |
| `--request-timeout`             | Délai d’attente pour les requêtes de traduction (secondes)                             | `pdf2zh_next example.pdf --request-timeout 30`                                                                         | `30`                                                                |
| `--max-retries`                 | Nombre maximum de tentatives pour les requêtes échouées                                 | `pdf2zh_next example.pdf --max-retries 3`                                                                              | `3`                                                                 |
| `--retry-delay`                 | Délai entre les tentatives (secondes)                                                  | `pdf2zh_next example.pdf --retry-delay 1`                                                                              | `1`                                                                 |
| `--cache`                       | Activer la mise en cache des résultats de traduction                                    | `pdf2zh_next example.pdf --cache`                                                                                      | `true`                                                              |
| `--cache-dir`                   | Répertoire pour la mise en cache des résultats de traduction                           | `pdf2zh_next example.pdf --cache-dir "./cache"`                                                                        | `"./cache"`                                                         |
| `--cache-ttl`                   | Durée de vie des entrées du cache (secondes)                                            | `pdf2zh_next example.pdf --cache-ttl 86400`                                                                            | `86400`                                                             |
| `--dry-run`                     | Effectuer une simulation sans traduction réelle                                         | `pdf2zh_next example.pdf --dry-run`                                                                                    | `false`                                                             |
| `--verbose`                     | Activer la sortie détaillée                                                            | `pdf2zh_next example.pdf --verbose`                                                                                    | `false`                                                             |
| `--debug`                       | Activer la sortie de débogage                                                           | `pdf2zh_next example.pdf --debug`                                                                                      | `false`                                                             |
| `--version`                     | Afficher les informations de version                                                   | `pdf2zh_next --version`                                                                                                | `false`                                                             |
| `--help`                        | Afficher le message d’aide                                                              | `pdf2zh_next --help`                                                                                                   | `false`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8001`                                                              |
| `--rpc-translate`               | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8002`                                                        |

---

### OUTPUT

| `--rpc-doclayout`               | Adresse hôte du service RPC pour l'analyse de la mise en page des documents | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--rpc-ocr`                     | Adresse hôte du service RPC pour l'OCR                                                  | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8001`                                                              |
| `--rpc-translate`               | Adresse hôte du service RPC pour la traduction                                          | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8002`                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--threads`                     | Number of concurrent threads for translation                                            | `pdf2zh_next example.pdf --threads 10`                                                                                |
| `--skip-translation`            | Skip the translation process and output the intermediate result                         | `pdf2zh_next example.pdf --skip-translation`                                                                          |
| `--force`                       | Force overwrite the output file if it already exists                                    | `pdf2zh_next example.pdf --force`                                                                                     |
| `--verbose`                     | Verbose output                                                                          | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--debug`                       | Debug output                                                                            | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATED TEXT

| `--qps`                         | Limite de QPS pour le service de traduction                                               | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| ------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--threads`                     | Nombre de threads simultanés pour la traduction                                           | `pdf2zh_next example.pdf --threads 10`                                                                                |
| `--skip-translation`            | Ignorer le processus de traduction et afficher le résultat intermédiaire                  | `pdf2zh_next example.pdf --skip-translation`                                                                          |
| `--force`                       | Forcer l'écrasement du fichier de sortie s'il existe déjà                                 | `pdf2zh_next example.pdf --force`                                                                                     |
| `--verbose`                     | Sortie détaillée                                                                          | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--debug`                       | Sortie de débogage                                                                        | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Afficher le message d'aide et quitter                                                     | `pdf2zh_next --help`                                                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--cache-dir`                   | Specify the cache directory                                                             | `pdf2zh_next example.pdf --cache-dir ~/.pdf2zh_next/cache`                                                            |
| `--cache-format`                | Specify the cache format (json, pickle)                                                 | `pdf2zh_next example.pdf --cache-format json`                                                                         |
| `--cache-max-size`              | Maximum cache size in MB (default: 1024)                                                | `pdf2zh_next example.pdf --cache-max-size 2048`                                                                       |
| `--cache-ttl`                   | Cache time-to-live in seconds (default: 604800, 7 days)                                 | `pdf2zh_next example.pdf --cache-ttl 86400`                                                                           |

---

### OUTPUT

| `--ignore-cache`                | Ignorer le cache de traduction                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--cache-dir`                   | Spécifier le répertoire du cache                                                             | `pdf2zh_next example.pdf --cache-dir ~/.pdf2zh_next/cache`                                                            |
| `--cache-format`                | Spécifier le format du cache (json, pickle)                                                 | `pdf2zh_next example.pdf --cache-format json`                                                                         |
| `--cache-max-size`              | Taille maximale du cache en Mo (par défaut : 1024)                                                | `pdf2zh_next example.pdf --cache-max-size 2048`                                                                       |
| `--cache-ttl`                   | Durée de vie du cache en secondes (par défaut : 604800, 7 jours)                                 | `pdf2zh_next example.pdf --cache-ttl 86400`                                                                           |
---

### OUTPUT

| `--custom-system-prompt`        | Invite système personnalisée pour la traduction. Utilisée pour `/no_think` dans Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--glossary_delimiter`          | The delimiter used in the glossary file. The default is `,`.                            | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_delimiter ";"`                         |
| `--glossary_format`             | The format of the glossary file. The default is `csv`.                                  | `pdf2zh_next example.pdf --glossaries "glossary1.txt,glossary2.txt" --glossary_format "txt" --glossary_delimiter " "` |
| `--glossary_src_lang`           | The source language of the glossary. The default is `en`.                               | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_src_lang "en"`                         |
| `--glossary_tgt_lang`           | The target language of the glossary. The default is `zh`.                               | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_tgt_lang "fr"`                         |
| `--glossary_case_sensitive`     | Whether the glossary is case sensitive. The default is `false`.                         | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_case_sensitive`                        |
| `--glossary_match_boundaries`   | Whether to match word boundaries when using the glossary. The default is `false`.       | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_match_boundaries`                      |
| `--glossary_ignore_terms_regex` | Regular expression to ignore certain terms in the glossary. The default is `None`.      | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_ignore_terms_regex ".*test.*"`         |
| `--glossary_merge`              | How to merge multiple glossaries. The default is `union`. Options: `union`, `intersect` | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary_merge "intersect"`                     |

---

### TRANSLATED TEXT

| `--glossaires`                  | Liste des fichiers de glossaire.                                                                  | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv,glossaire3.csv"`                                    |
| :------------------------------ | :------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------- |
| `--glossaire_delimiteur`        | Le délimiteur utilisé dans le fichier de glossaire. Par défaut : `,`.                             | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_delimiteur ";"`                        |
| `--glossaire_format`            | Le format du fichier de glossaire. Par défaut : `csv`.                                             | `pdf2zh_next example.pdf --glossaires "glossaire1.txt,glossaire2.txt" --glossaire_format "txt" --glossaire_delimiteur " "` |
| `--glossaire_lang_src`          | La langue source du glossaire. Par défaut : `en`.                                                 | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_lang_src "en"`                         |
| `--glossaire_lang_cible`        | La langue cible du glossaire. Par défaut : `zh`.                                                  | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_lang_cible "fr"`                       |
| `--glossaire_sensible_casse`    | Indique si le glossaire est sensible à la casse. Par défaut : `false`.                            | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_sensible_casse`                        |
| `--glossaire_limites_mots`      | Indique s'il faut respecter les limites des mots lors de l'utilisation du glossaire. Par défaut : `false`. | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_limites_mots`                          |
| `--glossaire_ignorer_termes_regex` | Expression régulière pour ignorer certains termes dans le glossaire. Par défaut : `None`.          | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_ignorer_termes_regex ".*test.*"`       |
| `--glossaire_fusion`            | Comment fusionner plusieurs glossaires. Par défaut : `union`. Options : `union`, `intersect`       | `pdf2zh_next example.pdf --glossaires "glossaire1.csv,glossaire2.csv" --glossaire_fusion "intersect"`                    |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--save-manual-glossary`        | save manually added glossary                                                           | `pdf2zh_next example.pdf --save-manual-glossary`                                                                     |
| `--save-all-glossary`           | save all glossary (auto extracted and manually added)                                   | `pdf2zh_next example.pdf --save-all-glossary`                                                                        |
| `--glossary`                    | path to the glossary file (default: `glossary.json`, `glossary.yaml`, `glossary.yml`) | `pdf2zh_next example.pdf --glossary custom_glossary.json`                                                             |
| `--glossary-format`             | format of the glossary file (default: `auto`)                                          | `pdf2zh_next example.pdf --glossary-format json`                                                                     |
| `--glossary-save-format`        | format to save the glossary file (default: `auto`)                                     | `pdf2zh_next example.pdf --glossary-save-format yaml`                                                                 |
| `--glossary-save-path`          | path to save the glossary file (default: `glossary.json`)                             | `pdf2zh_next example.pdf --glossary-save-path custom_glossary.json`                                                   |
| `--glossary-save-auto`          | automatically save the glossary after translation (default: `false`)                  | `pdf2zh_next example.pdf --glossary-save-auto`                                                                       |
| `--glossary-save-manual`        | save the manually added glossary after translation (default: `false`)                 | `pdf2zh_next example.pdf --glossary-save-manual`                                                                     |
| `--glossary-save-all`           | save all glossary after translation (default: `false`)                                 | `pdf2zh_next example.pdf --glossary-save-all`                                                                        |
| `--glossary-auto-extract`       | automatically extract glossary from the document (default: `true`)                    | `pdf2zh_next example.pdf --glossary-auto-extract false`                                                               |
| `--glossary-manual-add`         | manually add glossary entries (default: `true`)                                       | `pdf2zh_next example.pdf --glossary-manual-add false`                                                                 |
| `--glossary-use`                | use glossary during translation (default: `true`)                                      | `pdf2zh_next example.pdf --glossary-use false`                                                                       |
| `--glossary-update`             | update glossary during translation (default: `true`)                                   | `pdf2zh_next example.pdf --glossary-update false`                                                                    |
| `--glossary-ignore-case`        | ignore case when matching glossary entries (default: `false`)                         | `pdf2zh_next example.pdf --glossary-ignore-case`                                                                     |
| `--glossary-ignore-punctuation` | ignore punctuation when matching glossary entries (default: `false`)                  | `pdf2zh_next example.pdf --glossary-ignore-punctuation`                                                              |
| `--glossary-ignore-whitespace`  | ignore whitespace when matching glossary entries (default: `false`)                   | `pdf2zh_next example.pdf --glossary-ignore-whitespace`                                                               |
| `--glossary-ignore-digits`      | ignore digits when matching glossary entries (default: `false`)                       | `pdf2zh_next example.pdf --glossary-ignore-digits`                                                                   |
| `--glossary-ignore-symbols`      | ignore symbols when matching glossary entries (default: `false`)                      | `pdf2zh_next example.pdf --glossary-ignore-symbols`                                                                  |
| `--glossary-ignore-accents`      | ignore accents when matching glossary entries (default: `false`)                      | `pdf2zh_next example.pdf --glossary-ignore-accents`                                                                  |
| `--glossary-ignore-articles`     | ignore articles when matching glossary entries (default: `false`)                    | `pdf2zh_next example.pdf --glossary-ignore-articles`                                                                 |
| `--glossary-ignore-prepositions` | ignore prepositions when matching glossary entries (default: `false`)                 | `pdf2zh_next example.pdf --glossary-ignore-prepositions`                                                             |
| `--glossary-ignore-conjunctions` | ignore conjunctions when matching glossary entries (default: `false`)                | `pdf2zh_next example.pdf --glossary-ignore-conjunctions`                                                              |
| `--glossary-ignore-pronouns`     | ignore pronouns when matching glossary entries (default: `false`)                     | `pdf2zh_next example.pdf --glossary-ignore-pronouns`                                                                 |
| `--glossary-ignore-verbs`        | ignore verbs when matching glossary entries (default: `false`)                       | `pdf2zh_next example.pdf --glossary-ignore-verbs`                                                                    |
| `--glossary-ignore-nouns`        | ignore nouns when matching glossary entries (default: `false`)                       | `pdf2zh_next example.pdf --glossary-ignore-nouns`                                                                    |
| `--glossary-ignore-adjectives`   | ignore adjectives when matching glossary entries (default: `false`)                  | `pdf2zh_next example.pdf --glossary-ignore-adjectives`                                                               |
| `--glossary-ignore-adverbs`      | ignore adverbs when matching glossary entries (default: `false`)                     | `pdf2zh_next example.pdf --glossary-ignore-adverbs`                                                                  |
| `--glossary-ignore-other`        | ignore other words when matching glossary entries (default: `false`)                  | `pdf2zh_next example.pdf --glossary-ignore-other`                                                                    |
| `--glossary-ignore-custom`       | ignore custom words when matching glossary entries (default: `false`)                | `pdf2zh_next example.pdf --glossary-ignore-custom`                                                                   |
| `--glossary-ignore-list`         | path to a file containing words to ignore (default: `None`)                          | `pdf2zh_next example.pdf --glossary-ignore-list ignore_words.txt`                                                     |

---

### TRANSLATION RESULT

| `--save-auto-extracted-glossary` | enregistrer le glossaire extrait automatiquement                                        | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--save-manual-glossary`        | enregistrer le glossaire ajouté manuellement                                           | `pdf2zh_next example.pdf --save-manual-glossary`                                                                     |
| `--save-all-glossary`           | enregistrer tous les glossaires (extraits automatiquement et ajoutés manuellement)      | `pdf2zh_next example.pdf --save-all-glossary`                                                                        |
| `--glossary`                    | chemin vers le fichier de glossaire (par défaut : `glossary.json`, `glossary.yaml`, `glossary.yml`) | `pdf2zh_next example.pdf --glossary custom_glossary.json`                                                             |
| `--glossary-format`             | format du fichier de glossaire (par défaut : `auto`)                                   | `pdf2zh_next example.pdf --glossary-format json`                                                                     |
| `--glossary-save-format`        | format pour enregistrer le fichier de glossaire (par défaut : `auto`)                  | `pdf2zh_next example.pdf --glossary-save-format yaml`                                                                 |
| `--glossary-save-path`          | chemin pour enregistrer le fichier de glossaire (par défaut : `glossary.json`)         | `pdf2zh_next example.pdf --glossary-save-path custom_glossary.json`                                                   |
| `--glossary-save-auto`          | enregistrer automatiquement le glossaire après la traduction (par défaut : `false`)    | `pdf2zh_next example.pdf --glossary-save-auto`                                                                       |
| `--glossary-save-manual`        | enregistrer le glossaire ajouté manuellement après la traduction (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-save-manual`                                                                     |
| `--glossary-save-all`           | enregistrer tous les glossaires après la traduction (par défaut : `false`)             | `pdf2zh_next example.pdf --glossary-save-all`                                                                        |
| `--glossary-auto-extract`       | extraire automatiquement le glossaire du document (par défaut : `true`)                | `pdf2zh_next example.pdf --glossary-auto-extract false`                                                               |
| `--glossary-manual-add`         | ajouter manuellement des entrées de glossaire (par défaut : `true`)                    | `pdf2zh_next example.pdf --glossary-manual-add false`                                                                 |
| `--glossary-use`                | utiliser le glossaire pendant la traduction (par défaut : `true`)                      | `pdf2zh_next example.pdf --glossary-use false`                                                                       |
| `--glossary-update`             | mettre à jour le glossaire pendant la traduction (par défaut : `true`)                 | `pdf2zh_next example.pdf --glossary-update false`                                                                    |
| `--glossary-ignore-case`        | ignorer la casse lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-case`                                                                     |
| `--glossary-ignore-punctuation` | ignorer la ponctuation lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-punctuation`                                                              |
| `--glossary-ignore-whitespace`  | ignorer les espaces blancs lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-whitespace`                                                               |
| `--glossary-ignore-digits`      | ignorer les chiffres lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-digits`                                                                   |
| `--glossary-ignore-symbols`      | ignorer les symboles lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-symbols`                                                                  |
| `--glossary-ignore-accents`      | ignorer les accents lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-accents`                                                                  |
| `--glossary-ignore-articles`     | ignorer les articles lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-articles`                                                                 |
| `--glossary-ignore-prepositions` | ignorer les prépositions lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-prepositions`                                                             |
| `--glossary-ignore-conjunctions` | ignorer les conjonctions lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-conjunctions`                                                              |
| `--glossary-ignore-pronouns`     | ignorer les pronoms lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-pronouns`                                                                 |
| `--glossary-ignore-verbs`        | ignorer les verbes lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-verbs`                                                                    |
| `--glossary-ignore-nouns`        | ignorer les noms lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-nouns`                                                                    |
| `--glossary-ignore-adjectives`   | ignorer les adjectifs lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-adjectives`                                                               |
| `--glossary-ignore-adverbs`      | ignorer les adverbes lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-adverbs`                                                                  |
| `--glossary-ignore-other`        | ignorer les autres mots lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-other`                                                                    |
| `--glossary-ignore-custom`       | ignorer les mots personnalisés lors de la correspondance des entrées du glossaire (par défaut : `false`) | `pdf2zh_next example.pdf --glossary-ignore-custom`                                                                   |
| `--glossary-ignore-list`         | chemin vers un fichier contenant des mots à ignorer (par défaut : `None`)              | `pdf2zh_next example.pdf --glossary-ignore-list ignore_words.txt`                                                     |
| `--pool-max-workers`            | Nombre maximum de travailleurs pour le pool de traduction. Si non défini, utilisera qps comme nombre de travailleurs | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--term-api-key`                | API key for term extraction translation service. If not set, will follow `--api-key`.   | `pdf2zh_next example.pdf --term-api-key sk-xxxxxx`                                                                    |
| `--term-endpoint`               | Endpoint for term extraction translation service. If not set, will follow `--endpoint`. | `pdf2zh_next example.pdf --term-endpoint https://api.openai.com/v1/chat/completions`                                  |
| `--term-model`                  | Model for term extraction translation service. If not set, will follow `--model`.       | `pdf2zh_next example.pdf --term-model gpt-4o-mini`                                                                    |
| `--term-max-tokens`             | Max tokens for term extraction translation service. If not set, will follow `--max-tokens`. | `pdf2zh_next example.pdf --term-max-tokens 1000`                                                                   |
| `--term-temperature`            | Temperature for term extraction translation service. If not set, will follow `--temperature`. | `pdf2zh_next example.pdf --term-temperature 0.1`                                                                   |
| `--term-timeout`                | Timeout for term extraction translation service. If not set, will follow `--timeout`.   | `pdf2zh_next example.pdf --term-timeout 30`                                                                           |
| `--term-request-interval`       | Request interval for term extraction translation service. If not set, will follow `--request-interval`. | `pdf2zh_next example.pdf --term-request-interval 0.2`                                                              |
| `--term-max-retries`            | Max retries for term extraction translation service. If not set, will follow `--max-retries`. | `pdf2zh_next example.pdf --term-max-retries 5`                                                                     |
| `--term-backoff-factor`         | Backoff factor for term extraction translation service. If not set, will follow `--backoff-factor`. | `pdf2zh_next example.pdf --term-backoff-factor 0.5`                                                                |
| `--term-proxy`                  | Proxy for term extraction translation service. If not set, will follow `--proxy`.       | `pdf2zh_next example.pdf --term-proxy http://127.0.0.1:7890`                                                          |
| `--term-extra-body`             | Extra body for term extraction translation service. If not set, will follow `--extra-body`. | `pdf2zh_next example.pdf --term-extra-body '{"presence_penalty": 0, "frequency_penalty": 0}'`                        |
| `--term-extra-headers`          | Extra headers for term extraction translation service. If not set, will follow `--extra-headers`. | `pdf2zh_next example.pdf --term-extra-headers '{"X-Custom-Header": "value"}'`                                        |
| `--term-extra-query-parameters` | Extra query parameters for term extraction translation service. If not set, will follow `--extra-query-parameters`. | `pdf2zh_next example.pdf --term-extra-query-parameters '{"param": "value"}'`                                          |

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

| `--term-qps`                    | Limite de QPS pour le service de traduction d'extraction de termes. Si non défini, suivra qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `--term-api-key`                | Clé API pour le service de traduction d'extraction de termes. Si non défini, suivra `--api-key`.        | `pdf2zh_next example.pdf --term-api-key sk-xxxxxx`                                                                    |
| `--term-endpoint`               | Point de terminaison pour le service de traduction d'extraction de termes. Si non défini, suivra `--endpoint`. | `pdf2zh_next example.pdf --term-endpoint https://api.openai.com/v1/chat/completions`                                  |
| `--term-model`                  | Modèle pour le service de traduction d'extraction de termes. Si non défini, suivra `--model`.           | `pdf2zh_next example.pdf --term-model gpt-4o-mini`                                                                    |
| `--term-max-tokens`             | Nombre maximum de tokens pour le service de traduction d'extraction de termes. Si non défini, suivra `--max-tokens`. | `pdf2zh_next example.pdf --term-max-tokens 1000`                                                                   |
| `--term-temperature`            | Température pour le service de traduction d'extraction de termes. Si non défini, suivra `--temperature`. | `pdf2zh_next example.pdf --term-temperature 0.1`                                                                   |
| `--term-timeout`                | Délai d'attente pour le service de traduction d'extraction de termes. Si non défini, suivra `--timeout`. | `pdf2zh_next example.pdf --term-timeout 30`                                                                           |
| `--term-request-interval`       | Intervalle de requête pour le service de traduction d'extraction de termes. Si non défini, suivra `--request-interval`. | `pdf2zh_next example.pdf --term-request-interval 0.2`                                                              |
| `--term-max-retries`            | Nombre maximum de tentatives pour le service de traduction d'extraction de termes. Si non défini, suivra `--max-retries`. | `pdf2zh_next example.pdf --term-max-retries 5`                                                                     |
| `--term-backoff-factor`         | Facteur de backoff pour le service de traduction d'extraction de termes. Si non défini, suivra `--backoff-factor`. | `pdf2zh_next example.pdf --term-backoff-factor 0.5`                                                                |
| `--term-proxy`                  | Proxy pour le service de traduction d'extraction de termes. Si non défini, suivra `--proxy`.            | `pdf2zh_next example.pdf --term-proxy http://127.0.0.1:7890`                                                          |
| `--term-extra-body`             | Corps supplémentaire pour le service de traduction d'extraction de termes. Si non défini, suivra `--extra-body`. | `pdf2zh_next example.pdf --term-extra-body '{"presence_penalty": 0, "frequency_penalty": 0}'`                        |
| `--term-extra-headers`          | En-têtes supplémentaires pour le service de traduction d'extraction de termes. Si non défini, suivra `--extra-headers`. | `pdf2zh_next example.pdf --term-extra-headers '{"X-Custom-Header": "value"}'`                                        |
| `--term-extra-query-parameters` | Paramètres de requête supplémentaires pour le service de traduction d'extraction de termes. Si non défini, suivra `--extra-query-parameters`. | `pdf2zh_next example.pdf --term-extra-query-parameters '{"param": "value"}'`                                          |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| `--term-pool-max-workers`       | Nombre maximum de travailleurs pour le pool de traduction d'extraction de termes. Si non défini ou 0, suivra pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |

---

### OUTPUT

| `--term-pool-max-workers`       | Nombre maximum de travailleurs pour le pool de traduction d'extraction de termes. Si non défini ou 0, suivra pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-auto-translate-reference` | Disable auto translate reference                                                        | `pdf2zh_next example.pdf --no-auto-translate-reference`                                                               |
| `--no-auto-translate-figure`    | Disable auto translate figure                                                           | `pdf2zh_next example.pdf --no-auto-translate-figure`                                                                  |
| `--no-auto-translate-table`     | Disable auto translate table                                                            | `pdf2zh_next example.pdf --no-auto-translate-table`                                                                   |
| `--no-auto-translate-equation`  | Disable auto translate equation                                                         | `pdf2zh_next example.pdf --no-auto-translate-equation`                                                                |
| `--no-auto-translate-algorithm` | Disable auto translate algorithm                                                        | `pdf2zh_next example.pdf --no-auto-translate-algorithm`                                                               |
| `--no-auto-translate-title`     | Disable auto translate title                                                            | `pdf2zh_next example.pdf --no-auto-translate-title`                                                                   |
| `--no-auto-translate-abstract`  | Disable auto translate abstract                                                         | `pdf2zh_next example.pdf --no-auto-translate-abstract`                                                                |
| `--no-auto-translate-keywords`  | Disable auto translate keywords                                                         | `pdf2zh_next example.pdf --no-auto-translate-keywords`                                                                |
| `--no-auto-translate-caption`   | Disable auto translate caption                                                          | `pdf2zh_next example.pdf --no-auto-translate-caption`                                                                 |
| `--no-auto-translate-body`      | Disable auto translate body                                                             | `pdf2zh_next example.pdf --no-auto-translate-body`                                                                    |
| `--skip-translation`            | Skip translation process, only extract text and glossary                                | `pdf2zh_next example.pdf --skip-translation`                                                                          |
| `--skip-extract-glossary`       | Skip extract glossary process                                                           | `pdf2zh_next example.pdf --skip-extract-glossary`                                                                     |
| `--skip-figure`                 | Skip figure processing                                                                  | `pdf2zh_next example.pdf --skip-figure`                                                                               |
| `--skip-table`                  | Skip table processing                                                                   | `pdf2zh_next example.pdf --skip-table`                                                                                |
| `--skip-equation`               | Skip equation processing                                                                | `pdf2zh_next example.pdf --skip-equation`                                                                             |
| `--skip-algorithm`              | Skip algorithm processing                                                               | `pdf2zh_next example.pdf --skip-algorithm`                                                                            |
| `--skip-title`                  | Skip title processing                                                                   | `pdf2zh_next example.pdf --skip-title`                                                                                |
| `--skip-abstract`               | Skip abstract processing                                                                | `pdf2zh_next example.pdf --skip-abstract`                                                                             |
| `--skip-keywords`               | Skip keywords processing                                                                | `pdf2zh_next example.pdf --skip-keywords`                                                                             |
| `--skip-caption`                | Skip caption processing                                                                 | `pdf2zh_next example.pdf --skip-caption`                                                                              |
| `--skip-body`                   | Skip body processing                                                                    | `pdf2zh_next example.pdf --skip-body`                                                                                 |
| `--skip-reference`              | Skip reference processing                                                               | `pdf2zh_next example.pdf --skip-reference`                                                                            |
| `--skip-footnote`               | Skip footnote processing                                                                | `pdf2zh_next example.pdf --skip-footnote`                                                                             |
| `--skip-header`                 | Skip header processing                                                                  | `pdf2zh_next example.pdf --skip-header`                                                                               |
| `--skip-footer`                 | Skip footer processing                                                                  | `pdf2zh_next example.pdf --skip-footer`                                                                               |
| `--skip-page-number`            | Skip page number processing                                                             | `pdf2zh_next example.pdf --skip-page-number`                                                                          |
| `--skip-toc`                    | Skip table of contents processing                                                       | `pdf2zh_next example.pdf --skip-toc`                                                                                  |
| `--skip-index`                  | Skip index processing                                                                   | `pdf2zh_next example.pdf --skip-index`                                                                                |
| `--skip-bibliography`           | Skip bibliography processing                                                            | `pdf2zh_next example.pdf --skip-bibliography`                                                                         |
| `--skip-appendix`               | Skip appendix processing                                                                | `pdf2zh_next example.pdf --skip-appendix`                                                                             |
| `--skip-acknowledgements`       | Skip acknowledgements processing                                                        | `pdf2zh_next example.pdf --skip-acknowledgements`                                                                     |
| `--skip-dedication`             | Skip dedication processing                                                              | `pdf2zh_next example.pdf --skip-dedication`                                                                           |
| `--skip-preface`                | Skip preface processing                                                                 | `pdf2zh_next example.pdf --skip-preface`                                                                              |
| `--skip-foreword`               | Skip foreword processing                                                                | `pdf2zh_next example.pdf --skip-foreword`                                                                             |
| `--skip-introduction`           | Skip introduction processing                                                            | `pdf2zh_next example.pdf --skip-introduction`                                                                         |
| `--skip-conclusion`             | Skip conclusion processing                                                              | `pdf2zh_next example.pdf --skip-conclusion`                                                                           |
| `--skip-annex`                  | Skip annex processing                                                                   | `pdf2zh_next example.pdf --skip-annex`                                                                                |
| `--skip-glossary`               | Skip glossary processing                                                                | `pdf2zh_next example.pdf --skip-glossary`                                                                             |
| `--skip-abbreviations`          | Skip abbreviations processing                                                           | `pdf2zh_next example.pdf --skip-abbreviations`                                                                        |
| `--skip-symbols`                | Skip symbols processing                                                                 | `pdf2zh_next example.pdf --skip-symbols`                                                                              |
| `--skip-nomenclature`           | Skip nomenclature processing                                                            | `pdf2zh_next example.pdf --skip-nomenclature`                                                                         |
| `--skip-acronyms`               | Skip acronyms processing                                                                | `pdf2zh_next example.pdf --skip-acronyms`                                                                             |
| `--skip-cover`                  | Skip cover processing                                                                   | `pdf2zh_next example.pdf --skip-cover`                                                                                |
| `--skip-title-page`             | Skip title page processing                                                              | `pdf2zh_next example.pdf --skip-title-page`                                                                           |
| `--skip-copyright`              | Skip copyright processing                                                               | `pdf2zh_next example.pdf --skip-copyright`                                                                            |
| `--skip-dedication-page`        | Skip dedication page processing                                                         | `pdf2zh_next example.pdf --skip-dedication-page`                                                                      |
| `--skip-epigraph`               | Skip epigraph processing                                                                | `pdf2zh_next example.pdf --skip-epigraph`                                                                             |
| `--skip-table-of-contents`      | Skip table of contents processing                                                       | `pdf2zh_next example.pdf --skip-table-of-contents`                                                                    |
| `--skip-list-of-figures`        | Skip list of figures processing                                                         | `pdf2zh_next example.pdf --skip-list-of-figures`                                                                      |
| `--skip-list-of-tables`         | Skip list of tables processing                                                          | `pdf2zh_next example.pdf --skip-list-of-tables`                                                                       |
| `--skip-list-of-algorithms`     | Skip list of algorithms processing                                                      | `pdf2zh_next example.pdf --skip-list-of-algorithms`                                                                   |
| `--skip-list-of-equations`      | Skip list of equations processing                                                       | `pdf2zh_next example.pdf --skip-list-of-equations`                                                                    |
| `--skip-list-of-abbreviations`  | Skip list of abbreviations processing                                                   | `pdf2zh_next example.pdf --skip-list-of-abbreviations`                                                                |
| `--skip-list-of-symbols`        | Skip list of symbols processing                                                         | `pdf2zh_next example.pdf --skip-list-of-symbols`                                                                      |
| `--skip-list-of-acronyms`       | Skip list of acronyms processing                                                        | `pdf2zh_next example.pdf --skip-list-of-acronyms`                                                                     |
| `--skip-list-of-nomenclature`   | Skip list of nomenclature processing                                                    | `pdf2zh_next example.pdf --skip-list-of-nomenclature`                                                                 |
| `--skip-bibliography-page`      | Skip bibliography page processing                                                       | `pdf2zh_next example.pdf --skip-bibliography-page`                                                                    |
| `--skip-index-page`             | Skip index page processing                                                              | `pdf2zh_next example.pdf --skip-index-page`                                                                           |
| `--skip-appendix-page`          | Skip appendix page processing                                                           | `pdf2zh_next example.pdf --skip-appendix-page`                                                                        |
| `--skip-acknowledgements-page`  | Skip acknowledgements page processing                                                   | `pdf2zh_next example.pdf --skip-acknowledgements-page`                                                                |
| `--skip-dedication-page`        | Skip dedication page processing                                                         | `pdf2zh_next example.pdf --skip-dedication-page`                                                                      |
| `--skip-preface-page`           | Skip preface page processing                                                            | `pdf2zh_next example.pdf --skip-preface-page`                                                                         |
| `--skip-foreword-page`          | Skip foreword page processing                                                           | `pdf2zh_next example.pdf --skip-foreword-page`                                                                        |
| `--skip-introduction-page`      | Skip introduction page processing                                                       | `pdf2zh_next example.pdf --skip-introduction-page`                                                                    |
| `--skip-conclusion-page`        | Skip conclusion page processing                                                         | `pdf2zh_next example.pdf --skip-conclusion-page`                                                                      |
| `--skip-annex-page`             | Skip annex page processing                                                              | `pdf2zh_next example.pdf --skip-annex-page`                                                                           |
| `--skip-glossary-page`          | Skip glossary page processing                                                           | `pdf2zh_next example.pdf --skip-glossary-page`                                                                        |
| `--skip-abbreviations-page`     | Skip abbreviations page processing                                                      | `pdf2zh_next example.pdf --skip-abbreviations-page`                                                                   |
| `--skip-symbols-page`           | Skip symbols page processing                                                            | `pdf2zh_next example.pdf --skip-symbols-page`                                                                         |
| `--skip-nomenclature-page`      | Skip nomenclature page processing                                                       | `pdf2zh_next example.pdf --skip-nomenclature-page`                                                                    |
| `--skip-acronyms-page`          | Skip acronyms page processing                                                           | `pdf2zh_next example.pdf --skip-acronyms-page`                                                                        |
| `--skip-cover-page`             | Skip cover page processing                                                              | `pdf2zh_next example.pdf --skip-cover-page`                                                                           |
| `--skip-title-page`             | Skip title page processing                                                              | `pdf2zh_next example.pdf --skip-title-page`                                                                           |
| `--skip-copyright-page`         | Skip copyright page processing                                                          | `pdf2zh_next example.pdf --skip-copyright-page`                                                                       |
| `--skip-epigraph-page`          | Skip epigraph page processing                                                           | `pdf 极速中文版 example.pdf --skip-epigraph-page`                                                                      |

---

### OUTPUT

| `--no-auto-extract-glossary`    | Désactiver l'extraction automatique du glossaire                                         | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-auto-translate-reference` | Désactiver la traduction automatique des références                                      | `pdf2zh_next example.pdf --no-auto-translate-reference`                                                               |
| `--no-auto-translate-figure`    | Désactiver la traduction automatique des figures                                         | `pdf 极速中文版 example.pdf --no-auto-translate-figure`                                                                  |
| `--no-auto-translate-table`     | Désactiver la traduction automatique des tableaux                                        | `pdf2zh_next example.pdf --no-auto-translate-table`                                                                   |
| `--极速中文版-translate-equation`  | Désactiver la traduction automatique des équations                                       | `pdf2zh_next example.pdf --no-auto-translate-equation`                                                                |
| `--no-auto-translate-algorithm` | Désactiver la traduction automatique des algorithmes                                     | `pdf2zh_next example.pdf --no-auto-translate-algorithm`                                                               |
| `--no-auto-translate-title`     | Désactiver la traduction automatique des titres                                          | `pdf2zh_next example.pdf --no-auto-translate-title`                                                                   |
| `--no-auto-translate-abstract`  | Désactiver la traduction automatique des résumés                                         | `pdf2zh_next example.pdf --no-auto-translate-abstract`                                                                |
| `--no-auto-translate-keywords`  | Désactiver la traduction automatique des mots-clés                                       | `pdf2zh_next example.pdf --no-auto-translate-keywords`                                                                |
| `--no-auto-translate-caption`   | Désactiver la traduction automatique des légendes                                        | `pdf2zh_next example.pdf --no-auto-translate-caption`                                                                 |
| `--no-auto-translate-body`      | Désactiver la traduction automatique du corps de texte                                   | `pdf2zh_next example.pdf --no-auto-translate-body`                                                                    |
| `--skip-translation`            | Sauter le processus de traduction, extraire uniquement le texte et le glossaire          | `pdf2zh_next example.pdf --skip-translation`                                                                          |
| `--skip-extract-glossary`       | Sauter le processus d'extraction du glossaire                                            | `pdf2zh_next example.pdf --skip-extract-glossary`                                                                     |
| `--skip-figure`                 | Sauter le traitement des figures                                                         | `pdf2zh_next example.pdf --skip-figure`                                                                               |
| `--skip-table`                  | Sauter le traitement des tableaux                                                        | `pdf2zh_next example.pdf --skip-table`                                                                                |
| `--skip-equation`               | Sauter le traitement des équations                                                       | `pdf2zh_next example.pdf --skip-equation`                                                                             |
| `--skip-algorithm`              | Sauter le traitement des algorithmes                                                     | `pdf2zh_next example.pdf --极速中文版-algorithm`                                                                            |
| `--skip-title`                  | Sauter le traitement des titres                                                          | `pdf2zh_next example.pdf --skip-title`                                                                                |
| `--skip-abstract`               | Sauter le traitement des résumés                                                         | `pdf2zh_next example.pdf --skip-abstract`                                                                             |
| `--skip-keywords`               | Sauter le traitement des mots-clés                                                       | `pdf2zh_next example 极速中文版 --skip-keywords`                                                                             |
| `--skip-caption`                | Sauter le traitement des légendes                                                        | `pdf2zh_next example.pdf --skip-caption`                                                                              |
| `--skip-body`                   | Sauter le traitement du corps de texte                                                   | `pdf2zh_next example.pdf --skip-body`                                                                                 |
| `--skip-reference`              | Sauter le traitement des références                                                      | `pdf2zh_next example.pdf --skip-reference`                                                                            |
| `--skip-footnote`               | Sauter le traitement des notes de bas de page                                            | `pdf2zh_next example.pdf --skip-footnote`                                                                             |
| `--skip-header`                 | Sauter le traitement des en-têtes                                                        | `pdf2zh_next example.pdf --skip-header`                                                                               |
| `--skip-footer`                 | Sauter le traitement des pieds de page                                                   | `pdf2zh_next example.pdf --skip-footer`                                                                               |
| `--skip-page-number`            | Sauter le traitement des numéros de page                                                 | `pdf2zh_next example.pdf --skip-page-number`                                                                          |
| `--skip-toc`                    | Sauter le traitement de la table des matières                                            | `pdf2zh_next example.pdf --skip-t 极速中文版`                                                                                  |
| `--skip-index`                  | Sauter le traitement de l'index                                                          | `pdf2zh_next example.pdf --skip-index`                                                                                |
| `--skip-bibliography`           | Sauter le traitement de la bibliographie                                                 | `pdf2zh_next example.pdf --skip-bibliography`                                                                         |
| `--skip-appendix`               | Sauter le traitement de l'annexe                                                         | `pdf2zh_next example.pdf --skip-appendix`                                                                             |
| `--skip-acknowledgements`       | Sauter le traitement des remerciements                                                   | `pdf2zh_next example.pdf --skip-acknowledgements`                                                                     |
| `--skip-dedication`             | Sauter le traitement de la dédicace                                                      | `pdf2zh_next example.pdf --skip-dedication`                                                                           |
| `--skip-preface`                | Sauter le traitement de la préface                                                       | `pdf2zh_next example.pdf --skip-preface`                                                                              |
| `--skip-foreword`               | Sauter le traitement de l'avant-propos                                                   | `pdf2zh_next example.pdf --skip-foreword`                                                                             |
| `--skip-introduction`           | Sauter le traitement de l'introduction                                                   | `pdf2zh_next example.pdf --skip-introduction`                                                                         |
| `--skip-conclusion` 极速中文版         | Sauter le traitement de la conclusion                                                    | `pdf2zh_next example.pdf --skip-conclusion`                                                                           |
| `--skip-annex`                  | Sauter le traitement de l'annexe                                                         | `pdf2zh_next example.pdf --skip-annex`                                                                                |
| `--skip-glossary`               | Sauter le traitement du glossaire                                                        | `pdf2zh_next example.pdf --skip-glossary`                                                                             |
| `--skip-abbreviations`          | Sauter le traitement des abréviations                                                    | `pdf2zh_next example.pdf --skip-abbreviations`                                                                        |
| `--skip-symbols`                | Sauter le traitement des symboles                                                        | `pdf2zh_next example.pdf --skip-symbols`                                                                              |
| `--skip-nomenclature`           | Sauter le traitement de la nomenclature                                                  | `pdf2zh_next example.pdf --skip-nomenclature`                                                                         |
| `--skip-acronyms`               | Sauter le traitement des acronymes                                                       | `pdf2zh_next example.pdf --skip-acronyms`                                                                             |
| `--skip-cover`                  | Sauter le traitement de la couverture                                                    | `pdf2zh_next example.pdf --skip-cover`                                                                                |
| `--skip-title-page`             | Sauter le traitement de la page de titre                                                 | `pdf2zh_next example.pdf --skip-title-page`                                                                           |
| `--skip-copyright`              | Sauter le traitement du copyright                                                        | `pdf2zh_next example.pdf --skip-copyright`                                                                            |
| `--skip-dedication-page`        | Sauter le traitement de la page de dédicace                                              | `pdf2zh_next example.pdf --skip-dedication-page`                                                                      |
| `--skip-epigraph`               | Sauter le traitement de l'épigraphe                                                      | `pdf2zh_next example.pdf --skip-epigraph`                                                                             |
| `--skip-table-of-contents`      | Sauter le traitement de la table des matières                                            | `pdf2zh_next example.pdf --skip-table-of-contents`                                                                    |
| `--skip-list-of-figures`        | Sauter le traitement de la liste des figures                                             | `pdf2zh_next example.pdf --skip-list-of-figures`                                                                      |
| `--skip-list-of-tables`         | Sauter le traitement de la liste des tableaux                                            | `pdf2zh_next example.pdf --skip-list-of-tables`                                                                       |
| `--skip-list-of-algorithms`     | Sauter le traitement de la liste des algorithmes                                         | `pdf2zh_next example.pdf --skip-list-of-algorithms`                                                                   |
| `--skip-list-of-equations`      | Sauter le traitement de la liste des équations                                           | `pdf2zh_next example.pdf --skip-list-of-equations`                                                                    |
| `--skip-list-of-abbreviations`  | Sauter le traitement de la liste des abréviations                                        | `pdf2zh_next example.pdf --skip-list-of-abbreviations`                                                                |
| `--skip-list-of-symbols 极速中文版       | Sauter le traitement de la liste des symboles                                            | `pdf2zh_next example.pdf --skip-list-of-symbols`                                                                      |
| `--skip-list-of-acronyms`       | Sauter le traitement de la liste des acronymes                                           | `pdf2zh_next example.pdf --skip-list-of-acronyms`                                                                     |
| `--skip-list-of-nomenclature`   | Sauter le traitement de la liste de nomenclature                                         | `pdf2zh_next example.pdf --skip-list-of-nomenclature`                                                                 |
| `--skip-bibliography-page`      | Sauter le traitement de la page de bibliographie                                         | `pdf2zh_next example.pdf --skip-bibliography-page`                                                                    |
| `--skip-index-page`             | Sauter le traitement de la page d'index                                                  | `pdf2zh_next example.pdf --skip-index-page`                                                                           |
| `--skip-appendix-page`          | Sauter le traitement de la page d'annexe                                                 | `pdf2zh_next example.pdf --skip-appendix-page`                                                                        |
| `--skip-acknowledgements-page`  | Sauter le traitement de la page de remerciements                                         | `pdf2zh_next example.pdf --skip-acknowledgements-page`                                                                |
| `--skip-dedication-page`        | Sauter le traitement de la page de dédicace                                              | `pdf2zh_next example.pdf --skip-dedication-page`                                                                      |
| `--skip-preface-page`           | Sauter le traitement de la page de préface                                               | `pdf2zh_next example.pdf --skip-preface-page`                                                                         |
| `--skip-foreword-page`          | Sauter le traitement de la page d'avant-propos                                           | `pdf2zh_next example.pdf --skip-foreword-page`                                                                        |
| `--skip-introduction-page`      | Sauter le traitement de la page d'introduction                                           | `pdf2zh_next example.pdf --skip-introduction-page`                                                                    |
| `--skip-conclusion-page`        | Sauter le traitement de la page de conclusion                                            | `pdf2zh_next example.pdf --skip-conclusion-page`                                                                      |
| `--skip-annex-page`             | Sauter le traitement de la page d'annexe                                                 | `pdf2zh_next example.pdf --skip-annex-page`                                                                           |
| `--skip-glossary-page`          | Sauter le traitement de la page de glossaire                                             | `pdf2zh_next example.pdf --skip-glossary-page`                                                                        |
| `--skip-abbreviations-page`     | Sauter le traitement de la page d'abréviations                                           | `pdf2zh_next example.pdf --skip-abbreviations-page`                                                                   |
| `--skip-symbols-page`           | Sauter le traitement de la page de symboles                                              | `pdf2zh_next example.pdf --skip-symbols-page`                                                                         |
| `--skip-nomenclature-page`      | Sauter le traitement de la page de nomenclature                                          | `pdf2zh_next example.pdf --skip-nomenclature-page`                                                                    |
| `--skip-acronyms-page`          | Sauter le traitement de la page d'acronymes                                              | `pdf2zh_next example.pdf --skip-acronyms-page`                                                                        |
| `--skip-cover-page`             | Sauter le traitement de la page de couverture                                            | `pdf2zh_next example.pdf --skip-cover-page`                                                                           |
| `--skip-title-page`             | Sauter le traitement de la page de titre                                                 | `pdf2zh_next example.pdf --skip-title-page`                                                                           |
| `--skip-copyright-page`         | Sauter le traitement de la page de copyright                                             | `pdf2zh_next example.pdf --skip-copyright-page`                                                                       |
| `--skip-epigraph-page`          | Sauter le traitement de la page d'épigraphe                                              | `pdf2zh_next example.pdf --skip-epigraph-page`                                                                        |
| `--primary-font-family`         | Remplace la famille de police principale pour le texte traduit. Choix : 'serif' pour les polices à empattements, 'sans-serif' pour les polices sans empattements, 'script' pour les polices script/italiques. Si non spécifié, utilise la sélection automatique de police basée sur les propriétés du texte original. | `pdf2zh_next example.pdf --primary-font-family serif` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-v`, `--version`               | Display the version information                                                         | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Show help information                                                                   | `pdf2zh_next -h`                                                                                                      |

---

### OUTPUT

| `--no-dual`                     | Ne pas générer de fichiers PDF bilingues                                                | `pdf2zh_next example.pdf --no-dual`                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-v`, `--version`               | Afficher les informations de version                                                    | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Afficher l'aide                                                                         | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-trans`                    | Do not output translated PDF files                                                      | `pdf2zh_next example.pdf --no-trans`                                                                                  |
| `--no-ocr`                      | Do not output OCRed PDF files                                                           | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--no-pdf`                      | Do not output any PDF files. This option is useful when you only need the text output.   | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--ocr-only`                    | Only run the OCR process. This option implies `--no-trans` and `--no-mono`.             | `pdf2zh_next example.pdf --ocr-only`                                                                                  |
| `--trans-only`                  | Only run the translation process. This option implies `--no-ocr` and `--no-mono`.       | `pdf2zh_next example.pdf --trans-only`                                                                                |
| `--mono-only`                   | Only run the monolingual PDF generation process. This option implies `--no-ocr` and `--no-trans`. | `pdf2zh_next example.pdf --mono-only`                                                                                 |

---

### TRANSLATION RESULT

| `--no-mono`                     | Ne pas générer de fichiers PDF monolingues                                                | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-trans`                    | Ne pas générer de fichiers PDF traduits                                                 | `pdf2zh_next example.pdf --no-trans`                                                                                  |
| `--no-ocr`                      | Ne pas générer de fichiers PDF OCRisés                                                  | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--no-pdf`                      | Ne générer aucun fichier PDF. Cette option est utile lorsque vous n'avez besoin que de la sortie texte. | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--ocr-only`                    | Exécuter uniquement le processus OCR. Cette option implique `--no-trans` et `--no-mono`. | `pdf2zh_next example.pdf --ocr-only`                                                                                  |
| `--trans-only`                  | Exécuter uniquement le processus de traduction. Cette option implique `--no-ocr` et `--no-mono`. | `pdf2zh_next example.pdf --trans-only`                                                                                |
| `--mono-only`                   | Exécuter uniquement le processus de génération de PDF monolingue. Cette option implique `--no-ocr` et `--no-trans`. | `pdf2zh_next example.pdf --mono-only`                                                                                 |
`string` | `null`       |
| `--formular-font-size`          | Font size to identify formula text                                                      | `pdf2zh_next example.pdf --formular-font-size 10.5`                                                                   | `float`  | `null`       |
| `--formular-font-size-offset`   | Font size offset to identify formula text                                               | `pdf2zh_next example.pdf --formular-font-size-offset 0.5`                                                             | `float`  | `null`       |
| `--formular-font-bold`          | Whether to identify bold text as formula                                                | `pdf2zh_next example.pdf --formular-font-bold`                                                                        | `boolean`| `false`      |
| `--formular-font-italic`        | Whether to identify italic text as formula                                              | `pdf2zh_next example.pdf --formular-font-italic`                                                                      | `boolean`| `false`      |
| `--formular-font-margin`        | Margin to identify formula text                                                         | `pdf2zh_next example.pdf --formular-font-margin 0.5`                                                                  | `float`  | `null`       |
| `--formular-font-color`         | Font color to identify formula text                                                     | `pdf2zh_next example.pdf --formular-font-color "#FF0000"`                                                             | `string` | `null`       |
| `--formular-font-color-offset`  | Font color offset to identify formula text                                              | `pdf2zh_next example.pdf --formular-font-color-offset 10`                                                             | `int`    | `null`       |
| `--formular-font-family`        | Font family to identify formula text                                                    | `pdf2zh_next example.pdf --formular-font-family "Times New Roman"`                                                    | `string` | `null`       |

---

### TRANSLATION

| `--formular-font-pattern`       | Modèle de police pour identifier le texte de formule                                    | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            | `string` | `null`       |
| `--formular-font-size`          | Taille de police pour identifier le texte de formule                                    | `pdf2zh_next example.pdf --formular-font-size 10.5`                                                                   | `float`  | `null`       |
| `--formular-font-size-offset`   | Décalage de taille de police pour identifier le texte de formule                        | `pdf2zh_next example.pdf --formular-font-size-offset 0.5`                                                             | `float`  | `null`       |
| `--formular-font-bold`          | Indique si le texte en gras doit être identifié comme formule                           | `pdf2zh_next example.pdf --formular-font-bold`                                                                        | `boolean`| `false`      |
| `--formular-font-italic`        | Indique si le texte en italique doit être identifié comme formule                       | `pdf2zh_next example.pdf --formular-font-italic`                                                                      | `boolean`| `false`      |
| `--formular-font-margin`        | Marge pour identifier le texte de formule                                               | `pdf2zh_next example.pdf --formular-font-margin 0.5`                                                                  | `float`  | `null`       |
| `--formular-font-color`         | Couleur de police pour identifier le texte de formule                                   | `pdf2zh_next example.pdf --formular-font-color "#FF0000"`                                                             | `string` | `null`       |
| `--formular-font-color-offset`  | Décalage de couleur de police pour identifier le texte de formule                       | `pdf2zh_next example.pdf --formular-font-color-offset 10`                                                             | `int`    | `null`       |
| `--formular-font-family`        | Famille de police pour identifier le texte de formule                                   | `pdf2zh_next example.pdf --formular-font-family "Times New Roman"`                                                    | `string` | `null`       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--formular-char-replace`       | Replacement text for formula character                                                  | `pdf2zh_next example.pdf --formular-char-replace "\\text{formula}"`                                                   |
| `--formular-char-ignore-pattern`| Regex pattern to ignore certain characters in formula                                   | `pdf2zh_next example.pdf --formular-char-ignore-pattern "[0-9]"`                                                      |
| `--formular-char-ignore-string` | String to ignore in formula character replacement                                       | `pdf2zh_next example.pdf --formular-char-ignore-string "abc"`                                                         |

---

### OUTPUT

| `--formular-char-pattern`       | Modèle de caractères pour identifier le texte de formule                                 | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--formular-char-replace`       | Texte de remplacement pour le caractère de formule                                      | `pdf2zh_next example.pdf --formular-char-replace "\\text{formula}"`                                                   |
| `--formular-char-ignore-pattern`| Modèle regex pour ignorer certains caractères dans la formule                           | `pdf2zh_next example.pdf --formular-char-ignore-pattern "[0-9]"`                                                      |
| `--formular-char-ignore-string` | Chaîne à ignorer dans le remplacement des caractères de formule                         | `pdf2zh_next example.pdf --formular-char-ignore-string "abc"`                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-split-short-lines`        | Disable splitting short lines into different paragraphs                                 | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--split-paragraphs`            | Split paragraphs into different lines                                                   | `pdf2zh_next example.pdf --split-paragraphs`                                                                          |
| `--no-split-paragraphs`         | Disable splitting paragraphs into different lines                                       | `pdf2zh_next example.pdf --no-split-paragraphs`                                                                       |

---

### OUTPUT

| `--split-short-lines`           | Forcer la division des lignes courtes en paragraphes différents                         | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-split-short-lines`        | Désactiver la division des lignes courtes en paragraphes différents                     | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--split-paragraphs`            | Diviser les paragraphes en lignes différentes                                           | `pdf2zh_next example.pdf --split-paragraphs`                                                                          |
| `--no-split-paragraphs`         | Désactiver la division des paragraphes en lignes différentes                            | `pdf2zh_next example.pdf --no-split-paragraphs`                                                                       |
`1.2`  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------|
| `--short-line-threshold-factor` | Threshold factor for determining short lines                                            | `pdf2zh_next example.pdf --short-line-threshold-factor 0.8`                                                           | `0.8`  |
| `--short-line-length-limit`     | Character limit for short lines                                                         | `pdf2zh_next example.pdf --short-line-length-limit 15`                                                                | `15`   |
| `--short-line-merge-threshold`  | Merge threshold for short lines                                                         | `pdf2zh_next example.pdf --short-line-merge-threshold 0.8`                                                            | `0.8`  |

---

### OUTPUT

| `--short-line-split-factor`     | Facteur de seuil de division pour les lignes courtes                                    | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               | `1.2`  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------|
| `--short-line-threshold-factor` | Facteur de seuil pour déterminer les lignes courtes                                     | `pdf2zh_next example.pdf --short-line-threshold-factor 0.8`                                                           | `0.8`  |
| `--short-line-length-limit`     | Limite de caractères pour les lignes courtes                                            | `pdf2zh_next example.pdf --short-line-length-limit 15`                                                                | `15`   |
| `--short-line-merge-threshold`  | Seuil de fusion pour les lignes courtes                                                 | `pdf2zh_next example.pdf --short-line-merge-threshold 0.8`                                                            | `0.8`  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-format`                 | Skip formatting step                                                                    | `pdf2zh_next example.pdf --skip-format`                                                                               |
| `--skip-math`                   | Skip math translation step                                                              | `pdf2zh_next example.pdf --skip-math`                                                                                 |
| `--skip-docx`                   | Skip DOCX generation step                                                               | `pdf2zh_next example.pdf --skip-docx`                                                                                 |
| `--skip-pdf`                    | Skip PDF generation step                                                                | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--skip-zip`                    | Skip ZIP generation step                                                                | `pdf2zh_next example.pdf --skip-zip`                                                                                  |
| `--skip-embeddings`             | Skip embeddings generation step                                                         | `pdf2zh_next example.pdf --skip-embeddings`                                                                           |
| `--skip-html`                   | Skip HTML generation step                                                               | `pdf2zh_next example.pdf --skip-html`                                                                                 |
| `--skip-epub`                   | Skip EPUB generation step                                                               | `pdf2zh_next example.pdf --skip-epub`                                                                                 |
| `--skip-txt`                    | Skip TXT generation step                                                                | `pdf2zh_next example.pdf --skip-txt`                                                                                  |
| `--skip-json`                   | Skip JSON generation step                                                               | `pdf2zh_next example.pdf --skip-json`                                                                                 |
| `--skip-markdown`               | Skip Markdown generation step                                                           | `pdf2zh_next example.pdf --skip-markdown`                                                                             |
| `--skip-pptx`                   | Skip PPTX generation step                                                               | `pdf2zh_next example.pdf --skip-pptx`                                                                                 |
| `--skip-preview`                | Skip preview generation step                                                            | `pdf2zh_next example.pdf --skip-preview`                                                                              |
| `--skip-all`                    | Skip all generation steps except PDF generation (equivalent to `--skip-translate ...`)  | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--skip-all-except-pdf`         | Skip all generation steps except PDF generation (equivalent to `--skip-translate ...`)  | `pdf2zh_next example.pdf --skip-all-except-pdf`                                                                       |
| `--skip-all-except-docx`        | Skip all generation steps except DOCX generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-docx`                                                                      |
| `--skip-all-except-html`        | Skip all generation steps except HTML generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-html`                                                                      |
| `--skip-all-except-epub`        | Skip all generation steps except EPUB generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-epub`                                                                      |
| `--skip-all-except-txt`         | Skip all generation steps except TXT generation (equivalent to `--skip-translate ...`)  | `pdf2zh_next example.pdf --skip-all-except-txt`                                                                       |
| `--skip-all-except-json`        | Skip all generation steps except JSON generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-json`                                                                      |
| `--skip-all-except-markdown`    | Skip all generation steps except Markdown generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-markdown`                                                                  |
| `--skip-all-except-pptx`        | Skip all generation steps except PPTX generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-pptx`                                                                      |
| `--skip-all-except-preview`     | Skip all generation steps except preview generation (equivalent to `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-preview`                                                                   |

---

### TRANSLATION RESULT

| `--skip-clean`                  | Ignorer l'étape de nettoyage du PDF                                                          | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| :------------------------------ | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Ignorer l'étape de traduction                                                               | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-format`                 | Ignorer l'étape de formatage                                                                | `pdf2zh_next example.pdf --skip-format`                                                                               |
| `--skip-math`                   | Ignorer l'étape de traduction des mathématiques                                             | `pdf2zh_next example.pdf --skip-math`                                                                                 |
| `--skip-docx`                   | Ignorer l'étape de génération du DOCX                                                       | `pdf2zh_next example.pdf --skip-docx`                                                                                 |
| `--skip-pdf`                    | Ignorer l'étape de génération du PDF                                                        | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--skip-zip`                    | Ignorer l'étape de génération du ZIP                                                        | `pdf2zh_next example.pdf --skip-zip`                                                                                  |
| `--skip-embeddings`             | Ignorer l'étape de génération des embeddings                                                | `pdf2zh_next example.pdf --skip-embeddings`                                                                           |
| `--skip-html`                   | Ignorer l'étape de génération du HTML                                                       | `pdf2zh_next example.pdf --skip-html`                                                                                 |
| `--skip-epub`                   | Ignorer l'étape de génération de l'EPUB                                                     | `pdf2zh_next example.pdf --skip-epub`                                                                                 |
| `--skip-txt`                    | Ignorer l'étape de génération du TXT                                                        | `pdf2zh_next example.pdf --skip-txt`                                                                                  |
| `--skip-json`                   | Ignorer l'étape de génération du JSON                                                       | `pdf2zh_next example.pdf --skip-json`                                                                                 |
| `--skip-markdown`               | Ignorer l'étape de génération du Markdown                                                   | `pdf2zh_next example.pdf --skip-markdown`                                                                             |
| `--skip-pptx`                   | Ignorer l'étape de génération du PPTX                                                       | `pdf2zh_next example.pdf --skip-pptx`                                                                                 |
| `--skip-preview`                | Ignorer l'étape de génération de l'aperçu                                                   | `pdf2zh_next example.pdf --skip-preview`                                                                              |
| `--skip-all`                    | Ignorer toutes les étapes de génération sauf la génération de PDF (équivalent à `--skip-translate ...`)  | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--skip-all-except-pdf`         | Ignorer toutes les étapes de génération sauf la génération de PDF (équivalent à `--skip-translate ...`)  | `pdf2zh_next example.pdf --skip-all-except-pdf`                                                                       |
| `--skip-all-except-docx`        | Ignorer toutes les étapes de génération sauf la génération de DOCX (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-docx`                                                                      |
| `--skip-all-except-html`        | Ignorer toutes les étapes de génération sauf la génération de HTML (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-html`                                                                      |
| `--skip-all-except-epub`        | Ignorer toutes les étapes de génération sauf la génération de EPUB (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-epub`                                                                      |
| `--skip-all-except-txt`         | Ignorer toutes les étapes de génération sauf la génération de TXT (équivalent à `--skip-translate ...`)  | `pdf2zh_next example.pdf --skip-all-except-txt`                                                                       |
| `--skip-all-except-json`        | Ignorer toutes les étapes de génération sauf la génération de JSON (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-json`                                                                      |
| `--skip-all-except-markdown`    | Ignorer toutes les étapes de génération sauf la génération de Markdown (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-markdown`                                                                  |
| `--skip-all-except-pptx`        | Ignorer toutes les étapes de génération sauf la génération de PPTX (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-pptx`                                                                      |
| `--skip-all-except-preview`     | Ignorer toutes les étapes de génération sauf la génération de l'aperçu (équivalent à `--skip-translate ...`) | `pdf2zh_next example.pdf --skip-all-except-preview`                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-first`        | Placer les pages traduites en premier en mode PDF double                                | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-first`        | Put translated pages first in dual PDF mode                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-first`        | Placer les pages traduites en premier en mode PDF double                                | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |

---

### OUTPUT

| `--dual-translate-first`        | Placer les pages traduites en premier en mode PDF double                                | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-first`        | Placer les pages traduites en premier en mode PDF double                                | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-first`        | Placer les pages traduites en premier en mode PDF double                                | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-first`        | Placer les pages traduites en premier en mode PDF double                                | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
[Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--disable-math-translate`      | Disable math translation                                                                | `pdf2zh_next example.pdf --disable-math-translate`                                                                     | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-figure-translate`    | Disable figure translation                                                              | `pdf2zh_next example.pdf --disable-figure-translate`                                                                   | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-table-translate`     | Disable table translation                                                               | `pdf2zh_next example.pdf --disable-table-translate`                                                                    | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-code-translate`      | Disable code translation                                                                | `pdf2zh_next example.pdf --disable-code-translate`                                                                     | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-caption-translate`   | Disable caption translation                                                             | `pdf2zh_next example.pdf --disable-caption-translate`                                                                   | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-header-footer`       | Disable header and footer translation                                                   | `pdf2zh_next example.pdf --disable-header-footer`                                                                      | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-footnote-translate`  | Disable footnote translation                                                            | `pdf2zh_next example.pdf --disable-footnote-translate`                                                                  | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-annotation-translate` | Disable annotation translation                                                          | `pdf2zh_next example.pdf --disable-annotation-translate`                                                               | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-reference-translate` | Disable reference translation                                                           | `pdf2zh_next example.pdf --disable-reference-translate`                                                                | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-bibliography-translate` | Disable bibliography translation                                                        | `pdf2zh_next example.pdf --disable-bibliography-translate`                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |

---

### TRANSLATION RESULT

| `--disable-rich-text-translate` | Désactiver la traduction de texte enrichi                                                | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `--disable-math-translate`      | Désactiver la traduction mathématique                                                   | `pdf2zh_next example.pdf --disable-math-translate`                                                                     | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-figure-translate`    | Désactiver la traduction des figures                                                    | `pdf2zh_next example.pdf --disable-figure-translate`                                                                   | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-table-translate`     | Désactiver la traduction des tableaux                                                   | `pdf2zh_next example.pdf --disable-table-translate`                                                                    | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-code-translate`      | Désactiver la traduction du code                                                        | `pdf2zh_next example.pdf --disable-code-translate`                                                                     | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-caption-translate`   | Désactiver la traduction des légendes                                                   | `pdf2zh_next example.pdf --disable-caption-translate`                                                                   | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-header-footer`       | Désactiver la traduction des en-têtes et pieds de page                                  | `pdf2zh_next example.pdf --disable-header-footer`                                                                      | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-footnote-translate`  | Désactiver la traduction des notes de bas de page                                       | `pdf2zh_next example.pdf --disable-footnote-translate`                                                                  | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-annotation-translate` | Désactiver la traduction des annotations                                                | `pdf2zh_next example.pdf --disable-annotation-translate`                                                               | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-reference-translate` | Désactiver la traduction des références                                                 | `pdf2zh_next example.pdf --disable-reference-translate`                                                                | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--disable-bibliography-translate` | Désactiver la traduction de la bibliographie                                            | `pdf2zh_next example.pdf --disable-bibliography-translate`                                                             | [Utilisation de la **Ligne de commande**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--no-enhance-compatibility`    | Disable all compatibility enhancement options                                           | `pdf2zh_next example.pdf --no-enhance-compatibility`                                                                  |
| `--enhance-text-compatibility`  | Enable text compatibility enhancement                                                   | `pdf2zh_next example.pdf --enhance-text-compatibility`                                                                |
| `--no-enhance-text-compatibility` | Disable text compatibility enhancement                                                  | `pdf2zh_next example.pdf --no-enhance-text-compatibility`                                                             |
| `--enhance-table-compatibility` | Enable table compatibility enhancement                                                  | `pdf2zh_next example.pdf --enhance-table-compatibility`                                                               |
| `--no-enhance-table-compatibility` | Disable table compatibility enhancement                                                 | `pdf2zh_next example.pdf --no-enhance-table-compatibility`                                                            |
| `--enhance-equation-compatibility` | Enable equation compatibility enhancement                                               | `pdf2zh_next example.pdf --enhance-equation-compatibility`                                                            |
| `--no-enhance-equation-compatibility` | Disable equation compatibility enhancement                                              | `pdf2zh_next example.pdf --no-enhance-equation-compatibility`                                                         |

---

### TRANSLATION RESULT

| `--enhance-compatibility`       | Activer toutes les options d'amélioration de la compatibilité                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| :------------------------------ | :------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--no-enhance-compatibility`    | Désactiver toutes les options d'amélioration de la compatibilité                                         | `pdf2zh_next example.pdf --no-enhance-compatibility`                                                                  |
| `--enhance-text-compatibility`  | Activer l'amélioration de la compatibilité du texte                                                      | `pdf2zh_next example.pdf --enhance-text-compatibility`                                                                |
| `--no-enhance-text-compatibility` | Désactiver l'amélioration de la compatibilité du texte                                                   | `pdf2zh_next example.pdf --no-enhance-text-compatibility`                                                             |
| `--enhance-table-compatibility` | Activer l'amélioration de la compatibilité des tableaux                                                  | `pdf2zh_next example.pdf --enhance-table-compatibility`                                                               |
| `--no-enhance-table-compatibility` | Désactiver l'amélioration de la compatibilité des tableaux                                               | `pdf2zh_next example.pdf --no-enhance-table-compatibility`                                                            |
| `--enhance-equation-compatibility` | Activer l'amélioration de la compatibilité des équations                                                 | `pdf2zh_next example.pdf --enhance-equation-compatibility`                                                            |
| `--no-enhance-equation-compatibility` | Désactiver l'amélioration de la compatibilité des équations                                              | `pdf2zh_next example.pdf --no-enhance-equation-compatibility`                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |

---

### TRANSLATION RESULT

| `--use-alternating-pages-dual`  | Utiliser le mode pages alternées pour PDF double                                        | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Utiliser le mode pages alternées pour PDF simple                                        | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
`none`             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `--watermark-text`              | Watermark text                                                                          | `pdf2zh_next example.pdf --watermark-text "Translated with PDFMathTranslate"`                                         | `Translated with pdf2zh` |
| `--watermark-font-family`       | Watermark font family                                                                   | `pdf2zh_next example.pdf --watermark-font-family "Times New Roman"`                                                   | `Arial`            |
| `--watermark-font-size`         | Watermark font size                                                                     | `pdf2zh_next example.pdf --watermark-font-size 20`                                                                    | `20`               |
| `--watermark-color`             | Watermark color in hex code                                                             | `pdf2zh_next example.pdf --watermark-color "#FF0000"`                                                                 | `#000000`          |
| `--watermark-rotation`          | Watermark rotation angle in degrees                                                     | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     | `45`               |
| `--watermark-opacity`           | Watermark opacity (0-1)                                                                 | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     | `0.2`              |
| `--watermark-spacing`           | Spacing between watermark texts in points                                               | `pdf2zh_next example.pdf --watermark-spacing 100`                                                                     | `200`              |
| `--watermark-z-index`           | Watermark layer position (higher values are on top)                                     | `pdf2zh_next example.pdf --watermark-z-index 10`                                                                      | `-1`               |

---

### TRANSLATED TEXT

| `--watermark-output-mode`       | Mode de sortie du filigrane pour les fichiers PDF                                        | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `none`             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `--watermark-text`              | Texte du filigrane                                                                      | `pdf2zh_next example.pdf --watermark-text "Translated with PDFMathTranslate"`                                         | `Translated with pdf2zh` |
| `--watermark-font-family`       | Famille de police du filigrane                                                          | `pdf2zh_next example.pdf --watermark-font-family "Times New Roman"`                                                   | `Arial`            |
| `--watermark-font-size`         | Taille de police du filigrane                                                           | `pdf2zh_next example.pdf --watermark-font-size 20`                                                                    | `20`               |
| `--watermark-color`             | Couleur du filigrane en code hexadécimal                                                | `pdf2zh_next example.pdf --watermark-color "#FF0000"`                                                                 | `#000000`          |
| `--watermark-rotation`          | Angle de rotation du filigrane en degrés                                                | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     | `45`               |
| `--watermark-opacity`           | Opacité du filigrane (0-1)                                                              | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     | `0.2`              |
| `--watermark-spacing`           | Espacement entre les textes du filigrane en points                                      | `pdf2zh_next example.pdf --watermark-spacing 100`                                                                     | `200`              |
| `--watermark-z-index`           | Position de la couche du filigrane (les valeurs plus élevées sont au-dessus)            | `pdf2zh_next example.pdf --watermark-z-index 10`                                                                      | `-1`               |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--min-pages-per-part`          | Minimum pages per part for split translation                                            | `pdf2zh_next example.pdf --min-pages-per-part 10`                                                                     |
| `--max-chars-per-part`          | Maximum characters per part for split translation                                       | `pdf2zh_next example.pdf --max-chars-per-part 100000`                                                                 |
| `--min-chars-per-part`          | Minimum characters per part for split translation                                       | `pdf2zh_next example.pdf --min-chars-per-part 10000`                                                                  |
| `--max-pages-per-doc`           | Maximum pages per doc for split translation                                             | `pdf2zh_next example.pdf --max-pages-per-doc 100`                                                                     |
| `--min-pages-per-doc`           | Minimum pages per doc for split translation                                             | `pdf2zh_next example.pdf --min-pages-per-doc 10`                                                                      |
| `--max-chars-per-doc`           | Maximum characters per doc for split translation                                        | `pdf2zh_next example.pdf --max-chars-per-doc 1000000`                                                                 |
| `--min-chars-per-doc`           | Minimum characters per doc for split translation                                        | `pdf2zh_next example.pdf --min-chars-per-doc 100000`                                                                  |
| `--max-pages-per-request`       | Maximum pages per request for split translation                                         | `pdf2zh_next example.pdf --max-pages-per-request 10`                                                                  |
| `--min-pages-per-request`       | Minimum pages per request for split translation                                         | `pdf2zh_next example.pdf --min-pages-per-request 1`                                                                   |
| `--max-chars-per-request`       | Maximum characters per request for split translation                                    | `pdf2zh_next example.pdf --max-chars-per-request 10000`                                                               |
| `--min-chars-per-request`       | Minimum characters per request for split translation                                    | `pdf2zh_next example.pdf --min-chars-per-request 1000`                                                                |

---

### OUTPUT

| `--max-pages-per-part`          | Nombre maximum de pages par partie pour la traduction divisée                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| :------------------------------ | :------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--min-pages-per-part`          | Nombre minimum de pages par partie pour la traduction divisée                                            | `pdf2zh_next example.pdf --min-pages-per-part 10`                                                                     |
| `--max-chars-per-part`          | Nombre maximum de caractères par partie pour la traduction divisée                                       | `pdf2zh_next example.pdf --max-chars-per-part 100000`                                                                 |
| `--min-chars-per-part`          | Nombre minimum de caractères par partie pour la traduction divisée                                       | `pdf2zh_next example.pdf --min-chars-per-part 10000`                                                                  |
| `--max-pages-per-doc`           | Nombre maximum de pages par document pour la traduction divisée                                          | `pdf2zh_next example.pdf --max-pages-per-doc 100`                                                                     |
| `--min-pages-per-doc`           | Nombre minimum de pages par document pour la traduction divisée                                          | `pdf2zh_next example.pdf --min-pages-per-doc 10`                                                                      |
| `--max-chars-per-doc`           | Nombre maximum de caractères par document pour la traduction divisée                                     | `pdf2zh_next example.pdf --max-chars-per-doc 1000000`                                                                 |
| `--min-chars-per-doc`           | Nombre minimum de caractères par document pour la traduction divisée                                     | `pdf2zh_next example.pdf --min-chars-per-doc 100000`                                                                  |
| `--max-pages-per-request`       | Nombre maximum de pages par requête pour la traduction divisée                                           | `pdf2zh_next example.pdf --max-pages-per-request 10`                                                                  |
| `--min-pages-per-request`       | Nombre minimum de pages par requête pour la traduction divisée                                           | `pdf2zh_next example.pdf --min-pages-per-request 1`                                                                   |
| `--max-chars-per-request`       | Nombre maximum de caractères par requête pour la traduction divisée                                      | `pdf2zh_next example.pdf --max-chars-per-request 10000`                                                               |
| `--min-chars-per-request`       | Nombre minimum de caractères par requête pour la traduction divisée                                      | `pdf2zh_next example.pdf --min-chars-per-request 1000`                                                                |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--translate-figure-text`       | Translate figure text (experimental)                                                    | `pdf2zh_next example.pdf --translate-figure-text`                                                                     |
| `--translate-algorithm-text`    | Translate algorithm text (experimental)                                                  | `pdf2zh_next example.pdf --translate-algorithm-text`                                                                  |
| `--translate-equation-text`     | Translate equation text (experimental)                                                   | `pdf2zh_next example.pdf --translate-equation-text`                                                                   |
| `--translate-reference-text`    | Translate reference text (experimental)                                                  | `pdf2zh_next example.pdf --translate-reference-text`                                                                  |
| `--translate-citation-text`     | Translate citation text (experimental)                                                   | `pdf2zh_next example.pdf --translate-citation-text`                                                                   |
| `--translate-footnote-text`     | Translate footnote text (experimental)                                                   | `pdf2zh_next example.pdf --translate-footnote-text`                                                                   |
| `--translate-header-text`       | Translate header text (experimental)                                                     | `pdf2zh_next example.pdf --translate-header-text`                                                                     |
| `--translate-footer-text`       | Translate footer text (experimental)                                                     | `pdf2zh_next example.pdf --translate-footer-text`                                                                     |

---

### TRANSLATION

| `--translate-table-text`        | Traduire le texte des tableaux (expérimental)                                           | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--translate-figure-text`       | Traduire le texte des figures (expérimental)                                            | `pdf2zh_next example.pdf --translate-figure-text`                                                                     |
| `--translate-algorithm-text`    | Traduire le texte des algorithmes (expérimental)                                        | `pdf2zh_next example.pdf --translate-algorithm-text`                                                                  |
| `--translate-equation-text`     | Traduire le texte des équations (expérimental)                                          | `pdf2zh_next example.pdf --translate-equation-text`                                                                   |
| `--translate-reference-text`    | Traduire le texte des références (expérimental)                                         | `pdf2zh_next example.pdf --translate-reference-text`                                                                  |
| `--translate-citation-text`     | Traduire le texte des citations (expérimental)                                          | `pdf2zh_next example.pdf --translate-citation-text`                                                                   |
| `--translate-footnote-text`     | Traduire le texte des notes de bas de page (expérimental)                               | `pdf2zh_next example.pdf --translate-footnote-text`                                                                   |
| `--translate-header-text`       | Traduire le texte de l'en-tête (expérimental)                                           | `pdf2zh_next example.pdf --translate-header-text`                                                                     |
| `--translate-footer-text`       | Traduire le texte du pied de page (expérimental)                                        | `pdf2zh_next example.pdf --translate-footer-text`                                                                     |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--skip-title-detection`        | Skip title detection                                                                    | `pdf2zh_next example.pdf --skip-title-detection`                                                                      |
| `--skip-table-detection`        | Skip table detection                                                                    | `pdf2zh_next example.pdf --skip-table-detection`                                                                      |
| `--skip-formula-detection`      | Skip formula detection                                                                  | `pdf2zh_next example.pdf --skip-formula-detection`                                                                    |
| `--skip-reference-detection`    | Skip reference detection                                                                | `pdf2zh_next example.pdf --skip-reference-detection`                                                                  |
| `--skip-figure-detection`       | Skip figure detection                                                                   | `pdf2zh_next example.pdf --skip-figure-detection`                                                                     |
| `--skip-header-footer-detection`| Skip header and footer detection                                                        | `pdf2zh_next example.pdf --skip-header-footer-detection`                                                              |
| `--skip-footnote-detection`     | Skip footnote detection                                                                 | `pdf2zh_next example.pdf --skip-footnote-detection`                                                                   |
| `--skip-page-number-detection`  | Skip page number detection                                                              | `pdf2zh_next example.pdf --skip-page-number-detection`                                                                |
| `--skip-margin-text-detection`  | Skip margin text detection                                                              | `pdf2zh_next example.pdf --skip-margin-text-detection`                                                                |
| `--skip-watermark-detection`    | Skip watermark detection                                                                | `pdf2zh_next example.pdf --skip-watermark-detection`                                                                  |

---

### OUTPUT

| `--skip-scanned-detection`      | Ignorer la détection de documents scannés                                               | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--skip-title-detection`        | Ignorer la détection de titres                                                          | `pdf2zh_next example.pdf --skip-title-detection`                                                                      |
| `--skip-table-detection`        | Ignorer la détection de tableaux                                                        | `pdf2zh_next example.pdf --skip-table-detection`                                                                      |
| `--skip-formula-detection`      | Ignorer la détection de formules                                                        | `pdf2zh_next example.pdf --skip-formula-detection`                                                                    |
| `--skip-reference-detection`    | Ignorer la détection de références                                                      | `pdf2zh_next example.pdf --skip-reference-detection`                                                                  |
| `--skip-figure-detection`       | Ignorer la détection de figures                                                         | `pdf2zh_next example.pdf --skip-figure-detection`                                                                     |
| `--skip-header-footer-detection`| Ignorer la détection des en-têtes et pieds de page                                      | `pdf2zh_next example.pdf --skip-header-footer-detection`                                                              |
| `--skip-footnote-detection`     | Ignorer la détection de notes de bas de page                                            | `pdf2zh_next example.pdf --skip-footnote-detection`                                                                   |
| `--skip-page-number-detection`  | Ignorer la détection des numéros de page                                                | `pdf2zh_next example.pdf --skip-page-number-detection`                                                                |
| `--skip-margin-text-detection`  | Ignorer la détection de texte en marge                                                  | `pdf2zh_next example.pdf --skip-margin-text-detection`                                                                |
| `--skip-watermark-detection`    | Ignorer la détection de filigranes                                                      | `pdf2zh_next example.pdf --skip-watermark-detection`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-text-color`   | Force translated text to be the specified color (e.g., `black`, `#000000`)             | `pdf2zh_next example.pdf --ocr-workaround-text-color black`                                                           |
| `--ocr-workaround-bg-color`     | Force translated background to be the specified color (e.g., `white`, `#ffffff`)         | `pdf2zh_next example.pdf --ocr-workaround-bg-color white`                                                             |
| `--ocr-workaround-border-color` | Force translated border to be the specified color (e.g., `black`, `#000000`)            | `pdf2zh_next example.pdf --ocr-workaround-border-color black`                                                         |
| `--ocr-workaround-border-width` | Force translated border to be the specified width (e.g., `0.5pt`)                      | `pdf2zh_next example.pdf --ocr-workaround-border-width 0.5pt`                                                        |
| `--ocr-workaround-border-radius`| Force translated border to be the specified radius (e.g., `0.5pt`)                      | `pdf2zh_next example.pdf --ocr-workaround-border-radius 0.5pt`                                                        |

---

### TRANSLATED TEXT

| `--ocr-workaround`              | Force le texte traduit à être noir et ajoute un arrière-plan blanc                      | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-text-color`   | Force le texte traduit à être de la couleur spécifiée (par ex., `black`, `#000000`)     | `pdf2zh_next example.pdf --ocr-workaround-text-color black`                                                           |
| `--ocr-workaround-bg-color`     | Force l'arrière-plan traduit à être de la couleur spécifiée (par ex., `white`, `#ffffff`) | `pdf2zh_next example.pdf --ocr-workaround-bg-color white`                                                             |
| `--ocr-workaround-border-color` | Force la bordure traduite à être de la couleur spécifiée (par ex., `black`, `#000000`)  | `pdf2zh_next example.pdf --ocr-workaround-border-color black`                                                         |
| `--ocr-workaround-border-width` | Force la bordure traduite à être de la largeur spécifiée (par ex., `0.5pt`)             | `pdf2zh_next example.pdf --ocr-workaround-border-width 0.5pt`                                                        |
| `--ocr-workaround-border-radius`| Force la bordure traduite à être du rayon spécifié (par ex., `0.5pt`)                   | `pdf2zh_next example.pdf --ocr-workaround-border-radius 0.5pt`                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--ocr-workaround-threshold`    | Threshold for OCR workaround. If the ratio of scanned pages exceeds this value, OCR workaround will be enabled. (default: 0.5)                                                                      | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.7`                   |
| `--ocr-workaround-skip-pages`   | Skip the first N pages during scan detection. Useful for documents with cover pages that might be detected as scanned. (default: 0)                                                                 | `pdf2zh_next example.pdf --ocr-workaround-skip-pages 2`                    |

---

### TRANSLATED TEXT

| `--auto-enable-ocr-workaround`  | Active le contournement automatique de l'OCR. Si un document est détecté comme étant fortement scanné, cela tentera d'activer le traitement OCR et sautera la détection de scan ultérieure. Voir la documentation pour plus de détails. (par défaut : False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--ocr-workaround-threshold`    | Seuil pour le contournement de l'OCR. Si le ratio de pages scannées dépasse cette valeur, le contournement OCR sera activé. (par défaut : 0.5)                                                                      | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.7`                   |
| `--ocr-workaround-skip-pages`   | Ignore les N premières pages pendant la détection de scan. Utile pour les documents avec des pages de couverture qui pourraient être détectées comme scannées. (par défaut : 0)                                                                 | `pdf2zh_next example.pdf --ocr-workaround-skip-pages 2`                    |
---

### OUTPUT

| `--only-include-translated-page`| Inclure uniquement les pages traduites dans le PDF de sortie. Efficace uniquement lorsque --pages est utilisé.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `--no-merge-same-font-size`           | Disable merging of text blocks with the same font size                                          | `pdf2zh_next example.pdf --no-merge-same-font-size`                                                          |
| `--no-merge-vertically-overlapped`    | Disable merging of vertically overlapping text blocks                                           | `pdf2zh_next example.pdf --no-merge-vertically-overlapped`                                                   |
| `--no-merge-horizontally-overlapped`  | Disable merging of horizontally overlapping text blocks                                         | `pdf2zh_next example.pdf --no-merge-horizontally-overlapped`                                                 |

---

### TRANSLATED TEXT

| `--no-merge-alternating-line-numbers` | Désactiver la fusion des numéros de ligne alternés et des paragraphes de texte dans les documents avec des numéros de ligne | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `--no-merge-same-font-size`           | Désactiver la fusion des blocs de texte avec la même taille de police                                                       | `pdf2zh_next example.pdf --no-merge-same-font-size`                                                          |
| `--no-merge-vertically-overlapped`    | Désactiver la fusion des blocs de texte qui se chevauchent verticalement                                                    | `pdf2zh_next example.pdf --no-merge-vertically-overlapped`                                                   |
| `--no-merge-horizontally-overlapped`  | Désactiver la fusion des blocs de texte qui se chevauchent horizontalement                                                  | `pdf2zh_next example.pdf --no-merge-horizontally-overlapped`                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--remove-formula-lines`        | Remove formula lines within paragraph areas                                             | `pdf2zh_next example.pdf --remove-formula-lines`                                                                       |
| `--no-remove-formula-lines`     | Disable removal of formula lines within paragraph areas                                 | `pdf2zh_next example.pdf --no-remove-formula-lines`                                                                    |
| `--formula-detection-mode`      | Formula detection mode: `ml` (machine learning) or `rule` (rule-based)                  | `pdf2zh_next example.pdf --formula-detection-mode rule`                                                                |
| `--formula-detection-size-threshold` | Minimum formula detection size (pixels)                                             | `pdf2zh_next example.pdf --formula-detection-size-threshold 50`                                                        |
| `--formula-detection-padding`   | Formula detection padding (pixels)                                                      | `pdf2zh_next example.pdf --formula-detection-padding 10`                                                               |
| `--formula-detection-margin`    | Formula detection margin (pixels)                                                       | `pdf2zh_next example.pdf --formula-detection-margin 5`                                                                 |

---

### TRANSLATION

| `--no-remove-non-formula-lines` | Désactiver la suppression des lignes non-formules dans les zones de paragraphe                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--remove-formula-lines`        | Supprimer les lignes de formules dans les zones de paragraphe                                             | `pdf2zh_next example.pdf --remove-formula-lines`                                                                       |
| `--no-remove-formula-lines`     | Désactiver la suppression des lignes de formules dans les zones de paragraphe                                 | `pdf2zh_next example.pdf --no-remove-formula-lines`                                                                    |
| `--formula-detection-mode`      | Mode de détection de formules : `ml` (apprentissage automatique) ou `rule` (basé sur des règles)                  | `pdf2zh_next example.pdf --formula-detection-mode rule`                                                                |
| `--formula-detection-size-threshold` | Taille minimale de détection de formules (pixels)                                             | `pdf2zh_next example.pdf --formula-detection-size-threshold 50`                                                        |
| `--formula-detection-padding`   | Remplissage de détection de formules (pixels)                                                      | `pdf2zh_next example.pdf --formula-detection-padding 10`                                                               |
| `--formula-detection-margin`    | Marge de détection de formules (pixels)                                                       | `pdf2zh_next example.pdf --formula-detection-margin 5`                                                                 |
`0.8`   |
| ---------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------- |
| `--formula-line-iou-threshold`      | Set IoU threshold for identifying formula lines (0.0-1.0)                           | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                            | `0.8`   |
| `--formula-merge-iou-threshold`     | Set IoU threshold for merging adjacent formula blocks (0.0-1.0)                      | `pdf2zh_next example.pdf --formula-merge-iou-threshold 0.85`                                                           | `0.8`   |
| `--formula-merge-max-gap`           | Set maximum vertical gap (in pixels) for merging adjacent formula blocks            | `pdf2zh_next example.pdf --formula-merge-max-gap 50`                                                                   | `50`    |
| `--formula-merge-max-horizontal-gap` | Set maximum horizontal gap (in pixels) for merging adjacent formula blocks          | `pdf2zh_next example.pdf --formula-merge-max-horizontal-gap 50`                                                        | `50`    |
| `--formula-merge-max-vertical-gap`   | Set maximum vertical gap (in pixels) for merging adjacent formula blocks            | `pdf2zh_next example.pdf --formula-merge-max-vertical-gap 50`                                                          | `50`    |

---

### TRANSLATED TEXT

| `--non-formula-line-iou-threshold` | Définir le seuil IoU pour l'identification des lignes non-formules (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.8`   |
| ---------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------- |
| `--formula-line-iou-threshold`      | Définir le seuil IoU pour l'identification des lignes de formules (0.0-1.0)                           | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                            | `0.8`   |
| `--formula-merge-iou-threshold`     | Définir le seuil IoU pour la fusion des blocs de formules adjacents (0.0-1.0)                      | `pdf2zh_next example.pdf --formula-merge-iou-threshold 0.85`                                                           | `0.8`   |
| `--formula-merge-max-gap`           | Définir l'écart vertical maximum (en pixels) pour la fusion des blocs de formules adjacents            | `pdf2zh_next example.pdf --formula-merge-max-gap 50`                                                                   | `50`    |
| `--formula-merge-max-horizontal-gap` | Définir l'écart horizontal maximum (en pixels) pour la fusion des blocs de formules adjacents          | `pdf2zh_next example.pdf --formula-merge-max-horizontal-gap 50`                                                        | `50`    |
| `--formula-merge-max-vertical-gap`   | Définir l'écart vertical maximum (en pixels) pour la fusion des blocs de formules adjacents            | `pdf2zh_next example.pdf --formula-merge-max-vertical-gap 50`                                                          | `50`    |
0.95                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `--figure-table-protection-margin`    | Set protection margin for figures and tables (0.0-1.0). Lines within figures/tables will not be processed   | `pdf2zh_next example.pdf --figure-table-protection-margin 0.05`                                           | 0.05                                                                     |
| `--figure-table-protection-min-width` | Set minimum width for figures and tables (0.0-1.0). Lines within figures/tables will not be processed       | `pdf2zh_next example.pdf --figure-table-protection-min-width 0.2`                                         | 0.2                                                                      |

---

### OUTPUT

| `--figure-table-protection-threshold` | Définir le seuil de protection pour les figures et les tableaux (0.0-1.0). Les lignes dans les figures/tableaux ne seront pas traitées | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        | 0.95                                                                     |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `--figure-table-protection-margin`    | Définir la marge de protection pour les figures et les tableaux (0.0-1.0). Les lignes dans les figures/tableaux ne seront pas traitées | `pdf2zh_next example.pdf --figure-table-protection-margin 0.05`                                           | 0.05                                                                     |
| `--figure-table-protection-min-width` | Définir la largeur minimale pour les figures et les tableaux (0.0-1.0). Les lignes dans les figures/tableaux ne seront pas traitées   | `pdf2zh_next example.pdf --figure-table-protection-min-width 0.2`                                         | 0.2                                                                      |
---

### OUTPUT

| `--skip-formula-offset-calculation` | Ignorer le calcul du décalage des formules pendant le traitement | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### Arguments de l'interface graphique

| `--server_name`                 | Set server name                        | `pdf2zh_next --gui --server_name 0.0.0.0`       |
| `--server_port`                 | Set server port                        | `pdf2zh_next --gui --server_port 7861`          |
| `--auth`                        | Set authentication                     | `pdf2zh_next --gui --auth username:password`    |
| `--ssl_keyfile`                 | Set SSL key file path                  | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile`                | Set SSL certificate file path          | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--concurrency_count`           | Set the number of concurrent threads   | `pdf2zh_next --gui --concurrency_count 10`      |
| `--max_file_size`               | Set the maximum file size (in MB)      | `pdf2zh_next --gui --max_file_size 1024`        |
| `--allowed_path`                | Set allowed paths                      | `pdf2zh_next --gui --allowed_path ./input`      |
| `--queue_concurrency_count`     | Set the number of concurrent queues    | `pdf2zh_next --gui --queue_concurrency_count 5` |

---

### TRANSLATION RESULT

| Option                          | Fonction                               | Exemple                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Activer le mode de partage             | `pdf2zh_next --gui --share`                     |
| `--server_name`                 | Définir le nom du serveur              | `pdf2zh_next --gui --server_name 0.0.0.0`       |
| `--server_port`                 | Définir le port du serveur             | `pdf2zh_next --gui --server_port 7861`          |
| `--auth`                        | Définir l'authentification             | `pdf2zh_next --gui --auth username:password`    |
| `--ssl_keyfile`                 | Définir le chemin du fichier clé SSL   | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile`                | Définir le chemin du fichier certificat SSL | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--concurrency_count`           | Définir le nombre de threads concurrents | `pdf2zh_next --gui --concurrency_count 10`      |
| `--max_file_size`               | Définir la taille maximale du fichier (en Mo) | `pdf2zh_next --gui --max_file_size 1024`        |
| `--allowed_path`                | Définir les chemins autorisés           | `pdf2zh_next --gui --allowed_path ./input`      |
| `--queue_concurrency_count`     | Définir le nombre de files d'attente concurrentes | `pdf2zh_next --gui --queue_concurrency_count 5` |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--auth-username`               | Username for authentication            | `pdf2zh_next --gui --auth-username user`        |
| `--auth-password`               | Password for authentication            | `pdf2zh_next --gui --auth-password pwd`         |

---

### OUTPUT

| `--auth-file`                   | Chemin vers le fichier d'authentification        | `pdf2zh_next --gui --auth-file /path`           |
| ------------------------------- | ------------------------------------------------ | ----------------------------------------------- |
| `--auth-username`               | Nom d'utilisateur pour l'authentification        | `pdf2zh_next --gui --auth-username user`        |
| `--auth-password`               | Mot de passe pour l'authentification             | `pdf2zh_next --gui --auth-password pwd`         |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--help`                        | Show help message                      | `pdf2zh_next --help`                            |
| `--version`                     | Show version info                      | `pdf2zh_next --version`                         |

---

### TRANSLATED TEXT

| `--welcome-page`                | Chemin vers le fichier html d'accueil  | `pdf2zh_next --gui --welcome-page /path`        |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--help`                        | Afficher le message d'aide             | `pdf2zh_next --help`                            |
| `--version`                     | Afficher les informations de version   | `pdf2zh_next --version`                         |
Enable Bing and OpenAI translation services, and open the WebUI. |
| ------------------------------- | ------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------- |

---

### OUTPUT

| `--enabled-services`            | Services de traduction activés         | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | Activez les services de traduction Bing et OpenAI, et ouvrez le WebUI. |
| ------------------------------- | ------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------- |
This is a workaround when there is a conflict with the input method. |

---

### OUTPUT

| `--disable-gui-sensitive-input` | Désactiver l'entrée sensible de l'interface graphique | `pdf2zh_next --gui --disable-gui-sensitive-input` | Ceci est une solution de contournement en cas de conflit avec la méthode de saisie. |
---

### OUTPUT

| `--disable-config-auto-save`    | Désactiver la sauvegarde automatique de la configuration | `pdf2zh_next --gui --disable-config-auto-save`  |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | WebUI Host                             | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--no-gradio-queue`             | Disable Gradio Queue                   | `pdf2zh_next --gui --no-gradio-queue`           |
| `--share`                       | Share the WebUI                        | `pdf2zh_next --gui --share`                     |
| `--auth`                        | Set Gradio Authentication              | `pdf2zh_next --gui --auth username:password`    |
| `--ssl-keyfile`                 | SSL Key File Path                      | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | SSL Certificate File Path              | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
| `--concurrency-count`           | Gradio Concurrency Count               | `pdf2zh_next --gui --concurrency-count 10`      |
| `--max-file-size`               | Gradio Max File Size (MB)              | `pdf2zh_next --gui --max-file-size 100`         |
| `--max-files`                   | Gradio Max File Count                  | `pdf2zh_next --gui --max-files 20`              |
| `--allowed-path`                | Gradio Allowed Upload Paths            | `pdf2zh_next --gui --allowed-path /tmp`         |
| `--blocking-path`               | Gradio Blocked Upload Paths            | `pdf2zh_next --gui --blocking-path /root`       |
| `--show-error`                  | Show Error Details in WebUI            | `pdf2zh_next --gui --show-error`                |
| `--theme`                       | Gradio Theme                           | `pdf2zh_next --gui --theme soft`                |
| `--dark-theme`                  | Use Dark Theme                         | `pdf2zh_next --gui --dark-theme`                |
| `--language`                    | WebUI Language                         | `pdf2zh_next --gui --language en`               |
| `--favicon-path`                | WebUI Favicon Path                     | `pdf2zh_next --gui --favicon-path favicon.ico`  |
| `--title`                       | WebUI Title                            | `pdf2zh_next --gui --title "PDF Translate App"` |
| `--width`                       | WebUI Width                            | `pdf2zh_next --gui --width 100%`                |
| `--height`                      | WebUI Height                           | `pdf2zh_next --gui --height 700px`              |

---

### OUTPUT

| `--server-port`                 | Port WebUI                             | `pdf2zh_next --gui --server-port 7860`          |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | Hôte WebUI                             | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--no-gradio-queue`             | Désactiver la file d'attente Gradio    | `pdf2zh_next --gui --no-gradio-queue`           |
| `--share`                       | Partager l'interface WebUI             | `pdf2zh_next --gui --share`                     |
| `--auth`                        | Définir l'authentification Gradio      | `pdf2zh_next --gui --auth username:password`    |
| `--ssl-keyfile`                 | Chemin du fichier clé SSL              | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | Chemin du certificat SSL               | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
| `--concurrency-count`           | Nombre de concurrences Gradio          | `pdf2zh_next --gui --concurrency-count 10`      |
| `--max-file-size`               | Taille maximale de fichier Gradio (MB) | `pdf2zh_next --gui --max-file-size 100`         |
| `--max-files`                   | Nombre maximal de fichiers Gradio      | `pdf2zh_next --gui --max-files 20`              |
| `--allowed-path`                | Chemins de téléchargement autorisés Gradio | `pdf2zh_next --gui --allowed-path /tmp`         |
| `--blocking-path`               | Chemins de téléchargement bloqués Gradio | `pdf2zh_next --gui --blocking-path /root`       |
| `--show-error`                  | Afficher les détails d'erreur dans WebUI | `pdf2zh_next --gui --show-error`                |
| `--theme`                       | Thème Gradio                           | `pdf2zh_next --gui --theme soft`                |
| `--dark-theme`                  | Utiliser le thème sombre               | `pdf2zh_next --gui --dark-theme`                |
| `--language`                    | Langue de l'interface WebUI            | `pdf2zh_next --gui --language en`               |
| `--favicon-path`                | Chemin du favicon WebUI                | `pdf2zh_next --gui --favicon-path favicon.ico`  |
| `--title`                       | Titre de l'interface WebUI             | `pdf2zh_next --gui --title "PDF Translate App"` |
| `--width`                       | Largeur de l'interface WebUI           | `pdf2zh_next --gui --width 100%`                |
| `--height`                      | Hauteur de l'interface WebUI           | `pdf2zh_next --gui --height 700px`              |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--target-lang`                 | Target language of the output document | `pdf2zh_next --gui --target-lang fr`            |
| `--model`                       | Model name                             | `pdf2zh_next --gui --model gpt-4o-mini`         |
| `--proxy`                       | Proxy URL                              | `pdf2zh_next --gui --proxy http://127.0.0.1:7890` |
| `--no-proxy`                    | Disable proxy                          | `pdf2zh_next --gui --no-proxy`                  |
| `--api-key`                     | API key                                | `pdf2zh_next --gui --api-key sk-xxxxx`          |
| `--api-base`                    | API base URL                           | `pdf2zh_next --gui --api-base https://api.example.com` |

---

### OUTPUT

| `--ui-lang`                     | Langue de l'interface utilisateur      | `pdf2zh_next --gui --ui-lang zh`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--target-lang`                 | Langue cible du document de sortie     | `pdf2zh_next --gui --target-lang fr`            |
| `--model`                       | Nom du modèle                         | `pdf2zh_next --gui --model gpt-4o-mini`         |
| `--proxy`                       | URL du proxy                          | `pdf2zh_next --gui --proxy http://127.0.0.1:7890` |
| `--no-proxy`                    | Désactiver le proxy                   | `pdf2zh_next --gui --no-proxy`                  |
| `--api-key`                     | Clé API                               | `pdf2zh_next --gui --api-key sk-xxxxx`          |
| `--api-base`                    | URL de base de l'API                  | `pdf2zh_next --gui --api-base https://api.example.com` |

[⬆️ Retour en haut](#toc)

---

#### Guide de configuration des limites de débit

Lors de l'utilisation des services de traduction, une configuration appropriée des limites de débit est cruciale pour éviter les erreurs d'API et optimiser les performances. Ce guide explique comment configurer les paramètres `--qps` et `--pool-max-worker` en fonction des différentes limitations des services en amont.

> [!TIP]
>
> Il est recommandé que le pool_size ne dépasse pas 1000. Si le pool_size calculé par la méthode suivante dépasse 1000, veuillez utiliser 1000.

##### Limitation du taux RPM (Requêtes Par Minute)

Lorsque le service en amont a des limitations RPM, utilisez le calcul suivant :

**Formule de calcul :**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Le facteur de 10 est un coefficient empirique qui fonctionne généralement bien pour la plupart des scénarios.

### TEXTE ORIGINAL

**Exemple :**
Si votre service de traduction a une limite de 600 RPM :
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitation des connexions simultanées

Lorsque le service en amont a des limitations de connexions simultanées (comme le service officiel GLM), utilisez cette approche :

**Formule de calcul :**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Exemple :**
Si votre service de traduction autorise 50 connexions simultanées :
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Meilleures pratiques

> [!TIP]
> - Commencez toujours avec des valeurs conservatrices et augmentez-les progressivement si nécessaire
> - Surveillez les temps de réponse et les taux d'erreur de votre service
> - Différents services peuvent nécessiter différentes stratégies d'optimisation
> - Prenez en compte votre cas d'utilisation spécifique et la taille des documents lors de la configuration de ces paramètres


[⬆️ Retour en haut](#toc)

---

#### Traduction partielle

Utilisez le paramètre `--pages` pour traduire une partie d'un document.

- Si les numéros de page sont consécutifs, vous pouvez l'écrire comme ceci :

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` inclut toutes les pages après la page 25. Si votre document comporte 100 pages, cela équivaut à `25-100`.
> 
> De même, `-25` inclut toutes les pages avant la page 25, ce qui équivaut à `1-25`.

- Si les pages ne sont pas consécutives, vous pouvez utiliser une virgule `,` pour les séparer.

Par exemple, si vous souhaitez traduire la première et la troisième page, vous pouvez utiliser la commande suivante :

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Si les pages incluent à la fois des plages consécutives et non consécutives, vous pouvez également les connecter avec une virgule, comme ceci :

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Cette commande traduira la première page, la troisième page, les pages 10 à 20, et toutes les pages de 25 jusqu'à la fin.


[⬆️ Retour en haut](#toc)

---

#### Spécifier les langues source et cible

Voir [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Retour en haut](#toc)

---

#### Traduire avec exceptions

Utiliser des expressions régulières pour spécifier les polices de formule et les caractères à préserver :

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Conserve par défaut les polices `Latex`, `Mono`, `Code`, `Italic`, `Symbol` et `Math` :

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Retour en haut](#toc)

---

#### Invite personnalisée

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Invite système personnalisée pour la traduction. Elle est principalement utilisée pour ajouter l'instruction '/no_think' de Qwen 3 dans l'invite.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Retour en haut](#toc)

---

#### Configuration personnalisée

Il existe plusieurs façons de modifier et d'importer le fichier de configuration.

> [!NOTE]
> **Hiérarchie des fichiers de configuration**
>
> Lors de la modification d'un même paramètre à l'aide de différentes méthodes, le logiciel appliquera les modifications selon l'ordre de priorité ci-dessous.
>
> Les modifications de rang supérieur remplaceront celles de rang inférieur.
>
> **cli/gui > env > fichier de configuration utilisateur > fichier de configuration par défaut**

- Modification de la configuration via **Arguments de ligne de commande**

Pour la plupart des cas, vous pouvez directement passer vos paramètres souhaités via les arguments de ligne de commande. Veuillez vous référer à [Arguments de ligne de commande](#cmd) pour plus d'informations.

Par exemple, si vous souhaitez activer une fenêtre d'interface graphique, vous pouvez utiliser la commande suivante :

```bash
pdf2zh_next --gui
```

- Modification de la configuration via **Variables d'environnement**

Vous pouvez remplacer le `--` dans les arguments de ligne de commande par `PDF2ZH_`, connecter les paramètres en utilisant `=`, et remplacer `-` par `_` comme variables d'environnement.

Par exemple, si vous souhaitez activer une fenêtre d'interface graphique, vous pouvez utiliser la commande suivante :

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Fichier de **configuration** spécifié par l'utilisateur

Vous pouvez spécifier un fichier de configuration en utilisant l'argument de ligne de commande ci-dessous :

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Si vous n'êtes pas sûr du format du fichier de configuration, veuillez vous référer au fichier de configuration par défaut décrit ci-dessous.

- **Fichier de configuration par défaut**

Le fichier de configuration par défaut se trouve dans `~/.config/pdf2zh`.  
Veuillez ne pas modifier les fichiers de configuration dans le répertoire `default`.  
Il est fortement recommandé de se référer au contenu de ce fichier de configuration et d'utiliser **Configuration personnalisée** pour implémenter votre propre fichier de configuration.

> [!TIP]
> - Par défaut, pdf2zh 2.0 enregistre automatiquement la configuration actuelle dans `~/.config/pdf2zh/config.v3.toml` chaque fois que vous cliquez sur le bouton de traduction dans l'interface graphique. Ce fichier de configuration sera chargé par défaut au prochain démarrage.
> - Les fichiers de configuration dans le répertoire `default` sont générés automatiquement par le programme. Vous pouvez les copier pour les modifier, mais veuillez ne pas les modifier directement.
> - Les fichiers de configuration peuvent inclure des numéros de version tels que "v2", "v3", etc. Ce sont **des numéros de version des fichiers de configuration**, **et non** le numéro de version de pdf2zh lui-même.


[⬆️ Retour en haut](#toc)

---

#### Ignorer le nettoyage

Lorsque ce paramètre est défini sur True, l'étape de nettoyage du PDF sera ignorée, ce qui peut améliorer la compatibilité et éviter certains problèmes de traitement des polices.

Utilisation :

```bash
pdf2zh_next example.pdf --skip-clean
```

Ou en utilisant des variables d'environnement :

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Lorsque `--enhance-compatibility` est activé, Ignorer le nettoyage est automatiquement activé.

---

#### Cache de traduction

PDFMathTranslate met en cache les textes traduits pour augmenter la vitesse et éviter les appels API inutiles pour les mêmes contenus. Vous pouvez utiliser l'option `--ignore-cache` pour ignorer le cache de traduction et forcer une nouvelle traduction.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Retour en haut](#toc)

---

#### Déploiement en tant que services publics

Lors du déploiement d'une interface graphique pdf2zh sur des services publics, vous devez modifier le fichier de configuration comme décrit ci-dessous.

> [!WARNING]
>
> Ce projet n'a pas été audité professionnellement pour la sécurité et peut contenir des vulnérabilités de sécurité. Veuillez évaluer les risques et prendre les mesures de sécurité nécessaires avant de déployer sur des réseaux publics.


> [!TIP]
> - Lors d'un déploiement public, disable_gui_sensitive_input et disable_config_auto_save doivent tous deux être activés.
> - Séparez les différents services disponibles avec des *virgules anglaises* <kbd>,</kbd> .

Une configuration utilisable est la suivante :

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Retour en haut](#toc)

---

#### Authentification et page d'accueil

Lors de l'utilisation de l'Authentification et de la page d'accueil pour spécifier quel utilisateur doit utiliser l'interface Web et personnaliser la page de connexion :

exemple auth.txt
Chaque ligne contient deux éléments, le nom d'utilisateur et le mot de passe, séparés par une virgule.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

exemple welcome.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>Simple HTML</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my simple HTML page.</p>
</body>
</html>
```

> [!NOTE]
> La page d'accueil fonctionnera uniquement si le fichier d'authentification n'est pas vide.
> Si le fichier d'authentification est vide, il n'y aura pas d'authentification. :)

Une configuration utilisable est la suivante :

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Retour en haut](#toc)

---

#### Prise en charge du glossaire

PDFMathTranslate prend en charge la table de glossaire. Le fichier de tables de glossaire doit être un fichier `csv`.
Il y a trois colonnes dans le fichier. Voici un exemple de fichier de glossaire :

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | ML automatique  | fr   |
| a,a    | a       | fr   |
| "      | "       | fr   |


Pour les utilisateurs de la ligne de commande :
Vous pouvez utiliser plusieurs fichiers pour le glossaire. Et les différents fichiers doivent être séparés par `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Pour les utilisateurs de WebUI :

Vous pouvez maintenant télécharger votre propre fichier de glossaire. Après avoir téléchargé le fichier, vous pouvez le consulter en cliquant sur son nom et le contenu s'affichera ci-dessous.

[⬆️ Retour en haut](#toc)

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>