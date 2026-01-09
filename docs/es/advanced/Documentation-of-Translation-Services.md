[**Opciones avanzadas**](./introduction.md) > **Documentación de servicios de traducción** _(actual)_

---

### Ver servicios de traducción disponibles a través de la línea de comandos

Puedes confirmar los servicios de traducción disponibles y su uso imprimiendo el mensaje de ayuda en la línea de comandos.

```bash
pdf2zh_next -h
```

Al final del mensaje de ayuda, puedes ver información detallada sobre los diferentes servicios de traducción.


---

### Política de soporte de motores de traducción

pdf2zh utiliza múltiples servicios de traducción para proporcionar traducciones de alta calidad. Sin embargo, debido a las políticas de uso de cada servicio, es posible que algunos servicios no estén disponibles en ciertas regiones o que requieran configuración adicional.

#### Servicios de traducción soportados

Actualmente, pdf2zh soporta los siguientes servicios de traducción:

1. **DeepL** - Traducción de alta calidad, requiere clave API
2. **Google Translate** - Servicio gratuito, sin necesidad de clave API
3. **Microsoft Translator** - Traducción empresarial, requiere clave API
4. **OpenAI GPT** - Traducción basada en IA, requiere clave API
5. **Claude** - Traducción basada en IA, requiere clave API
6. **Gemini** - Traducción basada en IA, requiere clave API
7. **Ollama** - Traducción local, requiere configuración del modelo

#### Política de disponibilidad

1. **Servicios gratuitos**
   - Google Translate: Disponible globalmente, sin restricciones regionales
   - Ollama: Disponible localmente, requiere instalación del modelo

2. **Servicios de pago**
   - DeepL: Disponible en la mayoría de las regiones, requiere clave API
   - Microsoft Translator: Disponible globalmente, requiere clave API
   - OpenAI GPT: Disponible en la mayoría de las regiones, requiere clave API
   - Claude: Disponible en la mayoría de las regiones, requiere clave API
   - Gemini: Disponible en la mayoría de las regiones, requiere clave API

#### Recomendaciones de uso

1. **Para usuarios generales**
   - Recomendamos usar Google Translate como servicio predeterminado
   - No requiere configuración, disponible inmediatamente

2. **Para usuarios que requieren alta calidad**
   - Recomendamos usar DeepL o Microsoft Translator
   - Requiere registro y obtención de clave API

3. **Para usuarios que requieren privacidad**
   - Recomendamos usar Ollama para traducción local
   - Requiere instalación y configuración del modelo

#### Solución de problemas

Si encuentras problemas al usar algún servicio de traducción:

1. **Verifica la conectividad de red**
   - Asegúrate de que tu red pueda acceder al servicio correspondiente

2. **Verifica la validez de la clave API**
   - Para servicios que requieren clave API, asegúrate de que la clave sea válida

3. **Cambia el servicio de traducción**
   - Puedes cambiar a otro servicio de traducción en la configuración

4. **Consulta la documentación**
   - Consulta la [Documentación de servicios de traducción](./translation-services.md) para obtener información detallada

#### Notas importantes

1. **Límites de uso**
   - Cada servicio de traducción tiene sus propios límites de uso
   - Por favor, consulta los términos de servicio del proveedor correspondiente

2. **Costos**
   - Los servicios de pago pueden incurrir en costos
   - Por favor, consulta la política de precios del proveedor correspondiente

3. **Disponibilidad regional**
   - Algunos servicios pueden no estar disponibles en ciertas regiones
   - Por favor, consulta la cobertura regional del proveedor correspondiente

#### Actualizaciones de política

Esta política puede actualizarse periódicamente. Por favor, consulta esta página regularmente para obtener la información más reciente.

Para obtener información más detallada sobre cada servicio de traducción, consulta la [Documentación de servicios de traducción](./translation-services.md).

#### Nivel 1 (Soporte oficial)

**Los motores de traducción de Nivel 1** son mantenidos directamente por los mantenedores del proyecto. Aunque los mantenedores **no utilizan este proyecto regularmente**, confiarán en los problemas de GitHub para identificar problemas. Cuando cualquiera de estos motores encuentre problemas, los mantenedores los solucionarán lo antes posible para garantizar la estabilidad y la fiabilidad.

Actualmente, los motores de traducción de Nivel 1 soportados incluyen:
1. SiliconFlowFree
2. OpenAI
3. AliyunDashScope
4. DeepSeek
5. SiliconFlow
6. Zhipu
7. OpenAICompatible

#### Tier 2 (Soporte de la comunidad)

**Los motores de traducción de Nivel 2** son mantenidos y soportados por la comunidad.  
Cuando estos motores encuentran problemas, los mantenedores del proyecto no proporcionarán correcciones directas. En su lugar, etiquetarán los problemas relacionados con `help wanted` y darán la bienvenida a las solicitudes de extracción de los contribuyentes para ayudar a resolverlos.

Todos los motores que son soportados por el programa pero no están explícitamente listados bajo el Nivel 1 se consideran motores de traducción de Nivel 2.

#### Motores obsoletos

Los siguientes motores de traducción han sido **obsoletos** y ya no serán mantenidos ni soportados:

1. Bing
2. Google

<div align="right"> 
<h6><small>Parte del contenido de esta página ha sido traducido por GPT y puede contener errores.</small></h6>