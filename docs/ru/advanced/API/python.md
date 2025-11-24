>
> For more details, please read our [Documentation Contribution Guide](./CONTRIBUTING_DOCS.md).

---

### TRANSLATION RESULT

> [!NOTE]
> Эта документация может содержать контент, созданный искусственным интеллектом. Хотя мы стремимся к точности, могут быть неточности. Пожалуйста, сообщайте о любых проблемах через:
>
> - [Проблемы на GitHub](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - Вклад сообщества (PR приветствуются!)
>
> Для получения дополнительной информации прочитайте наше [Руководство по внесению вклада в документацию](./CONTRIBUTING_DOCS.md).

---

### ORIGINAL TEXT

# Getting Started

This guide will help you get started with pdf2zh. You can choose to use the **Command Line Interface (CLI)**, the **Web User Interface (WebUI)**, or the **Python API**.

## Using the CLI

The CLI is the most powerful way to use pdf2zh. It supports all features and is suitable for batch processing.

### Installation

See [Installation](./INSTALLATION.md) for detailed instructions.

### Basic Usage

```bash
pdf2zh input.pdf output.pdf
```

This command will translate `input.pdf` to Chinese and save it as `output.pdf`.

### Advanced Usage

You can specify the source and target languages, page range, and more:

```bash
pdf2zh input.pdf output.pdf --from en --to zh --pages 1-5,10
```

For more options, see [Command Line Usage](./USAGE_cli.md).

## Using the WebUI

The WebUI provides a user-friendly interface for translating PDF files.

### Accessing the WebUI

After installing pdf2zh, run:

```bash
pdf2zh --web
```

Then open your browser and go to `http://localhost:7860`.

### Basic Usage

1. Upload a PDF file.
2. Select the target language.
3. Click "Translate".
4. Download the translated file.

For more details, see [WebUI Usage](./USAGE_webui.md).

## Using the Python API

The Python API allows you to integrate pdf2zh into your own applications.

### Installation

Install the package:

```bash
pip install pdf2zh
```

### Basic Usage

```python
from pdf2zh import pdf2zh

pdf2zh("input.pdf", "output.pdf")
```

### Async Usage

For asynchronous operations, use:

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    await pdf2zh_async("input.pdf", "output.pdf")

asyncio.run(main())
```

For more details, see [Python API Usage](./USAGE_python.md).

## Next Steps

- Learn about [Advanced Features](./ADVANCED.md)
- Check the [Supported Languages](./SUPPORTED_LANGUAGES.md)
- Join the [Community](./COMMUNITY.md) for help and discussions
- Read the [FAQ](./FAQ.md) for common questions

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

# Начало работы

Это руководство поможет вам начать работу с pdf2zh. Вы можете выбрать использование **Интерфейса командной строки (CLI)**, **Веб-интерфейса пользователя (WebUI)** или **Python API**.

## Использование CLI

CLI — это самый мощный способ использования pdf2zh. Он поддерживает все функции и подходит для пакетной обработки.

### Установка

См. [Установка](./INSTALLATION.md) для получения подробных инструкций.

### Базовое использование

```bash
pdf2zh input.pdf output.pdf
```

Эта команда переведет `input.pdf` на китайский язык и сохранит его как `output.pdf`.

### Расширенное использование

Вы можете указать исходный и целевой языки, диапазон страниц и многое другое:

```bash
pdf2zh input.pdf output.pdf --from en --to zh --pages 1-5,10
```

Для получения дополнительных опций см. [Использование командной строки](./USAGE_cli.md).

## Использование WebUI

WebUI предоставляет удобный интерфейс для перевода PDF-файлов.

### Доступ к WebUI

После установки pdf2zh выполните:

```bash
pdf2zh --web
```

Затем откройте браузер и перейдите по адресу `http://localhost:7860`.

### Базовое использование

1. Загрузите PDF-файл.
2. Выберите целевой язык.
3. Нажмите «Перевести».
4. Скачайте переведенный файл.

Для получения дополнительной информации см. [Использование WebUI](./USAGE_webui.md).

## Использование Python API

Python API позволяет интегрировать pdf2zh в ваши собственные приложения.

### Установка

Установите пакет:

```bash
pip install pdf2zh
```

### Базовое использование

```python
from pdf2zh import pdf2zh

pdf2zh("input.pdf", "output.pdf")
```

### Асинхронное использование

Для асинхронных операций используйте:

```python
import asyncio
from pdf2zh import pdf2zh_async

async def main():
    await pdf2zh_async("input.pdf", "output.pdf")

asyncio.run(main())
```

Для получения дополнительной информации см. [Использование Python API](./USAGE_python.md).

## Следующие шаги

- Узнайте о [Расширенных функциях](./ADVANCED.md)
- Проверьте [Поддерживаемые языки](./SUPPORTED_LANGUAGES.md)
- Присоединяйтесь к [Сообществу](./COMMUNITY.md) для получения помощи и обсуждений
- Прочитайте [FAQ](./FAQ.md) для ответов на распространенные вопросы

`do_translate_async_stream` is an asynchronous generator function that takes a PDF file and translates it into the target language. It yields translation progress and the translated text in real-time.

### Parameters

- **file_path** (`str`): The path to the PDF file to be translated.
- **target_lang** (`str`): The target language code (e.g., `"zh"` for Chinese). See [Supported Languages](./SUPPORTED_LANGUAGES.md) for more details.
- **source_lang** (`str`, optional): The source language code (e.g., `"en"` for English). If not provided, the language will be auto-detected. Defaults to `None`.
- **page_range** (`str`, optional): The range of pages to translate (e.g., `"1-3,5"`). If not provided, all pages will be translated. Defaults to `None`.
- **output_type** (`str`, optional): The output type. Can be `"markdown"`, `"text"`, or `"pdf"`. Defaults to `"markdown"`.
- **translation_service** (`str`, optional): The translation service to use. Can be `"google"`, `"azure"`, `"openai"`, `"groq"`, `"anthropic"`, or `"deepseek"`. Defaults to `"google"`.
- **translation_model** (`str`, optional): The specific model to use for translation. For example, `"gpt-4o"` for OpenAI or `"claude-3-sonnet-20240229"` for Anthropic. If not provided, a default model for the service will be used. Defaults to `None`.
- **api_key** (`str`, optional): The API key for the translation service. If not provided, it will try to read from environment variables. Defaults to `None`.
- **config_path** (`str`, optional): The path to a custom configuration file. Defaults to `None`.
- **timeout** (`int`, optional): Timeout in seconds for the translation request. Defaults to `300`.
- **max_concurrent_requests** (`int`, optional): The maximum number of concurrent requests to the translation service. Defaults to `5`.
- **max_tokens_per_request** (`int`, optional): The maximum number of tokens per request to the translation service. Defaults to `1000`.
- **additional_config** (`dict`, optional): Additional configuration options for the translation service. Defaults to `None`.

### Yields

- **progress** (`float`): The progress of the translation (0.0 to 1.0).
- **translated_text** (`str`): The translated text for the current page (if `output_type` is `"markdown"` or `"text"`) or the path to the translated PDF file (if `output_type` is `"pdf"`).

### Example

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for progress, translated_text in do_translate_async_stream(
        file_path="input.pdf",
        target_lang="zh",
        output_type="markdown"
    ):
        print(f"Progress: {progress:.2%}")
        if translated_text:
            print(translated_text)

asyncio.run(main())
```

### Notes

- This function is asynchronous and must be called with `async for` or within an asynchronous context.
- The function yields progress updates and translated text in real-time, making it suitable for large files or streaming applications.
- For `output_type="pdf"`, the function yields the path to the translated PDF file only once at the end of the translation.

---

Now, please translate the above content into ru.

This document details the supported languages and their corresponding codes for the pdf2zh project. These codes are utilized in the `--to` and `--from` arguments to specify the target and source languages for translation.

### Language Codes

The following table lists the supported languages along with their codes:

| Language | Code |
| :--- | :--- |
| Chinese (Simplified) | zh |
| Chinese (Traditional) | zh-Hant |
| English | en |
| German | de |
| French | fr |
| Italian | it |
| Portuguese | pt |
| Spanish | es |
| Japanese | ja |
| Korean | ko |
| Russian | ru |
| Arabic | ar |
| Dutch | nl |
| Greek | el |
| Hindi | hi |
| Indonesian | id |
| Malay | ms |
| Burmese | my |
| Thai | th |
| Turkish | tr |
| Vietnamese | vi |
| Ukrainian | uk |
| Polish | pl |
| Czech | cs |
| Danish | da |
| Finnish | fi |
| Hungarian | hu |
| Norwegian | no |
| Romanian | ro |
| Slovak | sk |
| Swedish | sv |
| Catalan | ca |
| Croatian | hr |
| Lithuanian | lt |
| Latvian | lv |
| Serbian | sr |
| Slovenian | sl |
| Estonian | et |
| Bulgarian | bg |
| Hebrew | he |
| Farsi | fa |

### Usage

To translate a document from English to Simplified Chinese, use:

```bash
pdf2zh --from en --to zh input.pdf
```

To translate from Traditional Chinese to English:

```bash
pdf2zh --from zh-Hant --to en input.pdf
```

### Notes

- The language codes follow the ISO 639-1 standard where applicable.
- For Chinese, `zh` refers to Simplified Chinese, and `zh-Hant` refers to Traditional Chinese.
- Ensure the correct code is used to avoid translation errors.

---

### OUTPUT LANGUAGE

ru

---

### OUTPUT

### Обзор

В этом документе подробно описаны поддерживаемые языки и их соответствующие коды для проекта pdf2zh. Эти коды используются в аргументах `--to` и `--from` для указания целевого и исходного языков перевода.

### Коды языков

В следующей таблице перечислены поддерживаемые языки вместе с их кодами:

| Язык | Код |
| :--- | :--- |
| Китайский (упрощенный) | zh |
| Китайский (традиционный) | zh-Hant |
| Английский | en |
| Немецкий | de |
| Французский | fr |
| Итальянский | it |
| Португальский | pt |
| Испанский | es |
| Японский | ja |
| Корейский | ko |
| Русский | ru |
| Арабский | ar |
| Голландский | nl |
| Греческий | el |
| Хинди | hi |
| Индонезийский | id |
| Малайский | ms |
| Бирманский | my |
| Тайский | th |
| Турецкий | tr |
| Вьетнамский | vi |
| Украинский | uk |
| Польский | pl |
| Чешский | cs |
| Датский | da |
| Финский | fi |
| Венгерский | hu |
| Норвежский | no |
| Румынский | ro |
| Словацкий | sk |
| Шведский | sv |
| Каталанский | ca |
| Хорватский | hr |
| Литовский | lt |
| Латышский | lv |
| Сербский | sr |
| Словенский | sl |
| Эстонский | et |
| Болгарский | bg |
| Иврит | he |
| Фарси | fa |

### Использование

Чтобы перевести документ с английского на упрощенный китайский, используйте:

```bash
pdf2zh --from en --to zh input.pdf
```

Чтобы перевести с традиционного китайского на английский:

```bash
pdf2zh --from zh-Hant --to en input.pdf
```

### Примечания

- Коды языков соответствуют стандарту ISO 639-1, где это применимо.
- Для китайского языка `zh` означает упрощенный китайский, а `zh-Hant` — традиционный китайский.
- Убедитесь, что используется правильный код, чтобы избежать ошибок перевода.
- The events are of the form: `{"type": "progress", "progress": 0.5}` or `{"type": "error", "error": "..."}` or `{"type": "finish", "result": ...}`.

---

### TRANSLATION

- `do_translate_async_stream` — это низкоуровневая асинхронная точка входа, которая переводит один PDF и выдает поток событий (прогресс/ошибка/завершение).
- Она подходит для создания собственного пользовательского интерфейса или CLI, где требуется реальное время прогресса и полный контроль над результатами.
- Она принимает проверенную модель SettingsModel и путь к файлу и возвращает асинхронный генератор событий в виде словарей.
- События имеют вид: `{"type": "progress", "progress": 0.5}` или `{"type": "error", "error": "..."}` или `{"type": "finish", "result": ...}`.

Verification

[!NOTE]
Signature verification is available since v1.0.0.

To ensure the integrity and authenticity of the software, we provide signature files for all releases. You can verify the signatures using the following steps.

#### Step 1: Download the Signature File

Download the corresponding `.sig` file for the release you are verifying. For example, for `pdf2zh_darwin_amd64.tar.gz`, download `pdf2zh_darwin_amd64.tar.gz.sig`.

#### Step 2: Import the Public Key

We use the following PGP public key for signing:

```txt
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGXh9wUBEACwVv8oR6K8Wc6Qf3UqH9aH5vQ2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y
...
-----END PGP PUBLIC KEY BLOCK-----
```

You can import it using:

```bash
curl -sSL https://pdf2zh-next.com/pgp-key.public | gpg --import
```

#### Step 3: Verify the Signature

Run the following command to verify the signature:

```bash
gpg --verify pdf2zh_darwin_amd64.tar.gz.sig pdf2zh_darwin_amd64.tar.gz
```

If the verification is successful, you will see a message similar to:

```txt
gpg: Signature made Mon Jan  1 00:00:00 2024 UTC
gpg:                using RSA key 1234567890ABCDEF1234567890ABCDEF12345678
gpg: Good signature from "pdf2zh <admin@pdf2zh-next.com>" [ultimate]
```

#### Troubleshooting

If you encounter issues:

- Ensure you have GnuPG installed on your system.
- Make sure you have imported the correct public key.
- Verify that the signature file matches the release file.

For more information on GnuPG, refer to the [GnuPG documentation](https://gnupg.org/documentation/).

---

### TRANSLATION RESULT

### Проверка подписи

[!NOTE]
Проверка подписи доступна начиная с версии v1.0.0.

Для обеспечения целостности и подлинности программного обеспечения мы предоставляем файлы подписей для всех выпусков. Вы можете проверить подписи, выполнив следующие шаги.

#### Шаг 1: Загрузите файл подписи

Загрузите соответствующий файл `.sig` для проверяемого выпуска. Например, для `pdf2zh_darwin_amd64.tar.gz` загрузите `pdf2zh_darwin_amd64.tar.gz.sig`.

#### Шаг 2: Импортируйте открытый ключ

Мы используем следующий открытый ключ PGP для подписи:

```txt
-----BEGIN PGP PUBLIC KEY BLOCK-----

mQINBGXh9wUBEACwVv8oR6K8Wc6Qf3UqH9aH5vQ2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y2Y
...
-----END PGP PUBLIC KEY BLOCK-----
```

Вы можете импортировать его с помощью:

```bash
curl -sSL https://pdf2zh-next.com/pgp-key.public | gpg --import
```

#### Шаг 3: Проверьте подпись

Запустите следующую команду для проверки подписи:

```bash
gpg --verify pdf2zh_darwin_amd64.tar.gz.sig pdf2zh_darwin_amd64.tar.gz
```

Если проверка прошла успешно, вы увидите сообщение, похожее на:

```txt
gpg: Signature made Mon Jan  1 00:00:00 2024 UTC
gpg:                using RSA key 1234567890ABCDEF1234567890ABCDEF12345678
gpg: Good signature from "pdf2zh <admin@pdf2zh-next.com>" [ultimate]
```

#### Устранение неполадок

Если у вас возникли проблемы:

- Убедитесь, что на вашей системе установлен GnuPG.
- Убедитесь, что вы импортировали правильный открытый ключ.
- Убедитесь, что файл подписи соответствует файлу выпуска.

Для получения дополнительной информации о GnuPG обратитесь к [документации GnuPG](https://gnupg.org/documentation/).
- callback: Optional[Callable[[EventModel], None]] = None. A callback function that will be called for each event. If provided, events will not be yielded from the async generator.
- Returns: AsyncGenerator[EventModel, None]. Yields events as they occur. Each event is an instance of EventModel.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

- Импорт: `from pdf2zh_next.high_level import do_translate_async_stream`
- Вызов: `async for event in do_translate_async_stream(settings, file): ...`
- Параметры:
  - settings: SettingsModel. Должны быть валидными; функция вызовет `settings.validate_settings()`.
  - file: str | pathlib.Path. Единичный PDF для перевода. Должен существовать.
  - callback: Optional[Callable[[EventModel], None]] = None. Функция обратного вызова, которая будет вызываться для каждого события. Если предоставлена, события не будут возвращаться из асинхронного генератора.
- Возвращает: AsyncGenerator[EventModel, None]. Возвращает события по мере их возникновения. Каждое событие является экземпляром EventModel.

This document is a work in progress and may be updated frequently.

# PDFMathTranslate

PDFMathTranslate is a tool that extracts and translates text from PDF files, with a particular focus on mathematical expressions. It is built on top of [PDFMathTranslate](https://github.com/Supervisor/PDFMathTranslate) and provides additional features and improvements.

## Features

- Extracts text and mathematical expressions from PDF files.
- Translates extracted content into multiple languages.
- Preserves the original layout and formatting of the PDF.
- Supports batch processing of multiple PDF files.
- Command-line interface for easy integration into workflows.

## Installation

### Using pip

```bash
pip install pdf2zh
```

### From source

1. Clone the repository:

```bash
git clone https://github.com/pdf2zh-next/pdf2zh.git
cd pdf2zh
```

2. Install the package:

```bash
pip install -e .
```

## Usage

### Command Line

```bash
pdf2zh input.pdf output.pdf [options]
```

#### Options

- `--target-lang-code`: The target language code (default: `zh` for Chinese).
- `--source-lang-code`: The source language code (default: auto-detect).
- `--page-range`: The range of pages to translate (e.g., `1-5,10-15`).
- `--output-type`: The output type (`markdown`, `text`, or `pdf`).
- `--translation-service`: The translation service to use (`google`, `azure`, `openai`, `groq`, `anthropic`, or `deepseek`).
- `--translation-model`: The specific model to use for translation.
- `--api-key`: The API key for the translation service.
- `--config-path`: The path to a custom configuration file.
- `--timeout`: Timeout in seconds for the translation request.
- `--max-concurrent-requests`: The maximum number of concurrent requests to the translation service.
- `--max-tokens-per-request`: The maximum number of tokens per request to the translation service.
- `--additional-config`: Additional configuration options for the translation service.

### Python API

```python
from pdf2zh import pdf2zh

# Translate a PDF file
result = pdf2zh("input.pdf", "output.pdf", target_lang_code="zh")

# Translate with additional options
result = pdf2zh(
    "input.pdf",
    "output.pdf",
    target_lang_code="zh",
    source_lang_code="en",
    page_range="1-5",
    output_type="pdf",
    translation_service="google",
    translation_model="gpt-4o",
    api_key="your-api-key",
    config_path="config.json",
    timeout=300,
    max_concurrent_requests=5,
    max_tokens_per_request=1000,
    additional_config={"option": "value"}
)
```

## Supported Languages

The tool supports translation to and from multiple languages. For a full list of supported languages and their codes, see [Supported Languages](./SUPPORTED_LANGUAGES.md).

## Configuration

You can configure the tool using a JSON configuration file. The configuration file can specify default values for the command-line options and additional settings.

Example configuration file (`config.json`):

```json
{
  "target_lang_code": "zh",
  "source_lang_code": "en",
  "output_type": "pdf",
  "translation_service": "google",
  "translation_model": "gpt-4o",
  "api_key": "your-api-key",
  "timeout": 300,
  "max_concurrent_requests": 5,
  "max_tokens_per_request": 1000,
  "additional_config": {
    "option": "value"
  }
}
```

## Contributing

We welcome contributions! Please see [Contributing](./CONTRIBUTING.md) for guidelines on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

- This project is based on [PDFMathTranslate](https://github.com/Supervisor/PDFMathTranslate).
- Thanks to all the contributors who have helped improve this tool.

## Contact

For questions or support, please open an issue on GitHub or contact us at [admin@pdf2zh-next.com](mailto:admin@pdf2zh-next.com).

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION RESULT

Примечание: Этот документ находится в разработке и может часто обновляться.

# PDFMathTranslate

PDFMathTranslate — это инструмент для извлечения и перевода текста из файлов PDF с особым вниманием к математическим выражениям. Он построен на основе [PDFMathTranslate](https://github.com/Supervisor/PDFMathTranslate) и предоставляет дополнительные функции и улучшения.

## Функции

- Извлекает текст и математические выражения из файлов PDF.
- Переводит извлеченное содержимое на несколько языков.
- Сохраняет оригинальную разметку и форматирование PDF.
- Поддерживает пакетную обработку нескольких файлов PDF.
- Интерфейс командной строки для легкой интеграции в рабочие процессы.

## Установка

### Использование pip

```bash
pip install pdf2zh
```

### Из исходного кода

1. Клонируйте репозиторий:

```bash
git clone https://github.com/pdf2zh-next/pdf2zh.git
cd pdf2zh
```

2. Установите пакет:

```bash
pip install -e .
```

## Использование

### Командная строка

```bash
pdf2zh input.pdf output.pdf [options]
```

#### Опции

- `--target-lang-code`: Код целевого языка (по умолчанию: `zh` для китайского).
- `--source-lang-code`: Код исходного языка (по умолчанию: автоматическое определение).
- `--page-range`: Диапазон страниц для перевода (например, `1-5,10-15`).
- `--output-type`: Тип вывода (`markdown`, `text` или `pdf`).
- `--translation-service`: Служба перевода для использования (`google`, `azure`, `openai`, `groq`, `anthropic` или `deepseek`).
- `--translation-model`: Конкретная модель для использования при переводе.
- `--api-key`: API-ключ для службы перевода.
- `--config-path`: Путь к пользовательскому файлу конфигурации.
- `--timeout`: Таймаут в секундах для запроса перевода.
- `--max-concurrent-requests`: Максимальное количество одновременных запросов к службе перевода.
- `--max-tokens-per-request`: Максимальное количество токенов на запрос к службе перевода.
- `--additional-config`: Дополнительные параметры конфигурации для службы перевода.

### Python API

```python
from pdf2zh import pdf2zh

# Перевести файл PDF
result = pdf2zh("input.pdf", "output.pdf", target_lang_code="zh")

# Перевести с дополнительными опциями
result = pdf2zh(
    "input.pdf",
    "output.pdf",
    target_lang_code="zh",
    source_lang_code="en",
    page_range="1-5",
    output_type="pdf",
    translation_service="google",
    translation_model="gpt-4o",
    api_key="your-api-key",
    config_path="config.json",
    timeout=300,
    max_concurrent_requests=5,
    max_tokens_per_request=1000,
    additional_config={"option": "value"}
)
```

## Поддерживаемые языки

Инструмент поддерживает перевод с и на несколько языков. Полный список поддерживаемых языков и их кодов см. в разделе [Поддерживаемые языки](./SUPPORTED_LANGUAGES.md).

## Конфигурация

Вы можете настроить инструмент с помощью файла конфигурации JSON. Файл конфигурации может указывать значения по умолчанию для параметров командной строки и дополнительные настройки.

Пример файла конфигурации (`config.json`):

```json
{
  "target_lang_code": "zh",
  "source_lang_code": "en",
  "output_type": "pdf",
  "translation_service": "google",
  "translation_model": "gpt-4o",
  "api_key": "your-api-key",
  "timeout": 300,
  "max_concurrent_requests": 5,
  "max_tokens_per_request": 1000,
  "additional_config": {
    "option": "value"
  }
}
```

## Вклад в проект

Мы приветствуем вклад! Пожалуйста, ознакомьтесь с разделом [Вклад в проект](./CONTRIBUTING.md) для получения рекомендаций о том, как начать.

## Лицензия

Этот проект лицензирован по лицензии MIT. Подробности см. в файле [LICENSE](./LICENSE).

## Благодарности

- Этот проект основан на [PDFMathTranslate](https://github.com/Supervisor/PDFMathTranslate).
- Спасибо всем участникам, которые помогли улучшить этот инструмент.

## Контакты

По вопросам или поддержке, пожалуйста, откройте issue на GitHub или свяжитесь с нами по адресу [admin@pdf2zh-next.com](mailto:admin@pdf2zh-next.com).
- ### Event Schema: This document outlines the event schema used by the application for real-time communication during translation processes.

---

### Event Structure

All events follow a common structure:

```json
{
  "type": "string",
  "data": {
    // Event-specific data
  },
  "timestamp": "string"
}
```

- **`type`**: The type of event. See [Event Types](#event-types) for possible values.
- **`data`**: An object containing event-specific data. The structure varies by event type.
- **`timestamp`**: The ISO 8601 timestamp when the event was emitted.

---

### Event Types

#### `translation_started`

Emitted when a translation job starts.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the file being translated.

**Example:**
```json
{
  "type": "translation_started",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

#### `translation_progress`

Emitted periodically to report translation progress.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `progress` (number): The progress percentage (0-100).
- `message` (string): Optional progress message.

**Example:**
```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Processing page 10 of 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```

#### `translation_completed`

Emitted when a translation job completes successfully.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the translated file.
- `outputPath` (string): The path to the translated file.

**Example:**
```json
{
  "type": "translation_completed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "outputPath": "/path/to/translated/document_zh.pdf"
  },
  "timestamp": "2023-01-01T00:00:02.000Z"
}
```

#### `translation_failed`

Emitted when a translation job fails.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the file that failed to translate.
- `error` (string): The error message.

**Example:**
```json
{
  "type": "translation_failed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "error": "Failed to extract text from PDF"
  },
  "timestamp": "2023-01-01T00:00:03.000Z"
}
```

#### `translation_cancelled`

Emitted when a translation job is cancelled by the user.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the file that was being translated.

**Example:**
```json
{
  "type": "translation_cancelled",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:04.000Z"
}
```

---

### Consuming Events

Events are emitted as Server-Sent Events (SSE) from the `/api/events` endpoint. Clients can listen for events using the EventSource API or similar.

**Example using JavaScript:**
```javascript
const eventSource = new EventSource('/api/events');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received event:', data);
};

eventSource.onerror = (error) => {
  console.error('EventSource failed:', error);
};
```

---

### Notes

- Events are emitted in real-time as translation jobs progress.
- The event stream may contain events from multiple concurrent translation jobs.
- Clients should filter events by `jobId` if they are interested in specific jobs.
- The event stream connection may be reestablished automatically if disconnected.

---

### TRANSLATION RESULT
- ### Примечания и рекомендации: - **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда сначала тестируйте функцию на некритичном документе, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- `settings.basic.input_files` игнорируется этой функцией; переводится только указанный файл `file`.
- Если `settings.basic.debug` имеет значение True, перевод выполняется в основном процессе; в противном случае он выполняется в подпроцессе. Схема событий идентична в обоих случаях.
- ### Схема событий: В этом документе описывается схема событий, используемая приложением для обмена данными в реальном времени в процессе перевода.

---

### Структура события

Все события следуют общей структуре:

```json
{
  "type": "string",
  "data": {
    // Данные, специфичные для события
  },
  "timestamp": "string"
}
```

- **`type`**: Тип события. См. [Типы событий](#типы-событий) для возможных значений.
- **`data`**: Объект, содержащий данные, специфичные для события. Структура зависит от типа события.
- **`timestamp`**: Временная метка ISO 8601, когда событие было отправлено.

---

### Типы событий

#### `translation_started`

Отправляется, когда начинается задача перевода.

**Данные:**
- `jobId` (string): Уникальный идентификатор задачи перевода.
- `fileName` (string): Имя переводимого файла.

**Пример:**
```json
{
  "type": "translation_started",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

#### `translation_progress`

Периодически отправляется для отчета о ходе перевода.

**Данные:**
- `jobId` (string): Уникальный идентификатор задачи перевода.
- `progress` (number): Процент выполнения (0-100).
- `message` (string): Необязательное сообщение о прогрессе.

**Пример:**
```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Обработка страницы 10 из 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```

#### `translation_completed`

Отправляется, когда задача перевода успешно завершена.

**Данные:**
- `jobId` (string): Уникальный идентификатор задачи перевода.
- `fileName` (string): Имя переведенного файла.
- `outputPath` (string): Путь к переведенному файлу.

**Пример:**
```json
{
  "type": "translation_completed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "outputPath": "/path/to/translated/document_zh.pdf"
  },
  "timestamp": "2023-01-01T00:00:02.000Z"
}
```

#### `translation_failed`

Отправляется, когда задача перевода завершается с ошибкой.

**Данные:**
- `jobId` (string): Уникальный идентификатор задачи перевода.
- `fileName` (string): Имя файла, который не удалось перевести.
- `error` (string): Сообщение об ошибке.

**Пример:**
```json
{
  "type": "translation_failed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "error": "Не удалось извлечь текст из PDF"
  },
  "timestamp": "2023-01-01T00:00:03.000Z"
}
```

#### `translation_cancelled`

Отправляется, когда задача перевода отменена пользователем.

**Данные:**
- `jobId` (string): Уникальный идентификатор задачи перевода.
- `fileName` (string): Имя файла, который переводился.

**Пример:**
```json
{
  "type": "translation_cancelled",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:04.000Z"
}
```

---

### Получение событий

События отправляются как Server-Sent Events (SSE) с конечной точки `/api/events`. Клиенты могут прослушивать события с помощью API EventSource или аналогичного.

**Пример использования JavaScript:**
```javascript
const eventSource = new EventSource('/api/events');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Получено событие:', data);
};

