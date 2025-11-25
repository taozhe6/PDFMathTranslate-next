>
> Thank you for your understanding and support!

# PDFMathTranslate

**Translate PDFs with mathematical formulas accurately.**

PDFMathTranslate is a tool designed to translate PDF documents, especially those containing mathematical formulas, from one language to another. It supports multiple translation services and ensures that mathematical formulas are accurately translated and rendered.

## Features

- **Accurate Formula Translation**: Uses [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) to handle mathematical formulas.
- **Multiple Translation Services**: Supports Google Translate, DeepL, OpenAI, and more.
- **Flexible Output Formats**: Output translated documents in PDF, LaTeX, or Markdown.
- **Easy to Use**: Simple command-line interface and WebUI.

## Quick Start

### Installation

```bash
pip install pdf2zh
```

### Basic Usage

Translate a PDF file using the command line:

```bash
pdf2zh translate --file path/to/your/file.pdf
```

Or use the WebUI:

```bash
pdf2zh webui
```

## Documentation

For detailed documentation, visit [https://pdf2zh-next.com](https://pdf2zh-next.com).

- **[Getting Started](https://pdf2zh-next.com/getting-started/INSTALLATION.html)**: Installation and basic usage.
- **[Usage](https://pdf2zh-next.com/getting-started/USAGE.html)**: Detailed usage guide.
- **[Advanced](https://pdf2zh-next.com/getting-started/ADVANCED.html)**: Advanced configuration and customization.
- **[Supported Languages](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html)**: List of supported languages.
- **[FAQ](https://pdf2zh-next.com/getting-started/FAQ.html)**: Frequently asked questions.

## Community

Join our community for support and contributions:

- **GitHub**: [https://github.com/PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next)
- **Discord**: [Join our Discord server](https://discord.gg/example)

## Contributing

We welcome contributions! Please read our [Contribution Guidelines](https://pdf2zh-next.com/getting-started/CONTRIBUTING.html) for details.

For translators, see the [For Translators](https://pdf2zh-next.com/getting-started/FOR_TRANSLATORS.html) guide.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### TRANSLATION RESULT

> [!NOTE]
> Esta documentación puede contener contenido generado por IA. Aunque nos esforzamos por la precisión, pueden haber inexactitudes. Por favor, reporta cualquier problema a través de:
>
> - [Problemas de GitHub](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - Contribución de la comunidad (¡PRs son bienvenidos!)
>
> ¡Gracias por tu comprensión y apoyo!

# PDFMathTranslate

**Traduce PDFs con fórmulas matemáticas con precisión.**

PDFMathTranslate es una herramienta diseñada para traducir documentos PDF, especialmente aquellos que contienen fórmulas matemáticas, de un idioma a otro. Soporta múltiples servicios de traducción y garantiza que las fórmulas matemáticas se traduzcan y rendericen con precisión.

## Características

- **Traducción precisa de fórmulas**: Usa [PDFMathTranslate](https://github.com/PDFMathTranslate/PDFMathTranslate) para manejar fórmulas matemáticas.
- **Múltiples servicios de traducción**: Soporta Google Translate, DeepL, OpenAI y más.
- **Formatos de salida flexibles**: Genera documentos traducidos en PDF, LaTeX o Markdown.
- **Fácil de usar**: Interfaz de línea de comandos simple y WebUI.

## Empezar

### Instalación

```bash
pip install pdf2zh
```

### Uso básico

Traduce un archivo PDF usando la línea de comandos:

```bash
pdf2zh translate --file ruta/a/tu/archivo.pdf
```

O usa la WebUI:

```bash
pdf2zh webui
```

## Documentación

Para documentación detallada, visita [https://pdf2zh-next.com](https://pdf2zh-next.com).

- **[Empezar](https://pdf2zh-next.com/getting-started/INSTALLATION.html)**: Instalación y uso básico.
- **[Uso](https://pdf2zh-next.com/getting-started/USAGE.html)**: Guía de uso detallada.
- **[Opciones avanzadas](https://pdf2zh-next.com/getting-started/ADVANCED.html)**: Configuración y personalización avanzada.
- **[Idiomas soportados](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html)**: Lista de idiomas soportados.
- **[Preguntas frecuentes](https://pdf2zh-next.com/getting-started/FAQ.html)**: Preguntas frecuentes.

## Comunidad

Únete a nuestra comunidad para soporte y contribuciones:

- **GitHub**: [https://github.com/PDFMathTranslate/PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next)
- **Discord**: [Únete a nuestro servidor de Discord](https://discord.gg/example)

## Contribuciones

¡Agradecemos las contribuciones! Por favor lee nuestras [Guías de contribución](https://pdf2zh-next.com/getting-started/CONTRIBUTING.html) para detalles.

Para traductores, consulta la guía [Guía de contribución de traducciones](https://pdf2zh-next.com/getting-started/FOR_TRANSLATORS.html).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para detalles.

This is the API for streaming translation.

### Parameters

- `file_path` (str): Path to the PDF file to be translated.
- `target_language` (str): The target language to translate to, using the [Language Code](#supported-languages).
- `output_path` (str): The path to save the translated PDF file.
- `api_key` (str): Your OpenAI API key.
- `model` (str, optional): The model to use for translation. Default is `gpt-4o`.
- `pages` (str, optional): Specify pages to translate. For example, `1,3,5-9`. If not provided, all pages will be translated.
- `proxy` (str, optional): Proxy to use for the request. For example, `http://127.0.0.1:7890`.
- `api_base` (str, optional): The base URL for the API. Default is `https://api.openai.com/v1`.

### Returns

- `AsyncGenerator`: An async generator that yields translation progress updates.

### Example

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for progress in do_translate_async_stream(
        file_path="input.pdf",
        target_language="zh",
        output_path="output.pdf",
        api_key="your-api-key"
    ):
        print(f"Progress: {progress}")

asyncio.run(main())
```

### Notes

- This function is useful for real-time progress tracking during translation.
- The progress is a float between 0 and 1, indicating the completion percentage.

---

### OUTPUT

## Python API: do_translate_async_stream
Esta es la API para la traducción en flujo.

### Parámetros

- `file_path` (str): Ruta al archivo PDF a traducir.
- `target_language` (str): El idioma objetivo al que traducir, usando el [Código de idioma](#idiomas-soportados).
- `output_path` (str): La ruta para guardar el archivo PDF traducido.
- `api_key` (str): Tu clave de API de OpenAI.
- `model` (str, opcional): El modelo a usar para la traducción. Por defecto es `gpt-4o`.
- `pages` (str, opcional): Especifica las páginas a traducir. Por ejemplo, `1,3,5-9`. Si no se proporciona, se traducirán todas las páginas.
- `proxy` (str, opcional): Proxy a usar para la solicitud. Por ejemplo, `http://127.0.0.1:7890`.
- `api_base` (str, opcional): La URL base para la API. Por defecto es `https://api.openai.com/v1`.

### Retorna

- `AsyncGenerator`: Un generador asíncrono que produce actualizaciones de progreso de la traducción.

### Ejemplo

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for progress in do_translate_async_stream(
        file_path="input.pdf",
        target_language="zh",
        output_path="output.pdf",
        api_key="your-api-key"
    ):
        print(f"Progress: {progress}")

asyncio.run(main())
```

### Notas

- Esta función es útil para el seguimiento del progreso en tiempo real durante la traducción.
- El progreso es un flotante entre 0 y 1, indicando el porcentaje de completado.

`pdf2zh` is a tool designed for translating PDF documents from English to Chinese. It supports translation via various translation services, including **DeepSeek**, **DeepL**, **OpenAI**, and **Google Translate**. The tool can handle both text and mathematical formulas, ensuring accurate and high-quality translations.

### Key Features

- **Translate PDFs**: Convert English PDFs to Chinese while preserving the original layout and formatting.
- **Mathematical Formula Support**: Accurately translate mathematical formulas using **PDFMathTranslate**.
- **Multiple Translation Services**: Choose from **DeepSeek**, **DeepL**, **OpenAI**, or **Google Translate**.
- **Flexible Output Formats**: Generate translated documents in **PDF**, **LaTeX**, or **Markdown** formats.
- **Easy to Use**: Simple command-line interface and **WebUI** for seamless operation.

### Quick Start

To get started with `pdf2zh`, follow these steps:

1. **Installation**: Install the tool using pip:

   ```bash
   pip install pdf2zh
   ```

2. **Basic Usage**: Use the command line to translate a PDF:

   ```bash
   pdf2zh translate --file path/to/your/file.pdf
   ```

3. **WebUI**: Alternatively, use the **WebUI** for a graphical interface:

   ```bash
   pdf2zh webui
   ```

For detailed instructions, check out the [Usage](https://pdf2zh-next.com/getting-started/USAGE.html) guide.

### Supported Languages

`pdf2zh` primarily focuses on translating from **English** to **Chinese**. However, it also supports translations between other languages. For a full list of supported languages, see the [Supported Languages](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html) page.

### Advanced Options

For advanced users, `pdf2zh` offers several customization options:

- **Custom Translation Services**: Configure your own translation API keys.
- **Output Formatting**: Adjust the layout and style of the translated document.
- **Batch Processing**: Translate multiple files in one go.

Learn more in the [Advanced](https://pdf2zh-next.com/getting-started/ADVANCED.html) section.

### Community & Support

Join the community to get help, share feedback, or contribute to the project:

- **GitHub**: [https://github.com/p2z-ai/pdf2zh](https://github.com/p2z-ai/pdf2zh)
- **Discord**: [Join our Discord server](https://discord.gg/example)

For common questions, check the [FAQ](https://pdf2zh-next.com/getting-started/FAQ.html).

### Contributing

We welcome contributions! If you're interested in improving `pdf2zh` or adding new features, please read our [Contribution Guidelines](https://pdf2zh-next.com/getting-started/CONTRIBUTING.html).

For translators, see the [For Translators](https://pdf2zh-next.com/getting-started/FOR_TRANSLATORS.html) guide.

---

### TRANSLATION RESULT

### Resumen

`pdf2zh` es una herramienta diseñada para traducir documentos PDF del inglés al chino. Soporta traducción a través de varios servicios de traducción, incluyendo **DeepSeek**, **DeepL**, **OpenAI** y **Google Translate**. La herramienta puede manejar tanto texto como fórmulas matemáticas, garantizando traducciones precisas y de alta calidad.

### Características principales

- **Traducir PDFs**: Convierte PDFs en inglés a chino preservando el diseño y formato original.
- **Soporte de fórmulas matemáticas**: Traduce con precisión fórmulas matemáticas usando **PDFMathTranslate**.
- **Múltiples servicios de traducción**: Elige entre **DeepSeek**, **DeepL**, **OpenAI** o **Google Translate**.
- **Formatos de salida flexibles**: Genera documentos traducidos en formatos **PDF**, **LaTeX** o **Markdown**.
- **Fácil de usar**: Interfaz de línea de comandos simple y **WebUI** para una operación sin problemas.

### Empezar

Para comenzar con `pdf2zh`, sigue estos pasos:

1. **Instalación**: Instala la herramienta usando pip:

   ```bash
   pip install pdf2zh
   ```

2. **Uso básico**: Usa la línea de comandos para traducir un PDF:

   ```bash
   pdf2zh translate --file ruta/a/tu/archivo.pdf
   ```

3. **WebUI**: Alternativamente, usa la **WebUI** para una interfaz gráfica:

   ```bash
   pdf2zh webui
   ```

Para instrucciones detalladas, consulta la guía de [Uso](https://pdf2zh-next.com/getting-started/USAGE.html).

### Idiomas soportados

`pdf2zh` se enfoca principalmente en traducir del **inglés** al **chino**. Sin embargo, también soporta traducciones entre otros idiomas. Para una lista completa de idiomas soportados, consulta la página de [Idiomas soportados](https://pdf2zh-next.com/getting-started/SUPPORTED_LANGUAGES.html).

### Opciones avanzadas

Para usuarios avanzados, `pdf2zh` ofrece varias opciones de personalización:

- **Servicios de traducción personalizados**: Configura tus propias claves API de traducción.
- **Formateo de salida**: Ajusta el diseño y estilo del documento traducido.
- **Procesamiento por lotes**: Traduce múltiples archivos de una vez.

Aprende más en la sección [Opciones avanzadas](https://pdf2zh-next.com/getting-started/ADVANCED.html).

### Comunidad y soporte

Únete a la comunidad para obtener ayuda, compartir comentarios o contribuir al proyecto:

- **GitHub**: [https://github.com/p2z-ai/pdf2zh](https://github.com/p2z-ai/pdf2zh)
- **Discord**: [Únete a nuestro servidor de Discord](https://discord.gg/example)

Para preguntas comunes, consulta las [Preguntas frecuentes](https://pdf2zh-next.com/getting-started/FAQ.html).

### Contribuciones

¡Agradecemos las contribuciones! Si estás interesado en mejorar `pdf2zh` o añadir nuevas características, por favor lee nuestras [Guías de contribución](https://pdf2zh-next.com/getting-started/CONTRIBUTING.html).

Para traductores, consulta la guía [Guía de contribución de traducciones](https://pdf2zh-next.com/getting-started/FOR_TRANSLATORS.html).
- The events are:
    - `{"type": "progress", "data": {"progress": float, "message": str}}`
    - `{"type": "error", "data": {"error": str}}`
    - `{"type": "finish", "data": {"output_path": str, "pages": int, "translated_pages": int, "cost": float}}`

---

### TRANSLATION RESULT

- `do_translate_async_stream` es el punto de entrada asíncrono de bajo nivel que traduce un único PDF y produce un flujo de eventos (progreso/error/finalización).
- Es adecuado para construir tu propia interfaz de usuario o CLI donde quieras progreso en tiempo real y control total sobre los resultados.
- Acepta un SettingsModel validado y una ruta de archivo y devuelve un generador asíncrono de eventos dict.
- Los eventos son:
    - `{"type": "progress", "data": {"progress": float, "message": str}}`
    - `{"type": "error", "data": {"error": str}}`
    - `{"type": "finish", "data": {"output_path": str, "pages": int, "translated_pages": int, "cost": float}}`

- **File**: `src-tauri/src/commands/translation.rs`
- **Description**: This function is used to translate the text content of a PDF file.

```rust
#[tauri::command]
pub async fn translate_pdf(
    app_handle: tauri::AppHandle,
    path: String,
    from: String,
    to: String,
    service: String,
    ocr: bool,
) -> Result<String, String> {
    // Function implementation
}
```

### Parameters

- `app_handle`: The application handle, used to access the application's resources and state.
- `path`: The file path of the PDF file to be translated.
- `from`: The source language code (e.g., "en", "zh").
- `to`: The target language code (e.g., "en", "zh").
- `service`: The translation service to use (e.g., "google", "youdao", "deepl").
- `ocr`: A boolean value indicating whether to perform OCR on the PDF.

### Return Value

- Returns `Ok(String)` on success, where the string is a JSON object containing the translation result.
- Returns `Err(String)` on failure, where the string is an error message.

### Example

```json
{
    "path": "/path/to/translated.pdf",
    "pages": 100,
    "translated_pages": 100,
    "cost": 0.0
}
```

### Error Handling

- If the PDF file does not exist, returns an error.
- If the translation service is not supported, returns an error.
- If OCR is required but not available, returns an error.

---

### TRANSLATION RESULT

### Firma

- **Archivo**: `src-tauri/src/commands/translation.rs`
- **Descripción**: Esta función se utiliza para traducir el contenido de texto de un archivo PDF.

```rust
#[tauri::command]
pub async fn translate_pdf(
    app_handle: tauri::AppHandle,
    path: String,
    from: String,
    to: String,
    service: String,
    ocr: bool,
) -> Result<String, String> {
    // Implementación de la función
}
```

### Parámetros

- `app_handle`: El identificador de la aplicación, utilizado para acceder a los recursos y el estado de la aplicación.
- `path`: La ruta del archivo PDF a traducir.
- `from`: El código de idioma de origen (por ejemplo, "en", "zh").
- `to`: El código de idioma de destino (por ejemplo, "en", "zh").
- `service`: El servicio de traducción a utilizar (por ejemplo, "google", "youdao", "deepl").
- `ocr`: Un valor booleano que indica si se debe realizar OCR en el PDF.

### Valor de retorno

- Devuelve `Ok(String)` en caso de éxito, donde la cadena es un objeto JSON que contiene el resultado de la traducción.
- Devuelve `Err(String)` en caso de error, donde la cadena es un mensaje de error.

### Ejemplo

```json
{
    "path": "/ruta/al/archivo/traducido.pdf",
    "pages": 100,
    "translated_pages": 100,
    "cost": 0.0
}
```

### Manejo de errores

- Si el archivo PDF no existe, devuelve un error.
- Si el servicio de traducción no es compatible, devuelve un error.
- Si se requiere OCR pero no está disponible, devuelve un error.
- Returns: AsyncGenerator[TranslationEvent, None]. Yields TranslationEvent objects.
- Raises:
  - FileNotFoundError: If the file does not exist.
  - ValidationError: If the settings are invalid.
- Example:

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream
from pdf2zh_next.models import SettingsModel

async def main():
    settings = SettingsModel(
        target_language="zh",
        translation_service="google",
        translation_service_key="your-api-key",
    )
    async for event in do_translate_async_stream(settings, "input.pdf"):
        print(f"Event: {event.type}, Data: {event.data}")

asyncio.run(main())
```

- Event Types:
  - `start`: Translation started. Data: `{"file": "path/to/file.pdf"}`
  - `progress`: Translation progress. Data: `{"progress": 0.5, "message": "Translating page 10 of 20"}`
  - `result`: Translation completed. Data: `{"result": "path/to/translated.pdf"}`
  - `error`: Translation failed. Data: `{"error": "Error message"}`

- Notes:
  - This is a high-level function that handles the entire translation process.
  - Use this for simple integration where you just want to translate a PDF and get progress updates.
  - For more control, use the lower-level components directly.

---

### TRANSLATION RESULT

- Importar: `from pdf2zh_next.high_level import do_translate_async_stream`
- Llamar: `async for event in do_translate_async_stream(settings, file): ...`
- Parámetros:
  - settings: SettingsModel. Debe ser válido; la función llamará a `settings.validate_settings()`.
  - file: str | pathlib.Path. El PDF único a traducir. Debe existir.
- Retorna: AsyncGenerator[TranslationEvent, None]. Produce objetos TranslationEvent.
- Lanza:
  - FileNotFoundError: Si el archivo no existe.
  - ValidationError: Si la configuración no es válida.
- Ejemplo:

```python
import asyncio
from pdf2zh_next.high_level import do_translate_async_stream
from pdf2zh_next.models import SettingsModel

async def main():
    settings = SettingsModel(
        target_language="zh",
        translation_service="google",
        translation_service_key="your-api-key",
    )
    async for event in do_translate_async_stream(settings, "input.pdf"):
        print(f"Evento: {event.type}, Datos: {event.data}")

asyncio.run(main())
```

- Tipos de eventos:
  - `start`: Traducción iniciada. Datos: `{"file": "ruta/al/archivo.pdf"}`
  - `progress`: Progreso de la traducción. Datos: `{"progress": 0.5, "message": "Traduciendo página 10 de 20"}`
  - `result`: Traducción completada. Datos: `{"result": "ruta/al/archivo/traducido.pdf"}`
  - `error`: Traducción fallida. Datos: `{"error": "Mensaje de error"}`

- Notas:
  - Esta es una función de alto nivel que maneja todo el proceso de traducción.
  - Úsala para integraciones simples donde solo quieres traducir un PDF y obtener actualizaciones de progreso.
  - Para más control, usa los componentes de bajo nivel directamente.

The following is a list of all supported languages with their corresponding language codes. These codes are used to specify the target language when using the translation service.

### Supported Languages

| Language | Code |
|----------|------|
| Afrikaans | af |
| Albanian | sq |
| Amharic | am |
| Arabic | ar |
| Armenian | hy |
| Azerbaijani | az |
| Basque | eu |
| Belarusian | be |
| Bengali | bn |
| Bosnian | bs |
| Bulgarian | bg |
| Catalan | ca |
| Cebuano | ceb |
| Chichewa | ny |
| Chinese (Simplified) | zh |
| Chinese (Traditional) | zh-TW |
| Corsican | co |
| Croatian | hr |
| Czech | cs |
| Danish | da |
| Dutch | nl |
| English | en |
| Esperanto | eo |
| Estonian | et |
| Filipino | fil |
| Finnish | fi |
| French | fr |
| Frisian | fy |
| Galician | gl |
| Georgian | ka |
| German | de |
| Greek | el |
| Gujarati | gu |
| Haitian Creole | ht |
| Hausa | ha |
| Hawaiian | haw |
| Hebrew | he |
| Hindi | hi |
| Hmong | hmn |
| Hungarian | hu |
| Icelandic | is |
| Igbo | ig |
| Indonesian | id |
| Irish | ga |
| Italian | it |
| Japanese | ja |
| Javanese | jv |
| Kannada | kn |
| Kazakh | kk |
| Khmer | km |
| Korean | ko |
| Kurdish (Kurmanji) | ku |
| Kyrgyz | ky |
| Lao | lo |
| Latin | la |
| Latvian | lv |
| Lithuanian | lt |
| Luxembourgish | lb |
| Macedonian | mk |
| Malagasy | mg |
| Malay | ms |
| Malayalam | ml |
| Maltese | mt |
| Maori | mi |
| Marathi | mr |
| Mongolian | mn |
| Myanmar (Burmese) | my |
| Nepali | ne |
| Norwegian | no |
| Pashto | ps |
| Persian | fa |
| Polish | pl |
| Portuguese | pt |
| Punjabi | pa |
| Romanian | ro |
| Russian | ru |
| Samoan | sm |
| Scots Gaelic | gd |
| Serbian | sr |
| Sesotho | st |
| Shona | sn |
| Sindhi | sd |
| Sinhala | si |
| Slovak | sk |
| Slovenian | sl |
| Somali | so |
| Spanish | es |
| Sundanese | su |
| Swahili | sw |
| Swedish | sv |
| Tajik | tg |
| Tamil | ta |
| Telugu | te |
| Thai | th |
| Turkish | tr |
| Ukrainian | uk |
| Urdu | ur |
| Uzbek | uz |
| Vietnamese | vi |
| Welsh | cy |
| Xhosa | xh |
| Yiddish | yi |
| Yoruba | yo |
| Zulu | zu |

### Notes

- The language code is based on the ISO 639-1 standard where possible.
- For languages with multiple variants (like Chinese), specific codes are provided for each variant.
- Some languages may not be supported by all translation services. Please check the documentation of your chosen translation service for specific support details.

---

### TRANSLATION RESULT

Nota: La siguiente es una lista de todos los idiomas soportados con sus correspondientes códigos de idioma. Estos códigos se utilizan para especificar el idioma de destino al usar el servicio de traducción.

### Idiomas soportados

| Idioma | Código |
|--------|--------|
| Afrikaans | af |
| Albanés | sq |
| Amárico | am |
| Árabe | ar |
| Armenio | hy |
| Azerbaiyano | az |
| Vasco | eu |
| Bielorruso | be |
| Bengalí | bn |
| Bosnio | bs |
| Búlgaro | bg |
| Catalán | ca |
| Cebuano | ceb |
| Chichewa | ny |
| Chino (Simplificado) | zh |
| Chino (Tradicional) | zh-TW |
| Corso | co |
| Croata | hr |
| Checo | cs |
| Danés | da |
| Neerlandés | nl |
| Inglés | en |
| Esperanto | eo |
| Estonio | et |
| Filipino | fil |
| Finés | fi |
| Francés | fr |
| Frisón | fy |
| Gallego | gl |
| Georgiano | ka |
| Alemán | de |
| Griego | el |
| Gujarati | gu |
| Criollo haitiano | ht |
| Hausa | ha |
| Hawaiano | haw |
| Hebreo | he |
| Hindi | hi |
| Hmong | hmn |
| Húngaro | hu |
| Islandés | is |
| Igbo | ig |
| Indonesio | id |
| Irlandés | ga |
| Italiano | it |
| Japonés | ja |
| Javanés | jv |
| Canarés | kn |
| Kazajo | kk |
| Jemer | km |
| Coreano | ko |
| Kurdo (Kurmanji) | ku |
| Kirguís | ky |
| Lao | lo |
| Latín | la |
| Letón | lv |
| Lituano | lt |
| Luxemburgués | lb |
| Macedonio | mk |
| Malgache | mg |
| Malayo | ms |
| Malayalam | ml |
| Maltés | mt |
| Maorí | mi |
| Marathi | mr |
| Mongol | mn |
| Birmano | my |
| Nepalí | ne |
| Noruego | no |
| Pastún | ps |
| Persa | fa |
| Polaco | pl |
| Portugués | pt |
| Punjabi | pa |
| Rumano | ro |
| Ruso | ru |
| Samoano | sm |
| Gaélico escocés | gd |
| Serbio | sr |
| Sesotho | st |
| Shona | sn |
| Sindhi | sd |
| Cingalés | si |
| Eslovaco | sk |
| Esloveno | sl |
| Somalí | so |
| Español | es |
| Sondanés | su |
| Suajili | sw |
| Sueco | sv |
| Tayiko | tg |
| Tamil | ta |
| Telugu | te |
| Tailandés | th |
| Turco | tr |
| Ucraniano | uk |
| Urdu | ur |
| Uzbeko | uz |
| Vietnamita | vi |
| Galés | cy |
| Xhosa | xh |
| Yidis | yi |
| Yoruba | yo |
| Zulú | zu |

### Notas

- El código de idioma se basa en el estándar ISO 639-1 cuando es posible.
- Para idiomas con múltiples variantes (como el chino), se proporcionan códigos específicos para cada variante.
- Algunos idiomas pueden no ser soportados por todos los servicios de traducción. Por favor, consulta la documentación de tu servicio de traducción elegido para detalles específicos de soporte.
- `translator.translate_async` is the underlying function that does the translation; this function wraps it to provide events.

---

### TRANSLATION RESULT

- settings.basic.input_files es ignorado por esta función; solo se traduce el `file` dado.
- Si `settings.basic.debug` es True, la traducción se ejecuta en el proceso principal; de lo contrario, se ejecuta en un subproceso. El esquema de eventos es idéntico para ambos.
- `translator.translate_async` es la función subyacente que realiza la traducción; esta función la envuelve para proporcionar eventos.

This document describes the event stream contract for the `pdf2zh` application. The event stream is a server-sent events (SSE) stream that provides real-time updates on the translation process.

#### Event Types

The following event types are defined:

- `progress`: Indicates the progress of the translation process.
- `result`: Indicates that the translation is complete and provides the result.
- `error`: Indicates that an error has occurred.

#### Event Data

Each event has a `data` field that contains a JSON object. The structure of the JSON object depends on the event type.

##### Progress Event

The `progress` event has the following structure:

```json
{
  "type": "progress",
  "data": {
    "progress": 0.5,
    "message": "Translating page 10 of 20"
  }
}
```

- `progress`: A number between 0 and 1 indicating the progress of the translation.
- `message`: A human-readable message describing the current progress.

##### Result Event

The `result` event has the following structure:

```json
{
  "type": "result",
  "data": {
    "result": "The translated text"
  }
}
```

- `result`: The translated text.

##### Error Event

The `error` event has the following structure:

```json
{
  "type": "error",
  "data": {
    "error": "An error occurred"
  }
}
```

- `error`: A human-readable error message.

#### Example

Here is an example of an event stream:

```
event: progress
data: {"type":"progress","data":{"progress":0.5,"message":"Translating page 10 of 20"}}

event: result
data: {"type":"result","data":{"result":"The translated text"}}
```

#### Client Implementation

Clients should listen for the `message` event and parse the `data` field as JSON. The `type` field of the JSON object indicates the event type.

Here is an example client implementation in JavaScript:

```javascript
const eventSource = new EventSource('/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  switch (data.type) {
    case 'progress':
      console.log(`Progress: ${data.data.progress * 100}% - ${data.data.message}`);
      break;
    case 'result':
      console.log(`Result: ${data.data.result}`);
      break;
    case 'error':
      console.error(`Error: ${data.data.error}`);
      break;
  }
};
```

---

Now, please translate the `ORIGINAL TEXT` into **es**.
- `start`: Emitted when the translation starts. The data contains the total number of pages.
- `page_success`: Emitted when a page is successfully translated. The data contains the page number and the translated text.
- `page_skip`: Emitted when a page is skipped. The data contains the page number and the reason for skipping.
- `page_error`: Emitted when an error occurs while translating a page. The data contains the page number and the error message.
- `complete`: Emitted when the translation is complete. The data contains the path to the translated file.
- `error`: Emitted when a fatal error occurs. The data contains the error message.

Example of `start` event:
```json
{"type": "start", "data": {"total_pages": 100}}
```

Example of `page_success` event:
```json
{"type": "page_success", "data": {"page": 1, "translated_text": "This is the translated text."}}
```

Example of `page_skip` event:
```json
{"type": "page_skip", "data": {"page": 2, "reason": "Empty page"}}
```

Example of `page_error` event:
```json
{"type": "page_error", "data": {"page": 3, "error": "Translation service error"}}
```

Example of `complete` event:
```json
{"type": "complete", "data": {"output_path": "/path/to/output.pdf"}}
```

Example of `error` event:
```json
{"type": "error", "data": {"error": "Failed to open PDF file"}}
```

### TRANSLATION RESULT

El generador asíncrono produce eventos de tipo diccionario JSON con los siguientes tipos:
- `start`: Emitido cuando la traducción comienza. Los datos contienen el número total de páginas.
- `page_success`: Emitido cuando una página se traduce exitosamente. Los datos contienen el número de página y el texto traducido.
- `page_skip`: Emitido cuando se omite una página. Los datos contienen el número de página y la razón de la omisión.
- `page_error`: Emitido cuando ocurre un error al traducir una página. Los datos contienen el número de página y el mensaje de error.
- `complete`: Emitido cuando la traducción se completa. Los datos contienen la ruta al archivo traducido.
- `error`: Emitido cuando ocurre un error fatal. Los datos contienen el mensaje de error.

Ejemplo de evento `start`:
```json
{"type": "start", "data": {"total_pages": 100}}
```

Ejemplo de evento `page_success`:
```json
{"type": "page_success", "data": {"page": 1, "translated_text": "Este es el texto traducido."}}
```

Ejemplo de evento `page_skip`:
```json
{"type": "page_skip", "data": {"page": 2, "reason": "Página vacía"}}
```

Ejemplo de evento `page_error`:
```json
{"type": "page_error", "data": {"page": 3, "error": "Error del servicio de traducción"}}
```

Ejemplo de evento `complete`:
```json
{"type": "complete", "data": {"output_path": "/ruta/al/archivo/output.pdf"}}
```

Ejemplo de evento `error`:
```json
{"type": "error", "data": {"error": "Error al abrir el archivo PDF"}}
```

- `part_index`: part index where the error occurred (if applicable)
    - `total_parts`: total number of parts (if applicable)

- Note: All events are **optional**. The client should handle missing events gracefully.

- ### Stage summary event: `stage_summary` (opcional, puede aparecer primero)
  - Campos
    - `type`: "stage_summary"
    - `stages`: lista de objetos `{ "name": str, "percent": float }` que describe la distribución estimada del trabajo
    - `part_index`: puede ser 0 para este evento de resumen
    - `total_parts`: número total de partes (>= 1)

- Eventos de progreso: `progress_start`, `progress_update`, `progress_end`
  - Campos comunes
    - `type`: uno de los anteriores
    - `stage`: nombre de la etapa legible por humanos (por ejemplo, "Analizar PDF y crear representación intermedia", "Traducir párrafos", "Guardar PDF")
    - `stage_progress`: flotante en [0, 100] que indica el progreso dentro de la etapa actual
    - `overall_progress`: flotante en [0, 100] que indica el progreso general
    - `part_index`: índice de parte actual (típicamente basado en 1 para eventos de progreso)
    - `total_parts`: número total de partes (>= 1). Los documentos grandes pueden dividirse automáticamente.
    - `stage_current`: paso actual dentro de la etapa
    - `stage_total`: pasos totales dentro de la etapa

- Evento de finalización: `finish`
  - Campos
    - `type`: "finish"
    - `translate_result`: un **objeto** que proporciona salidas finales (NOTA: no un diccionario, sino una instancia de clase)
      - `original_pdf_path`: Ruta al PDF de entrada
      - `mono_pdf_path`: Ruta al PDF traducido monolingüe (o None)
      - `dual_pdf_path`: Ruta al PDF traducido bilingüe (o None)
      - `no_watermark_mono_pdf_path`: Ruta a la salida monolingüe sin marca de agua (si se produjo), de lo contrario None
      - `no_watermark_dual_pdf_path`: Ruta a la salida bilingüe sin marca de agua (si se produjo), de lo contrario None
      - `auto_extracted_glossary_path`: Ruta al glosario CSV extraído automáticamente (o None)
      - `total_seconds`: segundos transcurridos (flotante)
      - `peak_memory_usage`: uso máximo aproximado de memoria durante la traducción (flotante; unidades dependientes de la implementación)

- Evento de error: `error`
  - Campos
    - `type`: "error"
    - `error`: mensaje de error legible por humanos
    - `error_type`: uno de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details`: detalles opcionales (por ejemplo, error original o traza de ejecución)
    - `part_index`: índice de parte donde ocurrió el error (si es aplicable)
    - `total_parts`: número total de partes (si es aplicable)

- Nota: Todos los eventos son **opcionales**. El cliente debe manejar eventos faltantes con gracia.

---

### TRANSLATION RESULT

- Evento de resumen de etapa: `stage_summary` (opcional, puede aparecer primero)
  - Campos
    - `type`: "stage_summary"
    - `stages`: lista de objetos `{ "name": str, "percent": float }` que describe la distribución estimada del trabajo
    - `part_index`: puede ser 0 para este evento de resumen
    - `total_parts`: número total de partes (>= 1)

- Eventos de progreso: `progress_start`, `progress_update`, `progress_end`
  - Campos comunes
    - `type`: uno de los anteriores
    - `stage`: nombre de la etapa legible por humanos (por ejemplo, "Analizar PDF y crear representación intermedia", "Traducir párrafos", "Guardar PDF")
    - `stage_progress`: flotante en [0, 100] que indica el progreso dentro de la etapa actual
    - `overall_progress`: flotante en [0, 100] que indica el progreso general
    - `part_index`: índice de parte actual (típicamente basado en 1 para eventos de progreso)
    - `total_parts`: número total de partes (>= 1). Los documentos grandes pueden dividirse automáticamente.
    - `stage_current`: paso actual dentro de la etapa
    - `stage_total`: pasos totales dentro de la etapa

- Evento de finalización: `finish`
  - Campos
    - `type`: "finish"
    - `translate_result`: un **objeto** que proporciona salidas finales (NOTA: no un diccionario, sino una instancia de clase)
      - `original_pdf_path`: Ruta al PDF de entrada
      - `mono_pdf_path`: Ruta al PDF traducido monolingüe (o None)
      - `dual_pdf_path`: Ruta al PDF traducido bilingüe (o None)
      - `no_watermark_mono_pdf_path`: Ruta a la salida monolingüe sin marca de agua (si se produjo), de lo contrario None
      - `no_watermark_dual_pdf_path`: Ruta a la salida bilingüe sin marca de agua (si se produjo), de lo contrario None
      - `auto_extracted_glossary_path`: Ruta al glosario CSV extraído automáticamente (o None)
      - `total_seconds`: segundos transcurridos (flotante)
      - `peak_memory_usage`: uso máximo aproximado de memoria durante la traducción (flotante; unidades dependientes de la implementación)

- Evento de error: `error`
  - Campos
    - `type`: "error"
    - `error`: mensaje de error legible por humanos
    - `error_type`: uno de `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError`, etc.
    - `details`: detalles opcionales (por ejemplo, error original o traza de ejecución)
    - `part_index`: índice de parte donde ocurrió el error (si es aplicable)
    - `total_parts`: número total de partes (si es aplicable)

- Nota: Todos los eventos son **opcionales**. El cliente debe manejar eventos faltantes con gracia.

This function will check the `output_path` first. If the file already exists, it will skip the translation and return the existing file path immediately.

### Parameters

- `file_path` (str): Path to the PDF file to be translated.
- `target_language` (str): The target language to translate to, using the [Language Code](#supported-languages).
- `output_path` (str): The path to save the translated PDF file.
- `api_key` (str): Your OpenAI API key.
- `model` (str, optional): The model to use for translation. Default is `gpt-4o`.
- `pages` (str, optional): Specify pages to translate. For example, `1,3,5-9`. If not provided, all pages will be translated.
- `proxy` (str, optional): Proxy to use for the request. For example, `http://127.0.0.1:7890`.
- `api_base` (str, optional): The base URL for the API. Default is `https://api.openai.com/v1`.

### Returns

- `str`: The path to the translated PDF file.

### Example

```python
from pdf2zh import do_translate

result = do_translate(
    file_path="input.pdf",
    target_language="zh",
    output_path="output.pdf",
    api_key="your-api-key"
)
print(f"Translated file saved at: {result}")
```

### Notes

- This function is synchronous and will block until the translation is complete.
- If you need real-time progress updates, consider using the async version `do_translate_async_stream`.

---

### TRANSLATION RESULT

Comportamiento importante: Esta función verificará primero la `output_path`. Si el archivo ya existe, omitirá la traducción y devolverá inmediatamente la ruta del archivo existente.

### Parámetros

- `file_path` (str): Ruta al archivo PDF a traducir.
- `target_language` (str): El idioma objetivo al que traducir, usando el [Código de idioma](#idiomas-soportados).
- `output_path` (str): La ruta para guardar el archivo PDF traducido.
- `api_key` (str): Tu clave de API de OpenAI.
- `model` (str, opcional): El modelo a usar para la traducción. Por defecto es `gpt-4o`.
- `pages` (str, opcional): Especifica las páginas a traducir. Por ejemplo, `1,3,5-9`. Si no se proporciona, se traducirán todas las páginas.
- `proxy` (str, opcional): Proxy a usar para la solicitud. Por ejemplo, `http://127.0.0.1:7890`.
- `api_base` (str, opcional): La URL base para la API. Por defecto es `https://api.openai.com/v1`.

### Retorna

- `str`: La ruta al archivo PDF traducido.

### Ejemplo

```python
from pdf2zh import do_translate

result = do_translate(
    file_path="input.pdf",
    target_language="zh",
    output_path="output.pdf",
    api_key="your-api-key"
)
print(f"Archivo traducido guardado en: {result}")
```

### Notas

- Esta función es síncrona y se bloqueará hasta que la traducción se complete.
- Si necesitas actualizaciones de progreso en tiempo real, considera usar la versión asíncrona `do_translate_async_stream`.
- The `finish` event is guaranteed to be the last event in the stream.

---

### TRANSLATION RESULT

- Un `stage_summary` opcional puede emitirse antes de que comience el progreso.
- En ciertos fallos, el generador primero producirá un evento `error` y luego lanzará una excepción derivada de `TranslationError`. Debes verificar tanto los eventos de error como estar preparado para capturar excepciones.
- Los eventos `progress_update` pueden repetirse con valores idénticos; los consumidores deben eliminar rebotes si es necesario.
- Deja de consumir el flujo cuando recibas un evento `finish`.
- Se garantiza que el evento `finish` será el último evento en el flujo.

{#minimal-usage-example-async}

```python
from pdf2zh import pdf2zh
import asyncio

async def main():
    translator = pdf2zh.PDFTranslator()
    await translator.translate("input.pdf", "output.pdf")

asyncio.run(main())
```

### Minimal Usage Example (Sync) {#minimal-usage-example-sync}

```python
from pdf2zh import pdf2zh

translator = pdf2zh.PDFTranslator()
translator.translate_sync("input.pdf", "output.pdf")
```

### Advanced Usage Example (Async) {#advanced-usage-example-async}

```python
from pdf2zh import pdf2zh, Config
import asyncio

async def main():
    config = Config(
        source_language="en",  # source language code
        target_language="zh",  # target language code
        ocr_service="default",  # ocr service
        translation_service="google",  # translation service
        translation_service_key="",  # translation service key
        enable_glossary=True,  # enable glossary
        enable_parallel=True,  # enable parallel translation
        max_concurrency=10,  # max concurrency for parallel translation
    )
    translator = pdf2zh.PDFTranslator(config=config)
    await translator.translate("input.pdf", "output.pdf")

asyncio.run(main())
```

### Advanced Usage Example (Sync) {#advanced-usage-example-sync}

```python
from pdf2zh import pdf2zh, Config

config = Config(
    source_language="en",  # source language code
    target_language="zh",  # target language code
    ocr_service="default",  # ocr service
    translation_service="google",  # translation service
    translation_service_key="",  # translation service key
    enable_glossary=True,  # enable glossary
    enable_parallel=True,  # enable parallel translation
    max_concurrency=10,  # max concurrency for parallel translation
)
translator = pdf2zh.PDFTranslator(config=config)
translator.translate_sync("input.pdf", "output.pdf")
```

### Ejemplo de uso mínimo (Async) {#ejemplo-de-uso-mínimo-async}

```python
from pdf2zh import pdf2zh
import asyncio

async def main():
    translator = pdf2zh.PDFTranslator()
    await translator.translate("input.pdf", "output.pdf")

asyncio.run(main())
```

### Ejemplo de uso mínimo (Sync) {#ejemplo-de-uso-mínimo-sync}

```python
from pdf2zh import pdf2zh

translator = pdf2zh.PDFTranslator()
translator.translate_sync("input.pdf", "output.pdf")
```

### Ejemplo de uso avanzado (Async) {#ejemplo-de-uso-avanzado-async}

```python
from pdf2zh import pdf2zh, Config
import asyncio

async def main():
    config = Config(
        source_language="en",  # código de idioma de origen
        target_language="zh",  # código de idioma de destino
        ocr_service="default",  # servicio de OCR
        translation_service="google",  # servicio de traducción
        translation_service_key="",  # clave del servicio de traducción
        enable_glossary=True,  # habilitar glosario
        enable_parallel=True,  # habilitar traducción paralela
        max_concurrency=10,  # máxima concurrencia para traducción paralela
    )
    translator = pdf2zh.PDFTranslator(config=config)
    await translator.translate("input.pdf", "output.pdf")

asyncio.run(main())
```

### Ejemplo de uso avanzado (Sync) {#ejemplo-de-uso-avanzado-sync}

```python
from pdf2zh import pdf2zh, Config

config = Config(
    source_language="en",  # código de idioma de origen
    target_language="zh",  # código de idioma de destino
    ocr_service="default",  # servicio de OCR
    translation_service="google",  # servicio de traducción
    translation_service_key="",  # clave del servicio de traducción
    enable_glossary=True,  # habilitar glosario
    enable_parallel=True,  # habilitar traducción paralela
    max_concurrency=10,  # máxima concurrencia para traducción paralela
)
translator = pdf2zh.PDFTranslator(config=config)
translator.translate_sync("input.pdf", "output.pdf")
```
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

**Last updated: 2025-01-01**

Thank you for using **pdf2zh**. This Cancellation and Refund Policy outlines our guidelines regarding cancellations and refunds for services provided through our platform. By using our services, you agree to this policy.

#### 1. Cancellation Policy

- **Free Services**: Our basic translation services are provided free of charge. You may discontinue use at any time without any cancellation process.
- **Paid Services**: For any premium or paid features, you may cancel your subscription at any time through your account settings. Cancellation will take effect at the end of your current billing cycle.

#### 2. Refund Policy

- **Free Services**: Since our basic services are free, no refunds are applicable.
- **Paid Services**:
    - We offer refunds for paid services within **7 days** of purchase if you are dissatisfied with the service.
    - To request a refund, please contact us at [support@pdf2zh.com](mailto:support@pdf2zh.com) with your transaction details.
    - Refunds will be processed within **14 business days** after approval.

#### 3. Changes to This Policy

We may update this Cancellation and Refund Policy from time to time. Any changes will be posted on this page with an updated "Last updated" date.

#### 4. Contact Us

If you have any questions about this policy, please contact us at [support@pdf2zh.com](mailto:support@pdf2zh.com).

---

### TARGET LANGUAGE

es
The stream will be closed, and the translation process will be terminated.

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    # Create the async generator
    stream = do_translate_async_stream(
        file_path="input.pdf",
        target_language="zh",
        output_path="output.pdf",
        api_key="your-api-key"
    )
    
    # Iterate through the stream
    try:
        async for progress in stream:
            print(f"Progress: {progress}")
            if progress > 0.5:
                # Cancel the stream when progress exceeds 50%
                await stream.aclose()
                break
    except asyncio.CancelledError:
        print("Translation was cancelled")

asyncio.run(main())
```

### Notes

- When you cancel the stream, the underlying translation process is terminated.
- Any partially translated output will not be saved.
- The cancellation is graceful - the stream is closed and resources are cleaned up.

---

### TRANSLATION RESULT

Puedes cancelar la tarea que consume el flujo. La cancelación se propaga al proceso de traducción subyacente.
El flujo se cerrará y el proceso de traducción se terminará.

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    # Crear el generador asíncrono
    stream = do_translate_async_stream(
        file_path="input.pdf",
        target_language="zh",
        output_path="output.pdf",
        api_key="your-api-key"
    )
    
    # Iterar a través del flujo
    try:
        async for progress in stream:
            print(f"Progress: {progress}")
            if progress > 0.5:
                # Cancelar el flujo cuando el progreso exceda el 50%
                await stream.aclose()
                break
    except asyncio.CancelledError:
        print("La traducción fue cancelada")

asyncio.run(main())
```

### Notas

- Cuando cancelas el flujo, el proceso de traducción subyacente se termina.
- Cualquier salida traducida parcialmente no se guardará.
- La cancelación es elegante: el flujo se cierra y los recursos se liberan.

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

The following examples show how to use the `EventShape` class to define different shapes for events.

#### Example 1: Rectangle

```python
from pdf2zh.events import EventShape

# Create a rectangle shape
rect_shape = EventShape(
    shape_type="rectangle",
    x=10,
    y=20,
    width=100,
    height=50,
    color="blue"
)
```

#### Example 2: Circle

```python
from pdf2zh.events import EventShape

# Create a circle shape
circle_shape = EventShape(
    shape_type="circle",
    x=50,
    y=50,
    radius=30,
    color="red"
)
```

#### Example 3: Custom Path

```python
from pdf2zh.events import EventShape

# Create a custom path shape
path_shape = EventShape(
    shape_type="path",
    path_data="M10 10 L90 10 L50 90 Z",  # Triangle
    color="green"
)
```

### Event Shape Properties

Each `EventShape` has the following properties:

- `shape_type`: The type of shape ("rectangle", "circle", "path")
- `x`: X-coordinate position (for rectangle and circle)
- `y`: Y-coordinate position (for rectangle and circle)
- `width`: Width (for rectangle)
- `height`: Height (for rectangle)
- `radius`: Radius (for circle)
- `path_data`: SVG path data (for custom paths)
- `color`: Fill color of the shape

### Usage in Events

Event shapes can be used when creating events to define their visual representation:

```python
from pdf2zh.events import Event

# Create an event with a custom shape
event = Event(
    name="custom_event",
    shape=circle_shape,  # Use the circle shape defined earlier
    trigger=lambda: print("Event triggered!")
)
```

### Dynamic Shape Creation

You can also create shapes dynamically based on conditions:

```python
def create_shape_based_on_condition(condition):
    if condition == "rectangle":
        return EventShape(shape_type="rectangle", x=10, y=10, width=100, height=50)
    else:
        return EventShape(shape_type="circle", x=50, y=50, radius=25)
```

### Shape Animation

Event shapes can be animated by modifying their properties over time:

```python
import time

# Animate a shape moving across the screen
shape = EventShape(shape_type="rectangle", x=0, y=0, width=50, height=50, color="blue")

for i in range(100):
    shape.x = i  # Move the shape horizontally
    time.sleep(0.1)  # Wait a bit between movements
```

### Multiple Shapes for One Event

An event can have multiple shapes by using shape groups:

```python
from pdf2zh.events import EventShapeGroup

# Create multiple shapes
shape1 = EventShape(shape_type="rectangle", x=10, y=10, width=50, height=50)
shape2 = EventShape(shape_type="circle", x=70, y=70, radius=25)

# Create a shape group
shape_group = EventShapeGroup(shapes=[shape1, shape2])

# Use the shape group in an event
event = Event(
    name="multi_shape_event",
    shape=shape_group,
    trigger=lambda: print("Multi-shape event triggered!")
)
```

### Shape Visibility

Control shape visibility using the `visible` property:

```python
shape = EventShape(shape_type="rectangle", x=10, y=10, width=50, height=50)

# Make the shape invisible
shape.visible = False

# Later, make it visible again
shape.visible = True
```

### Shape Interaction

Shapes can respond to user interactions:

```python
shape = EventShape(shape_type="rectangle", x=10, y=10, width=50, height=50)

# Define what happens when the shape is clicked
def on_shape_click():
    print("Shape clicked!")
    shape.color = "red"  # Change color on click

# Assign the click handler
shape.on_click = on_shape_click
```

### Best Practices

1. **Reuse Shapes**: Create shape templates and reuse them across multiple events
2. **Keep it Simple**: Use simple shapes for better performance
3. **Consistent Styling**: Maintain consistent colors and styles across related events
4. **Test Visibility**: Ensure shapes are visible against different backgrounds

### Common Issues

- **Shape Not Visible**: Check if the shape coordinates are within the visible area
- **Wrong Color Format**: Use valid color names or hex codes ("#FF0000")
- **Performance Issues**: Too many complex shapes can impact performance

### See Also

- [Event System Overview](events.md)
- [Event Class Documentation](event_class.md)
- [Animation Guide](animation.md)

---

### TRANSLATION RESULT

### Ejemplos de formas de eventos

Los siguientes ejemplos muestran cómo usar la clase `EventShape` para definir diferentes formas para eventos.

#### Ejemplo 1: Rectángulo

```python
from pdf2zh.events import EventShape

# Crear una forma de rectángulo
rect_shape = EventShape(
    shape_type="rectangle",
    x=10,
    y=20,
    width=100,
    height=50,
    color="blue"
)
```

#### Ejemplo 2: Círculo

```python
from pdf2zh.events import EventShape

# Crear una forma de círculo
circle_shape = EventShape(
    shape_type="circle",
    x=50,
    y=50,
    radius=30,
    color="red"
)
```

#### Ejemplo 3: Ruta personalizada

```python
from pdf2zh.events import EventShape

# Crear una forma de ruta personalizada
path_shape = EventShape(
    shape_type="path",
    path_data="M10 10 L90 10 L50 90 Z",  # Triángulo
    color="green"
)
```

### Propiedades de formas de eventos

Cada `EventShape` tiene las siguientes propiedades:

- `shape_type`: El tipo de forma ("rectangle", "circle", "path")
- `x`: Posición de coordenada X (para rectángulo y círculo)
- `y`: Posición de coordenada Y (para rectángulo y círculo)
- `width`: Ancho (para rectángulo)
- `height`: Altura (para rectángulo)
- `radius`: Radio (para círculo)
- `path_data`: Datos de ruta SVG (para rutas personalizadas)
- `color`: Color de relleno de la forma

### Uso en eventos

Las formas de eventos se pueden usar al crear eventos para definir su representación visual:

```python
from pdf2zh.events import Event

# Crear un evento con una forma personalizada
event = Event(
    name="custom_event",
    shape=circle_shape,  # Usar la forma de círculo definida anteriormente
    trigger=lambda: print("¡Evento activado!")
)
```

### Creación dinámica de formas

También puedes crear formas dinámicamente según condiciones:

```python
def create_shape_based_on_condition(condition):
    if condition == "rectangle":
        return EventShape(shape_type="rectangle", x=10, y=10, width=100, height=50)
    else:
        return EventShape(shape_type="circle", x=50, y=50, radius=25)
```

### Animación de formas

Las formas de eventos se pueden animar modificando sus propiedades con el tiempo:

```python
import time

# Animar una forma moviéndose por la pantalla
shape = EventShape(shape_type="rectangle", x=0, y=0, width=50, height=50, color="blue")

for i in range(100):
    shape.x = i  # Mover la forma horizontalmente
    time.sleep(0.1)  # Esperar un poco entre movimientos
```

### Múltiples formas para un evento

Un evento puede tener múltiples formas usando grupos de formas:

```python
from pdf2zh.events import EventShapeGroup

# Crear múltiples formas
shape1 = EventShape(shape_type="rectangle", x=10, y=10, width=50, height=50)
shape2 = EventShape(shape_type="circle", x=70, y=70, radius=25)

# Crear un grupo de formas
shape_group = EventShapeGroup(shapes=[shape1, shape2])

# Usar el grupo de formas en un evento
event = Event(
    name="multi_shape_event",
    shape=shape_group,
    trigger=lambda: print("¡Evento de múltiples formas activado!")
)
```

### Visibilidad de formas

Controlar la visibilidad de formas usando la propiedad `visible`:

```python
shape = EventShape(shape_type="rectangle", x=10, y=10, width=50, height=50)

# Hacer la forma invisible
shape.visible = False

# Después, hacerla visible nuevamente
shape.visible = True
```

### Interacción de formas

Las formas pueden responder a interacciones del usuario:

```python
shape = EventShape(shape_type="rectangle", x=10, y=10, width=50, height=50)

# Definir qué pasa cuando se hace clic en la forma
def on_shape_click():
    print("¡Forma clickeada!")
    shape.color = "red"  # Cambiar color al hacer clic

# Asignar el manejador de clic
shape.on_click = on_shape_click
```

### Mejores prácticas

1. **Reutilizar formas**: Crear plantillas de formas y reutilizarlas en múltiples eventos
2. **Mantenerlo simple**: Usar formas simples para mejor rendimiento
3. **Estilo consistente**: Mantener colores y estilos consistentes en eventos relacionados
4. **Probar visibilidad**: Asegurar que las formas sean visibles contra diferentes fondos

### Problemas comunes

- **Forma no visible**: Verificar si las coordenadas de la forma están dentro del área visible
- **Formato de color incorrecto**: Usar nombres de color válidos o códigos hexadecimales ("#FF0000")
- **Problemas de rendimiento**: Demasiadas formas complejas pueden afectar el rendimiento

### Ver también

- [Resumen del sistema de eventos](events.md)
- [Documentación de la clase Event](event_class.md)
- [Guía de animación](animation.md)
This is an example of a stage summary event that occurs at the end of each translation stage.

```json
{
    "type": "stage_summary",
    "data": {
        "stage": "translation",
        "status": "completed",
        "metrics": {
            "total_pages": 100,
            "processed_pages": 100,
            "successful_pages": 95,
            "failed_pages": 5,
            "total_characters": 50000,
            "translated_characters": 49500
        },
        "duration": 120.5,
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-01T00:02:00Z"
    }
}
```

### Event Details

- **type**: Always "stage_summary" for stage summary events.
- **data**: Contains the summary information for the stage.
    - **stage**: The name of the stage (e.g., "translation", "ocr", "formatting").
    - **status**: The status of the stage ("completed", "failed", "cancelled").
    - **metrics**: Various metrics about the stage's execution.
        - **total_pages**: The total number of pages in the document.
        - **processed_pages**: The number of pages processed in this stage.
        - **successful_pages**: The number of pages successfully processed.
        - **failed_pages**: The number of pages that failed processing.
        - **total_characters**: The total number of characters in the document.
        - **translated_characters**: The number of characters translated.
    - **duration**: The duration of the stage in seconds.
    - **start_time**: The start time of the stage in ISO 8601 format.
    - **end_time**: The end time of the stage in ISO 8601 format.

### Example Usage

Clients can use stage summary events to:

1. Track the progress of each stage in the translation process.
2. Display statistics about the translation to the user.
3. Identify stages that are taking longer than expected or failing frequently.
4. Generate reports on translation performance.

### Error Handling

If a stage fails, the status will be "failed", and the metrics will reflect the number of failed pages. The event may also include an error message in the `data` field if available.

### Related Events

- Stage start event: Indicates the start of a stage.
- Stage progress event: Provides incremental progress updates during a stage.
- Stage end event: Indicates the end of a stage (success or failure).

---

### TRANSLATION RESULT

Evento de resumen de etapa (ejemplo): Este es un ejemplo de un evento de resumen de etapa que ocurre al final de cada etapa de traducción.

```json
{
    "type": "stage_summary",
    "data": {
        "stage": "translation",
        "status": "completed",
        "metrics": {
            "total_pages": 100,
            "processed_pages": 100,
            "successful_pages": 95,
            "failed_pages": 5,
            "total_characters": 50000,
            "translated_characters": 49500
        },
        "duration": 120.5,
        "start_time": "2024-01-01T00:00:00Z",
        "end_time": "2024-01-01T00:02:00Z"
    }
}
```

### Detalles del evento

- **type**: Siempre "stage_summary" para eventos de resumen de etapa.
- **data**: Contiene la información de resumen de la etapa.
    - **stage**: El nombre de la etapa (por ejemplo, "translation", "ocr", "formatting").
    - **status**: El estado de la etapa ("completed", "failed", "cancelled").
    - **metrics**: Varias métricas sobre la ejecución de la etapa.
        - **total_pages**: El número total de páginas en el documento.
        - **processed_pages**: El número de páginas procesadas en esta etapa.
        - **successful_pages**: El número de páginas procesadas exitosamente.
        - **failed_pages**: El número de páginas que fallaron en el procesamiento.
        - **total_characters**: El número total de caracteres en el documento.
        - **translated_characters**: El número de caracteres traducidos.
    - **duration**: La duración de la etapa en segundos.
    - **start_time**: La hora de inicio de la etapa en formato ISO 8601.
    - **end_time**: La hora de finalización de la etapa en formato ISO 8601.

### Ejemplo de uso

Los clientes pueden usar eventos de resumen de etapa para:

1. Seguir el progreso de cada etapa en el proceso de traducción.
2. Mostrar estadísticas sobre la traducción al usuario.
3. Identificar etapas que están tomando más tiempo de lo esperado o fallando frecuentemente.
4. Generar reportes sobre el rendimiento de la traducción.

### Manejo de errores

Si una etapa falla, el estado será "failed", y las métricas reflejarán el número de páginas fallidas. El evento también puede incluir un mensaje de error en el campo `data` si está disponible.

### Eventos relacionados

- Evento de inicio de etapa: Indica el inicio de una etapa.
- Evento de progreso de etapa: Proporciona actualizaciones de progreso incremental durante una etapa.
- Evento de fin de etapa: Indica el final de una etapa (éxito o fallo).
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
        "message": "Translating page 10 of 20"
    }
}
```

Result event (example): 
```json
{
    "type": "result",
    "data": {
        "result": "The translated text"
    }
}
```

Error event (example): 
```json
{
    "type": "error",
    "data": {
        "error": "An error occurred"
    }
}
```

---

### TRANSLATION RESULT

Evento de progreso (ejemplo):
```json
{
    "type": "progress",
    "data": {
        "progress": 0.5,
        "message": "Traduciendo página 10 de 20"
    }
}
```

Evento de resultado (ejemplo):
```json
{
    "type": "result",
    "data": {
        "result": "El texto traducido"
    }
}
```

Evento de error (ejemplo):
```json
{
    "type": "error",
    "data": {
        "error": "Ocurrió un error"
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
    "type": "finish",
    "data": {
        "path": "/path/to/translated.pdf",
        "pages": 100,
        "translated_pages": 100,
        "cost": 0.0
    }
}
```

---

### TRANSLATION RESULT

Evento de finalización (ejemplo):

```json
{
    "type": "finish",
    "data": {
        "path": "/ruta/al/archivo/traducido.pdf",
        "pages": 100,
        "translated_pages": 100,
        "cost": 0.0
    }
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

`{"type": "error", "data": {"error": "An error occurred"}}`

Progress event (example): `{"type": "progress", "data": {"progress": 0.5, "message": "Translating page 10 of 20"}}`

Result event (example): `{"type": "result", "data": {"result": "The translated text"}}`

---

### TRANSLATION RESULT

Evento de error (ejemplo): `{"type": "error", "data": {"error": "An error occurred"}}`

Evento de progreso (ejemplo): `{"type": "progress", "data": {"progress": 0.5, "message": "Translating page 10 of 20"}}`

Evento de resultado (ejemplo): `{"type": "result", "data": {"result": "The translated text"}}`
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

- **Translation Quality**: 
  - The translation quality depends on the translation service provider. 
  - If the translation quality is not satisfactory, you can try switching the service provider by modifying the `translation_service` parameter.

- **PDF Parsing Quality**:
  - The quality of the parsed PDF directly affects the final translation quality. 
  - You can adjust the `ocr_correct` parameter to optimize the PDF parsing results. 
  - If the parsing quality is poor, you can also try using other PDF to Markdown tools (such as [nougat](https://github.com/facebookresearch/nougat)) to convert the PDF to Markdown first, and then use this tool for translation.

- **Translation Speed**:
  - Translation speed is mainly limited by the translation service provider. 
  - If you need faster translation speed, consider using a local model (such as [Ollama](https://ollama.com/)). 
  - You can also adjust the `concurrency_limit` parameter to increase the number of concurrent translations, but please note that increasing concurrency may lead to a higher rate of request failures.

- **Error Handling**:
  - If an error occurs during translation, the program will attempt to retry. 
  - You can adjust the `retry_times` parameter to set the number of retries. 
  - If the error persists, please check the error message and the documentation of the corresponding translation service.

- **Other Tips**:
  - If the translation result contains garbled characters or formatting errors, you can try adjusting the `md_parse_config` parameter to optimize the Markdown parsing settings. 
  - For PDFs containing mathematical formulas, it is recommended to enable the `math` option to ensure accurate translation of the formulas.

---

### OUTPUT

### Notas y mejores prácticas

- **Calidad de la traducción**:
  - La calidad de la traducción depende del proveedor del servicio de traducción.
  - Si la calidad de la traducción no es satisfactoria, puedes intentar cambiar el proveedor del servicio modificando el parámetro `translation_service`.

- **Calidad del análisis del PDF**:
  - La calidad del PDF analizado afecta directamente la calidad final de la traducción.
  - Puedes ajustar el parámetro `ocr_correct` para optimizar los resultados del análisis del PDF.
  - Si la calidad del análisis es pobre, también puedes intentar usar otras herramientas de PDF a Markdown (como [nougat](https://github.com/facebookresearch/nougat)) para convertir primero el PDF a Markdown, y luego usar esta herramienta para la traducción.

- **Velocidad de la traducción**:
  - La velocidad de la traducción está limitada principalmente por el proveedor del servicio de traducción.
  - Si necesitas una velocidad de traducción más rápida, considera usar un modelo local (como [Ollama](https://ollama.com/)).
  - También puedes ajustar el parámetro `concurrency_limit` para aumentar el número de traducciones concurrentes, pero ten en cuenta que aumentar la concurrencia puede llevar a una mayor tasa de fallos en las solicitudes.

- **Manejo de errores**:
  - Si ocurre un error durante la traducción, el programa intentará reintentar.
  - Puedes ajustar el parámetro `retry_times` para establecer el número de reintentos.
  - Si el error persiste, por favor verifica el mensaje de error y la documentación del servicio de traducción correspondiente.

- **Otros consejos**:
  - Si el resultado de la traducción contiene caracteres ilegibles o errores de formato, puedes intentar ajustar el parámetro `md_parse_config` para optimizar la configuración del análisis de Markdown.
  - Para PDFs que contienen fórmulas matemáticas, se recomienda habilitar la opción `math` para garantizar una traducción precisa de las fórmulas.
---

### TRANSLATION RESULT

- Siempre maneja tanto los eventos de error como las excepciones del generador.
- Rompe el bucle en `finish` para evitar trabajo innecesario.
- Asegúrate de que el `archivo` exista y que `settings.validate_settings()` pase antes de llamar.
- Los documentos grandes pueden dividirse; usa `part_index/total_parts` y `overall_progress` para impulsar tu interfaz de usuario.
- Debounce `progress_update` si tu interfaz de usuario es sensible a actualizaciones repetidas e idénticas.
- `report_interval` (SettingsModel): controla solo la tasa de emisión de eventos `progress_update`. No afecta a `stage_summary`, `progress_start`, `progress_end` o `finish`. El valor predeterminado es 0.1s y el mínimo permitido es 0.05s. Según la lógica del monitor de progreso, cuando `stage_total <= 3`, las actualizaciones no son limitadas por `report_interval`.

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>