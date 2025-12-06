> [!NOTE]
> Esta documentação pode conter conteúdo gerado por IA. Embora nos esforcemos pela precisão, podem ocorrer imprecisões. Por favor, relate quaisquer problemas através de:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - Contribuição da comunidade (PRs são bem-vindos!)

## Python API: do_translate_async_stream

### Visão geral
- do_translate_async_stream é o ponto de entrada assíncrono de baixo nível que traduz um único PDF e produz um fluxo de eventos (progresso/erro/conclusão).
- É adequado para construir sua própria UI ou CLI onde você deseja progresso em tempo real e controle total sobre os resultados.
- Ele aceita um SettingsModel validado e um caminho de arquivo e retorna um gerador assíncrono de eventos de dicionário.

### Assinatura
- Importar: `from pdf2zh_next.high_level import do_translate_async_stream`
- Chamar: `async for event in do_translate_async_stream(settings, file): ...`
- Parâmetros:
  - settings: SettingsModel. Deve ser válido; a função chamará `settings.validate_settings()`.
  - file: str | pathlib.Path. O único PDF a ser traduzido. Deve existir.

Observação:

- `settings.basic.input_files` é ignorado por esta função; apenas o `file` fornecido é traduzido.
- Se `settings.basic.debug` for True, a tradução é executada no processo principal; caso contrário, é executada em um subprocesso. O esquema de eventos é idêntico para ambos.

### Contrato de Fluxo de Eventos
O gerador assíncrono produz eventos de dicionário semelhantes a JSON com os seguintes tipos:

- Evento de resumo de estágio: `stage_summary` (opcional, pode aparecer primeiro)
  - Campos
    - `type`: "stage_summary"
    - `stages`: lista de objetos `{ "name": str, "percent": float }` descrevendo a distribuição estimada do trabalho
    - `part_index`: pode ser 0 para este evento de resumo
    - `total_parts`: número total de partes (>= 1)

- Eventos de progresso: `progress_start`, `progress_update`, `progress_end`
  - Campos comuns
    - `type`: um dos acima
    - `stage`: nome do estágio legível por humanos (por exemplo, "Analisar PDF e Criar Representação Intermediária", "Traduzir Parágrafos", "Salvar PDF")
    - `stage_progress`: float em [0, 100] indicando o progresso dentro do estágio atual
    - `overall_progress`: float em [0, 100] indicando o progresso geral
    - `part_index`: índice da parte atual (normalmente baseado em 1 para eventos de progresso)
    - `total_parts`: número total de partes (>= 1). Documentos grandes podem ser divididos automaticamente.
    - `stage_current`: etapa atual dentro do estágio
    - `stage_total`: total de etapas dentro do estágio

- Evento de conclusão: `finish`
  - Campos
    - `type`: "finish"
    - `translate_result`: um **objeto** fornecendo as saídas finais (NOTA: não um dicionário, mas uma instância de classe)
      - `original_pdf_path`: Caminho para o PDF de entrada
      - `mono_pdf_path`: Caminho para o PDF traduzido monolíngue (ou None)
      - `dual_pdf_path`: Caminho para o PDF traduzido bilíngue (ou None)
      - `no_watermark_mono_pdf_path`: Caminho para a saída monolíngue sem marca d'água (se produzida), caso contrário None
      - `no_watermark_dual_pdf_path`: Caminho para a saída bilíngue sem marca d'água (se produzida), caso contrário None
      - `auto_extracted_glossary_path`: Caminho para o CSV do glossário extraído automaticamente (ou None)
      - `total_seconds`: segundos decorridos (float)
      - `peak_memory_usage`: uso aproximado de memória de pico durante a tradução (float; unidades dependentes da implementação)

- Evento de erro: `error`
  - Campos
    - `type`: "error"
    - `error`: mensagem de erro legível por humanos
    - `error_type`: um de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details`: detalhes opcionais (por exemplo, erro original ou traceback)

Comportamento importante:
- Um `stage_summary` opcional pode ser emitido antes do progresso começar.
- Em certas falhas, o gerador primeiro produzirá um evento `error` e, em seguida, levantará uma exceção derivada de `TranslationError`. Você deve verificar tanto os eventos de erro quanto estar preparado para capturar exceções.
- Eventos `progress_update` podem se repetir com valores idênticos; os consumidores devem fazer _debounce_ se necessário.
- Pare de consumir o fluxo quando receber um evento `finish`.

### Exemplo de Uso Mínimo (Assíncrono)
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

### Cancelamento
Você pode cancelar a tarefa consumindo o fluxo. O cancelamento é propagado para o processo de tradução subjacente.

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

### Formas de Eventos de Exemplo
Resumo do estágio (exemplo):
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

Progress event (exemplo):
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

Finish event (exemplo):
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

Evento de erro (exemplo):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### Notas e Melhores Práticas
- Sempre trate tanto os eventos de erro quanto as exceções do gerador.
- Interrompa o loop em `finish` para evitar trabalho desnecessário.
- Certifique-se de que o `file` existe e `settings.validate_settings()` passa antes de chamar.
- Documentos grandes podem ser divididos; use `part_index/total_parts` e `overall_progress` para orientar sua interface do usuário.
- Debounce `progress_update` se sua interface do usuário for sensível a atualizações repetidas e idênticas.
- `report_interval` (SettingsModel): controla apenas a taxa de emissão dos eventos `progress_update`. Não afeta `stage_summary`, `progress_start`, `progress_end` ou `finish`. O padrão é 0,1s e o mínimo permitido é 0,05s. Conforme a lógica do monitor de progresso, quando `stage_total <= 3`, as atualizações não são limitadas por `report_interval`.

<div align="right"> 
<h6><small>Parte do conteúdo desta página foi traduzida pelo GPT e pode conter erros.</small></h6>