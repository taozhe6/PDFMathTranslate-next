[**Erweiterte Optionen**](./introduction.md) > **Erweiterte Optionen** _(aktuell)_

---

<h3 id="inhaltsverzeichnis">Inhaltsverzeichnis</h3>

- [#### Kommandozeilenargumente](#kommandozeilenargumente)
- [#### Ratenbegrenzungskonfigurationsleitfaden](#ratenbegrenzungskonfigurationsleitfaden)
- [#### Teilweise Übersetzung](#teilweise-übersetzung)
- [#### Quell- und Zielsprachen angeben](#quell--und-zielsprachen-angeben)
- [#### Übersetzen mit Ausnahmen](#übersetzen-mit-ausnahmen)
- [#### Benutzerdefinierte Eingabeaufforderung](#benutzerdefinierte-eingabeaufforderung)
- [#### Benutzerdefinierte Konfiguration](#benutzerdefinierte-konfiguration)
- [#### Überspringe Bereinigung](#überspringe-bereinigung)
- [#### Übersetzungscache](#übersetzungscache)
- [#### Bereitstellung als öffentlicher Dienst](#bereitstellung-als-öffentlicher-dienst)
- [#### Authentifizierung und Willkommensseite](#authentifizierung-und-willkommensseite)
- [#### Glossar-Unterstützung](#glossar-unterstützung)

---

#### Kommandozeilenargumente

Führen Sie den Übersetzungsbefehl in der Kommandozeile aus, um das übersetzte Dokument `example-mono.pdf` und das zweisprachige Dokument `example-dual.pdf` im aktuellen Arbeitsverzeichnis zu generieren. Verwenden Sie Google als Standard-Übersetzungsdienst. Weitere unterstützte Übersetzungsdienste finden Sie [HIER](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

In der folgenden Tabelle listen wir alle erweiterten Optionen zur Referenz auf:

##### Args

| Option                          | Funktion                                                                               | Beispiel                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Eingabe-PDF-Dateien zur Verarbeitung                                                     | `pdf2zh_next example.pdf`                                                                                             |
| `--output`                      | Ausgabeverzeichnis für Dateien                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| `--<Services>`                  | Verwenden Sie [**einen bestimmten Dienst**](./Documentation-of-Translation-Services.md) für die Übersetzung | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| `--help`, `-h`                  | Hilfe-Nachricht anzeigen und beenden                                                    | `pdf2zh_next -h`                                                                                                      |
| `--config-file`                 | Pfad zur Konfigurationsdatei                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| `--report-interval`             | Fortschrittsberichtsintervall in Sekunden                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--debug`                       | Debug-Protokollierungsebene verwenden                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--gui`                         | Interaktion mit der GUI                                                                       | `pdf2zh_next --gui`                                                                                                   |
| `--warmup`                      | Lädt nur die erforderlichen Assets herunter und überprüft sie, dann wird beendet                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| `--generate-offline-assets`     | Erzeuge Offline-Asset-Paket im angegebenen Verzeichnis                              | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| `--restore-offline-assets`      | Offline-Asset-Paket aus dem angegebenen Verzeichnis wiederherstellen                    | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| `--version`                     | Zeige Version und beende dann                                                           | `pdf2zh_next --version`                                                                                               |
| `--pages`                       | Teilweise Dokumentübersetzung                                                            | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
| `--lang-in`                     | Quellsprachcode                                                                         | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| `--lang-out`                    | Zielsprachcode                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| `--min-text-length`             | Minimale Textlänge für die Übersetzung                                                        | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| `--rpc-doclayout`               | RPC-Dienst-Hostadresse für Dokumentlayoutanalyse                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| `--qps`                         | QPS-Begrenzung für den Übersetzungsdienst                                               | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| `--ignore-cache`                | Übersetzungscache ignorieren                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--custom-system-prompt`        | Benutzerdefinierte Systemaufforderung für Übersetzungen. Wird für `/no_think` in Qwen 3 verwendet                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--glossaries`                  | Liste der Glossardateien.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| `--save-auto-extracted-glossary`| speichere automatisch extrahiertes Glossar                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| `--pool-max-workers`            | Maximale Anzahl von Workern für den Übersetzungspool. Wenn nicht gesetzt, wird qps als Anzahl der Worker verwendet | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| `--term-qps`                    | QPS-Begrenzung für den Übersetzungsdienst zur Begriffsentnahme. Wenn nicht gesetzt, folgt es qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| `--term-pool-max-workers`       | Maximale Anzahl an Workern für den Extraktionsübersetzungspool von Begriffen. Wenn nicht gesetzt oder 0, folgt es pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| `--no-auto-extract-glossary`    | Deaktiviere automatische Glossarextraktion                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--primary-font-family`         | Überschreibt die primäre Schriftfamilie für übersetzten Text. Optionen: 'serif' für Serifenschriften, 'sans-serif' für serifenlose Schriften, 'script' für Schreibschrift/kursive Schriften. Wenn nicht angegeben, wird eine automatische Schriftauswahl basierend auf den Eigenschaften des Originaltextes verwendet. | `pdf2zh_next example.pdf --primary-font-family serif` |
| `--no-dual`                     | Bilinguale PDF-Dateien nicht ausgeben                                                   | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--no-mono`                     | Gibt keine einsprachigen PDF-Dateien aus                                                | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| `--formular-font-pattern`       | Schriftmuster zur Identifizierung von Formeltext                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| `--formular-char-pattern`       | Zeichenmuster zur Identifizierung von Formeltext                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| `--split-short-lines`           | Erzwingt das Aufteilen kurzer Zeilen in verschiedene Absätze                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| `--short-line-split-factor`     | Teilungsschwellenwertfaktor für kurze Zeilen                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| `--skip-clean`                  | Überspringe den PDF-Bereinigungsschritt                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| `--dual-translate-first`        | Platziert übersetzte Seiten zuerst im dualen PDF-Modus                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--disable-rich-text-translate` | Deaktiviere Rich-Text-Übersetzung                                                      | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| `--enhance-compatibility`       | Aktiviert alle Kompatibilitätsverbesserungsoptionen                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| `--use-alternating-pages-dual`  | Verwende den Wechselseitenmodus für duale PDFs                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| `--watermark-output-mode`       | Wasserzeichen-Ausgabemodus für PDF-Dateien                                              | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        |
| `--max-pages-per-part`          | Maximale Seiten pro Teil für geteilte Übersetzung                                       | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| `--translate-table-text`        | Tabellentext übersetzen (experimentell)                                                | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| `--skip-scanned-detection`      | Gescannte Erkennung überspringen                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| `--ocr-workaround`              | Erzwingt, dass übersetzter Text schwarz ist und fügt weißen Hintergrund hinzu           | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| `--auto-enable-ocr-workaround`  | Aktiviere automatische OCR-Workaround. Wenn ein Dokument als stark gescannt erkannt wird, wird versucht, die OCR-Verarbeitung zu aktivieren und weitere Scans zu überspringen. Siehe Dokumentation für Details. (Standard: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| `--only-include-translated-page`| Fügt nur übersetzte Seiten in die Ausgabe-PDF ein. Wirkt nur, wenn --pages verwendet wird.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| `--no-merge-alternating-line-numbers` | Deaktiviert das Zusammenführen von alternierenden Zeilennummern und Textabsätzen in Dokumenten mit Zeilennummern | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| `--no-remove-non-formula-lines` | Deaktiviert das Entfernen von Nicht-Formel-Zeilen innerhalb von Absatzbereichen | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| `--non-formula-line-iou-threshold` | Setze IoU-Schwellenwert zur Identifizierung von Nicht-Formel-Zeilen (0.0-1.0) | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85` |
| `--figure-table-protection-threshold` | Schutzschwelle für Abbildungen und Tabellen festlegen (0.0-1.0). Zeilen innerhalb von Abbildungen/Tabellen werden nicht verarbeitet | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        |
| `--skip-formula-offset-calculation` | Überspringe die Formel-Offset-Berechnung während der Verarbeitung | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### GUI-Argumente

| Option                          | Funktion                              | Beispiel                                        |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Freigabemodus aktivieren               | `pdf2zh_next --gui --share`                     |
| `--auth-file`                   | Pfad zur Authentifizierungsdatei        | `pdf2zh_next --gui --auth-file /pfad`           |
| `--welcome-page`                | Pfad zur Willkommens-HTML-Datei          | `pdf2zh_next --gui --welcome-page /path`        |
| `--enabled-services`            | Aktivierte Übersetzungsdienste           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Deaktiviere GUI-sensible Eingabe            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
| `--disable-config-auto-save`    | Automatisches Speichern der Konfiguration deaktivieren | `pdf2zh_next --gui --disable-config-auto-save`  |
| `--server-port`                 | WebUI-Port                             | `pdf2zh_next --gui --server-port 7860`          |
| `--ui-lang`                     | UI-Sprache                            | `pdf2zh_next --gui --ui-lang zh`                |

[⬆️ Zurück zum Anfang](#toc)

---

#### Ratenbegrenzungskonfigurationsleitfaden

Bei der Verwendung von Übersetzungsdiensten ist eine ordnungsgemäße Ratenbegrenzungskonfiguration entscheidend, um API-Fehler zu vermeiden und die Leistung zu optimieren. Dieser Leitfaden erklärt, wie die Parameter `--qps` und `--pool-max-worker` basierend auf den verschiedenen Einschränkungen der Upstream-Dienste konfiguriert werden.

> [!TIP]
>
> Es wird empfohlen, dass die pool_size 1000 nicht überschreitet. Wenn die nach folgender Methode berechnete pool_size 1000 überschreitet, verwenden Sie bitte 1000.

##### RPM (Requests Per Minute)-Ratenbegrenzung

Wenn der Upstream-Dienst RPM-Beschränkungen hat, verwenden Sie die folgende Berechnung:

**Berechnungsformel:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Der Faktor 10 ist ein empirischer Koeffizient, der in den meisten Szenarien im Allgemeinen gut funktioniert.

**Beispiel:**
Wenn Ihr Übersetzungsdienst ein Limit von 600 RPM hat:
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
Wenn Ihr Übersetzungsdienst 50 gleichzeitige Verbindungen erlaubt:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Best Practices

> [!TIP]
> - Beginnen Sie immer mit konservativen Werten und erhöhen Sie diese schrittweise bei Bedarf
> - Überwachen Sie die Antwortzeiten und Fehlerraten Ihres Dienstes
> - Unterschiedliche Dienste erfordern möglicherweise unterschiedliche Optimierungsstrategien
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
> `25-` enthält alle Seiten nach Seite 25. Wenn Ihr Dokument 100 Seiten hat, entspricht dies `25-100`.
>
> Ebenso enthält `-25` alle Seiten vor Seite 25, was `1-25` entspricht.

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

Verwenden Sie Regex, um Formelschriftarten und Zeichen anzugeben, die beibehalten werden müssen:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Behalte standardmäßig `Latex`-, `Mono`-, `Code`-, `Kursiv`-, `Symbol`- und `Mathe`-Schriftarten bei:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Benutzerdefinierte Eingabeaufforderung

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/pull/637). -->

Benutzerdefinierte Systemaufforderung für Übersetzungen. Wird hauptsächlich verwendet, um die '/no_think'-Anweisung von Qwen 3 in die Eingabeaufforderung hinzuzufügen.

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
> Höherrangige Änderungen überschreiben niederrangige.
>
> **cli/gui > env > Benutzerkonfigurationsdatei > Standardkonfigurationsdatei**

- Ändern der Konfiguration über **Kommandozeilenargumente**

In den meisten Fällen können Sie Ihre gewünschten Einstellungen direkt über Kommandozeilenargumente übergeben. Weitere Informationen finden Sie unter [Kommandozeilenargumente](#cmd).

Wenn Sie beispielsweise ein GUI-Fenster aktivieren möchten, können Sie den folgenden Befehl verwenden:

```bash
pdf2zh_next --gui
```

- Konfiguration über **Umgebungsvariablen** ändern

Sie können das `--` in den Kommandozeilenargumenten durch `PDF2ZH_` ersetzen, Parameter mit `=` verbinden und `-` durch `_` als Umgebungsvariablen ersetzen.

Wenn Sie beispielsweise ein GUI-Fenster aktivieren möchten, können Sie den folgenden Befehl verwenden:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Benutzerdefinierte **Konfigurationsdatei**

Sie können eine Konfigurationsdatei mit dem folgenden Kommandozeilenargument angeben:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Wenn Sie sich über das Format der Konfigurationsdatei unsicher sind, lesen Sie bitte die unten beschriebene Standardkonfigurationsdatei.

- **Standardkonfigurationsdatei**

Die Standardkonfigurationsdatei befindet sich unter `~/.config/pdf2zh`.  
Bitte ändern Sie die Konfigurationsdateien im `default`-Verzeichnis nicht.  
Es wird dringend empfohlen, auf den Inhalt dieser Konfigurationsdatei zu verweisen und **Benutzerdefinierte Konfiguration** zu verwenden, um Ihre eigene Konfigurationsdatei zu implementieren.

> [!TIP]
> - Standardmäßig speichert pdf2zh 2.0 die aktuelle Konfiguration bei jedem Klick auf die Übersetzen-Schaltfläche in der GUI automatisch in `~/.config/pdf2zh/config.v3.toml`. Diese Konfigurationsdatei wird beim nächsten Start standardmäßig geladen.
> - Die Konfigurationsdateien im `default`-Verzeichnis werden automatisch vom Programm generiert. Sie können sie zur Modifikation kopieren, bitte modifizieren Sie sie jedoch nicht direkt.
> - Konfigurationsdateien können Versionsnummern wie "v2", "v3" usw. enthalten. Dies sind **Konfigurationsdatei-Versionsnummern**, **nicht** die Versionsnummer von pdf2zh selbst.


[⬆️ Zurück zum Anfang](#toc)

---

#### Überspringe Bereinigung

Wenn dieser Parameter auf True gesetzt wird, wird der PDF-Bereinigungsschritt übersprungen, was die Kompatibilität verbessern und einige Schriftverarbeitungsprobleme vermeiden kann.

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

PDFMathTranslate cached übersetzte Texte, um die Geschwindigkeit zu erhöhen und unnötige API-Aufrufe für gleiche Inhalte zu vermeiden. Sie können die Option `--ignore-cache` verwenden, um den Übersetzungscache zu ignorieren und eine erneute Übersetzung zu erzwingen.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Zurück zum Anfang](#toc)

---

#### Bereitstellung als öffentlicher Dienst

Wenn Sie eine pdf2zh-GUI auf öffentlichen Diensten bereitstellen, sollten Sie die Konfigurationsdatei wie unten beschrieben ändern.

> [!WARNING]
>
> Dieses Projekt wurde nicht professionell auf Sicherheit überprüft und könnte Sicherheitslücken enthalten. Bitte bewerten Sie die Risiken und ergreifen Sie notwendige Sicherheitsmaßnahmen, bevor Sie es in öffentlichen Netzwerken bereitstellen.


> [!TIP]
> - Bei der öffentlichen Bereitstellung sollten sowohl `disable_gui_sensitive_input` als auch `disable_config_auto_save` aktiviert sein.
> - Trennen Sie verschiedene verfügbare Dienste mit *englischen Kommas* <kbd>,</kbd> .

Eine verwendbare Konfiguration ist wie folgt:

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

Bei Verwendung von Authentifizierung und Willkommensseite, um festzulegen, welcher Benutzer die Web UI verwenden darf und die Anmeldeseite anzupassen:

Beispiel auth.txt
Jede Zeile enthält zwei Elemente, Benutzername und Passwort, getrennt durch ein Komma.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

example welcome.html

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
> Wenn die Authentifizierungsdatei leer ist, erfolgt keine Authentifizierung. :)

Eine verwendbare Konfiguration ist wie folgt:

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

| source | target | tgt_lng |
|--------|--------|---------|
| AutoML | AutoML | de      |
| a,a    | a,a    | de      |
| "      | "      | de      |


Für CLI-Benutzer:
Sie können mehrere Dateien für das Glossar verwenden. Und verschiedene Dateien sollten durch `,` getrennt werden.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Für WebUI-Benutzer:

Sie können jetzt Ihre eigene Glossardatei hochladen. Nachdem Sie die Datei hochgeladen haben, können Sie sie überprüfen, indem Sie auf ihren Namen klicken und der Inhalt wird unten angezeigt.

[⬆️ Nach oben](#toc)

<div align="right"> 
<h6><small>Ein Teil des Inhalts dieser Seite wurde von GPT übersetzt und kann Fehler enthalten.</small></h6>