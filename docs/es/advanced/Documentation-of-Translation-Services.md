[**Opciones avanzadas**](./introduction.md) > **Documentación de servicios de traducción** _(actual)_

---

### Visualización de servicios de traducción disponibles mediante la Línea de comandos

Puedes confirmar los servicios de traducción disponibles y su uso imprimiendo el mensaje de ayuda en la línea de comandos.

```bash
pdf2zh_next -h
```

```bash
pdf2zh --help
```

### Translation Engine Support Policy
`pdf2zh` supports multiple translation engines, including **Google Translate**, **DeepL**, and more. The engine support list is as follows:

| Engine | Free | Key Required |
|:-------|:----:|:------------:|
| Google Translate | ✅ |  ❌ |
| DeepL | ❌ | ✅ |
| Baidu Translate | ❌ | ✅ |
| Youdao Translate | ❌ | ✅ |
| Tencent Translate | ❌ | ✅ |
| ChatGPT | ❌ | ✅ |

- **Free**: Whether the engine is free to use.
- **Key Required**: Whether an API key is required to use the engine.

### How to Set Up Translation Engine
You can set the translation engine by using the `-e` or `--engine` option, for example:
```bash
pdf2zh -e google input.pdf
```

**Note**: For engines that require an API key, you need to set the API key in the environment variables. For example, for DeepL, you need to set the `DEEPL_AUTH_KEY` environment variable.

### Translation Engine Configuration
The following table lists the environment variables required for each translation engine:

| Engine | Environment Variable | Description |
|:-------|:--------------------:|:------------|
| Google Translate | - | No API key required |
| DeepL | `DEEPL_AUTH_KEY` | DeepL API key |
| Baidu Translate | `BAIDU_APP_ID`<br>`BAIDU_APP_KEY` | Baidu Translate App ID and Key |
| Youdao Translate | `YOUDAO_APP_KEY`<br>`YOUDAO_APP_SECRET` | Youdao Translate App Key and Secret |
| Tencent Translate | `TENCENT_SECRET_ID`<br>`TENCENT_SECRET_KEY` | Tencent Cloud Secret ID and Key |
| ChatGPT | `OPENAI_API_KEY` | OpenAI API Key |

