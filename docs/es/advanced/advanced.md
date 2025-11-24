[**Opciones avanzadas**](./introduction.md) > **Opciones avanzadas** _(actual)_

---

<h3 id="toc">Tabla de Contenidos</h3>

- [Argumentos de línea de comandos](#argumentos-de-línea-de-comandos)
- [Guía de configuración de límite de tasa](#guía-de-configuración-de-límite-de-tasa)
- [Traducción parcial](#traducción-parcial)
- [Especificar idiomas de origen y destino](#especificar-idiomas-de-origen-y-destino)
- [Traducir con excepciones](#traducir-con-excepciones)
- [Prompt personalizado](#prompt-personalizado)
- [Configuración personalizada](#configuración-personalizada)
- [Omitir limpieza](#omitir-limpieza)
- [Caché de traducción](#caché-de-traducción)
- [Despliegue como servicio público](#despliegue-como-servicio-público)
- [Autenticación y página de bienvenida](#autenticación-y-página-de-bienvenida)
- [Soporte de glosario](#soporte-de-glosario)

---

#### Argumentos de la línea de comandos

Ejecuta el comando de traducción en la línea de comandos para generar el documento traducido `example-mono.pdf` y el documento bilingüe `example-dual.pdf` en el directorio de trabajo actual. Utiliza Google como el servicio de traducción predeterminado. Puedes encontrar más servicios de traducción soportados [AQUÍ](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

En la siguiente tabla, enumeramos todas las opciones avanzadas como referencia:

##### Argumentos

| `input-dir`                     | Input directory containing PDF files to process                                         | `pdf2zh_next -i ./pdfs`                                                                                               |
| `output-dir`                    | Output directory for translated PDFs                                                    | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `output-filename`               | Output filename (default: input filename + `_translated.pdf`)                           | `pdf2zh_next example.pdf --output-filename example_es.pdf`                                                             |
| `target-language`               | Target language code (default: `es`)                                                    | `pdf2zh_next example.pdf --target-language fr`                                                                        |
| `source-language`               | Source language code (default: `auto`)                                                  | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `translator`                    | Translation service (default: `google`)                                                 | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `translator-key`                | API key for translation service                                                         | `pdf2zh_next example.pdf --translator deepl --translator-key YOUR_DEEPL_API_KEY`                                       |
| `concurrency-limit`             | Maximum concurrent translation tasks (default: `5`)                                     | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `timeout`                       | Timeout for each translation request in seconds (default: `30`)                         | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `retry-attempts`                | Number of retry attempts for failed translations (default: `3`)                         | `pdf2zh_next example.pdf --retry-attempts 5`                                                                          |
| `retry-delay`                   | Delay between retry attempts in seconds (default: `2`)                                  | `pdf2zh_next example.pdf --retry-delay 5`                                                                             |
| `max-characters`                | Maximum characters per translation request (default: `5000`)                            | `pdf2zh_next example.pdf --max-characters 3000`                                                                       |
| `ocr`                           | Enable OCR for image-based PDFs (default: `false`)                                      | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `ocr-language`                  | Language for OCR (default: `auto`)                                                      | `pdf2zh_next example.pdf --ocr --ocr-language en`                                                                     |
| `ocr-whitelist`                 | Whitelist characters for OCR                                                            | `pdf2zh_next example.pdf --ocr --ocr-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`                                |
| `ocr-blacklist`                 | Blacklist characters for OCR                                                            | `pdf2zh_next example.pdf --ocr --ocr-blacklist "!@#$%^&*()"`                                                          |
| `font-family`                   | Font family for translated text (default: system default)                               | `pdf2zh_next example.pdf --font-family "Times New Roman"`                                                             |
| `font-size`                     | Font size for translated text (default: original font size)                             | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `font-color`                    | Font color for translated text (default: original font color)                           | `pdf2zh_next example.pdf --font-color "#FF0000"`                                                                      |
| `line-spacing`                  | Line spacing for translated text (default: original line spacing)                       | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `text-alignment`                | Text alignment for translated text (default: original alignment)                        | `pdf2zh_next example.pdf --text-alignment center`                                                                     |
| `preserve-formatting`           | Preserve original text formatting (default: `true`)                                     | `pdf2zh_next example.pdf --preserve-formatting false`                                                                 |
| `preserve-images`               | Preserve original images (default: `true`)                                              | `pdf2zh_next example.pdf --preserve-images false`                                                                     |
| `preserve-tables`               | Preserve original tables (default: `true`)                                              | `pdf2zh_next example.pdf --preserve-tables false`                                                                     |
| `preserve-links`                | Preserve original hyperlinks (default: `true`)                                          | `pdf2zh_next example.pdf --preserve-links false`                                                                      |
| `watermark`                     | Add watermark to translated PDF                                                         | `pdf2zh_next example.pdf --watermark "Translated by pdf2zh"`                                                          |
| `watermark-opacity`             | Watermark opacity (0-100, default: `20`)                                                | `pdf2zh_next example.pdf --watermark "Translated" --watermark-opacity 50`                                             |
| `watermark-font-size`           | Watermark font size (default: `48`)                                                     | `pdf2zh_next example.pdf --watermark "Translated" --watermark-font-size 24`                                           |
| `watermark-color`               | Watermark color (default: `#CCCCCC`)                                                    | `pdf2zh_next example.pdf --watermark "Translated" --watermark-color "#999999"`                                        |
| `watermark-rotation`            | Watermark rotation angle (default: `45`)                                                | `pdf2zh_next example.pdf --watermark "Translated" --watermark-rotation 30`                                            |
| `log-level`                     | Log level (`debug`, `info`, `warning`, `error`, `critical`, default: `info`)            | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `config`                        | Path to configuration file                                                              | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `version`                       | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `help`                          | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| Opción                          | Función                                                                                | Ejemplo                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Archivos PDF de entrada para procesar                                                   | `pdf2zh_next example.pdf`                                                                                             |
| `input-dir`                     | Directorio de entrada que contiene archivos PDF para procesar                           | `pdf2zh_next -i ./pdfs`                                                                                               |
| `output-dir`                    | Directorio de salida para los PDF traducidos                                            | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `output-filename`               | Nombre del archivo de salida (predeterminado: nombre del archivo de entrada + `_translated.pdf`) | `pdf2zh_next example.pdf --output-filename example_es.pdf`                                                             |
| `target-language`               | Código de idioma de destino (predeterminado: `es`)                                      | `pdf2zh_next example.pdf --target-language fr`                                                                        |
| `source-language`               | Código de idioma de origen (predeterminado: `auto`)                                     | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `translator`                    | Servicio de traducción (predeterminado: `google`)                                       | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `translator-key`                | Clave API para el servicio de traducción                                                | `pdf2zh_next example.pdf --translator deepl --translator-key YOUR_DEEPL_API_KEY`                                       |
| `concurrency-limit`             | Límite máximo de tareas de traducción concurrentes (predeterminado: `5`)                | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `timeout`                       | Tiempo de espera para cada solicitud de traducción en segundos (predeterminado: `30`)   | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `retry-attempts`                | Número de intentos de reintento para traducciones fallidas (predeterminado: `3`)        | `pdf2zh_next example.pdf --retry-attempts 5`                                                                          |
| `retry-delay`                   | Retraso entre intentos de reintento en segundos (predeterminado: `2`)                   | `pdf2zh_next example.pdf --retry-delay 5`                                                                             |
| `max-characters`                | Máximo de caracteres por solicitud de traducción (predeterminado: `5000`)               | `pdf2zh_next example.pdf --max-characters 3000`                                                                       |
| `ocr`                           | Habilitar OCR para PDF basados en imágenes (predeterminado: `false`)                    | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `ocr-language`                  | Idioma para OCR (predeterminado: `auto`)                                                | `pdf2zh_next example.pdf --ocr --ocr-language en`                                                                     |
| `ocr-whitelist`                 | Lista blanca de caracteres para OCR                                                     | `pdf2zh_next example.pdf --ocr --ocr-whitelist "0123456789abcdefghijklmnopqrstuvwxyz"`                                |
| `ocr-blacklist`                 | Lista negra de caracteres para OCR                                                      | `pdf2zh_next example.pdf --ocr --ocr-blacklist "!@#$%^&*()"`                                                          |
| `font-family`                   | Familia de fuentes para el texto traducido (predeterminado: predeterminado del sistema) | `pdf2zh_next example.pdf --font-family "Times New Roman"`                                                             |
| `font-size`                     | Tamaño de fuente para el texto traducido (predeterminado: tamaño de fuente original)    | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `font-color`                    | Color de fuente para el texto traducido (predeterminado: color de fuente original)      | `pdf2zh_next example.pdf --font-color "#FF0000"`                                                                      |
| `line-spacing`                  | Espaciado de línea para el texto traducido (predeterminado: espaciado de línea original)| `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `text-alignment`                | Alineación de texto para el texto traducido (predeterminado: alineación original)       | `pdf2zh_next example.pdf --text-alignment center`                                                                     |
| `preserve-formatting`           | Conservar el formato de texto original (predeterminado: `true`)                         | `pdf2zh_next example.pdf --preserve-formatting false`                                                                 |
| `preserve-images`               | Conservar las imágenes originales (predeterminado: `true`)                              | `pdf2zh_next example.pdf --preserve-images false`                                                                     |
| `preserve-tables`               | Conservar las tablas originales (predeterminado: `true`)                                | `pdf2zh_next example.pdf --preserve-tables false`                                                                     |
| `preserve-links`                | Conservar los hipervínculos originales (predeterminado: `true`)                         | `pdf2zh_next example.pdf --preserve-links false`                                                                      |
| `watermark`                     | Agregar marca de agua al PDF traducido                                                  | `pdf2zh_next example.pdf --watermark "Translated by pdf2zh"`                                                          |
| `watermark-opacity`             | Opacidad de la marca de agua (0-100, predeterminado: `20`)                              | `pdf2zh_next example.pdf --watermark "Translated" --watermark-opacity 50`                                             |
| `watermark-font-size`           | Tamaño de fuente de la marca de agua (predeterminado: `48`)                             | `pdf2zh_next example.pdf --watermark "Translated" --watermark-font-size 24`                                           |
| `watermark-color`               | Color de la marca de agua (predeterminado: `#CCCCCC`)                                   | `pdf2zh_next example.pdf --watermark "Translated" --watermark-color "#999999"`                                        |
| `watermark-rotation`            | Ángulo de rotación de la marca de agua (predeterminado: `45`)                           | `pdf2zh_next example.pdf --watermark "Translated" --watermark-rotation 30`                                            |
| `log-level`                     | Nivel de registro (`debug`, `info`, `warning`, `error`, `critical`, predeterminado: `info`) | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `config`                        | Ruta al archivo de configuración                                                        | `pdf2zh_next example.pdf --config ./config.json`                                                                      |
| `version`                       | Mostrar información de versión                                                          | `pdf2zh_next --version`                                                                                               |
| `help`                          | Mostrar mensaje de ayuda                                                                | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-name`                 | Output filename without extension                                                       | `pdf2zh_next example.pdf --output-name example_zh`                                                                    |
| `--output-format`               | Output format for translated files                                                      | `pdf2zh_next example.pdf --output-format docx`                                                                        |
| `--output-language`             | Output language code (see [Supported Languages](./SUPPORTED_LANGUAGES.md))              | `pdf2zh_next example.pdf --output-language ja`                                                                        |
| `--output-language`             | Output language code (see [Supported Languages](./SUPPORTED_LANGUAGES.md))              | `pdf2zh_next example.pdf --output-language ja`                                                                        |
| `--translator`                  | Translation service to use (see [Documentation of Translation Services](./TRANSLATORS.md)) | `pdf2zh_next example.pdf --translator google`                                                                         |

---

### OUTPUT

| `--output`                      | Directorio de salida para archivos                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--output-name`                 | Nombre de archivo de salida sin extensión                                                       | `pdf2zh_next example.pdf --output-name example_zh`                                                                    |
| `--output-format`               | Formato de salida para archivos traducidos                                                      | `pdf2zh_next example.pdf --output-format docx`                                                                        |
| `--output-language`             | Código de idioma de salida (ver [Idiomas soportados](./SUPPORTED_LANGUAGES.md))              | `pdf2zh_next example.pdf --output-language ja`                                                                        |
| `--output-language`             | Código de idioma de salida (ver [Idiomas soportados](./SUPPORTED_LANGUAGES.md))              | `pdf2zh_next example.pdf --output-language ja`                                                                        |
| `--translator`                  | Servicio de traducción a utilizar (ver [Documentación de servicios de traducción](./TRANSLATORS.md)) | `pdf2zh_next example.pdf --translator google`                                                                         |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-api-key`          | API key for the service.                                                               | `pdf2zh_next example.pdf --openai --openai-api-key sk-...`                                                            |
| `--<Services>-model`            | Model name for the service.                                                            | `pdf2zh_next example.pdf --openai --openai-model gpt-4o`                                                              |
| `--<Services>-api-base`         | API base URL for the service.                                                          | `pdf2zh_next example.pdf --openai --openai-api-base https://api.openai.com/v1`                                        |
| `--<Services>-prompt`           | Custom prompt for the service.                                                         | `pdf2zh_next example.pdf --openai --openai-prompt "Translate the following text into Chinese"`                        |
| `--<Services>-max-tokens`       | Maximum tokens for the service.                                                        | `pdf2zh_next example.pdf --openai --openai-max-tokens 4096`                                                           |
| `--<Services>-temperature`      | Temperature for the service.                                                           | `pdf2zh_next example.pdf --openai --openai-temperature 0.7`                                                           |
| `--<Services>-top-p`            | Top-p for the service.                                                                 | `pdf2zh_next example.pdf --openai --openai-top-p 0.9`                                                                 |
| `--<Services>-frequency-penalty`| Frequency penalty for the service.                                                     | `pdf2zh_next example.pdf --openai --openai-frequency-penalty 0.5`                                                     |
| `--<Services>-presence-penalty` | Presence penalty for the service.                                                      | `pdf2zh_next example.pdf --openai --openai-presence-penalty 0.5`                                                      |

---

### TRANSLATION RESULT

| `--<Services>`                  | Utilizar [**servicio específico**](./Documentation-of-Translation-Services.md) para la traducción | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-api-key`          | Clave de API para el servicio.                                                               | `pdf2zh_next example.pdf --openai --openai-api-key sk-...`                                                            |
| `--<Services>-model`            | Nombre del modelo para el servicio.                                                            | `pdf2zh_next example.pdf --openai --openai-model gpt-4o`                                                              |
| `--<Services>-api-base`         | URL base de la API para el servicio.                                                          | `pdf2zh_next example.pdf --openai --openai-api-base https://api.openai.com/v1`                                        |
| `--<Services>-prompt`           | Prompt personalizado para el servicio.                                                         | `pdf2zh_next example.pdf --openai --openai-prompt "Translate the following text into Chinese"`                        |
| `--<Services>-max-tokens`       | Tokens máximos para el servicio.                                                        | `pdf2zh_next example.pdf --openai --openai-max-tokens 4096`                                                           |
| `--<Services>-temperature`      | Temperatura para el servicio.                                                           | `pdf2zh_next example.pdf --openai --openai-temperature 0.7`                                                           |
| `--<Services>-top-p`            | Top-p para el servicio.                                                                 | `pdf2zh_next example.pdf --openai --openai-top-p 0.9`                                                                 |
| `--<Services>-frequency-penalty`| Penalización de frecuencia para el servicio.                                                     | `pdf2zh_next example.pdf --openai --openai-frequency-penalty 0.5`                                                     |
| `--<Services>-presence-penalty` | Penalización de presencia para el servicio.                                                      | `pdf2zh_next example.pdf --openai --openai-presence-penalty 0.5`                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i` <*input_path*>  | Input PDF file path                                                                     | `pdf2zh_next -i input.pdf` <br/> `pdf2zh_next -i /path/to/input.pdf`                                                  |
| `--output`, `-o` <*output_path*> | Output PDF file path                                                                    | `pdf2zh_next -i input.pdf -o output.pdf` <br/> `pdf2zh_next -i input.pdf -o /path/to/output.pdf`                      |
| `--lang`, `-l` <*language_code*> | Target language code, default is `zh` (Chinese)                                        | `pdf2zh_next -i input.pdf -l en` <br/> `pdf2zh_next -i input.pdf -l ja`                                               |
| `--config`, `-c` <*config_path*> | Configuration file path, default is `config.toml`                                      | `pdf2zh_next -i input.pdf -c config.toml` <br/> `pdf2zh_next -i input.pdf -c /path/to/config.toml`                    |
| `--list-languages`, `--ll`      | List all supported language codes and exit                                              | `pdf2zh_next --list-languages`                                                                                        |
| `--list-models`, `--lm`         | List all supported models and exit                                                      | `pdf2zh_next --list-models`                                                                                           |
| `--list-fonts`, `--lf`          | List all supported fonts and exit                                                       | `pdf2zh_next --list-fonts`                                                                                            |
| `--font`, `-f` <*font_name*>    | Font name, default is `Noto Sans CJK SC`                                               | `pdf2zh_next -i input.pdf -f "Noto Sans CJK SC"` <br/> `pdf2zh_next -i input.pdf -f "Source Han Serif CN"`             |
| `--model`, `-m` <*model_name*>  | Model name, default is `gpt-4o-mini`                                                   | `pdf2zh_next -i input.pdf -m "gpt-4o-mini"` <br/> `pdf2zh_next -i input.pdf -m "gpt-4o"`                              |
| `--use-cache`, `--uc`           | Use cache for translation, default is `true`                                           | `pdf2zh_next -i input.pdf --use-cache=false`                                                                          |
| `--cache-db`, `--cd` <*db_path*> | Cache database path, default is `cache.db`                                             | `pdf2zh_next -i input.pdf --cache-db custom_cache.db` <br/> `pdf2zh_next -i input.pdf --cache-db /path/to/cache.db`   |
| `--workers`, `-w` <*num*>       | Number of workers for translation, default is `4`                                      | `pdf2zh_next -i input.pdf -w 8`                                                                                       |
| `--batch-size`, `-b` <*num*>    | Batch size for translation, default is `10`                                            | `pdf2zh_next -i input.pdf -b 20`                                                                                      |
| `--timeout`, `-t` <*seconds*>   | Timeout for each translation request in seconds, default is `60`                       | `pdf2zh_next -i input.pdf -t 120`                                                                                     |
| `--max-retries`, `-r` <*num*>   | Maximum retries for each translation request, default is `3`                           | `pdf2zh_next -i input.pdf -r 5`                                                                                       |
| `--api-key` <*api_key*>         | API key for translation service, if not set, will use the one in config file or environment variable | `pdf2zh_next -i input.pdf --api-key sk-xxxxxx`                                                                        |
| `--api-base` <*api_base*>       | API base URL for translation service, if not set, will use the one in config file or environment variable | `pdf2zh_next -i input.pdf --api-base https://api.example.com`                                                         |
| `--dry-run`, `--dr`             | Dry run, only show the translation plan without actually translating                   | `pdf2zh_next -i input.pdf --dry-run`                                                                                  |
| `--verbose`, `-V`               | Verbose output, show more details                                                      | `pdf2zh_next -i input.pdf --verbose`                                                                                  |
| `--quiet`, `-q`                 | Quiet mode, only show errors and warnings                                              | `pdf2zh_next -i input.pdf --quiet`                                                                                    |

---

### TRANSLATED TEXT

| `--help`, `-h`                  | Mostrar mensaje de ayuda y salir                                                       | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Mostrar versión y salir                                                                 | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i` <*ruta_entrada*> | Ruta del archivo PDF de entrada                                                         | `pdf2zh_next -i input.pdf` <br/> `pdf2zh_next -i /ruta/a/entrada.pdf`                                                 |
| `--output`, `-o` <*ruta_salida*> | Ruta del archivo PDF de salida                                                          | `pdf2zh_next -i input.pdf -o output.pdf` <br/> `pdf2zh_next -i input.pdf -o /ruta/a/salida.pdf`                       |
| `--lang`, `-l` <*código_idioma*> | Código de idioma de destino, por defecto es `zh` (chino)                                | `pdf2zh_next -i input.pdf -l en` <br/> `pdf2zh_next -i input.pdf -l ja`                                               |
| `--config`, `-c` <*ruta_config*> | Ruta del archivo de configuración, por defecto es `config.toml`                         | `pdf2zh_next -i input.pdf -c config.toml` <br/> `pdf2zh_next -i input.pdf -c /ruta/a/config.toml`                     |
| `--list-languages`, `--ll`      | Listar todos los códigos de idioma soportados y salir                                   | `pdf2zh_next --list-languages`                                                                                        |
| `--list-models`, `--lm`         | Listar todos los modelos soportados y salir                                             | `pdf2zh_next --list-models`                                                                                           |
| `--list-fonts`, `--lf`          | Listar todas las fuentes soportadas y salir                                             | `pdf2zh_next --list-fonts`                                                                                            |
| `--font`, `-f` <*nombre_fuente*> | Nombre de la fuente, por defecto es `Noto Sans CJK SC`                                  | `pdf2zh_next -i input.pdf -f "Noto Sans CJK SC"` <br/> `pdf2zh_next -i input.pdf -f "Source Han Serif CN"`             |
| `--model`, `-m` <*nombre_modelo*> | Nombre del modelo, por defecto es `gpt-4o-mini`                                         | `pdf2zh_next -i input.pdf -m "gpt-4o-mini"` <br/> `pdf2zh_next -i input.pdf -m "gpt-4o"`                              |
| `--use-cache`, `--uc`           | Usar caché para la traducción, por defecto es `true`                                    | `pdf2zh_next -i input.pdf --use-cache=false`                                                                          |
| `--cache-db`, `--cd` <*ruta_bd*> | Ruta de la base de datos de caché, por defecto es `cache.db`                            | `pdf2zh_next -i input.pdf --cache-db custom_cache.db` <br/> `pdf2zh_next -i input.pdf --cache-db /ruta/a/cache.db`    |
| `--workers`, `-w` <*num*>       | Número de trabajadores para la traducción, por defecto es `4`                           | `pdf2zh_next -i input.pdf -w 8`                                                                                       |
| `--batch-size`, `-b` <*num*>    | Tamaño del lote para la traducción, por defecto es `10`                                 | `pdf2zh_next -i input.pdf -b 20`                                                                                      |
| `--timeout`, `-t` <*segundos*>  | Tiempo de espera para cada solicitud de traducción en segundos, por defecto es `60`     | `pdf2zh_next -i input.pdf -t 120`                                                                                     |
| `--max-retries`, `-r` <*num*>   | Intentos máximos para cada solicitud de traducción, por defecto es `3`                  | `pdf2zh_next -i input.pdf -r 5`                                                                                       |
| `--api-key` <*clave_api*>       | Clave API para el servicio de traducción, si no se establece, se usará la del archivo de configuración o variable de entorno | `pdf2zh_next -i input.pdf --api-key sk-xxxxxx`                                                                        |
| `--api-base` <*base_api*>       | URL base de la API para el servicio de traducción, si no se establece, se usará la del archivo de configuración o variable de entorno | `pdf2zh_next -i input.pdf --api-base https://api.example.com`                                                         |
| `--dry-run`, `--dr`             | Ejecución en seco, solo mostrar el plan de traducción sin traducir realmente            | `pdf2zh_next -i input.pdf --dry-run`                                                                                  |
| `--verbose`, `-V`               | Salida detallada, mostrar más detalles                                                  | `pdf2zh_next -i input.pdf --verbose`                                                                                  |
| `--quiet`, `-q`                 | Modo silencioso, solo mostrar errores y advertencias                                    | `pdf2zh_next -i input.pdf --quiet`                                                                                    |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`                  | Output directory for the translated files                                               | `pdf2zh_next --output-dir /path/to/output/`                                                                            |
| `--output-filename`             | Output filename for the translated files                                                | `pdf2zh_next --output-filename translated.pdf`                                                                         |
| `--output-format`               | Output format of the translated files, supports `pdf`, `text`, `html`, `markdown`       | `pdf2zh_next --output-format text`                                                                                     |
| `--output-language`             | Output language of the translated files, supports `zh`, `en`, `ja`, `ko`, and more      | `pdf2zh_next --output-language en`                                                                                     |
| `--output-encoding`             | Output encoding of the translated files, supports `utf-8`, `gbk`, `gb2312`, and more    | `pdf2zh_next --output-encoding gbk`                                                                                    |
| `--output-encoding-fallback`    | Fallback encoding for the output files                                                  | `pdf2zh_next --output-encoding-fallback gbk`                                                                           |
| `--output-encoding-error`       | Error handling for the output encoding, supports `strict`, `ignore`, `replace`          | `pdf2zh_next --output-encoding-error ignore`                                                                           |
| `--output-encoding-normalize`   | Normalize the output encoding                                                           | `pdf2zh_next --output-encoding-normalize`                                                                              |
| `--output-encoding-transcode`   | Transcode the output encoding                                                           | `pdf2zh_next --output-encoding-transcode`                                                                              |

---

### OUTPUT

| `--config-file`                 | Ruta al archivo de configuración                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| :------------------------------ | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--output-dir`                  | Directorio de salida para los archivos traducidos                                          | `pdf2zh_next --output-dir /path/to/output/`                                                                            |
| `--output-filename`             | Nombre de archivo de salida para los archivos traducidos                                    | `pdf2zh_next --output-filename translated.pdf`                                                                         |
| `--output-format`               | Formato de salida de los archivos traducidos, soporta `pdf`, `text`, `html`, `markdown`     | `pdf2zh_next --output-format text`                                                                                     |
| `--output-language`             | Idioma de salida de los archivos traducidos, soporta `zh`, `en`, `ja`, `ko`, y más          | `pdf2zh_next --output-language en`                                                                                     |
| `--output-encoding`             | Codificación de salida de los archivos traducidos, soporta `utf-8`, `gbk`, `gb2312`, y más  | `pdf2zh_next --output-encoding gbk`                                                                                    |
| `--output-encoding-fallback`    | Codificación de respaldo para los archivos de salida                                        | `pdf2zh_next --output-encoding-fallback gbk`                                                                           |
| `--output-encoding-error`       | Manejo de errores para la codificación de salida, soporta `strict`, `ignore`, `replace`     | `pdf2zh_next --output-encoding-error ignore`                                                                           |
| `--output-encoding-normalize`   | Normalizar la codificación de salida                                                       | `pdf2zh_next --output-encoding-normalize`                                                                              |
| `--output-encoding-transcode`   | Transcodificar la codificación de salida                                                    | `pdf2zh_next --output-encoding-transcode`                                                                              |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--report-interval`             | Intervalo de informe de progreso en segundos                                            | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--max-workers`                 | Maximum number of concurrent workers. Default is the number of CPU cores.               | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--max-workers`                 | Número máximo de trabajadores concurrentes. Por defecto, el número de núcleos de CPU.   | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--save-interval`               | Interval for saving progress in seconds. Default is 10.                                 | `pdf2zh_next example.pdf --save-interval 5`                                                                           |
| `--save-interval`               | Intervalo para guardar el progreso en segundos. Por defecto es 10.                      | `pdf2zh_next example.pdf --save-interval 5`                                                                           |
| `--ocr-request-timeout`         | Timeout for OCR requests in seconds. Default is 30.                                     | `pdf2zh_next example.pdf --ocr-request-timeout 60`                                                                    |
| `--ocr-request-timeout`         | Tiempo de espera para las solicitudes de OCR en segundos. Por defecto es 30.            | `pdf2zh_next example.pdf --ocr-request-timeout 60`                                                                    |
| `--ocr-request-max-retries`     | Maximum number of retries for OCR requests. Default is 3.                               | `pdf2zh_next example.pdf --ocr-request-max-retries 5`                                                                 |
| `--ocr-request-max-retries`     | Número máximo de reintentos para solicitudes de OCR. Por defecto es 3.                  | `pdf2zh_next example.pdf --ocr-request-max-retries 5`                                                                 |
| `--ocr-request-retry-delay`     | Delay between OCR request retries in seconds. Default is 1.                             | `pdf2zh_next example.pdf --ocr-request-retry-delay 2`                                                                 |
| `--ocr-request-retry-delay`     | Retraso entre reintentos de solicitud de OCR en segundos. Por defecto es 1.             | `pdf2zh_next example.pdf --ocr-request-retry-delay 2`                                                                 |
| `--ocr-request-concurrency`     | Maximum number of concurrent OCR requests. Default is 10.                               | `pdf2zh_next example.pdf --ocr-request-concurrency 20`                                                                |
| `--ocr-request-concurrency`     | Número máximo de solicitudes de OCR concurrentes. Por defecto es 10.                    | `pdf2zh_next example.pdf --ocr-request-concurrency 20`                                                                |
| `--ocr-queue-max-size`          | Maximum size of the OCR queue. Default is 1000.                                         | `pdf2zh_next example.pdf --ocr-queue-max-size 2000`                                                                   |
| `--ocr-queue-max-size`          | Tamaño máximo de la cola de OCR. Por defecto es 1000.                                   | `pdf2zh_next example.pdf --ocr-queue-max-size 2000`                                                                   |
| `--ocr-queue-put-timeout`       | Timeout for putting items in the OCR queue in seconds. Default is 5.                    | `pdf2zh_next example.pdf --ocr-queue-put-timeout 10`                                                                  |
| `--ocr-queue-put-timeout`       | Tiempo de espera para poner elementos en la cola de OCR en segundos. Por defecto es 5.  | `pdf2zh_next example.pdf --ocr-queue-put-timeout 10`                                                                  |
| `--ocr-queue-get-timeout`       | Timeout for getting items from the OCR queue in seconds. Default is 5.                  | `pdf2zh_next example.pdf --ocr-queue-get-timeout 10`                                                                  |
| `--ocr-queue-get-timeout`       | Tiempo de espera para obtener elementos de la cola de OCR en segundos. Por defecto es 5.| `pdf2zh_next example.pdf --ocr-queue-get-timeout 10`                                                                  |
| `--ocr-queue-empty-timeout`     | Timeout for waiting for the OCR queue to be empty in seconds. Default is 5.             | `pdf2zh_next example.pdf --ocr-queue-empty-timeout 10`                                                                |
| `--ocr-queue-empty-timeout`     | Tiempo de espera para que la cola de OCR esté vacía en segundos. Por defecto es 5.      | `pdf2zh_next example.pdf --ocr-queue-empty-timeout 10`                                                                |
| `--ocr-queue-full-timeout`      | Timeout for waiting for the OCR queue to be full in seconds. Default is 5.              | `pdf2zh_next example.pdf --ocr-queue-full-timeout 10`                                                                 |
| `--ocr-queue-full-timeout`      | Tiempo de espera para que la cola de OCR esté llena en segundos. Por defecto es 5.      | `pdf2zh_next example.pdf --ocr-queue-full-timeout 10`                                                                 |

---

### OUTPUT

| `--report-interval`             | Intervalo de informe de progreso en segundos                                            | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--max-workers`                 | Número máximo de trabajadores concurrentes. Por defecto, el número de núcleos de CPU.   | `pdf2zh_next example.pdf --max-workers 4`                                                                             |
| `--save-interval`               | Intervalo para guardar el progreso en segundos. Por defecto es 10.                      | `pdf2zh_next example.pdf --save-interval 5`                                                                           |
| `--ocr-request-timeout`         | Tiempo de espera para las solicitudes de OCR en segundos. Por defecto es 30.            | `pdf2zh_next example.pdf --ocr-request-timeout 60`                                                                    |
| `--ocr-request-max-retries`     | Número máximo de reintentos para solicitudes de OCR. Por defecto es 3.                  | `pdf2zh_next example.pdf --ocr-request-max-retries 5`                                                                 |
| `--ocr-request-retry-delay`     | Retraso entre reintentos de solicitud de OCR en segundos. Por defecto es 1.             | `pdf2zh_next example.pdf --ocr-request-retry-delay 2`                                                                 |
| `--ocr-request-concurrency`     | Número máximo de solicitudes de OCR concurrentes. Por defecto es 10.                    | `pdf2zh_next example.pdf --ocr-request-concurrency 20`                                                                |
| `--ocr-queue-max-size`          | Tamaño máximo de la cola de OCR. Por defecto es 1000.                                   | `pdf2zh_next example.pdf --ocr-queue-max-size 2000`                                                                   |
| `--ocr-queue-put-timeout`       | Tiempo de espera para poner elementos en la cola de OCR en segundos. Por defecto es 5.  | `pdf2zh_next example.pdf --ocr-queue-put-timeout 10`                                                                  |
| `--ocr-queue-get-timeout`       | Tiempo de espera para obtener elementos de la cola de OCR en segundos. Por defecto es 5.| `pdf2zh_next example.pdf --ocr-queue-get-timeout 10`                                                                  |
| `--ocr-queue-empty-timeout`     | Tiempo de espera para que la cola de OCR esté vacía en segundos. Por defecto es 5.      | `pdf2zh_next example.pdf --ocr-queue-empty-timeout 10`                                                                |
| `--ocr-queue-full-timeout`      | Tiempo de espera para que la cola de OCR esté llena en segundos. Por defecto es 5.      | `pdf2zh_next example.pdf --ocr-queue-full-timeout 10`                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-file LOG_FILE`           | Log file path                                                                           | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--log-level {debug,info,warn}` | Logging level                                                                           | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--debug`                       | Utilizar nivel de registro de depuración                                                | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--log-file LOG_FILE`           | Ruta del archivo de registro                                                            | `pdf2zh_next example.pdf --log-file log.txt`                                                                          |
| `--log-level {debug,info,warn}` | Nivel de registro                                                                       | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `-h`, `--help`                  | Mostrar mensaje de ayuda y salir                                                        | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--file`                        | The path of the file to be translated                                                   | `pdf2zh_next --file test.pdf`                                                                                         |
| `--to`                          | The language code of the target language                                                | `pdf2zh_next --file test.pdf --to es`                                                                                 |
| `--from`                        | The language code of the source language                                                | `pdf2zh_next --file test.pdf --from en --to es`                                                                       |
| `--translator`                  | The translator to use. See [Supported Languages](./SUPPORTED_LANG.md) for more details. | `pdf2zh_next --file test.pdf --translator google`                                                                     |
| `--model`                       | The model to use. See [Supported Languages](./SUPPORTED_LANG.md) for more details.      | `pdf2zh_next --file test.pdf --model gpt-3.5-turbo`                                                                   |
| `--key`                         | The API key for the translator                                                          | `pdf2zh_next --file test.pdf --translator google --key YOUR_API_KEY`                                                  |
| `--output`                      | The output file path                                                                    | `pdf2zh_next --file test.pdf --output translated.pdf`                                                                 |
| `--format`                      | The output format. Supported formats: `pdf`, `markdown`, `html`                         | `pdf2zh_next --file test.pdf --output translated.md --format markdown`                                                |
| `--timeout`                     | The timeout for the translation request in seconds                                      | `pdf2zh_next --file test.pdf --timeout 10`                                                                            |
| `--concurrency`                 | The number of concurrent translation requests                                           | `pdf2zh_next --file test.pdf --concurrency 5`                                                                         |
| `--retry`                       | The number of retries for failed translation requests                                   | `pdf2zh_next --file test.pdf --retry 3`                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                               |

---

### TRANSLATION

| `--gui`                         | Interactuar con la GUI                                                                  | `pdf2zh_next --gui`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--file`                        | La ruta del archivo a traducir                                                          | `pdf2zh_next --file test.pdf`                                                                                         |
| `--to`                          | El código de idioma del idioma de destino                                               | `pdf2zh_next --file test.pdf --to es`                                                                                 |
| `--from`                        | El código de idioma del idioma de origen                                                | `pdf2zh_next --file test.pdf --from en --to es`                                                                       |
| `--translator`                  | El traductor a utilizar. Consulta [Idiomas soportados](./SUPPORTED_LANG.md) para más detalles. | `pdf2zh_next --file test.pdf --translator google`                                                                     |
| `--model`                       | El modelo a utilizar. Consulta [Idiomas soportados](./SUPPORTED_LANG.md) para más detalles.  | `pdf2zh_next --file test.pdf --model gpt-3.5-turbo`                                                                   |
| `--key`                         | La clave API para el traductor                                                          | `pdf2zh_next --file test.pdf --translator google --key YOUR_API_KEY`                                                  |
| `--output`                      | La ruta del archivo de salida                                                           | `pdf2zh_next --file test.pdf --output translated.pdf`                                                                 |
| `--format`                      | El formato de salida. Formatos soportados: `pdf`, `markdown`, `html`                    | `pdf2zh_next --file test.pdf --output translated.md --format markdown`                                                |
| `--timeout`                     | El tiempo de espera para la solicitud de traducción en segundos                         | `pdf2zh_next --file test.pdf --timeout 10`                                                                            |
| `--concurrency`                 | El número de solicitudes de traducción concurrentes                                     | `pdf2zh_next --file test.pdf --concurrency 5`                                                                         |
| `--retry`                       | El número de reintentos para solicitudes de traducción fallidas                         | `pdf2zh_next --file test.pdf --retry 3`                                                                               |
| `--help`                        | Mostrar mensaje de ayuda y salir                                                        | `pdf2zh_next --help`                                                                                                  |
| `--version`                     | Mostrar versión y salir                                                                 | `pdf2zh_next --version`                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-cache`                    | Disable cache for translation service, will download models each time                   | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir <CACHE_DIR>`       | Specify cache directory for translation service                                         | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--target-language <LANG_CODE>` | Specify target language code, default is `zh` (Chinese)                                | `pdf2zh_next example.pdf --target-language en`                                                                        |
| `--source-language <LANG_CODE>` | Specify source language code, default is `auto` (auto detect)                          | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--engine <ENGINE>`             | Specify translation engine, default is `easyocr`                                       | `pdf2zh_next example.pdf --engine ocrspace`                                                                           |
| `--ocr <OCR>`                   | Specify OCR engine, default is `easyocr`                                               | `pdf2zh_next example.pdf --ocr paddleocr`                                                                             |
| `--translator <TRANSLATOR>`     | Specify translator engine, default is `argos`                                          | `pdf2zh_next example.pdf --translator libre`                                                                          |
| `--ocr-only`                    | Only perform OCR without translation                                                   | `pdf2zh_next example.pdf --ocr-only`                                                                                  |
| `--translator-only`             | Only perform translation without OCR (for text-only files)                             | `pdf2zh_next example.txt --translator-only`                                                                           |
| `--output <OUTPUT>`             | Specify output file path, default is `./output.pdf`                                    | `pdf2zh_next example.pdf --output ./result.pdf`                                                                       |
| `--format <FORMAT>`             | Specify output format, default is `pdf`, options: `pdf`, `txt`, `markdown`, `html`     | `pdf2zh_next example.pdf --format markdown`                                                                           |
| `--keep-original`               | Keep original text in output (for formats that support it)                             | `pdf2zh_next example.pdf --keep-original`                                                                             |
| `--threads <THREADS>`           | Number of threads to use, default is number of CPU cores                               | `pdf2zh_next example.pdf --threads 8`                                                                                 |
| `--batch-size <BATCH_SIZE>`     | Batch size for processing, default is 10                                               | `pdf2zh_next example.pdf --batch-size 5`                                                                              |
| `--timeout <TIMEOUT>`           | Timeout in seconds for each translation request, default is 30                         | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry <RETRY>`               | Number of retries for failed requests, default is 3                                    | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--log-level <LOG_LEVEL>`       | Log level, default is `INFO`, options: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--config <CONFIG>`             | Specify configuration file path                                                        | `pdf2zh_next example.pdf --config ./config.yaml`                                                                      |
| `--version`                     | Show version information                                                               | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message                                                                      | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--warmup`                      | Solo descargar y verificar los activos necesarios y luego salir                         | `pdf2zh_next example.pdf --warmup`                                                                                    |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--no-cache`                    | Deshabilitar caché para el servicio de traducción, descargará modelos cada vez         | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir <CACHE_DIR>`       | Especificar directorio de caché para el servicio de traducción                         | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `--target-language <LANG_CODE>` | Especificar el código de idioma de destino, por defecto es `zh` (chino)                | `pdf2zh_next example.pdf --target-language en`                                                                        |
| `--source-language <LANG_CODE>` | Especificar el código de idioma de origen, por defecto es `auto` (detección automática)| `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--engine <ENGINE>`             | Especificar el motor de traducción, por defecto es `easyocr`                           | `pdf2zh_next example.pdf --engine ocrspace`                                                                           |
| `--ocr <OCR>`                   | Especificar el motor OCR, por defecto es `easyocr`                                     | `pdf2zh_next example.pdf --ocr paddleocr`                                                                             |
| `--translator <TRANSLATOR>`     | Especificar el motor de traducción, por defecto es `argos`                             | `pdf2zh_next example.pdf --translator libre`                                                                          |
| `--ocr-only`                    | Solo realizar OCR sin traducción                                                       | `pdf2zh_next example.pdf --ocr-only`                                                                                  |
| `--translator-only`             | Solo realizar traducción sin OCR (para archivos solo de texto)                         | `pdf2zh_next example.txt --translator-only`                                                                           |
| `--output <OUTPUT>`             | Especificar la ruta del archivo de salida, por defecto es `./output.pdf`               | `pdf2zh_next example.pdf --output ./result.pdf`                                                                       |
| `--format <FORMAT>`             | Especificar el formato de salida, por defecto es `pdf`, opciones: `pdf`, `txt`, `markdown`, `html` | `pdf2zh_next example.pdf --format markdown`                                                                  |
| `--keep-original`               | Mantener el texto original en la salida (para formatos que lo soporten)                | `pdf2zh_next example.pdf --keep-original`                                                                             |
| `--threads <THREADS>`           | Número de hilos a usar, por defecto es el número de núcleos de CPU                     | `pdf2zh_next example.pdf --threads 8`                                                                                 |
| `--batch-size <BATCH_SIZE>`     | Tamaño del lote para procesamiento, por defecto es 10                                  | `pdf2zh_next example.pdf --batch-size 5`                                                                              |
| `--timeout <TIMEOUT>`           | Tiempo de espera en segundos para cada solicitud de traducción, por defecto es 30      | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry <RETRY>`               | Número de reintentos para solicitudes fallidas, por defecto es 3                       | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--log-level <LOG_LEVEL>`       | Nivel de registro, por defecto es `INFO`, opciones: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` | `pdf2zh_next example.pdf --log-level DEBUG`                                                                |
| `--config <CONFIG>`             | Especificar la ruta del archivo de configuración                                       | `pdf2zh_next example.pdf --config ./config.yaml`                                                                      |
| `--version`                     | Mostrar información de versión                                                        | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Mostrar mensaje de ayuda                                                              | `pdf2zh_next --help`                                                                                                  |
`pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| `--offline-assets-path`         | Use offline assets package from the specified directory                                  | `pdf2zh_next example.pdf --offline-assets-path /path`                                                                 | `pdf2zh_next example.pdf --offline-assets-path /path`                                                                 |
| `--offline-mode`                | Enable offline mode                                                                      | `pdf2zh_next example.pdf --offline-mode`                                                                              | `pdf2zh_next example.pdf --offline-mode`                                                                              |
| `--proxy`                       | Set proxy for network requests                                                           | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--proxy-type`                  | Set proxy type for network requests                                                      | `pdf2zh_next example.pdf --proxy-type socks5`                                                                         | `pdf2zh_next example.pdf --proxy-type socks5`                                                                         |
| `--retry-count`                 | Set retry count for network requests                                                     | `pdf2zh_next example.pdf --retry-count 5`                                                                             | `pdf2zh_next example.pdf --retry-count 5`                                                                             |
| `--retry-delay`                 | Set retry delay for network requests (in milliseconds)                                   | `pdf2zh_next example.pdf --retry-delay 1000`                                                                          | `pdf2zh_next example.pdf --retry-delay 1000`                                                                          |
| `--timeout`                     | Set timeout for network requests (in milliseconds)                                        | `pdf2zh_next example.pdf --timeout 30000`                                                                             | `pdf2zh_next example.pdf --timeout 30000`                                                                             |
| `--user-agent`                  | Set user agent for network requests                                                      | `pdf2zh_next example.pdf --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"`                                     | `pdf2zh_next example.pdf --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"`                                     |
| `--verbose`                     | Enable verbose output                                                                    | `pdf2zh_next example.pdf --verbose`                                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | Show version number                                                                      | `pdf2zh_next --version`                                                                                               | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help                                                                                | `pdf2zh_next --help`                                                                                                  | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--generate-offline-assets`     | Generar paquete de recursos sin conexión en el directorio especificado                  | `pdf2zh_next example.pdf --generate-offline-assets /ruta`                                                             | `pdf2zh_next example.pdf --generate-offline-assets /ruta`                                                             |
| `--offline-assets-path`         | Usar paquete de recursos sin conexión del directorio especificado                        | `pdf2zh_next example.pdf --offline-assets-path /ruta`                                                                 | `pdf2zh_next example.pdf --offline-assets-path /ruta`                                                                 |
| `--offline-mode`                | Habilitar modo sin conexión                                                              | `pdf2zh_next example.pdf --offline-mode`                                                                              | `pdf2zh_next example.pdf --offline-mode`                                                                              |
| `--proxy`                       | Establecer proxy para solicitudes de red                                                 | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--proxy-type`                  | Establecer tipo de proxy para solicitudes de red                                         | `pdf2zh_next example.pdf --proxy-type socks5`                                                                         | `pdf2zh_next example.pdf --proxy-type socks5`                                                                         |
| `--retry-count`                 | Establecer número de reintentos para solicitudes de red                                  | `pdf2zh_next example.pdf --retry-count 5`                                                                             | `pdf2zh_next example.pdf --retry-count 5`                                                                             |
| `--retry-delay`                 | Establecer retraso de reintento para solicitudes de red (en milisegundos)                | `pdf2zh_next example.pdf --retry-delay 1000`                                                                          | `pdf2zh_next example.pdf --retry-delay 1000`                                                                          |
| `--timeout`                     | Establecer tiempo de espera para solicitudes de red (en milisegundos)                    | `pdf2zh_next example.pdf --timeout 30000`                                                                             | `pdf2zh_next example.pdf --timeout 30000`                                                                             |
| `--user-agent`                  | Establecer agente de usuario para solicitudes de red                                     | `pdf2zh_next example.pdf --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"`                                     | `pdf2zh_next example.pdf --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"`                                     |
| `--verbose`                     | Habilitar salida detallada                                                               | `pdf2zh_next example.pdf --verbose`                                                                                   | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--version`                     | Mostrar número de versión                                                                | `pdf2zh_next --version`                                                                                               | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Mostrar ayuda                                                                            | `pdf2zh_next --help`                                                                                                  | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--use-offline-assets`          | Use the offline assets package from the specified directory                             | `pdf2zh_next example.pdf --use-offline-assets /path`                                                                  |

---

### OUTPUT

| `--restore-offline-assets`      | Restaurar el paquete de recursos sin conexión desde el directorio especificado          | `pdf2zh_next example.pdf --restore-offline-assets /ruta`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--use-offline-assets`          | Usar el paquete de recursos sin conexión desde el directorio especificado               | `pdf2zh_next example.pdf --use-offline-assets /ruta`                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-h`<br/>`--help`               | Show help message then exit                                                             | `pdf2zh_next -h`<br/>`pdf2zh_next --help`                                                                            |
| `-v`<br/>`--verbose`            | Enable verbose logging                                                                  | `pdf2zh_next -v`<br/>`pdf2zh_next --verbose`                                                                         |
| `-d`<br/>`--debug`              | Enable debug logging                                                                    | `pdf2zh_next -d`<br/>`pdf2zh_next --debug`                                                                           |
| `-n`<br/>`--dry-run`            | Perform a trial run with no changes made                                                | `pdf2zh_next -n`<br/>`pdf2zh_next --dry-run`                                                                         |
| `--cache`                       | Enable caching for faster processing on repeated runs                                   | `pdf2zh_next --cache`                                                                                                 |
| `--no-cache`                    | Disable caching                                                                         | `pdf2zh_next --no-cache`                                                                                              |
| `--cache-dir <directory>`       | Specify the cache directory                                                             | `pdf2zh_next --cache-dir ./my_cache`                                                                                  |
| `--clear-cache`                 | Clear the cache directory                                                               | `pdf2zh_next --clear-cache`                                                                                           |

---

### OUTPUT

| `--version`                     | Mostrar versión y salir                                                                  | `pdf2zh_next --version`                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `-h`<br/>`--help`               | Mostrar mensaje de ayuda y salir                                                        | `pdf2zh_next -h`<br/>`pdf2zh_next --help`                                                                            |
| `-v`<br/>`--verbose`            | Habilitar registro detallado                                                            | `pdf2zh_next -v`<br/>`pdf2zh_next --verbose`                                                                         |
| `-d`<br/>`--debug`              | Habilitar registro de depuración                                                        | `pdf2zh_next -d`<br/>`pdf2zh_next --debug`                                                                           |
| `-n`<br/>`--dry-run`            | Realizar una ejecución de prueba sin realizar cambios                                   | `pdf2zh_next -n`<br/>`pdf2zh_next --dry-run`                                                                         |
| `--cache`                       | Habilitar caché para un procesamiento más rápido en ejecuciones repetidas               | `pdf2zh_next --cache`                                                                                                 |
| `--no-cache`                    | Deshabilitar caché                                                                      | `pdf2zh_next --no-cache`                                                                                              |
| `--cache-dir <directory>`       | Especificar el directorio de caché                                                      | `pdf2zh_next --cache-dir ./my_cache`                                                                                  |
| `--clear-cache`                 | Limpiar el directorio de caché                                                          | `pdf2zh_next --clear-cache`                                                                                           |
[Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--model`                       | Specify the translation model                                                           | `pdf2zh_next example.pdf --model gpt-4o-mini`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--target-language`             | Specify the target language                                                             | `pdf2zh_next example.pdf --target-language ja`                                                                         | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--source-language`             | Specify the source language                                                             | `pdf2zh_next example.pdf --source-language en`                                                                         | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--translate-method`            | Specify the translation method                                                          | `pdf2zh_next example.pdf --translate-method gpt-4o-mini`                                                               | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--translation-service`         | Specify the translation service                                                         | `pdf2zh_next example.pdf --translation-service openai`                                                                 | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--api-key`                     | Specify the API key for the translation service                                         | `pdf2zh_next example.pdf --api-key sk-...`                                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--output-dir`                  | Specify the output directory                                                            | `pdf2zh_next example.pdf --output-dir ./output`                                                                        | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--output-filename`             | Specify the output filename                                                             | `pdf2zh_next example.pdf --output-filename example_zh.pdf`                                                             | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--output-format`               | Specify the output format                                                               | `pdf2zh_next example.pdf --output-format pdf`                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--proxy`                       | Specify the proxy server                                                                | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--force`                       | Force overwrite existing files                                                          | `pdf2zh_next example.pdf --force`                                                                                      | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--debug`                       | Enable debug mode                                                                       | `pdf2zh_next example.pdf --debug`                                                                                      | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--verbose`                     | Enable verbose mode                                                                     | `pdf2zh_next example.pdf --verbose`                                                                                    | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--config`                      | Specify a configuration file                                                            | `pdf2zh_next example.pdf --config config.json`                                                                         | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                                | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--help`                        | Show help information                                                                   | `pdf2zh_next --help`                                                                                                   | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-languages`              | List all supported languages                                                            | `pdf2zh_next --list-languages`                                                                                         | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-services`               | List all supported translation services                                                 | `pdf2zh_next --list-services`                                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-models`                 | List all supported models for a translation service                                     | `pdf2zh_next --list-models openai`                                                                                     | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-methods`                | List all supported translation methods                                                  | `pdf2zh_next --list-methods`                                                                                           | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-formats`                | List all supported output formats                                                       | `pdf2zh_next --list-formats`                                                                                           | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-options`                | List all available options                                                              | `pdf2zh_next --list-options`                                                                                           | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-commands`               | List all available commands                                                             | `pdf2zh_next --list-commands`                                                                                          | [Using **Command Line**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |

---

### OUTPUT

| `--pages`                       | Traducción parcial del documento                                                       | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `--model`                       | Especificar el modelo de traducción                                                     | `pdf2zh_next example.pdf --model gpt-4o-mini`                                                                          | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--target-language`             | Especificar el idioma de destino                                                        | `pdf2zh_next example.pdf --target-language ja`                                                                         | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--source-language`             | Especificar el idioma de origen                                                         | `pdf2zh_next example.pdf --source-language en`                                                                         | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--translate-method`            | Especificar el método de traducción                                                     | `pdf2zh_next example.pdf --translate-method gpt-4o-mini`                                                               | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--translation-service`         | Especificar el servicio de traducción                                                   | `pdf2zh_next example.pdf --translation-service openai`                                                                 | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--api-key`                     | Especificar la clave API para el servicio de traducción                                 | `pdf2zh_next example.pdf --api-key sk-...`                                                                             | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--output-dir`                  | Especificar el directorio de salida                                                     | `pdf2zh_next example.pdf --output-dir ./output`                                                                        | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--output-filename`             | Especificar el nombre del archivo de salida                                             | `pdf2zh_next example.pdf --output-filename example_zh.pdf`                                                             | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--output-format`               | Especificar el formato de salida                                                        | `pdf 极 2zh_next example.pdf --output-format pdf`                                                                          | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--proxy`                       | Especificar el servidor proxy                                                           | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | [Uso de **Línea de comandos**](https://pdf2 极 zh-next.com/getting-started/USAGE_command_line.html) |
| `--force`                       | Forzar la sobrescritura de archivos existentes                                          | `pdf2zh_next example.pdf --force`                                                                                      | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--debug`                       | Habilitar modo de depuración                                                            | `pdf2zh_next example 极.pdf --debug`                                                                                      | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--verbose`                     | Habilitar modo detallado                                                                | `pdf2zh_next example.pdf --verbose`                                                                                    | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--config`                      | Especificar un archivo de configuración                                                 | `pdf2zh_next example.pdf --config config.json`                                                                         | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--version`                     | Mostrar información de versión                                                          | `pdf2zh_next --version`                                                                                                | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--help`                        | Mostrar información de ayuda                                                            | `pdf2zh_next --help`                                                                                                   | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-languages`              | Listar todos los idiomas soportados                                                     | `pdf2zh_next --list-languages`                                                                                         | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-services`               | Listar todos los servicios de traducción soportados                                     | `pdf2zh_next --list-services`                                                                                          | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command 极_line.html) |
| `--list-models`                 | Listar todos los modelos soportados para un servicio de traducción                      | `pdf2zh_next --list-models openai`                                                                                     | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-methods`                | Listar todos los métodos de traducción soportados                                       | `pdf2zh_next --list-methods`                                                                                           | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-formats`                | Listar todos los formatos de salida soportados                                          | `pdf2zh_next --list-formats`                                                                                           | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-options`                | Listar todas las opciones disponibles                                                   | `pdf2zh_next --list-options`                                                                                           | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| `--list-commands`               | Listar todos los comandos disponibles                                                   | `pdf2zh_next --list-commands`                                                                                          | [Uso de **Línea de comandos**](https://pdf2zh-next.com/getting-started/USAGE_command_line.html) |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out es`                                                                                |
| `--translator`                  | Translation service to use                                                              | `pdf2zh_next example.pdf --translator google`                                                                          |
| `-c`<br/>`--cache-dir`          | Cache directory for translated segments                                                 | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          |
| `-o`<br/>`--output`             | Output file path                                                                        | `pdf2zh_next example.pdf -o example_es.pdf`                                                                            |
| `--no-cache`                    | Disable cache                                                                           | `pdf2zh_next example.pdf --no-cache`                                                                                   |
| `--force-retranslate`           | Force retranslate all segments                                                          | `pdf2zh_next example.pdf --force-retranslate`                                                                          |
| `--no-save-cache`               | Do not save cache                                                                       | `pdf2zh_next example.pdf --no-save-cache`                                                                              |
| `--config`                      | Path to configuration file                                                              | `pdf2zh_next example.pdf --config config.json`                                                                         |
| `--translator-config`           | Path to translator-specific configuration file                                          | `pdf2zh_next example.pdf --translator-config google_config.json`                                                        |
| `--debug`                       | Enable debug mode                                                                       | `pdf2zh_next example.pdf --debug`                                                                                      |
| `-v`<br/>`--version`            | Show version information                                                                | `pdf2zh_next --version`                                                                                                |
| `-h`<br/>`--help`               | Show help message                                                                       | `pdf2zh_next --help`                                                                                                   |

---

### TRANSLATION

| `--lang-in`                     | Código del idioma de origen                                                             | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Código del idioma de destino                                                            | `pdf2zh_next example.pdf --lang-out es`                                                                                |
| `--translator`                  | Servicio de traducción a utilizar                                                       | `pdf2zh_next example.pdf --translator google`                                                                          |
| `-c`<br/>`--cache-dir`          | Directorio de caché para segmentos traducidos                                           | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                          |
| `-o`<br/>`--output`             | Ruta del archivo de salida                                                              | `pdf2zh_next example.pdf -o example_es.pdf`                                                                            |
| `--no-cache`                    | Deshabilitar caché                                                                      | `pdf2zh_next example.pdf --no-cache`                                                                                   |
| `--force-retranslate`           | Forzar la retraducción de todos los segmentos                                           | `pdf2zh_next example.pdf --force-retranslate`                                                                          |
| `--no-save-cache`               | No guardar caché                                                                        | `pdf2zh_next example.pdf --no-save-cache`                                                                              |
| `--config`                      | Ruta al archivo de configuración                                                        | `pdf2zh_next example.pdf --config config.json`                                                                         |
| `--translator-config`           | Ruta al archivo de configuración específico del traductor                               | `pdf2zh_next example.pdf --translator-config google_config.json`                                                        |
| `--debug`                       | Habilitar modo de depuración                                                            | `pdf2zh_next example.pdf --debug`                                                                                      |
| `-v`<br/>`--version`            | Mostrar información de versión                                                          | `pdf2zh_next --version`                                                                                                |
| `-h`<br/>`--help`               | Mostrar mensaje de ayuda                                                                | `pdf2zh_next --help`                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | Source language code                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| `--translator`                  | Translation service to use                                                               | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-config`           | Configuration for the translation service                                                | `pdf2zh_next example.pdf --translator-config '{"api_key": "your_api_key"}'`                                           |
| `--translator-config-file`      | Path to a JSON file containing configuration for the translation service                 | `pdf2zh_next example.pdf --translator-config-file config.json`                                                        |
| `--translator-retry-attempts`   | Number of retry attempts for translation requests                                        | `pdf2zh_next example.pdf --translator-retry-attempts 3`                                                               |
| `--translator-retry-delay`      | Delay between retry attempts in milliseconds                                            | `pdf2zh_next example.pdf --translator-retry-delay 1000`                                                               |
| `--translator-timeout`          | Timeout for translation requests in milliseconds                                         | `pdf2zh_next example.pdf --translator-timeout 5000`                                                                   |
| `--translator-fallback`         | Fallback translation service to use if the primary fails                                 | `pdf2zh_next example.pdf --translator-fallback microsoft`                                                             |
| `--translator-fallback-config`  | Configuration for the fallback translation service                                       | `pdf2zh_next example.pdf --translator-fallback-config '{"api_key": "your_fallback_api_key"}'`                         |
| `--translator-fallback-config-file` | Path to a JSON file containing configuration for the fallback translation service        | `pdf2zh_next example.pdf --translator-fallback-config-file fallback_config.json`                                     |
| `--translator-fallback-retry-attempts` | Number of retry attempts for fallback translation requests                               | `pdf2zh_next example.pdf --translator-fallback-retry-attempts 3`                                                      |
| `--translator-fallback-retry-delay` | Delay between fallback retry attempts in milliseconds                                   | `pdf2zh_next example.pdf --translator-fallback-retry-delay 1000`                                                      |
| `--translator-fallback-timeout` | Timeout for fallback translation requests in milliseconds                                | `pdf2zh_next example.pdf --translator-fallback-timeout 5000`                                                          |
| `--translator-fallback-on-error` | Whether to use fallback translator on error (true/false)                                | `pdf2zh_next example.pdf --translator-fallback-on-error true`                                                         |
| `--translator-fallback-on-empty` | Whether to use fallback translator on empty response (true/false)                       | `pdf2zh_next example.pdf --translator-fallback-on-empty true`                                                         |
| `--translator-fallback-on-same` | Whether to use fallback translator if the translation is the same as the original (true/false) | `pdf2zh_next example.pdf --translator-fallback-on-same true`                                                  |
| `--translator-fallback-on-limit` | Whether to use fallback translator if the translation limit is reached (true/false)     | `pdf2zh_next example.pdf --translator-fallback-on-limit true`                                                         |
| `--translator-fallback-on-other` | Whether to use fallback translator on other conditions (true/false)                     | `pdf2zh_next example.pdf --translator-fallback-on-other true`                                                         |
| `--translator-fallback-on-all`  | Whether to use fallback translator on all conditions (true/false)                        | `pdf2zh_next example.pdf --translator-fallback-on-all true`                                                           |
| `--translator-fallback-on-none` | Whether to use fallback translator on no conditions (true/false)                         | `pdf2zh_next example.pdf --translator-fallback-on-none true`                                                          |
| `--translator-fallback-on-custom` | Whether to use fallback translator on custom conditions (true/false)                    | `pdf2zh_next example.pdf --translator-fallback-on-custom true`                                                        |
| `--translator-fallback-on-custom-function` | Custom function to determine when to use fallback translator                         | `pdf2zh_next example.pdf --translator-fallback-on-custom-function 'function(text) { return text.length > 100; }'`     |
| `--translator-fallback-on-custom-function-file` | Path to a JavaScript file containing a custom function to determine when to use fallback translator | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-file custom.js`                             |
| `--translator-fallback-on-custom-function-args` | Arguments to pass to the custom function                                              | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-args '{"max_length": 100}'`                         |
| `--translator-fallback-on-custom-function-args-file` | Path to a JSON file containing arguments to pass to the custom function               | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-args-file args.json`                                |
| `--translator-fallback-on-custom-function-context` | Context to pass to the custom function                                               | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-context '{"user": "admin"}'`                        |
| `--translator-fallback-on-custom-function-context-file` | Path to a JSON file containing context to pass to the custom function                | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-context-file context.json`                          |
| `--translator-fallback-on-custom-function-timeout` | Timeout for the custom function in milliseconds                                       | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-timeout 5000`                                       |
| `--translator-fallback-on-custom-function-retry-attempts` | Number of retry attempts for the custom function                                     | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-attempts 3`                                   |
| `--translator-fallback-on-custom-function-retry-delay` | Delay between retry attempts for the custom function in milliseconds                 | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-delay 1000`                                  |
| `--translator-fallback-on-custom-function-retry-on-error` | Whether to retry the custom function on error (true/false)                          | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-error true`                                 |
| `--translator-fallback-on-custom-function-retry-on-empty` | Whether to retry the custom function on empty response (true/false)                 | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-empty true`                                |
| `--translator-fallback-on-custom-function-retry-on-same` | Whether to retry the custom function if the result is the same as the original (true/false) | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-same true`                         |
| `--translator-fallback-on-custom-function-retry-on-limit` | Whether to retry the custom function if the limit is reached (true/false)           | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-limit true`                                |
| `--translator-fallback-on-custom-function-retry-on-other` | Whether to retry the custom function on other conditions (true/false)               | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-other true`                                 |
| `--translator-fallback-on-custom-function-retry-on-all` | Whether to retry the custom function on all conditions (true/false)                  | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-all true`                                   |
| `--translator-fallback-on-custom-function-retry-on-none` | Whether to retry the custom function on no conditions (true/false)                  | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-none true`                                  |
| `--translator-fallback-on-custom-function-retry-on-custom` | Whether to retry the custom function on custom conditions (true/false)             | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom true`                                |
| `--translator-fallback-on-custom-function-retry-on-custom-function` | Custom function to determine when to retry the custom function                    | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function 'function(result) { return result === null; }'` |
| `--translator-fallback-on-custom-function-retry-on-custom-function-file` | Path to a JavaScript file containing a custom function to determine when to retry the custom function | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-file retry_custom.js` |
| `--translator-fallback-on-custom-function-retry-on-custom-function-args` | Arguments to pass to the custom function                                           | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-args '{"max_retries": 3}'` |
| `--translator-fallback-on-custom-function-retry-on-custom-function-args-file` | Path to a JSON file containing arguments to pass to the custom function        | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-args-file retry_args.json` |
| `--translator-fallback-on-custom-function-retry-on-custom-function-context` | Context to pass to the custom function                                            | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-context '{"user": "admin"}'` |
| `--translator-fallback-on-custom-function-retry-on-custom-function-context-file` | Path to a JSON file containing context to pass to the custom function         | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-context-file retry_context.json` |
| `--translator-fallback-on-custom-function-retry-on-custom-function-timeout` | Timeout for the custom function in milliseconds                                    | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-timeout 5000`              |
| `--translator-fallback-on-custom-function-retry-on-custom-function-retry-attempts` | Number of retry attempts for the custom function                                | `pdf2zh_next example.pdf --translator-fallback-on-custom-function-retry-on-custom-function-retry-attempts 3`          |
| `--transl 极长文本，已截断

---

### OUTPUT

| `--lang-out`                    | Código de idioma de destino                                                             | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-in`                     | Código de idioma de origen                                                              | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| `--translator`                  | Servicio de traducción a utilizar                                                       | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-config`           | Configuración para el servicio de traducción                                            | `pdf2zh_next example.pdf --translator-config '{"api_key": "your_api_key"}'`                                           |
| `--translator-config-file`      | Ruta a un archivo JSON que contiene la configuración para el servicio de traducción     | `pdf2zh_next example.pdf --translator-config-file config.json`                                                        |
| `--translator-retry-attempts`   | Número de intentos de reintento para solicitudes de traducción                          | `pdf2zh_next example.pdf --translator-retry-attempts 3`                                                               |
| `--translator-retry-delay`      | Retraso entre intentos de reintento en milisegundos                                     | `pdf2zh_next example.pdf --transl 极长文本，已截断
`5`                                                                                        |
|---------------------------------|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `--max-text-length`             | Maximum text length to translate                                                        | `pdf2zh_next example.pdf --max-text-length 100`                                                                       | `100`                                                                                      |
| `--text-length-estimator`       | Method to estimate text length                                                          | `pdf2zh_next example.pdf --text-length-estimator char`                                                                | `char`                                                                                     |
| `--formula-detector`            | Method to detect formulas                                                               | `pdf2zh_next example.pdf --formula-detector mml`                                                                      | `none`, `simple`, `pix2tex`, `mml`                                                         |
| `--formula-translator`          | Method to translate formulas                                                            | `pdf2zh_next example.pdf --formula-translator simple`                                                                 | `none`, `simple`, `pix2tex`                                                                |
| `--batch-size`                  | Batch size for translation                                                              | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `10`                                                                                       |
| `--workers`                     | Number of workers for translation                                                       | `pdf2zh_next example.pdf --workers 5`                                                                                 | `5`                                                                                         |
| `--cache-dir`                   | Cache directory for translation models                                                  | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         | `./cache`                                                                                  |
| `--timeout`                     | Timeout for translation requests                                                        | `pdf2zh_next example.pdf --timeout 30`                                                                                | `30`                                                                                       |
| `--retry-attempts`              | Number of retry attempts for failed translations                                        | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          | `3`                                                                                        |
| `--retry-delay`                 | Delay between retry attempts in seconds                                                 | `pdf2zh_next example.pdf --retry-delay 1`                                                                             | `1`                                                                                        |

---

### OUTPUT

| `--min-text-length`             | Longitud mínima de texto a traducir                                                     | `pdf2zh_next example.pdf --min-text-length 5`                                                                         | `5`                                                                                        |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `--max-text-length`             | Longitud máxima de texto a traducir                                                     | `pdf2zh_next example.pdf --max-text-length 100`                                                                       | `100`                                                                                      |
| `--text-length-estimator`       | Método para estimar la longitud del texto                                               | `pdf2zh_next example.pdf --text-length-estimator char`                                                                | `char`                                                                                     |
| `--formula-detector`            | Método para detectar fórmulas                                                           | `pdf2zh_next example.pdf --formula-detector mml`                                                                      | `none`, `simple`, `pix2tex`, `mml`                                                         |
| `--formula-translator`          | Método para traducir fórmulas                                                           | `pdf2zh_next example.pdf --formula-translator simple`                                                                 | `none`, `simple`, `pix2tex`                                                                |
| `--batch-size`                  | Tamaño del lote para la traducción                                                      | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `10`                                                                                       |
| `--workers`                     | Número de trabajadores para la traducción                                               | `pdf2zh_next example.pdf --workers 5`                                                                                 | `5`                                                                                         |
| `--cache-dir`                   | Directorio de caché para modelos de traducción                                          | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         | `./cache`                                                                                  |
| `--timeout`                     | Tiempo de espera para las solicitudes de traducción                                     | `pdf2zh_next example.pdf --timeout 30`                                                                                | `30`                                                                                       |
| `--retry-attempts`              | Número de intentos de reintento para traducciones fallidas                              | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          | `3`                                                                                        |
| `--retry-delay`                 | Retraso entre intentos de reintento en segundos                                         | `pdf2zh_next example.pdf --retry-delay 1`                                                                             | `1`                                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8000`                                                             |
| `--rpc-translate`               | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8000`                                                       |
| `--layout-parser`               | Specify the layout parser to use, default: `yolov8`                                     | `pdf2zh_next example.pdf --layout-parser yolov8`                                                                      |
| `--ocr`                         | Specify the OCR engine to use, default: `paddleocr`                                     | `pdf2zh_next example.pdf --ocr paddleocr`                                                                             |
| `--translator`                  | Specify the translation service to use, default: `google`                               | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--target-language`             | Specify the target language code, default: `zh`                                         | `pdf2zh_next example.pdf --target-language zh`                                                                        |
| `--source-language`             | Specify the source language code, default: `auto`                                       | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--concurrency-limit`           | Specify the maximum number of concurrent translation requests, default: `10`            | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `--timeout`                     | Specify the timeout for translation requests in seconds, default: `30`                  | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry-attempts`              | Specify the number of retry attempts for failed requests, default: `3`                  | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          |
| `--retry-delay`                 | Specify the delay between retry attempts in seconds, default: `1`                       | `pdf2zh_next example.pdf --retry-delay 1`                                                                             |
| `--output-dir`                  | Specify the output directory for translated files, default: `./output`                  | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-format`               | Specify the output format, default: `pdf`                                               | `pdf2zh_next example.pdf --output-format pdf`                                                                         |
| `--image-dpi`                   | Specify the DPI for image processing, default: `300`                                    | `pdf2zh_next example.pdf --image-dpi 300`                                                                             |
| `--image-quality`               | Specify the image quality for output, default: `95`                                     | `pdf2zh_next example.pdf --image-quality 95`                                                                          |
| `--remove-original-text`        | Remove original text from output, default: `false`                                      | `pdf2zh_next example.pdf --remove-original-text`                                                                      |
| `--keep-line-breaks`            | Keep original line breaks in text, default: `false`                                     | `pdf2zh_next example.pdf --keep-line-breaks`                                                                          |
| `--font-family`                 | Specify the font family for translated text, default: `SimSun`                          | `pdf2zh_next example.pdf --font-family SimSun`                                                                        |
| `--font-size`                   | Specify the font size for translated text, default: `auto`                              | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--font-size-scale`             | Specify the font size scale factor, default: `1.0`                                      | `pdf2zh_next example.pdf --font-size-scale 1.2`                                                                       |
| `--color`                       | Specify the color for translated text, default: `#000000`                               | `pdf2zh_next example.pdf --color #FF0000`                                                                             |
| `--line-spacing`                | Specify the line spacing for translated text, default: `1.0`                            | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--char-spacing`                | Specify the character spacing for translated text, default: `0`                         | `pdf2zh_next example.pdf --char-spacing 1`                                                                            |
| `--margin-top`                  | Specify the top margin for text boxes, default: `0`                                     | `pdf2zh_next example.pdf --margin-top 5`                                                                              |
| `--margin-bottom`               | Specify the bottom margin for text boxes, default: `0`                                  | `pdf2zh_next example.pdf --margin-bottom 5`                                                                           |
| `--margin-left`                 | Specify the left margin for text boxes, default: `0`                                    | `pdf2zh_next example.pdf --margin-left 5`                                                                             |
| `--margin-right`                | Specify the right margin for text boxes, default: `0`                                   | `pdf2zh_next example.pdf --margin-right 5`                                                                            |
| `--text-align`                  | Specify the text alignment, default: `left`                                             | `pdf2zh_next example.pdf --text-align center`                                                                         |
| `--vertical-align`              | Specify the vertical alignment, default: `top`                                          | `pdf2zh_next example.pdf --vertical-align middle`                                                                     |
| `--page-number`                 | Specify the page number to process (e.g., `1`, `1-3`, `1,3,5`), default: `all`          | `pdf2zh_next example.pdf --page-number 1-3`                                                                           |
| `--log-level`                   | Specify the log level, default: `INFO`                                                  | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--config`                      | Specify a configuration file to load options from                                       | `pdf2zh_next example.pdf --config config.json`                                                                        |
| `--version`                     | Show version information and exit                                                       | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION RESULT

| `--rpc-doclayout`               | Dirección del host del servicio RPC para análisis de diseño de documentos               | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--rpc-ocr`                     | Dirección del host del servicio RPC para OCR                                            | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8000`                                                             |
| `--rpc-translate`               | Dirección del host del servicio RPC para traducción                                     | `pdf2zh_next example.pdf --rpc-translate http://127.0.0.1:8000`                                                       |
| `--layout-parser`               | Especifica el analizador de diseño a usar, predeterminado: `yolov8`                     | `pdf2zh_next example.pdf --layout-parser yolov8`                                                                      |
| `--ocr`                         | Especifica el motor OCR a usar, predeterminado: `paddleocr`                             | `pdf2zh_next example.pdf --ocr paddleocr`                                                                             |
| `--translator`                  | Especifica el servicio de traducción a usar, predeterminado: `google`                   | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--target-language`             | Especifica el código de idioma de destino, predeterminado: `zh`                         | `pdf2zh_next example.pdf --target-language zh`                                                                        |
| `--source-language`             | Especifica el código de idioma de origen, predeterminado: `auto`                        | `pdf2zh_next example.pdf --source-language en`                                                                        |
| `--concurrency-limit`           | Especifica el número máximo de solicitudes de traducción concurrentes, predeterminado: `10` | `pdf2zh_next example.pdf --concurrency-limit 10`                                                                      |
| `--timeout`                     | Especifica el tiempo de espera para las solicitudes de traducción en segundos, predeterminado: `30` | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry-attempts`              | Especifica el número de intentos de reintento para solicitudes fallidas, predeterminado: `3` | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          |
| `--retry-delay`                 | Especifica el retraso entre intentos de reintento en segundos, predeterminado: `1`      | `pdf2zh_next example.pdf --retry-delay 1`                                                                             |
| `--output-dir`                  | Especifica el directorio de salida para los archivos traducidos, predeterminado: `./output` | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-format`               | Especifica el formato de salida, predeterminado: `pdf`                                  | `pdf2zh_next example.pdf --output-format pdf`                                                                         |
| `--image-dpi`                   | Especifica el DPI para el procesamiento de imágenes, predeterminado: `300`              | `pdf2zh_next example.pdf --image-dpi 300`                                                                             |
| `--image-quality`               | Especifica la calidad de imagen para la salida, predeterminado: `95`                    | `pdf2zh_next example.pdf --image-quality 95`                                                                          |
| `--remove-original-text`        | Elimina el texto original de la salida, predeterminado: `false`                         | `pdf2zh_next example.pdf --remove-original-text`                                                                      |
| `--keep-line-breaks`            | Mantiene los saltos de línea originales en el texto, predeterminado: `false`            | `pdf2zh_next example.pdf --keep-line-breaks`                                                                          |
| `--font-family`                 | Especifica la familia de fuentes para el texto traducido, predeterminado: `SimSun`      | `pdf2zh_next example.pdf --font-family SimSun`                                                                        |
| `--font-size`                   | Especifica el tamaño de fuente para el texto traducido, predeterminado: `auto`          | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--font-size-scale`             | Especifica el factor de escala del tamaño de fuente, predeterminado: `1.0`              | `pdf2zh_next example.pdf --font-size-scale 1.2`                                                                       |
| `--color`                       | Especifica el color para el texto traducido, predeterminado: `#000000`                  | `pdf2zh_next example.pdf --color #FF0000`                                                                             |
| `--line-spacing`                | Especifica el interlineado para el texto traducido, predeterminado: `1.0`               | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--char-spacing`                | Especifica el espaciado de caracteres para el texto traducido, predeterminado: `0`      | `pdf2zh_next example.pdf --char-spacing 1`                                                                            |
| `--margin-top`                  | Especifica el margen superior para las cajas de texto, predeterminado: `0`              | `pdf2zh_next example.pdf --margin-top 5`                                                                              |
| `--margin-bottom`               | Especifica el margen inferior para las cajas de texto, predeterminado: `0`              | `pdf2zh_next example.pdf --margin-bottom 5`                                                                           |
| `--margin-left`                 | Especifica el margen izquierdo para las cajas de texto, predeterminado: `0`             | `pdf2zh_next example.pdf --margin-left 5`                                                                             |
| `--margin-right`                | Especifica el margen derecho para las cajas de texto, predeterminado: `极光 PDF 翻译`     | `pdf2zh_next example.pdf --margin-right 5`                                                                            |
| `--text-align`                  | Especifica la alineación del texto, predeterminado: `left`                              | `极光 PDF 翻译 example.pdf --text-align center`                                                                         |
| `--vertical-align`              | Especifica la alineación vertical, predeterminado: `top`                                | `极光 PDF 翻译 example.pdf --vertical-align middle`                                                                     |
| `--page-number`                 | Especifica el número de página a procesar (ej. `1`, `1-3`, `1,3,5`), predeterminado: `all` | `极光 PDF 翻译 example.pdf --page-number 1-3`                                                                           |
| `--log-level`                   | Especifica el nivel de registro, predeterminado: `INFO`                                 | `极光 PDF 翻译 example.pdf --log-level DEBUG`                                                                           |
| `--config`                      | Especifica un archivo de configuración para cargar opciones                             | `极光 PDF 翻译 example.pdf --config config.json`                                                                        |
| `--version`                     | Muestra información de versión y sale                                                   | `极光 PDF 翻译 --version`                                                                                               |
| `--help`                        | Muestra mensaje de ayuda y sale                                                         | `极光 PDF 翻译 --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-char`                     | The maximum character limit for a single translation request                            | `pdf2zh_next example.pdf --max-char 3000`                                                                             |
| `--no-merge`                     | Do not merge paragraphs after translation                                               | `pdf2zh_next example.pdf --no-merge`                                                                                  |

---

### OUTPUT

| `--qps`                         | Límite de QPS para el servicio de traducción                                            | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-char`                     | El límite máximo de caracteres para una sola solicitud de traducción                    | `pdf2zh_next example.pdf --max-char 3000`                                                                             |
| `--no-merge`                     | No fusionar párrafos después de la traducción                                           | `pdf2zh_next example.pdf --no-merge`                                                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--ignore-translated-cache`     | Ignore translated cache, re-extract text from the PDF file                              | `pdf2zh_next example.pdf --ignore-translated-cache`                                                                   |
| `--ignore-image-cache`          | Ignore image cache, re-extract images from the PDF file                                 | `pdf2zh_next example.pdf --ignore-image-cache`                                                                        |
| `--ignore-ocr-cache`            | Ignore OCR cache, re-OCR the images                                                     | `pdf2zh_next example.pdf --ignore-ocr-cache`                                                                          |
| `--ignore-layout-analysis-cache` | Ignore layout analysis cache, re-analyze the layout of the PDF file                     | `pdf2zh_next example.pdf --ignore-layout-analysis-cache`                                                              |
| `--ignore-all-cache`            | Ignore all caches, re-extract text and images, re-OCR, and re-analyze the layout        | `pdf2zh_next example.pdf --ignore-all-cache`                                                                          |

---

### OUTPUT

| `--ignore-cache`                | Ignorar caché de traducción                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| :------------------------------ | :----------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--ignore-translated-cache`     | Ignorar caché de traducción, reextraer texto del archivo PDF                               | `pdf2zh_next example.pdf --ignore-translated-cache`                                                                   |
| `--ignore-image-cache`          | Ignorar caché de imágenes, reextraer imágenes del archivo PDF                              | `pdf2zh_next example.pdf --ignore-image-cache`                                                                        |
| `--ignore-ocr-cache`            | Ignorar caché de OCR, rehacer OCR de las imágenes                                          | `pdf2zh_next example.pdf --ignore-ocr-cache`                                                                          |
| `--ignore-layout-analysis-cache` | Ignorar caché de análisis de diseño, reanalizar el diseño del archivo PDF                  | `pdf2zh_next example.pdf --ignore-layout-analysis-cache`                                                              |
| `--ignore-all-cache`            | Ignorar todas las cachés, reextraer texto e imágenes, rehacer OCR y reanalizar el diseño   | `pdf2zh_next example.pdf --ignore-all-cache`                                                                          |
`string` |
|---------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------|
| `-v`, `--verbose`               | Print more information                                                                  | `pdf2zh_next example.pdf -v`                                                                                             | `flag`   |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                                  | `flag`   |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                     | `flag`   |
| `--show-available-models`       | Show available models and exit                                                          | `pdf2zh_next --show-available-models`                                                                                    | `flag`   |
| `-o`, `--output`                | Output file path                                                                        | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                      | `string` |
| `--output-format`               | Output format, default is `pdf`. Choose from `pdf`, `markdown`, `text`                  | `pdf2zh_next example.pdf --output-format markdown`                                                                       | `string` |
| `--output-language`             | Output language code, default is `zh`                                                   | `pdf2zh_next example.pdf --output-language en`                                                                           | `string` |
| `--model`                       | Model name, default is `qwen/qwen2.5-7b-instruct`                                       | `pdf2zh_next example.pdf --model qwen/qwen2.5-14b-instruct`                                                              | `string` |
| `--api-base`                    | API base URL, default is `https://api-inference.huggingface.co/models`                  | `pdf2zh_next example.pdf --api-base http://localhost:8080/v1`                                                            | `string` |
| `--api-key`                     | API key, default is `hf_***`                                                            | `pdf2zh_next example.pdf --api-key your_api_key_here`                                                                    | `string` |
| `-c`, `--concurrency`           | Number of concurrent requests, default is `1`                                           | `pdf2zh_next example.pdf -c 4`                                                                                           | `int`    |
| `--timeout`                     | Request timeout in seconds, default is `60`                                             | `pdf2zh_next example.pdf --timeout 120`                                                                                  | `int`    |
| `--max-retries`                 | Maximum number of retries, default is `3`                                               | `pdf2zh_next example.pdf --max-retries 5`                                                                                | `int`    |
| `--retry-delay`                 | Delay between retries in seconds, default is `1`                                        | `pdf2zh_next example.pdf --retry-delay 2`                                                                                | `int`    |
| `--batch-size`                  | Batch size for translation, default is `5`                                              | `pdf2zh_next example.pdf --batch-size 10`                                                                                | `int`    |
| `--chunk-size`                  | Chunk size for splitting text, default is `1000`                                        | `pdf2zh_next example.pdf --chunk-size 500`                                                                               | `int`    |
| `--chunk-overlap`               | Chunk overlap size, default is `100`                                                    | `pdf2zh_next example.pdf --chunk-overlap 50`                                                                             | `int`    |
| `--temperature`                 | Temperature for generation, default is `0.1`                                            | `pdf2zh_next example.pdf --temperature 0.5`                                                                              | `float`  |
| `--top-p`                       | Top-p for generation, default is `0.9`                                                  | `pdf2zh_next example.pdf --top-p 0.95`                                                                                   | `float`  |
| `--max-tokens`                  | Maximum tokens per request, default is `4096`                                           | `pdf2zh_next example.pdf --max-tokens 8192`                                                                              | `int`    |
| `--thinking-tokens`             | Maximum tokens for thinking, default is `512`                                           | `pdf2zh_next example.pdf --thinking-tokens 1024`                                                                         | `int`    |
| `--no-thinking`                 | Disable thinking step                                                                   | `pdf2zh_next example.pdf --no-thinking`                                                                                  | `flag`   |
| `--custom-system-prompt`        | Custom system prompt for translation. Used for `/no_think` in Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` | `string` |
| `-v`, `--verbose`               | Print more information                                                                  | `pdf2zh_next example.pdf -v`                                                                                             | `flag`   |
| `--version`                     | Show version and exit                                                                   | `pdf2zh_next --version`                                                                                                  | `flag`   |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                     | `flag`   |
| `--show-available-models`       | Show available models and exit                                                          | `pdf2zh_next --show-available-models`                                                                                    | `flag`   |

---

### OUTPUT

| `--custom-system-prompt`        | Mensaje del sistema personalizado para la traducción. Se utiliza para `/no_think` en Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` | `string` |
|---------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------|
| `-v`, `--verbose`               | Imprimir más información                                                                  | `pdf2zh_next example.pdf -v`                                                                                             | `flag`   |
| `--version`                     | Mostrar la versión y salir                                                                   | `pdf2zh_next --version`                                                                                                  | `flag`   |
| `-h`, `--help`                  | Mostrar el mensaje de ayuda y salir                                                              | `pdf2zh_next --help`                                                                                                     | `flag`   |
| `--show-available-models`       | Mostrar los modelos disponibles y salir                                                          | `pdf2zh_next --show-available-models`                                                                                    | `flag`   |
| `-o`, `--output`                | Ruta del archivo de salida                                                                        | `pdf2zh_next example.pdf -o example_translated.pdf`                                                                      | `string` |
| `--output-format`               | Formato de salida, por defecto es `pdf`. Opciones: `pdf`, `markdown`, `text`                  | `pdf2zh_next example.pdf --output-format markdown`                                                                       | `string` |
| `--output-language`             | Código de idioma de salida, por defecto es `zh`                                                   | `pdf2zh_next example.pdf --output-language en`                                                                           | `string` |
| `--model`                       | Nombre del modelo, por defecto es `qwen/qwen2.5-7b-instruct`                                       | `pdf2zh_next example.pdf --model qwen/qwen2.5-14b-instruct`                                                              | `string` |
| `--api-base`                    | URL base de la API, por defecto es `https://api-inference.huggingface.co/models`                  | `pdf2zh_next example.pdf --api-base http://localhost:8080/v1`                                                            | `string` |
| `--api-key`                     | Clave de la API, por defecto es `hf_***`                                                            | `pdf2zh_next example.pdf --api-key your_api_key_here`                                                                    | `string` |
| `-c`, `--concurrency`           | Número de solicitudes concurrentes, por defecto es `1`                                           | `pdf2zh_next example.pdf -c 4`                                                                                           | `int`    |
| `--timeout`                     | Tiempo de espera de la solicitud en segundos, por defecto es `60`                                             | `pdf2zh_next example.pdf --timeout 120`                                                                                  | `int`    |
| `--max-retries`                 | Número máximo de reintentos, por defecto es `3`                                               | `pdf2zh_next example.pdf --max-retries 5`                                                                                | `int`    |
| `--retry-delay`                 | Retraso entre reintentos en segundos, por defecto es `1`                                        | `pdf2zh_next example.pdf --retry-delay 2`                                                                                | `int`    |
| `--batch-size`                  | Tamaño del lote para la traducción, por defecto es `5`                                              | `pdf2zh_next example.pdf --batch-size 10`                                                                                | `int`    |
| `--chunk-size`                  | Tamaño del fragmento para dividir el texto, por defecto es `1000`                                        | `pdf2zh_next example.pdf --chunk-size 500`                                                                               | `int`    |
| `--chunk-overlap`               | Tamaño de superposición de fragmentos, por defecto es `100`                                                    | `pdf2zh_next example.pdf --chunk-overlap 50`                                                                             | `int`    |
| `--temperature`                 | Temperatura para la generación, por defecto es `0.1`                                            | `pdf2zh_next example.pdf --temperature 0.5`                                                                              | `float`  |
| `--top-p`                       | Top-p para la generación, por defecto es `0.9`                                                  | `pdf2zh_next example.pdf --top-p 0.95`                                                                                   | `float`  |
| `--max-tokens`                  | Máximo de tokens por solicitud, por defecto es `4096`                                           | `pdf2zh_next example.pdf --max-tokens 8192`                                                                              | `int`    |
| `--thinking-tokens`             | Máximo de tokens para pensar, por defecto es `512`                                           | `pdf2zh_next example.pdf --thinking-tokens 1024`                                                                         | `int`    |
| `--no-thinking`                 | Deshabilitar el paso de pensamiento                                                                   | `pdf2zh_next example.pdf --no-thinking`                                                                                  | `flag`   |
| `--custom-system-prompt`        | Mensaje del sistema personalizado para la traducción. Se utiliza para `/no_think` en Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` | `string` |
| `-v`, `--verbose`               | Imprimir más información                                                                  | `pdf2zh_next example.pdf -v`                                                                                             | `flag`   |
| `--version`                     | Mostrar la versión y salir                                                                   | `pdf2zh_next --version`                                                                                                  | `flag`   |
| `-h`, `--help`                  | Mostrar el mensaje de ayuda y salir                                                              | `pdf2zh_next --help`                                                                                                     | `flag`   |
| `--show-available-models`       | Mostrar los modelos disponibles y salir                                                          | `pdf2zh_next --show-available-models`                                                                                    | `flag`   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary_path`               | Glossary path.                                                                          | `pdf2zh_next example.pdf --glossary_path "path/to/glossary"`                                                          |
| `--glossary_url`                | Glossary URL.                                                                           | `pdf2zh_next example.pdf --glossary_url "https://example.com/glossary.csv"`                                           |
| `--glossary`                    | Glossary string.                                                                        | `pdf2zh_next example.pdf --glossary "term1,translation1;term2,translation2;term3,translation3"`                      |
| `--glossary_merge`              | Merge glossaries.                                                                       | `pdf2zh_next example.pdf --glossary_merge`                                                                            |
| `--glossary_merge_strategy`     | Merge strategy for glossaries.                                                          | `pdf2zh_next example.pdf --glossary_merge_strategy "overwrite"`                                                       |
| `--glossary_merge_strategy_csv` | Merge strategy for CSV glossaries.                                                      | `pdf2zh_next example.pdf --glossary_merge_strategy_csv "overwrite"`                                                   |
| `--glossary_merge_strategy_url` | Merge strategy for URL glossaries.                                                      | `pdf2zh_next example.pdf --glossary_merge_strategy_url "overwrite"`                                                   |

---

### OUTPUT

| `--glossaries`                  | Lista de archivos de glosario.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary_path`               | Ruta del glosario.                                                                          | `pdf2zh_next example.pdf --glossary_path "path/to/glossary"`                                                          |
| `--glossary_url`                | URL del glosario.                                                                           | `pdf2zh_next example.pdf --glossary_url "https://example.com/glossary.csv"`                                           |
| `--glossary`                    | Cadena de glosario.                                                                        | `pdf2zh_next example.pdf --glossary "term1,translation1;term2,translation2;term3,translation3"`                      |
| `--glossary_merge`              | Combinar glosarios.                                                                       | `pdf2zh_next example.pdf --glossary_merge`                                                                            |
| `--glossary_merge_strategy`     | Estrategia de combinación para glosarios.                                                          | `pdf2zh_next example.pdf --glossary_merge_strategy "overwrite"`                                                       |
| `--glossary_merge_strategy_csv` | Estrategia de combinación para glosarios CSV.                                                      | `pdf2zh_next example.pdf --glossary_merge_strategy_csv "overwrite"`                                                   |
| `--glossary_merge_strategy_url` | Estrategia de combinación para glosarios URL.                                                      | `pdf2zh_next example.pdf --glossary_merge_strategy_url "overwrite"`                                                   |
---

### OUTPUT LANGUAGE

es

---

### TRANSLATED TEXT

| `--save-auto-extracted-glossary`| guardar glosario extraído automáticamente                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-retries`            | Maximum number of retries for translation pool. If not set, will use 3 as the default value       | `pdf2zh_next example.pdf --pool-max-retries 5`                                                             |
| `--pool-request-interval`       | Interval between requests for translation pool. If not set, will use 0 as the default value       | `pdf2zh_next example.pdf --pool-request-interval 1000`                                                     |
| `--pool-request-timeout`        | Timeout for each request in translation pool. If not set, will use 10 as the default value        | `pdf2zh_next example.pdf --pool-request-timeout 30`                                                        |
| `--pool-request-timeout-retries` | Maximum number of retries for timeout in translation pool. If not set, will use 3 as the default value | `pdf2zh_next example.pdf --pool-request-timeout-retries 5`                                                 |
| `--pool-request-timeout-interval` | Interval between retries for timeout in translation pool. If not set, will use 1 as the default value | `pdf2zh_next example.pdf --pool-request-timeout-interval 1000`                                             |

---

### TRANSLATION RESULT

| `--pool-max-workers`            | Número máximo de trabajadores para el pool de traducción. Si no se establece, se utilizará qps como el número de trabajadores | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-max-retries`            | Número máximo de reintentos para el pool de traducción. Si no se establece, se utilizará 3 como valor predeterminado       | `pdf2zh_next example.pdf --pool-max-retries 5`                                                             |
| `--pool-request-interval`       | Intervalo entre solicitudes para el pool de traducción. Si no se establece, se utilizará 0 como valor predeterminado       | `pdf2zh_next example.pdf --pool-request-interval 1000`                                                     |
| `--pool-request-timeout`        | Tiempo de espera para cada solicitud en el pool de traducción. Si no se establece, se utilizará 10 como valor predeterminado        | `pdf2zh_next example.pdf --pool-request-timeout 30`                                                        |
| `--pool-request-timeout-retries` | Número máximo de reintentos por tiempo de espera en el pool de traducción. Si no se establece, se utilizará 3 como valor predeterminado | `pdf2zh_next example.pdf --pool-request-timeout-retries 5`                                                 |
| `--pool-request-timeout-interval` | Intervalo entre reintentos por tiempo de espera en el pool de traducción. Si no se establece, se utilizará 1 como valor predeterminado | `pdf2zh_next example.pdf --pool-request-timeout-interval 1000`                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--qps`                         | QPS limit for translation service. If not set, will use the default value of the model. | `pdf2zh_next example.pdf --qps 20`                                                                                    |
| `--term-batch`                  | Batch size for term extraction translation service. If not set, will follow batch.       | `pdf2zh_next example.pdf --term-batch 20`                                                                             |
| `--batch`                       | Batch size for translation service. If not set, will use the default value of the model. | `pdf2zh_next example.pdf --batch 20`                                                                                  |
| `--term-translation-service-id` | Translation service ID for term extraction                                              | `pdf2zh_next example.pdf --term-translation-service-id aliyun`                                                        |
| `--translation-service-id`      | Translation service ID for translation                                                  | `pdf2zh_next example.pdf --translation-service-id aliyun`                                                              |
| `--term-lang`                   | Language code for term extraction                                                       | `pdf2zh_next example.pdf --term-lang en`                                                                              |
| `--lang`                        | Language code for translation                                                           | `pdf2zh_next example.pdf --lang en`                                                                                   |
| `--term-extra-args`             | Extra arguments for term extraction translation service                                 | `pdf2zh_next example.pdf --term-extra-args '{"key": "value"}'`                                                        |
| `--extra-args`                  | Extra arguments for translation service                                                 | `pdf2zh_next example.pdf --extra-args '{"key": "value"}'`                                                             |
| `--term-base-url`               | Base URL for term extraction translation service                                        | `pdf2zh_next example.pdf --term-base-url https://your-custom-endpoint.com`                                            |
| `--base-url`                    | Base URL for translation service                                                        | `pdf2zh_next example.pdf --base-url https://your-custom-endpoint.com`                                                 |
| `--term-ignore-tls-verification` | Ignore TLS verification for term extraction translation service                        | `pdf2zh_next example.pdf --term-ignore-tls-verification`                                                              |
| `--ignore-tls-verification`     | Ignore TLS verification for translation service                                         | `pdf2zh_next example.pdf --ignore-tls-verification`                                                                   |
| `--term-model`                  | Model for term extraction translation service                                           | `pdf2zh_next example.pdf --term-model gpt-4o`                                                                         |
| `--model`                       | Model for translation service                                                           | `pdf2zh_next example.pdf --model gpt-4o`                                                                              |
| `--term-api-key`                | API Key for term extraction translation service                                         | `pdf2zh_next example.pdf --term-api-key sk-xxx`                                                                       |
| `--api-key`                     | API Key for translation service                                                         | `pdf2zh_next example.pdf --api-key sk-xxx`                                                                            |
| `--term-provider`               | Provider for term extraction translation service                                        | `pdf2zh_next example.pdf --term-provider openai`                                                                      |
| `--provider`                    | Provider for translation service                                                        | `pdf2zh_next example.pdf --provider openai`                                                                           |

---

### OUTPUT

| `--term-qps`                    | Límite de QPS para el servicio de traducción de extracción de términos. Si no se establece, seguirá a qps. | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--qps`                         | Límite de QPS para el servicio de traducción. Si no se establece, se utilizará el valor predeterminado del modelo. | `pdf2zh_next example.pdf --qps 20`                                                                                    |
| `--term-batch`                  | Tamaño de lote para el servicio de traducción de extracción de términos. Si no se establece, seguirá a batch. | `pdf2zh_next example.pdf --term-batch 20`                                                                             |
| `--batch`                       | Tamaño de lote para el servicio de traducción. Si no se establece, se utilizará el valor predeterminado del modelo. | `pdf2zh_next example.pdf --batch 20`                                                                                  |
| `--term-translation-service-id` | ID del servicio de traducción para la extracción de términos                                               | `pdf2zh_next example.pdf --term-translation-service-id aliyun`                                                        |
| `--translation-service-id`      | ID del servicio de traducción para la traducción                                                           | `pdf2zh_next example.pdf --translation-service-id aliyun`                                                              |
| `--term-lang`                   | Código de idioma para la extracción de términos                                                           | `pdf2zh_next example.pdf --term-lang en`                                                                              |
| `--lang`                        | Código de idioma para la traducción                                                                       | `pdf2zh_next example.pdf --lang en`                                                                                   |
| `--term-extra-args`             | Argumentos adicionales para el servicio de traducción de extracción de términos                            | `pdf2zh_next example.pdf --term-extra-args '{"key": "value"}'`                                                        |
| `--extra-args`                  | Argumentos adicionales para el servicio de traducción                                                     | `pdf2zh_next example.pdf --extra-args '{"key": "value"}'`                                                             |
| `--term-base-url`               | URL base para el servicio de traducción de extracción de términos                                         | `pdf2zh_next example.pdf --term-base-url https://your-custom-endpoint.com`                                            |
| `--base-url`                    | URL base para el servicio de traducción                                                                   | `pdf2zh_next example.pdf --base-url https://your-custom-endpoint.com`                                                 |
| `--term-ignore-tls-verification` | Ignorar la verificación TLS para el servicio de traducción de extracción de términos                      | `pdf2zh_next example.pdf --term-ignore-tls-verification`                                                              |
| `--ignore-tls-verification`     | Ignorar la verificación TLS para el servicio de traducción                                                | `pdf2zh_next example.pdf --ignore-tls-verification`                                                                   |
| `--term-model`                  | Modelo para el servicio de traducción de extracción de términos                                           | `pdf2zh_next example.pdf --term-model gpt-4o`                                                                         |
| `--model`                       | Modelo para el servicio de traducción                                                                     | `pdf2zh_next example.pdf --model gpt-4o`                                                                              |
| `--term-api-key`                | Clave de API para el servicio de traducción de extracción de términos                                     | `pdf2zh_next example.pdf --term-api-key sk-xxx`                                                                       |
| `--api-key`                     | Clave de API para el servicio de traducción                                                               | `pdf2zh_next example.pdf --api-key sk-xxx`                                                                            |
| `--term-provider`               | Proveedor para el servicio de traducción de extracción de términos                                        | `pdf2zh_next example.pdf --term-provider openai`                                                                      |
| `--provider`                    | Proveedor para el servicio de traducción                                                                  | `pdf2zh_next example.pdf --provider openai`                                                                           |
`40`             |

---

### TARGET LANGUAGE

es

---

### TRANSLATION RESULT

| `--term-pool-max-workers`       | Número máximo de trabajadores para el pool de traducción de extracción de términos. Si no se establece o es 0, seguirá a pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  | `40`             |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Disable auto extract glossary                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Disable auto extract glossary                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |

---

### TRANSLATED TEXT

| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--no-auto-extract-glossary`    | Deshabilitar la extracción automática del glosario                                      | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `--secondary-font-family`       | Override secondary font family for translated text. Choices: same as `--primary-font-family`. If not specified, uses automatic font selection based on original text properties.                                                         | `pdf2zh_next example.pdf --secondary-font-family script` |
| `--font-size-scale`             | Scale factor for translated text font size. Value between 0.5 and 2.0. If not specified, uses automatic font size adjustment.                                                                                                           | `pdf2zh_next example.pdf --font-size-scale 1.2`       |
| `--line-height-scale`           | Scale factor for translated text line height. Value between 0.5 and 2.0. If not specified, uses automatic line height adjustment.                                                                                                        | `pdf2zh_next example.pdf --line-height-scale 1.1`     |
| `--letter-spacing-scale`        | Scale factor for translated text letter spacing. Value between 0.5 and 2.0. If not specified, uses automatic letter spacing adjustment.                                                                                                   | `pdf2zh_next example.pdf --letter-spacing-scale 0.9`  |

---

### TRANSLATION

| `--primary-font-family`         | Anula la familia de fuentes principal para el texto traducido. Opciones: 'serif' para fuentes serif, 'sans-serif' para fuentes sans-serif, 'script' para fuentes script/cursivas. Si no se especifica, utiliza la selección automática de fuentes basada en las propiedades del texto original. | `pdf2zh_next example.pdf --primary-font-family serif` |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `--secondary-font-family`       | Anula la familia de fuentes secundaria para el texto traducido. Opciones: igual que `--primary-font-family`. Si no se especifica, utiliza la selección automática de fuentes basada en las propiedades del texto original.                         | `pdf2zh_next example.pdf --secondary-font-family script` |
| `--font-size-scale`             | Factor de escala para el tamaño de fuente del texto traducido. Valor entre 0.5 y 2.0. Si no se especifica, utiliza el ajuste automático del tamaño de fuente.                                                                                                           | `pdf2zh_next example.pdf --font-size-scale 1.2`       |
| `--line-height-scale`           | Factor de escala para la altura de línea del texto traducido. Valor entre 0.5 y 2.0. Si no se especifica, utiliza el ajuste automático de la altura de línea.                                                                                                        | `pdf2zh_next example.pdf --line-height-scale 1.1`     |
| `--letter-spacing-scale`        | Factor de escala para el espaciado entre letras del texto traducido. Valor entre 0.5 y 2.0. Si no se especifica, utiliza el ajuste automático del espaciado entre letras.                                                                                                   | `pdf2zh_next example.pdf --letter-spacing-scale 0.9`  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual`                        | Output bilingual PDF files (default)                                                    | `pdf2zh_next example.pdf --dual`                                                                                      |
| `--output-dir <output_dir>`     | Specify the output directory                                                            | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <output_name>`   | Specify the output filename                                                             | `pdf2zh_next example.pdf --output-name translated.pdf`                                                                |
| `--translator <translator>`     | Specify the translation service to use                                                  | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--target-lang <target_lang>`   | Specify the target language                                                             | `pdf2zh_next example.pdf --target-lang es`                                                                            |
| `--source-lang <source_lang>`   | Specify the source language                                                             | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--proxy <proxy>`               | Set proxy address                                                                       | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--api-key <api_key>`           | Set API key for translation service                                                     | `pdf2zh_next example.pdf --translator openai --api-key sk-...`                                                        |
| `--concurrent <concurrent>`     | Set the number of concurrent requests (default: 5)                                      | `pdf2zh_next example.pdf --concurrent 10`                                                                             |
| `--retry <retry>`               | Set the number of retries for failed requests (default: 3)                              | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--timeout <timeout>`           | Set timeout for each request in seconds (default: 30)                                   | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--dpi <dpi>`                   | Set DPI for image rendering (default: 300)                                              | `pdf2zh_next example.pdf --dpi 150`                                                                                   |
| `--no-ocr`                      | Disable OCR for text extraction                                                         | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--ocr`                         | Enable OCR for text extraction (default)                                                | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-lang <ocr_lang>`         | Specify the OCR language                                                                | `pdf2zh_next example.pdf --ocr-lang en`                                                                               |
| `--model-size <model_size>`     | Specify the model size for OCR (default: base)                                          | `pdf2zh_next example.pdf --model-size small`                                                                          |
| `--font-family <font_family>`   | Specify the font family for the translated text                                         | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `--font-size <font_size>`       | Specify the font size for the translated text                                           | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing <line_spacing>` | Specify the line spacing for the translated text                                        | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--color <color>`               | Specify the color for the translated text                                               | `pdf2zh_next example.pdf --color "#333333"`                                                                           |
| `--bold`                        | Make the translated text bold                                                           | `pdf2zh_next example.pdf --bold`                                                                                      |
| `--italic`                      | Make the translated text italic                                                         | `pdf2zh_next example.pdf --italic`                                                                                    |
| `--debug`                       | Enable debug mode                                                                       | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT LANGUAGE

ISO 639-1 code: es

---

### OUTPUT

| `--no-dual`                     | No generar archivos PDF bilingües                                                       | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--dual`                        | Generar archivos PDF bilingües (por defecto)                                            | `pdf2zh_next example.pdf --dual`                                                                                      |
| `--output-dir <output_dir>`     | Especificar el directorio de salida                                                     | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <output_name>`   | Especificar el nombre del archivo de salida                                             | `pdf2zh_next example.pdf --output-name translated.pdf`                                                                |
| `--translator <translator>`     | Especificar el servicio de traducción a utilizar                                        | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--target-lang <target_lang>`   | Especificar el idioma de destino                                                        | `pdf2zh_next example.pdf --target-lang es`                                                                            |
| `--source-lang <source_lang>`   | Especificar el idioma de origen                                                         | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--proxy <proxy>`               | Establecer la dirección del proxy                                                       | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--api-key <api_key>`           | Establecer la clave API para el servicio de traducción                                  | `pdf2zh_next example.pdf --translator openai --api-key sk-...`                                                        |
| `--concurrent <concurrent>`     | Establecer el número de solicitudes concurrentes (por defecto: 5)                       | `pdf2zh_next example.pdf --concurrent 10`                                                                             |
| `--retry <retry>`               | Establecer el número de reintentos para solicitudes fallidas (por defecto: 3)           | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--timeout <timeout>`           | Establecer el tiempo de espera para cada solicitud en segundos (por defecto: 30)        | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--dpi <dpi>`                   | Establecer DPI para el renderizado de imágenes (por defecto: 300)                       | `pdf2zh_next example.pdf --dpi 150`                                                                                   |
| `--no-ocr`                      | Desactivar OCR para la extracción de texto                                              | `pdf2zh_next example.pdf --no-ocr`                                                                                    |
| `--ocr`                         | Activar OCR para la extracción de texto (por defecto)                                   | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-lang <ocr_lang>`         | Especificar el idioma de OCR                                                            | `pdf2zh_next example.pdf --ocr-lang en`                                                                               |
| `--model-size <model_size>`     | Especificar el tamaño del modelo para OCR (por defecto: base)                           | `pdf2zh_next example.pdf --model-size small`                                                                          |
| `--font-family <font_family>`   | Especificar la familia de fuentes para el texto traducido                               | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `--font-size <font_size>`       | Especificar el tamaño de fuente para el texto traducido                                 | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing <line_spacing>` | Especificar el interlineado para el texto traducido                                     | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--color <color>`               | Especificar el color para el texto traducido                                            | `pdf2zh_next example.pdf --color "#333333"`                                                                           |
| `--bold`                        | Hacer que el texto traducido sea en negrita                                             | `pdf2zh_next example.pdf --bold`                                                                                      |
| `--italic`                      | Hacer que el texto traducido sea en cursiva                                             | `pdf2zh_next example.pdf --italic`                                                                                    |
| `--debug`                       | Activar modo de depuración                                                              | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--help`                        | Mostrar mensaje de ayuda                                                                | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-bilingual`                | Do not output bilingual PDF files                                                       | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--output-dir <output_dir>`     | Specify the output directory for the results                                            | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <output_name>`   | Specify the name of the output file (without extension)                                 | `pdf2zh_next example.pdf --output-name example_translated`                                                            |
| `--source-lang <source_lang>`   | Specify the source language (default: `auto`)                                           | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--target-lang <target_lang>`   | Specify the target language (default: `zh`)                                             | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--translator <translator>`     | Specify the translation service to use (default: `google`)                              | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-args <key=value>` | Provide additional arguments for the translator (e.g., API key, custom endpoint)        | `pdf2zh_next example.pdf --translator-args api_key=your_api_key`                                                      |
| `--no-cache`                    | Disable caching of translation results                                                  | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir <cache_dir>`       | Specify the cache directory (default: `~/.cache/pdf2zh`)                                | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--force-refresh`               | Force refresh of the cache                                                              | `pdf2zh_next example.pdf --force-refresh`                                                                             |
| `--max-workers <max_workers>`   | Specify the maximum number of concurrent workers for translation (default: `4`)         | `pdf2zh_next example.pdf --max-workers 8`                                                                             |
| `--timeout <timeout>`           | Set the timeout for each translation request in seconds (default: `30`)                 | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry <retry>`               | Set the number of retry attempts for failed translations (default: `3`)                 | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--pdf-optimize`                | Optimize the output PDF file size                                                       | `pdf2zh_next example.pdf --pdf-optimize`                                                                              |
| `--ocr`                         | Enable OCR for scanned PDFs                                                             | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-language <ocr_language>` | Specify the language for OCR (default: `auto`)                                          | `pdf2zh_next example.pdf --ocr-language en`                                                                           |
| `--ocr-dpi <ocr_dpi>`           | Specify the DPI for OCR (default: `300`)                                                | `pdf2zh_next example.pdf --ocr-dpi 150`                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next example.pdf --help`                                                                                      |

---

### TRANSLATION RESULT

| `--no-mono`                     | No generar archivos PDF monolingües                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-bilingual`                | No generar archivos PDF bilingües                                                       | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--output-dir <output_dir>`     | Especificar el directorio de salida para los resultados                                 | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--output-name <output_name>`   | Especificar el nombre del archivo de salida (sin extensión)                             | `pdf2zh_next example.pdf --output-name example_translated`                                                            |
| `--source-lang <source_lang>`   | Especificar el idioma de origen (por defecto: `auto`)                                   | `pdf2zh_next example.pdf --source-lang en`                                                                            |
| `--target-lang <target_lang>`   | Especificar el idioma de destino (por defecto: `zh`)                                    | `pdf2zh_next example.pdf --target-lang ja`                                                                            |
| `--translator <translator>`     | Especificar el servicio de traducción a utilizar (por defecto: `google`)                | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-args <key=value>` | Proporcionar argumentos adicionales para el traductor (ej. clave API, endpoint personalizado) | `pdf2zh_next example.pdf --translator-args api_key=your_api_key`                                                      |
| `--no-cache`                    | Deshabilitar el almacenamiento en caché de los resultados de traducción                 | `pdf2zh_next example.pdf --no-cache`                                                                                  |
| `--cache-dir <cache_dir>`       | Especificar el directorio de caché (por defecto: `~/.cache/pdf2zh`)                     | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--force-refresh`               | Forzar la actualización de la caché                                                     | `pdf2zh_next example.pdf --force-refresh`                                                                             |
| `--max-workers <max_workers>`   | Especificar el número máximo de trabajadores concurrentes para la traducción (por defecto: `4`) | `pdf2zh_next example.pdf --max-workers 8`                                                                             |
| `--timeout <timeout>`           | Establecer el tiempo de espera para cada solicitud de traducción en segundos (por defecto: `30`) | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry <retry>`               | Establecer el número de intentos de reintento para traducciones fallidas (por defecto: `3`) | `pdf2zh_next example.pdf --retry 5`                                                                                   |
| `--pdf-optimize`                | Optimizar el tamaño del archivo PDF de salida                                           | `pdf2zh_next example.pdf --pdf-optimize`                                                                              |
| `--ocr`                         | Habilitar OCR para PDF escaneados                                                       | `pdf2zh_next example.pdf --ocr`                                                                                       |
| `--ocr-language <ocr_language>` | Especificar el idioma para OCR (por defecto: `auto`)                                    | `pdf2zh_next example.pdf --ocr-language en`                                                                           |
| `--ocr-dpi <ocr_dpi>`           | Especificar el DPI para OCR (por defecto: `300`)                                        | `pdf2zh_next example.pdf --ocr-dpi 150`                                                                               |
| `--help`                        | Mostrar mensaje de ayuda y salir                                                        | `pdf2zh_next example.pdf --help`                                                                                      |
`None`                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `--formular-font-size-ratio`    | Font size ratio to identify formula text                                                | `pdf2zh_next example.pdf --formular-font-size-ratio 1.1`                                                               | `1.1`                                                               |
| `--formular-char-ratio`         | Character ratio to identify formula text                                                | `pdf2zh_next example.pdf --formular-char-ratio 0.8`                                                                    | `0.8`                                                               |
| `--formular-char-pattern`       | Character pattern to identify formula text                                              | `pdf2zh_next example.pdf --formular-char-pattern "[a-zA-Z]"`                                                           | `None`                                                              |
| `--formular-char-set`           | Character set to identify formula text                                                  | `pdf2zh_next example.pdf --formular-char-set "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"`                  | `None`                                                              |
| `--formular-char-set-ratio`     | Character set ratio to identify formula text                                            | `pdf2zh_next example.pdf --formular-char-set-ratio 0.8`                                                                | `0.8`                                                               |
| `--formular-char-set-pattern`   | Character set pattern to identify formula text                                          | `pdf2zh_next example.pdf --formular-char-set-pattern "[a-zA-Z]"`                                                       | `None`                                                              |
| `--formular-char-set-size-ratio`| Character set size ratio to identify formula text                                       | `pdf2zh_next example.pdf --formular-char-set-size-ratio 0.8`                                                           | `0.8`                                                               |
| `--formular-char-set-size`      | Character set size to identify formula text                                             | `pdf2zh_next example.pdf --formular-char-set-size 10`                                                                  | `10`                                                                |
| `--formular-char-set-min-size`  | Character set minimum size to identify formula text                                     | `pdf2zh_next example.pdf --formular-char-set-min-size 5`                                                               | `5`                                                                 |
| `--formular-char-set-max-size`  | Character set maximum size to identify formula text                                     | `pdf2zh_next example.pdf --formular-char-set-max-size 15`                                                              | `15`                                                                |
| `--formular-char-set-min-ratio` | Character set minimum ratio to identify formula text                                    | `pdf2zh_next example.pdf --formular-char-set-min-ratio 0.5`                                                            | `0.5`                                                               |
| `--formular-char-set-max-ratio` | Character set maximum ratio to identify formula text                                    | `pdf2zh_next example.pdf --formular-char-set-max-ratio 0.9`                                                            | `0.9`                                                               |
| `--formular-char-set-min-count` | Character set minimum count to identify formula text                                    | `pdf2zh_next example.pdf --formular-char-set-min-count 5`                                                              | `5`                                                                 |
| `--formular-char-set-max-count` | Character set maximum count to identify formula text                                    | `pdf2zh_next example.pdf --formular-char-set-max-count 15`                                                             | `15`                                                                |
| `--formular-char-set-min-length`| Character set minimum length to identify formula text                                   | `pdf2zh_next example.pdf --formular-char-set-min-length 5`                                                             | `5`                                                                 |
| `--formular-char-set-max-length`| Character set maximum length to identify formula text                                   | `pdf2zh_next example.pdf --formular-char-set-max-length 15`                                                            | `15`                                                                |
| `--formular-char-set-min-width` | Character set minimum width to identify formula text                                    | `pdf2zh_next example.pdf --formular-char-set-min-width 5`                                                              | `5`                                                                 |
| `--formular-char-set-max-width` | Character set maximum width to identify formula text                                    | `pdf2zh_next example.pdf --formular-char-set-max-width 15`                                                             | `15`                                                                |
| `--formular-char-set-min-height`| Character set minimum height to identify formula text                                   | `pdf2zh_next example.pdf --formular-char-set-min-height 5`                                                             | `5`                                                                 |
| `--formular-char-set-max-height`| Character set maximum height to identify formula text                                   | `pdf2zh_next example.pdf --formular-char-set-max-height 15`                                                            | `15`                                                                |
| `--formular-char-set-min-area`  | Character set minimum area to identify formula text                                     | `pdf2zh_next example.pdf --formular-char-set-min-area 25`                                                              | `25`                                                                |
| `--formular-char-set-max-area`  | Character set maximum area to identify formula text                                     | `pdf2zh_next example.pdf --formular-char-set-max-area 225`                                                             | `225`                                                               |
| `--formular-char-set-min-aspect`| Character set minimum aspect ratio to identify formula text                             | `pdf2zh_next example.pdf --formular-char-set-min-aspect 0.5`                                                           | `0.5`                                                               |
| `--formular-char-set-max-aspect`| Character set maximum aspect ratio to identify formula text                             | `pdf2zh_next example.pdf --formular-char-set-max-aspect 2.0`                                                           | `2.0`                                                               |
| `--formular-char-set-min-density`| Character set minimum density to identify formula text                                  | `pdf2zh_next example.pdf --formular-char-set-min-density 0.5`                                                          | `0.5`                                                               |
| `--formular-char-set-max-density`| Character set maximum density to identify formula text                                  | `pdf2zh_next example.pdf --formular-char-set-max-density 2.0`                                                          | `2.0`                                                               |
| `--formular-char-set-min-spacing`| Character set minimum spacing to identify formula text                                  | `pdf2zh_next example.pdf --formular-char-set-min-spacing 0.5`                                                          | `0.5`                                                               |
| `--formular-char-set-max-spacing`| Character set maximum spacing to identify formula text                                  | `pdf2zh_next example.pdf --formular-char-set-max-spacing 2.0`                                                          | `2.0`                                                               |
| `--formular-char-set-min-line-spacing`| Character set minimum line spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-line-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-line-spacing`| Character set maximum line spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-line-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-word-spacing`| Character set minimum word spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-word-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-word-spacing`| Character set maximum word spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-word-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-char-spacing`| Character set minimum character spacing to identify formula text                      | `pdf 极速翻译 example.pdf --formular-char-set-min-char-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-char-spacing`| Character set maximum character spacing to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-max-char-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-line-length`| Character set minimum line length to identify formula text                            | `pdf2zh_next example.pdf --formular-char 极速翻译-min-line-length 5`                                                    | `5`                                                                 |
| `--formular-char-set-max-line-length`| Character set maximum line length to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-max-line-length 15`                                                       | `15`                                                                |
| `--formular-char-set-min-line-width` | Character set minimum line width to identify formula text                             | `pdf2zh_next example.pdf --formular-char-set-min-line-width 5`                                                         | `极速翻译`                                                               |
| `--formular-char-set-max-line-width` | Character set maximum line width to identify formula text                             | `pdf2zh_next example.pdf --formular-char-set-max-line-width 15`                                                        | `15`                                                                |
| `--formular-char-set-min-line-height`| Character set minimum line height to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-min-line-height 5`                                                        | `5`                                                                 |
| `--formular-char-set-max-line-height`| Character set maximum line height to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-max-line-height 15`                                                       | `15`                                                                |
| `--formular-char-set-min-line-area`  | Character set minimum line area to identify formula text                              | `pdf2zh_next example.pdf --formular-char-set-min-line-area 25`                                                         | `25`                                                                |
| `--formular-char-set-max-line-area`  | Character set maximum line area to identify formula text                              | `pdf2zh_next example.pdf --formular-char-set-max-line-area 225`                                                        | `225`                                                               |
| `--formular-char-set-min-line-aspect`| Character set minimum line aspect ratio to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-min-line-aspect 0.5`                                                      | `0.5`                                                               |
| `--formular-char-set-max-line-aspect`| Character set maximum line aspect ratio to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set 极速翻译-line-aspect 2.0`                                                  | `2.0`                                                               |
| `--formular-char-set-min-line-density`| Character set minimum line density to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-line-density 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-line-density`| Character set maximum line density to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-line-density 2.极速翻译`                                                | `2.0`                                                               |
| `--formular-char-set-min-line-spacing`| Character set minimum line spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-line-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-line-spacing`| Character set maximum line spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-line-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-word-spacing`| Character set minimum word spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-word-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-word-spacing 极速翻译`| Character set maximum word spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-word-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-char-spacing`| Character set minimum character spacing to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-min-char-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-char-spacing`| Character set maximum character spacing to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-max-char-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-line-length`| Character set minimum line length to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-min-line-length 5`                                                        | `5`                                                                 |
| `--formular-char-set-max-line-length`| Character set maximum line length to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-max-line-length 15`                                                       | `15`                                                                |
| `--formular-char-set-min-line-width` | Character set minimum line width to identify formula text                             | `pdf2zh_next example.pdf --formular-char-set-min-line-width 5`                                                         | `5`                                                                 |
| `--formular-char-set-max-line-width` | Character set maximum line width to identify formula text                             | `pdf2zh_next example.pdf --formular-char-set-max-line-width 15`                                                        | `15`                                                                |
| `--formular-char-set-min-line-height`| Character set minimum line height to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-min-line-height 5`                                                        | `5`                                                                 |
| `--formular-char-set-max-line-height`| Character set maximum line height to identify formula text                            | `pdf2zh_next example.pdf --formular-char-set-max-line-height 15`                                                       | `15`                                                                |
| `--formular-char-set-min-line-area`  | Character set minimum line area to identify formula text                              | `pdf2zh_next example.pdf --formular-char-set-min-line-area 25`                                                        极速翻译 `25`                                                                |
| `--formular-char-set-max-line-area`  | Character set maximum line area to identify formula text                              | `pdf2zh_next example.pdf --formular-char-set-max-line-area 225`                                                        | `225`                                                               |
| `--formular-char-set-min-line-aspect`| Character set minimum line aspect ratio to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-min-line-aspect 0.5`                                                      | `0.5`                                                               |
| `--formular-char-set-max-line-aspect`| Character set maximum line aspect ratio to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-max-line-aspect 2.0`                                                      | `2.0`                                                               |
| `--formular-char-set-min-line-density`| Character set minimum line density to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-line-density 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-line-density`| Character set maximum line density to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-line-density 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-line-spacing`| Character set minimum line spacing to identify formula text                          | `pdf2zh_next example.pdf --极速翻译-char-set-min-line-spacing 0.5`                                                     | `极速翻译`                                                               |
| `--formular-char-set-max-line-spacing`| Character set maximum line spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-line-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-word-spacing`| Character set minimum word spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-min-word-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-word-spacing`| Character set maximum word spacing to identify formula text                          | `pdf2zh_next example.pdf --formular-char-set-max-word-spacing 2.0`                                                     | `2.0`                                                               |
| `--formular-char-set-min-char-spacing`| Character set minimum character spacing to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-min-char-spacing 0.5`                                                     | `0.5`                                                               |
| `--formular-char-set-max-char-spacing`| Character set maximum character spacing to identify formula text                      | `pdf2zh_next example.pdf --formular-char-set-max-char-spacing 2.0`                                                     | `2.0`                                                               |

---

### OUTPUT LANGUAGE

es
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-pattern-flags` | Flags for the formula character pattern regex                                          | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-flags "i"`                           |
| `--formular-char-pattern-repl`  | Replacement for the formula character pattern                                          | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-repl "Microsoft $1"`                |
| `--formular-char-patterns-file` | Path to a file containing formula character patterns and their replacements             | `pdf2zh_next example.pdf --formular-char-patterns-file formular_char_patterns.txt`                                    |
| `--formular-char-patterns-json` | JSON string containing formula character patterns and their replacements                | `pdf2zh_next example.pdf --formular-char-patterns-json '[{"pattern": "(MS.*)", "repl": "Microsoft $1", "flags": "i"}]'` |

---

### OUTPUT LANGUAGE

es

---

### OUTPUT

| `--formular-char-pattern`       | Patrón de caracteres para identificar texto de fórmula                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-char-pattern-flags` | Banderas para la expresión regular del patrón de caracteres de fórmula                                          | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-flags "i"`                           |
| `--formular-char-pattern-repl`  | Reemplazo para el patrón de caracteres de fórmula                                          | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)" --formular-char-pattern-repl "Microsoft $1"`                |
| `--formular-char-patterns-file` | Ruta a un archivo que contiene patrones de caracteres de fórmula y sus reemplazos             | `pdf2zh_next example.pdf --formular-char-patterns-file formular_char_patterns.txt`                                    |
| `--formular-char-patterns-json` | Cadena JSON que contiene patrones de caracteres de fórmula y sus reemplazos                | `pdf2zh_next example.pdf --formular-char-patterns-json '[{"pattern": "(MS.*)", "repl": "Microsoft $1", "flags": "i"}]'` |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-bbox-extension <value>`| Extend the bounding box by a certain distance when splitting paragraphs (unit: pixels) | `pdf2zh_next example.pdf --split-bbox-extension 10`                                                                   |
| `--split-line-threshold <value>`| Threshold for determining whether two lines are on the same line (unit: pixels)         | `pdf2zh_next example.pdf --split-line-threshold 5`                                                                    |
| `--split-paragraph-threshold <value>` | Threshold for determining whether two lines belong to the same paragraph (unit: pixels) | `pdf2zh_next example.pdf --split-paragraph-threshold 10`                                                              |
| `--split-columns`               | Enable multi-column layout analysis to split paragraphs correctly in multi-column layouts | `pdf2zh_next example.pdf --split-columns`                                                                             |

---

### OUTPUT

| `--split-short-lines`           | Forzar la división de líneas cortas en diferentes párrafos                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-bbox-extension <value>`| Extender el cuadro delimitador por una cierta distancia al dividir párrafos (unidad: píxeles) | `pdf2zh_next example.pdf --split-bbox-extension 10`                                                                   |
| `--split-line-threshold <value>`| Umbral para determinar si dos líneas están en la misma línea (unidad: píxeles)         | `pdf2zh_next example.pdf --split-line-threshold 5`                                                                    |
| `--split-paragraph-threshold <value>` | Umbral para determinar si dos líneas pertenecen al mismo párrafo (unidad: píxeles) | `pdf2zh_next example.pdf --split-paragraph-threshold 10`                                                              |
| `--split-columns`               | Habilitar el análisis de diseño de varias columnas para dividir párrafos correctamente en diseños de varias columnas | `pdf2zh_next example.pdf --split-columns`                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--short-line-split-limit`      | Split limit for short lines                                                             | `pdf2zh_next example.pdf --short-line-split-limit 20`                                                                  |
| `--short-line-split-min-length` | Minimum length of a short line to be considered for splitting (in characters)           | `pdf2zh_next example.pdf --short-line-split-min-length 20`                                                             |
| `--short-line-merge-factor`     | Merge threshold factor for short lines                                                  | `pdf2zh_next example.pdf --short-line-merge-factor 1.2`                                                                |
| `--short-line-merge-limit`      | Merge limit for short lines                                                             | `pdf2zh_next example.pdf --short-line-merge-limit 20`                                                                  |
| `--short-line-merge-min-length` | Minimum length of a short line to be considered for merging (in characters)             | `pdf2zh_next example.pdf --short-line-merge-min-length 20`                                                             |
| `--short-line-merge-max-length` | Maximum length of a short line to be considered for merging (in characters)             | `pdf2zh_next example.pdf --short-line-merge-max-length 80`                                                             |
| `--short-line-merge-same-page`  | Only merge short lines that are on the same page                                        | `pdf2zh_next example.pdf --short-line-merge-same-page`                                                                 |
| `--short-line-merge-same-font`  | Only merge short lines that have the same font                                          | `pdf2zh_next example.pdf --short-line-merge-same-font`                                                                 |
| `--short-line-merge-same-size`  | Only merge short lines that have the same font size                                     | `pdf2zh_next example.pdf --short-line-merge-same-size`                                                                 |
| `--short-line-merge-same-color` | Only merge short lines that have the same color                                         | `pdf2zh_next example.pdf --short-line-merge-same-color`                                                                |

---

### OUTPUT

| `--short-line-split-factor`     | Factor de umbral de división para líneas cortas                                         | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--short-line-split-limit`      | Límite de división para líneas cortas                                                   | `pdf2zh_next example.pdf --short-line-split-limit 20`                                                                  |
| `--short-line-split-min-length` | Longitud mínima de una línea corta para ser considerada para división (en caracteres)   | `pdf2zh_next example.pdf --short-line-split-min-length 20`                                                             |
| `--short-line-merge-factor`     | Factor de umbral de fusión para líneas cortas                                           | `pdf2zh_next example.pdf --short-line-merge-factor 1.2`                                                                |
| `--short-line-merge-limit`      | Límite de fusión para líneas cortas                                                     | `pdf2zh_next example.pdf --short-line-merge-limit 20`                                                                  |
| `--short-line-merge-min-length` | Longitud mínima de una línea corta para ser considerada para fusión (en caracteres)     | `pdf2zh_next example.pdf --short-line-merge-min-length 20`                                                             |
| `--short-line-merge-max-length` | Longitud máxima de una línea corta para ser considerada para fusión (en caracteres)     | `pdf2zh_next example.pdf --short-line-merge-max-length 80`                                                             |
| `--short-line-merge-same-page`  | Solo fusionar líneas cortas que estén en la misma página                                | `pdf2zh_next example.pdf --short-line-merge-same-page`                                                                 |
| `--short-line-merge-same-font`  | Solo fusionar líneas cortas que tengan la misma fuente                                  | `pdf2zh_next example.pdf --short-line-merge-same-font`                                                                 |
| `--short-line-merge-same-size`  | Solo fusionar líneas cortas que tengan el mismo tamaño de fuente                        | `pdf2zh_next example.pdf --short-line-merge-same-size`                                                                 |
| `--short-line-merge-same-color` | Solo fusionar líneas cortas que tengan el mismo color                                   | `pdf2zh_next example.pdf --short-line-merge-same-color`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | Skip OCR step                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-text-extraction`        | Skip text extraction step                                                               | `pdf2zh_next example.pdf --skip-text-extraction`                                                                      |
| `--skip-text-reconstruction`    | Skip text reconstruction step                                                           | `pdf2zh_next example.pdf --skip-text-reconstruction`                                                                  |
| `--skip-layout-analysis`        | Skip layout analysis step                                                               | `pdf2zh_next example.pdf --skip-layout-analysis`                                                                      |
| `--skip-table-detection`        | Skip table detection step                                                               | `pdf2zh_next example.pdf --skip-table-detection`                                                                      |
| `--skip-equation-detection`     | Skip equation detection step                                                            | `pdf2zh_next example.pdf --skip-equation-detection`                                                                   |
| `--skip-image-detection`        | Skip image detection step                                                               | `pdf2zh_next example.pdf --skip-image-detection`                                                                      |
| `--skip-rendering`              | Skip rendering step                                                                     | `pdf2zh_next example.pdf --skip-rendering`                                                                            |
| `--skip-pdf-generation`         | Skip PDF generation step                                                                | `pdf2zh_next example.pdf --skip-pdf-generation`                                                                       |
| `--skip-postprocessing`         | Skip postprocessing step                                                                | `pdf2zh_next example.pdf --skip-postprocessing`                                                                       |
| `--skip-all`                    | Skip all steps (equivalent to `--skip-clean --skip-translate ... --skip-postprocessing`) | `pdf2zh_next example.pdf --skip-all`                                                                                  |

---

### OUTPUT

| `--skip-clean`                  | Omitir paso de limpieza de PDF                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--skip-translate`              | Omitir paso de traducción                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            |
| `--skip-ocr`                    | Omitir paso de OCR                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  |
| `--skip-text-extraction`        | Omitir paso de extracción de texto                                                               | `pdf2zh_next example.pdf --skip-text-extraction`                                                                      |
| `--skip-text-reconstruction`    | Omitir paso de reconstrucción de texto                                                           | `pdf2zh_next example.pdf --skip-text-reconstruction`                                                                  |
| `--skip-layout-analysis`        | Omitir paso de análisis de diseño                                                               | `pdf2zh_next example.pdf --skip-layout-analysis`                                                                      |
| `--skip-table-detection`        | Omitir paso de detección de tablas                                                               | `pdf2zh_next example.pdf --skip-table-detection`                                                                      |
| `--skip-equation-detection`     | Omitir paso de detección de ecuaciones                                                            | `pdf2zh_next example.pdf --skip-equation-detection`                                                                   |
| `--skip-image-detection`        | Omitir paso de detección de imágenes                                                               | `pdf2zh_next example.pdf --skip-image-detection`                                                                      |
| `--skip-rendering`              | Omitir paso de renderizado                                                                     | `pdf2zh_next example.pdf --skip-rendering`                                                                            |
| `--skip-pdf-generation`         | Omitir paso de generación de PDF                                                                | `pdf2zh_next example.pdf --skip-pdf-generation`                                                                       |
| `--skip-postprocessing`         | Omitir paso de postprocesado                                                                | `pdf2zh_next example.pdf --skip-postprocessing`                                                                       |
| `--skip-all`                    | Omitir todos los pasos (equivalente a `--skip-clean --skip-translate ... --skip-postprocessing`) | `pdf2zh_next example.pdf --skip-all`                                                                                  |
| `--dual-translate-second`       | Put translated pages second in dual PDF mode                                            | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `--dual-translate-both`         | Put translated pages both first and second in dual PDF mode                             | `pdf2zh_next example.pdf --dual-translate-both`                                                                       |
| `--dual-translate-none`         | Do not put translated pages in dual PDF mode                                            | `pdf2zh_next example.pdf --dual-translate-none`                                                                       |
| `--dual-translate-first`        | Colocar las páginas traducidas primero en modo PDF dual                                 | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-second`       | Colocar las páginas traducidas segundo en modo PDF dual                                 | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `--dual-translate-both`         | Colocar las páginas traducidas tanto primero como segundo en modo PDF dual              | `pdf2zh_next example.pdf --dual-translate-both`                                                                       |
| `--dual-translate-none`         | No colocar páginas traducidas en modo PDF dual                                          | `pdf2zh_next example.pdf --dual-translate-none`                                                                       |

---

### OUTPUT LANGUAGE

es

---

### TRANSLATION RESULT

| `--dual-translate-first`        | Colocar las páginas traducidas primero en modo PDF dual                                 | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--dual-translate-second`       | Colocar las páginas traducidas segundo en modo PDF dual                                 | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `--dual-translate-both`         | Colocar las páginas traducidas tanto primero como segundo en modo PDF dual              | `pdf2zh_next example.pdf --dual-translate-both`                                                                       |
| `--dual-translate-none`         | No colocar páginas traducidas en modo PDF dual                                          | `pdf2zh_next example.pdf --dual-translate-none`                                                                       |
`-drt`                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `--disable-formula-translate`   | Disable formula translation                                                             | `pdf2zh_next example.pdf --disable-formula-translate`                                                                 | `-dfm`                   |
| `--hide-page-number`            | Hide page numbers in the output PDF                                                     | `pdf2zh_next example.pdf --hide-page-number`                                                                          | `-hpn`                   |
| `--hide-footer`                 | Hide footers in the output PDF                                                          | `pdf2zh_next example.pdf --hide-footer`                                                                               | `-hf`                    |
| `--hide-header`                 | Hide headers in the output PDF                                                          | `pdf2zh_next example.pdf --hide-header`                                                                               | `-hh`                    |
| `--hide-table`                  | Hide tables in the output PDF                                                           | `pdf2zh_next example.pdf --hide-table`                                                                                | `-ht`                    |
| `--hide-image`                  | Hide images in the output PDF                                                           | `pdf2zh_next example.pdf --hide-image`                                                                                | `-hi`                    |
| `--hide-link`                   | Hide hyperlinks in the output PDF                                                       | `pdf2zh_next example.pdf --hide-link`                                                                                 | `-hl`                    |
| `--hide-textbox`                | Hide textboxes in the output PDF                                                        | `pdf2zh_next example.pdf --hide-textbox`                                                                              | `-htb`                   |
| `--hide-annotation`             | Hide annotations in the output PDF                                                      | `pdf2zh_next example.pdf --hide-annotation`                                                                           | `-ha`                    |
| `--hide-shape`                  | Hide shapes in the output PDF                                                           | `pdf2zh_next example.pdf --hide-shape`                                                                                | `-hs`                    |
| `--hide-line`                   | Hide lines in the output PDF                                                            | `pdf2zh_next example.pdf --hide-line`                                                                                 | `-hl`                    |
| `--hide-arrow`                  | Hide arrows in the output PDF                                                           | `pdf2zh_next example.pdf --hide-arrow`                                                                                | `-ha`                    |
| `--hide-graphic`                | Hide graphics in the output PDF                                                         | `pdf2zh_next example.pdf --hide-graphic`                                                                              | `-hg`                    |

---

### TRANSLATED TEXT

| `--disable-rich-text-translate` | Desactivar la traducción de texto enriquecido                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               | `-drt`                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `--disable-formula-translate`   | Desactivar la traducción de fórmulas                                                    | `pdf2zh_next example.pdf --disable-formula-translate`                                                                 | `-dfm`                   |
| `--hide-page-number`            | Ocultar números de página en el PDF de salida                                           | `pdf2zh_next example.pdf --hide-page-number`                                                                          | `-hpn`                   |
| `--hide-footer`                 | Ocultar pies de página en el PDF de salida                                              | `pdf2zh_next example.pdf --hide-footer`                                                                               | `-hf`                    |
| `--hide-header`                 | Ocultar encabezados en el PDF de salida                                                 | `pdf2zh_next example.pdf --hide-header`                                                                               | `-hh`                    |
| `--hide-table`                  | Ocultar tablas en el PDF de salida                                                      | `pdf2zh_next example.pdf --hide-table`                                                                                | `-ht`                    |
| `--hide-image`                  | Ocultar imágenes en el PDF de salida                                                    | `pdf2zh_next example.pdf --hide-image`                                                                                | `-hi`                    |
| `--hide-link`                   | Ocultar hipervínculos en el PDF de salida                                               | `pdf2zh_next example.pdf --hide-link`                                                                                 | `-hl`                    |
| `--hide-textbox`                | Ocultar cuadros de texto en el PDF de salida                                            | `pdf2zh_next example.pdf --hide-textbox`                                                                              | `-htb`                   |
| `--hide-annotation`             | Ocultar anotaciones en el PDF de salida                                                 | `pdf2zh_next example.pdf --hide-annotation`                                                                           | `-ha`                    |
| `--hide-shape`                  | Ocultar formas en el PDF de salida                                                      | `pdf2zh_next example.pdf --hide-shape`                                                                                | `-hs`                    |
| `--hide-line`                   | Ocultar líneas en el PDF de salida                                                      | `pdf2zh_next example.pdf --hide-line`                                                                                 | `-hl`                    |
| `--hide-arrow`                  | Ocultar flechas en el PDF de salida                                                     | `pdf2zh_next example.pdf --hide-arrow`                                                                                | `-ha`                    |
| `--hide-graphic`                | Ocultar gráficos en el PDF de salida                                                    | `pdf2zh_next example.pdf --hide-graphic`                                                                              | `-hg`                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-ignore` | Disable all compatibility enhancement options                                           | `pdf2zh_next example.pdf --enhance-compatibility-ignore`                                                              |
| `--use-ai-translate`            | Enable AI translation (requires additional configuration)                               | `pdf2zh_next example.pdf --use-ai-translate`                                                                          |
| `--use-ai-translate-ignore`     | Disable AI translation                                                                  | `pdf2zh_next example.pdf --use-ai-translate-ignore`                                                                   |
| `--use-ai-translate-api-key`    | Set the API key for AI translation                                                      | `pdf2zh_next example.pdf --use-ai-translate-api-key sk-xxxxxxxx`                                                      |
| `--use-ai-translate-base-url`   | Set the base URL for AI translation (for services compatible with OpenAI API)           | `pdf2zh_next example.pdf --use-ai-translate-base-url https://api.openai.com/v1`                                       |
| `--use-ai-translate-model`      | Set the model for AI translation (default: gpt-4o-mini)                                 | `pdf2zh_next example.pdf --use-ai-translate-model gpt-4o`                                                             |
| `--use-ai-translate-prompt`     | Set the prompt for AI translation (default: Translate the following text to Chinese)     | `pdf2zh_next example.pdf --use-ai-translate-prompt "Translate the following text to Chinese"`                         |
| `--use-ai-translate-language`   | Set the target language for AI translation (default: Chinese)                           | `pdf2zh_next example.pdf --use-ai-translate-language Spanish`                                                         |
| `--use-ai-translate-temperature`| Set the temperature for AI translation (default: 0.0)                                   | `pdf2zh_next example.pdf --use-ai-translate-temperature 0.7`                                                          |
| `--use-ai-translate-max-tokens` | Set the maximum tokens for AI translation (default: 4096)                               | `pdf2zh_next example.pdf --use-ai-translate-max-tokens 8192`                                                          |
| `--use-ai-translate-timeout`    | Set the timeout for AI translation (default: 60)                                        | `pdf2zh_next example.pdf --use-ai-translate-timeout 120`                                                              |
| `--use-ai-translate-retry`      | Set the retry times for AI translation (default: 3)                                     | `pdf2zh_next example.pdf --use-ai-translate-retry 5`                                                                  |
| `--use-ai-translate-retry-delay`| Set the retry delay for AI translation (default: 1)                                     | `pdf2zh_next example.pdf --use-ai-translate-retry-delay 2`                                                            |
| `--use-ai-translate-proxy`      | Set the proxy for AI translation                                                        | `pdf2zh_next example.pdf --use-ai-translate-proxy http://127.0.0.1:7890`                                              |
| `--use-ai-translate-org-id`     | Set the organization ID for AI translation (for OpenAI API)                             | `pdf2zh_next example.pdf --use-ai-translate-org-id org-xxxxxxxx`                                                      |
| `--use-ai-translate-project`    | Set the project for AI translation (for OpenAI API)                                     | `pdf2zh_next example.pdf --use-ai-translate-project proj-xxxxxxxx`                                                    |

---

### TRANSLATION RESULT

| `--enhance-compatibility`       | Habilitar todas las opciones de mejora de compatibilidad                                | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-compatibility-ignore` | Deshabilitar todas las opciones de mejora de compatibilidad                             | `pdf2zh_next example.pdf --enhance-compatibility-ignore`                                                              |
| `--use-ai-translate`            | Habilitar traducción por IA (requiere configuración adicional)                          | `pdf2zh_next example.pdf --use-ai-translate`                                                                          |
| `--use-ai-translate-ignore`     | Deshabilitar traducción por IA                                                          | `pdf2zh_next example.pdf --use-ai-translate-ignore`                                                                   |
| `--use-ai-translate-api-key`    | Establecer la clave API para la traducción por IA                                       | `pdf2zh_next example.pdf --use-ai-translate-api-key sk-xxxxxxxx`                                                      |
| `--use-ai-translate-base-url`   | Establecer la URL base para la traducción por IA (para servicios compatibles con la API de OpenAI) | `pdf2zh_next example.pdf --use-ai-translate-base-url https://api.openai.com/v1`                                       |
| `--use-ai-translate-model`      | Establecer el modelo para la traducción por IA (predeterminado: gpt-4o-mini)            | `pdf2zh_next example.pdf --use-ai-translate-model gpt-4o`                                                             |
| `--use-ai-translate-prompt`     | Establecer el prompt para la traducción por IA (predeterminado: Translate the following text to Chinese) | `pdf2zh_next example.pdf --use-ai-translate-prompt "Translate the following text to Chinese"`                         |
| `--use-ai-translate-language`   | Establecer el idioma de destino para la traducción por IA (predeterminado: Chinese)      | `pdf2zh_next example.pdf --use-ai-translate-language Spanish`                                                         |
| `--use-ai-translate-temperature`| Establecer la temperatura para la traducción por IA (predeterminado: 0.0)               | `pdf2zh_next example.pdf --use-ai-translate-temperature 0.7`                                                          |
| `--use-ai-translate-max-tokens` | Establecer el máximo de tokens para la traducción por IA (predeterminado: 4096)         | `pdf2zh_next example.pdf --use-ai-translate-max-tokens 8192`                                                          |
| `--use-ai-translate-timeout`    | Establecer el tiempo de espera para la traducción por IA (predeterminado: 60)           | `pdf2zh_next example.pdf --use-ai-translate-timeout 120`                                                              |
| `--use-ai-translate-retry`      | Establecer el número de reintentos para la traducción por IA (predeterminado: 3)        | `pdf2zh_next example.pdf --use-ai-translate-retry 5`                                                                  |
| `--use-ai-translate-retry-delay`| Establecer el retraso de reintento para la traducción por IA (predeterminado: 1)        | `pdf2zh_next example.pdf --use-ai-translate-retry-delay 2`                                                            |
| `--use-ai-translate-proxy`      | Establecer el proxy para la traducción por IA                                           | `pdf2zh_next example.pdf --use-ai-translate-proxy http://127.0.0.1:7890`                                              |
| `--use-ai-translate-org-id`     | Establecer el ID de organización para la traducción por IA (para la API de OpenAI)      | `pdf2zh_next example.pdf --use-ai-translate-org-id org-xxxxxxxx`                                                      |
| `--use-ai-translate-project`    | Establecer el proyecto para la traducción por IA (para la API de OpenAI)                | `pdf2zh_next example.pdf --use-ai-translate-project proj-xxxxxxxx`                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-column-layout`           | Use column layout mode                                                                  | `pdf2zh_next example.pdf --use-column-layout`                                                                         |
| `--use-paragraph-layout`        | Use paragraph layout mode                                                               | `pdf2zh_next example.pdf --use-paragraph-layout`                                                                      |
| `--use-text-layout`             | Use text layout mode                                                                    | `pdf2zh_next example.pdf --use-text-layout`                                                                           |

---

### OUTPUT

| `--use-alternating-pages-dual`  | Usar modo de páginas alternas para PDF dual                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Usar modo de páginas alternas para PDF único                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                              |
| `--use-column-layout`           | Usar modo de diseño en columnas                                                                  | `pdf2zh_next example.pdf --use-column-layout`                                                                         |
| `--use-paragraph-layout`        | Usar modo de diseño de párrafos                                                               | `pdf2zh_next example.pdf --use-paragraph-layout`                                                                      |
| `--use-text-layout`             | Usar modo de diseño de texto                                                                    | `pdf2zh_next example.pdf --use-text-layout`                                                                           |
`no_watermark`             |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------|
| `--watermark-text`              | Watermark text                                                                          | `pdf2zh_next example.pdf --watermark-text "Translated by pdf2zh"`                                                     | `Translated by pdf2zh`     |
| `--watermark-font-name`         | Watermark font name                                                                     | `pdf2zh_next example.pdf --watermark-font-name "Arial"`                                                               | `Helvetica`                |
| `--watermark-font-size`         | Watermark font size                                                                     | `pdf2zh_next example.pdf --watermark-font-size 24`                                                                    | `32`                       |
| `--watermark-font-color`        | Watermark font color                                                                    | `pdf2zh_next example.pdf --watermark-font-color "#000000"`                                                            | `"#000000"`                |
| `--watermark-opacity`           | Watermark opacity (0-1)                                                                 | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     | `0.3`                      |
| `--watermark-rotation`          | Watermark rotation angle (degrees)                                                      | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     | `45`                       |
| `--watermark-position`          | Watermark position (e.g., "center", "top-left", "bottom-right")                         | `pdf2zh_next example.pdf --watermark-position "center"`                                                               | `"center"`                 |
| `--watermark-spacing`           | Watermark spacing (pixels)                                                              | `pdf2zh_next example.pdf --watermark-spacing 100`                                                                     | `100`                      |

---

### TRANSLATION

| `--watermark-output-mode`       | Modo de salida de marca de agua para archivos PDF                                       | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `no_watermark`             |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------|
| `--watermark-text`              | Texto de la marca de agua                                                               | `pdf2zh_next example.pdf --watermark-text "Translated by pdf2zh"`                                                     | `Translated by pdf2zh`     |
| `--watermark-font-name`         | Nombre de la fuente de la marca de agua                                                 | `pdf2zh_next example.pdf --watermark-font-name "Arial"`                                                               | `Helvetica`                |
| `--watermark-font-size`         | Tamaño de la fuente de la marca de agua                                                 | `pdf2zh_next example.pdf --watermark-font-size 24`                                                                    | `32`                       |
| `--watermark-font-color`        | Color de la fuente de la marca de agua                                                  | `pdf2zh_next example.pdf --watermark-font-color "#000000"`                                                            | `"#000000"`                |
| `--watermark-opacity`           | Opacidad de la marca de agua (0-1)                                                      | `pdf2zh_next example.pdf --watermark-opacity 0.5`                                                                     | `0.3`                      |
| `--watermark-rotation`          | Ángulo de rotación de la marca de agua (grados)                                         | `pdf2zh_next example.pdf --watermark-rotation 45`                                                                     | `45`                       |
| `--watermark-position`          | Posición de la marca de agua (por ejemplo, "center", "top-left", "bottom-right")        | `pdf2zh_next example.pdf --watermark-position "center"`                                                               | `"center"`                 |
| `--watermark-spacing`           | Espaciado de la marca de agua (píxeles)                                                 | `pdf2zh_next example.pdf --watermark-spacing 100`                                                                     | `100`                      |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--max-tokens-per-part`         | Maximum tokens per part for split translation                                           | `pdf2zh_next example.pdf --max-tokens-per-part 1000`                                                                  |
| `--min-chars-per-part`          | Minimum characters per part for split translation                                       | `pdf2zh_next example.pdf --min-chars-per-part 100`                                                                    |
| `--max-chars-per-part`          | Maximum characters per part for split translation                                       | `pdf2zh_next example.pdf --max-chars-per-part 5000`                                                                   |
| `--max-tokens-per-request`      | Maximum tokens per request for translation                                              | `pdf2zh_next example.pdf --max-tokens-per-request 1000`                                                               |
| `--max-requests-per-minute`     | Maximum requests per minute for translation                                             | `pdf2zh_next example.pdf --max-requests-per-minute 10`                                                                |
| `--max-requests-per-hour`       | Maximum requests per hour for translation                                               | `pdf2zh_next example.pdf --max-requests-per-hour 100`                                                                 |
| `--max-requests-per-day`        | Maximum requests per day for translation                                                | `pdf2zh_next example.pdf --max-requests-per-day 1000`                                                                 |
| `--max-requests-per-month`      | Maximum requests per month for translation                                              | `pdf2zh_next example.pdf --max-requests-per-month 10000`                                                              |
| `--max-requests-per-translator` | Maximum requests per translator for translation (for multiple translators configuration) | `pdf2zh_next example.pdf --max-requests-per-translator 1000`                                                          |
| `--translator`                  | Translator to use (e.g., `google`, `azure`, `openai`, `deepl`, `claude`, `gemini`, etc.) | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-config`           | Configuration file for translator                                                       | `pdf2zh_next example.pdf --translator-config config.json`                                                             |
| `--translator-params`           | Parameters for translator (JSON string)                                                 | `pdf2zh_next example.pdf --translator-params '{"api_key": "your_api_key", "model": "gpt-4"}'`                         |
| `--translator-timeout`          | Timeout for translator request (in seconds)                                             | `pdf2zh_next example.pdf --translator-timeout 30`                                                                     |
| `--translator-retries`          | Number of retries for translator request                                                | `pdf2zh_next example.pdf --translator-retries 3`                                                                      |
| `--translator-retry-delay`      | Delay between retries for translator request (in seconds)                               | `pdf2zh_next example.pdf --translator-retry-delay 5`                                                                  |
| `--translator-concurrency`      | Number of concurrent requests for translator                                            | `pdf2zh_next example.pdf --translator-concurrency 5`                                                                  |
| `--translator-pool-size`        | Size of translator pool (for multiple translators configuration)                        | `pdf2zh_next example.pdf --translator-pool-size 3`                                                                    |
| `--translator-pool-strategy`    | Strategy for translator pool (e.g., `round-robin`, `random`, `weighted`)                | `pdf2zh_next example.pdf --translator-pool-strategy round-robin`                                                      |
| `--translator-pool-weights`     | Weights for translator pool (JSON string)                                               | `pdf2zh_next example.pdf --translator-pool-weights '{"google": 1, "azure": 2, "openai": 3}'`                          |
| `--translator-pool-timeout`     | Timeout for translator pool (in seconds)                                                | `pdf2zh_next example.pdf --translator-pool-timeout 30`                                                                |
| `--translator-pool-retries`     | Number of retries for translator pool                                                   | `pdf2zh_next example.pdf --translator-pool-retries 3`                                                                 |
| `--translator-pool-retry-delay` | Delay between retries for translator pool (in seconds)                                  | `pdf2zh_next example.pdf --translator-pool-retry-delay 5`                                                             |
| `--translator-pool-concurrency` | Number of concurrent requests for translator pool                                       | `pdf2zh_next example.pdf --translator-pool-concurrency 5`                                                             |
| `--translator-pool-max-size`    | Maximum size of translator pool                                                         | `pdf2zh_next example.pdf --translator-pool-max-size 10`                                                               |
| `--translator-pool-min-size`    | Minimum size of translator pool                                                         | `pdf2zh_next example.pdf --translator-pool-min-size 1`                                                                |
| `--translator-pool-max-requests`| Maximum requests per translator in pool                                                 | `pdf2zh_next example.pdf --translator-pool-max-requests 1000`                                                         |

---

### TRANSLATION

| `--max-pages-per-part`          | Máximo de páginas por parte para traducción dividida                                   | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--max-tokens-per-part`         | Máximo de tokens por parte para traducción dividida                                     | `pdf2zh_next example.pdf --max-tokens-per-part 1000`                                                                  |
| `--min-chars-per-part`          | Mínimo de caracteres por parte para traducción dividida                                 | `pdf2zh_next example.pdf --min-chars-per-part 100`                                                                    |
| `--max-chars-per-part`          | Máximo de caracteres por parte para traducción dividida                                 | `pdf2zh_next example.pdf --max-chars-per-part 5000`                                                                   |
| `--max-tokens-per-request`      | Máximo de tokens por solicitud para traducción                                          | `pdf2zh_next example.pdf --max-tokens-per-request 1000`                                                               |
| `--max-requests-per-minute`     | Máximo de solicitudes por minuto para traducción                                        | `pdf2zh_next example.pdf --max-requests-per-minute 10`                                                                |
| `--max-requests-per-hour`       | Máximo de solicitudes por hora para traducción                                          | `pdf2zh_next example.pdf --max-requests-per-hour 100`                                                                 |
| `--max-requests-per-day`        | Máximo de solicitudes por día para traducción                                           | `pdf2zh_next example.pdf --max-requests-per-day 1000`                                                                 |
| `--max-requests-per-month`      | Máximo de solicitudes por mes para traducción                                           | `pdf2zh_next example.pdf --max-requests-per-month 10000`                                                              |
| `--max-requests-per-translator` | Máximo de solicitudes por traductor para traducción (para configuración de múltiples traductores) | `pdf2zh_next example.pdf --max-requests-per-translator 1000`                                                          |
| `--translator`                  | Traductor a utilizar (por ejemplo, `google`, `azure`, `openai`, `deepl`, `claude`, `gemini`, etc.) | `pdf2zh_next example.pdf --translator google`                                                                         |
| `--translator-config`           | Archivo de configuración para el traductor                                              | `pdf2zh_next example.pdf --translator-config config.json`                                                             |
| `--translator-params`           | Parámetros para el traductor (cadena JSON)                                              | `pdf2zh_next example.pdf --translator-params '{"api_key": "your_api_key", "model": "gpt-4"}'`                         |
| `--translator-timeout`          | Tiempo de espera para la solicitud del traductor (en segundos)                          | `pdf2zh_next example.pdf --translator-timeout 30`                                                                     |
| `--translator-retries`          | Número de reintentos para la solicitud del traductor                                    | `pdf2zh_next example.pdf --translator-retries 3`                                                                      |
| `--translator-retry-delay`      | Retraso entre reintentos para la solicitud del traductor (en segundos)                  | `pdf2zh_next example.pdf --translator-retry-delay 5`                                                                  |
| `--translator-concurrency`      | Número de solicitudes concurrentes para el traductor                                    | `pdf2zh_next example.pdf --translator-concurrency 5`                                                                  |
| `--translator-pool-size`        | Tamaño del grupo de traductores (para configuración de múltiples traductores)           | `pdf2zh_next example.pdf --translator-pool-size 3`                                                                    |
| `--translator-pool-strategy`    | Estrategia para el grupo de traductores (por ejemplo, `round-robin`, `random`, `weighted`) | `pdf2zh_next example.pdf --translator-pool-strategy round-robin`                                                      |
| `--translator-pool-weights`     | Pesos para el grupo de traductores (cadena JSON)                                        | `pdf2zh_next example.pdf --translator-pool-weights '{"google": 1, "azure": 2, "openai": 3}'`                          |
| `--translator-pool-timeout`     | Tiempo de espera para el grupo de traductores (en segundos)                             | `pdf2zh_next example.pdf --translator-pool-timeout 30`                                                                |
| `--translator-pool-retries`     | Número de reintentos para el grupo de traductores                                       | `pdf2zh_next example.pdf --translator-pool-retries 3`                                                                 |
| `--translator-pool-retry-delay` | Retraso entre reintentos para el grupo de traductores (en segundos)                     | `pdf2zh_next example.pdf --translator-pool-retry-delay 5`                                                             |
| `--translator-pool-concurrency` | Número de solicitudes concurrentes para el grupo de traductores                         | `pdf2zh_next example.pdf --translator-pool-concurrency 5`                                                             |
| `--translator-pool-max-size`    | Tamaño máximo del grupo de traductores                                                  | `pdf2zh_next example.pdf --translator-pool-max-size 10`                                                               |
| `--translator-pool-min-size`    | Tamaño mínimo del grupo de traductores                                                  | `pdf2zh_next example.pdf --translator-pool-min-size 1`                                                                |
| `--translator-pool-max-requests`| Máximo de solicitudes por traductor en el grupo                                         | `pdf2zh_next example.pdf --translator-pool-max-requests 1000`                                                         |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Method to translate table text. Options: `line-by-line`, `table`. Default: `line-by-line` | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method table`                                  |
| `--translate-table-text-engine` | Translation engine to use for table text. Default: same as `--engine`                   | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-engine google`                                 |

---

### OUTPUT

| `--translate-table-text`        | Traducir texto de tablas (experimental)                                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| :------------------------------ | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Método para traducir texto de tablas. Opciones: `line-by-line`, `table`. Por defecto: `line-by-line` | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-method table`                                  |
| `--translate-table-text-engine` | Motor de traducción a utilizar para el texto de tablas. Por defecto: igual que `--engine`                   | `pdf2zh_next example.pdf --translate-table-text --translate-table-text-engine google`                                 |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--skip-table-detection`        | Skip table detection                                                                     | `pdf2zh_next example.pdf --skip-table-detection`                                                                       |
| `--skip-equation-detection`     | Skip equation detection                                                                  | `pdf2zh_next example.pdf --skip-equation-detection`                                                                    |
| `--skip-figure-detection`       | Skip figure detection                                                                    | `pdf2zh_next example.pdf --skip-figure-detection`                                                                      |
| `--skip-header-footer-detection`| Skip header and footer detection                                                         | `pdf2zh_next example.pdf --skip-header-footer-detection`                                                               |
| `--skip-footnote-detection`     | Skip footnote detection                                                                  | `pdf2zh_next example.pdf --skip-footnote-detection`                                                                    |
| `--skip-reference-detection`    | Skip reference detection                                                                 | `pdf2zh_next example.pdf --skip-reference-detection`                                                                   |
| `--skip-abstract-detection`     | Skip abstract detection                                                                  | `pdf2zh_next example.pdf --skip-abstract-detection`                                                                    |
| `--skip-keywords-detection`     | Skip keywords detection                                                                  | `pdf2zh_next example.pdf --skip-keywords-detection`                                                                    |
| `--skip-title-detection`        | Skip title detection                                                                     | `pdf2zh_next example.pdf --skip-title-detection`                                                                       |
| `--skip-author-detection`       | Skip author detection                                                                    | `pdf2zh_next example.pdf --skip-author-detection`                                                                      |
| `--skip-date-detection`         | Skip date detection                                                                      | `pdf2zh_next example.pdf --skip-date-detection`                                                                        |
| `--skip-institution-detection`  | Skip institution detection                                                               | `pdf2zh_next example.pdf --skip-institution-detection`                                                                 |
| `--skip-email-detection`        | Skip email detection                                                                     | `pdf2zh_next example.pdf --skip-email-detection`                                                                       |
| `--skip-url-detection`          | Skip URL detection                                                                       | `pdf2zh_next example.pdf --skip-url-detection`                                                                         |
| `--skip-doi-detection`          | Skip DOI detection                                                                       | `pdf2zh_next example.pdf --skip-doi-detection`                                                                         |

---

### TRANSLATED TEXT

| `--skip-scanned-detection`      | Omitir detección de documentos escaneados                                                | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--skip-table-detection`        | Omitir detección de tablas                                                               | `pdf2zh_next example.pdf --skip-table-detection`                                                                       |
| `--skip-equation-detection`     | Omitir detección de ecuaciones                                                           | `pdf2zh_next example.pdf --skip-equation-detection`                                                                    |
| `--skip-figure-detection`       | Omitir detección de figuras                                                              | `pdf2zh_next example.pdf --skip-figure-detection`                                                                      |
| `--skip-header-footer-detection`| Omitir detección de encabezados y pies de página                                         | `pdf2zh_next example.pdf --skip-header-footer-detection`                                                               |
| `--skip-footnote-detection`     | Omitir detección de notas al pie                                                         | `pdf2zh_next example.pdf --skip-footnote-detection`                                                                    |
| `--skip-reference-detection`    | Omitir detección de referencias                                                          | `pdf2zh_next example.pdf --skip-reference-detection`                                                                   |
| `--skip-abstract-detection`     | Omitir detección de resúmenes                                                            | `pdf2zh_next example.pdf --skip-abstract-detection`                                                                    |
| `--skip-keywords-detection`     | Omitir detección de palabras clave                                                       | `pdf2zh_next example.pdf --skip-keywords-detection`                                                                    |
| `--skip-title-detection`        | Omitir detección de títulos                                                              | `pdf2zh_next example.pdf --skip-title-detection`                                                                       |
| `--skip-author-detection`       | Omitir detección de autores                                                              | `pdf2zh_next example.pdf --skip-author-detection`                                                                      |
| `--skip-date-detection`         | Omitir detección de fechas                                                               | `pdf2zh_next example.pdf --skip-date-detection`                                                                        |
| `--skip-institution-detection`  | Omitir detección de instituciones                                                        | `pdf2zh_next example.pdf --skip-institution-detection`                                                                 |
| `--skip-email-detection`        | Omitir detección de correos electrónicos                                                 | `pdf2zh_next example.pdf --skip-email-detection`                                                                       |
| `--skip-url-detection`          | Omitir detección de URLs                                                                 | `pdf2zh_next example.pdf --skip-url-detection`                                                                         |
| `--skip-doi-detection`          | Omitir detección de DOIs                                                                 | `pdf2zh_next example.pdf --skip-doi-detection`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-color`         | Specify the color for the OCR workaround, default is black                              | `pdf2zh_next example.pdf --ocr-workaround-color="red"`                                                                |
| `--ocr-workaround-bg-color`      | Specify the background color for the OCR workaround, default is white                   | `pdf2zh_next example.pdf --ocr-workaround-bg-color="red"`                                                              |
| `--ocr-workaround-padding`       | Specify the padding for the OCR workaround, default is 1.5                              | `pdf2zh_next example.pdf --ocr-workaround-padding=2.5`                                                                 |
| `--ocr-workaround-border-radius` | Specify the border radius for the OCR workaround, default is 0                          | `pdf2zh_next example.pdf --ocr-workaround-border-radius=5`                                                             |
| `--ocr-workaround-font-size`     | Specify the font size for the OCR workaround, default is to use the original font size   | `pdf2zh_next example.pdf --ocr-workaround-font-size=20`                                                                |

---

### TRANSLATION RESULT

| `--ocr-workaround`              | Forzar que el texto traducido sea negro y añadir un fondo blanco                        | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--ocr-workaround-color`         | Especificar el color para la solución de OCR, por defecto es negro                      | `pdf2zh_next example.pdf --ocr-workaround-color="red"`                                                                |
| `--ocr-workaround-bg-color`      | Especificar el color de fondo para la solución de OCR, por defecto es blanco            | `pdf2zh_next example.pdf --ocr-workaround-bg-color="red"`                                                              |
| `--ocr-workaround-padding`       | Especificar el relleno para la solución de OCR, por defecto es 1.5                      | `pdf2zh_next example.pdf --ocr-workaround-padding=2.5`                                                                 |
| `--ocr-workaround-border-radius` | Especificar el radio del borde para la solución de OCR, por defecto es 0                | `pdf2zh_next example.pdf --ocr-workaround-border-radius=5`                                                             |
| `--ocr-workaround-font-size`     | Especificar el tamaño de fuente para la solución de OCR, por defecto usa el tamaño de fuente original | `pdf2zh_next example.pdf --ocr-workaround-font-size=20`                                                                |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `--ocr-workaround-threshold`    | Threshold for OCR workaround. If the proportion of scanned pages exceeds this value, OCR processing is enabled. (default: 0.5)                                                                     | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.3`                   |
| `--ocr-workaround-skip-pages`   | Skip the first N pages for OCR workaround scan detection. (default: 10)                                                                                                                            | `pdf2zh_next example.pdf --ocr-workaround-skip-pages 5`                    |
| `--ocr-workaround-sample-pages` | Number of pages to sample for OCR workaround scan detection. (default: 20)                                                                                                                         | `pdf2zh_next example.pdf --ocr-workaround-sample-pages 15`                 |

---

### OUTPUT

| `--auto-enable-ocr-workaround`  | Habilitar solución automática de OCR. Si se detecta que un documento está muy escaneado, intentará habilitar el procesamiento OCR y omitirá la detección de escaneo adicional. Consulte la documentación para más detalles. (predeterminado: Falso) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `--ocr-workaround-threshold`    | Umbral para la solución de OCR. Si la proporción de páginas escaneadas supera este valor, se habilita el procesamiento OCR. (predeterminado: 0.5)                                                                                                   | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.3`                   |
| `--ocr-workaround-skip-pages`   | Omitir las primeras N páginas para la detección de escaneo de la solución de OCR. (predeterminado: 10)                                                                                                                                             | `pdf2zh_next example.pdf --ocr-workaround-skip-pages 5`                    |
| `--ocr-workaround-sample-pages` | Número de páginas a muestrear para la detección de escaneo de la solución de OCR. (predeterminado: 20)                                                                                                                                             | `pdf2zh_next example.pdf --ocr-workaround-sample-pages 15`                 |
|---------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------| 
| `--only-include-translated-page`| Solo incluye las páginas traducidas en el PDF de salida. Solo es efectivo cuando se usa --pages. | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `--no-merge-alternating-line-numbers` | Deshabilitar la fusión de números de línea alternos y párrafos de texto en documentos con números de línea | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-formula-lines` | Desactivar la eliminación de líneas que no son fórmulas dentro de las áreas de párrafo | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                               |
`0.8`   |
| `--formula-line-iou-threshold`     | Set IoU threshold for identifying formula lines (0.0-1.0)                          | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.9`                                                            | `0.85`  |
| `--table-line-iou-threshold`       | Set IoU threshold for identifying table lines (0.0-1.0)                            | `pdf2zh_next example.pdf --table-line-iou-threshold 0.95`                                                              | `0.9`   |
| `--table-content-iou-threshold`    | Set IoU threshold for identifying table content (0.0-1.0)                          | `pdf2zh_next example.pdf --table-content-iou-threshold 0.95`                                                           | `0.9`   |
| `--table-merge-threshold`          | Set threshold for merging table cells (0.0-1.0)                                    | `pdf2zh_next example.pdf --table-merge-threshold 0.1`                                                                  | `0.05`  |
| `--table-merge-max-rows`           | Set maximum number of rows to merge in table                                       | `pdf2zh_next example.pdf --table-merge-max-rows 5`                                                                     | `3`     |
| `--table-merge-max-cols`           | Set maximum number of columns to merge in table                                    | `pdf2zh_next example.pdf --table-merge-max-cols 5`                                                                     | `3`     |

---

### TRANSLATION

| `--non-formula-line-iou-threshold` | Establece el umbral de IoU para identificar líneas que no son fórmulas (0.0-1.0)               | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.8`   |
| `--formula-line-iou-threshold`     | Establece el umbral de IoU para identificar líneas de fórmulas (0.0-1.0)                       | `pdf2zh_next example.pdf --formula-line-iou-threshold 0.9`                                                            | `0.85`  |
| `--table-line-iou-threshold`       | Establece el umbral de IoU para identificar líneas de tablas (0.0-1.0)                         | `pdf2zh_next example.pdf --table-line-iou-threshold 0.95`                                                              | `0.9`   |
| `--table-content-iou-threshold`    | Establece el umbral de IoU para identificar contenido de tablas (0.0-1.0)                      | `pdf2zh_next example.pdf --table-content-iou-threshold 0.95`                                                           | `0.9`   |
| `--table-merge-threshold`          | Establece el umbral para fusionar celdas de tabla (0.0-1.0)                                    | `pdf2zh_next example.pdf --table-merge-threshold 0.1`                                                                  | `0.05`  |
| `--table-merge-max-rows`           | Establece el número máximo de filas a fusionar en una tabla                                    | `pdf2zh_next example.pdf --table-merge-max-rows 5`                                                                     | `3`     |
| `--table-merge-max-cols`           | Establece el número máximo de columnas a fusionar en una tabla                                 | `pdf2zh_next example.pdf --table-merge-max-cols 5`                                                                     | `3`     |
`0.95` |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------ |

---

### OUTPUT

| `--figure-table-protection-threshold` | Establecer umbral de protección para figuras y tablas (0.0-1.0). Las líneas dentro de figuras/tablas no se procesarán | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        | `0.95` |
---

### OUTPUT

| `--skip-formula-offset-calculation` | Omitir el cálculo de desplazamiento de fórmulas durante el procesamiento | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### Argumentos de GUI

| `--server_port <port>`          | Set the server port                    | `pdf2zh_next --gui --server_port 8080`          |
| `--language <language>`         | Set the default language               | `pdf2zh_next --gui --language en`               |
| `--theme <theme>`               | Set the theme (light or dark)          | `pdf2zh_next --gui --theme dark`                |
| `--height <height>`             | Set the height of the interface        | `pdf2zh_next --gui --height 800`                |
| `--concurrency_count <count>`   | Set the number of concurrent processes | `pdf2zh_next --gui --concurrency_count 4`       |
| `--api_name <name>`             | Set the API name                       | `pdf2zh_next --gui --api_name /api`             |
| `--show_error <true/false>`     | Show error messages                    | `pdf2zh_next --gui --show_error true`           |
| `--max_file_size <size>`        | Set the maximum file size (MB)         | `pdf2zh_next --gui --max_file_size 100`         |
| `--auth <username:password>`    | Set authentication                     | `pdf2zh_next --gui --auth user:pass`            |
| `--ssl_keyfile <path>`          | Set SSL key file path                  | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile <path>`         | Set SSL certificate file path          | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--prevent_thread_lock <true/false>` | Prevent thread locking             | `pdf2zh_next --gui --prevent_thread_lock true`  |

---

### TRANSLATED TEXT

| Opción                          | Función                                | Ejemplo                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Habilitar modo de compartir            | `pdf2zh_next --gui --share`                     |
| `--server_port <port>`          | Establecer el puerto del servidor      | `pdf2zh_next --gui --server_port 8080`          |
| `--language <language>`         | Establecer el idioma predeterminado    | `pdf2zh_next --gui --language en`               |
| `--theme <theme>`               | Establecer el tema (claro u oscuro)    | `pdf2zh_next --gui --theme dark`                |
| `--height <height>`             | Establecer la altura de la interfaz    | `pdf2zh_next --gui --height 800`                |
| `--concurrency_count <count>`   | Establecer el número de procesos concurrentes | `pdf2zh_next --gui --concurrency_count 4`       |
| `--api_name <name>`             | Establecer el nombre de la API         | `pdf2zh_next --gui --api_name /api`             |
| `--show_error <true/false>`     | Mostrar mensajes de error              | `pdf2zh_next --gui --show_error true`           |
| `--max_file_size <size>`        | Establecer el tamaño máximo de archivo (MB) | `pdf2zh_next --gui --max_file_size 100`         |
| `--auth <usuario:contraseña>`   | Establecer autenticación               | `pdf2zh_next --gui --auth user:pass`            |
| `--ssl_keyfile <ruta>`          | Establecer la ruta del archivo de clave SSL | `pdf2zh_next --gui --ssl_keyfile key.pem`       |
| `--ssl_certfile <ruta>`         | Establecer la ruta del archivo de certificado SSL | `pdf2zh_next --gui --ssl_certfile cert.pem`     |
| `--prevent_thread_lock <true/false>` | Prevenir bloqueo de hilos          | `pdf2zh_next --gui --prevent_thread_lock true`  |
---

### OUTPUT

| `--auth-file`                   | Ruta al archivo de autenticación      | `pdf2zh_next --gui --auth-file /path`           |
-            |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ------------ |
| `--config-dir`                  | Path to the config directory           | `pdf2zh_next --gui --config-dir /path`          | -            |
| `--config-file`                 | Path to the config file                | `pdf2zh_next --gui --config-file /path`         | -            |
| `--data-dir`                    | Path to the data directory             | `pdf2zh_next --gui --data-dir /path`            | -            |
| `--cache-dir`                   | Path to the cache directory            | `pdf2zh_next --gui --cache-dir /path`           | -            |
| `--temp-dir`                    | Path to the temp directory             | `pdf2zh_next --gui --temp-dir /path`            | -            |
| `--log-dir`                     | Path to the log directory              | `pdf2zh_next --gui --log-dir /path`             | -            |
| `--log-file`                    | Path to the log file                   | `pdf2zh_next --gui --log-file /path`            | -            |
| `--log-level`                   | Log level                              | `pdf2zh_next --gui --log-level debug`            | `info`       |
| `--log-rotation`                | Log rotation                           | `pdf2zh_next --gui --log-rotation 1 week`        | `1 day`      |
| `--log-retention`               | Log retention                          | `pdf2zh_next --gui --log-retention 1 month`     | `1 week`     |
| `--log-compression`             | Log compression                        | `pdf2zh_next --gui --log-compression gzip`      | `disabled`   |
| `--log-format`                  | Log format                             | `pdf2zh_next --gui --log-format json`           | `text`       |
| `--log-color`                   | Log color                              | `pdf2zh_next --gui --log-color`                  | `false`      |
| `--log-no-color`                | Log no color                           | `pdf2zh_next --gui --log-no-color`               | `false`      |
| `--log-force-color`             | Log force color                        | `pdf2zh_next --gui --log-force-color`            | `false`      |
| `--log-disable-color`           | Log disable color                      | `pdf2zh_next --gui --log-disable-color`          | `false`      |

---

### OUTPUT

| `--welcome-page`                | Ruta al archivo html de bienvenida     | `pdf2zh_next --gui --welcome-page /ruta`        | -            |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ------------ |
| `--config-dir`                  | Ruta al directorio de configuración    | `pdf2zh_next --gui --config-dir /ruta`          | -            |
| `--config-file`                 | Ruta al archivo de configuración       | `pdf2zh_next --gui --config-file /ruta`         | -            |
| `--data-dir`                    | Ruta al directorio de datos            | `pdf2zh_next --gui --data-dir /ruta`            | -            |
| `--cache-dir`                   | Ruta al directorio de caché            | `pdf2zh_next --gui --cache-dir /ruta`           | -            |
| `--temp-dir`                    | Ruta al directorio temporal            | `pdf2zh_next --gui --temp-dir /ruta`            | -            |
| `--log-dir`                     | Ruta al directorio de registros        | `pdf2zh_next --gui --log-dir /ruta`             | -            |
| `--log-file`                    | Ruta al archivo de registro            | `pdf2zh_next --gui --log-file /ruta`            | -            |
| `--log-level`                   | Nivel de registro                      | `pdf2zh_next --gui --log-level debug`            | `info`       |
| `--log-rotation`                | Rotación de registros                  | `pdf2zh_next --gui --log-rotation 1 semana`     | `1 día`      |
| `--log-retention`               | Retención de registros                 | `pdf2zh_next --gui --log-retention 1 mes`       | `1 semana`   |
| `--log-compression`             | Compresión de registros                | `pdf2zh_next --gui --log-compression gzip`      | `disabled`   |
| `--log-format`                  | Formato de registro                    | `pdf2zh_next --gui --log-format json`           | `text`       |
| `--log-color`                   | Color de registro                      | `pdf2zh_next --gui --log-color`                  | `false`      |
| `--log-no-color`                | Sin color en registros                 | `pdf2zh_next --gui --log-no-color`               | `false`      |
| `--log-force-color`             | Forzar color en registros              | `pdf2zh_next --gui --log-force-color`            | `false`      |
| `--log-disable-color`           | Desactivar color en registros          | `pdf2zh_next --gui --log-disable-color`          | `false`      |
`PDFMathTranslate` will only use Bing and OpenAI translation services. |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Bing"`       | `PDFMathTranslate` will not use Bing translation service.              |
| `--service-order`               | Service priority order                 | `pdf2zh_next --gui --service-order "OpenAI,Google"`  | `PDFMathTranslate` will prioritize OpenAI, then Google.                |
| `--service-timeout`             | Service timeout (seconds)              | `pdf2zh_next --gui --service-timeout 30`             | Set translation service timeout to 30 seconds.                         |
| `--service-retry-times`         | Service retry times                    | `pdf2zh_next --gui --service-retry-times 3`          | Retry translation up to 3 times if service fails.                      |
| `--service-retry-interval`      | Service retry interval (seconds)       | `pdf2zh_next --gui --service-retry-interval 5`       | Wait 5 seconds between retries.                                        |
| `--service-fallback`            | Enable service fallback                | `pdf2zh_next --gui --service-fallback`               | Enable fallback to next service if current one fails.                  |
| `--no-service-fallback`         | Disable service fallback               | `pdf2zh_next --gui --no-service-fallback`            | Disable service fallback.                                              |
| `--service-concurrency`         | Maximum concurrent service requests    | `pdf2zh_next --gui --service-concurrency 5`          | Allow up to 5 concurrent translation requests.                         |

---

### TRANSLATION

| `--enabled-services`            | Servicios de traducción habilitados           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` | `PDFMathTranslate` solo utilizará los servicios de traducción Bing y OpenAI. |
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------- |
| `--disabled-services`           | Servicios de traducción deshabilitados          | `pdf2zh_next --gui --disabled-services "Bing"`       | `PDFMathTranslate` no utilizará el servicio de traducción Bing.              |
| `--service-order`               | Orden de prioridad de los servicios                 | `pdf2zh_next --gui --service-order "OpenAI,Google"`  | `PDFMathTranslate` priorizará OpenAI, luego Google.                |
| `--service-timeout`             | Tiempo de espera del servicio (segundos)              | `pdf2zh_next --gui --service-timeout 30`             | Establece el tiempo de espera del servicio de traducción a 30 segundos.                         |
| `--service-retry-times`         | Número de reintentos del servicio                    | `pdf2zh_next --gui --service-retry-times 3`          | Reintentar la traducción hasta 3 veces si el servicio falla.                      |
| `--service-retry-interval`      | Intervalo de reintento del servicio (segundos)       | `pdf2zh_next --gui --service-retry-interval 5`       | Esperar 5 segundos entre reintentos.                                        |
| `--service-fallback`            | Habilitar conmutación por error del servicio                | `pdf2zh_next --gui --service-fallback`               | Habilitar la conmutación por error al siguiente servicio si el actual falla.                  |
| `--no-service-fallback`         | Deshabilitar conmutación por error del servicio               | `pdf2zh_next --gui --no-service-fallback`            | Deshabilitar la conmutación por error del servicio.                                              |
| `--service-concurrency`         | Máximo de solicitudes de servicio concurrentes    | `pdf2zh_next --gui --service-concurrency 5`          | Permitir hasta 5 solicitudes de traducción concurrentes.                         |
| ------------------------------- | -------------------------------------- | ------------------------------------------------- |
| `--no-disable-gui-sensitive-input` | Enable GUI sensitive input (default)   | `pdf2zh_next --gui --no-disable-gui-sensitive-input` |

---

### TRANSLATION RESULT

| `--disable-gui-sensitive-input` | Deshabilitar entrada sensible de la GUI            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
| ------------------------------- | -------------------------------------- | ------------------------------------------------- |
| `--no-disable-gui-sensitive-input` | Habilitar entrada sensible de la GUI (por defecto)   | `pdf2zh_next --gui --no-disable-gui-sensitive-input` |
`pdf2zh_next --gui` with auto-save enabled by default |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- |
| `--disable-log-auto-save`       | Disable automatic log saving           | `pdf2zh_next --gui --disable-log-auto-save`     | `pdf2zh_next --gui` with auto-save enabled by default |

---

### OUTPUT

| `--disable-config-auto-save`    | Deshabilitar el guardado automático de configuración | `pdf2zh_next --gui --disable-config-auto-save`  | `pdf2zh_next --gui` con guardado automático habilitado por defecto |
| ------------------------------- | ---------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| `--disable-log-auto-save`       | Deshabilitar el guardado automático de registros     | `pdf2zh_next --gui --disable-log-auto-save`     | `pdf2zh_next --gui` con guardado automático habilitado por defecto |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--server-address`              | WebUI Address                          | `pdf2zh_next --gui --server-address 0.0.0.0`    |
| `--share`                       | Enable Public Network Access           | `pdf2zh_next --gui --share`                     |
| `--disable-gradio-queue`        | Disable Gradio Queue                   | `pdf2zh_next --gui --disable-gradio-queue`      |
| `--auth`                        | Set Gradio Authentication              | `pdf2zh_next --gui --auth username:password`    |
| `--auth-message`                | Set Gradio Login Page Message          | `pdf2zh_next --gui --auth-message "Please login"` |
| `--ssl-keyfile`                 | SSL Key File Path                      | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | SSL Certificate File Path              | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
| `--concurrency-count`           | Gradio Concurrency Count               | `pdf2zh_next --gui --concurrency-count 10`      |
| `--show-api`                    | Show API Documentation Page            | `pdf2zh_next --gui --show-api`                  |
| `--favicon-path`                | Custom Favicon Path                    | `pdf2zh_next --gui --favicon-path favicon.ico`  |
| `--app-kwargs`                  | Additional Gradio App Arguments (JSON) | `pdf2zh_next --gui --app-kwargs '{"title": "My App"}'` |

---

### OUTPUT LANGUAGE

ISO 639-1 code: es

---

### OUTPUT

| `--server-port`                 | Puerto de WebUI                            | `pdf2zh_next --gui --server-port 7860`          |
|---------------------------------|--------------------------------------------|-------------------------------------------------|
| `--server-address`              | Dirección de WebUI                         | `pdf2zh_next --gui --server-address 0.0.0.0`    |
| `--share`                       | Habilitar acceso a la red pública          | `pdf2zh_next --gui --share`                     |
| `--disable-gradio-queue`        | Deshabilitar cola de Gradio                | `pdf2zh_next --gui --disable-gradio-queue`      |
| `--auth`                        | Configurar autenticación de Gradio         | `pdf2zh_next --gui --auth usuario:contraseña`   |
| `--auth-message`                | Configurar mensaje de la página de inicio de sesión de Gradio | `pdf2zh_next --gui --auth-message "Por favor, inicia sesión"` |
| `--ssl-keyfile`                 | Ruta del archivo de clave SSL              | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | Ruta del archivo de certificado SSL        | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
| `--concurrency-count`           | Conteo de concurrencia de Gradio           | `pdf2zh_next --gui --concurrency-count 10`      |
| `--show-api`                    | Mostrar página de documentación de API     | `pdf2zh_next --gui --show-api`                  |
| `--favicon-path`                | Ruta personalizada del favicon             | `pdf2zh_next --gui --favicon-path favicon.ico`  |
| `--app-kwargs`                  | Argumentos adicionales de la aplicación Gradio (JSON) | `pdf2zh_next --gui --app-kwargs '{"title": "Mi App"}'` |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--translator`                  | Translation service                    | `pdf2zh_next --translator google`               |
| `--target-lang`                 | Target language                        | `pdf2zh_next --target-lang en`                  |
| `--src-lang`                    | Source language                        | `pdf2zh_next --src-lang zh`                     |
| `--proxy`                       | Proxy server                           | `pdf2zh_next --proxy http://127.0.0.1:7890`     |
| `--format`                      | Output format                          | `pdf2zh_next --format html`                     |
| `--output-dir`                  | Output directory                       | `pdf2zh_next --output-dir ./output`             |
| `--output-filename`             | Output filename                        | `pdf2zh_next --output-filename translated.pdf`  |
| `--mathpix-app-id`              | Mathpix App ID                         | `pdf2zh_next --mathpix-app-id <YOUR_APP_ID>`    |
| `--mathpix-app-key`             | Mathpix App Key                        | `pdf2zh_next --mathpix-app-key <YOUR_APP_KEY>`  |
| `--openai-api-key`              | OpenAI API Key                         | `pdf2zh_next --openai-api-key <YOUR_API_KEY>`   |
| `--openai-base-url`             | OpenAI Base URL                        | `pdf2zh_next --openai-base-url <YOUR_BASE_URL>` |
| `--openai-model`                | OpenAI Model                           | `pdf2zh_next --openai-model gpt-4o`             |
| `--openai-prompt`               | OpenAI Prompt                          | `pdf2zh_next --openai-prompt <YOUR_PROMPT>`     |
| `--webui-port`                  | WebUI port                             | `pdf2zh_next --webui-port 3000`                 |
| `--webui-host`                  | WebUI host                             | `pdf2zh_next --webui-host 0.0.0.0`              |
| `--webui-no-browser`            | Disable browser auto open              | `pdf2zh_next --webui-no-browser`                |
| `--webui-no-server-timing`      | Disable server timing                  | `pdf2zh_next --webui-no-server-timing`          |
| `--webui-concurrency`           | WebUI concurrency limit                | `pdf2zh_next --webui-concurrency 10`            |

---

### OUTPUT

| `--ui-lang`                     | Idioma de la interfaz de usuario      | `pdf2zh_next --gui --ui-lang zh`                |
|---------------------------------|----------------------------------------|-------------------------------------------------|
| `--translator`                  | Servicio de traducción                 | `pdf2zh_next --translator google`               |
| `--target-lang`                 | Idioma de destino                      | `pdf2zh_next --target-lang en`                  |
| `--src-lang`                    | Idioma de origen                       | `pdf2zh_next --src-lang zh`                     |
| `--proxy`                       | Servidor proxy                         | `pdf2zh_next --proxy http://127.0.0.1:7890`     |
| `--format`                      | Formato de salida                      | `pdf2zh_next --format html`                     |
| `--output-dir`                  | Directorio de salida                   | `pdf2zh_next --output-dir ./output`             |
| `--output-filename`             | Nombre del archivo de salida           | `pdf2zh_next --output-filename translated.pdf`  |
| `--mathpix-app-id`              | ID de aplicación de Mathpix            | `pdf2zh_next --mathpix-app-id <YOUR_APP_ID>`    |
| `--mathpix-app-key`             | Clave de aplicación de Mathpix         | `pdf2zh_next --mathpix-app-key <YOUR_APP_KEY>`  |
| `--openai-api-key`              | Clave de API de OpenAI                 | `pdf2zh_next --openai-api-key <YOUR_API_KEY>`   |
| `--openai-base-url`             | URL base de OpenAI                     | `pdf2zh_next --openai-base-url <YOUR_BASE_URL>` |
| `--openai-model`                | Modelo de OpenAI                       | `pdf2zh_next --openai-model gpt-4o`             |
| `--openai-prompt`               | Prompt de OpenAI                       | `pdf2zh_next --openai-prompt <YOUR_PROMPT>`     |
| `--webui-port`                  | Puerto de WebUI                        | `pdf2zh_next --webui-port 3000`                 |
| `--webui-host`                  | Host de WebUI                          | `pdf2zh_next --webui-host 0.0.0.0`              |
| `--webui-no-browser`            | Deshabilitar apertura automática del navegador | `pdf2zh_next --webui-no-browser`                |
| `--webui-no-server-timing`      | Deshabilitar tiempo del servidor       | `pdf2zh_next --webui-no-server-timing`          |
| `--webui-concurrency`           | Límite de concurrencia de WebUI        | `pdf2zh_next --webui-concurrency 10`            |

[⬆️ Volver arriba](#toc)

---

#### Guía de Configuración de Límite de Tasa

Al utilizar servicios de traducción, una configuración adecuada del límite de tasa es crucial para evitar errores de API y optimizar el rendimiento. Esta guía explica cómo configurar los parámetros `--qps` y `--pool-max-worker` según las limitaciones de diferentes servicios ascendentes.

> [!TIP]
>
> Se recomienda que el `pool_size` no exceda de 1000. Si el `pool_size` calculado por el siguiente método excede 1000, por favor utilice 1000.

##### Limitación de tasa RPM (Solicitudes Por Minuto)

Cuando el servicio ascendente tiene limitaciones de RPM, utiliza el siguiente cálculo:

**Fórmula de cálculo:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> El factor de 10 es un coeficiente empírico que generalmente funciona bien para la mayoría de los escenarios.

**Ejemplo:**
Si tu servicio de traducción tiene un límite de 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Limitación de conexiones concurrentes

Cuando el servicio ascendente tiene limitaciones de conexiones concurrentes (como el servicio oficial de GLM), utiliza este enfoque:

**Fórmula de cálculo:**
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

**Ejemplo:**
Si tu servicio de traducción permite 50 conexiones concurrentes:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### Mejores prácticas

> [!TIP]
> - Siempre comienza con valores conservadores y aumenta gradualmente si es necesario
> - Monitorea los tiempos de respuesta y las tasas de error de tu servicio
> - Diferentes servicios pueden requerir diferentes estrategias de optimización
> - Considera tu caso de uso específico y el tamaño del documento al configurar estos parámetros


[⬆️ Volver arriba](#toc)

---

#### Traducción parcial

Utiliza el parámetro `--pages` para traducir una parte de un documento.

- Si los números de página son consecutivos, puedes escribirlo así:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` incluye todas las páginas después de la página 25. Si tu documento tiene 100 páginas, esto es equivalente a `25-100`.
> 
> Del mismo modo, `-25` incluye todas las páginas antes de la página 25, lo que equivale a `1-25`.

- Si las páginas no son consecutivas, puedes usar una coma `,` para separarlas.

Por ejemplo, si deseas traducir la primera y tercera página, puedes usar el siguiente comando:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- Si las páginas incluyen rangos tanto consecutivos como no consecutivos, también puedes conectarlos con una coma, así:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

Este comando traducirá la primera página, la tercera página, las páginas 10-20 y todas las páginas desde la 25 hasta el final.


[⬆️ Volver arriba](#toc)

---

#### Especificar idiomas de origen y destino

Consulta los [Códigos de idioma de Google](https://developers.google.com/admin-sdk/directory/v1/languages) y los [Códigos de idioma de DeepL](https://developers.deepl.com/docs/resources/supported-languages)

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ Volver arriba](#toc)

---

#### Traducir con excepciones

Usar expresiones regulares para especificar fuentes de fórmulas y caracteres que deben preservarse:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

Preservar las fuentes `Latex`, `Mono`, `Code`, `Italic`, `Symbol` y `Math` por defecto:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Volver arriba](#toc)

---

#### Indicaciones personalizadas

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

Indicaciones personalizadas del sistema para traducción. Se utiliza principalmente para agregar la instrucción '/no_think' de Qwen 3 en la indicación.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ Volver arriba](#toc)

---

#### Configuración personalizada

Existen múltiples formas de modificar e importar el archivo de configuración.

> [!NOTE]
> **Jerarquía de archivos de configuración**
>
> Al modificar el mismo parámetro utilizando diferentes métodos, el software aplicará los cambios según el siguiente orden de prioridad.
>
> Las modificaciones de mayor prioridad anularán las de menor prioridad.
>
> **cli/gui > env > archivo de configuración del usuario > archivo de configuración predeterminado**

- Modificación de la configuración mediante **Argumentos de la línea de comandos**

En la mayoría de los casos, puedes pasar directamente tus configuraciones deseadas a través de argumentos de la línea de comandos. Consulta [Argumentos de la línea de comandos](#cmd) para obtener más información.

Por ejemplo, si deseas habilitar una ventana GUI, puedes usar el siguiente comando:

```bash
pdf2zh_next --gui
```

- Modificación de la configuración mediante **variables de entorno**

Puedes reemplazar el `--` en los argumentos de la línea de comandos con `PDF2ZH_`, conectar parámetros usando `=`, y reemplazar `-` con `_` como variables de entorno.

Por ejemplo, si deseas habilitar una ventana GUI, puedes usar el siguiente comando:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- Archivo de **configuración** especificado por el usuario

Puedes especificar un archivo de configuración utilizando el siguiente argumento de la línea de comandos:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

Si no está seguro del formato del archivo de configuración, consulte el archivo de configuración predeterminado que se describe a continuación.

- **Archivo de Configuración Predeterminado**

El archivo de configuración predeterminado se encuentra en `~/.config/pdf2zh`.  
Por favor, no modifiques los archivos de configuración en el directorio `default`.  
Se recomienda encarecidamente consultar el contenido de este archivo de configuración y utilizar **Configuración personalizada** para implementar tu propio archivo de configuración.

> [!TIP]
> - Por defecto, pdf2zh 2.0 guarda automáticamente la configuración actual en `~/.config/pdf2zh/config.v3.toml` cada vez que haces clic en el botón de traducción en la GUI. Este archivo de configuración se cargará por defecto en el próximo inicio.
> - Los archivos de configuración en el directorio `default` son generados automáticamente por el programa. Puedes copiarlos para modificarlos, pero por favor no los modifiques directamente.
> - Los archivos de configuración pueden incluir números de versión como "v2", "v3", etc. Estos son **números de versión del archivo de configuración**, **no** el número de versión de pdf2zh en sí.


[⬆️ Volver arriba](#toc)

---

#### Omitir limpieza

Cuando este parámetro se establece en True, se omitirá el paso de limpieza del PDF, lo que puede mejorar la compatibilidad y evitar algunos problemas de procesamiento de fuentes.

Uso:

```bash
pdf2zh_next example.pdf --skip-clean
```

O utilizando variables de entorno:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Cuando `--enhance-compatibility` está habilitado, Omitir limpieza se activa automáticamente.

---

#### Caché de traducción

PDFMathTranslate almacena en caché los textos traducidos para aumentar la velocidad y evitar llamadas API innecesarias para los mismos contenidos. Puedes usar la opción `--ignore-cache` para ignorar la caché de traducción y forzar la retraducción.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Volver arriba](#toc)

---

#### Despliegue como servicios públicos

Al desplegar una GUI de pdf2zh en servicios públicos, debes modificar el archivo de configuración como se describe a continuación.

> [!WARNING]
>
> Este proyecto no ha sido auditado profesionalmente en cuanto a seguridad y puede contener vulnerabilidades. Por favor, evalúe los riesgos y tome las medidas de seguridad necesarias antes de implementarlo en redes públicas.


> [!TIP]
> - Al implementar públicamente, tanto `disable_gui_sensitive_input` como `disable_config_auto_save` deben estar habilitados.
> - Separe los diferentes servicios disponibles con *comas en inglés* <kbd>,</kbd> .

Una configuración utilizable es la siguiente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ Volver arriba](#toc)

---

#### Autenticación y página de bienvenida

Al usar Autenticación y página de bienvenida para especificar qué usuario debe usar Web UI y personalizar la página de inicio de sesión:

ejemplo auth.txt
Cada línea contiene dos elementos, nombre de usuario y contraseña, separados por una coma.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

ejemplo welcome.html

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
> La página de bienvenida funcionará solo si el archivo de autenticación no está en blanco.
> Si el archivo de autenticación está en blanco, no habrá autenticación. :)

Una configuración utilizable es la siguiente:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ Volver arriba](#toc)

---

#### Soporte de glosario

PDFMathTranslate soporta la tabla de glosario. El archivo de tablas de glosario debe ser un archivo `csv`.
Hay tres columnas en el archivo. Aquí hay un archivo de glosario de demostración:

| fuente | objetivo  | idioma_destino |
|--------|---------|---------|
| AutoML | ML automático  | es   |
| a,a    | a       | es   |
| "      | "       | es   |


Para usuarios de CLI:
Puedes usar múltiples archivos para el glosario. Y los diferentes archivos deben estar separados por `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Para usuarios de WebUI:

Ahora puedes subir tu propio archivo de glosario. Después de subir el archivo, puedes verificarlo haciendo clic en su nombre y el contenido se mostrará a continuación.

[⬆️ Volver al inicio](#toc)

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>