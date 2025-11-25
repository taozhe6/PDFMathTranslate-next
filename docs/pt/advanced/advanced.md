[**Opções avançadas**](./introduction.md) > **Opções avançadas** _(atual)_

---

<h3 id="toc">Índice</h3>

- [Argumentos da Linha de Comando](#argumentos-da-linha-de-comando)
- [Guia de Configuração de Limitação de Taxa](#guia-de-configuração-de-limitação-de-taxa)
- [Tradução parcial](#tradução-parcial)
- [Especificar idiomas de origem e destino](#especificar-idiomas-de-origem-e-destino)
- [Traduzir com exceções](#traduzir-com-exceções)
- [Prompt personalizado](#prompt-personalizado)
- [Configuração personalizada](#configuração-personalizada)
- [Pular limpeza](#pular-limpeza)
- [Cache de tradução](#cache-de-tradução)
- [Implantação como serviços públicos](#implantação-como-serviços-públicos)
- [Autenticação e página de boas-vindas](#autenticação-e-página-de-boas-vindas)
- [Suporte a Glossário](#suporte-a-glossário)

---

#### Argumentos da Linha de Comando

Execute o comando de tradução na linha de comando para gerar o documento traduzido `example-mono.pdf` e o documento bilíngue `example-dual.pdf` no diretório de trabalho atual. Use o Google como o serviço de tradução padrão. Mais serviços de tradução suportados podem ser encontrados [AQUI](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

Na tabela a seguir, listamos todas as opções avançadas para referência:

##### Argumentos

| `-o`, `--output-dir`            | Specify the output directory                                                           | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `-l`, `--language`              | Specify the target language (default: `zh`)                                            | `pdf2zh_next example.pdf -l en`                                                                                       |
| `-s`, `--service`               | Specify the translation service (default: `google`)                                    | `pdf2zh_next example.pdf -s deepl`                                                                                    |
| `-c`, `--concurrency`           | Specify the number of concurrent translation requests (default: `5`)                   | `pdf2zh_next example.pdf -c 10`                                                                                       |
| `-t`, `--timeout`               | Specify the timeout for each translation request in seconds (default: `30`)             | `pdf2zh_next example.pdf -t 60`                                                                                       |
| `-k`, `--api-key`               | Specify the API key for the translation service                                        | `pdf2zh_next example.pdf -s deepl -k YOUR_DEEPL_API_KEY`                                                              |
| `--no-ocr`                      | Disable OCR for text extraction                                                        | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--ocr-language`                | Specify the language for OCR (default: `eng+chi_sim`)                                  | `pdf2zh_next example.pdf --ocr-language eng`                                                                          |
| `--ocr-dpi`                     | Specify the DPI for OCR (default: `300`)                                               | `pdf2zh_next example.pdf --ocr-dpi 150`                                                                               |
| `--ocr-timeout`                  | Specify the timeout for OCR in seconds (default: `600`)                                | `pdf2zh_next example.pdf --ocr-timeout 300`                                                                           |
| `--font-size`                   | Specify the font size for the output PDF (default: `10.5`)                             | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing`                | Specify the line spacing for the output PDF (default: `1.2`)                           | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--margin`                      | Specify the margin for the output PDF (default: `72`)                                  | `pdf2zh_next example.pdf --margin 50`                                                                                 |
| `--no-translate`                 | Only extract text without translation                                                  | `pdf2zh_next example.pdf --no-translate`                                                                              |
| `--only-translate`               | Only translate without generating PDF                                                  | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--debug`                       | Enable debug mode                                                                      | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Show help message                                                                      | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Show version information                                                               | `pdf2zh_next --version`                                                                                               |

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

| Opção                          | Função                                                                               | Exemplo                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Arquivos PDF de entrada para processar                                                  | `pdf2zh_next example.pdf`                                                                                             |
| `-o`, `--output-dir`            | Especifica o diretório de saída                                                        | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `-l`, `--language`              | Especifica o idioma de destino (padrão: `zh`)                                          | `pdf2zh_next example.pdf -l en`                                                                                       |
| `-s`, `--service`               | Especifica o serviço de tradução (padrão: `google`)                                    | `pdf2zh_next example.pdf -s deepl`                                                                                    |
| `-c`, `--concurrency`           | Especifica o número de solicitações de tradução simultâneas (padrão: `5`)              | `pdf2zh_next example.pdf -c 10`                                                                                       |
| `-t`, `--timeout`               | Especifica o tempo limite para cada solicitação de tradução em segundos (padrão: `30`)  | `pdf2zh_next example.pdf -t 60`                                                                                       |
| `-k`, `--api-key`               | Especifica a chave de API para o serviço de tradução                                    | `pdf2zh_next example.pdf -s deepl -k YOUR_DEEPL_API_KEY`                                                              |
| `--no-ocr`                      | Desativa o OCR para extração de texto                                                   | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--ocr-language`                | Especifica o idioma para OCR (padrão: `eng+chi_sim`)                                    | `pdf2zh_next example.pdf --ocr-language eng`                                                                          |
| `--ocr-dpi`                     | Especifica o DPI para OCR (padrão: `300`)                                              | `pdf2zh_next example.pdf --ocr-dpi 150`                                                                               |
| `--ocr-timeout`                  | Especifica o tempo limite para OCR em segundos (padrão: `600`)                          | `pdf2zh_next example.pdf --ocr-timeout 300`                                                                           |
| `--font-size`                   | Especifica o tamanho da fonte para o PDF de saída (padrão: `10.5`)                      | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing`                | Especifica o espaçamento de linha para o PDF de saída (padrão: `1.2`)                  | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--margin`                      | Especifica a margem para o PDF de saída (padrão: `72`)                                 | `pdf2zh_next example.pdf --margin 50`                                                                                 |
| `--no-translate`                 | Apenas extrai texto sem tradução                                                        | `pdf2zh_next example.pdf --no-translate`                                                                              |
| `--only-translate`               | Apenas traduz sem gerar PDF                                                             | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--debug`                       | Ativa o modo de depuração                                                               | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Mostra a mensagem de ajuda                                                              | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Mostra informações da versão                                                            | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-name`                 | Output filename for single file output                                                  | `pdf2zh_next example.pdf --output-name example_translated.pdf`                                                        |
| `--output-format`               | Output format, `pdf` or `html`                                                          | `pdf2zh_next example.pdf --output-format html`                                                                        |
| `--output-pdf-ocr`              | Enable OCR for output PDF, which improves text selection but may reduce image quality   | `pdf2zh_next example.pdf --output-pdf-ocr`                                                                            |
| `--output-html-embed-image`     | Embed images in the output HTML file instead of saving them as separate files           | `pdf2zh_next example.pdf --output-format html --output-html-embed-image`                                              |
| `--output-html-save-image`      | Save images as separate files in the output directory when generating HTML              | `pdf2zh_next example.pdf --output-format html --output-html-save-image`                                               |
| `--output-html-pretty`          | Enable pretty formatting for the output HTML file                                       | `pdf2zh_next example.pdf --output-format html --output-html-pretty`                                                   |
| `--output-html-pretty-indent`   | Set the indentation for pretty formatting in the output HTML file                       | `pdf2zh_next example.pdf --output-format html --output-html-pretty --output-html-pretty-indent 2`                     |
| `--output-html-pretty-max-width` | Set the maximum line width for pretty formatting in the output HTML file                | `pdf2zh_next example.pdf --output-format html --output-html-pretty --output-html-pretty-max-width 80`                 |
| `--output-pdf-ocr-dpi`          | Set the DPI for OCR in the output PDF. Higher values improve text quality but increase processing time and file size. | `pdf2zh_next example.pdf --output-pdf-ocr --output-pdf-ocr-dpi 300`                                                   |

---

### OUTPUT

| `--output`                      | Diretório de saída para os arquivos                                                     | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-name`                 | Nome do arquivo de saída para saída de arquivo único                                    | `pdf2zh_next example.pdf --output-name example_translated.pdf`                                                        |
| `--output-format`               | Formato de saída, `pdf` ou `html`                                                       | `pdf2zh_next example.pdf --output-format html`                                                                        |
| `--output-pdf-ocr`              | Ativar OCR para o PDF de saída, o que melhora a seleção de texto, mas pode reduzir a qualidade da imagem | `pdf2zh_next example.pdf --output-pdf-ocr`                                                                            |
| `--output-html-embed-image`     | Incorporar imagens no arquivo HTML de saída em vez de salvá-las como arquivos separados | `pdf2zh_next example.pdf --output-format html --output-html-embed-image`                                              |
| `--output-html-save-image`      | Salvar imagens como arquivos separados no diretório de saída ao gerar HTML              | `pdf2zh_next example.pdf --output-format html --output-html-save-image`                                               |
| `--output-html-pretty`          | Ativar formatação bonita para o arquivo HTML de saída                                   | `pdf2zh_next example.pdf --output-format html --output-html-pretty`                                                   |
| `--output-html-pretty-indent`   | Definir a indentação para formatação bonita no arquivo HTML de saída                    | `pdf2zh_next example.pdf --output-format html --output-html-pretty --output-html-pretty-indent 2`                     |
| `--output-html-pretty-max-width` | Definir a largura máxima da linha para formatação bonita no arquivo HTML de saída       | `pdf2zh_next example.pdf --output-format html --output-html-pretty --output-html-pretty-max-width 80`                 |
| `--output-pdf-ocr-dpi`          | Definir o DPI para OCR no PDF de saída. Valores mais altos melhoram a qualidade do texto, mas aumentam o tempo de processamento e o tamanho do arquivo. | `pdf2zh_next example.pdf --output-pdf-ocr --output-pdf-ocr-dpi 300`                                                   |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Language Code>`             | Specify the target [**language code**](./Supported-Languages.md)                       | `pdf2zh_next example.pdf --lang en`<br>`pdf2zh_next example.pdf --lang ru`                                            |
| `--<Advanced>`                  | Enable **advanced** options                                                            | `pdf2zh_next example.pdf --advanced`                                                                                  |
| `--<Community>`                 | Enable **community** features                                                          | `pdf2zh_next example.pdf --community`                                                                                 |
| `--faq`                         | Show **FAQ** page                                                                      | `pdf2zh_next --faq`                                                                                                   |
| `--for-translators`             | Show **translator guide** page                                                         | `pdf2zh_next --for-translators`                                                                                       |

---

### OUTPUT

| `--<Services>`                  | Usar [**serviço específico**](./Documentation-of-Translation-Services.md) para tradução | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Language Code>`             | Especificar o [**código do idioma**](./Supported-Languages.md) de destino              | `pdf2zh_next example.pdf --lang en`<br>`pdf2zh_next example.pdf --lang ru`                                            |
| `--<Advanced>`                  | Ativar opções **avançadas**                                                            | `pdf2zh_next example.pdf --advanced`                                                                                  |
| `--<Community>`                 | Ativar recursos da **comunidade**                                                      | `pdf2zh_next example.pdf --community`                                                                                 |
| `--faq`                         | Mostrar página de **perguntas frequentes**                                             | `pdf2zh_next --faq`                                                                                                   |
| `--for-translators`             | Mostrar página do **guia de contribuição para traduções**                              | `pdf2zh_next --for-translators`                                                                                       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               |
| `--input <file>`, `-i <file>`   | Input PDF file (required)                                                               | `pdf2zh_next --input example.pdf`                                                                                     |
| `--output <file>`, `-o <file>`  | Output file (default: input file name with `_translated.pdf` suffix)                    | `pdf2zh_next --input example.pdf --output example_translated.pdf`                                                      |
| `--engine <engine>`             | Translation engine (default: `google`)                                                  | `pdf2zh_next --input example.pdf --engine google`                                                                     |
| `--source <language>`           | Source language code (default: `en`)                                                    | `pdf2zh_next --input example.pdf --source en`                                                                         |
| `--target <language>`           | Target language code (default: `zh-CN`)                                                 | `pdf2zh_next --input example.pdf --target zh-CN`                                                                      |
| `--format <format>`             | Output format: `pdf` (default) or `docx`                                                | `pdf2zh_next --input example.pdf --format docx`                                                                       |
| `--openai-api-key <key>`        | OpenAI API key (required for `openai` engine)                                           | `pdf2zh_next --input example.pdf --engine openai --openai-api-key sk-...`                                             |
| `--openai-base-url <url>`       | OpenAI API base URL (optional for `openai` engine)                                      | `pdf2zh_next --input example.pdf --engine openai --openai-api-key sk-... --openai-base-url https://api.openai.com/v1/`|
| `--openai-model <model>`        | OpenAI model (default: `gpt-3.5-turbo`)                                                 | `pdf2zh_next --input example.pdf --engine openai --openai-api-key sk-... --openai-model gpt-4`                        |
| `--concurrency <number>`        | Number of concurrent translation tasks (default: `4`)                                   | `pdf2zh_next --input example.pdf --concurrency 8`                                                                     |
| `--mathpix-app-id <id>`         | Mathpix App ID (required for `mathpix` engine)                                          | `pdf2zh_next --input example.pdf --engine mathpix --mathpix-app-id your_app_id`                                       |
| `--mathpix-app-key <key>`       | Mathpix App Key (required for `mathpix` engine)                                         | `pdf2zh_next --input example.pdf --engine mathpix --mathpix-app-key your_app_key`                                     |
| `--mathpix-ocr <ocr>`           | Mathpix OCR preference: `math` (default) or `text`                                      | `pdf2zh_next --input example.pdf --engine mathpix --mathpix-app-id id --mathpix-app-key key --mathpix-ocr text`       |
| `--retry <number>`              | Number of retries for failed translations (default: `3`)                                | `pdf2zh_next --input example.pdf --retry 5`                                                                           |
| `--timeout <seconds>`           | Timeout for each translation request in seconds (default: `30`)                         | `pdf2zh_next --input example.pdf --timeout 60`                                                                        |
| `--no-cache`                    | Disable caching of translation results                                                  | `pdf2zh_next --input example.pdf --no-cache`                                                                          |
| `--cache-dir <dir>`             | Directory to store cache files (default: system cache directory)                        | `pdf2zh_next --input example.pdf --cache-dir ./cache`                                                                 |
| `--log-level <level>`           | Log level: `DEBUG`, `INFO` (default), `WARNING`, `ERROR`, `CRITICAL`                    | `pdf2zh_next --input example.pdf --log-level DEBUG`                                                                   |
| `--config <file>`               | Load configuration from a JSON file                                                     | `pdf2zh_next --input example.pdf --config config.json`                                                                |

---

### OUTPUT

| `--help`, `-h`                  | Mostrar mensagem de ajuda e sair                                                              | `pdf2zh_next -h`                                                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--version`, `-v`               | Mostrar versão e sair                                                                   | `pdf2zh_next --version`                                                                                               |
| `--input <file>`, `-i <file>`   | Arquivo PDF de entrada (obrigatório)                                                               | `pdf2zh_next --input example.pdf`                                                                                     |
| `--output <file>`, `-o <file>`  | Arquivo de saída (padrão: nome do arquivo de entrada com sufixo `_translated.pdf`)                    | `pdf2zh_next --input example.pdf --output example_translated.pdf`                                                      |
| `--engine <engine>`             | Motor de tradução (padrão: `google`)                                                  | `pdf2zh_next --input example.pdf --engine google`                                                                     |
| `--source <language>`           | Código do idioma de origem (padrão: `en`)                                                    | `pdf2zh_next --input example.pdf --source en`                                                                         |
| `--target <language>`           | Código do idioma de destino (padrão: `zh-CN`)                                                 | `pdf2zh_next --input example.pdf --target zh-CN`                                                                      |
| `--format <format>`             | Formato de saída: `pdf` (padrão) ou `docx`                                                | `pdf2zh_next --input example.pdf --format docx`                                                                       |
| `--openai-api-key <key>`        | Chave da API da OpenAI (obrigatório para o motor `openai`)                                           | `pdf2zh_next --input example.pdf --engine openai --openai-api-key sk-...`                                             |
| `--openai-base-url <url>`       | URL base da API da OpenAI (opcional para o motor `openai`)                                      | `pdf2zh_next --input example.pdf --engine openai --openai-api-key sk-... --openai-base-url https://api.openai.com/v1/`|
| `--openai-model <model>`        | Modelo da OpenAI (padrão: `gpt-3.5-turbo`)                                                 | `pdf2zh_next --input example.pdf --engine openai --openai-api-key sk-... --openai-model gpt-4`                        |
| `--concurrency <number>`        | Número de tarefas de tradução concorrentes (padrão: `4`)                                   | `pdf2zh_next --input example.pdf --concurrency 8`                                                                     |
| `--mathpix-app-id <id>`         | ID do aplicativo Mathpix (obrigatório para o motor `mathpix`)                                          | `pdf2zh_next --input example.pdf --engine mathpix --mathpix-app-id your_app_id`                                       |
| `--mathpix-app-key <key>`       | Chave do aplicativo Mathpix (obrigatório para o motor `mathpix`)                                         | `pdf2zh_next --input example.pdf --engine mathpix --mathpix-app-key your_app_key`                                     |
| `--mathpix-ocr <ocr>`           | Preferência de OCR do Mathpix: `math` (padrão) ou `text`                                      | `pdf2zh_next --input example.pdf --engine mathpix --mathpix-app-id id --mathpix-app-key key --mathpix-ocr text`       |
| `--retry <number>`              | Número de tentativas para traduções com falha (padrão: `3`)                                | `pdf2zh_next --input example.pdf --retry 5`                                                                           |
| `--timeout <seconds>`           | Tempo limite para cada solicitação de tradução em segundos (padrão: `30`)                         | `pdf2zh_next --input example.pdf --timeout 60`                                                                        |
| `--no-cache`                    | Desativar cache dos resultados da tradução                                                  | `pdf2zh_next --input example.pdf --no-cache`                                                                          |
| `--cache-dir <dir>`             | Diretório para armazenar arquivos de cache (padrão: diretório de cache do sistema)                        | `pdf2zh_next --input example.pdf --cache-dir ./cache`                                                                 |
| `--log-level <level>`           | Nível de log: `DEBUG`, `INFO` (padrão), `WARNING`, `ERROR`, `CRITICAL`                    | `pdf2zh_next --input example.pdf --log-level DEBUG`                                                                   |
| `--config <file>`               | Carregar configuração de um arquivo JSON                                                     | `pdf2zh_next --input example.pdf --config config.json`                                                                |
No       |


---

### OUTPUT

| `--config-file`                 | Caminho para o arquivo de configuração                                                  | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | Não       |
`1`       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|
| `--max-file-size`               | Maximum file size (in MB) for translation                                               | `pdf2zh_next example.pdf --max-file-size 10`                                                                          | `10`      |
| `--max-pages`                   | Maximum number of pages to translate                                                    | `pdf2zh_next example.pdf --max-pages 5`                                                                              | `100`     |
| `--ignore-images`               | Do not process images                                                                   | `pdf2zh_next example.pdf --ignore-images`                                                                            | `false`   |
| `--ignore-equations`            | Do not process equations                                                                | `pdf2zh_next example.pdf --ignore-equations`                                                                          | `false`   |
| `--ignore-tables`               | Do not process tables                                                                   | `pdf2zh_next example.pdf --ignore-tables`                                                                             | `false`   |
| `--ignore-code-blocks`          | Do not process code blocks                                                              | `pdf2zh_next example.pdf --ignore-code-blocks`                                                                       | `false`   |
| `--ignore-text-outside-body`    | Do not translate text outside the body of the document (e.g., headers, footers, etc.)   | `pdf2zh_next example.pdf --ignore-text-outside-body`                                                                 | `false`   |
| `--ignore-figure-captions`      | Do not translate figure captions                                                        | `pdf2zh_next example.pdf --ignore-figure-captions`                                                                    | `false`   |
| `--ignore-table-captions`       | Do not translate table captions                                                        | `pdf2zh_next example.pdf --ignore-table-captions`                                                                     | `false`   |
| `--ignore-abstract`             | Do not translate abstract section                                                      | `pdf2zh_next example.pdf --ignore-abstract`                                                                           | `false`   |
| `--ignore-references`           | Do not translate references section                                                    | `pdf2zh_next example.pdf --ignore-references`                                                                         | `false`   |
| `--ignore-footnotes`            | Do not translate footnotes                                                              | `pdf2zh_next example.pdf --ignore-footnotes`                                                                          | `false`   |
| `--ignore-appendix`             | Do not translate appendix section                                                       | `pdf2zh_next example.pdf --ignore-appendix`                                                                           | `false`   |
| `--ignore-document-metadata`    | Do not translate document metadata (e.g., title, author, etc.)                         | `pdf2zh_next example.pdf --ignore-document-metadata`                                                                  | `false`   |
| `--ignore-document-properties`  | Do not translate document properties (e.g., subject, keywords, etc.)                    | `pdf2zh_next example.pdf --ignore-document-properties`                                                                | `false`   |
| `--ignore-watermarks`           | Do not translate watermarks                                                             | `pdf2zh_next example.pdf --ignore-watermarks`                                                                         | `false`   |
| `--ignore-annotations`          | Do not translate annotations (e.g., comments, highlights, etc.)                        | `pdf2zh_next example.pdf --ignore-annotations`                                                                        | `false`   |

---

### OUTPUT

| `--report-interval`             | Intervalo do relatório de progresso em segundos                                        | `pdf2zh_next exemplo.pdf --report-interval 5`                                                                        | `1`       |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------|
| `--max-file-size`               | Tamanho máximo do arquivo (em MB) para tradução                                         | `pdf2zh_next exemplo.pdf --max-file-size 10`                                                                         | `10`      |
| `--max-pages`                   | Número máximo de páginas para traduzir                                                  | `pdf2zh_next exemplo.pdf --max-pages 5`                                                                               | `100`     |
| `--ignore-images`               | Não processar imagens                                                                   | `pdf2zh_next exemplo.pdf --ignore-images`                                                                            | `false`   |
| `--ignore-equations`            | Não processar equações                                                                  | `pdf2zh_next exemplo.pdf --ignore-equations`                                                                          | `false`   |
| `--ignore-tables`               | Não processar tabelas                                                                    | `pdf2zh_next exemplo.pdf --ignore-tables`                                                                             | `false`   |
| `--ignore-code-blocks`          | Não processar blocos de código                                                          | `pdf2zh_next exemplo.pdf --ignore-code-blocks`                                                                       | `false`   |
| `--ignore-text-outside-body`    | Não traduzir texto fora do corpo do documento (por exemplo, cabeçalhos, rodapés, etc.)   | `pdf2zh_next exemplo.pdf --ignore-text-outside-body`                                                                 | `false`   |
| `--ignore-figure-captions`      | Não traduzir legendas de figuras                                                        | `pdf2zh_next exemplo.pdf --ignore-figure-captions`                                                                    | `false`   |
| `--ignore-table-captions`       | Não traduzir legendas de tabelas                                                        | `pdf2zh_next exemplo.pdf --ignore-table-captions`                                                                     | `false`   |
| `--ignore-abstract`             | Não traduzir seção de resumo                                                            | `pdf2zh_next exemplo.pdf --ignore-abstract`                                                                           | `false`   |
| `--ignore-references`           | Não traduzir seção de referências                                                       | `pdf2zh_next exemplo.pdf --ignore-references`                                                                         | `false`   |
| `--ignore-footnotes`            | Não traduzir notas de rodapé                                                            | `pdf2zh_next exemplo.pdf --ignore-footnotes`                                                                          | `false`   |
| `--ignore-appendix`             | Não traduzir seção de apêndice                                                           | `pdf2zh_next exemplo.pdf --ignore-appendix`                                                                           | `false`   |
| `--ignore-document-metadata`    | Não traduzir metadados do documento (por exemplo, título, autor, etc.)                  | `pdf2zh_next exemplo.pdf --ignore-document-metadata`                                                                  | `false`   |
| `--ignore-document-properties`  | Não traduzir propriedades do documento (por exemplo, assunto, palavras-chave, etc.)    | `pdf2zh_next exemplo.pdf --ignore-document-properties`                                                                | `false`   |
| `--ignore-watermarks`           | Não traduzir marcas d'água                                                               | `pdf2zh_next exemplo.pdf --ignore-watermarks`                                                                         | `false`   |
| `--ignore-annotations`          | Não traduzir anotações (por exemplo, comentários, destaques, etc.)                      | `pdf2zh_next exemplo.pdf --ignore-annotations`                                                                        | `false`   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next example.pdf -h`                                                                                          |
| `--log-level`                   | Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)                               | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--log-path`                    | Set the log file path, default is `pdf2zh_next.log`                                     | `pdf2zh_next example.pdf --log-path my_log.log`                                                                       |
| `--log-format`                  | Set the log format, default is `%(asctime)s - %(name)s - %(levelname)s - %(message)s`   | `pdf2zh_next example.pdf --log-format "%(asctime)s - %(message)s"`                                                     |
| `--log-encoding`                | Set the log file encoding, default is `utf-8`                                           | `pdf2zh_next example.pdf --log-encoding gbk`                                                                          |

---

### TRANSLATED TEXT

| `--debug`                       | Usar nível de logging de depuração                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Mostrar mensagem de ajuda e sair                                                              | `pdf2zh_next example.pdf -h`                                                                                          |
| `--log-level`                   | Definir o nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)                               | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--log-path`                    | Definir o caminho do arquivo de log, padrão é `pdf2zh_next.log`                                     | `pdf2zh_next example.pdf --log-path my_log.log`                                                                       |
| `--log-format`                  | Definir o formato do log, padrão é `%(asctime)s - %(name)s - %(levelname)s - %(message)s`   | `pdf2zh_next example.pdf --log-format "%(asctime)s - %(message)s"`                                                     |
| `--log-encoding`                | Definir a codificação do arquivo de log, padrão é `utf-8`                                           | `pdf2zh_next example.pdf --log-encoding gbk`                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--input`                       | Specify the input file (can be a file or a folder)                                      | `pdf2zh_next --input ./paper.pdf`                                                                                     |
| `--output`                      | Specify the output path                                                                 | `pdf2zh_next --input ./paper.pdf --output ./paper_zh.pdf`                                                             |
| `--target_language`             | Specify the target language (default: zh)                                               | `pdf2zh_next --input ./paper.pdf --target_language ja`                                                                |
| `--model`                       | Specify the model to use (default: gpt-4o)                                              | `pdf2zh_next --input ./paper.pdf --model gpt-4o-mini`                                                                 |
| `--translation_service`         | Specify the translation service to use (default: openai)                                | `pdf2zh_next --input ./paper.pdf --translation_service azure_openai`                                                  |
| `--api_key`                     | Specify the API key (if not set, will use the environment variable)                     | `pdf2zh_next --input ./paper.pdf --api_key sk-xxx`                                                                    |
| `--max_concurrency`             | Specify the maximum number of concurrent requests (default: 3)                          | `pdf2zh_next --input ./paper.pdf --max_concurrency 5`                                                                 |
| `--max_requests_per_minute`     | Specify the maximum number of requests per minute (default: 50)                         | `pdf2zh_next --input ./paper.pdf --max_requests_per_minute 100`                                                       |
| `--retry_times`                 | Specify the number of times to retry if a request fails (default: 3)                    | `pdf2zh_next --input ./paper.pdf --retry_times 5`                                                                     |
| `--timeout`                     | Specify the timeout for each request in seconds (default: 60)                           | `pdf2zh_next --input ./paper.pdf --timeout 120`                                                                       |
| `--check_only`                  | Only check the translation, do not translate                                            | `pdf2zh_next --input ./paper.pdf --check_only`                                                                        |
| `--resume`                      | Resume from the last interrupted translation                                            | `pdf2zh_next --input ./paper.pdf --resume`                                                                            |
| `--force`                       | Force to translate even if the output file already exists                               | `pdf2zh_next --input ./paper.pdf --output ./paper_zh.pdf --force`                                                     |
| `--version`                     | Show the version of the program                                                         | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show the help message                                                                   | `pdf2zh_next --help`                                                                                                  |
| `--log_level`                   | Specify the log level (default: INFO)                                                   | `pdf2zh_next --input ./paper.pdf --log_level DEBUG`                                                                   |
| `--no_color`                    | Disable color output                                                                    | `pdf2zh_next --input ./paper.pdf --no_color`                                                                          |
| `--proxy`                       | Specify the proxy to use (e.g., http://127.0.0.1:7890)                                  | `pdf2zh_next --input ./paper.pdf --proxy http://127.0.0.1:7890`                                                       |
| `--model_list`                  | List all available models for the specified translation service                         | `pdf2zh_next --model_list --translation_service openai`                                                               |
| `--dry_run`                     | Dry run, only show the translation plan without actually translating                    | `pdf2zh_next --input ./paper.pdf --dry_run`                                                                           |
| `--page_range`                  | Specify the page range to translate (e.g., 1-5,10,12-15)                                | `pdf2zh_next --input ./paper.pdf --page_range 1-5,10,12-15`                                                           |
| `--custom_prompt`               | Specify a custom prompt for translation                                                 | `pdf2zh_next --input ./paper.pdf --custom_prompt "Translate the following content to Chinese"`                        |
| `--glossary`                    | Specify a glossary file to use for translation                                          | `pdf2zh_next --input ./paper.pdf --glossary ./glossary.txt`                                                           |
| `--output_format`               | Specify the output format (default: pdf, options: pdf, markdown, text)                  | `pdf2zh_next --input ./paper.pdf --output_format markdown`                                                            |
| `--remove_original_text`        | Remove the original text from the output                                                | `pdf2zh_next --input ./paper.pdf --remove_original_text`                                                              |
| `--layout`                      | Specify the layout of the output (default: original, options: original, bilingual)      | `pdf2zh_next --input ./paper.pdf --layout bilingual`                                                                  |
| `--font`                        | Specify the font to use for the output (default: Noto Sans SC)                          | `pdf2zh_next --input ./paper.pdf --font "Source Han Serif SC"`                                                        |
| `--font_size`                   | Specify the font size for the output (default: 12)                                      | `pdf2zh_next --input ./paper.pdf --font_size 14`                                                                      |
| `--line_spacing`                | Specify the line spacing for the output (default: 1.2)                                  | `pdf2zh_next --input ./paper.pdf --line_spacing 1.5`                                                                  |
| `--margin`                      | Specify the margin for the output (default: 72)                                         | `pdf2zh_next --input ./paper.pdf --margin 100`                                                                        |
| `--page_size`                   | Specify the page size for the output (default: A4, options: A4, Letter, Legal, A3, A5)  | `pdf2zh_next --input ./paper.pdf --page_size Letter`                                                                  |
| `--page_orientation`            | Specify the page orientation for the output (default: portrait, options: portrait, landscape) | `pdf2zh_next --input ./paper.pdf --page_orientation landscape`                                                    |
| `--title`                       | Specify the title for the output document                                               | `pdf2zh_next --input ./paper.pdf --title "Translated Paper"`                                                          |
| `--author`                      | Specify the author for the output document                                              | `pdf2zh_next --input ./paper.pdf --author "John Doe"`                                                                 |
| `--subject`                     | Specify the subject for the output document                                             | `pdf2zh_next --input ./paper.pdf --subject "Computer Science"`                                                        |
| `--keywords`                    | Specify the keywords for the output document                                            | `pdf2zh_next --input ./paper.pdf --keywords "translation, pdf, ai"`                                                   |
| `--no_cover`                    | Do not generate a cover page for the output document                                    | `pdf2zh_next --input ./paper.pdf --no_cover`                                                                          |
| `--no_toc`                      | Do not generate a table of contents for the output document                             | `pdf2zh_next --input ./paper.pdf --no_toc`                                                                            |
| `--toc_depth`                   | Specify the depth of the table of contents (default: 3)                                 | `pdf2zh_next --input ./paper.pdf --toc_depth 2`                                                                       |
| `--watermark`                   | Specify a watermark text for the output document                                        | `pdf2zh_next --input ./paper.pdf --watermark "DRAFT"`                                                                 |
| `--watermark_opacity`           | Specify the opacity of the watermark (default: 0.2)                                     | `pdf2zh_next --input ./paper.pdf --watermark_opacity 0.1`                                                             |
| `--config`                      | Specify a config file to use                                                            | `pdf2zh_next --config ./config.yaml`                                                                                  |
| `--save_config`                 | Save the current configuration to a file                                                | `pdf2zh_next --input ./paper.pdf --save_config ./config.yaml`                                                         |

---

### OUTPUT

| `--gui`                         | Interagir com a GUI                                                                     | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--input`                       | Especificar o arquivo de entrada (pode ser um arquivo ou uma pasta)                     | `pdf2zh_next --input ./paper.pdf`                                                                                     |
| `--output`                      | Especificar o caminho de saída                                                          | `pdf2zh_next --input ./paper.pdf --output ./paper_zh.pdf`                                                             |
| `--target_language`             | Especificar o idioma de destino (padrão: zh)                                            | `pdf2zh_next --input ./paper.pdf --target_language ja`                                                                |
| `--model`                       | Especificar o modelo a ser usado (padrão: gpt-4o)                                       | `pdf2zh_next --input ./paper.pdf --model gpt-4o-mini`                                                                 |
| `--translation_service`         | Especificar o serviço de tradução a ser usado (padrão: openai)                          | `pdf2zh_next --input ./paper.pdf --translation_service azure_openai`                                                  |
| `--api_key`                     | Especificar a chave da API (se não definida, usará a variável de ambiente)              | `pdf2zh_next --input ./paper.pdf --api_key sk-xxx`                                                                    |
| `--max_concurrency`             | Especificar o número máximo de solicitações simultâneas (padrão: 3)                     | `pdf2zh_next --input ./paper.pdf --max_concurrency 5`                                                                 |
| `--max_requests_per_minute`     | Especificar o número máximo de solicitações por minuto (padrão: 50)                     | `pdf2zh_next --input ./paper.pdf --max_requests_per_minute 100`                                                       |
| `--retry_times`                 | Especificar o número de tentativas se uma solicitação falhar (padrão: 3)                | `pdf2zh_next --input ./paper.pdf --retry_times 5`                                                                     |
| `--timeout`                     | Especificar o tempo limite para cada solicitação em segundos (padrão: 60)               | `pdf2zh_next --input ./paper.pdf --timeout 120`                                                                       |
| `--check_only`                  | Apenas verificar a tradução, não traduzir                                               | `pdf2zh_next --input ./paper.pdf --check_only`                                                                        |
| `--resume`                      | Retomar a partir da última tradução interrompida                                        | `pdf2zh_next --input ./paper.pdf --resume`                                                                            |
| `--force`                       | Forçar a tradução mesmo se o arquivo de saída já existir                                | `pdf2zh_next --input ./paper.pdf --output ./paper_zh.pdf --force`                                                     |
| `--version`                     | Mostrar a versão do programa                                                            | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Mostrar a mensagem de ajuda                                                             | `pdf2zh_next --help`                                                                                                  |
| `--log_level`                   | Especificar o nível de log (padrão: INFO)                                               | `pdf2zh_next --input ./paper.pdf --log_level DEBUG`                                                                   |
| `--no_color`                    | Desativar a saída colorida                                                              | `pdf2zh_next --input ./paper.pdf --no_color`                                                                          |
| `--proxy`                       | Especificar o proxy a ser usado (por exemplo, http://127.0.0.1:7890)                    | `pdf2zh_next --input ./paper.pdf --proxy http://127.0.0.1:7890`                                                       |
| `--model_list`                  | Listar todos os modelos disponíveis para o serviço de tradução especificado             | `pdf2zh_next --model_list --translation_service openai`                                                               |
| `--dry_run`                     | Execução seca, apenas mostrar o plano de tradução sem realmente traduzir                | `pdf2zh_next --input ./paper.pdf --dry_run`                                                                           |
| `--page_range`                  | Especificar o intervalo de páginas para traduzir (por exemplo, 1-5,10,12-15)            | `pdf2zh_next --input ./paper.pdf --page_range 1-5,10,12-15`                                                           |
| `--custom_prompt`               | Especificar um prompt personalizado para tradução                                       | `pdf2zh_next --input ./paper.pdf --custom_prompt "Translate the following content to Chinese"`                        |
| `--glossary`                    | Especificar um arquivo de glossário para usar na tradução                               | `pdf2zh_next --input ./paper.pdf --glossary ./glossary.txt`                                                           |
| `--output_format`               | Especificar o formato de saída (padrão: pdf, opções: pdf, markdown, text)               | `pdf2zh_next --input ./paper.pdf --output_format markdown`                                                            |
| `--remove_original_text`        | Remover o texto original da saída                                                       | `pdf2zh_next --input ./paper.pdf --remove_original_text`                                                              |
| `--layout`                      | Especificar o layout da saída (padrão: original, opções: original, bilingual)           | `pdf2zh_next --input ./paper.pdf --layout bilingual`                                                                  |
| `--font`                        | Especificar a fonte a ser usada na saída (padrão: Noto Sans SC)                         | `pdf2zh_next --input ./paper.pdf --font "Source Han Serif SC"`                                                        |
| `--font_size`                   | Especificar o tamanho da fonte para a saída (padrão: 12)                                | `pdf2zh_next --input ./paper.pdf --font_size 14`                                                                      |
| `--line_spacing`                | Especificar o espaçamento entre linhas para a saída (padrão: 1.2)                       | `pdf2zh_next --input ./paper.pdf --line_spacing 1.5`                                                                  |
| `--margin`                      | Especificar a margem para a saída (padrão: 72)                                          | `pdf2zh_next --input ./paper.pdf --margin 100`                                                                        |
| `--page_size`                   | Especificar o tamanho da página para a saída (padrão: A4, opções: A4, Letter, Legal, A3, A5) | `pdf2zh_next --input ./paper.pdf --page_size Letter`                                                              |
| `--page_orientation`            | Especificar a orientação da página para a saída (padrão: retrato, opções: retrato, paisagem) | `pdf2zh_next --input ./paper.pdf --page_orientation landscape`                                                     |
| `--title`                       | Especificar o título para o documento de saída                                          | `pdf2zh_next --input ./paper.pdf --title "Translated Paper"`                                                          |
| `--author`                      | Especificar o autor para o documento de saída                                           | `pdf2zh_next --input ./paper.pdf --author "John Doe"`                                                                 |
| `--subject`                     | Especificar o assunto para o documento de saída                                         | `pdf2zh_next --input ./paper.pdf --subject "Computer Science"`                                                        |
| `--keywords`                    | Especificar as palavras-chave para o documento de saída                                 | `pdf2zh_next --input ./paper.pdf --keywords "translation, pdf, ai"`                                                   |
| `--no_cover`                    | Não gerar uma página de capa para o documento de saída                                  | `pdf2zh_next --input ./paper.pdf --no_cover`                                                                          |
| `--no_toc`                      | Não gerar um índice para o documento de saída                                           | `pdf2zh_next --input ./paper.pdf --no_toc`                                                                            |
| `--toc_depth`                   | Especificar a profundidade do índice (padrão: 3)                                        | `pdf2zh_next --input ./paper.pdf --toc_depth 2`                                                                       |
| `--watermark`                   | Especificar um texto de marca d'água para o documento de saída                          | `pdf2zh_next --input ./paper.pdf --watermark "DRAFT"`                                                                 |
| `--watermark_opacity`           | Especificar a opacidade da marca d'água (padrão: 0.2)                                   | `pdf2zh_next --input ./paper.pdf --watermark_opacity 0.1`                                                             |
| `--config`                      | Especificar um arquivo de configuração para usar                                        | `pdf2zh_next --config ./config.yaml`                                                                                  |
| `--save_config`                 | Salvar a configuração atual em um arquivo                                               | `pdf2zh_next --input ./paper.pdf --save_config ./config.yaml`                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-warmup`                   | Skip the warmup process                                                                 | `pdf2zh_next example.pdf --no-warmup`                                                                                 |
| `--model <model_name>`          | Specify the model name for translation, default is `gpt-3.5-turbo`                      | `pdf2zh_next example.pdf --model gpt-4-turbo`                                                                         |
| `--target-lang <language_code>` | Specify the target language code, default is `zh` (Chinese), see [Supported Languages] | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--output <output_file_path>`   | Specify the output file path                                                            | `pdf2zh_next example.pdf --output example_zh.pdf`                                                                     |
| `--proxy <proxy_url>`           | Specify a proxy URL for the request                                                     | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--api-key <your_api_key>`      | Specify your OpenAI API key                                                             | `pdf2zh_next example.pdf --api-key sk-...`                                                                            |
| `--api-base <your_api_base>`    | Specify your OpenAI API base URL                                                        | `pdf2zh_next example.pdf --api-base https://api.example.com`                                                           |
| `--debug`                       | Enable debug mode, which will generate more detailed logs and intermediate files        | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATED TEXT

| `--warmup`                      | Apenas baixa e verifica os ativos necessários e depois sai                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-warmup`                   | Ignora o processo de warmup                                                                 | `pdf2zh_next example.pdf --no-warmup`                                                                                 |
| `--model <model_name>`          | Especifica o nome do modelo para tradução, o padrão é `gpt-3.5-turbo`                      | `pdf2zh_next example.pdf --model gpt-4-turbo`                                                                         |
| `--target-lang <language_code>` | Especifica o código do idioma de destino, o padrão é `zh` (Chinês), veja [Idiomas suportados] | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--output <output_file_path>`   | Especifica o caminho do arquivo de saída                                                            | `pdf2zh_next example.pdf --output example_zh.pdf`                                                                     |
| `--proxy <proxy_url>`           | Especifica uma URL de proxy para a requisição                                                     | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--api-key <your_api_key>`      | Especifica sua chave de API da OpenAI                                                             | `pdf2zh_next example.pdf --api-key sk-...`                                                                            |
| `--api-base <your_api_base>`    | Especifica sua URL base da API da OpenAI                                                        | `pdf2zh_next example.pdf --api-base https://api.example.com`                                                           |
| `--debug`                       | Ativa o modo de depuração, que irá gerar logs mais detalhados e arquivos intermediários        | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Mostra a mensagem de ajuda e sai                                                              | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets`              | Use offline assets from the specified directory                                          | `pdf2zh_next example.pdf --offline-assets /path`                                                                      |
| `--model-type`                  | Specify the model type, default is `"openai"`                                            | `pdf2zh_next example.pdf --model-type "openai"`                                                                       |
| `--model-name`                  | Specify the model name, default is `"gpt-4o"`                                            | `pdf2zh_next example.pdf --model-name "gpt-4o"`                                                                       |
| `--model-endpoint`              | Specify the model endpoint, default is `"https://api.openai.com/v1/chat/completions"`    | `pdf2zh_next example.pdf --model-endpoint "https://api.openai.com/v1/chat/completions"`                               |

---

### OUTPUT

| `--generate-offline-assets`     | Gerar pacote de recursos offline no diretório especificado                               | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets`              | Usar recursos offline do diretório especificado                                          | `pdf2zh_next example.pdf --offline-assets /path`                                                                      |
| `--model-type`                  | Especificar o tipo de modelo, padrão é `"openai"`                                        | `pdf2zh_next example.pdf --model-type "openai"`                                                                       |
| `--model-name`                  | Especificar o nome do modelo, padrão é `"gpt-4o"`                                        | `pdf2zh_next example.pdf --model-name "gpt-4o"`                                                                       |
| `--model-endpoint`              | Especificar o endpoint do modelo, padrão é `"https://api.openai.com/v1/chat/completions"`| `pdf2zh_next example.pdf --model-endpoint "https://api.openai.com/v1/chat/completions"`                               |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-dir`          | Directory for storing offline assets                                                     | `pdf2zh_next example.pdf --offline-assets-dir /path`                                                                   |
| `--offline-assets-package-name` | Package name for downloading offline assets (e.g., `zh-en`, `en-zh`)                     | `pdf2zh_next example.pdf --offline-assets-package-name zh-en`                                                          |
| `--offline-assets-package-url`  | Package URL for downloading offline assets (e.g., `https://example.com/zh-en.zip`)       | `pdf2zh_next example.pdf --offline-assets-package-url https://example.com/zh-en.zip`                                   |
| `--offline-assets-package-md5`  | MD5 hash of the offline assets package for integrity verification                        | `pdf2zh_next example.pdf --offline-assets-package-md5 5d41402abc4b2a76b9719d911017c592`                                |
| `--offline-assets-package-size` | Size of the offline assets package in bytes for integrity verification                   | `pdf2zh_next example.pdf --offline-assets-package-size 10240000`                                                       |
| `--offline-assets-package-download-timeout` | Timeout for downloading the offline assets package in seconds (default: 300)       | `pdf2zh_next example.pdf --offline-assets-package-download-timeout 600`                                                |

---

### OUTPUT

| `--restore-offline-assets`      | Restaurar o pacote de ativos offline do diretório especificado                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--offline-assets-dir`          | Diretório para armazenar ativos offline                                                     | `pdf2zh_next example.pdf --offline-assets-dir /path`                                                                   |
| `--offline-assets-package-name` | Nome do pacote para baixar ativos offline (por exemplo, `zh-en`, `en-zh`)                     | `pdf2zh_next example.pdf --offline-assets-package-name zh-en`                                                          |
| `--offline-assets-package-url`  | URL do pacote para baixar ativos offline (por exemplo, `https://example.com/zh-en.zip`)       | `pdf2zh_next example.pdf --offline-assets-package-url https://example.com/zh-en.zip`                                   |
| `--offline-assets-package-md5`  | Hash MD5 do pacote de ativos offline para verificação de integridade                        | `pdf2zh_next example.pdf --offline-assets-package-md5 5d41402abc4b2a76b9719d911017c592`                                |
| `--offline-assets-package-size` | Tamanho do pacote de ativos offline em bytes para verificação de integridade                   | `pdf2zh_next example.pdf --offline-assets-package-size 10240000`                                                       |
| `--offline-assets-package-download-timeout` | Tempo limite para baixar o pacote de ativos offline em segundos (padrão: 300)       | `pdf2zh_next example.pdf --offline-assets-package-download-timeout 600`                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Show help message then exit                                                              | `pdf2zh_next -h`                                                                                                      |
| `-v`, `--verbose`               | Set log level to verbose                                                                 | `pdf2zh_next -v`                                                                                                      |
| `-vv`, `--very-verbose`         | Set log level to very verbose                                                            | `pdf2zh_next -vv`                                                                                                     |
| `-q`, `--quiet`                 | Set log level to quiet                                                                   | `pdf2zh_next -q`                                                                                                      |
| `-i`, `--input`                 | Input file or directory                                                                  | `pdf2zh_next -i file.pdf` <br> `pdf2zh_next -i ./input_dir`                                                           |
| `-o`, `--output`                | Output file or directory                                                                 | `pdf2zh_next -i file.pdf -o file_translated.pdf` <br> `pdf2zh_next -i ./input_dir -o ./output_dir`                    |
| `-l`, `--lang`                  | Target language code (default: `zh-CN`)                                                  | `pdf2zh_next -i file.pdf -l en`                                                                                       |
| `-m`, `--model`                 | Translation model (default: `gpt-3.5-turbo`)                                             | `pdf2zh_next -i file.pdf -m gpt-4`                                                                                    |
| `-p`, `--prompt`                | Prompt file path                                                                         | `pdf2zh_next -i file.pdf -p ./prompt.txt`                                                                             |
| `-k`, `--key`                   | API key for translation service                                                          | `pdf2zh_next -i file.pdf -k sk-xxx`                                                                                   |
| `-c`, `--config`                | Config file path                                                                         | `pdf2zh_next -i file.pdf -c ./config.yaml`                                                                            |
| `--openai_base_url`             | OpenAI API base URL                                                                      | `pdf2zh_next -i file.pdf --openai_base_url https://api.openai.com/v1`                                                 |
| `--translator`                  | Translation service (default: `openai`)                                                  | `pdf2zh_next -i file.pdf --translator azure`                                                                          |
| `-t`, `--threads`               | Number of threads (default: `5`)                                                         | `pdf2zh_next -i file.pdf -t 10`                                                                                       |
| `--timeout`                     | Request timeout (default: `60`)                                                          | `pdf2zh_next -i file.pdf --timeout 120`                                                                               |
| `-s`, `--skip`                  | Skip existing files                                                                      | `pdf2zh_next -i ./input_dir -o ./output_dir -s`                                                                       |
| `--no-split`                    | Disable automatic splitting of large files                                               | `pdf2zh_next -i file.pdf --no-split`                                                                                  |
| `--split-size`                  | Split size in MB (default: `10`)                                                         | `pdf2zh_next -i file.pdf --split-size 20`                                                                             |
| `--split-pages`                 | Split by page count                                                                      | `pdf2zh_next -i file.pdf --split-pages 50`                                                                            |
| `--ocr`                         | Enable OCR for image-based PDFs                                                          | `pdf2zh_next -i file.pdf --ocr`                                                                                       |
| `--ocr-lang`                    | OCR language code (default: `eng`)                                                       | `pdf2zh_next -i file.pdf --ocr --ocr-lang chi_sim`                                                                    |
| `--ocr-engine`                  | OCR engine (default: `easyocr`)                                                          | `pdf2zh_next -i file.pdf --ocr --ocr-engine paddleocr`                                                                |
| `--format`                      | Output format (default: `pdf`)                                                           | `pdf2zh_next -i file.pdf --format markdown`                                                                           |
| `--font`                        | Font file path for PDF output                                                            | `pdf2zh_next -i file.pdf --font ./font.ttf`                                                                           |
| `--font-size`                   | Font size for PDF output (default: `12`)                                                 | `pdf2zh_next -i file.pdf --font-size 14`                                                                              |
| `--line-spacing`                | Line spacing for PDF output (default: `1.2`)                                             | `pdf2zh_next -i file.pdf --line-spacing 1.5`                                                                          |
| `--margin`                      | Margin for PDF output (default: `72`)                                                    | `pdf2zh_next -i file.pdf --margin 100`                                                                                |
| `--page-size`                   | Page size for PDF output (default: `A4`)                                                 | `pdf2zh_next -i file.pdf --page-size Letter`                                                                          |
| `--dpi`                         | DPI for image processing (default: `300`)                                                | `pdf2zh_next -i file.pdf --dpi 150`                                                                                   |
| `--no-backup`                   | Disable backup of original files                                                         | `pdf2zh_next -i file.pdf --no-backup`                                                                                 |
| `--backup-dir`                  | Backup directory (default: `./backup`)                                                   | `pdf2zh_next -i file.pdf --backup-dir ./my_backup`                                                                    |
| `--retry`                       | Number of retries on failure (default: `3`)                                              | `pdf2zh_next -i file.pdf --retry 5`                                                                                   |
| `--retry-delay`                 | Delay between retries in seconds (default: `5`)                                          | `pdf2zh_next -i file.pdf --retry-delay 10`                                                                            |
| `--max-tokens`                  | Maximum tokens per request (default: `4096`)                                             | `pdf2zh_next -i file.pdf --max-tokens 2048`                                                                           |
| `--temperature`                 | Temperature for translation (default: `0.1`)                                             | `pdf2zh_next -i file.pdf --temperature 0.5`                                                                           |
| `--batch-size`                  | Batch size for translation (default: `10`)                                               | `pdf2zh_next -i file.pdf --batch-size 20`                                                                             |
| `--no-cache`                    | Disable translation cache                                                                | `pdf2zh_next -i file.pdf --no-cache`                                                                                  |
| `--cache-dir`                   | Cache directory (default: `./cache`)                                                     | `pdf2zh_next -i file.pdf --cache-dir ./my_cache`                                                                      |
| `--clean-cache`                 | Clean cache before translation                                                           | `pdf2zh_next -i file.pdf --clean-cache`                                                                               |
| `--log-file`                    | Log file path                                                                            | `pdf2zh_next -i file.pdf --log-file ./translation.log`                                                                |
| `--log-level`                   | Log level (default: `INFO`)                                                              | `pdf2zh_next -i file.pdf --log-level DEBUG`                                                                           |
| `--no-color`                    | Disable colored output                                                                   | `pdf2zh_next -i file.pdf --no-color`                                                                                  |
| `--dry-run`                     | Dry run without actual translation                                                       | `pdf2zh_next -i file.pdf --dry-run`                                                                                   |
| `--version-check`               | Check for updates                                                                        | `pdf2zh_next --version-check`                                                                                         |
| `--list-languages`              | List supported languages                                                                 | `pdf2zh_next --list-languages`                                                                                        |
| `--list-models`                 | List available models                                                                    | `pdf2zh_next --list-models`                                                                                           |
| `--list-translators`            | List available translation services                                                      | `pdf2zh_next --list-translators`                                                                                      |
| `--list-formats`                | List supported output formats                                                            | `pdf2zh_next --list-formats`                                                                                          |
| `--list-ocr-languages`          | List supported OCR languages                                                             | `pdf2zh_next --list-ocr-languages`                                                                                    |
| `--list-ocr-engines`            | List supported OCR engines                                                               | `pdf2zh_next --list-ocr-engines`                                                                                      |

---

| `--version`                     | Mostrar versão e sair                                                                  | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Mostrar mensagem de ajuda e sair                                                         | `pdf2zh_next -h`                                                                                                      |
| `-v`, `--verbose`               | Definir nível de log para verboso                                                        | `pdf2zh_next -v`                                                                                                      |
| `-vv`, `--very-verbose`         | Definir nível de log para muito verboso                                                  | `pdf2zh_next -vv`                                                                                                     |
| `-q`, `--quiet`                 | Definir nível de log para silencioso                                                     | `pdf2zh_next -q`                                                                                                      |
| `-i`, `--input`                 | Arquivo ou diretório de entrada                                                          | `pdf2zh_next -i file.pdf` <br> `pdf2zh_next -i ./input_dir`                                                           |
| `-o`, `--output`                | Arquivo ou diretório de saída                                                            | `pdf2zh_next -i file.pdf -o file_translated.pdf` <br> `pdf2zh_next -i ./input_dir -o ./output_dir`                    |
| `-l`, `--lang`                  | Código do idioma de destino (padrão: `zh-CN`)                                            | `pdf2zh_next -i file.pdf -l en`                                                                                       |
| `-m`, `--model`                 | Modelo de tradução (padrão: `gpt-3.5-turbo`)                                             | `pdf2zh_next -i file.pdf -m gpt-4`                                                                                    |
| `-p`, `--prompt`                | Caminho do arquivo de prompt                                                             | `pdf2zh_next -i file.pdf -p ./prompt.txt`                                                                             |
| `-k`, `--key`                   | Chave de API para o serviço de tradução                                                  | `pdf2zh_next -i file.pdf -k sk-xxx`                                                                                   |
| `-c`, `--config`                | Caminho do arquivo de configuração                                                       | `pdf2zh_next -i file.pdf -c ./config.yaml`                                                                            |
| `--openai_base_url`             | URL base da API OpenAI                                                                   | `pdf2zh_next -i file.pdf --openai_base_url https://api.openai.com/v1`                                                 |
| `--translator`                  | Serviço de tradução (padrão: `openai`)                                                   | `pdf2zh_next -i file.pdf --translator azure`                                                                          |
| `-t`, `--threads`               | Número de threads (padrão: `5`)                                                          | `pdf2zh_next -i file.pdf -t 10`                                                                                       |
| `--timeout`                     | Tempo limite da requisição (padrão: `60`)                                                | `pdf2zh_next -i file.pdf --timeout 120`                                                                               |
| `-s`, `--skip`                  | Pular arquivos existentes                                                                | `pdf2zh_next -i ./input_dir -o ./output_dir -s`                                                                       |
| `--no-split`                    | Desativar divisão automática de arquivos grandes                                         | `pdf2zh_next -i file.pdf --no-split`                                                                                  |
| `--split-size`                  | Tamanho da divisão em MB (padrão: `10`)                                                  | `pdf2zh_next -i file.pdf --split-size 20`                                                                             |
| `--split-pages`                 | Dividir por contagem de páginas                                                          | `pdf2zh_next -i file.pdf --split-pages 50`                                                                            |
| `--ocr`                         | Ativar OCR para PDFs baseados em imagem                                                  | `pdf2zh_next -i file.pdf --ocr`                                                                                       |
| `--ocr-lang`                    | Código do idioma do OCR (padrão: `eng`)                                                  | `pdf2zh_next -i file.pdf --ocr --ocr-lang chi_sim`                                                                    |
| `--ocr-engine`                  | Motor de OCR (padrão: `easyocr`)                                                         | `pdf2zh_next -i file.pdf --ocr --ocr-engine paddleocr`                                                                |
| `--format`                      | Formato de saída (padrão: `pdf`)                                                         | `pdf2zh_next -i file.pdf --format markdown`                                                                           |
| `--font`                        | Caminho do arquivo de fonte para saída PDF                                               | `pdf2zh_next -i file.pdf --font ./font.ttf`                                                                           |
| `--font-size`                   | Tamanho da fonte para saída PDF (padrão: `12`)                                           | `pdf2zh_next -i file.pdf --font-size 14`                                                                              |
| `--line-spacing`                | Espaçamento entre linhas para saída PDF (padrão: `1.2`)                                  | `pdf2zh_next -i file.pdf --line-spacing 1.5`                                                                          |
| `--margin`                      | Margem para saída PDF (padrão: `72`)                                                     | `pdf2zh_next -i file.pdf --margin 100`                                                                                |
| `--page-size`                   | Tamanho da página para saída PDF (padrão: `A4`)                                          | `pdf2zh_next -i file.pdf --page-size Letter`                                                                          |
| `--dpi`                         | DPI para processamento de imagem (padrão: `300`)                                         | `pdf2zh_next -i file.pdf --dpi 150`                                                                                   |
| `--no-backup`                   | Desativar backup dos arquivos originais                                                  | `pdf2zh_next -i file.pdf --no-backup`                                                                                 |
| `--backup-dir`                  | Diretório de backup (padrão: `./backup`)                                                 | `pdf2zh_next -i file.pdf --backup-dir ./my_backup`                                                                    |
| `--retry`                       | Número de tentativas em caso de falha (padrão: `3`)                                      | `pdf2zh_next -i file.pdf --retry 5`                                                                                   |
| `--retry-delay`                 | Atraso entre tentativas em segundos (padrão: `5`)                                        | `pdf2zh_next -i file.pdf --retry-delay 10`                                                                            |
| `--max-tokens`                  | Tokens máximos por requisição (padrão: `4096`)                                           | `pdf2zh_next -i file.pdf --max-tokens 2048`                                                                           |
| `--temperature`                 | Temperatura para tradução (padrão: `0.1`)                                                | `pdf2zh_next -i file.pdf --temperature 0.5`                                                                           |
| `--batch-size`                  | Tamanho do lote para tradução (padrão: `10`)                                             | `pdf2zh_next -i file.pdf --batch-size 20`                                                                             |
| `--no-cache`                    | Desativar cache de tradução                                                              | `pdf2zh_next -i file.pdf --no-cache`                                                                                  |
| `--cache-dir`                   | Diretório de cache (padrão: `./cache`)                                                   | `pdf2zh_next -i file.pdf --cache-dir ./my_cache`                                                                      |
| `--clean-cache`                 | Limpar cache antes da tradução                                                           | `pdf2zh_next -i file.pdf --clean-cache`                                                                               |
| `--log-file`                    | Caminho do arquivo de log                                                                | `pdf2zh_next -i file.pdf --log-file ./translation.log`                                                                |
| `--log-level`                   | Nível de log (padrão: `INFO`)                                                            | `pdf2zh_next -i file.pdf --log-level DEBUG`                                                                           |
| `--no-color`                    | Desativar saída colorida                                                                 | `pdf2zh_next -i file.pdf --no-color`                                                                                  |
| `--dry-run`                     | Execução de teste sem tradução real                                                      | `pdf2zh_next -i file.pdf --dry-run`                                                                                   |
| `--version-check`               | Verificar atualizações                                                                   | `pdf2zh_next --version-check`                                                                                         |
| `--list-languages`              | Listar idiomas suportados                                                                | `pdf2zh_next --list-languages`                                                                                        |
| `--list-models`                 | Listar modelos disponíveis                                                               | `pdf2zh_next --list-models`                                                                                           |
| `--list-translators`            | Listar serviços de tradução disponíveis                                                  | `pdf2zh_next --list-translators`                                                                                      |
| `--list-formats`                | Listar formatos de saída suportados                                                      | `pdf2zh_next --list-formats`                                                                                          |
| `--list-ocr-languages`          | Listar idiomas de OCR suportados                                                         | `pdf2zh_next --list-ocr-languages`                                                                                    |
| `--list-ocr-engines`            | Listar motores de OCR suportados                                                         | `pdf2zh_next --list-ocr-engines`                                                                                      |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--output_dir`                  | Specify the output directory                                                            | `pdf2zh_next example.pdf --output_dir ./output`                                                                        |
| `--output_filename`             | Specify the output filename                                                             | `pdf2zh_next example.pdf --output_filename example_translated.pdf`                                                     |
| `--cache_dir`                   | Specify the cache directory (for storing temporary files)                               | `pdf2zh_next example.pdf --cache_dir ./cache`                                                                          |
| `--cache`                       | Enable cache for translation results (default: `true`)                                  | `pdf2zh_next example.pdf --cache false`                                                                                |
| `--overwrite`                   | Overwrite existing files (default: `false`)                                             | `pdf2zh_next example.pdf --overwrite true`                                                                             |
| `--timeout`                     | Set the timeout for the translation service (in seconds)                                | `pdf2zh_next example.pdf --timeout 300`                                                                                |
| `--proxy`                       | Set the proxy for the translation service                                               | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--retry`                       | Set the number of retries for the translation service (default: `3`)                    | `pdf2zh_next example.pdf --retry 5`                                                                                    |
| `--retry_delay`                 | Set the delay between retries (in seconds) (default: `5`)                               | `pdf2zh_next example.pdf --retry_delay 10`                                                                             |
| `--max_concurrent`              | Set the maximum number of concurrent translation requests (default: `5`)                | `pdf2zh_next example.pdf --max_concurrent 10`                                                                          |
| `--dry_run`                     | Perform a dry run without actually translating (default: `false`)                       | `pdf2zh_next example.pdf --dry_run true`                                                                               |
| `--verbose`                     | Enable verbose output (default: `false`)                                                | `pdf2zh_next example.pdf --verbose true`                                                                               |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Show help information                                                                   | `pdf2zh_next --help`                                                                                                   |

---

### TRANSLATED TEXT

| `--pages`                       | Tradução parcial do documento                                                           | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--output_dir`                  | Especificar o diretório de saída                                                        | `pdf2zh_next example.pdf --output_dir ./output`                                                                        |
| `--output_filename`             | Especificar o nome do arquivo de saída                                                  | `pdf2zh_next example.pdf --output_filename example_translated.pdf`                                                     |
| `--cache_dir`                   | Especificar o diretório de cache (para armazenar arquivos temporários)                  | `pdf2zh_next example.pdf --cache_dir ./cache`                                                                          |
| `--cache`                       | Ativar cache para resultados de tradução (padrão: `true`)                               | `pdf2zh_next example.pdf --cache false`                                                                                |
| `--overwrite`                   | Substituir arquivos existentes (padrão: `false`)                                        | `pdf2zh_next example.pdf --overwrite true`                                                                             |
| `--timeout`                     | Definir o tempo limite para o serviço de tradução (em segundos)                         | `pdf2zh_next example.pdf --timeout 300`                                                                                |
| `--proxy`                       | Definir o proxy para o serviço de tradução                                              | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--retry`                       | Definir o número de tentativas para o serviço de tradução (padrão: `3`)                 | `pdf2zh_next example.pdf --retry 5`                                                                                    |
| `--retry_delay`                 | Definir o atraso entre as tentativas (em segundos) (padrão: `5`)                        | `pdf2zh_next example.pdf --retry_delay 10`                                                                             |
| `--max_concurrent`              | Definir o número máximo de solicitações de tradução simultâneas (padrão: `5`)           | `pdf2zh_next example.pdf --max_concurrent 10`                                                                          |
| `--dry_run`                     | Executar uma simulação sem realmente traduzir (padrão: `false`)                         | `pdf2zh_next example.pdf --dry_run true`                                                                               |
| `--verbose`                     | Ativar saída detalhada (padrão: `false`)                                                | `pdf2zh_next example.pdf --verbose true`                                                                               |
| `--version`                     | Mostrar informações de versão                                                           | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Mostrar informações de ajuda                                                            | `pdf2zh_next --help`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               |
| `--translator`                  | Translation service to use                                                              | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-config`           | Path to translator configuration file                                                   | `pdf2zh_next example.pdf --translator-config config.json`                                                             |
| `--translator-key`              | API key for the translation service                                                     | `pdf2zh_next example.pdf --translator-key YOUR_API_KEY`                                                               |
| `--translator-endpoint`         | Endpoint for the translation service                                                    | `pdf2zh_next example.pdf --translator-endpoint https://api.cognitive.microsofttranslator.com`                         |
| `--translator-region`           | Region for the translation service                                                      | `pdf2zh_next example.pdf --translator-region eastus`                                                                  |
| `--translator-project-id`       | Project ID for the translation service                                                  | `pdf2zh_next example.pdf --translator-project-id YOUR_PROJECT_ID`                                                     |
| `--translator-model`            | Model for the translation service                                                       | `pdf2zh_next example.pdf --translator-model gpt-3.5-turbo`                                                            |

---

### TRANSLATION RESULT

| `--lang-in`                     | Código do idioma de origem                                                              | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Código do idioma de destino                                                              | `pdf2zh_next example.pdf --lang-out zh`                                                                               |
| `--translator`                  | Serviço de tradução a ser usado                                                          | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-config`           | Caminho para o arquivo de configuração do tradutor                                        | `pdf2zh_next example.pdf --translator-config config.json`                                                             |
| `--translator-key`              | Chave da API para o serviço de tradução                                                   | `pdf2zh_next example.pdf --translator-key YOUR_API_KEY`                                                               |
| `--translator-endpoint`         | Endpoint para o serviço de tradução                                                       | `pdf2zh_next example.pdf --translator-endpoint https://api.cognitive.microsofttranslator.com`                         |
| `--translator-region`           | Região para o serviço de tradução                                                         | `pdf2zh_next example.pdf --translator-region eastus`                                                                  |
| `--translator-project-id`       | ID do projeto para o serviço de tradução                                                   | `pdf2zh_next example.pdf --translator-project-id YOUR_PROJECT_ID`                                                     |
| `--translator-model`            | Modelo para o serviço de tradução                                                         | `pdf2zh_next example.pdf --translator-model gpt-3.5-turbo`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | Source language code                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                 |
| `--translator`                  | Translation service name                                                                | `pdf2zh_next example.pdf --translator google`                                                                          |
| `--api-key`                     | API key for the translation service                                                     | `pdf2zh_next example.pdf --translator openai --api-key YOUR_API_KEY`                                                   |
| `--model`                       | Model name for the translation service                                                  | `pdf2zh_next example.pdf --translator openai --model gpt-4`                                                            |
| `--proxy`                       | Proxy server address                                                                    | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--concurrent`                  | Number of concurrent translation requests                                               | `pdf2zh_next example.pdf --concurrent 10`                                                                              |
| `--retry`                       | Number of retries for failed translation requests                                       | `pdf2zh_next example.pdf --retry 3`                                                                                    |
| `--timeout`                     | Timeout for each translation request (seconds)                                          | `pdf2zh_next example.pdf --timeout 30`                                                                                 |
| `--output`                      | Output file path                                                                        | `pdf2zh_next example.pdf --output ./translated.pdf`                                                                    |
| `--force`                       | Overwrite existing output file without confirmation                                     | `pdf2zh_next example.pdf --output ./translated.pdf --force`                                                            |
| `--no-backup`                   | Skip backup of the original file                                                        | `pdf2zh_next example.pdf --no-backup`                                                                                  |
| `--ignore-size`                 | Ignore file size warning                                                                | `pdf2zh_next example.pdf --ignore-size`                                                                                |
| `--ignore-errors`               | Continue translation even if some pages fail                                            | `pdf2zh_next example.pdf --ignore-errors`                                                                              |
| `--ignore-glossary`             | Ignore glossary file                                                                    | `pdf2zh_next example.pdf --ignore-glossary`                                                                            |
| `--glossary`                    | Path to glossary file                                                                   | `pdf2zh_next example.pdf --glossary ./glossary.txt`                                                                    |
| `--save-config`                 | Save current configuration to a file                                                    | `pdf2zh_next example.pdf --save-config ./config.json`                                                                  |
| `--load-config`                 | Load configuration from a file                                                          | `pdf2zh_next example.pdf --load-config ./config.json`                                                                  |
| `--list-translators`            | List available translation services                                                     | `pdf2zh_next --list-translators`                                                                                       |
| `--list-languages`              | List supported languages for a translation service                                      | `pdf2zh_next --list-languages --translator google`                                                                     |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                   |

---

### TRANSLATION RESULT

| `--lang-out`                    | Código do idioma de destino                                                             | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | Código do idioma de origem                                                              | `pdf2zh_next example.pdf --lang-in en`                                                                                 |
| `--translator`                  | Nome do serviço de tradução                                                             | `pdf2zh_next example.pdf --translator google`                                                                          |
| `--api-key`                     | Chave de API para o serviço de tradução                                                 | `pdf2zh_next example.pdf --translator openai --api-key YOUR_API_KEY`                                                   |
| `--model`                       | Nome do modelo para o serviço de tradução                                               | `pdf2zh_next example.pdf --translator openai --model gpt-4`                                                            |
| `--proxy`                       | Endereço do servidor proxy                                                              | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                |
| `--concurrent`                  | Número de solicitações de tradução simultâneas                                          | `pdf2zh_next example.pdf --concurrent 10`                                                                              |
| `--retry`                       | Número de tentativas para solicitações de tradução com falha                            | `pdf2zh_next example.pdf --retry 3`                                                                                    |
| `--timeout`                     | Tempo limite para cada solicitação de tradução (segundos)                               | `pdf2zh_next example.pdf --timeout 30`                                                                                 |
| `--output`                      | Caminho do arquivo de saída                                                             | `pdf2zh_next example.pdf --output ./translated.pdf`                                                                    |
| `--force`                       | Sobrescrever arquivo de saída existente sem confirmação                                 | `pdf2zh_next example.pdf --output ./translated.pdf --force`                                                            |
| `--no-backup`                   | Ignorar backup do arquivo original                                                      | `pdf2zh_next example.pdf --no-backup`                                                                                  |
| `--ignore-size`                 | Ignorar aviso de tamanho do arquivo                                                     | `pdf2zh_next example.pdf --ignore-size`                                                                                |
| `--ignore-errors`               | Continuar a tradução mesmo que algumas páginas falhem                                   | `pdf2zh_next example.pdf --ignore-errors`                                                                              |
| `--ignore-glossary`             | Ignorar arquivo de glossário                                                            | `pdf2zh_next example.pdf --ignore-glossary`                                                                            |
| `--glossary`                    | Caminho para o arquivo de glossário                                                     | `pdf2zh_next example.pdf --glossary ./glossary.txt`                                                                    |
| `--save-config`                 | Salvar configuração atual em um arquivo                                                 | `pdf2zh_next example.pdf --save-config ./config.json`                                                                  |
| `--load-config`                 | Carregar configuração de um arquivo                                                     | `pdf2zh_next example.pdf --load-config ./config.json`                                                                  |
| `--list-translators`            | Listar serviços de tradução disponíveis                                                 | `pdf2zh_next --list-translators`                                                                                       |
| `--list-languages`              | Listar idiomas suportados para um serviço de tradução                                   | `pdf2zh_next --list-languages --translator google`                                                                     |
| `--version`                     | Mostrar informações de versão                                                           | `pdf2zh_next --version`                                                                                                |
| `--help`                        | Mostrar mensagem de ajuda                                                               | `pdf2zh_next --help`                                                                                                   |
| :------------------------------ | :------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--min-text-ratio`              | Minimum text ratio to translate (text length / block area)                             | `pdf2zh_next example.pdf --min-text-ratio 0.01`                                                                       |
| `--keep-drawings`               | Keep drawings in the output                                                            | `pdf2zh_next example.pdf --keep-drawings`                                                                             |
| `--keep-highlights`             | Keep highlights in the output                                                          | `pdf2zh_next example.pdf --keep-highlights`                                                                           |
| `--keep-underlines`             | Keep underlines in the output                                                          | `pdf2zh_next example.pdf --keep-underlines`                                                                           |
| `--keep-tables`                 | Keep tables in the output                                                              | `pdf2zh_next example.pdf --keep-tables`                                                                               |
| `--keep-mark-annotations`       | Keep mark annotations in the output                                                    | `pdf2zh_next example.pdf --keep-mark-annotations`                                                                     |
| `--keep-annotations`            | Keep annotations in the output                                                         | `pdf2zh_next example.pdf --keep-annotations`                                                                          |
| `--keep-fill-forms`             | Keep fill forms in the output                                                          | `pdf2zh_next example.pdf --keep-fill-forms`                                                                           |
| `--keep-hidden-text`            | Keep hidden text in the output                                                         | `pdf2zh_next example.pdf --keep-hidden-text`                                                                          |
| `--keep-page-layout`            | Keep page layout in the output                                                         | `pdf2zh_next example.pdf --keep-page-layout`                                                                          |
| `--remove-overlapping-text`     | Remove overlapping text in the output                                                  | `pdf2zh_next example.pdf --remove-overlapping-text`                                                                   |
| `--remove-watermark`            | Remove watermark in the output                                                         | `pdf2zh_next example.pdf --remove-watermark`                                                                          |
| `--remove-header`                | Remove header in the output                                                            | `pdf2zh_next example.pdf --remove-header`                                                                             |
| `--remove-footer`                | Remove footer in the output                                                            | `pdf2zh_next example.pdf --remove-footer`                                                                             |
| `--remove-invisible-text`       | Remove invisible text in the output                                                    | `pdf2zh_next example.pdf --remove-invisible-text`                                                                     |
| `--remove-redundant-text`       | Remove redundant text in the output                                                    | `pdf2zh_next example.pdf --remove-redundant-text`                                                                     |
| `--remove-redundant-characters` | Remove redundant characters in the output                                              | `pdf2zh_next example.pdf --remove-redundant-characters`                                                               |
| `--remove-redundant-blanks`     | Remove redundant blanks in the output                                                  | `pdf2zh_next example.pdf --remove-redundant-blanks`                                                                   |
| `--remove-line-breaks`          | Remove line breaks in the output                                                       | `pdf2zh_next example.pdf --remove-line-breaks`                                                                        |
| `--remove-non-standard-fonts`   | Remove non-standard fonts in the output                                                | `pdf2zh_next example.pdf --remove-non-standard-fonts`                                                                 |
| `--remove-non-ascii`            | Remove non-ASCII characters in the output                                              | `pdf2zh_next example.pdf --remove-non-ascii`                                                                          |
| `--remove-non-latin`            | Remove non-Latin characters in the output                                              | `pdf2zh_next example.pdf --remove-non-latin`                                                                          |
| `--remove-non-english`          | Remove non-English characters in the output                                            | `pdf2zh_next example.pdf --remove-non-english`                                                                        |
| `--remove-non-chinese`          | Remove non-Chinese characters in the output                                            | `pdf2zh_next example.pdf --remove-non-chinese`                                                                        |
| `--remove-non-japanese`         | Remove non-Japanese characters in the output                                           | `pdf2zh_next example.pdf --remove-non-japanese`                                                                       |
| `--remove-non-korean`           | Remove non-Korean characters in the output                                             | `pdf2zh_next example.pdf --remove-non-korean`                                                                         |
| `--remove-non-arabic`           | Remove non-Arabic characters in the output                                             | `pdf2zh_next example.pdf --remove-non-arabic`                                                                         |

---

| `--min-text-length`             | Comprimento mínimo do texto para traduzir                                                        | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| :------------------------------ | :------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--min-text-ratio`              | Proporção mínima do texto para traduzir (comprimento do texto / área do bloco)                             | `pdf2zh_next example.pdf --min-text-ratio 0.01`                                                                       |
| `--keep-drawings`               | Manter desenhos na saída                                                            | `pdf2zh_next example.pdf --keep-drawings`                                                                             |
| `--keep-highlights`             | Manter destaques na saída                                                          | `pdf2zh_next example.pdf --keep-highlights`                                                                           |
| `--keep-underlines`             | Manter sublinhados na saída                                                          | `pdf2zh_next example.pdf --keep-underlines`                                                                           |
| `--keep-tables`                 | Manter tabelas na saída                                                              | `pdf2zh_next example.pdf --keep-tables`                                                                               |
| `--keep-mark-annotations`       | Manter anotações de marcação na saída                                                    | `pdf2zh_next example.pdf --keep-mark-annotations`                                                                     |
| `--keep-annotations`            | Manter anotações na saída                                                         | `pdf2zh_next example.pdf --keep-annotations`                                                                          |
| `--keep-fill-forms`             | Manter formulários preenchíveis na saída                                                          | `pdf2zh_next example.pdf --keep-fill-forms`                                                                           |
| `--keep-hidden-text`            | Manter texto oculto na saída                                                         | `pdf2zh_next example.pdf --keep-hidden-text`                                                                          |
| `--keep-page-layout`            | Manter layout da página na saída                                                         | `pdf2zh_next example.pdf --keep-page-layout`                                                                          |
| `--remove-overlapping-text`     | Remover texto sobreposto na saída                                                  | `pdf2zh_next example.pdf --remove-overlapping-text`                                                                   |
| `--remove-watermark`            | Remover marca d'água na saída                                                         | `pdf2zh_next example.pdf --remove-watermark`                                                                          |
| `--remove-header`                | Remover cabeçalho na saída                                                            | `pdf2zh_next example.pdf --remove-header`                                                                             |
| `--remove-footer`                | Remover rodapé na saída                                                            | `pdf2zh_next example.pdf --remove-footer`                                                                             |
| `--remove-invisible-text`       | Remover texto invisível na saída                                                    | `pdf2zh_next example.pdf --remove-invisible-text`                                                                     |
| `--remove-redundant-text`       | Remover texto redundante na saída                                                    | `pdf2zh_next example.pdf --remove-redundant-text`                                                                     |
| `--remove-redundant-characters` | Remover caracteres redundantes na saída                                              | `pdf2zh_next example.pdf --remove-redundant-characters`                                                               |
| `--remove-redundant-blanks`     | Remover espaços em branco redundantes na saída                                                  | `pdf2zh_next example.pdf --remove-redundant-blanks`                                                                   |
| `--remove-line-breaks`          | Remover quebras de linha na saída                                                       | `pdf2zh_next example.pdf --remove-line-breaks`                                                                        |
| `--remove-non-standard-fonts`   | Remover fontes não padrão na saída                                                | `pdf2zh_next example.pdf --remove-non-standard-fonts`                                                                 |
| `--remove-non-ascii`            | Remover caracteres não ASCII na saída                                              | `pdf2zh_next example.pdf --remove-non-ascii`                                                                          |
| `--remove-non-latin`            | Remover caracteres não latinos na saída                                              | `pdf2zh_next example.pdf --remove-non-latin`                                                                          |
| `--remove-non-english`          | Remover caracteres não ingleses na saída                                            | `pdf2zh_next example.pdf --remove-non-english`                                                                        |
| `--remove-non-chinese`          | Remover caracteres não chineses na saída                                            | `pdf2zh_next example.pdf --remove-non-chinese`                                                                        |
| `--remove-non-japanese`         | Remover caracteres não japoneses na saída                                           | `pdf2zh_next example.pdf --remove-non-japanese`                                                                       |
| `--remove-non-korean`           | Remover caracteres não coreanos na saída                                             | `pdf2zh_next example.pdf --remove-non-korean`                                                                         |
| `--remove-non-arabic`           | Remover caracteres não árabes na saída                                             | `pdf2zh_next example.pdf --remove-non-arabic`                                                                         |
`http://127.0.0.1:8000` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--rpc-translation`             | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translation http://127.0.0.1:8001`                                                      | `http://127.0.0.1:8001` |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8002`                                                              | `http://127.0.0.1:8002` |
| `--rpc-ocr-multicol`            | RPC service host address for multi-column OCR                                           | `pdf2zh_next example.pdf --rpc-ocr-multicol http://127.0.0.1:8003`                                                     | `http://127.0.0.1:8003` |
| `--rpc-ocr-singlecol`           | RPC service host address for single-column OCR                                          | `pdf2zh_next example.pdf --rpc-ocr-singlecol http://127.0.0.1:8004`                                                    | `http://127.0.0.1:8004` |
| `--rpc-ocr-formula`             | RPC service host address for formula OCR                                                | `pdf2zh_next example.pdf --rpc-ocr-formula http://127.0.0.1:8005`                                                      | `http://127.0.0.1:8005` |
| `--rpc-ocr-table`               | RPC service host address for table OCR                                                  | `pdf2zh_next example.pdf --rpc-ocr-table http://127.0.0.1:8006`                                                        | `http://127.0.0.1:8006` |
| `--rpc-ocr-inline-formula`      | RPC service host address for inline formula OCR                                         | `pdf2zh_next example.pdf --rpc-ocr-inline-formula http://127.0.0.1:8007`                                               | `http://127.0.0.1:8007` |
| `--rpc-ocr-block-formula`       | RPC service host address for block formula OCR                                          | `pdf2zh_next example.pdf --rpc-ocr-block-formula http://127.0.0.1:8008`                                                | `http://127.0.0.1:8008` |
| `--rpc-ocr-figure`              | RPC service host address for figure OCR                                                 | `pdf2zh_next example.pdf --rpc-ocr-figure http://127.0.0.1:8009`                                                       | `http://127.0.0.1:8009` |
| `--rpc-ocr-caption`             | RPC service host address for caption OCR                                                | `pdf2zh_next example.pdf --rpc-ocr-caption http://127.0.0.1:8010`                                                      | `http://127.0.0.1:8010` |

---

### TRANSLATION

| `--rpc-doclayout`               | Endereço do host do serviço RPC para análise de layout do documento                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       | `http://127.0.0.1:8000` |
| ------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--rpc-translation`             | Endereço do host do serviço RPC para tradução                                                         | `pdf2zh_next example.pdf --rpc-translation http://127.0.0.1:8001`                                                      | `http://127.0.0.1:8001` |
| `--rpc-ocr`                     | Endereço do host do serviço RPC para OCR                                                              | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8002`                                                              | `http://127.0.0.1:8002` |
| `--rpc-ocr-multicol`            | Endereço do host do serviço RPC para OCR de múltiplas colunas                                         | `pdf2zh_next example.pdf --rpc-ocr-multicol http://127.0.0.1:8003`                                                     | `http://127.0.0.1:8003` |
| `--rpc-ocr-singlecol`           | Endereço do host do serviço RPC para OCR de coluna única                                              | `pdf2zh_next example.pdf --rpc-ocr-singlecol http://127.0.0.1:8004`                                                    | `http://127.0.0.1:8004` |
| `--rpc-ocr-formula`             | Endereço do host do serviço RPC para OCR de fórmulas                                                  | `pdf2zh_next example.pdf --rpc-ocr-formula http://127.0.0.1:8005`                                                      | `http://127.0.0.1:8005` |
| `--rpc-ocr-table`               | Endereço do host do serviço RPC para OCR de tabelas                                                   | `pdf2zh_next example.pdf --rpc-ocr-table http://127.0.0.1:8006`                                                        | `http://127.0.0.1:8006` |
| `--rpc-ocr-inline-formula`      | Endereço do host do serviço RPC para OCR de fórmulas em linha                                         | `pdf2zh_next example.pdf --rpc-ocr-inline-formula http://127.0.0.1:8007`                                               | `http://127.0.0.1:8007` |
| `--rpc-ocr-block-formula`       | Endereço do host do serviço RPC para OCR de fórmulas em bloco                                         | `pdf2zh_next example.pdf --rpc-ocr-block-formula http://127.0.0.1:8008`                                                | `http://127.0.0.1:8008` |
| `--rpc-ocr-figure`              | Endereço do host do serviço RPC para OCR de figuras                                                   | `pdf2zh_next example.pdf --rpc-ocr-figure http://127.0.0.1:8009`                                                       | `http://127.0.0.1:8009` |
| `--rpc-ocr-caption`             | Endereço do host do serviço RPC para OCR de legendas                                                  | `pdf2zh_next example.pdf --rpc-ocr-caption http://127.0.0.1:8010`                                                      | `http://127.0.0.1:8010` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--file-size`                   | File size limit for translation service (in MB)                                         | `pdf2zh_next example.pdf --file-size 50`                                                                              |
| `--page-count`                  | Page count limit for translation service                                                | `pdf2zh_next example.pdf --page-count 100`                                                                            |
| `--char-count`                  | Character count limit for translation service                                           | `pdf2zh_next example.pdf --char-count 100000`                                                                         |
| `--timeout`                     | Timeout for translation service (in seconds)                                            | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry`                       | Retry times for translation service                                                     | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--retry-interval`              | Retry interval for translation service (in seconds)                                     | `pdf2zh_next example.pdf --retry-interval 10`                                                                         |
| `--batch-size`                  | Batch size for translation service                                                      | `pdf2zh_next example.pdf --batch-size 5`                                                                              |
| `--batch-interval`              | Batch interval for translation service (in seconds)                                     | `pdf2zh_next example.pdf --batch-interval 1`                                                                          |
| `--batch-concurrency`           | Batch concurrency for translation service                                               | `pdf2zh_next example.pdf --batch-concurrency 2`                                                                       |
| `--batch-timeout`               | Batch timeout for translation service (in seconds)                                      | `pdf2zh_next example.pdf --batch-timeout 60`                                                                          |
| `--batch-retry`                 | Batch retry times for translation service                                               | `pdf2zh_next example.pdf --batch-retry 3`                                                                             |
| `--batch-retry-interval`        | Batch retry interval for translation service (in seconds)                               | `pdf2zh_next example.pdf --batch-retry-interval 10`                                                                   |
| `--batch-char-limit`            | Batch character limit for translation service                                           | `pdf2zh_next example.pdf --batch-char-limit 10000`                                                                    |
| `--batch-page-limit`            | Batch page limit for translation service                                                | `pdf2zh_next example.pdf --batch-page-limit 10`                                                                       |
| `--batch-file-limit`            | Batch file limit for translation service                                                | `pdf2zh_next example.pdf --batch-file-limit 10`                                                                       |
| `--batch-size-limit`            | Batch size limit for translation service (in MB)                                        | `pdf2zh_next example.pdf --batch-size-limit 50`                                                                       |
| `--batch-time-limit`            | Batch time limit for translation service (in seconds)                                   | `pdf2zh_next example.pdf --batch-time-limit 60`                                                                       |
| `--batch-concurrency-limit`     | Batch concurrency limit for translation service                                         | `pdf2zh_next example.pdf --batch-concurrency-limit 2`                                                                 |
| `--batch-timeout-limit`         | Batch timeout limit for translation service (in seconds)                                | `pdf2zh_next example.pdf --batch-timeout-limit 60`                                                                    |
| `--batch-retry-limit`           | Batch retry limit for translation service                                               | `pdf2zh_next example.pdf --batch-retry-limit 3`                                                                       |
| `--batch-retry-interval-limit`  | Batch retry interval limit for translation service (in seconds)                          | `pdf2zh_next example.pdf --batch-retry-interval-limit 10`                                                             |
| `--batch-char-limit-limit`      | Batch character limit limit for translation service                                     | `pdf2zh_next example.pdf --batch-char-limit-limit 10000`                                                              |
| `--batch-page-limit-limit`      | Batch page limit limit for translation service                                          | `pdf2zh_next example.pdf --batch-page-limit-limit 10`                                                                 |
| `--batch-file-limit-limit`      | Batch file limit limit for translation service                                          | `pdf2zh_next example.pdf --batch-file-limit-limit 10`                                                                 |
| `--batch-size-limit-limit`      | Batch size limit limit for translation service (in MB)                                  | `pdf2zh_next example.pdf --batch-size-limit-limit 50`                                                                 |
| `--batch-time-limit-limit`      | Batch time limit limit for translation service (in seconds)                             | `pdf2zh_next example.pdf --batch-time-limit-limit 60`                                                                 |
| `--batch-concurrency-limit-limit` | Batch concurrency limit limit for translation service                                 | `pdf2zh_next example.pdf --batch-concurrency-limit-limit 2`                                                           |
| `--batch-timeout-limit-limit`   | Batch timeout limit limit for translation service (in seconds)                          | `pdf2zh_next example.pdf --batch-timeout-limit-limit 60`                                                              |
| `--batch-retry-limit-limit`     | Batch retry limit limit for translation service                                         | `pdf2zh_next example.pdf --batch-retry-limit-limit 3`                                                                 |
| `--batch-retry-interval-limit-limit` | Batch retry interval limit limit for translation service (in seconds)                | `pdf2zh_next example.pdf --batch-retry-interval-limit-limit 10`                                                       |
| `--batch-char-limit-limit-limit` | Batch character limit limit limit for translation service                             | `pdf2zh_next example.pdf --batch-char-limit-limit-limit 10000`                                                        |
| `--batch-page-limit-limit-limit` | Batch page limit limit limit for translation service                                  | `pdf2zh_next example.pdf --batch-page-limit-limit-limit 10`                                                           |
| `--batch-file-limit-limit-limit` | Batch file limit limit limit for translation service                                  | `pdf2zh_next example.pdf --batch-file-limit-limit-limit 10`                                                           |
| `--batch-size-limit-limit-limit` | Batch size limit limit limit for translation service (in MB)                          | `pdf2zh_next example.pdf --batch-size-limit-limit-limit 50`                                                           |
| `--batch-time-limit-limit-limit` | Batch time limit limit limit for translation service (in seconds)                     | `pdf2zh_next example.pdf --batch-time-limit-limit-limit 60`                                                           |
| `--batch-concurrency-limit-limit-limit` | Batch concurrency limit limit limit for translation service                       | `pdf2zh_next example.pdf --batch-concurrency-limit-limit-limit 2`                                                     |
| `--batch-timeout-limit-limit-limit` | Batch timeout limit limit limit for translation service (in seconds)                | `pdf2zh_next example.pdf --batch-timeout-limit-limit-limit 60`                                                        |
| `--batch-retry-limit-limit-limit` | Batch retry limit limit limit for translation service                                 | `pdf2zh_next example.pdf --batch-retry-limit-limit-limit 3`                                                           |
| `--batch-retry-interval-limit-limit-limit` | Batch retry interval limit limit limit for translation service (in seconds)      | `pdf2zh_next example.pdf --batch-retry-interval-limit-limit-limit 10`                                                |
| `--batch-char-limit-limit-limit-limit` | Batch character limit limit limit limit for translation service               | `pdf2zh_next example.pdf --batch-char-limit-limit-limit-limit 10000`                                                 |
| `--batch-page-limit-limit-limit-limit` | Batch page limit limit limit limit for translation service                    | `pdf2zh_next example.pdf --batch-page-limit-limit-limit-limit 10`                                                     |
| `--batch-file-limit-limit-limit-limit` | Batch file limit limit limit limit for translation service                    | `pdf2zh_next example.pdf --batch-file-limit-limit-limit-limit 10`                                                     |
| `--batch-size-limit-limit-limit-limit` | Batch size limit limit limit limit for translation service (in MB)            | `pdf2zh_next example.pdf --batch-size-limit-limit-limit-limit 50`                                                     |
| `--batch-time-limit-limit-limit-limit` | Batch time limit limit limit limit for translation service (in seconds)         | `pdf2zh_next example.pdf --batch-time-limit-limit-limit-limit 60`                                                     |
| `--batch-concurrency-limit-limit-limit-limit` | Batch concurrency limit limit limit limit for translation service         | `pdf2zh_next example.pdf --batch-concurrency-limit-limit-limit-limit 2`                                               |
| `--batch-timeout-limit-limit-limit-limit` | Batch timeout limit limit limit limit for translation service (in seconds)  | `pdf2zh_next example.pdf --batch-timeout-limit-limit-limit-limit 60`                                                 |
| `--batch-retry-limit-limit-limit-limit` | Batch retry limit limit limit limit for translation service                 | `pdf2zh_next example.pdf --batch-retry-limit-limit-limit-limit 3`                                                     |
| `--batch-retry-interval-limit-limit-limit-limit` | Batch retry interval limit limit limit limit for translation service (in seconds) | `pdf2zh_next example.pdf --batch-retry-interval-limit-limit-limit-limit 10`                                          |

---

### TRANSLATION RESULT

| `--qps`                         | Limite de QPS para o serviço de tradução                                               | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--file-size`                   | Limite de tamanho de arquivo para o serviço de tradução (em MB)                          | `pdf2zh_next example.pdf --file-size 50`                                                                              |
| `--page-count`                  | Limite de contagem de páginas para o serviço de tradução                                 | `pdf2zh_next example.pdf --page-count 100`                                                                            |
| `--char-count`                  | Limite de contagem de caracteres para o serviço de tradução                             | `pdf2zh_next example.pdf --char-count 100000`                                                                         |
| `--timeout`                     | Tempo limite para o serviço de tradução (em segundos)                                    | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry`                       | Número de tentativas para o serviço de tradução                                          | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--retry-interval`              | Intervalo de repetição para o serviço de tradução (em segundos)                         | `pdf2zh_next example.pdf --retry-interval 10`                                                                         |
| `--batch-size`                  | Tamanho do lote para o serviço de tradução                                               | `pdf2zh_next example.pdf --batch-size 5`                                                                              |
| `--batch-interval`              | Intervalo do lote para o serviço de tradução (em segundos)                               | `pdf2zh_next example.pdf --batch-interval 1`                                                                          |
| `--batch-concurrency`           | Concorrência do lote para o serviço de tradução                                          | `pdf2zh_next example.pdf --batch-concurrency 2`                                                                       |
| `--batch-timeout`               | Tempo limite do lote para o serviço de tradução (em segundos)                           | `pdf2zh_next example.pdf --batch-timeout 60`                                                                          |
| `--batch-retry`                 | Número de tentativas do lote para o serviço de tradução                                  | `pdf2zh_next example.pdf --batch-retry 3`                                                                             |
| `--batch-retry-interval`        | Intervalo de repetição do lote para o serviço de tradução (em segundos)                 | `pdf2zh_next example.pdf --batch-retry-interval 10`                                                                   |
| `--batch-char-limit`            | Limite de caracteres do lote para o serviço de tradução                                 | `pdf2zh_next example.pdf --batch-char-limit 10000`                                                                    |
| `--batch-page-limit`            | Limite de páginas do lote para o serviço de tradução                                    | `pdf2zh_next example.pdf --batch-page-limit 10`                                                                       |
| `--batch-file-limit`            | Limite de arquivos do lote para o serviço de tradução                                   | `pdf2zh_next example.pdf --batch-file-limit 10`                                                                       |
| `--batch-size-limit`            | Limite de tamanho do lote para o serviço de tradução (em MB)                            | `pdf2zh_next example.pdf --batch-size-limit 50`                                                                       |
| `--batch-time-limit`            | Limite de tempo do lote para o serviço de tradução (em segundos)                       | `pdf2zh_next example.pdf --batch-time-limit 60`                                                                       |
| `--batch-concurrency-limit`     | Limite de concorrência do lote para o serviço de tradução                               | `pdf2zh_next example.pdf --batch-concurrency-limit 2`                                                                 |
| `--batch-timeout-limit`         | Limite de tempo limite do lote para o serviço de tradução (em segundos)                | `pdf2zh_next example.pdf --batch-timeout-limit 60`                                                                    |
| `--batch-retry-limit`           | Limite de tentativas do lote para o serviço de tradução                                 | `pdf2zh_next example.pdf --batch-retry-limit 3`                                                                       |
| `--batch-retry-interval-limit`  | Limite de intervalo de repetição do lote para o serviço de tradução (em segundos)      | `pdf2zh_next example.pdf --batch-retry-interval-limit 10`                                                             |
| `--batch-char-limit-limit`      | Limite de limite de caracteres do lote para o serviço de tradução                      | `pdf2zh_next example.pdf --batch-char-limit-limit 10000`                                                              |
| `--batch-page-limit-limit`      | Limite de limite de páginas do lote para o serviço de tradução                         | `pdf2zh_next example.pdf --batch-page-limit-limit 10`                                                                 |
| `--batch-file-limit-limit`      | Limite de limite de arquivos do lote para o serviço de tradução                        | `pdf2zh_next example.pdf --batch-file-limit-limit 10`                                                                 |
| `--batch-size-limit-limit`      | Limite de limite de tamanho do lote para o serviço de tradução (em MB)                 | `pdf2zh_next example.pdf --batch-size-limit-limit 50`                                                                 |
| `--batch-time-limit-limit`      | Limite de limite de tempo do lote para o serviço de tradução (em segundos)            | `pdf2zh_next example.pdf --batch-time-limit-limit 60`                                                                 |
| `--batch-concurrency-limit-limit` | Limite de limite de concorrência do lote para o serviço de tradução                   | `pdf2zh_next example.pdf --batch-concurrency-limit-limit 2`                                                           |
| `--batch-timeout-limit-limit`   | Limite de limite de tempo limite do lote para o serviço de tradução (em segundos)     | `pdf2zh_next example.pdf --batch-timeout-limit-limit 60`                                                              |
| `--batch-retry-limit-limit`     | Limite de limite de tentativas do lote para o serviço de tradução                      | `pdf2zh_next example.pdf --batch-retry-limit-limit 3`                                                                 |
| `--batch-retry-interval-limit-limit` | Limite de limite de intervalo de repetição do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-retry-interval-limit-limit 10`                                                       |
| `--batch-char-limit-limit-limit` | Limite de limite de limite de caracteres do lote para o serviço de tradução          | `pdf2zh_next example.pdf --batch-char-limit-limit-limit 10000`                                                        |
| `--batch-page-limit-limit-limit` | Limite de limite de limite de páginas do lote para o serviço de tradução             | `pdf2zh_next example.pdf --batch-page-limit-limit-limit 10`                                                           |
| `--batch-file-limit-limit-limit` | Limite de limite de limite de arquivos do lote para o serviço de tradução            | `pdf2zh_next example.pdf --batch-file-limit-limit-limit 10`                                                           |
| `--batch-size-limit-limit-limit` | Limite de limite de limite de tamanho do lote para o serviço de tradução (em MB)     | `pdf2zh_next example.pdf --batch-size-limit-limit-limit 50`                                                           |
| `--batch-time-limit-limit-limit` | Limite de limite de limite de tempo do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-time-limit-limit-limit 60`                                                           |
| `--batch-concurrency-limit-limit-limit` | Limite de limite de limite de concorrência do lote para o serviço de tradução     | `pdf2zh_next example.pdf --batch-concurrency-limit-limit-limit 2`                                                     |
| `--batch-timeout-limit-limit-limit` | Limite de limite de limite de tempo limite do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-timeout-limit-limit-limit 60`                                                        |
| `--batch-retry-limit-limit-limit` | Limite de limite de limite de tentativas do lote para o serviço de tradução          | `pdf2zh_next example.pdf --batch-retry-limit-limit-limit 3`                                                           |
| `--batch-retry-interval-limit-limit-limit` | Limite de limite de limite de intervalo de repetição do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-retry-interval-limit-limit-limit 10`                                                |
| `--batch-char-limit-limit-limit-limit` | Limite de limite de limite de limite de caracteres do lote para o serviço de tradução | `pdf2zh_next example.pdf --batch-char-limit-limit-limit-limit 10000`                                                 |
| `--batch-page-limit-limit-limit-limit` | Limite de limite de limite de limite de páginas do lote para o serviço de tradução | `pdf2zh_next example.pdf --batch-page-limit-limit-limit-limit 10`                                                     |
| `--batch-file-limit-limit-limit-limit` | Limite de limite de limite de limite de arquivos do lote para o serviço de tradução | `pdf2zh_next example.pdf --batch-file-limit-limit-limit-limit 10`                                                     |
| `--batch-size-limit-limit-limit-limit` | Limite de limite de limite de limite de tamanho do lote para o serviço de tradução (em MB) | `pdf2zh_next example.pdf --batch-size-limit-limit-limit-limit 50`                                                     |
| `--batch-time-limit-limit-limit-limit` | Limite de limite de limite de limite de tempo do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-time-limit-limit-limit-limit 60`                                                     |
| `--batch-concurrency-limit-limit-limit-limit` | Limite de limite de limite de limite de concorrência do lote para o serviço de tradução | `pdf2zh_next example.pdf --batch-concurrency-limit-limit-limit-limit 2`                                               |
| `--batch-timeout-limit-limit-limit-limit` | Limite de limite de limite de limite de tempo limite do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-timeout-limit-limit-limit-limit 60`                                                 |
| `--batch-retry-limit-limit-limit-limit` | Limite de limite de limite de limite de tentativas do lote para o serviço de tradução | `pdf2zh_next example.pdf --batch-retry-limit-limit-limit-limit 3`                                                     |
| `--batch-retry-interval-limit-limit-limit-limit` | Limite de limite de limite de limite de intervalo de repetição do lote para o serviço de tradução (em segundos) | `pdf2zh_next example.pdf --batch-retry-interval-limit-limit-limit-limit 10`                                          |
---

### TRANSLATED TEXT

| `--ignore-cache`                | Ignorar cache de tradução                                                               | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--custom-system-prompt`        | Prompt de sistema personalizado para tradução. Usado para `/no_think` no Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-fallback`           | Fallback to the next glossary if the current one does not contain the word.             | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-fallback`                              |
| `--glossary-case-sensitive`     | Enable case sensitivity for glossary matching.                                          | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-case-sensitive`                                       |
| `--glossary-full-match`         | Enable full match for glossary matching.                                                | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-full-match`                                           |
| `--glossary-source-lang`        | Source language of the glossary.                                                        | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-source-lang "en"`                                     |
| `--glossary-target-lang`        | Target language of the glossary.                                                        | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-target-lang "zh"`                                     |
| `--glossary-merge`              | Merge the glossary into one and use it for translation.                                 | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-merge`                                 |
| `--glossary-merge-separator`    | Separator for merging glossaries.                                                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-merge --glossary-merge-separator "||"` |

---

### OUTPUT

| `--glossaries`                  | Lista de arquivos de glossário.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-fallback`           | Recurso para o próximo glossário se o atual não contiver a palavra.             | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-fallback`                              |
| `--glossary-case-sensitive`     | Ativar sensibilidade a maiúsculas e minúsculas para correspondência de glossário.                                          | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-case-sensitive`                                       |
| `--glossary-full-match`         | Ativar correspondência completa para correspondência de glossário.                                                | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-full-match`                                           |
| `--glossary-source-lang`        | Idioma de origem do glossário.                                                        | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-source-lang "en"`                                     |
| `--glossary-target-lang`        | Idioma de destino do glossário.                                                        | `pdf2zh_next example.pdf --glossaries "glossary.csv" --glossary-target-lang "zh"`                                     |
| `--glossary-merge`              | Mesclar o glossário em um e usá-lo para tradução.                                 | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-merge`                                 |
| `--glossary-merge-separator`    | Separador para mesclar glossários.                                                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-merge --glossary-merge-separator "||"` |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-glossary`                 | use glossary to translate                                                              | `pdf2zh_next example.pdf --use-glossary`                                                                             |
| `--use-glossary-only`            | use glossary only to translate, and skip other translation services                    | `pdf2zh_next example.pdf --use-glossary-only`                                                                        |
| `--save-glossary`                | save glossary used in translation                                                      | `pdf2zh_next example.pdf --save-glossary`                                                                            |

---

### TRANSLATED TEXT

| `--save-auto-extracted-glossary`| salvar glossário extraído automaticamente                                                | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-glossary`                 | usar glossário para traduzir                                                              | `pdf2zh_next example.pdf --use-glossary`                                                                             |
| `--use-glossary-only`            | usar apenas o glossário para traduzir, e pular outros serviços de tradução                    | `pdf2zh_next example.pdf --use-glossary-only`                                                                        |
| `--save-glossary`                | salvar glossário usado na tradução                                                      | `pdf2zh_next example.pdf --save-glossary`                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-workers-per-service` | Maximum number of workers for each translation service. If not set, will use 10                   | `pdf2zh_next example.pdf --pool-max-workers-per-service 10`                                                |
| `--pool-max-retries`            | Maximum number of retries for translation pool. If not set, will use 3                           | `pdf2zh_next example.pdf --pool-max-retries 3`                                                             |

---

### OUTPUT

| `--pool-max-workers`            | Número máximo de workers para o pool de tradução. Se não for definido, usará o qps como o número de workers | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-workers-per-service` | Número máximo de workers para cada serviço de tradução. Se não for definido, usará 10                       | `pdf2zh_next example.pdf --pool-max-workers-per-service 10`                                                |
| `--pool-max-retries`            | Número máximo de tentativas para o pool de tradução. Se não for definido, usará 3                           | `pdf2zh_next example.pdf --pool-max-retries 3`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--term-requests-per-minute`    | RPM limit for term extraction translation service. If not set, will follow rpm.         | `pdf2zh_next example.pdf --term-requests-per-minute 1000`                                                             |
| `--term-max-requests`           | Maximum number of requests for term extraction translation service. If not set, will follow max-requests. | `pdf2zh_next example.pdf --term-max-requests 100`                                                                     |
| `--term-timeout`                | Timeout for term extraction translation service. If not set, will follow timeout.       | `pdf2zh_next example.pdf --term-timeout 10`                                                                           |
| `--term-model`                  | Model for term extraction translation service. If not set, will follow model.           | `pdf2zh_next example.pdf --term-model gpt-4o-mini`                                                                    |
| `--term-prompt`                 | Prompt for term extraction translation service. If not set, will follow prompt.         | `pdf2zh_next example.pdf --term-prompt "You are a professional translator, please translate the following text."`     |
| `--term-context`                | Context for term extraction translation service. If not set, will follow context.       | `pdf2zh_next example.pdf --term-context "This is a research paper about machine learning."`                           |
| `--term-role`                   | Role for term extraction translation service. If not set, will follow role.             | `pdf2zh_next example.pdf --term-role "You are a professional translator, please translate the following text."`       |
| `--term-system-prompt`          | System prompt for term extraction translation service. If not set, will follow system-prompt. | `pdf2zh_next example.pdf --term-system-prompt "You are a professional translator, please translate the following text."` |
| `--term-temperature`            | Temperature for term extraction translation service. If not set, will follow temperature. | `pdf2zh_next example.pdf --term-temperature 0.7`                                                                      |
| `--term-top-p`                  | Top-p for term extraction translation service. If not set, will follow top-p.           | `pdf2zh_next example.pdf --term-top-p 0.9`                                                                            |
| `--term-frequency-penalty`      | Frequency penalty for term extraction translation service. If not set, will follow frequency-penalty. | `pdf2zh_next example.pdf --term-frequency-penalty 0.5`                                                                |
| `--term-presence-penalty`       | Presence penalty for term extraction translation service. If not set, will follow presence-penalty. | `pdf2zh_next example.pdf --term-presence-penalty 0.5`                                                                 |
| `--term-stop`                   | Stop sequence for term extraction translation service. If not set, will follow stop.    | `pdf2zh_next example.pdf --term-stop "STOP"`                                                                          |

---

### OUTPUT

| `--term-qps`                    | Limite de QPS para o serviço de tradução de extração de termos. Se não for definido, seguirá o qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--term-requests-per-minute`    | Limite de RPM para o serviço de tradução de extração de termos. Se não for definido, seguirá o rpm.         | `pdf2zh_next example.pdf --term-requests-per-minute 1000`                                                             |
| `--term-max-requests`           | Número máximo de solicitações para o serviço de tradução de extração de termos. Se não for definido, seguirá max-requests. | `pdf2zh_next example.pdf --term-max-requests 100`                                                                     |
| `--term-timeout`                | Tempo limite para o serviço de tradução de extração de termos. Se não for definido, seguirá timeout.       | `pdf2zh_next example.pdf --term-timeout 10`                                                                           |
| `--term-model`                  | Modelo para o serviço de tradução de extração de termos. Se não for definido, seguirá model.           | `pdf2zh_next example.pdf --term-model gpt-4o-mini`                                                                    |
| `--term-prompt`                 | Prompt para o serviço de tradução de extração de termos. Se não for definido, seguirá prompt.         | `pdf2zh_next example.pdf --term-prompt "Você é um tradutor profissional, por favor, traduza o seguinte texto."`     |
| `--term-context`                | Contexto para o serviço de tradução de extração de termos. Se não for definido, seguirá context.       | `pdf2zh_next example.pdf --term-context "Este é um artigo de pesquisa sobre aprendizado de máquina."`                           |
| `--term-role`                   | Função para o serviço de tradução de extração de termos. Se não for definido, seguirá role.             | `pdf2zh_next example.pdf --term-role "Você é um tradutor profissional, por favor, traduza o seguinte texto."`       |
| `--term-system-prompt`          | Prompt de sistema para o serviço de tradução de extração de termos. Se não for definido, seguirá system-prompt. | `pdf2zh_next example.pdf --term-system-prompt "Você é um tradutor profissional, por favor, traduza o seguinte texto."` |
| `--term-temperature`            | Temperatura para o serviço de tradução de extração de termos. Se não for definido, seguirá temperature. | `pdf2zh_next example.pdf --term-temperature 0.7`                                                                      |
| `--term-top-p`                  | Top-p para o serviço de tradução de extração de termos. Se não for definido, seguirá top-p.           | `pdf2zh_next example.pdf --term-top-p 0.9`                                                                            |
| `--term-frequency-penalty`      | Penalidade de frequência para o serviço de tradução de extração de termos. Se não for definido, seguirá frequency-penalty. | `pdf2zh_next example.pdf --term-frequency-penalty 0.5`                                                                |
| `--term-presence-penalty`       | Penalidade de presença para o serviço de tradução de extração de termos. Se não for definido, seguirá presence-penalty. | `pdf2zh_next example.pdf --term-presence-penalty 0.5`                                                                 |
| `--term-stop`                   | Sequência de parada para o serviço de tradução de extração de termos. Se não for definido, seguirá stop.    | `pdf2zh_next example.pdf --term-stop "STOP"`                                                                          |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `--term-pool-max-workers`       | Número máximo de workers para o pool de tradução de extração de termos. Se não definido ou 0, seguirá pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |

---

### OUTPUT

| `--term-pool-max-workers`       | Número máximo de workers para o pool de tradução de extração de termos. Se não definido ou 0, seguirá pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `--term-pool-max-workers`       | Número máximo de workers para o pool de tradução de extração de termos. Se não definido ou 0, seguirá pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-file`               | Path to glossary file                                                                   | `pdf2zh_next example.pdf --glossary-file glossary.txt`                                                                |
| `--glossary`                    | Glossary content                                                                        | `pdf2zh_next example.pdf --glossary "PDF=PDF\nMath=Matemática"`                                                       |
| `--no-auto-extract-translation` | Disable auto extract translation                                                        | `pdf2zh_next example.pdf --no-auto-extract-translation`                                                               |
| `--translation-file`            | Path to translation file                                                                | `pdf2zh_next example.pdf --translation-file translation.txt`                                                          |
| `--translation`                 | Translation content                                                                     | `pdf2zh_next example.pdf --translation "Hello=Olá\nWorld=Mundo"`                                                      |
| `--no-auto-extract-prompt`      | Disable auto extract prompt                                                             | `pdf2zh_next example.pdf --no-auto-extract-prompt`                                                                    |
| `--prompt-file`                 | Path to prompt file                                                                     | `pdf2zh_next example.pdf --prompt-file prompt.txt`                                                                    |
| `--prompt`                      | Prompt content                                                                          | `pdf2zh_next example.pdf --prompt "Translate the following text from English to Portuguese."`                         |
| `--no-auto-extract-style`       | Disable auto extract style                                                              | `pdf2zh_next example.pdf --no-auto-extract-style`                                                                     |
| `--style-file`                  | Path to style file                                                                      | `pdf2zh_next example.pdf --style-file style.txt`                                                                      |
| `--style`                       | Style content                                                                           | `pdf2zh_next example.pdf --style "Translate the following text from English to Portuguese, keep the original style."` |
| `--no-auto-extract-ignore`      | Disable auto extract ignore                                                             | `pdf2zh_next example.pdf --no-auto-extract-ignore`                                                                    |
| `--ignore-file`                 | Path to ignore file                                                                     | `pdf2zh_next example.pdf --ignore-file ignore.txt`                                                                    |
| `--ignore`                      | Ignore content                                                                          | `pdf2zh_next example.pdf --ignore "ignore this text"`                                                                 |
| `--no-auto-extract-replace`     | Disable auto extract replace                                                            | `pdf2zh_next example.pdf --no-auto-extract-replace`                                                                   |
| `--replace-file`                | Path to replace file                                                                    | `pdf2zh_next example.pdf --replace-file replace.txt`                                                                  |
| `--replace`                     | Replace content                                                                         | `pdf2zh_next example.pdf --replace "replace this text with that text"`                                                |
| `--no-auto-extract-regex`       | Disable auto extract regex                                                              | `pdf2zh_next example.pdf --no-auto-extract-regex`                                                                     |
| `--regex-file`                  | Path to regex file                                                                      | `pdf2zh_next example.pdf --regex-file regex.txt`                                                                      |
| `--regex`                       | Regex content                                                                           | `pdf2zh_next example.pdf --regex "regex pattern"`                                                                     |
| `--no-auto-extract-regex-replace` | Disable auto extract regex replace                                                    | `pdf2zh_next example.pdf --no-auto-extract-regex-replace`                                                             |
| `--regex-replace-file`          | Path to regex replace file                                                              | `pdf2zh_next example.pdf --regex-replace-file regex-replace.txt`                                                      |
| `--regex-replace`               | Regex replace content                                                                   | `pdf2zh_next example.pdf --regex-replace "regex pattern"`                                                             |
| `--no-auto-extract-regex-ignore` | Disable auto extract regex ignore                                                     | `pdf2zh_next example.pdf --no-auto-extract-regex-ignore`                                                              |
| `--regex-ignore-file`           | Path to regex ignore file                                                               | `pdf2zh_next example.pdf --regex-ignore-file regex-ignore.txt`                                                        |
| `--regex-ignore`                | Regex ignore content                                                                    | `pdf2zh_next example.pdf --regex-ignore "regex pattern"`                                                              |
| `--no-auto-extract-regex-replace-ignore` | Disable auto extract regex replace ignore                                       | `pdf2zh_next example.pdf --no-auto-extract-regex-replace-ignore`                                                      |
| `--regex-replace-ignore-file`   | Path to regex replace ignore file                                                       | `pdf2zh_next example.pdf --regex-replace-ignore-file regex-replace-ignore.txt`                                        |
| `--regex-replace-ignore`        | Regex replace ignore content                                                            | `pdf2zh_next example.pdf --regex-replace-ignore "regex pattern"`                                                      |
| `--no-auto-extract-regex-replace-ignore-file` | Disable auto extract regex replace ignore file                                 | `pdf2zh_next example.pdf --no-auto-extract-regex-replace-ignore-file`                                                 |
| `--regex-replace-ignore-file-file` | Path to regex replace ignore file file                                               | `pdf2zh_next example.pdf --regex-replace-ignore-file-file regex-replace-ignore-file.txt`                              |
| `--regex-replace-ignore-file`   | Regex replace ignore file content                                                       | `pdf2zh_next example.pdf --regex-replace-ignore-file "regex pattern"`                                                 |

---

### TRANSLATION

| `--no-auto-extract-glossary`    | Desativar extração automática do glossário                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-file`               | Caminho para o arquivo de glossário                                                     | `pdf2zh_next example.pdf --glossary-file glossary.txt`                                                                |
| `--glossary`                    | Conteúdo do glossário                                                                   | `pdf2zh_next example.pdf --glossary "PDF=PDF\nMath=Matemática"`                                                       |
| `--no-auto-extract-translation` | Desativar extração automática da tradução                                               | `pdf2zh_next example.pdf --no-auto-extract-translation`                                                               |
| `--translation-file`            | Caminho para o arquivo de tradução                                                      | `pdf2zh_next example.pdf --translation-file translation.txt`                                                          |
| `--translation`                 | Conteúdo da tradução                                                                    | `pdf2zh_next example.pdf --translation "Hello=Olá\nWorld=Mundo"`                                                      |
| `--no-auto-extract-prompt`      | Desativar extração automática do prompt                                                 | `pdf2zh_next example.pdf --no-auto-extract-prompt`                                                                    |
| `--prompt-file`                 | Caminho para o arquivo de prompt                                                        | `pdf2zh_next example.pdf --prompt-file prompt.txt`                                                                    |
| `--prompt`                      | Conteúdo do prompt                                                                      | `pdf2zh_next example.pdf --prompt "Translate the following text from English to Portuguese."`                         |
| `--no-auto-extract-style`       | Desativar extração automática do estilo                                                 | `pdf2zh_next example.pdf --no-auto-extract-style`                                                                     |
| `--style-file`                  | Caminho para o arquivo de estilo                                                        | `pdf2zh_next example.pdf --style-file style.txt`                                                                      |
| `--style`                       | Conteúdo do estilo                                                                      | `pdf2zh_next example.pdf --style "Translate the following text from English to Portuguese, keep the original style."` |
| `--no-auto-extract-ignore`      | Desativar extração automática de ignorar                                                | `pdf2zh_next example.pdf --no-auto-extract-ignore`                                                                    |
| `--ignore-file`                 | Caminho para o arquivo de ignorar                                                       | `pdf2zh_next example.pdf --ignore-file ignore.txt`                                                                    |
| `--ignore`                      | Conteúdo a ignorar                                                                      | `pdf2zh_next example.pdf --ignore "ignore this text"`                                                                 |
| `--no-auto-extract-replace`     | Desativar extração automática de substituir                                             | `pdf2zh_next example.pdf --no-auto-extract-replace`                                                                   |
| `--replace-file`                | Caminho para o arquivo de substituir                                                    | `pdf2zh_next example.pdf --replace-file replace.txt`                                                                  |
| `--replace`                     | Conteúdo de substituição                                                                | `pdf2zh_next example.pdf --replace "replace this text with that text"`                                                |
| `--no-auto-extract-regex`       | Desativar extração automática de regex                                                  | `pdf2zh_next example.pdf --no-auto-extract-regex`                                                                     |
| `--regex-file`                  | Caminho para o arquivo de regex                                                         | `pdf2zh_next example.pdf --regex-file regex.txt`                                                                      |
| `--regex`                       | Conteúdo regex                                                                          | `pdf2zh_next example.pdf --regex "regex pattern"`                                                                     |
| `--no-auto-extract-regex-replace` | Desativar extração automática de substituição por regex                               | `pdf2zh_next example.pdf --no-auto-extract-regex-replace`                                                             |
| `--regex-replace-file`          | Caminho para o arquivo de substituição por regex                                        | `pdf2zh_next example.pdf --regex-replace-file regex-replace.txt`                                                      |
| `--regex-replace`               | Conteúdo de substituição por regex                                                      | `pdf2zh_next example.pdf --regex-replace "regex pattern"`                                                             |
| `--no-auto-extract-regex-ignore` | Desativar extração automática de ignorar por regex                                    | `pdf2zh_next example.pdf --no-auto-extract-regex-ignore`                                                              |
| `--regex-ignore-file`           | Caminho para o arquivo de ignorar por regex                                             | `pdf2zh_next example.pdf --regex-ignore-file regex-ignore.txt`                                                        |
| `--regex-ignore`                | Conteúdo de ignorar por regex                                                           | `pdf2zh_next example.pdf --regex-ignore "regex pattern"`                                                              |
| `--no-auto-extract-regex-replace-ignore` | Desativar extração automática de substituição e ignorar por regex               | `pdf2zh_next example.pdf --no-auto-extract-regex-replace-ignore`                                                      |
| `--regex-replace-ignore-file`   | Caminho para o arquivo de substituição e ignorar por regex                              | `pdf2zh_next example.pdf --regex-replace-ignore-file regex-replace-ignore.txt`                                        |
| `--regex-replace-ignore`        | Conteúdo de substituição e ignorar por regex                                            | `pdf2zh_next example.pdf --regex-replace-ignore "regex pattern"`                                                      |
| `--no-auto-extract-regex-replace-ignore-file` | Desativar extração automática do arquivo de substituição e ignorar por regex     | `pdf2zh_next example.pdf --no-auto-extract-regex-replace-ignore-file`                                                 |
| `--regex-replace-ignore-file-file` | Caminho para o arquivo do arquivo de substituição e ignorar por regex               | `pdf2zh_next example.pdf --regex-replace-ignore-file-file regex-replace-ignore-file.txt`                              |
| `--regex-replace-ignore-file`   | Conteúdo do arquivo de substituição e ignorar por regex                                 | `pdf2zh_next example.pdf --regex-replace-ignore-file "regex pattern"`                                                 |
---

### OUTPUT

| `--primary-font-family`         | Substitui a família de fontes primária para o texto traduzido. Opções: 'serif' para fontes serifadas, 'sans-serif' para fontes sem serifas, 'script' para fontes de script/itálicas. Se não especificado, utiliza a seleção automática de fontes baseada nas propriedades do texto original. | `pdf2zh_next example.pdf --primary-font-family serif` |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--no-dual`                     | Não gera arquivos PDF bilíngues                                                         | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--output-dir <output_dir>`     | Specify the output directory for the translated files                                   | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-dir <output_dir>`     | Especifica o diretório de saída para os arquivos traduzidos                             | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <output_name>`   | Specify the output file name for the translated files                                   | `pdf2zh_next example.pdf --output-name translated.pdf`                                                                |
| `--output-name <output_name>`   | Especifica o nome do arquivo de saída para os arquivos traduzidos                       | `pdf2zh_next example.pdf --output-name translated.pdf`                                                                |
| `--single-column`               | Force single-column layout for the translated PDF                                       | `pdf2zh_next example.pdf --single-column`                                                                             |
| `--single-column`               | Força o layout de coluna única para o PDF traduzido                                     | `pdf2zh_next example.pdf --single-column`                                                                             |
| `--target-lang <target_lang>`   | Specify the target language for translation (default: `zh`)                             | `pdf2zh_next example.pdf --target-lang en`                                                                            |
| `--target-lang <target_lang>`   | Especifica o idioma de destino para a tradução (padrão: `zh`)                           | `pdf2zh_next example.pdf --target-lang en`                                                                            |
| `--translation-service <service>` | Specify the translation service to use (default: `google`)                              | `pdf2zh_next example.pdf --translation-service deepl`                                                                 |
| `--translation-service <service>` | Especifica o serviço de tradução a ser utilizado (padrão: `google`)                     | `pdf2zh_next example.pdf --translation-service deepl`                                                                 |
| `--skip-translated`             | Skip pages that have already been translated (based on the output file)                 | `pdf2zh_next example.pdf --skip-translated`                                                                           |
| `--skip-translated`             | Pula páginas que já foram traduzidas (com base no arquivo de saída)                     | `pdf2zh_next example.pdf --skip-translated`                                                                           |
| `-v`, `--version`               | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `-v`, `--version`               | Mostra informações da versão                                                            | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |
| `-h`, `--help`                  | Mostra a mensagem de ajuda                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--no-dual`                     | Não gera arquivos PDF bilíngues                                                         | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--output-dir <output_dir>`     | Especifica o diretório de saída para os arquivos traduzidos                             | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <output_name>`   | Especifica o nome do arquivo de saída para os arquivos traduzidos                       | `pdf2zh_next example.pdf --output-name translated.pdf`                                                                |
| `--single-column`               | Força o layout de coluna única para o PDF traduzido                                     | `pdf2zh_next example.pdf --single-column`                                                                             |
| `--target-lang <target_lang>`   | Especifica o idioma de destino para a tradução (padrão: `zh`)                           | `pdf2zh_next example.pdf --target-lang en`                                                                            |
| `--translation-service <service>` | Especifica o serviço de tradução a ser utilizado (padrão: `google`)                     | `pdf2zh_next example.pdf --translation-service deepl`                                                                 |
| `--skip-translated`             | Pula páginas que já foram traduzidas (com base no arquivo de saída)                     | `pdf2zh_next example.pdf --skip-translated`                                                                           |
| `-v`, `--version`               | Mostra informações da versão                                                            | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Mostra a mensagem de ajuda                                                              | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-f`, `--force`                 | Force overwrite existing files                                                          | `pdf2zh_next example.pdf -f`                                                                                          |
| `-r`, `--reuse`                 | Reuse existing translated files                                                          | `pdf2zh_next example.pdf -r`                                                                                          |
| `-l`, `--language`              | Target language, default is `zh`                                                         | `pdf2zh_next example.pdf -l en`                                                                                       |
| `-s`, `--service`               | Translation service, default is `google`                                                 | `pdf2zh_next example.pdf -s deepl`                                                                                    |
| `-c`, `--concurrency`           | Max concurrency, default is `4`                                                          | `pdf2zh_next example.pdf -c 8`                                                                                        |
| `-d`, `--delay`                 | Delay between requests in seconds, default is `0.1`                                      | `pdf2zh_next example.pdf -d 0.5`                                                                                      |
| `-p`, `--proxy`                 | Proxy URL, e.g. `http://127.0.0.1:7890`                                                  | `pdf2zh_next example.pdf -p http://127.0.0.1:7890`                                                                    |
| `--api-key`                     | API key for the translation service                                                      | `pdf2zh_next example.pdf --api-key your_api_key`                                                                      |
| `--custom-endpoint`             | Custom endpoint for the translation service                                              | `pdf2zh_next example.pdf --custom-endpoint https://your-custom-endpoint.com`                                          |
| `--custom-model`                | Custom model for the translation service, e.g. `gpt-4`                                   | `pdf2zh_next example.pdf --custom-model gpt-4`                                                                        |
| `--custom-role`                 | Custom role for the translation service, e.g. `You are a helpful assistant`               | `pdf2zh_next example.pdf --custom-role "You are a helpful assistant"`                                                  |
| `--custom-template`             | Custom template for the translation service, e.g. `Translate the following text: {text}` | `pdf2zh_next example.pdf --custom-template "Translate the following text: {text}"`                                    |
| `--custom-parameters`           | Custom parameters for the translation service, e.g. `{"temperature": 0.7}`                | `pdf2zh_next example.pdf --custom-parameters '{"temperature": 0.7}'`                                                  |
| `--custom-request-parameters`   | Custom request parameters for the translation service, e.g. `{"headers": {"Authorization": "Bearer ..."}}` | `pdf2zh_next example.pdf --custom-request-parameters '{"headers": {"Authorization": "Bearer ..."}}'`                   |

---

### OUTPUT

| `--no-mono`                     | Não produzir ficheiros PDF monolingues                                                  | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-f`, `--force`                 | Forçar a sobrescrever ficheiros existentes                                              | `pdf2zh_next example.pdf -f`                                                                                          |
| `-r`, `--reuse`                 | Reutilizar ficheiros traduzidos existentes                                              | `pdf2zh_next example.pdf -r`                                                                                          |
| `-l`, `--language`              | Idioma de destino, o padrão é `zh`                                                      | `pdf2zh_next example.pdf -l en`                                                                                       |
| `-s`, `--service`               | Serviço de tradução, o padrão é `google`                                                | `pdf2zh_next example.pdf -s deepl`                                                                                    |
| `-c`, `--concurrency`           | Concorrência máxima, o padrão é `4`                                                      | `pdf2zh_next example.pdf -c 8`                                                                                        |
| `-d`, `--delay`                 | Atraso entre pedidos em segundos, o padrão é `0.1`                                       | `pdf2zh_next example.pdf -d 0.5`                                                                                      |
| `-p`, `--proxy`                 | URL do proxy, por exemplo `http://127.0.0.1:7890`                                       | `pdf2zh_next example.pdf -p http://127.0.0.1:7890`                                                                   |
| `--api-key`                     | Chave de API para o serviço de tradução                                                 | `pdf2zh_next example.pdf --api-key your_api_key`                                                                      |
| `--custom-endpoint`             | Endpoint personalizado para o serviço de tradução                                       | `pdf2zh_next example.pdf --custom-endpoint https://your-custom-endpoint.com`                                          |
| `--custom-model`                | Modelo personalizado para o serviço de tradução, por exemplo `gpt-4`                    | `pdf2zh_next example.pdf --custom-model gpt-4`                                                                       |
| `--custom-role`                 | Função personalizada para o serviço de tradução, por exemplo `You are a helpful assistant` | `pdf2zh_next example.pdf --custom-role "You are a helpful assistant"`                                               |
| `--custom-template`             | Modelo personalizado para o serviço de tradução, por exemplo `Translate the following text: {text}` | `pdf2zh_next example.pdf --custom-template "Translate the following text: {text}"`                               |
| `--custom-parameters`           | Parâmetros personalizados para o serviço de tradução, por exemplo `{"temperature": 0.7}` | `pdf2zh_next example.pdf --custom-parameters '{"temperature": 0.7}'`                                                |
| `--custom-request-parameters`   | Parâmetros de pedido personalizados para o serviço de tradução, por exemplo `{"headers": {"Authorization": "Bearer ..."}}` | `pdf2zh_next example.pdf --custom-request-parameters '{"headers": {"Authorization": "Bearer ..."}}'`            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--formular-replace-font`       | Font to replace formula text                                                            | `pdf2zh_next example.pdf --formular-replace-font "Times New Roman"`                                                    |
| `--formular-replace-font-size`  | Font size to replace formula text                                                       | `pdf2zh_next example.pdf --formular-replace-font-size 12`                                                              |
| `--formular-replace-font-color` | Font color to replace formula text                                                      | `pdf2zh_next example.pdf --formular-replace-font-color "#000000"`                                                      |
| `--formular-replace-font-bold`  | Whether to bold formula text                                                            | `pdf2zh_next example.pdf --formular-replace-font-bold`                                                                 |

---

### TRANSLATION RESULT

| `--formular-font-pattern`       | Padrão de fonte para identificar texto de fórmula                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--formular-replace-font`       | Fonte para substituir o texto de fórmula                                                            | `pdf2zh_next example.pdf --formular-replace-font "Times New Roman"`                                                    |
| `--formular-replace-font-size`  | Tamanho da fonte para substituir o texto de fórmula                                                       | `pdf2zh_next example.pdf --formular-replace-font-size 12`                                                              |
| `--formular-replace-font-color` | Cor da fonte para substituir o texto de fórmula                                                      | `pdf2zh_next example.pdf --formular-replace-font-color "#000000"`                                                      |
| `--formular-replace-font-bold`  | Se deve colocar o texto de fórmula em negrito                                                            | `pdf2zh_next example.pdf --formular-replace-font-bold`                                                                 |
- |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | - |
| `--formular-char-pattern-regex` | Whether to treat the character pattern as a regex                                      | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-regex`                              | - |
| `--formular-char-replace`       | Replacement string for the matched formula text                                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "formula"`                          | - |
| `--formular-char-replace-all`   | Replace all occurrences of the pattern in the matched text (default is to replace once) | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "formula" --formular-char-replace-all` | - |

---

### OUTPUT LANGUAGE

pt

---
| `--formular-char-pattern`       | Padrão de caracteres para identificar texto de fórmula                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            | - |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | - |
| `--formular-char-pattern-regex` | Se deve tratar o padrão de caracteres como uma expressão regular                                    | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-regex`                              | - |
| `--formular-char-replace`       | String de substituição para o texto de fórmula correspondente                                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "formula"`                          | - |
| `--formular-char-replace-all`   | Substituir todas as ocorrências do padrão no texto correspondente (o padrão é substituir uma vez) | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-replace "formula" --formular-char-replace-all` | - |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | The threshold to determine if a line is short, default is 0.3                           | `pdf2zh_next example.pdf --split-short-lines-threshold 0.5`                                                           |
| `--split-short-lines-max-len`   | The max length of a short line, default is 10                                           | `pdf2zh_next example.pdf --split-short-lines-max-len 20`                                                              |
| `--remove-short-lines`          | Remove short lines                                                                      | `pdf2zh_next example.pdf --remove-short-lines`                                                                        |
| `--remove-short-lines-threshold`| The threshold to determine if a line is short, default is 0.3                           | `pdf2zh_next example.pdf --remove-short-lines-threshold 0.5`                                                          |
| `--remove-short-lines-max-len`  | The max length of a short line, default is 10                                           | `pdf2zh_next example.pdf --remove-short-lines-max-len 20`                                                             |

---

### TRANSLATION RESULT

| `--split-short-lines`           | Forçar a divisão de linhas curtas em parágrafos diferentes                              | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | O limite para determinar se uma linha é curta, o padrão é 0.3                           | `pdf2zh_next example.pdf --split-short-lines-threshold 0.5`                                                           |
| `--split-short-lines-max-len`   | O comprimento máximo de uma linha curta, o padrão é 10                                  | `pdf2zh_next example.pdf --split-short-lines-max-len 20`                                                              |
| `--remove-short-lines`          | Remover linhas curtas                                                                   | `pdf2zh_next example.pdf --remove-short-lines`                                                                        |
| `--remove-short-lines-threshold`| O limite para determinar se uma linha é curta, o padrão é 0.3                           | `pdf2zh_next example.pdf --remove-short-lines-threshold 0.5`                                                          |
| `--remove-short-lines-max-len`  | O comprimento máximo de uma linha curta, o padrão é 10                                  | `pdf2zh_next example.pdf --remove-short-lines-max-len 20`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--short-line-split-factor-opt` | `short-line-split-factor` optimization factor for short lines (default: `0.8`)          | `pdf2zh_next example.pdf --short-line-split-factor-opt 0.9`                                                            |
| `--short-line-split-factor-ocr` | `short-line-split-factor` for OCR results (default: `1.0`)                              | `pdf2zh_next example.pdf --short-line-split-factor-ocr 1.2`                                                            |
| `--short-line-split-factor-opt-ocr` | `short-line-split-factor-opt` for OCR results (default: `0.8`)                          | `pdf2zh_next example.pdf --short-line-split-factor-opt-ocr 0.9`                                                        |
| `--short-line-split-factor-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt 0.9`                                                        |
| `--short-line-split-factor-ocr-opt-ocr` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr 0.9`                                                    |
| `--short-line-split-factor-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt 0.9`                                                |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr 0.9`                                            |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt 0.9`                                        |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`                                    |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`                                |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`                            |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`                        |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`                    |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`                |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`            |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`        |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Alias for `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9` |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Alias for `--short-line 极长文本-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9` |

---

### TRANSLATED TEXT

| `--short-line-split-factor`     | Fator de limite de divisão para linhas curtas                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--short-line-split-factor-opt` | Fator de otimização `short-line-split-factor` para linhas curtas (padrão: `0.8`)          | `pdf2zh_next example.pdf --short-line-split-factor-opt 0.9`                                                            |
| `--short-line-split-factor-ocr` | `short-line-split-factor` para resultados de OCR (padrão: `1.0`)                              | `pdf2zh_next example.pdf --short-line-split-factor-ocr 1.2`                                                            |
| `--short-line-split-factor-opt-ocr` | `short-line-split-factor-opt` para resultados de OCR (padrão: `0.8`)                          | `pdf2zh_next example.pdf --short-line-s 极长文本 plit-factor-opt-ocr 0.9`                                                        |
| `--short-line-split-factor-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt 0.9`                                                        |
| `--short-line-split-factor-ocr-opt-ocr` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr 0.9`                                                    |
| `--short-line-split-factor-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt 极长文本 0.9`                                                |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr 0.9`                                            |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt 0.9`                                        |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`                                    |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`                                |
| `--short-line-split-factor-ocr-opt-ocr-极长文本 opt-ocr-opt-ocr-opt-ocr` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`                            |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`                        |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`                    |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`                |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf 极长文本 2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-极长文本 opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9`            |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9`        |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt` | Apelido para `--short-line-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt 0.9` |
| `--short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr` | Apelido para `--short-line 极长文本-split-factor-opt-ocr`                                           | `pdf2zh_next example.pdf --short-line-split-factor-ocr-opt-ocr-opt-ocr-opt-ocr-极长文本-ocr-opt-ocr-opt-ocr-opt-ocr-opt-ocr 0.9` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--skip-layout`                 | Skip layout analysis step                                                               | `pdf2zh_next example.pdf --skip-layout`                                                                               |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | Skip OCR step (only for scanned PDFs)                                                   | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-export`                 | Skip export step                                                                        | `pdf2zh_next example.pdf --skip-export`                                                                               |
| `--skip-split`                  | Skip splitting step                                                                     | `pdf2zh_next example.pdf --skip-split`                                                                                |
| `--skip-merge`                  | Skip merging step                                                                       | `pdf2zh_next example.pdf --skip-merge`                                                                                |
| `--skip-all`                    | Skip all steps except the one you specify                                               | `pdf2zh_next example.pdf --skip-all --only-export`                                                                    |
| `--only-clean`                  | Only perform PDF cleaning step                                                          | `pdf2zh_next example.pdf --only-clean`                                                                                |
| `--only-layout`                 | Only perform layout analysis step                                                       | `pdf2zh_next example.pdf --only-layout`                                                                               |
| `--only-translate`              | Only perform translation step                                                           | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--only-ocr`                    | Only perform OCR step (only for scanned PDFs)                                           | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-export`                 | Only perform export step                                                                | `pdf2zh_next example.pdf --only-export`                                                                               |
| `--only-split`                  | Only perform splitting step                                                             | `pdf2zh_next example.pdf --only-split`                                                                                |
| `--only-merge`                  | Only perform merging step                                                               | `pdf2zh_next example.pdf --only-merge`                                                                                |

---

### TRANSLATED TEXT

| `--skip-clean`                  | Pular etapa de limpeza do PDF                                                           | `pdf2zh_next example.pdf --skip-clean`                                                                                |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--skip-layout`                 | Pular etapa de análise de layout                                                        | `pdf2zh_next example.pdf --skip-layout`                                                                               |
| `--skip-translate`              | Pular etapa de tradução                                                                 | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | Pular etapa de OCR (apenas para PDFs digitalizados)                                     | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-export`                 | Pular etapa de exportação                                                               | `pdf2zh_next example.pdf --skip-export`                                                                               |
| `--skip-split`                  | Pular etapa de divisão                                                                  | `pdf2zh_next example.pdf --skip-split`                                                                                |
| `--skip-merge`                  | Pular etapa de mesclagem                                                                | `pdf2zh_next example.pdf --skip-merge`                                                                                |
| `--skip-all`                    | Pular todas as etapas, exceto a que você especificar                                    | `pdf2zh_next example.pdf --skip-all --only-export`                                                                    |
| `--only-clean`                  | Apenas executar a etapa de limpeza do PDF                                               | `pdf2zh_next example.pdf --only-clean`                                                                                |
| `--only-layout`                 | Apenas executar a etapa de análise de layout                                            | `pdf2zh_next example.pdf --only-layout`                                                                               |
| `--only-translate`              | Apenas executar a etapa de tradução                                                     | `pdf2zh_next example.pdf --only-translate`                                                                            |
| `--only-ocr`                    | Apenas executar a etapa de OCR (apenas para PDFs digitalizados)                         | `pdf2zh_next example.pdf --only-ocr`                                                                                  |
| `--only-export`                 | Apenas executar a etapa de exportação                                                   | `pdf2zh_next example.pdf --only-export`                                                                               |
| `--only-split`                  | Apenas executar a etapa de divisão                                                      | `pdf2zh_next example.pdf --only-split`                                                                                |
| `--only-merge`                  | Apenas executar a etapa de mesclagem                                                    | `pdf2zh_next example.pdf --only-merge`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-first-custom` | Put translated pages first in dual PDF mode, with custom text                          | `pdf2zh_next example.pdf --dual-translate-first-custom "Custom Text"`                                                  |

---

### TRANSLATION RESULT

| `--dual-translate-first`        | Colocar páginas traduzidas primeiro no modo PDF duplo                                   | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-first-custom` | Colocar páginas traduzidas primeiro no modo PDF duplo, com texto personalizado          | `pdf2zh_next example.pdf --dual-translate-first-custom "Custom Text"`                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-latex-translate`     | Disable LaTeX translation                                                               | `pdf2zh_next example.pdf --disable-latex-translate`                                                                   |
| `--disable-formula-translate`   | Disable formula translation                                                             | `pdf2zh_next example.pdf --disable-formula-translate`                                                                 |
| `--disable-table-translate`     | Disable table translation                                                               | `pdf2zh_next example.pdf --disable-table-translate`                                                                   |
| `--disable-figure-translate`    | Disable figure translation                                                              | `pdf2zh_next example.pdf --disable-figure-translate`                                                                  |
| `--disable-algorithm-translate` | Disable algorithm translation                                                           | `pdf2zh_next example.pdf --disable-algorithm-translate`                                                               |
| `--disable-list-translate`      | Disable list translation                                                                | `pdf2zh_next example.pdf --disable-list-translate`                                                                    |
| `--disable-code-translate`      | Disable code translation                                                                | `pdf2zh_next example.pdf --disable-code-translate`                                                                    |
| `--disable-quote-translate`     | Disable quote translation                                                               | `pdf2zh_next example.pdf --disable-quote-translate`                                                                   |
| `--disable-reference-translate` | Disable reference translation                                                           | `pdf2zh_next example.pdf --disable-reference-translate`                                                               |
| `--disable-citation-translate`  | Disable citation translation                                                            | `pdf2zh_next example.pdf --disable-citation-translate`                                                                |
| `--disable-footnote-translate`  | Disable footnote translation                                                            | `pdf2zh_next example.pdf --disable-footnote-translate`                                                                |
| `--disable-header-translate`    | Disable header translation                                                              | `pdf2zh_next example.pdf --disable-header-translate`                                                                  |
| `--disable-footer-translate`    | Disable footer translation                                                              | `pdf2zh_next example.pdf --disable-footer-translate`                                                                  |
| `--disable-note-translate`      | Disable note translation                                                                | `pdf2zh_next example.pdf --disable-note-translate`                                                                    |
| `--disable-proof-translate`     | Disable proof translation                                                               | `pdf2zh_next example.pdf --disable-proof-translate`                                                                   |
| `--disable-example-translate`   | Disable example translation                                                             | `pdf2zh_next example.pdf --disable-example-translate`                                                                 |
| `--disable-definition-translate`| Disable definition translation                                                          | `pdf2zh_next example.pdf --disable-definition-translate`                                                              |
| `--disable-theorem-translate`   | Disable theorem translation                                                             | `pdf2zh_next example.pdf --disable-theorem-translate`                                                                 |
| `--disable-corollary-translate` | Disable corollary translation                                                           | `pdf2zh_next example.pdf --disable-corollary-translate`                                                               |
| `--disable-lemma-translate`     | Disable lemma translation                                                               | `pdf2zh_next example.pdf --disable-lemma-translate`                                                                   |
| `--disable-proposition-translate`| Disable proposition translation                                                         | `pdf2zh_next example.pdf --disable-proposition-translate`                                                             |
| `--disable-remark-translate`    | Disable remark translation                                                              | `pdf2zh_next example.pdf --disable-remark-translate`                                                                  |
| `--disable-assumption-translate`| Disable assumption translation                                                          | `pdf2zh_next example.pdf --disable-assumption-translate`                                                              |
| `--disable-conjecture-translate`| Disable conjecture translation                                                          | `pdf2zh_next example.pdf --disable-conjecture-translate`                                                              |
| `--disable-axiom-translate`     | Disable axiom translation                                                               | `pdf2zh_next example.pdf --disable-axiom-translate`                                                                   |
| `--disable-property-translate`  | Disable property translation                                                            | `pdf2zh_next example.pdf --disable-property-translate`                                                                |
| `--disable-exercise-translate`  | Disable exercise translation                                                            | `pdf2zh_next example.pdf --disable-exercise-translate`                                                                |
| `--disable-solution-translate`  | Disable solution translation                                                            | `pdf2zh_next example.pdf --disable-solution-translate`                                                                |
| `--disable-problem-translate`   | Disable problem translation                                                             | `pdf2zh_next example.pdf --disable-problem-translate`                                                                 |
| `--disable-question-translate`  | Disable question translation                                                            | `pdf2zh_next example.pdf --disable-question-translate`                                                                |
| `--disable-answer-translate`    | Disable answer translation                                                              | `pdf2zh_next example.pdf --disable-answer-translate`                                                                  |
| `--disable-hint-translate`      | Disable hint translation                                                                | `pdf2zh_next example.pdf --disable-hint-translate`                                                                    |
| `--disable-note-translate`      | Disable note translation                                                                | `pdf2zh_next example.pdf --disable-note-translate`                                                                    |
| `--disable-tip-translate`       | Disable tip translation                                                                 | `pdf2zh_next example.pdf --disable-tip-translate`                                                                     |
| `--disable-warning-translate`   | Disable warning translation                                                             | `pdf2zh_next example.pdf --disable-warning-translate`                                                                 |
| `--disable-caution-translate`   | Disable caution translation                                                             | `pdf2zh_next example.pdf --disable-caution-translate`                                                                 |
| `--disable-important-translate` | Disable important translation                                                           | `pdf2zh_next example.pdf --disable-important-translate`                                                               |
| `--disable-error-translate`     | Disable error translation                                                               | `pdf2zh_next example.pdf --disable-error-translate`                                                                   |
| `--disable-success-translate`   | Disable success translation                                                             | `pdf2zh_next example.pdf --disable-success-translate`                                                                 |
| `--disable-info-translate`      | Disable info translation                                                                | `pdf2zh_next example.pdf --disable-info-translate`                                                                    |
| `--disable-admonition-translate`| Disable admonition translation                                                          | `pdf2zh_next example.pdf --disable-admonition-translate`                                                              |

---

### TRANSLATION RESULT

| `--disable-rich-text-translate` | Desativar tradução de texto rico                                                       | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-latex-translate`     | Desativar tradução de LaTeX                                                             | `pdf2zh_next example.pdf --disable-latex-translate`                                                                   |
| `--disable-formula-translate`   | Desativar tradução de fórmulas                                                          | `pdf2zh_next example.pdf --disable-formula-translate`                                                                 |
| `--disable-table-translate`     | Desativar tradução de tabelas                                                           | `pdf2zh_next example.pdf --disable-table-translate`                                                                   |
| `--disable-figure-translate`    | Desativar tradução de figuras                                                           | `pdf2zh_next example.pdf --disable-figure-translate`                                                                  |
| `--disable-algorithm-translate` | Desativar tradução de algoritmos                                                        | `pdf2zh_next example.pdf --disable-algorithm-translate`                                                               |
| `--disable-list-translate`      | Desativar tradução de listas                                                            | `pdf2zh_next example.pdf --disable-list-translate`                                                                    |
| `--disable-code-translate`      | Desativar tradução de código                                                            | `pdf2zh_next example.pdf --disable-code-translate`                                                                    |
| `--disable-quote-translate`     | Desativar tradução de citações                                                          | `pdf2zh_next example.pdf --disable-quote-translate`                                                                   |
| `--disable-reference-translate` | Desativar tradução de referências                                                       | `pdf2zh_next example.pdf --disable-reference-translate`                                                               |
| `--disable-citation-translate`  | Desativar tradução de citações                                                          | `pdf2zh_next example.pdf --disable-citation-translate`                                                                |
| `--disable-footnote-translate`  | Desativar tradução de notas de rodapé                                                   | `pdf2zh_next example.pdf --disable-footnote-translate`                                                                |
| `--disable-header-translate`    | Desativar tradução de cabeçalhos                                                        | `pdf2zh_next example.pdf --disable-header-translate`                                                                  |
| `--disable-footer-translate`    | Desativar tradução de rodapés                                                           | `pdf2zh_next example.pdf --disable-footer-translate`                                                                  |
| `--disable-note-translate`      | Desativar tradução de notas                                                             | `pdf2zh_next example.pdf --disable-note-translate`                                                                    |
| `--disable-proof-translate`     | Desativar tradução de provas                                                            | `pdf2zh_next example.pdf --disable-proof-translate`                                                                   |
| `--disable-example-translate`   | Desativar tradução de exemplos                                                          | `pdf2zh_next example.pdf --disable-example-translate`                                                                 |
| `--disable-definition-translate`| Desativar tradução de definições                                                        | `pdf2zh_next example.pdf --disable-definition-translate`                                                              |
| `--disable-theorem-translate`   | Desativar tradução de teoremas                                                          | `pdf2zh_next example.pdf --disable-theorem-translate`                                                                 |
| `--disable-corollary-translate` | Desativar tradução de corolários                                                        | `pdf2zh_next example.pdf --disable-corollary-translate`                                                               |
| `--disable-lemma-translate`     | Desativar tradução de lemas                                                             | `pdf2zh_next example.pdf --disable-lemma-translate`                                                                   |
| `--disable-proposition-translate`| Desativar tradução de proposições                                                       | `pdf2zh_next example.pdf --disable-proposition-translate`                                                             |
| `--disable-remark-translate`    | Desativar tradução de observações                                                       | `pdf2zh_next example.pdf --disable-remark-translate`                                                                  |
| `--disable-assumption-translate`| Desativar tradução de suposições                                                        | `pdf2zh_next example.pdf --disable-assumption-translate`                                                              |
| `--disable-conjecture-translate`| Desativar tradução de conjecturas                                                       | `pdf2zh_next example.pdf --disable-conjecture-translate`                                                              |
| `--disable-axiom-translate`     | Desativar tradução de axiomas                                                           | `pdf2zh_next example.pdf --disable-axiom-translate`                                                                   |
| `--disable-property-translate`  | Desativar tradução de propriedades                                                      | `pdf2zh_next example.pdf --disable-property-translate`                                                                |
| `--disable-exercise-translate`  | Desativar tradução de exercícios                                                        | `pdf2zh_next example.pdf --disable-exercise-translate`                                                                |
| `--disable-solution-translate`  | Desativar tradução de soluções                                                          | `pdf2zh_next example.pdf --disable-solution-translate`                                                                |
| `--disable-problem-translate`   | Desativar tradução de problemas                                                         | `pdf2zh_next example.pdf --disable-problem-translate`                                                                 |
| `--disable-question-translate`  | Desativar tradução de perguntas                                                         | `pdf2zh_next example.pdf --disable-question-translate`                                                                |
| `--disable-answer-translate`    | Desativar tradução de respostas                                                         | `pdf2zh_next example.pdf --disable-answer-translate`                                                                  |
| `--disable-hint-translate`      | Desativar tradução de dicas                                                             | `pdf2zh_next example.pdf --disable-hint-translate`                                                                    |
| `--disable-note-translate`      | Desativar tradução de notas                                                             | `pdf2zh_next example.pdf --disable-note-translate`                                                                    |
| `--disable-tip-translate`       | Desativar tradução de dicas                                                             | `pdf2zh_next example.pdf --disable-tip-translate`                                                                     |
| `--disable-warning-translate`   | Desativar tradução de avisos                                                            | `pdf2zh_next example.pdf --disable-warning-translate`                                                                 |
| `--disable-caution-translate`   | Desativar tradução de cautelas                                                          | `pdf2zh_next example.pdf --disable-caution-translate`                                                                 |
| `--disable-important-translate` | Desativar tradução de importantes                                                       | `pdf2zh_next example.pdf --disable-important-translate`                                                               |
| `--disable-error-translate`     | Desativar tradução de erros                                                             | `pdf2zh_next example.pdf --disable-error-translate`                                                                   |
| `--disable-success-translate`   | Desativar tradução de sucessos                                                          | `pdf2zh_next example.pdf --disable-success-translate`                                                                 |
| `--disable-info-translate`      | Desativar tradução de informações                                                       | `pdf2zh_next example.pdf --disable-info-translate`                                                                    |
| `--disable-admonition-translate`| Desativar tradução de admoestações                                                      | `pdf2zh_next example.pdf --disable-admonition-translate`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-after` | Enable all compatibility enhancement options after translation                           | `pdf2zh_next example.pdf --enhance-compatibility-after`                                                               |
| `--enhance-compatibility-both`  | Enable all compatibility enhancement options before and after translation                | `pdf2zh_next example.pdf --enhance-compatibility-both`                                                                |
| `--enhance-compatibility-none`  | Disable all compatibility enhancement options                                            | `pdf2zh_next example.pdf --enhance-compatibility-none`                                                                |

---

### TRANSLATED TEXT

| `--enhance-compatibility`       | Ativar todas as opções de melhoria de compatibilidade                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-after` | Ativar todas as opções de melhoria de compatibilidade após a tradução                           | `pdf2zh_next example.pdf --enhance-compatibility-after`                                                               |
| `--enhance-compatibility-both`  | Ativar todas as opções de melhoria de compatibilidade antes e após a tradução                | `pdf2zh_next example.pdf --enhance-compatibility-both`                                                                |
| `--enhance-compatibility-none`  | Desativar todas as opções de melhoria de compatibilidade                                            | `pdf2zh_next example.pdf --enhance-compatibility-none`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-alternating-pages`        | Use alternating pages mode                                                              | `pdf2zh_next example.pdf --use-alternating-pages`                                                                     |
| `--use-vertical-text`            | Use vertical text mode                                                                  | `pdf2zh_next example.pdf --use-vertical-text`                                                                         |
| `--use-vertical-text-dual`       | Use vertical text mode for dual PDF                                                     | `pdf2zh_next example.pdf --use-vertical-text-dual`                                                                    |
| `--use-vertical-text-single`     | Use vertical text mode for single PDF                                                   | `pdf2zh_next example.pdf --use-vertical-text-single`                                                                  |

---

### TRANSLATED TEXT

| `--use-alternating-pages-dual`  | Usar modo de páginas alternadas para PDF duplo                                          | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Usar modo de páginas alternadas para PDF único                                          | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-alternating-pages`        | Usar modo de páginas alternadas                                                         | `pdf2zh_next example.pdf --use-alternating-pages`                                                                     |
| `--use-vertical-text`            | Usar modo de texto vertical                                                             | `pdf2zh_next example.pdf --use-vertical-text`                                                                         |
| `--use-vertical-text-dual`       | Usar modo de texto vertical para PDF duplo                                              | `pdf2zh_next example.pdf --use-vertical-text-dual`                                                                    |
| `--use-vertical-text-single`     | Usar modo de texto vertical para PDF único                                              | `pdf2zh_next example.pdf --use-vertical-text-single`                                                                  |
`no_watermark` / `watermark` / `watermark_only` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `--watermark-text`              | Watermark text                                                                          | `pdf2zh_next example.pdf --watermark-text "Translated by pdf2zh"`                                                     |                                                 |
| `--watermark-font-size`         | Watermark font size                                                                     | `pdf2zh_next example.pdf --watermark-font-size 18`                                                                    |                                                 |
| `--watermark-font-family`       | Watermark font family                                                                   | `pdf2zh_next example.pdf --watermark-font-family "Arial"`                                                             |                                                 |
| `--watermark-font-color`        | Watermark font color                                                                    | `pdf2zh_next example.pdf --watermark-font-color "#FF0000"`                                                            |                                                 |
| `--watermark-opacity`           | Watermark opacity (0-1)                                                                 | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     |                                                 |
| `--watermark-rotation`          | Watermark rotation angle (degrees)                                                      | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     |                                                 |

---

### TRANSLATION RESULT

| `--watermark-output-mode`       | Modo de saída da marca d'água para arquivos PDF                                         | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `no_watermark` / `watermark` / `watermark_only` |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `--watermark-text`              | Texto da marca d'água                                                                   | `pdf2zh_next example.pdf --watermark-text "Translated by pdf2zh"`                                                     |                                                 |
| `--watermark-font-size`         | Tamanho da fonte da marca d'água                                                        | `pdf2zh_next example.pdf --watermark-font-size 18`                                                                    |                                                 |
| `--watermark-font-family`       | Família da fonte da marca d'água                                                        | `pdf2zh_next example.pdf --watermark-font-family "Arial"`                                                             |                                                 |
| `--watermark-font-color`        | Cor da fonte da marca d'água                                                            | `pdf2zh_next example.pdf --watermark-font-color "#FF0000"`                                                            |                                                 |
| `--watermark-opacity`           | Opacidade da marca d'água (0-1)                                                         | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     |                                                 |
| `--watermark-rotation`          | Ângulo de rotação da marca d'água (graus)                                               | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     |                                                 |
`50`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `--max-tokens-per-part`         | Maximum tokens per part for split translation                                           | `pdf2zh_next example.pdf --max-tokens-per-part 1000`                                                                  | `1000`                                                                |
| `--max-characters-per-part`     | Maximum characters per part for split translation                                       | `pdf2zh_next example.pdf --max-characters-per-part 10000`                                                             | `10000`                                                               |
| `--max-words-per-part`          | Maximum words per part for split translation                                            | `pdf2zh_next example.pdf --max-words-per-part 2000`                                                                   | `2000`                                                                |
| `--max-sentences-per-part`      | Maximum sentences per part for split translation                                        | `pdf2zh_next example.pdf --max-sentences-per-part 100`                                                                | `100`                                                                 |
| `--max-paragraphs-per-part`     | Maximum paragraphs per part for split translation                                       | `pdf2zh_next example.pdf --max-paragraphs-per-part 10`                                                                | `10`                                                                  |
| `--split-by`                    | Split by `page`, `token`, `character`, `word`, `sentence`, `paragraph`                   | `pdf2zh_next example.pdf --split-by page`                                                                             | `page`                                                                |

---

### OUTPUT

| `--max-pages-per-part`          | Número máximo de páginas por parte para tradução dividida                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     | `50`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `--max-tokens-per-part`         | Número máximo de tokens por parte para tradução dividida                                           | `pdf2zh_next example.pdf --max-tokens-per-part 1000`                                                                  | `1000`                                                                |
| `--max-characters-per-part`     | Número máximo de caracteres por parte para tradução dividida                                       | `pdf2zh_next example.pdf --max-characters-per-part 10000`                                                             | `10000`                                                               |
| `--max-words-per-part`          | Número máximo de palavras por parte para tradução dividida                                            | `pdf2zh_next example.pdf --max-words-per-part 2000`                                                                   | `2000`                                                                |
| `--max-sentences-per-part`      | Número máximo de frases por parte para tradução dividida                                        | `pdf2zh_next example.pdf --max-sentences-per-part 100`                                                                | `100`                                                                 |
| `--max-paragraphs-per-part`     | Número máximo de parágrafos por parte para tradução dividida                                       | `pdf2zh_next example.pdf --max-paragraphs-per-part 10`                                                                | `10`                                                                  |
| `--split-by`                    | Dividir por `page`, `token`, `character`, `word`, `sentence`, `paragraph`                   | `pdf2zh_next example.pdf --split-by page`                                                                             | `page`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Method for translating table text, `row` or `col` (default: `row`)                      | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method col`                                    |
| `--translate-table-text-limit`  | Limit the number of rows or columns to translate (default: `10`)                        | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-limit 5`                                       |
| `--translate-table-text-split`  | Split table text into multiple parts for translation (default: `false`)                  | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-split`                                          |
| `--translate-table-text-split-limit` | Limit the number of rows or columns to split (default: `5`)                         | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-split --translate-table-text-split-limit 3`     |

---

### OUTPUT

| `--translate-table-text`        | Traduzir texto de tabela (experimental)                                                 | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Método para traduzir texto de tabela, `row` ou `col` (padrão: `row`)                    | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method col`                                    |
| `--translate-table-text-limit`  | Limitar o número de linhas ou colunas a traduzir (padrão: `10`)                          | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-limit 5`                                       |
| `--translate-table-text-split`  | Dividir texto de tabela em várias partes para tradução (padrão: `false`)                | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-split`                                          |
| `--translate-table-text-split-limit` | Limitar o número de linhas ou colunas para dividir (padrão: `5`)                     | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-split --translate-table-text-split-limit 3`     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection=true` | Skip scanned detection                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               |
| `--skip-scanned-detection=false`| Do not skip scanned detection                                                           | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              |
| `--scanned-image-dpi`           | Set the DPI for scanned image processing                                                | `pdf2zh_next example.pdf --scanned-image-dpi=300`                                                                     |
| `--scanned-image-dpi=300`       | Set the DPI for scanned image processing to 300                                         | `pdf2zh_next example.pdf --scanned-image-dpi=300`                                                                     |
| `--scanned-image-dpi=600`       | Set the DPI for scanned image processing to 600                                         | `pdf2zh_next example.pdf --scanned-image-dpi=600`                                                                     |
| `--skip-text-extraction`        | Skip text extraction                                                                    | `pdf2zh_next example.pdf --skip-text-extraction`                                                                      |
| `--skip-text-extraction=true`   | Skip text extraction                                                                    | `pdf2zh_next example.pdf --skip-text-extraction=true`                                                                 |
| `--skip-text-extraction=false`  | Do not skip text extraction                                                             | `pdf2zh_next example.pdf --skip-text-extraction=false`                                                                |
| `--skip-text-translation`       | Skip text translation                                                                   | `pdf2zh_next example.pdf --skip-text-translation`                                                                     |
| `--skip-text-translation=true`  | Skip text translation                                                                   | `pdf2zh_next example.pdf --skip-text-translation=true`                                                                |
| `--skip-text-translation=false` | Do not skip text translation                                                            | `pdf2zh_next example.pdf --skip-text-translation=false`                                                               |
| `--skip-image-translation`      | Skip image translation                                                                  | `pdf2zh_next example.pdf --skip-image-translation`                                                                    |
| `--skip-image-translation=true` | Skip image translation                                                                  | `pdf2zh_next example.pdf --skip-image-translation=true`                                                               |
| `--skip-image-translation=false`| Do not skip image translation                                                           | `pdf2zh_next example.pdf --skip-image-translation=false`                                                              |
| `--skip-image-ocr`              | Skip image OCR                                                                          | `pdf2zh_next example.pdf --skip-image-ocr`                                                                            |
| `--skip-image-ocr=true`         | Skip image OCR                                                                          | `pdf2zh_next example.pdf --skip-image-ocr=true`                                                                       |
| `--skip-image-ocr=false`        | Do not skip image OCR                                                                   | `pdf2zh_next example.pdf --skip-image-ocr=false`                                                                      |
| `--skip-image-inpainting`       | Skip image inpainting                                                                   | `pdf2zh_next example.pdf --skip-image-inpainting`                                                                     |
| `--skip-image-inpainting=true`  | Skip image inpainting                                                                   | `pdf2zh_next example.pdf --skip-image-inpainting=true`                                                                |
| `--skip-image-inpainting=false` | Do not skip image inpainting                                                            | `pdf2zh_next example.pdf --skip-image-inpainting=false`                                                               |
| `--skip-image-super-resolution` | Skip image super resolution                                                             | `pdf2zh_next example.pdf --skip-image-super-resolution`                                                               |
| `--skip-image-super-resolution=true` | Skip image super resolution                                                         | `pdf2zh_next example.pdf --skip-image-super-resolution=true`                                                          |
| `--skip-image-super-resolution=false` | Do not skip image super resolution                                                  | `pdf2zh_next example.pdf --skip-image-super-resolution=false`                                                         |
| `--skip-table-translation`      | Skip table translation                                                                  | `pdf2zh_next example.pdf --skip-table-translation`                                                                    |
| `--skip-table-translation=true` | Skip table translation                                                                  | `pdf2zh_next example.pdf --skip-table-translation=true`                                                               |
| `--skip-table-translation=false`| Do not skip table translation                                                           | `pdf2zh_next example.pdf --skip-table-translation=false`                                                              |
| `--skip-equation-translation`   | Skip equation translation                                                               | `pdf2zh_next example.pdf --skip-equation-translation`                                                                 |
| `--skip-equation-translation=true` | Skip equation translation                                                           | `pdf2zh_next example.pdf --skip-equation-translation=true`                                                            |
| `--skip-equation-translation=false` | Do not skip equation translation                                                    | `pdf2zh_next example.pdf --skip-equation-translation=false`                                                           |
| `--skip-reference-translation`  | Skip reference translation                                                              | `pdf2zh_next example.pdf --skip-reference-translation`                                                                |
| `--skip-reference-translation=true` | Skip reference translation                                                          | `pdf2zh_next example.pdf --skip-reference-translation=true`                                                           |
| `--skip-reference-translation=false` | Do not skip reference translation                                                   | `pdf2zh_next example.pdf --skip-reference-translation=false`                                                          |
| `--skip-caption-translation`    | Skip caption translation                                                                | `pdf2zh_next example.pdf --skip-caption-translation`                                                                  |
| `--skip-caption-translation=true` | Skip caption translation                                                            | `pdf2zh_next example.pdf --skip-caption-translation=true`                                                             |
| `--skip-caption-translation=false` | Do not skip caption translation                                                     | `pdf2zh_next example.pdf --skip-caption-translation=false`                                                            |
| `--skip-footnote-translation`   | Skip footnote translation                                                               | `pdf2zh_next example.pdf --skip-footnote-translation`                                                                 |
| `--skip-footnote-translation=true` | Skip footnote translation                                                           | `pdf2zh_next example.pdf --skip-footnote-translation=true`                                                            |
| `--skip-footnote-translation=false` | Do not skip footnote translation                                                    | `pdf2zh_next example.pdf --skip-footnote-translation=false`                                                           |
| `--skip-header-translation`     | Skip header translation                                                                 | `pdf2zh_next example.pdf --skip-header-translation`                                                                   |
| `--skip-header-translation=true` | Skip header translation                                                             | `pdf2zh_next example.pdf --skip-header-translation=true`                                                              |
| `--skip-header-translation=false` | Do not skip header translation                                                      | `pdf2zh_next example.pdf --skip-header-translation=false`                                                             |
| `--skip-footer-translation`     | Skip footer translation                                                                 | `pdf2zh_next example.pdf --skip-footer-translation`                                                                   |
| `--skip-footer-translation=true` | Skip footer translation                                                             | `pdf2zh_next example.pdf --skip-footer-translation=true`                                                              |
| `--skip-footer-translation=false` | Do not skip footer translation                                                      | `pdf2zh_next example.pdf --skip-footer-translation=false`                                                             |
| `--skip-page-number-translation`| Skip page number translation                                                            | `pdf2zh_next example.pdf --skip-page-number-translation`                                                              |
| `--skip-page-number-translation=true` | Skip page number translation                                                        | `pdf2zh_next example.pdf --skip-page-number-translation=true`                                                         |
| `--skip-page-number-translation=false` | Do not skip page number translation                                                 | `pdf2zh_next example.pdf --skip-page-number-translation=false`                                                        |
| `--skip-toc-translation`        | Skip table of contents translation                                                      | `pdf2zh_next example.pdf --skip-toc-translation`                                                                      |
| `--skip-toc-translation=true`   | Skip table of contents translation                                                      | `pdf2zh_next example.pdf --skip-toc-translation=true`                                                                 |
| `--skip-toc-translation=false`  | Do not skip table of contents translation                                               | `pdf2zh_next example.pdf --skip-toc-translation=false`                                                                |
| `--skip-index-translation`      | Skip index translation                                                                  | `pdf2zh_next example.pdf --skip-index-translation`                                                                    |
| `--skip-index-translation=true` | Skip index translation                                                                  | `pdf2zh_next example.pdf --skip-index-translation=true`                                                               |
| `--skip-index-translation=false`| Do not skip index translation                                                           | `pdf2zh_next example.pdf --skip-index-translation=false`                                                              |
| `--skip-glossary-translation`   | Skip glossary translation                                                               | `pdf2zh_next example.pdf --skip-glossary-translation`                                                                 |
| `--skip-glossary-translation=true` | Skip glossary translation                                                           | `pdf2zh_next example.pdf --skip-glossary-translation=true`                                                            |
| `--skip-glossary-translation=false` | Do not skip glossary translation                                                    | `pdf2zh_next example.pdf --skip-glossary-translation=false`                                                           |
| `--skip-bibliography-translation` | Skip bibliography translation                                                         | `pdf2zh_next example.pdf --skip-bibliography-translation`                                                             |
| `--skip-bibliography-translation=true` | Skip bibliography translation                                                     | `pdf2zh_next example.pdf --skip-bibliography-translation=true`                                                        |
| `--skip-bibliography-translation=false` | Do not skip bibliography translation                                              | `pdf2zh_next example.pdf --skip-bibliography-translation=false`                                                       |
| `--skip-abstract-translation`   | Skip abstract translation                                                               | `pdf2zh_next example.pdf --skip-abstract-translation`                                                                 |
| `--skip-abstract-translation=true` | Skip abstract translation                                                           | `pdf2zh_next example.pdf --skip-abstract-translation=true`                                                            |
| `--skip-abstract-translation=false` | Do not skip abstract translation                                                    | `pdf2zh_next example.pdf --skip-abstract-translation=false`                                                           |
| `--skip-title-translation`      | Skip title translation                                                                  | `pdf2zh_next example.pdf --skip-title-translation`                                                                    |
| `--skip-title-translation=true` | Skip title translation                                                                  | `pdf2zh_next example.pdf --skip-title-translation=true`                                                               |
| `--skip-title-translation=false`| Do not skip title translation                                                           | `pdf2zh_next example.pdf --skip-title-translation=false`                                                              |
| `--skip-author-translation`     | Skip author translation                                                                 | `pdf2zh_next example.pdf --skip-author-translation`                                                                   |
| `--skip-author-translation=true` | Skip author translation                                                             | `pdf2zh_next extreme.pdf --skip-author-translation=true`                                                              |
| `--skip-author-translation=false` | Do not skip author translation                                                      | `pdf2zh_next example.pdf --skip-author-translation=false`                                                             |
| `--skip-date-translation`       | Skip date translation                                                                   | `pdf2zh_next example.pdf --skip-date-translation`                                                                     |
| `--skip-date 极速模式-translation=true` | Skip date translation                                                               | `pdf2zh_next example.pdf --skip-date-translation=true`                                                                |
| `--skip-date-translation=false` | Do not skip date translation                                                            | `pdf2zh_next example.pdf --skip-date-translation=false`                                                               |

---

### TRANSLATED TEXT

| `--skip-scanned-detection`      | Ignorar detecção de digitalizado                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-scanned-detection=true` | Ignorar detecção de digitalizado                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               |
| `--极速模式-skip-scanned-detection=false`| Não ignorar detecção de digitalizado                                                           | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              |
| `--scanned-image-dpi`           | Definir o DPI para processamento de imagem digitalizada                                                | `pdf2zh_next example.pdf --scanned-image-dpi=300`                                                                     |
| `--scanned-image-dpi=300`       | Definir o DPI para processamento de imagem digitalizada como 300                                         | `pdf2zh_next example.pdf --scanned-image 极速模式-dpi=300`                                                                     |
| `--scanned-image-dpi=600`       | Definir o DPI para processamento de imagem digitalizada como 600                                         | `pdf2zh_next example.pdf --scanned-image-dpi=600`                                                                     |
| `--skip-text-extraction`        | Ignorar extração de texto                                                                    | `pdf2zh_next example.pdf --skip-text-extraction`                                                                      |
| `--skip-text-extraction=true`   | Ignorar extração de texto                                                                    | `pdf2zh_next example.pdf --skip-text-extraction=true`                                                                 |
| `--skip-text-extraction=false`  | Não ignorar extração de texto                                                             | `pdf2zh_next example.pdf --skip-text-extraction=false`                                                                |
| `--skip-text-translation`       | Ignorar tradução de texto                                                                   | `pdf2zh_next example.pdf --skip-text-translation`                                                                     |
| `--skip-text-translation=true`  | Ignorar tradução de texto                                                                   | `pdf2zh_next example.pdf --skip-text-translation=true`                                                                |
| `--skip-text-translation=false` | Não ignorar tradução de texto                                                            | `pdf2zh_next example.pdf --skip-text-translation=false`                                                               |
| `--skip-image-translation`      | Ignorar tradução de imagem                                                                  | `pdf2zh_next example.pdf --skip-image-translation`                                                                    |
| `--skip-image-translation=true` | Ignorar tradução de imagem                                                                  | `pdf2zh_next example.pdf --skip-image-translation=true`                                                               |
| `--skip-image-translation=false`| Não ignorar tradução de imagem                                                           | `pdf2zh_next example.pdf --skip-image-translation=false`                                                              |
| `--skip-image-ocr`              | Ignorar OCR de imagem                                                                          | `pdf 极速模式 2zh_next example.pdf --skip-image-ocr`                                                                            |
| `--skip-image-ocr=true`         | Ignorar OCR de imagem                                                                          | `pdf2zh_next example.pdf --skip-image-ocr=true`                                                                       |
| `--skip-image-ocr=false`        | Não ignorar OCR de imagem                                                                   | `pdf2zh_next example.pdf --skip-image-ocr=false`                                                                      |
| `--skip-image-inpainting`       | Ignorar preenchimento de imagem                                                                   | `pdf2zh_next example.pdf --skip-image-inpainting`                                                                     |
| `--skip-image-inpainting=true`  | Ignorar preenchimento de imagem                                                                   | `pdf2zh_next example.pdf --skip-image-inpainting=true`                                                                |
| `--skip-image-inpainting=false` | Não ignorar preenchimento de imagem                                                            | `pdf2zh_next example.pdf --skip-image-inpainting=false`                                                               |
| `--skip-image-super-resolution` | Ignorar super-resolução de imagem                                                             | `pdf2zh_next example.pdf --skip-image-super-resolution`                                                               |
| `--skip-image-super-resolution=true` | Ignorar super-resolução de imagem                                                         | `pdf2zh_next example.pdf --skip-image-super-resolution=true`                                                          |
| `--skip-image-super-resolution=false` | Não ignorar super-resolução de imagem                                                  | `pdf2zh_next example.pdf --skip-image-super-resolution=false`                                                         |
| `--skip-table-translation`      | Ignorar tradução de tabela                                                                  | `pdf2zh_next example.pdf --skip-table-translation`                                                                    |
| `--skip-table-translation=true` | Ignorar tradução de tabela                                                                  | `pdf2zh_next example.pdf --skip-table-translation=true`                                                               |
| `--skip-table-translation=false`| Não ignorar tradução de tabela                                                           | `pdf2zh_next example.pdf --skip-table-translation=false`                                                              |
| `--skip-equation-translation`   | Ignorar tradução de equação                                                               | `pdf2zh_next example.pdf --skip-equation-translation`                                                                 |
| `--skip-equation-translation=true` | Ignorar tradução de equação                                                           | `pdf2zh_next example.pdf --skip-equation-translation=true`                                                            |
| `--skip-equation-translation=false` | Não ignorar tradução de equação                                                    | `pdf2zh_next example.pdf --skip-equation-translation=false`                                                           |
| `--skip-reference-translation 极速模式`  | Ignorar tradução de referência                                                              | `pdf2zh_next example.pdf --skip-reference-translation`                                                                |
| `--skip-reference-translation=true` | Ignorar tradução de referência                                                          | `pdf2zh_next example.pdf --skip-reference-translation=true`                                                           |
| `--skip-reference-translation=false` | Não ignorar tradução de referência                                                   | `pdf2zh_next example.pdf --skip-reference-translation=false`                                                          |
| `--skip-caption-translation`    | Ignorar tradução de legenda                                                                | `pdf2zh_next example.pdf --skip-caption-translation`                                                                  |
| `--skip-caption-translation=true` | Ignorar tradução de legenda                                                            | `pdf2zh_next example.pdf --skip-caption-translation=true`                                                             |
| `--skip-caption-translation=false` | Não ignorar tradução de legenda                                                     | `pdf2zh_next example.pdf --skip-caption-translation=false`                                                            |
| `--skip-footnote-translation`   | Ignorar tradução de nota de rodapé                                                               | `pdf2zh_next example.pdf --skip-footnote-translation`                                                                 |
| `--skip-footnote-translation=true` | Ignorar tradução de nota de rodapé                                                           | `pdf2zh_next example.pdf --skip-footnote-translation=true`                                                            |
| `--skip-footnote-translation=false` | Não ignorar tradução de nota de rodapé                                                    | `pdf2zh_next example.pdf --skip-footnote-translation=false`                                                           |
| `--skip-header-translation`     | Ignorar tradução de cabeçalho                                                                 | `pdf2zh_next example.pdf --skip-header-translation`                                                                   |
| `--skip-header-translation=true` | Ignorar tradução de cabeçalho                                                             | `pdf2zh_next example.pdf --skip-header-translation=true`                                                              |
| `--skip-header-translation=false` | Não ignorar tradução de cabeçalho                                                      | `pdf2zh_next example.pdf --skip-header-translation=false`                                                             |
| `--skip-footer-translation`     | Ignorar tradução de rodapé                                                                 | `pdf2zh_next example.pdf --skip-footer-translation 极速模式`                                                                   |
| `--skip-footer-translation=true` | Ignorar tradução de rodapé                                                             | `pdf2 极速模式 zh_next example.pdf --skip-footer-translation=true`                                                              |
| `--skip-footer-translation=false` | Não ignorar tradução de rodapé                                                      | `pdf2zh_next example.pdf --skip-footer-translation=false`                                                             |
| `--skip-page-number-translation`| Ignorar tradução de número de página                                                            | `pdf2zh_next example.pdf --skip-page-number-translation`                                                              |
| `--skip-page-number-translation=true` | Ignorar tradução de número de página                                                        | `pdf2zh_next example.pdf --skip-page-number-translation=true`                                                         |
| `--skip-page-number-translation=false` | Não ignorar tradução de número de página                                                 | `pdf2zh_next example.pdf --skip-page-number-translation=false`                                                        |
| `--skip-toc-translation`        | Ignorar tradução de índice                                                      | `pdf2zh_next example.pdf --skip-toc-translation`                                                                      |
| `--skip-toc-translation=true`   | Ignorar tradução de índice                                                      | `pdf2zh_next example.pdf --skip-toc-translation=true`                                                                 |
| `--skip-toc-translation=false`  | Não ignorar tradução de índice                                               | `pdf2zh_next example.pdf --skip-toc-translation=false`                                                                |
| `--skip-index-translation`      | Ignorar tradução de índice                                                                  | `pdf2zh_next example.pdf --skip-index-translation`                                                                    |
| `--skip-index-translation=true` | Ignorar tradução de índice                                                                  | `pdf2zh_next example.pdf --skip-index-translation=true`                                                               |
| `--skip-index-translation=false`| Não ignorar tradução de índice                                                           | `pdf2zh_next example.pdf --skip-index-translation=false`                                                              |
| `--skip-glossary-translation`   | Ignorar tradução de glossário                                                               | `pdf2zh_next example.pdf --skip-glossary-translation`                                                                 |
| `--skip-glossary-translation=true` | Ignorar tradução de glossário                                                           | `pdf2zh_next example.pdf --skip-glossary-translation=true`                                                            |
| `--skip-glossary-translation=false` | Não ignorar tradução de glossário                                                    | `pdf2zh_next example.pdf --skip-glossary-translation=false`                                                           |
| `--skip-bibliography-translation` | Ignorar tradução de bibliografia                                                         | `pdf2zh_next example.pdf --skip-bibliography-translation`                                                             |
| `--skip-bibliography-translation=true` | Ignorar tradução de bibliografia                                                     | `pdf2zh_next example.pdf --skip-bibliography-translation=true`                                                        |
| `--skip-bibliography-translation=false` | Não ignorar tradução de bibliografia                                              | `pdf2zh_next example.pdf --skip-bibliography-translation=false`                                                       |
| `--skip-abstract-translation`   | Ignorar tradução de resumo                                                               | `pdf2zh_next example.pdf --skip-abstract-translation`                                                                 |
| `--skip-abstract-translation=true 极速模式` | Ignorar tradução de resumo                                                           | `pdf2zh_next example.pdf --skip-abstract-translation=true`                                                            |
| `--skip-abstract-translation=false` | Não ignorar tradução de resumo                                                    | `pdf2zh_next example.pdf --skip-abstract-translation=false`                                                           |
| `--skip-title-translation`      | Ignorar tradução de título                                                                  | `pdf2zh_next example.pdf --skip-title-translation`                                                                    |
| `--skip-title-translation=true` | Ignorar tradução de título                                                                  | `pdf2zh_next example.pdf --skip-title-translation=true`                                                               |
| `--skip-title-translation=false`| Não ignorar tradução de título                                                           | `pdf2zh_next example.pdf --skip-title-translation=false`                                                              |
| `--skip-author-translation`     | Ignorar tradução de autor                                                                 | `pdf2zh_next example.pdf --skip-author-translation`                                                                   |
| `--skip-author-translation=true` | Ignorar tradução de autor                                                             | `pdf2zh_next extreme.pdf --skip-author-translation=true`                                                              |
| `--skip-author-translation=false` | Não ignorar tradução de autor                                                      | `pdf2zh_next example.pdf --skip-author-translation=false`                                                             |
| `--skip-date-translation`       | Ignorar tradução de data                                                                   | `pdf2zh_next example.pdf --skip-date-translation`                                                                     |
| `--skip-date-translation=true` | Ignorar tradução de data                                                               | `pdf2zh_next example.pdf --skip-date-translation=true`                                                                |
| `--skip-date-translation=false` | Não ignorar tradução de data                                                            | `pdf2zh_next example.pdf --skip-date-translation=false`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-no-background` | Force translated text to be black without adding any background                         | `pdf2zh_next example.pdf --ocr-workaround-no-background`                                                              |
| `--ocr-workaround-no-text`      | Force adding white background without changing the text color                           | `pdf2zh_next example.pdf --ocr-workaround-no-text`                                                                   |
| `--ocr-workaround-color <color>` | Force translated text to be the specified color and add white background                | `pdf2zh_next example.pdf --ocr-workaround-color red`<br>`pdf2zh_next example.pdf --ocr-workaround-color "#ff0000"`    |
| `--ocr-workaround-bg <color>`   | Force translated text to be black and add the specified background                      | `pdf2zh_next example.pdf --ocr-workaround-bg yellow`<br>`pdf2zh_next example.pdf --ocr-workaround-bg "#ffff00"`       |
| `--ocr-workaround-custom <color> <color>` | Force translated text to be the first color and add the second background         | `pdf2zh_next example.pdf --ocr-workaround-custom red yellow`<br>`pdf2zh_next example.pdf --ocr-workaround-custom "#ff0000" "#ffff00"` |

---

### OUTPUT

| `--ocr-workaround`              | Forçar o texto traduzido a ser preto e adicionar fundo branco                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-no-background` | Forçar o texto traduzido a ser preto sem adicionar qualquer fundo                         | `pdf2zh_next example.pdf --ocr-workaround-no-background`                                                              |
| `--ocr-workaround-no-text`      | Forçar a adição de fundo branco sem alterar a cor do texto                           | `pdf2zh_next example.pdf --ocr-workaround-no-text`                                                                   |
| `--ocr-workaround-color <color>` | Forçar o texto traduzido a ser a cor especificada e adicionar fundo branco                | `pdf2zh_next example.pdf --ocr-workaround-color red`<br>`pdf2zh_next example.pdf --ocr-workaround-color "#ff0000"`    |
| `--ocr-workaround-bg <color>`   | Forçar o texto traduzido a ser preto e adicionar o fundo especificado                      | `pdf2zh_next example.pdf --ocr-workaround-bg yellow`<br>`pdf2zh_next example.pdf --ocr-workaround-bg "#ffff00"`       |
| `--ocr-workaround-custom <color> <color>` | Forçar o texto traduzido a ser a primeira cor e adicionar o segundo fundo         | `pdf2zh_next example.pdf --ocr-workaround-custom red yellow`<br>`pdf2zh_next example.pdf --ocr-workaround-custom "#ff0000" "#ffff00"` |
---

### OUTPUT

| `--auto-enable-ocr-workaround`  | Ativar solução alternativa automática de OCR. Se um documento for detectado como fortemente digitalizado, isso tentará ativar o processamento de OCR e ignorar a detecção de digitalização adicional. Consulte a documentação para obter detalhes. (padrão: Falso) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| `--only-include-translated-page`| Incluir apenas páginas traduzidas no PDF de saída. Eficaz apenas quando --pages é usado.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| `--no-merge-alternating-line-numbers` | Desativar a fusão de números de linha alternados e parágrafos de texto em documentos com numeração de linhas | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| -------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-formula-lines`  | Desativar a remoção de linhas não relacionadas a fórmulas dentro de áreas de parágrafo | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |

---

### TRANSLATION RESULT

| `--no-remove-non-formula-lines` | Desativar a remoção de linhas não relacionadas a fórmulas dentro de áreas de parágrafo | `pdf2zh_next example.pdf --no-remove-non-formula-lines` |
`0.85`   |
| `--non-formula-line-ignore-threshold` | Set ignore threshold for non-formula lines (0.0-1.0)                               | `pdf2zh_next example.pdf --non-formula-line-ignore-threshold 0.1`                                                      | `0.1`    |
| `--formula-line-iou-threshold`     | Set IoU threshold for identifying formula lines (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                            | `0.85`   |
| `--formula-line-ignore-threshold`  | Set ignore threshold for formula lines (0.0-1.0)                                   | `pdf2zh_next example.pdf --formula-line-ignore-threshold 0.1`                                                          | `0.1`    |
| `--table-line-iou-threshold`       | Set IoU threshold for identifying table lines (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                               | `0.85`   |
| `--table-line-ignore-threshold`    | Set ignore threshold for table lines (0.0-1.0)                                     | `pdf2zh_next example.pdf --table-line-ignore-threshold 0.1`                                                             | `0.1`    |

---

### OUTPUT

| `--non-formula-line-iou-threshold` | Definir o limite de IoU para identificar linhas não de fórmula (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.85`   |
| `--non-formula-line-ignore-threshold` | Definir o limite de ignorar para linhas não de fórmula (0.0-1.0)                               | `pdf2zh_next example.pdf --non-formula-line-ignore-threshold 0.1`                                                      | `0.1`    |
| `--formula-line-iou-threshold`     | Definir o limite de IoU para identificar linhas de fórmula (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                            | `0.85`   |
| `--formula-line-ignore-threshold`  | Definir o limite de ignorar para linhas de fórmula (0.0-1.0)                                   | `pdf2zh_next example.pdf --formula-line-ignore-threshold 0.1`                                                          | `0.1`    |
| `--table-line-iou-threshold`       | Definir o limite de IoU para identificar linhas de tabela (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                               | `0.85`   |
| `--table-line-ignore-threshold`    | Definir o limite de ignorar para linhas de tabela (0.0-1.0)                                     | `pdf2zh_next example.pdf --table-line-ignore-threshold 0.1`                                                             | `0.1`    |
`0.95` |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |

---

### OUTPUT

| `--figure-table-protection-threshold` | Define o limite de proteção para figuras e tabelas (0.0-1.0). Linhas dentro de figuras/tabelas não serão processadas | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        | `0.95` |
---

### TRANSLATION RESULT

| `--skip-formula-offset-calculation` | Ignorar o cálculo de deslocamento de fórmulas durante o processamento          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### Argumentos da GUI

| `--server_name <server_name>`   | Specify the server name                | `pdf2zh_next --gui --server_name 0.0.0.0`       |
| `--server_port <port>`          | Specify the server port                | `pdf2zh_next --gui --server_port 7861`          |
| `--concurrency_count <count>`   | Set the number of concurrent threads   | `pdf2zh_next --gui --concurrency_count 10`      |
| `--max_files <count>`           | Set the maximum number of upload files | `pdf2zh_next --gui --max_files 20`              |
| `--queue_timeout <timeout>`     | Set the queue timeout                  | `pdf2zh_next --gui --queue_timeout 120`         |
| `--auth <username:password>`    | Set the authentication                 | `pdf2zh_next --gui --auth admin:password`       |
| `--auth_message <message>`      | Set the authentication message         | `pdf2zh_next --gui --auth_message "请登录"`     |
| `--ssl_keyfile <keyfile_path>`  | Set the SSL key file path              | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile <certfile_path>`| Set the SSL certificate file path      | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--ssl_keyfile_password <pass>` | Set the SSL key file password          | `pdf2zh_next --gui --ssl_keyfile_password pass` |

---

### RESPONSE

| Opção                          | Função                                  | Exemplo                                         |
| ------------------------------ | --------------------------------------- | ----------------------------------------------- |
| `--share`                       | Ativar modo de compartilhamento         | `pdf2zh_next --gui --share`                     |
| `--server_name <server_name>`   | Especificar o nome do servidor          | `pdf2zh_next --gui --server_name 0.0.0.0`       |
| `--server_port <port>`          | Especificar a porta do servidor         | `pdf2zh_next --gui --server_port 7861`          |
| `--concurrency_count <count>`   | Definir o número de threads simultâneas | `pdf2zh_next --gui --concurrency_count 10`      |
| `--max_files <count>`           | Definir o número máximo de arquivos enviados | `pdf2zh_next --gui --max_files 20`              |
| `--queue_timeout <timeout>`     | Definir o tempo limite da fila          | `pdf2zh_next --gui --queue_timeout 120`         |
| `--auth <username:password>`    | Definir a autenticação                  | `pdf2zh_next --gui --auth admin:password`       |
| `--auth_message <message>`      | Definir a mensagem de autenticação      | `pdf2zh_next --gui --auth_message "Por favor, faça login"` |
| `--ssl_keyfile <keyfile_path>`  | Definir o caminho do arquivo de chave SSL | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile <certfile_path>`| Definir o caminho do arquivo de certificado SSL | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--ssl_keyfile_password <pass>` | Definir a senha do arquivo de chave SSL  | `pdf2zh_next --gui --ssl_keyfile_password pass` |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--auth-user`                   | Username for authentication            | `pdf2zh_next --gui --auth-user username`        |
| `--auth-pass`                   | Password for authentication            | `pdf2zh_next --gui --auth-pass password`        |
| `--auth-token`                  | Token for authentication               | `pdf2zh_next --gui --auth-token token`          |
| `--auth-provider`               | Authentication provider                | `pdf2zh_next --gui --auth-provider google`      |

---

### OUTPUT

| `--auth-file`                   | Caminho para o arquivo de autenticação | `pdf2zh_next --gui --auth-file /caminho`        |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--auth-user`                   | Nome de usuário para autenticação      | `pdf2zh_next --gui --auth-user nome_de_usuario` |
| `--auth-pass`                   | Senha para autenticação                | `pdf2zh_next --gui --auth-pass senha`           |
| `--auth-token`                  | Token para autenticação                | `pdf2zh_next --gui --auth-token token`          |
| `--auth-provider`               | Provedor de autenticação               | `pdf2zh_next --gui --auth-provider google`      |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--disable-welcome-page`        | Disable the welcome page               | `pdf2zh_next --gui --disable-welcome-page`      |

---

### OUTPUT

| `--welcome-page`                | Caminho para o arquivo HTML de boas-vindas          | `pdf2zh_next --gui --welcome-page /caminho`        |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--disable-welcome-page`        | Desativar a página de boas-vindas               | `pdf2zh_next --gui --disable-welcome-page`      |
Enable Bing and OpenAI translation services only. |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ------------------------------------------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Google"`     | Disable Google translation service only.          |
| `--service-priority`            | Service priority                       | `pdf2zh_next --gui --service-priority "OpenAI:Bing"` | Set OpenAI as the first priority, then Bing.      |
| `--service-timeout`             | Service timeout                        | `pdf2zh_next --gui --service-timeout 30`             | Set service timeout to 30 seconds.                |
| `--service-retry`               | Service retry count                    | `pdf2zh_next --gui --service-retry 3`                | Retry up to 3 times if translation fails.         |
| `--service-fallback`            | Service fallback                       | `pdf2zh_next --gui --service-fallback`               | Enable service fallback.                          |
| `--service-fallback-timeout`    | Service fallback timeout               | `pdf2zh_next --gui --service-fallback-timeout 10`    | Set service fallback timeout to 10 seconds.       |
| `--service-fallback-retry`      | Service fallback retry count           | `pdf2zh_next --gui --service-fallback-retry 2`       | Retry up to 2 times if fallback fails.            |
| `--service-fallback-priority`   | Service fallback priority              | `pdf2zh_next --gui --service-fallback-priority "Bing:OpenAI"` | Set Bing as the first fallback priority, then OpenAI. |
| `--service-fallback-enabled`    | Service fallback enabled               | `pdf2zh_next --gui --service-fallback-enabled`       | Enable service fallback.                          |
| `--service-fallback-disabled`   | Service fallback disabled              | `pdf2zh_next --gui --service-fallback-disabled`      | Disable service fallback.                         |
| `--service-fallback-timeout`    | Service fallback timeout               | `pdf2zh_next --gui --service-fallback-timeout 10`    | Set service fallback timeout to 10 seconds.       |
| `--service-fallback-retry`      | Service fallback retry count           | `pdf2zh_next --gui --service-fallback-retry 2`       | Retry up to 2 times if fallback fails.            |
| `--service-fallback-priority`   | Service fallback priority              | `pdf2zh_next --gui --service-fallback-priority "Bing:OpenAI"` | Set Bing as the first fallback priority, then OpenAI. |
| `--service-fallback-enabled`    | Service fallback enabled               | `pdf2zh_next --gui --service-fallback-enabled`       | Enable service fallback.                          |
| `--service-fallback-disabled`   | Service fallback disabled              | `pdf2zh_next --gui --service-fallback-disabled`      | Disable service fallback.                         |

---

### TRANSLATION RESULT

| `--enabled-services`            | Serviços de tradução habilitados       | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | Habilita apenas os serviços de tradução Bing e OpenAI. |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| `--disabled-services`           | Serviços de tradução desabilitados     | `pdf2zh_next --gui --disabled-services "Google"`     | Desabilita apenas o serviço de tradução Google.         |
| `--service-priority`            | Prioridade do serviço                  | `pdf2zh_next --gui --service-priority "OpenAI:Bing"` | Define OpenAI como a primeira prioridade, depois Bing.  |
| `--service-timeout`             | Tempo limite do serviço                | `pdf2zh_next --gui --service-timeout 30`             | Define o tempo limite do serviço para 30 segundos.      |
| `--service-retry`               | Contagem de tentativas do serviço      | `pdf2zh_next --gui --service-retry 3`                | Tenta até 3 vezes se a tradução falhar.                 |
| `--service-fallback`            | Fallback do serviço                    | `pdf2zh_next --gui --service-fallback`               | Habilita o fallback do serviço.                         |
| `--service-fallback-timeout`    | Tempo limite do fallback do serviço    | `pdf2zh_next --gui --service-fallback-timeout 10`    | Define o tempo limite do fallback do serviço para 10 segundos. |
| `--service-fallback-retry`      | Contagem de tentativas do fallback do serviço | `pdf2zh_next --gui --service-fallback-retry 2`       | Tenta até 2 vezes se o fallback falhar.                 |
| `--service-fallback-priority`   | Prioridade do fallback do serviço      | `pdf2zh_next --gui --service-fallback-priority "Bing:OpenAI"` | Define Bing como a primeira prioridade de fallback, depois OpenAI. |
| `--service-fallback-enabled`    | Fallback do serviço habilitado         | `pdf2zh_next --gui --service-fallback-enabled`       | Habilita o fallback do serviço.                         |
| `--service-fallback-disabled`   | Fallback do serviço desabilitado       | `pdf2zh_next --gui --service-fallback-disabled`      | Desabilita o fallback do serviço.                       |
| `--service-fallback-timeout`    | Tempo limite do fallback do serviço    | `pdf2zh_next --gui --service-fallback-timeout 10`    | Define o tempo limite do fallback do serviço para 10 segundos. |
| `--service-fallback-retry`      | Contagem de tentativas do fallback do serviço | `pdf2zh_next --gui --service-fallback-retry 2`       | Tenta até 2 vezes se o fallback falhar.                 |
| `--service-fallback-priority`   | Prioridade do fallback do serviço      | `pdf2zh_next --gui --service-fallback-priority "Bing:OpenAI"` | Define Bing como a primeira prioridade de fallback, depois OpenAI. |
| `--service-fallback-enabled`    | Fallback do serviço habilitado         | `pdf2zh_next --gui --service-fallback-enabled`       | Habilita o fallback do serviço.                         |
| `--service-fallback-disabled`   | Fallback do serviço desabilitado       | `pdf2zh_next --gui --service-fallback-disabled`      | Desabilita o fallback do serviço.                       |
Disable sensitive input in GUI mode, suitable for screenshots. |
|---------------------------------|----------------------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `--disable-gui-close-warning`   | Disable GUI close warning              | `pdf2zh_next --gui --disable-gui-close-warning`   | Disable the close warning in GUI mode.                         |
| `--disable-gui-auto-update`     | Disable GUI auto update                | `pdf2zh_next --gui --disable-gui-auto-update`     | Disable automatic updates in GUI mode.                         |
| `--disable-gui-auto-check-update` | Disable GUI auto check update          | `pdf2zh_next --gui --disable-gui-auto-check-update` | Disable automatic update checks in GUI mode.                   |

---

### OUTPUT

| `--disable-gui-sensitive-input` | Desativar entrada sensível da GUI            | `pdf2zh_next --gui --disable-gui-sensitive-input` | Desativa a entrada sensível no modo GUI, adequado para capturas de tela. |
|---------------------------------|----------------------------------------|---------------------------------------------------|----------------------------------------------------------------|
| `--disable-gui-close-warning`   | Desativar aviso de fechamento da GUI              | `pdf2zh_next --gui --disable-gui-close-warning`   | Desativa o aviso de fechamento no modo GUI.                         |
| `--disable-gui-auto-update`     | Desativar atualização automática da GUI                | `pdf2zh_next --gui --disable-gui-auto-update`     | Desativa as atualizações automáticas no modo GUI.                         |
| `--disable-gui-auto-check-update` | Desativar verificação automática de atualização da GUI          | `pdf2zh_next --gui --disable-gui-auto-check-update` | Desativa as verificações automáticas de atualização no modo GUI.                   |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--disable-config`              | Disable configuration file loading     | `pdf2zh_next --gui --disable-config`            |

---

### OUTPUT

| `--disable-config-auto-save`    | Desativar salvamento automático de configuração | `pdf2zh_next --gui --disable-config-auto-save`  | 
|---------------------------------|-------------------------------------------------|-------------------------------------------------|
| `--disable-config`              | Desativar carregamento do arquivo de configuração | `pdf2zh_next --gui --disable-config`            |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | WebUI Server Address                   | `pdf2zh_next --gui --server-name 127.0.0.1`     |
| `--no-browser`                  | Disable automatic browser opening      | `pdf2zh_next --gui --no-browser`                |

---

### OUTPUT

| `--server-port`                 | Porta do WebUI                         | `pdf2zh_next --gui --server-port 7860`          |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | Endereço do servidor WebUI             | `pdf2zh_next --gui --server-name 127.0.0.1`     |
| `--no-browser`                  | Desativar abertura automática do navegador | `pdf2zh_next --gui --no-browser`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--ui-lang`                     | Idioma da interface do usuário         | `pdf2zh_next --gui --ui-lang pt`                |

---

### OUTPUT

| `--ui-lang`                     | Idioma da interface do usuário         | `pdf2zh_next --gui --ui-lang pt`                |

[⬆️ Voltar ao topo](#toc)

---

#### Guia de Configuração de Limitação de Taxa

Ao utilizar serviços de tradução, a configuração adequada da limitação de taxa é crucial para evitar erros de API e otimizar o desempenho. Este guia explica como configurar os parâmetros `--qps` e `--pool-max-worker` com base nas diferentes limitações do serviço upstream.

> [!TIP]
>
> É recomendado que o `pool_size` não exceda 1000. Se o `pool_size` calculado pelo método a seguir exceder 1000, por favor, use 1000.

##### Limitação de Taxa RPM (Solicitações Por Minuto)

Quando o serviço upstream tem limitações de RPM, use o seguinte cálculo:

**Fórmula de Cálculo:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> O fator de 10 é um coeficiente empírico que geralmente funciona bem para a maioria dos cenários.

**Exemplo:**
Se o seu serviço de tradução tiver um limite de 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitação de Conexões Simultâneas

Quando o serviço upstream tem limitações de conexões simultâneas (como o serviço oficial GLM), use esta abordagem:

**Fórmula de Cálculo:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Exemplo:**
Se o seu serviço de tradução permitir 50 conexões simultâneas:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Melhores práticas

> [!TIP]
> - Sempre comece com valores conservadores e aumente gradualmente, se necessário
> - Monitore os tempos de resposta e as taxas de erro do seu serviço
> - Diferentes serviços podem exigir diferentes estratégias de otimização
> - Considere seu caso de uso específico e o tamanho do documento ao definir esses parâmetros


[⬆️ Voltar ao topo](#toc)

---

#### Tradução parcial

Use o parâmetro `--pages` para traduzir uma parte de um documento.

- Se os números das páginas forem consecutivos, você pode escrever assim:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` inclui todas as páginas após a página 25. Se o seu documento tiver 100 páginas, isso é equivalente a `25-100`.
> 
> Da mesma forma, `-25` inclui todas as páginas antes da página 25, o que é equivalente a `1-25`.

- Se as páginas não forem consecutivas, você pode usar uma vírgula `,` para separá-las.

Por exemplo, se você deseja traduzir a primeira e a terceira páginas, pode usar o seguinte comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Se as páginas incluírem intervalos consecutivos e não consecutivos, você também pode conectá-los com uma vírgula, assim:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Este comando irá traduzir a primeira página, a terceira página, as páginas 10-20 e todas as páginas de 25 até o final.

[⬆️ Voltar ao topo](#toc)

---

#### Especificar idiomas de origem e destino

Veja [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Voltar ao topo](#toc)

---

#### Traduzir com exceções

Use regex para especificar fontes de fórmulas e caracteres que precisam ser preservados:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Preservar as fontes `Latex`, `Mono`, `Code`, `Italic`, `Symbol` e `Math` por padrão:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Voltar ao topo](#toc)

---

#### Prompt personalizado

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Prompt personalizado do sistema para tradução. Ele é usado principalmente para adicionar a instrução '/no_think' do Qwen 3 no prompt.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Voltar ao topo](#toc)

---

#### Configuração personalizada

Existem várias maneiras de modificar e importar o arquivo de configuração.

> [!NOTE]
> **Hierarquia do Arquivo de Configuração**
>
> Ao modificar o mesmo parâmetro usando métodos diferentes, o software aplicará as alterações de acordo com a ordem de prioridade abaixo.
>
> Modificações com classificação mais alta substituirão as de classificação mais baixa.
>
> **cli/gui > env > arquivo de configuração do usuário > arquivo de configuração padrão**

- Modificando a Configuração via **Argumentos da Linha de Comando**

Na maioria dos casos, você pode passar diretamente suas configurações desejadas através dos argumentos da linha de comando. Consulte [Argumentos da Linha de Comando](#cmd) para obter mais informações.

Por exemplo, se você deseja habilitar uma janela GUI, pode usar o seguinte comando:

```bash
pdf2zh_next --gui
```

- Modificando a Configuração via **Variáveis de Ambiente**

Você pode substituir o `--` nos argumentos da linha de comando por `PDF2ZH_`, conectar parâmetros usando `=` e substituir `-` por `_` como variáveis de ambiente.

Por exemplo, se você quiser habilitar uma janela GUI, pode usar o seguinte comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Arquivo de **Configuração** Especificado pelo Usuário

Você pode especificar um arquivo de configuração usando o argumento da linha de comando abaixo:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Se você não tiver certeza sobre o formato do arquivo de configuração, consulte o arquivo de configuração padrão descrito abaixo.

- **Arquivo de Configuração Padrão**

O arquivo de configuração padrão está localizado em `~/.config/pdf2zh`.  
Por favor, não modifique os arquivos de configuração no diretório `default`.  
É altamente recomendável consultar o conteúdo deste arquivo de configuração e usar **Configuração personalizada** para implementar seu próprio arquivo de configuração.

> [!TIP]
> - Por padrão, o pdf2zh 2.0 salva automaticamente a configuração atual em `~/.config/pdf2zh/config.v3.toml` cada vez que você clica no botão de tradução na GUI. Este arquivo de configuração será carregado por padrão na próxima inicialização.
> - Os arquivos de configuração no diretório `default` são gerados automaticamente pelo programa. Você pode copiá-los para modificação, mas por favor não os modifique diretamente.
> - Os arquivos de configuração podem incluir números de versão como "v2", "v3", etc. Estes são **números de versão do arquivo de configuração**, **não** o número de versão do pdf2zh em si.


[⬆️ Voltar ao topo](#toc)

---

#### Pular limpeza

Quando este parâmetro é definido como True, a etapa de limpeza do PDF será ignorada, o que pode melhorar a compatibilidade e evitar alguns problemas de processamento de fontes.

Uso:

```bash
pdf2zh_next example.pdf --skip-clean
```

Ou usando variáveis de ambiente:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Quando `--enhance-compatibility` está ativado, Pular limpeza é automaticamente ativado.

---

#### Cache de tradução

O PDFMathTranslate armazena em cache os textos traduzidos para aumentar a velocidade e evitar chamadas desnecessárias à API para conteúdos idênticos. Você pode usar a opção `--ignore-cache` para ignorar o cache de tradução e forçar uma nova tradução.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Voltar ao topo](#toc)

---

#### Implantação como serviços públicos

Ao implantar uma GUI pdf2zh em serviços públicos, você deve modificar o arquivo de configuração conforme descrito abaixo.

> [!WARNING]
>
> Este projeto não foi auditado profissionalmente quanto à segurança e pode conter vulnerabilidades de segurança. Por favor, avalie os riscos e tome as medidas de segurança necessárias antes de implantar em redes públicas.


> [!TIP]
> - Ao implantar publicamente, tanto disable_gui_sensitive_input quanto disable_config_auto_save devem ser ativados.
> - Separe diferentes serviços disponíveis com *vírgulas em inglês* <kbd>,</kbd> .

Uma configuração utilizável é a seguinte:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Voltar ao topo](#toc)

---

#### Autenticação e página de boas-vindas

Ao usar Autenticação e página de boas-vindas para especificar qual usuário deve usar a Web UI e personalizar a página de login:

exemplo auth.txt
Cada linha contém dois elementos, nome de usuário e senha, separados por uma vírgula.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

exemplo welcome.html

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
> A página de boas-vindas funcionará apenas se o arquivo de autenticação não estiver vazio.
> Se o arquivo de autenticação estiver vazio, não haverá autenticação. :)

Uma configuração utilizável é a seguinte:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Voltar ao topo](#toc)

---

#### Suporte ao Glossário

PDFMathTranslate suporta a tabela de glossário. O arquivo da tabela de glossário deve ser um arquivo `csv`.
Há três colunas no arquivo. Aqui está um arquivo de glossário de demonstração:

| origem  | destino  | tgt_lng |
|--------|---------|---------|---------|
| AutoML | ML Automático | pt     |
| a,a    | a       | pt      |
| "      | "       | pt      |


Para usuários da CLI:
Você pode usar vários arquivos para o glossário. E arquivos diferentes devem ser separados por `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Para usuários do WebUI:

Agora você pode enviar seu próprio arquivo de glossário. Após enviar o arquivo, você pode verificar o conteúdo clicando no nome dele, que será exibido abaixo.

[⬆️ Voltar ao topo](#toc)

<div align="right"> 
<h6><small>Parte do conteúdo desta página foi traduzida pelo GPT e pode conter erros.</small></h6>