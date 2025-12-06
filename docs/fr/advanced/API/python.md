> [!NOTE]
> Cette documentation peut contenir du contenu généré par l'IA. Bien que nous nous efforcions d'être précis, il peut y avoir des inexactitudes. Veuillez signaler tout problème via :
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Contribution de la communauté (les PR sont les bienvenues !)

## Python API : do_translate_async_stream

### Aperçu
- do_translate_async_stream est le point d'entrée asynchrone de bas niveau qui traduit un seul PDF et produit un flux d'événements (progression/erreur/fin).
- Il est adapté pour construire votre propre interface utilisateur ou CLI où vous souhaitez une progression en temps réel et un contrôle total sur les résultats.
- Il accepte un SettingsModel validé et un chemin de fichier et retourne un générateur asynchrone d'événements sous forme de dictionnaires.

### Signature
- Importation : `from pdf2zh_next.high_level import do_translate_async_stream`
- Appel : `async for event in do_translate_async_stream(settings, file): ...`
- Paramètres :
  - settings : SettingsModel. Doit être valide ; la fonction appellera `settings.validate_settings()`.
  - file : str | pathlib.Path. Le PDF unique à traduire. Doit exister.

NOTE

- `settings.basic.input_files` est ignoré par cette fonction ; seul le `file` donné est traduit.
- Si `settings.basic.debug` est True, la traduction s'exécute dans le processus principal ; sinon, elle s'exécute dans un sous-processus. Le schéma d'événements est identique dans les deux cas.

### Contrat de flux d'événements
Le générateur asynchrone produit des événements de type dict similaires à JSON avec les types suivants :

- Événement de résumé des étapes : `stage_summary` (optionnel, peut apparaître en premier)
  - Champs
    - `type` : "stage_summary"
    - `stages` : liste d'objets `{ "name": str, "percent": float }` décrivant la répartition estimée du travail
    - `part_index` : peut être 0 pour cet événement de résumé
    - `total_parts` : nombre total de parties (>= 1)

- Événements de progression : `progress_start`, `progress_update`, `progress_end`
  - Champs communs
    - `type` : l'un des types ci-dessus
    - `stage` : nom d'étape lisible par un humain (par exemple, "Analyser le PDF et créer une représentation intermédiaire", "Traduire les paragraphes", "Enregistrer le PDF")
    - `stage_progress` : float dans [0, 100] indiquant la progression dans l'étape actuelle
    - `overall_progress` : float dans [0, 100] indiquant la progression globale
    - `part_index` : index de la partie actuelle (généralement basé sur 1 pour les événements de progression)
    - `total_parts` : nombre total de parties (>= 1). Les documents volumineux peuvent être divisés automatiquement.
    - `stage_current` : étape actuelle dans la phase
    - `stage_total` : nombre total d'étapes dans la phase

- Événement de fin : `finish`
  - Champs
    - `type` : "finish"
    - `translate_result` : un **objet** fournissant les sorties finales (NOTE : pas un dictionnaire, mais une instance de classe)
      - `original_pdf_path` : Chemin d'accès au PDF d'entrée
      - `mono_pdf_path` : Chemin d'accès au PDF traduit monolingue (ou None)
      - `dual_pdf_path` : Chemin d'accès au PDF traduit bilingue (ou None)
      - `no_watermark_mono_pdf_path` : Chemin d'accès à la sortie monolingue sans filigrane (si produite), sinon None
      - `no_watermark_dual_pdf_path` : Chemin d'accès à la sortie bilingue sans filigrane (si produite), sinon None
      - `auto_extracted_glossary_path` : Chemin d'accès au glossaire CSV extrait automatiquement (ou None)
      - `total_seconds` : secondes écoulées (float)
      - `peak_memory_usage` : utilisation maximale approximative de la mémoire pendant la traduction (float ; unités dépendantes de l'implémentation)

- Événement d'erreur : `error`
  - Champs
    - `type` : "error"
    - `error` : message d'erreur lisible par un humain
    - `error_type` : l'un de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details` : détails optionnels (par exemple, erreur originale ou traceback)

Comportement important :
- Un `stage_summary` facultatif peut être émis avant le début de la progression.
- En cas de certains échecs, le générateur produira d'abord un événement `error`, puis lèvera une exception dérivée de `TranslationError`. Vous devez à la fois vérifier les événements d'erreur et être prêt à intercepter les exceptions.
- Les événements `progress_update` peuvent se répéter avec des valeurs identiques ; les consommateurs doivent effectuer un anti-rebond si nécessaire.
- Arrêtez de consommer le flux lorsque vous recevez un événement `finish`.

### Exemple d'utilisation minimale (Asynchrone)
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

### Annulation
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

### Formes d'événements exemples
Résumé d'étape (exemple) :
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

Événement de progression (exemple) :
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

Événement de fin (exemple) :
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

Événement d'erreur (exemple) :
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Notes & Meilleures pratiques
- Toujours gérer à la fois les événements d'erreur et les exceptions provenant du générateur.
- Interrompre la boucle sur `finish` pour éviter un travail inutile.
- S'assurer que le `file` existe et que `settings.validate_settings()` passe avant d'appeler.
- Les documents volumineux peuvent être divisés ; utiliser `part_index/total_parts` et `overall_progress` pour piloter votre interface utilisateur.
- Débouncer `progress_update` si votre interface utilisateur est sensible aux mises à jour répétées et identiques.
- `report_interval` (SettingsModel) : contrôle uniquement le taux d'émission des événements `progress_update`. Il n'affecte pas `stage_summary`, `progress_start`, `progress_end` ou `finish`. La valeur par défaut est 0,1s et le minimum autorisé est 0,05s. Selon la logique du moniteur de progression, lorsque `stage_total <= 3`, les mises à jour ne sont pas limitées par `report_interval`.

<div align="right"> 
<h6><small>Une partie du contenu de cette page a été traduite par GPT et peut contenir des erreurs.</small></h6>