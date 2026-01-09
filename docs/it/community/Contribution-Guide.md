# Contribuire al Progetto

> [!CAUTION]
>
> Gli attuali manutentori del progetto stanno ricercando l'internazionalizzazione automatizzata della documentazione. Pertanto, qualsiasi PR relativa all'internazionalizzazione/traduzione della documentazione NON sarà accettata!
>
> Si prega di NON inviare PR relative all'internazionalizzazione/traduzione della documentazione!

Grazie per il tuo interesse in questo progetto! Prima di iniziare a contribuire, ti preghiamo di dedicare un po' di tempo a leggere le seguenti linee guida per garantire che il tuo contributo possa essere accettato senza problemi.

## Tipi di contributi non accettati

1. Documentazione internazionalizzazione/traduzione
2. Contributi relativi all'infrastruttura di base, come API HTTP, ecc.
3. Issue contrassegnate esplicitamente come "No help needed" (inclusi i problemi nei repository [Byaidu/PDFMathTranslate](Byaidu/PDFMathTranslate) e [PDFMathTranslate-next/PDFMathTranslate-next](PDFMathTranslate-next/PDFMathTranslate-next)).
4. Altri contributi ritenuti inappropriati dai manutentori.
5. Contributi alla documentazione, ma che modificano la documentazione in lingue diverse dall'inglese.
6. PR che richiedono la modifica di file PDF.
7. PR che modificano il file `pdf2zh_next/gui_translation.yaml`.

Si prega di NON inviare PR relativi ai tipi sopra menzionati.

> [!NOTE]
>
> Se desideri contribuire alla documentazione, **modifica solo la versione inglese della documentazione**. Le altre versioni linguistiche sono tradotte dai contributori stessi.

## PR consigliati per discutere con i manutentori tramite Issue prima dell'invio

Per i seguenti tipi di PR, si consiglia di discutere con i manutentori prima dell'invio:

