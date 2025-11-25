>
> For details, see [Translation Contribution Guide](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

---

### OUTPUT

> [!NOTE]
> Esta documentação pode conter conteúdo gerado por IA. Embora nos esforcemos pela precisão, podem ocorrer imprecisões. Por favor, reporte quaisquer problemas através de:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - Contribuição da comunidade (PRs são bem-vindos!)
>
> Para detalhes, consulte o [Guia de Contribuição para Traduções](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html).

```python
async for chunk in do_translate_async_stream(
    file_path: str,
    source_lang_code: str = "en",
    target_lang_code: str = "zh",
    translation_service: str = "google",
    api_key: str = None,
    **kwargs,
):
    yield chunk
```

This function is designed for translating the content of a `PDF` file and streaming the results in real-time. It is particularly useful for applications that require immediate feedback or for handling large files where waiting for the entire translation to complete is not feasible.

### Parameters

- **file_path** (`str`): The path to the `PDF` file to be translated.
- **source_lang_code** (`str`, optional): The language code of the source document. Defaults to `"en"`.
- **target_lang_code** (`str`, optional): The language code for the translation output. Defaults to `"zh"`.
- **translation_service** (`str`, optional): The translation service to use. Options include `"google"`, `"openai"`, `"azure"`, `"claude"`, `"ollama"`, `"gemini"`, `"groq"`, and `"deepseek"`. Defaults to `"google"`.
- **api_key** (`str`, optional): The API key for the chosen translation service. Required for services that need authentication.
- **kwargs**: Additional keyword arguments that can be passed to customize the translation process. These may include settings specific to the translation service or other operational parameters.

### Returns

- **chunk** (`str`): A chunk of the translated text. The function yields these chunks as they become available, allowing for real-time processing.

### Example Usage

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for chunk in do_translate_async_stream(
        file_path="sample.pdf",
        source_lang_code="en",
        target_lang_code="es",
        translation_service="google"
    ):
        print(chunk, end="", flush=True)

asyncio.run(main())
```

In this example, the function streams the translation of `sample.pdf` from English to Spanish using Google's translation service. Each chunk of translated text is printed as it is received.

### Notes

- The function is asynchronous and must be used within an async context.
- Ensure that the necessary dependencies for the chosen translation service are installed and configured.
- The streaming capability is beneficial for applications that need to display progress or handle the translation output incrementally.

---

### TRANSLATION RESULT

This document describes the process for contributing translations to the `pdf2zh` project. We welcome contributions for any language, whether it's adding new translations or improving existing ones.

### How to Contribute

#### 1. Fork the Repository

First, fork the [pdf2zh repository](https://github.com/PDFMathTranslate/pdf2zh) to your own GitHub account.

#### 2. Clone Your Fork

Clone your forked repository to your local machine:

```bash
git clone https://github.com/your-username/pdf2zh.git
cd pdf2zh
```

#### 3. Create a New Branch

Create a new branch for your translation work:

```bash
git checkout -b translate-your-language
```

Replace `your-language` with the language you are translating to (e.g., `translate-spanish`).

#### 4. Add or Edit Translation Files

Translation files are located in the `docs` directory. Each language has its own subdirectory named with its [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code (e.g., `es` for Spanish, `fr` for French).

- If you are adding a new language, create a new directory for it (e.g., `docs/es` for Spanish).
- If you are improving an existing translation, navigate to the corresponding language directory.

Inside each language directory, the structure mirrors the English documentation. For example, the English file `docs/getting-started/installation.md` would have a Spanish translation at `docs/es/getting-started/installation.md`.

#### 5. Translate the Content

Translate the content of the Markdown files. Please follow these guidelines:

- **Do not** translate technical terms, code blocks, or URLs unless necessary.
- Maintain the original Markdown structure and formatting.
- Use the same file names and directory structure as the English version.

#### 6. Test Your Changes

After translating, test your changes locally to ensure everything renders correctly. You can use tools like [MkDocs](https://www.mkdocs.org/) to preview the documentation.

#### 7. Commit and Push

Commit your changes and push them to your fork:

```bash
git add .
git commit -m "Add translation for [language]"
git push origin translate-your-language
```

#### 8. Create a Pull Request

Go to the original [pdf2zh repository](https://github.com/PDFMathTranslate/pdf2zh) and create a pull request from your branch. Provide a clear description of the changes you made.

### Translation Guidelines

- **Accuracy**: Ensure translations are accurate and convey the same meaning as the original text.
- **Consistency**: Use consistent terminology across all translated documents.
- **Clarity**: Write clearly and naturally in the target language.
- **Cultural Sensitivity**: Be mindful of cultural differences and avoid literal translations that may not make sense in the target language.

### Supported Languages

We currently support translations for the following languages:

- Spanish (`es`)
- French (`fr`)
- German (`de`)
- Chinese (`zh`)
- Japanese (`ja`)
- Korean (`ko`)
- Portuguese (`pt`)
- Russian (`ru`)
- Arabic (`ar`)
- Hindi (`hi`)

If your language is not listed, feel free to add it!

### Need Help?

If you have any questions or need assistance, please open an issue in the repository or reach out to the community.

Thank you for contributing to `pdf2zh`!

---

### OUTPUT LANGUAGE CODE

pt

---

### OUTPUT

### Visão Geral

Este documento descreve o processo para contribuir com traduções para o projeto `pdf2zh`. Acolhemos contribuições para qualquer idioma, seja adicionando novas traduções ou melhorando as existentes.

### Como Contribuir

#### 1. Fazer um Fork do Repositório

Primeiro, faça um fork do [repositório pdf2zh](https://github.com/PDFMathTranslate/pdf2zh) para a sua própria conta do GitHub.

#### 2. Clonar o Seu Fork

Clone o seu repositório forkado para a sua máquina local:

```bash
git clone https://github.com/your-username/pdf2zh.git
cd pdf2zh
```

#### 3. Criar um Novo Branch

Crie um novo branch para o seu trabalho de tradução:

```bash
git checkout -b translate-your-language
```

Substitua `your-language` pelo idioma para o qual está a traduzir (por exemplo, `translate-portuguese`).

#### 4. Adicionar ou Editar Ficheiros de Tradução

Os ficheiros de tradução estão localizados no diretório `docs`. Cada idioma tem o seu próprio subdiretório nomeado com o seu código de idioma [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (por exemplo, `es` para espanhol, `fr` para francês).

- Se estiver a adicionar um novo idioma, crie um novo diretório para ele (por exemplo, `docs/pt` para português).
- Se estiver a melhorar uma tradução existente, navegue para o diretório do idioma correspondente.

Dentro de cada diretório de idioma, a estrutura espelha a documentação em inglês. Por exemplo, o ficheiro em inglês `docs/getting-started/installation.md` teria uma tradução em português em `docs/pt/getting-started/installation.md`.

#### 5. Traduzir o Conteúdo

Traduza o conteúdo dos ficheiros Markdown. Por favor, siga estas diretrizes:

- **Não** traduza termos técnicos, blocos de código ou URLs, a menos que seja necessário.
- Mantenha a estrutura e formatação Markdown originais.
- Use os mesmos nomes de ficheiro e estrutura de diretório que a versão em inglês.

#### 6. Testar as Suas Alterações

Após traduzir, teste as suas alterações localmente para garantir que tudo é renderizado corretamente. Pode usar ferramentas como [MkDocs](https://www.mkdocs.org/) para pré-visualizar a documentação.

#### 7. Fazer Commit e Push

Faça commit das suas alterações e envie-as para o seu fork:

```bash
git add .
git commit -m "Add translation for [language]"
git push origin translate-your-language
```

#### 8. Criar um Pull Request

Vá ao [repositório pdf2zh](https://github.com/PDFMathTranslate/pdf2zh) original e crie um pull request a partir do seu branch. Forneça uma descrição clara das alterações que fez.

### Diretrizes de Tradução

- **Precisão**: Garanta que as traduções são precisas e transmitem o mesmo significado que o texto original.
- **Consistência**: Use terminologia consistente em todos os documentos traduzidos.
- **Clareza**: Escreva de forma clara e natural no idioma de destino.
- **Sensibilidade Cultural**: Esteja atento às diferenças culturais e evite traduções literais que possam não fazer sentido no idioma de destino.

### Idiomas Suportados

Atualmente, suportamos traduções para os seguintes idiomas:

- Espanhol (`es`)
- Francês (`fr`)
- Alemão (`de`)
- Chinês (`zh`)
- Japonês (`ja`)
- Coreano (`ko`)
- Português (`pt`)
- Russo (`ru`)
- Árabe (`ar`)
- Hindi (`hi`)

Se o seu idioma não estiver listado, sinta-se à vontade para adicioná-lo!

### Precisa de Ajuda?

Se tiver alguma dúvida ou precisar de assistência, por favor, abra um issue no repositório ou contacte a comunidade.

Obrigado por contribuir para o `pdf2zh`!
- The events are in the same format as the WebUI's SSE events.

---

### OUTPUT

- do_translate_async_stream é o ponto de entrada assíncrono de baixo nível que traduz um único PDF e produz um fluxo de eventos (progresso/erro/conclusão).
- É adequado para construir sua própria UI ou CLI onde você deseja progresso em tempo real e controle total sobre os resultados.
- Aceita um SettingsModel validado e um caminho de arquivo e retorna um gerador assíncrono de eventos dict.
- Os eventos estão no mesmo formato que os eventos SSE da WebUI.
- ### Installation: The installation process is straightforward. You can install `pdf2zh` using `pip`:

```bash
pip install pdf2zh
```

### Dependencies

`pdf2zh` depends on the following packages:

- `pdfplumber`: For extracting text from PDF files.
- `requests`: For making HTTP requests to translation services.
- `aiohttp`: For asynchronous HTTP requests.
- `Pillow`: For image processing (if needed).

These dependencies will be installed automatically when you install `pdf2zh`.

### Upgrading

To upgrade to the latest version of `pdf2zh`, use:

```bash
pip install --upgrade pdf2zh
```

### Verifying Installation

After installation, you can verify that `pdf2zh` is installed correctly by running:

```bash
python -c "import pdf2zh; print('pdf2zh installed successfully')"
```

If you see the message "pdf2zh installed successfully", the installation was successful.

### Troubleshooting

If you encounter any issues during installation, please check the following:

1. Ensure you have Python 3.7 or higher installed.
2. Make sure you have the latest version of `pip`.
3. Check your internet connection.

If problems persist, please open an issue on the [GitHub repository](https://github.com/PDFMathTranslate/pdf2zh/issues).

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

### Instalação

O processo de instalação é simples. Você pode instalar o `pdf2zh` usando `pip`:

```bash
pip install pdf2zh
```

### Dependências

O `pdf2zh` depende dos seguintes pacotes:

- `pdfplumber`: Para extrair texto de arquivos PDF.
- `requests`: Para fazer solicitações HTTP para serviços de tradução.
- `aiohttp`: Para solicitações HTTP assíncronas.
- `Pillow`: Para processamento de imagens (se necessário).

Essas dependências serão instaladas automaticamente quando você instalar o `pdf2zh`.

### Atualização

Para atualizar para a versão mais recente do `pdf2zh`, use:

```bash
pip install --upgrade pdf2zh
```

### Verificando a Instalação

Após a instalação, você pode verificar se o `pdf2zh` foi instalado corretamente executando:

```bash
python -c "import pdf2zh; print('pdf2zh instalado com sucesso')"
```

Se você vir a mensagem "pdf2zh instalado com sucesso", a instalação foi bem-sucedida.

### Solução de Problemas

Se você encontrar qualquer problema durante a instalação, por favor, verifique o seguinte:

1. Certifique-se de ter o Python 3.7 ou superior instalado.
2. Certifique-se de ter a versão mais recente do `pip`.
3. Verifique sua conexão com a internet.

Se os problemas persistirem, por favor, abra um issue no [repositório do GitHub](https://github.com/PDFMathTranslate/pdf2zh/issues).
- ### Command Line Interface: The Command Line Interface (CLI) of `pdf2zh` provides a convenient way to translate PDF files directly from the terminal.

### Basic Usage

To translate a PDF file, use the following command:

```bash
pdf2zh translate input.pdf
```

This command will translate `input.pdf` from English to Chinese (the default target language) and output the result to the terminal.

### Specifying Output File

To save the translation to a file, use the `-o` or `--output` option:

```bash
pdf2zh translate input.pdf -o output.txt
```

### Changing Target Language

You can specify the target language using the `-t` or `--target-lang` option:

```bash
pdf2zh translate input.pdf -t es
```

This will translate the PDF to Spanish.

### Specifying Source Language

If the source language is not English, you can specify it with the `-s` or `--source-lang` option:

```bash
pdf2zh translate input.pdf -s fr -t en
```

This will translate a French PDF to English.

### Using Different Translation Services

`pdf2zh` supports multiple translation services. You can choose one with the `--service` option:

```bash
pdf2zh translate input.pdf --service google
```

Available services include `google`, `deepl`, `openai`, and `azure`.

### Batch Processing

To translate multiple PDF files at once, you can use:

```bash
pdf2zh translate *.pdf
```

This will translate all PDF files in the current directory.

### Help Command

For more information on the available options, use the help command:

```bash
pdf2zh translate --help
```

### Environment Variables

You can set API keys for translation services as environment variables:

```bash
export GOOGLE_TRANSLATE_API_KEY="your_api_key"
export DEEPL_API_KEY="your_api_key"
export OPENAI_API_KEY="your_api_key"
export AZURE_TRANSLATOR_KEY="your_api_key"
```

Then, `pdf2zh` will use these keys automatically.

### Example

Here's an example command that uses all the options:

```bash
pdf2zh translate document.pdf -s en -t pt -o translated_document.txt --service deepl
```

This command translates `document.pdf` from English to Portuguese using DeepL and saves the result to `translated_document.txt`.

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

### Interface de Linha de Comando

A Interface de Linha de Comando (CLI) do `pdf2zh` fornece uma maneira conveniente de traduzir arquivos PDF diretamente do terminal.

### Uso Básico

Para traduzir um arquivo PDF, use o seguinte comando:

```bash
pdf2zh translate input.pdf
```

Este comando irá traduzir `input.pdf` do inglês para o chinês (o idioma de destino padrão) e enviar o resultado para o terminal.

### Especificando Arquivo de Saída

Para salvar a tradução em um arquivo, use a opção `-o` ou `--output`:

```bash
pdf2zh translate input.pdf -o output.txt
```

### Alterando o Idioma de Destino

Você pode especificar o idioma de destino usando a opção `-t` ou `--target-lang`:

```bash
pdf2zh translate input.pdf -t es
```

Isso irá traduzir o PDF para espanhol.

### Especificando o Idioma de Origem

Se o idioma de origem não for inglês, você pode especificá-lo com a opção `-s` ou `--source-lang`:

```bash
pdf2zh translate input.pdf -s fr -t en
```

Isso irá traduzir um PDF em francês para inglês.

### Usando Diferentes Serviços de Tradução

O `pdf2zh` suporta vários serviços de tradução. Você pode escolher um com a opção `--service`:

```bash
pdf2zh translate input.pdf --service google
```

Os serviços disponíveis incluem `google`, `deepl`, `openai` e `azure`.

### Processamento em Lote

Para traduzir vários arquivos PDF de uma vez, você pode usar:

```bash
pdf2zh translate *.pdf
```

Isso irá traduzir todos os arquivos PDF no diretório atual.

### Comando de Ajuda

Para mais informações sobre as opções disponíveis, use o comando de ajuda:

```bash
pdf2zh translate --help
```

### Variáveis de Ambiente

Você pode definir chaves de API para serviços de tradução como variáveis de ambiente:

```bash
export GOOGLE_TRANSLATE_API_KEY="sua_chave_api"
export DEEPL_API_KEY="sua_chave_api"
export OPENAI_API_KEY="sua_chave_api"
export AZURE_TRANSLATOR_KEY="sua_chave_api"
```

Então, o `pdf2zh` usará essas chaves automaticamente.

### Exemplo

Aqui está um exemplo de comando que usa todas as opções:

```bash
pdf2zh translate document.pdf -s en -t pt -o translated_document.txt --service deepl
```

Este comando traduz `document.pdf` do inglês para português usando o DeepL e salva o resultado em `translated_document.txt`.
- ### Web UI: The Web UI provides a user-friendly interface for translating PDF files without using the command line.

### Accessing the Web UI

To start the Web UI, run the following command:

```bash
pdf2zh serve
```

This will start a local server, and you can access the Web UI by opening your browser and navigating to `http://localhost:7860`.

### Uploading a PDF

1. Click the **Upload** button to select a PDF file from your computer.
2. Alternatively, you can drag and drop a PDF file into the upload area.

### Selecting Languages

1. Choose the source language of your PDF from the **Source Language** dropdown.
2. Choose the target language for translation from the **Target Language** dropdown.

### Translation Options

You can customize the translation process with the following options:

- **Translation Service**: Choose from supported translation services (Google, DeepL, OpenAI, Azure).
- **Ignore Formatting**: If enabled, only the text content will be translated, and formatting will be ignored.
- **Ignore Images**: Skip processing of images in the PDF.
- **Ignore Tables**: Skip processing of tables in the PDF.
- **Ignore Equations**: Skip processing of mathematical equations.

### Starting the Translation

Click the **Translate** button to start the translation process. The progress will be displayed in real-time.

### Viewing the Result

Once the translation is complete, the translated text will be displayed on the screen. You can:

- **Copy** the text to clipboard.
- **Download** the translated text as a text file.
- **Download** the translated PDF (if formatting is preserved).

### Saving API Keys

If you are using a translation service that requires an API key, you can enter it in the **API Key** field. The key will be saved in your browser's local storage for future use.

### Exiting the Web UI

To stop the Web UI, press `Ctrl+C` in the terminal where the server is running.

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

### Web UI

A Web UI fornece uma interface amigável para traduzir arquivos PDF sem usar a linha de comando.

### Acessando a Web UI

Para iniciar a Web UI, execute o seguinte comando:

```bash
pdf2zh serve
```

Isso iniciará um servidor local, e você pode acessar a Web UI abrindo seu navegador e navegando para `http://localhost:7860`.

### Fazendo Upload de um PDF

1. Clique no botão **Upload** para selecionar um arquivo PDF do seu computador.
2. Alternativamente, você pode arrastar e soltar um arquivo PDF na área de upload.

### Selecionando Idiomas

1. Escolha o idioma de origem do seu PDF no menu suspenso **Idioma de Origem**.
2. Escolha o idioma de destino para a tradução no menu suspenso **Idioma de Destino**.

### Opções de Tradução

Você pode personalizar o processo de tradução com as seguintes opções:

- **Serviço de Tradução**: Escolha entre os serviços de tradução suportados (Google, DeepL, OpenAI, Azure).
- **Ignorar Formatação**: Se habilitado, apenas o conteúdo de texto será traduzido, e a formatação será ignorada.
- **Ignorar Imagens**: Pular o processamento de imagens no PDF.
- **Ignorar Tabelas**: Pular o processamento de tabelas no PDF.
- **Ignorar Equações**: Pular o processamento de equações matemáticas.

### Iniciando a Tradução

Clique no botão **Traduzir** para iniciar o processo de tradução. O progresso será exibido em tempo real.

### Visualizando o Resultado

Quando a tradução estiver concluída, o texto traduzido será exibido na tela. Você pode:

- **Copiar** o texto para a área de transferência.
- **Baixar** o texto traduzido como um arquivo de texto.
- **Baixar** o PDF traduzido (se a formatação for preservada).

### Salvando Chaves de API

Se você estiver usando um serviço de tradução que requer uma chave de API, pode inseri-la no campo **Chave de API**. A chave será salva no armazenamento local do seu navegador para uso futuro.

### Saindo da Web UI

Para parar a Web UI, pressione `Ctrl+C` no terminal onde o servidor está sendo executado.

- **File**: `pdf2zh/utils/signature.py`
- **Function**: `sign()`

This function is used to generate a signature for the given string using the HMAC-SHA256 algorithm.

#### Parameters

- `message` (str): The string to be signed.
- `secret` (str): The secret key used for signing.

#### Returns

- `str`: The generated signature in hexadecimal format.

#### Example

```python
sign("hello world", "secret")
# returns: "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
```

---

### TASK

Translate the following `ORIGINAL TEXT` into pt(ISO 639-1 code).

---

### ORIGINAL TEXT

### Assinatura

- **Arquivo**: `pdf2zh/utils/signature.py`
- **Função**: `sign()`

Esta função é usada para gerar uma assinatura para a string fornecida usando o algoritmo HMAC-SHA256.

#### Parâmetros

- `message` (str): A string a ser assinada.
- `secret` (str): A chave secreta usada para assinar.

#### Retorna

- `str`: A assinatura gerada em formato hexadecimal.

#### Exemplo

```python
sign("hello world", "secret")
# retorna: "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
```
- Returns: An async iterator that yields `Event` objects. The `Event` class is defined in `pdf2zh_next.high_level` and has fields:
  - type: EventType (enum with values: `message`, `error`, `done`)
  - data: dict (the event data, which depends on the event type)
- Usage: This function is the main entry point for translating a PDF file asynchronously with streaming. It handles the entire translation process, including:
  - Validating the settings
  - Reading the PDF file
  - Extracting text
  - Sending text to the translation service
  - Streaming the results back in real-time
- Example:

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream, SettingsModel

async def main():
    settings = SettingsModel(
        source_lang_code="en",
        target_lang_code="zh",
        translation_service="google",
    )
    async for event in do_translate_async_stream(settings, "example.pdf"):
        if event.type == "message":
            print(event.data["content"], end="")
        elif event.type == "error":
            print("Error:", event.data["message"])
        elif event.type == "done":
            print("\nTranslation complete.")

asyncio.run(main())
```

---

### OUTPUT

- Importar: `from pdf2zh_next.high_level import do_translate_async_stream`
- Chamada: `async for event in do_translate_async_stream(settings, file): ...`
- Parâmetros:
  - settings: SettingsModel. Deve ser válido; a função chamará `settings.validate_settings()`.
  - file: str | pathlib.Path. O único PDF a traduzir. Deve existir.
- Retorna: Um iterador assíncrono que produz objetos `Event`. A classe `Event` é definida em `pdf2zh_next.high_level` e tem campos:
  - type: EventType (enum com valores: `message`, `error`, `done`)
  - data: dict (os dados do evento, que dependem do tipo de evento)
- Uso: Esta função é o ponto de entrada principal para traduzir um arquivo PDF de forma assíncrona com streaming. Ela trata de todo o processo de tradução, incluindo:
  - Validar as configurações
  - Ler o arquivo PDF
  - Extrair texto
  - Enviar texto para o serviço de tradução
  - Transmitir os resultados de volta em tempo real
- Exemplo:

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream, SettingsModel

async def main():
    settings = SettingsModel(
        source_lang_code="en",
        target_lang_code="zh",
        translation_service="google",
    )
    async for event in do_translate_async_stream(settings, "example.pdf"):
        if event.type == "message":
            print(event.data["content"], end="")
        elif event.type == "error":
            print("Error:", event.data["message"])
        elif event.type == "done":
            print("\nTranslation complete.")

asyncio.run(main())
```

The following content is a translated version of the original English documentation. While we strive for accuracy, there may be some discrepancies. Please refer to the [original documentation](https://pdf2zh-next.com/) for the most up-to-date information.

### Introduction

Welcome to the `pdf2zh` project! This tool is designed to help you translate `PDF` documents from various languages into Chinese (and other languages). Whether you're a researcher, student, or professional, `pdf2zh` aims to make document translation seamless and efficient.

### Key Features

- **Multi-language Support**: Translate from multiple source languages to Chinese and other target languages.
- **Format Preservation**: Maintain the original layout and formatting of your `PDF` documents.
- **Batch Processing**: Handle multiple documents efficiently.
- **Customizable Translation**: Choose from various translation services or use your own.
- **Open Source**: Fully open-source with a community-driven approach.

### Quick Start

To get started with `pdf2zh`, check out the [Getting Started](https://pdf2zh-next.com/getting-started/) guide. It will walk you through the installation process and basic usage.

### Supported Languages

`pdf2zh` supports a wide range of languages. For a complete list, visit the [Supported Languages](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) page.

### Contributing

We welcome contributions from the community! Whether it's adding new features, improving documentation, or translating content, your help is appreciated. See the [Contributing Guide](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) for more details.

### Community

Join our community to get help, share ideas, and collaborate:
- [GitHub Discussions](https://github.com/Alexander-Porter/pdf2zh/discussions)
- [Issue Tracker](https://github.com/Alexander-Porter/pdf2zh/issues)

### License

`pdf2zh` is released under the [MIT License](https://opensource.org/licenses/MIT).

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

Nota: O conteúdo a seguir é uma versão traduzida da documentação original em inglês. Embora nos esforcemos pela precisão, podem ocorrer algumas discrepâncias. Consulte a [documentação original](https://pdf2zh-next.com/) para obter as informações mais atualizadas.

### Introdução

Bem-vindo ao projeto `pdf2zh`! Esta ferramenta foi projetada para ajudá-lo a traduzir documentos `PDF` de vários idiomas para chinês (e outros idiomas). Quer você seja um pesquisador, estudante ou profissional, o `pdf2zh` visa tornar a tradução de documentos perfeita e eficiente.

### Características Principais

- **Suporte a Múltiplos Idiomas**: Traduza de vários idiomas de origem para chinês e outros idiomas de destino.
- **Preservação de Formatação**: Mantenha o layout e a formatação originais dos seus documentos `PDF`.
- **Processamento em Lote**: Lide com vários documentos de forma eficiente.
- **Tradução Personalizável**: Escolha entre vários serviços de tradução ou use o seu próprio.
- **Código Aberto**: Totalmente de código aberto com uma abordagem orientada pela comunidade.

### Começar Rápido

Para começar com o `pdf2zh`, consulte o guia [Começar](https://pdf2zh-next.com/getting-started/). Ele o guiará pelo processo de instalação e uso básico.

### Idiomas Suportados

O `pdf2zh` suporta uma ampla gama de idiomas. Para uma lista completa, visite a página [Idiomas Suportados](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html).

### Contribuindo

Acolhemos contribuições da comunidade! Seja adicionando novos recursos, melhorando a documentação ou traduzindo conteúdo, sua ajuda é apreciada. Veja o [Guia de Contribuição](https://pdf2zh-next.com/community/FOR_TRANSLATORS.html) para mais detalhes.

### Comunidade

Junte-se à nossa comunidade para obter ajuda, compartilhar ideias e colaborar:
- [Discussões no GitHub](https://github.com/Alexander-Porter/pdf2zh/discussions)
- [Rastreador de Problemas](https://github.com/Alexander-Porter/pdf2zh/issues)

### Licença

O `pdf2zh` é lançado sob a [Licença MIT](https://opensource.org/licenses/MIT).
- `settings.basic.ignore_images` is ignored by this function; images are always ignored. Use `do_translate_async_stream` if you need image translation.
- `settings.basic.ignore_tables` is ignored by this function; tables are always ignored. Use `do_translate_async_stream` if you need table translation.
- `settings.basic.ignore_equations` is ignored by this function; equations are always ignored. Use `do_translate_async_stream` if you need equation translation.
- `settings.basic.ignore_format` is ignored by this function; formatting is always ignored. Use `do_translate_async_stream` if you need to preserve formatting.
- `settings.basic.chunk_size` is ignored by this function; chunking is not supported. Use `do_translate_async_stream` if you need chunking.
- `settings.basic.overlap` is ignored by this function; chunking is not supported. Use `do_translate_async_stream` if you need chunking.
- `settings.basic.concurrency` is ignored by this function; concurrency is not supported. Use `do_translate_async_stream` if you need concurrency.
- `settings.basic.retry` is ignored by this function; retry logic is not supported. Use `do_translate_async_stream` if you need retry logic.
- `settings.basic.timeout` is ignored by this function; timeout is not supported. Use `do_translate_async_stream` if you need timeout.
- `settings.basic.cache` is ignored by this function; caching is not supported. Use `do_translate_async_stream` if you need caching.
- `settings.basic.progress_callback` is ignored by this function; progress callbacks are not supported. Use `do_translate_async_stream` if you need progress callbacks.
- `settings.basic.custom_translator` is ignored by this function; custom translators are not supported. Use `do_translate_async_stream` if you need a custom translator.
- `settings.basic.translation_service` is ignored by this function; only the given `translation_service` is used.
- `settings.basic.api_key` is ignored by this function; only the given `api_key` is used.
- `settings.basic.source_lang` is ignored by this function; only the given `source_lang_code` is used.
- `settings.basic.target_lang` is ignored by this function; only the given `target_lang_code` is used.
- `settings.basic.ignore_lang` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_low` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_high` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_low` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_high` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_low` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_high` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto_low` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto_high` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto_auto` is ignored by this function; language detection is not supported. Use `do_translate_async_stream` if you need language detection.

---

### OUTPUT

- `settings.basic.input_files` é ignorado por esta função; apenas o `file` fornecido é traduzido.
- Se `settings.basic.debug` for True, a tradução é executada no processo principal; caso contrário, é executada em um subprocesso. O esquema de eventos é idêntico para ambos.
- `settings.basic.ignore_images` é ignorado por esta função; as imagens são sempre ignoradas. Use `do_translate_async_stream` se precisar de tradução de imagens.
- `settings.basic.ignore_tables` é ignorado por esta função; as tabelas são sempre ignoradas. Use `do_translate_async_stream` se precisar de tradução de tabelas.
- `settings.basic.ignore_equations` é ignorado por esta função; as equações são sempre ignoradas. Use `do_translate_async_stream` se precisar de tradução de equações.
- `settings.basic.ignore_format` é ignorado por esta função; a formatação é sempre ignorada. Use `do_translate_async_stream` se precisar preservar a formatação.
- `settings.basic.chunk_size` é ignorado por esta função; a divisão em partes não é suportada. Use `do_translate_async_stream` se precisar de divisão em partes.
- `settings.basic.overlap` é ignorado por esta função; a divisão em partes não é suportada. Use `do_translate_async_stream` se precisar de divisão em partes.
- `settings.basic.concurrency` é ignorado por esta função; a concorrência não é suportada. Use `do_translate_async_stream` se precisar de concorrência.
- `settings.basic.retry` é ignorado por esta função; a lógica de repetição não é suportada. Use `do_translate_async_stream` se precisar de lógica de repetição.
- `settings.basic.timeout` é ignorado por esta função; o tempo limite não é suportado. Use `do_translate_async_stream` se precisar de tempo limite.
- `settings.basic.cache` é ignorado por esta função; o cache não é suportado. Use `do_translate_async_stream` se precisar de cache.
- `settings.basic.progress_callback` é ignorado por esta função; callbacks de progresso não são suportados. Use `do_translate_async_stream` se precisar de callbacks de progresso.
- `settings.basic.custom_translator` é ignorado por esta função; tradutores personalizados não são suportados. Use `do_translate_async_stream` se precisar de um tradutor personalizado.
- `settings.basic.translation_service` é ignorado por esta função; apenas o `translation_service` fornecido é usado.
- `settings.basic.api_key` é ignorado por esta função; apenas a `api_key` fornecida é usada.
- `settings.basic.source_lang` é ignorado por esta função; apenas o `source_lang_code` fornecido é usado.
- `settings.basic.target_lang` é ignorado por esta função; apenas o `target_lang_code` fornecido é usado.
- `settings.basic.ignore_lang` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_low` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_high` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_low` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_high` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_low` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_high` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto_low` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto_high` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.
- `settings.basic.ignore_lang_conf_threshold_auto_auto_auto_auto` é ignorado por esta função; a detecção de idioma não é suportada. Use `do_translate_async_stream` se precisar de detecção de idioma.

The Event Stream Contract defines the format of the SSE (Server-Sent Events) messages that the server sends to the client. The server sends a stream of events, each of which is a JSON object.

#### Event Types

The server sends the following types of events:

- `message`: A message from the assistant.
- `error`: An error occurred.
- `done`: The assistant has finished generating the response.

#### Message Event

The `message` event contains a message from the assistant. The message is a JSON object with the following fields:

- `id`: The unique identifier for the message.
- `role`: The role of the message sender. Always `assistant`.
- `content`: The content of the message. This is a string that may contain markdown.
- `created_at`: The timestamp when the message was created.

Example:

```json
{
  "id": "msg_123",
  "role": "assistant",
  "content": "Hello! How can I help you today?",
  "created_at": 1620000000
}
```

#### Error Event

The `error` event contains an error message. The error is a JSON object with the following fields:

- `code`: The error code.
- `message`: The error message.

Example:

```json
{
  "code": "rate_limit_exceeded",
  "message": "Rate limit exceeded. Please try again later."
}
```

#### Done Event

The `done` event indicates that the assistant has finished generating the response. The event is a JSON object with the following fields:

- `id`: The unique identifier for the message that was generated.
- `model`: The model that was used to generate the response.
- `usage`: The usage statistics for the response. This is a JSON object with the following fields:
  - `prompt_tokens`: The number of tokens in the prompt.
  - `completion_tokens`: The number of tokens in the completion.
  - `total_tokens`: The total number of tokens.

Example:

```json
{
  "id": "msg_123",
  "model": "gpt-4",
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
  }
}
```

#### Event Stream Format

The server sends events in the following format:

```
event: message
data: {"id": "msg_123", "role": "assistant", "content": "Hello!", "created_at": 1620000000}

event: done
data: {"id": "msg_123", "model": "gpt-4", "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}}
```

Each event is separated by two newlines. The `event` field specifies the type of event, and the `data` field contains the JSON object for the event.

---

### TRANSLATION RESULT

### Contrato de Fluxo de Eventos

O Contrato de Fluxo de Eventos define o formato das mensagens SSE (Server-Sent Events) que o servidor envia para o cliente. O servidor envia um fluxo de eventos, cada um dos quais é um objeto JSON.

#### Tipos de Eventos

O servidor envia os seguintes tipos de eventos:

- `message`: Uma mensagem do assistente.
- `error`: Ocorreu um erro.
- `done`: O assistente terminou de gerar a resposta.

#### Evento de Mensagem

O evento `message` contém uma mensagem do assistente. A mensagem é um objeto JSON com os seguintes campos:

- `id`: O identificador único da mensagem.
- `role`: O papel do remetente da mensagem. Sempre `assistant`.
- `content`: O conteúdo da mensagem. Esta é uma string que pode conter markdown.
- `created_at`: O timestamp de quando a mensagem foi criada.

Exemplo:

```json
{
  "id": "msg_123",
  "role": "assistant",
  "content": "Olá! Como posso ajudá-lo hoje?",
  "created_at": 1620000000
}
```

#### Evento de Erro

O evento `error` contém uma mensagem de erro. O erro é um objeto JSON com os seguintes campos:

- `code`: O código de erro.
- `message`: A mensagem de erro.

Exemplo:

```json
{
  "code": "rate_limit_exceeded",
  "message": "Limite de taxa excedido. Por favor, tente novamente mais tarde."
}
```

#### Evento de Conclusão

O evento `done` indica que o assistente terminou de gerar a resposta. O evento é um objeto JSON com os seguintes campos:

- `id`: O identificador único da mensagem que foi gerada.
- `model`: O modelo que foi usado para gerar a resposta.
- `usage`: As estatísticas de uso para a resposta. Este é um objeto JSON com os seguintes campos:
  - `prompt_tokens`: O número de tokens no prompt.
  - `completion_tokens`: O número de tokens na conclusão.
  - `total_tokens`: O número total de tokens.

Exemplo:

```json
{
  "id": "msg_123",
  "model": "gpt-4",
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
  }
}
```

#### Formato do Fluxo de Eventos

O servidor envia eventos no seguinte formato:

```
event: message
data: {"id": "msg_123", "role": "assistant", "content": "Olá!", "created_at": 1620000000}

event: done
data: {"id": "msg_123", "model": "gpt-4", "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30}}
```

Cada evento é separado por duas novas linhas. O campo `event` especifica o tipo de evento, e o campo `data` contém o objeto JSON para o evento.
- `"start"`: Emitted once at the beginning.
- `"document_metadata"`: Contains metadata about the PDF document.
- `"page_start"`: Indicates the start of a new page.
- `"page_content"`: Contains the content of the page.
- `"page_translation"`: Contains the translated content of the page.
- `"page_end"`: Indicates the end of the current page.
- `"document_end"`: Emitted once at the end of the document.
- `"error"`: Emitted when an error occurs.

The async generator yields JSON-like dict events with the following types:
- `"start"`: Emitted once at the beginning.
- `"document_metadata"`: Contains metadata about the PDF document.
- `"page_start"`: Indicates the start of a new page.
- `"page_content"`: Contains the content of the page.
- `"page_translation"`: Contains the translated content of the page.
- `"page_end"`: Indicates the end of the current page.
- `"document_end"`: Emitted once at the end of the document.
- `"error"`: Emitted when an error occurs.

### Event Details

#### `"start"` Event

Emitted once when the translation process begins.

**Fields:**
- `type` (str): Always `"start"`.
- `timestamp` (str): ISO 8601 timestamp of when the event was emitted.

Example:
```json
{
  "type": "start",
  "timestamp": "2023-10-05T14:48:00.000Z"
}
```

#### `"document_metadata"` Event

Contains metadata about the PDF document being processed.

**Fields:**
- `type` (str): Always `"document_metadata"`.
- `metadata` (dict): A dictionary containing document metadata. Common keys include:
  - `"num_pages"` (int): The total number of pages in the document.
  - `"author"` (str, optional): The author of the document.
  - `"title"` (str, optional): The title of the document.
  - `"subject"` (str, optional): The subject of the document.
  - `"creator"` (str, optional): The creator of the document.

Example:
```json
{
  "type": "document_metadata",
  "metadata": {
    "num_pages": 10,
    "author": "John Doe",
    "title": "Example Document",
    "subject": "Example Subject",
    "creator": "Example Creator"
  }
}
```

#### `"page_start"` Event

Indicates the start of processing for a new page.

**Fields:**
- `type` (str): Always `"page_start"`.
- `page_number` (int): The page number (1-indexed).

Example:
```json
{
  "type": "page_start",
  "page_number": 1
}
```

#### `"page_content"` Event

Contains the extracted content from the page.

**Fields:**
- `type` (str): Always `"page_content"`.
- `page_number` (int): The page number (1-indexed).
- `content` (str): The extracted text content from the page.

Example:
```json
{
  "type": "page_content",
  "page_number": 1,
  "content": "This is the content of page 1."
}
```

#### `"page_translation"` Event

Contains the translated content of the page.

**Fields:**
- `type` (str): Always `"page_translation"`.
- `page_number` (int): The page number (1-indexed).
- `translation` (str): The translated text content of the page.

Example:
```json
{
  "type": "page_translation",
  "page_number": 1,
  "translation": "Este é o conteúdo da página 1."
}
```

#### `"page_end"` Event

Indicates the end of processing for the current page.

**Fields:**
- `type` (str): Always `"page_end"`.
- `page_number` (int): The page number (1-indexed).

Example:
```json
{
  "type": "page_end",
  "page_number": 1
}
```

#### `"document_end"` Event

Emitted once when the entire document has been processed.

**Fields:**
- `type` (str): Always `"document_end"`.
- `timestamp` (str): ISO 8601 timestamp of when the event was emitted.

Example:
```json
{
  "type": "document_end",
  "timestamp": "2023-10-05T14:50:00.000Z"
}
```

#### `"error"` Event

Emitted when an error occurs during processing.

**Fields:**
- `type` (str): Always `"error"`.
- `error` (str): A description of the error.
- `page_number` (int, optional): The page number where the error occurred, if applicable.

Example:
```json
{
  "type": "error",
  "error": "Failed to extract text from page 5",
  "page_number": 5
}
```

### Example Event Stream

Here's an example of a complete event stream for a document with two pages:

```json
{"type": "start", "timestamp": "2023-10-05T14:48:00.000Z"}
{"type": "document_metadata", "metadata": {"num_pages": 2, "title": "Example Document"}}
{"type": "page_start", "page_number": 1}
{"type": "page_content", "page_number": 1, "content": "Page 1 content."}
{"type": "page_translation", "page_number": 1, "translation": "Conteúdo da página 1."}
{"type": "page_end", "page_number": 1}
{"type": "page_start", "page_number": 2}
{"type": "page_content", "page_number": 2, "content": "Page 2 content."}
{"type": "page_translation", "page_number": 2, "translation": "Conteúdo da página 2."}
{"type": "page_end", "page_number": 2}
{"type": "document_end", "timestamp": "2023-10-05T14:48:30.000Z"}
```

---

### OUTPUT

O gerador assíncrono produz eventos em formato de dicionário semelhante a JSON com os seguintes tipos:
- `"start"`: Emitido uma vez no início.
- `"document_metadata"`: Contém metadados sobre o documento PDF.
- `"page_start"`: Indica o início de uma nova página.
- `"page_content"`: Contém o conteúdo da página.
- `"page_translation"`: Contém o conteúdo traduzido da página.
- `"page_end"`: Indica o fim da página atual.
- `"document_end"`: Emitido uma vez no final do documento.
- `"error"`: Emitido quando ocorre um erro.

### Detalhes dos Eventos

#### Evento `"start"`

Emitido uma vez quando o processo de tradução começa.

**Campos:**
- `type` (str): Sempre `"start"`.
- `timestamp` (str): Timestamp ISO 8601 de quando o evento foi emitido.

Exemplo:
```json
{
  "type": "start",
  "timestamp": "2023-10-05T14:48:00.000Z"
}
```

#### Evento `"document_metadata"`

Contém metadados sobre o documento PDF que está sendo processado.

**Campos:**
- `type` (str): Sempre `"document_metadata"`.
- `metadata` (dict): Um dicionário contendo metadados do documento. Chaves comuns incluem:
  - `"num_pages"` (int): O número total de páginas no documento.
  - `"author"` (str, opcional): O autor do documento.
  - `"title"` (str, opcional): O título do documento.
  - `"subject"` (str, opcional): O assunto do documento.
  - `"creator"` (str, opcional): O criador do documento.

Exemplo:
```json
{
  "type": "document_metadata",
  "metadata": {
    "num_pages": 10,
    "author": "John Doe",
    "title": "Exemplo de Documento",
    "subject": "Exemplo de Assunto",
    "creator": "Exemplo de Criador"
  }
}
```

#### Evento `"page_start"`

Indica o início do processamento de uma nova página.

**Campos:**
- `type` (str): Sempre `"page_start"`.
- `page_number` (int): O número da página (indexado a partir de 1).

Exemplo:
```json
{
  "type": "page_start",
  "page_number": 1
}
```

#### Evento `"page_content"`

Contém o conteúdo extraído da página.

**Campos:**
- `type` (str): Sempre `"page_content"`.
- `page_number` (int): O número da página (indexado a partir de 1).
- `content` (str): O conteúdo de texto extraído da página.

Exemplo:
```json
{
  "type": "page_content",
  "page_number": 1,
  "content": "Este é o conteúdo da página 1."
}
```

#### Evento `"page_translation"`

Contém o conteúdo traduzido da página.

**Campos:**
- `type` (str): Sempre `"page_translation"`.
- `page_number` (int): O número da página (indexado a partir de 1).
- `translation` (str): O conteúdo de texto traduzido da página.

Exemplo:
```json
{
  "type": "page_translation",
  "page_number": 1,
  "translation": "Este é o conteúdo da página 1."
}
```

#### Evento `"page_end"`

Indica o fim do processamento da página atual.

**Campos:**
- `type` (str): Sempre `"page_end"`.
- `page_number` (int): O número da página (indexado a partir de 1).

Exemplo:
```json
{
  "type": "page_end",
  "page_number": 1
}
```

#### Evento `"document_end"`

Emitido uma vez quando todo o documento foi processado.

**Campos:**
- `type` (str): Sempre `"document_end"`.
- `timestamp` (str): Timestamp ISO 8601 de quando o evento foi emitido.

Exemplo:
```json
{
  "type": "document_end",
  "timestamp": "2023-10-05T14:50:00.000Z"
}
```

#### Evento `"error"`

Emitido quando ocorre um erro durante o processamento.

**Campos:**
- `type` (str): Sempre `"error"`.
- `error` (str): Uma descrição do erro.
- `page_number` (int, opcional): O número da página onde o erro ocorreu, se aplicável.

Exemplo:
```json
{
  "type": "error",
  "error": "Falha ao extrair texto da página 5",
  "page_number": 5
}
```

### Exemplo de Fluxo de Eventos

Aqui está um exemplo de um fluxo de eventos completo para um documento com duas páginas:

```json
{"type": "start", "timestamp": "2023-10-05T14:48:00.000Z"}
{"type": "document_metadata", "metadata": {"num_pages": 2, "title": "Exemplo de Documento"}}
{"type": "page_start", "page_number": 1}
{"type": "page_content", "page_number": 1, "content": "Conteúdo da página 1."}
{"type": "page_translation", "page_number": 1, "translation": "Conteúdo da página 1."}
{"type": "page_end", "page_number": 1}
{"type": "page_start", "page_number": 2}
{"type": "page_content", "page_number": 2, "content": "Conteúdo da página 2."}
{"type": "page_translation", "page_number": 2, "translation": "Conteúdo da página 2."}
{"type": "page_end", "page_number": 2}
{"type": "document_end", "timestamp": "2023-10-05T14:48:30.000Z"}
```

- `part_index`: if applicable

### Example Event Stream

```json
{"type": "stage_summary", "stages": [{"name": "Parse PDF", "percent": 20.0}, {"name": "Translate", "percent": 70.0}, {"name": "Save PDF", "percent": 10.0}], "part_index": 0, "total_parts": 1}
{"type": "progress_start", "stage": "Parse PDF and Create Intermediate Representation", "stage_progress": 0.0, "overall_progress": 0.0, "part_index": 1, "total_parts": 1, "stage_current": 0, "stage_total": 100}
{"type": "progress_update", "stage": "Parse PDF and Create Intermediate Representation", "stage_progress": 50.0, "overall_progress": 10.0, "part_index": 1, "total_parts": 1, "stage_current": 50, "stage_total": 100}
{"type": "progress_end", "stage": "Parse PDF and Create Intermediate Representation", "stage_progress": 100.0, "overall_progress": 20.0, "part_index": 1, "total_parts": 1, "stage_current": 100, "stage_total": 100}
{"type": "progress_start", "stage": "Translate Paragraphs", "stage_progress": 0.0, "overall_progress": 20.0, "part_index": 1, "total_parts": 1, "stage_current": 0, "stage_total": 500}
{"type": "progress_update", "stage": "Translate Paragraphs", "stage_progress": 50.0, "overall_progress": 55.0, "part_index": 1, "total_parts": 1, "stage_current": 250, "stage_total": 500}
{"type": "progress_end", "stage": "Translate Paragraphs", "stage_progress": 100.0, "overall_progress": 90.0, "part_index": 1, "total_parts": 1, "stage_current": 500, "stage_total": 500}
{"type": "progress_start", "stage": "Save PDF", "stage_progress": 0.0, "overall_progress": 90.0, "part_index": 1, "total_parts": 1, "stage_current": 0, "stage_total": 10}
{"type": "progress_update", "stage": "Save PDF", "stage_progress": 50.0, "overall_progress": 95.0, "part_index": 1, "total_parts": 1, "stage_current": 5, "stage_total": 10}
{"type": "progress_end", "stage": "Save PDF", "stage_progress": 100.0, "overall_progress": 100.0, "part_index": 1, "total_parts": 1, "stage_current": 10, "stage_total": 10}
{"type": "finish", "translate_result": {"original_pdf_path": "/path/to/input.pdf", "mono_pdf_path": "/path/to/output_mono.pdf", "dual_pdf_path": "/path/to/output_dual.pdf", "no_watermark_mono_pdf_path": null, "no_watermark_dual_pdf_path": null, "auto_extracted_glossary_path": "/path/to/glossary.csv", "total_seconds": 123.45, "peak_memory_usage": 256.0}}
```

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

- Evento de resumo de estágio: `stage_summary` (opcional, pode aparecer primeiro)
  - Campos
    - `type`: "stage_summary"
    - `stages`: lista de objetos `{ "name": str, "percent": float }` descrevendo a distribuição estimada de trabalho
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
    - `stage_current`: passo atual dentro do estágio
    - `stage_total`: total de passos dentro do estágio

- Evento de conclusão: `finish`
  - Campos
    - `type`: "finish"
    - `translate_result`: um **objeto** fornecendo saídas finais (NOTA: não um dicionário, mas uma instância de classe)
      - `original_pdf_path`: Caminho para o PDF de entrada
      - `mono_pdf_path`: Caminho para o PDF traduzido monolíngue (ou None)
      - `dual_pdf_path`: Caminho para o PDF traduzido bilíngue (ou None)
      - `no_watermark_mono_pdf_path`: Caminho para a saída monolíngue sem marca d'água (se produzida), caso contrário None
      - `no_watermark_dual_pdf_path`: Caminho para a saída bilíngue sem marca d'água (se produzida), caso contrário None
      - `auto_extracted_glossary_path`: Caminho para o CSV do glossário extraído automaticamente (ou None)
      - `total_seconds`: segundos decorridos (float)
      - `peak_memory_usage`: uso máximo aproximado de memória durante a tradução (float; unidades dependentes da implementação)

- Evento de erro: `error`
  - Campos
    - `type`: "error"
    - `error`: mensagem de erro legível por humanos
    - `error_type`: um de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details`: detalhes opcionais (por exemplo, erro original ou traceback)
    - `part_index`: se aplicável

### Exemplo de Fluxo de Eventos

```json
{"type": "stage_summary", "stages": [{"name": "Analisar PDF", "percent": 20.0}, {"name": "Traduzir", "percent": 70.0}, {"name": "Salvar PDF", "percent": 10.0}], "part_index": 0, "total_parts": 1}
{"type": "progress_start", "stage": "Analisar PDF e Criar Representação Intermediária", "stage_progress": 0.0, "overall_progress": 0.0, "part_index": 1, "total_parts": 1, "stage_current": 0, "stage_total": 100}
{"type": "progress_update", "stage": "Analisar PDF e Criar Representação Intermediária", "stage_progress": 50.0, "overall_progress": 10.0, "part_index": 1, "total_parts": 1, "stage_current": 50, "stage_total": 100}
{"type": "progress_end", "stage": "Analisar PDF e Criar Representação Intermediária", "stage_progress": 100.0, "overall_progress": 20.0, "part_index": 1, "total_parts": 1, "stage_current": 100, "stage_total": 100}
{"type": "progress_start", "stage": "Traduzir Parágrafos", "stage_progress": 0.0, "overall_progress": 20.0, "part_index": 1, "total_parts": 1, "stage_current": 0, "stage_total": 500}
{"type": "progress_update", "stage": "Traduzir Parágrafos", "stage_progress": 50.0, "overall_progress": 55.0, "part_index": 1, "total_parts": 1, "stage_current": 250, "stage_total": 500}
{"type": "progress_end", "stage": "Traduzir Parágrafos", "stage_progress": 100.0, "overall_progress": 90.0, "part_index": 1, "total_parts": 1, "stage_current": 500, "stage_total": 500}
{"type": "progress_start", "stage": "Salvar PDF", "stage_progress": 0.0, "overall_progress": 90.0, "part_index": 1, "total_parts": 1, "stage_current": 0, "stage_total": 10}
{"type": "progress_update", "stage": "Salvar PDF", "stage_progress": 50.0, "overall_progress": 95.0, "part_index": 1, "total_parts": 1, "stage_current": 5, "stage_total": 10}
{"type": "progress_end", "stage": "Salvar PDF", "stage_progress": 100.0, "overall_progress": 100.0, "part_index": 1, "total_parts": 1, "stage_current": 10, "stage_total": 10}
{"type": "finish", "translate_result": {"original_pdf_path": "/caminho/para/input.pdf", "mono_pdf_path": "/caminho/para/output_mono.pdf", "dual_pdf_path": "/caminho/para/output_dual.pdf", "no_watermark_mono_pdf_path": null, "no_watermark_dual_pdf_path": null, "auto_extracted_glossary_path": "/caminho/para/glossary.csv", "total_seconds": 123.45, "peak_memory_usage": 256.0}}
```

The `do_translate_async_stream` function is designed to handle PDF files and stream the translated content in real-time. It uses an asynchronous generator to yield chunks of translated text as they become available. This is particularly useful for large files or applications that require immediate feedback.

### Key Features

- **Real-time Streaming**: The function yields translated chunks as soon as they are available, allowing for progressive display of the translation.
- **Asynchronous Operation**: Built with async/await for non-blocking operations, making it suitable for web applications and other async environments.
- **Flexible Service Integration**: Supports multiple translation services (Google, OpenAI, Azure, etc.) through a unified interface.
- **Customizable Parameters**: Allows specification of source and target languages, translation service, API keys, and additional options via kwargs.

### Usage in Web Applications

When integrated into a web application, this function can be used to power real-time translation features. For example, as a user uploads a PDF, the application can start displaying translated text almost immediately, enhancing the user experience.

### Error Handling

The function includes basic error handling for common issues such as file not found, unsupported translation service, or API errors. Errors are raised as exceptions and should be caught by the calling code.

### Performance Considerations

- **Chunk Size**: The size of each yielded chunk can vary based on the translation service and the content of the PDF.
- **Memory Usage**: Since the function streams the output, it maintains a low memory footprint even for large documents.
- **Network Latency**: The speed of translation depends on the chosen service and network conditions.

### Example Integration

Here's how you might integrate `do_translate_async_stream` into a FastAPI application to create a streaming translation endpoint:

```python
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
import asyncio
from pdf2zh import do_translate_async_stream

app = FastAPI()

@app.post("/translate-stream/")
async def translate_stream(file: UploadFile):
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())
    
    # Create async generator for translation stream
    async def generate():
        async for chunk in do_translate_async_stream(
            file_path="temp.pdf",
            source_lang_code="en",
            target_lang_code="es",
            translation_service="google"
        ):
            yield chunk
    
    return StreamingResponse(generate(), media_type="text/plain")
```

This endpoint accepts a PDF upload and streams the translated text back to the client in real-time.

---

### OUTPUT

Comportamento importante: A função `do_translate_async_stream` é projetada para lidar com arquivos PDF e transmitir o conteúdo traduzido em tempo real. Ela usa um gerador assíncrono para produzir partes do texto traduzido à medida que ficam disponíveis. Isso é particularmente útil para arquivos grandes ou aplicações que exigem feedback imediato.

### Características Principais

- **Transmissão em Tempo Real**: A função produz partes traduzidas assim que estão disponíveis, permitindo a exibição progressiva da tradução.
- **Operação Assíncrona**: Construída com async/await para operações não bloqueantes, tornando-a adequada para aplicações web e outros ambientes assíncronos.
- **Integração Flexível de Serviços**: Suporta vários serviços de tradução (Google, OpenAI, Azure, etc.) através de uma interface unificada.
- **Parâmetros Personalizáveis**: Permite a especificação de idiomas de origem e destino, serviço de tradução, chaves de API e opções adicionais via kwargs.

### Uso em Aplicações Web

Quando integrada em uma aplicação web, esta função pode ser usada para alimentar recursos de tradução em tempo real. Por exemplo, enquanto um usuário faz upload de um PDF, a aplicação pode começar a exibir o texto traduzido quase imediatamente, melhorando a experiência do usuário.

### Tratamento de Erros

A função inclui tratamento básico de erros para problemas comuns, como arquivo não encontrado, serviço de tradução não suportado ou erros de API. Os erros são levantados como exceções e devem ser capturados pelo código chamador.

### Considerações de Desempenho

- **Tamanho da Parte**: O tamanho de cada parte produzida pode variar com base no serviço de tradução e no conteúdo do PDF.
- **Uso de Memória**: Como a função transmite a saída, ela mantém uma pegada de memória baixa mesmo para documentos grandes.
- **Latência de Rede**: A velocidade da tradução depende do serviço escolhido e das condições da rede.

### Exemplo de Integração

Aqui está como você pode integrar `do_translate_async_stream` em uma aplicação FastAPI para criar um endpoint de tradução em streaming:

```python
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
import asyncio
from pdf2zh import do_translate_async_stream

app = FastAPI()

@app.post("/translate-stream/")
async def translate_stream(file: UploadFile):
    # Salva o arquivo enviado temporariamente
    with open("temp.pdf", "wb") as f:
        f.write(await file.read())
    
    # Cria um gerador assíncrono para o fluxo de tradução
    async def generate():
        async for chunk in do_translate_async_stream(
            file_path="temp.pdf",
            source_lang_code="en",
            target_lang_code="es",
            translation_service="google"
        ):
            yield chunk
    
    return StreamingResponse(generate(), media_type="text/plain")
```

Este endpoint aceita um upload de PDF e transmite o texto traduzido de volta para o cliente em tempo real.
- The generator will not yield any more events after `finish`.
- If you need to cancel the translation, you can call the `.close()` method on the generator.

---

### TRANSLATION RESULT

- Um `stage_summary` opcional pode ser emitido antes do progresso começar.
- Em certas falhas, o gerador primeiro irá produzir um evento `error` e depois levantar uma exceção derivada de `TranslationError`. Você deve tanto verificar eventos de erro quanto estar preparado para capturar exceções.
- Eventos `progress_update` podem se repetir com valores idênticos; os consumidores devem fazer debounce se necessário.
- Pare de consumir o fluxo quando receber um evento `finish`.
- O gerador não produzirá mais eventos após `finish`.
- Se precisar cancelar a tradução, pode chamar o método `.close()` no gerador.
- ### Example Event Shapes: This is a list of example event shapes.

!!! note
    The examples below are for illustration purposes only. The actual events may vary.

#### Example 1: Simple Event

```json
{
  "event_id": "12345",
  "event_type": "user_login",
  "timestamp": "2023-10-05T14:48:00Z",
  "user_id": "user_67890",
  "ip_address": "192.168.1.1"
}
```

#### Example 2: Event with Nested Data

```json
{
  "event_id": "67890",
  "event_type": "purchase",
  "timestamp": "2023-10-05T15:30:00Z",
  "user": {
    "user_id": "user_12345",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_1",
      "quantity": 2,
      "price": 19.99
    },
    {
      "product_id": "prod_2",
      "quantity": 1,
      "price": 9.99
    }
  ],
  "total_amount": 49.97
}
```

#### Example 3: Event with Array of Strings

```json
{
  "event_id": "abcde",
  "event_type": "search",
  "timestamp": "2023-10-05T16:15:00Z",
  "query": "example query",
  "filters": ["filter1", "filter2", "filter3"],
  "results_count": 15
}
```

---

### OUTPUT

### Exemplo de Formas de Evento

Esta é uma lista de exemplo de formas de evento.

!!! note
    Os exemplos abaixo são apenas para fins de ilustração. Os eventos reais podem variar.

#### Exemplo 1: Evento Simples

```json
{
  "event_id": "12345",
  "event_type": "user_login",
  "timestamp": "2023-10-05T14:48:00Z",
  "user_id": "user_67890",
  "ip_address": "192.168.1.1"
}
```

#### Exemplo 2: Evento com Dados Aninhados

```json
{
  "event_id": "67890",
  "event_type": "purchase",
  "timestamp": "2023-10-05T15:30:00Z",
  "user": {
    "user_id": "user_12345",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_1",
      "quantity": 2,
      "price": 19.99
    },
    {
      "product_id": "prod_2",
      "quantity": 1,
      "price": 9.99
    }
  ],
  "total_amount": 49.97
}
```

#### Exemplo 3: Evento com Array de Strings

```json
{
  "event_id": "abcde",
  "event_type": "search",
  "timestamp": "2023-10-05T16:15:00Z",
  "query": "example query",
  "filters": ["filter1", "filter2", "filter3"],
  "results_count": 15
}
```
- ### Using the WebUI: The WebUI provides a user-friendly interface for translating PDF documents. You can access it at [https://pdf2zh-next.com](https://pdf2zh-next.com).

#### Steps to Use the WebUI

1. **Open the WebUI**: Navigate to [https://pdf2zh-next.com](https://pdf2zh-next.com) in your web browser.

2. **Upload a PDF File**: Click the **Upload** button and select the PDF file you want to translate.

3. **Select Languages**: Choose the source and target languages from the dropdown menus. The source language can be set to **Auto-Detect** if you are unsure.

4. **Start Translation**: Click the **Translate** button to begin the translation process.

5. **View Results**: Once the translation is complete, the translated text will be displayed on the screen. You can then download the translated document or copy the text to clipboard.

#### Features

- **Auto-Detect Language**: The WebUI can automatically detect the source language of your PDF document.
- **Multiple Translation Services**: You can choose from multiple translation services, including Google Translate, DeepL, and OpenAI.
- **Real-Time Progress**: The translation progress is displayed in real-time.
- **Error Handling**: If an error occurs, the WebUI will display an error message with suggestions for resolution.

#### Limitations

- The WebUI may not handle very large PDF files (e.g., over 100 pages) efficiently. For large files, consider using the [Command Line Interface](https://pdf2zh-next.com/getting-started/USAGE_cli.html).
- The WebUI requires an internet connection to use translation services.

---

### OUTPUT

### Usando a WebUI

A WebUI fornece uma interface amigável para traduzir documentos PDF. Você pode acessá-la em [https://pdf2zh-next.com](https://pdf2zh-next.com).

#### Passos para Usar a WebUI

1. **Abra a WebUI**: Navegue para [https://pdf2zh-next.com](https://pdf2zh-next.com) no seu navegador web.

2. **Faça Upload de um Arquivo PDF**: Clique no botão **Upload** e selecione o arquivo PDF que deseja traduzir.

3. **Selecione os Idiomas**: Escolha os idiomas de origem e destino nos menus suspensos. O idioma de origem pode ser definido como **Auto-Detectar** se você não tiver certeza.

4. **Inicie a Tradução**: Clique no botão **Traduzir** para iniciar o processo de tradução.

5. **Visualize os Resultados**: Uma vez que a tradução esteja concluída, o texto traduzido será exibido na tela. Você pode então baixar o documento traduzido ou copiar o texto para a área de transferência.

#### Funcionalidades

- **Auto-Detecção de Idioma**: A WebUI pode detectar automaticamente o idioma de origem do seu documento PDF.
- **Múltiplos Serviços de Tradução**: Você pode escolher entre vários serviços de tradução, incluindo Google Translate, DeepL e OpenAI.
- **Progresso em Tempo Real**: O progresso da tradução é exibido em tempo real.
- **Tratamento de Erros**: Se ocorrer um erro, a WebUI exibirá uma mensagem de erro com sugestões para resolução.

#### Limitações

- A WebUI pode não lidar eficientemente com arquivos PDF muito grandes (por exemplo, mais de 100 páginas). Para arquivos grandes, considere usar a [Interface de Linha de Comando](https://pdf2zh-next.com/getting-started/USAGE_cli.html).
- A WebUI requer uma conexão com a internet para usar os serviços de tradução.
- ### Notes & Best Practices: - **Check for Existing Translations**: Before starting a new translation, check the [Supported Languages](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) page to see if the language is already supported or if there's an ongoing effort.

- **Use the Official Glossary**: To maintain consistency, always refer to the project's [official glossary](https://github.com/PDFMathTranslate/pdf2zh-next/blob/main/docs/GLOSSARY.md) for key terms.

- **Consistency in Terminology**: Ensure that the same term is translated consistently throughout the documentation.

- **Cultural Adaptation**: Adapt examples and references to be culturally relevant to the target audience when necessary.

- **Keep It Simple**: Use clear and straightforward language. Avoid overly complex sentences.

- **Test Your Translations**: After translating, test the functionality to ensure that the translated text works well in the application context.

- **Collaborate**: Use pull requests and issues to collaborate with other translators and maintainers.

### Translation Style Guide

1. **Tone**: Maintain a professional and helpful tone. The documentation should be approachable yet authoritative.

2. **Voice**: Use active voice whenever possible to make the text more engaging and easier to understand.

3. **Punctuation**: Follow the punctuation rules of the target language. For example, in Chinese, use full-width punctuation marks.

4. **Formatting**: Preserve the original formatting, including code blocks, links, and headings. Only translate the textual content.

5. **Accessibility**: Ensure that the translation is accessible, using clear language and avoiding jargon unless it is well-defined.

---

### OUTPUT

### Notas e Melhores Práticas

- **Verifique Traduções Existentes**: Antes de iniciar uma nova tradução, verifique a página [Idiomas Suportados](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) para ver se o idioma já é suportado ou se há um esforço em andamento.

- **Use o Glossário Oficial**: Para manter a consistência, consulte sempre o [glossário oficial](https://github.com/PDFMathTranslate/pdf2zh-next/blob/main/docs/GLOSSARY.md) do projeto para termos-chave.

- **Consistência na Terminologia**: Certifique-se de que o mesmo termo seja traduzido de forma consistente em toda a documentação.

- **Adaptação Cultural**: Adapte exemplos e referências para serem culturalmente relevantes para o público-alvo quando necessário.

- **Mantenha Simples**: Use linguagem clara e direta. Evite frases excessivamente complexas.

- **Teste Suas Traduções**: Após traduzir, teste a funcionalidade para garantir que o texto traduzido funcione bem no contexto da aplicação.

- **Colabore**: Use pull requests e issues para colaborar com outros tradutores e mantenedores.

### Guia de Estilo de Tradução

1. **Tom**: Mantenha um tom profissional e prestativo. A documentação deve ser acessível, mas autoritária.

2. **Voz**: Use voz ativa sempre que possível para tornar o texto mais envolvente e fácil de entender.

3. **Pontuação**: Siga as regras de pontuação do idioma de destino. Por exemplo, em português, use sinais de pontuação de largura total.

4. **Formatação**: Preserve a formatação original, incluindo blocos de código, links e cabeçalhos. Traduza apenas o conteúdo textual.

5. **Acessibilidade**: Certifique-se de que a tradução seja acessível, usando linguagem clara e evitando jargões, a menos que estejam bem definidos.

{#minimal-usage-example-async}

The following code demonstrates the most basic usage of `pdf2zh`:

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    # Initialize the client
    client = pdf2zh_async()

    # Upload a PDF file and process it
    result = await client.process("sample.pdf")

    # Print the translated text
    print(result)

asyncio.run(main())
```

### Minimal Usage Example (Sync) {#minimal-usage-example-sync}

If you prefer synchronous code, here's the equivalent example:

```python
from pdf2zh import pdf2zh_sync

# Initialize the client
client = pdf2zh_sync()

# Upload a PDF file and process it
result = client.process("sample.pdf")

# Print the translated text
print(result)
```

### Processing Options {#processing-options}

The `process` method accepts several parameters to customize the translation:

```python
result = await client.process(
    "document.pdf",
    target_lang="pt",  # Target language (default: "zh")
    source_lang="en",  # Source language (auto-detected if not specified)
    translation_service="google",  # Translation service to use
    ignore_format=True,  # Ignore formatting (text only)
    ignore_images=True,  # Skip image processing
    ignore_tables=True,  # Skip table processing
    ignore_equations=True,  # Skip equation processing
)
```

### Handling Large Documents {#handling-large-documents}

For large PDF documents, you can process them in chunks to avoid memory issues:

```python
# Process with chunking enabled
result = await client.process(
    "large_document.pdf",
    chunk_size=10,  # Number of pages per chunk
    overlap=1,      # Overlap pages between chunks
)
```

### Error Handling {#error-handling}

Always wrap your processing in try-catch blocks:

```python
try:
    result = await client.process("document.pdf")
    print(result)
except Exception as e:
    print(f"Error processing document: {e}")
```

### Using Different Translation Services {#using-different-translation-services}

`pdf2zh` supports multiple translation services. You can specify which one to use:

```python
result = await client.process(
    "document.pdf",
    translation_service="google",  # Options: "google", "deepl", "openai", "azure"
    # Service-specific API keys are read from environment variables
)
```

See [Translation Services Documentation](translation-services.md) for setup instructions.

### Custom Translation Functions {#custom-translation-functions}

You can provide your own translation function for maximum flexibility:

```python
async def my_translator(text, source_lang, target_lang):
    # Your custom translation logic here
    return translated_text

result = await client.process(
    "document.pdf",
    custom_translator=my_translator
)
```

### Progress Tracking {#progress-tracking}

Track the progress of document processing:

```python
def progress_callback(current, total):
    print(f"Processed {current}/{total} pages")

result = await client.process(
    "document.pdf",
    progress_callback=progress_callback
)
```

### Saving Results {#saving-results}

Save the translated document to a file:

```python
result = await client.process("document.pdf")

# Save as text file
with open("translated.txt", "w", encoding="utf-8") as f:
    f.write(result)

# Save as PDF (preserves layout)
await client.save_as_pdf(result, "translated.pdf")
```

### Advanced Configuration {#advanced-configuration}

For advanced users, you can configure various aspects of the processing:

```python
client = pdf2zh_async(
    timeout=300,           # Request timeout in seconds
    max_retries=3,         # Maximum retry attempts
    concurrent_requests=5, # Number of concurrent translation requests
    cache_enabled=True,    # Enable caching of translations
)
```

Check the [Advanced Options](advanced-options.md) documentation for more details.

---

### TRANSLATION RESULT

### Exemplo Mínimo de Uso (Assíncrono) {#exemplo-mínimo-de-uso-assíncrono}

O código a seguir demonstra o uso mais básico do `pdf2zh`:

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    # Inicializa o cliente
    client = pdf2zh_async()

    # Faz upload de um arquivo PDF e o processa
    result = await client.process("sample.pdf")

    # Imprime o texto traduzido
    print(result)

asyncio.run(main())
```

### Exemplo Mínimo de Uso (Síncrono) {#exemplo-mínimo-de-uso-síncrono}

Se você prefere código síncrono, aqui está o exemplo equivalente:

```python
from pdf2zh import pdf2zh_sync

# Inicializa o cliente
client = pdf2zh_sync()

# Faz upload de um arquivo PDF e o processa
result = client.process("sample.pdf")

# Imprime o texto traduzido
print(result)
```

### Opções de Processamento {#opções-de-processamento}

O método `process` aceita vários parâmetros para personalizar a tradução:

```python
result = await client.process(
    "document.pdf",
    target_lang="pt",  # Idioma de destino (padrão: "zh")
    source_lang="en",  # Idioma de origem (detectado automaticamente se não especificado)
    translation_service="google",  # Serviço de tradução a ser usado
    ignore_format=True,  # Ignorar formatação (apenas texto)
    ignore_images=True,  # Pular processamento de imagens
    ignore_tables=True,  # Pular processamento de tabelas
    ignore_equations=True,  # Pular processamento de equações
)
```

### Manipulação de Documentos Grandes {#manipulação-de-documentos-grandes}

Para documentos PDF grandes, você pode processá-los em partes para evitar problemas de memória:

```python
# Processa com divisão em partes habilitada
result = await client.process(
    "large_document.pdf",
    chunk_size=10,  # Número de páginas por parte
    overlap=1,      # Sobreposição de páginas entre partes
)
```

### Tratamento de Erros {#tratamento-de-erros}

Sempre envolva seu processamento em blocos try-catch:

```python
try:
    result = await client.process("document.pdf")
    print(result)
except Exception as e:
    print(f"Erro ao processar documento: {e}")
```

### Usando Diferentes Serviços de Tradução {#usando-diferentes-serviços-de-tradução}

O `pdf2zh` suporta vários serviços de tradução. Você pode especificar qual usar:

```python
result = await client.process(
    "document.pdf",
    translation_service="google",  # Opções: "google", "deepl", "openai", "azure"
    # Chaves de API específicas do serviço são lidas das variáveis de ambiente
)
```

Consulte a [Documentação dos Serviços de Tradução](translation-services.md) para instruções de configuração.

### Funções de Tradução Personalizadas {#funções-de-tradução-personalizadas}

Você pode fornecer sua própria função de tradução para máxima flexibilidade:

```python
async def my_translator(text, source_lang, target_lang):
    # Sua lógica de tradução personalizada aqui
    return translated_text

result = await client.process(
    "document.pdf",
    custom_translator=my_translator
)
```

### Acompanhamento de Progresso {#acompanhamento-de-progresso}

Acompanhe o progresso do processamento do documento:

```python
def progress_callback(current, total):
    print(f"Páginas processadas {current}/{total}")

result = await client.process(
    "document.pdf",
    progress_callback=progress_callback
)
```

### Salvando Resultados {#salvando-resultados}

Salve o documento traduzido em um arquivo:

```python
result = await client.process("document.pdf")

# Salva como arquivo de texto
with open("translated.txt", "w", encoding="utf-8") as f:
    f.write(result)

# Salva como PDF (preserva layout)
await client.save_as_pdf(result, "translated.pdf")
```

### Configuração Avançada {#configuração-avançada}

Para usuários avançados, você pode configurar vários aspectos do processamento:

```python
client = pdf2zh_async(
    timeout=300,           # Tempo limite da solicitação em segundos
    max_retries=3,         # Tentativas máximas de repetição
    concurrent_requests=5, # Número de solicitações de tradução simultâneas
    cache_enabled=True,    # Habilita cache de traduções
)
```

Verifique a documentação de [Opções Avançadas](advanced-options.md) para mais detalhes.
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

If you want to cancel the translation, you can click the **Cancel** button in the upper right corner of the translation progress pop-up window.

### Error Handling

If an error occurs during the translation process, the system will automatically stop the translation and display an error message. You can check the error message and try to resolve the issue.

### Retry

If the translation fails, you can click the **Retry** button to restart the translation.

### Save Logs

If you encounter an error, you can click the **Save Logs** button to save the error logs for troubleshooting.

### Support

If you cannot resolve the issue, you can seek help in the [Community](https://github.com/Alexander-Porter/pdf2zh/discussions) or [FAQ](https://pdf2zh-next.com/faq.html).

---

### OUTPUT

### Cancelamento

Se você deseja cancelar a tradução, pode clicar no botão **Cancelar** no canto superior direito da janela pop-up de progresso da tradução.

### Tratamento de Erros

Se ocorrer um erro durante o processo de tradução, o sistema irá parar automaticamente a tradução e exibir uma mensagem de erro. Você pode verificar a mensagem de erro e tentar resolver o problema.

### Tentar Novamente

Se a tradução falhar, você pode clicar no botão **Tentar Novamente** para reiniciar a tradução.

### Salvar Logs

Se você encontrar um erro, pode clicar no botão **Salvar Logs** para salvar os logs de erro para solução de problemas.

### Suporte

Se você não conseguir resolver o problema, pode buscar ajuda na [Comunidade](https://github.com/Alexander-Porter/pdf2zh/discussions) ou nas [Perguntas frequentes](https://pdf2zh-next.com/faq.html).
- ### Example Event Shapes: Este é uma lista de formatos de evento de exemplo.

!!! note
    Os exemplos abaixo são apenas para fins de ilustração. Os eventos reais podem variar.

#### Exemplo 1: Evento Simples

```json
{
  "event_id": "12345",
  "event_type": "user_login",
  "timestamp": "2023-10-05T14:48:00Z",
  "user_id": "user_67890",
  "ip_address": "192.168.1.1"
}
```

#### Exemplo 2: Evento com Dados Aninhados

```json
{
  "event_id": "67890",
  "event_type": "purchase",
  "timestamp": "2023-10-05T15:30:00Z",
  "user": {
    "user_id": "user_12345",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_1",
      "quantity": 2,
      "price": 19.99
    },
    {
      "product_id": "prod_2",
      "quantity": 1,
      "price": 9.99
    }
  ],
  "total_amount": 49.97
}
```

#### Exemplo 3: Evento com Array de Strings

```json
{
  "event_id": "abcde",
  "event_type": "search",
  "timestamp": "2023-10-05T16:15:00Z",
  "query": "exemplo de consulta",
  "filters": ["filtro1", "filtro2", "filtro3"],
  "results_count": 15
}
```

---

### OUTPUT

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

This is a list of example event shapes.

!!! note
    The examples below are for illustration purposes only. The actual events may vary.

#### Example 1: Simple Event

```json
{
  "event_id": "12345",
  "event_type": "user_login",
  "timestamp": "2023-10-05T14:48:00Z",
  "user_id": "user_67890",
  "ip_address": "192.168.1.1"
}
```

#### Example 2: Event with Nested Data

```json
{
  "event_id": "67890",
  "event_type": "purchase",
  "timestamp": "2023-10-05T15:30:00Z",
  "user": {
    "user_id": "user_12345",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_1",
      "quantity": 2,
      "price": 19.99
    },
    {
      "product_id": "prod_2",
      "quantity": 1,
      "price": 9.99
    }
  ],
  "total_amount": 49.97
}
```

#### Example 3: Event with Array of Strings

```json
{
  "event_id": "abcde",
  "event_type": "search",
  "timestamp": "2023-10-05T16:15:00Z",
  "query": "example query",
  "filters": ["filter1", "filter2", "filter3"],
  "results_count": 15
}
```

---

### OUTPUT LANGUAGE

pt
json
{
  "type": "stage_summary",
  "stage": "translation",
  "status": "completed",
  "progress": 100,
  "details": {
    "total_pages": 10,
    "translated_pages": 10,
    "elapsed_time": "00:05:30"
  }
}
```

Page processing event (example):

```json
{
  "type": "page_processing",
  "page_number": 5,
  "status": "completed",
  "details": {
    "translated_text": "This is the translated content of page 5...",
    "source_text": "This is the original content of page 5...",
    "elapsed_time": "00:00:45"
  }
}
```

Error event (example):

```json
{
  "type": "error",
  "stage": "translation",
  "error_code": "translation_failed",
  "error_message": "Failed to translate page 5 due to network error.",
  "details": {
    "page_number": 5,
    "suggestion": "Please check your internet connection and try again."
  }
}
```

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

Evento de resumo de estágio (exemplo):

```json
{
  "type": "stage_summary",
  "stage": "translation",
  "status": "completed",
  "progress": 100,
  "details": {
    "total_pages": 10,
    "translated_pages": 10,
    "elapsed_time": "00:05:30"
  }
}
```

Evento de processamento de página (exemplo):

```json
{
  "type": "page_processing",
  "page_number": 5,
  "status": "completed",
  "details": {
    "translated_text": "Este é o conteúdo traduzido da página 5...",
    "source_text": "Este é o conteúdo original da página 5...",
    "elapsed_time": "00:00:45"
  }
}
```

Evento de erro (exemplo):

```json
{
  "type": "error",
  "stage": "translation",
  "error_code": "translation_failed",
  "error_message": "Falha ao traduzir a página 5 devido a erro de rede.",
  "details": {
    "page_number": 5,
    "suggestion": "Por favor, verifique sua conexão com a internet e tente novamente."
  }
}
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

json
{
  "type": "progress",
  "data": {
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
```

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

Evento de progresso (exemplo):

```json
{
  "type": "progress",
  "data": {
    "progress": 0.5,
    "message": "Processando página 10 de 20"
  }
}
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

json
{
  "id": "msg_1234567890",
  "object": "chat.completion",
  "created": 1700000000,
  "model": "gpt-4-turbo-preview",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I help you today?"
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
  },
  "system_fingerprint": "fp_1234567890"
}
```

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

Evento de conclusão (exemplo): 

```json
{
  "id": "msg_1234567890",
  "object": "chat.completion",
  "created": 1700000000,
  "model": "gpt-4-turbo-preview",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Olá! Como posso ajudá-lo hoje?"
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
  },
  "system_fingerprint": "fp_1234567890"
}
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

The `error` event contains an error message. The error is a JSON object with the following fields:

- `code`: The error code.
- `message`: The error message.

Example:

```json
{
  "code": "rate_limit_exceeded",
  "message": "Rate limit exceeded. Please try again later."
}
```

---

### OUTPUT

Evento de erro (exemplo): O evento `error` contém uma mensagem de erro. O erro é um objeto JSON com os seguintes campos:

- `code`: O código de erro.
- `message`: A mensagem de erro.

Exemplo:

```json
{
  "code": "rate_limit_exceeded",
  "message": "Limite de taxa excedido. Por favor, tente novamente mais tarde."
}
```
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

- **Check for Existing Translations**: Before starting a new translation, check the [Supported Languages](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) page to see if the language is already supported or if there's an ongoing effort.

- **Use the Official Glossary**: To maintain consistency, always refer to the project's [official glossary](https://github.com/PDFMathTranslate/pdf2zh-next/blob/main/docs/GLOSSARY.md) for key terms.

- **Consistency in Terminology**: Ensure that the same term is translated consistently throughout the documentation.

- **Cultural Adaptation**: Adapt examples and references to be culturally relevant to the target audience when necessary.

- **Keep It Simple**: Use clear and straightforward language. Avoid overly complex sentences.

- **Test Your Translations**: After translating, test the functionality to ensure that the translated text works well in the application context.

- **Collaborate**: Use pull requests and issues to collaborate with other translators and maintainers.

### Translation Style Guide

1. **Tone**: Maintain a professional and helpful tone. The documentation should be approachable yet authoritative.

2. **Voice**: Use active voice whenever possible to make the text more engaging and easier to understand.

3. **Punctuation**: Follow the punctuation rules of the target language. For example, in Chinese, use full-width punctuation marks.

4. **Formatting**: Preserve the original formatting, including code blocks, links, and headings. Only translate the textual content.

5. **Accessibility**: Ensure that the translation is accessible, using clear language and avoiding jargon unless it is well-defined.

---

### OUTPUT LANGUAGE

pt

---

### OUTPUT

### Notas e Melhores Práticas

- **Verifique Traduções Existentes**: Antes de iniciar uma nova tradução, verifique a página [Idiomas Suportados](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) para ver se o idioma já é suportado ou se há um esforço em andamento.

- **Use o Glossário Oficial**: Para manter a consistência, consulte sempre o [glossário oficial](https://github.com/PDFMathTranslate/pdf2zh-next/blob/main/docs/GLOSSARY.md) do projeto para termos-chave.

- **Consistência na Terminologia**: Certifique-se de que o mesmo termo seja traduzido de forma consistente em toda a documentação.

- **Adaptação Cultural**: Adapte exemplos e referências para serem culturalmente relevantes para o público-alvo quando necessário.

- **Mantenha Simples**: Use linguagem clara e direta. Evite frases excessivamente complexas.

- **Teste Suas Traduções**: Após traduzir, teste a funcionalidade para garantir que o texto traduzido funcione bem no contexto da aplicação.

- **Colabore**: Use pull requests e issues para colaborar com outros tradutores e mantenedores.

### Guia de Estilo de Tradução

1. **Tom**: Mantenha um tom profissional e prestativo. A documentação deve ser acessível, mas autoritária.

2. **Voz**: Use voz ativa sempre que possível para tornar o texto mais envolvente e fácil de entender.

3. **Pontuação**: Siga as regras de pontuação do idioma de destino. Por exemplo, em português, use sinais de pontuação de largura total.

4. **Formatação**: Preserve a formatação original, incluindo blocos de código, links e cabeçalhos. Traduza apenas o conteúdo textual.

5. **Acessibilidade**: Certifique-se de que a tradução seja acessível, usando linguagem clara e evitando jargões, a menos que estejam bem definidos.
---

### OUTPUT

- Sempre trate tanto eventos de erro quanto exceções do gerador.
- Interrompa o loop em `finish` para evitar trabalho desnecessário.
- Certifique-se de que o `file` existe e que `settings.validate_settings()` passa antes de chamar.
- Documentos grandes podem ser divididos; use `part_index/total_parts` e `overall_progress` para orientar sua interface do usuário.
- Faça debounce de `progress_update` se sua interface do usuário for sensível a atualizações repetidas e idênticas.
- `report_interval` (SettingsModel): controla apenas a taxa de emissão de eventos `progress_update`. Não afeta `stage_summary`, `progress_start`, `progress_end` ou `finish`. O padrão é 0,1s e o mínimo permitido é 0,05s. Conforme a lógica do monitor de progresso, quando `stage_total <= 3`, as atualizações não são limitadas por `report_interval`.

---

### ORIGINAL TEXT

### Example Event Shapes

This is a list of example event shapes.

!!! note
    The examples below are for illustration purposes only. The actual events may vary.

#### Example 1: Simple Event

```json
{
  "event_id": "12345",
  "event_type": "user_login",
  "timestamp": "2023-10-05T14:48:00Z",
  "user_id": "user_67890",
  "ip_address": "192.168.1.1"
}
```

#### Example 2: Event with Nested Data

```json
{
  "event_id": "67890",
  "event_type": "purchase",
  "timestamp": "2023-10-05T15:30:00Z",
  "user": {
    "user_id": "user_12345",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_1",
      "quantity": 2,
      "price": 19.99
    },
    {
      "product_id": "prod_2",
      "quantity": 1,
      "price": 9.99
    }
  ],
  "total_amount": 49.97
}
```

#### Example 3: Event with Array of Strings

```json
{
  "event_id": "abcde",
  "event_type": "search",
  "timestamp": "2023-10-05T16:15:00Z",
  "query": "example query",
  "filters": ["filter1", "filter2", "filter3"],
  "results_count": 15
}
```

---

### OUTPUT

### Exemplo de Formatos de Evento

Esta é uma lista de exemplo de formatos de evento.

!!! note
    Os exemplos abaixo são apenas para fins de ilustração. Os eventos reais podem variar.

#### Exemplo 1: Evento Simples

```json
{
  "event_id": "12345",
  "event_type": "user_login",
  "timestamp": "2023-10-05T14:48:00Z",
  "user_id": "user_67890",
  "ip_address": "192.168.1.1"
}
```

#### Exemplo 2: Evento com Dados Aninhados

```json
{
  "event_id": "67890",
  "event_type": "purchase",
  "timestamp": "2023-10-05T15:30:00Z",
  "user": {
    "user_id": "user_12345",
    "email": "user@example.com",
    "name": "John Doe"
  },
  "items": [
    {
      "product_id": "prod_1",
      "quantity": 2,
      "price": 19.99
    },
    {
      "product_id": "prod_2",
      "quantity": 1,
      "price": 9.99
    }
  ],
  "total_amount": 49.97
}
```

#### Exemplo 3: Evento com Array de Strings

```json
{
  "event_id": "abcde",
  "event_type": "search",
  "timestamp": "2023-10-05T16:15:00Z",
  "query": "example query",
  "filters": ["filter1", "filter2", "filter3"],
  "results_count": 15
}
```

<div align="right"> 
<h6><small>Parte do conteúdo desta página foi traduzida pelo GPT e pode conter erros.</small></h6>