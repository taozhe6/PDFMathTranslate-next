[**고급 옵션**](./introduction.md) > **고급 옵션** _(현재)_

---

<h3 id="목차">목차</h3>

- [명령줄 인수](#명령줄 - 인수)
- [속도 제한 구성 가이드](#속도 - 제한 - 구성 - 가이드)
- [부분 번역](#부분 - 번역)
- [소스 및 대상 언어 지정](#소스 - 및 - 대상 - 언어 - 지정)
- [예외와 함께 번역](#예외와 - 함께 - 번역)
- [사용자 정의 프롬프트](#사용자 - 정의 - 프롬프트)
- [사용자 정의 구성](#사용자 - 정의 - 구성)
- [정리 건너뛰기](#정리 - 건너뛰기)
- [번역 캐시](#번역 - 캐시)
- [공용 서비스로 배포](#공용 - 서비스로 - 배포)
- [인증 및 환영 페이지](#인증 - 및 - 환영 - 페이지)
- [용어집 지원](#용어집 - 지원)

---

#### 명령줄 인수

명령줄에서 번역 명령을 실행하여 현재 작업 디렉터리에 번역된 문서 `example-mono.pdf` 와 이중 언어 문서 `example-dual.pdf` 를 생성합니다. 기본 번역 서비스로 Google 을 사용합니다. 더 많은 지원되는 번역 서비스는 [여기](https://github.com/PDFMathTranslate/PDFMathTranslate-next/blob/main/docs/ADVANCED.md#services) 에서 확인할 수 있습니다.

<img src="./../../images/cmd_light.svg" width="580px"  alt="cmd"/>

다음 표에서는 참조용으로 모든 고급 옵션을 나열합니다:

##### 인수

| `output-dir`                    | Output directory for translated files                                                   | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `target-language`               | Target language code, defaults to `zh`                                                  | `pdf2zh_next example.pdf -t ja`                                                                                       |
| `engine`                        | Translation engine, defaults to `google`                                                | `pdf2zh_next example.pdf -e deepl`                                                                                    |
| `formula-detection`             | Formula detection mode, defaults to `hybrid`                                            | `pdf2zh_next example.pdf --formula-detection mml`                                                                     |
| `formula-translation`           | Whether to translate formulas, defaults to `false`                                      | `pdf2zh_next example.pdf --formula-translation true`                                                                  |
| `target-font`                   | Font family for translated text, defaults to `SimSun, NSimSun, STSong`                  | `pdf2zh_next example.pdf --target-font "Noto Serif SC"`                                                               |
| `target-font-size`              | Font size for translated text, defaults to `auto`                                       | `pdf2zh_next example.pdf --target-font-size 14`                                                                       |
| `line-spacing`                  | Line spacing for translated text, defaults to `auto`                                    | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `char-spacing`                  | Character spacing for translated text, defaults to `auto`                               | `pdf2zh_next example.pdf --char-spacing 0.1`                                                                          |
| `page-margin`                   | Page margin for translated text, defaults to `auto`                                     | `pdf2zh_next example.pdf --page-margin 20`                                                                            |
| `retry-count`                   | Number of retries for translation failures, defaults to `3`                             | `pdf2zh_next example.pdf --retry-count 5`                                                                             |
| `retry-interval`                | Retry interval in seconds, defaults to `1`                                              | `pdf2zh_next example.pdf --retry-interval 2`                                                                          |
| `concurrent`                    | Number of concurrent translations, defaults to `3`                                      | `pdf2zh_next example.pdf --concurrent 5`                                                                              |
| `timeout`                       | Translation timeout in seconds, defaults to `30`                                        | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `ignore-translated-pages`       | Whether to ignore pages that have already been translated, defaults to `false`          | `pdf2zh_next example.pdf --ignore-translated-pages true`                                                              |
| `ignore-translated-paragraphs`  | Whether to ignore paragraphs that have already been translated, defaults to `false`     | `pdf2zh_next example.pdf --ignore-translated-paragraphs true`                                                         |
| `cache-dir`                     | Directory for caching translation results, defaults to `./.pdf2zh_cache`                | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `config-file`                   | Path to the configuration file                                                          | `pdf2zh_next example.pdf --config-file ./config.json`                                                                 |
| `api-key`                       | API key for translation service                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      |
| `api-base-url`                  | Base URL for translation service                                                        | `pdf2zh_next example.pdf --api-base-url https://api.example.com`                                                      |
| `log-level`                     | Log level, defaults to `info`                                                           | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `help`                          | Show help information                                                                   | `pdf2zh_next --help`                                                                                                  |
| `version`                       | Show version information                                                                | `pdf2zh_next --version`                                                                                               |

---

### OUTPUT

| 옵션                          | 기능                                                                               | 예시                                                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `input-files`                   | 처리할 입력 PDF 파일                                                              | `pdf2zh_next example.pdf`                                                                                             |
| `output-dir`                    | 번역된 파일의 출력 디렉터리                                                   | `pdf2zh_next example.pdf -o ./output`                                                                                 |
| `target-language`               | 대상 언어 코드, 기본값은 `zh`                                                  | `pdf2zh_next example.pdf -t ja`                                                                                       |
| `engine`                        | 번역 엔진, 기본값은 `google`                                                | `pdf2zh_next example.pdf -e deepl`                                                                                    |
| `formula-detection`             | 수식 감지 모드, 기본값은 `hybrid`                                            | `pdf2zh_next example.pdf --formula-detection mml`                                                                     |
| `formula-translation`           | 수식을 번역할지 여부, 기본값은 `false`                                      | `pdf2zh_next example.pdf --formula-translation true`                                                                  |
| `target-font`                   | 번역된 텍스트의 글꼴 패밀리, 기본값은 `SimSun, NSimSun, STSong`                  | `pdf2zh_next example.pdf --target-font "Noto Serif SC"`                                                               |
| `target-font-size`              | 번역된 텍스트의 글꼴 크기, 기본값은 `auto`                                       | `pdf2zh_next example.pdf --target-font-size 14`                                                                       |
| `line-spacing`                  | 번역된 텍스트의 줄 간격, 기본값은 `auto`                                    | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `char-spacing`                  | 번역된 텍스트의 문자 간격, 기본값은 `auto`                               | `pdf2zh_next example.pdf --char-spacing 0.1`                                                                          |
| `page-margin`                   | 번역된 텍스트의 페이지 여백, 기본값은 `auto`                                     | `pdf2zh_next example.pdf --page-margin 20`                                                                            |
| `retry-count`                   | 번역 실패 시 재시도 횟수, 기본값은 `3`                             | `pdf2zh_next example.pdf --retry-count 5`                                                                             |
| `retry-interval`                | 재시도 간격 (초), 기본값은 `1`                                              | `pdf2zh_next example.pdf --retry-interval 2`                                                                          |
| `concurrent`                    | 동시 번역 수, 기본값은 `3`                                      | `pdf2zh_next example.pdf --concurrent 5`                                                                              |
| `timeout`                       | 번역 타임아웃 (초), 기본값은 `30`                                        | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `ignore-translated-pages`       | 이미 번역된 페이지를 무시할지 여부, 기본값은 `false`          | `pdf2zh_next example.pdf --ignore-translated-pages true`                                                              |
| `ignore-translated-paragraphs`  | 이미 번역된 단락을 무시할지 여부, 기본값은 `false`     | `pdf2zh_next example.pdf --ignore-translated-paragraphs true`                                                         |
| `cache-dir`                     | 번역 결과 캐시 디렉터리, 기본값은 `./.pdf2zh_cache`                | `pdf2zh_next example.pdf --cache-dir ./cache`                                                                         |
| `config-file`                   | 구성 파일 경로                                                          | `pdf2zh_next example.pdf --config-file ./config.json`                                                                 |
| `api-key`                       | 번역 서비스 API 키                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      |
| `api-base-url`                  | 번역 서비스 기본 URL                                                        | `pdf2zh_next example.pdf --api-base-url https://api.example.com`                                                      |
| `log-level`                     | 로그 수준, 기본값은 `info`                                                           | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `help`                          | 도움말 정보 표시                                                                   | `pdf2zh_next --help`                                                                                                  |
| `version`                       | 버전 정보 표시                                                                | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--format`                      | Output format, support `text`, `markdown`, `latex`, `docx`                              | `pdf2zh_next example.pdf --format markdown`                                                                           |
| `--model`                       | Translation model, support `gpt-3.5-turbo`, `gpt-4`, `gpt-4o`                           | `pdf2zh_next example.pdf --model gpt-4o`                                                                              |
| `--language`                    | Target language (ISO 639-1 code)                                                        | `pdf2zh_next example.pdf --language ko`                                                                               |
| `--service`                     | Translation service, support `openai`, `azure`, `deepseek`                              | `pdf2zh_next example.pdf --service azure`                                                                             |
| `--key`                         | API key for translation service                                                         | `pdf2zh_next example.pdf --key sk-xxxxx`                                                                              |
| `--endpoint`                    | Custom endpoint for translation service (optional)                                       | `pdf2zh_next example.pdf --endpoint https://api.example.com/v1/chat/completions`                                      |
| `--proxy`                       | Proxy for translation service (optional)                                                 | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--pages`                       | Page range to translate (e.g., 1,3,5-10)                                                | `pdf2zh_next example.pdf --pages 1,3,5-10`                                                                            |
| `--concurrency`                 | Number of concurrent translation tasks                                                  | `pdf2zh_next example.pdf --concurrency 5`                                                                             |
| `--timeout`                     | Timeout for each translation request (seconds)                                          | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry`                       | Number of retries for failed translations                                               | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--ignore-cache`                | Ignore cache and force retranslation                                                    | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--cache-dir`                   | Custom cache directory                                                                  | `pdf2zh_next example.pdf --cache-dir /custom/cache`                                                                   |
| `--log-level`                   | Log level (debug, info, warn, error)                                                    | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATED TEXT

| `--output`                      | 파일 출력 디렉터리                                                                      | `pdf2zh_next example.pdf --output /outputpath`                                                                        |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--format`                      | 출력 형식, `text`, `markdown`, `latex`, `docx` 지원                                     | `pdf2zh_next example.pdf --format markdown`                                                                           |
| `--model`                       | 번역 모델, `gpt-3.5-turbo`, `gpt-4`, `gpt-4o` 지원                                     | `pdf2zh_next example.pdf --model gpt-4o`                                                                              |
| `--language`                    | 대상 언어 (ISO 639-1 코드)                                                              | `pdf2zh_next example.pdf --language ko`                                                                               |
| `--service`                     | 번역 서비스, `openai`, `azure`, `deepseek` 지원                                         | `pdf2zh_next example.pdf --service azure`                                                                             |
| `--key`                         | 번역 서비스 API 키                                                                      | `pdf2zh_next example.pdf --key sk-xxxxx`                                                                              |
| `--endpoint`                    | 번역 서비스 사용자 정의 엔드포인트 (선택 사항)                                          | `pdf2zh_next example.pdf --endpoint https://api.example.com/v1/chat/completions`                                      |
| `--proxy`                       | 번역 서비스 프록시 (선택 사항)                                                          | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--pages`                       | 번역할 페이지 범위 (예: 1,3,5-10)                                                       | `pdf2zh_next example.pdf --pages 1,3,5-10`                                                                            |
| `--concurrency`                 | 동시 번역 작업 수                                                                       | `pdf2zh_next example.pdf --concurrency 5`                                                                             |
| `--timeout`                     | 각 번역 요청 시간 초과 (초)                                                             | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--retry`                       | 실패한 번역 재시도 횟수                                                                 | `pdf2zh_next example.pdf --retry 3`                                                                                   |
| `--ignore-cache`                | 캐시 무시 및 강제 재번역                                                                | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| `--cache-dir`                   | 사용자 정의 캐시 디렉터리                                                               | `pdf2zh_next example.pdf --cache-dir /custom/cache`                                                                   |
| `--log-level`                   | 로그 수준 (debug, info, warn, error)                                                    | `pdf2zh_next example.pdf --log-level debug`                                                                           |
| `--help`                        | 도움말 메시지 표시                                                                      | `pdf2zh_next --help`                                                                                                  |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-model`            | Specify model for the service                                                          | `pdf2zh_next example.pdf --openai-model gpt-4o`<br>`pdf2zh_next example.pdf --deepseek-model deepseek-chat`           |
| `--<Services>-key`              | Specify API key for the service                                                        | `pdf2zh_next example.pdf --openai-key $OPENAI_API_KEY`<br>`pdf2zh_next example.pdf --deepseek-key $DEEPSEEK_API_KEY`  |
| `--<Services>-base`             | Specify base URL for the service                                                       | `pdf2zh_next example.pdf --openai-base https://api.openai.com/v1`                                                     |
| `--<Services>-prompt`           | Custom prompt for the service                                                          | `pdf2zh_next example.pdf --openai-prompt "Translate the following content into Chinese"`                              |
| `--<Services>-max-tokens`       | Maximum tokens for the service                                                         | `pdf2zh_next example.pdf --openai-max-tokens 4096`                                                                    |

---

### TRANSLATION RESULT

| `--<Services>`                  | [**특정 서비스**](./Documentation-of-Translation-Services.md) 를 사용하여 번역 | `pdf2zh_next example.pdf --openai`<br>`pdf2zh_next example.pdf --deepseek`                                            |
| ------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--<Services>-model`            | 서비스에 사용할 모델 지정                                                              | `pdf2zh_next example.pdf --openai-model gpt-4o`<br>`pdf2zh_next example.pdf --deepseek-model deepseek-chat`           |
| `--<Services>-key`              | 서비스에 사용할 API 키 지정                                                            | `pdf2zh_next example.pdf --openai-key $OPENAI_API_KEY`<br>`pdf2zh_next example.pdf --deepseek-key $DEEPSEEK_API_KEY`  |
| `--<Services>-base`             | 서비스의 기본 URL 지정                                                                 | `pdf2zh_next example.pdf --openai-base https://api.openai.com/v1`                                                     |
| `--<Services>-prompt`           | 서비스에 사용할 사용자 정의 프롬프트                                                    | `pdf2zh_next example.pdf --openai-prompt "Translate the following content into Chinese"`                              |
| `--<Services>-max-tokens`       | 서비스에 사용할 최대 토큰 수                                                            | `pdf2zh_next example.pdf --openai-max-tokens 4096`                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | Show version and exit                                                                   | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i` `<input_path>`  | Input file path (required)                                                              | `pdf2zh_next -i ./test.pdf`                                                                                           |
| `--output`, `-o` `<output_dir>`  | Output directory (optional, default: same as input file directory)                       | `pdf2zh_next -i ./test.pdf -o ./output`                                                                               |
| `--mode`, `-m` `<mode>`         | Translation mode (optional, default: `extract`)                                          | `pdf2zh_next -i ./test.pdf -m translate`                                                                              |
| `--model`, `-M` `<model>`       | Model name (optional, default: `gpt-4o-mini`)                                           | `pdf2zh_next -i ./test.pdf -M gpt-4`                                                                                  |
| `--lang`, `-l` `<lang>`         | Target language (optional, default: `zh`), see [Supported Languages](supported-lang.md) | `pdf2zh_next -i ./test.pdf -l ja`                                                                                     |
| `--api-key`, `-k` `<api_key>`   | OpenAI API key (optional, default: read from environment variable `OPENAI_API_KEY`)     | `pdf2zh_next -i ./test.pdf -k sk-xxx`                                                                                |
| `--proxy`, `-p` `<proxy_url>`   | Proxy URL (optional, default: read from environment variable `ALL_PROXY`)               | `pdf2zh_next -i ./test.pdf -p http://127.0.0.1:7890`                                                                  |
| `--threads`, `-t` `<threads>`   | Number of threads (optional, default: `4`)                                              | `pdf2zh_next -i ./test.pdf -t 8`                                                                                      |
| `--retry`, `-r` `<retry_times>` | Retry times (optional, default: `3`)                                                    | `pdf2zh_next -i ./test.pdf -r 5`                                                                                      |
| `--timeout`, `-T` `<timeout>`   | Timeout in seconds (optional, default: `300`)                                           | `pdf2zh_next -i ./test.pdf -T 600`                                                                                    |
| `--debug`                       | Enable debug mode (optional)                                                             | `pdf2zh_next -i ./test.pdf --debug`                                                                                   |
| `--config`, `-c` `<config_path>`| Config file path (optional)                                                              | `pdf2zh_next -i ./test.pdf -c ./config.json`                                                                          |
| `--yes`, `-y`                   | Skip all confirmations (optional)                                                       | `pdf2zh_next -i ./test.pdf -y`                                                                                        |
| `--list-models`                 | List available models (optional)                                                        | `pdf2zh_next --list-models`                                                                                           |
| `--list-langs`                  | List supported languages (optional)                                                      | `pdf2zh_next --list-langs`                                                                                            |

---

### OUTPUT

| `--help`, `-h`                  | 도움말 표시 및 종료                                                                      | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--version`, `-v`               | 버전 표시 및 종료                                                                       | `pdf2zh_next -v`                                                                                                      |
| `--input`, `-i` `<input_path>`  | 입력 파일 경로 (필수)                                                                   | `pdf2zh_next -i ./test.pdf`                                                                                           |
| `--output`, `-o` `<output_dir>`  | 출력 디렉터리 (선택, 기본값: 입력 파일과 동일한 디렉터리)                               | `pdf2zh_next -i ./test.pdf -o ./output`                                                                               |
| `--mode`, `-m` `<mode>`         | 번역 모드 (선택, 기본값: `extract`)                                                     | `pdf2zh_next -i ./test.pdf -m translate`                                                                              |
| `--model`, `-M` `<model>`       | 모델 이름 (선택, 기본값: `gpt-4o-mini`)                                                 | `pdf2zh_next -i ./test.pdf -M gpt-4`                                                                                  |
| `--lang`, `-l` `<lang>`         | 대상 언어 (선택, 기본값: `zh`), [지원 언어](supported-lang.md) 참조                      | `pdf2zh_next -i ./test.pdf -l ja`                                                                                     |
| `--api-key`, `-k` `<api_key>`   | OpenAI API 키 (선택, 기본값: 환경 변수 `OPENAI_API_KEY` 에서 읽음)                        | `pdf2zh_next -i ./test.pdf -k sk-xxx`                                                                                |
| `--proxy`, `-p` `<proxy_url>`   | 프록시 URL (선택, 기본값: 환경 변수 `ALL_PROXY` 에서 읽음)                                | `pdf2zh_next -i ./test.pdf -p http://127.0.0.1:7890`                                                                  |
| `--threads`, `-t` `<threads>`   | 스레드 수 (선택, 기본값: `4`)                                                           | `pdf2zh_next -i ./test.pdf -t 8`                                                                                      |
| `--retry`, `-r` `<retry_times>` | 재시도 횟수 (선택, 기본값: `3`)                                                         | `pdf2zh_next -i ./test.pdf -r 5`                                                                                      |
| `--timeout`, `-T` `<timeout>`   | 타임아웃 (초 단위, 선택, 기본값: `300`)                                                 | `pdf2zh_next -i ./test.pdf -T 600`                                                                                    |
| `--debug`                       | 디버그 모드 활성화 (선택)                                                                | `pdf2zh_next -i ./test.pdf --debug`                                                                                   |
| `--config`, `-c` `<config_path>`| 설정 파일 경로 (선택)                                                                    | `pdf2zh_next -i ./test.pdf -c ./config.json`                                                                          |
| `--yes`, `-y`                   | 모든 확인 건너뛰기 (선택)                                                                | `pdf2zh_next -i ./test.pdf -y`                                                                                        |
| `--list-models`                 | 사용 가능한 모델 목록 표시 (선택)                                                        | `pdf2zh_next --list-models`                                                                                           |
| `--list-langs`                  | 지원 언어 목록 표시 (선택)                                                               | `pdf2zh_next --list-langs`                                                                                            |
If `--config-file` is not specified, the tool will use the default configuration. If the default configuration file does not exist, the tool will create one with default settings. |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--config-file`                 | The path to the configuration file.                                                     | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | If `--config-file` is not specified, the tool will use the default configuration. If the default configuration file does not exist, the tool will create one with default settings. |
| `--engine`                      | The translation engine to use.                                                          | `pdf2zh_next --engine google`                                                                                         |                                                                                                                                                                                    |
| `--source-language`             | The source language of the document.                                                    | `pdf2zh_next --source-language en`                                                                                    | If not specified, the tool will attempt to detect the source language automatically.                                                                                              |
| `--target-language`             | The target language for translation.                                                     | `pdf2zh_next --target-language zh-CN`                                                                                  | If not specified, the tool will use the default target language.                                                                                                                   |
| `--output-dir`                   | The directory where the translated files will be saved.                                 | `pdf2zh_next --output-dir /path/to/output`                                                                             | If not specified, the tool will save the translated files in the same directory as the source file.                                                                                 |
| `--output-format`                | The format of the output file.                                                           | `pdf2zh_next --output-format docx`                                                                                     | Supported formats: `pdf`, `docx`, `txt`, `markdown`. If not specified, the tool will use the same format as the source file.                                                        |
| `--concurrency`                  | The number of concurrent translation tasks.                                             | `pdf2zh_next --concurrency 5`                                                                                          | If not specified, the tool will use the default concurrency setting.                                                                                                               |
| `--timeout`                      | The timeout for each translation request in seconds.                                     | `pdf2zh_next --timeout 30`                                                                                             | If not specified, the tool will use the default timeout setting.                                                                                                                   |
| `--retry`                        | The number of retries for failed translation requests.                                   | `pdf2zh_next --retry 3`                                                                                                | If not specified, the tool will use the default retry setting.                                                                                                                     |
| `--log-level`                    | The log level for the tool.                                                              | `pdf2zh_next --log-level debug`                                                                                        | Supported levels: `debug`, `info`, `warning`, `error`. If not specified, the tool will use the default log level.                                                                  |
| `--log-file`                     | The file to which logs will be written.                                                  | `pdf2zh_next --log-file /path/to/log/file.log`                                                                         | If not specified, the tool will write logs to the console.                                                                                                                         |
| `--help`                         | Display help information.                                                                | `pdf2zh_next --help`                                                                                                   |                                                                                                                                                                                    |
| `--version`                      | Display the version of the tool.                                                         | `pdf2zh_next --version`                                                                                                |                                                                                                                                                                                    |

---

### OUTPUT

| `--config-file`                 | 구성 파일 경로                                                                          | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `--config-file` 을 지정하지 않으면 도구는 기본 구성을 사용합니다. 기본 구성 파일이 존재하지 않으면 도구는 기본 설정으로 구성 파일을 생성합니다. |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--config-file`                 | 구성 파일 경로.                                                                         | `pdf2zh_next --config-file /path/to/config/config.toml`                                                               | `--config-file` 을 지정하지 않으면 도구는 기본 구성을 사용합니다. 기본 구성 파일이 존재하지 않으면 도구는 기본 설정으로 구성 파일을 생성합니다. |
| `--engine`                      | 사용할 번역 엔진.                                                                       | `pdf2zh_next --engine google`                                                                                         |                                                                                                                                                                                    |
| `--source-language`             | 문서의 원본 언어.                                                                       | `pdf2zh_next --source-language en`                                                                                    | 지정하지 않으면 도구는 원본 언어를 자동으로 감지하려고 시도합니다.                                                                                              |
| `--target-language`             | 번역 대상 언어.                                                                         | `pdf2zh_next --target-language zh-CN`                                                                                  | 지정하지 않으면 도구는 기본 대상 언어를 사용합니다.                                                                                                                   |
| `--output-dir`                   | 번역된 파일이 저장될 디렉터리.                                                           | `pdf2zh_next --output-dir /path/to/output`                                                                             | 지정하지 않으면 도구는 번역된 파일을 원본 파일과 같은 디렉터리에 저장합니다.                                                                                 |
| `--output-format`                | 출력 파일 형식.                                                                         | `pdf2zh_next --output-format docx`                                                                                     | 지원 형식: `pdf`, `docx`, `txt`, `markdown`. 지정하지 않으면 도구는 원본 파일과 같은 형식을 사용합니다.                                                        |
| `--concurrency`                  | 동시 번역 작업 수.                                                                      | `pdf2zh_next --concurrency 5`                                                                                          | 지정하지 않으면 도구는 기본 동시성 설정을 사용합니다.                                                                                                               |
| `--timeout`                      | 각 번역 요청에 대한 타임아웃 (초 단위).                                                  | `pdf2zh_next --timeout 30`                                                                                             | 지정하지 않으면 도구는 기본 타임아웃 설정을 사용합니다.                                                                                                                   |
| `--retry`                        | 실패한 번역 요청에 대한 재시도 횟수.                                                     | `pdf2zh_next --retry 3`                                                                                                | 지정하지 않으면 도구는 기본 재시도 설정을 사용합니다.                                                                                                                     |
| `--log-level`                    | 도구의 로그 레벨.                                                                       | `pdf2zh_next --log-level debug`                                                                                        | 지원 레벨: `debug`, `info`, `warning`, `error`. 지정하지 않으면 도구는 기본 로그 레벨을 사용합니다.                                                                  |
| `--log-file`                     | 로그가 기록될 파일.                                                                     | `pdf2zh_next --log-file /path/to/log/file.log`                                                                         | 지정하지 않으면 도구는 로그를 콘솔에 출력합니다.                                                                                                                         |
| `--help`                         | 도움말 정보를 표시합니다.                                                               | `pdf2zh_next --help`                                                                                                   |                                                                                                                                                                                    |
| `--version`                      | 도구의 버전을 표시합니다.                                                               | `pdf2zh_next --version`                                                                                                |                                                                                                                                                                                    |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--report-interval`             | Progress report interval in seconds                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--report-interval`             | Progress report interval in seconds                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |

---

### OUTPUT

| `--report-interval`             | 진행 보고 간격 (초 단위)                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--report-interval`             | 진행 보고 간격 (초 단위)                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| `--report-interval`             | 진행 보고 간격 (초 단위)                                                     | `pdf2zh_next example.pdf --report-interval 5`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enable-cache`                | Enable cache for translation service                                                    | `pdf2zh_next example.pdf --enable-cache`                                                                              |
| `--disable-cache`               | Disable cache for translation service                                                   | `pdf2zh_next example.pdf --disable-cache`                                                                             |
| `--cache-dir <cache-dir>`       | Specify cache directory                                                                 | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--clean-cache`                 | Clean cache directory and exit                                                          | `pdf2zh_next --clean-cache`                                                                                           |
| `--cache-only`                  | Use cache only, do not call translation service                                         | `pdf2zh_next example.pdf --cache-only`                                                                                |
| `--force-refresh`               | Force refresh cache for translation service                                             | `pdf2zh_next example.pdf --force-refresh`                                                                             |
| `--dry-run`                     | Perform a trial run with no changes made                                                | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | Show version information and exit                                                       | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next --help`                                                                                                  |

---

### TRANSLATION

| `--debug`                       | 디버그 로깅 수준 사용                                                                   | `pdf2zh_next example.pdf --debug`                                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enable-cache`                | 번역 서비스에 캐시 활성화                                                                | `pdf2zh_next example.pdf --enable-cache`                                                                              |
| `--disable-cache`               | 번역 서비스에 캐시 비활성화                                                              | `pdf2zh_next example.pdf --disable-cache`                                                                             |
| `--cache-dir <cache-dir>`       | 캐시 디렉토리 지정                                                                       | `pdf2zh_next example.pdf --cache-dir ./my_cache`                                                                      |
| `--clean-cache`                 | 캐시 디렉토리 정리 후 종료                                                               | `pdf2zh_next --clean-cache`                                                                                           |
| `--cache-only`                  | 캐시만 사용, 번역 서비스 호출 안 함                                                      | `pdf2zh_next example.pdf --cache-only`                                                                                |
| `--force-refresh`               | 번역 서비스에 대한 캐시 강제 새로고침                                                    | `pdf2zh_next example.pdf --force-refresh`                                                                             |
| `--dry-run`                     | 변경 사항 없이 시험 실행 수행                                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | 버전 정보 표시 후 종료                                                                   | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 도움말 표시 후 종료                                                                      | `pdf2zh_next --help`                                                                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--webui`                       | Interact with WebUI                                                                     | `pdf2zh_next --webui`                                                                                                 |
| `--config`                      | Open config file in default editor                                                     | `pdf2zh_next --config`                                                                                                |
| `--version`                     | Print version information                                                               | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Print help information                                                                  | `pdf2zh_next --help`                                                                                                  |
| `--list-languages`              | List all supported language codes                                                       | `pdf2zh_next --list-languages`                                                                                        |
| `--list-translation-services`   | List all supported translation services                                                 | `pdf2zh_next --list-translation-services`                                                                             |
| `--list-models`                 | List all supported models for a translation service                                     | `pdf2zh_next --list-models --service=google`                                                                          |
| `--list-documentation`          | List documentation of translation services                                              | `pdf2zh_next --list-documentation`                                                                                    |
| `--open-documentation`          | Open documentation of a translation service in browser                                  | `pdf2zh_next --open-documentation --service=google`                                                                   |
| `--list-ocr-services`           | List all supported OCR services                                                         | `pdf2zh_next --list-ocr-services`                                                                                     |
| `--list-ocr-languages`          | List all supported languages for an OCR service                                         | `pdf2zh_next --list-ocr-languages --service=google`                                                                   |
| `--list-ocr-documentation`      | List documentation of OCR services                                                      | `pdf2zh_next --list-ocr-documentation`                                                                                |
| `--open-ocr-documentation`      | Open documentation of an OCR service in browser                                         | `pdf2zh_next --open-ocr-documentation --service=google`                                                               |

---

### TRANSLATION RESULT

| `--gui`                         | GUI 와 상호작용                                                                         | `pdf2zh_next --gui`                                                                                                   |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--webui`                       | WebUI 와 상호작용                                                                       | `pdf2zh_next --webui`                                                                                                 |
| `--config`                      | 기본 편집기에서 구성 파일 열기                                                          | `pdf2zh_next --config`                                                                                                |
| `--version`                     | 버전 정보 출력                                                                          | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 도움말 정보 출력                                                                        | `pdf2zh_next --help`                                                                                                  |
| `--list-languages`              | 지원되는 모든 언어 코드 목록                                                            | `pdf2zh_next --list-languages`                                                                                        |
| `--list-translation-services`   | 지원되는 모든 번역 서비스 목록                                                          | `pdf2zh_next --list-translation-services`                                                                             |
| `--list-models`                 | 번역 서비스에 대해 지원되는 모든 모델 목록                                              | `pdf2zh_next --list-models --service=google`                                                                          |
| `--list-documentation`          | 번역 서비스의 문서 목록                                                                 | `pdf2zh_next --list-documentation`                                                                                    |
| `--open-documentation`          | 브라우저에서 번역 서비스의 문서 열기                                                    | `pdf2zh_next --open-documentation --service=google`                                                                   |
| `--list-ocr-services`           | 지원되는 모든 OCR 서비스 목록                                                           | `pdf2zh_next --list-ocr-services`                                                                                     |
| `--list-ocr-languages`          | OCR 서비스에 대해 지원되는 모든 언어 목록                                               | `pdf2zh_next --list-ocr-languages --service=google`                                                                   |
| `--list-ocr-documentation`      | OCR 서비스의 문서 목록                                                                  | `pdf2zh_next --list-ocr-documentation`                                                                                |
| `--open-ocr-documentation`      | 브라우저에서 OCR 서비스의 문서 열기                                                     | `pdf2zh_next --open-ocr-documentation --service=google`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--list-languages`              | List all supported languages and exit.                                                  | `pdf2zh_next example.pdf --list-languages`                                                                            |
| `--list-models`                 | List all supported models and exit.                                                     | `pdf2zh_next example.pdf --list-models`                                                                               |
| `--list-services`               | List all supported translation services and exit.                                       | `pdf2zh_next example.pdf --list-services`                                                                             |
| `--list-fonts`                  | List all supported fonts and exit.                                                      | `pdf2zh_next example.pdf --list-fonts`                                                                                |
| `--list-ocrs`                   | List all supported OCR providers and exit.                                              | `pdf2zh_next example.pdf --list-ocrs`                                                                                 |
| `--list-all`                    | List all supported models, translation services, fonts and OCR providers, then exit.    | `pdf2zh_next example.pdf --list-all`                                                                                  |
| `--help`, `-h`                  | Show this help message and exit.                                                        | `pdf2zh_next example.pdf --help`                                                                                      |

---

### OUTPUT

| `--warmup`                      | 필요한 자산만 다운로드하고 검증한 후 종료                                      | `pdf2zh_next example.pdf --warmup`                                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--list-languages`              | 지원되는 모든 언어를 나열하고 종료.                                                  | `pdf2zh_next example.pdf --list-languages`                                                                            |
| `--list-models`                 | 지원되는 모든 모델을 나열하고 종료.                                                     | `pdf2zh_next example.pdf --list-models`                                                                               |
| `--list-services`               | 지원되는 모든 번역 서비스를 나열하고 종료.                                       | `pdf2zh_next example.pdf --list-services`                                                                             |
| `--list-fonts`                  | 지원되는 모든 글꼴을 나열하고 종료.                                                      | `pdf2zh_next example.pdf --list-fonts`                                                                                |
| `--list-ocrs`                   | 지원되는 모든 OCR 제공자를 나열하고 종료.                                              | `pdf2zh_next example.pdf --list-ocrs`                                                                                 |
| `--list-all`                    | 지원되는 모든 모델, 번역 서비스, 글꼴 및 OCR 제공자를 나열한 후 종료.    | `pdf2zh_next example.pdf --list-all`                                                                                  |
| `--help`, `-h`                  | 이 도움말 메시지를 표시하고 종료.                                                        | `pdf2zh_next example.pdf --help`                                                                                      |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--offline-mode`                | Enable offline mode                                                                      | `pdf2zh_next example.pdf --offline-mode`                                                                              |

---

### OUTPUT

| `--generate-offline-assets`     | 지정된 디렉토리에 오프라인 자산 패키지 생성                               | `pdf2zh_next example.pdf --generate-offline-assets /path`                                                             |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--offline-mode`                | 오프라인 모드 활성화                                                                      | `pdf2zh_next example.pdf --offline-mode`                                                                              |
|
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---|
| `--enable-offline-dictionary`   | Enable offline dictionary (requires `--restore-offline-assets` to be set)                | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-dictionary`                                  |   |
| `--enable-offline-ocr`          | Enable offline OCR (requires `--restore-offline-assets` to be set)                       | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-ocr`                                         |   |
| `--enable-offline-translation`  | Enable offline translation (requires `--restore-offline-assets` to be set)                | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-translation`                                  |   |
| `--enable-offline-pp`           | Enable offline post-processing (requires `--restore-offline-assets` to be set)            | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-pp`                                          |   |
| `--enable-offline-paragraph`    | Enable offline paragraph (requires `--restore-offline-assets` to be set)                 | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-paragraph`                                   |   |
| `--enable-offline-llm`          | Enable offline LLM (requires `--restore-offline-assets` to be set)                       | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-llm`                                         |   |

---

### OUTPUT

| `--restore-offline-assets`      | 지정된 디렉토리에서 오프라인 에셋 패키지를 복원합니다.                             | `pdf2zh_next example.pdf --restore-offline-assets /path`                                                              |   |
|---------------------------------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---|
| `--enable-offline-dictionary`   | 오프라인 사전을 활성화합니다. (`--restore-offline-assets` 설정 필요)                | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-dictionary`                                  |   |
| `--enable-offline-ocr`          | 오프라인 OCR 을 활성화합니다. (`--restore-offline-assets` 설정 필요)                       | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-ocr`                                         |   |
| `--enable-offline-translation`  | 오프라인 번역을 활성화합니다. (`--restore-offline-assets` 설정 필요)                | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-translation`                                  |   |
| `--enable-offline-pp`           | 오프라인 후처리를 활성화합니다. (`--restore-offline-assets` 설정 필요)            | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-pp`                                          |   |
| `--enable-offline-paragraph`    | 오프라인 단락 처리를 활성화합니다. (`--restore-offline-assets` 설정 필요)                 | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-paragraph`                                   |   |
| `--enable-offline-llm`          | 오프라인 LLM 을 활성화합니다. (`--restore-offline-assets` 설정 필요)                       | `pdf2zh_next example.pdf --restore-offline-assets /path --enable-offline-llm`                                         |   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | Show this message and exit                                                              | `pdf2zh_next -h`                                                                                                      |
| `-v`, `--verbose`               | Print more messages.                                                                    | `pdf2zh_next -v -i input.pdf -o output.pdf`                                                                           |
| `-i`, `--input <input_path>`    | Input file path.                                                                        | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output <output_path>`  | Output file path.                                                                       | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-l`, `--language <lang_code>`  | Language code of output. (default: `zh-CN`)                                             | `pdf2zh_next -i input.pdf -l zh-TW`                                                                                   |
| `-s`, `--service <service>`     | Translation service. (default: `google`)                                                | `pdf2zh_next -i input.pdf -s deeplx`                                                                                  |
| `-k`, `--key <api_key>`         | API key for translation service.                                                        | `pdf2zh_next -i input.pdf -s google -k YOUR_API_KEY`                                                                  |
| `-m`, `--mode <mode>`           | Mode of translation. (default: `markdown`)                                              | `pdf2zh_next -i input.pdf -m markdown`                                                                                |
| `-c`, `--config <config_path>`  | Path to config file.                                                                    | `pdf2zh_next -i input.pdf -c config.json`                                                                             |
| `-p`, `--proxy <proxy_url>`     | Proxy URL for translation service.                                                      | `pdf2zh_next -i input.pdf -p http://127.0.0.1:7890`                                                                   |
| `--ocr`                         | Enable OCR for images in PDF.                                                           | `pdf2zh_next -i input.pdf --ocr`                                                                                      |
| `--ocr-lang <ocr_lang>`         | Language for OCR. (default: `eng+chi_sim`)                                              | `pdf2zh_next -i input.pdf --ocr --ocr-lang eng+chi_sim`                                                               |
| `--no-translate`                | Disable translation. (Extract text only)                                                | `pdf2zh_next -i input.pdf --no-translate`                                                                             |
| `--no-format`                   | Disable markdown formatting. (Only available when `--no-translate` is enabled)          | `pdf2zh_next -i input.pdf --no-translate --no-format`                                                                 |
| `--font <font_path>`            | Path to font file for output PDF.                                                       | `pdf2zh_next -i input.pdf --font path/to/font.ttf`                                                                    |
| `--font-size <font_size>`       | Font size for output PDF. (default: 12)                                                 | `pdf2zh_next -i input.pdf --font-size 14`                                                                             |
| `--line-space <line_space>`     | Line spacing for output PDF. (default: 1.2)                                             | `pdf2zh_next -i input.pdf --line-space 1.5`                                                                           |
| `--page-width <page_width>`     | Page width for output PDF. (default: 595)                                               | `pdf2zh_next -i input.pdf --page-width 600`                                                                           |
| `--page-height <page_height>`   | Page height for output PDF. (default: 842)                                              | `pdf2zh_next -i input.pdf --page-height 800`                                                                          |
| `--margin <margin>`             | Page margin for output PDF. (default: 40)                                               | `pdf2zh_next -i input.pdf --margin 50`                                                                                |
| `--title <title>`               | Title for output PDF. (default: same as input)                                          | `pdf2zh_next -i input.pdf --title "My Document"`                                                                      |
| `--author <author>`             | Author for output PDF. (default: same as input)                                         | `pdf2zh_next -i input.pdf --author "John Doe"`                                                                        |
| `--subject <subject>`           | Subject for output PDF. (default: same as input)                                        | `pdf2zh_next -i input.pdf --subject "My Subject"`                                                                     |
| `--keywords <keywords>`         | Keywords for output PDF. (default: same as input)                                       | `pdf2zh_next -i input.pdf --keywords "keyword1, keyword2"`                                                            |
| `--creator <creator>`           | Creator for output PDF. (default: `pdf2zh`)                                             | `pdf2zh_next -i input.pdf --creator "My Creator"`                                                                     |
| `--producer <producer>`         | Producer for output PDF. (default: `pdf2zh`)                                            | `pdf2zh_next -i input.pdf --producer "My Producer"`                                                                   |
| `--creation-date <creation_date>` | Creation date for output PDF. (default: current date)                                   | `pdf2zh_next -i input.pdf --creation-date "2024-01-01"`                                                               |
| `--mod-date <mod_date>`         | Modification date for output PDF. (default: current date)                               | `pdf2zh_next -i input.pdf --mod-date "2024-01-01"`                                                                    |
| `--timeout <timeout>`           | Timeout for translation service in seconds. (default: 30)                               | `pdf2zh_next -i input.pdf --timeout 60`                                                                               |
| `--retry <retry>`               | Number of retries for translation service. (default: 3)                                 | `pdf2zh_next -i input.pdf --retry 5`                                                                                  |
| `--retry-delay <retry_delay>`   | Delay between retries in seconds. (default: 1)                                          | `pdf2zh_next -i input.pdf --retry-delay 2`                                                                            |
| `--batch-size <batch_size>`     | Batch size for translation. (default: 10)                                               | `pdf2zh_next -i input.pdf --batch-size 20`                                                                            |
| `--max-workers <max_workers>`   | Maximum number of workers for translation. (default: 5)                                 | `pdf2zh_next -i input.pdf --max-workers 10`                                                                           |
| `--no-cache`                    | Disable cache for translation.                                                          | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir <cache_dir>`       | Directory for cache. (default: `~/.cache/pdf2zh`)                                       | `pdf2zh_next -i input.pdf --cache-dir /path/to/cache`                                                                 |
| `--clean-cache`                 | Clean cache before translation.                                                         | `pdf2zh_next -i input.pdf --clean-cache`                                                                              |
| `--list-services`               | List available translation services.                                                    | `pdf2zh_next --list-services`                                                                                         |
| `--list-languages`              | List supported languages for translation.                                               | `pdf2zh_next --list-languages`                                                                                        |
| `--list-ocr-languages`          | List supported languages for OCR.                                                       | `pdf2zh_next --list-ocr-languages`                                                                                    |
| `--list-fonts`                  | List available fonts for output PDF.                                                    | `pdf2zh_next --list-fonts`                                                                                            |

---

### TRANSLATION RESULT

| `--version`                     | 버전을 표시한 후 종료                                                                   | `pdf2zh_next --version`                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `-h`, `--help`                  | 이 메시지를 표시하고 종료                                                               | `pdf2zh_next -h`                                                                                                      |
| `-v`, `--verbose`               | 더 많은 메시지를 출력합니다.                                                              | `pdf2zh_next -v -i input.pdf -o output.pdf`                                                                           |
| `-i`, `--input <input_path>`    | 입력 파일 경로                                                                           | `pdf2zh_next -i input.pdf`                                                                                            |
| `-o`, `--output <output_path>`  | 출력 파일 경로                                                                           | `pdf2zh_next -i input.pdf -o output.pdf`                                                                              |
| `-l`, `--language <lang_code>`  | 출력 언어 코드 (기본값: `zh-CN`)                                                          | `pdf2zh_next -i input.pdf -l zh-TW`                                                                                   |
| `-s`, `--service <service>`     | 번역 서비스 (기본값: `google`)                                                            | `pdf2zh_next -i input.pdf -s deeplx`                                                                                  |
| `-k`, `--key <api_key>`         | 번역 서비스 API 키                                                                        | `pdf2zh_next -i input.pdf -s google -k YOUR_API_KEY`                                                                  |
| `-m`, `--mode <mode>`           | 번역 모드 (기본값: `markdown`)                                                            | `pdf2zh_next -i input.pdf -m markdown`                                                                                |
| `-c`, `--config <config_path>`  | 설정 파일 경로                                                                           | `pdf2zh_next -i input.pdf -c config.json`                                                                             |
| `-p`, `--proxy <proxy_url>`     | 번역 서비스 프록시 URL                                                                    | `pdf2zh_next -i input.pdf -p http://127.0.0.1:7890`                                                                   |
| `--ocr`                         | PDF 내 이미지에 대해 OCR 활성화                                                           | `pdf2zh_next -i input.pdf --ocr`                                                                                      |
| `--ocr-lang <ocr_lang>`         | OCR 언어 (기본값: `eng+chi_sim`)                                                          | `pdf2zh_next -i input.pdf --ocr --ocr-lang eng+chi_sim`                                                               |
| `--no-translate`                | 번역 비활성화 (텍스트만 추출)                                                              | `pdf2zh_next -i input.pdf --no-translate`                                                                             |
| `--no-format`                   | 마크다운 서식 지정 비활성화 (`--no-translate` 이 활성화된 경우에만 사용 가능)                       | `pdf2zh_next -i input.pdf --no-translate --no-format`                                                                 |
| `--font <font_path>`            | 출력 PDF 용 글꼴 파일 경로                                                                 | `pdf2zh_next -i input.pdf --font path/to/font.ttf`                                                                    |
| `--font-size <font_size>`       | 출력 PDF 용 글꼴 크기 (기본값: 12)                                                          | `pdf2zh_next -i input.pdf --font-size 14`                                                                             |
| `--line-space <line_space>`     | 출력 PDF 용 줄 간격 (기본값: 1.2)                                                           | `pdf2zh_next -i input.pdf --line-space 1.5`                                                                           |
| `--page-width <page_width>`     | 출력 PDF 용 페이지 너비 (기본값: 595)                                                        | `pdf2zh_next -i input.pdf --page-width 600`                                                                           |
| `--page-height <page_height>`   | 출력 PDF 용 페이지 높이 (기본값: 842)                                                        | `pdf2zh_next -i input.pdf --page-height 800`                                                                          |
| `--margin <margin>`             | 출력 PDF 용 페이지 여백 (기본값: 40)                                                         | `pdf2zh_next -i input.pdf --margin 50`                                                                                |
| `--title <title>`               | 출력 PDF 용 제목 (기본값: 입력 파일과 동일)                                                   | `pdf2zh_next -i input.pdf --title "My Document"`                                                                      |
| `--author <author>`             | 출력 PDF 용 저자 (기본값: 입력 파일과 동일)                                                   | `pdf2zh_next -i input.pdf --author "John Doe"`                                                                        |
| `--subject <subject>`           | 출력 PDF 용 주제 (기본값: 입력 파일과 동일)                                                   | `pdf2zh_next -i input.pdf --subject "My Subject"`                                                                     |
| `--keywords <keywords>`         | 출력 PDF 용 키워드 (기본값: 입력 파일과 동일)                                                  | `pdf2zh_next -i input.pdf --keywords "keyword1, keyword2"`                                                            |
| `--creator <creator>`           | 출력 PDF 용 생성자 (기본값: `pdf2zh`)                                                        | `pdf2zh_next -i input.pdf --creator "My Creator"`                                                                     |
| `--producer <producer>`         | 출력 PDF 용 제작자 (기본값: `pdf2zh`)                                                        | `pdf2zh_next -i input.pdf --producer "My Producer"`                                                                   |
| `--creation-date <creation_date>` | 출력 PDF 용 생성 날짜 (기본값: 현재 날짜)                                                     | `pdf2zh_next -i input.pdf --creation-date "2024-01-01"`                                                               |
| `--mod-date <mod_date>`         | 출력 PDF 용 수정 날짜 (기본값: 현재 날짜)                                                     | `pdf2zh_next -i input.pdf --mod-date "2024-01-01"`                                                                    |
| `--timeout <timeout>`           | 번역 서비스 타임아웃 (초 단위, 기본값: 30)                                                   | `pdf2zh_next -i input.pdf --timeout 60`                                                                               |
| `--retry <retry>`               | 번역 서비스 재시도 횟수 (기본값: 3)                                                         | `pdf2zh_next -i input.pdf --retry 5`                                                                                  |
| `--retry-delay <retry_delay>`   | 재시도 간 지연 시간 (초 단위, 기본값: 1)                                                     | `pdf2zh_next -i input.pdf --retry-delay 2`                                                                            |
| `--batch-size <batch_size>`     | 번역 배치 크기 (기본값: 10)                                                                | `pdf2zh_next -i input.pdf --batch-size 20`                                                                            |
| `--max-workers <max_workers>`   | 번역용 최대 작업자 수 (기본값: 5)                                                           | `pdf2zh_next -i input.pdf --max-workers 10`                                                                           |
| `--no-cache`                    | 번역 캐시 비활성화                                                                        | `pdf2zh_next -i input.pdf --no-cache`                                                                                 |
| `--cache-dir <cache_dir>`       | 캐시 디렉토리 (기본값: `~/.cache/pdf2zh`)                                                  | `pdf2zh_next -i input.pdf --cache-dir /path/to/cache`                                                                 |
| `--clean-cache`                 | 번역 전 캐시 정리                                                                         | `pdf2zh_next -i input.pdf --clean-cache`                                                                              |
| `--list-services`               | 사용 가능한 번역 서비스 목록 표시                                                           | `pdf2zh_next --list-services`                                                                                         |
| `--list-languages`              | 지원되는 번역 언어 목록 표시                                                               | `pdf2zh_next --list-languages`                                                                                        |
| `--list-ocr-languages`          | 지원되는 OCR 언어 목록 표시                                                                | `pdf2zh_next --list-ocr-languages`                                                                                    |
| `--list-fonts`                  | 출력 PDF 용 사용 가능한 글꼴 목록 표시                                                        | `pdf2zh_next --list-fonts`                                                                                            |
`1,2,1-,-3,3-5` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------- |
| `--engine <engine>`             | Specify the translation engine                                                          | `pdf2zh_next example.pdf --engine google`                                                                              | `google`        |
| `--source-language <language>`  | Source language code (ISO 639-1)                                                        | `pdf2zh_next example.pdf --source-language en`                                                                         | `en`            |
| `--target-language <language>`  | Target language code (ISO 639-1)                                                        | `pdf2zh_next example.pdf --target-language zh`                                                                         | `zh`            |
| `--output <path>`               | Specify the output path                                                                 | `pdf2zh_next example.pdf --output ./output.pdf`                                                                        | `./output.pdf`  |
| `--no-translate`                | Do not translate, only extract and reconstruct the document                             | `pdf2zh_next example.pdf --no-translate`                                                                               | `true`          |
| `--no-reconstruct`              | Do not reconstruct the document, only translate the text                                | `pdf2zh_next example.pdf --no-reconstruct`                                                                             | `true`          |
| `--config <path>`               | Load configuration from a JSON file                                                     | `pdf2zh_next example.pdf --config ./config.json`                                                                       | `./config.json` |
| `--save-config <path>`          | Save the current configuration to a JSON file                                           | `pdf2zh_next example.pdf --save-config ./config.json`                                                                  | `./config.json` |
| `--proxy <proxy_url>`           | Use a proxy for translation requests                                                    | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | `http://127.0.0.1:7890` |
| `--api-key <key>`               | API key for translation service                                                         | `pdf2zh_next example.pdf --engine deepl --api-key your_api_key`                                                        | `your_api_key`  |
| `--model <model_name>`          | Model name for OpenAI or other services                                                 | `pdf2zh_next example.pdf --engine openai --model gpt-4o`                                                               | `gpt-4o`        |
| `--retry <times>`               | Number of retries for failed translation requests                                       | `pdf2zh_next example.pdf --retry 3`                                                                                    | `3`             |
| `--timeout <seconds>`           | Timeout for each translation request                                                    | `pdf2zh_next example.pdf --timeout 30`                                                                                 | `30`            |
| `--concurrency <number>`        | Number of concurrent translation requests                                               | `pdf2zh_next example.pdf --concurrency 5`                                                                              | `5`             |
| `--help`                        | Show help                                                                               | `pdf2zh_next --help`                                                                                                   | `true`          |

---

### OUTPUT

| `--pages`                       | 문서 일부 번역                                                                          | `pdf2zh_next example.pdf --pages 1,2,1-,-3,3-5`                                                                       | `1,2,1-,-3,3-5` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------- |
| `--engine <engine>`             | 번역 엔진 지정                                                                          | `pdf2zh_next example.pdf --engine google`                                                                              | `google`        |
| `--source-language <language>`  | 원본 언어 코드 (ISO 639-1)                                                              | `pdf2zh_next example.pdf --source-language en`                                                                         | `en`            |
| `--target-language <language>`  | 대상 언어 코드 (ISO 639-1)                                                              | `pdf2zh_next example.pdf --target-language zh`                                                                         | `zh`            |
| `--output <path>`               | 출력 경로 지정                                                                          | `pdf2zh_next example.pdf --output ./output.pdf`                                                                        | `./output.pdf`  |
| `--no-translate`                | 번역하지 않고 문서만 추출 및 재구성                                                     | `pdf2zh_next example.pdf --no-translate`                                                                               | `true`          |
| `--no-reconstruct`              | 문서를 재구성하지 않고 텍스트만 번역                                                    | `pdf2zh_next example.pdf --no-reconstruct`                                                                             | `true`          |
| `--config <path>`               | JSON 파일에서 구성 로드                                                                 | `pdf2zh_next example.pdf --config ./config.json`                                                                       | `./config.json` |
| `--save-config <path>`          | 현재 구성을 JSON 파일로 저장                                                            | `pdf2zh_next example.pdf --save-config ./config.json`                                                                  | `./config.json` |
| `--proxy <proxy_url>`           | 번역 요청에 프록시 사용                                                                 | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                                | `http://127.0.0.1:7890` |
| `--api-key <key>`               | 번역 서비스 API 키                                                                      | `pdf2zh_next example.pdf --engine deepl --api-key your_api_key`                                                        | `your_api_key`  |
| `--model <model_name>`          | OpenAI 또는 기타 서비스용 모델 이름                                                     | `pdf2zh_next example.pdf --engine openai --model gpt-4o`                                                               | `gpt-4o`        |
| `--retry <times>`               | 실패한 번역 요청 재시도 횟수                                                            | `pdf2zh_next example.pdf --retry 3`                                                                                    | `3`             |
| `--timeout <seconds>`           | 각 번역 요청 타임아웃                                                                   | `pdf2zh_next example.pdf --timeout 30`                                                                                 | `30`            |
| `--concurrency <number>`        | 동시 번역 요청 수                                                                       | `pdf2zh_next example.pdf --concurrency 5`                                                                              | `5`             |
| `--help`                        | 도움말 표시                                                                             | `pdf2zh_next --help`                                                                                                   | `true`          |
The language code of the source document. If not specified, the language will be automatically detected.              |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | Target language code                                                                    | `pdf2zh_next example.pdf --lang-out ko`                                                                               | The language code of the target document.                                                                             |
| `--engine`                      | Translation engine                                                                       | `pdf2zh_next example.pdf --engine openai`                                                                             | The translation engine to be used. Currently supported engines: `openai`, `google`, `azure`, `youdao`, `deepl`, `gemini`. |
| `--translator-args`             | Arguments for translation engine                                                         | `pdf2zh_next example.pdf --translator-args '{"api_key": "your-api-key"}'`                                             | Arguments for the translation engine.                                                                                 |
| `--translator-args-file`        | File path of translation engine arguments                                                | `pdf2zh_next example.pdf --translator-args-file args.json`                                                            | File path of translation engine arguments.                                                                            |
| `--translator-args-env-prefix`  | Environment variable prefix for translation engine arguments                             | `pdf2zh_next example.pdf --translator-args-env-prefix PDF2ZH_`                                                        | Environment variable prefix for translation engine arguments.                                                         |
| `--translator-args-json`        | JSON string of translation engine arguments                                              | `pdf2zh_next example.pdf --translator-args-json '{"api_key": "your-api-key"}'`                                        | JSON string of translation engine arguments.                                                                          |
| `--translator-args-yaml`        | YAML string of translation engine arguments                                              | `pdf2zh_next example.pdf --translator-args-yaml 'api_key: your-api-key'`                                              | YAML string of translation engine arguments.                                                                          |
| `--translator-args-toml`        | TOML string of translation engine arguments                                              | `pdf2zh_next example.pdf --translator-args-toml 'api_key = "your-api-key"'`                                           | TOML string of translation engine arguments.                                                                          |
| `--translator-args-ini`         | INI string of translation engine arguments                                               | `pdf2zh_next example.pdf --translator-args-ini 'api_key=your-api-key'`                                                | INI string of translation engine arguments.                                                                           |
| `--translator-args-env`         | Environment variable names for translation engine arguments                              | `pdf2zh_next example.pdf --translator-args-env API_KEY`                                                               | Environment variable names for translation engine arguments.                                                          |
| `--translator-args-default`     | Default arguments for translation engine                                                 | `pdf2zh_next example.pdf --translator-args-default`                                                                   | Default arguments for translation engine.                                                                             |
| `--translator-args-override`    | Override arguments for translation engine                                                | `pdf2zh_next example.pdf --translator-args-override`                                                                  | Override arguments for translation engine.                                                                            |
| `--translator-args-merge`       | Merge arguments for translation engine                                                   | `pdf2zh_next example.pdf --translator-args-merge`                                                                     | Merge arguments for translation engine.                                                                               |
| `--translator-args-deep-merge`  | Deep merge arguments for translation engine                                              | `pdf2zh_next example.pdf --translator-args-deep-merge`                                                                | Deep merge arguments for translation engine.                                                                          |
| `--translator-args-no-merge`    | Do not merge arguments for translation engine                                            | `pdf2zh_next example.pdf --translator-args-no-merge`                                                                  | Do not merge arguments for translation engine.                                                                        |
| `--translator-args-no-override` | Do not override arguments for translation engine                                         | `pdf2zh_next example.pdf --translator-args-no-override`                                                               | Do not override arguments for translation engine.                                                                     |
| `--translator-args-no-default`  | Do not use default arguments for translation engine                                      | `pdf2zh_next example.pdf --translator-args-no-default`                                                                | Do not use default arguments for translation engine.                                                                  |
| `--translator-args-no-env`      | Do not use environment variables for translation engine arguments                        | `pdf2zh_next example.pdf --translator-args-no-env`                                                                    | Do not use environment variables for translation engine arguments.                                                    |
| `--translator-args-no-file`     | Do not use file for translation engine arguments                                         | `pdf2zh_next example.pdf --translator-args-no-file`                                                                   | Do not use file for translation engine arguments.                                                                     |
| `--translator-args-no-json`     | Do not use JSON string for translation engine arguments                                  | `pdf2zh_next example.pdf --translator-args-no-json`                                                                   | Do not use JSON string for translation engine arguments.                                                              |
| `--translator-args-no-yaml`     | Do not use YAML string for translation engine arguments                                  | `pdf2zh_next example.pdf --translator-args-no-yaml`                                                                   | Do not use YAML string for translation engine arguments.                                                              |
| `--translator-args-no-toml`     | Do not use TOML string for translation engine arguments                                  | `pdf2zh_next example.pdf --translator-args-no-toml`                                                                   | Do not use TOML string for translation engine arguments.                                                              |
| `--translator-args-no-ini`      | Do not use INI string for translation engine arguments                                   | `pdf2zh_next example.pdf --translator-args-no-ini`                                                                    | Do not use INI string for translation engine arguments.                                                               |
| `--translator-args-no-cli`      | Do not use command line arguments for translation engine arguments                       | `pdf2zh_next example.pdf --translator-args-no-cli`                                                                    | Do not use command line arguments for translation engine arguments.                                                   |
| `--translator-args-cli`         | Command line arguments for translation engine arguments                                  | `pdf2zh_next example.pdf --translator-args-cli`                                                                       | Command line arguments for translation engine arguments.                                                              |
| `--translator-args-cli-prefix`  | Command line argument prefix for translation engine arguments                            | `pdf2zh_next example.pdf --translator-args-cli-prefix PDF2ZH_`                                                        | Command line argument prefix for translation engine arguments.                                                        |
| `--translator-args-cli-sep`     | Command line argument separator for translation engine arguments                         | `pdf2zh_next example.pdf --translator-args-cli-sep _`                                                                 | Command line argument separator for translation engine arguments.                                                     |
| `--translator-args-cli-no-prefix` | Do not use command line argument prefix for translation engine arguments                 | `pdf2zh_next example.pdf --translator-args-cli-no-prefix`                                                             | Do not use command line argument prefix for translation engine arguments.                                              |
| `--translator-args-cli-no-sep`  | Do not use command line argument separator for translation engine arguments              | `pdf2zh_next example.pdf --translator-args-cli-no-sep`                                                                | Do not use command line argument separator for translation engine arguments.                                           |
| `--translator-args-cli-no-merge` | Do not merge command line arguments for translation engine arguments                     | `pdf2zh_next example.pdf --translator-args-cli-no-merge`                                                              | Do not merge command line arguments for translation engine arguments.                                                  |
| `--translator-args-cli-no-override` | Do not override command line arguments for translation engine arguments                  | `pdf2zh_next example.pdf --translator-args-cli-no-override`                                                           | Do not override command line arguments for translation engine arguments.                                               |
| `--translator-args-cli-no-default` | Do not use default command line arguments for translation engine arguments               | `pdf2zh_next example.pdf --translator-args-cli-no-default`                                                            | Do not use default command line arguments for translation engine arguments.                                            |
| `--translator-args-cli-no-env`  | Do not use environment variables for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-no-env`                                                                | Do not use environment variables for command line arguments for translation engine arguments.                          |
| `--translator-args-cli-no-file` | Do not use file for command line arguments for translation engine arguments              | `pdf2zh_next example.pdf --translator-args-cli-no-file`                                                               | Do not use file for command line arguments for translation engine arguments.                                           |
| `--translator-args-cli-no-json` | Do not use JSON string for command line arguments for translation engine arguments       | `pdf2zh_next example.pdf --translator-args-cli-no-json`                                                               | Do not use JSON string for command line arguments for translation engine arguments.                                    |
| `--translator-args-cli-no-yaml` | Do not use YAML string for command line arguments for translation engine arguments       | `pdf2zh_next example.pdf --translator-args-cli-no-yaml`                                                               | Do not use YAML string for command line arguments for translation engine arguments.                                    |
| `--translator-args-cli-no-toml` | Do not use TOML string for command line arguments for translation engine arguments       | `pdf2zh_next example.pdf --translator-args-cli-no-toml`                                                               | Do not use TOML string for command line arguments for translation engine arguments.                                    |
| `--translator-args-cli-no-ini`  | Do not use INI string for command line arguments for translation engine arguments        | `pdf2zh_next example.pdf --translator-args-cli-no-ini`                                                                | Do not use INI string for command line arguments for translation engine arguments.                                     |
| `--translator-args-cli-no-cli`  | Do not use command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-no-cli`                                                                | Do not use command line arguments for command line arguments for translation engine arguments.                         |
| `--translator-args-cli-cli`     | Command line arguments for command line arguments for translation engine arguments       | `pdf2zh_next example.pdf --translator-args-cli-cli`                                                                   | Command line arguments for command line arguments for translation engine arguments.                                    |
| `--translator-args-cli-cli-prefix` | Command line argument prefix for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-prefix PDF2ZH_`                                                    | Command line argument prefix for command line arguments for translation engine arguments.                              |
| `--translator-args-cli-cli-sep` | Command line argument separator for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cl 极速-cli-sep _`                                                          | Command line argument separator for command line arguments for translation engine arguments.                           |
| `--translator-args-cli-cli-no-prefix` | Do not use command line argument prefix for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-prefix`                                                         | Do not use command line argument prefix for command line arguments for translation engine arguments.                   |
| `--transl 极速-cli-cli-no-sep`   | Do not use command line argument separator for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-sep`                                                            | Do not use command line argument separator for command line arguments 极速 translation engine arguments.                |
| `--translator-args-cli-cli-no-merge` | Do not merge command line arguments for command line arguments for translation engine arguments | `pdf 极速_next example.pdf --translator-args-cli-cli-no-merge`                                                         | Do not merge command line arguments for command line arguments for translation engine arguments.                       |
| `--translator-args-cli-cli-no-override` | Do not override command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-override`                                                       | Do not override command line arguments for command line arguments for translation engine arguments.                    |
| `--translator-args-cli-cli-no-default` | Do not use default command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-default`                                                        | Do not use default command line arguments for command line arguments for translation engine arguments.                 |
| `--translator-args-cli-cli-no-env` | Do not use environment variables for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-env`                                                            | Do not use environment variables for command line arguments for command line arguments for translation engine arguments. |
| `--translator-args-cli-cli-no-file` | Do not use file for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli 极速-cli-no-file`                                                       | Do not use file for command line arguments for command line arguments for translation engine arguments.                |
| `--translator-args-cli-cli-no-json` | Do not use JSON string for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-json`                                                           | Do not use JSON string for command line arguments for command line arguments for translation engine arguments.         |
| `--translator-args-cli-cli-no-yaml` | Do not use YAML string for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-yaml`                                                          极速 Do not use YAML string for command line arguments for command line arguments for translation engine arguments.         |
| `--translator-args-cli-cli-no-toml` | Do not use TOML string for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-toml`                                                           | Do not use TOML string for command line arguments for command line arguments for translation engine arguments.         |
| `--translator-args-cli-cli-no-ini` | Do not use INI string for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-in 极速`                                                         | Do not use INI string for command line arguments for command line arguments for translation engine arguments.          |
| `--translator-args-cli-cli-no-cli` | Do not use command line arguments for command line arguments for command line arguments for translation engine arguments | `pdf2zh_next example.pdf --translator-args-cli-cli-no-cli`                                                            | Do not use command line arguments for command line arguments for command line arguments for translation engine arguments. |

---

### OUTPUT

| `--lang-in`                     | 소스 언어 코드                                                                          | `pdf2zh_next example.pdf --lang-in en`                                                                                | 소스 문서의 언어 코드입니다. 지정하지 않으면 언어가 자동으로 감지됩니다.                                           |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--lang-out`                    | 대상 언어 코드                                                                          | `pdf2zh_next example.pdf --lang-out ko`                                                                               | 대상 문서의 언어 코드입니다.                                                                                         |
| `--engine`                      | 번역 엔진                                                                               | `pdf2zh_next example.pdf --engine openai`                                                                             | 사용할 번역 엔진입니다. 현재 지원되는 엔진: `openai`, `google`, `azure`, `youdao`, `deepl`, `gemini`.                  |
| `--translator-args`             | 번역 엔진 인수                                                                          | `pdf2zh_next example.pdf --translator-args '{"api_key": "your-api-key"}'`                                             | 번역 엔진의 인수입니다.                                                                                              |
| `--translator 极速-file`        | 번역 엔진 인수 파일 경로                                                                | `pdf2zh_next example.pdf --translator-args-file args.json`                                                            | 번역 엔진 인수의 파일 경로입니다.                                                                                    |
| `--translator-args-env-prefix`  | 번역 엔진 인수를 위한 환경 변수 접두사                                                  | `pdf2zh_next example.pdf --translator-args-en 极速-prefix PDF2ZH_`                                                     | 번역 엔진 인수를 위한 환경 변수 접두사입니다.                                                                        |
| `--translator-args-json`        | 번역 엔진 인수의 JSON 문자열                                                            | `pdf2zh_next example.pdf --translator-args-json '{"api_key": "your-api-key"}'`                                        | 번역 엔진 인수의 JSON 문자열입니다.                                                                                  |
| `--translator-args-yaml`        | 번역 엔진 인수의 YAML 문자열                                                            | `pdf2zh_next example.pdf --translator-args-yaml 'api_key: your-api-key'`                                              | 번역 엔진 인수의 YAML 문자열입니다.                                                                                  |
| `--translator-args-toml`        | 번역 엔진 인수의 TOML 문자열                                                            | `pdf2zh_next example.pdf --translator-args-toml 'api_key = "your-api-key"'`                                           | 번역 엔진 인수의 TOML 문자열입니다.                                                                                  |
| `--translator-args-ini`         | 번역 엔진 인수의 INI 문자열                                                             | `pdf2zh_next example.pdf --translator-args-ini 'api_key=your-api-key 极速`                                             | 번역 엔진 인수의 INI 문자열입니다.                                                                                   |
| `--translator-args-env`         | 번역 엔진 인수를 위한 환경 변수 이름                                                    | `极速 2zh_next example.pdf --translator-args-env API_KEY`                                                              | 번역 엔진 인수를 위한 환경 변수 이름입니다.                                                                          |
| `--translator-args-default`     | 번역 엔진 기본 인수                                                                     | `pdf2zh_next example.pdf --translator-args-default`                                                                   | 번역 엔진의 기본 인수입니다.                                                                                         |
| `--translator-args-override`    | 번역 엔진 재정의 인수                                                                   | `pdf2zh_next example.pdf --translator-args-override`                                                                  | 번역 엔진의 재정의 인수입니다.                                                                                       |
| `--translator-args-merge`       | 번역 엔진 병합 인수                                                                     | `pdf2zh_next example.pdf --translator-args-merge`                                                                     | 번역 엔진의 병합 인수입니다.                                                                                         |
| `--translator-args-deep-merge`  | 번역 엔진 심층 병합 인수                                                                | `pdf2zh_next example.pdf --translator-args-deep-merge`                                                                | 번역 엔진의 심층 병합 인수입니다.                                                                                    |
| `--translator-args-no-merge`    | 번역 엔진 인수 병합 안 함                                                               | `pdf2zh_next example.pdf --translator-args-no-merge`                                                                  | 번역 엔진 인수의 병합을 사용하지 않습니다.                                                                           |
| `--translator-args-no-override` | 번역 엔진 인수 재정의 안 함                                                             | `pdf2zh_next example.pdf --translator-args-no-override`                                                               | 번역 엔진 인수의 재정의를 사용하지 않습니다.                                                                         |
| `--translator-args-no-default`  | 번역 엔진 기본 인수 사용 안 함                                                          | `pdf2zh_next example.pdf --translator-args-no-default`                                                                | 번역 엔진의 기본 인수를 사용하지 않습니다.                                                                           |
| `--translator-args-no-env`      | 번역 엔진 인수를 위한 환경 변수 사용 안 함                                              | `pdf2zh_next example.pdf --translator-args-no-env`                                                                    | 번역 엔진 인수를 위한 환경 변수를 사용하지 않습니다.                                                                 |
| `--translator-args-no-file`     | 번역 엔진 인수를 위한 파일 사용 안 함                                                   | `pdf2zh_next example.pdf --translator-args-no-file`                                                                   | 번역 엔진 인수를 위한 파일을 사용하지 않습니다.                                                                      |
| `--translator-args-no-极速`     | 번역 엔진 인수를 위한 JSON 문자열 사용 안 함                                            | `pdf2zh_next example.pdf --translator-args-no-json`                                                                   | 번역 엔진 인수를 위한 JSON 문자열을 사용하지 않습니다.                                                               |
| `--translator-args-no-yaml`     | 번역 엔진 인수를 위한 YAML 문자열 사용 안 함                                            | `pdf2zh_next example.pdf --translator-args-no-yaml`                                                                   | 번역 엔진 인수를 위한 YAML 문자열을 사용하지 않습니다.                                                               |
| `--translator-args-no-toml 极速` | 번역 엔진 인수를 위한 TOML 문자열 사용 안 함                                            | `pdf2zh_next example.pdf --translator-args-no-toml`                                                                   | 번역 엔진 인수를 위한 TOML 문자열을 사용하지 않습니다.                                                               |
| `--translator-args-no-ini`      | 번역 엔진 인수를 위한 INI 문자열 사용 안 함                                             | `pdf2zh_next example.pdf --translator-args-no-ini`                                                                    | 번역 엔진 인수를 위한 INI 문자열을 사용하지 않습니다.                                                                |
| `--translator-args-no-cli`      | 번역 엔진 인수를 위한 명령줄 인수 사용 안 함                                            | `pdf2zh_next example.pdf --translator-args-no-cli`                                                                    | 번역 엔진 인수를 위한 명령줄 인수를 사용하지 않습니다.                                                               |
| `--translator-args-cli`         | 번역 엔진 인수를 위한 명령줄 인수                                                       | `pdf2zh_next example.pdf --translator-args-cli`                                                                       | 번역 엔진 인수를 위한 명령줄 인수입니다.                                                                            |
| `--translator-args-cli-prefix`  | 번역 엔진 인수를 위한 명령줄 인수 접두사                                                | `pdf2zh_next example.pdf --translator-args-cli-prefix PDF2ZH_`                                                        | 번역 엔진 인수를 위한 명령줄 인수 접두사입니다.                                                                     |
| `--translator-args-cli-sep`     | 번역 엔진 인수를 위한 명령줄 인수 구분자                                                | `pdf2zh_next example.pdf --translator-args-cli-sep _`                                                                 | 번역 엔진 인수를 위한 명령줄 인수 구분자입니다.                                                                     |
| `--translator-args-cli-no-prefix` | 번역 엔진 인수를 위한 명령줄 인수 접두사 사용 안 함                                     | `pdf2zh_next example.pdf --translator-args-cli-no-prefix`                                                             | 번역 엔진 인수를 위한 명령줄 인수 접두사를 사용하지 않습니다.                                                       |
| `--translator-args-cli-no-sep`  | 번역 엔진 인수를 위한 명령줄 인수 구분자 사용 안 함                                     | `pdf2zh_next example.pdf --translator-args-cli-no-se 极速`                                                             | 번역 엔진 인수를 위한 명령줄 인수 구분자를 사용하지 않습니다.                                                       |
| `--translator-args-cli-no-merge` | 번역 엔진 인수를 위한 명령줄 인수 병합 안 함                                            | `pdf2zh_next example.pdf --translator-args-cli-no-merge`                                                              | 번역 엔진 인수를 위한 명령줄 인수의 병합을 사용하지 않습니다.                                                       |
| `--translator-args-cli-no-override` | 번역 엔진 인수를 위한 명령줄 인수 재정의 안 함                                          | `pdf2zh_next example.pdf --translator-args-cli-no-override`                                                           | 번역 엔진 인수를 위한 명령줄 인수의 재정의를 사용하지 않습니다.                                                     |
| `--translator-args-cli-no-default` | 번역 엔진 인수를 위한 기본 명령줄 인수 사용 안 함                                       | `pdf2zh_next example.pdf --translator-args-cli-no-default`                                                            | 번역 엔진 인수를 위한 기본 명령줄 인수를 사용하지 않습니다.                                                         |
| `--translator-args-cli-no-env`  | 번역 엔진 인수를 위한 명령줄 인수의 환경 변수 사용 안 함                                | `pdf2zh_next example.pdf --translator-args-cli-no-env`                                                                | 번역 엔진 인수를 위한 명령줄 인수의 환경 변수를 사용하지 않습니다.                                                   |
| `--translator-args-cli-no-file` | 번역 엔진 인수를 위한 명령줄 인수의 파일 사용 안 함                                     | `pdf2zh_next example.pdf --translator-args-cli-no-file`                                                               | 번역 엔진极速를 위한 명령줄 인수의 파일을 사용하지 않습니다.                                                        |
| `--translator-args-cli-no-json` | 번역 엔진 인수를 위한 명령줄 인수의 JSON 문자열 사용 안 함                              | `pdf2zh_next example.pdf --translator-args-cli-no-json`                                                               | 번역 엔진 인수를 위한 명령줄 인수의 JSON 문자열을 사용하지 않습니다.                                                 |
| `--translator-args-cli-no-yaml` | 번역 엔진 인수를 위한 명령줄 인수의 YAML 문자열 사용 안 함                              | `pdf2zh_next example.pdf --translator-args-cli-no-yaml`                                                               | 번역 엔진 인수를 위한 명령줄 인수의 YAML 문자열을 사용하지 않습니다.                                                 |
| `--translator-args-cli-no-toml` | 번역 엔진 인수를 위한 명령줄 인수의 TOML 문자열 사용 안 함                              | `pdf2zh_next example.pdf --translator-args-cli-no-toml`                                                               | 번역 엔진 인수를 위한 명령줄 인수의 TOML 문자열을 사용하지 않습니다.                                                 |
| `--translator-args-cli-no-ini`  | 번역 엔진 인수를 위한 명령줄 인수의 INI 문자열 사용 안 함                               | `pdf2zh_next example.pdf --translator-args-cli-no-ini`                                                                | 번역 엔진 인수를 위한 명령줄 인수의 INI 문자열을 사용하지 않습니다.                                                  |
| `--translator-args-cli-no-cli`  | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 사용 안 함                              | `pdf2zh_next example.pdf --translator-args-cli-no-cli`                                                                | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수를 사용하지 않습니다.                                                 |
| `--translator-args-cli-cli`     | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수                                         | `pdf2zh_next example.pdf --translator-args-cli-cli`                                                                   | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수입니다.                                                              |
| `--translator-args-cli-cli-prefix` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 접두사                                 | `pdf2zh_next example.pdf --translator-args-cli-cli-prefix PDF2ZH_`                                                    | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 접두사입니다.                                                       |
| `--translator-args-cli-cli-sep` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인极速 구분자                                | `pdf2zh_next example.pdf --translator-args-cli-cli-sep _`                                                             | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 구분자입니다.                                                       |
| `--translator-args-cli-cli-no-prefix` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 접두사 사용 안 함                      | `pdf2zh_next example.pdf --translator-args-cli-cl 极速-no-prefix`                                                      | 번역 엔진 인수를 위한 명령줄 인수의 명령极速 인수 접두사를 사용하지 않습니다.                                      |
| `--translator-args-cli-cli-no-sep` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 구분자 사용 안 함                      | `pdf2zh_next example.pdf --translator-args-cli-cli-no-sep`                                                            | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 구분자를 사용하지 않습니다.                                         |
| `--translator-args-cli-cli-no-merge` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 병합 안 함                             | `pdf2zh_next example.pdf --translator-args-cli-cli-no-merge`                                                          | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 병합을 사용하지 않습니다.                                           |
| `--translator-args-cli-cli-no-override` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 재정의 안 함                           | `pdf2zh_next example.pdf --translator-args-cli-cli-no-override`                                                       | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수 재정의를 사용하지 않습니다.                                         |
| `--translator-args-cli-cli-no-default` | 번역 엔진 인수를 위한 명령줄 인수의 기본 명령줄 인수 사용 안 함                        | `pdf2zh_next example.pdf --translator-args-cli-cli-no-default`                                                        | 번역 엔진 인수를 위한 명령줄 인수의 기본 명령줄 인수를 사용하지 않습니다.                                           |
| `--translator-args-cli-cli-no-env` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 환경 변수 사용 안 함                 | `pdf2zh_next example.pdf --translator-args-cli-cli-no-env`                                                            | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 환경 변수를 사용하지 않습니다.                                     |
| `--translator-args-cli-cli-no-file` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 파일 사용 안 함                      | `pdf2zh_next example.pdf --translator-args-cli-cli-no-file`                                                           | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 파일을 사용하지 않습니다.                                         |
| `--translator-args-cli-cli-no-json` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 JSON 문자열 사용 안 함              | `pdf2zh_next example.pdf --translator-args-cli-cli-no-json`                                                           | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 JSON 문자열을 사용하지 않습니다.                                   |
| `--translator-args-cli-cli-no-yaml` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 YAML 문자열 사용 안 함              | `pdf2zh_next example.pdf --translator-args-cli-cli-no-yaml`                                                           | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 YAML 문자열을 사용하지 않습니다.                                   |
| `--translator-args-cli-cli-no-toml` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 TOML 문자열 사용 안 함              | `pdf2zh_next example.pdf --translator-args-cli-cli-no-toml`                                                           | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 TOML 문자열을 사용하지 않습니다.                                   |
| `--translator-args-cli-cli-no-ini` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 INI 문자열 사용 안 함               | `pdf2zh_next example.pdf --translator-args-cli-cli-no-ini`                                                            | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 INI 문자열을 사용하지 않습니다.                                    |
| `--translator-args-cli-cli-no-cli` | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 명령줄 인수 사용 안 함              | `pdf2zh_next example.pdf --translator-args-cli-cli-no-cli`                                                            | 번역 엔진 인수를 위한 명령줄 인수의 명령줄 인수의 명령줄 인수를 사용하지 않습니다.                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-engine`                  | OCR engine to use. Default is `easyocr`                                                 | `pdf2zh_next example.pdf --ocr-engine paddleocr`                                                                      |
| `--ocr-lang`                    | Language for OCR. Default is `en,ch_sim`                                                | `pdf2zh_next example.pdf --ocr-lang en,ch_sim`                                                                        |
| `--ocr-whitelist`               | Whitelist characters for OCR. Default is empty                                          | `pdf2zh_next example.pdf --ocr-whitelist "0123456789"`                                                                |
| `--ocr-max-workers`             | Maximum number of workers for OCR. Default is 4                                         | `pdf2zh_next example.pdf --ocr-max-workers 8`                                                                         |
| `--ocr-gpu-offload`             | Enable GPU offload for OCR. Default is `true`                                           | `pdf2zh_next example.pdf --ocr-gpu-offload false`                                                                     |
| `--translator`                  | Translation service. Default is `google`                                                | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-api-key`          | API key for translation service                                                         | `pdf2zh_next example.pdf --translator-api-key "YOUR_API_KEY"`                                                         |
| `--translator-api-url`          | API URL for translation service. Default is based on the service                        | `pdf2zh_next example.pdf --translator-api-url "https://api.deepl.com/v2/translate"`                                   |
| `--translator-max-workers`      | Maximum number of workers for translation. Default is 4                                 | `pdf2zh_next example.pdf --translator-max-workers 8`                                                                  |
| `--translator-request-interval` | Interval between translation requests in milliseconds. Default is 1000                  | `pdf2zh_next example.pdf --translator-request-interval 500`                                                           |
| `--translator-retry-attempts`   | Number of retry attempts for translation. Default is 3                                  | `pdf2zh_next example.pdf --translator-retry-attempts 5`                                                               |
| `--translator-timeout`          | Timeout for translation requests in seconds. Default is 30                              | `pdf2zh_next example.pdf --translator-timeout 60`                                                                     |
| `--translator-proxy`            | Proxy for translation requests                                                          | `pdf2zh_next example.pdf --translator-proxy "http://127.0.0.1:7890"`                                                  |
| `--translator-fallback`         | Fallback translation service if the primary fails. Default is `google`                  | `pdf2zh_next example.pdf --translator-fallback bing`                                                                  |
| `--translator-format`           | Format of text for translation. Default is `html`                                       | `pdf2zh_next example.pdf --translator-format text`                                                                    |
| `--font-family`                 | Font family for the output PDF. Default is `SimSun`                                     | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `--font-size`                   | Font size for the output PDF. Default is 10                                             | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing`                | Line spacing for the output PDF. Default is 1.2                                         | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--char-spacing`                | Character spacing for the output PDF. Default is 0                                      | `pdf2zh_next example.pdf --char-spacing 0.5`                                                                          |
| `--margin`                      | Margin for the output PDF in points. Default is 36                                       | `pdf2zh_next example.pdf --margin 72`                                                                                 |
| `--output`                      | Output file path. Default is `{original_filename}_translated.pdf`                       | `pdf2zh_next example.pdf --output "translated_example.pdf"`                                                           |
| `--output-format`               | Output format. Can be `pdf` or `markdown`. Default is `pdf`                             | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--markdown-output`             | Output file path for markdown. Default is `{original_filename}_translated.md`           | `pdf2zh_next example.pdf --markdown-output "translated_example.md"`                                                   |
| `--debug`                       | Enable debug mode. Default is `false`                                                   | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--verbose`                     | Enable verbose output. Default is `false`                                               | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT

| `--lang-out`                    | 대상 언어 코드                                                                          | `pdf2zh_next example.pdf --lang-out zh-CN`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--ocr-engine`                  | 사용할 OCR 엔진. 기본값은 `easyocr`                                                     | `pdf2zh_next example.pdf --ocr-engine paddleocr`                                                                      |
| `--ocr-lang`                    | OCR 언어. 기본값은 `en,ch_sim`                                                          | `pdf2zh_next example.pdf --ocr-lang en,ch_sim`                                                                        |
| `--ocr-whitelist`               | OCR 화이트리스트 문자. 기본값은 비어 있음                                               | `pdf2zh_next example.pdf --ocr-whitelist "0123456789"`                                                                |
| `--ocr-max-workers`             | OCR 최대 작업자 수. 기본값은 4                                                          | `pdf2zh_next example.pdf --ocr-max-workers 8`                                                                         |
| `--ocr-gpu-offload`             | OCR GPU 오프로드 활성화. 기본값은 `true`                                                | `pdf2zh_next example.pdf --ocr-gpu-offload false`                                                                     |
| `--translator`                  | 번역 서비스. 기본값은 `google`                                                          | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-api-key`          | 번역 서비스 API 키                                                                      | `pdf2zh_next example.pdf --translator-api-key "YOUR_API_KEY"`                                                         |
| `--translator-api-url`          | 번역 서비스 API URL. 기본값은 서비스에 따라 다름                                        | `pdf2zh_next example.pdf --translator-api-url "https://api.deepl.com/v2/translate"`                                   |
| `--translator-max-workers`      | 번역 최대 작업자 수. 기본값은 4                                                         | `pdf2zh_next example.pdf --translator-max-workers 8`                                                                  |
| `--translator-request-interval` | 번역 요청 간 간격 (밀리초). 기본값은 1000                                               | `pdf2zh_next example.pdf --translator-request-interval 500`                                                           |
| `--translator-retry-attempts`   | 번역 재시도 횟수. 기본값은 3                                                            | `pdf2zh_next example.pdf --translator-retry-attempts 5`                                                               |
| `--translator-timeout`          | 번역 요청 타임아웃 (초). 기본값은 30                                                    | `pdf2zh_next example.pdf --translator-timeout 60`                                                                     |
| `--translator-proxy`            | 번역 요청 프록시                                                                        | `pdf2zh_next example.pdf --translator-proxy "http://127.0.0.1:7890"`                                                  |
| `--translator-fallback`         | 기본 번역 서비스 실패 시 사용할 폴백 번역 서비스. 기본값은 `google`                      | `pdf2zh_next example.pdf --translator-fallback bing`                                                                  |
| `--translator-format`           | 번역용 텍스트 형식. 기본값은 `html`                                                     | `pdf2zh_next example.pdf --translator-format text`                                                                    |
| `--font-family`                 | 출력 PDF 글꼴 패밀리. 기본값은 `SimSun`                                                 | `pdf2zh_next example.pdf --font-family "Noto Sans SC"`                                                                |
| `--font-size`                   | 출력 PDF 글꼴 크기. 기본값은 10                                                         | `pdf2zh_next example.pdf --font-size 12`                                                                              |
| `--line-spacing`                | 출력 PDF 줄 간격. 기본값은 1.2                                                          | `pdf2zh_next example.pdf --line-spacing 1.5`                                                                          |
| `--char-spacing`                | 출력 PDF 문자 간격. 기본값은 0                                                          | `pdf2zh_next example.pdf --char-spacing 0.5`                                                                          |
| `--margin`                      | 출력 PDF 여백 (포인트). 기본값은 36                                                     | `pdf2zh_next example.pdf --margin 72`                                                                                 |
| `--output`                      | 출력 파일 경로. 기본값은 `{original_filename}_translated.pdf`                           | `pdf2zh_next example.pdf --output "translated_example.pdf"`                                                           |
| `--output-format`               | 출력 형식. `pdf` 또는 `markdown` 가능. 기본값은 `pdf`                                   | `pdf2zh_next example.pdf --output-format markdown`                                                                    |
| `--markdown-output`             | 마크다운 출력 파일 경로. 기본값은 `{original_filename}_translated.md`                   | `pdf2zh_next example.pdf --markdown-output "translated_example.md"`                                                   |
| `--debug`                       | 디버그 모드 활성화. 기본값은 `false`                                                    | `pdf2zh_next example.pdf --debug`                                                                                     |
| `--verbose`                     | 자세한 출력 활성화. 기본값은 `false`                                                    | `pdf2zh_next example.pdf --verbose`                                                                                   |
| `--help`                        | 도움말 메시지 표시                                                                      | `pdf2zh_next --help`                                                                                                  |
`0`    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------ |
| `--max-text-length`             | Maximum text length to translate                                                        | `pdf2zh_next example.pdf --max-text-length 500`                                                                       | `1000` |
| `--text-length-ratio-limit`     | Limit for text length ratio between original and translated text                       | `pdf2zh_next example.pdf --text-length-ratio-limit 2.0`                                                               | `2.0`  |
| `--text-similarity-threshold`   | Threshold for text similarity to determine if translation is needed                     | `pdf2zh_next example.pdf --text-similarity-threshold 0.9`                                                             | `0.9`  |
| `--batch-size`                  | Number of texts to process in each batch                                                | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `10`   |
| `--request-interval`            | Interval between requests in milliseconds                                               | `pdf2zh_next example.pdf --request-interval 1000`                                                                     | `1000` |
| `--request-timeout`             | Timeout for each request in milliseconds                                                | `pdf2zh_next example.pdf --request-timeout 30000`                                                                     | `30000`|
| `--max-retries`                 | Maximum number of retries for failed requests                                           | `pdf2zh_next example.pdf --max-retries 3`                                                                             | `3`    |
| `--exclude-elements`            | Exclude specific elements from translation (e.g., code, math)                           | `pdf2zh_next example.pdf --exclude-elements code,math`                                                                | `None` |
| `--include-only-elements`       | Include only specific elements for translation (e.g., text)                             | `pdf2zh_next example.pdf --include-only-elements text`                                                                | `None` |
| `--line-break-strategy`         | Strategy for handling line breaks (`preserve`, `remove`, `single`)                     | `pdf2zh_next example.pdf --line-break-strategy preserve`                                                              | `None` |
| `--preserve-formatting`         | Preserve formatting tags (e.g., `<b>`, `<i>`) in the output                             | `pdf2zh_next example.pdf --preserve-formatting`                                                                       | `False`|
| `--formula-detection-strategy`  | Strategy for detecting formulas (`aggressive`, `conservative`)                          | `pdf2zh_next example.pdf --formula-detection-strategy aggressive`                                                     | `conservative` |
| `--formula-translation-strategy`| Strategy for translating formulas (`ignore`, `placeholder`, `translate`)                | `pdf2zh_next example.pdf --formula-translation-strategy placeholder`                                                  | `ignore` |
| `--table-translation-strategy`  | Strategy for translating tables (`markdown`, `html`, `text`)                            | `pdf2zh_next example.pdf --table-translation-strategy markdown`                                                       | `markdown` |
| `--url-translation-strategy`    | Strategy for translating URLs (`ignore`, `translate`)                                   | `pdf2zh_next example.pdf --url-translation-strategy ignore`                                                           | `ignore` |
| `--title-detection-enhancement` | Enhance title detection in the document                                                 | `pdf2zh_next example.pdf --title-detection-enhancement`                                                               | `False`|
| `--context-window-size`         | Size of the context window for improving translation quality                            | `pdf2zh_next example.pdf --context-window-size 3`                                                                     | `3`    |
| `--cache-translations`          | Cache translations to avoid re-translating the same text                                 | `pdf2zh_next example.pdf --cache-translations`                                                                        | `False`|
| `--cache-file`                  | File path for caching translations                                                      | `pdf2zh_next example.pdf --cache-file ./translation_cache.json`                                                       | `None` |
| `--log-level`                   | Log level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)                            | `pdf2zh_next example.pdf --log-level INFO`                                                                            | `INFO` |
| `--save-log`                    | Save log to a file                                                                      | `pdf2zh_next example.pdf --save-log`                                                                                  | `False`|
| `--log-file`                    | File path for saving logs                                                               | `pdf2zh_next example.pdf --log-file ./translation.log`                                                                | `None` |
| `--progress-bar`                | Show progress bar during translation                                                    | `pdf2zh_next example.pdf --progress-bar`                                                                              | `True` |
| `--config-file`                 | Path to a configuration file                                                            | `pdf2zh_next example.pdf --config-file ./config.json`                                                                 | `None` |

---

### TRANSLATION RESULT

| `--min-text-length`             | 번역할 최소 텍스트 길이                                                                 | `pdf2zh_next example.pdf --min-text-length 5`                                                                         | `0`    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------ |
| `--max-text-length`             | 번역할 최대 텍스트 길이                                                                 | `pdf2zh_next example.pdf --max-text-length 500`                                                                       | `1000` |
| `--text-length-ratio-limit`     | 원본 텍스트와 번역된 텍스트 간의 텍스트 길이 비율 제한                                  | `pdf2zh_next example.pdf --text-length-ratio-limit 2.0`                                                               | `2.0`  |
| `--text-similarity-threshold`   | 번역 필요 여부를 결정하기 위한 텍스트 유사도 임계값                                     | `pdf2zh_next example.pdf --text-similarity-threshold 0.9`                                                             | `0.9`  |
| `--batch-size`                  | 각 배치에서 처리할 텍스트 수                                                            | `pdf2zh_next example.pdf --batch-size 10`                                                                             | `10`   |
| `--request-interval`            | 요청 간 간격 (밀리초)                                                                   | `pdf2zh_next example.pdf --request-interval 1000`                                                                     | `1000` |
| `--request-timeout`             | 각 요청에 대한 타임아웃 (밀리초)                                                        | `pdf2zh_next example.pdf --request-timeout 30000`                                                                     | `30000`|
| `--max-retries`                 | 실패한 요청에 대한 최대 재시도 횟수                                                     | `pdf2zh_next example.pdf --max-retries 3`                                                                             | `3`    |
| `--exclude-elements`            | 번역에서 특정 요소 제외 (예: 코드, 수학)                                                | `pdf2zh_next example.pdf --exclude-elements code,math`                                                                | `None` |
| `--include-only-elements`       | 번역을 위해 특정 요소만 포함 (예: 텍스트)                                               | `pdf2zh_next example.pdf --include-only-elements text`                                                                | `None` |
| `--line-break-strategy`         | 줄 바꿈 처리 전략 (`preserve`, `remove`, `single`)                                      | `pdf2zh_next example.pdf --line-break-strategy preserve`                                                              | `None` |
| `--preserve-formatting`         | 출력에서 서식 태그 (예: `<b>`, `<i>`) 보존                                              | `pdf2zh_next example.pdf --preserve-formatting`                                                                       | `False`|
| `--formula-detection-strategy`  | 수식 감지 전략 (`aggressive`, `conservative`)                                           | `pdf2zh_next example.pdf --formula-detection-strategy aggressive`                                                     | `conservative` |
| `--formula-translation-strategy`| 수식 번역 전략 (`ignore`, `placeholder`, `translate`)                                   | `pdf2zh_next example.pdf --formula-translation-strategy placeholder`                                                  | `ignore` |
| `--table-translation-strategy`  | 표 번역 전략 (`markdown`, `html`, `text`)                                               | `pdf2zh_next example.pdf --table-translation-strategy markdown`                                                       | `markdown` |
| `--url-translation-strategy`    | URL 번역 전략 (`ignore`, `translate`)                                                   | `pdf2zh_next example.pdf --url-translation-strategy ignore`                                                           | `ignore` |
| `--title-detection-enhancement` | 문서 내 제목 감지 향상                                                                  | `pdf2zh_next example.pdf --title-detection-enhancement`                                                               | `False`|
| `--context-window-size`         | 번역 품질 향상을 위한 컨텍스트 창 크기                                                  | `pdf2zh_next example.pdf --context-window-size 3`                                                                     | `3`    |
| `--cache-translations`          | 동일한 텍스트 재번역 방지를 위해 번역 캐시                                              | `pdf2zh_next example.pdf --cache-translations`                                                                        | `False`|
| `--cache-file`                  | 번역 캐시를 위한 파일 경로                                                              | `pdf2zh_next example.pdf --cache-file ./translation_cache.json`                                                       | `None` |
| `--log-level`                   | 로그 레벨 (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`)                             | `pdf2zh_next example.pdf --log-level INFO`                                                                            | `INFO` |
| `--save-log`                    | 로그를 파일로 저장                                                                      | `pdf2zh_next example.pdf --save-log`                                                                                  | `False`|
| `--log-file`                    | 로그 저장을 위한 파일 경로                                                              | `pdf2zh_next example.pdf --log-file ./translation.log`                                                                | `None` |
| `--progress-bar`                | 번역 중 진행률 표시줄 표시                                                              | `pdf2zh_next example.pdf --progress-bar`                                                                              | `True` |
| `--config-file`                 | 구성 파일 경로                                                                          | `pdf2zh_next example.pdf --config-file ./config.json`                                                                 | `None` |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--rpc-translation`             | RPC service host address for translation                                                | `pdf2zh_next example.pdf --rpc-translation http://127.0.0.1:8001`                                                      |
| `--rpc-ocr`                     | RPC service host address for OCR                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8002`                                                              |

---

### TRANSLATION RESULT

| `--rpc-doclayout`               | 문서 레이아웃 분석을 위한 RPC 서비스 호스트 주소                                   | `pdf2zh_next example.pdf --rpc-doclayout http://127.0.0.1:8000`                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--rpc-translation`             | 번역을 위한 RPC 서비스 호스트 주소                                                | `pdf2zh_next example.pdf --rpc-translation http://127.0.0.1:8001`                                                      |
| `--rpc-ocr`                     | OCR 을 위한 RPC 서비스 호스트 주소                                                        | `pdf2zh_next example.pdf --rpc-ocr http://127.0.0.1:8002`                                                              |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--max-characters`              | Maximum number of characters per request for translation service                        | `pdf2zh_next example.pdf --max-characters 2000`                                                                       |
| `--max-workers`                 | Maximum number of concurrent workers for translation service                            | `pdf2zh_next example.pdf --max-workers 20`                                                                            |
| `--service`                     | Translation service to use (e.g., `google`, `openai`, `azure`, `deepl`, `youdao`, etc.) | `pdf2zh_next example.pdf --service google`                                                                            |
| `--service-url`                 | Custom URL for translation service (for self-hosted services)                           | `pdf2zh_next example.pdf --service-url "https://your-translation-service.com/translate"`                              |
| `--service-key`                 | API key for translation service (if required)                                           | `pdf2zh_next example.pdf --service-key "your-api-key"`                                                                |
| `--service-region`              | Region for translation service (if required, e.g., Azure)                               | `pdf2zh_next example.pdf --service-region "eastus"`                                                                   |
| `--glossary`                    | Path to a glossary file for translation service                                         | `pdf2zh_next example.pdf --glossary "./glossary.txt"`                                                                 |
| `--formality`                   | Formality level for translation service (e.g., `more`, `less`, `prefer_more`, `prefer_less`) | `pdf2zh_next example.pdf --formality more`                                                                        |
| `--split-sentences`             | How to split sentences for translation service (e.g., `none`, `punctuation`, `newlines`) | `pdf2zh_next example.pdf --split-sentences punctuation`                                                               |
| `--preserve-formatting`         | Whether to preserve formatting in translation service (e.g., `true`, `false`)           | `pdf2zh_next example.pdf --preserve-formatting true`                                                                  |
| `--tag-handling`                | How to handle tags in translation service (e.g., `xml`, `html`)                         | `pdf2zh_next example.pdf --tag-handling xml`                                                                          |
| `--outline-placement`           | How to handle outline placement in translation service (e.g., `before`, `after`)        | `pdf2zh_next example.pdf --outline-placement before`                                                                  |
| `--non-splitting-tags`          | List of non-splitting tags for translation service (comma-separated)                    | `pdf2zh_next example.pdf --non-splitting-tags "p,span"`                                                               |
| `--ignore-tags`                 | List of tags to ignore for translation service (comma-separated)                        | `pdf2zh_next example.pdf --ignore-tags "code,math"`                                                                   |
| `--splitting-tags`              | List of splitting tags for translation service (comma-separated)                        | `pdf2zh_next example.pdf --splitting-tags "p,div"`                                                                    |
| `--timeout`                     | Timeout for translation service requests (in seconds)                                   | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry-attempts`              | Number of retry attempts for failed translation requests                                | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          |
| `--retry-delay`                 | Delay between retry attempts for failed translation requests (in seconds)               | `pdf2zh_next example.pdf --retry-delay 1`                                                                             |
| `--fallback-services`           | Fallback translation services to use if primary fails (comma-separated)                 | `pdf2zh_next example.pdf --fallback-services "google,azure"`                                                          |
| `--fallback-threshold`          | Confidence threshold for fallback (0-1)                                                 | `pdf2zh_next example.pdf --fallback-threshold 0.8`                                                                    |
| `--custom-glossary`             | Custom glossary entries for translation service (comma-separated key:value pairs)       | `pdf2zh_next example.pdf --custom-glossary "term1:translation1,term2:translation2"`                                   |
| `--context`                     | Context for translation service (e.g., "This is a technical document about physics")    | `pdf2zh_next example.pdf --context "This is a technical document about physics"`                                      |
| `--style`                       | Style for translation service (e.g., "formal", "informal")                              | `pdf2zh_next example.pdf --style formal`                                                                              |
| `--domain`                      | Domain for translation service (e.g., "IT", "medical", "legal")                         | `pdf2zh_next example.pdf --domain IT`                                                                                 |

---

### OUTPUT

| `--qps`                         | 번역 서비스의 QPS 제한                                                                  | `pdf2zh_next example.pdf --qps 200`                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--max-characters`              | 번역 서비스 요청당 최대 문자 수                                                          | `pdf2zh_next example.pdf --max-characters 2000`                                                                       |
| `--max-workers`                 | 번역 서비스의 최대 동시 작업자 수                                                        | `pdf2zh_next example.pdf --max-workers 20`                                                                            |
| `--service`                     | 사용할 번역 서비스 (예: `google`, `openai`, `azure`, `deepl`, `youdao` 등)                | `pdf2zh_next example.pdf --service google`                                                                            |
| `--service-url`                 | 번역 서비스의 사용자 정의 URL (자체 호스팅 서비스용)                                      | `pdf2zh_next example.pdf --service-url "https://your-translation-service.com/translate"`                              |
| `--service-key`                 | 번역 서비스의 API 키 (필요한 경우)                                                       | `pdf2zh_next example.pdf --service-key "your-api-key"`                                                                |
| `--service-region`              | 번역 서비스의 지역 (필요한 경우, 예: Azure)                                              | `pdf2zh_next example.pdf --service-region "eastus"`                                                                   |
| `--glossary`                    | 번역 서비스용 용어집 파일 경로                                                           | `pdf2zh_next example.pdf --glossary "./glossary.txt"`                                                                 |
| `--formality`                   | 번역 서비스의 공식성 수준 (예: `more`, `less`, `prefer_more`, `prefer_less`)              | `pdf2zh_next example.pdf --formality more`                                                                        |
| `--split-sentences`             | 번역 서비스를 위한 문장 분할 방식 (예: `none`, `punctuation`, `newlines`)                 | `pdf2zh_next example.pdf --split-sentences punctuation`                                                               |
| `--preserve-formatting`         | 번역 서비스에서 서식을 유지할지 여부 (예: `true`, `false`)                                | `pdf2zh_next example.pdf --preserve-formatting true`                                                                  |
| `--tag-handling`                | 번역 서비스에서 태그 처리 방식 (예: `xml`, `html`)                                       | `pdf2zh_next example.pdf --tag-handling xml`                                                                          |
| `--outline-placement`           | 번역 서비스에서 아웃라인 배치 방식 (예: `before`, `after`)                               | `pdf2zh_next example.pdf --outline-placement before`                                                                  |
| `--non-splitting-tags`          | 번역 서비스용 비분할 태그 목록 (쉼표로 구분)                                             | `pdf2zh_next example.pdf --non-splitting-tags "p,span"`                                                               |
| `--ignore-tags`                 | 번역 서비스에서 무시할 태그 목록 (쉼표로 구분)                                           | `pdf2zh_next example.pdf --ignore-tags "code,math"`                                                                   |
| `--splitting-tags`              | 번역 서비스용 분할 태그 목록 (쉼표로 구분)                                               | `pdf2zh_next example.pdf --splitting-tags "p,div"`                                                                    |
| `--timeout`                     | 번역 서비스 요청의 타임아웃 (초 단위)                                                    | `pdf2zh_next example.pdf --timeout 30`                                                                                |
| `--retry-attempts`              | 실패한 번역 요청의 재시도 횟수                                                           | `pdf2zh_next example.pdf --retry-attempts 3`                                                                          |
| `--retry-delay`                 | 실패한 번역 요청의 재시도 간 지연 시간 (초 단위)                                          | `pdf2zh_next example.pdf --retry-delay 1`                                                                             |
| `--fallback-services`           | 기본 서비스 실패 시 사용할 폴백 번역 서비스 (쉼표로 구분)                                 | `pdf2zh_next example.pdf --fallback-services "google,azure"`                                                          |
| `--fallback-threshold`          | 폴백을 위한 신뢰도 임계값 (0-1)                                                         | `pdf2zh_next example.pdf --fallback-threshold 0.8`                                                                    |
| `--custom-glossary`             | 번역 서비스용 사용자 정의 용어집 항목 (쉼표로 구분된 key:value 쌍)                        | `pdf2zh_next example.pdf --custom-glossary "term1:translation1,term2:translation2"`                                   |
| `--context`                     | 번역 서비스용 컨텍스트 (예: "This is a technical document about physics")                | `pdf2zh_next example.pdf --context "This is a technical document about physics"`                                      |
| `--style`                       | 번역 서비스용 스타일 (예: "formal", "informal")                                          | `pdf2zh_next example.pdf --style formal`                                                                              |
| `--domain`                      | 번역 서비스용 도메인 (예: "IT", "medical", "legal")                                      | `pdf2zh_next example.pdf --domain IT`                                                                                 |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--ignore-file-cache`           | Ignore file cache                                                                       | `pdf2zh_next example.pdf --ignore-file-cache`                                                                         |
| `--ignore-translation-cache`    | Ignore translation cache                                                                | `pdf2zh_next example.pdf --ignore-translation-cache`                                                                  |
| `--ignore-llm-cache`            | Ignore LLM cache                                                                        | `pdf2zh_next example.pdf --ignore-llm-cache`                                                                          |
| `--ignore-ocr-cache`            | Ignore OCR cache                                                                        | `pdf2zh_next example.pdf --ignore-ocr-cache`                                                                          |
| `--ignore-image-cache`          | Ignore image cache                                                                      | `pdf2zh_next example.pdf --ignore-image-cache`                                                                        |
| `--ignore-text-cache`           | Ignore text cache                                                                       | `pdf2zh_next example.pdf --ignore-text-cache`                                                                         |
| `--ignore-pdf-cache`            | Ignore PDF cache                                                                        | `pdf2zh_next example.pdf --ignore-pdf-cache`                                                                          |
| `--ignore-font-cache`           | Ignore font cache                                                                       | `pdf2zh_next example.pdf --ignore-font-cache`                                                                         |
| `--ignore-color-cache`          | Ignore color cache                                                                      | `pdf2zh_next example.pdf --ignore-color-cache`                                                                        |
| `--ignore-layout-cache`         | Ignore layout cache                                                                     | `pdf2zh_next example.pdf --ignore-layout-cache`                                                                       |
| `--ignore-table-cache`          | Ignore table cache                                                                      | `pdf2zh_next example.pdf --ignore-table-cache`                                                                        |
| `--ignore-math-cache`           | Ignore math cache                                                                       | `pdf2zh_next example.pdf --ignore-math-cache`                                                                         |
| `--ignore-equation-cache`       | Ignore equation cache                                                                   | `pdf2zh_next example.pdf --ignore-equation-cache`                                                                     |
| `--ignore-formula-cache`        | Ignore formula cache                                                                    | `pdf2zh_next example.pdf --ignore-formula-cache`                                                                      |
| `--ignore-figure-cache`         | Ignore figure cache                                                                     | `pdf2zh_next example.pdf --ignore-figure-cache`                                                                       |
| `--ignore-graphic-cache`        | Ignore graphic cache                                                                    | `pdf2zh_next example.pdf --ignore-graphic-cache`                                                                      |
| `--ignore-chart-cache`          | Ignore chart cache                                                                      | `pdf2zh_next example.pdf --ignore-chart-cache`                                                                        |
| `--ignore-diagram-cache`        | Ignore diagram cache                                                                    | `pdf2zh_next example.pdf --ignore-diagram-cache`                                                                      |
| `--ignore-vector-cache`         | Ignore vector cache                                                                     | `pdf2zh_next example.pdf --ignore-vector-cache`                                                                       |
| `--ignore-raster-cache`         | Ignore raster cache                                                                     | `pdf2zh_next example.pdf --ignore-raster-cache`                                                                       |
| `--ignore-bitmap-cache`         | Ignore bitmap cache                                                                     | `pdf2zh_next example.pdf --ignore-bitmap-cache`                                                                       |
| `--ignore-image-text-cache`     | Ignore image text cache                                                                 | `pdf2zh_next example.pdf --ignore-image-text-cache`                                                                   |
| `--ignore-text-image-cache`     | Ignore text image cache                                                                 | `pdf2zh_next example.pdf --ignore-text-image-cache`                                                                   |
| `--ignore-pdf-text-cache`       | Ignore PDF text cache                                                                   | `pdf2zh_next example.pdf --ignore-pdf-text-cache`                                                                     |
| `--ignore-text-pdf-cache`       | Ignore text PDF cache                                                                   | `pdf2zh_next example.pdf --ignore-text-pdf-cache`                                                                     |
| `--ignore-pdf-image-cache`      | Ignore PDF image cache                                                                  | `pdf2zh_next example.pdf --ignore-pdf-image-cache`                                                                    |
| `--ignore-image-pdf-cache`      | Ignore image PDF cache                                                                  | `pdf2zh_next example.pdf --ignore-image-pdf-cache`                                                                    |
| `--ignore-pdf-layout-cache`     | Ignore PDF layout cache                                                                 | `pdf2zh_next example.pdf --ignore-pdf-layout-cache`                                                                   |
| `--ignore-layout-pdf-cache`     | Ignore layout PDF cache                                                                 | `pdf2zh_next example.pdf --ignore-layout-pdf-cache`                                                                   |
| `--ignore-pdf-table-cache`      | Ignore PDF table cache                                                                  | `pdf2zh_next example.pdf --ignore-pdf-table-cache`                                                                    |
| `--ignore-table-pdf-cache`      | Ignore table PDF cache                                                                  | `pdf2zh_next example.pdf --ignore-table-pdf-cache`                                                                    |
| `--ignore-pdf-math-cache`       | Ignore PDF math cache                                                                   | `pdf2zh_next example.pdf --ignore-pdf-math-cache`                                                                     |
| `--ignore-math-pdf-cache`       | Ignore math PDF cache                                                                   | `pdf2zh_next example.pdf --ignore-math-pdf-cache`                                                                     |
| `--ignore-pdf-equation-cache`   | Ignore PDF equation cache                                                               | `pdf2zh_next example.pdf --ignore-pdf-equation-cache`                                                                 |
| `--ignore-equation-pdf-cache`   | Ignore equation PDF cache                                                               | `pdf2zh_next example.pdf --ignore-equation-pdf-cache`                                                                 |
| `--ignore-pdf-formula-cache`    | Ignore PDF formula cache                                                                | `pdf2zh_next example.pdf --ignore-pdf-formula-cache`                                                                  |
| `--ignore-formula-pdf-cache`    | Ignore formula PDF cache                                                                | `pdf2zh_next example.pdf --ignore-formula-pdf-cache`                                                                  |
| `--ignore-pdf-figure-cache`     | Ignore PDF figure cache                                                                 | `pdf2zh_next example.pdf --ignore-pdf-figure-cache`                                                                   |
| `--ignore-figure-pdf-cache`     | Ignore figure PDF cache                                                                 | `pdf2zh_next example.pdf --ignore-figure-pdf-cache`                                                                   |
| `--ignore-pdf-graphic-cache`    | Ignore PDF graphic cache                                                                | `pdf2zh_next example.pdf --ignore-pdf-graphic-cache`                                                                  |
| `--ignore-graphic-pdf-cache`    | Ignore graphic PDF cache                                                                | `pdf2zh_next example.pdf --ignore-graphic-pdf-cache`                                                                  |
| `--ignore-pdf-chart-cache`      | Ignore PDF chart cache                                                                  | `pdf2zh_next example.pdf --ignore-pdf-chart-cache`                                                                    |
| `--ignore-chart-pdf-cache`      | Ignore chart PDF cache                                                                  | `pdf2zh_next example.pdf --ignore-chart-pdf-cache`                                                                    |
| `--ignore-pdf-diagram-cache`    | Ignore PDF diagram cache                                                                | `pdf2zh_next example.pdf --ignore-pdf-diagram-cache`                                                                  |
| `--ignore-diagram-pdf-cache`    | Ignore diagram PDF cache                                                                | `pdf2zh_next example.pdf --ignore-diagram-pdf-cache`                                                                  |
| `--ignore-pdf-vector-cache`     | Ignore PDF vector cache                                                                 | `pdf2zh_next example.pdf --ignore-pdf-vector-cache`                                                                   |
| `--ignore-vector-pdf-cache`     | Ignore vector PDF cache                                                                 | `pdf2zh_next example.pdf --ignore-vector-pdf-cache`                                                                   |
| `--ignore-pdf-raster-cache`     | Ignore PDF raster cache                                                                 | `pdf2zh_next example.pdf --ignore-pdf-raster-cache`                                                                   |
| `--ignore-raster-pdf-cache`     | Ignore raster PDF cache                                                                 | `pdf2zh_next example.pdf --ignore-raster-pdf-cache`                                                                   |
| `--ignore-pdf-bitmap-cache`     | Ignore PDF bitmap cache                                                                 | `pdf2zh_next example.pdf --ignore-pdf-bitmap-cache`                                                                   |
| `--ignore-bitmap-pdf-cache`     | Ignore bitmap PDF cache                                                                 | `pdf2zh_next example.pdf --ignore-bitmap-pdf-cache`                                                                   |
| `--ignore-pdf-image-text-cache` | Ignore PDF image text cache                                                             | `pdf2zh_next example.pdf --ignore-pdf-image-text-cache`                                                               |
| `--ignore-image-text-pdf-cache` | Ignore image text PDF cache                                                             | `pdf2zh_next example.pdf --ignore-image-text-pdf-cache`                                                               |
| `--ignore-pdf-text-image-cache` | Ignore PDF text image cache                                                             | `pdf2zh_next example.pdf --ignore-pdf-text-image-cache`                                                               |
| `--ignore-text-image-pdf-cache` | Ignore text image PDF cache                                                             | `pdf2zh_next example.pdf --ignore-text-image-pdf-cache`                                                               |
| `--ignore-pdf-pdf-cache`        | Ignore PDF PDF cache                                                                    | `pdf2zh_next example.pdf --ignore-pdf-pdf-cache`                                                                      |
| `--ignore-pdf-pdf-pdf-cache`    | Ignore PDF PDF PDF cache                                                                | `pdf2zh_next example.pdf --ignore-pdf-pdf-pdf-cache`                                                                  |

---

| `--ignore-cache`                | 번역 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-cache`                                                                              |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--ignore-file-cache`           | 파일 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-file-cache`                                                                         |
| `--ignore-translation-cache`    | 번역 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-translation-cache`                                                                  |
| `--ignore-llm-cache`            | LLM 캐시 무시                                                                           | `pdf2zh_next example.pdf --ignore-llm-cache`                                                                          |
| `--ignore-ocr-cache`            | OCR 캐시 무시                                                                           | `pdf2zh_next example.pdf --ignore-ocr-cache`                                                                          |
| `--ignore-image-cache`          | 이미지 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-image-cache`                                                                        |
| `--ignore-text-cache`           | 텍스트 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-text-cache`                                                                         |
| `--ignore-pdf-cache`            | PDF 캐시 무시                                                                           | `pdf2zh_next example.pdf --ignore-pdf-cache`                                                                          |
| `--ignore-font-cache`           | 폰트 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-font-cache`                                                                         |
| `--ignore-color-cache`          | 색상 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-color-cache`                                                                        |
| `--ignore-layout-cache`         | 레이아웃 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-layout-cache`                                                                       |
| `--ignore-table-cache`          | 테이블 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-table-cache`                                                                        |
| `--ignore-math-cache`           | 수학 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-math-cache`                                                                         |
| `--ignore-equation-cache`       | 방정식 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-equation-cache`                                                                     |
| `--ignore-formula-cache`        | 공식 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-formula-cache`                                                                      |
| `--ignore-figure-cache`         | 그림 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-figure-cache`                                                                       |
| `--ignore-graphic-cache`        | 그래픽 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-graphic-cache`                                                                      |
| `--ignore-chart-cache`          | 차트 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-chart-cache`                                                                        |
| `--ignore-diagram-cache`        | 다이어그램 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-diagram-cache`                                                                      |
| `--ignore-vector-cache`         | 벡터 캐시 무시                                                                          | `pdf2zh_next example.pdf --ignore-vector-cache`                                                                       |
| `--ignore-raster-cache`         | 래스터 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-raster-cache`                                                                       |
| `--ignore-bitmap-cache`         | 비트맵 캐시 무시                                                                        | `pdf2zh_next example.pdf --ignore-bitmap-cache`                                                                       |
| `--ignore-image-text-cache`     | 이미지 텍스트 캐시 무시                                                                 | `pdf2zh_next example.pdf --ignore-image-text-cache`                                                                   |
| `--ignore-text-image-cache`     | 텍스트 이미지 캐시 무시                                                                 | `pdf2zh_next example.pdf --ignore-text-image-cache`                                                                   |
| `--ignore-pdf-text-cache`       | PDF 텍스트 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-text-cache`                                                                     |
| `--ignore-text-pdf-cache`       | 텍스트 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-text-pdf-cache`                                                                     |
| `--ignore-pdf-image-cache`      | PDF 이미지 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-image-cache`                                                                    |
| `--ignore-image-pdf-cache`      | 이미지 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-image-pdf-cache`                                                                    |
| `--ignore-pdf-layout-cache`     | PDF 레이아웃 캐시 무시                                                                  | `pdf2zh_next example.pdf --ignore-pdf-layout-cache`                                                                   |
| `--ignore-layout-pdf-cache`     | 레이아웃 PDF 캐시 무시                                                                  | `pdf2zh_next example.pdf --ignore-layout-pdf-cache`                                                                   |
| `--ignore-pdf-table-cache`      | PDF 테이블 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-table-cache`                                                                    |
| `--ignore-table-pdf-cache`      | 테이블 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-table-pdf-cache`                                                                    |
| `--ignore-pdf-math-cache`       | PDF 수학 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-pdf-math-cache`                                                                     |
| `--ignore-math-pdf-cache`       | 수학 PDF 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-math-pdf-cache`                                                                     |
| `--ignore-pdf-equation-cache`   | PDF 방정식 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-equation-cache`                                                                 |
| `--ignore-equation-pdf-cache`   | 방정식 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-equation-pdf-cache`                                                                 |
| `--ignore-pdf-formula-cache`    | PDF 공식 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-pdf-formula-cache`                                                                  |
| `--ignore-formula-pdf-cache`    | 공식 PDF 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-formula-pdf-cache`                                                                  |
| `--ignore-pdf-figure-cache`     | PDF 그림 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-pdf-figure-cache`                                                                   |
| `--ignore-figure-pdf-cache`     | 그림 PDF 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-figure-pdf-cache`                                                                   |
| `--ignore-pdf-graphic-cache`    | PDF 그래픽 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-graphic-cache`                                                                  |
| `--ignore-graphic-pdf-cache`    | 그래픽 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-graphic-pdf-cache`                                                                  |
| `--ignore-pdf-chart-cache`      | PDF 차트 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-pdf-chart-cache`                                                                    |
| `--ignore-chart-pdf-cache`      | 차트 PDF 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-chart-pdf-cache`                                                                    |
| `--ignore-pdf-diagram-cache`    | PDF 다이어그램 캐시 무시                                                                | `pdf2zh_next example.pdf --ignore-pdf-diagram-cache`                                                                  |
| `--ignore-diagram-pdf-cache`    | 다이어그램 PDF 캐시 무시                                                                | `pdf2zh_next example.pdf --ignore-diagram-pdf-cache`                                                                  |
| `--ignore-pdf-vector-cache`     | PDF 벡터 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-pdf-vector-cache`                                                                   |
| `--ignore-vector-pdf-cache`     | 벡터 PDF 캐시 무시                                                                      | `pdf2zh_next example.pdf --ignore-vector-pdf-cache`                                                                   |
| `--ignore-pdf-raster-cache`     | PDF 래스터 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-raster-cache`                                                                   |
| `--ignore-raster-pdf-cache`     | 래스터 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-raster-pdf-cache`                                                                   |
| `--ignore-pdf-bitmap-cache`     | PDF 비트맵 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-pdf-bitmap-cache`                                                                   |
| `--ignore-bitmap-pdf-cache`     | 비트맵 PDF 캐시 무시                                                                    | `pdf2zh_next example.pdf --ignore-bitmap-pdf-cache`                                                                   |
| `--ignore-pdf-image-text-cache` | PDF 이미지 텍스트 캐시 무시                                                             | `pdf2zh_next example.pdf --ignore-pdf-image-text-cache`                                                               |
| `--ignore-image-text-pdf-cache` | 이미지 텍스트 PDF 캐시 무시                                                             | `pdf2zh_next example.pdf --ignore-image-text-pdf-cache`                                                               |
| `--ignore-pdf-text-image-cache` | PDF 텍스트 이미지 캐시 무시                                                             | `pdf2zh_next example.pdf --ignore-pdf-text-image-cache`                                                               |
| `--ignore-text-image-pdf-cache` | 텍스트 이미지 PDF 캐시 무시                                                             | `pdf2zh_next example.pdf --ignore-text-image-pdf-cache`                                                               |
| `--ignore-pdf-pdf-cache`        | PDF PDF 캐시 무시                                                                       | `pdf2zh_next example.pdf --ignore-pdf-pdf-cache`                                                                      |
| `--ignore-pdf-pdf-pdf-cache`    | PDF PDF PDF 캐시 무시                                                                   | `pdf2zh_next example.pdf --ignore-pdf-pdf-pdf-cache`                                                                  |
|---------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `--custom-user-prompt`          | Custom user prompt for translation. Used for `/no_think` in Qwen 3                     | `pdf2zh_next example.pdf --custom-user-prompt "/no_think Please translate the following text into Chinese"`                |
| `--custom-system-prompt-format` | Custom system prompt for format. Used for `/no_think` in Qwen 3                        | `pdf2zh_next example.pdf --custom-system-prompt-format "/no_think You are a professional, authentic machine translation engine"` |
| `--custom-user-prompt-format`   | Custom user prompt for format. Used for `/no_think` in Qwen 3                          | `pdf2zh_next example.pdf --custom-user-prompt-format "/no_think Please translate the following text into Chinese"`         |

---

### TRANSLATION RESULT

| `--custom-system-prompt`        | 번역을 위한 사용자 정의 시스템 프롬프트. Qwen 3 의 `/no_think` 에 사용됨                    | `pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional, authentic machine translation engine"` | 
|---------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| `--custom-user-prompt`          | 번역을 위한 사용자 정의 사용자 프롬프트. Qwen 3 의 `/no_think` 에 사용됨                     | `pdf2zh_next example.pdf --custom-user-prompt "/no_think Please translate the following text into Chinese"`                |
| `--custom-system-prompt-format` | 형식 지정을 위한 사용자 정의 시스템 프롬프트. Qwen 3 의 `/no_think` 에 사용됨                | `pdf2zh_next example.pdf --custom-system-prompt-format "/no_think You are a professional, authentic machine translation engine"` |
| `--custom-user-prompt-format`   | 형식 지정을 위한 사용자 정의 사용자 프롬프트. Qwen 3 의 `/no_think` 에 사용됨                | `pdf2zh_next example.pdf --custom-user-prompt-format "/no_think Please translate the following text into Chinese"`         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-format`             | Glossary file format. Default: `csv`.                                                   | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-format csv`                            |
| `--glossary-dir`                | Glossary directory.                                                                     | `pdf2zh_next example.pdf --glossary-dir ./glossaries`                                                                 |
| `--glossary-key-column`         | Key column index in glossary file. Default: `0`.                                        | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-key-column 0`                                        |
| `--glossary-value-column`       | Value column index in glossary file. Default: `1`.                                      | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-value-column 1`                                      |
| `--glossary-src-lang`           | Source language of glossary. Default: `en`.                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-src-lang en`                                         |
| `--glossary-tgt-lang`           | Target language of glossary. Default: `zh`.                                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-tgt-lang zh`                                         |
| `--glossary-case-sensitive`     | Case sensitive for glossary matching. Default: `false`.                                | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-case-sensitive`                                      |
| `--glossary-whole-word`         | Whole word matching for glossary. Default: `false`.                                    | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-whole-word`                                          |
| `--glossary-ignore-punctuation` | Ignore punctuation for glossary matching. Default: `false`.                            | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-ignore-punctuation`                                   |
| `--glossary-ignore-whitespace`  | Ignore whitespace for glossary matching. Default: `false`.                             | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-ignore-whitespace`                                    |
| `--glossary-ignore-case`        | Ignore case for glossary matching. Default: `false`.                                   | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-ignore-case`                                         |

---

### OUTPUT

| `--glossaries`                  | 용어집 파일 목록.                                                                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"`                                    |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--glossary-format`             | 용어집 파일 형식. 기본값: `csv`.                                                        | `pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv" --glossary-format csv`                            |
| `--glossary-dir`                | 용어집 디렉터리.                                                                        | `pdf2zh_next example.pdf --glossary-dir ./glossaries`                                                                 |
| `--glossary-key-column`         | 용어집 파일의 키 열 인덱스. 기본값: `0`.                                                 | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-key-column 0`                                        |
| `--glossary-value-column`       | 용어집 파일의 값 열 인덱스. 기본값: `1`.                                                 | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-value-column 1`                                      |
| `--glossary-src-lang`           | 용어집의 원본 언어. 기본값: `en`.                                                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-src-lang en`                                         |
| `--glossary-tgt-lang`           | 용어집의 대상 언어. 기본값: `zh`.                                                       | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-tgt-lang zh`                                         |
| `--glossary-case-sensitive`     | 용어집 일치 시 대소문자 구분. 기본값: `false`.                                          | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-case-sensitive`                                      |
| `--glossary-whole-word`         | 용어집의 전체 단어 일치. 기본값: `false`.                                               | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-whole-word`                                          |
| `--glossary-ignore-punctuation` | 용어집 일치 시 구두점 무시. 기본값: `false`.                                            | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-ignore-punctuation`                                   |
| `--glossary-ignore-whitespace`  | 용어집 일치 시 공백 무시. 기본값: `false`.                                              | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-ignore-whitespace`                                    |
| `--glossary-ignore-case`        | 용어집 일치 시 대소문자 무시. 기본값: `false`.                                          | `pdf2zh_next example.pdf --glossaries "glossary1.csv" --glossary-ignore-case`                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--glossary`                    | glossary file path                                                                      | `pdf2zh_next example.pdf --glossary=my_glossary.json`                                                                  |
| `--glossary-fallback`           | fallback to auto-extracted glossary when the word is not found in the provided glossary | `pdf2zh_next example.pdf --glossary=my_glossary.json --glossary-fallback`                                              |
| `--no-glossary`                 | disable glossary                                                                        | `pdf2zh_next example.pdf --no-glossary`                                                                                |
| `--glossary-min-freq`           | minimum frequency for auto-extracted glossary                                           | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-min-freq=5`                                         |
| `--glossary-min-freq-ratio`     | minimum frequency ratio for auto-extracted glossary                                     | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-min-freq-ratio=0.01`                                |
| `--glossary-min-length`         | minimum length for auto-extracted glossary                                              | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-min-length=2`                                       |
| `--glossary-max-length`         | maximum length for auto-extracted glossary                                              | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-max-length=20`                                      |

---

### TRANSLATION

| `--save-auto-extracted-glossary`| 자동 추출 용어집 저장                                                   | `pdf2zh_next example.pdf --save-auto-extracted-glossary`                                                              |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--glossary`                    | 용어집 파일 경로                                                                      | `pdf2zh_next example.pdf --glossary=my_glossary.json`                                                                  |
| `--glossary-fallback`           | 제공된 용어집에서 단어를 찾을 수 없을 때 자동 추출 용어집으로 대체 | `pdf2zh_next example.pdf --glossary=my_glossary.json --glossary-fallback`                                              |
| `--no-glossary`                 | 용어집 비활성화                                                                        | `pdf2zh_next example.pdf --no-glossary`                                                                                |
| `--glossary-min-freq`           | 자동 추출 용어집의 최소 빈도                                           | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-min-freq=5`                                         |
| `--glossary-min-freq-ratio`     | 자동 추출 용어집의 최소 빈도 비율                                     | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-min-freq-ratio=0.01`                                |
| `--glossary-min-length`         | 자동 추출 용어집의 최소 길이                                              | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-min-length=2`                                       |
| `--glossary-max-length`         | 자동 추출 용어집의 최대 길이                                              | `pdf2zh_next example.pdf --save-auto-extracted-glossary --glossary-max-length=20`                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| `--pool-request-qps`            | QPS for translation pool. If not set, will use 1 as default.                                      | `pdf2zh_next example.pdf --pool-request-qps 100`                                                           |
| `--pool-request-rate-limit`     | Rate limit for translation pool. If not set, will use 100 as default.                             | `pdf2zh_next example.pdf --pool-request-rate-limit 100`                                                    |
| `--pool-request-rate-limit-str` | Rate limit strategy for translation pool. If not set, will use `concurrent` as default.           | `pdf2zh_next example.pdf --pool-request-rate-limit-str concurrent`                                         |
| `--pool-request-timeout`        | Timeout for translation pool. If not set, will use 100 as default.                                | `pdf2zh_next example.pdf --pool-request-timeout 100`                                                       |
| `--pool-request-max-attempts`   | Maximum attempts for translation pool. If not set, will use 3 as default.                         | `pdf2zh_next example.pdf --pool-request-max-attempts 3`                                                    |
| `--pool-request-retry-wait`     | Retry wait time for translation pool. If not set, will use 3 as default.                          | `pdf2zh_next example.pdf --pool-request-retry-wait 3`                                                      |
| `--pool-request-retry-jitter`   | Retry jitter for translation pool. If not set, will use 0.1 as default.                           | `pdf2zh_next example.pdf --pool-request-retry-jitter 0.1`                                                  |

---

### RESPONSE

| `--pool-max-workers`            | 번역 풀의 최대 작업자 수입니다. 설정하지 않으면 qps 를 작업자 수로 사용합니다.                                | `pdf2zh_next example.pdf --pool-max-workers 100`                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `--pool-request-qps`            | 번역 풀의 QPS 입니다. 설정하지 않으면 기본값 1 을 사용합니다.                                                   | `pdf2zh_next example.pdf --pool-request-qps 100`                                                           |
| `--pool-request-rate-limit`     | 번역 풀의 속도 제한입니다. 설정하지 않으면 기본값 100 을 사용합니다.                                            | `pdf2zh_next example.pdf --pool-request-rate-limit 100`                                                    |
| `--pool-request-rate-limit-str` | 번역 풀의 속도 제한 전략입니다. 설정하지 않으면 기본값 `concurrent` 를 사용합니다.                              | `pdf2zh_next example.pdf --pool-request-rate-limit-str concurrent`                                         |
| `--pool-request-timeout`        | 번역 풀의 타임아웃입니다. 설정하지 않으면 기본값 100 을 사용합니다.                                             | `pdf2zh_next example.pdf --pool-request-timeout 100`                                                       |
| `--pool-request-max-attempts`   | 번역 풀의 최대 시도 횟수입니다. 설정하지 않으면 기본값 3 을 사용합니다.                                         | `pdf2zh_next example.pdf --pool-request-max-attempts 3`                                                    |
| `--pool-request-retry-wait`     | 번역 풀의 재시도 대기 시간입니다. 설정하지 않으면 기본값 3 을 사용합니다.                                       | `pdf2zh_next example.pdf --pool-request-retry-wait 3`                                                      |
| `--pool-request-retry-jitter`   | 번역 풀의 재시도 지터입니다. 설정하지 않으면 기본값 0.1 을 사용합니다.                                          | `pdf2zh_next example.pdf --pool-request-retry-jitter 0.1`                                                  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--term-service`                | Term extraction translation service (default: `youdao`).                                | `pdf2zh_next example.pdf --term-service baidu`                                                                        |
| `--term-sleep`                  | Sleep time between term extraction requests (default: `0.5`).                           | `pdf2zh_next example.pdf --term-sleep 0.2`                                                                            |
| `--term-timeout`                | Timeout for term extraction translation service (default: `10`).                        | `pdf2zh_next example.pdf --term-timeout 5`                                                                            |

---

### TRANSLATION RESULT

| `--term-qps`                    | 용어 추출 번역 서비스의 QPS 제한. 설정하지 않으면 qps 를 따릅니다.         | `pdf2zh_next example.pdf --term-qps 20`                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--term-service`                | 용어 추출 번역 서비스 (기본값: `youdao`).                                | `pdf2zh_next example.pdf --term-service baidu`                                                                        |
| `--term-sleep`                  | 용어 추출 요청 간 대기 시간 (기본값: `0.5`).                           | `pdf2zh_next example.pdf --term-sleep 0.2`                                                                            |
| `--term-timeout`                | 용어 추출 번역 서비스의 타임아웃 (기본값: `10`).                        | `pdf2zh_next example.pdf --term-timeout 5`                                                                            |
---

### TRANSLATION RESULT

| `--term-pool-max-workers`       | 용어 추출 번역 풀의 최대 작업자 수입니다. 설정하지 않거나 0 으로 설정하면 `pool_max_workers` 를 따릅니다. | `pdf2zh_next example.pdf --term-pool-max-workers 40`                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--glossary <path>`             | Use custom glossary file                                                                | `pdf2zh_next example.pdf --glossary ./my-glossary.json`                                                               |
| `--glossary-output <path>`      | Save auto extracted glossary to file                                                    | `pdf2zh_next example.pdf --glossary-output ./auto-glossary.json`                                                      |
| `--ignore-glossary-case`        | Ignore case when matching glossary terms                                                | `pdf2zh_next example.pdf --ignore-glossary-case`                                                                      |
| `--glossary-min-length <number>` | Minimum length of glossary terms to extract (
|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `--secondary-font-family`       | Override secondary font family for translated text. Choices are the same as `--primary-font-family`. If not specified, uses automatic font selection based on original text properties.                                                      | `pdf2zh_next example.pdf --secondary-font-family serif` |
| `--font-size-multiplier`        | Scale factor for font sizes in translated text. Values >1.0 increase font size, <1.0 decrease font size. If not specified, uses automatic size adjustment.                                                                                  | `pdf2zh_next example.pdf --font-size-multiplier 1.2`   |
| `--line-height-multiplier`      | Scale factor for line spacing in translated text. Values >1.0 increase line spacing, <1.0 decrease line spacing. If not specified, uses automatic spacing adjustment.                                                                       | `pdf2zh_next example.pdf --line-height-multiplier 1.1` |
| `--character-spacing-multiplier`| Scale factor for character spacing in translated text. Values >1.0 increase spacing, <1.0 decrease spacing. If not specified, uses automatic spacing adjustment.                                                                            | `pdf2zh_next example.pdf --character-spacing-multiplier 1.05` |
| `--font-family-mapping`         | Custom font family mapping rules. Format: `original_font:target_font[,original_font2:target_font2...]`. If not specified, uses default mapping rules.                                                                                       | `pdf2zh_next example.pdf --font-family-mapping "Arial:Noto Sans SC"` |

---

### TRANSLATION RESULT

| `--primary-font-family` | 번역된 텍스트의 기본 글꼴 패밀리를 재정의합니다. 선택지: 'serif'는 세리프 글꼴, 'sans-serif'는 산세리프 글꼴, 'script'는 필기체/이탤릭 글꼴입니다. 지정하지 않으면 원본 텍스트 속성을 기반으로 자동 글꼴 선택을 사용합니다. | `pdf2zh_next example.pdf --primary-font-family serif` |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| `--secondary-font-family` | 번역된 텍스트의 보조 글꼴 패밀리를 재정의합니다. 선택지는 `--primary-font-family` 와 동일합니다. 지정하지 않으면 원본 텍스트 속성을 기반으로 자동 글꼴 선택을 사용합니다.                                                               | `pdf2zh_next example.pdf --secondary-font-family serif` |
| `--font-size-multiplier` | 번역된 텍스트의 글꼴 크기 배율 인자입니다. 값 >1.0 은 글꼴 크기를 증가시키고, <1.0 은 감소시킵니다. 지정하지 않으면 자동 크기 조정을 사용합니다.                                                                               | `pdf2zh_next example.pdf --font-size-multiplier 1.2`   |
| `--line-height-multiplier` | 번역된 텍스트의 행간 배율 인자입니다. 값 >1.0 은 행간을 증가시키고, <1.0 은 감소시킵니다. 지정하지 않으면 자동 간격 조정을 사용합니다.                                                                                    | `pdf2zh_next example.pdf --line-height-multiplier 1.1` |
| `--character-spacing-multiplier` | 번역된 텍스트의 자간 배율 인자입니다. 값 >1.0 은 간격을 증가시키고, <1.0 은 감소시킵니다. 지정하지 않으면 자동 간격 조정을 사용합니다.                                                                                    | `pdf2zh_next example.pdf --character-spacing-multiplier 1.05` |
| `--font-family-mapping` | 사용자 정의 글꼴 패밀리 매핑 규칙입니다. 형식: `원본_글꼴:대상_글꼴 [,원본_글꼴 2:대상_글꼴 2...]`. 지정하지 않으면 기본 매핑 규칙을 사용합니다.                                                                               | `pdf2zh_next example.pdf --font-family-mapping "Arial:Noto Sans SC"` |
---

### OUTPUT

| `--no-dual`                     | 이중 언어 PDF 파일을 출력하지 않음                                                      | `pdf2zh_next example.pdf --no-dual`                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-bilingual`                | Do not output bilingual PDF files                                                       | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--mono-prefix <prefix>`        | Prefix for monolingual PDF files (default: `_mono`)                                     | `pdf2zh_next example.pdf --mono-prefix _mono`                                                                         |
| `--bilingual-prefix <prefix>`   | Prefix for bilingual PDF files (default: `_bilingual`)                                  | `pdf2zh_next example.pdf --bilingual-prefix _bilingual`                                                               |
| `--output-dir <dir>`            | Output directory for translated PDF files (default: `./`)                               | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--source <lang>`               | Source language (default: `en`)                                                         | `pdf2zh_next example.pdf --source en`                                                                                 |
| `--target <lang>`               | Target language (default: `zh`)                                                         | `pdf2zh_next example.pdf --target ja`                                                                                 |
| `--translator <translator>`     | Translation service to use (default: `google`)                                          | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-config <config>`  | Path to translator configuration file (default: `translator_config.json`)               | `pdf2zh_next example.pdf --translator-config ./translator_config.json`                                                |
| `--translator-args <args>`      | Additional arguments for the translation service (default: `{}`)                        | `pdf2zh_next example.pdf --translator-args '{"api_key": "your_api_key"}'`                                             |
| `--max-concurrent-requests <n>` | Maximum number of concurrent requests to the translation service (default: `5`)         | `pdf2zh_next example.pdf --max-concurrent-requests 10`                                                                |
| `--request-interval <ms>`       | Interval between requests to the translation service in milliseconds (default: `1000`)  | `pdf2zh_next example.pdf --request-interval 500`                                                                      |
| `--retry-attempts <n>`          | Number of retry attempts for failed requests (default: `3`)                             | `pdf2zh_next example.pdf --retry-attempts 5`                                                                          |
| `--retry-delay <ms>`            | Delay between retry attempts in milliseconds (default: `1000`)                          | `pdf2zh_next example.pdf --retry-delay 2000`                                                                          |
| `--timeout <ms>`                | Timeout for each request to the translation service in milliseconds (default: `10000`)  | `pdf2zh_next example.pdf --timeout 15000`                                                                             |
| `--ignore-errors`               | Continue processing even if some requests fail                                          | `pdf2zh_next example.pdf --ignore-errors`                                                                             |
| `--log-level <level>`           | Log level (default: `INFO`)                                                             | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--log-file <file>`             | Path to log file (default: `pdf2zh_next.log`)                                           | `pdf2zh_next example.pdf --log-file ./pdf2zh_next.log`                                                                |
| `--config <config>`             | Path to configuration file (default: `pdf2zh_next_config.json`)                         | `pdf2zh_next example.pdf --config ./pdf2zh_next_config.json`                                                          |
| `--help`                        | Show help message and exit                                                              | `pdf2zh_next example.pdf --help`                                                                                      |

---

### TRANSLATION

| `--no-mono`                     | 단일 언어 PDF 파일 출력하지 않음                                                                                     | `pdf2zh_next example.pdf --no-mono`                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--no-bilingual`                | 이중 언어 PDF 파일 출력하지 않음                                                                                     | `pdf2zh_next example.pdf --no-bilingual`                                                                              |
| `--mono-prefix <prefix>`        | 단일 언어 PDF 파일 접두사 (기본값: `_mono`)                                                                          | `pdf2zh_next example.pdf --mono-prefix _mono`                                                                         |
| `--bilingual-prefix <prefix>`   | 이중 언어 PDF 파일 접두사 (기본값: `_bilingual`)                                                                     | `pdf2zh_next example.pdf --bilingual-prefix _bilingual`                                                               |
| `--output-dir <dir>`            | 번역된 PDF 파일 출력 디렉토리 (기본값: `./`)                                                                         | `pdf2zh_next example.pdf --output-dir ./output`                                                                       |
| `--source <lang>`               | 원본 언어 (기본값: `en`)                                                                                             | `pdf2zh_next example.pdf --source en`                                                                                 |
| `--target <lang>`               | 대상 언어 (기본값: `zh`)                                                                                             | `pdf2zh_next example.pdf --target ja`                                                                                 |
| `--translator <translator>`     | 사용할 번역 서비스 (기본값: `google`)                                                                                | `pdf2zh_next example.pdf --translator deepl`                                                                          |
| `--translator-config <config>`  | 번역 서비스 구성 파일 경로 (기본값: `translator_config.json`)                                                         | `pdf2zh_next example.pdf --translator-config ./translator_config.json`                                                |
| `--translator-args <args>`      | 번역 서비스에 대한 추가 인수 (기본값: `{}`)                                                                          | `pdf2zh_next example.pdf --translator-args '{"api_key": "your_api_key"}'`                                             |
| `--max-concurrent-requests <n>` | 번역 서비스에 대한 최대 동시 요청 수 (기본값: `5`)                                                                   | `pdf2zh_next example.pdf --max-concurrent-requests 10`                                                                |
| `--request-interval <ms>`       | 번역 서비스에 대한 요청 간격 (밀리초 단위, 기본값: `1000`)                                                             | `pdf2zh_next example.pdf --request-interval 500`                                                                      |
| `--retry-attempts <n>`          | 실패한 요청에 대한 재시도 횟수 (기본값: `3`)                                                                         | `pdf2zh_next example.pdf --retry-attempts 5`                                                                          |
| `--retry-delay <ms>`            | 재시도 간 지연 시간 (밀리초 단위, 기본값: `1000`)                                                                     | `pdf2zh_next example.pdf --retry-delay 2000`                                                                          |
| `--timeout <ms>`                | 번역 서비스에 대한 각 요청의 타임아웃 (밀리초 단위, 기본값: `10000`)                                                   | `pdf2zh_next example.pdf --timeout 15000`                                                                             |
| `--ignore-errors`               | 일부 요청이 실패해도 계속 처리                                                                                       | `pdf2zh_next example.pdf --ignore-errors`                                                                             |
| `--log-level <level>`           | 로그 수준 (기본값: `INFO`)                                                                                           | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--log-file <file>`             | 로그 파일 경로 (기본값: `pdf2zh_next.log`)                                                                           | `pdf2zh_next example.pdf --log-file ./pdf2zh_next.log`                                                                |
| `--config <config>`             | 구성 파일 경로 (기본값: `pdf2zh_next_config.json`)                                                                   | `pdf2zh_next example.pdf --config ./pdf2zh_next_config.json`                                                          |
| `--help`                        | 도움말 메시지 표시 후 종료                                                                                           | `pdf2zh_next example.pdf --help`                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-font-name`          | Font name to use for formula text                                                       | `pdf2zh_next example.pdf --formular-font-name "Times New Roman"`                                                      |
| `--formular-font-size`          | Font size to use for formula text                                                       | `pdf2zh_next example.pdf --formular-font-size 10.5`                                                                   |
| `--formular-font-style`         | Font style to use for formula text                                                      | `pdf2zh_next example.pdf --formular-font-style "normal"`                                                              |
| `--formular-font-color`         | Font color to use for formula text                                                      | `pdf2zh_next example.pdf --formular-font-color "#000000"`                                                             |
| `--formular-ocr-engine`         | OCR engine to use for formula text                                                      | `pdf2zh_next example.pdf --formular-ocr-engine "paddleocr"`                                                           |
| `--formular-ocr-lang`           | OCR language to use for formula text                                                    | `pdf2zh_next example.pdf --formular-ocr-lang "en"`                                                                    |
| `--formular-ocr-dpi`            | OCR DPI to use for formula text                                                         | `pdf2zh_next example.pdf --formular-ocr-dpi 300`                                                                      |
| `--formular-ocr-whitelist`      | OCR whitelist to use for formula text                                                   | `pdf2zh_next example.pdf --formular-ocr-whitelist "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"`   |
| `--formular-ocr-blacklist`      | OCR blacklist to use for formula text                                                   | `pdf2zh_next example.pdf --formular-ocr-blacklist "!@#$%^&*()_+-=[]{}|;:,./<>?"`                                     |
| `--formular-ocr-timeout`        | OCR timeout to use for formula text                                                     | `pdf2zh_next example.pdf --formular-ocr-timeout 10`                                                                   |
| `--formular-ocr-max-workers`    | OCR max workers to use for formula text                                                 | `pdf2zh_next example.pdf --formular-ocr-max-workers 4`                                                                |
| `--formular-ocr-batch-size`     | OCR batch size to use for formula text                                                  | `pdf2zh_next example.pdf --formular-ocr-batch-size 10`                                                                |
| `--formular-ocr-skip-text`      | Skip OCR for formula text                                                               | `pdf2zh_next example.pdf --formular-ocr-skip-text`                                                                    |
| `--formular-ocr-skip-bbox`      | Skip OCR for formula bounding box                                                       | `pdf2zh_next example.pdf --formular-ocr-skip-bbox`                                                                    |
| `--formular-ocr-skip-line`      | Skip OCR for formula line                                                               | `pdf2zh_next example.pdf --formular-ocr-skip-line`                                                                    |
| `--formular-ocr-skip-word`      | Skip OCR for formula word                                                               | `pdf2zh_next example.pdf --formular-ocr-skip-word`                                                                    |
| `--formular-ocr-skip-char`      | Skip OCR for formula character                                                          | `pdf2zh_next example.pdf --formular-ocr-skip-char`                                                                    |
| `--formular-ocr-skip-formula`   | Skip OCR for formula                                                                    | `pdf2zh_next example.pdf --formular-ocr-skip-formula`                                                                 |
| `--formular-ocr-skip-table`     | Skip OCR for formula table                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-table`                                                                   |
| `--formular-ocr-skip-image`     | Skip OCR for formula image                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-image`                                                                   |
| `--formular-ocr-skip-shape`     | Skip OCR for formula shape                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-shape`                                                                   |
| `--formular-ocr-skip-annot`     | Skip OCR for formula annotation                                                         | `pdf2zh_next example.pdf --formular-ocr-skip-annot`                                                                   |
| `--formular-ocr-skip-link`      | Skip OCR for formula link                                                               | `pdf2zh_next example.pdf --formular-ocr-skip-link`                                                                    |
| `--formular-ocr-skip-field`     | Skip OCR for formula field                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-field`                                                                   |
| `--formular-ocr-skip-widget`    | Skip OCR for formula widget                                                             | `pdf2zh_next example.pdf --formular-ocr-skip-widget`                                                                  |
| `--formular-ocr-skip-signature` | Skip OCR for formula signature                                                          | `pdf2zh_next example.pdf --formular-ocr-skip-signature`                                                               |
| `--formular-ocr-skip-redact`    | Skip OCR for formula redaction                                                          | `pdf2zh_next example.pdf --formular-ocr-skip-redact`                                                                  |
| `--formular-ocr-skip-3d`        | Skip OCR for formula 3D                                                                 | `pdf2zh_next example.pdf --formular-ocr-skip-3d`                                                                      |
| `--formular-ocr-skip-xobject`   | Skip OCR for formula XObject                                                            | `pdf2zh_next example.pdf --formular-ocr-skip-xobject`                                                                 |
| `--formular-ocr-skip-group`     | Skip OCR for formula group                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-group`                                                                   |
| `--formular-ocr-skip-marker`    | Skip OCR for formula marker                                                             | `pdf2zh_next example.pdf --formular-ocr-skip-marker`                                                                  |
| `--formular-ocr-skip-artifact`  | Skip OCR for formula artifact                                                           | `pdf2zh_next example.pdf --formular-ocr-skip-artifact`                                                                |
| `--formular-ocr-skip-unknown`   | Skip OCR for formula unknown                                                            | `pdf2zh_next example.pdf --formular-ocr-skip-unknown`                                                                 |
| `--formular-ocr-skip-other`     | Skip OCR for formula other                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-other`                                                                   |
| `--formular-ocr-skip-all`       | Skip OCR for all formula elements                                                       | `pdf2zh_next example.pdf --formular-ocr-skip-all`                                                                     |

---

### TRANSLATED TEXT

| `--formular-font-pattern`       | 수식 텍스트를 식별하기 위한 폰트 패턴                                                      | `pdf2zh_next example.pdf --formular-font-pattern "(MS.*)"`                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--formular-font-name`          | 수식 텍스트에 사용할 폰트 이름                                                              | `pdf2zh_next example.pdf --formular-font-name "Times New Roman"`                                                      |
| `--formular-font-size`          | 수식 텍스트에 사용할 폰트 크기                                                              | `pdf2zh_next example.pdf --formular-font-size 10.5`                                                                   |
| `--formular-font-style`         | 수식 텍스트에 사용할 폰트 스타일                                                             | `pdf2zh_next example.pdf --formular-font-style "normal"`                                                              |
| `--formular-font-color`         | 수식 텍스트에 사용할 폰트 색상                                                              | `pdf2zh_next example.pdf --formular-font-color "#000000"`                                                             |
| `--formular-ocr-engine`         | 수식 텍스트에 사용할 OCR 엔진                                                              | `pdf2zh_next example.pdf --formular-ocr-engine "paddleocr"`                                                           |
| `--formular-ocr-lang`           | 수식 텍스트에 사용할 OCR 언어                                                              | `pdf2zh_next example.pdf --formular-ocr-lang "en"`                                                                    |
| `--formular-ocr-dpi`            | 수식 텍스트에 사용할 OCR DPI                                                              | `pdf2zh_next example.pdf --formular-ocr-dpi 300`                                                                      |
| `--formular-ocr-whitelist`      | 수식 텍스트에 사용할 OCR 화이트리스트                                                          | `pdf2zh_next example.pdf --formular-ocr-whitelist "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"`   |
| `--formular-ocr-blacklist`      | 수식 텍스트에 사용할 OCR 블랙리스트                                                          | `pdf2zh_next example.pdf --formular-ocr-blacklist "!@#$%^&*()_+-=[]{}|;:,./<>?"`                                     |
| `--formular-ocr-timeout`        | 수식 텍스트에 사용할 OCR 타임아웃                                                           | `pdf2zh_next example.pdf --formular-ocr-timeout 10`                                                                   |
| `--formular-ocr-max-workers`    | 수식 텍스트에 사용할 OCR 최대 작업자 수                                                        | `pdf2zh_next example.pdf --formular-ocr-max-workers 4`                                                                |
| `--formular-ocr-batch-size`     | 수식 텍스트에 사용할 OCR 배치 크기                                                           | `pdf2zh_next example.pdf --formular-ocr-batch-size 10`                                                                |
| `--formular-ocr-skip-text`      | 수식 텍스트에 대한 OCR 건너뛰기                                                             | `pdf2zh_next example.pdf --formular-ocr-skip-text`                                                                    |
| `--formular-ocr-skip-bbox`      | 수식 바운딩 박스에 대한 OCR 건너뛰기                                                          | `pdf2zh_next example.pdf --formular-ocr-skip-bbox`                                                                    |
| `--formular-ocr-skip-line`      | 수식 라인에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-line`                                                                    |
| `--formular-ocr-skip-word`      | 수식 단어에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-word`                                                                    |
| `--formular-ocr-skip-char`      | 수식 문자에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-char`                                                                    |
| `--formular-ocr-skip-formula`   | 수식에 대한 OCR 건너뛰기                                                                  | `pdf2zh_next example.pdf --formular-ocr-skip-formula`                                                                 |
| `--formular-ocr-skip-table`     | 수식 테이블에 대한 OCR 건너뛰기                                                             | `pdf2zh_next example.pdf --formular-ocr-skip-table`                                                                   |
| `--formular-ocr-skip-image`     | 수식 이미지에 대한 OCR 건너뛰기                                                             | `pdf2zh_next example.pdf --formular-ocr-skip-image`                                                                   |
| `--formular-ocr-skip-shape`     | 수식 도형에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-shape`                                                                   |
| `--formular-ocr-skip-annot`     | 수식 주석에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-annot`                                                                   |
| `--formular-ocr-skip-link`      | 수식 링크에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-link`                                                                    |
| `--formular-ocr-skip-field`     | 수식 필드에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-field`                                                                   |
| `--formular-ocr-skip-widget`    | 수식 위젯에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-widget`                                                                  |
| `--formular-ocr-skip-signature` | 수식 서명에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-signature`                                                               |
| `--formular-ocr-skip-redact`    | 수식 수정에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-redact`                                                                  |
| `--formular-ocr-skip-3d`        | 수식 3D 에 대한 OCR 건너뛰기                                                               | `pdf2zh_next example.pdf --formular-ocr-skip-3d`                                                                      |
| `--formular-ocr-skip-xobject`   | 수식 XObject 에 대한 OCR 건너뛰기                                                            | `pdf2zh_next example.pdf --formular-ocr-skip-xobject`                                                                 |
| `--formular-ocr-skip-group`     | 수식 그룹에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-group`                                                                   |
| `--formular-ocr-skip-marker`    | 수식 마커에 대한 OCR 건너뛰기                                                              | `pdf2zh_next example.pdf --formular-ocr-skip-marker`                                                                  |
| `--formular-ocr-skip-artifact`  | 수식 아티팩트에 대한 OCR 건너뛰기                                                            | `pdf2zh_next example.pdf --formular-ocr-skip-artifact`                                                                |
| `--formular-ocr-skip-unknown`   | 수식 알 수 없는 요소에 대한 OCR 건너뛰기                                                        | `pdf2zh_next example.pdf --formular-ocr-skip-unknown`                                                                 |
| `--formular-ocr-skip-other`     | 수식 기타 요소에 대한 OCR 건너뛰기                                                            | `pdf2zh_next example.pdf --formular-ocr-skip-other`                                                                   |
| `--formular-ocr-skip-all`       | 모든 수식 요소에 대한 OCR 건너뛰기                                                            | `pdf2zh_next example.pdf --formular-ocr-skip-all`                                                                     |
| `--formular-char-replace`       | Replace formula text with specified character                                           | `pdf2zh_next example.pdf --formular-char-replace " "`                                                                 |
| `--formular-char-ignore`        | Ignore formula text and keep original                                                   | `pdf2zh_next example.pdf --formular-char-ignore`                                                                      |
| `--formular-char-merge`         | Merge formula text with adjacent text                                                   | `pdf2zh_next example.pdf --formular-char-merge`                                                                       |
| `--formular-char-translate`     | Translate formula text                                                                  | `pdf2zh_next example.pdf --formular-char-translate`                                                                   |
| `--formular-char-keep-original` | Keep original formula text and add translated text as note                              | `pdf2zh_next example.pdf --formular-char-keep-original`                                                               |

---

### TRANSLATION RESULT

| `--formular-char-pattern`       | 수식 텍스트를 식별하는 문자 패턴                                              | `pdf2zh_next example.pdf --formular-char-pattern "(MS.*)"`                                                            |
| `--formular-char-replace`       | 지정된 문자로 수식 텍스트를 대체                                              | `pdf2zh_next example.pdf --formular-char-replace " "`                                                                 |
| `--formular-char-ignore`        | 수식 텍스트를 무시하고 원본 유지                                              | `pdf2zh_next example.pdf --formular-char-ignore`                                                                      |
| `--formular-char-merge`         | 수식 텍스트를 인접 텍스트와 병합                                              | `pdf2zh_next example.pdf --formular-char-merge`                                                                       |
| `--formular-char-translate`     | 수식 텍스트를 번역                                                           | `pdf2zh_next example.pdf --formular-char-translate`                                                                   |
| `--formular-char-keep-original` | 원본 수식 텍스트를 유지하고 번역된 텍스트를 노트로 추가                       | `pdf2zh_next example.pdf --formular-char-keep-original`                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | Set the threshold for splitting short lines (default: 0.5)                              | `pdf2zh_next example.pdf --split-short-lines-threshold 0.3`                                                           |
| `--split-short-lines-min-len`   | Set the minimum length for splitting short lines (default: 5)                           | `pdf2zh_next example.pdf --split-short-lines-min-len 3`                                                               |
| `--split-short-lines-max-len`   | Set the maximum length for splitting short lines (default: 50)                          | `pdf2zh_next example.pdf --split-short-lines-max-len 100`                                                             |
| `--split-short-lines-ratio`     | Set the ratio for splitting short lines (default: 0.5)                                  | `pdf2zh_next example.pdf --split-short-lines-ratio 0.3`                                                               |
| `--split-short-lines-mode`      | Set the mode for splitting short lines (default: "ratio", options: "ratio", "absolute") | `pdf2zh_next example.pdf --split-short-lines-mode absolute`                                                           |

---

### TRANSLATION RESULT

| `--split-short-lines`           | 짧은 줄을 강제로 다른 단락으로 분할                                                       | `pdf2zh_next example.pdf --split-short-lines`                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--split-short-lines-threshold` | 짧은 줄 분할 임계값 설정 (기본값: 0.5)                                                    | `pdf2zh_next example.pdf --split-short-lines-threshold 0.3`                                                           |
| `--split-short-lines-min-len`   | 짧은 줄 분할 최소 길이 설정 (기본값: 5)                                                   | `pdf2zh_next example.pdf --split-short-lines-min-len 3`                                                               |
| `--split-short-lines-max-len`   | 짧은 줄 분할 최대 길이 설정 (기본값: 50)                                                  | `pdf2zh_next example.pdf --split-short-lines-max-len 100`                                                             |
| `--split-short-lines-ratio`     | 짧은 줄 분할 비율 설정 (기본값: 0.5)                                                      | `pdf2zh_next example.pdf --split-short-lines-ratio 0.3`                                                               |
| `--split-short-lines-mode`      | 짧은 줄 분할 모드 설정 (기본값: "ratio", 옵션: "ratio", "absolute")                        | `pdf2zh_next example.pdf --split-short-lines-mode absolute`                                                           |
`1.0`  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------ |
| `--short-line-split-min-length` | Minimum length of a short line to be considered for splitting                           | `pdf2zh_next example.pdf --short-line-split-min-length 10`                                                            | `0`    |
| `--short-line-split-max-length` | Maximum length of a short line to be considered for splitting                           | `pdf2zh_next example.pdf --short-line-split-max-length 50`                                                            | `1000` |
| `--short-line-split-min-gap`    | Minimum gap between words in a short line to be considered for splitting (in font size) | `pdf2zh_next example.pdf --short-line-split-min-gap 0.2`                                                              | `0.0`  |
| `--short-line-split-max-gap`    | Maximum gap between words in a short line to be considered for splitting (in font size) | `pdf2zh_next example.pdf --short-line-split-max-gap 10.0`                                                             | `100.0`|
| `--short-line-split-min-ratio`  | Minimum ratio of the gap to the font size for a short line to be considered for splitting | `pdf2zh_next example.pdf --short-line-split-min-ratio 0.1`                                                            | `0.0`  |
| `--short-line-split-max-ratio`  | Maximum ratio of the gap to the font size for a short line to be considered for splitting | `pdf2zh_next example.pdf --short-line-split-max-ratio 10.0`                                                           | `100.0`|

---

### TRANSLATION RESULT

| `--short-line-split-factor`     | 짧은 줄 분할 임계값 계수                                                  | `pdf2zh_next example.pdf --short-line-split-factor 1.2`                                                               | `1.0`  |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------ |
| `--short-line-split-min-length` | 분할을 위해 고려되는 짧은 줄의 최소 길이                           | `pdf2zh_next example.pdf --short-line-split-min-length 10`                                                            | `0`    |
| `--short-line-split-max-length` | 분할을 위해 고려되는 짧은 줄의 최대 길이                           | `pdf2zh_next example.pdf --short-line-split-max-length 50`                                                            | `1000` |
| `--short-line-split-min-gap`    | 분할을 위해 고려되는 짧은 줄 내 단어 간 최소 간격 (글꼴 크기 기준) | `pdf2zh_next example.pdf --short-line-split-min-gap 0.2`                                                              | `0.0`  |
| `--short-line-split-max-gap`    | 분할을 위해 고려되는 짧은 줄 내 단어 간 최대 간격 (글꼴 크기 기준) | `pdf2zh_next example.pdf --short-line-split-max-gap 10.0`                                                             | `100.0`|
| `--short-line-split-min-ratio`  | 분할을 위해 고려되는 짧은 줄에 대한 간격 대 글꼴 크기 비율의 최소값 | `pdf2zh_next example.pdf --short-line-split-min-ratio 0.1`                                                            | `0.0`  |
| `--short-line-split-max-ratio`  | 분할을 위해 고려되는 짧은 줄에 대한 간격 대 글꼴 크기 비율의 최대값 | `pdf2zh_next example.pdf --short-line-split-max-ratio 10.0`                                                           | `100.0`|
`false`                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `--skip-translate`              | Skip translation step                                                                   | `pdf2zh_next example.pdf --skip-translate`                                                                            | `false`                                |
| `--skip-ocr`                    | Skip OCR step                                                                           | `pdf2zh_next example.pdf --skip-ocr`                                                                                  | `false`                                |
| `--skip-pdf-reconstruct`        | Skip PDF reconstruction step                                                            | `pdf2zh_next example.pdf --skip-pdf-reconstruct`                                                                      | `false`                                |
| `--skip-extract`                | Skip extraction step                                                                    | `pdf2zh_next example.pdf --skip-extract`                                                                              | `false`                                |
| `--skip-inline-equation-render` | Skip inline equation rendering step                                                     | `pdf2zh_next example.pdf --skip-inline-equation-render`                                                               | `false`                                |
| `--skip-block-equation-render`  | Skip block equation rendering step                                                      | `pdf2zh_next example.pdf --skip-block-equation-render`                                                                | `false`                                |
| `--skip-table-render`           | Skip table rendering step                                                               | `pdf2zh_next example.pdf --skip-table-render`                                                                         | `false`                                |
| `--skip-figure-render`          | Skip figure rendering step                                                              | `pdf2zh_next example.pdf --skip-figure-render`                                                                        | `false`                                |
| `--skip-title-render`           | Skip title rendering step                                                               | `pdf2zh_next example.pdf --skip-title-render`                                                                         | `false`                                |
| `--skip-list-render`            | Skip list rendering step                                                                | `pdf2zh_next example.pdf --skip-list-render`                                                                          | `false`                                |
| `--skip-text-render`            | Skip text rendering step                                                                | `pdf2zh_next example.pdf --skip-text-render`                                                                          | `false`                                |
| `--skip-reference-render`       | Skip reference rendering step                                                           | `pdf2zh_next example.pdf --skip-reference-render`                                                                     | `false`                                |
| `--skip-footnote-render`        | Skip footnote rendering step                                                            | `pdf2zh_next example.pdf --skip-footnote-render`                                                                      | `false`                                |
| `--skip-caption-render`         | Skip caption rendering step                                                             | `pdf2zh_next example.pdf --skip-caption-render`                                                                       | `false`                                |
| `--skip-header-render`          | Skip header rendering step                                                              | `pdf2zh_next example.pdf --skip-header-render`                                                                        | `false`                                |
| `--skip-footer-render`          | Skip footer rendering step                                                              | `pdf2zh_next example.pdf --skip-footer-render`                                                                        | `false`                                |

---

### TRANSLATION RESULT

| `--skip-clean`                  | PDF 정리 단계 건너뛰기                                                                  | `pdf2zh_next example.pdf --skip-clean`                                                                                | `false`                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `--skip-translate`              | 번역 단계 건너뛰기                                                                      | `pdf2zh_next example.pdf --skip-translate`                                                                            | `false`                                |
| `--skip-ocr`                    | OCR 단계 건너뛰기                                                                       | `pdf2zh_next example.pdf --skip-ocr`                                                                                  | `false`                                |
| `--skip-pdf-reconstruct`        | PDF 재구성 단계 건너뛰기                                                                | `pdf2zh_next example.pdf --skip-pdf-reconstruct`                                                                      | `false`                                |
| `--skip-extract`                | 추출 단계 건너뛰기                                                                      | `pdf2zh_next example.pdf --skip-extract`                                                                              | `false`                                |
| `--skip-inline-equation-render` | 인라인 수식 렌더링 단계 건너뛰기                                                         | `pdf2zh_next example.pdf --skip-inline-equation-render`                                                               | `false`                                |
| `--skip-block-equation-render`  | 블록 수식 렌더링 단계 건너뛰기                                                           | `pdf2zh_next example.pdf --skip-block-equation-render`                                                                | `false`                                |
| `--skip-table-render`           | 표 렌더링 단계 건너뛰기                                                                 | `pdf2zh_next example.pdf --skip-table-render`                                                                         | `false`                                |
| `--skip-figure-render`          | 그림 렌더링 단계 건너뛰기                                                                | `pdf2zh_next example.pdf --skip-figure-render`                                                                        | `false`                                |
| `--skip-title-render`           | 제목 렌더링 단계 건너뛰기                                                                | `pdf2zh_next example.pdf --skip-title-render`                                                                         | `false`                                |
| `--skip-list-render`            | 목록 렌더링 단계 건너뛰기                                                                | `pdf2zh_next example.pdf --skip-list-render`                                                                          | `false`                                |
| `--skip-text-render`            | 텍스트 렌더링 단계 건너뛰기                                                              | `pdf2zh_next example.pdf --skip-text-render`                                                                          | `false`                                |
| `--skip-reference-render`       | 참조문헌 렌더링 단계 건너뛰기                                                            | `pdf2zh_next example.pdf --skip-reference-render`                                                                     | `false`                                |
| `--skip-footnote-render`        | 각주 렌더링 단계 건너뛰기                                                                | `pdf2zh_next example.pdf --skip-footnote-render`                                                                      | `false`                                |
| `--skip-caption-render`         | 캡션 렌더링 단계 건너뛰기                                                                | `pdf2zh_next example.pdf --skip-caption-render`                                                                       | `false`                                |
| `--skip-header-render`          | 머리글 렌더링 단계 건너뛰기                                                              | `pdf2zh_next example.pdf --skip-header-render`                                                                        | `false`                                |
| `--skip-footer-render`          | 바닥글 렌더링 단계 건너뛰기                                                              | `pdf2zh_next example.pdf --skip-footer-render`                                                                        | `false`                                |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-second`       | Put translated pages second in dual PDF mode                                            | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `--dual-translate-both`         | Put translated pages both first and second in dual PDF mode                             | `pdf2zh_next example.pdf --dual-translate-both`                                                                       |
| `--dual-translate-none`         | Do not put translated pages in dual PDF mode                                            | `pdf2zh_next example.pdf --dual-translate-none`                                                                       |
| `--dual-translate-omit-original`| Omit original pages in dual PDF mode (only translated pages are included)               | `pdf2zh_next example.pdf --dual-translate-omit-original`                                                              |
| `--dual-translate-omit-translated`| Omit translated pages in dual PDF mode (only original pages are included)               | `pdf2zh_next example.pdf --dual-translate-omit-translated`                                                            |
| `--dual-page-num`               | Display page numbers in dual PDF mode                                                   | `pdf2zh_next example.pdf --dual-page-num`                                                                             |

---

### TRANSLATION

| `--dual-translate-first`        | 이중 PDF 모드에서 번역된 페이지를 먼저 배치합니다                                             | `pdf2zh_next example.pdf --dual-translate-first`                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--dual-translate-second`       | 이중 PDF 모드에서 번역된 페이지를 두 번째로 배치합니다                                          | `pdf2zh_next example.pdf --dual-translate-second`                                                                     |
| `--dual-translate-both`         | 이중 PDF 모드에서 번역된 페이지를 첫 번째와 두 번째 모두에 배치합니다                             | `pdf2zh_next example.pdf --dual-translate-both`                                                                       |
| `--dual-translate-none`         | 이중 PDF 모드에서 번역된 페이지를 배치하지 않습니다                                             | `pdf2zh_next example.pdf --dual-translate-none`                                                                       |
| `--dual-translate-omit-original`| 이중 PDF 모드에서 원본 페이지를 생략합니다 (번역된 페이지만 포함됨)                               | `pdf2zh_next example.pdf --dual-translate-omit-original`                                                              |
| `--dual-translate-omit-translated`| 이중 PDF 모드에서 번역된 페이지를 생략합니다 (원본 페이지만 포함됨)                               | `pdf2zh_next example.pdf --dual-translate-omit-translated`                                                            |
| `--dual-page-num`               | 이중 PDF 모드에서 페이지 번호를 표시합니다                                                   | `pdf2zh_next example.pdf --dual-page-num`                                                                             |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--disable-ocr`                 | Disable OCR                                                                             | `pdf2zh_next example.pdf --disable-ocr`                                                                              |
| `--disable-inline-math`         | Disable inline math translation                                                         | `pdf2zh_next example.pdf --disable-inline-math`                                                                      |
| `--disable-block-math`          | Disable block math translation                                                          | `pdf2zh_next example.pdf --disable-block-math`                                                                       |
| `--disable-table-translate`     | Disable table translation                                                               | `pdf2zh_next example.pdf --disable-table-translate`                                                                  |
| `--disable-figure-translate`    | Disable figure translation                                                              | `pdf2zh_next example.pdf --disable-figure-translate`                                                                  |
| `--disable-list-translate`      | Disable list translation                                                                 | `pdf2zh_next example.pdf --disable-list-translate`                                                                   |
| `--disable-footnote-translate`  | Disable footnote translation                                                            | `pdf2zh_next example.pdf --disable-footnote-translate`                                                                |
| `--disable-cite-translate`      | Disable citation translation                                                            | `pdf2zh_next example.pdf --disable-cite-translate`                                                                   |
| `--disable-code-translate`      | Disable code translation                                                                | `pdf2zh_next example.pdf --disable-code-translate`                                                                   |
| `--disable-formula-translate`   | Disable formula translation                                                             | `pdf2zh_next example.pdf --disable-formula-translate`                                                                |
| `--disable-symbol-translate`    | Disable symbol translation                                                              | `pdf2zh_next example.pdf --disable-symbol-translate`                                                                  |
| `--disable-abbr-translate`      | Disable abbreviation translation                                                        | `pdf2zh_next example.pdf --disable-abbr-translate`                                                                   |
| `--disable-caption-translate`   | Disable caption translation                                                             | `pdf2zh_next example.pdf --disable-caption-translate`                                                                 |
| `--disable-header-translate`    | Disable header translation                                                              | `pdf2zh_next example.pdf --disable-header-translate`                                                                 |
| `--disable-footer-translate`    | Disable footer translation                                                              | `pdf2zh_next example.pdf --disable-footer-translate`                                                                 |

---

### TRANSLATED TEXT

| `--disable-rich-text-translate` | 리치 텍스트 번역 비활성화                                                               | `pdf2zh_next example.pdf --disable-rich-text-translate`                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| `--disable-ocr`                 | OCR 비활성화                                                                             | `pdf2zh_next example.pdf --disable-ocr`                                                                              |
| `--disable-inline-math`         | 인라인 수식 번역 비활성화                                                         | `pdf2zh_next example.pdf --disable-inline-math`                                                                      |
| `--disable-block-math`          | 블록 수식 번역 비활성화                                                          | `pdf2zh_next example.pdf --disable-block-math`                                                                       |
| `--disable-table-translate`     | 표 번역 비활성화                                                               | `pdf2zh_next example.pdf --disable-table-translate`                                                                  |
| `--disable-figure-translate`    | 그림 번역 비활성화                                                              | `pdf2zh_next example.pdf --disable-figure-translate`                                                                  |
| `--disable-list-translate`      | 목록 번역 비활성화                                                                 | `pdf2zh_next example.pdf --disable-list-translate`                                                                   |
| `--disable-footnote-translate`  | 각주 번역 비활성화                                                            | `pdf2zh_next example.pdf --disable-footnote-translate`                                                                |
| `--disable-cite-translate`      | 인용 번역 비활성화                                                            | `pdf2zh_next example.pdf --disable-cite-translate`                                                                   |
| `--disable-code-translate`      | 코드 번역 비활성화                                                                | `pdf2zh_next example.pdf --disable-code-translate`                                                                   |
| `--disable-formula-translate`   | 공식 번역 비활성화                                                             | `pdf2zh_next example.pdf --disable-formula-translate`                                                                |
| `--disable-symbol-translate`    | 기호 번역 비활성화                                                              | `pdf2zh_next example.pdf --disable-symbol-translate`                                                                  |
| `--disable-abbr-translate`      | 약어 번역 비활성화                                                        | `pdf2zh_next example.pdf --disable-abbr-translate`                                                                   |
| `--disable-caption-translate`   | 캡션 번역 비활성화                                                             | `pdf2zh_next example.pdf --disable-caption-translate`                                                                 |
| `--disable-header-translate`    | 헤더 번역 비활성화                                                              | `pdf2zh_next example.pdf --disable-header-translate`                                                                 |
| `--disable-footer-translate`    | 푸터 번역 비활성화                                                              | `pdf2zh_next example.pdf --disable-footer-translate`                                                                 |
`--enhance-compatibility`       | 모든 호환성 향상 옵션을 활성화합니다.                                            | `pdf2zh_next example.pdf --enhance-compatibility`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--enhance-ocr`                 | Enable all OCR enhancement options                                                      | `pdf2zh_next example.pdf --enhance-ocr`                                                                               | `--enhance-ocr`                 | 모든 OCR 향상 옵션을 활성화합니다.                                                      | `pdf2zh_next example.pdf --enhance-ocr`                                                                               |
| `--enhance-table`               | Enable all table enhancement options                                                    | `pdf2zh_next example.pdf --enhance-table`                                                                             | `--enhance-table`               | 모든 테이블 향상 옵션을 활성화합니다.                                                    | `pdf2zh_next example.pdf --enhance-table`                                                                             |
| `--enhance-equation`             | Enable all equation enhancement options                                                 | `pdf2zh_next example.pdf --enhance-equation`                                                                          | `--enhance-equation`             | 모든 수식 향상 옵션을 활성화합니다.                                                 | `pdf2zh_next example.pdf --enhance-equation`                                                                          |
| `--enhance-reference`           | Enable all reference enhancement options                                                | `pdf2zh_next example.pdf --enhance-reference`                                                                         | `--enhance-reference`           | 모든 참조 향상 옵션을 활성화합니다.                                                | `pdf2zh_next example.pdf --enhance-reference`                                                                         |
| `--enhance-image`               | Enable all image enhancement options                                                    | `pdf2zh_next example.pdf --enhance-image`                                                                             | `--enhance-image`               | 모든 이미지 향상 옵션을 활성화합니다.                                                    | `pdf2zh_next example.pdf --enhance-image`                                                                             |
| `--enhance-code-block`          | Enable all code block enhancement options                                               | `pdf2zh_next example.pdf --enhance-code-block`                                                                       | `--enhance-code-block`          | 모든 코드 블록 향상 옵션을 활성화합니다.                                               | `pdf2zh_next example.pdf --enhance-code-block`                                                                       |
| `--enhance-page-number`         | Enable all page number enhancement options                                              | `pdf2zh_next example.pdf --enhance-page-number`                                                                      | `--enhance-page-number`         | 모든 페이지 번호 향상 옵션을 활성화합니다.                                              | `pdf2zh_next example.pdf --enhance-page-number`                                                                      |
| `--enhance-font`                | Enable all font enhancement options                                                     | `pdf2zh_next example.pdf --enhance-font`                                                                              | `--enhance-font`                | 모든 글꼴 향상 옵션을 활성화합니다.                                                     | `pdf2zh_next example.pdf --enhance-font`                                                                              |
| `--enhance-layout`              | Enable all layout enhancement options                                                   | `pdf2zh_next example.pdf --enhance-layout`                                                                            | `--enhance-layout`              | 모든 레이아웃 향상 옵션을 활성화합니다.                                                   | `pdf2zh_next example.pdf --enhance-layout`                                                                            |
| `--enhance-paragraph`           | Enable all paragraph enhancement options                                                 | `pdf2zh_next example.pdf --enhance-paragraph`                                                                         | `--enhance-paragraph`           | 모든 단락 향상 옵션을 활성화합니다.                                                 | `pdf2zh_next example.pdf --enhance-paragraph`                                                                         |
| `--enhance-list`                | Enable all list enhancement options                                                      | `pdf2zh_next example.pdf --enhance-list`                                                                              | `--enhance-list`                | 모든 목록 향상 옵션을 활성화합니다.                                                      | `pdf2zh_next example.pdf --enhance-list`                                                                              |
| `--enhance-heading`             | Enable all heading enhancement options                                                  | `pdf2zh_next example.pdf --enhance-heading`                                                                            | `--enhance-heading`             | 모든 제목 향상 옵션을 활성화합니다.                                                  | `pdf2zh_next example.pdf --enhance-heading`                                                                            |

---

### OUTPUT
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | Use alternating pages mode for single PDF                                               | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                               |
| `--use-columns-dual`             | Use columns mode for dual PDF                                                           | `pdf2zh_next example.pdf --use-columns-dual`                                                                          |
| `--use-columns-single`           | Use columns mode for single PDF                                                         | `pdf2zh_next example.pdf --use-columns-single`                                                                        |
| `--use-rows-dual`                | Use rows mode for dual PDF                                                              | `pdf2zh_next example.pdf --use-rows-dual`                                                                             |
| `--use-rows-single`              | Use rows mode for single PDF                                                            | `pdf2zh_next example.pdf --use-rows-single`                                                                           |
| `--use-vertical-dual`            | Use vertical mode for dual PDF                                                          | `pdf2zh_next example.pdf --use-vertical-dual`                                                                         |
| `--use-vertical-single`          | Use vertical mode for single PDF                                                        | `pdf2zh_next example.pdf --use-vertical-single`                                                                       |
| `--use-vertical-right-dual`      | Use vertical-right mode for dual PDF                                                    | `pdf2zh_next example.pdf --use-vertical-right-dual`                                                                   |
| `--use-vertical-right-single`    | Use vertical-right mode for single PDF                                                  | `pdf2zh_next example.pdf --use-vertical-right-single`                                                                 |
| `--use-none`                     | Use none mode (default)                                                                 | `pdf2zh_next example.pdf --use-none`                                                                                  |
| `--use-ai-mode`                  | Use AI mode (requires `--openai-key`)                                                   | `pdf2zh_next example.pdf --use-ai-mode --openai-key <your-openai-key>`                                                |
| `--use-ai-mode-azure`            | Use AI mode for Azure (requires `--openai-key`, `--openai-base`, `--openai-version`)    | `pdf2zh_next example.pdf --use-ai-mode-azure --openai-key <your-openai-key> --openai-base <your-openai-base> --openai-version <your-openai-version>` |

---

### TRANSLATION

| `--use-alternating-pages-dual`  | 이중 PDF 에 대해 번갈아 가는 페이지 모드 사용                                                 | `pdf2zh_next example.pdf --use-alternating-pages-dual`                                                                |
| :------------------------------ | :------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------- |
| `--use-alternating-pages-single` | 단일 PDF 에 대해 번갈아 가는 페이지 모드 사용                                                 | `pdf2zh_next example.pdf --use-alternating-pages-single`                                                               |
| `--use-columns-dual`             | 이중 PDF 에 대해 열 모드 사용                                                                 | `pdf2zh_next example.pdf --use-columns-dual`                                                                          |
| `--use-columns-single`           | 단일 PDF 에 대해 열 모드 사용                                                                 | `pdf2zh_next example.pdf --use-columns-single`                                                                        |
| `--use-rows-dual`                | 이중 PDF 에 대해 행 모드 사용                                                                 | `pdf2zh_next example.pdf --use-rows-dual`                                                                             |
| `--use-rows-single`              | 단일 PDF 에 대해 행 모드 사용                                                                 | `pdf2zh_next example.pdf --use-rows-single`                                                                           |
| `--use-vertical-dual`            | 이중 PDF 에 대해 세로 모드 사용                                                               | `pdf2zh_next example.pdf --use-vertical-dual`                                                                         |
| `--use-vertical-single`          | 단일 PDF 에 대해 세로 모드 사용                                                               | `pdf2zh_next example.pdf --use-vertical-single`                                                                       |
| `--use-vertical-right-dual`      | 이중 PDF 에 대해 오른쪽 세로 모드 사용                                                        | `pdf2zh_next example.pdf --use-vertical-right-dual`                                                                   |
| `--use-vertical-right-single`    | 단일 PDF 에 대해 오른쪽 세로 모드 사용                                                        | `pdf2zh_next example.pdf --use-vertical-right-single`                                                                 |
| `--use-none`                     | 모드 미사용 (기본값)                                                                         | `pdf2zh_next example.pdf --use-none`                                                                                  |
| `--use-ai-mode`                  | AI 모드 사용 (`--openai-key` 필요)                                                           | `pdf2zh_next example.pdf --use-ai-mode --openai-key <your-openai-key>`                                                |
| `--use-ai-mode-azure`            | Azure 용 AI 모드 사용 (`--openai-key`, `--openai-base`, `--openai-version` 필요)              | `pdf2zh_next example.pdf --use-ai-mode-azure --openai-key <your-openai-key> --openai-base <your-openai-base> --openai-version <your-openai-version>` |
`watermark`         | `watermark` (default), `no_watermark`, `watermark_only` |
| `--watermark-only`              | Output only the watermark layer                                                         | `pdf2zh_next example.pdf --watermark-only`                                                                            | `watermark_only`     | `false` (default), `true`                               |
| `--watermark`                   | Watermark text                                                                          | `pdf2zh_next example.pdf --watermark "Confidential"`                                                                  | `watermark`          | `null`                                                   |

---

### OUTPUT

| `--watermark-output-mode`       | PDF 파일의 워터마크 출력 모드                                                     | `pdf2zh_next example.pdf --watermark-output-mode no_watermark`                                                        | `watermark`         | `watermark` (기본값), `no_watermark`, `watermark_only` |
| `--watermark-only`              | 워터마크 레이어만 출력                                                         | `pdf2zh_next example.pdf --watermark-only`                                                                            | `watermark_only`     | `false` (기본값), `true`                               |
| `--watermark`                   | 워터마크 텍스트                                                                          | `pdf2zh_next example.pdf --watermark "Confidential"`                                                                  | `watermark`          | `null`                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-chars-per-part`          | Maximum characters per part for split translation                                       | `pdf2zh_next example.pdf --max-chars-per-part 3000`                                                                   |
| `--max-parts-per-request`       | Maximum parts per request for split translation                                         | `pdf2zh_next example.pdf --max-parts-per-request 50`                                                                  |
| `--split-strategy`              | Strategy for splitting content, options: `page`, `auto`                                 | `pdf2zh_next example.pdf --split-strategy page`                                                                       |
| `--max-retries`                 | Maximum retry attempts for failed translations                                          | `pdf2zh_next example.pdf --max-retries 5`                                                                             |
| `--retry-delay`                 | Delay (in seconds) between retry attempts                                               | `pdf2zh_next example.pdf --retry-delay 3`                                                                             |
| `--timeout`                     | Timeout (in seconds) for each translation request                                       | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--concurrent`                  | Number of concurrent translation requests                                               | `pdf2zh_next example.pdf --concurrent 5`                                                                              |
| `--proxy`                       | Proxy server address (e.g., `http://127.0.0.1:7890`)                                    | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--api-key`                     | API key for translation service                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      |
| `--model`                       | Model name for translation service (e.g., `gpt-3.5-turbo`)                              | `pdf2zh_next example.pdf --model gpt-3.5-turbo`                                                                       |
| `--temperature`                 | Temperature parameter for translation model (0.0 to 1.0)                                | `pdf2zh_next example.pdf --temperature 0.5`                                                                           |
| `--max-tokens`                  | Maximum tokens for translation model                                                    | `pdf2zh_next example.pdf --max-tokens 2000`                                                                           |
| `--top-p`                       | Top-p parameter for translation model (0.0 to 1.0)                                      | `pdf2zh_next example.pdf --top-p 0.9`                                                                                 |
| `--frequency-penalty`           | Frequency penalty parameter for translation model (-2.0 to 2.0)                         | `pdf2zh_next example.pdf --frequency-penalty 0.0`                                                                     |
| `--presence-penalty`            | Presence penalty parameter for translation model (-2.0 to 2.0)                          | `pdf2zh_next example.pdf --presence-penalty 0.0`                                                                      |
| `--stop`                        | Stop sequences for translation model (comma-separated)                                  | `pdf2zh_next example.pdf --stop "###, END"`                                                                           |
| `--log-level`                   | Log level (e.g., `DEBUG`, `INFO`, `WARNING`, `ERROR`)                                   | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--log-file`                    | Log file path                                                                           | `pdf2zh_next example.pdf --log-file ./logs/translation.log`                                                            |
| `--no-color`                    | Disable colored output                                                                  | `pdf2zh_next example.pdf --no-color`                                                                                  |
| `--dry-run`                     | Perform a dry run without actual translation                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | Show version information                                                                | `pdf2zh_next --version`                                                                                               |
| `--help`                        | Show help message                                                                       | `pdf2zh_next --help`                                                                                                  |

---

### OUTPUT

| `--max-pages-per-part`          | 부분별 최대 페이지 수 (분할 번역용)                                            | `pdf2zh_next example.pdf --max-pages-per-part 50`                                                                     |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--max-chars-per-part`          | 부분별 최대 문자 수 (분할 번역용)                                       | `pdf2zh_next example.pdf --max-chars-per-part 3000`                                                                   |
| `--max-parts-per-request`       | 요청당 최대 부분 수 (분할 번역용)                                         | `pdf2zh_next example.pdf --max-parts-per-request 50`                                                                  |
| `--split-strategy`              | 콘텐츠 분할 전략, 옵션: `page`, `auto`                                 | `pdf2zh_next example.pdf --split-strategy page`                                                                       |
| `--max-retries`                 | 실패한 번역 시도 최대 재시도 횟수                                          | `pdf2zh_next example.pdf --max-retries 5`                                                                             |
| `--retry-delay`                 | 재시도 간 지연 시간 (초 단위)                                               | `pdf2zh_next example.pdf --retry-delay 3`                                                                             |
| `--timeout`                     | 각 번역 요청에 대한 타임아웃 (초 단위)                                       | `pdf2zh_next example.pdf --timeout 60`                                                                                |
| `--concurrent`                  | 동시 번역 요청 수                                               | `pdf2zh_next example.pdf --concurrent 5`                                                                              |
| `--proxy`                       | 프록시 서버 주소 (예: `http://127.0.0.1:7890`)                                    | `pdf2zh_next example.pdf --proxy http://127.0.0.1:7890`                                                               |
| `--api-key`                     | 번역 서비스 API 키                                                         | `pdf2zh_next example.pdf --api-key YOUR_API_KEY`                                                                      |
| `--model`                       | 번역 서비스 모델 이름 (예: `gpt-3.5-turbo`)                              | `pdf2zh_next example.pdf --model gpt-3.5-turbo`                                                                       |
| `--temperature`                 | 번역 모델 온도 매개변수 (0.0 ~ 1.0)                                | `pdf2zh_next example.pdf --temperature 0.5`                                                                           |
| `--max-tokens`                  | 번역 모델 최대 토큰 수                                                    | `pdf2zh_next example.pdf --max-tokens 2000`                                                                           |
| `--top-p`                       | 번역 모델 Top-p 매개변수 (0.0 ~ 1.0)                                      | `pdf2zh_next example.pdf --top-p 0.9`                                                                                 |
| `--frequency-penalty`           | 번역 모델 빈도 패널티 매개변수 (-2.0 ~ 2.0)                         | `pdf2zh_next example.pdf --frequency-penalty 0.0`                                                                     |
| `--presence-penalty`            | 번역 모델 존재 패널티 매개변수 (-2.0 ~ 2.0)                          | `pdf2zh_next example.pdf --presence-penalty 0.0`                                                                      |
| `--stop`                        | 번역 모델 중지 시퀀스 (쉼표로 구분)                                  | `pdf2zh_next example.pdf --stop "###, END"`                                                                           |
| `--log-level`                   | 로그 레벨 (예: `DEBUG`, `INFO`, `WARNING`, `ERROR`)                                   | `pdf2zh_next example.pdf --log-level DEBUG`                                                                           |
| `--log-file`                    | 로그 파일 경로                                                                           | `pdf2zh_next example.pdf --log-file ./logs/translation.log`                                                            |
| `--no-color`                    | 컬러 출력 비활성화                                                                  | `pdf2zh_next example.pdf --no-color`                                                                                  |
| `--dry-run`                     | 실제 번역 없이 드라이 런 수행                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `--version`                     | 버전 정보 표시                                                                | `pdf2zh_next --version`                                                                                               |
| `--help`                        | 도움말 메시지 표시                                                                       | `pdf2zh_next --help`                                                                                                  |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | Method to translate table text (experimental)                                           | `pdf2zh_next example.pdf --translate-table-text-method="separate"`                                                    |
| `--translate-table-text-type`   | Type of table text to translate (experimental)                                          | `pdf2zh_next example.pdf --translate-table-text-type="table"`                                                         |
| `--translate-table-text-only`   | Only translate table text (experimental)                                                | `pdf2zh_next example.pdf --translate-table-text-only`                                                                 |
| `-o`, `--output`                | Path to output translated file                                                          | `pdf2zh_next example.pdf -o translated.md`                                                                            |
| `-f`, `--format`                | Output format. Options: `markdown`, `html`                                              | `pdf2zh_next example.pdf -f html`                                                                                     |
| `-s`, `--source-language`       | Source language for translation. See [Language Code](LANGUAGE_CODE.md) for more details | `pdf2zh_next example.pdf -s en`                                                                                       |
| `-t`, `--target-language`       | Target language for translation. See [Language Code](LANGUAGE_CODE.md) for more details | `pdf2zh_next example.pdf -t zh`                                                                                       |
| `-m`, `--model`                 | Translation model to use. See [Documentation of Translation Services](TRANSLATE.md)     | `pdf2zh_next example.pdf -m google`                                                                                   |
| `-k`, `--api-key`               | API key for translation service                                                         | `pdf2zh_next example.pdf -k "your-api-key"`                                                                           |
| `--api-base`                    | API base URL for translation service                                                    | `pdf2zh_next example.pdf --api-base "https://api.example.com"`                                                        |
| `--api-version`                 | API version for translation service                                                     | `pdf2zh_next example.pdf --api-version "2023-05-15"`                                                                  |
| `--max-concurrent-requests`     | Maximum number of concurrent requests to translation service                            | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 |
| `--max-characters-per-request`  | Maximum characters per request to translation service                                   | `pdf2zh_next example.pdf --max-characters-per-request 1000`                                                           |
| `--dry-run`                     | Perform a dry run without actual translation                                            | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `-v`, `--verbose`               | Enable verbose output                                                                   | `pdf2zh_next example.pdf -v`                                                                                          |
| `-q`, `--quiet`                 | Suppress non-essential output                                                           | `pdf2zh_next example.pdf -q`                                                                                          |
| `--version`                     | Show version information and exit                                                       | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | Show help message and exit                                                              | `pdf2zh_next -h`                                                                                                      |

---

### TRANSLATION RESULT

| `--translate-table-text`        | 표  텍스트 번역 (실험적 기능)                                                                 | `pdf2zh_next example.pdf --translate-table-text`                                                                      |
| :------------------------------ | :------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| `--translate-table-text-method` | 표  텍스트 번역 방법 (실험적 기능)                                                               | `pdf2zh_next example.pdf --translate-table-text-method="separate"`                                                    |
| `--translate-table-text-type`   | 번역할 표 텍스트 유형 (실험적 기능)                                                              | `pdf2zh_next example.pdf --translate-table-text-type="table"`                                                         |
| `--translate-table-text-only`   | 표  텍스트만 번역 (실험적 기능)                                                                 | `pdf2zh_next example.pdf --translate-table-text-only`                                                                 |
| `-o`, `--output`                | 번역된 파일 출력 경로                                                                          | `pdf2zh_next example.pdf -o translated.md`                                                                            |
| `-f`, `--format`                | 출력 형식.  옵션: `markdown`, `html`                                                          | `pdf2zh_next example.pdf -f html`                                                                                     |
| `-s`, `--source-language`       | 번역 소스 언어. 자세한 내용은 [Language Code](LANGUAGE_CODE.md) 참조                             | `pdf2zh_next example.pdf -s en`                                                                                       |
| `-t`, `--target-language`       | 번역 대상 언어. 자세한 내용은 [Language Code](LANGUAGE_CODE.md) 참조                             | `pdf2zh_next example.pdf -t zh`                                                                                       |
| `-m`, `--model`                 | 사용할 번역 모델. 자세한 내용은 [Documentation of Translation Services](TRANSLATE.md) 참조        | `pdf2zh_next example.pdf -m google`                                                                                   |
| `-k`, `--api-key`               | 번역 서비스 API 키                                                                            | `pdf2zh_next example.pdf -k "your-api-key"`                                                                           |
| `--api-base`                    | 번역 서비스 API 기본 URL                                                                     | `pdf2zh_next example.pdf --api-base "https://api.example.com"`                                                        |
| `--api-version`                 | 번역 서비스 API 버전                                                                         | `pdf2zh_next example.pdf --api-version "2023-05-15"`                                                                  |
| `--max-concurrent-requests`     | 번역 서비스에 대한 최대 동시 요청 수                                                              | `pdf2zh_next example.pdf --max-concurrent-requests 5`                                                                 |
| `--max-characters-per-request`  | 번역 서비스에 대한 요청당 최대 문자 수                                                             | `pdf2zh_next example.pdf --max-characters-per-request 1000`                                                           |
| `--dry-run`                     | 실제 번역 없이 시뮬레이션 실행                                                                 | `pdf2zh_next example.pdf --dry-run`                                                                                   |
| `-v`, `--verbose`               | 상세 출력 활성화                                                                              | `pdf2zh_next example.pdf -v`                                                                                          |
| `-q`, `--quiet`                 | 불필요한 출력  억제                                                                             | `pdf2zh_next example.pdf -q`                                                                                          |
| `--version`                     | 버전 정보 표시 및 종료                                                                         | `pdf2zh_next --version`                                                                                               |
| `-h`, `--help`                  | 도움말 메시지 표시 및 종료                                                                      | `pdf2zh_next -h`                                                                                                      |
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | 
| `--skip-scanned-detection=true` | Skip scanned detection                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               | 
| `--skip-scanned-detection=false`| Perform scanned detection (default)                                                     | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              | 
| `--scanned-detection-method`    | Scanned detection method. Options: 'tesseract', 'ocrmypdf', 'ocrmypdf_engine', 'pdf2image' | `pdf2zh_next example.pdf --scanned-detection-method ocrmypdf`                                                         | 
| `--scanned-detection-threshold` | Scanned detection threshold (0-1). Default is 0.5                                       | `pdf2zh_next example.pdf --scanned-detection-threshold 0.7`                                                           | 
| `--scanned-detection-dpi`       | DPI for scanned detection. Default is 300                                               | `pdf2zh_next example.pdf --scanned-detection-dpi 200`                                                                 | 
| `--scanned-detection-timeout`   | Timeout for scanned detection in seconds. Default is 60                                 | `pdf2zh_next example.pdf --scanned-detection-timeout 120`                                                             | 
| `--scanned-detection-language`  | Language for scanned detection. Default is 'eng'                                        | `pdf2zh_next example.pdf --scanned-detection-language eng`                                                            | 
| `--scanned-detection-whitelist` | Whitelist for scanned detection. Default is 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' | `pdf2zh_next example.pdf --scanned-detection-whitelist abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789` | 
| `--scanned-detection-blacklist` | Blacklist for scanned detection. Default is ''                                          | `pdf2zh_next example.pdf --scanned-detection-blacklist '!@#$%^&*()_+-=[]{}|;:,.<>?/'`                                 | 

---

### TRANSLATED TEXT

| `--skip-scanned-detection`      | 스캔된 문서 감지 건너뛰기                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection`                                                                    | 
| ------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | 
| `--skip-scanned-detection=true` | 스캔된 문서 감지 건너뛰기                                                                  | `pdf2zh_next example.pdf --skip-scanned-detection=true`                                                               | 
| `--skip-scanned-detection=false`| 스캔된 문서 감지 수행 (기본값)                                                              | `pdf2zh_next example.pdf --skip-scanned-detection=false`                                                              | 
| `--scanned-detection-method`    | 스캔된 문서 감지 방법. 옵션: 'tesseract', 'ocrmypdf', 'ocrmypdf_engine', 'pdf2image' | `pdf2zh_next example.pdf --scanned-detection-method ocrmypdf`                                                         | 
| `--scanned-detection-threshold` | 스캔된 문서 감지 임계값 (0-1). 기본값은 0.5                                       | `pdf2zh_next example.pdf --scanned-detection-threshold 0.7`                                                           | 
| `--scanned-detection-dpi`       | 스캔된 문서 감지 DPI. 기본값은 300                                               | `pdf2zh_next example.pdf --scanned-detection-dpi 200`                                                                 | 
| `--scanned-detection-timeout`   | 스캔된 문서 감지 타임아웃 (초 단위). 기본값은 60                                 | `pdf2zh_next example.pdf --scanned-detection-timeout 120`                                                             | 
| `--scanned-detection-language`  | 스캔된 문서 감지 언어. 기본값은 'eng'                                        | `pdf2zh_next example.pdf --scanned-detection-language eng`                                                            | 
| `--scanned-detection-whitelist` | 스캔된 문서 감지 화이트리스트. 기본값은 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' | `pdf2zh_next example.pdf --scanned-detection-whitelist abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789` | 
| `--scanned-detection-blacklist` | 스캔된 문서 감지 블랙리스트. 기본값은 ''                                          | `pdf2zh_next example.pdf --scanned-detection-blacklist '!@#$%^&*()_+-=[]{}|;:,.<>?/'`                                 |
---

### OUTPUT

| `--ocr-workaround`              | 번역된 텍스트를 검정색으로 강제 설정하고  흰색 배경을 추가합니다.                              | `pdf2zh_next example.pdf --ocr-workaround`                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--ocr-workaround-threshold`    | Threshold for auto-enabling OCR workaround. Lower values make OCR more likely to be enabled. (default: 0.8)                                                                                         | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.6`                   |
| `--ocr-workaround-skip-pages`   | Number of initial pages to skip for scan detection. Useful for documents with cover pages that may be misdetected. (default: 0)                                                                      | `pdf2zh_next example.pdf --ocr-workaround-skip-pages 1`                    |
| `--ocr-workaround-sample-pages` | Number of pages to sample for scan detection. Higher values improve accuracy but increase processing time. (default: 3)                                                                              | `pdf2zh_next example.pdf --ocr-workaround-sample-pages 5`                  |
| `--ocr-workaround-min-density`  | Minimum text density threshold for considering a page as scanned. Lower values make pages more likely to be detected as scanned. (default: 0.01)                                                     | `pdf2zh_next example.pdf --ocr-workaround-min-density 0.005`               |

---

### OUTPUT

| `--auto-enable-ocr-workaround`  | 자동 OCR 우회 기능을 활성화합니다. 문서가 심하게 스캔된 것으로 감지되면 OCR 처리를 활성화하고 추가 스캔 감지를 건너뜁니다. 자세한 내용은 문서를 참조하세요. (기본값: False) | `pdf2zh_next example.pdf --auto-enable-ocr-workaround`                     |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `--ocr-workaround-threshold`    | 자동 OCR 우회 활성화 임계값. 값이 낮을수록 OCR 이 활성화될 가능성이 높아집니다. (기본값: 0.8)                                                                                  | `pdf2zh_next example.pdf --ocr-workaround-threshold 0.6`                   |
| `--ocr-workaround-skip-pages`   | 스캔 감지를 위해 건너뛸 초기 페이지 수. 표지 페이지가 잘못 감지될 수 있는 문서에 유용합니다. (기본값: 0)                                                                          | `pdf2zh_next example.pdf --ocr-workaround-skip-pages 1`                    |
| `--ocr-workaround-sample-pages` | 스캔 감지용 샘플 페이지 수. 값이 높을수록 정확도가 향상되지만 처리 시간이 증가합니다. (기본값: 3)                                                                                | `pdf2zh_next example.pdf --ocr-workaround-sample-pages 5`                  |
| `--ocr-workaround-min-density`  | 페이지를 스캔된 것으로 간주하기 위한 최소 텍스트 밀도 임계값. 값이 낮을수록 페이지가 스캔된 것으로 감지될 가능성이 높아집니다. (기본값: 0.01)                                               | `pdf2zh_next example.pdf --ocr-workaround-min-density 0.005`               |
| `--only-include-translated-page`| 번역된 페이지만 출력 PDF 에 포함합니다. --pages 가 사용된 경우에만 유효합니다. | `pdf2zh_next example.pdf --pages 1-5 --only-include-translated-page`                                                  |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `--no-merge-lines`                    | Disable the merging of lines into paragraphs                                                    | `pdf2zh_next example.pdf --no-merge-lines`                                                                   |

---

### TRANSLATION

| `--no-merge-alternating-line-numbers` | 줄 번호가 있는 문서에서 교대로 나오는 줄 번호와 텍스트 단락의 병합을 비활성화합니다 | `pdf2zh_next example.pdf --no-merge-alternating-line-numbers`                                                |
| :------------------------------------ | :---------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- |
| `--no-merge-lines`                    | 줄을 단락으로 병합하는 기능을 비활성화합니다                                                    | `pdf2zh_next example.pdf --no-merge-lines`                                                                   |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-english-lines` | Disable removal of non-English lines within paragraph areas                             | `pdf2zh_next example.pdf --no-remove-non-english-lines`                                                                |
| `--no-remove-non-chinese-lines` | Disable removal of non-Chinese lines within paragraph areas                             | `pdf2zh_next example.pdf --no-remove-non-chinese-lines`                                                                |
| `--remove-non-chinese-lines`    | Remove non-Chinese lines within paragraph areas (default)                               | `pdf2zh_next example.pdf --remove-non-chinese-lines`                                                                   |
| `--remove-non-english-lines`    | Remove non-English lines within paragraph areas (default)                               | `pdf2zh_next example.pdf --remove-non-english-lines`                                                                   |
| `--remove-non-formula-lines`    | Remove non-formula lines within paragraph areas (default)                               | `pdf2zh_next example.pdf --remove-non-formula-lines`                                                                   |
| `--save-translated-only`        | Save only the translated pages                                                          | `pdf2zh_next example.pdf --save-translated-only`                                                                       |
| `--save-original-only`          | Save only the original pages                                                            | `pdf2zh_next example.pdf --save-original-only`                                                                         |
| `--save-both`                   | Save both original and translated pages (default)                                       | `pdf2zh_next example.pdf --save-both`                                                                                  |
| `--save-format`                 | Output format for the translated document. Options: `pdf`, `docx`, `pptx` (default: pdf) | `pdf2zh_next example.pdf --save-format docx`                                                                           |

---

### TRANSLATION RESULT

| `--no-remove-non-formula-lines` | 단락 영역 내에서 수식이 아닌 줄 제거 비활성화                             | `pdf2zh_next example.pdf --no-remove-non-formula-lines`                                                                |
| :------------------------------ | :-------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- |
| `--no-remove-non-english-lines` | 단락 영역 내에서 영어가 아닌 줄 제거 비활성화                             | `pdf2zh_next example.pdf --no-remove-non-english-lines`                                                                |
| `--no-remove-non-chinese-lines` | 단락 영역 내에서 중국어가 아닌 줄 제거 비활성화                             | `pdf2zh_next example.pdf --no-remove-non-chinese-lines`                                                                |
| `--remove-non-chinese-lines`    | 단락 영역 내에서 중국어가 아닌 줄 제거 (기본값)                               | `pdf2zh_next example.pdf --remove-non-chinese-lines`                                                                   |
| `--remove-non-english-lines`    | 단락 영역 내에서 영어가 아닌 줄 제거 (기본값)                               | `pdf2zh_next example.pdf --remove-non-english-lines`                                                                   |
| `--remove-non-formula-lines`    | 단락 영역 내에서 수식이 아닌 줄 제거 (기본값)                               | `pdf2zh_next example.pdf --remove-non-formula-lines`                                                                   |
| `--save-translated-only`        | 번역된 페이지만 저장                                                          | `pdf2zh_next example.pdf --save-translated-only`                                                                       |
| `--save-original-only`          | 원본 페이지만 저장                                                            | `pdf2zh_next example.pdf --save-original-only`                                                                         |
| `--save-both`                   | 원본 및 번역된 페이지 모두 저장 (기본값)                                       | `pdf2zh_next example.pdf --save-both`                                                                                  |
| `--save-format`                 | 번역된 문서의 출력 형식. 옵션: `pdf`, `docx`, `pptx` (기본값: pdf) | `pdf2zh_next example.pdf --save-format docx`                                                                           |
`0.8`    |
| `--non-formula-line-font-size-ratio` | Set font size ratio threshold for identifying non-formula lines (0.0-1.0)            | `pdf2zh_next example.pdf --non-formula-line-font-size-ratio 0.85`                                                     | `0.8`    |
| `--non-formula-line-font-family-similarity` | Set font family similarity threshold for identifying non-formula lines (0.0-1.0)    | `pdf2zh_next example.pdf --non-formula-line-font-family-similarity 0.85`                                              | `0.8`    |

---

### OUTPUT

| `--non-formula-line-iou-threshold` | 비수식 라인 식별을 위한 IoU 임계값 설정 (0.0-1.0)                      | `pdf2zh_next example.pdf --non-formula-line-iou-threshold 0.85`                                                       | `0.8`    |
| `--non-formula-line-font-size-ratio` | 비수식 라인 식별을 위한 글꼴 크기 비율 임계값 설정 (0.0-1.0)            | `pdf2zh_next example.pdf --non-formula-line-font-size-ratio 0.85`                                                     | `0.8`    |
| `--non-formula-line-font-family-similarity` | 비수식 라인 식별을 위한 글꼴 패밀리 유사도 임계값 설정 (0.0-1.0)    | `pdf2zh_next example.pdf --non-formula-line-font-family-similarity 0.85`                                              | `0.8`    |
| `--figure-table-protection-threshold` | 그림과 표에 대한 보호 임계값 설정 (0.0-1.0). 그림/표 내부의 라인은 처리되지 않음 | `pdf2zh_next example.pdf --figure-table-protection-threshold 0.95`                                        |
---

### TRANSLATED TEXT

| `--skip-formula-offset-calculation` | 처리 중 수식 오프셋 계산 생략          | `pdf2zh_next example.pdf --skip-formula-offset-calculation`                                                           |


##### GUI 인수

| `--server_name <server_name>`   | Set server name                        | `pdf2zh_next --gui --server_name 192.168.1.100` |
| `--server_port <server_port>`   | Set server port                        | `pdf2zh_next --gui --server_port 7861`          |
| `--concurrency_count <count>`   | Set the number of concurrent processes | `pdf2zh_next --gui --concurrency_count 10`      |
| `--queue_count <count>`         | Set the number of queues               | `pdf2zh_next --gui --queue_count 5`             |
| `--max_file_size <size>`        | Set the maximum file size              | `pdf2zh_next --gui --max_file_size 100`         |
| `--allowed_file_types <types>`  | Set allowed file types                 | `pdf2zh_next --gui --allowed_file_types pdf`    |
| `--enable_webui_api`            | Enable WebUI API                       | `pdf2zh_next --gui --enable_webui_api`          |
| `--enable_cors`                 | Enable CORS                            | `pdf2zh_next --gui --enable_cors`               |
| `--enable_cors_header <header>` | Set CORS header                        | `pdf2zh_next --gui --enable_cors_header <header>` |

---

### OUTPUT

| 옵션                          | 기능                               | 예시                                         |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--share`                       | 공유 모드 활성화                    | `pdf2zh_next --gui --share`                     |
| `--server_name <server_name>`   | 서버 이름 설정                        | `pdf2zh_next --gui --server_name 192.168.1.100` |
| `--server_port <server_port>`   | 서버 포트 설정                        | `pdf2zh_next --gui --server_port 7861`          |
| `--concurrency_count <count>`   | 동시 프로세스 수 설정 | `pdf2zh_next --gui --concurrency_count 10`      |
| `--queue_count <count>`         | 큐 수 설정               | `pdf2zh_next --gui --queue_count 5`             |
| `--max_file_size <size>`        | 최대 파일 크기 설정              | `pdf2zh_next --gui --max_file_size 100`         |
| `--allowed_file_types <types>`  | 허용된 파일 유형 설정                 | `pdf2zh_next --gui --allowed_file_types pdf`    |
| `--enable_webui_api`            | WebUI API 활성화                       | `pdf2zh_next --gui --enable_webui_api`          |
| `--enable_cors`                 | CORS 활성화                            | `pdf2zh_next --gui --enable_cors`               |
| `--enable_cors_header <header>` | CORS 헤더 설정                        | `pdf2zh_next --gui --enable_cors_header <header>` |
---

### OUTPUT

| `--auth-file`                   | 인증 파일 경로        | `pdf2zh_next --gui --auth-file /path`           |
Show the welcome page instead of the main page |
| `--disable-welcome-page`        | Disable the welcome page               | `pdf2zh_next --gui --disable-welcome-page`      | Disable the welcome page                       |
| `--disable-update-check`        | Disable update check                    | `pdf2zh_next --gui --disable-update-check`      | Disable update check                           |
| `--disable-auto-update`         | Disable auto update                     | `pdf2zh_next --gui --disable-auto-update`        | Disable auto update                            |
| `--disable-auto-update-check`   | Disable auto update check               | `pdf2zh_next --gui --disable-auto-update-check` | Disable auto update check                      |
| `--disable-auto-update-download`| Disable auto update download            | `pdf2zh_next --gui --disable-auto-update-download` | Disable auto update download                 |
| `--disable-auto-update-install` | Disable auto update install             | `pdf2zh_next --gui --disable-auto-update-install` | Disable auto update install                  |
| `--disable-auto-update-restart` | Disable auto update restart             | `pdf2zh_next --gui --disable-auto-update-restart` | Disable auto update restart                  |

---

### OUTPUT

| `--welcome-page`                | 환영 페이지 HTML 파일 경로             | `pdf2zh_next --gui --welcome-page /path`        | 메인 페이지 대신 환영 페이지 표시             |
| `--disable-welcome-page`        | 환영 페이지 비활성화                   | `pdf2zh_next --gui --disable-welcome-page`      | 환영 페이지 비활성화                         |
| `--disable-update-check`        | 업데이트 확인 비활성화                 | `pdf2zh_next --gui --disable-update-check`      | 업데이트 확인 비활성화                       |
| `--disable-auto-update`         | 자동 업데이트 비활성화                 | `pdf2zh_next --gui --disable-auto-update`        | 자동 업데이트 비활성화                       |
| `--disable-auto-update-check`   | 자동 업데이트 확인 비활성화            | `pdf2zh_next --gui --disable-auto-update-check` | 자동 업데이트 확인 비활성화                  |
| `--disable-auto-update-download`| 자동 업데이트 다운로드 비활성화        | `pdf2zh_next --gui --disable-auto-update-download` | 자동 업데이트 다운로드 비활성화            |
| `--disable-auto-update-install` | 자동 업데이트 설치 비활성화            | `pdf2zh_next --gui --disable-auto-update-install` | 자동 업데이트 설치 비활성화                |
| `--disable-auto-update-restart` | 자동 업데이트 재시작 비활성화          | `pdf2zh_next --gui --disable-auto-update-restart` | 자동 업데이트 재시작 비활성화              |
|
| ------------------------------- | -------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--disabled-services`           | Disabled translation services          | `pdf2zh_next --gui --disabled-services "Bing"`       |                                                                                                                              |
| `--service-configs`             | Service configs                        | `pdf2zh_next --gui --service-configs "Bing:xxx,xxx"` | Please refer to [Documentation of Translation Services](https://pdf2zh-next.com/advanced/SERVICE.html) for more information. |
| `--concurrent`                  | Concurrent translation tasks           | `pdf2zh_next --gui --concurrent 5`                   |                                                                                                                              |
| `--source-language`             | Source language                        | `pdf2zh_next --gui --source-language en`             | Please refer to [Supported Languages](https://pdf2zh-next.com/advanced/LANGUAGE.html) for more information.                  |
| `--target-language`             | Target language                        | `pdf2zh_next --gui --target-language zh-CN`          | Please refer to [Supported Languages](https://pdf2zh-next.com/advanced/LANGUAGE.html) for more information.                  |
| `--translate-tags`              | Translate tags                         | `pdf2zh_next --gui --translate-tags "p,span"`        |                                                                                                                              |
| `--translate-attributes`        | Translate attributes                   | `pdf2zh_next --gui --translate-attributes "title"`   |                                                                                                                              |
| `--size-limit`                  | Size limit for single request (bytes)  | `pdf2zh_next --gui --size-limit 2000`                |                                                                                                                              |
| `--request-interval`            | Request interval (ms)                  | `pdf2zh_next --gui --request-interval 1000`          |                                                                                                                              |
| `--request-timeout`             | Request timeout (ms)                   | `pdf2zh_next --gui --request-timeout 30000`          |                                                                                                                              |
| `--request-max-retries`         | Max retries for single request         | `pdf2zh_next --gui --request-max-retries 3`          |                                                                                                                              |
| `--log-level`                   | Log level                              | `pdf2zh_next --gui --log-level INFO`                 |                                                                                                                              |
| `--cache-dir`                   | Cache directory                        | `pdf2zh_next --gui --cache-dir ./cache`              |                                                                                                                              |
| `--proxy`                       | Proxy                                  | `pdf2zh_next --gui --proxy http://127.0.0.1:7890`    |                                                                                                                              |
| `--user-agent`                  | User agent                             | `pdf2zh_next --gui --user-agent "Mozilla/5.0..."`    |                                                                                                                              |
| `--check`                       | Check the environment                  | `pdf2zh_next --gui --check`                          |                                                                                                                              |
| `--help`                        | Show help                              | `pdf2zh_next --gui --help`                           |                                                                                                                              |

---

### TRANSLATED TEXT

| `--enabled-services`            | 활성화된 번역 서비스           | `pdf2zh_next --gui --enabled-services "Bing,OpenAI"` |                                                                                                                              |
| ------------------------------- | ------------------------------ | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--disabled-services`           | 비활성화된 번역 서비스          | `pdf2zh_next --gui --disabled-services "Bing"`       |                                                                                                                              |
| `--service-configs`             | 서비스 구성                     | `pdf2zh_next --gui --service-configs "Bing:xxx,xxx"` | 자세한 내용은 [번역 서비스 문서](https://pdf2zh-next.com/advanced/SERVICE.html) 를 참조하십시오. |
| `--concurrent`                  | 동시 번역 작업 수               | `pdf2zh_next --gui --concurrent 5`                   |                                                                                                                              |
| `--source-language`             | 원본 언어                       | `pdf2zh_next --gui --source-language en`             | 자세한 내용은 [지원 언어](https://pdf2zh-next.com/advanced/LANGUAGE.html) 를 참조하십시오.                  |
| `--target-language`             | 대상 언어                       | `pdf2zh_next --gui --target-language zh-CN`          | 자세한 내용은 [지원 언어](https://pdf2zh-next.com/advanced/LANGUAGE.html) 를 참조하십시오.                  |
| `--translate-tags`              | 번역할 태그                     | `pdf2zh_next --gui --translate-tags "p,span"`        |                                                                                                                              |
| `--translate-attributes`        | 번역할 속성                     | `pdf2zh_next --gui --translate-attributes "title"`   |                                                                                                                              |
| `--size-limit`                  | 단일 요청 크기 제한 (바이트)    | `pdf2zh_next --gui --size-limit 2000`                |                                                                                                                              |
| `--request-interval`            | 요청 간격 (밀리초)              | `pdf2zh_next --gui --request-interval 1000`          |                                                                                                                              |
| `--request-timeout`             | 요청 시간 초과 (밀리초)         | `pdf2zh_next --gui --request-timeout 30000`          |                                                                                                                              |
| `--request-max-retries`         | 단일 요청 최대 재시도 횟수       | `pdf2zh_next --gui --request-max-retries 3`          |                                                                                                                              |
| `--log-level`                   | 로그 레벨                       | `pdf2zh_next --gui --log-level INFO`                 |                                                                                                                              |
| `--cache-dir`                   | 캐시 디렉터리                   | `pdf2zh_next --gui --cache-dir ./cache`              |                                                                                                                              |
| `--proxy`                       | 프록시                          | `pdf2zh_next --gui --proxy http://127.0.0.1:7890`    |                                                                                                                              |
| `--user-agent`                  | 사용자 에이전트                 | `pdf2zh_next --gui --user-agent "Mozilla/5.0..."`    |                                                                                                                              |
| `--check`                       | 환경 확인                       | `pdf2zh_next --gui --check`                          |                                                                                                                              |
| `--help`                        | 도움말 표시                     | `pdf2zh_next --gui --help`                           |                                                                                                                              |
|---------------------------------|----------------------------------------|---------------------------------------------------|
| `--disable-gui-print`           | Disable GUI printing                   | `pdf2zh_next --gui --disable-gui-print`           |
| `--disable-gui-save`            | Disable GUI saving                     | `pdf2zh_next --gui --disable-gui-save`            |
| `--disable-gui-export`          | Disable GUI exporting                  | `pdf2zh_next --gui --disable-gui-export`          |
| `--disable-gui-import`          | Disable GUI importing                  | `pdf2zh_next --gui --disable-gui-import`          |
| `--disable-gui-copy`            | Disable GUI copying                    | `pdf2zh_next --gui --disable-gui-copy`            |
| `--disable-gui-paste`           | Disable GUI pasting                    | `pdf2zh_next --gui --disable-gui-paste`           |
| `--disable-gui-cut`             | Disable GUI cutting                    | `pdf2zh_next --gui --disable-gui-cut`             |
| `--disable-gui-undo`            | Disable GUI undo                       | `pdf2zh_next --gui --disable-gui-undo`            |
| `--disable-gui-redo`            | Disable GUI redo                       | `pdf2zh_next --gui --disable-gui-redo`            |

---

### TRANSLATED TEXT

| `--disable-gui-sensitive-input` | GUI 민감 입력 비활성화            | `pdf2zh_next --gui --disable-gui-sensitive-input` |
|---------------------------------|----------------------------------------|---------------------------------------------------|
| `--disable-gui-print`           | GUI 인쇄 비활성화                   | `pdf2zh_next --gui --disable-gui-print`           |
| `--disable-gui-save`            | GUI 저장 비활성화                     | `pdf2zh_next --gui --disable-gui-save`            |
| `--disable-gui-export`          | GUI 내보내기 비활성화                  | `pdf2zh_next --gui --disable-gui-export`          |
| `--disable-gui-import`          | GUI 가져오기 비활성화                  | `pdf2zh_next --gui --disable-gui-import`          |
| `--disable-gui-copy`            | GUI 복사 비활성화                    | `pdf2zh_next --gui --disable-gui-copy`            |
| `--disable-gui-paste`           | GUI 붙여넣기 비활성화                    | `pdf2zh_next --gui --disable-gui-paste`           |
| `--disable-gui-cut`             | GUI 잘라내기 비활성화                    | `pdf2zh_next --gui --disable-gui-cut`             |
| `--disable-gui-undo`            | GUI 실행 취소 비활성화                       | `pdf2zh_next --gui --disable-gui-undo`            |
| `--disable-gui-redo`            | GUI 다시 실행 비활성화                       | `pdf2zh_next --gui --disable-gui-redo`            |
---

### OUTPUT

| `--disable-config-auto-save`    | 자동 설정 저장 비활성화 | `pdf2zh_next --gui --disable-config-auto-save`  |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | WebUI Server IP                        | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--server-name localhost`       | Only local access                      | `pdf2zh_next --gui --server-name localhost`     |
| `--no-gradio-queue`             | Disable Gradio Queue                   | `pdf2zh_next --gui --no-gradio-queue`           |
| `--share`                       | Create a public link                   | `pdf2zh_next --gui --share`                     |
| `--auth USERNAME:PASSWORD`      | Set username and password for WebUI    | `pdf2zh_next --gui --auth "username:password"`  |
| `--ssl-keyfile`                 | SSL Key file path                      | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | SSL Certificate file path              | `pdf2zh_next --gui --ssl-certfile cert.pem`     |

---

### OUTPUT

| `--server-port`                 | WebUI 포트                             | `pdf2zh_next --gui --server-port 7860`          |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--server-name`                 | WebUI 서버 IP                          | `pdf2zh_next --gui --server-name 0.0.0.0`       |
| `--server-name localhost`       | 로컬 액세스만 허용                     | `pdf2zh_next --gui --server-name localhost`     |
| `--no-gradio-queue`             | Gradio 대기열 비활성화                 | `pdf2zh_next --gui --no-gradio-queue`           |
| `--share`                       | 공개 링크 생성                         | `pdf2zh_next --gui --share`                     |
| `--auth USERNAME:PASSWORD`      | WebUI 사용자 이름 및 비밀번호 설정     | `pdf2zh_next --gui --auth "username:password"`  |
| `--ssl-keyfile`                 | SSL 키 파일 경로                       | `pdf2zh_next --gui --ssl-keyfile key.pem`       |
| `--ssl-certfile`                | SSL 인증서 파일 경로                   | `pdf2zh_next --gui --ssl-certfile cert.pem`     |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--src-lang`                    | Source language                        | `pdf2zh_next --gui --src-lang en`               |
| `--dst-lang`                    | Target language                        | `pdf2zh_next --gui --dst-lang zh`               |
| `--translator`                  | Translator                             | `pdf2zh_next --gui --translator google`         |
| `--translator-key`              | Translator API key                     | `pdf2zh_next --gui --translator-key <your_key>` |
| `--translator-url`              | Translator API URL                     | `pdf2zh_next --gui --translator-url <your_url>` |
| `--translator-model`            | Translator model                       | `pdf2zh_next --gui --translator-model gpt-4o`   |
| `--translator-context`          | Translator context                     | `pdf2zh_next --gui --translator-context true`   |
| `--translator-formality`        | Translator formality                   | `pdf2zh_next --gui --translator-formality more` |
| `--translator-glossary`         | Translator glossary                    | `pdf2zh_next --gui --translator-glossary <id>`  |
| `--translator-glossary-name`    | Translator glossary name               | `pdf2zh_next --gui --translator-glossary-name <name>` |
| `--translator-option-<option>`  | Translator specific options            | `pdf2zh_next --gui --translator-option-a 1 --translator-option-b 2` |
| `--proxy`                       | Proxy server                           | `pdf2zh_next --gui --proxy http://127.0.0.1:7890` |
| `--log-level`                   | Log level                              | `pdf2zh_next --gui --log-level debug`           |
| `--log-file`                    | Log file                               | `pdf2zh_next --gui --log-file pdf2zh.log`       |
| `--cache`                       | Cache directory                        | `pdf2zh_next --gui --cache ./cache`             |
| `--config`                      | Config file                            | `pdf2zh_next --gui --config ./config.json`      |

---

### TRANSLATION RESULT

| `--ui-lang`                     | UI 언어                                | `pdf2zh_next --gui --ui-lang zh`                |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| `--src-lang`                    | 원본 언어                              | `pdf2zh_next --gui --src-lang en`               |
| `--dst-lang`                    | 대상 언어                              | `pdf2zh_next --gui --dst-lang zh`               |
| `--translator`                  | 번역기                                 | `pdf2zh_next --gui --translator google`         |
| `--translator-key`              | 번역기 API 키                          | `pdf2zh_next --gui --translator-key <your_key>` |
| `--translator-url`              | 번역기 API URL                         | `pdf2zh_next --gui --translator-url <your_url>` |
| `--translator-model`            | 번역기 모델                            | `pdf2zh_next --gui --translator-model gpt-4o`   |
| `--translator-context`          | 번역기 컨텍스트                        | `pdf2zh_next --gui --translator-context true`   |
| `--translator-formality`        | 번역기 격식도                          | `pdf2zh_next --gui --translator-formality more` |
| `--translator-glossary`         | 번역기 용어집                          | `pdf2zh_next --gui --translator-glossary <id>`  |
| `--translator-glossary-name`    | 번역기 용어집 이름                     | `pdf2zh_next --gui --translator-glossary-name <name>` |
| `--translator-option-<option>`  | 번역기 특정 옵션                       | `pdf2zh_next --gui --translator-option-a 1 --translator-option-b 2` |
| `--proxy`                       | 프록시 서버                            | `pdf2zh_next --gui --proxy http://127.0.0.1:7890` |
| `--log-level`                   | 로그 레벨                              | `pdf2zh_next --gui --log-level debug`           |
| `--log-file`                    | 로그 파일                              | `pdf2zh_next --gui --log-file pdf2zh.log`       |
| `--cache`                       | 캐시 디렉터리                          | `pdf2zh_next --gui --cache ./cache`             |
| `--config`                      | 구성 파일                              | `pdf2zh_next --gui --config ./config.json`      |

[⬆️ 맨 위로](#toc)

---

#### 속도 제한 구성 가이드

번역 서비스를 사용할 때 적절한 속도 제한 구성은 API 오류를 방지하고 성능을 최적화하는 데 중요합니다. 이 가이드는 다양한 업스트림 서비스 제한에 따라 `--qps` 및 `--pool-max-worker` 매개변수를 구성하는 방법을 설명합니다.

> [!TIP]
>
> `pool_size` 는 1000 을 초과하지 않는 것이 권장됩니다. 아래 방법으로 계산된 `pool_size` 가 1000 을 초과하는 경우 1000 을 사용하세요.

##### RPM (Requests Per Minute) 요청 속도 제한

업스트림 서비스에 RPM 제한이 있을 때 다음 계산을 사용하세요:

**계산 공식:**
- `qps = floor(rpm / 60)`
- `pool_size = qps * 10`

> [!NOTE]
> 10 이라는 계수는 대부분의 시나리오에서 잘 작동하는 경험적 계수입니다.

**예시:**
번역 서비스의 제한이 600 RPM 인 경우:
- `qps = floor(600 / 60) = 10`
- `pool_size = 10 * 10 = 100`

```bash
pdf2zh example.pdf --qps 10 --pool-max-worker 100
```

##### 동시 연결 제한

`Concurrent Connection Limit = (Number of Workers) × (Number of GPUs per Worker) × (Number of Concurrent Requests per GPU)`

**Example:**

- If you have 2 workers (`--workers 2`), each with 1 GPU (`CUDA_VISIBLE_DEVICES=0`), and each GPU handles 2 concurrent requests (`--concurrency 2`), then:
  
  ```bash
  Concurrent Connection Limit = 2 × 1 × 2 = 4
  ```

- If you have 1 worker (`--workers 1`) with 2 GPUs (`CUDA_VISIBLE_DEVICES=0,1`), and each GPU handles 3 concurrent requests (`--concurrency 3`), then:
  
  ```bash
  Concurrent Connection Limit = 1 × 2 × 3 = 6
  ```

**Note:** This calculation assumes each GPU processes requests independently. If your model implementation shares resources across GPUs (e.g., tensor parallelism), adjust accordingly.

---

### TRANSLATED TEXT

업스트림 서비스에 동시 연결 제한이 있는 경우 (예: GLM 공식 서비스), 이 방법을 사용하세요:

**계산 공식:**
`동시 연결 제한 = (작업자 수) × (작업자당 GPU 수) × (GPU 당 동시 요청 수)`

**예시:**

- 작업자가 2 개 (`--workers 2`), 각 작업자에 GPU 가 1 개 (`CUDA_VISIBLE_DEVICES=0`), GPU 당 동시 요청이 2 개 (`--concurrency 2`) 인 경우:
  
  ```bash
  동시 연결 제한 = 2 × 1 × 2 = 4
  ```

- 작업자가 1 개 (`--workers 1`), GPU 가 2 개 (`CUDA_VISIBLE_DEVICES=0,1`), GPU 당 동시 요청이 3 개 (`--concurrency 3`) 인 경우:
  
  ```bash
  동시 연결 제한 = 1 × 2 × 3 = 6
  ```

**참고:** 이 계산은 각 GPU 가 요청을 독립적으로 처리한다고 가정합니다. 모델 구현이 GPU 간 리소스를 공유하는 경우 (예: 텐서 병렬화), 이에 따라 조정하세요.
- `pool_size = max(floor(0.9 * official_concurrent_limit), official_concurrent_limit - 20)`
- `qps = pool_size`

---

### 번역 결과

**예시:**
번역 서비스가 50 개의 동시 연결을 허용하는 경우:
- `pool_size = max(floor(0.9 * 50), 50 - 20) = max(45, 30) = 45`
- `qps = 45`

```bash
pdf2zh example.pdf --qps 45 --pool-max-worker 45
```

##### 모범 사례

> [!TIP]
> - 항상 보수적인 값으로 시작하고 필요에 따라 점진적으로 증가시키세요
> - 서비스의 응답 시간과 오류율을 모니터링하세요
> - 서비스마다 다른 최적화 전략이 필요할 수 있습니다
> - 이러한 매개변수를 설정할 때 특정 사용 사례와 문서 크기를 고려하세요


[⬆️ 맨 위로](#toc)

---

#### 부분 번역

`--pages` 매개변수를 사용하여 문서의 일부를 번역합니다.

- 페이지 번호가 연속적인 경우 다음과 같이 작성할 수 있습니다:

```bash
pdf2zh_next example.pdf --pages 1-3
```

```bash
pdf2zh_next example.pdf --pages 25-
```

> [!TIP]
> `25-` 는 25 페이지 이후의 모든 페이지를 포함합니다. 문서가 100 페이지인 경우, 이는 `25-100` 과 동일합니다.
> 
> 마찬가지로, `-25` 는 25 페이지 이전의 모든 페이지를 포함하며, 이는 `1-25` 와 동일합니다.

- 페이지가 연속적이지 않은 경우 쉼표 `,` 를 사용하여 구분할 수 있습니다.

예를 들어, 첫 번째와 세 번째 페이지를 번역하려면 다음 명령을 사용할 수 있습니다:

```bash
pdf2zh_next example.pdf --pages "1,3"
```

- 페이지에 연속적 및 비연속적 범위가 모두 포함된 경우, 다음과 같이 쉼표로 연결할 수도 있습니다:

```bash
pdf2zh_next example.pdf --pages "1,3,10-20,25-"
```

이 명령은 첫 번째 페이지, 세 번째 페이지, 10-20 페이지, 그리고 25 페이지부터 끝까지의 모든 페이지를 번역합니다.

[⬆️ 맨 위로 이동](#toc)

---

#### 소스 및 대상 언어 지정

[Google 언어 코드](https://developers.google.com/admin-sdk/directory/v1/languages), [DeepL 언어 코드](https://developers.deepl.com/docs/resources/supported-languages) 참조

```bash
pdf2zh_next example.pdf --lang-in en -lang-out ja
```

[⬆️ 맨 위로](#toc)

---

#### 예외와 함께 번역하기

보존해야 할 수식 글꼴과 문자를 지정하기 위해 정규식을 사용합니다:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^RT].*|MS.*|.*Ital)" --formular-char-pattern "(\(|\||\)|\+|=|\d|[\u0080-\ufaff])"
```

기본적으로 `Latex`, `Mono`, `Code`, `Italic`, `Symbol` 및 `Math` 글꼴을 보존합니다:

```bash
pdf2zh_next example.pdf --formular-font-pattern "(CM[^R]|MS.M|XY|MT|BL|RM|EU|LA|RS|LINE|LCIRCLE|TeX-|rsfs|txsy|wasy|stmary|.*Mono|.*Code|.*Ital|.*Sym|.*Math)"
```

[⬆️ 맨 위로](#toc)

---

#### 사용자 정의 프롬프트

<!-- Note: System prompt is currently not supported. See [this change](https://github.com/PDFMathTranslate/PDFMathTranslate-next/pull/637). -->

번역을 위한 사용자 정의 시스템 프롬프트. 주로 프롬프트에 Qwen 3 의 '/no_think' 지시를 추가하는 데 사용됩니다.

```bash
pdf2zh_next example.pdf --custom-system-prompt "/no_think You are a professional and reliable machine translation engine responsible for translating the input text into zh_CN.When translating, strictly follow the instructions below to ensure translation quality and preserve all formatting, tags, and placeholders:"
```

[⬆️ 맨 위로](#toc)

---

#### 사용자 지정 구성

구성 파일을 수정하고 가져오는 방법에는 여러 가지가 있습니다.

> [!NOTE]
> **구성 파일 계층 구조**
>
> 동일한 매개변수를 다른 방법으로 수정할 때, 소프트웨어는 아래의 우선순위에 따라 변경 사항을 적용합니다.
>
> 상위 순위의 수정 사항은 하위 순위의 것을 덮어씁니다.
>
> **cli/gui > env > 사용자 구성 파일 > 기본 구성 파일**

- **명령줄 인수**를 통한 구성 수정

대부분의 경우 원하는 설정을 명령줄 인수를 통해 직접 전달할 수 있습니다. 자세한 내용은 [명령줄 인수](#cmd) 를 참조하세요.

예를 들어 GUI 창을 활성화하려면 다음 명령을 사용할 수 있습니다:

```bash
pdf2zh_next --gui
```

- **환경 변수**를 통한 구성 수정

명령줄 인수에서 `--` 를 `PDF2ZH_` 로 대체하고, `=` 를 사용하여 매개변수를 연결하며, `-` 를 `_` 로 대체하여 환경 변수로 사용할 수 있습니다.

예를 들어, GUI 창을 활성화하려면 다음 명령을 사용할 수 있습니다:

```bash
PDF2ZH_GUI=TRUE pdf2zh_next
```

<img src="./../../images/ev_light.svg" width="580px"  alt="env"/>

- 사용자 지정 **구성 파일**

아래 명령줄 인수를 사용하여 구성 파일을 지정할 수 있습니다:

```bash
pdf2zh_next --config-file '/path/config.toml'
```

구성 파일 형식이 확실하지 않은 경우 아래 설명된 기본 구성 파일을 참조하세요.

- **기본 구성 파일**

기본 구성 파일은 `~/.config/pdf2zh` 에 위치합니다.  
`default` 디렉토리의 구성 파일은 수정하지 마십시오.  
이 구성 파일의 내용을 참조하고 **사용자 지정 구성 파일**을 사용하여 자신의 구성 파일을 구현하는 것이 강력히 권장됩니다.

> [!TIP]
> - 기본적으로 pdf2zh 2.0 은 GUI 에서 번역 버튼을 클릭할 때마다 현재 구성을 `~/.config/pdf2zh/config.v3.toml` 에 자동으로 저장합니다. 이 구성 파일은 다음 시작 시 기본적으로 로드됩니다.
> - `default` 디렉토리의 구성 파일은 프로그램에 의해 자동으로 생성됩니다. 수정을 위해 복사할 수 있지만 직접 수정하지 마십시오.
> - 구성 파일에는 "v2", "v3" 등의 버전 번호가 포함될 수 있습니다. 이는 **구성 파일 버전 번호**이며, pdf2zh 자체의 버전 번호가 **아닙니다**.


[⬆️ 맨 위로](#toc)

---

#### 클린 건너뛰기

이 매개변수가 True 로 설정되면 PDF 클린 단계가 건너뛰어지며, 이는 호환성을 향상시키고 일부 폰트 처리 문제를 피할 수 있습니다.

사용법:

```bash
pdf2zh_next example.pdf --skip-clean
```

환경 변수를 사용하는 방법:

```bash
PDF2ZH_SKIP_CLEAN=TRUE pdf2zh_next example.pdf
```

> [!TIP]
> `--enhance-compatibility` 가 활성화되면 클린 건너뛰기가 자동으로 활성화됩니다.

---

#### 번역 캐시

PDFMathTranslate 는 번역 속도를 높이고 동일한 내용에 대한 불필요한 API 호출을 방지하기 위해 번역된 텍스트를 캐시합니다. `--ignore-cache` 옵션을 사용하여 번역 캐시를 무시하고 강제로 재번역할 수 있습니다.

```bash
pdf2zh_next example.pdf --ignore-cache
```

[⬆️ 맨 위로](#toc)

---

#### 공개 서비스로 배포하기

공개 서비스에 pdf2zh GUI 를 배포할 때는 아래 설명대로 구성 파일을 수정해야 합니다.

> [!WARNING]
>
> 이 프로젝트는 보안 전문 감사를 받지 않았으며 보안 취약점이 포함되어 있을 수 있습니다. 공용 네트워크에 배포하기 전에 위험을 평가하고 필요한 보안 조치를 취하세요.


> [!TIP]
> - 공개적으로 배포할 때는 `disable_gui_sensitive_input` 과 `disable_config_auto_save` 를 모두 활성화해야 합니다.
> - 사용 가능한 서비스를 *영어 쉼표* <kbd>,</kbd> 로 구분하세요.

사용 가능한 구성은 다음과 같습니다:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
enabled_services = "Bing,OpenAI"
disable_gui_sensitive_input = true
disable_config_auto_save = true
```

[⬆️ 맨 위로](#toc)

---

#### 인증 및 환영 페이지

인증 및 환영 페이지를 사용하여 Web UI 를 사용할 사용자를 지정하고 로그인 페이지를 사용자 정의할 때:

예시 auth.txt
각 줄에는 사용자 이름과 비밀번호 두 요소가 쉼표로 구분되어 포함됩니다.

```
admin,123456
user1,password1
user2,abc123
guest,guest123
test,test123
```

예시 welcome.html

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
> 인증 파일이 비어 있지 않은 경우에만 환영 페이지가 작동합니다.
> 인증 파일이 비어 있으면 인증이 없습니다. :)

사용 가능한 구성은 다음과 같습니다:

```toml title="config.toml"
[basic]
gui = true

[gui_settings]
auth_file = "/path/to/auth/file"
welcome_page = "/path/to/welcome/html/file"
```

[⬆️ 맨 위로](#toc)

---

#### 용어집 지원

PDFMathTranslate 는 용어집 테이블을 지원합니다. 용어집 테이블 파일은 `csv` 파일이어야 합니다.  
파일에는 세 개의 열이 있습니다. 다음은 데모 용어집 파일입니다:

| source | target  | tgt_lng |
|--------|---------|---------|
| AutoML | 자동 ML  | ko     |
| a,a    | a       | ko     |
| "      | "       | ko     |


CLI 사용자의 경우:
용어집으로 여러 파일을 사용할 수 있습니다. 다른 파일은 `,` 로 구분해야 합니다.

```bash
pdf2zh_next example.pdf --glossaries "glossary1.csv,glossary2.csv,glossary3.csv"
```

웹 UI 사용자를 위해:

이제 자신의 용어집 파일을 업로드할 수 있습니다. 파일을 업로드한 후에는 이름을 클릭하여 내용을 확인할 수 있으며, 내용이 아래에 표시됩니다.

[⬆️ 맨 위로 돌아가기](#toc)

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>