[**Opzioni avanzate**](./introduction.md) > **Opzioni avanzate** _(corrente)_

---

<h3 id="toc">Indice dei contenuti</h3>

- [#### Argomenti della Riga di Comando](#argomenti-della-riga-di-comando)
- [#### Guida alla configurazione della limitazione della frequenza](#guida-alla-configurazione-della-limitazione-della-frequenza)
- [#### Traduzione parziale](#traduzione-parziale)
- [#### Specificare le lingue di origine e di destinazione](#specificare-le-lingue-di-origine-e-di-destinazione)
- [#### Traduci con eccezioni](#traduci-con-eccezioni)
- [#### Prompt personalizzato](#prompt-personalizzato)
- [#### Configurazione personalizzata](#configurazione-personalizzata)
- [#### Salta pulizia](#salta-pulizia)
- [#### Cache delle traduzioni](#cache-delle-traduzioni)
- [#### Distribuzione come servizi pubblici](#distribuzione-come-servizi-pubblici)
- [#### Autenticazione e pagina di benvenuto](#autenticazione-e-pagina-di-benvenuto)
- [#### Glossario Supportato](#glossario-supportato)

---

#### Argomenti della Riga di Comando

Esegui il comando di traduzione nella riga di comando per generare il documento tradotto `example-mono.pdf` e il documento bilingue `example-dual.pdf` nella directory di lavoro corrente. Utilizza Google come servizio di traduzione predefinito. Altri servizi di traduzione supportati possono essere trovati [QUI](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

Nella seguente tabella, elenchiamo tutte le opzioni avanzate per riferimento:

##### Argomenti

| Opzione                          | Funzione                                                                               | Esempio                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | File PDF di input da elaborare                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `--output`                      | Directory di output per i file                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| `--<Services>`                  | Utilizza [**servizi specifici**](./Documentation-of-Translation-Services.md) per la traduzione | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| `--help`, `-h`                  | Mostra il messaggio di aiuto ed esci                                                              | `pdf2zh_next -h`                                                                                                      |
| `--config-file`                 | Percorso del file di configurazione                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| `--report-interval`             | Intervallo di segnalazione del progresso in secondi                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--debug`                       | Usa il livello di registrazione di debug                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--gui`                         | Interagisci con la GUI                                                                       | `pdf2zh_next --gui`                                                                                                   |
| `--warmup`                      | Scarica e verifica solo gli asset richiesti, quindi esci                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| `--generate-offline-assets`     | Genera pacchetto di risorse offline nella directory specificata                         | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| `--restore-offline-assets`      | Ripristina il pacchetto di risorse offline dalla directory specificata                  | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| `--version`                     | Mostra la versione e poi esci                                                                  | `pdf2zh_next --version`                                                                                               |
| `--pages`                       | Traduzione parziale del documento                                                            | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
| `--lang-in`                     | Codice lingua di origine                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| `--lang-out`                    | Codice lingua di destinazione                                                           | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| `--min-text-length`             | Lunghezza minima del testo da tradurre                                                        | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| `--rpc-doclayout`               | Indirizzo host del servizio RPC per l'analisi del layout del documento                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| `--qps`                         | Limite QPS per il servizio di traduzione                                                | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| `--ignore-cache`                | Ignora la cache delle traduzioni                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--custom-system-prompt`        | Prompt di sistema personalizzato per la traduzione. Utilizzato per `/no_think` in Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--glossaries`                  | Elenco dei file del glossario.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| `--save-auto-extracted-glossary`| salva automaticamente il glossario estratto                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| `--pool-max-workers`            | Numero massimo di lavoratori per il pool di traduzione. Se non impostato, utilizzerà qps come numero di lavoratori | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| `--term-qps`                    | Limite QPS per il servizio di traduzione di estrazione dei termini. Se non impostato, seguirà qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| `--term-pool-max-workers`       | Numero massimo di worker per il pool di traduzione dell'estrazione dei termini. Se non impostato o 0, seguirà pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| `--no-auto-extract-glossary`    | Disabilita l'estrazione automatica del glossario                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--primary-font-family`         | Sovrascrive la famiglia di caratteri primaria per il testo tradotto. Scelte: 'serif' per caratteri con grazie, 'sans-serif' per caratteri senza grazie, 'script' per caratteri corsivi/stilizzati. Se non specificato, utilizza la selezione automatica dei caratteri basata sulle proprietà del testo originale. | `pdf2zh_next example.pdf --primary-font-family serif` |
| `--no-dual`                     | Non produrre file PDF bilingue                                                          | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--no-mono`                     | Non generare file PDF monolingue                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| `--formular-font-pattern`       | Pattern del font per identificare il testo delle formule                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| `--formular-char-pattern`       | Modello di caratteri per identificare il testo della formula                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| `--split-short-lines`           | Forza la divisione di righe brevi in paragrafi diversi                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| `--short-line-split-factor`     | Fattore di soglia di divisione per righe brevi                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| `--skip-clean`                  | Salta il passaggio di pulizia del PDF                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| `--dual-translate-first`        | Metti le pagine tradotte per prime in modalità PDF duale                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--disable-rich-text-translate` | Disabilita la traduzione del testo formattato                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| `--enhance-compatibility`       | Abilita tutte le opzioni di miglioramento della compatibilità                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| `--use-alternating-pages-dual`  | Utilizza la modalità pagine alternate per PDF duali                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| `--watermark-output-mode`       | Modalità di output della filigrana per i file PDF                                                     | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        |
| `--max-pages-per-part`          | Numero massimo di pagine per parte per la traduzione divisa                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| `--translate-table-text`        | Traduci il testo della tabella (sperimentale)                                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| `--skip-scanned-detection`      | Salta il rilevamento dei documenti scansionati                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| `--ocr-workaround`              | Forza il testo tradotto a essere nero e aggiunge uno sfondo bianco                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| `--auto-enable-ocr-workaround`  | Abilita la soluzione automatica OCR. Se un documento viene rilevato come fortemente scansionato, questo tenterà di abilitare l'elaborazione OCR e salterà ulteriori rilevamenti di scansione. Vedi la documentazione per i dettagli. (predefinito: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| `--only-include-translated-page`| Includi solo le pagine tradotte nel PDF di output. Efficace solo quando viene utilizzato --pages.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| `--no-merge-alternating-line-numbers` | Disabilita l'unione dei numeri di riga alternati e dei paragrafi di testo nei documenti con numeri di riga | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| `--no-remove-non-formula-lines` | Disabilita la rimozione delle righe non di formula all'interno delle aree di paragrafo | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| `--non-formula-line-iou-threshold` | Imposta la soglia IoU per identificare le righe non formule (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       |
| `--figure-table-protection-threshold` | Imposta la soglia di protezione per figure e tabelle (0.0-1.0). Le righe all'interno di figure/tabelle non verranno elaborate | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        |
| `--skip-formula-offset-calculation` | Salta il calcolo dell'offset della formula durante l'elaborazione | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### Argomenti GUI

| Opzione                          | Funzione                               | Esempio                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Abilita modalità condivisione          | `pdf2zh_next --gui --share`                     |
| `--auth-file`                   | Percorso del file di autenticazione        | `pdf2zh_next --gui --auth-file /percorso`           |
| `--welcome-page`                | Percorso al file html di benvenuto     | `pdf2zh_next --gui --welcome-page /path`        |
| `--enabled-services`            | Servizi di traduzione abilitati           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Disabilita input sensibile GUI            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
| `--disable-config-auto-save`    | Disabilita il salvataggio automatico della configurazione | `pdf2zh_next --gui --disable-config-auto-save`  |
| `--server-port`                 | Porta WebUI                             | `pdf2zh_next --gui --server-port 7860`          |
| `--ui-lang`                     | Lingua dell'interfaccia utente        | `pdf2zh_next --gui --ui-lang zh`                |

[⬆️ Torna all'inizio](#toc)

---

#### Guida alla configurazione della limitazione della frequenza

Quando si utilizzano i servizi di traduzione, una corretta configurazione della limitazione della frequenza è fondamentale per evitare errori API e ottimizzare le prestazioni. Questa guida spiega come configurare i parametri `--qps` e `--pool-max-worker` in base alle diverse limitazioni dei servizi upstream.

> [!TIP]
>
> Si consiglia che il pool_size non superi 1000. Se il pool_size calcolato con il metodo seguente supera 1000, si prega di utilizzare 1000.

##### RPM (Richieste Per Minuto) Limitazione della velocità

Quando il servizio upstream ha limitazioni RPM, utilizza il seguente calcolo:

**Formula di calcolo:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Il fattore 10 è un coefficiente empirico che generalmente funziona bene per la maggior parte degli scenari.

**Esempio:**
Se il tuo servizio di traduzione ha un limite di 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitazione delle connessioni simultanee

Quando il servizio upstream ha limitazioni di connessione simultanea (come il servizio ufficiale GLM), utilizza questo approccio:

**Formula di Calcolo:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Esempio:**
Se il tuo servizio di traduzione consente 50 connessioni simultanee:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Pratiche consigliate

> [!TIP]
> - Inizia sempre con valori conservativi e aumenta gradualmente se necessario
> - Monitora i tempi di risposta del servizio e i tassi di errore
> - Servizi diversi possono richiedere strategie di ottimizzazione diverse
> - Considera il tuo caso d'uso specifico e la dimensione del documento quando imposti questi parametri


[⬆️ Torna all'inizio](#toc)

---

#### Traduzione parziale

Usa il parametro `--pages` per tradurre una porzione di un documento.

- Se i numeri di pagina sono consecutivi, puoi scriverlo così:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` include tutte le pagine dopo la pagina 25. Se il tuo documento ha 100 pagine, questo equivale a `25-100`.
> 
> Allo stesso modo, `-25` include tutte le pagine prima della pagina 25, che equivale a `1-25`.

- Se le pagine non sono consecutive, puoi usare una virgola `,` per separarle.

Ad esempio, se desideri tradurre la prima e la terza pagina, puoi utilizzare il seguente comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Se le pagine includono sia intervalli consecutivi che non consecutivi, puoi anche collegarli con una virgola, in questo modo:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Questo comando tradurrà la prima pagina, la terza pagina, le pagine da 10 a 20 e tutte le pagine da 25 alla fine.

[⬆️ Torna all'inizio](#toc)

---

#### Specificare le lingue di origine e di destinazione

Vedi [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Torna all'inizio](#toc)

---

#### Traduci con eccezioni

Utilizza regex per specificare i caratteri e i font delle formule che devono essere preservati:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Preserva i caratteri `Latex`, `Mono`, `Code`, `Italic`, `Symbol` e `Math` per impostazione predefinita:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Torna all'inizio](#toc)

---

#### Prompt personalizzato

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/pull/637). -->

Prompt di sistema personalizzato per la traduzione. Viene utilizzato principalmente per aggiungere l'istruzione '/no_think' di Qwen 3 nel prompt.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Torna all'inizio](#toc)

---

#### Configurazione personalizzata

Esistono diversi modi per modificare e importare il file di configurazione.

> [!NOTE]
> **Gerarchia dei File di Configurazione**
>
> Quando si modifica lo stesso parametro utilizzando metodi diversi, il software applicherà le modifiche secondo l'ordine di priorità riportato di seguito.
>
> Le modifiche con priorità più alta sovrascriveranno quelle con priorità più bassa.
>
> **cli/gui > env > file di configurazione utente > file di configurazione predefinito**

- Modifica della configurazione tramite **Argomenti della Riga di Comando**

Per la maggior parte dei casi, puoi passare direttamente le impostazioni desiderate tramite gli argomenti della riga di comando. Si prega di fare riferimento a [Argomenti della Riga di Comando](#cmd) per ulteriori informazioni.

Ad esempio, se desideri abilitare una finestra GUI, puoi utilizzare il seguente comando:

```bash
pdf2zh_next --gui
```

- Modifica della configurazione tramite **Variabili d'ambiente**

È possibile sostituire il `--` negli argomenti della riga di comando con `PDF2ZH_`, collegare i parametri utilizzando `=`, e sostituire `-` con `_` come variabili d'ambiente.

Ad esempio, se si desidera abilitare una finestra GUI, è possibile utilizzare il seguente comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- File di **Configurazione** Specificato dall'Utente

Puoi specificare un file di configurazione utilizzando l'argomento della riga di comando qui sotto:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Se non sei sicuro del formato del file di configurazione, consulta il file di configurazione predefinito descritto di seguito.

- **File di configurazione predefinito**

Il file di configurazione predefinito si trova in `~/.config/pdf2zh`.  
Si prega di non modificare i file di configurazione nella directory `default`.  
È fortemente consigliato fare riferimento al contenuto di questo file di configurazione e utilizzare **Configurazione personalizzata** per implementare il proprio file di configurazione.

> [!TIP]
> - Per impostazione predefinita, pdf2zh 2.0 salva automaticamente la configurazione corrente in `~/.config/pdf2zh/config.v3.toml` ogni volta che si fa clic sul pulsante di traduzione nella GUI. Questo file di configurazione verrà caricato per impostazione predefinita al prossimo avvio.
> - I file di configurazione nella directory `default` vengono generati automaticamente dal programma. È possibile copiarli per modificarli, ma si prega di non modificarli direttamente.
> - I file di configurazione possono includere numeri di versione come "v2", "v3", ecc. Questi sono **numeri di versione del file di configurazione**, **non** il numero di versione di pdf2zh stesso.


[⬆️ Torna all'inizio](#toc)

---

#### Salta pulizia

Quando questo parametro è impostato su True, il passaggio di pulizia del PDF verrà saltato, il che può migliorare la compatibilità ed evitare alcuni problemi di elaborazione dei caratteri.

Utilizzo:

```bash
pdf2zh_next example.pdf --skip-clean
```

O utilizzando variabili d'ambiente:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Quando `--enhance-compatibility` è abilitato, Salta pulizia viene automaticamente abilitato.

---

#### Cache delle traduzioni

PDFMathTranslate memorizza nella cache i testi tradotti per aumentare la velocità ed evitare chiamate API non necessarie per contenuti identici. Puoi utilizzare l'opzione `--ignore-cache` per ignorare la cache delle traduzioni e forzare una nuova traduzione.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Torna all'inizio](#toc)

---

#### Distribuzione come servizi pubblici

Quando si distribuisce un'interfaccia grafica pdf2zh su servizi pubblici, è necessario modificare il file di configurazione come descritto di seguito.

> [!WARNING]
>
> Questo progetto non è stato sottoposto a un audit di sicurezza professionale e potrebbe contenere vulnerabilità di sicurezza. Si prega di valutare i rischi e adottare le misure di sicurezza necessarie prima di distribuire su reti pubbliche.


> [!TIP]
> - Quando si distribuisce pubblicamente, sia disable_gui_sensitive_input che disable_config_auto_save dovrebbero essere abilitati.
> - Separare i diversi servizi disponibili con *virgole inglesi* <kbd>,</kbd> .

Una configurazione utilizzabile è la seguente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Torna all'inizio](#toc)

---

#### Autenticazione e pagina di benvenuto

Quando si utilizza Autenticazione e pagina di benvenuto per specificare quale utente può utilizzare Web UI e personalizzare la pagina di accesso:

esempio auth.txt
Ogni riga contiene due elementi, nome utente e password, separati da una virgola.

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
> La pagina di benvenuto funzionerà solo se il file di autenticazione non è vuoto.
> Se il file di autenticazione è vuoto, non ci sarà alcuna autenticazione. :)

Una configurazione utilizzabile è la seguente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Torna all'inizio](#toc)

---

#### Glossario Supportato

PDFMathTranslate supporta la tabella del glossario. Il file della tabella del glossario dovrebbe essere un file `csv`.
Ci sono tre colonne nel file. Ecco un file di glossario demo:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | AutoML  | it      |
| a,a    | a       | it      |
| "      | "       | it      |


Per l'utente CLI:
Puoi utilizzare più file per il glossario. E i file diversi dovrebbero essere separati da `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Per gli utenti di WebUI:

Ora puoi caricare il tuo file di glossario. Dopo aver caricato il file, puoi verificarli facendo clic sul loro nome e il contenuto verrà visualizzato di seguito.

[⬆️ Torna all'inizio](#toc)

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>