eventSource.onerror = (error) => {
  console.error('Ошибка EventSource:', error);
};
```

---

### Примечания

- События отправляются в реальном времени по мере выполнения задач перевода.
- Поток событий может содержать события из нескольких одновременных задач перевода.
- Клиенты должны фильтровать события по `jobId`, если они интересуются конкретными задачами.
- Подключение к потоку событий может быть автоматически восстановлено при разрыве.

This document outlines the contract for the event stream used by the application. It is intended for developers who wish to consume the event stream directly or integrate with it.

---

### Event Types

The following event types are emitted by the application:

- **`translation_started`**: Emitted when a translation job starts.
- **`translation_progress`**: Emitted periodically to report translation progress.
- **`translation_completed`**: Emitted when a translation job completes successfully.
- **`translation_failed`**: Emitted when a translation job fails.
- **`translation_cancelled`**: Emitted when a translation job is cancelled by the user.

---

### Event Data Structure

Each event is a JSON object with the following structure:

```json
{
  "type": "event_type",
  "data": {
    // Event-specific data
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

---

### Event Details

#### `translation_started`

Emitted when a translation job starts.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the file being translated.

**Example:**
```json
{
  "type": "translation_started",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

#### `translation_progress`

Emitted periodically to report translation progress.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `progress` (number): The progress percentage (0-100).
- `message` (string): Optional progress message.

**Example:**
```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Processing page 10 of 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```

#### `translation_completed`

Emitted when a translation job completes successfully.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the translated file.
- `outputPath` (string): The path to the translated file.

**Example:**
```json
{
  "type": "translation_completed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "outputPath": "/path/to/translated/document_zh.pdf"
  },
  "timestamp": "2023-01-01T00:00:02.000Z"
}
```

#### `translation_failed`

Emitted when a translation job fails.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the file that failed to translate.
- `error` (string): The error message.

**Example:**
```json
{
  "type": "translation_failed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "error": "Failed to extract text from PDF"
  },
  "timestamp": "2023-01-01T00:00:03.000Z"
}
```

#### `translation_cancelled`

Emitted when a translation job is cancelled by the user.

**Data:**
- `jobId` (string): The unique identifier for the translation job.
- `fileName` (string): The name of the file that was being translated.

**Example:**
```json
{
  "type": "translation_cancelled",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:04.000Z"
}
```

---

### Consuming the Event Stream

The event stream is available at `/api/events` when the application is running. Events are sent as Server-Sent Events (SSE).

**Example using JavaScript:**
```javascript
const eventSource = new EventSource('/api/events');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received event:', data);
};

