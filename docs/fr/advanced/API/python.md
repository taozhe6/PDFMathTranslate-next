>
> Thank you for your understanding and support!

### Quick Links

- [Home](https://pdf2zh-next.com/)
- [Getting Started](https://pdf2zh-next.com/getting-started/)
- [Command Line](https://pdf2zh-next.com/getting-started/CLI.html)
- [WebUI](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
- [Supported Languages](https://pdf2zh-next.com/advanced/LANGUAGE.html)
- [FAQ](https://pdf2zh-next.com/community/FAQ.html)
- [For Translators](https://pdf2zh-next.com/community/CONTRIBUTING_translation.html)

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

> [!NOTE]
> Cette documentation peut contenir du contenu généré par IA. Bien que nous nous efforcions d'être précis, il peut y avoir des inexactitudes. Veuillez signaler tout problème via :
>
> - [Problèmes GitHub](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - Contribution communautaire (les PR sont les bienvenues !)
>
> Merci pour votre compréhension et votre soutien !

### Liens rapides

- [Accueil](https://pdf2zh-next.com/)
- [Commencer](https://pdf2zh-next.com/getting-started/)
- [Ligne de commande](https://pdf2zh-next.com/getting-started/CLI.html)
- [WebUI](https://pdf2zh-next.com/getting-started/USAGE_webui.html)
- [Langues supportées](https://pdf2zh-next.com/advanced/LANGUAGE.html)
- [FAQ](https://pdf2zh-next.com/community/FAQ.html)
- [Guide de contribution des traductions](https://pdf2zh-next.com/community/CONTRIBUTING_translation.html)

This function is an asynchronous generator that streams the translation results. It is useful for translating large documents without waiting for the entire translation to complete.

### Parameters
- `pdf_path`: Path to the PDF file to be translated.
- `source_lang`: Source language code (e.g., 'en' for English).
- `target_lang`: Target language code (e.g., 'zh' for Chinese).
- `api_key`: Your API key for the translation service.
- `api_url`: Base URL for the translation service API.
- `timeout`: Timeout for each API request in seconds.
- `retries`: Number of retries for failed requests.
- `retry_delay`: Delay between retries in seconds.
- `batch_size`: Number of pages to process in each batch.
- `batch_delay`: Delay between batches in seconds.
- `callback`: Callback function to handle progress updates.

### Returns
An asynchronous generator that yields tuples of `(page_number, translated_text)`.

### Example
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for page_num, translated_text in do_translate_async_stream(
        pdf_path="document.pdf",
        source_lang="en",
        target_lang="zh",
        api_key="your_api_key",
        api_url="https://api.example.com/translate",
        timeout=30,
        retries=3,
        retry_delay=1,
        batch_size=5,
        batch_delay=0.5,
        callback=lambda progress: print(f"Progress: {progress}%")
    ):
        print(f"Page {page_num}: {translated_text}")

asyncio.run(main())
```

### Notes
- The function processes the PDF in batches to manage memory and API usage.
- Use the `callback` parameter to monitor progress.
- Ensure proper error handling for production use.

---

### TRANSLATION RESULT

pdf2zh is an open-source tool that allows you to translate PDF documents from English to Chinese, supporting various translation services.

!!! Note

    This tool is based on the [PDFMathTranslate](https://github.com/SUSYUSTC/PdfTranslate) project, which is licensed under the GPLv3. We have made some modifications and optimizations.

### Features

- [x] Support for multiple translation services
- [x] Support for command line and WebUI
- [x] Support for LaTeX and Word output formats
- [x] Support for custom translation prompts
- [x] Support for bilingual output

---

### TRANSLATION RESULT

### Aperçu

pdf2zh est un outil open-source qui vous permet de traduire des documents PDF de l'anglais vers le chinois, en prenant en charge divers services de traduction.

!!! Note

    Cet outil est basé sur le projet [PDFMathTranslate](https://github.com/SUSYUSTC/PdfTranslate), qui est sous licence GPLv3. Nous avons effectué quelques modifications et optimisations.

### Fonctionnalités

- [x] Prise en charge de plusieurs services de traduction
- [x] Prise en charge de la ligne de commande et de l'interface WebUI
- [x] Prise en charge des formats de sortie LaTeX et Word
- [x] Prise en charge des invites de traduction personnalisées
- [x] Prise en charge de la sortie bilingue
- Each event has a type and a payload. The payload depends on the event type.

### Event Types

- `progress`: Emitted for each page translated. Payload: `{"page": 1, "total": 10, "percent": 10.0}`
- `translated_page`: Emitted when a page is translated. Payload: `{"page": 1, "translated_text": "..."}`
- `error`: Emitted when an error occurs. Payload: `{"error": "Error message"}`
- `finished`: Emitted when translation is complete. Payload: `{"output_file": "path/to/output.pdf"}`

### Example Usage

```python
from pdf2zh import do_translate_async_stream, SettingsModel

async def main():
    settings = SettingsModel(
        input_file="input.pdf",
        output_file="output.pdf",
        source_lang="en",
        target_lang="zh",
        service="google",
        api_key="your_api_key"
    )
    
    async for event in do_translate_async_stream(settings, "input.pdf"):
        if event["type"] == "progress":
            print(f"Progress: {event['payload']['percent']}%")
        elif event["type"] == "translated_page":
            print(f"Page {event['payload']['page']} translated")
        elif event["type"] == "error":
            print(f"Error: {event['payload']['error']}")
        elif event["type"] == "finished":
            print(f"Translation complete: {event['payload']['output_file']}")

asyncio.run(main())
```

### Notes

- This function is designed for advanced users who need fine-grained control over the translation process.
- The async generator will yield events in the order they occur.
- You must handle errors appropriately in your application.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

- do_translate_async_stream est le point d'entrée asynchrone de bas niveau qui traduit un seul PDF et produit un flux d'événements (progrès/erreur/fin).
- Il est adapté pour construire votre propre interface utilisateur ou CLI où vous voulez un progrès en temps réel et un contrôle total sur les résultats.
- Il accepte un SettingsModel validé et un chemin de fichier et retourne un générateur asynchrone d'événements dict.
- Chaque événement a un type et une charge utile. La charge utile dépend du type d'événement.

### Types d'événements

- `progress` : Émis pour chaque page traduite. Charge utile : `{"page": 1, "total": 10, "percent": 10.0}`
- `translated_page` : Émis lorsqu'une page est traduite. Charge utile : `{"page": 1, "translated_text": "..."}`
- `error` : Émis lorsqu'une erreur se produit. Charge utile : `{"error": "Message d'erreur"}`
- `finished` : Émis lorsque la traduction est terminée. Charge utile : `{"output_file": "chemin/vers/output.pdf"}`

### Exemple d'utilisation

```python
from pdf2zh import do_translate_async_stream, SettingsModel

async def main():
    settings = SettingsModel(
        input_file="input.pdf",
        output_file="output.pdf",
        source_lang="en",
        target_lang="zh",
        service="google",
        api_key="your_api_key"
    )
    
    async for event in do_translate_async_stream(settings, "input.pdf"):
        if event["type"] == "progress":
            print(f"Progrès : {event['payload']['percent']}%")
        elif event["type"] == "translated_page":
            print(f"Page {event['payload']['page']} traduite")
        elif event["type"] == "error":
            print(f"Erreur : {event['payload']['error']}")
        elif event["type"] == "finished":
            print(f"Traduction terminée : {event['payload']['output_file']}")

asyncio.run(main())
```

### Notes

- Cette fonction est conçue pour les utilisateurs avancés qui ont besoin d'un contrôle fin du processus de traduction.
- Le générateur asynchrone produira des événements dans l'ordre où ils se produisent.
- Vous devez gérer les erreurs de manière appropriée dans votre application.

If you want to add a signature to the translated PDF, you can use the `--signature` parameter to specify the signature content.

```bash
pdf2zh input.pdf --signature "Translated by pdf2zh"
```

The default signature is `Translated by PDFMathTranslate`.

---

### OUTPUT LANGUAGE

fr
- Returns: AsyncIterator[TranslateEvent]
- Raises:
  - FileNotFoundError: if the input PDF does not exist.
  - ValidationError: if the settings are invalid.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

- Importation : `from pdf2zh_next.high_level import do_translate_async_stream`
- Appel : `async for event in do_translate_async_stream(settings, file): ...`
- Paramètres :
  - settings : SettingsModel. Doit être valide ; la fonction appellera `settings.validate_settings()`.
  - file : str | pathlib.Path. Le PDF unique à traduire. Doit exister.
- Retourne : AsyncIterator[TranslateEvent]
- Lève :
  - FileNotFoundError : si le PDF d'entrée n'existe pas.
  - ValidationError : si les paramètres sont invalides.

This is a note.

Warning: This is a warning.

Important: This is important.

Tip: This is a tip.

Caution: This is a caution.

---

### OUTPUT

Note : Ceci est une note.

Warning : Ceci est un avertissement.

Important : Ceci est important.

Tip : Ceci est un conseil.

Caution : Ceci est une mise en garde.
- If `settings.basic.overwrite` is True, the output file will be overwritten if it exists.
- If `settings.basic.overwrite` is False, the output file path will be modified to avoid overwriting (e.g., `output_1.pdf`).

---

### TRANSLATION RESULT

- settings.basic.input_files est ignoré par cette fonction ; seul le `file` donné est traduit.
- Si `settings.basic.debug` est True, la traduction s'exécute dans le processus principal ; sinon, elle s'exécute dans un sous-processus. Le schéma d'événement est identique dans les deux cas.
- Si `settings.basic.overwrite` est True, le fichier de sortie sera écrasé s'il existe.
- Si `settings.basic.overwrite` est False, le chemin du fichier de sortie sera modifié pour éviter l'écrasement (par exemple, `output_1.pdf`).

This document outlines the event stream contract for the PDFMathTranslate application.

#### Event Types

The application emits the following events:

- `file_processing_started`: Emitted when a PDF file starts being processed.
- `file_processing_completed`: Emitted when a PDF file has been processed.
- `file_processing_failed`: Emitted when a PDF file fails to process.

#### Event Data

Each event includes the following data:

- `event_type`: The type of event (as listed above).
- `timestamp`: The time the event occurred (ISO 8601 format).
- `file_path`: The path to the PDF file being processed.
- `additional_data`: Additional context-specific data (if applicable).

#### Example

```json
{
  "event_type": "file_processing_started",
  "timestamp": "2023-10-05T14:48:00.000Z",
  "file_path": "/path/to/file.pdf",
  "additional_data": null
}
```

---

### OUTPUT LANGUAGE

fr

---

Please begin.
- `job.progress`: Emitted periodically to report progress. Contains `progress` (0-100) and `message`.
- `job.done`: Emitted when the job completes successfully. Contains the final result.
- `job.error`: Emitted when the job fails. Contains error details.

### Example Output

```json
{"type": "job.progress", "data": {"progress": 50, "message": "Processing page 10"}}
{"type": "job.done", "data": {"result": "Translation completed successfully"}}
{"type": "job.error", "data": {"error": "Network error", "details": "Failed to connect to API"}}
```

### Notes

- The event stream is newline-delimited JSON (JSONL).
- Each event is a complete JSON object on a single line.
- The stream may contain multiple events of the same type.
- The client should handle events as they are received and not wait for the stream to complete.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

Le générateur asynchrone produit des événements de type dict JSON avec les types suivants :
- `job.progress` : Émis périodiquement pour rapporter la progression. Contient `progress` (0-100) et `message`.
- `job.done` : Émis lorsque le travail se termine avec succès. Contient le résultat final.
- `job.error` : Émis lorsque le travail échoue. Contient les détails de l'erreur.

### Exemple de sortie

```json
{"type": "job.progress", "data": {"progress": 50, "message": "Traitement de la page 10"}}
{"type": "job.done", "data": {"result": "Traduction terminée avec succès"}}
{"type": "job.error", "data": {"error": "Erreur réseau", "details": "Échec de connexion à l'API"}}
```

### Notes

- Le flux d'événements est du JSON délimité par des nouvelles lignes (JSONL).
- Chaque événement est un objet JSON complet sur une seule ligne.
- Le flux peut contenir plusieurs événements du même type.
- Le client doit traiter les événements au fur et à mesure de leur réception et ne pas attendre la fin du flux.

- `stage`: stage where error occurred

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

- Événement de résumé d'étape : `stage_summary` (optionnel, peut apparaître en premier)
  - Champs
    - `type` : "stage_summary"
    - `stages` : liste d'objets `{ "name": str, "percent": float }` décrivant la répartition estimée du travail
    - `part_index` : peut être 0 pour cet événement de résumé
    - `total_parts` : nombre total de parties (>= 1)

- Événements de progression : `progress_start`, `progress_update`, `progress_end`
  - Champs communs
    - `type` : l'un des types ci-dessus
    - `stage` : nom d'étape lisible par l'humain (par exemple, "Analyser le PDF et créer une représentation intermédiaire", "Traduire les paragraphes", "Sauvegarder le PDF")
    - `stage_progress` : float dans [0, 100] indiquant la progression dans l'étape actuelle
    - `overall_progress` : float dans [0, 100] indiquant la progression globale
    - `part_index` : index de la partie actuelle (généralement basé sur 1 pour les événements de progression)
    - `total_parts` : nombre total de parties (>= 1). Les documents volumineux peuvent être divisés automatiquement.
    - `stage_current` : étape actuelle dans le stage
    - `stage_total` : nombre total d'étapes dans le stage

- Événement de fin : `finish`
  - Champs
    - `type` : "finish"
    - `translate_result` : un **objet** fournissant les sorties finales (NOTE : pas un dictionnaire, mais une instance de classe)
      - `original_pdf_path` : Chemin vers le PDF d'entrée
      - `mono_pdf_path` : Chemin vers le PDF traduit monolingue (ou None)
      - `dual_pdf_path` : Chemin vers le PDF traduit bilingue (ou None)
      - `no_watermark_mono_pdf_path` : Chemin vers la sortie monolingue sans filigrane (si produite), sinon None
      - `no_watermark_dual_pdf_path` : Chemin vers la sortie bilingue sans filigrane (si produite), sinon None
      - `auto_extracted_glossary_path` : Chemin vers le glossaire CSV extrait automatiquement (ou None)
      - `total_seconds` : secondes écoulées (float)
      - `peak_memory_usage` : utilisation maximale approximative de la mémoire pendant la traduction (float ; unités dépendantes de l'implémentation)

- Événement d'erreur : `error`
  - Champs
    - `type` : "error"
    - `error` : message d'erreur lisible par l'humain
    - `error_type` : l'un de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details` : détails optionnels (par exemple, erreur originale ou traceback)
    - `stage` : étape où l'erreur s'est produite

When using the `--output` parameter, if the output file already exists, it will be overwritten without warning. To avoid accidental overwrites, use the `--force` flag to confirm overwriting.

---

### TRANSLATION RESULT

Comportement important : Lors de l'utilisation du paramètre `--output`, si le fichier de sortie existe déjà, il sera écrasé sans avertissement. Pour éviter les écrasements accidentels, utilisez le drapeau `--force` pour confirmer l'écrasement.
- The generator is not reusable after completion or error.
- The generator may be prematurely closed by the caller, which will cancel the translation.

---

### TRANSLATION RESULT

- Un `stage_summary` facultatif peut être émis avant le début de la progression.
- En cas de certains échecs, le générateur émettra d'abord un événement `error`, puis lèvera une exception dérivée de `TranslationError`. Vous devez à la fois vérifier les événements d'erreur et être prêt à attraper les exceptions.
- Les événements `progress_update` peuvent se répéter avec des valeurs identiques ; les consommateurs doivent effectuer un debounce si nécessaire.
- Arrêtez de consommer le flux lorsque vous recevez un événement `finish`.
- Le générateur n'est pas réutilisable après achèvement ou erreur.
- Le générateur peut être fermé prématurément par l'appelant, ce qui annulera la traduction.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

- Un `stage_summary` facultatif peut être émis avant le début de la progression.
- En cas de certains échecs, le générateur émettra d'abord un événement `error`, puis lèvera une exception dérivée de `TranslationError`. Vous devez à la fois vérifier les événements d'erreur et être prêt à attraper les exceptions.
- Les événements `progress_update` peuvent se répéter avec des valeurs identiques ; les consommateurs doivent effectuer un debounce si nécessaire.
- Arrêtez de consommer le flux lorsque vous recevez un événement `finish`.
- Le générateur n'est pas réutilisable après achèvement ou erreur.
- Le générateur peut être fermé prématurément par l'appelant, ce qui annulera la traduction.

{#minimal-usage-example-async}

Here is a minimal example of how to use `pdf2zh` asynchronously with default settings:

```python
import asyncio
from pdf2zh import PDFTranslator

async def main():
    translator = PDFTranslator()
    await translator.translate(
        input_file="input.pdf",
        output_file="output.pdf"
    )

if __name__ == "__main__":
    asyncio.run(main())
```

This will:
- Translate all text in `input.pdf` to Chinese (default target language)
- Preserve the original layout and formatting
- Save the result to `output.pdf`

---

### ORIGINAL TEXT

### Exemple d'utilisation minimal (Asynchrone) {#exemple-dutilisation-minimal-asynchrone}

Voici un exemple minimal d'utilisation de `pdf2zh` de manière asynchrone avec les paramètres par défaut :

```python
import asyncio
from pdf2zh import PDFTranslator

async def main():
    translator = PDFTranslator()
    await translator.translate(
        input_file="input.pdf",
        output_file="output.pdf"
    )

if __name__ == "__main__":
    asyncio.run(main())
```

Cela va :
- Traduire tout le texte dans `input.pdf` en chinois (langue cible par défaut)
- Préserver la mise en page et le formatage d'origine
- Sauvegarder le résultat dans `output.pdf`
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

and Refund Policy

#### 1. Cancellation of Services

You may cancel your subscription to our services at any time through your account settings or by contacting our customer support team. Upon cancellation, your subscription will remain active until the end of the current billing cycle, after which it will not renew.

#### 2. Refund Policy

We offer a 30-day money-back guarantee for all subscription plans. If you are not satisfied with our services within the first 30 days of your subscription, you may request a full refund. Refund requests must be submitted within 30 days of the initial purchase.

To request a refund, please contact our customer support team with your order details. Once your request is received and processed, we will issue a refund to your original method of payment within 7-10 business days.

Please note that refunds are only available for the first subscription payment and do not apply to renewals or additional purchases made during the subscription period.

#### 3. Exceptions

Refunds are not available for:

- Partial months of service
- Services that have been used excessively or in violation of our Terms of Service
- Subscription renewals after the initial 30-day period

#### 4. Changes to This Policy

We reserve the right to modify this Cancellation and Refund Policy at any time. Any changes will be effective immediately upon posting on our website. Your continued use of our services after any changes constitutes your acceptance of the new terms.

#### 5. Contact Us

If you have any questions about this Cancellation and Refund Policy, please contact us at support@example.com.

---

### TRANSLATION RESULT

### Politique d'annulation et de remboursement

#### 1. Annulation des services

Vous pouvez annuler votre abonnement à nos services à tout moment via les paramètres de votre compte ou en contactant notre équipe de support client. Lors de l'annulation, votre abonnement restera actif jusqu'à la fin du cycle de facturation en cours, après quoi il ne sera pas renouvelé.

#### 2. Politique de remboursement

Nous offrons une garantie de remboursement de 30 jours pour tous les plans d'abonnement. Si vous n'êtes pas satisfait de nos services dans les 30 premiers jours de votre abonnement, vous pouvez demander un remboursement intégral. Les demandes de remboursement doivent être soumises dans les 30 jours suivant l'achat initial.

Pour demander un remboursement, veuillez contacter notre équipe de support client avec les détails de votre commande. Une fois votre demande reçue et traitée, nous procéderons au remboursement sur votre mode de paiement initial dans un délai de 7 à 10 jours ouvrables.

Veuillez noter que les remboursements ne sont disponibles que pour le premier paiement d'abonnement et ne s'appliquent pas aux renouvellements ou aux achats supplémentaires effectués pendant la période d'abonnement.

#### 3. Exceptions

Les remboursements ne sont pas disponibles pour :

- Les mois partiels de service
- Les services qui ont été utilisés de manière excessive ou en violation de nos Conditions d'utilisation
- Les renouvellements d'abonnement après la période initiale de 30 jours

#### 4. Modifications de cette politique

Nous nous réservons le droit de modifier cette Politique d'annulation et de remboursement à tout moment. Toute modification sera effective immédiatement après sa publication sur notre site web. Votre utilisation continue de nos services après toute modification constitue votre acceptation des nouvelles conditions.

#### 5. Contactez-nous

Si vous avez des questions concernant cette Politique d'annulation et de remboursement, veuillez nous contacter à support@example.com.
- You can cancel the task consuming the stream. Cancellation is propagated to the underlying translation process.

---

### TRANSLATION RESULT

Vous pouvez annuler la tâche consommant le flux. L'annulation est propagée au processus de traduction sous-jacent.

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

!!! Note
    This feature is in beta. We are looking for feedback!

Event shapes are defined with the `shape` property in the event definition. The shape defines the area of the event that is interactive. The shape is defined as a polygon of points relative to the event's position. The points are defined in the order they are connected.

The following example shows how to define a triangle event shape.

```json
{
  "events": [
    {
      "id": "triangle-event",
      "name": "Triangle Event",
      "description": "This event has a triangular shape.",
      "shape": [
        { "x": 0, "y": 0 },
        { "x": 100, "y": 0 },
        { "x": 50, "y": 100 }
      ]
    }
  ]
}
```

The shape is defined as a polygon with three points. The points are relative to the event's position. The first point is at (0, 0), the second at (100, 0), and the third at (50, 100). The points are connected in the order they are defined.

The following example shows how to define a circle event shape. Circles are approximated using a polygon with many points.

```json
{
  "events": [
    {
      "id": "circle-event",
      "name": "Circle Event",
      "description": "This event has a circular shape.",
      "shape": [
        { "x": 50, "y": 0 },
        { "x": 49, "y": 3 },
        { "x": 48, "y": 6 },
        // ... many more points to approximate a circle
        { "x": 50, "y": 100 },
        { "x": 52, "y": 97 },
        // ... and so on
        { "x": 50, "y": 0 }
      ]
    }
  ]
}
```

The circle is approximated using a polygon with many points. The more points you use, the smoother the circle will appear. However, using too many points may impact performance.

You can also define complex shapes by combining multiple polygons. The following example shows how to define a donut shape.

```json
{
  "events": [
    {
      "id": "donut-event",
      "name": "Donut Event",
      "description": "This event has a donut shape.",
      "shape": [
        // Outer circle
        { "x": 50, "y": 0 },
        { "x": 49, "y": 3 },
        // ... many points for outer circle
        { "x": 50, "y": 100 },
        // Inner circle (hole)
        { "x": 50, "y": 10 },
        { "x": 49, "y": 13 },
        // ... many points for inner circle
        { "x": 50, "y": 90 }
      ]
    }
  ]
}
```

The donut shape is defined by first defining the outer circle and then the inner circle. The inner circle creates a hole in the shape. The order of the points matters. The outer circle should be defined in clockwise order, and the inner circle should be defined in counter-clockwise order.

For more information on event shapes, see the [Event Shapes](../advanced/event-shapes.md) documentation.

---

### FORMES D'ÉVÉNEMENTS EXEMPLES

!!! Note
    Cette fonctionnalité est en version bêta. Nous recherchons des retours d'expérience !

Les formes d'événements sont définies avec la propriété `shape` dans la définition de l'événement. La forme définit la zone de l'événement qui est interactive. La forme est définie comme un polygone de points relatifs à la position de l'événement. Les points sont définis dans l'ordre où ils sont connectés.

L'exemple suivant montre comment définir une forme d'événement triangulaire.

```json
{
  "events": [
    {
      "id": "triangle-event",
      "name": "Triangle Event",
      "description": "This event has a triangular shape.",
      "shape": [
        { "x": 0, "y": 0 },
        { "x": 100, "y": 0 },
        { "x": 50, "y": 100 }
      ]
    }
  ]
}
```

La forme est définie comme un polygone à trois points. Les points sont relatifs à la position de l'événement. Le premier point est à (0, 0), le deuxième à (100, 0) et le troisième à (50, 100). Les points sont connectés dans l'ordre où ils sont définis.

L'exemple suivant montre comment définir une forme d'événement circulaire. Les cercles sont approximés en utilisant un polygone avec de nombreux points.

```json
{
  "events": [
    {
      "id": "circle-event",
      "name": "Circle Event",
      "description": "This event has a circular shape.",
      "shape": [
        { "x": 50, "y": 0 },
        { "x": 49, "y": 3 },
        { "x": 48, "y": 6 },
        // ... beaucoup plus de points pour approximer un cercle
        { "x": 50, "y": 100 },
        { "x": 52, "y": 97 },
        // ... et ainsi de suite
        { "x": 50, "y": 0 }
      ]
    }
  ]
}
```

Le cercle est approximé en utilisant un polygone avec de nombreux points. Plus vous utilisez de points, plus le cercle apparaîtra lisse. Cependant, utiliser trop de points peut impacter les performances.

Vous pouvez également définir des formes complexes en combinant plusieurs polygones. L'exemple suivant montre comment définir une forme de donut.

```json
{
  "events": [
    {
      "id": "donut-event",
      "name": "Donut Event",
      "description": "This event has a donut shape.",
      "shape": [
        // Cercle extérieur
        { "x": 50, "y": 0 },
        { "x": 49, "y": 3 },
        // ... nombreux points pour le cercle extérieur
        { "x": 50, "y": 100 },
        // Cercle intérieur (trou)
        { "x": 50, "y": 10 },
        { "x": 49, "y": 13 },
        // ... nombreux points pour le cercle intérieur
        { "x": 50, "y": 90 }
      ]
    }
  ]
}
```

La forme de donut est définie en définissant d'abord le cercle extérieur puis le cercle intérieur. Le cercle intérieur crée un trou dans la forme. L'ordre des points est important. Le cercle extérieur doit être défini dans le sens horaire, et le cercle intérieur doit être défini dans le sens anti-horaire.

Pour plus d'informations sur les formes d'événements, consultez la documentation [Formes d'événements](../advanced/event-shapes.md).
This is an example of a stage summary event.

```json
{
  "event": "stage_summary",
  "data": {
    "stage": "translation",
    "status": "completed",
    "summary": {
      "total_pages": 100,
      "translated_pages": 100,
      "failed_pages": 0,
      "start_time": "2023-10-05T14:48:00.000Z",
      "end_time": "2023-10-05T15:30:00.000Z",
      "duration_seconds": 2520,
      "average_time_per_page": 25.2
    }
  }
}
```

This event is emitted when a stage (e.g., translation, OCR, etc.) is completed. It provides a summary of the stage's execution.

---

### TRANSLATION RESULT

Événement de résumé d'étape (exemple) : Ceci est un exemple d'événement de résumé d'étape.

```json
{
  "event": "stage_summary",
  "data": {
    "stage": "translation",
    "status": "completed",
    "summary": {
      "total_pages": 100,
      "translated_pages": 100,
      "failed_pages": 0,
      "start_time": "2023-10-05T14:48:00.000Z",
      "end_time": "2023-10-05T15:30:00.000Z",
      "duration_seconds": 2520,
      "average_time_per_page": 25.2
    }
  }
}
```

Cet événement est émis lorsqu'une étape (par exemple, traduction, OCR, etc.) est terminée. Il fournit un résumé de l'exécution de l'étape.
- ### Quick Start: This guide will help you get started with pdf2zh quickly.

#### Installation

You can install pdf2zh using pip:

```bash
pip install pdf2zh
```

#### Basic Usage

1. **Using Command Line**:

    ```bash
    pdf2zh input.pdf
    ```

    This will translate `input.pdf` to Chinese and save the result as `input_zh.pdf`.

2. **Using WebUI**:

    Start the WebUI server:

    ```bash
    pdf2zh --web
    ```

    Then open your browser and go to `http://localhost:7860`.

3. **Using Python API**:

    ```python
    from pdf2zh import PDFTranslator

    translator = PDFTranslator()
    translator.translate("input.pdf", "output.pdf")
    ```

For more detailed information, please refer to the [Usage](https://pdf2zh-next.com/getting-started/USAGE.html) documentation.

---

### TRANSLATION RESULT

### Commencer rapidement

Ce guide vous aidera à démarrer rapidement avec pdf2zh.

#### Installation

Vous pouvez installer pdf2zh en utilisant pip :

```bash
pip install pdf2zh
```

#### Utilisation de base

1. **Utilisation de la ligne de commande** :

    ```bash
    pdf2zh input.pdf
    ```

    Cela traduira `input.pdf` en chinois et sauvegardera le résultat sous `input_zh.pdf`.

2. **Utilisation de l'interface WebUI** :

    Démarrez le serveur WebUI :

    ```bash
    pdf2zh --web
    ```

    Puis ouvrez votre navigateur et allez à `http://localhost:7860`.

3. **Utilisation de l'API Python** :

    ```python
    from pdf2zh import PDFTranslator

    translator = PDFTranslator()
    translator.translate("input.pdf", "output.pdf")
    ```

Pour des informations plus détaillées, veuillez consulter la documentation [Utilisation](https://pdf2zh-next.com/getting-started/USAGE.html).

---

### BYPASS LIST

- pdf2zh
- WebUI
- Python API
- ---

---

### ORIGINAL TEXT

### Using the WebUI: {#using-the-webui}

The WebUI provides a graphical interface for translating PDF documents. It is especially useful for users who are not familiar with the command line.

#### Starting the WebUI

To start the WebUI, run the following command:

```bash
pdf2zh --web
```

This will start a local server. By default, the WebUI is accessible at `http://localhost:7860`.

#### Using the WebUI

1. Open your browser and go to `http://localhost:7860`.
2. Upload the PDF file you want to translate.
3. Select the source and target languages.
4. Click the "Translate" button to start the translation.
5. Once the translation is complete, you can download the translated PDF.

#### WebUI Options

The WebUI provides several options for customizing the translation:

- **Source Language**: The language of the original PDF document.
- **Target Language**: The language to translate to.
- **Translation Service**: The translation service to use.
- **Output Format**: The format of the output file (PDF, LaTeX, or Word).
- **Bilingual Output**: Whether to include the original text alongside the translation.

For more information on the available options, please refer to the [WebUI Documentation](https://pdf2zh-next.com/getting-started/USAGE_webui.html).

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

### Utilisation de l'interface WebUI {#utilisation-de-linterface-webui}

L'interface WebUI fournit une interface graphique pour traduire des documents PDF. Elle est particulièrement utile pour les utilisateurs qui ne sont pas familiers avec la ligne de commande.

#### Démarrage de l'interface WebUI

Pour démarrer l'interface WebUI, exécutez la commande suivante :

```bash
pdf2zh --web
```

Cela démarrera un serveur local. Par défaut, l'interface WebUI est accessible à l'adresse `http://localhost:7860`.

#### Utilisation de l'interface WebUI

1. Ouvrez votre navigateur et allez à `http://localhost:7860`.
2. Téléchargez le fichier PDF que vous souhaitez traduire.
3. Sélectionnez les langues source et cible.
4. Cliquez sur le bouton "Traduire" pour démarrer la traduction.
5. Une fois la traduction terminée, vous pouvez télécharger le PDF traduit.

#### Options de l'interface WebUI

L'interface WebUI propose plusieurs options pour personnaliser la traduction :

- **Langue source** : La langue du document PDF original.
- **Langue cible** : La langue vers laquelle traduire.
- **Service de traduction** : Le service de traduction à utiliser.
- **Format de sortie** : Le format du fichier de sortie (PDF, LaTeX ou Word).
- **Sortie bilingue** : Indique s'il faut inclure le texte original à côté de la traduction.

Pour plus d'informations sur les options disponibles, veuillez consulter la [Documentation WebUI](https://pdf2zh-next.com/getting-started/USAGE_webui.html).
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

The `progress` event is emitted during the translation process to provide updates on the current progress. The event object contains the following properties:

- `type`: Always `"progress"`
- `current`: The current page being processed (number)
- `total`: The total number of pages (number)
- `percentage`: The completion percentage (number between 0 and 100)

Example event object:
```json
{
  "type": "progress",
  "current": 5,
  "total": 20,
  "percentage": 25
}
```

You can listen for this event using the `on` method:

```javascript
translator.on('progress', (event) => {
  console.log(`Processing page ${event.current} of ${event.total} (${event.percentage}%)`);
});
```

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

Événement de progression (exemple) : L'événement `progress` est émis pendant le processus de traduction pour fournir des mises à jour sur la progression actuelle. L'objet d'événement contient les propriétés suivantes :

- `type` : Toujours `"progress"`
- `current` : La page en cours de traitement (nombre)
- `total` : Le nombre total de pages (nombre)
- `percentage` : Le pourcentage d'avancement (nombre entre 0 et 100)

Exemple d'objet d'événement :
```json
{
  "type": "progress",
  "current": 5,
  "total": 20,
  "percentage": 25
}
```

Vous pouvez écouter cet événement en utilisant la méthode `on` :

```javascript
translator.on('progress', (event) => {
  console.log(`Traitement de la page ${event.current} sur ${event.total} (${event.percentage}%)`);
});
```
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

This event is emitted when the translation process is complete.

### Event Data

- `total_pages`: The total number of pages processed.
- `successful_pages`: The number of pages successfully translated.
- `failed_pages`: The number of pages that failed to translate.
- `output_file`: The path to the output file.
- `translation_time`: The total time taken for the translation process (in seconds).

### Example

```json
{
  "event_type": "finish",
  "timestamp": "2023-10-05T14:48:00.000Z",
  "data": {
    "total_pages": 100,
    "successful_pages": 95,
    "failed_pages": 5,
    "output_file": "/path/to/output.pdf",
    "translation_time": 120.5
  }
}
```

### Notes

- This event is emitted regardless of whether the translation was successful or not.
- If the translation process is interrupted, this event may not be emitted.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

Événement de fin (exemple) : Cet événement est émis lorsque le processus de traduction est terminé.

### Données de l'événement

- `total_pages` : Le nombre total de pages traitées.
- `successful_pages` : Le nombre de pages traduites avec succès.
- `failed_pages` : Le nombre de pages dont la traduction a échoué.
- `output_file` : Le chemin vers le fichier de sortie.
- `translation_time` : Le temps total pris pour le processus de traduction (en secondes).

### Exemple

```json
{
  "event_type": "finish",
  "timestamp": "2023-10-05T14:48:00.000Z",
  "data": {
    "total_pages": 100,
    "successful_pages": 95,
    "failed_pages": 5,
    "output_file": "/path/to/output.pdf",
    "translation_time": 120.5
  }
}
```

### Notes

- Cet événement est émis que la traduction ait réussi ou non.
- Si le processus de traduction est interrompu, cet événement peut ne pas être émis.
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

This event is triggered when an error occurs during the translation process.

```json
{
  "event_type": "translation_error",
  "timestamp": "2023-10-05T14:48:00.000Z",
  "file_path": "/path/to/file.pdf",
  "error_message": "Failed to connect to translation service",
  "error_code": "CONNECTION_ERROR"
}
```

### Event Data

- `event_type`: Always "translation_error"
- `timestamp`: The time the error occurred (ISO 8601 format)
- `file_path`: The path to the PDF file being processed
- `error_message`: A human-readable description of the error
- `error_code`: A machine-readable error code

### Error Codes

- `CONNECTION_ERROR`: Failed to connect to the translation service
- `AUTHENTICATION_ERROR`: Invalid API key or authentication failure
- `RATE_LIMIT_EXCEEDED`: Too many requests to the translation service
- `INVALID_FILE`: The PDF file is invalid or corrupted
- `UNKNOWN_ERROR`: An unexpected error occurred

### Handling Errors

When this event is emitted, the translation process will be stopped. You should handle this event to provide user feedback and potentially retry the operation.

For more information on error handling, see the [Error Handling](../advanced/error-handling.md) documentation.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

Événement d'erreur (exemple) : Cet événement est déclenché lorsqu'une erreur se produit pendant le processus de traduction.

```json
{
  "event_type": "translation_error",
  "timestamp": "2023-10-05T14:48:00.000Z",
  "file_path": "/path/to/file.pdf",
  "error_message": "Échec de la connexion au service de traduction",
  "error_code": "CONNECTION_ERROR"
}
```

### Données de l'événement

- `event_type` : Toujours "translation_error"
- `timestamp` : L'heure à laquelle l'erreur s'est produite (format ISO 8601)
- `file_path` : Le chemin du fichier PDF en cours de traitement
- `error_message` : Une description lisible par l'homme de l'erreur
- `error_code` : Un code d'erreur lisible par machine

### Codes d'erreur

- `CONNECTION_ERROR` : Échec de la connexion au service de traduction
- `AUTHENTICATION_ERROR` : Clé API invalide ou échec d'authentification
- `RATE_LIMIT_EXCEEDED` : Trop de requêtes au service de traduction
- `INVALID_FILE` : Le fichier PDF est invalide ou corrompu
- `UNKNOWN_ERROR` : Une erreur inattendue s'est produite

### Gestion des erreurs

Lorsque cet événement est émis, le processus de traduction sera arrêté. Vous devez gérer cet événement pour fournir un retour à l'utilisateur et potentiellement réessayer l'opération.

Pour plus d'informations sur la gestion des erreurs, consultez la documentation [Gestion des erreurs](../advanced/error-handling.md).
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

- **Translation Quality**: The quality of the translation depends on the translation service you choose. For more information, please refer to the [Documentation of Translation Services](https://pdf2zh-next.com/advanced/SERVICE.html).
- **Text Recognition**: If the PDF contains images with text, OCR (Optical Character Recognition) is required. pdf2zh supports OCR functionality. For more information, please refer to the [OCR](https://pdf2zh-next.com/advanced/OCR.html) documentation.
- **Mathematical Formulas**: If the PDF contains mathematical formulas, please refer to the [PDFMathTranslate](https://pdf2zh-next.com/advanced/MATH.html) documentation.
- **Language Code**: For the list of supported languages and their corresponding language codes, please refer to the [Supported Languages](https://pdf2zh-next.com/advanced/LANGUAGE.html) documentation.

---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

### Notes & Bonnes pratiques

- **Qualité de la traduction** : La qualité de la traduction dépend du service de traduction que vous choisissez. Pour plus d'informations, veuillez consulter la [Documentation des services de traduction](https://pdf2zh-next.com/advanced/SERVICE.html).
- **Reconnaissance de texte** : Si le PDF contient des images avec du texte, une OCR (Reconnaissance Optique de Caractères) est nécessaire. pdf2zh prend en charge la fonctionnalité OCR. Pour plus d'informations, veuillez consulter la documentation [OCR](https://pdf2zh-next.com/advanced/OCR.html).
- **Formules mathématiques** : Si le PDF contient des formules mathématiques, veuillez consulter la documentation [PDFMathTranslate](https://pdf2zh-next.com/advanced/MATH.html).
- **Code de langue** : Pour la liste des langues supportées et leurs codes de langue correspondants, veuillez consulter la documentation [Langues supportées](https://pdf2zh-next.com/advanced/LANGUAGE.html).
---

### OUTPUT LANGUAGE

fr

---

### OUTPUT

- Toujours gérer à la fois les événements d'erreur et les exceptions du générateur.
- Interrompre la boucle sur `finish` pour éviter un travail inutile.
- S'assurer que le `file` existe et que `settings.validate_settings()` passe avant l'appel.
- Les documents volumineux peuvent être divisés ; utiliser `part_index/total_parts` et `overall_progress` pour piloter votre interface utilisateur.
- Débouncer `progress_update` si votre interface utilisateur est sensible aux mises à jour répétées et identiques.
- `report_interval` (SettingsModel) : contrôle uniquement le taux d'émission des événements `progress_update`. Il n'affecte pas `stage_summary`, `progress_start`, `progress_end` ou `finish`. La valeur par défaut est 0.1s et le minimum autorisé est 0.05s. Selon la logique du moniteur de progression, lorsque `stage_total <= 3`, les mises à jour ne sont pas limitées par `report_interval`.

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>