[**Расширенные параметры**](./introduction.md) > **Расширенные параметры** _(текущая)_

---

<h3 id="оглавление">Оглавление</h3>

- [#### Аргументы командной строки](#аргументы-командной-строки)
- [#### Руководство по настройке ограничения частоты запросов](#руководство-по-настройке-ограничения-частоты-запросов)
- [#### Частичный перевод](#частичный-перевод)
- [#### Указание исходного и целевого языков](#указание-исходного-и-целевого-языков)
- [#### Перевод с исключениями](#перевод-с-исключениями)
- [#### Пользовательский промпт](#пользовательский-промпт)
- [#### Пользовательская конфигурация](#пользовательская-конфигурация)
- [#### Пропустить очистку](#пропустить-очистку)
- [#### Кэш перевода](#кэш-перевода)
- [#### Развертывание в качестве общедоступных служб](#развертывание-в-качестве-общедоступных-служб)
- [#### Аутентификация и приветственная страница](#аутентификация-и-приветственная-страница)
- [#### Поддержка глоссария](#поддержка-глоссария)

---

#### Аргументы командной строки

Выполните команду перевода в командной строке, чтобы сгенерировать переведенный документ `example-mono.pdf` и двуязычный документ `example-dual.pdf` в текущем рабочем каталоге. Используйте Google в качестве службы перевода по умолчанию. Дополнительные поддерживаемые службы перевода можно найти [ЗДЕСЬ](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services).

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

В следующей таблице мы перечисляем все расширенные параметры для справки:

##### Аргументы

| Опция                          | Функция                                                                               | Пример                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | Входные PDF-файлы для обработки                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `--output`                      | Выходной каталог для файлов                                                              | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| `--<Services>`                  | Использовать [**определенную службу**](./Documentation-of-Translation-Services.md) для перевода | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| `--help`, `-h`                  | Показать справочное сообщение и выйти                                                              | `pdf2zh_next -h`                                                                                                      |
| `--config-file`                 | Путь к файлу конфигурации                                                               | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               |
| `--report-interval`             | Интервал отчёта о прогрессе в секундах                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--debug`                       | Использовать уровень логирования отладки                                                                 | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--gui`                         | Взаимодействие с GUI                                                                       | `pdf2zh_next --gui`                                                                                                   |
| `--warmup`                      | Только загрузить и проверить необходимые ресурсы, затем выйти                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| `--generate-offline-assets`     | Создать пакет офлайн-ресурсов в указанной директории                              | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
| `--restore-offline-assets`      | Восстановить пакет автономных ресурсов из указанного каталога                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |
| `--version`                     | Показать версию и выйти                                                                  | `pdf2zh_next --version`                                                                                               |
| `--pages`                       | Частичный перевод документа                                                            | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       |
| `--lang-in`                     | Исходный код языка                                                                    | `pdf2zh_next example.pdf --lang-in en`                                                                                |
| `--lang-out`                    | Целевой код языка                                                                    | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| `--min-text-length`             | Минимальная длина текста для перевода                                                   | `pdf2zh_next example.pdf --min-text-length 5`                                                                         |
| `--rpc-doclayout`               | Адрес хоста службы RPC для анализа структуры документа                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| `--qps`                         | Ограничение QPS для службы перевода                                                       | `pdf2zh_next example.pdf --qps 200`                                                                                   |
| `--ignore-cache`                | Игнорировать кэш перевода                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--custom-system-prompt`        | Пользовательский системный промпт для перевода. Используется для `/no_think` в Qwen 3                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` |
| `--glossaries`                  | Список файлов глоссария.                                                                     | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| `--save-auto-extracted-glossary`| сохранить автоматически извлеченный глоссарий                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| `--pool-max-workers`            | Максимальное количество воркеров для пула перевода. Если не задано, будет использоваться qps в качестве количества воркеров | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| `--term-qps`                    | Ограничение QPS для службы перевода извлечения терминов. Если не установлено, будет следовать qps.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| `--term-pool-max-workers`       | Максимальное количество воркеров для пула перевода извлечения терминов. Если не задано или 0, будет следовать pool_max_workers. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| `--no-auto-extract-glossary`    | Отключить автоматическое извлечение глоссария                                                           | `pdf2zh_next example.pdf --no-auto-extract-glossary`                                                                  |
| `--primary-font-family`         | Переопределяет основное семейство шрифтов для переведенного текста. Варианты: 'serif' для шрифтов с засечками, 'sans-serif' для рубленых шрифтов, 'script' для рукописных/курсивных шрифтов. Если не указано, используется автоматический выбор шрифта на основе свойств исходного текста. | `pdf2zh_next example.pdf --primary-font-family serif` |
| `--no-dual`                     | Не выводить двуязычные PDF-файлы                                                       | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| `--no-mono`                     | Не выводить одноязычные PDF-файлы                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| `--formular-font-pattern`       | Шаблон шрифта для идентификации текста формул                                                   | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| `--formular-char-pattern`       | Символьный шаблон для идентификации текста формул                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| `--split-short-lines`           | Принудительное разделение коротких строк на разные абзацы                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| `--short-line-split-factor`     | Коэффициент порога разделения для коротких строк                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               |
| `--skip-clean`                  | Пропустить шаг очистки PDF                                                              | `pdf2zh_next example.pdf --skip-clean`                                                                                |
| `--dual-translate-first`        | Помещать переведенные страницы первыми в режиме двойного PDF                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| `--disable-rich-text-translate` | Отключить перевод форматированного текста                                                           | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
| `--enhance-compatibility`       | Включить все опции повышения совместимости                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| `--use-alternating-pages-dual`  | Использовать режим чередующихся страниц для двойного PDF                               | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| `--watermark-output-mode`       | Режим вывода водяных знаков для PDF-файлов                                              | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        |
| `--max-pages-per-part`          | Максимальное количество страниц на часть для раздельного перевода                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| `--translate-table-text`        | Перевести текст таблицы (экспериментальная функция)                                     | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| `--skip-scanned-detection`      | Пропустить обнаружение сканированных документов                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    |
| `--ocr-workaround`              | Принудительно сделать переведенный текст черным и добавить белый фон                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| `--auto-enable-ocr-workaround`  | Включить автоматическое обходное решение OCR. Если документ определяется как сильно отсканированный, будет предпринята попытка включить обработку OCR и пропустить дальнейшее обнаружение сканирования. Подробности см. в документации. (по умолчанию: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| `--only-include-translated-page`| Включать в выходной PDF только переведенные страницы. Действует только при использовании --pages.  | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| `--no-merge-alternating-line-numbers` | Отключить объединение чередующихся номеров строк и текстовых абзацев в документах с номерами строк | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| `--no-remove-non-formula-lines` | Отключить удаление строк без формул в областях абзацев                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| `--non-formula-line-iou-threshold` | Установить порог IoU для идентификации строк без формул (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       |
| `--figure-table-protection-threshold` | Установить порог защиты для рисунков и таблиц (0.0-1.0). Строки внутри рисунков/таблиц обрабатываться не будут | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        |
| `--skip-formula-offset-calculation` | Пропустить расчет смещения формул во время обработки          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### Аргументы GUI

| Опция                           | Функция                                | Пример                                          |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | Включить режим общего доступа          | `pdf2zh_next --gui --share`                     |
| `--auth-file`                   | Путь к файлу аутентификации        | `pdf2zh_next --gui --auth-file /path`           |
| `--welcome-page`                | Путь к HTML-файлу приветственной страницы | `pdf2zh_next --gui --welcome-page /path`        |
| `--enabled-services`            | Включенные службы перевода           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` |
| `--disable-gui-sensitive-input` | Отключить чувствительный ввод в GUI            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
| `--disable-config-auto-save`    | Отключить автоматическое сохранение конфигурации | `pdf2zh_next --gui --disable-config-auto-save`  |
| `--server-port`                 | Порт WebUI                             | `pdf2zh_next --gui --server-port 7860`          |
| `--ui-lang`                     | Язык интерфейса                            | `pdf2zh_next --gui --ui-lang zh`                |

[⬆️ Наверх](#toc)

---

#### Руководство по настройке ограничения частоты запросов

При использовании служб перевода правильная настройка ограничения частоты запросов крайне важна для избежания ошибок API и оптимизации производительности. Это руководство объясняет, как настраивать параметры `--qps` и `--pool-max-worker` в зависимости от ограничений различных вышестоящих служб.

> [!TIP]
>
> Рекомендуется, чтобы размер пула (pool_size) не превышал 1000. Если размер пула, рассчитанный следующим методом, превышает 1000, используйте значение 1000.

##### Ограничение скорости RPM (запросов в минуту)

Когда вышестоящая служба имеет ограничения RPM, используйте следующий расчет:

**Формула расчета:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> Коэффициент 10 является эмпирическим коэффициентом, который обычно хорошо работает в большинстве сценариев.

**Пример:**
Если ваша служба перевода имеет ограничение в 600 RPM:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### Ограничение одновременных подключений

Когда вышестоящая служба имеет ограничения на одновременные подключения (например, официальная служба GLM), используйте этот подход:

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
> - Следите за временем отклика вашей службы и частотой ошибок
> - Различные службы могут требовать различных стратегий оптимизации
> - Учитывайте ваш конкретный случай использования и размер документа при установке этих параметров


[⬆️ Наверх](#toc)

---

#### Частичный перевод

Используйте параметр `--pages` для перевода части документа.

- Если номера страниц идут подряд, вы можете записать это так:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` включает все страницы после страницы 25. Если ваш документ содержит 100 страниц, это эквивалентно `25-100`.
> 
> Аналогично, `-25` включает все страницы до страницы 25, что эквивалентно `1-25`.

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

Сохранение шрифтов `Latex`, `Mono`, `Code`, `Italic`, `Symbol` и `Math` по умолчанию:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ Наверх](#toc)

---

#### Пользовательский промпт

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/pull/637). -->

Пользовательский системный промпт для перевода. В основном используется для добавления инструкции '/no_think' Qwen 3 в промпт.

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
> При изменении одного и того же параметра с использованием различных методов, программное обеспечение будет применять изменения в соответствии с приведенным ниже порядком приоритета.
>
> Изменения с более высоким приоритетом переопределяют изменения с более низким приоритетом.
>
> **cli/gui > env > пользовательский файл конфигурации > файл конфигурации по умолчанию**

- Изменение конфигурации с помощью **аргументов командной строки**

В большинстве случаев вы можете напрямую передать нужные настройки через аргументы командной строки. Для получения дополнительной информации обратитесь к [Аргументы командной строки](#cmd).

Например, если вы хотите включить окно GUI, вы можете использовать следующую команду:

```bash
pdf2zh_next --gui
```

- Изменение конфигурации через **переменные окружения**

Вы можете заменить `--` в аргументах командной строки на `PDF2ZH_`, соединить параметры с помощью `=`, и заменить `-` на `_` в качестве переменных окружения.

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

Если вы не уверены в формате файла конфигурации, обратитесь к файлу конфигурации по умолчанию, описанному ниже.

- **Файл конфигурации по умолчанию**

Файл конфигурации по умолчанию находится в `~/.config/pdf2zh`.
Пожалуйста, не изменяйте файлы конфигурации в каталоге `default`.
Настоятельно рекомендуется ознакомиться с содержимым этого файла конфигурации и использовать **Пользовательский файл конфигурации** для реализации собственного файла конфигурации.

> [!TIP]
> - По умолчанию pdf2zh 2.0 автоматически сохраняет текущую конфигурацию в `~/.config/pdf2zh/config.v3.toml` каждый раз, когда вы нажимаете кнопку перевода в GUI. Этот файл конфигурации будет загружен по умолчанию при следующем запуске.
> - Файлы конфигурации в каталоге `default` автоматически генерируются программой. Вы можете скопировать их для изменения, но, пожалуйста, не изменяйте их напрямую.
> - Файлы конфигурации могут включать номера версий, такие как "v2", "v3" и т.д. Это **номера версий файла конфигурации**, **а не** номер версии самого pdf2zh.


[⬆️ Наверх](#toc)

---

#### Пропустить очистку

Когда этот параметр установлен в значение True, шаг очистки PDF будет пропущен, что может повысить совместимость и избежать некоторых проблем с обработкой шрифтов.

Использование:

```bash
pdf2zh_next example.pdf --skip-clean
```

Или используя переменные окружения:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> Когда включен параметр `--enhance-compatibility`, функция "Пропустить очистку" автоматически активируется.

---

#### Кэш перевода

PDFMathTranslate кэширует переведенные тексты для увеличения скорости и избежания ненужных вызовов API для одинакового содержимого. Вы можете использовать опцию `--ignore-cache`, чтобы игнорировать кэш перевода и принудительно выполнить повторный перевод.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ Наверх](#toc)

---

#### Развертывание в качестве общедоступных служб

При развертывании графического интерфейса pdf2zh в общедоступных службах вам следует изменить файл конфигурации, как описано ниже.

> [!WARNING]
>
> Этот проект не проходил профессиональную проверку безопасности и может содержать уязвимости. Пожалуйста, оцените риски и примите необходимые меры безопасности перед развертыванием в общедоступных сетях.


> [!TIP]
> - При публичном развертывании следует включить как `disable_gui_sensitive_input`, так и `disable_config_auto_save`.
> - Разделяйте различные доступные службы с помощью *английских запятых* <kbd>,</kbd> .

Рабочая конфигурация выглядит следующим образом:

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

При использовании аутентификации и приветственной страницы для указания, какой пользователь должен использовать Web UI и настройки страницы входа:

пример auth.txt
Каждая строка содержит два элемента: имя пользователя и пароль, разделенные запятой.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

example welcome.html

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
> Если файл аутентификации пуст, аутентификации не будет. :)

Рабочая конфигурация выглядит следующим образом:

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

PDFMathTranslate поддерживает таблицу глоссария. Файл таблицы глоссария должен быть файлом `csv`.
В файле три столбца. Вот демонстрационный файл глоссария:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | AutoML  | ru      |
| a,a    | a       | ru      |
| "      | "       | ru      |


Для пользователей CLI:
Вы можете использовать несколько файлов для глоссария. Разные файлы следует разделять запятыми `,`.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

Для пользователей WebUI:

Теперь вы можете загрузить собственный файл глоссария. После загрузки файла вы можете проверить его, нажав на его название, и содержимое отобразится ниже.

[⬆️ Наверх](#toc)

<div align="right"> 
<h6><small>Часть содержимого этой страницы была переведена GPT и может содержать ошибки.</small></h6>