1. PR relativi alla funzionalità di condivisione multi-utente. (Questo progetto è principalmente progettato per l'uso da parte di un singolo utente e non intende introdurre un sistema multi-utente completo).

## Processo di Contribuzione

1. Forka questo repository e clonalo localmente.
2. Crea un nuovo branch: `git checkout -b feature/<feature-name>`.
3. Sviluppa e assicurati che il tuo codice soddisfi i requisiti.
4. Committa il tuo codice:
   ```bash
   git add .
   git commit -m "<semantic commit message>"
   ```
5. Pusha sul tuo repository: `git push origin feature/<feature-name>`.
6. Crea una PR su GitHub, fornisci una descrizione dettagliata e richiedi una revisione da [@awwaawwa](https://github.com/awwaawwa).
7. Assicurati che tutti i controlli automatici siano superati.

> [!TIP]
>
> Non è necessario attendere che lo sviluppo sia completamente terminato per creare una PR. Crearne una in anticipo ci permette di rivedere la tua implementazione e fornire suggerimenti.
>
> Se hai domande sul codice sorgente o su questioni correlate, contatta il manutentore all'indirizzo aw@funstory.ai.
>
> I file di risorse per la versione 2.0 sono condivisi con [BabelDOC](https://github.com/funstory-ai/BabelDOC). Il codice per scaricare le risorse correlate si trova in BabelDOC. Se desideri aggiungere nuovi file di risorse, contatta il manutentore di BabelDOC all'indirizzo aw@funstory.ai.

## Requisiti di base

<h4 id="sop">1. Flusso di lavoro</h4>

   - Si prega di effettuare il fork dal ramo `main` e sviluppare sul proprio ramo forkato.
   - Quando si invia una Pull Request (PR), fornire una descrizione dettagliata delle modifiche apportate.
   - Se la PR non supera i controlli automatici (indicati da `checks failed` e una croce rossa), si prega di rivedere i corrispondenti `details` e modificare l'invio per garantire che la nuova PR superi tutti i controlli.


<h4 id="dev&test">2. Sviluppo e Test</h4>

   - Usa il comando `pip install -e .` per lo sviluppo e il testing.


<h4 id="format">3. Formattazione del Codice</h4>

   - Configura lo strumento `pre-commit` e abilita `black` e `flake8` per la formattazione del codice.


<h4 id="requpdate">4. Aggiornamenti delle Dipendenze</h4>

   - Se introduci nuove dipendenze, aggiorna tempestivamente l'elenco delle dipendenze nel file `pyproject.toml`.


<h4 id="docupdate">5. Aggiornamenti della Documentazione</h4>

   - Se aggiungi nuove opzioni da riga di comando, aggiorna di conseguenza l'elenco delle opzioni da riga di comando in tutte le versioni linguistiche del file `README.md`.


<h4 id="commitmsg">6. Messaggi di Commit</h4>

   - Utilizza [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), ad esempio: `feat(translator): add openai`.


<h4 id="codestyle">7. Stile di Codifica</h4>

   - Assicurati che il codice inviato aderisca agli standard di base dello stile di codifica.
   - Utilizza snake_case o camelCase per la denominazione delle variabili.


<h4 id="doctypo">8. Formattazione della Documentazione</h4>

   - Per la formattazione di `README.md`, si prega di seguire le [Linee guida per la scrittura in cinese](https://github.com/sparanoid/chinese-copywriting-guidelines).
   - Assicurarsi che la documentazione in inglese e cinese sia sempre aggiornata; gli aggiornamenti della documentazione in altre lingue sono opzionali.

## Aggiungere un motore di traduzione

1. Aggiungi una nuova classe di configurazione del traduttore nel file `pdf2zh/config/translate_engine_model.py`.
2. Aggiungi un'istanza della nuova classe di configurazione del traduttore all'alias di tipo `TRANSLATION_ENGINE_SETTING_TYPE` nello stesso file.
3. Aggiungi la nuova classe di implementazione del traduttore nella cartella `pdf2zh/translator/translator_impl`.

> [!NOTE]
>
> Questo progetto non intende supportare alcun motore di traduzione con un RPS (richieste al secondo) inferiore a 4. Si prega di non inviare supporto per tali motori.
> Anche i seguenti tipi di traduttori non verranno integrati:
> - Traduttori che sono stati interrotti dai manutentori upstream (come deeplx)
> - Traduttori con dipendenze pesanti (come quelli che dipendono da pytorch)
> - Traduttori instabili
> - Traduttori basati su API di reverse engineering
>
> Quando non sei sicuro se un traduttore soddisfa i requisiti, puoi inviare un issue per discuterne con i manutentori.

## Struttura del progetto

- **cartella config**: Sistema di configurazione.
- **cartella translator**: Implementazioni relative ai traduttori.
- **gui.py**: Fornisce l'interfaccia GUI.
- **const.py**: Alcune costanti.
- **main.py**: Fornisce lo strumento da riga di comando.
- **high_level.py**: Interfacce di alto livello basate su BabelDOC.
- **http_api.py**: Fornisce l'API HTTP (non avviata).

Chiedi all'AI di comprendere il progetto: [DeepWiki](https://deepwiki.com/PDFMathTranslate-next/PDFMathTranslate-next)

## Contattaci

Se hai domande, invia feedback tramite Issue o unisciti al nostro Gruppo Telegram. Grazie per il tuo contributo!

> [!TIP]
>
> [Immersive Translate](https://immersivetranslate.com) sponsorizza codici mensili di abbonamento Pro per i contributori attivi di questo progetto. Per i dettagli, consultare: [Regole di ricompensa per i contributori di BabelDOC/PDFMathTranslate](https://funstory-ai.github.io/BabelDOC/CONTRIBUTOR_REWARD/)

<div align="right"> 
<h6><small>Parte del contenuto di questa pagina è stata tradotta da GPT e potrebbe contenere errori.</small></h6>