[**Erweiterte Optionen**](./introduction.md) > **Erweiterte Optionen** _(aktuell)_

---

<h3 id="toc">Inhaltsverzeichnis</h3>

- [Kommandozeilenargumente](#kommandozeilenargumente)
- [Rate-Limiting-Konfigurationsleitfaden](#rate-limiting-konfigurationsleitfaden)
- [Partielle Übersetzung](#partielle-übersetzung)
- [Quell- und Zielsprachen angeben](#quell--und-zielsprachen-angeben)
- [Übersetzung mit Ausnahmen](#übersetzung-mit-ausnahmen)
- [Benutzerdefinierte Eingabeaufforderung](#benutzerdefinierte-eingabeaufforderung)
- [Benutzerdefinierte Konfiguration](#benutzerdefinierte-konfiguration)
- [Bereinigung überspringen](#bereinigung-überspringen)
- [Übersetzungscache](#übersetzungscache)
- [Bereitstellung als öffentlicher Dienst](#bereitstellung-als-öffentlicher-dienst)
- [Authentifizierung und Willkommensseite](#authentifizierung-und-willkommensseite)
- [Glossarunterstützung](#glossarunterstützung)

---

#### Kommandozeilen-Argumente

Führen Sie den Übersetzungsbefehl in der Kommandozeile aus, um das übersetzte Dokument `example-mono.pdf` und das zweisprachige Dokument `example-dual.pdf` im aktuellen Arbeitsverzeichnis zu generieren. Verwenden Sie Google als Standard-Übersetzungsdienst. Weitere unterstützte Übersetzungsdienste finden Sie [HIER](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

In der folgenden Tabelle listen wir alle erweiterten Optionen zur Referenz auf:

##### Argumente

| `input-dir`                     | Input directory containing PDF files to process                                         | `pdf2zh_next -d ./pdfs`                                                                                               |
| `output-dir`                    | Output directory for translated files                                                   | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `output-filename`               | Output filename (without extension)                                                     | `pdf2zh_next example.pdf --output-filename translated`                                                                |
| `language`                      | Target language (default: zh)                                                           | `pdf2zh_next example.pdf -l en`                                                                                       |
| `translator`                    | Translation service (default: google)                                                   | `pdf2zh_next example.pdf -t deepl`                                                                                    |
| `api-key`                       | API key for translation service                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      |
| `translator-url`                | Custom endpoint for translation service                                                 | `pdf2zh_next example.pdf --translator-url https://your-custom-endpoint.com`                                           |
| `proxy`                         | Proxy server for translation requests                                                   | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `ocr`                           | Use OCR for text extraction (default: false)                                            | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `no-crop`                       | Disable margin cropping (default: false)                                                | `pdf2zh_next example.pdf --no-crop`                                                                                   |
| `formula-detection`             | Enable formula detection (default: true)                                                | `pdf2zh_next example.pdf --no-formula-detection`                                                                      |
| `formula-scaling`               | Scaling factor for formulas (default: 1.0)                                              | `pdf2zh_next example.pdf --formula-scaling 1.2`                                                                       |
| `formula-render-mode`           | Formula rendering mode (default: vector)                                                | `pdf2zh_next example.pdf --formula-render-mode raster`                                                                |
| `formula-render-dpi`            | DPI for raster formula rendering (default: 300)                                         | `pdf2zh_next example.pdf --formula-render-dpi 600`                                                                    |
| `formula-font`                  | Font for formula rendering (default: stix)                                              | `pdf2zh_next example.pdf --formula-font xits`                                                                         |
| `font-family`                   | Font family for text (default: Noto Serif SC)                                           | `pdf2zh_next example.pdf --font-family "Times New Roman"`                                                             |
| `font-size`                     | Font size adjustment (default: 0)                                                       | `pdf2zh_next example.pdf --font-size 1`                                                                               |
| `line-spacing`                  | Line spacing adjustment (default: 0)                                                    | `pdf2zh_next example.pdf --line-spacing 1.2`                                                                          |
| `letter-spacing`                | Letter spacing adjustment (default: 0)                                                  | `pdf2zh_next example.pdf --letter-spacing 0.5`                                                                        |
| `margin`                        | Page margin adjustment (default: 0)                                                     | `pdf2zh_next example.pdf --margin 10`                                                                                 |
| `no-translate`                  | Disable translation (extract text only)                                                 | `pdf2zh_next example.pdf --no-translate`                                                                              |
| `only-translate`                | Extract and translate text without PDF reconstruction                                   | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `concurrency`                   | Number of concurrent translation tasks (default: 5)                                     | `pdf2zh_next example.pdf --concurrency 10`                                                                            |
| `retry-attempts`                | Number of retry attempts for failed translations (default: 3)                           | `pdf2zh_next example.pdf --retry-attempts 5`                                                                          |
| `retry-delay`                   | Delay between retry attempts in seconds (default: 1)                                    | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |
| `timeout`                       | Timeout for translation requests in seconds (default: 30)                               | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `config`                        | Path to config file                                                                     | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `cache-dir`                     | Directory for caching translation results                                               | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `no-cache`                      | Disable caching of translation results                                                  | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `force`                         | Force reprocessing even if cached                                                       | `pdf2zh_next example.pdf --force`                                                                                     |
| `verbose`                       | Enable verbose logging                                                                  | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `quiet`                         | Disable all logging output                                                              | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `version`                       | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `help`                          | Show help information                                                                   | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| Option                          | Funktion                                                                               | Beispiel                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Eingabe-PDF-Dateien zur Verarbeitung                                                     | `pdf2zh_next example.pdf`                                                                                             |
| `input-dir`                     | Eingabeverzeichnis mit PDF-Dateien zur Verarbeitung                                      | `pdf2zh_next -d ./pdfs`                                                                                               |
| `output-dir`                    | Ausgabeverzeichnis für übersetzte Dateien                                                | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `output-filename`               | Ausgabedateiname (ohne Erweiterung)                                                      | `pdf2zh_next example.pdf --output-filename translated`                                                                |
| `language`                      | Zielsprache (Standard: zh)                                                              | `pdf2zh_next example.pdf -l en`                                                                                       |
| `translator`                    | Übersetzungsdienst (Standard: google)                                                   | `pdf2zh_next example.pdf -t deepl`                                                                                    |
| `api-key`                       | API-Schlüssel für den Übersetzungsdienst                                                 | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      |
| `translator-url`                | Benutzerdefinierter Endpunkt für den Übersetzungsdienst                                  | `pdf2zh_next example.pdf --translator-url https://your-custom-endpoint.com`                                           |
| `proxy`                         | Proxy-Server für Übersetzungsanfragen                                                   | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `ocr`                           | OCR für Textextraktion verwenden (Standard: false)                                       | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `no-crop`                       | Randbeschnitt deaktivieren (Standard: false)                                             | `pdf2zh_next example.pdf --no-crop`                                                                                   |
| `formula-detection`             | Formelerkennung aktivieren (Standard: true)                                              | `pdf2zh_next example.pdf --no-formula-detection`                                                                      |
| `formula-scaling`               | Skalierungsfaktor für Formeln (Standard: 1.0)                                            | `pdf2zh_next example.pdf --formula-scaling 1.2`                                                                       |
| `formula-render-mode`           | Formelrendering-Modus (Standard: vector)                                                 | `pdf2zh_next example.pdf --formula-render-mode raster`                                                                |
| `formula-render-dpi`            | DPI für Raster-Formelrendering (Standard: 300)                                           | `pdf2zh_next example.pdf --formula-render-dpi 600`                                                                    |
| `formula-font`                  | Schriftart für Formelrendering (Standard: stix)                                          | `pdf2zh_next example.pdf --formula-font xits`                                                                         |
| `font-family`                   | Schriftfamilie für Text (Standard: Noto Serif SC)                                        | `pdf2zh_next example.pdf --font-family "Times New Roman"`                                                             |
| `font-size`                     | Schriftgrößenanpassung (Standard: 0)                                                     | `pdf2zh_next example.pdf --font-size 1`                                                                               |
| `line-spacing`                  | Zeilenabstandsanpassung (Standard: 0)                                                    | `pdf2zh_next example.pdf --line-spacing 1.2`                                                                          |
| `letter-spacing`                | Zeichenabstandsanpassung (Standard: 0)                                                   | `pdf2zh_next example.pdf --letter-spacing 0.5`                                                                        |
| `margin`                        | Seitenrandanpassung (Standard: 0)                                                        | `pdf2zh_next example.pdf --margin 10`                                                                                 |
| `no-translate`                  | Übersetzung deaktivieren (nur Textextraktion)                                            | `pdf2zh_next example.pdf --no-translate`                                                                              |
| `only-translate`                | Text extrahieren und übersetzen ohne PDF-Rekonstruktion                                  | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `concurrency`                   | Anzahl gleichzeitiger Übersetzungsaufgaben (Standard: 5)                                 | `pdf2zh_next example.pdf --concurrency 10`                                                                            |
| `retry-attempts`                | Anzahl der Wiederholungsversuche für fehlgeschlagene Übersetzungen (Standard: 3)        | `pdf2zh_next example.pdf --retry-attempts 5`                                                                          |
| `retry-delay`                   | Verzögerung zwischen Wiederholungsversuchen in Sekunden (Standard: 1)                   | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |
| `timeout`                       | Timeout für Übersetzungsanfragen in Sekunden (Standard: 30)                              | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `config`                        | Pfad zur Konfigurationsdatei                                                             | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `cache-dir`                     | Verzeichnis zum Zwischenspeichern von Übersetzungsergebnissen                            | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `no-cache`                      | Zwischenspeicherung von Übersetzungsergebnissen deaktivieren                             | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `force`                         | Erneute Verarbeitung erzwingen, auch wenn zwischengespeichert                            | `pdf2zh_next example.pdf --force`                                                                                     |
| `verbose`                       | Detaillierte Protokollierung aktivieren                                                  | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `quiet`                         | Alle Protokollausgaben deaktivieren                                                      | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `version`                       | Versionsinformationen anzeigen                                                           | `pdf2zh_next --version`                                                                                               |
| `help`                          | Hilfeinformationen anzeigen                                                              | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-filename`             | Output filename                                                                         | `pdf2zh_next example.pdf --output-filename example_zh.pdf`                                                            |
| `--output-type`                 | Output file type, `pdf` or `docx`                                                       | `pdf2zh_next example.pdf --output-type docx`                                                                          |
| `--output-language`             | Output language, see [Supported Languages](#supported-languages)                        | `pdf2zh_next example.pdf --output-language ja`                                                                        |
| `--output-translation-provider` | Output translation provider, see [Translation Services](#translation-services)          | `pdf2zh_next example.pdf --output-translation-provider google`                                                        |
| `--output-translation-key`      | Output translation provider key, see [Translation Services](#translation-services)      | `pdf2zh_next example.pdf --output-translation-provider azure --output-translation-key <your-azure-translator-key>`    |
| `--output-translation-region`   | Output translation provider region, see [Translation Services](#translation-services)   | `pdf2zh_next example.pdf --output-translation-provider azure --output-translation-region <your-azure-translator-region>` |
| `--output-translation-url`      | Output translation provider url, see [Translation Services](#translation-services)      | `pdf2zh_next example.pdf --output-translation-provider azure --output-translation-url <your-azure-translator-url>`     |

---

### TRANSLATED TEXT

| `--output`                      | Ausgabeverzeichnis für Dateien                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-filename`             | Ausgabedateiname                                                                           | `pdf2zh_next example.pdf --output-filename example_zh.pdf`                                                            |
| `--output-type`                 | Ausgabedateityp, `pdf` oder `docx`                                                         | `pdf2zh_next example.pdf --output-type docx`                                                                          |
| `--output-language`             | Ausgabesprache, siehe [Unterstützte Sprachen](#unterstützte-sprachen)                      | `pdf2zh_next example.pdf --output-language ja`                                                                        |
| `--output-translation-provider` | Ausgabe-Übersetzungsanbieter, siehe [Übersetzungsdienste](#übersetzungsdienste)            | `pdf2zh_next example.pdf --output-translation-provider google`                                                        |
| `--output-translation-key`      | Schlüssel des Ausgabe-Übersetzungsanbieters, siehe [Übersetzungsdienste](#übersetzungsdienste) | `pdf2zh_next example.pdf --output-translation-provider azure --output-translation-key <your-azure-translator-key>`    |
| `--output-translation-region`   | Region des Ausgabe-Übersetzungsanbieters, siehe [Übersetzungsdienste](#übersetzungsdienste) | `pdf2zh_next example.pdf --output-translation-provider azure --output-translation-region <your-azure-translator-region>` |
| `--output-translation-url`      | URL des Ausgabe-Übersetzungsanbieters, siehe [Übersetzungsdienste](#übersetzungsdienste)   | `pdf2zh_next example.pdf --output-translation-provider azure --output-translation-url <your-azure-translator-url>`     |
| ------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-<Config>`         | Use [**specific service**](./Documentation-of-Translation-Services.md) with config     | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o`                                         |
| `--<Services>-<Config>-<Proxy>` | Use [**specific service**](./Documentation-of-Translation-Services.md) with proxy      | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o --openai-proxy=http://127.0.0.1:7890`    |
| `--<Services>-<Config>-<Proxy>` | Use [**specific service**](./Documentation-of-Translation-Services.md) with proxy      | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o --openai-proxy=http://127.0.0.1:7890`    |
| `--<Services>-<Config>-<Proxy>` | Use [**specific service**](./Documentation-of-Translation-Services.md) with proxy      | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o --openai-proxy=http://127.0.0.1:7890`    |

---

### TRANSLATION RESULT

| `--<Services>`                  | Verwenden Sie einen [**bestimmten Service**](./Documentation-of-Translation-Services.md) für die Übersetzung | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-<Config>`         | Verwenden Sie einen [**bestimmten Service**](./Documentation-of-Translation-Services.md) mit Konfiguration   | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o`                                         |
| `--<Services>-<Config>-<Proxy>` | Verwenden Sie einen [**bestimmten Service**](./Documentation-of-Translation-Services.md) mit Proxy            | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o --openai-proxy=http://127.0.0.1:7890`    |
| `--<Services>-<Config>-<Proxy>` | Verwenden Sie einen [**bestimmten Service**](./Documentation-of-Translation-Services.md) mit Proxy            | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o --openai-proxy=http://127.0.0.1:7890`    |
| `--<Services>-<Config>-<Proxy>` | Verwenden Sie einen [**bestimmten Service**](./Documentation-of-Translation-Services.md) mit Proxy            | `pdf2zh_next example.pdf --openai --openai-api-key=xxx --openai-model=gpt-4o --openai-proxy=http://127.0.0.1:7890`    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | Input PDF file path                                                                     | `pdf2zh_next -i ./example.pdf`                                                                                        |
| `--output`, `-o`                | Output PDF file path                                                                    | `pdf2zh_next -i ./example.pdf -o ./example_zh.pdf`                                                                    |
| `--lang`, `-l`                  | Target language code, default is `zh`, see [Supported Languages](./SUPPORTED_LANG.md)   | `pdf2zh_next -i ./example.pdf -l ja`                                                                                  |
| `--service`, `-s`               | Translation service, default is `google`, see [Translation Services](./TRANSLATION.md)  | `pdf2zh_next -i ./example.pdf -s deepl`                                                                               |
| `--service-url`, `-su`          | Custom translation service URL                                                          | `pdf2zh_next -i ./example.pdf --service-url http://localhost:8080/translate`                                          |
| `--service-key`, `-sk`         | Translation service API key (if required)                                               | `pdf2zh_next -i ./example.pdf -s deepl -sk YOUR_DEEPL_API_KEY`                                                        |
| `--service-region`, `-sr`       | Translation service region (if required)                                                | `pdf2zh_next -i ./example.pdf -s azure -sr eastus`                                                                    |
| `--model`, `-m`                 | Translation model (if required)                                                         | `pdf2zh_next -i ./example.pdf -s openai -m gpt-4`                                                                     |
| `--math-mode`, `-mm`            | Math translation mode, default is `normal`, see [Math Translation](./MATH_TRANSLATE.md) | `pdf2zh_next -i ./example.pdf -mm hybrid`                                                                             |
| `--math-translator`, `-mt`      | Math translator, default is `latex`, see [Math Translation](./MATH_TRANSLATE.md)        | `pdf2zh_next -i ./example.pdf -mt google`                                                                             |
| `--font-size`, `-fs`            | Font size adjustment, default is `0`                                                    | `pdf2zh_next -i ./example.pdf -fs 2`                                                                                  |
| `--font-family`, `-ff`          | Font family, default is `SimSun, NSimSun, serif`                                        | `pdf2zh_next -i ./example.pdf -ff "Times New Roman, serif"`                                                           |
| `--font-family-cjk`, `-ffc`     | CJK font family, default is `SimSun, NSimSun, serif`                                    | `pdf2zh_next -i ./example.pdf -ffc "SimHei, sans-serif"`                                                              |
| `--line-spacing`, `-ls`         | Line spacing, default is `1.2`                                                          | `pdf2zh_next -i ./example.pdf -ls 1.5`                                                                                |
| `--paragraph-spacing`, `-ps`    | Paragraph spacing, default is `0.3`                                                     | `pdf2zh_next -i ./example.pdf -ps 0.5`                                                                                |
| `--char-spacing`, `-cs`         | Character spacing, default is `0`                                                       | `pdf2zh_next -i ./example.pdf -cs 0.5`                                                                                |
| `--page-margin`, `-pm`          | Page margin, default is `0`                                                             | `pdf2zh_next -i ./example.pdf -pm 10`                                                                                 |
| `--workers`, `-w`               | Number of workers, default is `4`                                                       | `pdf2zh_next -i ./example.pdf -w 8`                                                                                   |
| `--timeout`, `-t`               | Translation timeout in seconds, default is `30`                                          | `pdf2zh_next -i ./example.pdf -t 60`                                                                                  |
| `--retry`, `-r`                 | Number of retries, default is `3`                                                       | `pdf2zh_next -i ./example.pdf -r 5`                                                                                   |
| `--config`, `-c`                | Configuration file path                                                                 | `pdf2zh_next -c ./config.json`                                                                                        |
| `--debug`, `-d`                 | Enable debug mode                                                                       | `pdf2zh_next -i ./example.pdf -d`                                                                                      |
| `--yes`, `-y`                   | Skip confirmation prompts                                                               | `pdf2zh_next -i ./example.pdf -y`                                                                                     |
| `--list-languages`, `-ll`       | List supported languages                                                                 | `pdf2zh_next -ll`                                                                                                     |
| `--list-services`, `-lsv`       | List supported translation services                                                     | `pdf2zh_next -lsv`                                                                                                    |
| `--list-math-modes`, `-lmm`     | List math translation modes                                                             | `pdf2zh_next -lmm`                                                                                                    |
| `--list-math-translators`, `-lmt` | List math translators                                                                   | `pdf2zh_next -lmt`                                                                                                    |

---

### OUTPUT

| `--help`, `-h`                  | Zeige Hilfenachricht und beende                                                         | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Zeige Version und beende                                                                | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i`                 | Eingabe-`PDF`-Dateipfad                                                                 | `pdf2zh_next -i ./example.pdf`                                                                                        |
| `--output`, `-o`                | Ausgabe-`PDF`-Dateipfad                                                                 | `pdf2zh_next -i ./example.pdf -o ./example_zh.pdf`                                                                    |
| `--lang`, `-l`                  | Zielsprachcode, Standard ist `zh`, siehe [Unterstützte Sprachen](./SUPPORTED_LANG.md)   | `pdf2zh_next -i ./example.pdf -l ja`                                                                                  |
| `--service`, `-s`               | Übersetzungsdienst, Standard ist `google`, siehe [Übersetzungsdienste](./TRANSLATION.md)| `pdf2zh_next -i ./example.pdf -s deepl`                                                                               |
| `--service-url`, `-su`          | Benutzerdefinierte Übersetzungsdienst-URL                                               | `pdf2zh_next -i ./example.pdf --service-url http://localhost:8080/translate`                                          |
| `--service-key`, `-sk`          | API-Schlüssel des Übersetzungsdienstes (falls erforderlich)                             | `pdf2zh_next -i ./example.pdf -s deepl -sk YOUR_DEEPL_API_KEY`                                                        |
| `--service-region`, `-sr`       | Region des Übersetzungsdienstes (falls erforderlich)                                     | `pdf2zh_next -i ./example.pdf -s azure -sr eastus`                                                                    |
| `--model`, `-m`                 | Übersetzungsmodell (falls erforderlich)                                                 | `pdf2zh_next -i ./example.pdf -s openai -m gpt-4`                                                                     |
| `--math-mode`, `-mm`            | Mathematik-Übersetzungsmodus, Standard ist `normal`, siehe [Mathematik-Übersetzung](./MATH_TRANSLATE.md) | `pdf2zh_next -i ./example.pdf -mm hybrid`                                                                             |
| `--math-translator`, `-mt`      | Mathematik-Übersetzer, Standard ist `latex`, siehe [Mathematik-Übersetzung](./MATH_TRANSLATE.md) | `pdf2zh_next -i ./example.pdf -mt google`                                                                             |
| `--font-size`, `-fs`            | Schriftgrößenanpassung, Standard ist `0`                                                | `pdf2zh_next -i ./example.pdf -fs 2`                                                                                  |
| `--font-family`, `-ff`          | Schriftfamilie, Standard ist `SimSun, NSimSun, serif`                                   | `pdf2zh_next -i ./example.pdf -ff "Times New Roman, serif"`                                                           |
| `--font-family-cjk`, `-ffc`     | CJK-Schriftfamilie, Standard ist `SimSun, NSimSun, serif`                               | `pdf2zh_next -i ./example.pdf -ffc "SimHei, sans-serif"`                                                              |
| `--line-spacing`, `-ls`         | Zeilenabstand, Standard ist `1.2`                                                       | `pdf2zh_next -i ./example.pdf -ls 1.5`                                                                                |
| `--paragraph-spacing`, `-ps`    | Absatzabstand, Standard ist `0.3`                                                       | `pdf2zh_next -i ./example.pdf -ps 0.5`                                                                                |
| `--char-spacing`, `-cs`         | Zeichenabstand, Standard ist `0`                                                        | `pdf2zh_next -i ./example.pdf -cs 0.5`                                                                                |
| `--page-margin`, `-pm`          | Seitenrand, Standard ist `0`                                                            | `pdf2zh_next -i ./example.pdf -pm 10`                                                                                 |
| `--workers`, `-w`               | Anzahl der Worker, Standard ist `4`                                                     | `pdf2zh_next -i ./example.pdf -w 8`                                                                                   |
| `--timeout`, `-t`               | Übersetzungs-Timeout in Sekunden, Standard ist `30`                                     | `pdf2zh_next -i ./example.pdf -t 60`                                                                                  |
| `--retry`, `-r`                 | Anzahl der Wiederholungsversuche, Standard ist `3`                                      | `pdf2zh_next -i ./example.pdf -r 5`                                                                                   |
| `--config`, `-c`                | Konfigurationsdateipfad                                                                 | `pdf2zh_next -c ./config.json`                                                                                        |
| `--debug`, `-d`                 | Aktiviere Debug-Modus                                                                   | `pdf2zh_next -i ./example.pdf -d`                                                                                      |
| `--yes`, `-y`                   | Überspringe Bestätigungsaufforderungen                                                  | `pdf2zh_next -i ./example.pdf -y`                                                                                     |
| `--list-languages`, `-ll`       | Zeige unterstützte Sprachen                                                             | `pdf2zh_next -ll`                                                                                                     |
| `--list-services`, `-lsv`       | Zeige unterstützte Übersetzungsdienste                                                  | `pdf2zh_next -lsv`                                                                                                    |
| `--list-math-modes`, `-lmm`     | Zeige Mathematik-Übersetzungsmodi                                                       | `pdf2zh_next -lmm`                                                                                                    |
| `--list-math-translators`, `-lmt` | Zeige Mathematik-Übersetzer                                                            | `pdf2zh_next -lmt`                                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--proxy`                       | Proxy settings, such as `http://127.0.0.1:7890` or `socks5://127.0.0.1:7890`            | `pdf2zh_next --proxy http://127.0.0.1:7890`                                                                            |
| `--api-key`                     | API key for the translation service                                                     | `pdf2zh_next --api-key sk-xxxxx`                                                                                       |
| `--api-base`                    | Base URL for the translation service, such as `https://api.openai.com`                  | `pdf2zh_next --api-base https://api.openai.com`                                                                        |
| `--model`                       | Model to use for translation, such as `gpt-4o-mini` or `gpt-4o`                         | `pdf2zh_next --model gpt-4o-mini`                                                                                      |
| `--target-language`             | Target language for translation, such as `zh` or `en`                                   | `pdf2zh_next --target-language zh`                                                                                     |
| `--source-language`             | Source language of the document, such as `en` or `ja`                                   | `pdf2zh_next --source-language en`                                                                                     |
| `--concurrency-limit`           | Maximum number of concurrent translation requests                                       | `pdf2zh_next --concurrency-limit 5`                                                                                    |
| `--request-timeout`             | Timeout for each translation request in seconds                                         | `pdf2zh_next --request-timeout 30`                                                                                     |
| `--max-retries`                 | Maximum number of retries for failed translation requests                               | `pdf2zh_next --max-retries 3`                                                                                          |
| `--retry-delay`                 | Delay between retries in seconds                                                        | `pdf2zh_next --retry-delay 5`                                                                                          |
| `--batch-size`                  | Number of text segments to process in each batch                                        | `pdf2zh_next --batch-size 10`                                                                                          |
| `--temperature`                 | Temperature for the translation model, between 0 and 2                                  | `pdf2zh_next --temperature 0.7`                                                                                        |
| `--top-p`                       | Top-p sampling for the translation model, between 0 and 1                               | `pdf2zh_next --top-p 0.9`                                                                                              |
| `--presence-penalty`            | Presence penalty for the translation model, between -2 and 2                            | `pdf2zh_next --presence-penalty 0`                                                                                     |
| `--frequency-penalty`           | Frequency penalty for the translation model, between -2 and 2                           | `pdf2zh_next --frequency-penalty 0`                                                                                    |
| `--max-tokens`                  | Maximum number of tokens to generate in each translation request                        | `pdf2zh_next --max-tokens 4096`                                                                                        |
| `--log-level`                   | Log level, such as `debug`, `info`, `warning`, `error`                                  | `pdf2zh_next --log-level info`                                                                                         |
| `--log-file`                    | Path to the log file                                                                    | `pdf2zh_next --log-file /path/to/log/file.log`                                                                         |
| `--no-cache`                    | Disable caching of translation results                                                  | `pdf2zh_next --no-cache`                                                                                               |
| `--cache-dir`                   | Directory to store cache files                                                          | `pdf2zh_next --cache-dir /path/to/cache`                                                                               |
| `--clean-cache`                 | Clean the cache directory before starting                                               | `pdf2zh_next --clean-cache`                                                                                            |
| `--output-dir`                  | Directory to save the translated document                                               | `pdf2zh_next --output-dir /path/to/output`                                                                             |
| `--output-format`               | Format of the output document, such as `pdf`, `docx`, `txt`, `markdown`                 | `pdf2zh_next --output-format pdf`                                                                                      |
| `--keep-original-format`        | Keep the original document format                                                       | `pdf2zh_next --keep-original-format`                                                                                   |
| `--no-translate`                | Only extract text without translation                                                   | `pdf2zh_next --no-translate`                                                                                           |
| `--translate-only`              | Only translate without extracting text (requires pre-extracted text)                    | `pdf2zh_next --translate-only`                                                                                         |
| `--extract-only`                | Only extract text without translation                                                   | `pdf2zh_next --extract-only`                                                                                           |
| `--resume`                      | Resume from the last interrupted translation                                            | `pdf2zh_next --resume`                                                                                                 |
| `--overwrite`                   | Overwrite existing output files                                                         | `pdf2zh_next --overwrite`                                                                                              |
| `--dry-run`                     | Perform a dry run without actually translating                                          | `pdf2zh_next --dry-run`                                                                                                |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                   |
| `--list-languages`              | List all supported languages                                                            | `pdf2zh_next --list-languages`                                                                                         |
| `--list-models`                 | List all available models for the translation service                                   | `pdf2zh_next --list-models`                                                                                            |
| `--list-output-formats`         | List all supported output formats                                                       | `pdf2zh_next --list-output-formats`                                                                                    |
| `--list-translation-services`   | List all available translation services                                                 | `pdf2zh_next --list-translation-services`                                                                              |

---

### TRANSLATION

| `--config-file`                 | Pfad zur Konfigurationsdatei                                                            | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--proxy`                       | Proxy-Einstellungen, z. B. `http://127.0.0.1:7890` oder `socks5://127.0.0.1:7890`       | `pdf2zh_next --proxy http://127.0.0.1:7890`                                                                            |
| `--api-key`                     | API-Schlüssel für den Übersetzungsdienst                                                | `pdf2zh_next --api-key sk-xxxxx`                                                                                       |
| `--api-base`                    | Basis-URL für den Übersetzungsdienst, z. B. `https://api.openai.com`                    | `pdf2zh_next --api-base https://api.openai.com`                                                                        |
| `--model`                       | Modell für die Übersetzung, z. B. `gpt-4o-mini` oder `gpt-4o`                           | `pdf2zh_next --model gpt-4o-mini`                                                                                      |
| `--target-language`             | Zielsprache für die Übersetzung, z. B. `zh` oder `en`                                   | `pdf2zh_next --target-language zh`                                                                                     |
| `--source-language`             | Ausgangssprache des Dokuments, z. B. `en` oder `ja`                                     | `pdf2zh_next --source-language en`                                                                                     |
| `--concurrency-limit`           | Maximale Anzahl gleichzeitiger Übersetzungsanfragen                                     | `pdf2zh_next --concurrency-limit 5`                                                                                    |
| `--request-timeout`             | Timeout für jede Übersetzungsanfrage in Sekunden                                        | `pdf2zh_next --request-timeout 30`                                                                                     |
| `--max-retries`                 | Maximale Anzahl von Wiederholungsversuchen für fehlgeschlagene Übersetzungsanfragen     | `pdf2zh_next --max-retries 3`                                                                                          |
| `--retry-delay`                 | Verzögerung zwischen Wiederholungsversuchen in Sekunden                                 | `pdf2zh_next --retry-delay 5`                                                                                          |
| `--batch-size`                  | Anzahl der Textsegmente, die in jedem Batch verarbeitet werden                          | `pdf2zh_next --batch-size 10`                                                                                          |
| `--temperature`                 | Temperatur für das Übersetzungsmodell, zwischen 0 und 2                                 | `pdf2zh_next --temperature 0.7`                                                                                        |
| `--top-p`                       | Top-p-Sampling für das Übersetzungsmodell, zwischen 0 und 1                             | `pdf2zh_next --top-p 0.9`                                                                                              |
| `--presence-penalty`            | Presence-Penalty für das Übersetzungsmodell, zwischen -2 und 2                          | `pdf2zh_next --presence-penalty 0`                                                                                     |
| `--frequency-penalty`           | Frequency-Penalty für das Übersetzungsmodell, zwischen -2 und 2                         | `pdf2zh_next --frequency-penalty 0`                                                                                    |
| `--max-tokens`                  | Maximale Anzahl von Tokens, die in jeder Übersetzungsanfrage generiert werden           | `pdf2zh_next --max-tokens 4096`                                                                                        |
| `--log-level`                   | Protokollierungsstufe, z. B. `debug`, `info`, `warning`, `error`                        | `pdf2zh_next --log-level info`                                                                                         |
| `--log-file`                    | Pfad zur Protokolldatei                                                                 | `pdf2zh_next --log-file /path/to/log/file.log`                                                                         |
| `--no-cache`                    | Deaktiviert das Zwischenspeichern von Übersetzungsergebnissen                           | `pdf2zh_next --no-cache`                                                                                               |
| `--cache-dir`                   | Verzeichnis zum Speichern von Cache-Dateien                                             | `pdf2zh_next --cache-dir /path/to/cache`                                                                               |
| `--clean-cache`                 | Bereinigt das Cache-Verzeichnis vor dem Start                                           | `pdf2zh_next --clean-cache`                                                                                            |
| `--output-dir`                  | Verzeichnis zum Speichern des übersetzten Dokuments                                     | `pdf2zh_next --output-dir /path/to/output`                                                                             |
| `--output-format`               | Format des Ausgabedokuments, z. B. `pdf`, `docx`, `txt`, `markdown`                     | `pdf2zh_next --output-format pdf`                                                                                      |
| `--keep-original-format`        | Behält das ursprüngliche Dokumentformat bei                                             | `pdf2zh_next --keep-original-format`                                                                                   |
| `--no-translate`                | Extrahiert nur Text ohne Übersetzung                                                    | `pdf2zh_next --no-translate`                                                                                           |
| `--translate-only`              | Übersetzt nur ohne Textextraktion (erfordert vorab extrahierten Text)                   | `pdf2zh_next --translate-only`                                                                                         |
| `--extract-only`                | Extrahiert nur Text ohne Übersetzung                                                    | `pdf2zh_next --extract-only`                                                                                           |
| `--resume`                      | Setzt die letzte unterbrochene Übersetzung fort                                         | `pdf2zh_next --resume`                                                                                                 |
| `--overwrite`                   | Überschreibt vorhandene Ausgabedateien                                                  | `pdf2zh_next --overwrite`                                                                                              |
| `--dry-run`                     | Führt einen Probelauf ohne tatsächliche Übersetzung durch                               | `pdf2zh_next --dry-run`                                                                                                |
| `--version`                     | Zeigt Versionsinformationen an                                                          | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Zeigt eine Hilfenachricht an                                                            | `pdf2zh_next --help`                                                                                                   |
| `--list-languages`              | Listet alle unterstützten Sprachen auf                                                  | `pdf2zh_next --list-languages`                                                                                         |
| `--list-models`                 | Listet alle verfügbaren Modelle für den Übersetzungsdienst auf                          | `pdf2zh_next --list-models`                                                                                            |
| `--list-output-formats`         | Listet alle unterstützten Ausgabeformate auf                                            | `pdf2zh_next --list-output-formats`                                                                                    |
| `--list-translation-services`   | Listet alle verfügbaren Übersetzungsdienste auf                                         | `pdf2zh_next --list-translation-services`                                                                              |
`5`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `--save-interval`               | Save interval in seconds                                                                 | `pdf2zh_next example.pdf --save-interval 5`                                                                           | `5`                                                                                    |
| `--skip-upload`                 | Skip Uploading, only process local files                                                | `pdf2zh_next example.pdf --skip-upload`                                                                               | `False`                                                                                |
| `--skip-download`               | Skip Downloading, only process online files                                             | `pdf2zh_next example.pdf --skip-download`                                                                             | `False`                                                                                |
| `--skip-process`                | Skip Processing, only upload or download                                                | `pdf2zh_next example.pdf --skip-process`                                                                              | `False`                                                                                |
| `--skip-save`                   | Skip Saving, only process without saving                                                | `pdf2zh_next example.pdf --skip-save`                                                                                | `False`                                                                                |
| `--skip-clean`                  | Skip Cleaning, keep temporary files                                                     | `pdf2zh_next example.pdf --skip-clean`                                                                               | `False`                                                                                |
| `--skip-ocr`                    | Skip OCR, only process text                                                             | `pdf2zh_next example.pdf --skip-ocr`                                                                                 | `False`                                                                                |
| `--skip-translate`              | Skip Translate, only process OCR                                                        | `pdf2zh_next example.pdf --skip-translate`                                                                            | `False`                                                                                |
| `--skip-merge`                  | Skip Merge, only process without merging                                                | `pdf2zh_next example.pdf --skip-merge`                                                                               | `False`                                                                                |

---

### OUTPUT

| `--report-interval`             | Fortschrittsberichtsintervall in Sekunden                                               | `pdf2zh_next example.pdf --report-interval 5`                                                                         | `5`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `--save-interval`               | Speicherintervall in Sekunden                                                           | `pdf2zh_next example.pdf --save-interval 5`                                                                           | `5`                                                                                    |
| `--skip-upload`                 | Hochladen überspringen, nur lokale Dateien verarbeiten                                 | `pdf2zh_next example.pdf --skip-upload`                                                                               | `False`                                                                                |
| `--skip-download`               | Herunterladen überspringen, nur Online-Dateien verarbeiten                              | `pdf2zh_next example.pdf --skip-download`                                                                             | `False`                                                                                |
| `--skip-process`                | Verarbeitung überspringen, nur hochladen oder herunterladen                             | `pdf2zh_next example.pdf --skip-process`                                                                              | `False`                                                                                |
| `--skip-save`                   | Speichern überspringen, nur verarbeiten ohne zu speichern                               | `pdf2zh_next example.pdf --skip-save`                                                                                | `False`                                                                                |
| `--skip-clean`                  | Bereinigen überspringen, temporäre Dateien behalten                                     | `pdf2zh_next example.pdf --skip-clean`                                                                               | `False`                                                                                |
| `--skip-ocr`                    | OCR überspringen, nur Text verarbeiten                                                  | `pdf2zh_next example.pdf --skip-ocr`                                                                                 | `False`                                                                                |
| `--skip-translate`              | Übersetzung überspringen, nur OCR verarbeiten                                           | `pdf2zh_next example.pdf --skip-translate`                                                                            | `False`                                                                                |
| `--skip-merge`                  | Zusammenführen überspringen, nur verarbeiten ohne Zusammenführung                       | `pdf2zh_next example.pdf --skip-merge`                                                                               | `False`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-to-file`                 | Log to a file in the same directory as the output file                                  | `pdf2zh_next example.pdf --log-to-file`                                                                               |
| `--log-level`                   | Set the log level, default is `info`                                                    | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-format`                  | Set the log format, default is `text`                                                   | `pdf2zh_next example.pdf --log-format json`                                                                           |
| `--version`                     | Show version number                                                                     | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |
| `--cache-dir`                   | Set the cache directory, default is `~/.cache/pdf2zh_next`                              | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--cache-size`                  | Set the cache size, default is `100` MB                                                 | `pdf2zh_next example.pdf --cache-size 200`                                                                            |
| `--cache-ttl`                   | Set the cache TTL, default is `7` days                                                  | `pdf2zh_next example.pdf --cache-ttl 30`                                                                              |
| `--cache-cleanup-interval`      | Set the cache cleanup interval, default is `1` hour                                     | `pdf2zh_next example.pdf --cache-cleanup-interval 2`                                                                  |
| `--cache-max-files`             | Set the maximum number of cache files, default is `1000`                                | `pdf2zh_next example.pdf --cache-max-files 2000`                                                                      |
| `--cache-max-size`              | Set the maximum cache size, default is `100` MB                                         | `pdf2zh_next example.pdf --cache-max-size 200`                                                                        |
| `--cache-compression`           | Enable cache compression, default is `false`                                            | `pdf2zh_next example.pdf --cache-compression`                                                                         |
| `--cache-encryption`            | Enable cache encryption, default is `false`                                             | `pdf2zh_next example.pdf --cache-encryption`                                                                          |
| `--cache-encryption-key`        | Set the cache encryption key, default is empty                                          | `pdf2zh_next example.pdf --cache-encryption-key mykey`                                                                |
| `--cache-encryption-algorithm`  | Set the cache encryption algorithm, default is `aes-256-gcm`                            | `pdf2zh_next example.pdf --cache-encryption-algorithm aes-128-gcm`                                                    |
| `--cache-encryption-iv`         | Set the cache encryption IV, default is empty                                           | `pdf2zh_next example.pdf --cache-encryption-iv myiv`                                                                  |
| `--cache-encryption-salt`       | Set the cache encryption salt, default is empty                                         | `pdf2zh_next example.pdf --cache-encryption-salt mysalt`                                                              |
| `--cache-encryption-iterations` | Set the cache encryption iterations, default is `10000`                                 | `pdf2zh_next example.pdf --cache-encryption-iterations 20000`                                                         |
| `--cache-encryption-key-length` | Set the cache encryption key length, default is `32`                                    | `pdf2zh_next example.pdf --cache-encryption-key-length 16`                                                            |
| `--cache-encryption-mode`       | Set the cache encryption mode, default is `gcm`                                         | `pdf2zh_next example.pdf --cache-encryption-mode cbc`                                                                 |
| `--cache-encryption-padding`    | Set the cache encryption padding, default is `pkcs7`                                    | `pdf2zh_next example.pdf --cache-encryption-padding none`                                                             |
| `--cache-encryption-hash`       | Set the cache encryption hash, default is `sha256`                                      | `pdf2zh_next example.pdf --cache-encryption-hash sha512`                                                              |
| `--cache-encryption-hmac`       | Set the cache encryption HMAC, default is `false`                                       | `pdf2zh_next example.pdf --cache-encryption-hmac`                                                                     |
| `--cache-encryption-hmac-key`   | Set the cache encryption HMAC key, default is empty                                     | `pdf2zh_next example.pdf --cache-encryption-hmac-key myhmackey`                                                       |
| `--cache-encryption-hmac-algorithm` | Set the cache encryption HMAC algorithm, default is `sha256`                        | `pdf2zh_next example.pdf --cache-encryption-hmac-algorithm sha512`                                                    |
| `--cache-encryption-hmac-length` | Set the cache encryption HMAC length, default is `32`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-length 64`                                                           |
| `--cache-encryption-hmac-mode`  | Set the cache encryption HMAC mode, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Set the cache encryption HMAC padding, default is `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Set the cache encryption HMAC hash, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Set the cache encryption HMAC iterations, default is `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length` | Set the cache encryption HMAC key length, default is `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Set the cache encryption HMAC salt, default is empty                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Set the cache encryption HMAC IV, default is empty                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmaciv`                                                         |
| `--cache-encryption-hmac-mode`  | Set the cache encryption HMAC mode, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Set the cache encryption HMAC padding, default is `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Set the cache encryption HMAC hash, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Set the cache encryption HMAC iterations, default is `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length` | Set the cache encryption HMAC key length, default is `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Set the cache encryption HMAC salt, default is empty                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Set the cache encryption HMAC IV, default is empty                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmaciv`                                                         |
| `--cache-encryption-hmac-mode`  | Set the cache encryption HMAC mode, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Set the cache encryption HMAC padding, default is `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Set the cache encryption HMAC hash, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Set the cache encryption HMAC iterations, default is `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length` | Set the cache encryption HMAC key length, default is `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Set the cache encryption HMAC salt, default is empty                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Set the cache encryption HMAC IV, default is empty                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmaciv`                                                         |
| `--cache-encryption-hmac-mode`  | Set the cache encryption HMAC mode, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Set the cache encryption HMAC padding, default is `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Set the cache encryption HMAC hash, default is `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Set the cache encryption HMAC iterations, default is `极客时间`                       | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |

---

### OUTPUT

| `--debug`                       | Debug-Logging-Level verwenden                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-to-file`                 | In eine Datei im selben Verzeichnis wie die Ausgabedatei loggen                                  | `pdf2zh_next example.pdf --log-to-file`                                                                               |
| `--log-level`                   | Log-Level festlegen, Standard ist `info`                                                    | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-format`                  | Log-Format festlegen, Standard ist `text`                                                   | `pdf2zh_next example.pdf --log-format json`                                                                           |
| `--version`                     | Versionsnummer anzeigen                                                                     | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Hilfe-Nachricht anzeigen                                                                       | `pdf2zh_next --help`                                                                                                  |
| `--cache-dir`                   | Cache-Verzeichnis festlegen, Standard ist `~/.cache/pdf2zh_next`                              | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--cache-size`                  | Cache-Größe festlegen, Standard ist `100` MB                                                 | `pdf2zh_next example.pdf --cache-size 200`                                                                            |
| `--cache-ttl`                   | Cache-TTL festlegen, Standard ist `7` Tage                                                  | `pdf2zh_next example.pdf --cache-ttl 30`                                                                              |
| `--cache-cleanup-interval`      | Cache-Bereinigungsintervall festlegen, Standard ist `1` Stunde                                     | `pdf2zh_next example.pdf --cache-cleanup-interval 2`                                                                  |
| `--cache-max-files`             | Maximale Anzahl an Cache-Dateien festlegen, Standard ist `1000`                                | `pdf2zh_next example.pdf --cache-max-files 2000`                                                                      |
| `--cache-max-size`              | Maximale Cache-Größe festlegen, Standard ist `100` MB                                         | `pdf2zh_next example.pdf --cache-max-size 200`                                                                        |
| `--cache-compression`           | Cache-Kompression aktivieren, Standard ist `false`                                            | `pdf2zh_next example.pdf --cache-compression`                                                                         |
| `--cache-encryption`            | Cache-Verschlüsselung aktivieren, Standard ist `false`                                             | `pdf2zh_next example.pdf --cache-encryption`                                                                          |
| `--cache-encryption-key`        | Cache-Verschlüsselungsschlüssel festlegen, Standard ist leer                                          | `pdf2zh_next example.pdf --cache-encryption-key mykey`                                                                |
| `--cache-encryption-algorithm`  | Cache-Verschlüsselungsalgorithmus festlegen, Standard ist `aes-256-gcm`                            | `pdf2zh_next example.pdf --cache-encryption-algorithm aes-128-gcm`                                                    |
| `--cache-encryption-iv`         | Cache-Verschlüsselungs-IV festlegen, Standard ist leer                                           | `pdf2zh_next example.pdf --cache-encryption-iv myiv`                                                                  |
| `--cache-encryption-salt`       | Cache-Verschlüsselungs-Salt festlegen, Standard ist leer                                         | `pdf2zh_next example.pdf --cache-encryption-salt mysalt`                                                              |
| `--cache-encryption-iterations` | Cache-Verschlüsselungs-Iterationen festlegen, Standard ist `10000`                                 | `pdf2zh_next example.pdf --cache-encryption-iterations 极客时间`                                                         |
| `--cache-encryption-key-length` | Cache-Verschlüsselungsschlüssellänge festlegen, Standard ist `32`                                    | `极客时间 example.pdf --cache-encryption-key-length 16`                                                            |
| `--cache-encryption-mode`       | Cache-Verschlüsselungsmodus festlegen, Standard ist `gcm`                                         | `pdf2zh_next example.pdf --cache-encryption-mode cbc`                                                                 |
| `--极客时间-padding`    | Cache-Verschlüsselungs-Padding festlegen, Standard ist `pkcs7`                                    | `pdf2zh_next example.pdf --cache-encryption-padding none`                                                             |
| `--cache-encryption-hash`       | Cache-Verschlüsselungs-Hash festlegen, Standard ist `sha256`                                      | `pdf2zh_next example.pdf --cache-encryption-hash sha512`                                                              |
| `--cache-encryption-hmac`       | Cache-Verschlüsselungs-HMAC aktivieren, Standard ist `false`                                       | `pdf 极客时间 example.pdf --cache-encryption-hmac`                                                                     |
| `--cache-encryption-hmac-key`   | Cache-Verschlüsselungs-HMAC-Schlüssel festlegen, Standard ist leer                                     | `pdf2zh_next example.pdf --cache-encryption-hmac-key myhmackey`                                                       |
| `--cache-encryption-hmac-algorithm` | Cache-Verschlüsselungs-HMAC-Algorithmus festlegen, Standard ist `sha256`                        | `pdf2zh_next example.pdf --cache-encryption-hmac-algorithm sha512`                                                    |
| `--cache-encryption-hmac-length` | Cache-Verschlüsselungs-HMAC-Länge festlegen, Standard ist `32`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-length 64`                                                           |
| `--cache-encryption-hmac-mode`  | Cache-Verschlüsselungs-HMAC-Modus festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Cache-Verschlüsselungs-HMAC-Padding festlegen, Standard ist `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-h 极客时间`  | Cache-Verschlüsselungs-HMAC-Hash festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Cache-Verschlüsselungs-HMAC-Iterationen festlegen, Standard ist `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length` | Cache-Verschlüsselungs-HMAC-Schlüssellänge festlegen, Standard ist `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Cache-Verschlüsselungs-HMAC-Salt festlegen, Standard ist leer                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Cache-Verschlüsselungs-HMAC-IV festlegen, Standard ist leer                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmac 极客时间`                                                         |
| `--cache-encryption-hmac-mode`  | Cache-Verschlüsselungs-HMAC-Modus festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Cache-Verschlüsselungs-HMAC-Padding festlegen, Standard ist `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Cache-Verschlüsselungs-HMAC-Hash festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Cache-Verschlüsselungs-HMAC-Iterationen festlegen, Standard ist `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length` | Cache-Verschlüsselungs-HMAC-Schlüssellänge festlegen, Standard ist `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Cache-Verschlüsselungs-HMAC-Salt festlegen, Standard ist leer                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Cache-Verschlüsselungs-HMAC-IV festlegen, Standard ist leer                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmaciv`                                                         |
| `--cache-encryption-hmac-mode`  | Cache-Verschlüsselungs-HMAC-Modus festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Cache-Verschlüsselungs-HMAC-Padding festlegen, Standard ist `pkcs 极客时间`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Cache-Verschlüsselungs-HMAC-Hash festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Cache-Verschlüsselungs-HMAC-Iterationen festlegen, Standard ist `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length 极客时间` | Cache-Verschlüsselungs-HMAC-Schlüssellänge festlegen, Standard ist `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Cache-Verschlüsselungs-HMAC-Salt festlegen, Standard ist leer                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Cache-Verschlüsselungs-HMAC-IV festlegen, Standard ist leer                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmaciv`                                                         |
| `--cache-encryption-hmac-mode`  | Cache-Verschlüsselungs-HMAC-Modus festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Cache-Verschlüsselungs-HMAC-Padding festlegen, Standard ist `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption 极客时间-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Cache-Verschlüsselungs-HMAC-Hash festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Cache-Verschlüsselungs-HMAC-Iterationen festlegen, Standard ist `10000`                         | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| `--cache-encryption-hmac-key-length` | Cache-Verschlüsselungs-HMAC-Schlüssellänge festlegen, Standard ist `32`                          | `pdf2zh_next example.pdf --cache-encryption-hmac-key-length 16`                                                       |
| `--cache-encryption-hmac-salt`  | Cache-Verschlüsselungs-HMAC-Salt festlegen, Standard ist leer                                    | `pdf2zh_next example.pdf --cache-encryption-hmac-salt myhmacsalt`                                                     |
| `--cache-encryption-hmac-iv`    | Cache-Verschlüsselungs-HMAC-IV festlegen, Standard ist leer                                      | `pdf2zh_next example.pdf --cache-encryption-hmac-iv myhmaciv`                                                         |
| `--cache-encryption-hmac-mode`  | Cache-Verschlüsselungs-HMAC-Modus festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-mode sha512`                                                         |
| `--cache-encryption-hmac-padding` | Cache-Verschlüsselungs-HMAC-Padding festlegen, Standard ist `pkcs7`                             | `pdf2zh_next example.pdf --cache-encryption-hmac-padding none`                                                        |
| `--cache-encryption-hmac-hash`  | Cache-Verschlüsselungs-HMAC-Hash festlegen, Standard ist `sha256`                                 | `pdf2zh_next example.pdf --cache-encryption-hmac-hash sha512`                                                         |
| `--cache-encryption-hmac-iterations` | Cache-Verschlüsselungs-HMAC-Iterationen festlegen, Standard ist `极客时间`                       | `pdf2zh_next example.pdf --cache-encryption-hmac-iterations 20000`                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-i <path>, --input <path>`     | Input file path                                                                         | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o <path>, --output <path>`    | Output file path                                                                        | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-s <code>, --source <code>`    | Source language code                                                                    | `pdf2zh_next -i input.pdf -s en`                                                                                      |
| `-t <code>, --target <code>`    | Target language code                                                                    | `pdf2zh_next -i input.pdf -t zh`                                                                                      |
| `-m <code>, --model <code>`     | Translation model, refer to [Supported Languages](./SUPPORTED_LANGUAGES.md) for details | `pdf2zh_next -i input.pdf -m gpt-4o-mini`                                                                             |
| `--pdf-translator <translator>` | PDF translator, refer to [Supported Languages](./SUPPORTED_LANGUAGES.md) for details    | `pdf2zh_next -i input.pdf --pdf-translator docling`                                                                   |
| `--translator <translator>`     | Translation service, refer to [Documentation of Translation Services](./TRANSLATOR.md)  | `pdf2zh_next -i input.pdf --translator azure`                                                                         |
| `--key <key>`                   | API key for translation service                                                         | `pdf2zh_next -i input.pdf --translator azure --key <your_key>`                                                        |
| `--endpoint <endpoint>`         | API endpoint for translation service                                                    | `pdf2zh_next -i input.pdf --translator azure --endpoint <your_endpoint>`                                              |
| `--region <region>`             | API region for translation service                                                      | `pdf2zh_next -i input.pdf --translator azure --region <your_region>`                                                  |
| `--workers <number>`            | Number of concurrent workers for translation                                            | `pdf2zh_next -i input.pdf --workers 4`                                                                                |
| `--no-split`                    | Disable paragraph splitting                                                             | `pdf2zh_next -i input.pdf --no-split`                                                                                 |
| `--no-translate`                | Disable translation (useful for extracting text)                                        | `pdf2zh_next -i input.pdf --no-translate`                                                                             |
| `--no-ocr`                      | Disable OCR (useful for text-based PDFs)                                                | `pdf2zh_next -i input.pdf --no-ocr`                                                                                   |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next -i input.pdf --verbose`                                                                                  |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--gui`                         | Interaktion mit der GUI                                                                       | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-i <path>, --input <path>`     | Eingabedateipfad                                                                              | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o <path>, --output <path>`    | Ausgabedateipfad                                                                              | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-s <code>, --source <code>`    | Quellsprachcode                                                                               | `pdf2zh_next -i input.pdf -s en`                                                                                      |
| `-t <code>, --target <code>`    | Zielsprachcode                                                                                | `pdf2zh_next -i input.pdf -t zh`                                                                                      |
| `-m <code>, --model <code>`     | Übersetzungsmodell, siehe [Unterstützte Sprachen](./SUPPORTED_LANGUAGES.md) für Details       | `pdf2zh_next -i input.pdf -m gpt-4o-mini`                                                                             |
| `--pdf-translator <translator>` | PDF-Übersetzer, siehe [Unterstützte Sprachen](./SUPPORTED_LANGUAGES.md) für Details           | `pdf2zh_next -i input.pdf --pdf-translator docling`                                                                   |
| `--translator <translator>`     | Übersetzungsdienst, siehe [Dokumentation der Übersetzungsdienste](./TRANSLATOR.md)            | `pdf2zh_next -i input.pdf --translator azure`                                                                         |
| `--key <key>`                   | API-Schlüssel für den Übersetzungsdienst                                                      | `pdf2zh_next -i input.pdf --translator azure --key <your_key>`                                                        |
| `--endpoint <endpoint>`         | API-Endpunkt für den Übersetzungsdienst                                                       | `pdf2zh_next -i input.pdf --translator azure --endpoint <your_endpoint>`                                              |
| `--region <region>`             | API-Region für den Übersetzungsdienst                                                         | `pdf2zh_next -i input.pdf --translator azure --region <your_region>`                                                  |
| `--workers <number>`            | Anzahl der gleichzeitigen Worker für die Übersetzung                                           | `pdf2zh_next -i input.pdf --workers 4`                                                                                |
| `--no-split`                    | Absatzaufteilung deaktivieren                                                                 | `pdf2zh_next -i input.pdf --no-split`                                                                                 |
| `--no-translate`                | Übersetzung deaktivieren (nützlich zum Extrahieren von Text)                                  | `pdf2zh_next -i input.pdf --no-translate`                                                                             |
| `--no-ocr`                      | OCR deaktivieren (nützlich für textbasierte PDFs)                                             | `pdf2zh_next -i input.pdf --no-ocr`                                                                                   |
| `--verbose`                     | Ausführliche Ausgabe aktivieren                                                               | `pdf2zh_next -i input.pdf --verbose`                                                                                  |
| `--version`                     | Versionsinformationen anzeigen                                                                | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Hilfenachricht anzeigen                                                                       | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-warmup`                   | Disable the warmup process, which includes downloading and verifying required assets    | `pdf2zh_next example.pdf --no-warmup`                                                                                 |
| `--log-level <level>`           | Set the log level (default: `info`)                                                     | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-to-file`                 | Save logs to a file (default: disabled)                                                 | `pdf2zh_next example.pdf --log-to-file`                                                                               |
| `--log-file <path>`             | Specify the log file path (default: `pdf2zh_next.log`)                                  | `pdf2zh_next example.pdf --log-file mylog.txt`                                                                        |
| `--log-format <format>`         | Set the log format (`json` or `text`, default: `text`)                                  | `pdf2zh_next example.pdf --log-format json`                                                                           |
| `--log-keep <number>`           | Number of log files to keep (default: `5`)                                              | `pdf2zh_next example.pdf --log-keep 10`                                                                               |
| `--log-compress`                | Compress old log files (default: disabled)                                              | `pdf2zh_next example.pdf --log-compress`                                                                              |
| `--config <path>`               | Specify a custom configuration file                                                     | `pdf2zh_next example.pdf --config ./myconfig.yaml`                                                                    |
| `--cache-dir <path>`            | Specify the cache directory (default: `~/.cache/pdf2zh_next`)                           | `pdf2zh_next example.pdf --cache-dir ./mycache`                                                                       |
| `--output-dir <path>`           | Specify the output directory (default: current directory)                               | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-suffix <suffix>`      | Add a suffix to the output filename (default: `_translated`)                            | `pdf2zh_next example.pdf --output-suffix _zh`                                                                         |
| `--output-format <format>`      | Set the output format (`pdf`, `markdown`, or `text`, default: `pdf`)                    | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--target-lang <lang>`          | Set the target language (default: `zh`)                                                 | `pdf2zh_next example.pdf --target-lang en`                                                                            |
| `--source-lang <lang>`          | Set the source language (default: `auto`)                                               | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--translator <translator>`     | Set the translator service (`google`, `azure`, `deepl`, `openai`, default: `google`)    | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-key <key>`        | Set the translator API key (if required)                                                | `pdf2zh_next example.pdf --translator-key YOUR_API_KEY`                                                               |
| `--translator-endpoint <url>`   | Set the translator endpoint (for self-hosted services)                                  | `pdf2zh_next example.pdf --translator-endpoint http://localhost:8080`                                                 |
| `--translator-region <region>`  | Set the translator region (for some services like Azure)                                | `pdf2zh_next example.pdf --translator-region eastus`                                                                  |
| `--translator-model <model>`    | Set the translator model (for some services like OpenAI)                                | `pdf2zh_next example.pdf --translator-model gpt-4`                                                                    |
| `--math-translator <translator>`| Set the math translator service (`none`, `pdfmathtranslate`, default: `pdfmathtranslate`) | `pdf2zh_next example.pdf --math-translator none`                                                                      |
| `--math-translator-key <key>`   | Set the math translator API key (if required)                                           | `pdf2zh_next example.pdf --math-translator-key YOUR_API_KEY`                                                          |
| `--math-translator-endpoint <url>`| Set the math translator endpoint (for self-hosted services)                             | `pdf2zh_next example.pdf --math-translator-endpoint http://localhost:8081`                                            |
| `--math-keep-original`          | Keep the original math expressions (default: disabled)                                  | `pdf2zh_next example.pdf --math-keep-original`                                                                        |
| `--math-translate-words`        | Translate words in math expressions (default: disabled)                                 | `pdf2zh_next example.pdf --math-translate-words`                                                                      |
| `--ocr-engine <engine>`         | Set the OCR engine (`tesseract`, `easyocr`, default: `tesseract`)                       | `pdf2zh_next example.pdf --ocr-engine easyocr`                                                                        |
| `--ocr-lang <lang>`             | Set the OCR language (default: `eng`)                                                   | `pdf2zh_next example.pdf --ocr-lang chi_sim`                                                                          |
| `--ocr-dpi <dpi>`               | Set the OCR DPI (default: `300`)                                                        | `pdf2zh_next example.pdf --ocr-dpi 600`                                                                               |
| `--ocr-timeout <seconds>`       | Set the OCR timeout in seconds (default: `30`)                                          | `pdf2zh_next example.pdf --ocr-timeout 60`                                                                            |
| `--concurrency <number>`        | Set the number of concurrent tasks (default: `4`)                                       | `pdf2zh_next example.pdf --concurrency 8`                                                                             |
| `--timeout <seconds>`           | Set the overall timeout in seconds (default: `3600`)                                    | `pdf2zh_next example.pdf --timeout 7200`                                                                              |
| `--retry <number>`              | Set the number of retries for failed tasks (default: `3`)                               | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--retry-delay <seconds>`       | Set the delay between retries in seconds (default: `1`)                                 | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |
| `--max-requests <number>`       | Set the maximum number of requests per minute (default: `60`)                           | `pdf2zh_next example.pdf --max-requests 30`                                                                           |
| `--proxy <url>`                 | Set the proxy URL                                                                       | `pdf2zh_next example.pdf --proxy http://proxy.example.com:8080`                                                       |
| `--no-proxy`                    | Disable proxy usage                                                                     | `pdf2zh_next example.pdf --no-proxy`                                                                                  |
| `--user-agent <string>`         | Set the user agent string                                                               | `pdf2zh_next example.pdf --user-agent "My Custom Agent"`                                                              |
| `--cookie <string>`             | Set the cookie string                                                                   | `pdf2zh_next example.pdf --cookie "session=abc123"`                                                                   |
| `--header <string>`             | Add a custom header (can be used multiple times)                                        | `pdf2zh_next example.pdf --header "Authorization: Bearer token" --header "X-Custom: value"`                           |
| `--page-range <range>`          | Process only specified pages (e.g., `1-5,8,10-12`)                                      | `pdf2zh_next example.pdf --page-range 1-5,10`                                                                         |
| `--ignore-images`               | Skip image processing                                                                   | `pdf2zh_next example.pdf --ignore-images`                                                                             |
| `--ignore-tables`               | Skip table processing                                                                   | `pdf2zh_next example.pdf --ignore-tables`                                                                             |
| `--ignore-math`                 | Skip math processing                                                                    | `pdf2zh_next example.pdf --ignore-math`                                                                               |
| `--ignore-footnotes`            | Skip footnote processing                                                                | `pdf2zh_next example.pdf --ignore-footnotes`                                                                          |
| `--ignore-headers`              | Skip header processing                                                                  | `pdf2zh_next example.pdf --ignore-headers`                                                                            |
| `--ignore-footers`              | Skip footer processing                                                                  | `pdf2zh_next example.pdf --ignore-footers`                                                                            |
| `--keep-layout`                 | Preserve the original layout as much as possible (default: enabled)                     | `pdf2zh_next example.pdf --no-keep-layout`                                                                            |
| `--keep-fonts`                  | Preserve the original fonts (default: enabled)                                          | `pdf2zh_next example.pdf --no-keep-fonts`                                                                             |
| `--keep-colors`                 | Preserve the original colors (default: enabled)                                         | `pdf2zh_next example.pdf --no-keep-colors`                                                                            |
| `--keep-links`                  | Preserve hyperlinks (default: enabled)                                                  | `pdf2zh_next example.pdf --no-keep-links`                                                                             |
| `--keep-annotations`            | Preserve annotations (default: enabled)                                                 | `pdf2zh_next example.pdf --no-keep-annotations`                                                                       |
| `--watermark <text>`            | Add a watermark to the output                                                           | `pdf2zh_next example.pdf --watermark "Translated by pdf2zh"`                                                          |
| `--watermark-opacity <opacity>` | Set the watermark opacity (0.0 to 1.0, default: `0.2`)                                  | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     |
| `--watermark-font-size <size>`  | Set the watermark font size (default: `48`)                                             | `pdf2zh_next example.pdf --watermark-font-size 24`                                                                    |
| `--watermark-rotation <angle>`  | Set the watermark rotation angle in degrees (default: `45`)                             | `pdf2zh_next example.pdf --watermark-rotation 30`                                                                     |
| `--watermark-color <color>`     | Set the watermark color (default: `#cccccc`)                                            | `pdf2zh_next example.pdf --watermark-color #ff0000`                                                                   |
| `--progress`                    | Show progress bar (default: enabled)                                                    | `pdf2zh_next example.pdf --no-progress`                                                                               |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--quiet`                       | Disable all non-error output                                                            | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `--version`                     | Show version information and exit                                                       | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT

| `--warmup`                      | Lädt und überprüft nur die erforderlichen Assets und beendet dann den Vorgang                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-warmup`                   | Deaktiviert den Warmup-Prozess, der das Herunterladen und Überprüfen der erforderlichen Assets umfasst            | `pdf2zh_next example.pdf --no-warmup`                                                                                 |
| `--log-level <level>`           | Legt den Log-Level fest (Standard: `info`)                                                                        | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-to-file`                 | Speichert Logs in einer Datei (Standard: deaktiviert)                                                             | `pdf2zh_next example.pdf --log-to-file`                                                                               |
| `--log-file <path>`             | Gibt den Pfad der Log-Datei an (Standard: `pdf2zh_next.log`)                                                      | `pdf2zh_next example.pdf --log-file mylog.txt`                                                                        |
| `--log-format <format>`         | Legt das Log-Format fest (`json` oder `text`, Standard: `text`)                                                   | `pdf2zh_next example.pdf --log-format json`                                                                           |
| `--log-keep <number>`           | Anzahl der aufzubewahrenden Log-Dateien (Standard: `5`)                                                           | `pdf2zh_next example.pdf --log-keep 10`                                                                               |
| `--log-compress`                | Komprimiert alte Log-Dateien (Standard: deaktiviert)                                                              | `pdf2zh_next example.pdf --log-compress`                                                                              |
| `--config <path>`               | Gibt eine benutzerdefinierte Konfigurationsdatei an                                                               | `pdf2zh_next example.pdf --config ./myconfig.yaml`                                                                    |
| `--cache-dir <path>`            | Gibt das Cache-Verzeichnis an (Standard: `~/.cache/pdf2zh_next`)                                                  | `pdf2zh_next example.pdf --cache-dir ./mycache`                                                                       |
| `--output-dir <path>`           | Gibt das Ausgabeverzeichnis an (Standard: aktuelles Verzeichnis)                                                  | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-suffix <suffix>`      | Fügt dem Ausgabedateinamen ein Suffix hinzu (Standard: `_translated`)                                             | `pdf2zh_next example.pdf --output-suffix _zh`                                                                         |
| `--output-format <format>`      | Legt das Ausgabeformat fest (`pdf`, `markdown` oder `text`, Standard: `pdf`)                                      | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--target-lang <lang>`          | Legt die Zielsprache fest (Standard: `zh`)                                                                        | `pdf2zh_next example.pdf --target-lang en`                                                                            |
| `--source-lang <lang>`          | Legt die Ausgangssprache fest (Standard: `auto`)                                                                  | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--translator <translator>`     | Legt den Übersetzungsdienst fest (`google`, `azure`, `deepl`, `openai`, Standard: `google`)                        | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-key <key>`        | Legt den Übersetzer-API-Schlüssel fest (falls erforderlich)                                                       | `pdf2zh_next example.pdf --translator-key YOUR_API_KEY`                                                               |
| `--translator-endpoint <url>`   | Legt den Übersetzer-Endpunkt fest (für selbst gehostete Dienste)                                                  | `pdf2zh_next example.pdf --translator-endpoint http://localhost:8080`                                                 |
| `--translator-region <region>`  | Legt die Übersetzer-Region fest (für einige Dienste wie Azure)                                                    | `pdf2zh_next example.pdf --translator-region eastus`                                                                  |
| `--translator-model <model>`    | Legt das Übersetzer-Modell fest (für einige Dienste wie OpenAI)                                                    | `pdf2zh_next example.pdf --translator-model gpt-4`                                                                    |
| `--math-translator <translator>`| Legt den Mathematik-Übersetzungsdienst fest (`none`, `pdfmathtranslate`, Standard: `pdfmathtranslate`)             | `pdf2zh_next example.pdf --math-translator none`                                                                      |
| `--math-translator-key <key>`   | Legt den Mathematik-Übersetzer-API-Schlüssel fest (falls erforderlich)                                            | `pdf2zh_next example.pdf --math-translator-key YOUR_API_KEY`                                                          |
| `--math-translator-endpoint <url>`| Legt den Mathematik-Übersetzer-Endpunkt fest (für selbst gehostete Dienste)                                       | `pdf2zh_next example.pdf --math-translator-endpoint http://localhost:8081`                                            |
| `--math-keep-original`          | Behält die ursprünglichen mathematischen Ausdrücke bei (Standard: deaktiviert)                                    | `pdf2zh_next example.pdf --math-keep-original`                                                                        |
| `--math-translate-words`        | Übersetzt Wörter in mathematischen Ausdrücken (Standard: deaktiviert)                                             | `pdf2zh_next example.pdf --math-translate-words`                                                                      |
| `--ocr-engine <engine>`         | Legt die OCR-Engine fest (`tesseract`, `easyocr`, Standard: `tesseract`)                                          | `pdf2zh_next example.pdf --ocr-engine easyocr`                                                                        |
| `--ocr-lang <lang>`             | Legt die OCR-Sprache fest (Standard: `eng`)                                                                       | `pdf2zh_next example.pdf --ocr-lang chi_sim`                                                                          |
| `--ocr-dpi <dpi>`               | Legt die OCR-DPI fest (Standard: `300`)                                                                           | `pdf2zh_next example.pdf --ocr-dpi 600`                                                                               |
| `--ocr-timeout <seconds>`       | Legt den OCR-Timeout in Sekunden fest (Standard: `30`)                                                            | `pdf2zh_next example.pdf --ocr-timeout 60`                                                                            |
| `--concurrency <number>`        | Legt die Anzahl der gleichzeitigen Aufgaben fest (Standard: `4`)                                                  | `pdf2zh_next example.pdf --concurrency 8`                                                                             |
| `--timeout <seconds>`           | Legt den Gesamt-Timeout in Sekunden fest (Standard: `3600`)                                                       | `pdf2zh_next example.pdf --timeout 7200`                                                                              |
| `--retry <number>`              | Legt die Anzahl der Wiederholungsversuche für fehlgeschlagene Aufgaben fest (Standard: `3`)                       | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--retry-delay <seconds>`       | Legt die Verzögerung zwischen Wiederholungsversuchen in Sekunden fest (Standard: `1`)                             | `pdf2zh_next example.pdf --retry-delay 2`                                                                             |
| `--max-requests <number>`       | Legt die maximale Anzahl der Anfragen pro Minute fest (Standard: `60`)                                            | `pdf2zh_next example.pdf --max-requests 30`                                                                           |
| `--proxy <url>`                 | Legt die Proxy-URL fest                                                                                           | `pdf2zh_next example.pdf --proxy http://proxy.example.com:8080`                                                       |
| `--no-proxy`                    | Deaktiviert die Proxy-Verwendung                                                                                  | `pdf2zh_next example.pdf --no-proxy`                                                                                  |
| `--user-agent <string>`         | Legt den User-Agent-String fest                                                                                   | `pdf2zh_next example.pdf --user-agent "My Custom Agent"`                                                              |
| `--cookie <string>`             | Legt den Cookie-String fest                                                                                       | `pdf2zh_next example.pdf --cookie "session=abc123"`                                                                   |
| `--header <string>`             | Fügt einen benutzerdefinierten Header hinzu (kann mehrfach verwendet werden)                                      | `pdf2zh_next example.pdf --header "Authorization: Bearer token" --header "X-Custom: value"`                           |
| `--page-range <range>`          | Verarbeitet nur angegebene Seiten (z. B. `1-5,8,10-12`)                                                           | `pdf2zh_next example.pdf --page-range 1-5,10`                                                                         |
| `--ignore-images`               | Überspringt die Bildverarbeitung                                                                                  | `pdf2zh_next example.pdf --ignore-images`                                                                             |
| `--ignore-tables`               | Überspringt die Tabellenverarbeitung                                                                              | `pdf2zh_next example.pdf --ignore-tables`                                                                             |
| `--ignore-math`                 | Überspringt die mathematische Verarbeitung                                                                        | `pdf2zh_next example.pdf --ignore-math`                                                                               |
| `--ignore-footnotes`            | Überspringt die Fußnotenverarbeitung                                                                              | `pdf2zh_next example.pdf --ignore-footnotes`                                                                          |
| `--ignore-headers`              | Überspringt die Kopfzeilenverarbeitung                                                                            | `pdf2zh_next example.pdf --ignore-headers`                                                                            |
| `--ignore-footers`              | Überspringt die Fußzeilenverarbeitung                                                                             | `pdf2zh_next example.pdf --ignore-footers`                                                                            |
| `--keep-layout`                 | Bewahrt die ursprüngliche Layout so weit wie möglich (Standard: aktiviert)                                        | `pdf2zh_next example.pdf --no-keep-layout`                                                                            |
| `--keep-fonts`                  | Bewahrt die ursprünglichen Schriftarten (Standard: aktiviert)                                                     | `pdf2zh_next example.pdf --no-keep-fonts`                                                                             |
| `--keep-colors`                 | Bewahrt die ursprünglichen Farben (Standard: aktiviert)                                                           | `pdf2zh_next example.pdf --no-keep-colors`                                                                            |
| `--keep-links`                  | Bewahrt Hyperlinks (Standard: aktiviert)                                                                          | `pdf2zh_next example.pdf --no-keep-links`                                                                             |
| `--keep-annotations`            | Bewahrt Anmerkungen (Standard: aktiviert)                                                                         | `pdf2zh_next example.pdf --no-keep-annotations`                                                                       |
| `--watermark <text>`            | Fügt dem Ausgabedokument einen Wasserzeichen hinzu                                                                | `pdf2zh_next example.pdf --watermark "Translated by pdf2zh"`                                                          |
| `--watermark-opacity <opacity>` | Legt die Deckkraft des Wasserzeichens fest (0.0 bis 1.0, Standard: `0.2`)                                         | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     |
| `--watermark-font-size <size>`  | Legt die Schriftgröße des Wasserzeichens fest (Standard: `48`)                                                    | `pdf2zh_next example.pdf --watermark-font-size 24`                                                                    |
| `--watermark-rotation <angle>`  | Legt den Rotationswinkel des Wasserzeichens in Grad fest (Standard: `45`)                                         | `pdf2zh_next example.pdf --watermark-rotation 30`                                                                     |
| `--watermark-color <color>`     | Legt die Farbe des Wasserzeichens fest (Standard: `#cccccc`)                                                      | `pdf2zh_next example.pdf --watermark-color #ff0000`                                                                   |
| `--progress`                    | Zeigt die Fortschrittsleiste an (Standard: aktiviert)                                                             | `pdf2zh_next example.pdf --no-progress`                                                                               |
| `--verbose`                     | Aktiviert die ausführliche Ausgabe                                                                                | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--quiet`                       | Deaktiviert alle Nicht-Fehler-Ausgaben                                                                            | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `--version`                     | Zeigt Versionsinformationen an und beendet das Programm                                                           | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Zeigt die Hilfemeldung an und beendet das Programm                                                                | `pdf2zh_next --help`                                                                                                  |
`-g`    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- |
| `--generate-offline-assets-only` | Generate offline assets without translating                                             | `pdf2zh_next example.pdf --generate-offline-assets-only /path`                                                        | `-G`    |
| `--offline-assets`              | Use offline assets                                                                      | `pdf2zh_next example.pdf --offline-assets /path`                                                                      | `-o`    |

---

### TRANSLATION RESULT

| `--generate-offline-assets`     | Generiere ein Offline-Asset-Paket im angegebenen Verzeichnis                           | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             | `-g`    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- |
| `--generate-offline-assets-only` | Generiere Offline-Assets ohne Übersetzung                                               | `pdf2zh_next example.pdf --generate-offline-assets-only /path`                                                        | `-G`    |
| `--offline-assets`              | Verwende Offline-Assets                                                                 | `pdf2zh_next example.pdf --offline-assets /path`                                                                      | `-o`    |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--use-offline-assets`          | Use offline assets package from the specified directory                                  | `pdf2zh_next example.pdf --use-offline-assets /path`                                                                   |
| `--clear-offline-assets`        | Clear the offline assets package in the default directory                                | `pdf2zh_next example.pdf --clear-offline-assets`                                                                       |
| `--check-offline-assets`        | Check the offline assets package in the default directory                                | `pdf2zh_next example.pdf --check-offline-assets`                                                                       |
| `--download-offline-assets`     | Download offline assets package to the default directory                                 | `pdf2zh_next example.pdf --download-offline-assets`                                                                    |
| `--download-offline-assets-url` | Download offline assets package from the specified URL                                   | `pdf2zh_next example.pdf --download-offline-assets-url https://example.com/offline-assets.zip`                         |
| `--download-offline-assets-dir` | Download offline assets package to the specified directory                               | `pdf2zh_next example.pdf --download-offline-assets-dir /path`                                                          |
| `--offline-assets-dir`          | Set the directory to store the offline assets package (default: `~/.pdf2zh/offline-assets`) | `pdf2zh_next example.pdf --offline-assets-dir /path`                                                                   |
| `--offline-assets-url`          | Set the URL to download the offline assets package                                       | `pdf2zh_next example.pdf --offline-assets-url https://example.com/offline-assets.zip`                                  |
| `--offline-assets-force`        | Force download the offline assets package even if it exists                              | `pdf2zh_next example.pdf --offline-assets-force`                                                                       |
| `--offline-assets-skip-download`| Skip downloading the offline assets package                                              | `pdf2zh_next example.pdf --offline-assets-skip-download`                                                               |
| `--offline-assets-skip-extract` | Skip extracting the offline assets package                                               | `pdf2zh_next example.pdf --offline-assets-skip-extract`                                                                |
| `--offline-assets-skip-check`   | Skip checking the offline assets package                                                 | `pdf2zh_next example.pdf --offline-assets-skip-check`                                                                  |
| `--offline-assets-skip-clear`   | Skip clearing the offline assets package                                                 | `pdf2zh_next example.pdf --offline-assets-skip-clear`                                                                  |
| `--offline-assets-skip-restore` | Skip restoring the offline assets package                                                | `pdf2zh_next example.pdf --offline-assets-skip-restore`                                                                |
| `--offline-assets-skip-use`     | Skip using the offline assets package                                                    | `pdf2zh_next example.pdf --offline-assets-skip-use`                                                                    |

---

### TRANSLATION

| `--restore-offline-assets`      | Stellt das Offline-Assets-Paket aus dem angegebenen Verzeichnis wieder her                             | `pdf2zh_next example.pdf --restore-offline-assets /pfad`                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `--use-offline-assets`          | Verwendet das Offline-Assets-Paket aus dem angegebenen Verzeichnis                                     | `pdf2zh_next example.pdf --use-offline-assets /pfad`                                                                   |
| `--clear-offline-assets`        | Löscht das Offline-Assets-Paket im Standardverzeichnis                                                 | `pdf2zh_next example.pdf --clear-offline-assets`                                                                       |
| `--check-offline-assets`        | Überprüft das Offline-Assets-Paket im Standardverzeichnis                                              | `pdf2zh_next example.pdf --check-offline-assets`                                                                       |
| `--download-offline-assets`     | Lädt das Offline-Assets-Paket in das Standardverzeichnis herunter                                      | `pdf2zh_next example.pdf --download-offline-assets`                                                                    |
| `--download-offline-assets-url` | Lädt das Offline-Assets-Paket von der angegebenen URL herunter                                         | `pdf2zh_next example.pdf --download-offline-assets-url https://example.com/offline-assets.zip`                         |
| `--download-offline-assets-dir` | Lädt das Offline-Assets-Paket in das angegebene Verzeichnis herunter                                   | `pdf2zh_next example.pdf --download-offline-assets-dir /pfad`                                                          |
| `--offline-assets-dir`          | Legt das Verzeichnis fest, in dem das Offline-Assets-Paket gespeichert werden soll (Standard: `~/.pdf2zh/offline-assets`) | `pdf2zh_next example.pdf --offline-assets-dir /pfad`                                                                   |
| `--offline-assets-url`          | Legt die URL fest, von der das Offline-Assets-Paket heruntergeladen werden soll                        | `pdf2zh_next example.pdf --offline-assets-url https://example.com/offline-assets.zip`                                  |
| `--offline-assets-force`        | Erzwingt den Download des Offline-Assets-Pakets, auch wenn es bereits vorhanden ist                    | `pdf2zh_next example.pdf --offline-assets-force`                                                                       |
| `--offline-assets-skip-download`| Überspringt den Download des Offline-Assets-Pakets                                                     | `pdf2zh_next example.pdf --offline-assets-skip-download`                                                               |
| `--offline-assets-skip-extract` | Überspringt das Entpacken des Offline-Assets-Pakets                                                    | `pdf2zh_next example.pdf --offline-assets-skip-extract`                                                                |
| `--offline-assets-skip-check`   | Überspringt die Überprüfung des Offline-Assets-Pakets                                                  | `pdf2zh_next example.pdf --offline-assets-skip-check`                                                                  |
| `--offline-assets-skip-clear`   | Überspringt das Löschen des Offline-Assets-Pakets                                                      | `pdf2zh_next example.pdf --offline-assets-skip-clear`                                                                  |
| `--offline-assets-skip-restore` | Überspringt das Wiederherstellen des Offline-Assets-Pakets                                             | `pdf2zh_next example.pdf --offline-assets-skip-restore`                                                                |
| `--offline-assets-skip-use`     | Überspringt die Verwendung des Offline-Assets-Pakets                                                   | `pdf2zh_next example.pdf --offline-assets-skip-use`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Show help message then exit                                                             | `pdf2zh_next --help`                                                                                                  |
| `-v`, `--verbose`               | Show more information                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--log-level`                   | Set log level, default is `INFO`                                                        | `pdf2zh_next --log-level DEBUG`                                                                                       |
| `--log-file`                    | Set log file path, default is `pdf2zh_next.log`                                          | `pdf2zh_next --log-file /path/to/log/file.log`                                                                        |
| `--log-format`                  | Set log format, default is `%(asctime)s - %(name)s - %(levelname)s - %(message)s`       | `pdf2zh_next --log-format "%(asctime)s - %(name)s - %(levelname)s - %(message)s"`                                    |
| `--log-datefmt`                 | Set log date format, default is `%Y-%m-%d %H:%M:%S`                                      | `pdf2zh_next --log-datefmt "%Y-%m-%d %H:%M:%S"`                                                                       |
| `--log-backup-count`            | Set log backup count, default is `7`                                                     | `pdf2zh_next --log-backup-count 7`                                                                                    |
| `--log-max-bytes`               | Set log max bytes, default is `10485760` (10MB)                                          | `pdf2zh_next --log-max-bytes 10485760`                                                                                |
| `--log-encoding`                | Set log encoding, default is `utf-8`                                                    | `pdf2zh_next --log-encoding utf-8`                                                                                    |
| `--log-mode`                    | Set log mode, default is `a` (append)                                                   | `pdf2zh_next --log-mode a`                                                                                            |
| `--log-compress`                | Set log compress, default is `False`                                                    | `pdf2zh_next --log-compress False`                                                                                    |
| `--log-delay`                   | Set log delay, default is `False`                                                       | `pdf2zh_next --log-delay False`                                                                                       |
| `--log-utc`                     | Set log utc, default is `False`                                                         | `pdf2zh_next --log-utc False`                                                                                         |
| `--log-color`                   | Set log color, default is `False`                                                       | `pdf2zh_next --log-color False`                                                                                       |
| `--log-colors`                  | Set log colors, default is `None`                                                       | `pdf2zh_next --log-colors None`                                                                                       |
| `--log-style`                   | Set log style, default is `%`                                                           | `pdf2zh_next --log-style "%"`                                                                                         |
| `--log-traceback`               | Set log traceback, default is `True`                                                    | `pdf2zh_next --log-traceback True`                                                                                    |
| `--log-traceback-limit`         | Set log traceback limit, default is `100`                                                | `pdf2zh_next --log-traceback-limit 100`                                                                               |
| `--log-traceback-format`        | Set log traceback format, default is `None`                                              | `pdf2zh_next --log-traceback-format None`                                                                             |
| `--log-traceback-locals`        | Set log traceback locals, default is `False`                                             | `pdf2zh_next --log-traceback-locals False`                                                                            |
| `--log-traceback-max-frames`    | Set log traceback max frames, default is `100`                                           | `pdf2zh_next --log-traceback-max-frames 100`                                                                          |
| `--log-traceback-show-locals`   | Set log traceback show locals, default is `False`                                        | `pdf2zh_next --log-traceback-show-locals False`                                                                       |
| `--log-traceback-show-vars`     | Set log traceback show vars, default is `False`                                          | `pdf2zh_next --log-traceback-show-vars False`                                                                         |
| `--log-traceback-show-ids`      | Set log traceback show ids, default is `False`                                           | `pdf2zh_next --log-traceback-show-ids False`                                                                          |
| `--log-traceback-show-values`   | Set log traceback show values, default is `False`                                        | `pdf2zh_next --log-traceback-show-values False`                                                                       |
| `--log-traceback-show-types`    | Set log traceback show types, default is `False`                                         | `pdf2zh_next --log-traceback-show-types False`                                                                        |
| `--log-traceback-show-lengths`  | Set log traceback show lengths, default is `False`                                       | `pdf2zh_next --log-traceback-show-lengths False`                                                                      |
| `--log-traceback-show-filenames`| Set log traceback show filenames, default is `False`                                     | `pdf2zh_next --log-traceback-show-filenames False`                                                                    |
| `--log-traceback-show-linenos`  | Set log traceback show linenos, default is `False`                                       | `pdf2zh_next --log-traceback-show-linenos False`                                                                      |
| `--log-traceback-show-functions`| Set log traceback show functions, default is `False`                                     | `pdf2zh_next --log-traceback-show-functions False`                                                                    |
| `--log-traceback-show-modules`  | Set log traceback show modules, default is `False`                                       | `pdf2zh_next --log-traceback-show-modules False`                                                                      |
| `--log-traceback-show-paths`    | Set log traceback show paths, default is `False`                                         | `pdf2zh_next --log-traceback-show-paths False`                                                                        |
| `--log-traceback-show-urls`     | Set log traceback show urls, default is `False`                                          | `pdf2zh_next --log-traceback-show-urls False`                                                                         |
| `--log-traceback-show-args`     | Set log traceback show args, default is `False`                                          | `pdf2zh_next --log-traceback-show-args False`                                                                         |
| `--log-traceback-show-kwargs`   | Set log traceback show kwargs, default is `False`                                        | `pdf2zh_next --log-traceback-show-kwargs False`                                                                       |
| `--log-traceback-show-varnames` | Set log traceback show varnames, default is `False`                                      | `pdf2zh_next --log-traceback-show-varnames False`                                                                     |
| `--log-traceback-show-argnames` | Set log traceback show argnames, default is `False`                                      | `pdf2zh_next --log-traceback-show-argnames False`                                                                     |
| `--log-traceback-show-kwnames`  | Set log traceback show kwnames, default is `False`                                       | `pdf2zh_next --log-traceback-show-kwnames False`                                                                      |
| `--log-traceback-show-exc-info` | Set log traceback show exc info, default is `False`                                      | `pdf2zh_next --log-traceback-show-exc-info False`                                                                     |
| `--log-traceback-show-exc-cause`| Set log traceback show exc cause, default is `False`                                     | `pdf2zh_next --log-traceback-show-exc-cause False`                                                                    |
| `--log-traceback-show-exc-context`| Set log traceback show exc context, default is `False`                                   | `pdf2zh_next --log-traceback-show-exc-context False`                                                                  |
| `--log-traceback-show-exc-chain`| Set log traceback show exc chain, default is `False`                                     | `pdf2zh_next --log-traceback-show-exc-chain False`                                                                    |
| `--log-traceback-show-exc-full` | Set log traceback show exc full, default is `False`                                      | `pdf2zh_next --log-traceback-show-exc-full False`                                                                     |
| `--log-traceback-show-exc-limit`| Set log traceback show exc limit, default is `None`                                      | `pdf2zh_next --log-traceback-show-exc-limit None`                                                                     |
| `--log-traceback-show-exc-tb`   | Set log traceback show exc tb, default is `False`                                        | `pdf2zh_next --log-traceback-show-exc-tb False`                                                                       |
| `--log-traceback-show-exc-value`| Set log traceback show exc value, default is `False`                                     | `pdf2zh_next --log-traceback-show-exc-value False`                                                                    |
| `--log-traceback-show-exc-type` | Set log traceback show exc type, default is `False`                                      | `pdf2zh_next --log-traceback-show-exc-type False`                                                                     |
| `--log-traceback-show-exc-msg`  | Set log traceback show exc msg, default is `False`                                       | `pdf2zh_next --log 极 traceback-show-exc-msg False`                                                                     |

---

### OUTPUT

| `--version`                     | Version anzeigen und beenden                                                                 | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Hilfenachricht anzeigen und beenden                                                         | `pdf2zh_next --help`                                                                                                  |
| `-v`, `--verbose`               | Mehr Informationen anzeigen                                                                  | `pdf2zh_next -v`                                                                                                      |
| `--log-level`                   | Protokollierungsstufe festlegen, Standard ist `INFO`                                         | `pdf2zh_next --log-level DEBUG`                                                                                       |
| `--log-file`                    | Pfad der Protokolldatei festlegen, Standard ist `pdf2zh_next.log`                            | `pdf2zh_next --log-file /path/to/log/file.log`                                                                        |
| `--log-format`                  | Protokollformat festlegen, Standard ist `%(asctime)s - %(name)s - %(levelname)s - %(message)s` | `pdf2zh_next --log-format "%(asctime)s - %(name)s - %(levelname)s - %(message)s"`                                    |
| `--log-datefmt`                 | Datumsformat für Protokoll festlegen, Standard ist `%Y-%m-%d %H:%M:%S`                       | `pdf 极 zh_next --log-datefmt "%Y-%m-%d %H:%M:%S"`                                                                       |
| `--log-backup-count`            | Anzahl der Protokollsicherungen festlegen, Standard ist `7`                                  | `pdf2zh_next --log-back 极 up-count 7`                                                                                    |
| `--log-max-bytes`               | Maximale Größe der Protokolldatei festlegen, Standard ist `10485760` (10MB)                  | `pdf2zh_next --log-max-bytes 10485760`                                                                                |
| `--log-encoding`                | Kodierung der Protokolldatei festlegen, Standard ist `utf-8`                                 | `pdf2zh_next --log-encoding utf-8`                                                                                    |
| `--log-mode`                    | Modus der Protokolldatei festlegen, Standard ist `a` (Anhängen)                              | `pdf2zh_next --log-mode a`                                                                                            |
| `--log-compress`                | Komprimierung der Protokolldatei festlegen, Standard ist `False`                             | `pdf2zh_next --log-compress False`                                                                                    |
| `--极 log-delay`                   | Verzögerung der Protokollierung festlegen, Standard ist `False`                              | `pdf2zh_next --log-delay False`                                                                                       |
| `--log-utc`                     | UTC-Zeit für Protokollierung festlegen, Standard ist `False`                                | `pdf2zh_next --log-utc False`                                                                                         |
| `--log-color`                   | Farbige Protokollausgabe festlegen, Standard ist `False`                                     | `pdf2zh_next --log-color False`                                                                                       |
| `--log-colors`                  | Farben für Protokollausgabe festlegen, Standard ist `None`                                  | `pdf2zh_next --log-colors None`                                                                                       |
| `--log-style`                   | Stil der Protokollausgabe festlegen, Standard ist `%`                                       | `pdf2zh_next --log-style "%"`                                                                                         |
| `--log-traceback`               | Traceback-Protokollierung aktivieren, Standard ist `True`                                   | `pdf2zh_next --log-traceback True`                                                                                    |
| `--log-traceback-limit`         | Limit für Traceback-Protokollierung festlegen, Standard ist `100`                            | `pdf2zh_next --log-traceback-limit 100`                                                                               |
| `--log-traceback-format`        | Format für Traceback-Protokollierung festlegen, Standard ist `None`                          | `pdf2zh_next --log-traceback-format None`                                                                             |
| `--log-traceback-locals`        | Lokale Variablen in Traceback anzeigen, Standard ist `False`                                | `pdf2zh_next --log-traceback-locals False`                                                                            |
| `--log-traceback-max-frames`    | Maximale Anzahl von Frames im Traceback festlegen, Standard ist `极 100`                       | `pdf2zh_next --log-traceback-max-frames 100`                                                                          |
| `--log-traceback-show-locals`   | Lokale Variablen im Traceback anzeigen, Standard ist `False`                               | `pdf2zh_next --log-traceback-show-locals False`                                                                       |
| `--log-traceback-show-vars`     | Variablen im Traceback anzeigen, Standard ist `False`                                       | `pdf2zh_next --log-traceback-show-vars False`                                                                         |
| `--log-traceback-show-ids`      | IDs im Traceback anzeigen, Standard ist `False`                                             | `pdf2zh_next --log-traceback-show-ids False`                                                                          |
| `--log-traceback-show-values`   | Werte im Traceback anzeigen, Standard ist `False`                                           | `pdf2zh_next --log-traceback-show-values False`                                                                       |
| `--log-traceback-show-types`    | Typen im Traceback anzeigen, Standard ist `False`                                           | `pdf2zh_next --log-traceback-show-types False`                                                                        |
| `--log-traceback-show-lengths`  | Längen im Traceback anzeigen, Standard ist `False`                                         | `pdf2zh_next --log-traceback-show-lengths False`                                                                      |
| `--log-traceback-show-filenames`| Dateinamen im Traceback anzeigen, Standard ist `False`                                      | `pdf2zh_next --log-traceback-show-filenames False`                                                                    |
| `--log-traceback-show-linenos`  | Zeilennummern im Traceback anzeigen, Standard ist `False`                                  | `pdf2zh_next --log-traceback-show-linenos False`                                                                      |
| `--log-traceback-show-functions`| Funktionen im Traceback anzeigen, Standard ist `False`                                     | `pdf2zh_next --log-traceback-show-functions False`                                                                    |
| `--log-traceback-show-modules`  | Module im Traceback anzeigen, Standard ist `False`                                         | `pdf2zh_next --log-traceback-show-modules False`                                                                      |
| `--log-traceback-show-paths`    | Pfade im Traceback anzeigen, Standard ist `False`                                           | `pdf2zh_next --log-traceback-show-paths False`                                                                        |
| `--log-traceback-show-urls`     | URLs im Traceback anzeigen, Standard ist `False`                                           | `pdf2zh_next --log-traceback-show-urls False`                                                                         |
| `--log-traceback-show-args`     | Argumente im Traceback anzeigen, Standard ist `False`                                      | `pdf2zh_next --log-traceback-show-args False`                                                                         |
| `--log-traceback-show-kwargs`   | Keyword-Argumente im Traceback anzeigen, Standard ist `False`                               | `pdf2zh_next --log-traceback-show-kwargs False`                                                                       |
| `--log-traceback-show-varnames` | Variablennamen im Traceback anzeigen, Standard ist `False`                                  | `pdf2zh_next --log-traceback-show-varnames False`                                                                     |
| `--log-traceback-show-argnames` | Argumentnamen im Traceback anzeigen, Standard ist `False`                                  | `pdf2zh_next --log-traceback-show-argnames False`                                                                     |
| `--log-traceback-show-kwnames`  | Keyword-Argumentnamen im Traceback anzeigen, Standard ist `False`                          | `pdf2zh_next --log-traceback-show-kwnames False`                                                                      |
| `--log-traceback-show-exc-info` | Ausnahmeinformationen im Traceback anzeigen, Standard ist `False`                          | `pdf2zh_next --log-traceback-show-exc-info False`                                                                     |
| `--log-traceback-show-exc-cause`| Ausnahmeursache im Traceback anzeigen, Standard ist `False`                                | `pdf2zh_next --log-traceback-show-exc-cause False`                                                                    |
| `--log-traceback-show-exc-context`| Ausnahmekontext im Traceback anzeigen, Standard ist `False`                               | `pdf2zh_next --log-traceback-show-exc-context False`                                                                  |
| `--log-traceback-show-exc-chain`| Ausnahmekette im Traceback anzeigen, Standard ist `False`                                  | `pdf2zh_next --log-traceback-show-exc-chain False`                                                                    |
| `--log-traceback-show-exc-full` | Vollständige Ausnahme im Traceback anzeigen, Standard ist `False`                           | `pdf2zh_next --log-traceback-show-exc-full False`                                                                     |
| `--log-traceback-show 极-exc-limit`| Limit für Ausnahmeanzeige im Traceback festlegen, Standard ist `None`                     | `pdf2zh_next --log-traceback-show-exc-limit None`                                                                     |
| `--log-traceback-show-exc-tb`   | Traceback der Ausnahme anzeigen, Standard ist `False`                                      | `pdf2zh_next --log-traceback-show-exc-tb False`                                                                       |
| `--log-traceback-show-exc-value`| Ausnahmewert im Traceback anzeigen, Standard ist `False`                                   | `pdf2zh_next --log-traceback-show-exc-value False`                                                                    |
| `--log-traceback-show-exc-type` | Ausnahmetyp im Traceback anzeigen, Standard ist `False`                                    | `pdf2zh_next --log-traceback-show-exc-type False`                                                                     |
| `--log-traceback-show-exc-msg`  | Ausnahmemeldung im Traceback anzeigen, Standard ist `False`                                | `pdf2zh_next --log-traceback-show-exc-msg False`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--target-lang`                 | Specify target language                                                                 | `pdf2zh_next example.pdf --target-lang de`                                                                             |
| `--source-lang`                 | Specify source language (if you know it)                                                | `pdf2zh_next example.pdf --source-lang en`                                                                             |
| `--engine`                      | Specify the translation engine to use                                                   | `pdf2zh_next example.pdf --engine google`                                                                              |
| `--proxy`                       | Set proxy for translation engine                                                         | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--output`                      | Specify output file name                                                                | `pdf2zh_next example.pdf --output example_translated.pdf`                                                              |
| `--no-ocr`                      | Disable OCR for the document                                                            | `pdf2zh_next example.pdf --no-ocr`                                                                                     |
| `--ocr-only`                    | Only perform OCR on the document                                                        | `pdf2zh_next example.pdf --ocr-only`                                                                                   |
| `--ocr-language`                | Specify OCR language                                                                    | `pdf2zh_next example.pdf --ocr-language en`                                                                            |
| `--ocr-timeout`                 | Set timeout for OCR                                                                     | `pdf2zh_next example.pdf --ocr-timeout 30`                                                                             |
| `--ocr-ignore-existing-text`    | Ignore existing text in the document during OCR                                         | `pdf2zh_next example.pdf --ocr-ignore-existing-text`                                                                   |
| `--ocr-max-workers`             | Set the maximum number of workers for OCR                                               | `pdf2zh_next example.pdf --ocr-max-workers 4`                                                                          |
| `--ocr-retry`                   | Set the number of retries for OCR                                                       | `pdf2zh_next example.pdf --ocr-retry 3`                                                                                |
| `--ocr-max-task-count`          | Set the maximum number of tasks for OCR                                                 | `pdf2zh_next example.pdf --ocr-max-task-count 10`                                                                      |
| `--ocr-options`                 | Specify additional options for OCR                                                      | `pdf2zh_next example.pdf --ocr-options '{"tesseract": {"dpi": 300}}'`                                                  |
| `--translation-timeout`         | Set timeout for translation                                                             | `pdf2zh_next example.pdf --translation-timeout 30`                                                                     |
| `--translation-max-workers`     | Set the maximum number of workers for translation                                       | `pdf2zh_next example.pdf --translation-max-workers 4`                                                                  |
| `--translation-retry`           | Set the number of retries for translation                                               | `pdf2zh_next example.pdf --translation-retry 3`                                                                        |
| `--translation-max-task-count`  | Set the maximum number of tasks for translation                                         | `pdf2zh_next example.pdf --translation-max-task-count 10`                                                              |
| `--translation-options`         | Specify additional options for translation                                              | `pdf2zh_next example.pdf --translation-options '{"google": {"formality": "more"}}'`                                    |
| `--font`                        | Specify font for the translated document                                                | `pdf2zh_next example.pdf --font "Noto Sans SC"`                                                                        |
| `--font-size`                   | Specify font size for the translated document                                           | `pdf2zh_next example.pdf --font-size 12`                                                                               |
| `--line-spacing`                | Specify line spacing for the translated document                                        | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                           |
| `--char-spacing`                | Specify character spacing for the translated document                                   | `pdf2zh_next example.pdf --char-spacing 0.1`                                                                           |
| `--margin`                      | Specify margin for the translated document                                              | `pdf2zh_next example.pdf --margin 50`                                                                                  |
| `--no-backup`                   | Disable backup of the original document                                                 | `pdf2zh_next example.pdf --no-backup`                                                                                  |
| `--debug`                       | Enable debug mode                                                                       | `pdf2zh_next example.pdf --debug`                                                                                      |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                    |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Show help information                                                                   | `pdf2zh_next --help`                                                                                                   |

---

### TRANSLATION RESULT

| `--pages`                       | Teilweise Übersetzung des Dokuments                                                    | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--target-lang`                 | Zielsprache angeben                                                                     | `pdf2zh_next example.pdf --target-lang de`                                                                             |
| `--source-lang`                 | Quellsprache angeben (falls bekannt)                                                    | `pdf2zh_next example.pdf --source-lang en`                                                                             |
| `--engine`                      | Zu verwendende Übersetzungs-Engine angeben                                              | `pdf2zh_next example.pdf --engine google`                                                                              |
| `--proxy`                       | Proxy für die Übersetzungs-Engine setzen                                                | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--output`                      | Ausgabedateinamen angeben                                                               | `pdf2zh_next example.pdf --output example_translated.pdf`                                                              |
| `--no-ocr`                      | OCR für das Dokument deaktivieren                                                       | `pdf2zh_next example.pdf --no-ocr`                                                                                     |
| `--ocr-only`                    | Nur OCR für das Dokument durchführen                                                    | `pdf2zh_next example.pdf --ocr-only`                                                                                   |
| `--ocr-language`                | OCR-Sprache angeben                                                                     | `pdf2zh_next example.pdf --ocr-language en`                                                                            |
| `--ocr-timeout`                 | Timeout für OCR setzen                                                                  | `pdf2zh_next example.pdf --ocr-timeout 30`                                                                             |
| `--ocr-ignore-existing-text`    | Vorhandenen Text im Dokument während der OCR ignorieren                                 | `pdf2zh_next example.pdf --ocr-ignore-existing-text`                                                                   |
| `--ocr-max-workers`             | Maximale Anzahl von Workern für OCR setzen                                              | `pdf2zh_next example.pdf --ocr-max-workers 4`                                                                          |
| `--ocr-retry`                   | Anzahl der Wiederholungen für OCR setzen                                                | `pdf2zh_next example.pdf --ocr-retry 3`                                                                                |
| `--ocr-max-task-count`          | Maximale Anzahl von Aufgaben für OCR setzen                                             | `pdf2zh_next example.pdf --ocr-max-task-count 10`                                                                      |
| `--ocr-options`                 | Zusätzliche Optionen für OCR angeben                                                    | `pdf2zh_next example.pdf --ocr-options '{"tesseract": {"dpi": 300}}'`                                                  |
| `--translation-timeout`         | Timeout für Übersetzung setzen                                                          | `pdf2zh_next example.pdf --translation-timeout 30`                                                                     |
| `--translation-max-workers`     | Maximale Anzahl von Workern für Übersetzung setzen                                      | `pdf2zh_next example.pdf --translation-max-workers 4`                                                                  |
| `--translation-retry`           | Anzahl der Wiederholungen für Übersetzung setzen                                        | `pdf2zh_next example.pdf --translation-retry 3`                                                                        |
| `--translation-max-task-count`  | Maximale Anzahl von Aufgaben für Übersetzung setzen                                     | `pdf2zh_next example.pdf --translation-max-task-count 10`                                                              |
| `--translation-options`         | Zusätzliche Optionen für Übersetzung angeben                                            | `pdf2zh_next example.pdf --translation-options '{"google": {"formality": "more"}}'`                                    |
| `--font`                        | Schriftart für das übersetzte Dokument angeben                                          | `pdf2zh_next example.pdf --font "Noto Sans SC"`                                                                        |
| `--font-size`                   | Schriftgröße für das übersetzte Dokument angeben                                        | `pdf2zh_next example.pdf --font-size 12`                                                                               |
| `--line-spacing`                | Zeilenabstand für das übersetzte Dokument angeben                                       | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                           |
| `--char-spacing`                | Zeichenabstand für das übersetzte Dokument angeben                                      | `pdf2zh_next example.pdf --char-spacing 0.1`                                                                           |
| `--margin`                      | Rand für das übersetzte Dokument angeben                                                | `pdf2zh_next example.pdf --margin 50`                                                                                  |
| `--no-backup`                   | Sicherung des Originaldokuments deaktivieren                                            | `pdf2zh_next example.pdf --no-backup`                                                                                  |
| `--debug`                       | Debug-Modus aktivieren                                                                  | `pdf2zh_next example.pdf --debug`                                                                                      |
| `--verbose`                     | Ausführliche Ausgabe aktivieren                                                         | `pdf2zh_next example.pdf --verbose`                                                                                    |
| `--version`                     | Versionsinformationen anzeigen                                                          | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Hilfeinformationen anzeigen                                                             | `pdf2zh_next --help`                                                                                                   |
`auto`        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               | `zh`          |
| `--translator`                  | Translation service, see [Documentation of Translation Services](./TRANSLATORS.md)      | `pdf2zh_next example.pdf --translator google`                                                                         | `google`      |
| `--translator-key`              | The API key for the translation service, if required                                    | `pdf2zh_next example.pdf --translator deepl --translator-key YOUR_DEEPL_API_KEY`                                      |               |
| `--translator-url`              | The custom endpoint for the translation service, if required                            | `pdf2zh_next example.pdf --translator azure --translator-url YOUR_AZURE_ENDPOINT`                                     |               |
| `--translator-region`           | The region for the translation service, if required                                     | `pdf2zh_next example.pdf --translator azure --translator-region YOUR_AZURE_REGION`                                    |               |
| `--translator-model`            | The model for the translation service, if required                                      | `pdf2zh_next example.pdf --translator openai --translator-model gpt-4o`                                               |               |
| `--translator-extra-params`     | Extra parameters for the translation service, if required                               | `pdf2zh_next example.pdf --translator openai --translator-extra-params '{"temperature": 0.1}'`                        |               |
| `--translator-timeout`          | Timeout for the translation service, in seconds                                         | `pdf2zh_next example.pdf --translator google --translator-timeout 30`                                                 | `10`          |
| `--translator-max-retries`      | Maximum retries for the translation service                                             | `pdf2zh_next example.pdf --translator google --translator-max-retries 3`                                              | `3`           |
| `--translator-retry-delay`      | Delay between retries for the translation service, in seconds                           | `pdf2zh_next example.pdf --translator google --translator-retry-delay 1`                                              | `1`           |
| `--translator-concurrent-limit` | Maximum number of concurrent requests to the translation service                        | `pdf2zh_next example.pdf --translator google --translator-concurrent-limit 10`                                        | `5`           |
| `--translator-request-interval` | Minimum interval between requests to the translation service, in seconds                | `pdf2zh_next example.pdf --translator google --translator-request-interval 0.1`                                       | `0.1`         |
| `--translator-batch-size`       | Batch size for the translation service                                                  | `pdf2zh_next example.pdf --translator google --translator-batch-size 10`                                              | `50`          |
| `--translator-batch-delay`      | Delay between batches for the translation service, in seconds                           | `pdf2zh_next example.pdf --translator google --translator-batch-delay 1`                                              | `1`           |

---

### OUTPUT

| `--lang-in`                     | Quellsprachencode                                                                       | `pdf2zh_next example.pdf --lang-in en`                                                                                | `auto`        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------- |
| `--lang-out`                    | Zielsprachencode                                                                        | `pdf2zh_next example.pdf --lang-out zh`                                                                               | `zh`          |
| `--translator`                  | Übersetzungsdienst, siehe [Dokumentation der Übersetzungsdienste](./TRANSLATORS.md)     | `pdf2zh_next example.pdf --translator google`                                                                         | `google`      |
| `--translator-key`              | Der API-Schlüssel für den Übersetzungsdienst, falls erforderlich                        | `pdf2zh_next example.pdf --translator deepl --translator-key YOUR_DEEPL_API_KEY`                                      |               |
| `--translator-url`              | Der benutzerdefinierte Endpunkt für den Übersetzungsdienst, falls erforderlich          | `pdf2zh_next example.pdf --translator azure --translator-url YOUR_AZURE_ENDPOINT`                                     |               |
| `--translator-region`           | Die Region für den Übersetzungsdienst, falls erforderlich                               | `pdf2zh_next example.pdf --translator azure --translator-region YOUR_AZURE_REGION`                                    |               |
| `--translator-model`            | Das Modell für den Übersetzungsdienst, falls erforderlich                               | `pdf2zh_next example.pdf --translator openai --translator-model gpt-4o`                                               |               |
| `--translator-extra-params`     | Zusätzliche Parameter für den Übersetzungsdienst, falls erforderlich                    | `pdf2zh_next example.pdf --translator openai --translator-extra-params '{"temperature": 0.1}'`                        |               |
| `--translator-timeout`          | Timeout für den Übersetzungsdienst, in Sekunden                                         | `pdf2zh_next example.pdf --translator google --translator-timeout 30`                                                 | `10`          |
| `--translator-max-retries`      | Maximale Wiederholungsversuche für den Übersetzungsdienst                               | `pdf2zh_next example.pdf --translator google --translator-max-retries 3`                                              | `3`           |
| `--translator-retry-delay`      | Verzögerung zwischen Wiederholungsversuchen für den Übersetzungsdienst, in Sekunden     | `pdf2zh_next example.pdf --translator google --translator-retry-delay 1`                                              | `1`           |
| `--translator-concurrent-limit` | Maximale Anzahl gleichzeitiger Anfragen an den Übersetzungsdienst                       | `pdf2zh_next example.pdf --translator google --translator-concurrent-limit 10`                                        | `5`           |
| `--translator-request-interval` | Mindestintervall zwischen Anfragen an den Übersetzungsdienst, in Sekunden               | `pdf2zh_next example.pdf --translator google --translator-request-interval 0.1`                                       | `0.1`         |
| `--translator-batch-size`       | Batch-Größe für den Übersetzungsdienst                                                  | `pdf2zh_next example.pdf --translator google --translator-batch-size 10`                                              | `50`          |
| `--translator-batch-delay`      | Verzögerung zwischen Batches für den Übersetzungsdienst, in Sekunden                    | `pdf2zh_next example.pdf --translator google --translator-batch-delay 1`                                              | `1`           |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--model`                       | Model to use for translation, see [Supported Models](#supported-models)                 | `pdf2zh_next example.pdf --model gpt-4o`                                                                             |
| `--service`                     | Translation service to use, see [Translation Services](#translation-services)            | `pdf2zh_next example.pdf --service azure`                                                                            |
| `--api-key`                     | API key for the translation service                                                     | `pdf2zh_next example.pdf --service azure --api-key your_api_key_here`                                                |
| `--endpoint`                    | Endpoint for the translation service (if applicable)                                    | `pdf2zh_next example.pdf --service azure --endpoint https://your-custom-endpoint.cognitiveservices.azure.com/`       |
| `--region`                      | Region for the translation service (if applicable)                                       | `pdf2zh_next example.pdf --service azure --region eastus`                                                             |
| `--proxy`                       | Proxy server to use for requests                                                         | `pdf2zh_next example.pdf --proxy http://your-proxy-server:port`                                                       |
| `--concurrency`                 | Number of concurrent requests to the translation service                                 | `pdf2zh_next example.pdf --concurrency 5`                                                                            |
| `--timeout`                     | Timeout in seconds for each translation request                                          | `pdf2zh_next example.pdf --timeout 30`                                                                               |
| `--max-retries`                 | Maximum number of retries for failed requests                                           | `pdf2zh_next example.pdf --max-retries 3`                                                                            |
| `--retry-delay`                 | Delay in seconds between retries                                                        | `pdf2zh_next example.pdf --retry-delay 1`                                                                            |
| `--ignore-size-limit`          | Ignore size limit warnings and proceed with translation                                 | `pdf2zh_next example.pdf --ignore-size-limit`                                                                         |
| `--output`                      | Output file path                                                                         | `pdf2zh_next example.pdf --output ./translated_example.pdf`                                                           |
| `--log-level`                   | Log level (debug, info, warning, error)                                                | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION

| `--lang-out`                    | Zielsprachencode                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| :------------------------------ | :---------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--model`                       | Zu verwendendes Modell für die Übersetzung, siehe [Unterstützte Modelle](#unterstützte-modelle)                 | `pdf2zh_next example.pdf --model gpt-4o`                                                                             |
| `--service`                     | Zu verwendender Übersetzungsdienst, siehe [Übersetzungsdienste](#übersetzungsdienste)            | `pdf2zh_next example.pdf --service azure`                                                                            |
| `--api-key`                     | API-Schlüssel für den Übersetzungsdienst                                                     | `pdf2zh_next example.pdf --service azure --api-key your_api_key_here`                                                |
| `--endpoint`                    | Endpunkt für den Übersetzungsdienst (falls zutreffend)                                    | `pdf2zh_next example.pdf --service azure --endpoint https://your-custom-endpoint.cognitiveservices.azure.com/`       |
| `--region`                      | Region für den Übersetzungsdienst (falls zutreffend)                                       | `pdf2zh_next example.pdf --service azure --region eastus`                                                             |
| `--proxy`                       | Proxy-Server für Anfragen                                                         | `pdf2zh_next example.pdf --proxy http://your-proxy-server:port`                                                       |
| `--concurrency`                 | Anzahl der gleichzeitigen Anfragen an den Übersetzungsdienst                                 | `pdf2zh_next example.pdf --concurrency 5`                                                                            |
| `--timeout`                     | Timeout in Sekunden für jede Übersetzungsanfrage                                          | `pdf2zh_next example.pdf --timeout 30`                                                                               |
| `--max-retries`                 | Maximale Anzahl der Wiederholungsversuche für fehlgeschlagene Anfragen                                           | `pdf2zh_next example.pdf --max-retries 3`                                                                            |
| `--retry-delay`                 | Verzögerung in Sekunden zwischen Wiederholungsversuchen                                                        | `pdf2zh_next example.pdf --retry-delay 1`                                                                            |
| `--ignore-size-limit`          | Größenbeschränkungswarnungen ignorieren und mit der Übersetzung fortfahren                                 | `pdf2zh_next example.pdf --ignore-size-limit`                                                                         |
| `--output`                      | Ausgabedateipfad                                                                         | `pdf2zh_next example.pdf --output ./translated_example.pdf`                                                           |
| `--log-level`                   | Protokollierungsstufe (debug, info, warning, error)                                                | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--help`                        | Hilfenachricht anzeigen und beenden                                                              | `pdf2zh_next --help`                                                                                                  |
`5`                |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `--max-text-length`             | Maximum text length to translate                                                        | `pdf2zh_next example.pdf --max-text-length 1000`                                                                      | `1000`             |
| `--min-char-limit`              | Minimum number of characters to translate a text block                                 | `pdf2zh_next example.pdf --min-char-limit 5`                                                                          | `5`                |
| `--max-char-limit`              | Maximum number of characters to translate a text block                                 | `pdf2zh_next example.pdf --max-char-limit 1000`                                                                       | `1000`             |
| `--char-limit-hard`             | Hard limit on the number of characters to translate a text block                       | `pdf2zh_next example.pdf --char-limit-hard 1000`                                                                      | `1000`             |
| `--char-limit-soft`             | Soft limit on the number of characters to translate a text block                       | `pdf2zh_next example.pdf --char-limit-soft 1000`                                                                      | `1000`             |

---

### TRANSLATION RESULT

| `--min-text-length`             | Minimale Textlänge für die Übersetzung                                                | `pdf2zh_next example.pdf --min-text-length 5`                                                                         | `5`                |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `--max-text-length`             | Maximale Textlänge für die Übersetzung                                                | `pdf2zh_next example.pdf --max-text-length 1000`                                                                      | `1000`             |
| `--min-char-limit`              | Minimale Anzahl von Zeichen, um einen Textblock zu übersetzen                          | `pdf2zh_next example.pdf --min-char-limit 5`                                                                          | `5`                |
| `--max-char-limit`              | Maximale Anzahl von Zeichen, um einen Textblock zu übersetzen                          | `pdf2zh_next example.pdf --max-char-limit 1000`                                                                       | `1000`             |
| `--char-limit-hard`             | Harte Grenze für die Anzahl von Zeichen, um einen Textblock zu übersetzen              | `pdf2zh_next example.pdf --char-limit-hard 1000`                                                                      | `1000`             |
| `--char-limit-soft`             | Weiche Grenze für die Anzahl von Zeichen, um einen Textblock zu übersetzen             | `pdf2zh_next example.pdf --char-limit-soft 1000`                                                                      | `1000`             |
`http://127.0.0.1:8000`                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8001`                                                               | `http://127.0.0.1:8001`                                   |
| `--rpc-translate`                | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8002`                                                         | `http://127.0.0.1:8002`                                   |
| `--rpc-math`                    | RPC service host address for math formula recognition                                   | `pdf2zh_next example.pdf --rpc-math http://127.0.0.1:8003`                                                              | `http://127.0.0.1:8003`                                   |
| `--rpc-table`                   | RPC service host address for table recognition                                          | `pdf2zh_next example.pdf --rpc-table http://127.0.0.1:8004`                                                             | `http://127.0.0.1:8004`                                   |

---

### TRANSLATION RESULT

| `--rpc-doclayout`               | RPC-Dienst-Hostadresse für Dokumentlayoutanalyse                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       | `http://127.0.0.1:8000`                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| `--rpc-ocr`                     | RPC-Dienst-Hostadresse für OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8001`                                                               | `http://127.0.0.1:8001`                                   |
| `--rpc-translate`                | RPC-Dienst-Hostadresse für Übersetzung                                                | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8002`                                                         | `http://127.0.0.1:8002`                                   |
| `--rpc-math`                    | RPC-Dienst-Hostadresse für mathematische Formelerkennung                                   | `pdf2zh_next example.pdf --rpc-math http://127.0.0.1:8003`                                                              | `http://127.0.0.1:8003`                                   |
| `--rpc-table`                   | RPC-Dienst-Hostadresse für Tabellenerkennung                                          | `pdf2zh_next example.pdf --rpc-table http://127.0.0.1:8004`                                                             | `http://127.0.0.1:8004`                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--timeout`                     | Timeout for translation service                                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--proxy`                       | Proxy for translation service, e.g. `http://127.0.0.1:7890` or `socks5://127.0.0.1:7890` | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--service`                     | Translation service to use, default: `google`                                           | `pdf2zh_next example.pdf --service deepl`                                                                             |
| `--source`                      | Source language, default: `auto`                                                        | `pdf2zh_next example.pdf --source en`                                                                                 |
| `--target`                      | Target language, default: `zh`                                                          | `pdf2zh_next example.pdf --target en`                                                                                 |
| `--formula-strategy`            | Strategy for handling formulas, default: `html`                                         | `pdf2zh_next example.pdf --formula-strategy hybrid`                                                                   |
| `--formula-render-mode`         | Render mode for formulas, default: `svg`                                                | `pdf2zh_next example.pdf --formula-render-mode mathml`                                                                |
| `--ignore-translated-files`     | Ignore files that have already been translated                                          | `pdf2zh_next example.pdf --ignore-translated-files`                                                                   |
| `--only-translate-keywords`     | Only translate keywords, not the entire document                                        | `pdf2zh_next example.pdf --only-translate-keywords`                                                                   |
| `--no-translate-figure-caption` | Do not translate figure captions                                                        | `pdf2zh_next example.pdf --no-translate-figure-caption`                                                               |
| `--no-translate-table-caption`  | Do not translate table captions                                                         | `pdf2zh_next example.pdf --no-translate-table-caption`                                                                |
| `--no-translate-references`     | Do not translate references                                                             | `pdf2zh_next example.pdf --no-translate-references`                                                                   |
| `--no-translate-appendix`       | Do not translate appendix                                                               | `pdf2zh_next example.pdf --no-translate-appendix`                                                                     |
| `--no-translate-abstract`       | Do not translate abstract                                                               | `pdf2zh_next example.pdf --no-translate-abstract`                                                                     |
| `--no-translate-code-block`     | Do not translate code blocks                                                            | `pdf2zh_next example.pdf --no-translate-code-block`                                                                   |
| `--no-translate-keywords`       | Do not translate keywords                                                               | `pdf2zh_next example.pdf --no-translate-keywords`                                                                     |
| `--translate-figure-caption`    | Translate figure captions (default: true)                                               | `pdf2zh_next example.pdf --translate-figure-caption false`                                                            |
| `--translate-table-caption`     | Translate table captions (default: true)                                                | `pdf2zh_next example.pdf --translate-table-caption false`                                                             |
| `--translate-references`        | Translate references (default: true)                                                    | `pdf2zh_next example.pdf --translate-references false`                                                                |
| `--translate-appendix`          | Translate appendix (default: true)                                                      | `pdf2zh_next example.pdf --translate-appendix false`                                                                  |
| `--translate-abstract`          | Translate abstract (default: true)                                                      | `pdf2zh_next example.pdf --translate-abstract false`                                                                  |
| `--translate-code-block`        | Translate code blocks (default: false)                                                  | `pdf2zh_next example.pdf --translate-code-block true`                                                                 |
| `--translate-keywords`          | Translate keywords (default: true)                                                      | `pdf2zh_next example.pdf --translate-keywords false`                                                                  |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir`                   | Cache directory, default: `~/.cache/pdf2zh_next`                                        | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `--config`                      | Path to config file                                                                     | `pdf2zh_next example.pdf --config /path/to/config.json`                                                               |
| `--help`                        | Show help                                                                               | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Show version                                                                            | `pdf2zh_next --version`                                                                                               |

---

### TRANSLATED TEXT

| `--qps`                         | QPS-Limit für Übersetzungsdienst                                                       | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--timeout`                     | Timeout für Übersetzungsdienst                                                         | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--proxy`                       | Proxy für Übersetzungsdienst, z.B. `http://127.0.0.1:7890` oder `socks5://127.0.0.1:7890` | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--service`                     | Zu verwendender Übersetzungsdienst, Standard: `google`                                 | `pdf2zh_next example.pdf --service deepl`                                                                             |
| `--source`                      | Ausgangssprache, Standard: `auto`                                                      | `pdf2zh_next example.pdf --source en`                                                                                 |
| `--target`                      | Zielsprache, Standard: `zh`                                                            | `pdf2zh_next example.pdf --target en`                                                                                 |
| `--formula-strategy`            | Strategie für die Behandlung von Formeln, Standard: `html`                             | `pdf2zh_next example.pdf --formula-strategy hybrid`                                                                   |
| `--formula-render-mode`         | Render-Modus für Formeln, Standard: `svg`                                              | `pdf2zh_next example.pdf --formula-render-mode mathml`                                                                |
| `--ignore-translated-files`     | Bereits übersetzte Dateien ignorieren                                                  | `pdf2zh_next example.pdf --ignore-translated-files`                                                                   |
| `--only-translate-keywords`     | Nur Schlüsselwörter übersetzen, nicht das gesamte Dokument                             | `pdf2zh_next example.pdf --only-translate-keywords`                                                                   |
| `--no-translate-figure-caption` | Bildunterschriften nicht übersetzen                                                    | `pdf2zh_next example.pdf --no-translate-figure-caption`                                                               |
| `--no-translate-table-caption`  | Tabellenunterschriften nicht übersetzen                                                | `pdf2zh_next example.pdf --no-translate-table-caption`                                                                |
| `--no-translate-references`     | Referenzen nicht übersetzen                                                            | `pdf2zh_next example.pdf --no-translate-references`                                                                   |
| `--no-translate-appendix`       | Anhang nicht übersetzen                                                                | `pdf2zh_next example.pdf --no-translate-appendix`                                                                     |
| `--no-translate-abstract`       | Zusammenfassung nicht übersetzen                                                       | `pdf2zh_next example.pdf --no-translate-abstract`                                                                     |
| `--no-translate-code-block`     | Code-Blöcke nicht übersetzen                                                           | `pdf2zh_next example.pdf --no-translate-code-block`                                                                   |
| `--no-translate-keywords`       | Schlüsselwörter nicht übersetzen                                                       | `pdf2zh_next example.pdf --no-translate-keywords`                                                                     |
| `--translate-figure-caption`    | Bildunterschriften übersetzen (Standard: true)                                         | `pdf2zh_next example.pdf --translate-figure-caption false`                                                            |
| `--translate-table-caption`     | Tabellenunterschriften übersetzen (Standard: true)                                      | `pdf2zh_next example.pdf --translate-table-caption false`                                                             |
| `--translate-references`        | Referenzen übersetzen (Standard: true)                                                 | `pdf2zh_next example.pdf --translate-references false`                                                                |
| `--translate-appendix`          | Anhang übersetzen (Standard: true)                                                     | `pdf2zh_next example.pdf --translate-appendix false`                                                                  |
| `--translate-abstract`          | Zusammenfassung übersetzen (Standard: true)                                            | `pdf2zh_next example.pdf --translate-abstract false`                                                                  |
| `--translate-code-block`        | Code-Blöcke übersetzen (Standard: false)                                               | `pdf2zh_next example.pdf --translate-code-block true`                                                                 |
| `--translate-keywords`          | Schlüsselwörter übersetzen (Standard: true)                                            | `pdf2zh_next example.pdf --translate-keywords false`                                                                  |
| `--no-cache`                    | Cache deaktivieren                                                                     | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir`                   | Cache-Verzeichnis, Standard: `~/.cache/pdf2zh_next`                                    | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `--config`                      | Pfad zur Konfigurationsdatei                                                           | `pdf2zh_next example.pdf --config /path/to/config.json`                                                               |
| `--help`                        | Hilfe anzeigen                                                                         | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Version anzeigen                                                                       | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--ignore-html-cache`           | Ignore HTML cache                                                                       | `pdf2zh_next example.pdf --ignore-html-cache`                                                                          |
| `--ignore-translation-cache`    | Ignore translation cache (same as `--ignore-cache`)                                     | `pdf2zh_next example.pdf --ignore-translation-cache`                                                                   |
| `--ignore-all-cache`            | Ignore all cache (same as `--ignore-cache --ignore-html-cache`)                         | `pdf2zh_next example.pdf --ignore-all-cache`                                                                           |
| `--ignore-image`                | Ignore image translation                                                                | `pdf2zh_next example.pdf --ignore-image`                                                                               |
| `--ignore-text`                 | Ignore text translation                                                                 | `pdf2zh_next example.pdf --ignore-text`                                                                                |
| `--ignore-table`                | Ignore table translation                                                                | `pdf2zh_next example.pdf --ignore-table`                                                                               |
| `--ignore-equation`             | Ignore equation translation                                                             | `pdf2zh_next example.pdf --ignore-equation`                                                                            |
| `--ignore-list`                 | Ignore list translation                                                                 | `pdf2zh_next example.pdf --ignore-list`                                                                                |
| `--ignore-figure`               | Ignore figure translation                                                               | `pdf2zh_next example.pdf --ignore-figure`                                                                              |
| `--ignore-footnote`             | Ignore footnote translation                                                             | `pdf2zh_next example.pdf --ignore-footnote`                                                                            |
| `--ignore-bib`                  | Ignore bibliography translation                                                         | `pdf2zh_next example.pdf --ignore-bib`                                                                                 |
| `--ignore-code`                 | Ignore code block translation                                                           | `pdf2zh_next example.pdf --ignore-code`                                                                                |
| `--ignore-quote`                | Ignore quote translation                                                                | `pdf2zh_next example.pdf --ignore-quote`                                                                               |
| `--ignore-all`                  | Ignore all content translation (same as `--ignore-image --ignore-text --ignore-table ...`) | `pdf2zh_next example.pdf --ignore-all`                                                                                 |

---

### TRANSLATION

| `--ignore-cache`                | Übersetzungscache ignorieren                                                                 | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--ignore-html-cache`           | HTML-Cache ignorieren                                                                        | `pdf2zh_next example.pdf --ignore-html-cache`                                                                          |
| `--ignore-translation-cache`    | Übersetzungscache ignorieren (gleich wie `--ignore-cache`)                                   | `pdf2zh_next example.pdf --ignore-translation-cache`                                                                   |
| `--ignore-all-cache`            | Alle Caches ignorieren (gleich wie `--ignore-cache --ignore-html-cache`)                     | `pdf2zh_next example.pdf --ignore-all-cache`                                                                           |
| `--ignore-image`                | Bildübersetzung ignorieren                                                                   | `pdf2zh_next example.pdf --ignore-image`                                                                               |
| `--ignore-text`                 | Textübersetzung ignorieren                                                                   | `pdf2zh_next example.pdf --ignore-text`                                                                                |
| `--ignore-table`                | Tabellenübersetzung ignorieren                                                               | `pdf2zh_next example.pdf --ignore-table`                                                                               |
| `--ignore-equation`             | Gleichungsübersetzung ignorieren                                                             | `pdf2zh_next example.pdf --ignore-equation`                                                                            |
| `--ignore-list`                 | Listenübersetzung ignorieren                                                                 | `pdf2zh_next example.pdf --ignore-list`                                                                                |
| `--ignore-figure`               | Abbildungsübersetzung ignorieren                                                             | `pdf2zh_next example.pdf --ignore-figure`                                                                              |
| `--ignore-footnote`             | Fußnotenübersetzung ignorieren                                                               | `pdf2zh_next example.pdf --ignore-footnote`                                                                            |
| `--ignore-bib`                  | Literaturverzeichnisübersetzung ignorieren                                                   | `pdf2zh_next example.pdf --ignore-bib`                                                                                 |
| `--ignore-code`                 | Codeblockübersetzung ignorieren                                                              | `pdf2zh_next example.pdf --ignore-code`                                                                                |
| `--ignore-quote`                | Zitatübersetzung ignorieren                                                                  | `pdf2zh_next example.pdf --ignore-quote`                                                                               |
| `--ignore-all`                  | Alle Inhaltsübersetzungen ignorieren (gleich wie `--ignore-image --ignore-text --ignore-table ...`) | `pdf2zh_next example.pdf --ignore-all`                                                                                 |
---

### OUTPUT

| `--custom-system-prompt`        | Benutzerdefinierte Systemaufforderung für Übersetzungen. Wird für `/no_think` in Qwen 3 verwendet | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary`                    | Glossary file.                                                                          | `pdf2zh_next example.pdf --glossary "glossary.csv"`                                                                   |
| `--disable-glossary`            | Disable glossary.                                                                       | `pdf2zh_next example.pdf --disable-glossary`                                                                          |
| `--glossary-fallback`           | Fallback mode for glossary. Options: "keep", "ignore", "use"                            | `pdf2zh_next example.pdf --glossary-fallback "keep"`                                                                  |
| `--glossary-case-sensitive`     | Case sensitive for glossary.                                                            | `pdf2zh_next example.pdf --glossary-case-sensitive`                                                                   |
| `--glossary-merge-strategy`     | Merge strategy for multiple glossaries. Options: "first", "merge", "overwrite"          | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-merge-strategy "merge"`                |
| `--glossary-min-length`         | Minimum length of glossary terms.                                                       | `pdf2zh_next example.pdf --glossary-min-length 2`                                                                     |
| `--glossary-max-length`         | Maximum length of glossary terms.                                                       | `pdf2zh_next example.pdf --glossary-max-length 20`                                                                    |
| `--glossary-min-occurrence`     | Minimum occurrence of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-min-occurrence 2`                                                                 |
| `--glossary-max-occurrence`     | Maximum occurrence of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-max-occurrence 100`                                                               |
| `--glossary-min-confidence`     | Minimum confidence of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-min-confidence 0.5`                                                               |
| `--glossary-max-confidence`     | Maximum confidence of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-max-confidence 1.0`                                                               |
| `--glossary-min-precision`      | Minimum precision of glossary terms.                                                    | `pdf2zh_next example.pdf --glossary-min-precision 0.5`                                                                |
| `--glossary-max-precision`      | Maximum precision of glossary terms.                                                    | `pdf2zh_next example.pdf --glossary-max-precision 1.0`                                                                |
| `--glossary-min-recall`         | Minimum recall of glossary terms.                                                       | `pdf2zh_next example.pdf --glossary-min-recall 0.5`                                                                   |
| `--glossary-max-recall`         | Maximum recall of glossary terms.                                                       | `pdf2zh_next example.pdf --glossary-max-recall 1.0`                                                                   |
| `--glossary-min-f1`             | Minimum F1 score of glossary terms.                                                     | `pdf2zh_next example.pdf --glossary-min-f1 0.5`                                                                       |
| `--glossary-max-f1`             | Maximum F1 score of glossary terms.                                                     | `pdf2zh_next example.pdf --glossary-max-f1 1.0`                                                                       |
| `--glossary-min-support`        | Minimum support of glossary terms.                                                      | `pdf2zh_next example.pdf --glossary-min-support 2`                                                                    |
| `--glossary-max-support`        | Maximum support of glossary terms.                                                      | `pdf2zh_next example.pdf --glossary-max-support 100`                                                                  |
| `--glossary-min-coverage`       | Minimum coverage of glossary terms.                                                     | `pdf2zh_next example.pdf --glossary-min-coverage 0.5`                                                                 |
| `--glossary-max-coverage`       | Maximum coverage of glossary terms.                                                     | `pdf2zh_next example.pdf --glossary-max-coverage 1.0`                                                                 |
| `--glossary-min-density`        | Minimum density of glossary terms.                                                      | `pdf2zh_next example.pdf --glossary-min-density 0.5`                                                                  |
| `--glossary-max-density`        | Maximum density of glossary terms.                                                      | `pdf2zh_next example.pdf --glossary-max-density 1.0`                                                                  |
| `--glossary-min-entropy`        | Minimum entropy of glossary terms.                                                      | `pdf2zh_next example.pdf --glossary-min-entropy 0.5`                                                                  |
| `--glossary-max-entropy`        | Maximum entropy of glossary terms.                                                      | `pdf2zh_next example.pdf --glossary-max-entropy 1.0`                                                                  |
| `--glossary-min-specificity`    | Minimum specificity of glossary terms.                                                  | `pdf2zh_next example.pdf --glossary-min-specificity 0.5`                                                              |
| `--glossary-max-specificity`    | Maximum specificity of glossary terms.                                                  | `pdf2zh_next example.pdf --glossary-max-specificity 1.0`                                                              |
| `--glossary-min-accuracy`       | Minimum accuracy of glossary terms.                                                     | `pdf2zh_next example.pdf --glossary-min-accuracy 0.5`                                                                 |
| `--glossary-max-accuracy`       | Maximum accuracy of glossary terms.                                                     | `pdf2zh_next example.pdf --glossary-max-accuracy 1.0`                                                                 |
| `--glossary-min-balanced-accuracy` | Minimum balanced accuracy of glossary terms.                                         | `pdf2zh_next example.pdf --glossary-min-balanced-accuracy 0.5`                                                        |
| `--glossary-max-balanced-accuracy` | Maximum balanced accuracy of glossary terms.                                         | `pdf2zh_next example.pdf --glossary-max-balanced-accuracy 1.0`                                                        |
| `--glossary-min-matthews-correlation` | Minimum Matthews correlation coefficient of glossary terms.                          | `pdf2zh_next example.pdf --glossary-min-matthews-correlation 0.5`                                                     |
| `--glossary-max-matthews-correlation` | Maximum Matthews correlation coefficient of glossary terms.                          | `pdf2zh_next example.pdf --glossary-max-matthews-correlation 1.0`                                                     |
| `--glossary-min-informedness`   | Minimum informedness of glossary terms.                                                 | `pdf2zh_next example.pdf --glossary-min-informedness 0.5`                                                             |
| `--glossary-max-informedness`   | Maximum informedness of glossary terms.                                                 | `pdf2zh_next example.pdf --glossary-max-informedness 1.0`                                                             |
| `--glossary-min-markedness`     | Minimum markedness of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-min-markedness 0.5`                                                               |
| `--glossary-max-markedness`     | Maximum markedness of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-max-markedness 1.0`                                                               |
| `--glossary-min-prevalence`     | Minimum prevalence of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-min-prevalence 0.5`                                                               |
| `--glossary-max-prevalence`     | Maximum prevalence of glossary terms.                                                   | `pdf2zh_next example.pdf --glossary-max-prevalence 1.0`                                                               |
| `--glossary-min-bias`           | Minimum bias of glossary terms.                                                         | `pdf2zh_next example.pdf --glossary-min-bias 0.5`                                                                     |
| `--glossary-max-bias`           | Maximum bias of glossary terms.                                                         | `pdf2zh_next example.pdf --glossary-max-bias 1.0`                                                                     |
| `--glossary-min-prevalence-ratio` | Minimum prevalence ratio of glossary terms.                                           | `pdf2zh_next example.pdf --glossary-min-prevalence-ratio 0.5`                                                         |
| `--glossary-max-prevalence-ratio` | Maximum prevalence ratio of glossary terms.                                           | `pdf2zh_next example.pdf --glossary-max-prevalence-ratio 1.0`                                                         |
| `--glossary-min-prevalence-difference` | Minimum prevalence difference of glossary terms.                                    | `pdf2zh_next example.pdf --glossary-min-prevalence-difference 0.5`                                                    |
| `--glossary-max-prevalence-difference` | Maximum prevalence difference of glossary terms.                                    | `pdf2zh_next example.pdf --glossary-max-prevalence-difference 1.0`                                                    |
| `--glossary-min-prevalence-ratio-difference` | Minimum prevalence ratio difference of glossary terms.                          | `pdf2zh_next example.pdf --glossary-min-prevalence-ratio-difference 0.5`                                              |
| `--glossary-max-prevalence-ratio-difference` | Maximum prevalence ratio difference of glossary terms.                          | `pdf2zh_next example.pdf --glossary-max-prevalence-ratio-difference 1.极`                                             |

---

### OUTPUT

| `--glossaries`                  | Liste der Glossardateien.                                                                 | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary`                    | Glossardatei.                                                                          | `pdf2zh_next example.pdf --glossary "glossary.csv"`                                                                   |
| `--disable-glossary`            | Glossar deaktivieren.                                                                       | `pdf2zh_next example.pdf --disable-glossary`                                                                          |
| `--glossary-fallback`           | Fallback-Modus für das Glossar. Optionen: "keep", "ignore", "use"                            | `pdf2zh_next example.pdf --glossary-fallback "keep"`                                                                  |
| `--glossary-case-sensitive`     | Groß-/Kleinschreibung für das Glossar beachten.                                                            | `pdf2zh_next example.pdf --glossary-case-sensitive`                                                                   |
| `--glossary-merge-strategy`     | Zusammenführungsstrategie für mehrere Glossare. Optionen: "first", "merge", "overwrite"          | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-merge-strategy "merge"`                |
| `--glossary-min-length`         | Minimale Länge der Glossarbegriffe.                                                       | `pdf2zh_next example.pdf --glossary-min-length 2`                                                                     |
| `--glossary-max-length`         | Maximale Länge der Glossarbegriffe.                                                       | `pdf2zh_next example.pdf --glossary-max-length 20`                                                                    |
| `--glossary-min-occurrence`     | Minimale Häufigkeit der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-min-occurrence 极`                                                                 |
| `--glossary-max-occurrence`     | Maximale Häufigkeit der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-max-occurrence 100`                                                               |
| `--glossary-min-confidence`     | Minimale Konfidenz der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-min-confidence 0.5`                                                               |
| `--glossary-max-confidence`     | Maximale Konfidenz der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-max-confidence 1.0`                                                               |
| `--glossary-min-precision`      | Minimale Präzision der Glossarbegriffe.                                                    | `pdf 极 zh_next example.pdf --glossary-min-precision 0.5`                                                                |
| `--glossary-max-precision`      | Maximale Präzision der Glossarbegriffe.                                                    | `pdf2zh_next example.pdf --glossary-max-precision 1.0`                                                                |
| `--glossary-min-recall`         | Minimale Recall der Glossarbegriffe.                                                       | `pdf2zh_next example.pdf --glossary-min-recall 0.5`                                                                   |
| `--glossary 极 max-recall`         | Maximale Recall der Glossarbegriffe.                                                       | `pdf2zh_next example.pdf --glossary-max-recall 1.0`                                                                   |
| `--glossary-min-f1`             | Minimaler F1-Score der Glossarbegriffe.                                                     | `pdf2zh_next example.pdf --glossary-min-f1 0.5`                                                                       |
| `--glossary-max-f1`             | Maximaler F1-Score der Glossarbegriffe.                                                     | `pdf2zh_next example.pdf --glossary-max-f1 1.0`                                                                       |
| `--glossary-min-support`        | Minimale Unterstützung der Glossarbegriffe.                                                      | `pdf2zh_next example.pdf --glossary-min-support 2`                                                                    |
| `--glossary-max-support`        | Maximale Unterstützung der Glossarbegriffe.                                                      | `pdf2zh_next example.pdf --glossary-max-support 100`                                                                  |
| `--glossary-min-coverage`       | Minimale Abdeckung der Glossarbegriffe.                                                     | `pdf2zh_next example.pdf --glossary-min-coverage 0.5`                                                                 |
| `--glossary-max-coverage`       | Maximale Abdeckung der Glossarbegriffe.                                                     | `pdf2zh_next example.pdf --glossary-max-coverage 1.0`                                                                 |
| `--glossary-min-density`        | Minimale Dichte der Glossarbegriffe.                                                      | `pdf2zh_next example.pdf --glossary-min-density 0.5`                                                                  |
| `--glossary-max-density`        | Maximale Dichte der Glossarbegriffe.                                                      | `pdf2zh_next example.pdf --glossary-max-density 1.0`                                                                  |
| `--glossary-min-entropy`        | Minimale Entropie der Glossarbegriffe.                                                      | `pdf2zh_next example.pdf --glossary-min-entropy 0.5`                                                                  |
| `--glossary-max-entropy`        | Maximale Entropie der Glossarbegriffe.                                                      | `pdf2zh_next example.pdf --glossary-max-entropy 1.0`                                                                  |
| `--glossary-min-specificity`    | Minimale Spezifität der Glossarbegriffe.                                                  | `pdf2zh_next example.pdf --glossary-min-specificity 0.5`                                                              |
| `--glossary-max-specificity`    | Maximale Spezifität der Glossarbegriffe.                                                  | `pdf2zh_next example.pdf --glossary-max-specificity 1.0`                                                              |
| `--glossary-min-accuracy`       | Minimale Genauigkeit der Glossarb 极 egriffe.                                                     | `pdf2zh_next example.pdf --glossary-min-accuracy 0.5`                                                                 |
| `--glossary-max-accuracy`       | Maximale Genauigkeit der Glossarbegriffe.                                                     | `pdf2zh_next example.pdf --glossary-max-accuracy 1.0`                                                                 |
| `--glossary-min-balanced-accuracy` | Minimale ausbalancierte Genauigkeit der Glossarbegriffe.                                         | `pdf2zh_next example.pdf --glossary-min-balanced-accuracy 0.5`                                                        |
| `--glossary-max-balanced-accuracy` | Maximale ausbalancierte Genauigkeit der Glossarbegriffe.                                         | `pdf2zh_next example.pdf --glossary-max-balanced-accuracy 1.0`                                                        |
| `--glossary-min-matthews-correlation` | Minimaler Matthews-Korrelationskoeffizient der Glossarbegriffe.                          | `pdf2zh_next example.pdf --glossary-min-matthews-correlation 0.5`                                                     |
| `--glossary-max-matthews-correlation` | Maximaler Matthews-Korrelationskoeffizient der Glossarbegriffe.                          | `pdf2zh_next example.pdf --glossary-max-matthews-correlation 1.0`                                                     |
| `--glossary-min-informedness`   | Minimale Informiertheit der Glossarbegriffe.                                                 | `pdf2zh_next example.pdf --glossary-min-informedness 0.5`                                                             |
| `--glossary-max-informedness`   | Maximale Informiertheit der Glossarbegriffe.                                                 | `pdf2zh_next example.pdf --glossary-max-informedness 1.0`                                                             |
| `--glossary-min-markedness`     | Minimale Markiertheit der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-min-markedness 0.5`                                                               |
| `--glossary-max-markedness`     | Maximale Markiertheit der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-max-markedness 1.0`                                                               |
| `--glossary-min-prevalence`     | Minimale Prävalenz der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-min-prevalence 0.5`                                                               |
| `--glossary-max-prevalence`     | Maximale Prävalenz der Glossarbegriffe.                                                   | `pdf2zh_next example.pdf --glossary-max-prevalence 1.0`                                                               |
| `--glossary-min-bias`           | Minimale Verzerrung der Glossarbegriffe.                                                         | `pdf2zh_next example.pdf --glossary-min-bias 0.5`                                                                     |
| `--glossary-max-bias`           | Maximale Verzerrung der Glossarbegriffe.                                                         | `pdf2zh_next example.pdf --glossary-max-bias 1.0`                                                                     |
| `--glossary-min-prevalence-ratio` | Minimales Prävalenzverhältnis der Glossarbegriffe.                                           | `pdf2zh_next example.pdf --glossary-min-prevalence-ratio 0.5`                                                         |
| `--glossary-max-prevalence-ratio` | Maximales Prävalenzverhältnis der Glossarbegriffe.                                           | `pdf2zh_next example.pdf --glossary-max-prevalence-ratio 1.0`                                                         |
| `--glossary-min-prevalence-difference` | Minimale Prävalenzdifferenz der Glossarbegriffe.                                    | `pdf2zh_next example.pdf --glossary-min-prevalence-difference 0.5`                                                    |
| `--glossary-max-prevalence-difference` | Maximale Prävalenzdifferenz der Glossarbegriffe.                                    | `pdf2zh_next example.pdf --glossary-max-prevalence-difference 1.0`                                                    |
| `--glossary-min-prevalence-ratio-difference` | Minimale Prävalenzverhältnisdifferenz der Glossarbegriffe.                          | `pdf2zh_next example.pdf --glossary-min-prevalence-ratio-difference 0.5`                                              |
| `--glossary-max-prevalence-ratio-difference` | Maximale Prävalenzverhältnisdifferenz der Glossarbegriffe.                          | `pdf2zh_next example.pdf --glossary-max-prevalence-ratio-difference 1.0`                                              |
| :------------------------------- | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--glossary`                     | use glossary                                                                            | `pdf2zh_next example.pdf --glossary glossary.json`                                                                     |
| `--glossary-url`                 | use glossary from URL                                                                   | `pdf2zh_next example.pdf --glossary-url https://example.com/glossary.json`                                             |
| `--glossary-merge-mode`          | glossary merge mode, options: `merge`, `overwrite`, default: `merge`                    | `pdf2zh_next example.pdf --glossary-merge-mode overwrite`                                                              |
| `--glossary-min-freq`            | minimum frequency for automatically extracted glossary, default: `2`                    | `pdf2zh_next example.pdf --glossary-min-freq 5`                                                                        |
| `--glossary-min-prob`            | minimum probability for automatically extracted glossary, default: `0.5`                | `pdf2zh_next example.pdf --glossary-min-prob 0.7`                                                                      |
| `--glossary-min-score`           | minimum score for automatically extracted glossary, default: `0.5`                      | `pdf2zh_next example.pdf --glossary-min-score 0.7`                                                                     |

---

### TRANSLATION RESULT

| `--save-auto-extracted-glossary` | Automatisch extrahiertes Glossar speichern                                             | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| :------------------------------- | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--glossary`                     | Glossar verwenden                                                                       | `pdf2zh_next example.pdf --glossary glossary.json`                                                                     |
| `--glossary-url`                 | Glossar von URL verwenden                                                               | `pdf2zh_next example.pdf --glossary-url https://example.com/glossary.json`                                             |
| `--glossary-merge-mode`          | Glossar-Zusammenführungsmodus, Optionen: `merge`, `overwrite`, Standard: `merge`        | `pdf2zh_next example.pdf --glossary-merge-mode overwrite`                                                              |
| `--glossary-min-freq`            | Mindesthäufigkeit für automatisch extrahiertes Glossar, Standard: `2`                   | `pdf2zh_next example.pdf --glossary-min-freq 5`                                                                        |
| `--glossary-min-prob`            | Mindestwahrscheinlichkeit für automatisch extrahiertes Glossar, Standard: `0.5`         | `pdf2zh_next example.pdf --glossary-min-prob 0.7`                                                                      |
| `--glossary-min-score`           | Mindestpunktzahl für automatisch extrahiertes Glossar, Standard: `0.5`                  | `pdf2zh_next example.pdf --glossary-min-score 0.7`                                                                     |
`number`  |
| `--pool-min-workers`            | Minimum number of workers for translation pool. If not set, will use qps as the number of workers | `pdf2zh_next example.pdf --pool-min-workers 10`                                                            | `number`  |
| `--pool-max-tasks-per-child`    | Maximum number of tasks per worker before it is replaced with a new one                          | `pdf2zh_next example.pdf --pool-max-tasks-per-child 100`                                                   | `number`  |
| `--pool-max-tasks-queued`       | Maximum number of tasks that can be queued for execution in the pool                             | `pdf2zh_next example.pdf --pool-max-tasks-queued 1000`                                                     | `number`  |

---

### TRANSLATION RESULT

| `--pool-max-workers`            | Maximale Anzahl von Workern für den Übersetzungspool. Wenn nicht festgelegt, wird qps als Anzahl der Worker verwendet | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           | `number`  |
| `--pool-min-workers`            | Minimale Anzahl von Workern für den Übersetzungspool. Wenn nicht festgelegt, wird qps als Anzahl der Worker verwendet | `pdf2zh_next example.pdf --pool-min-workers 10`                                                            | `number`  |
| `--pool-max-tasks-per-child`    | Maximale Anzahl von Aufgaben pro Worker, bevor dieser durch einen neuen ersetzt wird                                 | `pdf2zh_next example.pdf --pool-max-tasks-per-child 100`                                                   | `number`  |
| `--pool-max-tasks-queued`       | Maximale Anzahl von Aufgaben, die für die Ausführung im Pool in die Warteschlange gestellt werden können              | `pdf2zh_next example.pdf --pool-max-tasks-queued 1000`                                                     | `number`  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--term-concurrency`            | Maximum number of concurrent requests for term extraction translation service.          | `pdf2zh_next example.pdf --term-concurrency 5`                                                                         |
| `--term-timeout`                | Timeout for term extraction translation service (seconds).                              | `pdf2zh_next example.pdf --term-timeout 30`                                                                            |
| `--term-max-retries`            | Maximum number of retries for term extraction translation service.                      | `pdf2zh_next example.pdf --term-max-retries 3`                                                                         |

---

### OUTPUT

| `--term-qps`                    | QPS-Limit für den Übersetzungsdienst zur Begriffsentnahme. Wenn nicht gesetzt, folgt es qps. | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| :------------------------------ | :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--term-concurrency`            | Maximale Anzahl gleichzeitiger Anfragen für den Übersetzungsdienst zur Begriffsentnahme.      | `pdf2zh_next example.pdf --term-concurrency 5`                                                                         |
| `--term-timeout`                | Zeitüberschreitung für den Übersetzungsdienst zur Begriffsentnahme (Sekunden).               | `pdf2zh_next example.pdf --term-timeout 30`                                                                            |
| `--term-max-retries`            | Maximale Anzahl von Wiederholungsversuchen für den Übersetzungsdienst zur Begriffsentnahme.   | `pdf2zh_next example.pdf --term-max-retries 3`                                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `--term-pool-max-workers-per-id` | Maximum number of workers for term extraction translation pool per language ID. If not set or 0, will follow pool_max_workers_per_id. | `pdf2zh_next example.pdf --term-pool-max-workers-per-id 2`                                            |

---

### OUTPUT

| `--term-pool-max-workers`       | Maximale Anzahl von Arbeitern für den Übersetzungspool zur Begriffsentnahme. Wenn nicht gesetzt oder 0, folgt es pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `--term-pool-max-workers-per-id` | Maximale Anzahl von Arbeitern für den Übersetzungspool zur Begriffsentnahme pro Sprach-ID. Wenn nicht gesetzt oder 0, folgt es pool_max_workers_per_id. | `pdf2zh_next example.pdf --term-pool-max-workers-per-id 2`                                            |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--glossary-file <file_path>`   | Use a custom glossary file                                                              | `pdf2zh_next example.pdf --glossary-file my_glossary.txt`                                                             |
| `--glossary-string <json_str>`  | Use a custom glossary string in JSON format                                             | `pdf2zh_next example.pdf --glossary-string '{"PDFMathTranslate": "PDF 数学翻译", "pdf2zh": "pdf 转中"}'`                |
| `--glossary-merge-strategy`     | Strategy for merging glossaries (default: `prioritize_non_empty`)                       | `pdf2zh_next example.pdf --glossary-merge-strategy prioritize_custom`                                                 |
| `--glossary-merge-strategy`     | Available options: `prioritize_non_empty`, `prioritize_custom`, `prioritize_auto`       | `pdf2zh_next example.pdf --glossary-merge-strategy prioritize_auto`                                                   |

---

### OUTPUT

| `--no-auto-extract-glossary`    | Deaktiviert das automatische Extrahieren des Glossars                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--glossary-file <file_path>`   | Verwendet eine benutzerdefinierte Glossardatei                                                                  | `pdf2zh_next example.pdf --glossary-file my_glossary.txt`                                                             |
| `--glossary-string <json_str>`  | Verwendet eine benutzerdefinierte Glossarzeichenkette im JSON-Format                                            | `pdf2zh_next example.pdf --glossary-string '{"PDFMathTranslate": "PDF 数学翻译", "pdf2zh": "pdf 转中"}'`                |
| `--glossary-merge-strategy`     | Strategie zum Zusammenführen von Glossaren (Standard: `prioritize_non_empty`)                                   | `pdf2zh_next example.pdf --glossary-merge-strategy prioritize_custom`                                                 |
| `--glossary-merge-strategy`     | Verfügbare Optionen: `prioritize_non_empty`, `prioritize_custom`, `prioritize_auto`                            | `pdf2zh_next example.pdf --glossary-merge-strategy prioritize_auto`                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `--secondary-font-family`       | Override secondary font family for auxiliary text (like page numbers). Same choices as `--primary-font-family`.                                                                                                                           | `pdf2zh_next example.pdf --secondary-font-family serif` |
| `--font-size-multiplier`        | Scale factor for font sizes (0.8-1.2). Useful for adjusting text density.                                                                                                                                                                 | `pdf2zh_next example.pdf --font-size-multiplier 1.1`   |
| `--line-height-multiplier`      | Scale factor for line spacing (0.8-1.2).                                                                                                                                                                                                  | `pdf2zh_next example.pdf --line-height-multiplier 0.9` |
| `--char-spacing-multiplier`     | Scale factor for character spacing (0.8-1.2).                                                                                                                                                                                             | `pdf2zh_next example.pdf --char-spacing-multiplier 1.0`|
| `--word-spacing-multiplier`     | Scale factor for word spacing (0.8-1.2).                                                                                                                                                                                                  | `pdf2zh_next example.pdf --word-spacing-multiplier 1.0`|

---

### TRANSLATION RESULT

| `--primary-font-family`         | Überschreibt die primäre Schriftfamilie für den übersetzten Text. Optionen: 'serif' für Serifenschriften, 'sans-serif' für serifenlose Schriften, 'script' für Schreibschrift/kursive Schriften. Wenn nicht angegeben, wird eine automatische Schriftauswahl basierend auf den Eigenschaften des Originaltextes verwendet. | `pdf2zh_next example.pdf --primary-font-family serif` |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `--secondary-font-family`       | Überschreibt die sekundäre Schriftfamilie für Hilfstext (wie Seitenzahlen). Gleiche Optionen wie `--primary-font-family`.                                                                                                                                  | `pdf2zh_next example.pdf --secondary-font-family serif` |
| `--font-size-multiplier`        | Skalierungsfaktor für Schriftgrößen (0.8-1.2). Nützlich zum Anpassen der Textdichte.                                                                                                                                                                      | `pdf2zh_next example.pdf --font-size-multiplier 1.1`   |
| `--line-height-multiplier`      | Skalierungsfaktor für den Zeilenabstand (0.8-1.2).                                                                                                                                                                                                         | `pdf2zh_next example.pdf --line-height-multiplier 0.9` |
| `--char-spacing-multiplier`     | Skalierungsfaktor für den Zeichenabstand (0.8-1.2).                                                                                                                                                                                                       | `pdf2zh_next example.pdf --char-spacing-multiplier 1.0`|
| `--word-spacing-multiplier`     | Skalierungsfaktor für den Wortabstand (0.8-1.2).                                                                                                                                                                                                          | `pdf2zh_next example.pdf --word-spacing-multiplier 1.0`|
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-image`                    | Do not output images                                                                    | `pdf2zh_next example.pdf --no-image`                                                                                  |
| `--no-text`                     | Do not output text                                                                      | `pdf2zh_next example.pdf --no-text`                                                                                   |
| `--no-table`                    | Do not output tables                                                                    | `pdf2zh_next example.pdf --no-table`                                                                                  |
| `--no-math`                     | Do not output mathematical formulas                                                     | `pdf2zh_next example.pdf --no-math`                                                                                   |
| `--no-graphics`                 | Do not output graphics                                                                  | `pdf2zh_next example.pdf --no-graphics`                                                                               |
| `--no-code`                     | Do not output code blocks                                                               | `pdf2zh_next example.pdf --no-code`                                                                                   |
| `--no-list`                     | Do not output lists                                                                     | `pdf2zh_next example.pdf --no-list`                                                                                   |
| `--no-quote`                    | Do not output quotes                                                                    | `pdf2zh_next example.pdf --no-quote`                                                                                  |
| `--no-footnote`                 | Do not output footnotes                                                                 | `pdf2zh_next example.pdf --no-footnote`                                                                               |
---

### OUTPUT

| `--no-dual`                     | Keine zweisprachigen PDF-Dateien ausgeben                                               | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-image`                    | Keine Bilder ausgeben                                                                   | `pdf2zh_next example.pdf --no-image`                                                                                  |
| `--no-text`                     | Keinen Text ausgeben                                                                    | `pdf2zh_next example.pdf --no-text`                                                                                   |
| `--no-table`                    | Keine Tabellen ausgeben                                                                 | `pdf2zh_next example.pdf --no-table`                                                                                  |
| `--no-math`                     | Keine mathematischen Formeln ausgeben                                                   | `pdf2zh_next example.pdf --no-math`                                                                                   |
| `--no-graphics`                 | Keine Grafiken ausgeben                                                                 | `pdf2zh_next example.pdf --no-graphics`                                                                               |
| `--no-code`                     | Keine Codeblöcke ausgeben                                                               | `pdf2zh_next example.pdf --no-code`                                                                                   |
| `--no-list`                     | Keine Listen ausgeben                                                                   | `pdf2zh_next example.pdf --no-list`                                                                                   |
| `--no-quote`                    | Keine Zitate ausgeben                                                                   | `pdf2zh_next example.pdf --no-quote`                                                                                  |
| `--no-footnote`                 | Keine Fußnoten ausgeben                                                                 | `pdf2zh_next example.pdf --no-footnote`                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-bilingual`                | Do not output bilingual PDF files                                                       | `pdf2zh_next example.pdf --no-bilingual`                                                                               |
| `--no-tex`                      | Do not output LaTeX files                                                               | `pdf2zh_next example.pdf --no-tex`                                                                                     |

---

### OUTPUT

| `--no-mono`                     | Einsprachige PDF-Dateien nicht ausgeben                                                 | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-bilingual`                | Zweisprachige PDF-Dateien nicht ausgeben                                                | `pdf2zh_next example.pdf --no-bilingual`                                                                               |
| `--no-tex`                      | LaTeX-Dateien nicht ausgeben                                                            | `pdf2zh_next example.pdf --no-tex`                                                                                     |

| `--formular-char-pattern-replace` | Replacement text for the matched formula character pattern                             | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-replace "\\1"`                      |
| `--formular-char-pattern-ignore` | Ignore formula character pattern matches                                                | `pdf2zh_next example.pdf --formular-char-pattern-ignore "(MS.*)"`                                                     |
| `--formular-char-pattern-ignore-replace` | Replacement text for ignored formula character pattern matches                         | `pdf2zh_next example.pdf --formular-char-pattern-ignore "(MS.*)" --formular-char-pattern-ignore-replace "\\1"`        |
| `--formular-preserve-color`      | Preserve color information in formulas                                                  | `pdf2zh_next example.pdf --formular-preserve-color`                                                                   |
| `--formular-preserve-font-family` | Preserve font family information in formulas                                            | `pdf2zh_next example.pdf --formular-preserve-font-family`                                                             |
| `--formular-preserve-font-size`  | Preserve font size information in formulas                                              | `pdf2zh_next example.pdf --formular-preserve-font-size`                                                               |
| `--formular-preserve-font-style` | Preserve font style information in formulas                                             | `pdf2zh_next example.pdf --formular-preserve-font-style`                                                              |
| `--formular-preserve-font-weight`| Preserve font weight information in formulas                                            | `pdf2zh_next example.pdf --formular-preserve-font-weight`                                                             |
| `--formular-preserve-font-variant`| Preserve font variant information in formulas                                           | `pdf2zh_next example.pdf --formular-preserve-font-variant`                                                            |
| `--formular-preserve-font-stretch`| Preserve font stretch information in formulas                                           | `pdf2zh_next example.pdf --formular-preserve-font-stretch`                                                            |
| `--formular-preserve-font-decoration`| Preserve font decoration information in formulas                                        | `pdf2zh_next example.pdf --formular-preserve-font-decoration`                                                         |
| `--formular-preserve-font-kerning`| Preserve font kerning information in formulas                                           | `pdf2zh_next example.pdf --formular-preserve-font-kerning`                                                            |
| `--formular-preserve-font-ligatures`| Preserve font ligatures information in formulas                                         | `pdf2zh_next example.pdf --formular-preserve-font-ligatures`                                                          |
| `--formular-preserve-font-variant-ligatures`| Preserve font variant ligatures information in formulas                                | `pdf2zh_next example.pdf --formular-preserve-font-variant-ligatures`                                                  |
| `--formular-preserve-font-variant-caps`| Preserve font variant caps information in formulas                                      | `pdf2zh_next example.pdf --formular-preserve-font-variant-caps`                                                       |
| `--formular-preserve-font-variant-numeric`| Preserve font variant numeric information in formulas                                   | `pdf2zh_next example.pdf --formular-preserve-font-variant-numeric`                                                    |
| `--formular-preserve-font-variant-alternates`| Preserve font variant alternates information in formulas                               | `pdf2zh_next example.pdf --formular-preserve-font-variant-alternates`                                                 |
| `--formular-preserve-font-variant-east-asian`| Preserve font variant east asian information in formulas                               | `pdf2zh_next example.pdf --formular-preserve-font-variant-east-asian`                                                 |
| `--formular-preserve-font-variant-position`| Preserve font variant position information in formulas                                 | `pdf2zh_next example.pdf --formular-preserve-font-variant-position`                                                   |
| `--formular-preserve-font-variant-emoji`| Preserve font variant emoji information in formulas                                     | `pdf2zh_next example.pdf --formular-preserve-font-variant-emoji`                                                      |
| `--formular-preserve-font-variant-annotation`| Preserve font variant annotation information in formulas                               | `pdf2zh_next example.pdf --formular-preserve-font-variant-annotation`                                                 |
| `--formular-preserve-font-feature-settings`| Preserve font feature settings information in formulas                                  | `pdf2zh_next example.pdf --formular-preserve-font-feature-settings`                                                   |
| `--formular-preserve-font-variation-settings`| Preserve font variation settings information in formulas                               | `pdf2zh_next example.pdf --formular-preserve-font-variation-settings`                                                 |
| `--formular-preserve-font-palette`| Preserve font palette information in formulas                                           | `pdf2zh_next example.pdf --formular-preserve-font-palette`                                                            |
| `--formular-preserve-font-synthesis`| Preserve font synthesis information in formulas                                         | `pdf2zh_next example.pdf --formular-preserve-font-synthesis`                                                          |
| `--formular-preserve-font-synthesis-weight`| Preserve font synthesis weight information in formulas                                  | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-weight`                                                   |
| `--formular-preserve-font-synthesis-style`| Preserve font synthesis style information in formulas                                   | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-style`                                                    |
| `--formular-preserve-font-synthesis-small-caps`| Preserve font synthesis small caps information in formulas                             | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-small-caps`                                               |
| `--formular-preserve-font-synthesis-position`| Preserve font synthesis position information in formulas                               | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-position`                                                 |
| `--formular-preserve-font-synthesis-emoji`| Preserve font synthesis emoji information in formulas                                   | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-emoji`                                                    |
| `--formular-preserve-font-synthesis-annotation`| Preserve font synthesis annotation information in formulas                             | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-annotation`                                               |
| `--formular-preserve-font-synthesis-feature-settings`| Preserve font synthesis feature settings information in formulas                       | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-feature-settings`                                         |
| `--formular-preserve-font-synthesis-variation-settings`| Preserve font synthesis variation settings information in formulas                    | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-variation-settings`                                       |
| `--formular-preserve-font-synthesis-palette`| Preserve font synthesis palette information in formulas                                 | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-palette`                                                  |
| `--formular-preserve-font-synthesis-optical-sizing`| Preserve font synthesis optical sizing information in formulas                         | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-optical-sizing`                                           |
| `--formular-preserve-font-synthesis-size-adjust`| Preserve font synthesis size adjust information in formulas                            | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-size-adjust`                                              |
| `--formular-preserve-font-synthesis-size`| Preserve font synthesis size information in formulas                                    | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-size`                                                     |
| `--formular-preserve-font-synthesis-size-adjust`| Preserve font synthesis size adjust information in formulas                            | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-size-adjust`                                              |

---

### TRANSLATION

| `--formular-char-pattern`       | Zeichenmuster zur Identifizierung von Formeltext                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| `--formular-char-pattern-replace` | Ersatztext für das übereinstimmende Formelzeichenmuster                             | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-replace "\\1"`                      |
| `--formular-char-pattern-ignore` | Ignoriere Übereinstimmungen mit Formelzeichenmustern                                                | `pdf2zh_next example.pdf --formular-char-pattern-ignore "(MS.*)"`                                                     |
| `--formular-char-pattern-ignore-replace` | Ersatztext für ignorierte Übereinstimmungen mit Formelzeichenmustern                         | `pdf2zh_next example.pdf --formular-char-pattern-ignore "(MS.*)" --formular-char-pattern-ignore-replace "\\1"`        |
| `--formular-preserve-color`      | Behalte Farbinformationen in Formeln                                                  | `pdf2zh_next example.pdf --formular-preserve-color`                                                                   |
| `--formular-preserve-font-family` | Behalte Schriftartinformationen in Formeln                                            | `pdf2zh_next example.pdf --formular-preserve-font-family`                                                             |
| `--formular-preserve-font-size`  | Behalte Schriftgrößeninformationen in Formeln                                              | `pdf2zh_next example.pdf --formular-preserve-font-size`                                                               |
| `--formular-preserve-font-style` | Behalte Schriftstilinformationen in Formeln                                             | `pdf2zh_next example.pdf --formular-preserve-font-style`                                                              |
| `--formular-preserve-font-weight`| Behalte Schriftdickeninformationen in Formeln                                            | `pdf2zh_next example.pdf --formular-preserve-font-weight`                                                             |
| `--formular-preserve-font-variant`| Behalte Schriftvariationsinformationen in Formeln                                           | `pdf2zh_next example.pdf --formular-preserve-font-variant`                                                            |
| `--formular-preserve-font-stretch`| Behalte Schriftdehnungsinformationen in Formeln                                           | `pdf2zh_next example.pdf --formular-preserve-font-stretch`                                                            |
| `--formular-preserve-font-decoration`| Behalte Schriftdekorationeninformationen in Formeln                                        | `pdf2zh_next example.pdf --formular-preserve-font-decoration`                                                         |
| `--formular-preserve-font-kerning`| Behalte Schriftabstandsausgleichsinformationen in Formeln                                           | `pdf2zh_next example.pdf --formular-preserve-font-kerning`                                                            |
| `--formular-preserve-font-ligatures`| Behalte Ligatureninformationen in Formeln                                         | `pdf2zh_next example.pdf --formular-preserve-font-ligatures`                                                          |
| `--formular-preserve-font-variant-ligatures`| Behalte Informationen zu Schriftvariantenligaturen in Formeln                                | `pdf2zh_next example.pdf --formular-preserve-font-variant-ligatures`                                                  |
| `--formular-preserve-font-variant-caps`| Behalte Informationen zu Schriftvariantengroßbuchstaben in Formeln                                      | `pdf2zh_next example.pdf --formular-preserve-font-variant-caps`                                                       |
| `--formular-preserve-font-variant-numeric`| Behalte Informationen zu Schriftvariantenzahlen in Formeln                                   | `pdf2zh_next example.pdf --formular-preserve-font-variant-numeric`                                                    |
| `--formular-preserve-font-variant-alternates`| Behalte Informationen zu Schriftvariantenalternativen in Formeln                               | `pdf2zh_next example.pdf --formular-preserve-font-variant-alternates`                                                 |
| `--formular-preserve-font-variant-east-asian`| Behalte Informationen zu Schriftvariantenostasiatischen Zeichen in Formeln                               | `pdf2zh_next example.pdf --formular-preserve-font-variant-east-asian`                                                 |
| `--formular-preserve-font-variant-position`| Behalte Informationen zu Schriftvariantenpositionen in Formeln                                 | `pdf2zh_next example.pdf --formular-preserve-font-variant-position`                                                   |
| `--formular-preserve-font-variant-emoji`| Behalte Informationen zu Schriftvariantenemojis in Formeln                                     | `pdf2zh_next example.pdf --formular-preserve-font-variant-emoji`                                                      |
| `--formular-preserve-font-variant-annotation`| Behalte Informationen zu Schriftvariantenanmerkungen in Formeln                               | `pdf2zh_next example.pdf --formular-preserve-font-variant-annotation`                                                 |
| `--formular-preserve-font-feature-settings`| Behalte Informationen zu Schriftspezialfunktionen in Formeln                                  | `pdf2zh_next example.pdf --formular-preserve-font-feature-settings`                                                   |
| `--formular-preserve-font-variation-settings`| Behalte Informationen zu Schriftvariationseinstellungen in Formeln                               | `pdf2zh_next example.pdf --formular-preserve-font-variation-settings`                                                 |
| `--formular-preserve-font-palette`| Behalte Informationen zu Schriftfarbpaletten in Formeln                                           | `pdf2zh_next example.pdf --formular-preserve-font-palette`                                                            |
| `--formular-preserve-font-synthesis`| Behalte Informationen zu Schriftsynthese in Formeln                                         | `pdf2zh_next example.pdf --formular-preserve-font-synthesis`                                                          |
| `--formular-preserve-font-synthesis-weight`| Behalte Informationen zur Schriftsynthesegewichtung in Formeln                                  | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-weight`                                                   |
| `--formular-preserve-font-synthesis-style`| Behalte Informationen zum Schriftsynthesestil in Formeln                                   | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-style`                                                    |
| `--formular-preserve-font-synthesis-small-caps`| Behalte Informationen zur Schriftsynthesekleinschrift in Formeln                             | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-small-caps`                                               |
| `--formular-preserve-font-synthesis-position`| Behalte Informationen zur Schriftsyntheseposition in Formeln                               | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-position`                                                 |
| `--formular-preserve-font-synthesis-emoji`| Behalte Informationen zur Schriftsyntheseemojis in Formeln                                   | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-emoji`                                                    |
| `--formular-preserve-font-synthesis-annotation`| Behalte Informationen zur Schriftsyntheseanmerkungen in Formeln                             | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-annotation`                                               |
| `--formular-preserve-font-synthesis-feature-settings`| Behalte Informationen zu Schriftsynthesespezialfunktionen in Formeln                       | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-feature-settings`                                         |
| `--formular-preserve-font-synthesis-variation-settings`| Behalte Informationen zu Schriftsynthesevariationseinstellungen in Formeln                    | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-variation-settings`                                       |
| `--formular-preserve-font-synthesis-palette`| Behalte Informationen zu Schriftsynthesefarbpaletten in Formeln                                 | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-palette`                                                  |
| `--formular-preserve-font-synthesis-optical-sizing`| Behalte Informationen zur Schriftsyntheseoptischen Größenanpassung in Formeln                         | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-optical-sizing`                                           |
| `--formular-preserve-font-synthesis-size-adjust`| Behalte Informationen zur Schriftsynthesegrößenanpassung in Formeln                            | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-size-adjust`                                              |
| `--formular-preserve-font-synthesis-size`| Behalte Informationen zur Schriftsynthesegröße in Formeln                                    | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-size`                                                     |
| `--formular-preserve-font-synthesis-size-adjust`| Behalte Informationen zur Schriftsynthesegrößenanpassung in Formeln                            | `pdf2zh_next example.pdf --formular-preserve-font-synthesis-size-adjust`                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-long-lines`            | Force split long lines into different paragraphs                                        | `pdf2zh_next example.pdf --split-long-lines`                                                                          |
| `--split-line-length-threshold` | Set the threshold for splitting lines. Default is `20` for short lines and `50` for long lines | `pdf2zh_next example.pdf --split-long-lines --split-line-length-threshold 60`                                         |
| `--split-paragraphs`            | Force split paragraphs                                                                  | `pdf2zh_next example.pdf --split-paragraphs`                                                                          |
| `--split-paragraph-length`      | Set the threshold for splitting paragraphs. Default is `200`                            | `pdf2zh_next example.pdf --split-paragraphs --split-paragraph-length 300`                                             |
| `--split-paragraph-lines`       | Set the number of lines to split paragraphs. Default is `5`                             | `pdf2zh_next example.pdf --split-paragraphs --split-paragraph-lines 10`                                               |

---

### TRANSLATED TEXT

| `--split-short-lines`           | Erzwingt das Aufteilen kurzer Zeilen in verschiedene Absätze                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-long-lines`            | Erzwingt das Aufteilen langer Zeilen in verschiedene Absätze                                        | `pdf2zh_next example.pdf --split-long-lines`                                                                          |
| `--split-line-length-threshold` | Legt den Schwellenwert für das Aufteilen von Zeilen fest. Standard ist `20` für kurze Zeilen und `50` für lange Zeilen | `pdf2zh_next example.pdf --split-long-lines --split-line-length-threshold 60`                                         |
| `--split-paragraphs`            | Erzwingt das Aufteilen von Absätzen                                                                  | `pdf2zh_next example.pdf --split-paragraphs`                                                                          |
| `--split-paragraph-length`      | Legt den Schwellenwert für das Aufteilen von Absätzen fest. Standard ist `200`                            | `pdf2zh_next example.pdf --split-paragraphs --split-paragraph-length 300`                                             |
| `--split-paragraph-lines`       | Legt die Anzahl der Zeilen zum Aufteilen von Absätzen fest. Standard ist `5`                             | `pdf2zh_next example.pdf --split-paragraphs --split-paragraph-lines 10`                                               |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--long-line-merge-factor`      | Merge threshold factor for long lines                                                   | `pdf2zh_next example.pdf --long-line-merge-factor 1.5`                                                                |
| `--table-merge-threshold`       | Table cell merge threshold (in inches)                                                  | `pdf2zh_next example.pdf --table-merge-threshold 0.1`                                                                 |
| `--table-vertical-threshold`    | Table vertical alignment threshold (in inches)                                          | `pdf2zh_next example.pdf --table-vertical-threshold 0.05`                                                             |

---

### OUTPUT

| `--short-line-split-factor`     | Teilungsschwellwertfaktor für kurze Zeilen                                              | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--long-line-merge-factor`      | Zusammenführungsschwellwertfaktor für lange Zeilen                                      | `pdf2zh_next example.pdf --long-line-merge-factor 1.5`                                                                |
| `--table-merge-threshold`       | Tabellenzellen-Zusammenführungsschwelle (in Zoll)                                       | `pdf2zh_next example.pdf --table-merge-threshold 0.1`                                                                 |
| `--table-vertical-threshold`    | Tabellenvertikale Ausrichtungsschwelle (in Zoll)                                        | `pdf2zh_next example.pdf --table-vertical-threshold 0.05`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translation`            | Skip the translation step                                                               | `pdf2zh_next example.pdf --skip-translation`                                                                          |
| `--skip-ocr`                    | Skip the OCR step (if the document contains images, OCR will still be performed)        | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-clean-format`           | Skip PDF cleaning and formatting step                                                   | `pdf2zh_next example.pdf --skip-clean-format`                                                                         |
| `--skip-extract`                | Skip the text extraction step (requires the input to be an already extracted JSON file) | `pdf2zh_next example.json --skip-extract`                                                                             |
| `--skip-reconstruction`         | Skip the reconstruction step (requires the input to be an already translated JSON file) | `pdf2zh_next example.json --skip-reconstruction`                                                                      |
| `--skip-save`                   | Skip the saving step (only output to stdout)                                            | `pdf2zh_next example.pdf --skip-save`                                                                                 |
| `--translate-to <language>`     | Set the translation target language (default: zh)                                       | `pdf2zh_next example.pdf --translate-to en`                                                                           |
| `--translate-service <service>` | Set the translation service (default: google)                                           | `pdf2zh_next example.pdf --translate-service google`                                                                  |
| `--translate-options <options>` | Set the translation options (JSON string)                                               | `pdf2zh_next example.pdf --translate-options '{"timeout": 10, "retries": 3}'`                                         |
| `--translate-key <key>`         | Set the translation API key (if required)                                               | `pdf2zh_next example.pdf --translate-key <your-api-key>`                                                              |
| `--ocr-language <language>`     | Set the OCR language (default: eng)                                                     | `pdf2zh_next example.pdf --ocr-language eng+chi_sim`                                                                  |
| `--ocr-options <options>`       | Set the OCR options (JSON string)                                                       | `pdf2zh_next example.pdf --ocr-options '{"tesseract_path": "/usr/bin/tesseract", "tessdata_dir": "/usr/share/tesseract-ocr/4.00/tessdata"}'` |
| `--output-dir <dir>`            | Set the output directory (default: current directory)                                   | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <name>`          | Set the output filename (without extension)                                             | `pdf2zh_next example.pdf --output-name translated`                                                                    |
| `--output-format <format>`      | Set the output format (pdf, json, txt, all; default: pdf)                               | `pdf2zh_next example.pdf --output-format all`                                                                         |
| `--output-options <options>`    | Set the output options (JSON string)                                                    | `pdf2zh_next example.pdf --output-options '{"pdf": {"compress": true}, "json": {"indent": 2}}'`                       |
| `--log-level <level>`           | Set the log level (debug, info, warning, error, critical; default: info)                | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file <file>`             | Set the log file (default: stdout)                                                      | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                        |
| `--config <file>`               | Set the config file (JSON or YAML)                                                      | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `--version`                     | Show the version                                                                        | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show the help message                                                                   | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION

| `--skip-clean`                  | Überspringe den PDF-Bereinigungsschritt                                                                 | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translation`            | Überspringe den Übersetzungsschritt                                                                     | `pdf2zh_next example.pdf --skip-translation`                                                                          |
| `--skip-ocr`                    | Überspringe den OCR-Schritt (wenn das Dokument Bilder enthält, wird OCR trotzdem durchgeführt)          | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-clean-format`           | Überspringe den PDF-Bereinigungs- und Formatierungsschritt                                              | `pdf2zh_next example.pdf --skip-clean-format`                                                                         |
| `--skip-extract`                | Überspringe den Textextraktionsschritt (erfordert, dass die Eingabe eine bereits extrahierte JSON-Datei ist) | `pdf2zh_next example.json --skip-extract`                                                                             |
| `--skip-reconstruction`         | Überspringe den Rekonstruktionsschritt (erfordert, dass die Eingabe eine bereits übersetzte JSON-Datei ist) | `pdf2zh_next example.json --skip-reconstruction`                                                                      |
| `--skip-save`                   | Überspringe den Speicherschritt (gibt nur an stdout aus)                                                | `pdf2zh_next example.pdf --skip-save`                                                                                 |
| `--translate-to <language>`     | Setze die Zielsprache für die Übersetzung (Standard: zh)                                                | `pdf2zh_next example.pdf --translate-to en`                                                                           |
| `--translate-service <service>` | Setze den Übersetzungsdienst (Standard: google)                                                         | `pdf2zh_next example.pdf --translate-service google`                                                                  |
| `--translate-options <options>` | Setze die Übersetzungsoptionen (JSON-String)                                                            | `pdf2zh_next example.pdf --translate-options '{"timeout": 10, "retries": 3}'`                                         |
| `--translate-key <key>`         | Setze den Übersetzungs-API-Schlüssel (falls erforderlich)                                               | `pdf2zh_next example.pdf --translate-key <your-api-key>`                                                              |
| `--ocr-language <language>`     | Setze die OCR-Sprache (Standard: eng)                                                                   | `pdf2zh_next example.pdf --ocr-language eng+chi_sim`                                                                  |
| `--ocr-options <options>`       | Setze die OCR-Optionen (JSON-String)                                                                    | `pdf2zh_next example.pdf --ocr-options '{"tesseract_path": "/usr/bin/tesseract", "tessdata_dir": "/usr/share/tesseract-ocr/4.00/tessdata"}'` |
| `--output-dir <dir>`            | Setze das Ausgabeverzeichnis (Standard: aktuelles Verzeichnis)                                          | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <name>`          | Setze den Ausgabedateinamen (ohne Erweiterung)                                                          | `pdf2zh_next example.pdf --output-name translated`                                                                    |
| `--output-format <format>`      | Setze das Ausgabeformat (pdf, json, txt, all; Standard: pdf)                                            | `pdf2zh_next example.pdf --output-format all`                                                                         |
| `--output-options <options>`    | Setze die Ausgabeoptionen (JSON-String)                                                                 | `pdf2zh_next example.pdf --output-options '{"pdf": {"compress": true}, "json": {"indent": 2}}'`                       |
| `--log-level <level>`           | Setze den Log-Level (debug, info, warning, error, critical; Standard: info)                             | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file <file>`             | Setze die Log-Datei (Standard: stdout)                                                                  | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                        |
| `--config <file>`               | Setze die Konfigurationsdatei (JSON oder YAML)                                                          | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `--version`                     | Zeige die Version                                                                                       | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Zeige die Hilfenachricht                                                                                | `pdf2zh_next --help`                                                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--dual-translate-second`       | Put translated pages second in dual PDF mode                                            | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `-o, --output`                  | Path to the output file, defaults to `{input_path}_translated.pdf`                      | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                   |
| `--output-pdf-options`          | Options for the output PDF, e.g., `--output-pdf-options="--no-pdf-compression"`         | `pdf2zh_next example.pdf --output-pdf-options="--no-pdf-compression"`                                                 |
| `--output-pdf-options-file`     | Path to a file containing options for the output PDF, one per line                      | `pdf2zh_next example.pdf --output-pdf-options-file=options.txt`                                                       |
| `--output-pdf-version`          | PDF version of the output file, e.g., `1.4`, `1.5`, defaults to `1.4`                   | `pdf2zh_next example.pdf --output-pdf-version=1.5`                                                                    |
| `--output-pdf-version-file`     | Path to a file containing the PDF version of the output file, e.g., `1.4`               | `pdf2zh_next example.pdf --output-pdf-version-file=version.txt`                                                       |
| `--output-pdf-version-override` | Override the PDF version of the output file, e.g., `1.4`, `1.5`, defaults to `1.4`      | `pdf2zh_next example.pdf --output-pdf-version-override=1.5`                                                           |
| `--output-pdf-version-override-file` | Path to a file containing the PDF version of the output file to override, e.g., `1.4` | `pdf2zh_next example.pdf --output-pdf-version-override-file=version.txt`                                              |

---

### OUTPUT

| `--dual-translate-first`        | Platziere übersetzte Seiten zuerst im dualen PDF-Modus                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--dual-translate-second`       | Platziere übersetzte Seiten an zweiter Stelle im dualen PDF-Modus                                            | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `-o, --output`                  | Pfad zur Ausgabedatei, Standardwert ist `{input_path}_translated.pdf`                      | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                   |
| `--output-pdf-options`          | Optionen für die Ausgabe-PDF, z.B. `--output-pdf-options="--no-pdf-compression"`         | `pdf2zh_next example.pdf --output-pdf-options="--no-pdf-compression"`                                                 |
| `--output-pdf-options-file`     | Pfad zu einer Datei mit Optionen für die Ausgabe-PDF, eine pro Zeile                      | `pdf2zh_next example.pdf --output-pdf-options-file=options.txt`                                                       |
| `--output-pdf-version`          | PDF-Version der Ausgabedatei, z.B. `1.4`, `1.5`, Standardwert ist `1.4`                   | `pdf2zh_next example.pdf --output-pdf-version=1.5`                                                                    |
| `--output-pdf-version-file`     | Pfad zu einer Datei mit der PDF-Version der Ausgabedatei, z.B. `1.4`               | `pdf2zh_next example.pdf --output-pdf-version-file=version.txt`                                                       |
| `--output-pdf-version-override` | Überschreibe die PDF-Version der Ausgabedatei, z.B. `1.4`, `1.5`, Standardwert ist `1.4`      | `pdf2zh_next example.pdf --output-pdf-version-override=1.5`                                                           |
| `--output-pdf-version-override-file` | Pfad zu einer Datei mit der PDF-Version der Ausgabedatei zum Überschreiben, z.B. `1.4` | `pdf2zh_next example.pdf --output-pdf-version-override-file=version.txt`                                              |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--disable-image-translate`     | Disable image translation                                                               | `pdf2zh_next example.pdf --disable-image-translate`                                                                   |
| `-o`, `--output`                | Specify output file path                                                                | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                  |
| `-d`, `--output-dir`            | Specify output directory                                                                | `pdf2zh_next example.pdf -d output/`                                                                                 |
| `-f`, `--force`                 | Force overwrite output file if it exists                                                | `pdf2zh_next example.pdf -f`                                                                                          |
| `-l`, `--target-language`       | Specify target language (default: zh)                                                  | `pdf2zh_next example.pdf -l en`                                                                                      |
| `-s`, `--service`               | Specify translation service (default: google)                                          | `pdf2zh_next example.pdf -s deepl`                                                                                    |
| `--api-key`                     | Specify API key for translation service (if required)                                    | `pdf2zh_next example.pdf -s deepl --api-key YOUR_DEEPL_API_KEY`                                                       |
| `--api-base-url`                | Specify API base URL for translation service (if required)                               | `pdf2zh_next example.pdf -s deepl --api-base-url https://api-free.deepl.com`                                          |
| `--api-region`                  | Specify API region for translation service (if required)                                 | `pdf2zh_next example.pdf -s azure --api-region eastus`                                                                |
| `--timeout`                     | Set timeout for translation requests in seconds (default: 10)                           | `pdf2zh_next example.pdf --timeout 30`                                                                               |
| `--retry`                       | Set number of retries for failed translation requests (default: 3)                       | `pdf2zh_next example.pdf --retry 5`                                                                                  |
| `--concurrency`                 | Set maximum number of concurrent translation requests (default: 10)                     | `pdf2zh_next example.pdf --concurrency 20`                                                                            |
| `--dry-run`                     | Perform a dry run without actually translating                                          | `pdf2zh_next example.pdf --dry-run`                                                                                  |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                  |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                              |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                 |

---

### ORIGINAL LANGUAGE

en

---

### TARGET LANGUAGE

de
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-ocr`   | Enable OCR compatibility enhancement                                                    | `pdf2zh_next example.pdf --enhance-compatibility-ocr`                                                                 |
| `--enhance-compatibility-math`  | Enable LaTeX math compatibility enhancement                                             | `pdf2zh_next example.pdf --enhance-compatibility-math`                                                                |
| `--enhance-compatibility-table` | Enable table compatibility enhancement                                                   | `pdf2zh_next example.pdf --enhance-compatibility-table`                                                               |
| `--enhance-compatibility-image` | Enable image compatibility enhancement                                                  | `pdf2zh_next example.pdf --enhance-compatibility-image`                                                               |
| `--enhance-compatibility-font`  | Enable font compatibility enhancement                                                   | `pdf2zh_next example.pdf --enhance-compatibility-font`                                                                |
| `--enhance-compatibility-color` | Enable color compatibility enhancement                                                  | `pdf2zh_next example.pdf --enhance-compatibility-color`                                                               |
| `--enhance-compatibility-link`  | Enable hyperlink compatibility enhancement                                              | `pdf2zh_next example.pdf --enhance-compatibility-link`                                                                |
| `--enhance-compatibility-list`  | Enable list compatibility enhancement                                                   | `pdf2zh_next example.pdf --enhance-compatibility-list`                                                                |
| `--enhance-compatibility-other` | Enable other compatibility enhancement options                                          | `pdf2zh_next example.pdf --enhance-compatibility-other`                                                               |
| `--enhance-compatibility-none`  | Disable all compatibility enhancement options                                           | `pdf2zh_next example.pdf --enhance-compatibility-none`                                                                |
| `--enhance-compatibility-all`   | Enable all compatibility enhancement options (same as `--enhance-compatibility`)        | `pdf2zh_next example.pdf --enhance-compatibility-all`                                                                 |

---

### TRANSLATION RESULT

| `--enhance-compatibility`       | Aktiviert alle Kompatibilitätsverbesserungsoptionen                                     | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-ocr`   | Aktiviert OCR-Kompatibilitätsverbesserung                                               | `pdf2zh_next example.pdf --enhance-compatibility-ocr`                                                                 |
| `--enhance-compatibility-math`  | Aktiviert LaTeX-Mathematik-Kompatibilitätsverbesserung                                  | `pdf2zh_next example.pdf --enhance-compatibility-math`                                                                |
| `--enhance-compatibility-table` | Aktiviert Tabellen-Kompatibilitätsverbesserung                                          | `pdf2zh_next example.pdf --enhance-compatibility-table`                                                               |
| `--enhance-compatibility-image` | Aktiviert Bild-Kompatibilitätsverbesserung                                              | `pdf2zh_next example.pdf --enhance-compatibility-image`                                                               |
| `--enhance-compatibility-font`  | Aktiviert Schriftart-Kompatibilitätsverbesserung                                        | `pdf2zh_next example.pdf --enhance-compatibility-font`                                                                |
| `--enhance-compatibility-color` | Aktiviert Farb-Kompatibilitätsverbesserung                                              | `pdf2zh_next example.pdf --enhance-compatibility-color`                                                               |
| `--enhance-compatibility-link`  | Aktiviert Hyperlink-Kompatibilitätsverbesserung                                         | `pdf2zh_next example.pdf --enhance-compatibility-link`                                                                |
| `--enhance-compatibility-list`  | Aktiviert Listen-Kompatibilitätsverbesserung                                            | `pdf2zh_next example.pdf --enhance-compatibility-list`                                                                |
| `--enhance-compatibility-other` | Aktiviert andere Kompatibilitätsverbesserungsoptionen                                   | `pdf2zh_next example.pdf --enhance-compatibility-other`                                                               |
| `--enhance-compatibility-none`  | Deaktiviert alle Kompatibilitätsverbesserungsoptionen                                   | `pdf2zh_next example.pdf --enhance-compatibility-none`                                                                |
| `--enhance-compatibility-all`   | Aktiviert alle Kompatibilitätsverbesserungsoptionen (gleich wie `--enhance-compatibility`) | `pdf2zh_next example.pdf --enhance-compatibility-all`                                                                 |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-split` | Use alternating pages mode for split PDF                                                | `pdf2zh_next example.pdf --use-alternating-pages-split`                                                               |
| `--use-paragraphs`              | Use paragraph mode (default)                                                            | `pdf2zh_next example.pdf --use-paragraphs`                                                                            |
| `--use-tables`                  | Use table mode                                                                          | `pdf2zh_next example.pdf --use-tables`                                                                                |
| `--use-tables-only`             | Use table mode only                                                                     | `pdf2zh_next example.pdf --use-tables-only`                                                                           |
| `--use-lines`                   | Use line mode                                                                           | `pdf2zh_next example.pdf --use-lines`                                                                                 |
| `--use-lines-only`              | Use line mode only                                                                      | `pdf2zh_next example.pdf --use-lines-only`                                                                            |
| `-d`, `--dictionary`            | Path to custom dictionary file                                                          | `pdf2zh_next example.pdf -d ./dictionary.txt`                                                                         |
| `-c`, `--config`                | Path to config file                                                                     | `pdf2zh_next example.pdf -c ./config.json`                                                                            |
| `-s`, `--source-lang`           | Source language code (default: "auto")                                                  | `pdf2zh_next example.pdf -s en`                                                                                       |
| `-t`, `--target-lang`           | Target language code (default: "zh")                                                    | `pdf2zh_next example.pdf -t ja`                                                                                       |
| `-f`, `--format`                | Output format, one of: "pdf", "docx", "txt", "markdown", "json" (default: "pdf")        | `pdf2zh_next example.pdf -f docx`                                                                                     |
| `-p`, `--provider`              | Translation provider, one of: "google", "openai", "azure", "deepl", "youdao", "baidu"   | `pdf2zh_next example.pdf -p openai`                                                                                   |
| `-k`, `--api-key`               | API key for translation provider                                                        | `pdf2zh_next example.pdf -p openai -k YOUR_OPENAI_API_KEY`                                                            |
| `-o`, `--output`                | Output file path                                                                        | `pdf2zh_next example.pdf -o ./output.pdf`                                                                             |
| `--threads`                     | Number of threads to use (default: 4)                                                   | `pdf2zh_next example.pdf --threads 8`                                                                                 |
| `--timeout`                     | Timeout for each translation request in seconds (default: 30)                           | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry`                       | Number of retries for failed translations (default: 3)                                  | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--batch-size`                  | Number of paragraphs to translate in each batch (default: 10)                           | `pdf2zh_next example.pdf --batch-size 20`                                                                             |
| `--dry-run`                     | Perform a dry run without actual translation                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Show help message                                                                       | `pdf2zh_next -h`                                                                                                      |

---

### OUTPUT

| `--use-alternating-pages-dual`  | Verwende den Wechselseitenmodus für doppelseitige PDFs                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| :------------------------------ | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-split` | Verwende den Wechselseitenmodus für geteilte PDFs                                                       | `pdf2zh_next example.pdf --use-alternating-pages-split`                                                               |
| `--use-paragraphs`              | Verwende den Absatzmodus (Standard)                                                                     | `pdf2zh_next example.pdf --use-paragraphs`                                                                            |
| `--use-tables`                  | Verwende den Tabellenmodus                                                                              | `pdf2zh_next example.pdf --use-tables`                                                                                |
| `--use-tables-only`             | Verwende nur den Tabellenmodus                                                                          | `pdf2zh_next example.pdf --use-tables-only`                                                                           |
| `--use-lines`                   | Verwende den Zeilenmodus                                                                                | `pdf2zh_next example.pdf --use-lines`                                                                                 |
| `--use-lines-only`              | Verwende nur den Zeilenmodus                                                                            | `pdf2zh_next example.pdf --use-lines-only`                                                                            |
| `-d`, `--dictionary`            | Pfad zur benutzerdefinierten Wörterbuchdatei                                                            | `pdf2zh_next example.pdf -d ./dictionary.txt`                                                                         |
| `-c`, `--config`                | Pfad zur Konfigurationsdatei                                                                            | `pdf2zh_next example.pdf -c ./config.json`                                                                            |
| `-s`, `--source-lang`           | Quellsprachcode (Standard: "auto")                                                                      | `pdf2zh_next example.pdf -s en`                                                                                       |
| `-t`, `--target-lang`           | Zielsprachcode (Standard: "zh")                                                                         | `pdf2zh_next example.pdf -t ja`                                                                                       |
| `-f`, `--format`                | Ausgabeformat, eines von: "pdf", "docx", "txt", "markdown", "json" (Standard: "pdf")                    | `pdf2zh_next example.pdf -f docx`                                                                                     |
| `-p`, `--provider`              | Übersetzungsanbieter, einer von: "google", "openai", "azure", "deepl", "youdao", "baidu"                | `pdf2zh_next example.pdf -p openai`                                                                                   |
| `-k`, `--api-key`               | API-Schlüssel für den Übersetzungsanbieter                                                              | `pdf2zh_next example.pdf -p openai -k YOUR_OPENAI_API_KEY`                                                            |
| `-o`, `--output`                | Ausgabedateipfad                                                                                        | `pdf2zh_next example.pdf -o ./output.pdf`                                                                             |
| `--threads`                     | Anzahl der zu verwendenden Threads (Standard: 4)                                                        | `pdf2zh_next example.pdf --threads 8`                                                                                 |
| `--timeout`                     | Timeout für jede Übersetzungsanfrage in Sekunden (Standard: 30)                                         | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry`                       | Anzahl der Wiederholungsversuche für fehlgeschlagene Übersetzungen (Standard: 3)                        | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--batch-size`                  | Anzahl der Absätze, die in jedem Batch übersetzt werden sollen (Standard: 10)                           | `pdf2zh_next example.pdf --batch-size 20`                                                                             |
| `--dry-run`                     | Führe einen Probelauf ohne tatsächliche Übersetzung durch                                               | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--verbose`                     | Aktiviere ausführliche Ausgabe                                                                          | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | Zeige Versionsinformationen                                                                             | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Zeige Hilfenachricht                                                                                    | `pdf2zh_next -h`                                                                                                      |
`no_watermark`, `watermark`, `only_watermark` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |

---

### RESPONSE

| `--watermark-output-mode`       | Wasserzeichen-Ausgabemodus für PDF-Dateien                                              | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `no_watermark`, `watermark`, `only_watermark` |
`50`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `--force-split`                 | Force split translation even if the PDF is small                                        | `pdf2zh_next example.pdf --force-split`                                                                               | `False`                                                          |
| `--no-split`                    | Disable split translation                                                               | `pdf2zh_next example.pdf --no-split`                                                                                  | `False`                                                          |
| `--max-characters-per-part`     | Maximum characters per part for split translation                                       | `pdf2zh_next example.pdf --max-characters-per-part 10000`                                                             | `10000`                                                          |
| `--max-tokens-per-part`         | Maximum tokens per part for split translation                                           | `pdf2zh_next example.pdf --max-tokens-per-part 2000`                                                                  | `2000`                                                           |
| `--min-tokens-per-part`         | Minimum tokens per part for split translation                                           | `pdf2zh_next example.pdf --min-tokens-per-part 500`                                                                   | `500`                                                            |
| `--split-on-headers`            | Split on headers                                                                        | `pdf2zh_next example.pdf --split-on-headers`                                                                          | `True`                                                           |
| `--split-on-figures`            | Split on figures                                                                        | `pdf2zh_next example.pdf --split-on-figures`                                                                         | `True`                                                           |
| `--split-on-tables`             | Split on tables                                                                         | `pdf2zh_next example.pdf --split-on-tables`                                                                          | `True`                                                           |
| `--split-on-equations`          | Split on equations                                                                      | `pdf2zh_next example.pdf --split-on-equations`                                                                       | `True`                                                           |
| `--split-on-lists`              | Split on lists                                                                          | `pdf2zh_next example.pdf --split-on-lists`                                                                           | `True`                                                           |
| `--split-on-paragraphs`         | Split on paragraphs                                                                     | `pdf2zh_next example.pdf --split-on-paragraphs`                                                                      | `True`                                                           |
| `--split-on-sentences`          | Split on sentences                                                                      | `pdf2zh_next example.pdf --split-on-sentences`                                                                       | `False`                                                          |
| `--split-on-words`              | Split on words                                                                          | `pdf2zh_next example.pdf --split-on-words`                                                                            | `False`                                                          |
| `--split-on-characters`         | Split on characters                                                                      | `pdf2zh_next example.pdf --split-on-characters`                                                                       | `False`                                                          |
| `--split-on-pages`              | Split on pages                                                                          | `pdf2zh_next example.pdf --split-on-pages`                                                                            | `False`                                                          |
| `--split-on-chapters`           | Split on chapters                                                                       | `pdf2zh_next example.pdf --split-on-chapters`                                                                         | `False`                                                          |
| `--split-on-sections`           | Split on sections                                                                       | `pdf2zh_next example.pdf --split-on-sections`                                                                        | `False`                                                          |
| `--split-on-sub-sections`       | Split on sub-sections                                                                   | `pdf2zh_next example.pdf --split-on-sub-sections`                                                                    | `False`                                                          |
| `--split-on-sub-sub-sections`   | Split on sub-sub-sections                                                               | `pdf2zh_next example.pdf --split-on-sub-sub-sections`                                                                 | `False`                                                          |
| `--split-on-sub-sub-sub-sections` | Split on sub-sub-sub-sections                                                         | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sections`                                                             | `False`                                                          |
| `--split-on-sub-sub-sub-sub-sections` | Split on sub-sub-sub-sub-sections                                                   | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sub-sections`                                                         | `False`                                                          |
| `--split-on-sub-sub-sub-sub-sub-sections` | Split on sub-sub-sub-sub-sub-sections                                             | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sub-sub-sections`                                                     | `False`                                                          |
| `--split-on-sub-sub-sub-sub-sub-sub-sections` | Split on sub-sub-sub-sub-sub-sub-sections                                       | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sub-sub-sub-sections`                                                 | `False`                                                          |

---

### TRANSLATED TEXT

| `--max-pages-per-part`          | Maximale Seiten pro Teil für geteilte Übersetzung                                       | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     | `50`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `--force-split`                 | Erzwinge geteilte Übersetzung auch wenn die PDF klein ist                               | `pdf2zh_next example.pdf --force-split`                                                                               | `False`                                                          |
| `--no-split`                    | Deaktiviere geteilte Übersetzung                                                        | `pdf2zh_next example.pdf --no-split`                                                                                  | `False`                                                          |
| `--max-characters-per-part`     | Maximale Zeichen pro Teil für geteilte Übersetzung                                      | `pdf2zh_next example.pdf --max-characters-per-part 10000`                                                             | `10000`                                                          |
| `--max-tokens-per-part`         | Maximale Tokens pro Teil für geteilte Übersetzung                                       | `pdf2zh_next example.pdf --max-tokens-per-part 2000`                                                                  | `2000`                                                           |
| `--min-tokens-per-part`         | Minimale Tokens pro Teil für geteilte Übersetzung                                       | `pdf2zh_next example.pdf --min-tokens-per-part 500`                                                                   | `500`                                                            |
| `--split-on-headers`            | Teile bei Überschriften                                                                 | `pdf2zh_next example.pdf --split-on-headers`                                                                          | `True`                                                           |
| `--split-on-figures`            | Teile bei Abbildungen                                                                   | `pdf2zh_next example.pdf --split-on-figures`                                                                         | `True`                                                           |
| `--split-on-tables`             | Teile bei Tabellen                                                                      | `pdf2zh_next example.pdf --split-on-tables`                                                                          | `True`                                                           |
| `--split-on-equations`          | Teile bei Gleichungen                                                                    | `pdf2zh_next example.pdf --split-on-equations`                                                                       | `True`                                                           |
| `--split-on-lists`              | Teile bei Listen                                                                        | `pdf2zh_next example.pdf --split-on-lists`                                                                           | `True`                                                           |
| `--split-on-paragraphs`         | Teile bei Absätzen                                                                      | `pdf2zh_next example.pdf --split-on-paragraphs`                                                                      | `True`                                                           |
| `--split-on-sentences`          | Teile bei Sätzen                                                                        | `pdf2zh_next example.pdf --split-on-sentences`                                                                       | `False`                                                          |
| `--split-on-words`              | Teile bei Wörtern                                                                       | `pdf2zh_next example.pdf --split-on-words`                                                                            | `False`                                                          |
| `--split-on-characters`         | Teile bei Zeichen                                                                       | `pdf2zh_next example.pdf --split-on-characters`                                                                       | `False`                                                          |
| `--split-on-pages`              | Teile bei Seiten                                                                        | `pdf2zh_next example.pdf --split-on-pages`                                                                            | `False`                                                          |
| `--split-on-chapters`           | Teile bei Kapiteln                                                                      | `pdf2zh_next example.pdf --split-on-chapters`                                                                         | `False`                                                          |
| `--split-on-sections`           | Teile bei Abschnitten                                                                   | `pdf2zh_next example.pdf --split-on-sections`                                                                        | `False`                                                          |
| `--split-on-sub-sections`       | Teile bei Unterabschnitten                                                              | `pdf2zh_next example.pdf --split-on-sub-sections`                                                                    | `False`                                                          |
| `--split-on-sub-sub-sections`   | Teile bei Unter-Unterabschnitten                                                        | `pdf2zh_next example.pdf --split-on-sub-sub-sections`                                                                 | `False`                                                          |
| `--split-on-sub-sub-sub-sections` | Teile bei Unter-Unter-Unterabschnitten                                                | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sections`                                                             | `False`                                                          |
| `--split-on-sub-sub-sub-sub-sections` | Teile bei Unter-Unter-Unter-Unterabschnitten                                      | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sub-sections`                                                         | `False`                                                          |
| `--split-on-sub-sub-sub-sub-sub-sections` | Teile bei Unter-Unter-Unter-Unter-Unterabschnitten                            | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sub-sub-sections`                                                     | `False`                                                          |
| `--split-on-sub-sub-sub-sub-sub-sub-sections` | Teile bei Unter-Unter-Unter-Unter-Unter-Unterabschnitten                  | `pdf2zh_next example.pdf --split-on-sub-sub-sub-sub-sub-sub-sections`                                                 | `False`                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | How to translate table text, `inner` or `markdown` (experimental)                       | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method markdown`                               |
| `--translate-table-text-delimiter` | Delimiter used to separate table cells when using the `markdown` method (experimental)  | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method markdown --translate-table-text-delimiter "\\|"` |

---

### TRANSLATION RESULT

| `--translate-table-text`        | Tabellentext übersetzen (experimentell)                                                 | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Methode zum Übersetzen von Tabellentext, `inner` oder `markdown` (experimentell)        | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method markdown`                               |
| `--translate-table-text-delimiter` | Trennzeichen zur Trennung von Tabellenzellen bei Verwendung der `markdown`-Methode (experimentell) | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method markdown --translate-table-text-delimiter "\\|"` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection=true` | Skip scanned detection, same as above                                                   | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                                |
| `--skip-scanned-detection=auto` | Automatically determine if the PDF is a scanned document, and skip if it is a scan      | `pdf2zh_next example.pdf --skip-scanned-detection=auto`                                                                |
| `--skip-scanned-detection=skip` | Skip scanned detection, same as `true`                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=skip`                                                                |
| `--skip-scanned-detection=force`| Force to skip scanned detection, even if the PDF is determined to be a scanned document | `pdf2zh_next example.pdf --skip-scanned-detection=force`                                                               |

---

### TRANSLATION RESULT

| `--skip-scanned-detection`      | Überspringe die Erkennung gescannter Dokumente                                                                 | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection=true` | Überspringe die Erkennung gescannter Dokumente, identisch zur obigen Option                                    | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                                |
| `--skip-scanned-detection=auto` | Automatische Erkennung, ob das PDF ein gescanntes Dokument ist, und Überspringen, wenn es sich um einen Scan handelt | `pdf2zh_next example.pdf --skip-scanned-detection=auto`                                                                |
| `--skip-scanned-detection=skip` | Überspringe die Erkennung gescannter Dokumente, identisch zu `true`                                            | `pdf2zh_next example.pdf --skip-scanned-detection=skip`                                                                |
| `--skip-scanned-detection=force`| Erzwinge das Überspringen der Erkennung gescannter Dokumente, auch wenn das PDF als gescanntes Dokument erkannt wurde | `pdf2zh_next example.pdf --skip-scanned-detection=force`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-font-size`    | Font size for OCR workaround (default: 16)                                              | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-size 20`                                              |
| `--ocr-workaround-font-family`  | Font family for OCR workaround (default: "SimHei")                                      | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-family "Arial"`                                       |
| `--ocr-workaround-font-color`   | Font color for OCR workaround (default: "black")                                        | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-color "white"`                                        |
| `--ocr-workaround-background`   | Background color for OCR workaround (default: "white")                                  | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-background "black"`                                        |
| `--ocr-workaround-line-spacing` | Line spacing for OCR workaround (default: 1.5)                                          | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-line-spacing 2.0`                                          |
| `--ocr-workaround-font-weight`  | Font weight for OCR workaround (default: "normal")                                      | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-weight "bold"`                                        |
| `--ocr-workaround-font-style`   | Font style for OCR workaround (default: "normal")                                       | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-style "italic"`                                       |
| `--ocr-workaround-font-stretch` | Font stretch for OCR workaround (default: "normal")                                     | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-stretch "condensed"`                                  |
| `--ocr-workaround-font-variant` | Font variant for OCR workaround (default: "normal")                                     | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-variant "small-caps"`                                 |

---

### TRANSLATION RESULT

| `--ocr-workaround`              | Erzwingt, dass übersetzter Text schwarz ist und fügt weißen Hintergrund hinzu           | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-font-size`    | Schriftgröße für OCR-Workaround (Standard: 16)                                          | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-size 20`                                              |
| `--ocr-workaround-font-family`  | Schriftfamilie für OCR-Workaround (Standard: "SimHei")                                  | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-family "Arial"`                                       |
| `--ocr-workaround-font-color`   | Schriftfarbe für OCR-Workaround (Standard: "black")                                     | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-color "white"`                                        |
| `--ocr-workaround-background`   | Hintergrundfarbe für OCR-Workaround (Standard: "white")                                 | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-background "black"`                                        |
| `--ocr-workaround-line-spacing` | Zeilenabstand für OCR-Workaround (Standard: 1.5)                                        | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-line-spacing 2.0`                                          |
| `--ocr-workaround-font-weight`  | Schriftgewicht für OCR-Workaround (Standard: "normal")                                  | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-weight "bold"`                                        |
| `--ocr-workaround-font-style`   | Schriftstil für OCR-Workaround (Standard: "normal")                                     | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-style "italic"`                                       |
| `--ocr-workaround-font-stretch` | Schriftdehnung für OCR-Workaround (Standard: "normal")                                  | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-stretch "condensed"`                                  |
| `--ocr-workaround-font-variant` | Schriftvariante für OCR-Workaround (Standard: "normal")                                 | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-font-variant "small-caps"`                                 |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------| 
| `--progress`                    | Display progress bar. (default: True)                                                                                                   | `pdf2zh_next example.pdf --progress False`                                 | 

---

### OUTPUT

| `--auto-enable-ocr-workaround`  | Aktiviert die automatische OCR-Workaround. Wenn ein Dokument als stark gescannt erkannt wird, versucht dies, die OCR-Verarbeitung zu aktivieren und weitere Scan-Erkennung zu überspringen. Weitere Details finden Sie in der Dokumentation. (Standard: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     | 
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------| 
| `--progress`                    | Zeigt die Fortschrittsleiste an. (Standard: True)                                                                                                                                              | `pdf2zh_next example.pdf --progress False`                                 |
| ------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `--no-ocr`                      | Disable OCR for the entire PDF.                                                       | `pdf2zh_next example.pdf --no-ocr`                                                                                   |
| `--ocr-whole-page`              | Enable OCR for the entire page (use with caution, may introduce noise).               | `pdf2zh_next example.pdf --ocr-whole-page`                                                                           |
| `--ocr-lang`                    | Specify the OCR language for the entire PDF.                                          | `pdf2zh_next example.pdf --ocr-lang jpn_vert`                                                                        |
| `--ocr-timeout`                 | Set the timeout for OCR processing in seconds.                                        | `pdf2zh_next example.pdf --ocr-timeout 120`                                                                          |
| `--ocr-skip-text`               | Skip OCR for text that already exists in the PDF.                                     | `pdf2zh_next example.pdf --ocr-skip-text`                                                                            |
| `--ocr-engine`                  | Choose the OCR engine to use. Options: `easyocr`, `tesseract`.                        | `pdf2zh_next example.pdf --ocr-engine tesseract`                                                                     |
| `--ocr-dpi`                     | Set the DPI for OCR processing.                                                       | `pdf2zh_next example.pdf --ocr-dpi 300`                                                                              |
| `--ocr-max-workers`             | Set the maximum number of workers for OCR.                                            | `pdf2zh_next example.pdf --ocr-max-workers 4`                                                                        |
| `--ocr-retry`                   | Number of retries for OCR.                                                            | `pdf2zh_next example.pdf --ocr-retry 3`                                                                              |

---

### TRANSLATED TEXT

| `--only-include-translated-page` | Nur übersetzte Seiten in der Ausgabe-PDF einbeziehen. Nur wirksam, wenn --pages verwendet wird. | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page` |
| ------------------------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `--no-ocr`                      | OCR für die gesamte PDF deaktivieren.                                                           | `pdf2zh_next example.pdf --no-ocr`                                   |
| `--ocr-whole-page`              | OCR für die gesamte Seite aktivieren (mit Vorsicht verwenden, kann Rauschen verursachen).       | `pdf2zh_next example.pdf --ocr-whole-page`                           |
| `--ocr-lang`                    | Die OCR-Sprache für die gesamte PDF angeben.                                                    | `pdf2zh_next example.pdf --ocr-lang jpn_vert`                        |
| `--ocr-timeout`                 | Timeout für die OCR-Verarbeitung in Sekunden festlegen.                                         | `pdf2zh_next example.pdf --ocr-timeout 120`                          |
| `--ocr-skip-text`               | OCR für Text überspringen, der bereits in der PDF vorhanden ist.                                | `pdf2zh_next example.pdf --ocr-skip-text`                            |
| `--ocr-engine`                  | Den zu verwendenden OCR-Engine auswählen. Optionen: `easyocr`, `tesseract`.                     | `pdf2zh_next example.pdf --ocr-engine tesseract`                     |
| `--ocr-dpi`                     | DPI für die OCR-Verarbeitung festlegen.                                                         | `pdf2zh_next example.pdf --ocr-dpi 300`                              |
| `--ocr-max-workers`             | Maximale Anzahl von Workern für OCR festlegen.                                                  | `pdf2zh_next example.pdf --ocr-max-workers 4`                        |
| `--ocr-retry`                   | Anzahl der Wiederholungsversuche für OCR.                                                       | `pdf2zh_next example.pdf --ocr-retry 3`                              |
| :------------------------------------ | :--------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `--no-merge-alternating-text`         | Disable merging of alternating text and image paragraphs                                        | `pdf2zh_next example.pdf --no-merge-alternating-text`                                                       |
| `--no-merge-alternating-text-images`  | Disable merging of alternating text and image paragraphs                                        | `pdf2zh_next example.pdf --no-merge-alternating-text-images`                                                 |
| `--no-merge-alternating-text-pattern` | Disable merging of alternating text and image paragraphs based on pattern matching              | `pdf2zh_next example.pdf --no-merge-alternating-text-pattern`                                                |

---

### TRANSLATION RESULT

| `--no-merge-alternating-line-numbers` | Deaktiviert das Zusammenführen von abwechselnden Zeilennummern und Textabsätzen in Dokumenten mit Zeilennummern | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `--no-merge-alternating-text`         | Deaktiviert das Zusammenführen von abwechselnden Text- und Bildabsätzen                                         | `pdf2zh_next example.pdf --no-merge-alternating-text`                                                       |
| `--no-merge-alternating-text-images`  | Deaktiviert das Zusammenführen von abwechselnden Text- und Bildabsätzen                                         | `pdf2zh_next example.pdf --no-merge-alternating-text-images`                                                 |
| `--no-merge-alternating-text-pattern` | Deaktiviert das Zusammenführen von abwechselnden Text- und Bildabsätzen basierend auf Mustervergleich           | `pdf2zh_next example.pdf --no-merge-alternating-text-pattern`                                                |
| -------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-formula-lines`  | Deaktiviert das Entfernen von Nicht-Formel-Zeilen innerhalb von Absatzbereichen         | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |

---

### OUTPUT

| `--no-remove-non-formula-lines` | Deaktiviert das Entfernen von Nicht-Formel-Zeilen innerhalb von Absatzbereichen         | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
`0.8`     |
| `--formula-line-iou-threshold`     | Set IoU threshold for identifying formula lines (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                           | `0.8`     |
| `--table-line-iou-threshold`       | Set IoU threshold for identifying table lines (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                             | `0.8`     |
| `--line-merge-threshold`           | Set threshold for merging lines (0.0-1.0)                                          | `pdf2zh_next example.pdf --line-merge-threshold 0.85`                                                                 | `0.8`     |
| `--table-merge-threshold`          | Set threshold for merging tables (0.0-1.0)                                         | `pdf2zh_next example.pdf --table-merge-threshold 0.85`                                                                | `0.8`     |

---

### TRANSLATED TEXT

| `--non-formula-line-iou-threshold` | Setze IoU-Schwellenwert für die Identifizierung von Nicht-Formel-Zeilen (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.8`     |
| `--formula-line-iou-threshold`     | Setze IoU-Schwellenwert für die Identifizierung von Formel-Zeilen (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                           | `0.8`     |
| `--table-line-iou-threshold`       | Setze IoU-Schwellenwert für die Identifizierung von Tabellen-Zeilen (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                             | `0.8`     |
| `--line-merge-threshold`           | Setze Schwellenwert für das Zusammenführen von Zeilen (0.0-1.0)                                          | `pdf2zh_next example.pdf --line-merge-threshold 0.85`                                                                 | `0.8`     |
| `--table-merge-threshold`          | Setze Schwellenwert für das Zusammenführen von Tabellen (0.0-1.0)                                         | `pdf2zh_next example.pdf --table-merge-threshold 0.85`                                                                | `0.8`     |
`0.9`  |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |

---

### TRANSLATED TEXT

| `--figure-table-protection-threshold` | Legt den Schutzschwellenwert für Abbildungen und Tabellen fest (0.0-1.0). Linien innerhalb von Abbildungen/Tabellen werden nicht verarbeitet | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95` | `0.9` |
---

### OUTPUT

| `--skip-formula-offset-calculation` | Überspringt die Berechnung des Formel-Offsets während der Verarbeitung          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### GUI-Argumente

| `--port`                        | Specify the port number                | `pdf2zh_next --gui --port 8080`                 |
| `--host`                        | Specify the host address               | `pdf2zh_next --gui --host 127.0.0.1`            |
| `--gui`                         | Launch the WebUI                       | `pdf2zh_next --gui`                             |
| `--help`                        | Display help information               | `pdf2zh_next --help`                            |
| `--version`                     | Display version information            | `pdf2zh_next --version`                         |
| `--input-file <PATH>`           | Specify the input file path            | `pdf2zh_next --input-file ./example.pdf`        |
| `--output-file <PATH>`          | Specify the output file path           | `pdf2zh_next --output-file ./output.pdf`        |
| `--source-lang <LANG>`          | Specify the source language            | `pdf2zh_next --source-lang en`                  |
| `--target-lang <LANG>`          | Specify the target language            | `pdf2zh_next --target-lang zh`                  |
| `--translator <TYPE>`           | Specify the translator                 | `pdf2zh_next --translator google`               |
| `--api-key <KEY>`               | Specify the API key                    | `pdf2zh_next --api-key YOUR_API_KEY`            |
| `--proxy <PROXY_URL>`           | Specify the proxy server               | `pdf2zh_next --proxy http://127.0.0.1:10809`    |
| `--concurrency-limit <NUM>`     | Specify the concurrency limit          | `pdf2zh_next --concurrency-limit 5`             |
| `--request-interval <SECONDS>`  | Specify the request interval           | `pdf2zh_next --request-interval 0.5`            |
| `--check`                       | Check the installation status          | `pdf2zh_next --check`                           |
| `--math-inline-method <METHOD>` | Specify the inline math method         | `pdf2zh_next --math-inline-method hybrid`       |
| `--math-equation-method <METHOD>` | Specify the equation math method       | `pdf2zh_next --math-equation-method remove`     |
| `--no-cache`                    | Disable caching                        | `pdf2zh_next --no-cache`                        |
| `--cache-dir <PATH>`            | Specify the cache directory            | `pdf2zh_next --cache-dir ./cache`               |
| `--force`                       | Force overwrite existing output file   | `pdf2zh_next --force`                           |
| `--ignore-error`                | Ignore errors and continue processing  | `pdf2zh_next --ignore-error`                    |
| `--debug`                       | Enable debug mode                      | `pdf2zh_next --debug`                           |

---

### TRANSLATED TEXT

| Option                          | Funktion                              | Beispiel                                        |
| ------------------------------- | ------------------------------------- | ----------------------------------------------- |
| `--share`                       | Freigabemodus aktivieren              | `pdf2zh_next --gui --share`                     |
| `--port`                        | Portnummer angeben                    | `pdf2zh_next --gui --port 8080`                 |
| `--host`                        | Host-Adresse angeben                  | `pdf2zh_next --gui --host 127.0.0.1`            |
| `--gui`                         | WebUI starten                         | `pdf2zh_next --gui`                             |
| `--help`                        | Hilfsinformationen anzeigen           | `pdf2zh_next --help`                            |
| `--version`                     | Versionsinformationen anzeigen        | `pdf2zh_next --version`                         |
| `--input-file <PATH>`           | Eingabedateipfad angeben              | `pdf2zh_next --input-file ./example.pdf`        |
| `--output-file <PATH>`          | Ausgabedateipfad angeben              | `pdf2zh_next --output-file ./output.pdf`        |
| `--source-lang <LANG>`          | Quellsprache angeben                  | `pdf2zh_next --source-lang en`                  |
| `--target-lang <LANG>`          | Zielsprache angeben                   | `pdf2zh_next --target-lang zh`                  |
| `--translator <TYPE>`           | Übersetzer angeben                    | `pdf2zh_next --translator google`               |
| `--api-key <KEY>`               | API-Schlüssel angeben                 | `pdf2zh_next --api-key YOUR_API_KEY`            |
| `--proxy <PROXY_URL>`           | Proxy-Server angeben                  | `pdf2zh_next --proxy http://127.0.0.1:10809`    |
| `--concurrency-limit <NUM>`     | Nebenläufigkeitslimit angeben         | `pdf2zh_next --concurrency-limit 5`             |
| `--request-interval <SECONDS>`  | Anforderungsintervall angeben         | `pdf2zh_next --request-interval 0.5`            |
| `--check`                       | Installationsstatus überprüfen        | `pdf2zh_next --check`                           |
| `--math-inline-method <METHOD>` | Inline-Mathematik-Methode angeben     | `pdf2zh_next --math-inline-method hybrid`       |
| `--math-equation-method <METHOD>` | Gleichungs-Mathematik-Methode angeben | `pdf2zh_next --math-equation-method remove`     |
| `--no-cache`                    | Caching deaktivieren                  | `pdf2zh_next --no-cache`                        |
| `--cache-dir <PATH>`            | Cache-Verzeichnis angeben             | `pdf2zh_next --cache-dir ./cache`               |
| `--force`                       | Vorhandene Ausgabedatei überschreiben | `pdf2zh_next --force`                           |
| `--ignore-error`                | Fehler ignorieren und fortfahren      | `pdf2zh_next --ignore-error`                    |
| `--debug`                       | Debug-Modus aktivieren                | `pdf2zh_next --debug`                           |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--auth-service`                | Service name for authentication        | `pdf2zh_next --gui --auth-service myservice`    |

!!! note "Note"

    If `--auth-file` is specified, the `--auth-service` option is ignored.

---

### TRANSLATED TEXT

| `--auth-file`                   | Pfad zur Authentifizierungsdatei       | `pdf2zh_next --gui --auth-file /path`           |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--auth-service`                | Dienstname für die Authentifizierung   | `pdf2zh_next --gui --auth-service myservice`    |

!!! note "Hinweis"

    Wenn `--auth-file` angegeben ist, wird die Option `--auth-service` ignoriert.
Show the welcome page at the specified path. |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | -------------------------------------------- |

---

### OUTPUT

| `--welcome-page`                | Pfad zur Willkommens-HTML-Datei        | `pdf2zh_next --gui --welcome-page /path`        | Zeigt die Willkommensseite am angegebenen Pfad an. |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | -------------------------------------------- |
Enable Bing and OpenAI translation services only.                     |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Google"`     | Disable Google translation service.                                   |
| `--language`                    | Language code of the target language   | `pdf2zh_next --gui --language "de"`                  | Set the target language to German.                                    |
| `--translate-format`            | Translate content format               | `pdf2zh_next --gui --translate-format "text"`        | Translate only the text content.                                      |
| `--translate-tags`              | Translate specific tags                | `pdf2zh_next --gui --translate-tags "p,span,div"`    | Translate content within `<p>`, `<span>`, and `<div>` tags.           |
| `--exclude-tags`                | Exclude specific tags                  | `pdf2zh_next --gui --exclude-tags "code,pre"`        | Exclude content within `<code>` and `<pre>` tags from translation.    |
| `--translator-args`             | Additional arguments for the translator | `pdf2zh_next --gui --translator-args '{"api_key": "your_api_key"}'` | Pass additional arguments (e.g., API key) to the translator.          |
| `--concurrency-limit`           | Maximum number of concurrent requests  | `pdf2zh_next --gui --concurrency-limit 10`           | Set the maximum number of concurrent translation requests to 10.     |
| `--request-timeout`             | Timeout for each translation request   | `pdf2zh_next --gui --request-timeout 30`             | Set the timeout for each translation request to 30 seconds.          |
| `--request-interval`            | Interval between translation requests  | `pdf2zh_next --gui --request-interval 1`             | Set the interval between translation requests to 1 second.            |
| `--max-characters`              | Maximum characters per request         | `pdf2zh_next --gui --max-characters 5000`            | Limit each translation request to 5000 characters.                     |
| `--glossary`                    | Glossary file for translation          | `pdf2zh_next --gui --glossary "glossary.txt"`        | Use a glossary file to ensure consistent translation of specific terms. |
| `--html`                        | Output format as HTML                  | `pdf2zh_next --gui --html`                           | Output the translated content in HTML format.                         |
| `--markdown`                    | Output format as Markdown              | `pdf2zh_next --gui --markdown`                       | Output the translated content in Markdown format.                     |
| `--output`                      | Output file path                       | `pdf2zh_next --gui --output "output.pdf"`             | Specify the output file path.                                         |
| `--config`                      | Configuration file path                 | `pdf2zh_next --gui --config "config.json"`           | Use a configuration file to set multiple options.                      |
| `--help`                        | Show help message                      | `pdf2zh_next --gui --help`                           | Display the help message for the GUI command.                         |

---

### OUTPUT

| `--enabled-services`            | Aktivierte Übersetzungsdienste         | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | Aktivieren Sie nur die Bing- und OpenAI-Übersetzungsdienste.          |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- |
| `--disabled-services`           | Deaktivierte Übersetzungsdienste       | `pdf2zh_next --gui --disabled-services "Google"`     | Deaktivieren Sie den Google-Übersetzungsdienst.                       |
| `--language`                    | Sprachcode der Zielsprache            | `pdf2zh_next --gui --language "de"`                  | Setzen Sie die Zielsprache auf Deutsch.                               |
| `--translate-format`            | Zu übersetzendes Inhaltsformat         | `pdf2zh_next --gui --translate-format "text"`        | Übersetzen Sie nur den Textinhalt.                                    |
| `--translate-tags`              | Bestimmte Tags übersetzen              | `pdf2zh_next --gui --translate-tags "p,span,div"`    | Übersetzen Sie Inhalte innerhalb von `<p>`, `<span>` und `<div>` Tags. |
| `--exclude-tags`                | Bestimmte Tags ausschließen            | `pdf2zh_next --gui --exclude-tags "code,pre"`        | Schließen Sie Inhalte innerhalb von `<code>` und `<pre>` Tags von der Übersetzung aus. |
| `--translator-args`             | Zusätzliche Argumente für den Übersetzer | `pdf2zh_next --gui --translator-args '{"api_key": "your_api_key"}'` | Übergeben Sie zusätzliche Argumente (z. B. API-Schlüssel) an den Übersetzer. |
| `--concurrency-limit`           | Maximale Anzahl gleichzeitiger Anfragen | `pdf2zh_next --gui --concurrency-limit 10`           | Setzen Sie die maximale Anzahl gleichzeitiger Übersetzungsanfragen auf 10. |
| `--request-timeout`             | Timeout für jede Übersetzungsanfrage   | `pdf2zh_next --gui --request-timeout 30`             | Setzen Sie das Timeout für jede Übersetzungsanfrage auf 30 Sekunden.  |
| `--request-interval`            | Intervall zwischen Übersetzungsanfragen | `pdf2zh_next --gui --request-interval 1`             | Setzen Sie das Intervall zwischen Übersetzungsanfragen auf 1 Sekunde. |
| `--max-characters`              | Maximale Zeichen pro Anfrage           | `pdf2zh_next --gui --max-characters 5000`            | Begrenzen Sie jede Übersetzungsanfrage auf 5000 Zeichen.              |
| `--glossary`                    | Glossardatei für die Übersetzung       | `pdf2zh_next --gui --glossary "glossary.txt"`        | Verwenden Sie eine Glossardatei, um eine konsistente Übersetzung bestimmter Begriffe sicherzustellen. |
| `--html`                        | Ausgabeformat als HTML                 | `pdf2zh_next --gui --html`                           | Geben Sie den übersetzten Inhalt im HTML-Format aus.                  |
| `--markdown`                    | Ausgabeformat als Markdown             | `pdf2zh_next --gui --markdown`                       | Geben Sie den übersetzten Inhalt im Markdown-Format aus.              |
| `--output`                      | Ausgabedateipfad                       | `pdf2zh_next --gui --output "output.pdf"`             | Geben Sie den Ausgabedateipfad an.                                    |
| `--config`                      | Konfigurationsdateipfad                 | `pdf2zh_next --gui --config "config.json"`           | Verwenden Sie eine Konfigurationsdatei, um mehrere Optionen festzulegen. |
| `--help`                        | Hilfenachricht anzeigen                 | `pdf2zh_next --gui --help`                           | Zeigen Sie die Hilfenachricht für den GUI-Befehl an.                 |

|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--config-file <path>`          | Use a custom configuration file        | `pdf2zh_next --gui --config-file ./config.json` | 
| `--debug`                       | Enable debug mode                      | `pdf2zh_next --gui --debug`                     | 
| `--disable-gpu`                 | Disable GPU acceleration               | `pdf2zh_next --gui --disable-gpu`               | 
| `--disable-web-security`        | Disable web security (for development) | `pdf2zh_next --gui --disable-web-security`      | 

---

### TRANSLATION RESULT

| `--disable-config-auto-save`    | Automatisches Speichern der Konfiguration deaktivieren | `pdf2zh_next --gui --disable-config-auto-save`  | 
|---------------------------------|--------------------------------------------------------|-------------------------------------------------|
| `--config-file <path>`          | Benutzerdefinierte Konfigurationsdatei verwenden       | `pdf2zh_next --gui --config-file ./config.json` | 
| `--debug`                       | Debug-Modus aktivieren                                 | `pdf2zh_next --gui --debug`                     | 
| `--disable-gpu`                 | GPU-Beschleunigung deaktivieren                        | `pdf2zh_next --gui --disable-gpu`               | 
| `--disable-web-security`        | Web-Sicherheit deaktivieren (für Entwicklung)          | `pdf2zh_next --gui --disable-web-security`      |
`7860`                            |

---

### TRANSLATION RESULT

| `--server-port`                 | WebUI Port                             | `pdf2zh_next --gui --server-port 7860`          | `7860`                            |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--src-lang`                    | Source language                        | `pdf2zh_next --src-lang en`                     |
| `--dst-lang`                    | Target language                        | `pdf2zh_next --dst-lang zh`                     |
| `--translator`                  | Translator service                     | `pdf2zh_next --translator google`               |
| `--translator-config`           | Translator configuration               | `pdf2zh_next --translator-config '{"key": ""}'` |
| `--translator-config-file`      | Translator configuration file          | `pdf2zh_next --translator-config-file config.json` |
| `--translator-config-file-type` | Translator configuration file type     | `pdf2zh_next --translator-config-file-type json` |

---

### TRANSLATION RESULT

| `--ui-lang`                     | UI-Sprache                             | `pdf2zh_next --gui --ui-lang zh`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--src-lang`                    | Quellsprache                           | `pdf2zh_next --src-lang en`                     |
| `--dst-lang`                    | Zielsprache                            | `pdf2zh_next --dst-lang zh`                     |
| `--translator`                  | Übersetzungsdienst                     | `pdf2zh_next --translator google`               |
| `--translator-config`           | Übersetzerkonfiguration                | `pdf2zh_next --translator-config '{"key": ""}'` |
| `--translator-config-file`      | Übersetzerkonfigurationsdatei          | `pdf2zh_next --translator-config-file config.json` |
| `--translator-config-file-type` | Übersetzerkonfigurationsdateityp       | `pdf2zh_next --translator-config-file-type json` |

[⬆️ Zurück zum Anfang](#toc)

---

#### Anleitung zur Ratenbegrenzungskonfiguration

Bei der Verwendung von Übersetzungsdiensten ist eine korrekte Ratenbegrenzungskonfiguration entscheidend, um API-Fehler zu vermeiden und die Leistung zu optimieren. Diese Anleitung erklärt, wie die Parameter `--qps` und `--pool-max-worker` basierend auf den verschiedenen Einschränkungen des Upstream-Dienstes konfiguriert werden.

> [!TIP]
>
> Es wird empfohlen, dass die pool_size 1000 nicht überschreitet. Wenn die nach folgender Methode berechnete pool_size 1000 überschreitet, verwenden Sie bitte 1000.

##### RPM (Anfragen pro Minute) Ratenbegrenzung

Wenn der Upstream-Dienst RPM-Beschränkungen hat, verwenden Sie die folgende Berechnung:

**Berechnungsformel:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Der Faktor 10 ist ein empirischer Koeffizient, der in den meisten Szenarien gut funktioniert.

**Beispiel:**
Wenn Ihr Übersetzungsdienst eine Begrenzung von 600 RPM hat:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Begrenzung gleichzeitiger Verbindungen

Wenn der Upstream-Dienst Einschränkungen bei gleichzeitigen Verbindungen hat (wie der offizielle GLM-Dienst), verwenden Sie diesen Ansatz:

**Berechnungsformel:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Beispiel:**
Wenn Ihr Übersetzungsdienst 50 gleichzeitige Verbindungen zulässt:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Best Practices

> [!TIP]
> - Beginnen Sie immer mit konservativen Werten und erhöhen Sie diese schrittweise, falls erforderlich
> - Überwachen Sie die Antwortzeiten und Fehlerraten Ihres Dienstes
> - Unterschiedliche Dienste können unterschiedliche Optimierungsstrategien erfordern
> - Berücksichtigen Sie Ihren spezifischen Anwendungsfall und die Dokumentgröße bei der Festlegung dieser Parameter


[⬆️ Zurück zum Anfang](#toc)

---

#### Teilweise Übersetzung

Verwenden Sie den `--pages`-Parameter, um einen Teil eines Dokuments zu übersetzen.

- Wenn die Seitenzahlen aufeinanderfolgend sind, können Sie es so schreiben:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` schließt alle Seiten ab Seite 25 ein. Wenn Ihr Dokument 100 Seiten hat, entspricht dies `25-100`.
> 
> Ebenso schließt `-25` alle Seiten vor Seite 25 ein, was `1-25` entspricht.

- Wenn die Seiten nicht aufeinanderfolgend sind, können Sie ein Komma `,` verwenden, um sie zu trennen.

Zum Beispiel, wenn Sie die erste und dritte Seite übersetzen möchten, können Sie den folgenden Befehl verwenden:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Wenn die Seiten sowohl aufeinanderfolgende als auch nicht aufeinanderfolgende Bereiche enthalten, können Sie diese auch mit einem Komma verbinden, wie folgt:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Dieser Befehl übersetzt die erste Seite, die dritte Seite, die Seiten 10-20 und alle Seiten von 25 bis zum Ende.

[⬆️ Zurück zum Anfang](#toc)

---

#### Quell- und Zielsprachen angeben

Siehe [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Übersetzen mit Ausnahmen

Verwenden Sie reguläre Ausdrücke, um Formelschriften und Zeichen anzugeben, die erhalten bleiben sollen:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Standardmäßig werden `Latex`, `Mono`, `Code`, `Italic`, `Symbol` und `Math` Schriftarten beibehalten:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Benutzerdefinierte Eingabeaufforderung

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Benutzerdefinierte Systemeingabeaufforderung für die Übersetzung. Sie wird hauptsächlich verwendet, um die '/no_think'-Anweisung von Qwen 3 in die Eingabeaufforderung einzufügen.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Benutzerdefinierte Konfiguration

Es gibt mehrere Möglichkeiten, die Konfigurationsdatei zu ändern und zu importieren.

> [!NOTE]
> **Konfigurationsdatei-Hierarchie**
>
> Wenn derselbe Parameter mit verschiedenen Methoden geändert wird, wendet die Software die Änderungen gemäß der folgenden Prioritätsreihenfolge an.
>
> Höherrangige Änderungen überschreiben niedrigerrangige.
>
> **cli/gui > env > Benutzerkonfigurationsdatei > Standardkonfigurationsdatei**

- Konfiguration über **Kommandozeilen-Argumente** ändern

In den meisten Fällen können Sie Ihre gewünschten Einstellungen direkt über Kommandozeilen-Argumente übergeben. Weitere Informationen finden Sie unter [Kommandozeilen-Argumente](#kommandozeilen-argumente).

Beispielsweise können Sie mit dem folgenden Befehl ein GUI-Fenster aktivieren:

```bash
pdf2zh_next --gui
```

- Konfiguration über **Umgebungsvariablen** anpassen

Sie können das `--` in Kommandozeilen-Argumenten durch `PDF2ZH_` ersetzen, Parameter mit `=` verbinden und `-` durch `_` als Umgebungsvariablen ersetzen.

Zum Beispiel, wenn Sie ein GUI-Fenster aktivieren möchten, können Sie den folgenden Befehl verwenden:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Benutzerdefinierte **Konfigurationsdatei**

Sie können eine Konfigurationsdatei mit dem folgenden Kommandozeilen-Argument angeben:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Wenn Sie sich über das Format der Konfigurationsdatei unsicher sind, lesen Sie bitte die unten beschriebene Standardkonfigurationsdatei.

- **Standardkonfigurationsdatei**

Die Standardkonfigurationsdatei befindet sich unter `~/.config/pdf2zh`.  
Bitte ändern Sie die Konfigurationsdateien im Verzeichnis `default` nicht.  
Es wird dringend empfohlen, sich auf den Inhalt dieser Konfigurationsdatei zu beziehen und **Benutzerdefinierte Konfigurationsdatei** zu verwenden, um Ihre eigene Konfigurationsdatei zu implementieren.

> [!TIP]
> - Standardmäßig speichert pdf2zh 2.0 die aktuelle Konfiguration automatisch in `~/.config/pdf2zh/config.v3.toml` jedes Mal, wenn Sie im GUI auf die Übersetzungsschaltfläche klicken. Diese Konfigurationsdatei wird beim nächsten Start standardmäßig geladen.
> - Die Konfigurationsdateien im Verzeichnis `default` werden automatisch vom Programm generiert. Sie können sie zur Modifikation kopieren, aber bitte ändern Sie sie nicht direkt.
> - Konfigurationsdateien können Versionsnummern wie "v2", "v3" usw. enthalten. Dies sind **Versionsnummern der Konfigurationsdatei**, **nicht** die Versionsnummer von pdf2zh selbst.


[⬆️ Zurück zum Anfang](#toc)

---

#### Bereinigung überspringen

Wenn dieser Parameter auf True gesetzt wird, wird der Schritt zur PDF-Bereinigung übersprungen, was die Kompatibilität verbessern und einige Probleme bei der Schriftverarbeitung vermeiden kann.

Verwendung:

```bash
pdf2zh_next example.pdf --skip-clean
```

Oder Umgebungsvariablen verwenden:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Wenn `--enhance-compatibility` aktiviert ist, wird die Bereinigung automatisch übersprungen.

---

#### Übersetzungscache

PDFMathTranslate speichert übersetzte Texte zwischen, um die Geschwindigkeit zu erhöhen und unnötige API-Aufrufe für dieselben Inhalte zu vermeiden. Sie können die Option `--ignore-cache` verwenden, um den Übersetzungscache zu ignorieren und eine erneute Übersetzung zu erzwingen.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Bereitstellung als öffentlicher Dienst

Wenn Sie eine pdf2zh-GUI auf öffentlichen Diensten bereitstellen, sollten Sie die Konfigurationsdatei wie unten beschrieben anpassen.

> [!WARNING]
>
> Dieses Projekt wurde nicht professionell auf Sicherheit überprüft und könnte Sicherheitslücken enthalten. Bitte bewerten Sie die Risiken und ergreifen Sie die notwendigen Sicherheitsmaßnahmen, bevor Sie es in öffentlichen Netzwerken bereitstellen.


> [!TIP]
> - Bei der öffentlichen Bereitstellung sollten sowohl `disable_gui_sensitive_input` als auch `disable_config_auto_save` aktiviert sein.
> - Trennen Sie verschiedene verfügbare Dienste mit *englischen Kommas* <kbd>,</kbd> .

Eine brauchbare Konfiguration ist wie folgt:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Authentifizierung und Willkommensseite

Bei Verwendung von Authentifizierung und Willkommensseite, um festzulegen, welcher Benutzer die Web UI nutzen und die Login-Seite anpassen kann:

Beispiel auth.txt
Jede Zeile enthält zwei Elemente, Benutzername und Passwort, getrennt durch ein Komma.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

Beispiel welcome.html

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
> Die Willkommensseite funktioniert nur, wenn die Authentifizierungsdatei nicht leer ist.
> Wenn die Authentifizierungsdatei leer ist, gibt es keine Authentifizierung. :)

Eine brauchbare Konfiguration ist wie folgt:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Glossar-Unterstützung

PDFMathTranslate unterstützt die Glossartabelle. Die Glossartabellendatei sollte eine `csv`-Datei sein.
Die Datei enthält drei Spalten. Hier ist eine Demo-Glossardatei:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | Automatisches ML | de   |
| a,a    | a       | de   |
| "      | "       | de   |


Für CLI-Benutzer:
Sie können mehrere Dateien für das Glossar verwenden. Und verschiedene Dateien sollten durch `,` getrennt werden.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Für WebUI-Benutzer:

Sie können jetzt Ihre eigene Glossardatei hochladen. Nachdem Sie die Datei hochgeladen haben, können Sie sie überprüfen, indem Sie auf ihren Namen klicken und der Inhalt wird unten angezeigt.

[⬆️ Zurück zum Anfang](#toc)

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>