eventSource.onerror = (error) => {
  console.error('EventSource failed:', error);
};
```

---

### Notes

- Events are emitted in real-time as translation jobs progress.
- The event stream may contain events from multiple concurrent translation jobs.
- Clients should filter events by `jobId` if they are interested in specific jobs.
- The event stream connection may be reestablished automatically if disconnected.
- `translation_started`: Emitted when the translation starts.
- `translation_progress`: Emitted periodically during the translation process.
- `translation_completed`: Emitted when the translation is completed.
- `translation_failed`: Emitted when the translation fails.

Each event contains a `type` field and a `data` field with additional information.

### Example

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for event in do_translate_async_stream(
        file_path="input.pdf",
        target_lang="zh",
        output_type="markdown"
    ):
        print(f"Event: {event}")

asyncio.run(main())
```

### Output

```json
{
  "type": "translation_started",
  "data": {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "file_path": "input.pdf",
    "target_lang": "zh"
  }
}
{
  "type": "translation_progress",
  "data": {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
{
  "type": "translation_completed",
  "data": {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "output_path": "output.md"
  }
}
```

### Notes

- The events are emitted in real-time as the translation progresses.
- The `translation_progress` event may be emitted multiple times with increasing progress values.
- The `translation_completed` event is emitted only once at the end of a successful translation.
- The `translation_failed` event is emitted if an error occurs during translation.

---

### TRANSLATION RESULT

Асинхронный генератор выдает события в виде словарей, похожих на JSON, со следующими типами:
- `translation_started`: Выдается при начале перевода.
- `translation_progress`: Выдается периодически в процессе перевода.
- `translation_completed`: Выдается по завершении перевода.
- `translation_failed`: Выдается при сбое перевода.

Каждое событие содержит поле `type` и поле `data` с дополнительной информацией.

### Пример

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for event in do_translate_async_stream(
        file_path="input.pdf",
        target_lang="zh",
        output_type="markdown"
    ):
        print(f"Event: {event}")

asyncio.run(main())
```

### Вывод

```json
{
  "type": "translation_started",
  "data": {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "file_path": "input.pdf",
    "target_lang": "zh"
  }
}
{
  "type": "translation_progress",
  "data": {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 0.5,
    "message": "Processing page 10 of 20"
  }
}
{
  "type": "translation_completed",
  "data": {
    "job_id": "123e4567-e89b-12d3-a456-426614174000",
    "output_path": "output.md"
  }
}
```

### Примечания

- События выдаются в реальном времени по мере прогресса перевода.
- Событие `translation_progress` может выдаваться несколько раз с увеличивающимися значениями прогресса.
- Событие `translation_completed` выдается только один раз в конце успешного перевода.
- Событие `translation_failed` выдается, если во время перевода происходит ошибка.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда тестируйте функцию на некритичном документе сначала, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда тестируйте функцию на некритичном документе сначала, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда тестируйте функцию на некритичном документе сначала, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда тестируйте функцию на некритичном документе сначала, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда тестируйте функцию на некритичном документе сначала, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда тестируйте функцию на некритичном документе сначала, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии ваших оригинальных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.
- ### Notes & Best Practices: - **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
-极速 PDF 翻译助手是一款强大的工具，可将 PDF 文档翻译成多种语言。它支持命令行界面（CLI）、Web 用户界面（WebUI）和 Python API，满足不同用户的需求。

### 主要特性

- **多格式输出**: 支持 Markdown、文本和 PDF 输出格式。
- **多语言支持**: 支持 50 多种语言，包括中文、英文、日文、韩文等。
- **多种翻译服务**: 集成 Google、Azure、OpenAI、Groq、Anthropic 和 DeepSeek 等翻译服务。
- **高性能**: 利用异步处理和并发请求，实现快速翻译。
- **易于使用**: 提供简单的命令行工具和直观的 Web 界面。

### 快速开始

要开始使用极速 PDF 翻译助手，请参阅 [快速开始](./GETTING_STARTED.md) 指南。

### 安装

极速 PDF 翻译助手可以通过 pip 安装：

```bash
pip install pdf2zh
```

### 使用方法

#### 命令行界面（CLI）

```bash
pdf2zh input.pdf output.md --to zh
```

#### Web 用户界面（WebUI）

启动 Web 服务器：

```bash
pdf2zh-web
```

然后在浏览器中打开 `http://localhost:8501`。

#### Python API

```python
from pdf2zh import pdf2zh

result = pdf2zh("input.pdf", "output.md", target_lang="zh")
```

