[**Расширенные параметры**](./introduction.md) > **Расширенные параметры** _(текущая)_

---

<h3 id="содержание">Содержание</h3>

- [Аргументы командной строки](#аргументы-командной-строки)
- [Руководство по настройке ограничения скорости](#руководство-по-настройке-ограничения-скорости)
- [Частичный перевод](#частичный-перевод)
- [Указание исходного и целевого языков](#указание-исходного-и-целевого-языков)
- [Перевод с исключениями](#перевод-с-исключениями)
- [Пользовательский промпт](#пользовательский-промпт)
- [Пользовательская конфигурация](#пользовательская-конфигурация)
- [Пропуск очистки](#пропуск-очистки)
- [Кеширование перевода](#кеширование-перевода)
- [Развертывание как публичный сервис](#развертывание-как-публичный-сервис)
- [Аутентификация и приветственная страница](#аутентификация-и-приветственная-страница)
- [Поддержка глоссария](#поддержка-глоссария)

---

#### Аргументы командной строки

Выполните команду перевода в командной строке, чтобы сгенерировать переведенный документ `example-mono.pdf` и двуязычный документ `example-dual.pdf` в текущей рабочей директории. В качестве сервиса перевода по умолчанию используется Google. Дополнительные поддерживаемые сервисы перевода можно найти [ЗДЕСЬ](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

В следующей таблице перечислены все расширенные параметры для справки:

##### Аргументы

| `output-directory`              | Output directory for translated files (default: `_translated`)                           | `pdf2zh_next example.pdf --output-directory ./output`                                                                 |
| `translation-service`           | Translation service to use (default: `google` or `google_free`)                          | `pdf2zh_next example.pdf --translation-service deepl`                                                                 |
| `source-language`               | Source language (ISO 639-1 code) (default: `en`)                                        | `pdf2zh_next example.pdf --source-language ja`                                                                        |
| `target-language`               | Target language (ISO 639-1 code) (default: `zh`)                                        | `pdf2zh_next example.pdf --target-language fr`                                                                        |
| `translation-options`           | Additional options for the translation service (JSON format)                            | `pdf2zh_next example.pdf --translation-options '{"formality": "more"}'`                                               |
| `concurrency-limit`             | Maximum number of concurrent translation requests (default: 5)                          | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `page-range`                    | Specific page range to translate (e.g., "1-5,8,10-15")                                 | `pdf2zh_next example.pdf --page-range "1-10"`                                                                         |
| `ocr`                           | Enable OCR for images and scanned documents (default: false)                            | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `ocr-language`                  | Language for OCR (ISO 639-1 code) (default: `en`)                                       | `pdf2zh_next example.pdf --ocr --ocr-language ja`                                                                     |
| `ocr-resolution`                | Resolution for OCR in DPI (default: 300)                                                | `pdf2zh_next example.pdf --ocr --ocr-resolution 150`                                                                  |
| `math-translate`                | Enable translation of mathematical formulas (default: false)                            | `pdf2zh_next example.pdf --math-translate`                                                                            |
| `math-mode`                     | Mode for mathematical formula translation (default: `both`)                             | `pdf2zh_next example.pdf --math-translate --math-mode hybrid`                                                         |
| `math-method`                   | Method for mathematical formula translation (default: `pdf2zh`)                         | `pdf2zh_next example.pdf --math-translate --math-method PDFMathTranslate`                                             |
| `math-options`                  | Additional options for mathematical formula translation (JSON format)                   | `pdf2zh_next example.pdf --math-translate --math-options '{"keep_original": true}'`                                   |
| `cache`                         | Enable caching of translations (default: true)                                          | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `cache-directory`               | Directory for cache files (default: `_cache`)                                           | `pdf2zh_next example.pdf --cache-directory ./my_cache`                                                                |
| `clean-cache`                   | Clean the cache before processing (default: false)                                      | `pdf2zh_next example.pdf --clean-cache`                                                                               |
| `config`                        | Path to a configuration file                                                            | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `help`                          | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |
| `version`                       | Show version information                                                                | `pdf2zh_next --version`                                                                                               |

---

### TRANSLATED TEXT

| Опция                          | Функция                                                                               | Пример                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Входные PDF-файлы для обработки                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `output-directory`              | Выходная директория для переведённых файлов (по умолчанию: `_translated`)                           | `pdf2zh_next example.pdf --output-directory ./output`                                                                 |
| `translation-service`           | Служба перевода для использования (по умолчанию: `google` или `google_free`)                          | `pdf2zh_next example.pdf --translation-service deepl`                                                                 |
| `source-language`               | Исходный язык (код ISO 639-1) (по умолчанию: `en`)                                        | `pdf2zh_next example.pdf --source-language ja`                                                                        |
| `target-language`               | Целевой язык (код ISO 639-1) (по умолчанию: `zh`)                                        | `pdf2zh_next example.pdf --target-language fr`                                                                        |
| `translation-options`           | Дополнительные опции для службы перевода (формат JSON)                            | `pdf2zh_next example.pdf --translation-options '{"formality": "more"}'`                                               |
| `concurrency-limit`             | Максимальное количество одновременных запросов перевода (по умолчанию: 5)                          | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `page-range`                    | Определённый диапазон страниц для перевода (например, "1-5,8,10-15")                                 | `pdf2zh_next example.pdf --page-range "1-10"`                                                                         |
| `ocr`                           | Включить OCR для изображений и сканированных документов (по умолчанию: false)                            | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `ocr-language`                  | Язык для OCR (код ISO 639-1) (по умолчанию: `en`)                                       | `pdf2zh_next example.pdf --ocr --ocr-language ja`                                                                     |
| `ocr-resolution`                | Разрешение для OCR в DPI (по умолчанию: 300)                                                | `pdf2zh_next example.pdf --ocr --ocr-resolution 150`                                                                  |
| `math-translate`                | Включить перевод математических формул (по умолчанию: false)                            | `pdf2zh_next example.pdf --math-translate`                                                                            |
| `math-mode`                     | Режим перевода математических формул (по умолчанию: `both`)                             | `pdf2zh_next example.pdf --math-translate --math-mode hybrid`                                                         |
| `math-method`                   | Метод перевода математических формул (по умолчанию: `pdf2zh`)                         | `pdf2zh_next example.pdf --math-translate --math-method PDFMathTranslate`                                             |
| `math-options`                  | Дополнительные опции для перевода математических формул (формат JSON)                   | `pdf2zh_next example.pdf --math-translate --math-options '{"keep_original": true}'`                                   |
| `cache`                         | Включить кэширование переводов (по умолчанию: true)                                          | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `cache-directory`               | Директория для файлов кэша (по умолчанию: `_cache`)                                           | `pdf2zh_next example.pdf --cache-directory ./my_cache`                                                                |
| `clean-cache`                   | Очистить кэш перед обработкой (по умолчанию: false)                                      | `pdf2zh_next example.pdf --clean-cache`                                                                               |
| `config`                        | Путь к файлу конфигурации                                                            | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `help`                          | Показать сообщение справки                                                                       | `pdf2zh_next --help`                                                                                                  |
| `version`                       | Показать информацию о версии                                                                | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang`                        | Language code of the output file, default is `zh`, [supported languages](#supported-languages) | `pdf2zh_next example.pdf --lang ru`                                                                                   |
| `--translator`                  | Translation service to use, default is `google`, [supported translators](#supported-translators)   | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-key`              | API Key for the translation service                                                     | `pdf2zh_next example.pdf --translator deepl --translator-key your-deepl-key`                                          |
| `--translator-url`              | API URL for the translation service (for self-hosted services)                           | `pdf2zh_next example.pdf --translator deepl --translator-url https://api-free.deepl.com`                              |
| `--translator-model`            | Model for the translation service (for OpenAI)                                           | `pdf2zh_next example.pdf --translator openai --translator-model gpt-3.5-turbo`                                        |
| `--translator-context`          | Whether to use context for translation, default is `true`                               | `pdf2zh_next example.pdf --translator-context false`                                                                  |
| `--translator-timeout`          | Timeout for the translation service in seconds, default is `10`                         | `pdf2zh_next example.pdf --translator-timeout 20`                                                                     |
| `--translator-retries`          | Number of retries for the translation service, default is `3`                           | `pdf2zh_next example.pdf --translator-retries 5`                                                                      |
| `--translator-batch-size`       | Batch size for the translation service, default is `50`                                 | `pdf2zh_next example.pdf --translator-batch-size 100`                                                                 |
| `--translator-batch-delay`      | Delay between batches in seconds, default is `1`                                        | `pdf2zh_next example.pdf --translator-batch-delay 2`                                                                  |
| `--translator-batch-concurrency`| Number of concurrent batches, default is `1`                                            | `pdf2zh_next example.pdf --translator-batch-concurrency 3`                                                            |
| `--translator-batch-timeout`    | Timeout for each batch in seconds, default is `30`                                      | `pdf2zh_next example.pdf --translator-batch-timeout 60`                                                               |
| `--translator-batch-retries`    | Number of retries for each batch, default is `3`                                        | `pdf2zh_next example.pdf --translator-batch-retries 5`                                                                |
| `--translator-batch-delay-retry`| Delay between retries in seconds, default is `1`                                        | `pdf2zh_next example.pdf --translator-batch-delay-retry 2`                                                            |
| `--translator-batch-concurrency-retry`| Number of concurrent retries, default is `1`                                        | `pdf2zh_next example.pdf --translator-batch-concurrency-retry 3`                                                      |
| `--translator-batch-timeout-retry`| Timeout for each retry in seconds, default is `30`                                    | `pdf2zh_next example.pdf --translator-batch-timeout-retry 60`                                                         |
| `--translator-batch-retries-retry`| Number of retries for each retry, default is `3`                                      | `pdf2zh_next example.pdf --translator-batch-retries-retry 5`                                                          |
| `--translator-batch-delay-retry-retry`| Delay between retries for retries in seconds, default is `1`                        | `pdf2zh_next example.pdf --translator-batch-delay-retry-retry 2`                                                      |
| `--translator-batch-concurrency-retry-retry`| Number of concurrent retries for retries, default is `1`                        | `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry 3`                                                |
| `--translator-batch-timeout-retry-retry`| Timeout for each retry for retries in seconds, default is `30`                    | `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry 60`                                                   |
| `--translator-batch-retries-retry-retry`| Number of retries for each retry for retries, default is `3`                      | `pdf2zh_next example.pdf --translator-batch-retries-retry-retry 5`                                                    |
| `--translator-batch-delay-retry-retry-retry`| Delay between retries for retries for retries in seconds, default is `1`        | `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry 2`                                                |
| `--translator-batch-concurrency-retry-retry-retry`| Number of concurrent retries for retries for retries, default is `1`        | `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry 3`                                          |
| `--translator-batch-timeout-retry-retry-retry`| Timeout for each retry for retries for retries in seconds, default is `30`    | `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry 60`                                             |
| `--translator-batch-retries-retry-retry-retry`| Number of retries for each retry for retries for retries, default is `3`      | `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry 5`                                              |
| `--translator-batch-delay-retry-retry-retry-retry`| Delay between retries for retries for retries for retries in seconds, default is `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry 2`                                          |
| `--translator-batch-concurrency-retry-retry-retry-retry`| Number of concurrent retries for retries for retries for retries, default is `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry 3`                                    |
| `--translator-batch-timeout-retry-retry-retry-retry`| Timeout for each retry for retries for retries for retries in seconds, default is `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry 60`                                       |
| `--translator-batch-retries-retry-retry-retry-retry`| Number of retries for each retry for retries for retries for retries, default is `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry 5`                                        |
| `--translator-batch-delay-retry-retry-retry-retry-retry`| Delay between retries for retries for retries for retries for retries in seconds, default is `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry-retry 2`                                    |
| `--translator-batch-concurrency-retry-retry-retry-retry-retry`| Number of concurrent retries for retries for retries for retries for retries, default is `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry-retry 3`                              |
| `--translator-batch-timeout-retry-retry-retry-retry-retry`| Timeout for each retry for retries for retries for retries for retries in seconds, default is `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry-retry 60`                                 |
| `--translator-batch-retries-retry-retry-retry-retry-retry`| Number of retries for each retry for retries for retries for retries for retries, default is `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry-retry 5`                                  |
| `--translator-batch-delay-retry-retry-retry-retry-retry-retry`| Delay between retries for retries for retries for retries for retries for retries in seconds, default is `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry-retry-retry 2`                              |
| `--translator-batch-concurrency-retry-retry-retry-retry-retry-retry`| Number of concurrent retries for retries for retries for retries for retries for retries, default is `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry-retry-retry 3`                        |
| `--translator-batch-timeout-retry-retry-retry-retry-retry-retry`| Timeout for each retry for retries for retries for retries for retries for retries in seconds, default is `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry-retry-retry 60`                           |
| `--translator-batch-retries-retry-retry-retry-retry-retry-retry`| Number of retries for each retry for retries for retries for retries for retries for retries, default is `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry-retry-retry 5`                            |
| `--translator-batch-delay-ret 极-retry-retry-retry-retry-retry-retry`| Delay between retries for retries for retries for retries for retries for retries for retries in seconds, default is `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry-retry-retry-retry 2`                        |
| `--translator-batch-concurrency-retry-retry-retry-retry-retry-retry-retry`| Number of concurrent retries for retries for retries for retries for retries for retries for retries, default is `1`| `pdf2zh_next example.pdf --translator 极-batch-concurrency-retry-retry-retry-retry-retry-retry-retry 3`                |
| `--translator-batch-timeout-retry-retry-retry-retry-retry-retry-retry`| Timeout for each retry for retries for retries for retries for retries for retries for retries in seconds, default is `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry-retry-retry-retry 60`                     |
| `--translator-batch-retries-retry-retry-retry 极-retry-retry-retry`| Number of retries for each retry for retries for retries for retries for retries for retries for retries, default is `极`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry-retry-retry-retry 5`                      |

---

### TRANSLATION RESULT

| `--output`                      | Выходной каталог для файлов                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang`                        | Код языка выходного файла, по умолчанию `zh`, [поддерживаемые языки](#supported-languages) | `pdf2zh_next example.pdf --lang ru`                                                                                   |
| `--translator`                  | Служба перевода для использования, по умолчанию `google`, [поддерживаемые переводчики](#supported-translators)   | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-key`              | API Key для службы перевода                                                     | `pdf 极 2zh_next example.pdf --translator deepl --translator-key your-deepl-key`                                          |
| `--translator-url`              | API URL для службы перевода (для самодостаточных служб)                           | `pdf2zh_next example.pdf --translator deepl --translator-url https://api-free.deepl.com`                              |
| `--translator-model`            | Модель для службы перевода (для OpenAI)                                           | `pdf2zh_next example.pdf --translator openai --translator-model gpt-3.5-turbo`                                        |
| `--translator-context`          | Использовать ли контекст для перевода, по умолчанию `true`                               | `pdf2zh_next example.pdf --translator-context false`                                                                  |
| `--translator-timeout`          | Таймаут для службы перевода в секундах, по умолчанию `10`                         | `pdf2zh_next example.pdf --translator-timeout 20`                                                                     |
| `--translator-retries`          | Количество повторных попыток для службы перевода, по умолчанию `3`                           | `pdf2zh_next example.pdf --translator-retries 5`                                                                      |
| `--translator-batch-size`       | Размер пакета для службы перевода, по умолчанию `50`                                 | `pdf2zh_next example.pdf --translator-batch-size 100`                                                                 |
| `--translator-batch-delay`      | Задержка между пакетами в секундах, по умолчанию `1`                                        | `pdf2zh_next example.pdf --translator-batch-del 极 ay 2`                                                                  |
| `--translator-batch-concurrency`| Количество параллельных пакетов, по умолчанию `1`                                            | `pdf2zh_next example.pdf --translator-batch-concurrency 3`                                                            |
| `--translator-batch-timeout`    | Таймаут для каждого пакета в секундах, по умолчанию `30`                                      | `pdf2zh_next example.pdf --translator-batch-timeout 60`                                                               |
| `--translator-batch-retries`    | Количество повторных попыток для каждого пакета, по умолчанию `3`                                        | `pdf2zh_next example.pdf --translator-batch-retries 5`                                                                |
| `--translator-batch-delay-retry`| Задержка между повторными попытками в секундах, по умолчанию `1`                                        | `pdf2zh_next example.pdf --translator-batch-delay-retry 2`                                                            |
| `--translator-batch-concurrency-retry`| Количество параллельных повторных попыток, по умолчанию `1`                                        | `pdf2zh_next example.pdf --translator-batch-concurrency-retry 3`                                                      |
| `--translator-batch-timeout-retry`| Таймаут для каждой повторной попытки в секундах, по умолчанию `30`                                    | `pdf2zh_next example.pdf --translator-batch-timeout-retry 极 60`                                                         |
| `--translator-batch-retries-retry`| Количество повторных попыток для каждой повторной попытки, по умолчанию `3`                                      | `pdf2zh_next example.pdf --translator-batch-retries-retry 5`                                                          |
| `--translator-batch-delay-retry-retry`| Задержка между повторными попытками для повторных попыток в секундах, по умолчанию `1`                        | `pdf2zh_next example.pdf --translator-batch-delay-retry-retry 2`                                                      |
| `--translator-batch-concurrency-retry-retry`| Количество параллельных повторных попыток для повторных попыток, по умолчанию `1`                        | `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry 3`                                                |
| `--translator-batch-timeout-retry-retry`| Таймаут для каждой повторной попытки для повторных попыток в секундах, по умолчанию `30`                    | `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry 60`                                                   |
| `--translator 极-batch-retries-retry-retry`| Количество повторных попыток для каждой повторной попытки для повторных попыток, по умолчанию `3`                      | `pdf2zh_next example.pdf --translator-batch-retries-retry-retry 5`                                                    |
| `--translator-batch-delay-retry-retry-retry`| Задержка между повторными попытками для повторных попыток для повторных попыток в секундах, по умолчанию `1`        | `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry 2`                                                |
| `--translator-batch-concurrency-retry-retry-retry`| Количество параллельных повторных попыток для повторных попыток для повторных попыток, по умолчанию `1`        | `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry 3`                                          |
| `--translator-batch-timeout-retry-retry-retry`| Таймаут для каждой повторной попытки для повторных попыток для повторных попыток в секундах, по умолчанию `30`    | `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry 60`                                             |
| `--translator-batch-retries-retry-retry-retry`| Количество повторных попыток для каждой повторной попытки для повторных попыток для повторных попыток, по умолчанию `3`      | `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry 5`                                              |
| `--translator-batch-delay-retry-retry-retry-retry`| Задержка между повторными попытками для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry 2`                                          |
| `--translator-batch-concurrency-retry-retry 极-retry-retry`| Количество параллельных повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry 3`                                    |
| `--translator-batch-timeout-retry-retry-retry-retry`| Таймаут для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry 60`                                       |
| `--translator-batch-retries-retry-retry-retry-retry`| Количество повторных попыток для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток, по умолчанию `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry 5`                                        |
| `--translator-batch-delay-retry-retry-retry-retry-retry`| Задержка между повторными попытками для повторных попыток для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `极 1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-ret 极 ry-retry-retry-retry 2`                                    |
| `--translator-batch-concurrency-retry-retry-retry-retry-retry`| Количество параллельных повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry-retry 3`                              |
| `--translator-batch-timeout-retry-retry-retry-retry-retry`| Таймаут для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry-retry 60`                                 |
| `--translator-batch-retries-retry-retry-retry-retry-retry`| Количество повторных попыток для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry-retry 5`                                  |
| `--translator-batch-delay-retry-retry-retry-retry-retry-retry`| Задержка между повторными попытками для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry-retry-retry 2`                              |
| `--translator-batch-concurrency-retry-retry-retry-ret 极 ry-retry-retry`| Количество параллельных повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry-retry-retry 3`                        |
| `--translator-batch-timeout-retry-retry-retry-retry-retry-retry`| Таймаут для каждой повторной попытки для повторных попыток для повторных попыток для повторных поп极ыток для повторных попыток для повторных попыток в секундах, по умолчанию `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry-retry-retry 60`                           |
| `--translator-batch-retries-retry-retry-retry-retry-retry-retry`| Количество повторных попыток для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry 极-retry-retry 5`                            |
| `--translator-batch-delay-retry-retry-retry-retry-retry-retry-retry`| Задержка между повторными попытками для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-delay-retry-retry-retry-retry-retry-retry-retry 2`                        |
| `--translator-batch-concurrency-retry-retry-retry-retry-retry-retry-retry`| Количество параллельных повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `1`| `pdf2zh_next example.pdf --translator-batch-concurrency-retry-retry-retry-retry-retry-retry-retry 3`                |
| `--translator-batch-timeout-retry-retry-retry-retry-retry-retry-retry`| Таймаут для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток в секундах, по умолчанию `30`| `pdf2zh_next example.pdf --translator-batch-timeout-retry-retry-retry-retry-retry-retry-retry 60`                     |
| `--translator-batch-retries-retry-retry-retry-retry-retry-retry-retry`| Количество повторных попыток для каждой повторной попытки для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток для повторных попыток, по умолчанию `3`| `pdf2zh_next example.pdf --translator-batch-retries-retry-retry-retry-retry-retry-retry-retry 5`                      |
| ------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Languages>`                 | Set source/target language                                                            | `pdf2zh_next example.pdf --source-lang en --target-lang zh`                                                           |
| `--<Output>`                    | Set output file/folder name                                                           | `pdf2zh_next example.pdf --output example_translated.pdf`<br>`pdf2zh_next example.pdf --output-dir ./translated_pdfs` |
| `--<Advanced>`                  | Set advanced options                                                                   | `pdf2zh_next example.pdf --page 1-5,10`<br>`pdf2zh_next example.pdf --ocr`                                            |

---

### OUTPUT

| `--<Services>`                  | Использование [**специфического сервиса**](./Documentation-of-Translation-Services.md) для перевода | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Languages>`                 | Установка исходного/целевого языка                                                                  | `pdf2zh_next example.pdf --source-lang en --target-lang zh`                                                           |
| `--<Output>`                    | Установка имени выходного файла/папки                                                               | `pdf2zh_next example.pdf --output example_translated.pdf`<br>`pdf2zh_next example.pdf --output-dir ./translated_pdfs` |
| `--<Advanced>`                  | Установка расширенных параметров                                                                    | `pdf2zh_next example.pdf --page 1-5,10`<br>`pdf2zh_next example.pdf --ocr`                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--config`, `-c` <br> `CONFIG`  | Path to the config file. If not provided, the program will look for `config.toml` in the current directory | `pdf2zh_next -c config.toml` <br> `pdf2zh_next --config config.toml`                                                  |
| `--input`, `-i` <br> `INPUT`    | Path to the input PDF file or directory                                                 | `pdf2zh_next -i input.pdf` <br> `pdf2zh_next --input input.pdf`                                                       |
| `--output`, `-o` <br> `OUTPUT`  | Path to the output directory                                                            | `pdf2zh_next -o output/` <br> `pdf2zh_next --output output/`                                                          |
| `--engine`, `-e` <br> `ENGINE`  | Translation engine to use. Available options: `google`, `deepl`, `openai`               | `pdf2zh_next -e google` <br> `pdf2zh_next --engine openai`                                                            |
| `--target`, `-t` <br> `TARGET`  | Target language code. Defaults to `zh` (Chinese)                                        | `pdf2zh_next -t ja` <br> `pdf2zh_next --target ja`                                                                    |
| `--source`, `-s` <br> `SOURCE`  | Source language code. Defaults to `en` (English)                                        | `pdf2zh_next -s en` <br> `pdf2zh_next --source en`                                                                    |
| `--key`, `-k` <br> `KEY`        | API key for the translation engine. If not provided, the program will look for the key in the config file or environment variables | `pdf2zh_next -k YOUR_API_KEY` <br> `pdf2zh_next --key YOUR_API_KEY`                                                   |
| `--concurrency`, `-C` <br> `CONCURRENCY` | Number of concurrent translation tasks. Defaults to `4`                                 | `pdf2zh_next -C 8` <br> `pdf2zh_next --concurrency 8`                                                                 |
| `--retry`, `-r` <br> `RETRY`    | Number of retries for failed translation tasks. Defaults to `3`                         | `pdf2zh_next -r 5` <br> `pdf2zh_next --retry 5`                                                                       |
| `--timeout`, `-T` <br> `TIMEOUT` | Timeout in seconds for each translation request. Defaults to `30`                       | `pdf2zh_next -T 60` <br> `pdf2zh_next --timeout 60`                                                                   |
| `--proxy`, `-p` <br> `PROXY`    | Proxy server to use for translation requests. Format: `http://user:pass@host:port`      | `pdf2zh_next -p http://user:pass@proxy.example.com:8080` <br> `pdf2zh_next --proxy http://user:pass@proxy.example.com:8080` |
| `--verbose`, `-V`               | Enable verbose output                                                                   | `pdf2zh_next -V` <br> `pdf2zh_next --verbose`                                                                         |

---

### TRANSLATION RESULT

| `--help`, `-h`                  | Показать справочное сообщение и выйти                                                   | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Показать версию и выйти                                                                 | `pdf2zh_next -v`                                                                                                      |
| `--config`, `-c` <br> `CONFIG`  | Путь к файлу конфигурации. Если не указан, программа будет искать `config.toml` в текущей директории | `pdf2zh_next -c config.toml` <br> `pdf2zh_next --config config.toml`                                                  |
| `--input`, `-i` <br> `INPUT`    | Путь к входному PDF-файлу или директории                                                | `pdf2zh_next -i input.pdf` <br> `pdf2zh_next --input input.pdf`                                                       |
| `--output`, `-o` <br> `OUTPUT`  | Путь к выходной директории                                                              | `pdf2zh_next -o output/` <br> `pdf2zh_next --output output/`                                                          |
| `--engine`, `-e` <br> `ENGINE`  | Движок перевода для использования. Доступные опции: `google`, `deepl`, `openai`         | `pdf2zh_next -e google` <br> `pdf2zh_next --engine openai`                                                            |
| `--target`, `-t` <br> `TARGET`  | Код языка назначения. По умолчанию `zh` (китайский)                                     | `pdf2zh_next -t ja` <br> `pdf2zh_next --target ja`                                                                    |
| `--source`, `-s` <br> `SOURCE`  | Код исходного языка. По умолчанию `en` (английский)                                     | `pdf2zh_next -s en` <br> `pdf2zh_next --source en`                                                                    |
| `--key`, `-k` <br> `KEY`        | API-ключ для движка перевода. Если не указан, программа будет искать ключ в файле конфигурации или переменных окружения | `pdf2zh_next -k YOUR_API_KEY` <br> `pdf2zh_next --key YOUR_API_KEY`                                                   |
| `--concurrency`, `-C` <br> `CONCURRENCY` | Количество параллельных задач перевода. По умолчанию `4`                                | `pdf2zh_next -C 8` <br> `pdf2zh_next --concurrency 8`                                                                 |
| `--retry`, `-r` <br> `RETRY`    | Количество повторных попыток для неудачных задач перевода. По умолчанию `3`             | `pdf2zh_next -r 5` <br> `pdf2zh_next --retry 5`                                                                       |
| `--timeout`, `-T` <br> `TIMEOUT` | Таймаут в секундах для каждого запроса перевода. По умолчанию `30`                      | `pdf2zh_next -T 60` <br> `pdf2zh_next --timeout 60`                                                                   |
| `--proxy`, `-p` <br> `PROXY`    | Прокси-сервер для использования в запросах перевода. Формат: `http://user:pass@host:port` | `pdf2zh_next -p http://user:pass@proxy.example.com:8080` <br> `pdf2zh_next --proxy http://user:pass@proxy.example.com:8080` |
| `--verbose`, `-V`               | Включить подробный вывод                                                                | `pdf2zh_next -V` <br> `pdf2zh_next --verbose`                                                                         |
`config.toml`                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `--config-file`                 | Path to the configuration file                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `config.toml`                                                                 |
| `--config-file`                 | Path to the configuration file                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `config.toml`                                                                 |

---

### OUTPUT

| `--config-file`                 | Путь к файлу конфигурации                                                               | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `config.toml`                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `--config-file`                 | Путь к файлу конфигурации                                                               | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `config.toml`                                                                 |
| `--config-file`                 | Путь к файлу конфигурации                                                               | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `config.toml`                                                                 |
`5`                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `--report-interval:milliseconds` | Progress report interval in milliseconds                                                | `pdf2zh_next example.pdf --report-interval:milliseconds 5000`                                                         | `5000`                                                                       |
| `--report-interval:seconds`      | Progress report interval in seconds                                                     | `pdf2zh_next example.pdf --report-interval:seconds 5`                                                                | `5`                                                                          |
| `--report-interval:minutes`      | Progress report interval in minutes                                                     | `pdf2zh_next example.pdf --report-interval:minutes 1`                                                                 | `1`                                                                          |
| `--report-interval:hours`        | Progress report interval in hours                                                       | `pdf2zh_next example.pdf --report-interval:hours 1`                                                                   | `1`                                                                          |

---

### OUTPUT

| `--report-interval`             | Интервал отчёта о прогрессе в секундах                                                  | `pdf2zh_next example.pdf --report-interval 5`                                                                         | `5`                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `--report-interval:milliseconds` | Интервал отчёта о прогрессе в миллисекундах                                             | `pdf2zh_next example.pdf --report-interval:milliseconds 5000`                                                         | `5000`                                                                       |
| `--report-interval:seconds`      | Интервал отчёта о прогрессе в секундах                                                  | `pdf2zh_next example.pdf --report-interval:seconds 5`                                                                | `5`                                                                          |
| `--report-interval:minutes`      | Интервал отчёта о прогрессе в минутах                                                   | `pdf2zh_next example.pdf --report-interval:minutes 1`                                                                 | `1`                                                                          |
| `--report-interval:hours`        | Интервал отчёта о прогрессе в часах                                                     | `pdf2zh_next example.pdf --report-interval:hours 1`                                                                   | `1`                                                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-level`                   | Set logging level, default is `info`                                                    | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | Save logs to file                                                                       | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--log-format`                  | Set log format, default is `%(asctime)s - %(name)s - %(levelname)s - %(message)s`       | `pdf2zh_next example.pdf --log-format "%(asctime)s - %(name)s - %(levelname)s - %(message)s"`                         |
| `--log-rotate`                  | Enable log rotation, default is `False`                                                 | `pdf2zh_next example.pdf --log-rotate`                                                                                |
| `--log-rotate-max-bytes`        | Max bytes per log file, default is `10485760` (10MB)                                    | `pdf2zh_next example.pdf --log-rotate-max-bytes 20971520`                                                             |
| `--log-rotate-backup-count`     | Number of backup logs to keep, default is `5`                                           | `pdf2zh_next example.pdf --log-rotate-backup-count 10`                                                                |
| `--log-rotate-when`             | When to rotate logs, default is `midnight`                                              | `pdf2zh_next example.pdf --log-rotate-when midnight`                                                                  |
| `--log-rotate-interval`         | Interval for log rotation, default is `1`                                               | `pdf2zh_next example.pdf --log-rotate-interval 1`                                                                     |
| `--log-rotate-utc`              | Use UTC time for log rotation, default is `False`                                       | `pdf2zh_next example.pdf --log-rotate-utc`                                                                            |
| `--log-rotate-at-time`          | Time to rotate logs, default is `None`                                                  | `pdf2zh_next example.pdf --log-rotate-at-time "00:00"`                                                                |
| `--log-rotate-encoding`         | Encoding for log files, default is `utf-8`                                              | `pdf2zh_next example.pdf --log-rotate-encoding utf-8`                                                                 |
| `--log-rotate-delay`            | Delay log rotation until next check, default is `False`                                 | `pdf2zh_next example.pdf --log-rotate-delay`                                                                          |
| `--log-rotate-compression`      | Compression method for rotated logs, default is `None`                                   | `pdf2zh_next example.pdf --log-rotate-compression zip`                                                                |
| `--log-rotate-compression-level` | Compression level, default is `None`                                                    | `pdf2zh_next example.pdf --log-rotate-compression-level 9`                                                            |

---

### OUTPUT LANGUAGE

ru

---

| `--debug`                       | Использовать уровень логирования отладки                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-level`                   | Установить уровень логирования, по умолчанию `info`                                                      | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--log-file`                    | Сохранять логи в файл                                                                                    | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--log-format`                  | Установить формат лога, по умолчанию `%(asctime)s - %(name)s - %(levelname)s - %(message)s`              | `pdf2zh_next example.pdf --log-format "%(asctime)s - %(name)s - %(levelname)s - %(message)s"`                         |
| `--log-rotate`                  | Включить ротацию логов, по умолчанию `False`                                                             | `pdf2zh_next example.pdf --log-rotate`                                                                                |
| `--log-rotate-max-bytes`        | Максимальный размер файла лога в байтах, по умолчанию `10485760` (10 МБ)                                 | `pdf2zh_next example.pdf --log-rotate-max-bytes 20971520`                                                             |
| `--log-rotate-backup-count`     | Количество резервных копий логов для хранения, по умолчанию `5`                                          | `pdf2zh_next example.pdf --log-rotate-backup-count 10`                                                                |
| `--log-rotate-when`             | Когда выполнять ротацию логов, по умолчанию `midnight`                                                   | `pdf2zh_next example.pdf --log-rotate-when midnight`                                                                  |
| `--log-rotate-interval`         | Интервал ротации логов, по умолчанию `1`                                                                 | `pdf2zh_next example.pdf --log-rotate-interval 1`                                                                     |
| `--log-rotate-utc`              | Использовать UTC время для ротации логов, по умолчанию `False`                                           | `pdf2zh_next example.pdf --log-rotate-utc`                                                                            |
| `--log-rotate-at-time`          | Время для ротации логов, по умолчанию `None`                                                             | `pdf2zh_next example.pdf --log-rotate-at-time "00:00"`                                                                |
| `--log-rotate-encoding`         | Кодировка файлов логов, по умолчанию `utf-8`                                                             | `pdf2zh_next example.pdf --log-rotate-encoding utf-8`                                                                 |
| `--log-rotate-delay`            | Отложить ротацию логов до следующей проверки, по умолчанию `False`                                       | `pdf2zh_next example.pdf --log-rotate-delay`                                                                          |
| `--log-rotate-compression`      | Метод сжатия для ротированных логов, по умолчанию `None`                                                 | `pdf2zh_next example.pdf --log-rotate-compression zip`                                                                |
| `--log-rotate-compression-level` | Уровень сжатия, по умолчанию `None`                                                                      | `pdf2zh_next example.pdf --log-rotate-compression-level 9`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--input <path>`                | Input file path                                                                         | `pdf2zh_next --input example.pdf`                                                                                     |
| `--output <path>`               | Output file path                                                                        | `pdf2zh_next --input example.pdf --output example_zh.pdf`                                                             |
| `--lang <lang>`                 | Target language, default is `zh-cn` (Chinese)                                           | `pdf2zh_next --input example.pdf --lang en`                                                                          |
| `--mode <mode>`                 | Translation mode, default is `fast`. Options: `fast`, `standard`, `quality`, `custom`   | `pdf2zh_next --input example.pdf --mode quality`                                                                      |
| `--ocr <ocr>`                   | OCR engine, default is `easyocr`. Options: `easyocr`, `paddleocr`                       | `pdf2zh_next --input example.pdf --ocr paddleocr`                                                                     |
| `--translator <translator>`     | Translator, default is `google`. Options: `google`, `google_free`, `azure`, `openai`   | `pdf2zh_next --input example.pdf --translator azure`                                                                  |
| `--retry <number>`              | Retry times, default is `3`                                                             | `pdf2zh_next --input example.pdf --retry 5`                                                                           |
| `--timeout <seconds>`           | Timeout for each translation request, default is `10`                                   | `pdf2zh_next --input example.pdf --timeout 20`                                                                        |
| `--concurrency <number>`        | Concurrency number, default is `5`                                                      | `pdf2zh_next --input example.pdf --concurrency 10`                                                                    |
| `--proxy <proxy>`               | Proxy for translation, e.g., `http://127.0.0.1:7890`                                   | `pdf2zh_next --input example.pdf --proxy http://127.0.0.1:7890`                                                       |
| `--api-key <key>`               | API key for translation service, e.g., OpenAI API key                                   | `pdf2zh_next --input example.pdf --translator openai --api-key sk-xxx`                                                |
| `--api-base <url>`              | API base URL for translation service, e.g., OpenAI API base URL                         | `pdf2zh_next --input example.pdf --translator openai --api-base https://api.openai.com/v1`                            |
| `--model <model>`               | Model for translation service, e.g., OpenAI model                                       | `pdf2zh_next --input example.pdf --translator openai --model gpt-4`                                                   |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next --input example.pdf --no-cache`                                                                          |
| `--cache-dir <path>`            | Cache directory, default is `./cache`                                                   | `pdf2zh_next --input example.pdf --cache-dir /tmp/cache`                                                              |
| `--config <path>`               | Config file path                                                                        | `pdf2zh_next --input example.pdf --config config.json`                                                                |
| `--help`                        | Show help                                                                               | `pdf2zh_next --help`                                                                                                  |

---

### LANGUAGE

ru

---

### OUTPUT

| `--gui`                         | Взаимодействие с графическим интерфейсом                                                                       | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--input <path>`                | Путь к входному файлу                                                                                          | `pdf2zh_next --input example.pdf`                                                                                     |
| `--output <path>`               | Путь к выходному файлу                                                                                         | `pdf2zh_next --input example.pdf --output example_zh.pdf`                                                             |
| `--lang <lang>`                 | Целевой язык, по умолчанию `zh-cn` (китайский)                                                                 | `pdf2zh_next --input example.pdf --lang en`                                                                          |
| `--mode <mode>`                 | Режим перевода, по умолчанию `fast`. Варианты: `fast`, `standard`, `quality`, `custom`                         | `pdf2zh_next --input example.pdf --mode quality`                                                                      |
| `--ocr <ocr>`                   | Движок OCR, по умолчанию `easyocr`. Варианты: `easyocr`, `paddleocr`                                           | `pdf2zh_next --input example.pdf --ocr paddleocr`                                                                     |
| `--translator <translator>`     | Переводчик, по умолчанию `google`. Варианты: `google`, `google_free`, `azure`, `openai`                        | `pdf2zh_next --input example.pdf --translator azure`                                                                  |
| `--retry <number>`              | Количество повторных попыток, по умолчанию `3`                                                                 | `pdf2zh_next --input example.pdf --retry 5`                                                                           |
| `--timeout <seconds>`           | Таймаут для каждого запроса перевода, по умолчанию `10`                                                        | `pdf2zh_next --input example.pdf --timeout 20`                                                                        |
| `--concurrency <number>`        | Количество одновременных запросов, по умолчанию `5`                                                            | `pdf2zh_next --input example.pdf --concurrency 10`                                                                    |
| `--proxy <proxy>`               | Прокси для перевода, например, `http://127.0.0.1:7890`                                                         | `pdf2zh_next --input example.pdf --proxy http://127.0.0.1:7890`                                                       |
| `--api-key <key>`               | API-ключ для службы перевода, например, ключ API OpenAI                                                        | `pdf2zh_next --input example.pdf --translator openai --api-key sk-xxx`                                                |
| `--api-base <url>`              | Базовый URL API для службы перевода, например, базовый URL API OpenAI                                           | `pdf2zh_next --input example.pdf --translator openai --api-base https://api.openai.com/v1`                            |
| `--model <model>`               | Модель для службы перевода, например, модель OpenAI                                                            | `pdf2zh_next --input example.pdf --translator openai --model gpt-4`                                                   |
| `--no-cache`                    | Отключить кэширование                                                                                          | `pdf2zh_next --input example.pdf --no-cache`                                                                          |
| `--cache-dir <path>`            | Директория кэша, по умолчанию `./cache`                                                                        | `pdf2zh_next --input example.pdf --cache-dir /tmp/cache`                                                              |
| `--config <path>`               | Путь к файлу конфигурации                                                                                      | `pdf2zh_next --input example.pdf --config config.json`                                                                |
| `--help`                        | Показать справку                                                                                               | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--clean`                       | Clean all temporary files then exit                                                     | `pdf2zh_next --clean`                                                                                                 |
| `--clean-cache`                 | Clean the cache directory (default: `~/.cache/pdf2zh`) then exit                        | `pdf2zh_next --clean-cache`                                                                                           |
| `--clean-translated-pdf`        | Clean the translated PDF directory (default: `~/.cache/pdf2zh/translated_pdf`) then exit | `pdf2zh_next --clean-translated-pdf`                                                                                  |
| `--clean-temp`                  | Clean the temporary directory (default: `~/.cache/pdf2zh/temp`) then exit               | `pdf2zh_next --clean-temp`                                                                                            |
| `--clean-all`                   | Clean all then exit                                                                     | `pdf2zh_next --clean-all`                                                                                             |
| `--version`                     | Show the version of pdf2zh                                                              | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show the help message                                                                   | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--warmup`                      | Только загрузить и проверить необходимые ресурсы, затем выйти                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--clean`                       | Очистить все временные файлы, затем выйти                                                     | `pdf2zh_next --clean`                                                                                                 |
| `--clean-cache`                 | Очистить кэш-директорию (по умолчанию: `~/.cache/pdf2zh`), затем выйти                        | `pdf2zh_next --clean-cache`                                                                                           |
| `--clean-translated-pdf`        | Очистить директорию переведенных PDF (по умолчанию: `~/.cache/pdf2zh/translated_pdf`), затем выйти | `pdf2zh_next --clean-translated-pdf`                                                                                  |
| `--clean-temp`                  | Очистить временную директорию (по умолчанию: `~/.cache/pdf2zh/temp`), затем выйти               | `pdf2zh_next --clean-temp`                                                                                            |
| `--clean-all`                   | Очистить все, затем выйти                                                                     | `pdf2zh_next --clean-all`                                                                                             |
| `--version`                     | Показать версию pdf2zh                                                              | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Показать справочное сообщение                                                                   | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`                  | Output directory of the translated PDF files                                           | `pdf2zh_next example.pdf --output-dir /path/to/output`                                                                 |
| `--offline-mode`                | Enable offline mode, which requires the offline assets package to be pre-downloaded     | `pdf2zh_next example.pdf --offline-mode --offline-assets-dir /path/to/assets`                                          |
| `--offline-assets-dir`          | Directory of the offline assets package                                                | `pdf2zh_next example.pdf --offline-mode --offline-assets-dir /path/to/assets`                                          |

---

### TRANSLATED TEXT

| `--generate-offline-assets`     | Создать пакет офлайн-ресурсов в указанной директории                                   | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`                  | Выходная директория для переведённых PDF-файлов                                        | `pdf2zh_next example.pdf --output-dir /path/to/output`                                                                 |
| `--offline-mode`                | Включить офлайн-режим, для которого требуется предварительная загрузка пакета офлайн-ресурсов | `pdf2zh_next example.pdf --offline-mode --offline-assets-dir /path/to/assets`                                          |
| `--offline-assets-dir`          | Директория пакета офлайн-ресурсов                                                       | `pdf2zh_next example.pdf --offline-mode --offline-assets-dir /path/to/assets`                                          |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-offline-assets`      | Disable the offline assets package, use online API instead                              | `pdf2zh_next example.pdf --disable-offline-assets`                                                                    |
| `--no-progress-bar`             | Disable the progress bar                                                                | `pdf2zh_next example.pdf --no-progress-bar`                                                                           |
| `--no-color`                    | Disable color output                                                                    | `pdf2zh_next example.pdf --no-color`                                                                                  |
| `--version`                     | Show the version of pdf2zh                                                              | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show the help message                                                                   | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION

| `--restore-offline-assets`      | Восстановить пакет офлайн-ресурсов из указанной директории                               | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--disable-offline-assets`      | Отключить пакет офлайн-ресурсов, использовать онлайн-API вместо него                    | `pdf2zh_next example.pdf --disable-offline-assets`                                                                    |
| `--no-progress-bar`             | Отключить индикатор выполнения                                                          | `pdf2zh_next example.pdf --no-progress-bar`                                                                           |
| `--no-color`                    | Отключить цветной вывод                                                                 | `pdf2zh_next example.pdf --no-color`                                                                                  |
| `--version`                     | Показать версию pdf2zh                                                                  | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Показать справочное сообщение                                                           | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--input <input>`               | Path of input file or directory                                                         | `pdf2zh_next --input input.pdf`                                                                                       |
| `--output <output>`             | Path of output file or directory                                                        | `pdf2zh_next --output output.pdf`                                                                                     |
| `--translator <translator>`     | Name of translator to use                                                               | `pdf2zh_next --translator google`                                                                                     |
| `--source-lang <source_lang>`   | Source language code                                                                    | `pdf2zh_next --source-lang en`                                                                                        |
| `--target-lang <target_lang>`   | Target language code                                                                    | `pdf2zh_next --target-lang zh`                                                                                        |
| `--pages <pages>`               | Pages to translate (e.g. 1-5,8,11-13)                                                   | `pdf2zh_next --pages 1-5,8,11-13`                                                                                     |
| `--ocr <ocr>`                   | OCR engine to use (auto, paddle, tesseract)                                             | `pdf2zh_next --ocr paddle`                                                                                            |
| `--ocr-lang <ocr_lang>`         | Language for OCR engine                                                                 | `pdf2zh_next --ocr-lang en`                                                                                           |
| `--force-ocr`                   | Force OCR even if text can be extracted directly                                        | `pdf2zh_next --force-ocr`                                                                                             |
| `--single-thread`               | Run in single thread mode                                                               | `pdf2zh_next --single-thread`                                                                                         |
| `--config <config>`             | Path to config file                                                                     | `pdf2zh_next --config config.toml`                                                                                    |
| `--api-key <api_key>`           | API key for translator                                                                  | `pdf2zh_next --api-key YOUR_API_KEY`                                                                                  |
| `--model <model>`               | Model name for translator                                                               | `pdf2zh_next --model gpt-3.5-turbo`                                                                                   |
| `--concurrency-limit <limit>`   | Max number of concurrent requests                                                       | `pdf2zh_next --concurrency-limit 5`                                                                                   |
| `--request-interval <interval>` | Interval between requests in seconds                                                    | `pdf2zh_next --request-interval 1`                                                                                    |
| `--help`                        | Print help                                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--version`                     | Показать версию и выйти                                                                 | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--input <input>`               | Путь к входному файлу или директории                                                    | `pdf2zh_next --input input.pdf`                                                                                       |
| `--output <output>`             | Путь к выходному файлу или директории                                                   | `pdf2zh_next --output output.pdf`                                                                                     |
| `--translator <translator>`     | Название используемого переводчика                                                      | `pdf2zh_next --translator google`                                                                                     |
| `--source-lang <source_lang>`   | Код языка оригинала                                                                     | `pdf2zh_next --source-lang en`                                                                                        |
| `--target-lang <target_lang>`   | Код целевого языка                                                                      | `pdf2zh_next --target-lang zh`                                                                                        |
| `--pages <pages>`               | Страницы для перевода (например, 1-5,8,11-13)                                           | `pdf2zh_next --pages 1-5,8,11-13`                                                                                     |
| `--ocr <ocr>`                   | Движок OCR для использования (auto, paddle, tesseract)                                  | `pdf2zh_next --ocr paddle`                                                                                            |
| `--ocr-lang <ocr_lang>`         | Язык для движка OCR                                                                     | `pdf2zh_next --ocr-lang en`                                                                                           |
| `--force-ocr`                   | Принудительно использовать OCR, даже если текст можно извлечь напрямую                  | `pdf2zh_next --force-ocr`                                                                                             |
| `--single-thread`               | Запуск в однопоточном режиме                                                            | `pdf2zh_next --single-thread`                                                                                         |
| `--config <config>`             | Путь к файлу конфигурации                                                               | `pdf2zh_next --config config.toml`                                                                                    |
| `--api-key <api_key>`           | API-ключ для переводчика                                                                | `pdf2zh_next --api-key YOUR_API_KEY`                                                                                  |
| `--model <model>`               | Название модели для переводчика                                                         | `pdf2zh_next --model gpt-3.5-turbo`                                                                                   |
| `--concurrency-limit <limit>`   | Максимальное количество одновременных запросов                                          | `pdf2zh_next --concurrency-limit 5`                                                                                   |
| `--request-interval <interval>` | Интервал между запросами в секундах                                                     | `pdf2zh_next --request-interval 1`                                                                                    |
| `--help`                        | Вывести справку                                                                         | `pdf2zh_next --help`                                                                                                  |
[Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#pages)  |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `--ocr-version`                 | Specify the OCR engine                                                                  | `pdf2zh_next example.pdf --ocr-version rapid`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#ocr-version) |
| `--ocr-engine-args`             | Pass additional arguments to the OCR engine                                             | `pdf2zh_next example.pdf --ocr-engine-args '{"tessedit_pageseg_mode": "6"}'`                                           | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#ocr-engine-args) |
| `--output-format`               | Specify the output format                                                               | `pdf2zh_next example.pdf --output-format pdf`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output-format) |
| `--output-filename`             | Specify the output filename                                                             | `pdf2zh_next example.pdf --output-filename example_zh.pdf`                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output-filename) |
| `--output-directory`            | Specify the output directory                                                            | `pdf2zh_next example.pdf --output-directory ./output`                                                                  | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output-directory) |
| `--target-language`             | Specify the target language                                                             | `pdf2zh_next example.pdf --target-language ru`                                                                         | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#target-language) |
| `--translate-service`           | Specify the translation service                                                         | `pdf2zh_next example.pdf --translate-service google`                                                                   | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#translate-service) |
| `--translate-service-args`      | Pass additional arguments to the translation service                                    | `pdf2zh_next example.pdf --translate-service-args '{"api_key": "your-api-key"}'`                                       | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#translate-service-args) |
| `--translation-cache`           | Enable or disable translation cache                                                     | `pdf2zh_next example.pdf --translation-cache false`                                                                    | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#translation-cache) |
| `--cache-dir`                   | Specify the cache directory                                                             | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#cache-dir) |
| `--concurrency-limit`           | Specify the concurrency limit for translation                                          | `pdf2zh_next example.pdf --concurrency-limit 5`                                                                        | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#concurrency-limit) |
| `--log-level`                   | Specify the log level                                                                   | `pdf2zh_next example.pdf --log-level debug`                                                                            | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#log-level) |
| `--log-file`                    | Specify the log file                                                                    | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                         | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#log-file) |
| `--config-file`                 | Specify the config file                                                                 | `pdf2zh_next example.pdf --config-file ./config.yaml`                                                                  | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#config-file) |
| `--help`                        | Show help                                                                               | `pdf2zh_next --help`                                                                                                   | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#help)    |
| `--version`                     | Show version                                                                            | `pdf2zh_next --version`                                                                                                | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#version) |

---

### OUTPUT

| `--pages`                       | Частичный перевод документа                                                             | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#pages)  |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `--ocr-version`                 | Указание OCR-движка                                                                     | `pdf2zh_next example.pdf --ocr-version rapid`                                                                          | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#ocr-version) |
| `--ocr-engine-args`             | Передача дополнительных аргументов в OCR-движок                                        | `pdf2zh_next example.pdf --ocr-engine-args '{"tessedit_pageseg_mode": "6"}'`                                           | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#ocr-engine-args) |
| `--output-format`               | Указание формата вывода                                                                 | `pdf2zh_next example.pdf --output-format pdf`                                                                          | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output-format) |
| `--output-filename`             | Указание имени выходного файла                                                          | `pdf2zh_next example.pdf --output-filename example_zh.pdf`                                                             | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output-filename) |
| `--output-directory`            | Указание выходной директории                                                            | `pdf2zh_next example.pdf --output-directory ./output`                                                                  | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#output-directory) |
| `--target-language`             | Указание целевого языка                                                                 | `pdf2zh_next example.pdf --target-language ru`                                                                         | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#target-language) |
| `--translate-service`           | Указание службы перевода                                                                | `pdf2zh_next example.pdf --translate-service google`                                                                   | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#translate-service) |
| `--translate-service-args`      | Передача дополнительных аргументов в службу перевода                                    | `pdf2zh_next example.pdf --translate-service-args '{"api_key": "your-api-key"}'`                                       | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#translate-service-args) |
| `--translation-cache`           | Включение или отключение кэша переводов                                                 | `pdf2zh_next example.pdf --translation-cache false`                                                                    | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#translation-cache) |
| `--cache-dir`                   | Указание директории кэша                                                                | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#cache-dir) |
| `--concurrency-limit`           | Указание ограничения параллелизма для переводов                                         | `pdf2zh_next example.pdf --concurrency-limit 5`                                                                        | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#concurrency-limit) |
| `--log-level`                   | Указание уровня логирования                                                             | `pdf2zh_next example.pdf --log-level debug`                                                                            | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#log-level) |
| `--log-file`                    | Указание файла лога                                                                     | `pdf2zh_next example.pdf --log-file ./log.txt`                                                                         | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#log-file) |
| `--config-file`                 | Указание конфигурационного файла                                                        | `pdf2zh_next example.pdf --config-file ./config.yaml`                                                                  | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#config-file) |
| `--help`                        | Показать справку                                                                        | `pdf2zh_next --help`                                                                                                   | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#help)    |
| `--version`                     | Показать версию                                                                         | `pdf2zh_next --version`                                                                                                | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_cli.html#version) |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out zh`                                                                               |
| `-o`, `--output`                | Output file name                                                                        | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                   |
| `-d`, `--debug`                 | Enable debug mode, which will output more detailed information during the process       | `pdf2zh_next example.pdf -d`                                                                                          |
| `-y`, `--yes`                   | Skip confirmation prompts and automatically confirm all                                 | `pdf2zh_next example.pdf -y`                                                                                          |
| `-f`, `--force`                 | Force overwrite existing output files                                                   | `pdf2zh_next example.pdf -f`                                                                                          |
| `--ocr`                         | Enable OCR mode, which will perform OCR on the PDF before translation                   | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-option`                  | Additional options for OCR, passed to the OCR engine.                                   | `pdf2zh_next example.pdf --ocr-option '{"languages": ["en", "zh"]}'`                                                  |
| `--translator`                  | Specify the translation service to use                                                  | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-option`           | Additional options for the translation service, passed to the translation engine.       | `pdf2zh_next example.pdf --translator-option '{"api_key": "your_api_key"}'`                                           |
| `--concurrency-limit`           | Maximum number of concurrent translation requests                                       | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `--request-interval`            | Time interval (in seconds) between translation requests                                 | `pdf2zh_next example.pdf --request-interval 1`                                                                        |
| `--batch-size`                  | Number of texts to be sent for translation in each request                              | `pdf2zh_next example.pdf --batch-size 5`                                                                              |
| `--cache`                       | Enable caching of translation results to avoid repeated translations of the same text   | `pdf2zh_next example.pdf --cache`                                                                                     |
| `--cache-db`                    | Specify the cache database file path                                                    | `pdf2zh_next example.pdf --cache-db ./cache.db`                                                                       |
| `--no-cache`                    | Disable caching                                                                         | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--dry-run`                     | Perform a dry run without actually translating the PDF                                  | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Show help message                                                                       | `pdf2zh_next -h`                                                                                                      |

---

### TRANSLATION RESULT

| `--lang-in`                     | Код языка исходного текста                                                              | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Код языка перевода                                                                      | `pdf2zh_next example.pdf --lang-out zh`                                                                               |
| `-o`, `--output`                | Имя выходного файла                                                                     | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                   |
| `-d`, `--debug`                 | Включить режим отладки, который выводит более подробную информацию в процессе           | `pdf2zh_next example.pdf -d`                                                                                          |
| `-y`, `--yes`                   | Пропустить запросы подтверждения и автоматически подтверждать все                       | `pdf2zh_next example.pdf -y`                                                                                          |
| `-f`, `--force`                 | Принудительно перезаписывать существующие выходные файлы                                | `pdf2zh_next example.pdf -f`                                                                                          |
| `--ocr`                         | Включить режим OCR, который выполнит OCR на PDF перед переводом                         | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-option`                  | Дополнительные опции для OCR, передаваемые в движок OCR.                                | `pdf2zh_next example.pdf --ocr-option '{"languages": ["en", "zh"]}'`                                                  |
| `--translator`                  | Указать службу перевода для использования                                               | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-option`           | Дополнительные опции для службы перевода, передаваемые в движок перевода.               | `pdf2zh_next example.pdf --translator-option '{"api_key": "your_api_key"}'`                                           |
| `--concurrency-limit`           | Максимальное количество одновременных запросов на перевод                               | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `--request-interval`            | Временной интервал (в секундах) между запросами на перевод                              | `pdf2zh_next example.pdf --request-interval 1`                                                                        |
| `--batch-size`                  | Количество текстов, отправляемых на перевод в каждом запросе                            | `pdf2zh_next example.pdf --batch-size 5`                                                                              |
| `--cache`                       | Включить кэширование результатов перевода, чтобы избежать повторного перевода одного текста | `pdf2zh_next example.pdf --cache`                                                                                     |
| `--cache-db`                    | Указать путь к файлу базы данных кэша                                                   | `pdf2zh_next example.pdf --cache-db ./cache.db`                                                                       |
| `--no-cache`                    | Отключить кэширование                                                                   | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--dry-run`                     | Выполнить пробный запуск без фактического перевода PDF                                  | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | Показать информацию о версии                                                            | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Показать справочное сообщение                                                           | `pdf2zh_next -h`                                                                                                      |
[Language Code](https://pdf2zh-next.com/getting-started/LANGUAGE_CODE.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--lang-in`                     | Source language code                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                | [Language Code](https://pdf2zh-next.com/getting-started/LANGUAGE_CODE.html) |
| `--translator`                  | Translation service                                                                     | `pdf2zh_next example.pdf --translator google`                                                                         | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-key`              | API Key for the translation service                                                     | `pdf2zh_next example.pdf --translator deepl --translator-key YOUR_DEEPL_KEY`                                          | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-url`              | Custom endpoint for the translation service                                             | `pdf2zh_next example.pdf --translator azure --translator-url "https://api.cognitive.microsofttranslator.com/"`        | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-region`           | Region for the translation service                                                      | `pdf2zh_next example.pdf --translator azure --translator-region "global"`                                             | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-model`            | Model for the translation service                                                       | `pdf2zh_next example.pdf --translator openai --translator-model "gpt-4o"`                                             | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-version`          | Version for the translation service                                                     | `pdf2zh_next example.pdf --translator azure --translator-version "3.0"`                                               | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-extra-params`     | Extra parameters for the translation service (JSON format)                              | `pdf2zh_next example.pdf --translator google --translator-extra-params '{"glossary": "projects/..."}'`                | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-extra-headers`    | Extra headers for the translation service (JSON format)                                 | `pdf2zh_next example.pdf --translator azure --translator-extra-headers '{"Ocp-Apim-Subscription-Key": "YOUR_KEY"}'`   | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-path`             | Path for the translation service                                                        | `pdf2zh_next example.pdf --translator azure --translator-path "/translate"`                                           | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-retry`            | Number of retries for the translation service                                           | `pdf2zh_next example.pdf --translator google --translator-retry 5`                                                    | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-timeout`          | Timeout for the translation service (seconds)                                           | `pdf2zh_next example.pdf --translator google --translator-timeout 30`                                                 | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-concurrency-limit`| Concurrency limit for the translation service                                           | `pdf2zh_next example.pdf --translator google --translator-concurrency-limit 10`                                       | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-interval` | Request interval for the translation service (milliseconds)                             | `pdf2zh_next example.pdf --translator google --translator-request-interval 1000`                                      | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-timeout`  | Request timeout for the translation service (milliseconds)                              | `pdf2zh_next example.pdf --translator google --translator-request-timeout 5000`                                       | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry`    | Request retry for the translation service                                               | `pdf2zh_next example.pdf --translator google --translator-request-retry 3`                                            | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-interval` | Request retry interval for the translation service (milliseconds)                   | `pdf2zh_next example.pdf --translator google --translator-request-retry-interval 1000`                                | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-timeout`  | Request retry timeout for the translation service (milliseconds)                    | `pdf2zh_next example.pdf --translator google --translator-request-retry-timeout 5000`                                 | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-max`| Request retry max for the translation service                                           | `pdf2zh_next example.pdf --translator google --translator-request-retry-max 5`                                        | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-backoff-factor` | Request retry backoff factor for the translation service                        | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-factor 2`                             | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-backoff-max` | Request retry backoff max for the translation service (milliseconds)                | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-max 10000`                            | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-backoff-jitter` | Request retry backoff jitter for the translation service                       | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-jitter 0.1`                           | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |
| `--translator-request-retry-backoff-jitter-max` | Request retry backoff jitter max for the translation service (milliseconds)     | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-jitter-max 1000`                      | [Translator](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)      |

---

### TRANSLATION RESULT

| `--lang-out`                    | Код языка назначения                                                                     | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            | [Код языка](https://pdf2zh-next.com/getting-started/LANGUAGE_CODE.html)     |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--lang-in`                     | Код исходного языка                                                                      | `pdf2zh_next example.pdf --lang-in en`                                                                                | [Код языка](https://pdf2zh-next.com/getting-started/LANGUAGE_CODE.html)     |
| `--translator`                  | Сервис перевода                                                                          | `pdf2zh_next example.pdf --translator google`                                                                         | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-key`              | API-ключ для сервиса перевода                                                            | `pdf2zh_next example.pdf --translator deepl --translator-key YOUR_DEEPL_KEY`                                          | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-url`              | Пользовательская конечная точка для сервиса перевода                                     | `pdf2zh_next example.pdf --translator azure --translator-url "https://api.cognitive.microsofttranslator.com/"`        | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-region`           | Регион для сервиса перевода                                                              | `pdf2zh_next example.pdf --translator azure --translator-region "global"`                                             | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-model`            | Модель для сервиса перевода                                                              | `pdf2zh_next example.pdf --translator openai --translator-model "gpt-4o"`                                             | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-version`          | Версия для сервиса перевода                                                              | `pdf2zh_next example.pdf --translator azure --translator-version "3.0"`                                               | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-extra-params`     | Дополнительные параметры для сервиса перевода (формат JSON)                              | `pdf2zh_next example.pdf --translator google --translator-extra-params '{"glossary": "projects/..."}'`                | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-extra-headers`    | Дополнительные заголовки для сервиса перевода (формат JSON)                              | `pdf2zh_next example.pdf --translator azure --translator-extra-headers '{"Ocp-Apim-Subscription-Key": "YOUR_KEY"}'`   | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-path`             | Путь для сервиса перевода                                                                | `pdf 极 2zh_next example.pdf --translator azure --translator-path "/translate"`                                         | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-retry`            | Количество повторных попыток для сервиса перевода                                        | `pdf2zh_next example.pdf --transl 极 ator google --translator-retry 5`                                                  | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-timeout`          | Таймаут для сервиса перевода (секунды)                                                   | `pdf2zh_next example.pdf --translator google --translator-timeout 30`                                                 | [Переводчик](https://pdf2zh 极-next.com/getting-started/TRANSLATOR.html)     |
| `--translator-concurrency-limit`| Лимит параллелизма для сервиса перевода                                                  | `pdf2zh_next example.pdf --translator google --translator-concurrency-limit 10`                                       | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-interval` | Интервал запросов для сервиса перевода (миллисекунды)                                    | `pdf2zh_next example.pdf --translator google --translator-request-interval 1000`                                      | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-timeout`  | Таймаут запроса для сервиса перевода (миллисекунды)                                      | `pdf2zh_next example.pdf --translator google --translator-request-timeout 500 极 0`                                     | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry`    | Повторная попытка запроса для сервиса перевода                                           | `pdf2zh_next example.pdf --translator google --translator-request-retry 3`                                            | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry-interval` | Интервал повторных попыток запроса для сервиса перевода (миллисекунды)               | `pdf2zh_next example.pdf --translator google --translator-request-retry-interval 1000`                                | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry-timeout`  | Таймаут повторных попыток запроса для сервиса перевода (миллисекунды)                | `pdf2zh_next example.pdf --translator google --translator-request-retry-timeout 5000`                                 | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry-max`| Максимальное количество повторных попыток запроса для сервиса перевода                   | `pdf2zh_next example.pdf --translator google --translator-request-retry-max 5`                                        | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry-backoff-factor` | Фактор экспоненциального отката повторных попыток запроса для сервиса перевода  | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-factor 2`                             | [Переводчик](https://pdf2zh-next.com/getting-started/极 TRANSLATOR.html)     |
| `--translator-request-retry-backoff-max` | Максимальное значение экспоненциального отката повторных попыток запроса для сервиса перевода (миллисекунды) | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-max 10000`                            | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry-backoff-jitter` | Джиттер экспоненциального отката повторных попыток запроса для сервиса перевода | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-jitter 0.1`                           | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
| `--translator-request-retry-backoff-jitter-max` | Максимальный джиттер экспоненциального отката повторных попыток запроса для сервиса перевода (миллисекунды) | `pdf2zh_next example.pdf --translator google --translator-request-retry-backoff-jitter-max 1000`                      | [Переводчик](https://pdf2zh-next.com/getting-started/TRANSLATOR.html)       |
`5`                                           |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `--min-block-length`            | Minimum block length to translate                                                       | `pdf2zh_next example.pdf --min-block-length 5`                                                                        | `5`                                           |
| `--max-text-length`             | Maximum text length to translate                                                        | `pdf2zh_next example.pdf --max-text-length 10000`                                                                     | `10000`                                       |
| `--max-block-length`            | Maximum block length to translate                                                       | `pdf2zh_next example.pdf --max-block-length 10000`                                                                    | `10000`                                       |
| `--max-text-characters`         | Maximum characters in a text block                                                      | `pdf2zh_next example.pdf --max-text-characters 1000`                                                                  | `1000`                                        |
| `--max-block-characters`        | Maximum characters in a block                                                           | `pdf2zh_next example.pdf --max-block-characters 1000`                                                                 | `1000`                                        |
| `--text-length-ratio`           | Text length ratio between source and target language                                    | `pdf2zh_next example.pdf --text-length-ratio 2.0`                                                                     | `2.0`                                         |
| `--block-length-ratio`          | Block length ratio between source and target language                                   | `pdf2zh_next example.pdf --block-length-ratio 2.0`                                                                    | `2.0`                                         |
| `--text-split-sentences`        | Split text into sentences                                                               | `pdf2zh_next example.pdf --text-split-sentences`                                                                      | `false`                                       |
| `--block-split-sentences`       | Split block into sentences                                                              | `pdf2zh_next example.pdf --block-split-sentences`                                                                     | `false`                                       |

---

### TRANSLATION

| `--min-text-length`             | Минимальная длина текста для перевода                                                   | `pdf2zh_next example.pdf --min-text-length 5`                                                                         | `5`                                           |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| `--min-block-length`            | Минимальная длина блока для перевода                                                    | `pdf2zh_next example.pdf --min-block-length 5`                                                                        | `5`                                           |
| `--max-text-length`             | Максимальная длина текста для перевода                                                  | `pdf2zh_next example.pdf --max-text-length 10000`                                                                     | `10000`                                       |
| `--max-block-length`            | Максимальная длина блока для перевода                                                   | `pdf2zh_next example.pdf --max-block-length 10000`                                                                    | `10000`                                       |
| `--max-text-characters`         | Максимальное количество символов в текстовом блоке                                      | `pdf2zh_next example.pdf --max-text-characters 1000`                                                                  | `1000`                                        |
| `--max-block-characters`        | Максимальное количество символов в блоке                                                | `pdf2zh_next example.pdf --max-block-characters 1000`                                                                 | `1000`                                        |
| `--text-length-ratio`           | Соотношение длины текста между исходным и целевым языком                                | `pdf2zh_next example.pdf --text-length-ratio 2.0`                                                                     | `2.0`                                         |
| `--block-length-ratio`          | Соотношение длины блока между исходным и целевым языком                                 | `pdf2zh_next example.pdf --block-length-ratio 2.0`                                                                    | `2.0`                                         |
| `--text-split-sentences`        | Разделять текст на предложения                                                          | `pdf2zh_next example.pdf --text-split-sentences`                                                                      | `false`                                       |
| `--block-split-sentences`       | Разделять блок на предложения                                                           | `pdf2zh_next example.pdf --block-split-sentences`                                                                     | `false`                                       |
`http://127.0.0.1:8000` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8001`                                                              | `http://127.0.0.1:8001` |
| `--rpc-translate`                | RPC service host address for translation                                                 | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8002`                                                         | `http://127.0.0.1:8002` |
| `--rpc-ocr-translate`            | RPC service host address for OCR and translation                                         | `pdf2zh_next example.pdf --rpc-ocr-translate http://127.0.0.1:8003`                                                     | `http://127.0.0.1:8003` |
| `--rpc-doclayout-ocr-translate` | RPC service host address for document layout analysis, OCR, and translation             | `pdf2zh_next example.pdf --rpc-doclayout-ocr-translate http://127.0.0.1:8004`                                           | `http://127.0.0.1:8004` |

---

### TRANSLATION RESULT

| `--rpc-doclayout`               | Адрес хоста службы RPC для анализа макета документа                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       | `http://127.0.0.1:8000` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--rpc-ocr`                     | Адрес хоста службы RPC для OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8001`                                                              | `http://127.0.0.1:8001` |
| `--rpc-translate`                | Адрес хоста службы RPC для перевода                                                 | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8002`                                                         | `http://127.0.0.1:8002` |
| `--rpc-ocr-translate`            | Адрес хоста службы RPC для OCR и перевода                                         | `pdf2zh_next example.pdf --rpc-ocr-translate http://127.0.0.1:8003`                                                     | `http://127.0.0.1:8003` |
| `--rpc-doclayout-ocr-translate` | Адрес хоста службы RPC для анализа макета документа, OCR и перевода             | `pdf2zh_next example.pdf --rpc-doclayout-ocr-translate http://127.0.0.1:8004`                                           | `http://127.0.0.1:8004` |
`int`   | `None`  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- | ------- |
| `--batch-size`                  | Batch size for translation service                                                      | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `int`   | `None`  |
| `--batch-wait`                  | Wait time (seconds) between batches                                                     | `pdf2zh_next example.pdf --batch-wait 30`                                                                             | `int`   | `None`  |
| `--concurrent`                  | Number of concurrent translation requests                                                | `pdf2zh_next example.pdf --concurrent 5`                                                                              | `int`   | `None`  |
| `--retry`                       | Number of retries for translation requests                                               | `pdf2zh_next example.pdf --retry 3`                                                                                   | `int`   | `None`  |
| `--retry-wait`                  | Wait time (seconds) between retries                                                     | `pdf2zh_next example.pdf --retry-wait 10`                                                                             | `int`   | `None`  |
| `--timeout`                     | Timeout (seconds) for translation requests                                              | `pdf2zh_next example.pdf --timeout 30`                                                                                | `int`   | `None`  |
| `--proxy`                       | Proxy for translation service (e.g., `http://127.0.0.1:7890`)                            | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               | `str`   | `None`  |
| `--save-translated-json`        | Save the translated JSON file                                                           | `pdf2zh_next example.pdf --save-translated-json`                                                                      | `bool`  | `False` |
| `--save-raw-json`               | Save the raw JSON file                                                                  | `pdf2zh_next example.pdf --save-raw-json`                                                                             | `bool`  | `False` |

---

### TRANSLATED TEXT

| `--qps`                         | Ограничение QPS для службы перевода                                                     | `pdf2zh_next example.pdf --qps 200`                                                                                   | `int`   | `None`  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- | ------- |
| `--batch-size`                  | Размер пакета для службы перевода                                                       | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `int`   | `None`  |
| `--batch-wait`                  | Время ожидания (в секундах) между пакетами                                              | `pdf2zh_next example.pdf --batch-wait 30`                                                                             | `int`   | `None`  |
| `--concurrent`                  | Количество одновременных запросов на перевод                                            | `pdf2zh_next example.pdf --concurrent 5`                                                                              | `int`   | `None`  |
| `--retry`                       | Количество повторных попыток для запросов на перевод                                    | `pdf2zh_next example.pdf --retry 3`                                                                                   | `int`   | `None`  |
| `--retry-wait`                  | Время ожидания (в секундах) между повторными попытками                                  | `pdf2zh_next example.pdf --retry-wait 10`                                                                             | `int`   | `None`  |
| `--timeout`                     | Таймаут (в секундах) для запросов на перевод                                            | `pdf2zh_next example.pdf --timeout 30`                                                                                | `int`   | `None`  |
| `--proxy`                       | Прокси для службы перевода (например, `http://127.0.0.1:7890`)                          | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               | `str`   | `None`  |
| `--save-translated-json`        | Сохранить переведенный JSON-файл                                                        | `pdf2zh_next example.pdf --save-translated-json`                                                                      | `bool`  | `False` |
| `--save-raw-json`               | Сохранить исходный JSON-файл                                                            | `pdf2zh_next example.pdf --save-raw-json`                                                                             | `bool`  | `False` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--cache-dir <cache_dir>`       | Set the directory to store translation cache, default is `./.pdf2zh_cache`              | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `--cache-size <cache_size>`     | Set the maximum number of cache entries, default is 1000, set to 0 to disable cache     | `pdf2zh_next example.pdf --cache-size 2000`                                                                           |
| `--cache-ttl <cache_ttl>`       | Set the time to live for cache entries in seconds, default is 86400 (1 day)             | `pdf2zh_next example.pdf --cache-ttl 3600`                                                                            |
| `--cache-cleanup-interval <sec>` | Set the interval in seconds for automatic cache cleanup, default is 3600 (1 hour)       | `pdf2zh_next example.pdf --cache-cleanup-interval 1800`                                                               |
| `--cache-storage <type>`        | Set the cache storage type, `memory` or `disk`, default is `disk`                       | `pdf2zh_next example.pdf --cache-storage memory`                                                                      |
| `--cache-compress`              | Enable compression for cache entries (only for disk storage)                            | `pdf2zh_next example.pdf --cache-compress`                                                                            |

---

### OUTPUT

| `--ignore-cache`                | Игнорировать кэш перевода                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--cache-dir <cache_dir>`       | Установить директорию для хранения кэша перевода, по умолчанию `./.pdf2zh_cache`         | `pdf2zh_next example.pdf --cache-dir /path/to/cache`                                                                  |
| `--cache-size <cache_size>`     | Установить максимальное количество записей в кэше, по умолчанию 1000, установите 0 для отключения кэша | `pdf2zh_next example.pdf --cache-size 2000`                                                                           |
| `--cache-ttl <cache_ttl>`       | Установить время жизни записей кэша в секундах, по умолчанию 86400 (1 день)              | `pdf2zh_next example.pdf --cache-ttl 3600`                                                                            |
| `--cache-cleanup-interval <sec>` | Установить интервал в секундах для автоматической очистки кэша, по умолчанию 3600 (1 час) | `pdf2zh_next example.pdf --cache-cleanup-interval 1800`                                                               |
| `--cache-storage <type>`        | Установить тип хранения кэша, `memory` или `disk`, по умолчанию `disk`                   | `pdf2zh_next example.pdf --cache-storage memory`                                                                      |
| `--cache-compress`              | Включить сжатие записей кэша (только для хранения на диске)                              | `pdf2zh_next example.pdf --cache-compress`                                                                            |
`""`                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `--custom-user-prompt`          | Custom user prompt for translation. Used for `/no_think` in Qwen 3                      | `pdf2zh_next example.pdf --custom-user-prompt "/no_think Please translate the following text into Chinese"`                | `""`                      |
| `--custom-system-prompt-format` | Custom system prompt for format. Used for `/no_think` in Qwen 3                         | `pdf2zh_next example.pdf --custom-system-prompt-format "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-format`   | Custom user prompt for format. Used for `/no_think` in Qwen 3                           | `pdf2zh_next example.pdf --custom-user-prompt-format "/no_think Please format the following text"`                         | `""`                      |
| `--custom-system-prompt-ocr`    | Custom system prompt for OCR. Used for `/no_think` in Qwen 3                            | `pdf2zh_next example.pdf --custom-system-prompt-ocr "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-ocr`      | Custom user prompt for OCR. Used for `/no_think` in Qwen 3                              | `pdf2zh_next example.pdf --custom-user-prompt-ocr "/no_think Please OCR the following text"`                               | `""`                      |
| `--custom-system-prompt-table`  | Custom system prompt for table. Used for `/no_think` in Qwen 3                          | `pdf2zh_next example.pdf --custom-system-prompt-table "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-table`    | Custom user prompt for table. Used for `/no_think` in Qwen 3                            | `pdf2zh_next example.pdf --custom-user-prompt-table "/no_think Please translate the following table into Chinese"`          | `""`                      |
| `--custom-system-prompt-math`   | Custom system prompt for math. Used for `/no_think` in Qwen 3                           | `pdf2zh_next example.pdf --custom-system-prompt-math "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-math`     | Custom user prompt for math. Used for `/no_think` in Qwen 3                             | `pdf2zh_next example.pdf --custom-user-prompt-math "/no_think Please translate the following math into Chinese"`           | `""`                      |
| `--custom-system-prompt-figure` | Custom system prompt for figure. Used for `/no_think` in Qwen 3                         | `pdf2zh_next example.pdf --custom-system-prompt-figure "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-figure`   | Custom user prompt for figure. Used for `/no_think` in Qwen 3                           | `pdf2zh_next example.pdf --custom-user-prompt-figure "/no_think Please translate the following figure into Chinese"`       | `""`                      |

---

### OUTPUT

| `--custom-system-prompt`        | Пользовательский системный промпт для перевода. Используется для `/no_think` в Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `--custom-user-prompt`          | Пользовательский пользовательский промпт для перевода. Используется для `/no_think` в Qwen 3                      | `pdf2zh_next example.pdf --custom-user-prompt "/no_think Please translate the following text into Chinese"`                | `""`                      |
| `--custom-system-prompt-format` | Пользовательский системный промпт для форматирования. Используется для `/no_think` в Qwen 3                         | `pdf2zh_next example.pdf --custom-system-prompt-format "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-format`   | Пользовательский пользовательский промпт для форматирования. Используется для `/no_think` в Qwen 3                           | `pdf2zh_next example.pdf --custom-user-prompt-format "/no_think Please format the following text"`                         | `""`                      |
| `--custom-system-prompt-ocr`    | Пользовательский системный промпт для OCR. Используется для `/no_think` в Qwen 3                            | `pdf2zh_next example.pdf --custom-system-prompt-ocr "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-ocr`      | Пользовательский пользовательский промпт для OCR. Используется для `/no_think` в Qwen 3                              | `pdf2zh_next example.pdf --custom-user-prompt-ocr "/no_think Please OCR the following text"`                               | `""`                      |
| `--custom-system-prompt-table`  | Пользовательский системный промпт для таблиц. Используется для `/no_think` в Qwen 3                          | `pdf2zh_next example.pdf --custom-system-prompt-table "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-table`    | Пользовательский пользовательский промпт для таблиц. Используется для `/no_think` в Qwen 3                            | `pdf2zh_next example.pdf --custom-user-prompt-table "/no_think Please translate the following table into Chinese"`          | `""`                      |
| `--custom-system-prompt-math`   | Пользовательский системный промпт для математики. Используется для `/no_think` в Qwen 3                           | `pdf2zh_next example.pdf --custom-system-prompt-math "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-math`     | Пользовательский пользовательский промпт для математики. Используется для `/no_think` в Qwen 3                             | `pdf2zh_next example.pdf --custom-user-prompt-math "/no_think Please translate the following math into Chinese"`           | `""`                      |
| `--custom-system-prompt-figure` | Пользовательский системный промпт для рисунков. Используется для `/no_think` в Qwen 3                         | `pdf2zh_next example.pdf --custom-system-prompt-figure "/no_think You are a professional, authentic machine translation engine"` | `""`                      |
| `--custom-user-prompt-figure`   | Пользовательский пользовательский промпт для рисунков. Используется для `/no_think` в Qwen 3                           | `pdf2zh_next example.pdf --custom-user-prompt-figure "/no_think Please translate the following figure into Chinese"`       | `""`                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary_dir`                | Glossary directory.                                                                     | `pdf2zh_next example.pdf --glossary_dir "path/to/glossaries"`                                                          |
| `--glossary_dir_recursive`      | Whether to recursively search for glossary files in the glossary directory. Default is `false`. | `pdf2zh_next example.pdf --glossary_dir "path/to/glossaries" --glossary_dir_recursive true`                           |
| `--glossary_file_extensions`    | Glossary file extensions to search for. Default is `csv,txt,tsv`.                      | `pdf2zh_next example.pdf --glossary_dir "path/to/glossaries" --glossary_file_extensions "csv,txt,tsv,xlsx"`           |

---

### OUTPUT

| `--glossaries`                  | Список файлов глоссария.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary_dir`                | Директория глоссария.                                                                     | `pdf2zh_next example.pdf --glossary_dir "path/to/glossaries"`                                                          |
| `--glossary_dir_recursive`      | Следует ли рекурсивно искать файлы глоссария в директории глоссария. По умолчанию `false`. | `pdf2zh_next example.pdf --glossary_dir "path/to/glossaries" --glossary_dir_recursive true`                           |
| `--glossary_file_extensions`    | Расширения файлов глоссария для поиска. По умолчанию `csv,txt,tsv`.                      | `pdf2zh_next example.pdf --glossary_dir "path/to/glossaries" --glossary_file_extensions "csv,txt,tsv,xlsx"`           |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--glossary`                    | use custom glossary                                                                    | `pdf2zh_next example.pdf --glossary my-glossary.txt`                                                                  |
| `--save-glossary`               | save the merged glossary to a file                                                     | `pdf2zh_next example.pdf --save-glossary output-glossary.txt`                                                         |
| `--save-glossary-to-origin-dir` | save the merged glossary to the same directory as the original file, with a suffix     | `pdf2zh_next example.pdf --save-glossary-to-origin-dir`                                                               |
| `--save-translated-glossary`    | save the translated glossary to a file (after translation)                             | `pdf2zh_next example.pdf --save-translated-glossary output-translated-glossary.txt`                                   |
| `--save-translated-glossary-to-origin-dir` | save the translated glossary to the same directory as the original file, with a suffix | `pdf2zh_next example.pdf --save-translated-glossary-to-origin-dir`                                                    |

---

### OUTPUT

| `--save-auto-extracted-glossary`| сохранить автоматически извлечённый глоссарий                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--glossary`                    | использовать пользовательский глоссарий                                                                    | `pdf2zh_next example.pdf --glossary my-glossary.txt`                                                                  |
| `--save-glossary`               | сохранить объединённый глоссарий в файл                                                     | `pdf2zh_next example.pdf --save-glossary output-glossary.txt`                                                         |
| `--save-glossary-to-origin-dir` | сохранить объединённый глоссарий в ту же директорию, что и исходный файл, с суффиксом     | `pdf2zh_next example.pdf --save-glossary-to-origin-dir`                                                               |
| `--save-translated-glossary`    | сохранить переведённый глоссарий в файл (после перевода)                             | `pdf2zh_next example.pdf --save-translated-glossary output-translated-glossary.txt`                                   |
| `--save-translated-glossary-to-origin-dir` | сохранить переведённый глоссарий в ту же директорию, что и исходный файл, с суффиксом | `pdf2zh_next example.pdf --save-translated-glossary-to-origin-dir`                                                    |
`number`  | `-`   |
|---------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------|-------|
| `--pool-timeout`                | Timeout for translation pool. If not set, will use 10 seconds                                     | `pdf2zh_next example.pdf --pool-timeout 60`                                                                | `number`  | `-`   |
| `--pool-queue-size`             | Queue size for translation pool. If not set, will use 1000                                        | `pdf2zh_next example.pdf --pool-queue-size 1000`                                                           | `number`  | `-`   |
| `--pool-max-retries`            | Maximum retries for translation pool. If not set, will use 3                                      | `pdf2zh_next example.pdf --pool-max-retries 5`                                                             | `number`  | `-`   |
| `--pool-retry-delay`            | Delay between retries for translation pool. If not set, will use 1 second                         | `pdf2zh_next example.pdf --pool-retry-delay 2`                                                             | `number`  | `-`   |

---

### TRANSLATION

| `--pool-max-workers`            | Максимальное количество воркеров для пула переводов. Если не установлено, будет использоваться qps в качестве количества воркеров | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           | `number`  | `-`   |
|---------------------------------|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------|-------|
| `--pool-timeout`                | Таймаут для пула переводов. Если не установлено, будет использоваться 10 секунд                                     | `pdf2zh_next example.pdf --pool-timeout 60`                                                                | `number`  | `-`   |
| `--pool-queue-size`             | Размер очереди для пула переводов. Если не установлено, будет использоваться 1000                                        | `pdf2zh_next example.pdf --pool-queue-size 1000`                                                           | `number`  | `-`   |
| `--pool-max-retries`            | Максимальное количество повторных попыток для пула переводов. Если не установлено, будет использоваться 3                                      | `pdf2zh_next example.pdf --pool-max-retries 5`                                                             | `number`  | `-`   |
| `--pool-retry-delay`            | Задержка между повторными попытками для пула переводов. Если не установлено, будет использоваться 1 секунда                         | `pdf2zh_next example.pdf --pool-retry-delay 2`                                                             | `number`  | `-`   |
| ------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--term-timeout`                | Timeout for term extraction translation service. If not set, will follow timeout.        | `pdf2zh_next example.pdf --term-timeout 60`                                                                            |
| `--term-retry`                  | Retry count for term extraction translation service. If not set, will follow retry.     | `pdf2zh_next example.pdf --term-retry 3`                                                                               |
| `--term-fallback`               | Fallback translation service for term extraction. If not set, will follow fallback.      | `pdf2zh_next example.pdf --term-fallback google`                                                                       |
| `--term-fallback-languages`     | Fallback languages for term extraction translation service. If not set, will follow fallback-languages. | `pdf2zh_next example.pdf --term-fallback-languages en,ja`                                                               |
| `--term-fallback-qps`           | QPS limit for term extraction fallback translation service. If not set, will follow fallback-qps. | `pdf2zh_next example.pdf --term-fallback-qps 20`                                                                       |
| `--term-fallback-timeout`       | Timeout for term extraction fallback translation service. If not set, will follow fallback-timeout. | `pdf2zh_next example.pdf --term-fallback-timeout 60`                                                                   |
| `--term-fallback-retry`         | Retry count for term extraction fallback translation service. If not set, will follow fallback-retry. | `pdf2zh_next example.pdf --term-fallback-retry 3`                                                                      |
| `--term-fallback-fallback`      | Fallback translation service for term extraction fallback. If not set, will follow fallback-fallback. | `pdf2zh_next example.pdf --term-fallback-fallback google`                                                               |
| `--term-fallback-fallback-languages` | Fallback languages for term extraction fallback translation service. If not set, will follow fallback-fallback-languages. | `pdf2zh_next example.pdf --term-fallback-fallback-languages en,ja`                                                      |
| `--term-fallback-fallback-qps`  | QPS limit for term extraction fallback fallback translation service. If not set, will follow fallback-fallback-qps. | `pdf2zh_next example.pdf --term-fallback-fallback-qps 20`                                                               |
| `--term-fallback-fallback-timeout` | Timeout for term extraction fallback fallback translation service. If not set, will follow fallback-fallback-timeout. | `pdf2zh_next example.pdf --term-fallback-fallback-timeout 60`                                                           |
| `--term-fallback-fallback-retry` | Retry count for term extraction fallback fallback translation service. If not set, will follow fallback-fallback-retry. | `pdf2zh_next example.pdf --term-fallback-fallback-retry 3`                                                              |

---

### OUTPUT LANGUAGE

ru

---

### OUTPUT

| `--term-qps`                    | Ограничение QPS для службы перевода извлечения терминов. Если не установлено, будет следовать qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--term-timeout`                | Таймаут для службы перевода извлечения терминов. Если не установлено, будет следовать timeout.             | `pdf2zh_next example.pdf --term-timeout 60`                                                                            |
| `--term-retry`                  | Количество повторных попыток для службы перевода извлечения терминов. Если не установлено, будет следовать retry. | `pdf2zh_next example.pdf --term-retry 3`                                                                               |
| `--term-fallback`               | Резервная служба перевода для извлечения терминов. Если не установлено, будет следовать fallback.           | `pdf2zh_next example.pdf --term-fallback google`                                                                       |
| `--term-fallback-languages`     | Резервные языки для службы перевода извлечения терминов. Если не установлено, будет следовать fallback-languages. | `pdf2zh_next example.pdf --term-fallback-languages en,ja`                                                               |
| `--term-fallback-qps`           | Ограничение QPS для резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-qps. | `pdf2zh_next example.pdf --term-fallback-qps 20`                                                                       |
| `--term-fallback-timeout`       | Таймаут для резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-timeout. | `pdf2zh_next example.pdf --term-fallback-timeout 60`                                                                   |
| `--term-fallback-retry`         | Количество повторных попыток для резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-retry. | `pdf2zh_next example.pdf --term-fallback-retry 3`                                                                      |
| `--term-fallback-fallback`      | Резервная служба перевода для резервного извлечения терминов. Если не установлено, будет следовать fallback-fallback. | `pdf2zh_next example.pdf --term-fallback-fallback google`                                                               |
| `--term-fallback-fallback-languages` | Резервные языки для резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-fallback-languages. | `pdf2zh_next example.pdf --term-fallback-fallback-languages en,ja`                                                      |
| `--term-fallback-fallback-qps`  | Ограничение QPS для резервной резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-fallback-qps. | `pdf2zh_next example.pdf --term-fallback-fallback-qps 20`                                                               |
| `--term-fallback-fallback-timeout` | Таймаут для резервной резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-fallback-timeout. | `pdf2zh_next example.pdf --term-fallback-fallback-timeout 60`                                                           |
| `--term-fallback-fallback-retry` | Количество повторных попыток для резервной резервной службы перевода извлечения терминов. Если не установлено, будет следовать fallback-fallback-retry. | `pdf2zh_next example.pdf --term-fallback-fallback-retry 3`                                                              |
|
| `--term-pool-max-workers`       | Максимальное количество рабочих процессов для пула перевода терминов. Если не установлено или равно 0, следует за pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |   |

---

### TRANSLATION

```markdown
| `--term-pool-max-workers`       | Максимальное количество рабочих процессов для пула перевода терминов. Если не установлено или равно 0, следует за pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |   |
```
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-file`               | Specify a custom glossary file                                                          | `pdf2zh_next example.pdf --glossary-file my-glossary.txt`                                                             |
| `--no-merge-glossary`           | Disable merge glossary                                                                  | `pdf2zh_next example.pdf --no-merge-glossary`                                                                         |
| `--no-merge-glossary-fallback`  | Disable fallback to default glossary when custom glossary fails                         | `pdf2zh_next example.pdf --no-merge-glossary-fallback`                                                                |
| `--glossary-merge-strategy`     | Specify the strategy for merging glossaries: `overwrite`, `combine`, `priority`         | `pdf2zh_next example.pdf --glossary-merge-strategy priority`                                                          |
| `--glossary-priority`           | Specify the priority of the custom glossary when using the `priority` merge strategy    | `pdf2zh_next example.pdf --glossary-priority 10`                                                                      |
| `--glossary-fallback-strategy`  | Specify the fallback strategy: `ignore`, `use_default`, `abort`                         | `pdf2zh_next example.pdf --glossary-fallback-strategy use_default`                                                    |

---

### TRANSLATION RESULT

| `--no-auto-extract-glossary`    | Отключить автоматическое извлечение глоссария                                                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-file`               | Указать пользовательский файл глоссария                                                                            | `pdf2zh_next example.pdf --glossary-file my-glossary.txt`                                                             |
| `--no-merge-glossary`           | Отключить объединение глоссариев                                                                                   | `pdf2zh_next example.pdf --no-merge-glossary`                                                                         |
| `--no-merge-glossary-fallback`  | Отключить возврат к глоссарию по умолчанию при сбое пользовательского глоссария                                     | `pdf2zh_next example.pdf --no-merge-glossary-fallback`                                                                |
| `--glossary-merge-strategy`     | Указать стратегию объединения глоссариев: `overwrite`, `combine`, `priority`                                        | `pdf2zh_next example.pdf --glossary-merge-strategy priority`                                                          |
| `--glossary-priority`           | Указать приоритет пользовательского глоссария при использовании стратегии объединения `priority`                    | `pdf2zh_next example.pdf --glossary-priority 10`                                                                      |
| `--glossary-fallback-strategy`  | Указать стратегию возврата: `ignore`, `use_default`, `abort`                                                        | `pdf2zh_next example.pdf --glossary-fallback-strategy use_default`                                                    |
| `--primary-font-family`         | Переопределяет основное семейство шрифтов для переведенного текста. Варианты: 'serif' для шрифтов с засечками, 'sans-serif' для рубленых шрифтов, 'script' для рукописных/курсивных шрифтов. Если не указано, используется автоматический выбор шрифта на основе свойств исходного текста. | `pdf2zh_next example.pdf --primary-font-family serif` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-cover`                    | Do not output cover pages for bilingual PDF files                                       | `pdf2zh_next example.pdf --no-cover`                                                                                  |
| `--cover-logo <path>`           | Set logo for cover pages (default: `logo.png` in the same directory as the PDF file)    | `pdf2zh_next example.pdf --cover-logo ./logo.png`                                                                     |
| `--cover-title <title>`         | Set title for cover pages (default: same as the PDF file name)                          | `pdf2zh_next example.pdf --cover-title "My Report"`                                                                   |
| `--cover-subtitle <subtitle>`   | Set subtitle for cover pages (default: empty)                                           | `pdf2zh_next example.pdf --cover-subtitle "Translated Version"`                                                        |
| `--cover-footer <footer>`       | Set footer for cover pages (default: empty)                                             | `pdf2zh_next example.pdf --cover-footer "Confidential"`                                                               |
| `--cover-background <path>`     | Set background image for cover pages (default: empty)                                   | `pdf2zh_next example.pdf --cover-background ./background.png`                                                          |
| `--cover-date <date>`           | Set date for cover pages (default: current date)                                        | `pdf2zh_next example.pdf --cover-date "2024-01-01"`                                                                   |
| `--cover-author <author>`       | Set author for cover pages (default: empty)                                             | `pdf2zh_next example.pdf --cover-author "John Doe"`                                                                   |
| `--cover-organization <org>`    | Set organization for cover pages (default: empty)                                       | `pdf2zh_next example.pdf --cover-organization "My Company"`                                                           |
| `--cover-language <lang>`       | Set language for cover pages (default: `en`)                                            | `pdf2zh_next example.pdf --cover-language zh`                                                                         |
| `--cover-template <path>`       | Set custom cover template (default: built-in template)                                  | `pdf2zh_next example.pdf --cover-template ./custom_template.html`                                                      |
| `--cover-css <path>`            | Set custom CSS for cover pages (default: built-in CSS)                                  | `pdf2zh_next example.pdf --cover-css ./custom_style.css`                                                              |
| `--cover-ignore-missing-logo`   | Ignore missing logo file and proceed without logo                                       | `pdf2zh_next example.pdf --cover-ignore-missing-logo`                                                                 |
| `--cover-ignore-missing-bg`     | Ignore missing background image and proceed without background                          | `pdf2zh_next example.pdf --cover-ignore-missing-bg`                                                                   |
| `--cover-force`                 | Force regenerate cover pages even if they already exist                                 | `pdf2zh_next example.pdf --cover-force`                                                                               |

---

### OUTPUT LANGUAGE

ru

---

| `--no-dual`                     | Не выводить двуязычные PDF-файлы                                                       | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-cover`                    | Не выводить титульные страницы для двуязычных PDF-файлов                                | `pdf2zh_next example.pdf --no-cover`                                                                                  |
| `--cover-logo <path>`           | Установить логотип для титульных страниц (по умолчанию: `logo.png` в той же директории, что и PDF-файл) | `pdf2zh_next example.pdf --cover-logo ./logo.png`                                                                     |
| `--cover-title <title>`         | Установить заголовок для титульных страниц (по умолчанию: то же, что и имя PDF-файла)   | `pdf2zh_next example.pdf --cover-title "My Report"`                                                                   |
| `--cover-subtitle <subtitle>`   | Установить подзаголовок для титульных страниц (по умолчанию: пусто)                     | `pdf2zh_next example.pdf --cover-subtitle "Translated Version"`                                                        |
| `--cover-footer <footer>`       | Установить нижний колонтитул для титульных страниц (по умолчанию: пусто)                | `pdf2zh_next example.pdf --cover-footer "Confidential"`                                                               |
| `--cover-background <path>`     | Установить фоновое изображение для титульных страниц (по умолчанию: пусто)              | `pdf2zh_next example.pdf --cover-background ./background.png`                                                          |
| `--cover-date <date>`           | Установить дату для титульных страниц (по умолчанию: текущая дата)                      | `pdf2zh_next example.pdf --cover-date "2024-01-01"`                                                                   |
| `--cover-author <author>`       | Установить автора для титульных страниц (по умолчанию: пусто)                           | `pdf2zh_next example.pdf --cover-author "John Doe"`                                                                   |
| `--cover-organization <org>`    | Установить организацию для титульных страниц (по умолчанию: пусто)                      | `pdf2zh_next example.pdf --cover-organization "My Company"`                                                           |
| `--cover-language <lang>`       | Установить язык для титульных страниц (по умолчанию: `en`)                              | `pdf2zh_next example.pdf --cover-language zh`                                                                         |
| `--cover-template <path>`       | Установить пользовательский шаблон титульной страницы (по умолчанию: встроенный шаблон) | `pdf2zh_next example.pdf --cover-template ./custom_template.html`                                                      |
| `--cover-css <path>`            | Установить пользовательский CSS для титульных страниц (по умолчанию: встроенный CSS)    | `pdf2zh_next example.pdf --cover-css ./custom_style.css`                                                              |
| `--cover-ignore-missing-logo`   | Игнорировать отсутствующий файл логотипа и продолжить без логотипа                      | `pdf2zh_next example.pdf --cover-ignore-missing-logo`                                                                 |
| `--cover-ignore-missing-bg`     | Игнорировать отсутствующее фоновое изображение и продолжить без фона                    | `pdf2zh_next example.pdf --cover-ignore-missing-bg`                                                                   |
| `--cover-force`                 | Принудительно перегенерировать титульные страницы, даже если они уже существуют        | `pdf2zh_next example.pdf --cover-force`                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-bilingual`                | Do not output bilingual PDF files                                                       | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--no-ocr`                      | Do not perform OCR on the PDF file                                                      | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--no-tex`                      | Do not output LaTeX files                                                               | `pdf2zh_next example.pdf --no-tex`                                                                                    |
| `--no-pdf`                      | Do not output PDF files                                                                 | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--no-markdown`                 | Do not output Markdown files                                                            | `pdf2zh_next example.pdf --no-markdown`                                                                               |
| `--no-html`                     | Do not output HTML files                                                                | `pdf2zh_next example.pdf --no-html`                                                                                   |
| `--no-json`                     | Do not output JSON files                                                                | `pdf2zh_next example.pdf --no-json`                                                                                   |
| `--no-docx`                     | Do not output DOCX files                                                                | `pdf2zh_next example.pdf --no-docx`                                                                                   |
| `--no-pptx`                     | Do not output PPTX files                                                                | `pdf2zh_next example.pdf --no-pptx`                                                                                   |
| `--no-xlsx`                     | Do not output XLSX files                                                                | `pdf2zh_next example.pdf --no-xlsx`                                                                                   |
| `--no-txt`                      | Do not output TXT files                                                                 | `pdf2zh_next example.pdf --no-txt`                                                                                    |
| `--no-csv`                      | Do not output CSV files                                                                 | `pdf2zh_next example.pdf --no-csv`                                                                                    |
| `--no-tsv`                      | Do not output TSV files                                                                 | `pdf2zh_next example.pdf --no-tsv`                                                                                    |

---

### TRANSLATION RESULT

| `--no-mono`                     | Не выводить односторонние PDF-файлы                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-bilingual`                | Не выводить двусторонние PDF-файлы                                                      | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--no-ocr`                      | Не выполнять OCR на PDF-файле                                                           | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--no-tex`                      | Не выводить LaTeX-файлы                                                                 | `pdf2zh_next example.pdf --no-tex`                                                                                    |
| `--no-pdf`                      | Не выводить PDF-файлы                                                                   | `pdf2zh_next example.pdf --no-pdf`                                                                                    |
| `--no-markdown`                 | Не выводить Markdown-файлы                                                              | `pdf2zh_next example.pdf --no-markdown`                                                                               |
| `--no-html`                     | Не выводить HTML-файлы                                                                  | `pdf2zh_next example.pdf --no-html`                                                                                   |
| `--no-json`                     | Не выводить JSON-файлы                                                                  | `pdf2zh_next example.pdf --no-json`                                                                                   |
| `--no-docx`                     | Не выводить DOCX-файлы                                                                  | `pdf2zh_next example.pdf --no-docx`                                                                                   |
| `--no-pptx`                     | Не выводить PPTX-файлы                                                                  | `pdf2zh_next example.pdf --no-pptx`                                                                                   |
| `--no-xlsx`                     | Не выводить XLSX-файлы                                                                  | `pdf2zh_next example.pdf --no-xlsx`                                                                                   |
| `--no-txt`                      | Не выводить TXT-файлы                                                                   | `pdf2zh_next example.pdf --no-txt`                                                                                    |
| `--no-csv`                      | Не выводить CSV-файлы                                                                   | `pdf2zh_next example.pdf --no-csv`                                                                                    |
| `--no-tsv`                      | Не выводить TSV-файлы                                                                   | `pdf2zh_next example.pdf --no-tsv`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-font-size-relative` | Relative size of formula text compared to normal text                                   | `pdf2zh_next example.pdf --formular-font-size-relative 0.8`                                                           |
| `--formular-merge-vertical`     | Merge vertically adjacent formulas                                                      | `pdf2zh_next example.pdf --formular-merge-vertical`                                                                   |
| `--formular-merge-horizontal`   | Merge horizontally adjacent formulas                                                    | `pdf2zh_next example.pdf --formular-merge-horizontal`                                                                 |
| `--formular-merge-max-distance` | Maximum distance for merging formulas (default: 1.0)                                    | `pdf2zh_next example.pdf --formular-merge-max-distance 2.0`                                                           |
| `--formular-merge-max-angle`    | Maximum angle difference for merging formulas (default: 0.1)                            | `pdf2zh_next example.pdf --formular-merge-max-angle 0.2`                                                              |
| `--formular-merge-same-font`    | Only merge formulas with the same font                                                  | `pdf2zh_next example.pdf --formular-merge-same-font`                                                                  |
| `--formular-merge-same-size`    | Only merge formulas with the same size                                                  | `pdf2zh_next example.pdf --formular-merge-same-size`                                                                  |
| `--formular-ocr-engine`         | OCR engine for formula recognition (default: "mathpix")                                 | `pdf2zh_next example.pdf --formular-ocr-engine paddle`                                                                |
| `--formular-ocr-lang`           | Language for formula OCR (default: "formula")                                           | `pdf2zh_next example.pdf --formular-ocr-lang en`                                                                      |
| `--formular-ocr-format`         | Output format for formula OCR (default: "latex")                                        | `pdf2zh_next example.pdf --formular-ocr-format text`                                                                  |
| `--formular-ocr-mathpix-appid`  | Mathpix App ID for formula OCR                                                          | `pdf2zh_next example.pdf --formular-ocr-mathpix-appid your_app_id`                                                    |
| `--formular-ocr-mathpix-appkey` | Mathpix App Key for formula OCR                                                         | `pdf2zh_next example.pdf --formular-ocr-mathpix-appkey your_app_key`                                                  |
| `--formular-ocr-paddle-model`   | PaddleOCR model for formula recognition (default: "formula_rec")                        | `pdf2zh_next example.pdf --formular-ocr-paddle-model ch_ppocr_v3_rec`                                                 |
| `--formular-ocr-paddle-lang`    | PaddleOCR language for formula recognition (default: "ch")                              | `pdf2zh_next example.pdf --formular-ocr-paddle-lang en`                                                               |
| `--formular-ocr-paddle-cpu`     | Use CPU for PaddleOCR instead of GPU                                                    | `pdf2zh_next example.pdf --formular-ocr-paddle-cpu`                                                                   |
| `--formular-ocr-paddle-threads` | Number of threads for PaddleOCR (default: 4)                                            | `pdf2zh_next example.pdf --formular-ocr-paddle-threads 8`                                                             |
| `--formular-ocr-paddle-precision` | Precision mode for PaddleOCR (default: "fp32")                                        | `pdf2zh_next example.pdf --formular-ocr-paddle-precision fp16`                                                        |
| `--formular-ocr-paddle-layout`  | Enable layout analysis for PaddleOCR                                                    | `pdf2zh_next example.pdf --formular-ocr-paddle-layout`                                                                |

---

### OUTPUT

| `--formular-font-pattern`       | Шаблон шрифта для идентификации текста формул                                          | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-font-size-relative` | Относительный размер текста формул по сравнению с обычным текстом                      | `pdf2zh_next example.pdf --formular-font-size-relative 0.8`                                                           |
| `--formular-merge-vertical`     | Объединять вертикально смежные формулы                                                 | `pdf2zh_next example.pdf --formular-merge-vertical`                                                                   |
| `--formular-merge-horizontal`   | Объединять горизонтально смежные формулы                                               | `pdf2zh_next example.pdf --formular-merge-horizontal`                                                                 |
| `--formular-merge-max-distance` | Максимальное расстояние для объединения формул (по умолчанию: 1.0)                     | `pdf2zh_next example.pdf --formular-merge-max-distance 2.0`                                                           |
| `--formular-merge-max-angle`    | Максимальная разница углов для объединения формул (по умолчанию: 0.1)                  | `pdf2zh_next example.pdf --formular-merge-max-angle 0.2`                                                              |
| `--formular-merge-same-font`    | Объединять только формулы с одинаковым шрифтом                                         | `pdf2zh_next example.pdf --formular-merge-same-font`                                                                  |
| `--formular-merge-same-size`    | Объединять только формулы с одинаковым размером                                         | `pdf2zh_next example.pdf --formular-merge-same-size`                                                                  |
| `--formular-ocr-engine`         | Движок OCR для распознавания формул (по умолчанию: "mathpix")                          | `pdf2zh_next example.pdf --formular-ocr-engine paddle`                                                                |
| `--formular-ocr-lang`           | Язык для OCR формул (по умолчанию: "formula")                                          | `pdf2zh_next example.pdf --formular-ocr-lang en`                                                                      |
| `--formular-ocr-format`         | Формат вывода для OCR формул (по умолчанию: "latex")                                   | `pdf2zh_next example.pdf --formular-ocr-format text`                                                                  |
| `--formular-ocr-mathpix-appid`  | Mathpix App ID для OCR формул                                                          | `pdf2zh_next example.pdf --formular-ocr-mathpix-appid your_app_id`                                                    |
| `--formular-ocr-mathpix-appkey` | Mathpix App Key для OCR формул                                                         | `pdf2zh_next example.pdf --formular-ocr-mathpix-appkey your_app_key`                                                  |
| `--formular-ocr-paddle-model`   | Модель PaddleOCR для распознавания формул (по умолчанию: "formula_rec")                | `pdf2zh_next example.pdf --formular-ocr-paddle-model ch_ppocr_v3_rec`                                                 |
| `--formular-ocr-paddle-lang`    | Язык PaddleOCR для распознавания формул (по умолчанию: "ch")                           | `pdf2zh_next example.pdf --formular-ocr-paddle-lang en`                                                               |
| `--formular-ocr-paddle-cpu`     | Использовать CPU для PaddleOCR вместо GPU                                              | `pdf2zh_next example.pdf --formular-ocr-paddle-cpu`                                                                   |
| `--formular-ocr-paddle-threads` | Количество потоков для PaddleOCR (по умолчанию: 4)                                     | `pdf2zh_next example.pdf --formular-ocr-paddle-threads 8`                                                             |
| `--formular-ocr-paddle-precision` | Режим точности для PaddleOCR (по умолчанию: "fp32")                                  | `pdf2zh_next example.pdf --formular-ocr-paddle-precision fp16`                                                        |
| `--formular-ocr-paddle-layout`  | Включить анализ макета для PaddleOCR                                                   | `pdf2zh_next example.pdf --formular-ocr-paddle-layout`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-pattern-repl`  | Replacement for matched formula text                                                    | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-repl "\\1"`                         |
| `--formular-char-pattern-keep`  | Whether to keep the matched formula text (default: `True`)                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-keep False`                         |
| `--formular-char-pattern-color` | Color to use for the matched formula text (default: `#FF0000`)                          | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-color "#00FF00"`                    |
| `--formular-char-pattern-size`  | Font size to use for the matched formula text (default: `12`)                           | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-size 14`                            |
| `--formular-char-pattern-font`  | Font family to use for the matched formula text (default: `Times New Roman`)            | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-font "Arial"`                       |
| `--formular-char-pattern-style` | Font style to use for the matched formula text (default: `normal`)                      | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-style "italic"`                     |
| `--formular-char-pattern-weight` | Font weight to use for the matched formula text (default: `normal`)                     | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-weight "bold"`                      |
| `--formular-char-pattern-align` | Text alignment to use for the matched formula text (default: `center`)                  | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-align "left"`                       |
| `--formular-char-pattern-pos`   | Text position to use for the matched formula text (default: `relative`)                 | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-pos "absolute"`                     |
| `--formular-char-pattern-top`   | Top position to use for the matched formula text (default: `0`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-top 10`                             |
| `--formular-char-pattern-left`  | Left position to use for the matched formula text (default: `0`)                        | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-left 10`                            |
| `--formular-char-pattern-right` | Right position to use for the matched formula text (default: `0`)                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-right 10`                           |
| `--formular-char-pattern-bottom` | Bottom position to use for the matched formula text (default: `0`)                      | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-bottom 10`                          |
| `--formular-char-pattern-zindex` | Z-index to use for the matched formula text (default: `0`)                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-zindex 1`                           |
| `--formular-char-pattern-opacity` | Opacity to use for the matched formula text (default: `1`)                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-opacity 0.5`                        |
| `--formular-char-pattern-rotation` | Rotation angle to use for the matched formula text (default: `0`)                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-rotation 90`                        |
| `--formular-char-pattern-scale` | Scale factor to use for the matched formula text (default: `1`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-scale 1.5`                          |
| `--formular-char-pattern-transform` | Transform to use for the matched formula text (default: `none`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-transform "rotate(90deg)"`          |
| `--formular-char-pattern-transition` | Transition to use for the matched formula text (default: `none`)                        | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-transition "all 0.3s ease-in-out"`  |
| `--formular-char-pattern-animation` | Animation to use for the matched formula text (default: `none`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-animation "fadeIn 1s"`              |

---

| `--formular-char-pattern`       | Символьный шаблон для идентификации текста формул                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-pattern-repl`  | Замена для совпавшего текста формул                                                    | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-repl "\\1"`                         |
| `--formular-char-pattern-keep`  | Сохранять ли совпавший текст формул (по умолчанию: `True`)                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-keep False`                         |
| `--formular-char-pattern-color` | Цвет для совпавшего текста формул (по умолчанию: `#FF0000`)                          | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-color "#00FF00"`                    |
| `--formular-char-pattern-size`  | Размер шрифта для совпавшего текста формул (по умолчанию: `12`)                           | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-size 14`                            |
| `--formular-char-pattern-font`  | Семейство шрифтов для совпавшего текста формул (по умолчанию: `Times New Roman`)            | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-font "Arial"`                       |
| `--formular-char-pattern-style` | Стиль шрифта для совпавшего текста формул (по умолчанию: `normal`)                      | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-style "italic"`                     |
| `--formular-char-pattern-weight` | Насыщенность шрифта для совпавшего текста формул (по умолчанию: `normal`)                     | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-weight "bold"`                      |
| `--formular-char-pattern-align` | Выравнивание текста для совпавшего текста формул (по умолчанию: `center`)                  | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-align "left"`                       |
| `--formular-char-pattern-pos`   | Позиция текста для совпавшего текста формул (по умолчанию: `relative`)                 | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-pos "absolute"`                     |
| `--formular-char-pattern-top`   | Верхняя позиция для совпавшего текста формул (по умолчанию: `0`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-top 10`                             |
| `--formular-char-pattern-left`  | Левая позиция для совпавшего текста формул (по умолчанию: `0`)                        | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-left 10`                            |
| `--formular-char-pattern-right` | Правая позиция для совпавшего текста формул (по умолчанию: `0`)                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-right 10`                           |
| `--formular-char-pattern-bottom` | Нижняя позиция для совпавшего текста формул (по умолчанию: `0`)                      | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-bottom 10`                          |
| `--formular-char-pattern-zindex` | Z-индекс для совпавшего текста формул (по умолчанию: `0`)                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-zindex 1`                           |
| `--formular-char-pattern-opacity` | Прозрачность для совпавшего текста формул (по умолчанию: `1`)                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-opacity 0.5`                        |
| `--formular-char-pattern-rotation` | Угол поворота для совпавшего текста формул (по умолчанию: `0`)                       | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-rotation 90`                        |
| `--formular-char-pattern-scale` | Коэффициент масштабирования для совпавшего текста формул (по умолчанию: `1`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-scale 1.5`                          |
| `--formular-char-pattern-transform` | Трансформация для совпавшего текста формул (по умолчанию: `none`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-transform "rotate(90deg)"`          |
| `--formular-char-pattern-transition` | Переход для совпавшего текста формул (по умолчанию: `none`)                        | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-transition "all 0.3s ease-in-out"`  |
| `--formular-char-pattern-animation` | Анимация для совпавшего текста формул (по умолчанию: `none`)                         | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-animation "fadeIn 1s"`              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | The threshold for splitting short lines, default is 0.5. See below for more information | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-threshold 0.7`                                       |
| `--split-short-lines-ratio`     | The ratio for splitting short lines, default is 0.5. See below for more information      | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-ratio 0.7`                                           |
| `--no-split-short-lines`        | Disable splitting short lines, which is enabled by default                               | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--no-split-long-lines`         | Disable splitting long lines, which is enabled by default                                | `pdf2zh_next example.pdf --no-split-long-lines`                                                                       |

---

### TRANSLATION RESULT

| `--split-short-lines`           | Принудительное разделение коротких строк на разные абзацы                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | Порог для разделения коротких строк, по умолчанию 0.5. Подробнее см. ниже | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-threshold 0.7`                                       |
| `--split-short-lines-ratio`     | Коэффициент для разделения коротких строк, по умолчанию 0.5. Подробнее см. ниже      | `pdf2zh_next example.pdf --split-short-lines --split-short-lines-ratio 0.7`                                           |
| `--no-split-short-lines`        | Отключить разделение коротких строк, включено по умолчанию                               | `pdf2zh_next example.pdf --no-split-short-lines`                                                                      |
| `--no-split-long-lines`         | Отключить разделение длинных строк, включено по умолчанию                                | `pdf2zh_next example.pdf --no-split-long-lines`                                                                       |
`float`  | `1.0`  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------|--------|
| `--short-line-split-min-length` | Minimum length threshold for short lines to be split                                    | `pdf2zh_next example.pdf --short-line-split-min-length 10`                                                             | `int`    | `5`    |
| `--short-line-split-max-length` | Maximum length threshold for short lines to be split                                    | `pdf2zh_next example.pdf --short-line-split-max-length 50`                                                             | `int`    | `30`   |

---

### TRANSLATION RESULT

| `--short-line-split-factor`     | Коэффициент порога разделения для коротких строк                                        | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               | `float`  | `1.0`  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------|--------|
| `--short-line-split-min-length` | Минимальный порог длины для разделения коротких строк                                   | `pdf2zh_next example.pdf --short-line-split-min-length 10`                                                             | `int`    | `5`    |
| `--short-line-split-max-length` | Максимальный порог длины для разделения коротких строк                                  | `pdf2zh_next example.pdf --short-line-split-max-length 50`                                                             | `int`    | `30`   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-latex`                  | Skip LaTeX compilation step                                                            | `pdf2zh_next example.pdf --skip-latex`                                                                                |
| `--skip-pdf`                    | Skip PDF generation step                                                                | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--skip-all`                    | Skip all steps except for the first step                                                | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--clean-only`                  | Only perform PDF cleaning step                                                          | `pdf2zh_next example.pdf --clean-only`                                                                                |
| `--translate-only`              | Only perform translation step                                                           | `pdf2zh_next example.pdf --translate-only`                                                                            |
| `--latex-only`                  | Only perform LaTeX compilation step                                                     | `pdf2zh_next example.pdf --latex-only`                                                                                |
| `--pdf-only`                    | Only perform PDF generation step                                                        | `pdf2zh_next example.pdf --pdf-only`                                                                                  |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir <dir>`             | Specify cache directory                                                                 | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--clean-cache`                 | Clean cache before processing                                                           | `pdf2zh_next example.pdf --clean-cache`                                                                               |
| `--clean-cache-after`           | Clean cache after processing                                                            | `pdf2zh_next example.pdf --clean-cache-after`                                                                         |
| `--clean-cache-both`            | Clean cache before and after processing                                                 | `pdf2zh_next example.pdf --clean-cache-both`                                                                          |
| `--force`                       | Force overwrite existing files                                                          | `pdf2zh_next example.pdf --force`                                                                                     |
| `--yes`                         | Automatically answer yes to all prompts                                                 | `pdf2zh_next example.pdf --yes`                                                                                       |
| `--no`                          | Automatically answer no to all prompts                                                  | `pdf2zh_next example.pdf --no`                                                                                        |
| `--verbose`                     | Enable verbose output                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--quiet`                       | Disable all output                                                                      | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help information                                                                   | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT

| `--skip-clean`                  | Пропустить шаг очистки PDF                                                              | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Пропустить шаг перевода                                                                 | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-latex`                  | Пропустить шаг компиляции LaTeX                                                         | `pdf2zh_next example.pdf --skip-latex`                                                                                |
| `--skip-pdf`                    | Пропустить шаг генерации PDF                                                            | `pdf2zh_next example.pdf --skip-pdf`                                                                                  |
| `--skip-all`                    | Пропустить все шаги, кроме первого                                                      | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--clean-only`                  | Выполнить только шаг очистки PDF                                                        | `pdf2zh_next example.pdf --clean-only`                                                                                |
| `--translate-only`              | Выполнить только шаг перевода                                                           | `pdf2zh_next example.pdf --translate-only`                                                                            |
| `--latex-only`                  | Выполнить только шаг компиляции LaTeX                                                   | `pdf2zh_next example.pdf --latex-only`                                                                                |
| `--pdf-only`                    | Выполнить только шаг генерации PDF                                                      | `pdf2zh_next example.pdf --pdf-only`                                                                                  |
| `--no-cache`                    | Отключить кэширование                                                                   | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir <dir>`             | Указать директорию кэша                                                                 | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--clean-cache`                 | Очистить кэш перед обработкой                                                           | `pdf2zh_next example.pdf --clean-cache`                                                                               |
| `--clean-cache-after`           | Очистить кэш после обработки                                                            | `pdf2zh_next example.pdf --clean-cache-after`                                                                         |
| `--clean-cache-both`            | Очистить кэш до и после обработки                                                       | `pdf2zh_next example.pdf --clean-cache-both`                                                                          |
| `--force`                       | Принудительно перезаписать существующие файлы                                           | `pdf2zh_next example.pdf --force`                                                                                     |
| `--yes`                         | Автоматически отвечать «да» на все запросы                                              | `pdf2zh_next example.pdf --yes`                                                                                       |
| `--no`                          | Автоматически отвечать «нет» на все запросы                                             | `pdf2zh_next example.pdf --no`                                                                                        |
| `--verbose`                     | Включить подробный вывод                                                                | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--quiet`                       | Отключить весь вывод                                                                    | `pdf2zh_next example.pdf --quiet`                                                                                     |
| `--version`                     | Показать информацию о версии                                                            | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Показать справочную информацию                                                         | `pdf2zh_next --help`                                                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--dual-translate-first-cover`  | Put translated cover page first in dual PDF mode                                        | `pdf2zh_next example.pdf --dual-translate-first-cover`                                                                |
| `--dual-translate-first-cover-translated`  | Put translated cover page first in dual PDF mode, and translate the cover page.         | `pdf2zh_next example.pdf --dual-translate-first-cover-translated`                                                      |

---

### TRANSLATION RESULT

| `--dual-translate-first`        | Помещать переведенные страницы первыми в режиме двойного PDF                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--dual-translate-first-cover`  | Помещать переведенную титульную страницу первой в режиме двойного PDF                                        | `pdf2zh_next example.pdf --dual-translate-first-cover`                                                                |
| `--dual-translate-first-cover-translated`  | Помещать переведенную титульную страницу первой в режиме двойного PDF и переводить титульную страницу.         | `pdf2zh_next example.pdf --dual-translate-first-cover-translated`                                                      |
| `--disable-rich-text-translate` | Отключить перевод форматированного текста                                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-ocr`   | Enable OCR compatibility enhancement                                                    | `pdf2zh_next example.pdf --enhance-compatibility-ocr`                                                                 |
| `--enhance-compatibility-layout`| Enable layout compatibility enhancement                                                  | `pdf2zh_next example.pdf --enhance-compatibility-layout`                                                              |
| `--enhance-compatibility-font`  | Enable font compatibility enhancement                                                   | `pdf2zh_next example.pdf --enhance-compatibility-font`                                                                |
| `--enhance-compatibility-math`  | Enable math compatibility enhancement                                                   | `pdf2zh_next example.pdf --enhance-compatibility-math`                                                                |
| `--enhance-compatibility-table` | Enable table compatibility enhancement                                                  | `pdf2zh_next example.pdf --enhance-compatibility-table`                                                               |

---

### OUTPUT

| `--enhance-compatibility`       | Включить все опции повышения совместимости                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-ocr`   | Включить повышение совместимости OCR                                                    | `pdf2zh_next example.pdf --enhance-compatibility-ocr`                                                                 |
| `--enhance-compatibility-layout`| Включить повышение совместимости макета                                                  | `pdf2zh_next example.pdf --enhance-compatibility-layout`                                                              |
| `--enhance-compatibility-font`  | Включить повышение совместимости шрифтов                                                   | `pdf2zh_next example.pdf --enhance-compatibility-font`                                                                |
| `--enhance-compatibility-math`  | Включить повышение совместимости математики                                                   | `pdf2zh_next example.pdf --enhance-compatibility-math`                                                                |
| `--enhance-compatibility-table` | Включить повышение совместимости таблиц                                                  | `pdf2zh_next example.pdf --enhance-compatibility-table`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-vertical-writing`         | Use vertical writing mode (for Japanese, Traditional Chinese, and other vertical texts) | `pdf2zh_next example.pdf --use-vertical-writing`                                                                      |
| `--use-continuous-writing`       | Use continuous writing mode (for Japanese, Traditional Chinese, and other vertical texts) | `pdf2zh_next example.pdf --use-continuous-writing`                                                                    |

---

### TRANSLATION RESULT

| `--use-alternating-pages-dual`  | Использовать режим чередования страниц для двойного PDF                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Использовать режим чередования страниц для одиночного PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-vertical-writing`         | Использовать режим вертикального письма (для японского, традиционного китайского и других вертикальных текстов) | `pdf2zh_next example.pdf --use-vertical-writing`                                                                      |
| `--use-continuous-writing`       | Использовать режим непрерывного письма (для японского, традиционного китайского и других вертикальных текстов) | `pdf2zh_next example.pdf --use-continuous-writing`                                                                    |
`none`, `watermark`, `no_watermark`                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `--watermark-text`              | Watermark text for PDF files                                                            | `pdf2zh_next example.pdf --watermark-text "Translated by pdf2zh"`                                                     | Any string                                                                                         |
| `--watermark-font-name`         | Font name for watermark text                                                            | `pdf2zh_next example.pdf --watermark-font-name "Helvetica"`                                                           | Any font name                                                                                      |
| `--watermark-font-size`         | Font size for watermark text                                                            | `pdf2zh_next example.pdf --watermark-font-size 12`                                                                    | Any positive integer                                                                               |
| `--watermark-color`             | Color for watermark text                                                                | `pdf2zh_next example.pdf --watermark-color "gray"`                                                                    | Any color name or hex code                                                                         |
| `--watermark-opacity`           | Opacity for watermark text                                                              | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     | Float value between 0 and 1                                                                        |
| `--watermark-rotation`          | Rotation angle for watermark text                                                       | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     | Integer value between 0 and 360                                                                    |
| `--watermark-position`          | Position for watermark text                                                             | `pdf2zh_next example.pdf --watermark-position "center"`                                                               | `top-left`, `top-center`, `top-right`, `center-left`, `center`, `center-right`, `bottom-left`, `bottom-center`, `bottom-right` |
| `--watermark-spacing`           | Spacing between watermark texts                                                         | `pdf2zh_next example.pdf --watermark-spacing 100`                                                                     | Any positive integer                                                                               |
| `--watermark-density`           | Density of watermark texts                                                              | `pdf2zh_next example.pdf --watermark-density 10`                                                                      | Any positive integer                                                                               |
| `--watermark-layout`            | Layout of watermark texts                                                               | `pdf2zh_next example.pdf --watermark-layout "grid"`                                                                   | `grid`, `diagonal`                                                                                 |
| `--watermark-layer`             | Layer for watermark text                                                                | `pdf2zh_next example.pdf --watermark-layer "above"`                                                                   | `above`, `below`                                                                                   |

---

### TRANSLATION RESULT

| `--watermark-output-mode`       | Режим вывода водяного знака для файлов PDF                                               | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `none`, `watermark`, `no_watermark`                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `--watermark-text`              | Текст водяного знака для файлов PDF                                                     | `pdf2zh_next example.pdf --watermark-text "Translated by pdf2zh"`                                                     | Любая строка                                                                                         |
| `--watermark-font-name`         | Название шрифта для текста водяного знака                                               | `pdf2zh_next example.pdf --watermark-font-name "Helvetica"`                                                           | Любое название шрифта                                                                                      |
| `--watermark-font-size`         | Размер шрифта для текста водяного знака                                                 | `pdf2zh_next example.pdf --watermark-font-size 12`                                                                    | Любое положительное целое число                                                                               |
| `--watermark-color`             | Цвет текста водяного знака                                                              | `pdf2zh_next example.pdf --watermark-color "gray"`                                                                    | Любое название цвета или шестнадцатеричный код                                                                         |
| `--watermark-opacity`           | Прозрачность текста водяного знака                                                      | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     | Значение с плавающей точкой от 0 до 1                                                                        |
| `--watermark-rotation`          | Угол поворота текста водяного знака                                                     | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     | Целочисленное значение от 0 до 360                                                                    |
| `--watermark-position`          | Положение текста водяного знака                                                         | `pdf2zh_next example.pdf --watermark-position "center"`                                                               | `top-left`, `top-center`, `top-right`, `center-left`, `center`, `center-right`, `bottom-left`, `bottom-center`, `bottom-right` |
| `--watermark-spacing`           | Расстояние между текстами водяного знака                                                | `pdf2zh_next example.pdf --watermark-spacing 100`                                                                     | Любое положительное целое число                                                                               |
| `--watermark-density`           | Плотность текстов водяного знака                                                        | `pdf2zh_next example.pdf --watermark-density 10`                                                                      | Любое положительное целое число                                                                               |
| `--watermark-layout`            | Расположение текстов водяного знака                                                     | `pdf2zh_next example.pdf --watermark-layout "grid"`                                                                   | `grid`, `diagonal`                                                                                 |
| `--watermark-layer`             | Слой для текста водяного знака                                                          | `pdf2zh_next example.pdf --watermark-layer "above"`                                                                   | `above`, `below`                                                                                   |
`None` (no split) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------- |
| `--split-by-chapter`            | Split by chapter (if available)                                                         | `pdf2zh_next example.pdf --split-by-chapter`                                                                          | `False`           |
| `--split-by-chapter-min-pages`  | Minimum pages per chapter part (only when `--split-by-chapter` is enabled)              | `pdf2zh_next example.pdf --split-by-chapter --split-by-chapter-min-pages 10`                                          | `5`               |
| `--split-by-chapter-max-pages`  | Maximum pages per chapter part (only when `--split-by-chapter` is enabled)              | `pdf2zh_next example.pdf --split-by-chapter --split-by-chapter-max-pages 100`                                         | `None` (no limit) |

---

### OUTPUT

| `--max-pages-per-part`          | Максимальное количество страниц на часть для раздельного перевода                       | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     | `None` (без разделения) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `--split-by-chapter`            | Разделять по главам (если доступно)                                                     | `pdf2zh_next example.pdf --split-by-chapter`                                                                          | `False`                 |
| `--split-by-chapter-min-pages`  | Минимальное количество страниц на часть главы (только при включенном `--split-by-chapter`) | `pdf2zh_next example.pdf --split-by-chapter --split-by-chapter-min-pages 10`                                          | `5`                     |
| `--split-by-chapter-max-pages`  | Максимальное количество страниц на часть главы (только при включенном `--split-by-chapter`) | `pdf2zh_next example.pdf --split-by-chapter --split-by-chapter-max-pages 100`                                         | `None` (без ограничений) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Method to translate table text, choose from `row`, `col`, `cell` (default: `row`)      | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method=cell`                                   |
| `--translate-table-text-split`  | Whether to split table text, which may improve translation accuracy (default: `false`)  | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-split`                                         |
| `--translate-table-text-merge` | Whether to merge table text, which may improve translation accuracy (default: `false`)  | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-merge`                                         |
| `--translate-table-text-limit`  | The maximum number of words in a table text (default: `1000`)                           | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-limit=500`                                     |
| `--translate-table-text-retry`  | The maximum number of retries for table text translation (default: `3`)                 | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-retry=5`                                       |

---

### TRANSLATION RESULT

| `--translate-table-text`        | Перевести текст таблицы (экспериментальная функция)                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Метод перевода текста таблицы, выбирается из `row`, `col`, `cell` (по умолчанию: `row`) | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method=cell`                                   |
| `--translate-table-text-split`  | Разделять ли текст таблицы, что может повысить точность перевода (по умолчанию: `false`) | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-split`                                         |
| `--translate-table-text-merge`  | Объединять ли текст таблицы, что может повысить точность перевода (по умолчанию: `false`) | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-merge`                                         |
| `--translate-table-text-limit`  | Максимальное количество слов в тексте таблицы (по умолчанию: `1000`)                     | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-limit=500`                                     |
| `--translate-table-text-retry`  | Максимальное количество повторных попыток перевода текста таблицы (по умолчанию: `3`)   | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-retry=5`                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--skip-table-detection`        | Skip table detection                                                                    | `pdf2zh_next example.pdf --skip-table-detection`                                                                       |
| `--skip-formula-detection`      | Skip formula detection                                                                  | `pdf2zh_next example.pdf --skip-formula-detection`                                                                     |
| `--skip-figure-detection`       | Skip figure detection                                                                   | `pdf2zh_next example.pdf --skip-figure-detection`                                                                      |
| `--skip-reference-detection`    | Skip reference detection                                                                | `pdf2zh_next example.pdf --skip-reference-detection`                                                                   |
| `--skip-title-detection`        | Skip title detection                                                                    | `pdf2zh_next example.pdf --skip-title-detection`                                                                       |
| `--skip-header-footer-detection`| Skip header and footer detection                                                        | `pdf2zh_next example.pdf --skip-header-footer-detection`                                                               |
| `--skip-footnote-detection`     | Skip footnote detection                                                                 | `pdf2zh_next example.pdf --skip-footnote-detection`                                                                    |
| `--skip-caption-detection`      | Skip caption detection                                                                  | `pdf2zh_next example.pdf --skip-caption-detection`                                                                     |
| `--skip-list-detection`         | Skip list detection                                                                     | `pdf2zh_next example.pdf --skip-list-detection`                                                                        |
| `--skip-code-detection`         | Skip code detection                                                                     | `pdf2zh_next example.pdf --skip-code-detection`                                                                        |
| `--skip-quote-detection`        | Skip quote detection                                                                    | `pdf2zh_next example.pdf --skip-quote-detection`                                                                       |
| `--skip-equation-detection`     | Skip equation detection                                                                 | `pdf2zh_next example.pdf --skip-equation-detection`                                                                    |
| `--skip-algorithm-detection`    | Skip algorithm detection                                                                | `pdf2zh_next example.pdf --skip-algorithm-detection`                                                                   |
| `--skip-theorem-detection`      | Skip theorem detection                                                                  | `pdf2zh_next example.pdf --skip-theorem-detection`                                                                     |
| `--skip-proof-detection`        | Skip proof detection                                                                    | `pdf2zh_next example.pdf --skip-proof-detection`                                                                       |
| `--skip-definition-detection`   | Skip definition detection                                                               | `pdf2zh_next example.pdf --skip-definition-detection`                                                                  |
| `--skip-example-detection`      | Skip example detection                                                                  | `pdf2zh_next example.pdf --skip-example-detection`                                                                     |
| `--skip-remark-detection`       | Skip remark detection                                                                   | `pdf2zh_next example.pdf --skip-remark-detection`                                                                      |
| `--skip-note-detection`         | Skip note detection                                                                     | `pdf2zh_next example.pdf --skip-note-detection`                                                                        |
| `--skip-warning-detection`      | Skip warning detection                                                                  | `pdf2zh_next example.pdf --skip-warning-detection`                                                                     |
| `--skip-error-detection`        | Skip error detection                                                                    | `pdf2zh_next example.pdf --skip-error-detection`                                                                       |
| `--skip-info-detection`         | Skip info detection                                                                     | `pdf2zh_next example.pdf --skip-info-detection`                                                                        |
| `--skip-tip-detection`          | Skip tip detection                                                                      | `pdf2zh_next example.pdf --skip-tip-detection`                                                                         |
| `--skip-success-detection`      | Skip success detection                                                                  | `pdf2zh_next example.pdf --skip-success-detection`                                                                     |
| `--skip-question-detection`     | Skip question detection                                                                 | `pdf2zh_next example.pdf --skip-question-detection`                                                                    |
| `--skip-caution-detection`      | Skip caution detection                                                                  | `pdf2zh_next example.pdf --skip-caution-detection`                                                                     |
| `--skip-important-detection`    | Skip important detection                                                                | `pdf2zh_next example.pdf --skip-important-detection`                                                                   |
| `--skip-custom-detection`       | Skip custom detection                                                                   | `pdf2zh_next example.pdf --skip-custom-detection`                                                                      |
| `--skip-all-detection`          | Skip all detection                                                                      | `pdf2zh_next example.pdf --skip-all-detection`                                                                         |

---

### TRANSLATION RESULT

| `--skip-scanned-detection`      | Пропустить обнаружение сканированных страниц                                            | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--skip-table-detection`        | Пропустить обнаружение таблиц                                                           | `pdf2zh_next example.pdf --skip-table-detection`                                                                       |
| `--skip-formula-detection`      | Пропустить обнаружение формул                                                           | `pdf2zh_next example.pdf --skip-formula-detection`                                                                     |
| `--skip-figure-detection`       | Пропустить обнаружение рисунков                                                         | `pdf2zh_next example.pdf --skip-figure-detection`                                                                      |
| `--skip-reference-detection`    | Пропустить обнаружение ссылок                                                           | `pdf2zh_next example.pdf --skip-reference-detection`                                                                   |
| `--skip-title-detection`        | Пропустить обнаружение заголовков                                                       | `pdf2zh_next example.pdf --skip-title-detection`                                                                       |
| `--skip-header-footer-detection`| Пропустить обнаружение верхних и нижних колонтитулов                                    | `pdf2zh_next example.pdf --skip-header-footer-detection`                                                               |
| `--skip-footnote-detection`     | Пропустить обнаружение сносок                                                           | `pdf2zh_next example.pdf --skip-footnote-detection`                                                                    |
| `--skip-caption-detection`      | Пропустить обнаружение подписей                                                         | `pdf2zh_next example.pdf --skip-caption-detection`                                                                     |
| `--skip-list-detection`         | Пропустить обнаружение списков                                                          | `pdf2zh_next example.pdf --skip-list-detection`                                                                        |
| `--skip-code-detection`         | Пропустить обнаружение кода                                                             | `pdf2zh_next example.pdf --skip-code-detection`                                                                        |
| `--skip-quote-detection`        | Пропустить обнаружение цитат                                                            | `pdf2zh_next example.pdf --skip-quote-detection`                                                                       |
| `--skip-equation-detection`     | Пропустить обнаружение уравнений                                                        | `pdf2zh_next example.pdf --skip-equation-detection`                                                                    |
| `--skip-algorithm-detection`    | Пропустить обнаружение алгоритмов                                                       | `pdf2zh_next example.pdf --skip-algorithm-detection`                                                                   |
| `--skip-theorem-detection`      | Пропустить обнаружение теорем                                                           | `pdf2zh_next example.pdf --skip-theorem-detection`                                                                     |
| `--skip-proof-detection`        | Пропустить обнаружение доказательств                                                    | `pdf2zh_next example.pdf --skip-proof-detection`                                                                       |
| `--skip-definition-detection`   | Пропустить обнаружение определений                                                      | `pdf2zh_next example.pdf --skip-definition-detection`                                                                  |
| `--skip-example-detection`      | Пропустить обнаружение примеров                                                         | `pdf2zh_next example.pdf --skip-example-detection`                                                                     |
| `--skip-remark-detection`       | Пропустить обнаружение замечаний                                                        | `pdf2zh_next example.pdf --skip-remark-detection`                                                                      |
| `--skip-note-detection`         | Пропустить обнаружение примечаний                                                       | `pdf2zh_next example.pdf --skip-note-detection`                                                                        |
| `--skip-warning-detection`      | Пропустить обнаружение предупреждений                                                   | `pdf2zh_next example.pdf --skip-warning-detection`                                                                     |
| `--skip-error-detection`        | Пропустить обнаружение ошибок                                                           | `pdf2zh_next example.pdf --skip-error-detection`                                                                       |
| `--skip-info-detection`         | Пропустить обнаружение информации                                                       | `pdf2zh_next example.pdf --skip-info-detection`                                                                        |
| `--skip-tip-detection`          | Пропустить обнаружение советов                                                          | `pdf2zh_next example.pdf --skip-tip-detection`                                                                         |
| `--skip-success-detection`      | Пропустить обнаружение успешных операций                                                | `pdf2zh_next example.pdf --skip-success-detection`                                                                     |
| `--skip-question-detection`     | Пропустить обнаружение вопросов                                                         | `pdf2zh_next example.pdf --skip-question-detection`                                                                    |
| `--skip-caution-detection`      | Пропустить обнаружение предостережений                                                  | `pdf2zh_next example.pdf --skip-caution-detection`                                                                     |
| `--skip-important-detection`    | Пропустить обнаружение важных заметок                                                   | `pdf2zh_next example.pdf --skip-important-detection`                                                                   |
| `--skip-custom-detection`       | Пропустить пользовательское обнаружение                                                 | `pdf2zh_next example.pdf --skip-custom-detection`                                                                      |
| `--skip-all-detection`          | Пропустить все виды обнаружения                                                         | `pdf2zh_next example.pdf --skip-all-detection`                                                                         |
[Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `--ocr-workaround-threshold`    | Threshold (0 to 1) for OCR workaround, higher value means more text will be black       | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-threshold 0.5`                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--ocr-workaround-whiten-bg`    | Whether to whiten the background of the text box in OCR workaround, default is `true`   | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-whiten-bg false`                                           | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--ocr-workaround-whiten-fg`    | Whether to whiten the foreground (text) in OCR workaround, default is `false`           | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-whiten-fg true`                                            | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |

---

### TRANSLATED TEXT

| `--ocr-workaround`              | Принудительно делает переведенный текст черным и добавляет белый фон                     | `pdf2zh_next example.pdf --ocr-workaround`                                                                            | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `--ocr-workaround-threshold`    | Порог (от 0 до 1) для обходного решения OCR, более высокое значение означает, что больше текста будет черным | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-threshold 0.5`                                             | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--ocr-workaround-whiten-bg`    | Следует ли отбеливать фон текстового поля в обходном решении OCR, по умолчанию `true`   | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-whiten-bg false`                                           | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--ocr-workaround-whiten-fg`    | Следует ли отбеливать передний план (текст) в обходном решении OCR, по умолчанию `false` | `pdf2zh_next example.pdf --ocr-workaround --ocr-workaround-whiten-fg true`                                            | [Использование **Командной строки**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--disable-ocr-workaround`      | Disable OCR workaround. This will skip OCR processing even if the document is detected as heavily scanned. (default: False)              | `pdf2zh_next example.pdf --disable-ocr-workaround`                         |
| `--ocr-workaround-threshold`    | Set the threshold for OCR workaround. Documents with a scan score above this value will be considered heavily scanned. (default: 0.8)    | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.9`                   |

---

### TRANSLATION RESULT

| `--auto-enable-ocr-workaround`  | Включить автоматическое обходное решение OCR. Если документ определяется как сильно отсканированный, будет предпринята попытка включить обработку OCR и пропустить дальнейшее обнаружение сканирования. Подробности см. в документации. (по умолчанию: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--disable-ocr-workaround`      | Отключить обходное решение OCR. Это пропустит обработку OCR, даже если документ определяется как сильно отсканированный. (по умолчанию: False)                                                                                                              | `pdf2zh_next example.pdf --disable-ocr-workaround`                         |
| `--ocr-workaround-threshold`    | Установить порог для обходного решения OCR. Документы с оценкой сканирования выше этого значения будут считаться сильно отсканированными. (по умолчанию: 0.8)                                                                                               | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.9`                   |
| `--only-include-translated-page`| Включать в выходной PDF только переведённые страницы. Действует только при использовании --pages.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf2zh_next example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf2zh_next example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf2zh_next example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf2zh_next example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf2zh_next example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf2zh_next example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf2zh_next example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf2zh_next example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf2zh_next example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf2zh_next example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf2zh_next example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf2zh_next example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf2zh_next example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf2zh_next example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf2zh_next example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf2zh_next example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf2zh_next example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf 极速翻译 example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf 极速翻译 example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf 极速翻译 example.pdf --no-merge-极速翻译-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Disable merging of identical parentheses at the beginning and end of a paragraph               | `pdf 极速翻译 example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Disable merging of identical brackets at the beginning and end of a paragraph                  | `pdf 极速翻译 example.pdf --no-merge-identical-brackets`                                                      |
| `极速翻译`                            | Disable merging of identical quotation marks at the beginning and end of a paragraph           | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Disable merging of identical punctuation marks at the beginning and end of a paragraph         | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |

---

### TRANSLATION

| `--no-merge-alternating-line-numbers` | Отключает объединение чередующихся номеров строк и текстовых абзацев в документах с номерами строк | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf2zh_next example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-极速翻译-identical-brackets`                                                   |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example 极速翻译 --no-merge-identical-parenthesis`                                               |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example 极速翻译 --no-merge-identical-brackets`                                                  |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example 极速翻译 --no-merge-identical-quotation`                                                 |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example 极速翻译 --no-merge-identical-punctuation`                                               |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example 极速翻译 --no-merge-identical-parenthesis`                                               |
| `--no-merge-identical-b 极速翻译`      | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example 极速翻译 --no-merge-identical-brackets`                                                  |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example 极速翻译 --no-merge-identical-quotation`                                                 |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example 极速翻译 --no-merge-identical-punctuation`                                               |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example 极速翻译 --no-merge-identical-parenthesis`                                               |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example 极速翻译 --no-merge-identical-brackets`                                                  |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example 极速翻译 --no-merge-identical-quotation`                                                 |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-brackets`                                                      |
| `--no-merge-identical-quotation`      | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
| `--no-merge-identical-parenthesis`    | Отключает объединение одинаковых скобок в начале и конце абзаца                               | `pdf 极速翻译 example.pdf --no-merge-identical-parenthesis`                                                   |
| `--no-merge-identical-brackets`       | Отключает объединение одинаковых квадратных скобок в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-brackets`                                                      |
| `极速翻译`                            | Отключает объединение одинаковых кавычек в начале и конце абзаца                              | `pdf 极速翻译 example.pdf --no-merge-identical-quotation`                                                     |
| `--no-merge-identical-punctuation`    | Отключает объединение одинаковых знаков пунктуации в начале и конце абзаца                    | `pdf 极速翻译 example.pdf --no-merge-identical-punctuation`                                                   |
---

### OUTPUT

| `--no-remove-non-formula-lines` | Отключить удаление строк, не являющихся формулами, в областях абзацев                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
0.8   |
| `--formula-line-iou-threshold`     | Set IoU threshold for identifying formula lines (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                           | 0.8   |
| `--table-line-iou-threshold`       | Set IoU threshold for identifying table lines (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                             | 0.8   |
| `--remove-overlap`                 | Enable overlapping removal for text blocks                                        | `pdf2zh_next example.pdf --remove-overlap`                                                                            | false |
| `--overlap-threshold`              | Set IoU threshold for overlapping removal (0.0-1.0)                               | `pdf2zh_next example.pdf --overlap-threshold 0.5`                                                                     | 0.5   |

---

### OUTPUT

| `--non-formula-line-iou-threshold` | Установить порог IoU для идентификации строк без формул (0.0-1.0)                | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | 0.8   |
| `--formula-line-iou-threshold`     | Установить порог IoU для идентификации строк с формулами (0.0-1.0)               | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.85`                                                           | 0.8   |
| `--table-line-iou-threshold`       | Установить порог IoU для идентификации строк таблиц (0.0-1.0)                    | `pdf2zh_next example.pdf --table-line-iou-threshold 0.85`                                                             | 0.8   |
| `--remove-overlap`                 | Включить удаление перекрывающихся текстовых блоков                               | `pdf2zh_next example.pdf --remove-overlap`                                                                            | false |
| `--overlap-threshold`              | Установить порог IoU для удаления перекрытий (0.0-1.0)                           | `pdf2zh_next example.pdf --overlap-threshold 0.5`                                                                     | 0.5   |
`0.95` |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |

---

### OUTPUT

| `--figure-table-protection-threshold` | Установите порог защиты для рисунков и таблиц (0.0-1.0). Строки внутри рисунков/таблиц не будут обрабатываться | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        | `0.95` |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |
---

### OUTPUT

| `--skip-formula-offset-calculation` | Пропустить расчет смещения формул во время обработки          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### Аргументы GUI

| `--server_name <SERVER_NAME>`   | Set server name                        | `pdf2zh_next --gui --server_name 127.0.0.1`     |
| `--server_port <SERVER_PORT>`   | Set server port                        | `pdf2zh_next --gui --server_port 7860`          |
| `--concurrency_count <COUNT>`   | Set concurrency count                  | `pdf2zh_next --gui --concurrency_count 10`      |
| `--auth <USERNAME:PASSWORD>`    | Set username and password for the page | `pdf2zh_next --gui --auth user:password`        |
| `--auth_message <MESSAGE>`      | Set the message to display on the page | `pdf2zh_next --gui --auth_message "Welcome!"`   |
| `--ssl_keyfile <SSL_KEYFILE>`   | Set the path to the SSL key file       | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile <SSL_CERTFILE>` | Set the path to the SSL certificate    | `pdf2zh_next --gui --ssl_certfile cert.pem`     |

---

### OUTPUT

| Опция                          | Функция                               | Пример                                         |
| ------------------------------- | ------------------------------------- | ---------------------------------------------- |
| `--share`                       | Включить режим совместного использования | `pdf2zh_next --gui --share`                     |
| `--server_name <SERVER_NAME>`   | Установить имя сервера                | `pdf2zh_next --gui --server_name 127.0.0.1`     |
| `--server_port <SERVER_PORT>`   | Установить порт сервера               | `pdf2zh_next --gui --server_port 7860`          |
| `--concurrency_count <COUNT>`   | Установить количество одновременных подключений | `pdf2zh_next --gui --concurrency_count 10`      |
| `--auth <USERNAME:PASSWORD>`    | Установить имя пользователя и пароль для страницы | `pdf2zh_next --gui --auth user:password`        |
| `--auth_message <MESSAGE>`      | Установить сообщение для отображения на странице | `pdf2zh_next --gui --auth_message "Welcome!"`   |
| `--ssl_keyfile <SSL_KEYFILE>`   | Установить путь к файлу SSL-ключа     | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile <SSL_CERTFILE>` | Установить путь к SSL-сертификату     | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
`pdf2zh_next --gui --auth-file /path`           |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `--auth-type`                   | Authentication type                    | `pdf2zh_next --gui --auth-type basic`           | `pdf2zh_next --gui --auth-type basic`           |
| `--auth-username`               | Authentication username                | `pdf2zh_next --gui --auth-username user`        | `pdf2zh_next --gui --auth-username user`        |
| `--auth-password`               | Authentication password                | `pdf2zh_next --gui --auth-password pass`        | `pdf2zh_next --gui --auth-password pass`        |
| `--auth-token`                  | Authentication token                   | `pdf2zh_next --gui --auth-token token`          | `pdf2zh_next --gui --auth-token token`          |
| `--auth-token-type`             | Authentication token type             | `pdf2zh_next --gui --auth-token-type Bearer`    | `pdf2zh_next --gui --auth-token-type Bearer`    |
| `--auth-header-prefix`          | Authentication header prefix          | `pdf2zh_next --gui --auth-header-prefix Basic` | `pdf2zh_next --gui --auth-header-prefix Basic` |
| `--auth-custom-header`          | Custom authentication header          | `pdf2zh_next --gui --auth-custom-header X-API`  | `pdf2zh_next --gui --auth-custom-header X-API`  |
| `--auth-custom-header-value`    | Custom authentication header value    | `pdf2zh_next --gui --auth-custom-header-value`  | `pdf2zh_next --gui --auth-custom-header-value`  |
| `--auth-custom-query-param`     | Custom authentication query parameter | `pdf2zh_next --gui --auth-custom-query-param`   | `pdf2zh_next --gui --auth-custom-query-param`   |
| `--auth-custom-query-param-value` | Custom authentication query parameter value | `pdf2zh_next --gui --auth-custom-query-param-value` | `pdf2zh_next --gui --auth-custom-query-param-value` |

---

### TRANSLATION RESULT

| `--auth-file`                   | Путь к файлу аутентификации             | `pdf2zh_next --gui --auth-file /path`           | `pdf2zh_next --gui --auth-file /path`           |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `--auth-type`                   | Тип аутентификации                     | `pdf2zh_next --gui --auth-type basic`           | `pdf2zh_next --gui --auth-type basic`           |
| `--auth-username`               | Имя пользователя для аутентификации    | `pdf2zh_next --gui --auth-username user`        | `pdf2zh_next --gui --auth-username user`        |
| `--auth-password`               | Пароль для аутентификации              | `pdf2zh_next --gui --auth-password pass`        | `pdf2zh_next --gui --auth-password pass`        |
| `--auth-token`                  | Токен аутентификации                   | `pdf2zh_next --gui --auth-token token`          | `pdf2zh_next --gui --auth-token token`          |
| `--auth-token-type`             | Тип токена аутентификации              | `pdf2zh_next --gui --auth-token-type Bearer`    | `pdf2zh_next --gui --auth-token-type Bearer`    |
| `--auth-header-prefix`          | Префикс заголовка аутентификации       | `pdf2zh_next --gui --auth-header-prefix Basic` | `pdf2zh_next --gui --auth-header-prefix Basic` |
| `--auth-custom-header`          | Пользовательский заголовок аутентификации | `pdf2zh_next --gui --auth-custom-header X-API`  | `pdf2zh_next --gui --auth-custom-header X-API`  |
| `--auth-custom-header-value`    | Значение пользовательского заголовка аутентификации | `pdf2zh_next --gui --auth-custom-header-value`  | `pdf2zh_next --gui --auth-custom-header-value`  |
| `--auth-custom-query-param`     | Пользовательский параметр запроса аутентификации | `pdf2zh_next --gui --auth-custom-query-param`   | `pdf2zh_next --gui --auth-custom-query-param`   |
| `--auth-custom-query-param-value` | Значение пользовательского параметра запроса аутентификации | `pdf2zh_next --gui --auth-custom-query-param-value` | `pdf2zh_next --gui --auth-custom-query-param-value` |
Show the welcome page, and then the main window |

---

### OUTPUT

| `--welcome-page`                | Путь к HTML-файлу приветственной страницы          | `pdf2zh_next --gui --welcome-page /path`        | Показать приветственную страницу, а затем главное окно |
`Bing,OpenAI` |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Bing"`       | `Bing`        |
| `--service-order`               | Service order                          | `pdf2zh_next --gui --service-order "Bing,OpenAI"`    | `Bing,OpenAI` |
| `--custom-service-config`       | Custom service config                  | `pdf2zh_next --gui --custom-service-config "{}"`     | `{}`          |
| `--custom-service-config-file`  | Custom service config file             | `pdf2zh_next --gui --custom-service-config-file ""`  | `""`          |
| `--custom-service-config-files` | Custom service config files            | `pdf2zh_next --gui --custom-service-config-files ""` | `""`          |

---

### TRANSLATION RESULT

| `--enabled-services`            | Включенные службы перевода             | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | `Bing,OpenAI` |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ------------- |
| `--disabled-services`           | Отключенные службы перевода            | `pdf2zh_next --gui --disabled-services "Bing"`       | `Bing`        |
| `--service-order`               | Порядок служб                          | `pdf2zh_next --gui --service-order "Bing,OpenAI"`    | `Bing,OpenAI` |
| `--custom-service-config`       | Пользовательская конфигурация службы   | `pdf2zh_next --gui --custom-service-config "{}"`     | `{}`          |
| `--custom-service-config-file`  | Файл пользовательской конфигурации службы | `pdf2zh_next --gui --custom-service-config-file ""`  | `""`          |
| `--custom-service-config-files` | Файлы пользовательской конфигурации службы | `pdf2zh_next --gui --custom-service-config-files ""` | `""`          |
| `--disable-gui-sensitive-input` | Отключить чувствительный ввод GUI | `pdf2zh_next --gui --disable-gui-sensitive-input` |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--disable-auto-start-server`    | Disable auto start server              | `pdf2zh_next --gui --disable-auto-start-server` |

---

### OUTPUT

| `--disable-config-auto-save`    | Отключить автоматическое сохранение конфигурации | `pdf2zh_next --gui --disable-config-auto-save`  |
|---------------------------------|--------------------------------------------------|-------------------------------------------------|
| `--disable-auto-start-server`    | Отключить автоматический запуск сервера          | `pdf2zh_next --gui --disable-auto-start-server` |
`7860`         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | -------------- |
| `--server-name`                 | WebUI Host                             | `pdf2zh_next --gui --server-name 127.0.0.1`     | `127.0.0.1`    |
| `--share`                       | Share WebUI via public link            | `pdf2zh_next --gui --share`                     | `False`        |
| `--server-certfile`             | Certificate file path for HTTPS server | `pdf2zh_next --gui --server-certfile cert.pem`  | `None`         |
| `--server-keyfile`              | Key file path for HTTPS server         | `pdf2zh_next --gui --server-keyfile key.pem`    | `None`         |

---

### OUTPUT

| `--server-port`                 | Порт WebUI                             | `pdf2zh_next --gui --server-port 7860`          | `7860`         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | -------------- |
| `--server-name`                 | Хост WebUI                             | `pdf2zh_next --gui --server-name 127.0.0.1`     | `127.0.0.1`    |
| `--share`                       | Поделиться WebUI через публичную ссылку| `pdf2zh_next --gui --share`                     | `False`        |
| `--server-certfile`             | Путь к файлу сертификата для HTTPS сервера | `pdf2zh_next --gui --server-certfile cert.pem`  | `None`         |
| `--server-keyfile`              | Путь к файлу ключа для HTTPS сервера   | `pdf2zh_next --gui --server-keyfile key.pem`    | `None`         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--model`                       | Model name                             | `pdf2zh_next --model gpt-4o-mini`               |
| `--api-key`                     | API key                                | `pdf2zh_next --api-key sk-...`                  |
| `--api-base`                    | API base URL                           | `pdf2zh_next --api-base https://api.example.com` |
| `--proxy`                       | Proxy URL                              | `pdf2zh_next --proxy http://127.0.0.1:7890`     |
| `--concurrent`                  | Concurrent requests                    | `pdf2zh_next --concurrent 5`                    |
| `--timeout`                     | Request timeout (seconds)              | `pdf2zh_next --timeout 60`                      |
| `--retry`                       | Retry attempts                         | `pdf2zh_next --retry 3`                         |
| `--retry-delay`                 | Retry delay (seconds)                  | `pdf2zh_next --retry-delay 5`                   |
| `--max-tokens`                  | Max tokens per request                 | `pdf2zh_next --max-tokens 4096`                 |
| `--temperature`                 | Temperature                            | `pdf2zh_next --temperature 0.7`                 |
| `--top-p`                       | Top-p                                  | `pdf2zh_next --top-p 0.95`                      |
| `--frequency-penalty`           | Frequency penalty                      | `pdf2zh_next --frequency-penalty 0`             |
| `--presence-penalty`            | Presence penalty                       | `pdf2zh_next --presence-penalty 0`              |
| `--stop`                        | Stop sequences                         | `pdf2zh_next --stop "END" --stop "###"`         |
| `--batch-size`                  | Batch size                             | `pdf2zh_next --batch-size 10`                   |
| `--batch-delay`                 | Batch delay (seconds)                  | `pdf2zh_next --batch-delay 1`                   |
| `--output-dir`                  | Output directory                       | `pdf2zh_next --output-dir ./output`             |
| `--output-format`               | Output format                          | `pdf2zh_next --output-format markdown`          |
| `--output-filename`             | Output filename pattern                | `pdf2zh_next --output-filename "{title}.md"`    |
| `--output-encoding`             | Output encoding                        | `pdf2zh_next --output-encoding utf-8`          |
| `--output-overwrite`            | Overwrite existing files               | `pdf2zh_next --output-overwrite`                |
| `--output-keep-temp`            | Keep temporary files                   | `pdf2zh_next --output-keep-temp`                |
| `--log-level`                   | Log level                              | `pdf2zh_next --log-level info`                  |
| `--log-file`                    | Log file                               | `pdf2zh_next --log-file ./pdf2zh.log`           |
| `--config`                      | Config file                            | `pdf2zh_next --config ./config.toml`            |
| `--help`                        | Show help                              | `pdf2zh_next --help`                            |
| `--version`                     | Show version                           | `pdf2zh_next --version`                         |

---

### OUTPUT

| `--ui-lang`                     | Язык интерфейса                        | `pdf2zh_next --gui --ui-lang zh`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--model`                       | Название модели                        | `pdf2zh_next --model gpt-4o-mini`               |
| `--api-key`                     | API-ключ                               | `pdf2zh_next --api-key sk-...`                  |
| `--api-base`                    | Базовый URL API                        | `pdf2zh_next --api-base https://api.example.com` |
| `--proxy`                       | URL прокси                             | `pdf2zh_next --proxy http://127.0.0.1:7890`     |
| `--concurrent`                  | Количество одновременных запросов      | `pdf2zh_next --concurrent 5`                    |
| `--timeout`                     | Таймаут запроса (секунды)              | `pdf2zh_next --timeout 60`                      |
| `--retry`                       | Количество попыток повтора             | `pdf2zh_next --retry 3`                         |
| `--retry-delay`                 | Задержка повтора (секунды)             | `pdf2zh_next --retry-delay 5`                   |
| `--max-tokens`                  | Максимальное количество токенов на запрос | `pdf2zh_next --max-tokens 4096`                 |
| `--temperature`                 | Температура                            | `pdf2zh_next --temperature 0.7`                 |
| `--top-p`                       | Top-p                                  | `pdf2zh_next --top-p 0.95`                      |
| `--frequency-penalty`           | Штраф за частоту                       | `pdf2zh_next --frequency-penalty 0`             |
| `--presence-penalty`            | Штраф за присутствие                   | `pdf2zh_next --presence-penalty 0`              |
| `--stop`                        | Стоп-последовательности                | `pdf2zh_next --stop "END" --stop "###"`         |
| `--batch-size`                  | Размер пакета                          | `pdf2zh_next --batch-size 10`                   |
| `--batch-delay`                 | Задержка пакета (секунды)              | `pdf2zh_next --batch-delay 1`                   |
| `--output-dir`                  | Выходная директория                    | `pdf2zh_next --output-dir ./output`             |
| `--output-format`               | Формат вывода                          | `pdf2zh_next --output-format markdown`          |
| `--output-filename`             | Шаблон имени выходного файла           | `pdf2zh_next --output-filename "{title}.md"`    |
| `--output-encoding`             | Кодировка вывода                       | `pdf2zh_next --output-encoding utf-8`          |
| `--output-overwrite`            | Перезаписывать существующие файлы      | `pdf2zh_next --output-overwrite`                |
| `--output-keep-temp`            | Сохранять временные файлы              | `pdf2zh_next --output-keep-temp`                |
| `--log-level`                   | Уровень логирования                    | `pdf2zh_next --log-level info`                  |
| `--log-file`                    | Файл лога                              | `pdf2zh_next --log-file ./pdf2zh.log`           |
| `--config`                      | Файл конфигурации                      | `pdf2zh_next --config ./config.toml`            |
| `--help`                        | Показать справку                       | `pdf2zh_next --help`                            |
| `--version`                     | Показать версию                        | `pdf2zh_next --version`                         |

[⬆️ Наверх](#toc)

---

#### Руководство по настройке ограничения скорости

При использовании служб перевода правильная настройка ограничения скорости крайне важна для предотвращения ошибок API и оптимизации производительности. В этом руководстве объясняется, как настроить параметры `--qps` и `--pool-max-worker` в зависимости от ограничений различных вышестоящих служб.

> [!TIP]
>
> Рекомендуется, чтобы `pool_size` не превышал 1000. Если `pool_size`, рассчитанный следующим методом, превышает 1000, используйте 1000.

##### Ограничение скорости RPM (запросов в минуту)

Если вышестоящий сервис имеет ограничения RPM, используйте следующий расчет:

**Формула расчета:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Коэффициент 10 является эмпирическим и обычно хорошо работает в большинстве сценариев.

**Пример:**
Если ваша служба перевода имеет ограничение в 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Ограничение количества одновременных подключений

Если вышестоящий сервис имеет ограничения на количество одновременных подключений (например, официальный сервис GLM), используйте этот подход:

**Формула расчета:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Пример:**
Если ваша служба перевода позволяет 50 одновременных подключений:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Лучшие практики

> [!TIP]
> - Всегда начинайте с консервативных значений и постепенно увеличивайте их при необходимости
> - Мониторьте время отклика вашего сервиса и частоту ошибок
> - Разные сервисы могут требовать разных стратегий оптимизации
> - Учитывайте ваш конкретный случай использования и размер документа при настройке этих параметров


[⬆️ Наверх](#toc)

---

#### Частичный перевод

Используйте параметр `--pages` для перевода части документа.

- Если номера страниц идут подряд, можно записать это так:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` включает все страницы после 25-й. Если ваш документ содержит 100 страниц, это эквивалентно `25-100`.
> 
> Аналогично, `-25` включает все страницы до 25-й, что эквивалентно `1-25`.

- Если страницы не идут подряд, вы можете использовать запятую `,` для их разделения.

Например, если вы хотите перевести первую и третью страницы, вы можете использовать следующую команду:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Если страницы включают как последовательные, так и непоследовательные диапазоны, вы также можете соединить их запятой, например:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Эта команда переведет первую страницу, третью страницу, страницы с 10 по 20 и все страницы с 25 до конца.

[⬆️ Наверх](#toc)

---

#### Указание исходного и целевого языков

См. [Google Languages Codes](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL Languages Codes](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Наверх](#toc)

---

#### Перевод с исключениями

Используйте регулярные выражения для указания шрифтов формул и символов, которые необходимо сохранить:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Сохранять шрифты `Latex`, `Mono`, `Code`, `Italic`, `Symbol` и `Math` по умолчанию:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Наверх](#toc)

---

#### Пользовательский запрос

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Пользовательский системный запрос для перевода. В основном используется для добавления инструкции '/no_think' Qwen 3 в запрос.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Наверх](#toc)

---

#### Пользовательская конфигурация

Существует несколько способов изменения и импорта файла конфигурации.

> [!NOTE]
> **Иерархия файлов конфигурации**
>
> При изменении одного и того же параметра разными способами, программное обеспечение будет применять изменения в соответствии с указанным ниже порядком приоритета.
>
> Изменения с более высоким приоритетом переопределяют изменения с более низким приоритетом.
>
> **cli/gui > env > пользовательский файл конфигурации > файл конфигурации по умолчанию**

- Изменение конфигурации через **аргументы командной строки**

В большинстве случаев вы можете напрямую передать желаемые настройки через аргументы командной строки. Подробнее см. в разделе [Аргументы командной строки](#cmd).

Например, если вы хотите включить окно GUI, можно использовать следующую команду:

```bash
pdf2zh_next --gui
```

- Изменение конфигурации через **переменные среды**

Вы можете заменить `--` в аргументах командной строки на `PDF2ZH_`, соединять параметры с помощью `=`, а также заменять `-` на `_` в качестве переменных окружения.

Например, если вы хотите включить окно GUI, вы можете использовать следующую команду:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Пользовательский **Файл конфигурации**

Вы можете указать файл конфигурации, используя следующий аргумент командной строки:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Если вы не уверены в формате конфигурационного файла, обратитесь к стандартному конфигурационному файлу, описанному ниже.

- **Файл конфигурации по умолчанию**

Файл конфигурации по умолчанию находится в `~/.config/pdf2zh`.  
Пожалуйста, не изменяйте файлы конфигурации в каталоге `default`.  
Настоятельно рекомендуется ознакомиться с содержимым этого файла конфигурации и использовать **Пользовательскую конфигурацию** для реализации собственного файла конфигурации.

> [!TIP]
> - По умолчанию pdf2zh 2.0 автоматически сохраняет текущую конфигурацию в файл `~/.config/pdf2zh/config.v3.toml` каждый раз, когда вы нажимаете кнопку перевода в GUI. Этот файл конфигурации будет загружен по умолчанию при следующем запуске.
> - Файлы конфигурации в директории `default` автоматически генерируются программой. Вы можете скопировать их для внесения изменений, но, пожалуйста, не изменяйте их напрямую.
> - Файлы конфигурации могут включать номера версий, такие как "v2", "v3" и т.д. Это **номера версий файлов конфигурации**, а **не** номер версии самого pdf2zh.


[⬆️ Наверх](#toc)

---

#### Пропустить очистку

Когда этот параметр установлен в значение True, шаг очистки PDF будет пропущен, что может повысить совместимость и избежать некоторых проблем с обработкой шрифтов.

Использование:

```bash
pdf2zh_next example.pdf --skip-clean
```

Или использование переменных окружения:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Когда включен параметр `--enhance-compatibility`, автоматически активируется Пропустить очистку.

---

#### Кэш перевода

PDFMathTranslate кэширует переведенные тексты для увеличения скорости и избежания ненужных вызовов API для одинакового содержимого. Вы можете использовать опцию `--ignore-cache`, чтобы игнорировать кэш перевода и принудительно выполнить повторный перевод.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Наверх](#toc)

---

#### Развертывание в качестве общедоступных сервисов

При развертывании графического интерфейса pdf2zh в общедоступных сервисах вам следует изменить конфигурационный файл, как описано ниже.

> [!WARNING]
>
> Этот проект не проходил профессиональной проверки на безопасность и может содержать уязвимости. Пожалуйста, оцените риски и примите необходимые меры безопасности перед развертыванием в публичных сетях.


> [!TIP]
> - При публичном развертывании следует включить как `disable_gui_sensitive_input`, так и `disable_config_auto_save`.
> - Разделяйте различные доступные сервисы с помощью *английских запятых* <kbd>,</kbd>.

Вот пример рабочей конфигурации:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Наверх](#toc)

---

#### Аутентификация и приветственная страница

При использовании аутентификации и приветственной страницы для указания, какой пользователь может использовать Web UI и настройки страницы входа:

пример auth.txt
Каждая строка содержит два элемента: имя пользователя и пароль, разделенные запятой.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

пример welcome.html

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
> Приветственная страница будет работать, только если файл аутентификации не пуст.
> Если файл аутентификации пуст, аутентификация не будет выполняться. :)

Вот пример рабочей конфигурации:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Наверх](#toc)

---

#### Поддержка глоссария

PDFMathTranslate поддерживает таблицу глоссария. Файл таблицы глоссария должен быть в формате `csv`.
В файле три столбца. Вот демонстрационный файл глоссария:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | Автоматизированный ML  | ru   |
| a,a    | a       | ru   |
| "      | "       | ru   |


Для пользователей CLI:
Вы можете использовать несколько файлов для глоссария. Разные файлы должны быть разделены `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Для пользователей WebUI:

Теперь вы можете загрузить свой собственный файл глоссария. После загрузки файла вы можете проверить его, нажав на его имя, и содержимое отобразится ниже.

[⬆️ Наверх](#toc)

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>