For more details, please refer to the [Documentation of Translation Services](https://pdf2zh-next.com/advanced/TRANSLATION_SERVICE.html).

---

### OUTPUT

Al final del mensaje de ayuda, puedes ver información detallada sobre los diferentes servicios de traducción.

```bash
pdf2zh --help
```

### Política de soporte de motores de traducción
`pdf2zh` soporta múltiples motores de traducción, incluyendo **Google Translate**, **DeepL**, y más. La lista de soporte de motores es la siguiente:

| Motor | Gratuito | Clave requerida |
|:-------|:----:|:------------:|
| Google Translate | ✅ | ❌ |
| DeepL |  ❌ | ✅ |
| Baidu Translate |  ❌ | ✅ |
| Youdao Translate |  ❌ | ✅ |
| Tencent Translate |  ❌ | ✅ |
| ChatGPT |  ❌ | ✅ |

- **Gratuito**: Si el motor es gratuito de usar.
- **Clave requerida**: Si se requiere una clave de API para usar el motor.

### Cómo configurar el motor de traducción
Puedes configurar el motor de traducción usando la opción `-e` o `--engine`, por ejemplo:
```bash
pdf2zh -e google input.pdf
```

**Nota**: Para los motores que requieren una clave de API, necesitas configurar la clave de API en las variables de entorno. Por ejemplo, para DeepL, necesitas configurar la variable de entorno `DEEPL_AUTH_KEY`.

### Configuración del motor de traducción
La siguiente tabla lista las variables de entorno requeridas para cada motor de traducción:

| Motor | Variable de entorno | Descripción |
|:-------|:--------------------:|:------------|
| Google Translate | - | No se requiere clave de API |
| DeepL | `DEEPL_AUTH_KEY` | Clave de API de DeepL |
| Baidu Translate | `BAIDU_APP_ID`<br>`BAIDU_APP_KEY` | ID de aplicación y clave de Baidu Translate |
| Youdao Translate | `YOUDAO_APP_KEY`<br>`YOUDAO_APP_SECRET` | Clave de aplicación y secreto de Youdao Translate |
| Tencent Translate | `TENCENT_SECRET_ID`<br>`TENCENT_SECRET_KEY` | ID secreto y clave secreta de Tencent Cloud |
| ChatGPT | `OPENAI_API_KEY` | Clave de API de OpenAI |

Para más detalles, por favor consulta la [Documentación de servicios de traducción](https://pdf2zh-next.com/advanced/TRANSLATION_SERVICE.html).


---

`pdf2zh` supports multiple translation engines, including **Google Translate**, **DeepL**, and more. The engine support list is as follows:

| Engine | Free | Key Required |
|:-------|:----:|:------------:|
| Google Translate | ✅ | ❌ |
| DeepL | ❌ | ✅ |
| Baidu Translate | ❌ | ✅ |
| Youdao Translate | ❌ | ✅ |
| Tencent Translate | ❌ | ✅ |
| ChatGPT | ❌ | ✅ |

- **Free**: Whether the engine is free to use.
- **Key Required**: Whether an API key is required to use the engine.

### How to Set Up Translation Engine
You can set the translation engine by using the `-e` or `--engine` option, for example:
```bash
pdf2zh -e google input.pdf
```

**Note**: For engines that require an API key, you need to set the API key in the environment variables. For example, for DeepL, you need to set the `DEEPL_AUTH_KEY` environment variable.

### Translation Engine Configuration
The following table lists the environment variables required for each translation engine:

| Engine | Environment Variable | Description |
|:-------|:--------------------:|:------------|
| Google Translate | - | No API key required |
| DeepL | `DEEPL_AUTH_KEY` | DeepL API key |
| Baidu Translate | `BAIDU_APP_ID`<br>`BAIDU_APP_KEY` | Baidu Translate App ID and Key |
| Youdao Translate | `YOUDAO_APP_KEY`<br>`YOUDAO_APP_SECRET` | Youdao Translate App Key and Secret |
| Tencent Translate | `TENCENT_SECRET_ID`<br>`TENCENT_SECRET_KEY` | Tencent Cloud Secret ID and Key |
| ChatGPT | `OPENAI_API_KEY` | OpenAI API Key |

For more details, please refer to the [Documentation of Translation Services](https://pdf2zh-next.com/advanced/TRANSLATION_SERVICE.html).

---

### OUTPUT LANGUAGE

es

- **English (en)**: English is the default language of the project, and the documentation is primarily written in English. All updates and new features are first documented in English.
- **Chinese (zh)**: Chinese documentation is maintained by the core team and is kept up-to-date with the English version.

#### Tier 2 (Community Support)
- **Spanish (es)**: Community-translated documentation. May lag behind the English version but is actively maintained.
- **Japanese (ja)**: Community-translated documentation. May lag behind the English version but is actively maintained.
- **Korean (ko)**: Community-translated documentation. May lag behind the English version but is actively maintained.
- **French (fr)**: Community-translated documentation. May lag behind the English version but is actively maintained.
- **German (de)**: Community-translated documentation. May lag behind the English version but is actively maintained.

---

### OUTPUT LANGUAGE

es

- **Google Translate** (engine name: `google`): A free translation service from Google.
- **DeepL** (engine name: `deepl`): A high-quality translation service that supports many languages. It is free for small amounts of text, but requires a paid API key for large-scale use.

**Tier 2 translation engines** are maintained by the community. They may be less stable than Tier 1 engines, but the maintainers will still try their best to fix issues when they are reported.

Currently supported Tier 2 translation engines include:

- **Azure Translator** (engine name: `azure`): A translation service provided by Microsoft. It supports many languages and offers a free tier for small amounts of text, but requires a paid API key for large-scale use.

**Tier 3 translation engines** are experimental and may be unstable. They are provided for testing purposes only and may be removed in the future if they are not widely used.

Currently supported Tier 3 translation engines include:

- **OpenAI** (engine name: `openai`): OpenAI provides translation services through its GPT models. It requires a paid API key for use.
- **Gemini** (engine name: `gemini`): Gemini is a translation service provided by Google. It requires a paid API key for use.
- **Claude** (engine name: `claude`): Claude is a translation service provided by Anthropic. It requires a paid API key for use.

---

### OUTPUT

**Los motores de traducción de Nivel 1** son mantenidos directamente por los mantenedores del proyecto. Aunque los mantenedores **no utilizan este proyecto regularmente**, se basarán en los issues de GitHub para identificar problemas. Cuando alguno de estos motores encuentre problemas, los mantenedores los solucionarán lo antes posible para garantizar la estabilidad y la fiabilidad.

Actualmente, los motores de traducción de Nivel 1 soportados incluyen:

- **Google Translate** (nombre del motor: `google`): Un servicio de traducción gratuito de Google.
- **DeepL** (nombre del motor: `deepl`): Un servicio de traducción de alta calidad que soporta muchos idiomas. Es gratuito para pequeñas cantidades de texto, pero requiere una clave API de pago para uso a gran escala.

**Los motores de traducción de Nivel 2** son mantenidos por la comunidad. Pueden ser menos estables que los motores de Nivel 1, pero los mantenedores seguirán intentando solucionar los problemas cuando se informen.

Actualmente, los motores de traducción de Nivel 2 soportados incluyen:

- **Azure Translator** (nombre del motor: `azure`): Un servicio de traducción proporcionado por Microsoft. Soporta muchos idiomas y ofrece un nivel gratuito para pequeñas cantidades de texto, pero requiere una clave API de pago para uso a gran escala.

**Los motores de traducción de Nivel 3** son experimentales y pueden ser inestables. Se proporcionan únicamente con fines de prueba y podrían eliminarse en el futuro si no se utilizan ampliamente.

Actualmente, los motores de traducción de Nivel 3 soportados incluyen:

- **OpenAI** (nombre del motor: `openai`): OpenAI proporciona servicios de traducción a través de sus modelos GPT. Requiere una clave API de pago para su uso.
- **Gemini** (nombre del motor: `gemini`): Gemini es un servicio de traducción proporcionado por Google. Requiere una clave API de pago para su uso.
- **Claude** (nombre del motor: `claude`): Claude es un servicio de traducción proporcionado por Anthropic. Requiere una clave API de pago para su uso.
8. AzureOpenAI

---

### OUTPUT

1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible
8. AzureOpenAI

- **DeepL**: DeepL is a high-quality translation service that supports many languages. It is free for small amounts of text, but requires a paid API key for large-scale use.
- **Google Translate**: Google Translate is a widely used translation service that supports many languages. It is free for small amounts of text, but requires a paid API key for large-scale use.
- **Azure Translator**: Azure Translator is a translation service provided by Microsoft. It supports many languages and offers a free tier for small amounts of text, but requires a paid API key for large-scale use.

#### Tier 3 (Community Support)
- **OpenAI**: OpenAI provides translation services through its GPT models. It requires a paid API key for use.
- **Gemini**: Gemini is a translation service provided by Google. It requires a paid API key for use.
- **Claude**: Claude is a translation service provided by Anthropic. It requires a paid API key for use.

---

### OUTPUT LANGUAGE

es

**Los motores de traducción de Nivel 2** son mantenidos y soportados por la comunidad.  
Cuando estos motores encuentran problemas, los mantenedores del proyecto no proporcionarán correcciones directas. En su lugar, etiquetarán los problemas relacionados con `help wanted` y darán la bienvenida a las solicitudes de extracción de los colaboradores para ayudar a resolverlos.

Todos los motores que son compatibles con el programa pero no están explícitamente listados bajo el Nivel 1 se consideran motores de traducción de Nivel 2.

We've deprecated the following engines due to their poor performance in Chinese-English translation. If you have a specific need for these engines, please open an issue to let us know.

- `google`: Google Translate, a popular free translation service.
- `google_cloud`: Google Cloud Translation API, a paid service from Google.
- `google_cloud_advanced`: Google Cloud Translation API (Advanced), a paid service from Google.
- `microsoft`: Microsoft Translator, a free translation service from Microsoft.
- `microsoft_advanced`: Microsoft Translator (Advanced), a paid service from Microsoft.
- `youdao`: Youdao Translate, a free translation service from Netease.
- `baidu`: Baidu Translate, a free translation service from Baidu.
- `niutrans`: NiuTrans, a free translation service from NiuTrans.
- `caiyun`: Caiyun Translate, a free translation service from Caiyun.
- `deepl`: DeepL Translate, a free translation service from DeepL.
- `deepl_pro`: DeepL Pro, a paid service from DeepL.

---

### OUTPUT

#### Motores en desuso
Hemos dejado de utilizar los siguientes motores debido a su bajo rendimiento en la traducción chino-inglés. Si tiene una necesidad específica de estos motores, por favor abra un issue para informarnos.

- `google`: Google Translate, un servicio de traducción gratuito popular.
- `google_cloud`: Google Cloud Translation API, un servicio de pago de Google.
- `google_cloud_advanced`: Google Cloud Translation API (Advanced), un servicio de pago de Google.
- `microsoft`: Microsoft Translator, un servicio de traducción gratuito de Microsoft.
- `microsoft_advanced`: Microsoft Translator (Advanced), un servicio de pago de Microsoft.
- `youdao`: Youdao Translate, un servicio de traducción gratuito de Netease.
- `baidu`: Baidu Translate, un servicio de traducción gratuito de Baidu.
- `niutrans`: NiuTrans, un servicio de traducción gratuito de NiuTrans.
- `caiyun`: Caiyun Translate, un servicio de traducción gratuito de Caiyun.
- `deepl`: DeepL Translate, un servicio de traducción gratuito de DeepL.
- `deepl_pro`: DeepL Pro, un servicio de pago de DeepL.

- `google`
- `google_cloud`
- `google_cloud_advanced`
- `microsoft`
- `microsoft_advanced`
- `youdao`
- `baidu`
- `niutrans`
- `caiyun`
- `deepl`
- `deepl_pro`

---

### OUTPUT

Los siguientes motores de traducción han sido **desaprobados** y ya no se mantendrán ni admitirán:
- `google`
- `google_cloud`
- `google_cloud_advanced`
- `microsoft`
- `microsoft_advanced`
- `youdao`
- `baidu`
- `niutrans`
- `caiyun`
- `deepl`
- `deepl_pro`

3. DeepSeek
4. Claude
5. GPT
6. GLM
7. Qwen
8. MoonShot
9. 01
10. ZeroOne

---

### OUTPUT

1. Bing
2. Google
3. DeepSeek
4. Claude
5. GPT
6. GLM
7. Qwen
8. MoonShot
9. 01
10. ZeroOne

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>