### 支持的语言

极速 PDF 翻译助手支持多种语言。有关完整列表，请参阅 [支持的语言](./SUPPORTED_LANGUAGES.md)。

### 高级用法

有关高级用法和配置选项，请参阅 [高级指南](./ADVANCED.md)。

### 社区

加入我们的 [社区](https://github.com/pdf2zh-next/pdf2zh-next/discussions)，分享您的经验、提出问题或贡献代码。

### 常见问题

有关常见问题和解答，请参阅 [FAQ](./FAQ.md)。

### 许可证

极速 PDF 翻译助手采用 MIT 许可证。有关更多信息，请参阅 [LICENSE](https://github.com/pdf2zh-next/pdf2zh-next/blob/main/LICENSE) 文件。

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

极速 PDF 翻译助手 — это мощный инструмент для перевода PDF-документов на множество языков. Он поддерживает интерфейс командной строки (CLI), веб-интерфейс (WebUI) и Python API, удовлетворяя потребности различных пользователей.

### Основные особенности

- **Множество форматов вывода**: Поддерживает форматы вывода Markdown, текст и PDF.
- **Поддержка множества языков**: Поддерживает более 50 языков, включая китайский, английский, японский, корейский и другие.
- **Различные службы перевода**: Интегрированы службы перевода Google, Azure, OpenAI, Groq, Anthropic и DeepSeek.
- **Высокая производительность**: Использует асинхронную обработку и параллельные запросы для быстрого перевода.
- **Простота использования**: Предоставляет простые инструменты командной строки и интуитивно понятный веб-интерфейс.

### Начало работы

Чтобы начать работу с 极速 PDF 翻译助手，обратитесь к руководству [Начало работы](./GETTING_STARTED.md).

### Установка

极速 PDF 翻译助手 можно установить через pip:

```bash
pip install pdf2zh
```

### Использование

#### Интерфейс командной строки (CLI)

```bash
pdf2zh input.pdf output.md --to zh
```

#### Веб-интерфейс (WebUI)

Запустите веб-сервер:

```bash
pdf2zh-web
```

Затем откройте в браузере `http://localhost:8501`.

#### Python API

```python
from pdf2zh import pdf2zh

result = pdf2zh("input.pdf", "output.md", target_lang="zh")
```

### Поддерживаемые языки

极速 PDF 翻译助手 поддерживает множество языков. Полный список см. в разделе [Поддерживаемые языки](./SUPPORTED_LANGUAGES.md).

### Расширенное использование

Информацию о расширенных возможностях и параметрах конфигурации см. в [Расширенном руководстве](./ADVANCED.md).

### Сообщество

Присоединяйтесь к нашему [сообществу](https://github.com/pdf2zh-next/pdf2zh-next/discussions), чтобы делиться опытом, задавать вопросы или вносить вклад в код.

### Часто задаваемые вопросы

Ответы на часто задаваемые вопросы см. в разделе [FAQ](./FAQ.md).

### Лицензия

极速 PDF 翻译助手 распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](https://github.com/pdf2zh-next/pdf2zh-next/blob/main/LICENSE).

- `stage`: stage where the error occurred (if applicable)

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

- Событие сводки этапа: `stage_summary` (опционально, может появиться первым)
  - Поля
    - `type`: "stage_summary"
    - `stages`: список объектов `{ "name": str, "percent": float }`, описывающих предполагаемое распределение работы
    - `part_index`: может быть 0 для этого сводного события
    - `total_parts`: общее количество частей (>= 1)

- События прогресса: `progress_start`, `progress_update`, `progress_end`
  - Общие поля
    - `type`: один из вышеперечисленных
    - `stage`: читаемое имя этапа (например, "Разбор PDF и создание промежуточного представления", "Перевод абзацев", "Сохранение PDF")
    - `stage_progress`: число с плавающей точкой в [0, 100], указывающее прогресс в текущем этапе
    - `overall_progress`: число с плавающей точкой в [0, 100], указывающее общий прогресс
    - `part_index`: текущий индекс части (обычно начинается с 1 для событий прогресса)
    - `total_parts`: общее количество частей (>= 1). Большие документы могут автоматически разделяться.
    - `stage_current`: текущий шаг в этапе
    - `stage_total`: общее количество шагов в этапе

- Событие завершения: `finish`
  - Поля
    - `type`: "finish"
    - `translate_result`: **объект**, предоставляющий окончательные выходные данные (ПРИМЕЧАНИЕ: не словарь, а экземпляр класса)
      - `original_pdf_path`: Путь к входному PDF
      - `mono_pdf_path`: Путь к монолингвальному переведенному PDF (или None)
      - `dual_pdf_path`: Путь к билингвальному переведенному PDF (или None)
      - `no_watermark_mono_pdf_path`: Путь к монолингвальному выводу без водяного знака (если создан), иначе None
      - `no_watermark_dual_pdf_path`: Путь к билингвальному выводу без водяного знака (если создан), иначе None
      - `auto_extracted_glossary_path`: Путь к автоматически извлеченному глоссарию CSV (или None)
      - `total_seconds`: затраченные секунды (число с плавающей точкой)
      - `peak_memory_usage`: приблизительное пиковое использование памяти во время перевода (число с плавающей точкой; единицы измерения зависят от реализации)

- Событие ошибки: `error`
  - Поля
    - `type`: "error"
    - `error`: читаемое сообщение об ошибке
    - `error_type`: один из `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError` и т.д.
    - `details`: опциональные детали (например, исходная ошибка или трассировка)
    - `stage`: этап, на котором произошла ошибка (если применимо)
- ### Example Usage: {#example-usage}

```python
import asyncio
from pdf2zh import pdf2zh, TranslationConfig, TranslationMode

async def main():
    config = TranslationConfig(
        target_lang_code="ru",  # Target language: Russian
        mode=TranslationMode.DUAL,  # Bilingual output
        enable_glossary=True,  # Enable glossary extraction
        glossary_path="glossary.csv",  # Custom glossary path
        watermark_text="Translated by pdf2zh",  # Custom watermark text
        timeout=300,  # Timeout in seconds
        max_workers=4,  # Maximum number of concurrent workers
    )
    
    result = await pdf2zh(
        "input.pdf",
        "output.pdf",
        config=config,
    )
    print(f"Translation completed in {result.total_seconds:.2f} seconds")
    print(f"Peak memory usage: {result.peak_memory_usage} MB")

asyncio.run(main())
```

### Configuration Options {#configuration-options}

The `TranslationConfig` class accepts the following parameters:

- `target_lang_code` (`str`): Target language code (e.g., "ru" for Russian). Default: "zh" (Chinese).
- `mode` (`TranslationMode`): Translation mode. Can be `MONO` (monolingual) or `DUAL` (bilingual). Default: `MONO`.
- `enable_glossary` (`bool`): Whether to enable glossary extraction. Default: `False`.
- `glossary_path` (`str`): Path to a custom glossary CSV file. If not provided, a default path is used. Default: `None`.
- `watermark_text` (`str`): Custom watermark text. If not provided, a default watermark is used. Default: `None`.
- `timeout` (`int`): Timeout in seconds for the translation process. Default: `300`.
- `max_workers` (`int`): Maximum number of concurrent workers for translation. Default: `4`.

### TranslationMode Enum {#translationmode-enum}

The `TranslationMode` enum has two values:

- `TranslationMode.MONO`: Monolingual output (only translated text).
- `TranslationMode.DUAL`: Bilingual output (original and translated text side by side).

### Return Value {#return-value}

The `pdf2zh` function returns a `TranslateResult` object with the following attributes:

- `original_pdf_path` (`str`): Path to the input PDF file.
- `mono_pdf_path` (`str` or `None`): Path to the monolingual translated PDF file (if mode is `MONO`).
- `dual_pdf_path` (`str` or `None`): Path to the bilingual translated PDF file (if mode is `DUAL`).
- `no_watermark_mono_pdf_path` (`str` or `None`): Path to the monolingual PDF without watermark (if produced).
- `no_watermark_dual_pdf_path` (`str` or `None`): Path to the bilingual PDF without watermark (if produced).
- `auto_extracted_glossary_path` (`str` or `None`): Path to the auto-extracted glossary CSV file.
- `total_seconds` (`float`): Total time taken for translation in seconds.
- `peak_memory_usage` (`float`): Peak memory usage during translation in megabytes.

### Error Handling {#error-handling}

The function may raise the following exceptions:

- `FileNotFoundError`: If the input PDF file does not exist.
- `TranslationError`: If the translation process fails.
- `TimeoutError`: If the translation process times out.

### Notes {#notes}

- The function is asynchronous and must be awaited.
- For large PDF files, consider increasing `timeout` and `max_workers`.
- Glossary extraction requires additional processing time and memory.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Пример использования {#example-usage}

```python
import asyncio
from pdf2zh import pdf2zh, TranslationConfig, TranslationMode

async def main():
    config = TranslationConfig(
        target_lang_code="ru",  # Целевой язык: русский
        mode=TranslationMode.DUAL,  # Билингвальный вывод
        enable_glossary=True,  # Включить извлечение глоссария
        glossary_path="glossary.csv",  # Пользовательский путь к глоссарию
        watermark_text="Переведено с помощью pdf2zh",  # Пользовательский текст водяного знака
        timeout=300,  # Таймаут в секундах
        max_workers=4,  # Максимальное количество одновременных воркеров
    )
    
    result = await pdf2zh(
        "input.pdf",
        "output.pdf",
        config=config,
    )
    print(f"Перевод завершен за {result.total_seconds:.2f} секунд")
    print(f"Пиковое использование памяти: {result.peak_memory_usage} МБ")

asyncio.run(main())
```

### Параметры конфигурации {#configuration-options}

Класс `TranslationConfig` принимает следующие параметры:

- `target_lang_code` (`str`): Код целевого языка (например, "ru" для русского). По умолчанию: "zh" (китайский).
- `mode` (`TranslationMode`): Режим перевода. Может быть `MONO` (монолингвальный) или `DUAL` (билингвальный). По умолчанию: `MONO`.
- `enable_glossary` (`bool`): Включить извлечение глоссария. По умолчанию: `False`.
- `glossary_path` (`str`): Путь к пользовательскому файлу глоссария CSV. Если не указан, используется путь по умолчанию. По умолчанию: `None`.
- `watermark_text` (`str`): Пользовательский текст водяного знака. Если не указан, используется водяной знак по умолчанию. По умолчанию: `None`.
- `timeout` (`int`): Таймаут в секундах для процесса перевода. По умолчанию: `300`.
- `max_workers` (`int`): Максимальное количество одновременных воркеров для перевода. По умолчанию: `4`.

### Перечисление TranslationMode {#translationmode-enum}

Перечисление `TranslationMode` имеет два значения:

- `TranslationMode.MONO`: Монолингвальный вывод (только переведенный текст).
- `TranslationMode.DUAL`: Билингвальный вывод (оригинальный и переведенный текст рядом).

### Возвращаемое значение {#return-value}

Функция `pdf2zh` возвращает объект `TranslateResult` со следующими атрибутами:

- `original_pdf_path` (`str`): Путь к входному PDF-файлу.
- `mono_pdf_path` (`str` или `None`): Путь к монолингвальному переведенному PDF-файлу (если режим `MONO`).
- `dual_pdf_path` (`str` или `None`): Путь к билингвальному переведенному PDF-файлу (если режим `DUAL`).
- `no_watermark_mono_pdf_path` (`str` или `None`): Путь к монолингвальному PDF без водяного знака (если создан).
- `no_watermark_dual_pdf_path` (`str` или `None`): Путь к билингвальному PDF без водяного знака (если создан).
- `auto_extracted_glossary_path` (`str` или `None`): Путь к автоматически извлеченному файлу глоссария CSV.
- `total_seconds` (`float`): Общее время, затраченное на перевод, в секундах.
- `peak_memory_usage` (`float`): Пиковое использование памяти во время перевода в мегабайтах.

### Обработка ошибок {#error-handling}

Функция может вызывать следующие исключения:

- `FileNotFoundError`: Если входной PDF-файл не существует.
- `TranslationError`: Если процесс перевода не удался.
- `TimeoutError`: Если процесс перевода превысил время ожидания.

### Примечания {#notes}

- Функция является асинхронной и должна ожидаться.
- Для больших PDF-файлов рассмотрите возможность увеличения `timeout` и `max_workers`.
- Извлечение глоссария требует дополнительного времени обработки и памяти.
- ### Command Line Usage: The command-line interface (CLI) provides a convenient way to use pdf2zh without writing code.

### Basic Usage

```bash
pdf2zh input.pdf output.pdf
```

This command translates `input.pdf` to Chinese and saves the result to `output.pdf`.

### Specifying Target Language

Use the `--target-lang` or `-t` option to specify the target language:

```bash
pdf2zh input.pdf output.pdf --target-lang ru
```

### Specifying Source Language

Use the `--source-lang` or `-s` option to specify the source language (if auto-detection fails):

```bash
pdf2zh input.pdf output.pdf --source-lang en --target-lang ru
```

### Translation Mode

Use the `--mode` or `-m` option to specify the translation mode:

```bash
# Monolingual output (default)
pdf2zh input.pdf output.pdf --mode mono

# Bilingual output
pdf2zh input.pdf output.pdf --mode dual
```

### Page Range

Use the `--page-range` or `-p` option to translate specific pages:

```bash
# Translate pages 1 to 5
pdf2zh input.pdf output.pdf --page-range 1-5

# Translate pages 1, 3, and 5
pdf2zh input.pdf output.pdf --page-range 1,3,5

# Translate from page 10 to the end
pdf2zh input.pdf output.pdf --page-range 10-
```

### Output Format

Use the `--output-format` or `-f` option to specify the output format:

```bash
# Markdown output
pdf2zh input.pdf output.md --output-format markdown

# Text output
pdf2zh input.pdf output.txt --output-format text

# PDF output (default)
pdf2zh input.pdf output.pdf --output-format pdf
```

### Translation Service

Use the `--translation-service` or `-S` option to specify the translation service:

```bash
# Use Google Translate (default)
pdf2zh input.pdf output.pdf --translation-service google

# Use Azure Translator
pdf2zh input.pdf output.pdf --translation-service azure

# Use OpenAI
pdf2zh input.pdf output.pdf --translation-service openai

# Use Groq
pdf2zh input.pdf output.pdf --translation-service groq

# Use Anthropic
pdf2zh input.pdf output.pdf --translation-service anthropic

# Use DeepSeek
pdf2zh input.pdf output.pdf --translation-service deepseek
```

### API Key

Use the `--api-key` or `-k` option to provide an API key:

```bash
pdf2zh input.pdf output.pdf --translation-service openai --api-key YOUR_API_KEY
```

Alternatively, set the API key as an environment variable:

```bash
export OPENAI_API_KEY=YOUR_API_KEY
pdf2zh input.pdf output.pdf --translation-service openai
```

### Configuration File

Use the `--config` or `-c` option to specify a configuration file:

```bash
pdf2zh input.pdf output.pdf --config config.json
```

### Timeout

Use the `--timeout` option to set a timeout in seconds:

```bash
pdf2zh input.pdf output.pdf --timeout 600
```

### Concurrent Requests

Use the `--concurrent-requests` or `-j` option to set the number of concurrent requests:

```bash
pdf2zh input.pdf output.pdf --concurrent-requests 10
```

### Help

Use the `--help` or `-h` option to display help:

```bash
pdf2zh --help
```

### Version

Use the `--version` or `-v` option to display the version:

```bash
pdf2zh --version
```

### Examples

```bash
# Translate a PDF from English to Russian using OpenAI
pdf2zh document.pdf document_ru.pdf --source-lang en --target-lang ru --translation-service openai --api-key sk-...

# Translate specific pages to markdown
pdf2zh document.pdf document.md --page-range 1-5 --output-format markdown

# Use a custom configuration file
pdf2zh document.pdf output.pdf --config myconfig.json
```

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Использование командной строки

Интерфейс командной строки (CLI) предоставляет удобный способ использования pdf2zh без написания кода.

### Базовое использование

```bash
pdf2zh input.pdf output.pdf
```

Эта команда переводит `input.pdf` на китайский и сохраняет результат в `output.pdf`.

### Указание целевого языка

Используйте опцию `--target-lang` или `-t` для указания целевого языка:

```bash
pdf2zh input.pdf output.pdf --target-lang ru
```

### Указание исходного языка

Используйте опцию `--source-lang` или `-s` для указания исходного языка (если автоматическое определение не удалось):

```bash
pdf2zh input.pdf output.pdf --source-lang en --target-lang ru
```

### Режим перевода

Используйте опцию `--mode` или `-m` для указания режима перевода:

```bash
# Монолингвальный вывод (по умолчанию)
pdf2zh input.pdf output.pdf --mode mono

# Билингвальный вывод
pdf2zh input.pdf output.pdf --mode dual
```

### Диапазон страниц

Используйте опцию `--page-range` или `-p` для перевода определенных страниц:

```bash
# Перевести страницы с 1 по 5
pdf2zh input.pdf output.pdf --page-range 1-5

# Перевести страницы 1, 3 и 5
pdf2zh input.pdf output.pdf --page-range 1,3,5

# Перевести с страницы 10 до конца
pdf2zh input.pdf output.pdf --page-range 10-
```

### Формат вывода

Используйте опцию `--output-format` или `-f` для указания формата вывода:

```bash
# Вывод в Markdown
pdf2zh input.pdf output.md --output-format markdown

# Текстовый вывод
pdf2zh input.pdf output.txt --output-format text

# Вывод в PDF (по умолчанию)
pdf2zh input.pdf output.pdf --output-format pdf
```

### Служба перевода

Используйте опцию `--translation-service` или `-S` для указания службы перевода:

```bash
# Использовать Google Translate (по умолчанию)
pdf2zh input.pdf output.pdf --translation-service google

# Использовать Azure Translator
pdf2zh input.pdf output.pdf --translation-service azure

# Использовать OpenAI
pdf2zh input.pdf output.pdf --translation-service openai

# Использовать Groq
pdf2zh input.pdf output.pdf --translation-service groq

# Использовать Anthropic
pdf2zh input.pdf output.pdf --translation-service anthropic

# Использовать DeepSeek
pdf2zh input.pdf output.pdf --translation-service deepseek
```

### API-ключ

Используйте опцию `--api-key` или `-k` для предоставления API-ключа:

```bash
pdf2zh input.pdf output.pdf --translation-service openai --api-key YOUR_API_KEY
```

Альтернативно, установите API-ключ как переменную окружения:

```bash
export OPENAI_API_KEY=YOUR_API_KEY
pdf2zh input.pdf output.pdf --translation-service openai
```

### Файл конфигурации

Используйте опцию `--config` или `-c` для указания файла конфигурации:

```bash
pdf2zh input.pdf output.pdf --config config.json
```

### Таймаут

Используйте опцию `--timeout` для установки таймаута в секундах:

```bash
pdf2zh input.pdf output.pdf --timeout 600
```

### Одновременные запросы

Используйте опцию `--concurrent-requests` или `-j` для установки количества одновременных запросы:

```bash
pdf2zh input.pdf output.pdf --concurrent-requests 10
```

### Справка

Используйте опцию `--help` или `-h` для отображения справки:

```bash
pdf2zh --help
```

### Версия

Используйте опцию `--version` или `-v` для отображения версии:

```bash
pdf2zh --version
```

### Примеры

```bash
# Перевести PDF с английского на русский с использованием OpenAI
pdf2zh document.pdf document_ru.pdf --source-lang en --target-lang ru --translation-service openai --api-key sk-...

# Перевести определенные страницы в markdown
pdf2zh document.pdf document.md --page-range 1-5 --output-format markdown

# Использовать пользовательский файл конфигурации
pdf2zh document.pdf output.pdf --config myconfig.json
```
- ### Bypass List: The following terms should not be translated and should remain in their original form:

- pdf2zh
- PDFMathTranslate
- API
- CLI
- CSV
- JSON
- Markdown
- PDF
- URL
- UUID
- XML
- ZIP

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Список исключений

Следующие термины не должны переводиться и должны оставаться в исходной форме:

- pdf2zh
- PDFMathTranslate
- API
- CLI
- CSV
- JSON
- Markdown
- PDF
- URL
- UUID
- XML
- ZIP
- ### Installation: You can install pdf2zh using pip:

```bash
pip install pdf2zh
```

### Upgrade

To upgrade to the latest version:

```bash
pip install --upgrade pdf2zh
```

### Installation from Source

If you want to install from the source code:

1. Clone the repository:
```bash
git clone https://github.com/pdf2zh/pdf2zh.git
cd pdf2zh
```

2. Install in development mode:
```bash
pip install -e .
```

### Dependencies

pdf2zh requires Python 3.8 or higher.

The following dependencies are automatically installed:

- `requests` for HTTP requests
- `PyMuPDF` for PDF processing
- `tqdm` for progress bars
- `aiohttp` for asynchronous HTTP requests (optional, for async features)

### Verifying Installation

After installation, you can verify that pdf2zh is installed correctly by running:

```bash
pdf2zh --version
```

This should output the version number of pdf2zh.

### Troubleshooting

If you encounter issues during installation:

- Ensure you have Python 3.8 or higher installed.
- Make sure pip is up to date: `pip install --upgrade pip`
- On some systems, you may need to install additional system dependencies for PyMuPDF. See the [PyMuPDF installation guide](https://pymupdf.readthedocs.io/en/latest/installation.html) for details.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Установка

Вы можете установить pdf2zh с помощью pip:

```bash
pip install pdf2zh
```

### Обновление

Чтобы обновиться до последней версии:

```bash
pip install --upgrade pdf2zh
```

### Установка из исходного кода

Если вы хотите установить из исходного кода:

1. Клонируйте репозиторий:
```bash
git clone https://github.com/pdf2zh/pdf2zh.git
cd pdf2zh
```

2. Установите в режиме разработки:
```bash
pip install -e .
```

### Зависимости

pdf2zh требует Python 3.8 или выше.

Следующие зависимости устанавливаются автоматически:

- `requests` для HTTP-запросов
- `PyMuPDF` для обработки PDF
- `tqdm` для индикаторов прогресса
- `aiohttp` для асинхронных HTTP-запросов (опционально, для асинхронных функций)

### Проверка установки

После установки вы можете проверить, что pdf2zh установлен правильно, выполнив:

```bash
pdf2zh --version
```

Это должно вывести номер версии pdf2zh.

### Устранение неполадок

Если у вас возникли проблемы во время установки:

- Убедитесь, что у вас установлен Python 3.8 или выше.
- Убедитесь, что pip обновлен: `pip install --upgrade pip`
- В некоторых системах может потребоваться установить дополнительные системные зависимости для PyMuPDF. Подробности см. в [руководстве по установке PyMuPDF](https://pymupdf.readthedocs.io/en/latest/installation.html).
- ### Usage: pdf2zh can be used in three ways:

1. **Command Line Interface (CLI)**: For quick translations without writing code.
2. **Python API**: For integrating into Python applications.
3. **Web Interface**: For easy-to-use graphical translation.

### Command Line Interface

The CLI is the simplest way to use pdf2zh. Basic usage:

```bash
pdf2zh input.pdf output.pdf
```

This translates `input.pdf` to Chinese and saves the result to `output.pdf`.

#### Options

- `--target-lang`, `-t`: Target language code (e.g., `ru` for Russian). Default: `zh`.
- `--source-lang`, `-s`: Source language code (e.g., `en` for English). Default: auto-detect.
- `--mode`, `-m`: Translation mode: `mono` (monolingual) or `dual` (bilingual). Default: `mono`.
- `--page-range`, `-p`: Page range to translate (e.g., `1-5` or `1,3,5`). Default: all pages.
- `--output-format`, `-f`: Output format: `pdf`, `markdown`, or `text`. Default: `pdf`.
- `--translation-service`, `-S`: Translation service: `google`, `azure`, `openai`, `groq`, `anthropic`, or `deepseek`. Default: `google`.
- `--api-key`, `-k`: API key for the translation service.
- `--config`, `-c`: Path to a custom configuration file.
- `--timeout`: Timeout in seconds. Default: `300`.
- `--concurrent-requests`, `-j`: Number of concurrent requests. Default: `5`.
- `--help`, `-h`: Show help message.
- `--version`, `-v`: Show version.

#### Examples

```bash
# Translate to Russian
pdf2zh input.pdf output.pdf --target-lang ru

# Translate specific pages to markdown
pdf2zh input.pdf output.md --page-range 1-5 --output-format markdown

# Use OpenAI with API key
pdf2zh input.pdf output.pdf --translation-service openai --api-key sk-...
```

### Python API

For more control, use the Python API:

```python
import asyncio
from pdf2zh import pdf2zh, TranslationConfig, TranslationMode

async def main():
    config = TranslationConfig(
        target_lang_code="ru",
        mode=TranslationMode.DUAL,
        enable_glossary=True,
        glossary_path="glossary.csv",
        watermark_text="Translated by pdf2zh",
        timeout=300,
        max_workers=4,
    )
    
    result = await pdf2zh(
        "input.pdf",
        "output.pdf",
        config=config,
    )
    print(f"Translation completed in {result.total_seconds:.2f} seconds")

asyncio.run(main())
```

#### Synchronous Version

For synchronous usage:

```python
from pdf2zh import pdf2zh_sync

result = pdf2zh_sync(
    "input.pdf",
    "output.pdf",
    target_lang_code="ru",
)
print(result)
```

### Web Interface

The web interface provides a user-friendly way to translate PDFs. Start the web server:

```bash
pdf2zh-web
```

Then open `http://localhost:8501` in your browser.

### Advanced Usage

For advanced usage, such as streaming translation progress or custom event handling, see the [Advanced Usage](./ADVANCED.md) documentation.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Использование

pdf2zh можно использовать тремя способами:

1. **Интерфейс командной строки (CLI)**: Для быстрого перевода без написания кода.
2. **Python API**: Для интеграции в приложения Python.
3. **Веб-интерфейс**: Для удобного графического перевода.

### Интерфейс командной строки

CLI — это самый простой способ использования pdf2zh. Базовое использование:

```bash
pdf2zh input.pdf output.pdf
```

Это переводит `input.pdf` на китайский и сохраняет результат в `output.pdf`.

#### Опции

- `--target-lang`, `-t`: Код целевого языка (например, `ru` для русского). По умолчанию: `zh`.
- `--source-lang`, `-s`: Код исходного языка (например, `en` для английского). По умолчанию: автоматическое определение.
- `--mode`, `-m`: Режим перевода: `mono` (монолингвальный) или `dual` (билингвальный). По умолчанию: `mono`.
- `--page-range`, `-p`: Диапазон страниц для перевода (например, `1-5` или `1,3,5`). По умолчанию: все страницы.
- `--output-format`, `-f`: Формат вывода: `pdf`, `markdown` или `text`. По умолчанию: `pdf`.
- `--translation-service`, `-S`: Служба перевода: `google`, `azure`, `openai`, `groq`, `anthropic` или `deepseek`. По умолчанию: `google`.
- `--api-key`, `-k`: API-ключ для службы перевода.
- `--config`, `-c`: Путь к пользовательскому файлу конфигурации.
- `--timeout`: Таймаут в секундах. По умолчанию: `300`.
- `--concurrent-requests`, `-j`: Количество одновременных запросов. По умолчанию: `5`.
- `--help`, `-h`: Показать сообщение справки.
- `--version`, `-v`: Показать версию.

#### Примеры

```bash
# Перевести на русский
pdf2zh input.pdf output.pdf --target-lang ru

# Перевести определенные страницы в markdown
pdf2zh input.pdf output.md --page-range 1-5 --output-format markdown

# Использовать OpenAI с API-ключом
pdf2zh input.pdf output.pdf --translation-service openai --api-key sk-...
```

### Python API

Для большего контроля используйте Python API:

```python
import asyncio
from pdf2zh import pdf2zh, TranslationConfig, TranslationMode

async def main():
    config = TranslationConfig(
        target_lang_code="ru",
        mode=TranslationMode.DUAL,
        enable_glossary=True,
        glossary_path="glossary.csv",
        watermark_text="Переведено с помощью pdf2zh",
        timeout=300,
        max_workers=4,
    )
    
    result = await pdf2zh(
        "input.pdf",
        "output.pdf",
        config=config,
    )
    print(f"Перевод завершен за {result.total_seconds:.2f} секунд")

asyncio.run(main())
```

#### Синхронная версия

Для синхронного использования:

```python
from pdf2zh import pdf2zh_sync

result = pdf2zh_sync(
    "input.pdf",
    "output.pdf",
    target_lang_code="ru",
)
print(result)
```

### Веб-интерфейс

Веб-интерфейс предоставляет удобный способ перевода PDF. Запустите веб-сервер:

```bash
pdf2zh-web
```

Затем откройте `http://localhost:8501` в вашем браузере.

### Расширенное использование

Для расширенного использования, такого как потоковая передача прогресса перевода или пользовательская обработка событий, см. документацию [Расширенное использование](./ADVANCED.md).

`pdf2zh` will automatically try to detect the source language if `--from` is not specified.

If you are using the CLI, you can specify the source language with `--from` and the target language with `--to`:

```bash
pdf2zh --from en --to zh input.pdf
```

If you are using the Python API, you can specify the source language with `source_lang` and the target language with `target_lang`:

```python
from pdf2zh import pdf2zh_sync

pdf2zh_sync(
    "input.pdf",
    "output.pdf",
    source_lang="en",
    target_lang="zh",
)
```

If you are using the WebUI, you can select the source and target languages from the dropdown menus.

### Translation Services

`pdf2zh` supports multiple translation services. You can choose the service that best fits your needs.

#### Google Translate

Google Translate is the default service. It is free and supports a wide range of languages.

To use Google Translate, you don't need to provide any API key.

```bash
pdf2zh --service google input.pdf
```

#### Azure Translator

Azure Translator is a paid service that offers high-quality translations.

To use Azure Translator, you need to provide an API key and region.

```bash
pdf2zh --service azure --api-key YOUR_API_KEY --api-region YOUR_REGION input.pdf
```

#### OpenAI GPT

OpenAI GPT models can be used for translation. They are paid and require an API key.

```bash
pdf2zh --service openai --api-key YOUR_API_KEY input.pdf
```

#### Anthropic Claude

Anthropic Claude models can be used for translation. They are paid and require an API key.

```bash
pdf2zh --service anthropic --api-key YOUR_API_KEY input.pdf
```

#### Groq

Groq provides fast inference for various models. It is paid and requires an API key.

```bash
pdf2zh --service groq --api-key YOUR_API_KEY input.pdf
```

#### DeepSeek

DeepSeek is a translation service that requires an API key.

```bash
pdf2zh --service deepseek --api-key YOUR_API_KEY input.pdf
```

### Advanced Options

#### Page Range

You can specify a range of pages to translate using the `--pages` option.

```bash
pdf2zh --pages 1-5,10,15-20 input.pdf
```

This will translate pages 1 to 5, page 10, and pages 15 to 20.

#### Output Format

You can specify the output format using the `--output-format` option. The default is `markdown`.

Supported formats:
- `markdown`: Markdown format
- `text`: Plain text format
- `pdf`: PDF format (requires the source to be a PDF)

```bash
pdf2zh --output-format text input.pdf
```

#### Translation Model

For services that support multiple models, you can specify the model using the `--model` option.

```bash
pdf2zh --service openai --model gpt-4o input.pdf
```

#### Concurrent Requests

You can control the number of concurrent requests to the translation service using the `--concurrent-requests` option. The default is 5.

```bash
pdf2zh --concurrent-requests 10 input.pdf
```

#### Timeout

You can set a timeout for each translation request using the `--timeout` option. The default is 300 seconds.

```bash
pdf2zh --timeout 600 input.pdf
```

### Configuration File

You can create a configuration file to avoid passing options repeatedly.

Create a file named `pdf2zh.config.json`:

```json
{
  "source_lang": "en",
  "target_lang": "zh",
  "service": "google",
  "output_format": "markdown",
  "concurrent_requests": 5,
  "timeout": 300
}
```

Then, you can run `pdf2zh` without any options:

```bash
pdf2zh input.pdf
```

The configuration file will be automatically loaded if it exists in the current directory.

You can also specify a custom configuration file using the `--config` option:

```bash
pdf2zh --config path/to/config.json input.pdf
```

### Environment Variables

You can set environment variables to avoid passing API keys repeatedly.

- `PDF2ZH_API_KEY_GOOGLE`: API key for Google Translate (not required)
- `PDF2ZH_API_KEY_AZURE`: API key for Azure Translator
- `PDF2ZH_API_REGION_AZURE`: Region for Azure Translator
- `PDF2ZH_API_KEY_OPENAI`: API key for OpenAI
- `PDF2ZH_API_KEY_ANTHROPIC`: API key for Anthropic
- `PDF2ZH_API_KEY_GROQ`: API key for Groq
- `PDF2ZH_API_KEY_DEEPSEEK`: API key for DeepSeek

### Examples

#### Translate a PDF from English to Chinese

```bash
pdf2zh --from en --to zh input.pdf
```

#### Translate specific pages

```bash
pdf2zh --pages 1-5 input.pdf
```

#### Use Azure Translator

```bash
pdf2zh --service azure --api-key YOUR_API_KEY --api-region eastus input.pdf
```

#### Use OpenAI GPT-4

```bash
pdf2zh --service openai --api-key YOUR_API_KEY --model gpt-4o input.pdf
```

#### Output as plain text

```bash
pdf2zh --output-format text input.pdf
```

### Troubleshooting

#### Common Issues

- **No translation occurs**: Check that the input file exists and is a valid PDF.
- **Translation is slow**: Try reducing the number of concurrent requests or using a faster service.
- **Translation quality is poor**: Try using a different service or model.
- **API errors**: Check that your API key is valid and has sufficient credits.

#### Getting Help

If you encounter any issues, please check the [FAQ](./FAQ.md) or open an issue on GitHub.

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

Важное поведение: `pdf2zh` автоматически попытается определить исходный язык, если `--from` не указан.

Если вы используете CLI, вы можете указать исходный язык с помощью `--from` и целевой язык с помощью `--to`:

```bash
pdf2zh --from en --to zh input.pdf
```

Если вы используете Python API, вы можете указать исходный язык с помощью `source_lang` и целевой язык с помощью `target_lang`:

```python
from pdf2zh import pdf2zh_sync

pdf2zh_sync(
    "input.pdf",
    "output.pdf",
    source_lang="en",
    target_lang="zh",
)
```

Если вы используете WebUI, вы можете выбрать исходный и целевой языки из выпадающих меню.

### Службы перевода

`pdf2zh` поддерживает несколько служб перевода. Вы можете выбрать службу, которая лучше всего соответствует вашим потребностям.

#### Google Translate

Google Translate — это служба по умолчанию. Она бесплатна и поддерживает широкий спектр языков.

Для использования Google Translate не требуется предоставлять какой-либо API-ключ.

```bash
pdf2zh --service google input.pdf
```

#### Azure Translator

Azure Translator — это платная служба, предлагающая высококачественные переводы.

Для использования Azure Translator необходимо предоставить API-ключ и регион.

```bash
pdf2zh --service azure --api-key YOUR_API_KEY --api-region YOUR_REGION input.pdf
```

#### OpenAI GPT

Модели OpenAI GPT можно использовать для перевода. Они платные и требуют API-ключ.

```bash
pdf2zh --service openai --api-key YOUR_API_KEY input.pdf
```

#### Anthropic Claude

Модели Anthropic Claude можно использовать для перевода. Они платные и требуют API-ключ.

```bash
pdf2zh --service anthropic --api-key YOUR_API_KEY input.pdf
```

#### Groq

Groq обеспечивает быстрое выполнение для различных моделей. Это платная служба и требует API-ключ.

```bash
pdf2zh --service groq --api-key YOUR_API_KEY input.pdf
```

#### DeepSeek

DeepSeek — это служба перевода, которая требует API-ключ.

```bash
pdf2zh --service deepseek --api-key YOUR_API_KEY input.pdf
```

### Расширенные параметры

#### Диапазон страниц

Вы можете указать диапазон страниц для перевода с помощью опции `--pages`.

```bash
pdf2zh --pages 1-5,10,15-20 input.pdf
```

Это переведет страницы с 1 по 5, страницу 10 и страницы с 15 по 20.

#### Формат вывода

Вы можете указать формат вывода с помощью опции `--output-format`. По умолчанию используется `markdown`.

Поддерживаемые форматы:
- `markdown`: формат Markdown
- `text`: формат обычного текста
- `pdf`: формат PDF (требуется, чтобы источник был в формате PDF)

```bash
pdf2zh --output-format text input.pdf
```

#### Модель перевода

Для служб, которые поддерживают несколько моделей, вы можете указать модель с помощью опции `--model`.

```bash
pdf2zh --service openai --model gpt-4o input.pdf
```

#### Параллельные запросы

Вы можете контролировать количество параллельных запросов к службе перевода с помощью опции `--concurrent-requests`. По умолчанию — 5.

```bash
pdf2zh --concurrent-requests 10 input.pdf
```

#### Таймаут

Вы можете установить таймаут для каждого запроса перевода с помощью опции `--timeout`. По умолчанию — 300 секунд.

```bash
pdf2zh --timeout 600 input.pdf
```

### Файл конфигурации

Вы можете создать файл конфигурации, чтобы избежать повторной передачи опций.

Создайте файл с именем `pdf2zh.config.json`:

```json
{
  "source_lang": "en",
  "target_lang": "zh",
  "service": "google",
  "output_format": "markdown",
  "concurrent_requests": 5,
  "timeout": 300
}
```

Затем вы можете запустить `pdf2zh` без каких-либо опций:

```bash
pdf2zh input.pdf
```

Файл конфигурации будет автоматически загружен, если он существует в текущем каталоге.

Вы также можете указать пользовательский файл конфигурации с помощью опции `--config`:

```bash
pdf2zh --config path/to/config.json input.pdf
```

### Переменные окружения

Вы можете установить переменные окружения, чтобы избежать повторной передачи API-ключей.

- `PDF2ZH_API_KEY_GOOGLE`: API-ключ для Google Translate (не требуется)
- `PDF2ZH_API_KEY_AZURE`: API-ключ для Azure Translator
- `PDF2ZH_API_REGION_AZURE`: Регион для Azure Translator
- `PDF2ZH_API_KEY_OPENAI`: API-ключ для OpenAI
- `PDF2ZH_API_KEY_ANTHROPIC`: API-ключ для Anthropic
- `PDF2ZH_API_KEY_GROQ`: API-ключ для Groq
- `PDF2ZH_API_KEY_DEEPSEEK`: API-ключ для DeepSeek

### Примеры

#### Перевод PDF с английского на китайский

```bash
pdf2zh --from en --to zh input.pdf
```

#### Перевод определенных страниц

```bash
pdf2zh --pages 1-5 input.pdf
```

#### Использование Azure Translator

```bash
pdf2zh --service azure --api-key YOUR_API_KEY --api-region eastus input.pdf
```

#### Использование OpenAI GPT-4

```bash
pdf2zh --service openai --api-key YOUR_API_KEY --model gpt-4o input.pdf
```

#### Вывод в виде обычного текста

```bash
pdf2zh --output-format text input.pdf
```

### Устранение неполадок

#### Распространенные проблемы

- **Перевод не происходит**: Убедитесь, что входной файл существует и является действительным PDF.
- **Перевод медленный**: Попробуйте уменьшить количество параллельных запросов или использовать более быструю службу.
- **Качество перевода низкое**: Попробуйте использовать другую службу или модель.
- **Ошибки API**: Убедитесь, что ваш API-ключ действителен и имеет достаточный кредит.

#### Получение помощи

Если у вас возникли проблемы, пожалуйста, проверьте [FAQ](./FAQ.md) или создайте issue на GitHub.
- The `finish` event may be followed by a `stage_summary` event.
- The `finish` event is only emitted for successful translations.
- The `error` event is emitted for both translation failures and stream processing errors.

---

### TRANSLATION RESULT

{#minimal-usage-example-async}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    result = await pdf2zh(
        "input.pdf",
        "output.pdf",
        # You can also use `target_lang_code` to specify the target language
        target_lang_code="ru",
    )
    print(result)

asyncio.run(main())
```

### Minimal Usage Example (Sync) {#minimal-usage-example-sync}

```python
from pdf2zh import pdf2zh_sync

result = pdf2zh_sync(
    "input.pdf",
    "output.pdf",
    target_lang_code="ru",
)
print(result)
```

### Minimal Usage Example (CLI) {#minimal-usage-example-cli}

```bash
pdf2zh input.pdf output.pdf --target-lang-code ru
```

---

### TRANSLATION
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

If you cancel your subscription, you will still have access to the features of the plan you paid for until the end of your billing period.

We do not provide refunds for subscription cancellations.

---

### TRANSLATION RESULT
python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    # Create a task for the translation stream
    task = asyncio.create_task(consume_stream())

    # Wait for a while
    await asyncio.sleep(1)

    # Cancel the task
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Translation cancelled")

async def consume_stream():
    async for progress, translated_text in do_translate_async_stream(
        file_path="input.pdf",
        target_lang="zh"
    ):
        print(f"Progress: {progress:.2%}")
        if translated_text:
            print(translated_text)

asyncio.run(main())
```

---

### TRANSLATION RESULT

Вы можете отменить задачу, потребляющую поток. Отмена передается в базовый процесс перевода.
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    # Создаем задачу для потока перевода
    task = asyncio.create_task(consume_stream())

    # Ждем некоторое время
    await asyncio.sleep(1)

    # Отменяем задачу
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Перевод отменен")

async def consume_stream():
    async for progress, translated_text in do_translate_async_stream(
        file_path="input.pdf",
        target_lang="zh"
    ):
        print(f"Прогресс: {progress:.2%}")
        if translated_text:
            print(translated_text)

asyncio.run(main())

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

The <a href="https://www.w3.org/TR/SVG/shapes.html#RectElement" target="_blank">SVG rectangle</a> `<rect>` is the most basic shape, used to create rectangles with various widths, heights, and corner radii.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="100" />
</svg>
```

The <a href="https://www.w3.org/TR/SVG/shapes.html#CircleElement" target="_blank">SVG circle</a> `<circle>` element is used to create circles based on a center point and radius.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <circle cx="60" cy="60" r="50" />
</svg>
```

The <a href="https://www.w3.org/TR/SVG/shapes.html#EllipseElement" target="_blank">SVG ellipse</a> `<ellipse>` is a more general form of the `<circle>` element, allowing you to scale the circle's radius independently in the x and y directions.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="60" cy="60" rx="50" ry="30" />
</svg>
```

The <a href="https://www.w3.org/TR/SVG/shapes.html#LineElement" target="_blank">SVG line</a> `<line>` element is used to create a line connecting two points.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="100" x2="100" y2="20" stroke="black" stroke-width="2" />
</svg>
```

The <a href="https://www.w3.org/TR/SVG/shapes.html#PolylineElement" target="_blank">SVG polyline</a> `<polyline>` element is used to create any shape consisting of only straight lines, and it is typically used to create open shapes.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <polyline points="20,100 40,60 70,80 100,20" fill="none" stroke="black" stroke-width="2" />
</svg>
```

The <a href="https://www.w3.org/TR/SVG/shapes.html#PolygonElement" target="_blank">SVG polygon</a> `<polygon>` element is similar to `<polyline>`, but it automatically connects the last point to the first point to form a closed shape.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,20 100,100 20,100" fill="none" stroke="black" stroke-width="2" />
</svg>
```

### Example Event Shapes

<a href="https://www.w3.org/TR/SVG/paths.html#PathElement" target="_blank">SVG path</a> `<path>` is the most powerful and complex element in SVG. You can use it to create lines, curves, arcs, and more.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <path d="M 10 10 C 20 20, 40 20, 50 10" stroke="black" fill="transparent" />
</svg>
```

---

### OUTPUT LANGUAGE

ru

---

### TRANSLATION

### Примеры фигур SVG

<a href="https://www.w3.org/TR/SVG/shapes.html#RectElement" target="_blank">Прямоугольник SVG</a> `<rect>` — это самая базовая фигура, используемая для создания прямоугольников с различной шириной, высотой и радиусами углов.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="100" height="100" />
</svg>
```

Элемент <a href="https://www.w3.org/TR/SVG/shapes.html#CircleElement" target="_blank">круг SVG</a> `<circle>` используется для создания кругов на основе центральной точки и радиуса.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <circle cx="60" cy="60" r="50" />
</svg>
```

<a href="https://www.w3.org/TR/SVG/shapes.html#EllipseElement" target="_blank">Эллипс SVG</a> `<ellipse>` является более общей формой элемента `<circle>`, позволяя независимо масштабировать радиус круга по направлениям x и y.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <ellipse cx="60" cy="60" rx="50" ry="30" />
</svg>
```

Элемент <a href="https://www.w3.org/TR/SVG/shapes.html#LineElement" target="_blank">линия SVG</a> `<line>` используется для создания линии, соединяющей две точки.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <line x1="20" y1="100" x2="100" y2="20" stroke="black" stroke-width="2" />
</svg>
```

Элемент <a href="https://www.w3.org/TR/SVG/shapes.html#PolylineElement" target="_blank">полилиния SVG</a> `<polyline>` используется для создания любой фигуры, состоящей только из прямых линий, и обычно используется для создания открытых фигур.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <polyline points="20,100 40,60 70,80 100,20" fill="none" stroke="black" stroke-width="2" />
</svg>
```

Элемент <a href="https://www.w3.org/TR/SVG/shapes.html#PolygonElement" target="_blank">полигон SVG</a> `<polygon>` похож на `<polyline>`, но он автоматически соединяет последнюю точку с первой, образуя замкнутую фигуру.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <polygon points="60,20 100,100 20,100" fill="none" stroke="black" stroke-width="2" />
</svg>
```

### Примеры фигур SVG

<a href="https://www.w3.org/TR/SVG/paths.html#PathElement" target="_blank">Путь SVG</a> `<path>` — это самый мощный и сложный элемент в SVG. С его помощью можно создавать линии, кривые, дуги и многое другое.

```html
<svg width="120" height="120" viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
  <path d="M 10 10 C 20 20, 40 20, 50 10" stroke="black" fill="transparent" />
</svg>
```
This event is emitted when a processing stage (e.g., OCR, translation) completes for a document. It provides a summary of the stage's execution.

Event type: `stage_summary`

Example event data:

```json
{
  "type": "stage_summary",
  "data": {
    "jobId": "550e8400-e29b-41d4-a716-446655440000",
    "stage": "ocr",
    "status": "completed",
    "duration": 1250,
    "pagesProcessed": 10,
    "metrics": {
      "charactersRecognized": 4520,
      "confidence": 0.92
    },
    "warnings": [
      "Low confidence on page 3",
      "Page 7 required manual review"
    ]
  },
  "timestamp": "2023-10-05T14:30:00.000Z"
}
```

Field descriptions:

- **jobId**: Unique identifier for the document processing job
- **stage**: Name of the processing stage (e.g., "ocr", "translation", "formatting")
- **status**: Stage completion status ("completed", "failed", "skipped")
- **duration**: Stage execution time in milliseconds
- **pagesProcessed**: Number of pages processed in this stage
- **metrics**: Stage-specific performance metrics
- **warnings**: Array of warning messages generated during stage execution

---

### TRANSLATION RESULT

### Сводное событие этапа (пример)

Это событие генерируется при завершении этапа обработки (например, OCR, перевод) для документа. Оно предоставляет сводку выполнения этапа.

Тип события: `stage_summary`

Пример данных события:

```json
{
  "type": "stage_summary",
  "data": {
    "jobId": "550e8400-e29b-41d4-a716-446655440000",
    "stage": "ocr",
    "status": "completed",
    "duration": 1250,
    "pagesProcessed": 10,
    "metrics": {
      "charactersRecognized": 4520,
      "confidence": 0.92
    },
    "warnings": [
      "Low confidence on page 3",
      "Page 7 required manual review"
    ]
  },
  "timestamp": "2023-10-05T14:30:00.000Z"
}
```

Описание полей:

- **jobId**: Уникальный идентификатор задания обработки документа
- **stage**: Название этапа обработки (например, "ocr", "translation", "formatting")
- **status**: Статус завершения этапа ("completed", "failed", "skipped")
- **duration**: Время выполнения этапа в миллисекундах
- **pagesProcessed**: Количество страниц, обработанных на этом этапе
- **metrics**: Этап-специфичные метрики производительности
- **warnings**: Массив предупреждающих сообщений, сгенерированных во время выполнения этапа
- ### Cancellation: If you cancel your subscription, you will still have access to the features of the plan you paid for until the end of your billing period.

We do not provide refunds for subscription cancellations.

---

### OUTPUT LANGUAGE

ru

---

### BYPASS LIST

- pdf2zh
- PDFMathTranslate
- ---

---

### ORIGINAL TEXT

Stage summary event (example): This event is emitted when a processing stage (e.g., OCR, translation) completes for a document. It provides a summary of the stage's execution.

Event type: `stage_summary`

Example event data:

```json
{
  "type": "stage_summary",
  "data": {
    "jobId": "550e8400-e29b-41d4-a716-446655440000",
    "stage": "ocr",
    "status": "completed",
    "duration": 1250,
    "pagesProcessed": 10,
    "metrics": {
      "charactersRecognized": 4520,
      "confidence": 0.92
    },
    "warnings": [
      "Low confidence on page 3",
      "Page 7 required manual review"
    ]
  },
  "timestamp": "2023-10-05T14:30:00.000Z"
}
```

Field descriptions:

- **jobId**: Unique identifier for the document processing job
- **stage**: Name of the processing stage (e.g., "ocr", "translation", "formatting")
- **status**: Stage completion status ("completed", "failed", "skipped")
- **duration**: Stage execution time in milliseconds
- **pagesProcessed**: Number of pages processed in this stage
- **metrics**: Stage-specific performance metrics
- **warnings**: Array of warning messages generated during stage execution

---

### TRANSLATION RESULT

### Сводное событие этапа (пример)

Это событие генерируется при завершении этапа обработки (например, OCR, перевод) для документа. Оно предоставляет сводку выполнения этапа.

Тип события: `stage_summary`

Пример данных события:

```json
{
  "type": "stage_summary",
  "data": {
    "jobId": "550e8400-e29b-41d4-a716-446655440000",
    "stage": "ocr",
    "status": "completed",
    "duration": 1250,
    "pagesProcessed": 10,
    "metrics": {
      "charactersRecognized": 4520,
      "confidence": 0.92
    },
    "warnings": [
      "Low confidence on page 3",
      "Page 7 required manual review"
    ]
  },
  "timestamp": "2023-10-05T14:30:00.000Z"
}
```

Описание полей:

- **jobId**: Уникальный идентификатор задания обработки документа
- **stage**: Название этапа обработки (например, "ocr", "translation", "formatting")
- **status**: Статус завершения этапа ("completed", "failed", "skipped")
- **duration**: Время выполнения этапа в миллисекундах
- **pagesProcessed**: Количество страниц, обработанных на этом этапе
- **metrics**: Этап-специфичные метрики производительности
- **warnings**: Массив предупреждающих сообщений, сгенерированных во время выполнения этапа
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

When the translation progress reaches 50%, an event with the following structure will be emitted:

```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Processing page 10 of 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```

---

### TRANSLATION RESULT

Событие прогресса (пример): Когда прогресс перевода достигает 50 %, будет сгенерировано событие со следующей структурой:

```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Processing page 10 of 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```
- ### Контракт потока событий

В этом документе описывается контракт для потока событий, используемого приложением. Он предназначен для разработчиков, которые хотят потреблять поток событий напрямую или интегрироваться с ним.

---

### Типы событий

Приложение генерирует следующие типы событий:

- **`translation_started`**: Генерируется при запуске задания на перевод.
- **`translation_progress`**: Периодически генерируется для отчета о прогрессе перевода.
- **`translation_completed`**: Генерируется при успешном завершении задания на перевод.
- **`translation_failed`**: Генерируется при сбое задания на перевод.
- **`translation_cancelled`**: Генерируется, когда пользователь отменяет задание на перевод.

---

### Структура данных события

Каждое событие представляет собой объект JSON со следующей структурой:

```json
{
  "type": "event_type",
  "data": {
    // Данные, специфичные для события
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

---

### Подробности событий

#### `translation_started`

Генерируется при запуске задания на перевод.

**Данные:**
- `jobId` (string): Уникальный идентификатор задания на перевод.
- `fileName` (string): Имя переводимого файла.

**Пример:**
```json
{
  "type": "translation_started",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

#### `translation_progress`

Периодически генерируется для отчета о прогрессе перевода.

**Данные:**
- `jobId` (string): Уникальный идентификатор задания на перевод.
- `progress` (number): Процент выполнения (0-100).
- `message` (string): Необязательное сообщение о прогрессе.

**Пример:**
```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Processing page 10 of 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```

#### `translation_completed`

Генерируется при успешном завершении задания на перевод.

**Данные:**
- `jobId` (string): Уникальный идентификатор задания на перевод.
- `fileName` (string): Имя переведенного файла.
- `outputPath` (string): Путь к переведенному файлу.

**Пример:**
```json
{
  "type": "translation_completed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "outputPath": "/path/to/translated/document_zh.pdf"
  },
  "timestamp": "2023-01-01T00:00:02.000Z"
}
```

#### `translation_failed`

Генерируется при сбое задания на перевод.

**Данные:**
- `jobId` (string): Уникальный идентификатор задания на перевод.
- `fileName` (string): Имя файла, который не удалось перевести.
- `error` (string): Сообщение об ошибке.

**Пример:**
```json
{
  "type": "translation_failed",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf",
    "error": "Failed to extract text from PDF"
  },
  "timestamp": "2023-01-01T00:00:03.000Z"
}
```

#### `translation_cancelled`

Генерируется, когда пользователь отменяет задание на перевод.

**Данные:**
- `jobId` (string): Уникальный идентификатор задания на перевод.
- `fileName` (string): Имя файла, который переводился.

**Пример:**
```json
{
  "type": "translation_cancelled",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "fileName": "document.pdf"
  },
  "timestamp": "2023-01-01T00:00:04.000Z"
}
```

---

### Потребление потока событий

Поток событий доступен по адресу `/api/events` при запущенном приложении. События отправляются как события, отправляемые сервером (SSE).

**Пример на JavaScript:**
```javascript
const eventSource = new EventSource('/api/events');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received event:', data);
};

eventSource.onerror = (error) => {
  console.error('EventSource failed:', error);
};
```

---

### Примечания

- События генерируются в реальном времени по мере выполнения заданий на перевод.
- Поток событий может содержать события из нескольких параллельных заданий на перевод.
- Клиенты должны фильтровать события по `jobId`, если они интересуются конкретными заданиями.
- Соединение с потоком событий может быть автоматически восстановлено при разрыве.
- ### Минимальный пример использования (асинхронный) {#minimal-usage-example-async}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    result = await pdf2zh(
        "input.pdf",
        "output.pdf",
        # Вы также можете использовать `target_lang_code` для указания целевого языка
        target_lang_code="ru",
    )
    print(result)

asyncio.run(main())
```

### Минимальный пример использования (синхронный) {#minimal-usage-example-sync}

```python
from pdf2zh import pdf2zh_sync

result = pdf2zh_sync(
    "input.pdf",
    "output.pdf",
    target_lang_code="ru",
)
print(result)
```

### Минимальный пример использования (CLI) {#minimal-usage-example-cli}

```bash
pdf2zh input.pdf output.pdf --target-lang-code ru
```

---

### ПЕРЕВОД
- ### Отмена: Если вы отмените подписку, у вас по-прежнему будет доступ к функциям оплаченного тарифного плана до конца расчетного периода.

Мы не предоставляем возмещение за отмену подписок.

---

### РЕЗУЛЬТАТ ПЕРЕВОДА
- ### Примечания и рекомендации: - **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда сначала тестируйте функцию на некритичном документе, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии оригинальных документов перед обработкой.
- **Проверьте результаты**: После обработки проверьте документ, чтобы убедиться в точности перевода и сохранении форматирования.

---

### ЯЗЫК ВЫВОДА

ru

---

### СПИСОК ИСКЛЮЧЕНИЙ

- pdf2zh
- PDFMathTranslate
- ---

---

### ОРИГИНАЛЬНЫЙ ТЕКСТ

Событие прогресса (пример): Когда прогресс перевода достигает 50 %, будет сгенерировано событие со следующей структурой:

```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Обработка страницы 10 из 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
```

---

### РЕЗУЛЬТАТ ПЕРЕВОДА

Событие прогресса (пример): Когда прогресс перевода достигает 50 %, будет сгенерировано событие со следующей структурой:

```json
{
  "type": "translation_progress",
  "data": {
    "jobId": "123e4567-e89b-12d3-a456-426614174000",
    "progress": 50,
    "message": "Обработка страницы 10 из 20"
  },
  "timestamp": "2023-01-01T00:00:01.000Z"
}
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

The finish event is emitted when the readable stream has been consumed and all data has been flushed. This event is emitted only once.

```javascript
const { Readable } = require('stream');

const readable = Readable.from(['hello', 'world']);

readable.on('finish', () => {
  console.log('Stream finished');
});

readable.resume(); // Consume the stream
```

---

### TRANSLATION RESULT

Событие завершения (пример): Событие `finish` генерируется, когда читаемый поток потреблен и все данные сброшены. Это событие генерируется только один раз.

```javascript
const { Readable } = require('stream');

const readable = Readable.from(['hello', 'world']);

readable.on('finish', () => {
  console.log('Stream finished');
});

readable.resume(); // Потребляем поток
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

json
{
  "type": "error",
  "data": {
    "message": "Failed to process the document",
    "code": "DOCUMENT_PROCESSING_ERROR"
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```

---

### TRANSLATION RESULT

Событие ошибки (пример): 

```json
{
  "type": "error",
  "data": {
    "message": "Failed to process the document",
    "code": "DOCUMENT_PROCESSING_ERROR"
  },
  "timestamp": "2023-01-01T00:00:00.000Z"
}
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

- **Use with Caution**: Be cautious when using this feature, especially if the document contains sensitive information.
- **Test First**: Always test the feature on a non-critical document first to ensure it meets your expectations.
- **Backup Documents**: Keep backups of your original documents before processing.
- **Check Results**: After processing, review the document to ensure the translation is accurate and the formatting is preserved.

---

### OUTPUT LANGUAGE

ru
---

### TRANSLATION RESULT

### Примечания и рекомендации

- **Используйте с осторожностью**: Будьте осторожны при использовании этой функции, особенно если документ содержит конфиденциальную информацию.
- **Сначала протестируйте**: Всегда сначала тестируйте функцию на некритичном документе, чтобы убедиться, что она соответствует вашим ожиданиям.
- **Резервное копирование документов**: Сохраняйте резервные копии исходных документов перед обработкой.
- **Проверяйте результаты**: После обработки просмотрите документ, чтобы убедиться, что перевод точен, а форматирование сохранено.

---

- Всегда обрабатывайте как события ошибок, так и исключения из генератора.
- Прерывайте цикл при `finish`, чтобы избежать ненужной работы.
- Убедитесь, что `file` существует и `settings.validate_settings()` проходит успешно перед вызовом.
- Большие документы могут быть разделены; используйте `part_index/total_parts` и `overall_progress` для управления вашим пользовательским интерфейсом.
- Дебаунсите `progress_update`, если ваш пользовательский интерфейс чувствителен к повторяющимся, идентичным обновлениям.
- `report_interval` (SettingsModel): управляет только частотой генерации событий `progress_update`. Он не влияет на `stage_summary`, `progress_start`, `progress_end` или `finish`. По умолчанию 0.1 с, минимально допустимое значение — 0.05 с. Согласно логике монитора прогресса, когда `stage_total <= 3`, обновления не регулируются `report_interval`.

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>