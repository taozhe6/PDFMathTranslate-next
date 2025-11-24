>
> For more information, read our [Documentation Guide](https://pdf2zh.com/docs/guide).

---

### TRANSLATION RESULT

> [!NOTE]
> Questa documentazione potrebbe contenere contenuti generati da AI. Sebbene ci sforziamo per l'accuratezza, potrebbero esserci imprecisioni. Si prega di segnalare eventuali problemi tramite:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - Contributo della comunità (PR benvenuti!)
>
> Per ulteriori informazioni, leggi la nostra [Guida alla documentazione](https://pdf2zh.com/docs/guide).

The `do_translate_async_stream` function is an asynchronous generator that performs translation on a stream of text chunks. It is designed to handle continuous input streams, such as those from a file being read in chunks, and yields translated chunks as they become available.

### Function Signature
```python
async def do_translate_async_stream(
    text_chunks: AsyncIterator[str],
    source_language: str = "en",
    target_language: str = "zh",
    translation_services: Optional[List[str]] = None,
    translation_service: Optional[str] = None,
    api_key: Optional[str] = None,
    glossary: Optional[List[Tuple[str, str]]] = None,
    context: Optional[str] = None,
    instruction: Optional[str] = None,
    request_params: Optional[Dict[str, Any]] = None,
    **kwargs: Any
) -> AsyncIterator[str]:
```

### Parameters
- `text_chunks` (AsyncIterator[str]): An asynchronous iterator that yields chunks of text to be translated.
- `source_language` (str, optional): The language code of the source text. Defaults to "en".
- `target_language` (str, optional): The language code of the target translation. Defaults to "zh".
- `translation_services` (Optional[List[str]], optional): A list of translation service names to use. If not provided, defaults to the services configured in the environment.
- `translation_service` (Optional[str], optional): A specific translation service to use. If provided, overrides `translation_services`.
- `api_key` (Optional[str], optional): The API key for the translation service. If not provided, uses the key from environment variables.
- `glossary` (Optional[List[Tuple[str, str]]], optional): A list of tuples representing custom glossary terms. Each tuple should be (source_term, target_term).
- `context` (Optional[str], optional): Additional context to provide to the translation service for better accuracy.
- `instruction` (Optional[str], optional): Specific instructions for the translation service.
- `request_params` (Optional[Dict[str, Any]], optional): Additional parameters to pass to the translation service API request.
- `**kwargs`: Additional keyword arguments that may be passed to the underlying translation functions.

### Returns
- `AsyncIterator[str]`: An asynchronous iterator that yields translated chunks of text.

### Example Usage
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    # Simulate reading chunks from a file or stream
    chunks = ["First chunk of text.", "Second chunk of text.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)  # Simulate async delay

async def main():
    translated_chunks = []
    async for translated_chunk in do_translate_async_stream(
        text_chunk_generator(),
        source_language="en",
        target_language="zh"
    ):
        translated_chunks.append(translated_chunk)
        print(f"Translated: {translated_chunk}")
    
    full_translation = "".join(translated_chunks)
    print("Full translation:", full_translation)

asyncio.run(main())
```

### Notes
- This function is useful for processing large texts in a memory-efficient manner, as it processes and yields translations chunk by chunk.
- The function handles the concatenation of chunks internally to ensure coherent translations across chunk boundaries.
- Error handling is built into the function, and it will raise exceptions if the translation services encounter issues.

---

### TRANSLATION RESULT

## API Python: do_translate_async_stream
La funzione `do_translate_async_stream` è un generatore asincrono che esegue la traduzione su un flusso di blocchi di testo. È progettata per gestire flussi di input continui, come quelli provenienti da un file letto in blocchi, e restituisce i blocchi tradotti man mano che diventano disponibili.

### Firma della funzione
```python
async def do_translate_async_stream(
    text_chunks: AsyncIterator[str],
    source_language: str = "en",
    target_language: str = "zh",
    translation_services: Optional[List[str]] = None,
    translation_service: Optional[str] = None,
    api_key: Optional[str] = None,
    glossary: Optional[List[Tuple[str, str]]] = None,
    context: Optional[str] = None,
    instruction: Optional[str] = None,
    request_params: Optional[Dict[str, Any]] = None,
    **kwargs: Any
) -> AsyncIterator[str]:
```

### Parametri
- `text_chunks` (AsyncIterator[str]): Un iteratore asincrono che restituisce blocchi di testo da tradurre.
- `source_language` (str, opzionale): Il codice lingua del testo sorgente. Predefinito a "en".
- `target_language` (str, opzionale): Il codice lingua della traduzione di destinazione. Predefinito a "zh".
- `translation_services` (Optional[List[str]], opzionale): Un elenco di nomi di servizi di traduzione da utilizzare. Se non fornito, utilizza i servizi configurati nell'ambiente.
- `translation_service` (Optional[str], opzionale): Un servizio di traduzione specifico da utilizzare. Se fornito, sovrascrive `translation_services`.
- `api_key` (Optional[str], opzionale): La chiave API per il servizio di traduzione. Se non fornita, utilizza la chiave dalle variabili d'ambiente.
- `glossary` (Optional[List[Tuple[str, str]]], opzionale): Un elenco di tuple che rappresentano termini personalizzati del glossario. Ogni tupla dovrebbe essere (termine_sorgente, termine_destinazione).
- `context` (Optional[str], opzionale): Contesto aggiuntivo da fornire al servizio di traduzione per una migliore accuratezza.
- `instruction` (Optional[str], opzionale): Istruzioni specifiche per il servizio di traduzione.
- `request_params` (Optional[Dict[str, Any]], opzionale): Parametri aggiuntivi da passare alla richiesta API del servizio di traduzione.
- `**kwargs`: Argomenti chiave aggiuntivi che possono essere passati alle funzioni di traduzione sottostanti.

### Restituisce
- `AsyncIterator[str]`: Un iteratore asincrono che restituisce blocchi di testo tradotti.

### Esempio di utilizzo
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    # Simula la lettura di blocchi da un file o flusso
    chunks = ["First chunk of text.", "Second chunk of text.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)  # Simula un ritardo asincrono

async def main():
    translated_chunks = []
    async for translated_chunk in do_translate_async_stream(
        text_chunk_generator(),
        source_language="en",
        target_language="zh"
    ):
        translated_chunks.append(translated_chunk)
        print(f"Translated: {translated_chunk}")
    
    full_translation = "".join(translated_chunks)
    print("Full translation:", full_translation)

asyncio.run(main())
```

### Note
- Questa funzione è utile per elaborare testi di grandi dimensioni in modo efficiente in termini di memoria, poiché elabora e restituisce le traduzioni blocco per blocco.
- La funzione gestisce la concatenazione dei blocchi internamente per garantire traduzioni coerenti attraverso i confini dei blocchi.
- La gestione degli errori è integrata nella funzione e solleverà eccezioni se i servizi di traduzione incontrano problemi.

This document provides a comprehensive guide for translators who wish to contribute to the **pdf2zh** project. It covers everything from setting up the environment to submitting translations. The guide is divided into several sections for clarity.

!!! Note

    The main translation platform for this project is [Crowdin](https://crowdin.com/project/pdf2zh). If you are not familiar with Crowdin, please refer to the [Crowdin Documentation](https://support.crowdin.com/).

### Table of Contents

- [Getting Started](#getting-started)
- [Advanced](#advanced)
- [Supported Languages](#supported-languages)
- [Community](#community)
- [FAQ](#faq)

---

### Getting Started

This section will guide you through the initial steps to start translating.

#### Step 1: Join the Project

1. Visit the [Crowdin project page](https://crowdin.com/project/pdf2zh).
2. Click the "Join" button to request access to the project.
3. Wait for approval from the project maintainers.

#### Step 2: Choose a Language

1. After joining, select the language you wish to translate into from the list of supported languages.
2. If your language is not listed, you can request it by contacting the project maintainers.

#### Step 3: Start Translating

1. Navigate to the file you wish to translate.
2. Click on a segment to open the translation editor.
3. Enter your translation in the provided field.
4. Save your translation.

!!! Tip

    You can use the translation memory and machine translation suggestions to speed up your work.

### Advanced

This section covers advanced topics for experienced translators.

#### Translation Memory

Translation Memory (TM) is a database that stores previously translated segments. It helps maintain consistency and speed up the translation process.

#### Glossary

The project glossary contains key terms and their approved translations. Please refer to the glossary to ensure consistency.

#### Quality Assurance

Crowdin provides quality assurance checks to help you identify potential issues in your translations. Please pay attention to these checks.

### Supported Languages

The project currently supports the following languages:

- English (en)
- Chinese (zh-CN)
- Japanese (ja)
- Korean (ko)
- French (fr)
- German (de)
- Spanish (es)
- Italian (it)
- Russian (ru)
- Arabic (ar)

If you would like to add a new language, please contact the project maintainers.

### Community

Join our community to connect with other translators and get help.

- [Discord Server](https://discord.gg/example)
- [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions)

### FAQ

#### How do I become a proofreader?

To become a proofreader, you need to have a good track record of quality translations. Contact the project maintainers to express your interest.

#### Can I translate the documentation?

Yes! The documentation is also hosted on Crowdin. You can find it under the "Documentation" folder.

#### What if I find a mistake in the source text?

If you find a mistake in the source text, please report it by creating an issue on [GitHub](https://github.com/pdf2zh/pdf2zh/issues).

---

### ORIGINAL TEXT END

---

### TRANSLATION RESULT

### Panoramica

Questo documento fornisce una guida completa per i traduttori che desiderano contribuire al progetto **pdf2zh**. Copre tutto, dalla configurazione dell'ambiente all'invio delle traduzioni. La guida è divisa in diverse sezioni per chiarezza.

!!! Note

    La piattaforma di traduzione principale per questo progetto è [Crowdin](https://crowdin.com/project/pdf2zh). Se non hai familiarità con Crowdin, consulta la [Documentazione di Crowdin](https://support.crowdin.com/).

### Indice

- [Iniziare](#iniziare)
- [Opzioni avanzate](#opzioni-avanzate)
- [Lingue supportate](#lingue-supportate)
- [Comunità](#comunità)
- [Domande frequenti](#domande-frequenti)

---

### Iniziare

Questa sezione ti guiderà attraverso i passi iniziali per iniziare a tradurre.

#### Passo 1: Unisciti al progetto

1. Visita la [pagina del progetto Crowdin](https://crowdin.com/project/pdf2zh).
2. Clicca il pulsante "Unisciti" per richiedere l'accesso al progetto.
3. Attendi l'approvazione dai maintainer del progetto.

#### Passo 2: Scegli una lingua

1. Dopo esserti unito, seleziona la lingua in cui desideri tradurre dalla lista delle lingue supportate.
2. Se la tua lingua non è elencata, puoi richiederla contattando i maintainer del progetto.

#### Passo 3: Inizia a tradurre

1. Naviga fino al file che desideri tradurre.
2. Clicca su un segmento per aprire l'editor di traduzione.
3. Inserisci la tua traduzione nel campo fornito.
4. Salva la tua traduzione.

!!! Tip

    Puoi utilizzare la memoria di traduzione e i suggerimenti di traduzione automatica per velocizzare il tuo lavoro.

### Opzioni avanzate

Questa sezione tratta argomenti avanzati per traduttori esperti.

#### Memoria di traduzione

La Memoria di Traduzione (TM) è un database che memorizza segmenti precedentemente tradotti. Aiuta a mantenere la coerenza e a velocizzare il processo di traduzione.

#### Glossario

Il glossario del progetto contiene i termini chiave e le loro traduzioni approvate. Si prega di fare riferimento al glossario per garantire la coerenza.

#### Controllo qualità

Crowdin fornisce controlli di garanzia della qualità per aiutarti a identificare potenziali problemi nelle tue traduzioni. Si prega di prestare attenzione a questi controlli.

### Lingue supportate

Il progetto supporta attualmente le seguenti lingue:

- Inglese (en)
- Cinese (zh-CN)
- Giapponese (ja)
- Coreano (ko)
- Francese (fr)
- Tedesco (de)
- Spagnolo (es)
- Italiano (it)
- Russo (ru)
- Arabo (ar)

Se desideri aggiungere una nuova lingua, contatta i maintainer del progetto.

### Comunità

Unisciti alla nostra comunità per connetterti con altri traduttori e ottenere aiuto.

- [Server Discord](https://discord.gg/example)
- [Discussioni GitHub](https://github.com/pdf2zh/pdf2zh/discussions)

### Domande frequenti

#### Come posso diventare un correttore di bozze?

Per diventare un correttore di bozze, devi avere una buona storia di traduzioni di qualità. Contatta i maintainer del progetto per esprimere il tuo interesse.

#### Posso tradurre la documentazione?

Sì! La documentazione è anche ospitata su Crowdin. Puoi trovarla sotto la cartella "Documentazione".

#### Cosa succede se trovo un errore nel testo sorgente?

Se trovi un errore nel testo sorgente, segnalalo creando un issue su [GitHub](https://github.com/pdf2zh/pdf2zh/issues).

---
- The events are in Server-Sent Events (SSE) format.

```python
async def do_translate_async_stream(
    settings: SettingsModel,
    file_path: str
) -> AsyncGenerator[dict, None]:
    ...
```

### Example Usage

```python
import asyncio
from pdf2zh import SettingsModel, do_translate_async_stream

async def main():
    settings = SettingsModel(
        target_language="it",
        translation_service="google",
        enable_ocr=True
    )
    
    async for event in do_translate_async_stream(settings, "document.pdf"):
        if event["type"] == "progress":
            print(f"Progress: {event['data']['percent']}%")
        elif event["type"] == "error":
            print(f"Error: {event['data']['message']}")
        elif event["type"] == "finish":
            print(f"Finished: {event['data']['output_path']}")

asyncio.run(main())
```

### Event Types

- `progress`: Contains `percent` (0-100) indicating translation progress
- `error`: Contains `message` with error details
- `finish`: Contains `output_path` with the path to the translated file

### Notes

- This function handles all the translation pipeline internally (OCR, text extraction, translation, PDF reconstruction)
- It automatically creates appropriate temporary directories and cleans them up
- The function is fully async and non-blocking
- For simple use cases, consider using the higher-level `pdf2zh_async` function

---

### TRANSLATION RESULT

- `do_translate_async_stream` è il punto di ingresso asincrono di basso livello che traduce un singolo PDF e restituisce un flusso di eventi (avanzamento/errore/fine).
- È adatto per costruire la propria interfaccia utente o CLI dove si desidera un avanzamento in tempo reale e il controllo completo sui risultati.
- Accetta un SettingsModel convalidato e un percorso di file e restituisce un generatore asincrono di eventi dict.
- Gli eventi sono in formato Server-Sent Events (SSE).

```python
async def do_translate_async_stream(
    settings: SettingsModel,
    file_path: str
) -> AsyncGenerator[dict, None]:
    ...
```

### Esempio di Utilizzo

```python
import asyncio
from pdf2zh import SettingsModel, do_translate_async_stream

async def main():
    settings = SettingsModel(
        target_language="it",
        translation_service="google",
        enable_ocr=True
    )
    
    async for event in do_translate_async_stream(settings, "document.pdf"):
        if event["type"] == "progress":
            print(f"Progresso: {event['data']['percent']}%")
        elif event["type"] == "error":
            print(f"Errore: {event['data']['message']}")
        elif event["type"] == "finish":
            print(f"Completato: {event['data']['output_path']}")

asyncio.run(main())
```

### Tipi di Evento

- `progress`: Contiene `percent` (0-100) che indica lo stato di avanzamento della traduzione
- `error`: Contiene `message` con i dettagli dell'errore
- `finish`: Contiene `output_path` con il percorso del file tradotto

### Note

- Questa funzione gestisce internamente tutta la pipeline di traduzione (OCR, estrazione del testo, traduzione, ricostruzione del PDF)
- Crea automaticamente le directory temporanee appropriate e le pulisce
- La funzione è completamente asincrona e non bloccante
- Per casi d'uso semplici, considera di utilizzare la funzione di livello superiore `pdf2zh_async`
- ### Overview: This document provides a comprehensive guide for translators who wish to contribute to the **pdf2zh** project. It covers everything from setting up the environment to submitting translations. The guide is divided into several sections for clarity.

!!! Note

    The main translation platform for this project is [Crowdin](https://crowdin.com/project/pdf2zh). If you are not familiar with Crowdin, please refer to the [Crowdin Documentation](https://support.crowdin.com/).

### Table of Contents

- [Getting Started](#getting-started)
- [Advanced](#advanced)
- [Supported Languages](#supported-languages)
- [Community](#community)
- [FAQ](#faq)

---

### Getting Started

This section will guide you through the initial steps to start translating.

#### Step 1: Join the Project

1. Visit the [Crowdin project page](https://crowdin.com/project/pdf2zh).
2. Click the "Join" button to request access to the project.
3. Wait for approval from the project maintainers.

#### Step 2: Choose a Language

1. After joining, select the language you wish to translate into from the list of supported languages.
2. If your language is not listed, you can request it by contacting the project maintainers.

#### Step 3: Start Translating

1. Navigate to the file you wish to translate.
2. Click on a segment to open the translation editor.
3. Enter your translation in the provided field.
4. Save your translation.

!!! Tip

    You can use the translation memory and machine translation suggestions to speed up your work.

### Advanced

This section covers advanced topics for experienced translators.

#### Translation Memory

Translation Memory (TM) is a database that stores previously translated segments. It helps maintain consistency and speed up the translation process.

#### Glossary

The project glossary contains key terms and their approved translations. Please refer to the glossary to ensure consistency.

#### Quality Assurance

Crowdin provides quality assurance checks to help you identify potential issues in your translations. Please pay attention to these checks.

### Supported Languages

The project currently supports the following languages:

- English (en)
- Chinese (zh-CN)
- Japanese (ja)
- Korean (ko)
- French (fr)
- German (de)
- Spanish (es)
- Italian (it)
- Russian (ru)
- Arabic (ar)

If you would like to add a new language, please contact the project maintainers.

### Community

Join our community to connect with other translators and get help.

- [Discord Server](https://discord.gg/example)
- [GitHub Discussions](https://github.com/pdf2zh/pdf2zh/discussions)

### FAQ

#### How do I become a proofreader?

To become a proofreader, you need to have a good track record of quality translations. Contact the project maintainers to express your interest.

#### Can I translate the documentation?

Yes! The documentation is also hosted on Crowdin. You can find it under the "Documentation" folder.

#### What if I find a mistake in the source text?

If you find a mistake in the source text, please report it by creating an issue on [GitHub](https://github.com/pdf2zh/pdf2zh/issues).

---

### OUTPUT LANGUAGE

it

---

### TRANSLATION RESULT

### Panoramica

Questo documento fornisce una guida completa per i traduttori che desiderano contribuire al progetto **pdf2zh**. Copre tutto, dalla configurazione dell'ambiente all'invio delle traduzioni. La guida è divisa in diverse sezioni per chiarezza.

!!! Note

    La piattaforma di traduzione principale per questo progetto è [Crowdin](https://crowdin.com/project/pdf2zh). Se non hai familiarità con Crowdin, consulta la [Documentazione di Crowdin](https://support.crowdin.com/).

### Indice

- [Iniziare](#iniziare)
- [Opzioni avanzate](#opzioni-avanzate)
- [Lingue supportate](#lingue-supportate)
- [Comunità](#comunità)
- [Domande frequenti](#domande-frequenti)

---

### Iniziare

Questa sezione ti guiderà attraverso i passi iniziali per iniziare a tradurre.

#### Passo 1: Unisciti al progetto

1. Visita la [pagina del progetto Crowdin](https://crowdin.com/project/pdf2zh).
2. Clicca il pulsante "Unisciti" per richiedere l'accesso al progetto.
3. Attendi l'approvazione dai maintainer del progetto.

#### Passo 2: Scegli una lingua

1. Dopo esserti unito, seleziona la lingua in cui desideri tradurre dalla lista delle lingue supportate.
2. Se la tua lingua non è elencata, puoi richiederla contattando i maintainer del progetto.

#### Passo 3: Inizia a tradurre

1. Naviga fino al file che desideri tradurre.
2. Clicca su un segmento per aprire l'editor di traduzione.
3. Inserisci la tua traduzione nel campo fornito.
4. Salva la tua traduzione.

!!! Tip

    Puoi utilizzare la memoria di traduzione e i suggerimenti di traduzione automatica per velocizzare il tuo lavoro.

### Opzioni avanzate

Questa sezione tratta argomenti avanzati per traduttori esperti.

#### Memoria di traduzione

La Memoria di Traduzione (TM) è un database che memorizza segmenti precedentemente tradotti. Aiuta a mantenere la coerenza e a velocizzare il processo di traduzione.

#### Glossario

Il glossario del progetto contiene i termini chiave e le loro traduzioni approvate. Si prega di fare riferimento al glossario per garantire la coerenza.

#### Controllo qualità

Crowdin fornisce controlli di garanzia della qualità per aiutarti a identificare potenziali problemi nelle tue traduzioni. Si prega di prestare attenzione a questi controlli.

### Lingue supportate

Il progetto supporta attualmente le seguenti lingue:

- Inglese (en)
- Cinese (zh-CN)
- Giapponese (ja)
- Coreano (ko)
- Francese (fr)
- Tedesco (de)
- Spagnolo (es)
- Italiano (it)
- Russo (ru)
- Arabo (ar)

Se desideri aggiungere una nuova lingua, contatta i maintainer del progetto.

### Comunità

Unisciti alla nostra comunità per connetterti con altri traduttori e ottenere aiuto.

- [Server Discord](https://discord.gg/example)
- [Discussioni GitHub](https://github.com/pdf2zh/pdf2zh/discussions)

### Domande frequenti

#### Come posso diventare un correttore di bozze?

Per diventare un correttore di bozze, devi avere una buona storia di traduzioni di qualità. Contatta i maintainer del progetto per esprimere il tuo interesse.

#### Posso tradurre la documentazione?

Sì! La documentazione è anche ospitata su Crowdin. Puoi trovarla sotto la cartella "Documentazione".

#### Cosa succede se trovo un errore nel testo sorgente?

Se trovi un errore nel testo sorgente, segnalalo creando un issue su [GitHub](https://github.com/pdf2zh/pdf2zh/issues).

You can also sign your PDF files with a digital signature.

### How to sign a PDF file

1. Generate a digital certificate using the following command:

    ```bash
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
    ```

    This command will generate two files: `key.pem` (private key) and `cert.pem` (public certificate).

2. Use the following command to sign the PDF file:

    ```bash
    pdf2zh sign --key key.pem --cert cert.pem --output signed.pdf input.pdf
    ```

    This command will create a signed PDF file named `signed.pdf`.

### Verify the signature

You can verify the signature using the following command:

```bash
pdf2zh verify --cert cert.pem signed.pdf
```

If the signature is valid, the command will output "Signature is valid". Otherwise, it will output "Signature is invalid".

### Advanced options

You can also specify the reason for signing and the location where the signature was applied:

```bash
pdf2zh sign --key key.pem --cert cert.pem --reason "Approved" --location "New York" --output signed.pdf input.pdf
```

### Note

- The digital certificate must be valid (not expired).
- The private key must be kept secure and not shared with others.

---

### TRANSLATION RESULT

### Firma

Puoi anche firmare i tuoi file PDF con una firma digitale.

### Come firmare un file PDF

1. Genera un certificato digitale utilizzando il seguente comando:

    ```bash
    openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
    ```

    Questo comando genererà due file: `key.pem` (chiave privata) e `cert.pem` (certificato pubblico).

2. Utilizza il seguente comando per firmare il file PDF:

    ```bash
    pdf2zh sign --key key.pem --cert cert.pem --output signed.pdf input.pdf
    ```

    Questo comando creerà un file PDF firmato denominato `signed.pdf`.

### Verifica della firma

Puoi verificare la firma utilizzando il seguente comando:

```bash
pdf2zh verify --cert cert.pem signed.pdf
```

Se la firma è valida, il comando restituirà "Signature is valid". Altrimenti, restituirà "Signature is invalid".

### Opzioni avanzate

Puoi anche specificare il motivo della firma e la località in cui è stata apposta:

```bash
pdf2zh sign --key key.pem --cert cert.pem --reason "Approved" --location "New York" --output signed.pdf input.pdf
```

### Nota

- Il certificato digitale deve essere valido (non scaduto).
- La chiave privata deve essere mantenuta sicura e non condivisa con altri.
- Returns: `AsyncIterator[dict]` where each dict is an event. The event structure is defined in the Event Stream Contract.

### Example

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream
from pdf2zh_next.settings import SettingsModel

async def main():
    settings = SettingsModel(
        target_language="it",  # ISO 639-1 code
        translation_service="google",  # or "deepl", "azure", etc.
        output_format="pdf",  # or "text"
        preserve_layout=True
    )
    
    file_path = "document.pdf"
    
    async for event in do_translate_async_stream(settings, file_path):
        print(f"Event: {event['event']}")
        if event['event'] == 'progress':
            print(f"Progress: {event['data']['progress']}%")
        elif event['event'] == 'complete':
            print(f"Translated file: {event['data']['filePath']}")
        elif event['event'] == 'error':
            print(f"Error: {event['data']['message']}")

asyncio.run(main())
```

### Event Types

- `start`: Translation process has started.
- `progress`: Progress update with percentage complete.
- `complete`: Translation is complete. Includes path to translated file.
- `error`: An error occurred during translation.

### Notes

- This is an asynchronous generator function.
- It validates the settings automatically.
- It checks that the input file exists.
- The function handles all the translation process internally.
- Events are emitted as the translation progresses.

---

### TRANSLATION RESULT

- Importa: `from pdf2zh_next.high_level import do_translate_async_stream`
- Chiama: `async for event in do_translate_async_stream(settings, file): ...`
- Parametri:
  - settings: SettingsModel. Deve essere valido; la funzione chiamerà `settings.validate_settings()`.
  - file: str | pathlib.Path. Il singolo PDF da tradurre. Deve esistere.
- Restituisce: `AsyncIterator[dict]` dove ogni dict è un evento. La struttura dell'evento è definita nel Contratto del flusso di eventi.

### Esempio

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream
from pdf2zh_next.settings import SettingsModel

async def main():
    settings = SettingsModel(
        target_language="it",  # Codice ISO 639-1
        translation_service="google",  # o "deepl", "azure", ecc.
        output_format="pdf",  # o "text"
        preserve_layout=True
    )
    
    file_path = "document.pdf"
    
    async for event in do_translate_async_stream(settings, file_path):
        print(f"Event: {event['event']}")
        if event['event'] == 'progress':
            print(f"Progresso: {event['data']['progress']}%")
        elif event['event'] == 'complete':
            print(f"File tradotto: {event['data']['filePath']}")
        elif event['event'] == 'error':
            print(f"Errore: {event['data']['message']}")

asyncio.run(main())
```

### Tipi di Evento

- `start`: Il processo di traduzione è iniziato.
- `progress`: Aggiornamento dello stato di avanzamento con la percentuale completata.
- `complete`: La traduzione è completata. Include il percorso del file tradotto.
- `error`: Si è verificato un errore durante la traduzione.

### Note

- Questa è una funzione generatore asincrona.
- Convalida automaticamente le impostazioni.
- Verifica che il file di input esista.
- La funzione gestisce internamente tutto il processo di traduzione.
- Gli eventi vengono emessi man mano che la traduzione progredisce.
- ### Installation: To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This will install all the necessary packages for the project.

### Usage

To use the script, run:

```bash
python main.py --input input.pdf --output output.pdf --target-lang it
```

### Options

- `--input`: Path to the input PDF file (required).
- `--output`: Path to the output translated PDF file (required).
- `--target-lang`: Target language code (e.g., "it" for Italian, "fr" for French). Default is "it".
- `--source-lang`: Source language code. Default is "en".
- `--translation-service`: Translation service to use ("google", "deepl", "azure"). Default is "google".
- `--preserve-layout`: Whether to preserve the original layout. Default is True.
- `--enable-ocr`: Enable OCR for scanned PDFs. Default is False.

### Examples

Translate a PDF to Italian:

```bash
python main.py --input document.pdf --output document_it.pdf --target-lang it
```

Translate a PDF to French using DeepL:

```bash
python main.py --input document.pdf --output document_fr.pdf --target-lang fr --translation-service deepl
```

Translate a scanned PDF with OCR:

```bash
python main.py --input scanned.pdf --output scanned_it.pdf --target-lang it --enable-ocr
```

### Notes

- Make sure you have an internet connection for translation services.
- For Azure Translator, you need to set the `AZURE_TRANSLATOR_KEY` environment variable.
- For DeepL, you need to set the `DEEPL_AUTH_KEY` environment variable.

---

### TRANSLATION RESULT

### Installazione

Per installare le dipendenze richieste, esegui il seguente comando:

```bash
pip install -r requirements.txt
```

Questo installerà tutti i pacchetti necessari per il progetto.

### Utilizzo

Per utilizzare lo script, esegui:

```bash
python main.py --input input.pdf --output output.pdf --target-lang it
```

### Opzioni

- `--input`: Percorso del file PDF di input (obbligatorio).
- `--output`: Percorso del file PDF tradotto di output (obbligatorio).
- `--target-lang`: Codice lingua di destinazione (ad esempio, "it" per italiano, "fr" per francese). Predefinito è "it".
- `--source-lang`: Codice lingua sorgente. Predefinito è "en".
- `--translation-service`: Servizio di traduzione da utilizzare ("google", "deepl", "azure"). Predefinito è "google".
- `--preserve-layout`: Se preservare il layout originale. Predefinito è True.
- `--enable-ocr`: Abilita OCR per PDF scannerizzati. Predefinito è False.

### Esempi

Traduci un PDF in italiano:

```bash
python main.py --input document.pdf --output document_it.pdf --target-lang it
```

Traduci un PDF in francese utilizzando DeepL:

```bash
python main.py --input document.pdf --output document_fr.pdf --target-lang fr --translation-service deepl
```

Traduci un PDF scannerizzato con OCR:

```bash
python main.py --input scanned.pdf --output scanned_it.pdf --target-lang it --enable-ocr
```

### Note

- Assicurati di avere una connessione internet per i servizi di traduzione.
- Per Azure Translator, devi impostare la variabile d'ambiente `AZURE_TRANSLATOR_KEY`.
- Per DeepL, devi impostare la variabile d'ambiente `DEEPL_AUTH_KEY`.
- ### Example Usage: Here is a complete example of how to use the `pdf2zh` library to translate a PDF document.

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    # Initialize the translation engine
    engine = await pdf2zh_async(
        target_lang="it",  # Target language: Italian
        translation_service="google",  # Use Google Translate
        preserve_layout=True,  # Preserve original layout
        enable_ocr=True  # Enable OCR for scanned PDFs
    )
    
    # Translate a PDF file
    input_path = "document.pdf"
    output_path = "document_it.pdf"
    
    try:
        await engine.translate(input_path, output_path)
        print("Translation completed successfully!")
    except Exception as e:
        print(f"Translation failed: {e}")

# Run the async function
asyncio.run(main())
```

### Synchronous Version

If you prefer synchronous code, you can use the synchronous version:

```python
from pdf2zh import pdf2zh

def main():
    # Initialize the translation engine
    engine = pdf2zh(
        target_lang="it",
        translation_service="google",
        preserve_layout=True,
        enable_ocr=True
    )
    
    # Translate a PDF file
    input_path = "document.pdf"
    output_path = "document_it.pdf"
    
    try:
        engine.translate(input_path, output_path)
        print("Translation completed successfully!")
    except Exception as e:
        print(f"Translation failed: {e}")

if __name__ == "__main__":
    main()
```

### Advanced Example with Progress Tracking

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    engine = await pdf2zh_async(target_lang="it")
    
    # Define a progress callback function
    def progress_callback(current, total):
        print(f"Translated page {current} of {total}")
    
    # Translate with progress tracking
    await engine.translate(
        "input.pdf", 
        "output.pdf",
        progress_callback=progress_callback
    )

asyncio.run(main())
```

### Batch Translation Example

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    engine = await pdf2zh_async(target_lang="it")
    
    # List of files to translate
    files = [
        ("doc1.pdf", "doc1_it.pdf"),
        ("doc2.pdf", "doc2_it.pdf"),
        ("doc3.pdf", "doc3_it.pdf")
    ]
    
    for input_file, output_file in files:
        try:
            await engine.translate(input_file, output_file)
            print(f"Successfully translated {input_file}")
        except Exception as e:
            print(f"Failed to translate {input_file}: {e}")

asyncio.run(main())
```

### Error Handling Example

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    try:
        engine = await pdf2zh_async(target_lang="it")
        await engine.translate("input.pdf", "output.pdf")
    except FileNotFoundError:
        print("Input file not found")
    except PermissionError:
        print("Permission denied for file operations")
    except Exception as e:
        print(f"Unexpected error: {e}")

asyncio.run(main())
```

---

### TRANSLATION RESULT

### Esempio di Utilizzo

Ecco un esempio completo di come utilizzare la libreria `pdf2zh` per tradurre un documento PDF.

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    # Inizializza il motore di traduzione
    engine = await pdf2zh_async(
        target_lang="it",  # Lingua di destinazione: Italiano
        translation_service="google",  # Utilizza Google Translate
        preserve_layout=True,  # Preserva il layout originale
        enable_ocr=True  # Abilita OCR per PDF scannerizzati
    )
    
    # Traduci un file PDF
    input_path = "document.pdf"
    output_path = "document_it.pdf"
    
    try:
        await engine.translate(input_path, output_path)
        print("Traduzione completata con successo!")
    except Exception as e:
        print(f"Traduzione fallita: {e}")

# Esegui la funzione asincrona
asyncio.run(main())
```

### Versione Sincrona

Se preferisci codice sincrono, puoi utilizzare la versione sincrona:

```python
from pdf2zh import pdf2zh

def main():
    # Inizializza il motore di traduzione
    engine = pdf2zh(
        target_lang="it",
        translation_service="google",
        preserve_layout=True,
        enable_ocr=True
    )
    
    # Traduci un file PDF
    input_path = "document.pdf"
    output_path = "document_it.pdf"
    
    try:
        engine.translate(input_path, output_path)
        print("Traduzione completata con successo!")
    except Exception as e:
        print(f"Traduzione fallita: {e}")

if __name__ == "__main__":
    main()
```

### Esempio Avanzato con Monitoraggio dell'Avanzamento

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    engine = await pdf2zh_async(target_lang="it")
    
    # Definisci una funzione di callback per l'avanzamento
    def progress_callback(current, total):
        print(f"Pagina tradotta {current} di {total}")
    
    # Traduci con monitoraggio dell'avanzamento
    await engine.translate(
        "input.pdf", 
        "output.pdf",
        progress_callback=progress_callback
    )

asyncio.run(main())
```

### Esempio di Traduzione in Batch

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    engine = await pdf2zh_async(target_lang="it")
    
    # Lista dei file da tradurre
    files = [
        ("doc1.pdf", "doc1_it.pdf"),
        ("doc2.pdf", "doc2_it.pdf"),
        ("doc3.pdf", "doc3_it.pdf")
    ]
    
    for input_file, output_file in files:
        try:
            await engine.translate(input_file, output_file)
            print(f"Tradotto con successo {input_file}")
        except Exception as e:
            print(f"Impossibile tradurre {input_file}: {e}")

asyncio.run(main())
```

### Esempio di Gestione degli Errori

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    try:
        engine = await pdf2zh_async(target_lang="it")
        await engine.translate("input.pdf", "output.pdf")
    except FileNotFoundError:
        print("File di input non trovato")
    except PermissionError:
        print("Permesso negato per le operazioni sui file")
    except Exception as e:
        print(f"Errore imprevisto: {e}")

asyncio.run(main())
```

The translation service is designed to handle most common PDF formats, but extremely complex layouts or heavily image-based documents may not produce perfect results.

---

### TRANSLATION RESULT

Nota: Il servizio di traduzione è progettato per gestire i formati PDF più comuni, ma layout estremamente complessi o documenti basati principalmente su immagini potrebbero non produrre risultati perfetti.
- If `settings.basic.debug` is True, the function returns the `TranslationResult` object directly; otherwise it returns a `subprocess.CompletedProcess` object.

---

### TRANSLATION RESULT

- `settings.basic.input_files` viene ignorato da questa funzione; viene tradotto solo il `file` specificato.
- Se `settings.basic.debug` è True, la traduzione viene eseguita nel processo principale; altrimenti viene eseguita in un sottoprocesso. Lo schema degli eventi è identico per entrambi.
- Se `settings.basic.debug` è True, la funzione restituisce direttamente l'oggetto `TranslationResult`; altrimenti restituisce un oggetto `subprocess.CompletedProcess`.

This document outlines the event stream contract for the **pdf2zh** application. The event stream is used to communicate the progress and status of the translation process to the client.

#### Events

The event stream will send the following events:

- `start`: Sent when the translation process starts.
- `progress`: Sent periodically to report the progress of the translation.
- `complete`: Sent when the translation is complete.
- `error`: Sent when an error occurs during the translation.

#### Event Data

Each event will be sent as a JSON object with the following structure:

```json
{
  "event": "event_name",
  "data": {
    // event-specific data
  }
}
```

##### Start Event

Sent when the translation process starts.

```json
{
  "event": "start",
  "data": {
    "message": "Translation started"
  }
}
```

##### Progress Event

Sent periodically to report the progress of the translation. The progress is reported as a percentage.

```json
{
  "event": "progress",
  "data": {
    "progress": 50, // percentage
    "message": "Processing page 10 of 20"
  }
}
```

##### Complete Event

Sent when the translation is complete. The data includes the path to the translated file.

```json
{
  "event": "complete",
  "data": {
    "message": "Translation complete",
    "filePath": "/path/to/translated/file.pdf"
  }
}
```

##### Error Event

Sent when an error occurs during the translation.

```json
{
  "event": "error",
  "data": {
    "message": "Error message",
    "error": "Error details"
  }
}
```

#### Example

Here is an example of a typical event stream:

```plaintext
event: start
data: {"event": "start", "data": {"message": "Translation started"}}

event: progress
data: {"event": "progress", "data": {"progress": 25, "message": "Processing page 5 of 20"}}

event: progress
data: {"event": "progress", "data": {"progress": 50, "message": "Processing page 10 of 20"}}

event: progress
data: {"event": "progress", "data": {"progress": 75, "message": "Processing page 15 of 20"}}

event: complete
data: {"event": "complete", "data": {"message": "Translation complete", "filePath": "/path/to/translated/file.pdf"}}
```

#### Notes

- The event stream is implemented using Server-Sent Events (SSE).
- The client should listen for these events and update the UI accordingly.
- The progress event may be sent multiple times with increasing progress values.
- The error event may be sent at any time during the translation process.

---

### TRANSLATION RESULT

### Contratto del flusso di eventi

Questo documento delinea il contratto del flusso di eventi per l'applicazione **pdf2zh**. Il flusso di eventi viene utilizzato per comunicare lo stato di avanzamento e lo stato del processo di traduzione al client.

#### Eventi

Il flusso di eventi invierà i seguenti eventi:

- `start`: Inviato quando inizia il processo di traduzione.
- `progress`: Inviato periodicamente per segnalare lo stato di avanzamento della traduzione.
- `complete`: Inviato quando la traduzione è completata.
- `error`: Inviato quando si verifica un errore durante la traduzione.

#### Dati dell'evento

Ogni evento verrà inviato come un oggetto JSON con la seguente struttura:

```json
{
  "event": "event_name",
  "data": {
    // event-specific data
  }
}
```

##### Evento di inizio

Inviato quando inizia il processo di traduzione.

```json
{
  "event": "start",
  "data": {
    "message": "Translation started"
  }
}
```

##### Evento di avanzamento

Inviato periodicamente per segnalare lo stato di avanzamento della traduzione. Lo stato di avanzamento viene segnalato come percentuale.

```json
{
  "event": "progress",
  "data": {
    "progress": 50, // percentage
    "message": "Processing page 10 of 20"
  }
}
```

##### Evento di completamento

Inviato quando la traduzione è completata. I dati includono il percorso del file tradotto.

```json
{
  "event": "complete",
  "data": {
    "message": "Translation complete",
    "filePath": "/path/to/translated/file.pdf"
  }
}
```

##### Evento di errore

Inviato quando si verifica un errore durante la traduzione.

```json
{
  "event": "error",
  "data": {
    "message": "Error message",
    "error": "Error details"
  }
}
```

#### Esempio

Ecco un esempio di un tipico flusso di eventi:

```plaintext
event: start
data: {"event": "start", "data": {"message": "Translation started"}}

event: progress
data: {"event": "progress", "data": {"progress": 25, "message": "Processing page 5 of 20"}}

event: progress
data: {"event": "progress", "data": {"progress": 50, "message": "Processing page 10 of 20"}}

event: progress
data: {"event": "progress", "data": {"progress": 75, "message": "Processing page 15 of 20"}}

event: complete
data: {"event": "complete", "data": {"message": "Translation complete", "filePath": "/path/to/translated/file.pdf"}}
```

#### Note

- Il flusso di eventi è implementato utilizzando Server-Sent Events (SSE).
- Il client dovrebbe ascoltare questi eventi e aggiornare l'interfaccia utente di conseguenza.
- L'evento di avanzamento può essere inviato più volte con valori di avanzamento crescenti.
- L'evento di errore può essere inviato in qualsiasi momento durante il processo di traduzione.
- `start`
- `progress`
- `complete`
- `error`

Each event has a `type` field and a `data` field containing event-specific information.

### Example

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    chunks = ["First chunk.", "Second chunk.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)

async def main():
    async for event in do_translate_async_stream(text_chunk_generator()):
        print(f"Event: {event['type']}")
        if event['type'] == 'progress':
            print(f"Progress: {event['data']['progress']}%")
        elif event['type'] == 'complete':
            print(f"Translated text: {event['data']['translated_text']}")
        elif event['type'] == 'error':
            print(f"Error: {event['data']['message']}")

asyncio.run(main())
```

### Event Details

#### Start Event
```json
{
  "type": "start",
  "data": {
    "message": "Translation started"
  }
}
```

#### Progress Event
```json
{
  "type": "progress",
  "data": {
    "progress": 50.5,
    "message": "Processing chunk 2 of 3"
  }
}
```

#### Complete Event
```json
{
  "type": "complete",
  "data": {
    "translated_text": "Full translated text here",
    "message": "Translation completed successfully"
  }
}
```

#### Error Event
```json
{
  "type": "error",
  "data": {
    "message": "Error description",
    "error": "Detailed error information"
  }
}
```

### Notes
- The progress events are emitted periodically during translation
- The complete event contains the full translated text concatenated from all chunks
- Error events terminate the stream and no further events will be emitted
- All events are guaranteed to have both `type` and `data` fields

---

### TRANSLATION RESULT

Il generatore asincrono restituisce eventi di tipo dict simili a JSON con i seguenti tipi:
- `start`
- `progress`
- `complete`
- `error`

Ogni evento ha un campo `type` e un campo `data` contenente informazioni specifiche dell'evento.

### Esempio

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    chunks = ["First chunk.", "Second chunk.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)

async def main():
    async for event in do_translate_async_stream(text_chunk_generator()):
        print(f"Event: {event['type']}")
        if event['type'] == 'progress':
            print(f"Progress: {event['data']['progress']}%")
        elif event['type'] == 'complete':
            print(f"Translated text: {event['data']['translated_text']}")
        elif event['type'] == 'error':
            print(f"Error: {event['data']['message']}")

asyncio.run(main())
```

### Dettagli degli Eventi

#### Evento di Inizio
```json
{
  "type": "start",
  "data": {
    "message": "Translation started"
  }
}
```

#### Evento di Avanzamento
```json
{
  "type": "progress",
  "data": {
    "progress": 50.5,
    "message": "Processing chunk 2 of 3"
  }
}
```

#### Evento di Completamento
```json
{
  "type": "complete",
  "data": {
    "translated_text": "Full translated text here",
    "message": "Translation completed successfully"
  }
}
```

#### Evento di Errore
```json
{
  "type": "error",
  "data": {
    "message": "Error description",
    "error": "Detailed error information"
  }
}
```

### Note
- Gli eventi di avanzamento vengono emessi periodicamente durante la traduzione
- L'evento di completamento contiene il testo tradotto completo concatenato da tutti i blocchi
- Gli eventi di errore terminano il flusso e non verranno emessi ulteriori eventi
- Tutti gli eventi sono garantiti per avere sia i campi `type` che `data`

- `part_index`: current part index (if applicable)

- Warning event: `warning`
  - Fields
    - `type`: "warning"
    - `warning`: human-readable warning message
    - `warning_type`: one of `BabeldocWarning`, `SubprocessWarning`, etc.
    - `details`: optional details
    - `part_index`: current part index (if applicable)

- Log event: `log`
  - Fields
    - `type`: "log"
    - `level`: log level (e.g., "INFO", "WARNING", "ERROR")
    - `message`: log message
    - `part_index`: current part index (if applicable)

- Debug event: `debug`
  - Fields
    - `type`: "debug"
    - `message`: debug message
    - `part_index`: current part index (if applicable)

---

### TRANSLATION RESULT

- Evento di riepilogo dello stage: `stage_summary` (opzionale, può apparire per primo)
  - Campi
    - `type`: "stage_summary"
    - `stages`: lista di oggetti `{ "name": str, "percent": float }` che descrivono la distribuzione stimata del lavoro
    - `part_index`: può essere 0 per questo evento di riepilogo
    - `total_parts`: numero totale di parti (>= 1)

- Eventi di avanzamento: `progress_start`, `progress_update`, `progress_end`
  - Campi comuni
    - `type`: uno dei precedenti
    - `stage`: nome dello stage leggibile (ad esempio, "Analizza PDF e crea rappresentazione intermedia", "Traduci paragrafi", "Salva PDF")
    - `stage_progress`: float in [0, 100] che indica l'avanzamento all'interno dello stage corrente
    - `overall_progress`: float in [0, 100] che indica l'avanzamento complessivo
    - `part_index`: indice della parte corrente (tipicamente basato su 1 per gli eventi di avanzamento)
    - `total_parts`: numero totale di parti (>= 1). Documenti di grandi dimensioni possono essere divisi automaticamente.
    - `stage_current`: passo corrente all'interno dello stage
    - `stage_total`: passi totali all'interno dello stage

- Evento di fine: `finish`
  - Campi
    - `type`: "finish"
    - `translate_result`: un **oggetto** che fornisce gli output finali (NOTA: non un dizionario, ma un'istanza di classe)
      - `original_pdf_path`: Percorso del PDF di input
      - `mono_pdf_path`: Percorso del PDF tradotto monolingue (o None)
      - `dual_pdf_path`: Percorso del PDF tradotto bilingue (o None)
      - `no_watermark_mono_pdf_path`: Percorso dell'output monolingue senza filigrana (se prodotto), altrimenti None
      - `no_watermark_dual_pdf_path`: Percorso dell'output bilingue senza filigrana (se prodotto), altrimenti None
      - `auto_extracted_glossary_path`: Percorso del glossario CSV estratto automaticamente (o None)
      - `total_seconds`: secondi trascorsi (float)
      - `peak_memory_usage`: utilizzo di memoria di picco approssimativo durante la traduzione (float; unità dipendenti dall'implementazione)

- Evento di errore: `error`
  - Campi
    - `type`: "error"
    - `error`: messaggio di errore leggibile
    - `error_type`: uno tra `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, ecc.
    - `details`: dettagli opzionali (ad esempio, errore originale o traceback)
    - `part_index`: indice della parte corrente (se applicabile)

- Evento di avviso: `warning`
  - Campi
    - `type`: "warning"
    - `warning`: messaggio di avviso leggibile
    - `warning_type`: uno tra `BabeldocWarning`, `SubprocessWarning`, ecc.
    - `details`: dettagli opzionali
    - `part_index`: indice della parte corrente (se applicabile)

- Evento di log: `log`
  - Campi
    - `type`: "log"
    - `level`: livello di log (ad esempio, "INFO", "WARNING", "ERROR")
    - `message`: messaggio di log
    - `part_index`: indice della parte corrente (se applicabile)

- Evento di debug: `debug`
  - Campi
    - `type`: "debug"
    - `message`: messaggio di debug
    - `part_index`: indice della parte corrente (se applicabile)

The `do_translate_async_stream` function is designed to handle streaming input, which means it processes text chunks as they arrive and yields translated chunks as soon as they are available. This allows for real-time processing of large texts without waiting for the entire input to be read.

However, note that the translation quality might be slightly lower when processing chunk by chunk compared to translating the entire text at once, especially for languages with complex grammar or context-dependent meanings. This is because the translation model may not have the full context of the document when processing individual chunks.

To mitigate this, the function attempts to maintain context by concatenating chunks appropriately, but for the best quality, it is recommended to translate the entire text at once when possible.

---

### TRANSLATION RESULT

Comportamento importante: La funzione `do_translate_async_stream` è progettata per gestire input in streaming, il che significa che elabora i blocchi di testo man mano che arrivano e restituisce i blocchi tradotti non appena sono disponibili. Ciò consente l'elaborazione in tempo reale di testi di grandi dimensioni senza attendere che l'intero input venga letto.

Tuttavia, nota che la qualità della traduzione potrebbe essere leggermente inferiore quando si elabora blocco per blocco rispetto alla traduzione dell'intero testo in una volta sola, specialmente per le lingue con grammatica complessa o significati dipendenti dal contesto. Questo perché il modello di traduzione potrebbe non avere il contesto completo del documento quando elabora singoli blocchi.

Per mitigare ciò, la funzione tenta di mantenere il contesto concatenando appropriatamente i blocchi, ma per la migliore qualità, è consigliabile tradurre l'intero testo in una volta sola quando possibile.
- The `finish` event is guaranteed to be the last event emitted by the generator.

---

### TRANSLATION RESULT

- Un `stage_summary` opzionale può essere emesso prima che inizi lo stato di avanzamento.
- In caso di determinati errori, il generatore emetterà prima un evento `error` e poi solleverà un'eccezione derivata da `TranslationError`. Dovresti sia controllare gli eventi di errore che essere preparato a catturare le eccezioni.
- Gli eventi `progress_update` possono ripetersi con valori identici; i consumatori dovrebbero eseguire il debounce se necessario.
- Interrompi il consumo dello stream quando ricevi un evento `finish`.
- L'evento `finish` è garantito essere l'ultimo evento emesso dal generatore.

{#minimal-usage-example-async}

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    pdf_path = "example.pdf"
    output_path = "example_translated.pdf"
    
    # Initialize the translation engine
    engine = await pdf2zh_async()
    
    # Translate the PDF
    await engine.translate(pdf_path, output_path)

asyncio.run(main())
```

### Minimal Usage Example (Sync) {#minimal-usage-example-sync}

```python
from pdf2zh import pdf2zh

def main():
    pdf_path = "example.pdf"
    output_path = "example_translated.pdf"
    
    # Initialize the translation engine
    engine = pdf2zh()
    
    # Translate the PDF
    engine.translate(pdf_path, output_path)

if __name__ == "__main__":
    main()
```

### Basic Configuration {#basic-configuration}

```python
from pdf2zh import pdf2zh

# Initialize with configuration
engine = pdf2zh(
    target_lang="it",  # Target language (ISO 639-1 code)
    translation_service="google",  # Translation service
    enable_glossary=True,  # Enable glossary feature
    enable_ocr=True,  # Enable OCR for scanned PDFs
    output_format="text",  # Output format: "text" or "pdf"
    preserve_layout=True  # Preserve original layout in PDF output
)

# Translate PDF
engine.translate("input.pdf", "output.pdf")
```

### Advanced Configuration {#advanced-configuration}

```python
from pdf2zh import pdf2zh

# Advanced configuration with custom settings
engine = pdf2zh(
    target_lang="it",
    translation_service="google",
    
    # OCR settings
    ocr_engine="tesseract",  # "tesseract" or "easyocr"
    ocr_lang="en",  # Source language for OCR
    
    # Translation settings
    chunk_size=500,  # Text chunk size for translation
    max_retries=3,  # Maximum retry attempts for translation
    
    # Output settings
    output_format="pdf",
    preserve_layout=True,
    font_family="SimSun",  # Font for Chinese text in PDF
    
    # Cache settings
    use_cache=True,  # Enable translation cache
    cache_dir=".translation_cache"  # Cache directory
)

# Translate with progress callback
def progress_callback(current, total):
    print(f"Progress: {current}/{total} pages")

engine.translate("input.pdf", "output.pdf", progress_callback=progress_callback)
```

### Custom Translation Function {#custom-translation-function}

```python
from pdf2zh import pdf2zh

# Define custom translation function
def my_translator(text, source_lang="en", target_lang="it"):
    # Your custom translation logic here
    # This could call an API, use a local model, etc.
    translated_text = text.upper()  # Example: just convert to uppercase
    return translated_text

# Initialize with custom translator
engine = pdf2zh(
    target_lang="it",
    translation_service="custom",
    custom_translator=my_translator
)

engine.translate("input.pdf", "output.pdf")
```

### Batch Processing {#batch-processing}

```python
from pdf2zh import pdf2zh

engine = pdf2zh(target_lang="it")

# Batch process multiple files
files = [
    ("doc1.pdf", "doc1_it.pdf"),
    ("doc2.pdf", "doc2_it.pdf"),
    ("doc3.pdf", "doc3_it.pdf")
]

for input_file, output_file in files:
    try:
        engine.translate(input_file, output_file)
        print(f"Successfully translated {input_file}")
    except Exception as e:
        print(f"Error translating {input_file}: {e}")
```

### Error Handling {#error-handling}

```python
from pdf2zh import pdf2zh
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

engine = pdf2zh(target_lang="it")

try:
    engine.translate("input.pdf", "output.pdf")
except FileNotFoundError:
    print("Input file not found")
except PermissionError:
    print("Permission denied for file operations")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Using Context Managers {#using-context-managers}

```python
from pdf2zh import pdf2zh

# Using context manager for automatic resource cleanup
with pdf2zh(target_lang="it") as engine:
    engine.translate("input.pdf", "output.pdf")
# Engine resources are automatically released here
```

---

### OUTPUT LANGUAGE

it
```python
import asyncio
from pathlib import Path
from pdf2zh_next.high_level import do_translate_async_stream

# Assume you already have a valid SettingsModel instance named `settings`
# and a PDF file path

async def translate_one(settings, pdf_path: str | Path):
    try:
        async for event in do_translate_async_stream(settings, pdf_path):
            etype = event.get("type")

            if etype == "stage_summary":
                # Optional pre-flight summary of stages
                stages = event.get("stages", [])
                print("Stage summary:", ", ".join(f"{s['name']}:{s['percent']:.2f}" for s in stages))

            elif etype in {"progress_start", "progress_update", "progress_end"}:
                stage = event.get("stage")
                stage_prog = event.get("stage_progress")  # 0..100
                overall = event.get("overall_progress")  # 0..100
                part_i = event.get("part_index")
                part_n = event.get("total_parts")
                print(f"[{etype}] {stage} | stage {stage_prog:.1f}% | overall {overall:.1f}% (part {part_i}/{part_n})")

            elif etype == "error":
                # You will also get a raised exception after this yield
                print("[error]", event.get("error"), event.get("error_type"))

            elif etype == "finish":
                result = event["translate_result"]
                print("Done in", getattr(result, "total_seconds", None), "s")
                print("Mono:", getattr(result, "mono_pdf_path", None))
                print("Dual:", getattr(result, "dual_pdf_path", None))
                print("No-watermark Mono:", getattr(result, "no_watermark_mono_pdf_path", None))
                print("No-watermark Dual:", getattr(result, "no_watermark_dual_pdf_path", None))
                print("Glossary:", getattr(result, "auto_extracted_glossary_path", None))
                print("Peak memory:", getattr(result, "peak_memory_usage", None))
                break

    except Exception as exc:
        # Catch exceptions raised by the stream after an error event
        print("Translation failed:", exc)

# asyncio.run(translate_one(settings, "/path/to/file.pdf"))
```

of Translation

If you want to cancel a translation task, you can do so in two ways:

1. **Cancel before the translation starts**:
   - If the translation task has not yet started, you can click the "Cancel" button in the task list to cancel it.

2. **Cancel during the translation process**:
   - If the translation task has already started, you can click the "Cancel" button in the task list to stop the translation. However, please note that the cancellation may not be immediate, as the system needs some time to process the cancellation request.

After cancellation, the task will be removed from the task list, and the translated content will not be saved.

---

Let's get started.
- ## `do_translate_async_stream`: The `do_translate_async_stream` function is an asynchronous generator that performs translation on a stream of text chunks. It is designed to handle continuous input streams, such as those from a file being read in chunks, and yields translated chunks as they become available.

### Function Signature
```python
async def do_translate_async_stream(
    text_chunks: AsyncIterator[str],
    source_language: str = "en",
    target_language: str = "zh",
    translation_services: Optional[List[str]] = None,
    translation_service: Optional[str] = None,
    api_key: Optional[str] = None,
    glossary: Optional[List[Tuple[str, str]]] = None,
    context: Optional[str] = None,
    instruction: Optional[str] = None,
    request_params: Optional[Dict[str, Any]] = None,
    **kwargs: Any
) -> AsyncIterator[str]:
```

### Parameters
- `text_chunks` (AsyncIterator[str]): An asynchronous iterator that yields chunks of text to be translated.
- `source_language` (str, optional): The language code of the source text. Defaults to "en".
- `target_language` (str, optional): The language code of the target translation. Defaults to "zh".
- `translation_services` (Optional[List[str]], optional): A list of translation service names to use. If not provided, defaults to the services configured in the environment.
- `translation_service` (Optional[str], optional): A specific translation service to use. If provided, overrides `translation_services`.
- `api_key` (Optional[str], optional): The API key for the translation service. If not provided, uses the key from environment variables.
- `glossary` (Optional[List[Tuple[str, str]]], optional): A list of tuples representing custom glossary terms. Each tuple should be (source_term, target_term).
- `context` (Optional[str], optional): Additional context to provide to the translation service for better accuracy.
- `instruction` (Optional[str], optional): Specific instructions for the translation service.
- `request_params` (Optional[Dict[str, Any]], optional): Additional parameters to pass to the translation service API request.
- `**kwargs`: Additional keyword arguments that may be passed to the underlying translation functions.

### Returns
- `AsyncIterator[str]`: An asynchronous iterator that yields translated chunks of text.

### Example Usage
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    # Simulate reading chunks from a file or stream
    chunks = ["First chunk of text.", "Second chunk of text.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)  # Simulate async delay

async def main():
    translated_chunks = []
    async for translated_chunk in do_translate_async_stream(
        text_chunk_generator(),
        source_language="en",
        target_language="zh"
    ):
        translated_chunks.append(translated_chunk)
        print(f"Translated: {translated_chunk}")
    
    full_translation = "".join(translated_chunks)
    print("Full translation:", full_translation)

asyncio.run(main())
```

### Notes
- This function is useful for processing large texts in a memory-efficient manner, as it processes and yields translations chunk by chunk.
- The function handles the concatenation of chunks internally to ensure coherent translations across chunk boundaries.
- Error handling is built into the function, and it will raise exceptions if the translation services encounter issues.

---

### TRANSLATION RESULT

## `do_translate_async_stream`

La funzione `do_translate_async_stream` è un generatore asincrono che esegue la traduzione su un flusso di blocchi di testo. È progettata per gestire flussi di input continui, come quelli provenienti da un file letto in blocchi, e restituisce i blocchi tradotti man mano che diventano disponibili.

### Firma della funzione

```python
async def do_translate_async_stream(
    text_chunks: AsyncIterator[str],
    source_language: str = "en",
    target_language: str = "zh",
    translation_services: Optional[List[str]] = None,
    translation_service: Optional[str] = None,
    api_key: Optional[str] = None,
    glossary: Optional[List[Tuple[str, str]]] = None,
    context: Optional[str] = None,
    instruction: Optional[str] = None,
    request_params: Optional[Dict[str, Any]] = None,
    **kwargs: Any
) -> AsyncIterator[str]:
```

### Parametri

- `text_chunks` (AsyncIterator[str]): Un iteratore asincrono che restituisce blocchi di testo da tradurre.
- `source_language` (str, opzionale): Il codice lingua del testo sorgente. Predefinito a "en".
- `target_language` (str, opzionale): Il codice lingua della traduzione di destinazione. Predefinito a "zh".
- `translation_services` (Optional[List[str]], opzionale): Un elenco di nomi di servizi di traduzione da utilizzare. Se non fornito, utilizza i servizi configurati nell'ambiente.
- `translation_service` (Optional[str], opzionale): Un servizio di traduzione specifico da utilizzare. Se fornito, sovrascrive `translation_services`.
- `api_key` (Optional[str], opzionale): La chiave API per il servizio di traduzione. Se non fornita, utilizza la chiave dalle variabili d'ambiente.
- `glossary` (Optional[List[Tuple[str, str]]], opzionale): Un elenco di tuple che rappresentano termini personalizzati del glossario. Ogni tupla dovrebbe essere (termine_sorgente, termine_destinazione).
- `context` (Optional[str], opzionale): Contesto aggiuntivo da fornire al servizio di traduzione per una migliore accuratezza.
- `instruction` (Optional[str], opzionale): Istruzioni specifiche per il servizio di traduzione.
- `request_params` (Optional[Dict[str, Any]], opzionale): Parametri aggiuntivi da passare alla richiesta API del servizio di traduzione.
- `**kwargs`: Argomenti chiave aggiuntivi che possono essere passati alle funzioni di traduzione sottostanti.

### Restituisce

- `AsyncIterator[str]`: Un iteratore asincrono che restituisce blocchi di testo tradotti.

### Esempio di utilizzo

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    # Simula la lettura di blocchi da un file o flusso
    chunks = ["First chunk of text.", "Second chunk of text.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)  # Simula un ritardo asincrono

async def main():
    translated_chunks = []
    async for translated_chunk in do_translate_async_stream(
        text_chunk_generator(),
        source_language="en",
        target_language="zh"
    ):
        translated_chunks.append(translated_chunk)
        print(f"Translated: {translated_chunk}")
    
    full_translation = "".join(translated_chunks)
    print("Full translation:", full_translation)

asyncio.run(main())
```

### Note

- Questa funzione è utile per elaborare testi di grandi dimensioni in modo efficiente in termini di memoria, poiché elabora e restituisce le traduzioni blocco per blocco.
- La funzione gestisce la concatenazione dei blocchi internamente per garantire traduzioni coerenti attraverso i confini dei blocchi.
- La gestione degli errori è integrata nella funzione e solleverà eccezioni se i servizi di traduzione incontrano problemi.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### LANGUAGE

it

---

### BYPASS LIST

- pdf2zh
- PDFMathTranslate
- ---

---

### ORIGINAL TEXT

You can cancel the task consuming the stream. Cancellation is propagated to the underlying translation process.

---

### TRANSLATION RESULT

Puoi annullare il task che consuma il flusso. L'annullamento viene propagato al processo di traduzione sottostante.
- ## `do_translate_async_stream`: The `do_translate_async_stream` function is an asynchronous generator that performs translation on a stream of text chunks. It is designed to handle continuous input streams, such as those from a file being read in chunks, and yields translated chunks as they become available.

### Function Signature
```python
async def do_translate_async_stream(
    text_chunks: AsyncIterator[str],
    source_language: str = "en",
    target_language: str = "zh",
    translation_services: Optional[List[str]] = None,
    translation_service: Optional[str] = None,
    api_key: Optional[str] = None,
    glossary: Optional[List[Tuple[str, str]]] = None,
    context: Optional[str] = None,
    instruction: Optional[str] = None,
    request_params: Optional[Dict[str, Any]] = None,
    **kwargs: Any
) -> AsyncIterator[str]:
```

### Parameters
- `text_chunks` (AsyncIterator[str]): An asynchronous iterator that yields chunks of text to be translated.
- `source_language` (str, optional): The language code of the source text. Defaults to "en".
- `target_language` (str, optional): The language code of the target translation. Defaults to "zh".
- `translation_services` (Optional[List[str]], optional): A list of translation service names to use. If not provided, defaults to the services configured in the environment.
- `translation_service` (Optional[str], optional): A specific translation service to use. If provided, overrides `translation_services`.
- `api_key` (Optional[str], optional): The API key for the translation service. If not provided, uses the key from environment variables.
- `glossary` (Optional[List[Tuple[str, str]]], optional): A list of tuples representing custom glossary terms. Each tuple should be (source_term, target_term).
- `context` (Optional[str], optional): Additional context to provide to the translation service for better accuracy.
- `instruction` (Optional[str], optional): Specific instructions for the translation service.
- `request_params` (Optional[Dict[str, Any]], optional): Additional parameters to pass to the translation service API request.
- `**kwargs`: Additional keyword arguments that may be passed to the underlying translation functions.

### Returns
- `AsyncIterator[str]`: An asynchronous iterator that yields translated chunks of text.

### Example Usage
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    # Simulate reading chunks from a file or stream
    chunks = ["First chunk of text.", "Second chunk of text.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)  # Simulate async delay

async def main():
    translated_chunks = []
    async for translated_chunk in do_translate_async_stream(
        text_chunk_generator(),
        source_language="en",
        target_language="zh"
    ):
        translated_chunks.append(translated_chunk)
        print(f"Translated: {translated_chunk}")
    
    full_translation = "".join(translated_chunks)
    print("Full translation:", full_translation)

asyncio.run(main())
```

### Notes
- This function is useful for processing large texts in a memory-efficient manner, as it processes and yields translations chunk by chunk.
- The function handles the concatenation of chunks internally to ensure coherent translations across chunk boundaries.
- Error handling is built into the function, and it will raise exceptions if the translation services encounter issues.

---

### TRANSLATION RESULT

## `do_translate_async_stream`

La funzione `do_translate_async_stream` è un generatore asincrono che esegue la traduzione su un flusso di blocchi di testo. È progettata per gestire flussi di input continui, come quelli provenienti da un file letto in blocchi, e restituisce i blocchi tradotti man mano che diventano disponibili.

### Firma della funzione

```python
async def do_translate_async_stream(
    text_chunks: AsyncIterator[str],
    source_language: str = "en",
    target_language: str = "zh",
    translation_services: Optional[List[str]] = None,
    translation_service: Optional[str] = None,
    api_key: Optional[str] = None,
    glossary: Optional[List[Tuple[str, str]]] = None,
    context: Optional[str] = None,
    instruction: Optional[str] = None,
    request_params: Optional[Dict[str, Any]] = None,
    **kwargs: Any
) -> AsyncIterator[str]:
```

### Parametri

- `text_chunks` (AsyncIterator[str]): Un iteratore asincrono che restituisce blocchi di testo da tradurre.
- `source_language` (str, opzionale): Il codice lingua del testo sorgente. Predefinito a "en".
- `target_language` (str, opzionale): Il codice lingua della traduzione di destinazione. Predefinito a "zh".
- `translation_services` (Optional[List[str]], opzionale): Un elenco di nomi di servizi di traduzione da utilizzare. Se non fornito, utilizza i servizi configurati nell'ambiente.
- `translation_service` (Optional[str], opzionale): Un servizio di traduzione specifico da utilizzare. Se fornito, sovrascrive `translation_services`.
- `api_key` (Optional[str], opzionale): La chiave API per il servizio di traduzione. Se non fornita, utilizza la chiave dalle variabili d'ambiente.
- `glossary` (Optional[List[Tuple[str, str]]], opzionale): Un elenco di tuple che rappresentano termini personalizzati del glossario. Ogni tupla dovrebbe essere (termine_sorgente, termine_destinazione).
- `context` (Optional[str], opzionale): Contesto aggiuntivo da fornire al servizio di traduzione per una migliore accuratezza.
- `instruction` (Optional[str], opzionale): Istruzioni specifiche per il servizio di traduzione.
- `request_params` (Optional[Dict[str, Any]], opzionale): Parametri aggiuntivi da passare alla richiesta API del servizio di traduzione.
- `**kwargs`: Argomenti chiave aggiuntivi che possono essere passati alle funzioni di traduzione sottostanti.

### Restituisce

- `AsyncIterator[str]`: Un iteratore asincrono che restituisce blocchi di testo tradotti.

### Esempio di utilizzo

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def text_chunk_generator():
    # Simula la lettura di blocchi da un file o flusso
    chunks = ["First chunk of text.", "Second chunk of text.", "Third chunk."]
    for chunk in chunks:
        yield chunk
        await asyncio.sleep(0.1)  # Simula un ritardo asincrono

async def main():
    translated_chunks = []
    async for translated_chunk in do_translate_async_stream(
        text_chunk_generator(),
        source_language="en",
        target_language="zh"
    ):
        translated_chunks.append(translated_chunk)
        print(f"Translated: {translated_chunk}")
    
    full_translation = "".join(translated_chunks)
    print("Full translation:", full_translation)

asyncio.run(main())
```

### Note

- Questa funzione è utile per elaborare testi di grandi dimensioni in modo efficiente in termini di memoria, poiché elabora e restituisce le traduzioni blocco per blocco.
- La funzione gestisce la concatenazione dei blocchi internamente per garantire traduzioni coerenti attraverso i confini dei blocchi.
- La gestione degli errori è integrata nella funzione e solleverà eccezioni se i servizi di traduzione incontrano problemi.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### LANGUAGE

it

---

### BYPASS LIST

- pdf2zh
- PDFMathTranslate
- ---

---

### ORIGINAL TEXT

You can cancel the task consuming the stream. Cancellation is propagated to the underlying translation process.

---

### TRANSLATION RESULT

Puoi annullare il task che consuma il flusso. L'annullamento viene propagato al processo di traduzione sottostante.

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream

async def cancellable(settings, pdf):
    task = asyncio.create_task(_consume(settings, pdf))
    await asyncio.sleep(1.0)  # let it start
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Cancelled")

async def _consume(settings, pdf):
    async for event in do_translate_async_stream(settings, pdf):
        if event["type"] == "finish":
            break
```

This example shows how to define a custom event shape for a specific event type.

```yaml
eventShapes:
  - type: "custom"
    name: "My Custom Event"
    color: "#ff0000"
    description: "A custom event for demonstration purposes"
    defaultIcon: "star"
    defaultSize: 2.0
    defaultOpacity: 0.8
```

### Event Shape Properties

Each event shape can have the following properties:

- `type` (string, required): The type of event this shape applies to. Must match the event type in your timeline data.
- `name` (string, required): A human-readable name for this event shape.
- `color` (string): The default color for events of this type, in hex format (e.g., "#ff0000" for red).
- `description` (string): A description of this event type.
- `defaultIcon` (string): The default icon to use for events of this type. See the [icon list](ICONS.md) for available icons.
- `defaultSize` (number): The default size multiplier for events of this type (1.0 = normal size).
- `defaultOpacity` (number): The default opacity for events of this type (0.0 to 1.0).

### Default Event Shapes

The timeline includes several built-in event shapes for common event types:

```yaml
eventShapes:
  - type: "milestone"
    name: "Milestone"
    color: "#ff6b6b"
    description: "A significant milestone or achievement"
    defaultIcon: "flag"
    defaultSize: 1.5
    defaultOpacity: 1.0

  - type: "task"
    name: "Task"
    color: "#4ecdc4"
    description: "A task or action item"
    defaultIcon: "check-circle"
    defaultSize: 1.0
    defaultOpacity: 0.8

  - type: "meeting"
    name: "Meeting"
    color: "#45b7d1"
    description: "A meeting or discussion"
    defaultIcon: "users"
    defaultSize: 1.2
    defaultOpacity: 0.9

  - type: "deadline"
    name: "Deadline"
    color: "#f9ca24"
    description: "A deadline or due date"
    defaultIcon: "clock"
    defaultSize: 1.3
    defaultOpacity: 0.9

  - type: "note"
    name: "Note"
    color: "#a55eea"
    description: "A note or reminder"
    defaultIcon: "sticky-note"
    defaultSize: 0.8
    defaultOpacity: 0.7
```

You can override these defaults by defining your own event shapes with the same `type` values.

---

### TRANSLATION RESULT

### Esempio di Forme degli Eventi

Questo esempio mostra come definire una forma di evento personalizzata per un tipo di evento specifico.

```yaml
eventShapes:
  - type: "custom"
    name: "My Custom Event"
    color: "#ff0000"
    description: "A custom event for demonstration purposes"
    defaultIcon: "star"
    defaultSize: 2.0
    defaultOpacity: 0.8
```

### Proprietà delle Forme degli Eventi

Ogni forma di evento può avere le seguenti proprietà:

- `type` (stringa, obbligatorio): Il tipo di evento a cui si applica questa forma. Deve corrispondere al tipo di evento nei tuoi dati della timeline.
- `name` (stringa, obbligatorio): Un nome leggibile per questa forma di evento.
- `color` (stringa): Il colore predefinito per gli eventi di questo tipo, in formato esadecimale (ad esempio, "#ff0000" per il rosso).
- `description` (stringa): Una descrizione di questo tipo di evento.
- `defaultIcon` (stringa): L'icona predefinita da utilizzare per gli eventi di questo tipo. Vedi l'[elenco delle icone](ICONS.md) per le icone disponibili.
- `defaultSize` (numero): Il moltiplicatore di dimensione predefinito per gli eventi di questo tipo (1.0 = dimensione normale).
- `defaultOpacity` (numero): L'opacità predefinita per gli eventi di questo tipo (da 0.0 a 1.0).

### Forme degli Eventi Predefinite

La timeline include diverse forme di evento integrate per i tipi di evento comuni:

```yaml
eventShapes:
  - type: "milestone"
    name: "Milestone"
    color: "#ff6b6b"
    description: "Una pietra miliare o un risultato significativo"
    defaultIcon: "flag"
    defaultSize: 1.5
    defaultOpacity: 1.0

  - type: "task"
    name: "Task"
    color: "#4ecdc4"
    description: "Un compito o un elemento d'azione"
    defaultIcon: "check-circle"
    defaultSize: 1.0
    defaultOpacity: 0.8

  - type: "meeting"
    name: "Meeting"
    color: "#45b7d1"
    description: "Un incontro o una discussione"
    defaultIcon: "users"
    defaultSize: 1.2
    defaultOpacity: 0.9

  - type: "deadline"
    name: "Deadline"
    color: "#f9ca24"
    description: "Una scadenza o una data di scadenza"
    defaultIcon: "clock"
    defaultSize: 1.3
    defaultOpacity: 0.9

  - type: "note"
    name: "Note"
    color: "#a55eea"
    description: "Una nota o un promemoria"
    defaultIcon: "sticky-note"
    defaultSize: 0.8
    defaultOpacity: 0.7
```

Puoi sovrascrivere questi valori predefiniti definendo le tue forme di evento con gli stessi valori `type`.
A stage summary event is a special type of event that represents a summary or overview of a stage in the timeline. It typically spans a period of time and provides a high-level description of what occurred during that stage.

```yaml
events:
  - type: "stage_summary"
    title: "Project Initiation Phase"
    startDate: "2023-01-01"
    endDate: "2023-03-31"
    description: "This phase involved initial planning, requirement gathering, and team formation for the new project."
    color: "#6c5ce7"
    icon: "clipboard-list"
    priority: 1
```

### Properties

- `type` (string): Must be "stage_summary" for stage summary events.
- `title` (string): The title of the stage summary.
- `startDate` (string): The start date of the stage in ISO format (YYYY-MM-DD).
- `endDate` (string): The end date of the stage in ISO format (YYYY-MM-DD).
- `description` (string): A description of what occurred during this stage.
- `color` (string, optional): The color for this event in hex format. Defaults to a system color if not specified.
- `icon` (string, optional): The icon to use for this event. See the [icon list](ICONS.md) for available icons.
- `priority` (number, optional): The priority level of this event. Higher numbers indicate higher priority. Defaults to 0.

### Display Behavior

Stage summary events are typically displayed as:
- A colored bar spanning the stage duration on the timeline
- With the title and optional icon visible
- Often used as parent events that contain other detailed events within their time range

### Example Use Cases

1. **Project Phases**: Representing initiation, planning, execution, and closure phases of a project.
2. **Development Sprints**: Summarizing what was accomplished during a specific sprint or iteration.
3. **Historical Periods**: Representing historical eras or periods in a historical timeline.
4. **Product Lifecycles**: Showing different stages in a product's lifecycle (development, launch, growth, maturity).

### Related Event Types

- [Milestone events](#milestone-events): For specific point-in-time achievements within a stage.
- [Task events](#task-events): For individual tasks that occur within a stage.
- [Meeting events](#meeting-events): For meetings that occurred during the stage.

---

### TRANSLATION RESULT

Evento di riepilogo della fase (esempio): Un evento di riepilogo della fase è un tipo speciale di evento che rappresenta un riepilogo o una panoramica di una fase nella timeline. Tipicamente copre un periodo di tempo e fornisce una descrizione di alto livello di ciò che è accaduto durante quella fase.

```yaml
events:
  - type: "stage_summary"
    title: "Fase di Inizializzazione del Progetto"
    startDate: "2023-01-01"
    endDate: "2023-03-31"
    description: "Questa fase ha coinvolto la pianificazione iniziale, la raccolta dei requisiti e la formazione del team per il nuovo progetto."
    color: "#6c5ce7"
    icon: "clipboard-list"
    priority: 1
```

### Proprietà

- `type` (stringa): Deve essere "stage_summary" per gli eventi di riepilogo della fase.
- `title` (stringa): Il titolo del riepilogo della fase.
- `startDate` (stringa): La data di inizio della fase in formato ISO (YYYY-MM-DD).
- `endDate` (stringa): La data di fine della fase in formato ISO (YYYY-MM-DD).
- `description` (stringa): Una descrizione di ciò che è accaduto durante questa fase.
- `color` (stringa, opzionale): Il colore per questo evento in formato esadecimale. Predefinito a un colore di sistema se non specificato.
- `icon` (stringa, opzionale): L'icona da utilizzare per questo evento. Vedi l'[elenco delle icone](ICONS.md) per le icone disponibili.
- `priority` (numero, opzionale): Il livello di priorità di questo evento. Numeri più alti indicano priorità più alta. Predefinito a 0.

### Comportamento di visualizzazione

Gli eventi di riepilogo della fase sono tipicamente visualizzati come:
- Una barra colorata che copre la durata della fase sulla timeline
- Con il titolo e l'icona opzionale visibili
- Spesso utilizzati come eventi padre che contengono altri eventi dettagliati all'interno del loro intervallo di tempo

### Casi d'uso di esempio

1. **Fasi del progetto**: Rappresentazione delle fasi di inizializzazione, pianificazione, esecuzione e chiusura di un progetto.
2. **Sprint di sviluppo**: Riepilogo di ciò che è stato realizzato durante uno sprint o iterazione specifica.
3. **Periodi storici**: Rappresentazione di epoche o periodi storici in una timeline storica.
4. **Cicli di vita del prodotto**: Mostra le diverse fasi del ciclo di vita di un prodotto (sviluppo, lancio, crescita, maturità).

### Tipi di evento correlati

- [Eventi milestone](#milestone-events): Per realizzazioni specifiche in un punto nel tempo all'interno di una fase.
- [Eventi task](#task-events): Per singoli compiti che si verificano all'interno di una fase.
- [Eventi meeting](#meeting-events): Per riunioni che si sono verificate durante la fase.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccole.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccole.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccule.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale or accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccule.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccule.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccule.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibles. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Notes & Best Practices: - **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### TRANSLATION RESULT

### Note & Best Practices

- **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccule.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente confidenziali attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
```json
{
  "type": "stage_summary",
  "stages": [
    {"name": "Parse PDF and Create Intermediate Representation", "percent": 0.1086},
    {"name": "DetectScannedFile", "percent": 0.0188},
    {"name": "Parse Page Layout", "percent": 0.1079}
    // ... more stages ...
  ],
  "part_index": 0,
  "total_parts": 1
}
```

This event is emitted multiple times during the translation process to indicate progress.

```json
{
  "event": "progress",
  "data": {
    "progress": 50,
    "message": "Processing page 10 of 20"
  }
}
```

- `progress`: The progress percentage (0-100)
- `message`: A human-readable message describing the current progress

---

Let's get started.

---

### TRANSLATION RESULT

Evento di avanzamento (esempio): Questo evento viene emesso più volte durante il processo di traduzione per indicare l'avanzamento.

```json
{
  "event": "progress",
  "data": {
    "progress": 50,
    "message": "Processing page 10 of 20"
  }
}
```

- `progress`: La percentuale di avanzamento (0-100)
- `message`: Un messaggio leggibile che descrive l'avanzamento corrente
- ### Notes & Best Practices: - **Qualità della traduzione**: Sebbene il servizio fornisca traduzioni di alta qualità, è importante rivedere le traduzioni critiche, specialmente per uso professionale o accademico.
- **Dimensione del file**: I file di grandi dimensioni potrebbero richiedere più tempo per essere elaborati. Considera di suddividere documenti molto grandi in parti più piccole.
- **Formattazione**: Alcune formattazioni complesse potrebbero non essere preservate perfettamente. I documenti semplici e basati su testo si traducono al meglio.
- **Privacy**: Sii consapevole delle informazioni sensibili. Sebbene il servizio sia sicuro, evita di tradurre documenti altamente riservati attraverso qualsiasi servizio online.
- **Lingue supportate**: Controlla l'elenco delle lingue supportate prima di elaborare i tuoi documenti.
- ### Cancellazione: della traduzione

Se desideri annullare un'attività di traduzione, puoi farlo in due modi:

1. **Annulla prima che la traduzione inizi**:
   - Se l'attività di traduzione non è ancora iniziata, puoi fare clic sul pulsante "Annulla" nell'elenco delle attività per annullarla.

2. **Annulla durante il processo di traduzione**:
   - Se l'attività di traduzione è già iniziata, puoi fare clic sul pulsante "Annulla" nell'elenco delle attività per fermare la traduzione. Tuttavia, nota che l'annullamento potrebbe non essere immediato, poiché il sistema ha bisogno di un po' di tempo per elaborare la richiesta di annullamento.

Dopo l'annullamento, l'attività verrà rimossa dall'elenco delle attività e il contenuto tradotto non verrà salvato.

---

Iniziamo.
- ### Esempio di utilizzo minimo (Async): {#esempio-di-utilizzo-minimo-async}

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    pdf_path = "example.pdf"
    output_path = "example_translated.pdf"
    
    # Inizializza il motore di traduzione
    engine = await pdf2zh_async()
    
    # Traduci il PDF
    await engine.translate(pdf_path, output_path)

asyncio.run(main())
```

### Esempio di utilizzo minimo (Sincrono) {#esempio-di-utilizzo-minimo-sincrono}

```python
from pdf2zh import pdf2zh

def main():
    pdf_path = "example.pdf"
    output_path = "example_translated.pdf"
    
    # Inizializza il motore di traduzione
    engine = pdf2zh()
    
    # Traduci il PDF
    engine.translate(pdf_path, output_path)

if __name__ == "__main__":
    main()
```

### Configurazione di base {#configurazione-di-base}

```python
from pdf2zh import pdf2zh

# Inizializza con configurazione
engine = pdf2zh(
    target_lang="it",  # Lingua di destinazione (codice ISO 639-1)
    translation_service="google",  # Servizio di traduzione
    enable_glossary=True,  # Abilita la funzione glossario
    enable_ocr=True,  # Abilita OCR per PDF scannerizzati
    output_format="text",  # Formato di output: "text" o "pdf"
    preserve_layout=True  # Mantieni il layout originale nell'output PDF
)

# Traduci PDF
engine.translate("input.pdf", "output.pdf")
```

### Configurazione avanzata {#configurazione-avanzata}

```python
from pdf2zh import pdf2zh

# Configurazione avanzata con impostazioni personalizzate
engine = pdf2zh(
    target_lang="it",
    translation_service="google",
    
    # Impostazioni OCR
    ocr_engine="tesseract",  # "tesseract" o "easyocr"
    ocr_lang="en",  # Lingua sorgente per OCR
    
    # Impostazioni traduzione
    chunk_size=500,  # Dimensione del blocco di testo per la traduzione
    max_retries=3,  # Tentativi massimi di ripetizione per la traduzione
    
    # Impostazioni output
    output_format="pdf",
    preserve_layout=True,
    font_family="SimSun",  # Font per il testo cinese in PDF
    
    # Impostazioni cache
    use_cache=True,  # Abilita cache traduzioni
    cache_dir=".translation_cache"  # Directory cache
)

# Traduci con callback di avanzamento
def progress_callback(current, total):
    print(f"Avanzamento: {current}/{total} pagine")

engine.translate("input.pdf", "output.pdf", progress_callback=progress_callback)
```

### Funzione di traduzione personalizzata {#funzione-di-traduzione-personalizzata}

```python
from pdf2zh import pdf2zh

# Definisci funzione di traduzione personalizzata
def my_translator(text, source_lang="en", target_lang="it"):
    # La tua logica di traduzione personalizzata qui
    # Questo potrebbe chiamare un'API, usare un modello locale, ecc.
    translated_text = text.upper()  # Esempio: converte in maiuscolo
    return translated_text

# Inizializza con traduttore personalizzato
engine = pdf2zh(
    target_lang="it",
    translation_service="custom",
    custom_translator=my_translator
)

engine.translate("input.pdf", "output.pdf")
```

### Elaborazione in batch {#elaborazione-in-batch}

```python
from pdf2zh import pdf2zh

engine = pdf2zh(target_lang="it")

# Elabora in batch più file
files = [
    ("doc1.pdf", "doc1_it.pdf"),
    ("doc2.pdf", "doc2_it.pdf"),
    ("doc3.pdf", "doc3_it.pdf")
]

for input_file, output_file in files:
    try:
        engine.translate(input_file, output_file)
        print(f"Tradotto con successo {input_file}")
    except Exception as e:
        print(f"Errore nella traduzione di {input_file}: {e}")
```

### Gestione degli errori {#gestione-degli-errori}

```python
from pdf2zh import pdf2zh
import logging

# Configura il logging
logging.basicConfig(level=logging.INFO)

engine = pdf2zh(target_lang="it")

try:
    engine.translate("input.pdf", "output.pdf")
except FileNotFoundError:
    print("File di input non trovato")
except PermissionError:
    print("Permesso negato per le operazioni sui file")
except Exception as e:
    print(f"Errore imprevisto: {e}")
```

### Utilizzo dei context manager {#utilizzo-dei-context-manager}

```python
from pdf2zh import pdf2zh

# Utilizzo del context manager per la pulizia automatica delle risorse
with pdf2zh(target_lang="it") as engine:
    engine.translate("input.pdf", "output.pdf")
# Le risorse del motore vengono rilasciate automaticamente qui
```

---
```json
{
  "type": "progress_update",
  "stage": "Translate Paragraphs",
  "stage_progress": 2.04,
  "stage_current": 1,
  "stage_total": 49,
  "overall_progress": 53.44,
  "part_index": 1,
  "total_parts": 1
}
```

This event is sent when the translation process is completed successfully.

```json
{
  "event": "finish",
  "data": {
    "message": "Translation completed successfully",
    "filePath": "/path/to/translated/file.pdf",
    "pagesTranslated": 10,
    "timeTaken": "00:05:30"
  }
}
```

---

### TRANSLATION RESULT

Evento di completamento (esempio): Questo evento viene inviato quando il processo di traduzione viene completato con successo.

```json
{
  "event": "finish",
  "data": {
    "message": "Translation completed successfully",
    "filePath": "/path/to/translated/file.pdf",
    "pagesTranslated": 10,
    "timeTaken": "00:05:30"
  }
}
```
```json
{
  "type": "finish",
  "translate_result": {
    "original_pdf_path": "pdf2zh_files/<session>/table.pdf",
    "mono_pdf_path": "pdf2zh_files/<session>/table.zh-CN.mono.pdf",
    "dual_pdf_path": "pdf2zh_files/<session>/table.zh-CN.dual.pdf",
    "no_watermark_mono_pdf_path": "pdf2zh_files/<session>/table.no_watermark.zh-CN.mono.pdf",
    "no_watermark_dual_pdf_path": "pdf2zh_files/<session>/table.no_watermark.zh-CN.dual.pdf",
    "auto_extracted_glossary_path": "pdf2zh_files/<session>/table.zh-CN.glossary.csv",
    "total_seconds": 42.83,
    "peak_memory_usage": 4651.55
  }
}
```

If an error occurs during translation, the event stream will send an error event with details about the error.

```json
{
  "event": "error",
  "data": {
    "message": "Failed to translate document",
    "error": "The document is corrupted and cannot be read."
  }
}
```

### Event Stream Client Example

Here's how you can listen to the event stream in a web application:

```javascript
const eventSource = new EventSource('/api/translate/stream');

eventSource.onmessage = function(event) {
  const data = JSON.parse(event.data);
  
  switch (data.event) {
    case 'start':
      console.log('Translation started:', data.data.message);
      break;
    case 'progress':
      console.log(`Progress: ${data.data.progress}%`);
      break;
    case 'complete':
      console.log('Translation complete:', data.data.filePath);
      break;
    case 'error':
      console.error('Error:', data.data.message);
      break;
  }
};

eventSource.onerror = function(error) {
  console.error('EventSource failed:', error);
};
```

### Notes

- The event stream will automatically close when the translation is complete or when an error occurs.
- You can also manually close the event stream by calling `eventSource.close()`.
- The progress event may not be emitted for very short translations.

---

### TRANSLATION RESULT

Evento di errore (esempio): Se si verifica un errore durante la traduzione, il flusso di eventi invierà un evento di errore con i dettagli dell'errore.

```json
{
  "event": "error",
  "data": {
    "message": "Failed to translate document",
    "error": "The document is corrupted and cannot be read."
  }
}
```

### Esempio di Client del Flusso di Eventi

Ecco come puoi ascoltare il flusso di eventi in un'applicazione web:

```javascript
const eventSource = new EventSource('/api/translate/stream');

eventSource.onmessage = function(event) {
  const data = JSON.parse(event.data);
  
  switch (data.event) {
    case 'start':
      console.log('Translation started:', data.data.message);
      break;
    case 'progress':
      console.log(`Progress: ${data.data.progress}%`);
      break;
    case 'complete':
      console.log('Translation complete:', data.data.filePath);
      break;
    case 'error':
      console.error('Error:', data.data.message);
      break;
  }
};

eventSource.onerror = function(error) {
  console.error('EventSource failed:', error);
};
```

### Note

- Il flusso di eventi si chiuderà automaticamente quando la traduzione è completata o quando si verifica un errore.
- Puoi anche chiudere manualmente il flusso di eventi chiamando `eventSource.close()`.
- L'evento di avanzamento potrebbe non essere emesso per traduzioni molto brevi.
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

- **Translation Quality**: While the service provides high-quality translations, it's important to review critical translations, especially for professional or academic use.
- **File Size**: Large files may take longer to process. Consider breaking very large documents into smaller parts.
- **Formatting**: Some complex formatting might not be preserved perfectly. Simple, text-based documents translate best.
- **Privacy**: Be mindful of sensitive information. While the service is secure, avoid translating highly confidential documents through any online service.
- **Supported Languages**: Check the list of supported languages before processing your documents.

---

### LANGUAGE

it
### Example

```python
import asyncio
from typing import Optional
from pdf2zh import translate_pdf

async def handle_translation():
    try:
        # Initialize the translation
        generator = translate_pdf(
            file="document.pdf",
            target_language="es",
            source_language="en"
        )
        
        # Process events
        async for event in generator:
            if event['type'] == 'progress_start':
                print(f"Starting translation: {event['data']['message']}")
                
            elif event['type'] == 'stage_summary':
                stage = event['data']
                print(f"Stage: {stage['stage']} - {stage['description']}")
                
            elif event['type'] == 'progress_update':
                progress = event['data']
                print(f"Progress: {progress['current']}/{progress['total']} "
                      f"({progress['percentage']}%) - Part {progress['part_index']}/{progress['total_parts']}")
                
            elif event['type'] == 'progress_end':
                print(f"Translation completed: {event['data']['message']}")
                
            elif event['type'] == 'finish':
                result = event['data']
                print(f"Translation finished. Output file: {result['output_file']}")
                break
                
    except Exception as e:
        print(f"Translation failed: {e}")

# Run the translation
asyncio.run(handle_translation())
```

### Event Types

- `progress_start`: Emitted when translation starts. Contains a welcome message.
- `stage_summary`: Emitted at the beginning of each major stage. Describes the stage.
- `progress_update`: Emitted periodically during processing. Shows current progress.
- `progress_end`: Emitted when translation processing completes. Contains completion message.
- `finish`: Emitted when the entire translation is complete. Contains result data.
- `error`: Emitted when an error occurs. Contains error information.

### Data Structure

Each event contains:
- `type`: The event type (string)
- `data`: Event-specific data (dictionary)

### Error Handling

The generator may raise exceptions for:
- Invalid file paths
- Unsupported languages  
- Network errors
- Permission errors

Always wrap the async for loop in a try-except block.

---

### TRANSLATION RESULT

- Gestisci sempre sia gli eventi di errore che le eccezioni dal generatore.
- Interrompi il ciclo su `finish` per evitare lavoro non necessario.
- Assicurati che il `file` esista e che `settings.validate_settings()` passi prima di chiamare.
- I documenti di grandi dimensioni possono essere divisi; utilizza `part_index/total_parts` e `overall_progress` per guidare la tua UI.
- Debounce `progress_update` se la tua UI è sensibile ad aggiornamenti ripetuti e identici.
- `report_interval` (SettingsModel): controlla solo la frequenza di emissione degli eventi `progress_update`. Non influisce su `stage_summary`, `progress_start`, `progress_end` o `finish`. Il valore predefinito è 0.1s e il minimo consentito è 0.05s. Secondo la logica del monitor di avanzamento, quando `stage_total <= 3`, gli aggiornamenti non vengono limitati da `report_interval`.

### Esempio

```python
import asyncio
from typing import Optional
from pdf2zh import translate_pdf

async def handle_translation():
    try:
        # Inizializza la traduzione
        generator = translate_pdf(
            file="document.pdf",
            target_language="es",
            source_language="en"
        )
        
        # Elabora gli eventi
        async for event in generator:
            if event['type'] == 'progress_start':
                print(f"Starting translation: {event['data']['message']}")
                
            elif event['type'] == 'stage_summary':
                stage = event['data']
                print(f"Stage: {stage['stage']} - {stage['description']}")
                
            elif event['type'] == 'progress_update':
                progress = event['data']
                print(f"Progress: {progress['current']}/{progress['total']} "
                      f"({progress['percentage']}%) - Part {progress['part_index']}/{progress['total_parts']}")
                
            elif event['type'] == 'progress_end':
                print(f"Translation completed: {event['data']['message']}")
                
            elif event['type'] == 'finish':
                result = event['data']
                print(f"Translation finished. Output file: {result['output_file']}")
                break
                
    except Exception as e:
        print(f"Translation failed: {e}")

# Esegui la traduzione
asyncio.run(handle_translation())
```

### Tipi di Evento

- `progress_start`: Emesso quando inizia la traduzione. Contiene un messaggio di benvenuto.
- `stage_summary`: Emesso all'inizio di ogni fase principale. Descrive la fase.
- `progress_update`: Emesso periodicamente durante l'elaborazione. Mostra lo stato di avanzamento corrente.
- `progress_end`: Emesso quando l'elaborazione della traduzione è completata. Contiene un messaggio di completamento.
- `finish`: Emesso quando l'intera traduzione è completa. Contiene i dati del risultato.
- `error`: Emesso quando si verifica un errore. Contiene informazioni sull'errore.

### Struttura dei Dati

Ogni evento contiene:
- `type`: Il tipo di evento (stringa)
- `data`: Dati specifici dell'evento (dizionario)

### Gestione degli Errori

Il generatore può sollevare eccezioni per:
- Percorsi di file non validi
- Lingue non supportate
- Errori di rete
- Errori di permesso

Avvolgi sempre il ciclo async for in un blocco try-except.

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>