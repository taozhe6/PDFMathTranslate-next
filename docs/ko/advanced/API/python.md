>
> For more details, see [For Translators](for-translators/FOR_TRANSLATORS.md).

# PDFMathTranslate

[English](README.md) | [简体中文](README_zh.md) | [繁體中文](README_zh_tw.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Español](README_es.md) | [Italiano](README_it.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md)

**PDFMathTranslate** is a tool designed to translate PDF files while preserving the original layout and formatting, including mathematical formulas and tables. It supports multiple translation services and offers both command-line and web interface options.

## Features

- **Layout Preservation**: Maintains original PDF layout including text formatting, mathematical formulas, tables, and images
- **Multiple Translation Services**: Supports Google Translate, DeepL, OpenAI, and more
- **Flexible Output**: Generate translated PDFs or markdown files
- **OCR Support**: Optional OCR for scanned PDFs using Tesseract
- **Web Interface**: User-friendly browser-based interface
- **Batch Processing**: Translate multiple files simultaneously
- **Customizable**: Adjustable translation parameters and model settings

## Quick Start

### Installation

```bash
pip install pdf2zh
```

### Basic Usage

```bash
# Translate PDF to Chinese
pdf2zh input.pdf -t zh

# Translate with specific service
pdf2zh input.pdf -t ja --service deepl

# Generate markdown output
pdf2zh input.pdf -t es --format markdown
```

### Web Interface

```bash
pdf2zh --web
```
Then open http://localhost:7860 in your browser.

## Documentation

- [Getting Started](getting-started/GETTING_STARTED.md)
- [Installation Guide](getting-started/INSTALLATION.md)
- [Usage Examples](getting-started/USAGE.md)
- [Advanced Options](advanced/ADVANCED.md)
- [Supported Languages](supported-languages/SUPPORTED_LANGUAGES.md)

## Supported Languages

PDFMathTranslate supports translation between numerous languages including:

- **Asian Languages**: Chinese (Simplified/Traditional), Japanese, Korean, Hindi, Thai, Vietnamese
- **European Languages**: English, French, German, Spanish, Italian, Portuguese, Russian
- **Middle Eastern**: Arabic, Hebrew, Turkish
- **And many more**...

See [Supported Languages](supported-languages/SUPPORTED_LANGUAGES.md) for complete list.

## Community & Support

- [FAQ](faq/FAQ.md) - Common questions and troubleshooting
- [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues) - Report bugs and request features
- [Contributing Guide](community/CONTRIBUTING.md) - How to contribute to the project

## Related Projects

- [PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next) - Next-generation version with improved performance
- [pdf2text](https://github.com/PDFMathTranslate/pdf2text) - PDF text extraction utilities

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Happy Translating!** 🌍✨

</div>

---

### TRANSLATION RESULT

> [!NOTE]
> 이 문서는 AI 생성 콘텐츠를 포함할 수 있습니다. 정확성을 위해 노력하지만 부정확한 내용이 있을 수 있습니다. 문제가 발생하면 다음을 통해 신고해 주세요:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues)
> - 커뮤니티 기여 (PR 환영!)
>
> 자세한 내용은 [문서 번역 기여 가이드](for-translators/FOR_TRANSLATORS.md) 를 참조하세요.

# PDFMathTranslate

[English](README.md) | [简体中文](README_zh.md) | [繁體中文](README_zh_tw.md) | [日本語](README_ja.md) | [한국어](README_ko.md) | [Français](README_fr.md) | [Deutsch](README_de.md) | [Español](README_es.md) | [Italiano](README_it.md) | [Português](README_pt.md) | [Русский](README_ru.md) | [العربية](README_ar.md) | [हिन्दी](README_hi.md)

**PDFMathTranslate**는 수학 공식과 표를 포함한 원본 레이아웃과 서식을 유지하면서 PDF 파일을 번역하도록 설계된 도구입니다. 여러 번역 서비스를 지원하며 명령줄과 웹 인터페이스 옵션을 모두 제공합니다.

## 기능

- **레이아웃 유지**: 텍스트 서식, 수학 공식, 표 및 이미지를 포함한 원본 PDF 레이아웃 유지
- **다중 번역 서비스**: Google 번역, DeepL, OpenAI 등 지원
- **유연한 출력**: 번역된 PDF 또는 마크다운 파일 생성
- **OCR 지원**: Tesseract 를 사용한 스캔된 PDF 에 대한 선택적 OCR
- **웹 인터페이스**: 사용자 친화적인 브라우저 기반 인터페이스
- **일괄 처리**: 여러 파일을 동시에 번역
- **사용자 정의 가능**: 조정 가능한 번역 매개변수 및 모델 설정

## 빠른 시작

### 설치

```bash
pip install pdf2zh
```

### 기본 사용법

```bash
# PDF 를 중국어로 번역
pdf2zh input.pdf -t zh

# 특정 서비스로 번역
pdf2zh input.pdf -t ja --service deepl

# 마크다운 출력 생성
pdf2zh input.pdf -t es --format markdown
```

### 웹 인터페이스

```bash
pdf2zh --web
```
그런 다음 브라우저에서 http://localhost:7860 을 엽니다.

## 문서

- [시작하기](getting-started/GETTING_STARTED.md)
- [설치 가이드](getting-started/INSTALLATION.md)
- [사용 예시](getting-started/USAGE.md)
- [고급 옵션](advanced/ADVANCED.md)
- [지원 언어](supported-languages/SUPPORTED_LANGUAGES.md)

## 지원 언어

PDFMathTranslate 는 다음과 같은 다양한 언어 간 번역을 지원합니다:

- **아시아 언어**: 중국어 (간체/번체), 일본어, 한국어, 힌디어, 태국어, 베트남어
- **유럽 언어**: 영어, 프랑스어, 독일어, 스페인어, 이탈리아어, 포르투갈어, 러시아어
- **중동 언어**: 아랍어, 히브리어, 터키어
- **그 외 많은 언어**...

전체 목록은 [지원 언어](supported-languages/SUPPORTED_LANGUAGES.md) 를 참조하세요.

## 커뮤니티 및 지원

- [자주 묻는 질문](faq/FAQ.md) - 일반적인 질문 및 문제 해결
- [GitHub Issues](https://github.com/PDFMathTranslate/PDFMathTranslate-next/issues) - 버그 신고 및 기능 요청
- [기여 가이드](community/CONTRIBUTING.md) - 프로젝트에 기여하는 방법

## 관련 프로젝트

- [PDFMathTranslate-next](https://github.com/PDFMathTranslate/PDFMathTranslate-next) - 향상된 성능을 갖춘 차세대 버전
- [pdf2text](https://github.com/PDFMathTranslate/pdf2text) - PDF 텍스트 추출 유틸리티

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

<div align="center">

**즐거운 번역 되세요!** 🌍✨

</div>

`do_translate_async_stream` is a function that performs translation asynchronously and returns a stream of results. This is useful for handling large documents or real-time translation where you want to process results as they become available.

### Parameters
- `pdf_file`: The PDF file to be translated. Can be a file path or a file-like object.
- `output_file`: The path to save the translated document. If not provided, the result will not be saved to a file.
- `target_lang`: The target language for translation. Default is 'zh' (Chinese).
- `source_lang`: The source language of the document. Default is 'auto' for automatic detection.
- `translator`: The translation service to use. Default is 'google'.
- `api_key`: API key for the translation service, if required.
- `other_params`: Additional parameters for the translation service.

### Returns
An asynchronous generator that yields tuples of `(status, result)`, where `status` indicates the current processing stage and `result` contains the translated content or progress information.

### Example Usage
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for status, result in do_translate_async_stream(
        pdf_file="document.pdf",
        output_file="translated_document.docx",
        target_lang="ko",
        translator="google"
    ):
        if status == "progress":
            print(f"Progress: {result}%")
        elif status == "translated":
            print(f"Translated page: {result}")
        elif status == "completed":
            print("Translation completed!")

asyncio.run(main())
```

### Notes
- The function uses asynchronous I/O operations, making it suitable for applications that require non-blocking behavior.
- The stream includes progress updates, translated pages, and a completion message.
- Ensure proper error handling for network issues or API limitations.

---

### OUTPUT

## Python API: do_translate_async_stream
`do_translate_async_stream` 는 비동기적으로 번역을 수행하고 결과 스트림을 반환하는 함수입니다. 이는 큰 문서를 처리하거나 결과를 사용할 수 있을 때 실시간으로 처리하려는 번역에 유용합니다.

### 매개변수
- `pdf_file`: 번역할 PDF 파일. 파일 경로나 파일류 객체일 수 있습니다.
- `output_file`: 번역된 문서를 저장할 경로. 제공되지 않으면 결과가 파일에 저장되지 않습니다.
- `target_lang`: 번역 대상 언어. 기본값은 'zh'(중국어) 입니다.
- `source_lang`: 문서의 원본 언어. 기본값은 자동 감지를 위한 'auto'입니다.
- `translator`: 사용할 번역 서비스. 기본값은 'google'입니다.
- `api_key`: 필요한 경우 번역 서비스를 위한 API 키.
- `other_params`: 번역 서비스를 위한 추가 매개변수.

### 반환값
`(status, result)` 튜플을 생성하는 비동기 생성자로, `status` 는 현재 처리 단계를 나타내고 `result` 는 번역된 내용이나 진행 정보를 포함합니다.

### 사용 예시
```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for status, result in do_translate_async_stream(
        pdf_file="document.pdf",
        output_file="translated_document.docx",
        target_lang="ko",
        translator="google"
    ):
        if status == "progress":
            print(f"Progress: {result}%")
        elif status == "translated":
            print(f"Translated page: {result}")
        elif status == "completed":
            print("Translation completed!")

asyncio.run(main())
```

### 참고사항
- 이 함수는 비동기 I/O 작업을 사용하므로 비차단 동작이 필요한 애플리케이션에 적합합니다.
- 스트림에는 진행 업데이트, 번역된 페이지 및 완료 메시지가 포함됩니다.
- 네트워크 문제나 API 제한에 대한 적절한 오류 처리를 보장하세요.

`pdf2zh` is a tool for extracting and translating text from PDF documents. It supports **OCR** for scanned PDFs and **AI-powered translation** for multilingual content. The tool is designed to handle complex layouts and preserve formatting as much as possible.

### Key Features

- **OCR Support**: Extract text from scanned PDFs using Tesseract OCR.
- **AI Translation**: Translate text using various translation services (e.g., Google Translate, DeepL, OpenAI).
- **Layout Preservation**: Maintain original document structure and formatting.
- **Batch Processing**: Process multiple PDFs in one go.
- **Customizable Output**: Choose output format (PDF, Markdown, HTML, etc.).

### Getting Started

To get started with `pdf2zh`, check out the [Installation](https://pdf2zh-next.com/getting-started/INSTALLATION.html) guide and the [Usage](https://pdf2zh-next.com/getting-started/USAGE.html) instructions.

### Advanced

For advanced usage, refer to the [Advanced](https://pdf2zh-next.com/advanced/ADVANCED.html) section.

### Supported Languages

See the list of [Supported Languages](https://pdf2zh-next.com/supported-languages/SUPPORTED_LANGUAGES.html) for translation.

### Community

Join the community for support and contributions: [Community](https://pdf2zh-next.com/community/COMMUNITY.html).

### FAQ

Check the [FAQ](https://pdf2zh-next.com/faq/FAQ.html) for common questions and troubleshooting.

### For Translators

If you want to contribute to the translation of this documentation, see [For Translators](https://pdf2zh-next.com/for-translators/FOR_TRANSLATORS.html).

---

### TRANSLATION RESULT

### 개요

`pdf2zh` 는 PDF 문서에서 텍스트를 추출하고 번역하는 도구입니다. 스캔된 PDF 에 대해 **OCR**을 지원하고 다국어 콘텐츠에 대해 **AI 기반 번역**을 지원합니다. 이 도구는 복잡한 레이아웃을 처리하고 가능한 한 서식을 유지하도록 설계되었습니다.

### 주요 기능

- **OCR 지원**: Tesseract OCR 을 사용하여 스캔된 PDF 에서  텍스트를 추출합니다.
- **AI 번역**: 다양한 번역 서비스 (예: Google 번역, DeepL, OpenAI) 를 사용하여 텍스트를 번역합니다.
- **레이아웃 유지**: 원본 문서 구조와 서식을 유지합니다.
- **일괄 처리**: 여러 PDF 를 한 번에 처리합니다.
- **사용자 정의 출력**: 출력 형식 (PDF, Markdown, HTML 등) 을 선택할 수 있습니다.

### 시작하기

`pdf2zh` 를 시작하려면 [설치](https://pdf2zh-next.com/getting-started/INSTALLATION.html) 가이드와 [사용법](https://pdf2zh-next.com/getting-started/USAGE.html) 지침을 확인하세요.

### 고급  옵션

고급 사용법은 [고급  옵션](https://pdf2zh-next.com/advanced/ADVANCED.html)  섹션을 참조하세요.

### 지원 언어

번역 지원 언어 목록은 [지원 언어](https://pdf2zh-next.com/supported-languages/SUPPORTED_LANGUAGES.html) 를 참조하세요.

### 커뮤니티

지원 및 기여를 위해 커뮤니티에 참여하세요: [커뮤니티](https://pdf2zh-next.com/community/COMMUNITY.html).

### 자주  묻는 질문

일반적인 질문과 문제 해결은 [자주  묻는 질문](https://pdf2zh-next.com/faq/FAQ.html) 을 확인하세요.

### 문서 번역 기여 가이드

이 문서의 번역에 기여하고 싶다면 [문서 번역 기여 가이드](https://pdf2zh-next.com/for-translators/FOR_TRANSLATORS.html) 를 참조하세요.
- The event stream contract is defined below.

### Event Stream Contract

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### OUTPUT

- `do_translate_async_stream` 는 단일 PDF 를 번역하고 이벤트 스트림 (진행/오류/완료) 을 생성하는 저수준 비동기 진입점입니다.
- 실시간 진행 상황과 결과에 대한 완전한 제어를 원하는 사용자 정의 UI 나 CLI 를 구축하는 데 적합합니다.
- 검증된 SettingsModel 과 파일 경로를 수락하고 dict 이벤트의 비동기 생성자를 반환합니다.
- 이벤트 스트림 계약은 아래에 정의되어 있습니다.

### 이벤트 스트림 계약

이벤트 스트림은 이벤트의 스트림으로, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 줄바꿈으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 반드시 포함해야 하며 다른 필드를 포함할 수 있는 JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 과 1 사이의 숫자인 `progress` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되었을 때 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생했을 때 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트는 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

This is the signature of the `translator` function for the command line:

```python
def translator(
    pdf_path: str, 
    target_lang: str,
    output_path: str = None,
    pages: str = "all",
    open_file: bool = False,
    model_name: str = "gpt-3.5-turbo",
    api_key: str = None,
    api_base: str = None,
    is_translate_text: bool = True,
    is_translate_formula: bool = True,
    retry_limit: int = 3,
    timeout: int = 10,
    proxy: str = None,
    detail: bool = False,
    is_ignore_error: bool = False,
    is_concat: bool = False,
    **kwargs,
) -> None:
    ...
```

### Parameters

- `pdf_path`: The path to the PDF file to be translated. **Required**.
- `target_lang`: The target language code. **Required**. See [Supported Languages](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html) for details.
- `output_path`: The path to save the translated PDF file. If not specified, the default is `{original_name}_{target_lang}.pdf`.
- `pages`: The pages to be translated. The default is "all". You can specify a single page (e.g., "1"), a range of pages (e.g., "1-3"), or multiple pages (e.g., "1,3,5").
- `open_file`: Whether to open the translated PDF file after translation. The default is `False`.
- `model_name`: The name of the model to be used for translation. The default is "gpt-3.5-turbo". See [Documentation of Translation Services](https://pdf2zh-next.com/advanced/TRANSLATION_SERVICES.html) for details.
- `api_key`: The API key for the translation service. If not specified, the environment variable `OPENAI_API_KEY` will be used.
- `api_base`: The API base URL for the translation service. If not specified, the environment variable `OPENAI_API_BASE` will be used.
- `is_translate_text`: Whether to translate the text. The default is `True`.
- `is_translate_formula`: Whether to translate the formulas. The default is `True`.
- `retry_limit`: The number of retries when translation fails. The default is 3.
- `timeout`: The timeout for each translation request. The default is 10 seconds.
- `proxy`: The proxy to use for the translation service. If not specified, the environment variable `HTTP_PROXY` or `HTTPS_PROXY` will be used.
- `detail`: Whether to output detailed information during translation. The default is `False`.
- `is_ignore_error`: Whether to ignore errors and continue translation. The default is `False`.
- `is_concat`: Whether to concatenate the translated PDF with the original PDF. The default is `False`.
- `**kwargs`: Other parameters to be passed to the translation service.

---

### OUTPUT

### 함수 시그니처

다음은 명령줄에서 사용되는 `translator` 함수의 시그니처입니다:

```python
def translator(
    pdf_path: str, 
    target_lang: str,
    output_path: str = None,
    pages: str = "all",
    open_file: bool = False,
    model_name: str = "gpt-3.5-turbo",
    api_key: str = None,
    api_base: str = None,
    is_translate_text: bool = True,
    is_translate_formula: bool = True,
    retry_limit: int = 3,
    timeout: int = 10,
    proxy: str = None,
    detail: bool = False,
    is_ignore_error: bool = False,
    is_concat: bool = False,
    **kwargs,
) -> None:
    ...
```

### 매개변수

- `pdf_path`: 번역할 PDF 파일의 경로. **필수**.
- `target_lang`: 목표 언어 코드. **필수**. 자세한 내용은 [지원 언어](https://pdf2zh-next.com/advanced/SUPPORTED_LANGUAGES.html) 를 참조하세요.
- `output_path`: 번역된 PDF 파일을 저장할 경로. 지정하지 않으면 기본값은 `{original_name}_{target_lang}.pdf` 입니다.
- `pages`: 번역할 페이지. 기본값은 "all"입니다. 단일 페이지 (예: "1"), 페이지 범위 (예: "1-3") 또는 여러 페이지 (예: "1,3,5") 를 지정할 수 있습니다.
- `open_file`: 번역 후 번역된 PDF 파일을 열지 여부. 기본값은 `False` 입니다.
- `model_name`: 번역에 사용할 모델 이름. 기본값은 "gpt-3.5-turbo"입니다. 자세한 내용은 [번역 서비스 문서](https://pdf2zh-next.com/advanced/TRANSLATION_SERVICES.html) 를 참조하세요.
- `api_key`: 번역 서비스의 API 키. 지정하지 않으면 환경 변수 `OPENAI_API_KEY` 가 사용됩니다.
- `api_base`: 번역 서비스의 API 기본 URL. 지정하지 않으면 환경 변수 `OPENAI_API_BASE` 가 사용됩니다.
- `is_translate_text`: 텍스트를 번역할지 여부. 기본값은 `True` 입니다.
- `is_translate_formula`: 수식을 번역할지 여부. 기본값은 `True` 입니다.
- `retry_limit`: 번역 실패 시 재시도 횟수. 기본값은 3 입니다.
- `timeout`: 각 번역 요청에 대한 타임아웃. 기본값은 10 초입니다.
- `proxy`: 번역 서비스에 사용할 프록시. 지정하지 않으면 환경 변수 `HTTP_PROXY` 또는 `HTTPS_PROXY` 가 사용됩니다.
- `detail`: 번역 중 상세 정보를 출력할지 여부. 기본값은 `False` 입니다.
- `is_ignore_error`: 오류를 무시하고 번역을 계속할지 여부. 기본값은 `False` 입니다.
- `is_concat`: 번역된 PDF 를 원본 PDF 와 연결할지 여부. 기본값은 `False` 입니다.
- `**kwargs`: 번역 서비스에 전달할 기타 매개변수.
- Returns: AsyncGenerator[TranslateEvent, None]. The events are:
  - `StartEvent`: Fired when the translation starts.
  - `PageTranslateProgressEvent`: Fired for each page's translation progress. Contains:
    - `page_number: int`
    - `progress: float` (0.0 to 1.0)
  - `PageTranslatedEvent`: Fired when a page is translated. Contains:
    - `page_number: int`
    - `translated_page: TranslatedPage`
  - `PageTranslateFailedEvent`: Fired when a page translation fails. Contains:
    - `page_number: int`
    - `error: Exception`
  - `EndEvent`: Fired when the translation ends. Contains:
    - `output_file: str | None` (if `settings.output_file` is set)
    - `total_pages: int`
    - `translated_pages: int`
    - `failed_pages: int`
- Exceptions:
  - `FileNotFoundError`: If the file does not exist.
  - `ValidationError`: If the settings are invalid.

---

### TRANSLATION

### 이벤트 스트림 계약

이벤트 스트림 계약은 서버가 장기간 HTTP 연결을 통해 클라이언트에 이벤트를 보낼 수 있도록 하는 서버와 클라이언트 간의 계약입니다. 이는 장기 실행 작업 중 진행 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 이벤트 스트림으로, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 줄바꿈으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 포함해야 하는 JSON 객체이며 다른 필드를 포함할 수 있습니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 과 1 사이의 숫자인 `progress` 필드를 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되면 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생하면 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 포함해야 합니다.

예시:

```json
{"type": "error", "error": "오류가 발생했습니다"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트는 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### 취소 및 환불 정책

**최종 업데이트: 2025 년 2 월 21 일**

#### 취소

구독은 언제든지 취소할 수 있습니다. 취소는 현재 유료 기간이 끝날 때 효력이 발생합니다.

#### 환불

구매에 100% 만족하지 못하는 경우, 원래 구매일로부터 14 일 이내에 환불 요청을 하면 환불해 드립니다. 이유를 묻지 않습니다.

취소 및 환불 정책에 대한 질문이 있으시면 다음으로 연락하세요:

- 이메일: pdf2zh@gmail.com

---

### 참고사항 및 모범 사례

#### 참고사항

- 번역 속도는 모델 속도와 PDF 의 페이지 수에 따라 다릅니다. 큰 PDF 의 경우 시간이 걸릴 수 있습니다.
- 번역 품질은 번역 서비스와 모델에 따라 다릅니다. 특히 영어가 아닌 언어에서 중국어로 번역하는 경우 더 나은 결과를 위해 프롬프트를 조정해야 할 수 있습니다.
- 일부 PDF 는 제대로 구문 분석되지 않아 번역 품질이 낮을 수 있습니다. 이러한 경우 PDF 를 먼저 HTML 과 같은 더 구문 분석하기 쉬운 형식으로 변환하는 다른 도구를 사용하는 것을 고려하세요.

#### 모범 사례

- 최고의 품질을 위해 `gpt-4` 모델 (기본값) 을 사용하세요. 예산이 부담된다면 `gpt-3.5-turbo` 를 고려하세요.
- 더 나은 서식을 위해 `markdown` 출력 형식 (기본값) 을 사용하세요. 더 WYSIWYG 접근 방식을 선호한다면 `html` 을 사용하세요.
- 번역 품질이 만족스럽지 않다면 프롬프트를 조정해 보세요. 예를 들어, 모델에 더 직역하거나 더 자유롭게 번역하도록 요청할 수 있습니다.
- 복잡한 레이아웃의 PDF 의 경우 레이아웃을 무시하고 텍스트만 추출하는 `--no-layout` 옵션을 사용하는 것을 고려하세요. 이렇게 하면 번역 품질이 향상될 수 있지만 서식을 잃을 수 있습니다.
- 이미지가 많은 PDF 의 경우 먼저 OCR 도구를 사용하여 이미지에서 텍스트를 추출하는 것을 고려하세요.

---

시작해 봅시다!

---

### 우회 목록

- pdf2zh
- PDFMathTranslate
- ---

---

### 원본 텍스트

- 가져오기: `from pdf2zh_next.high_level import do_translate_async_stream`
- 호출: `async for event in do_translate_async_stream(settings, file): ...`
- 매개변수:
  - settings: SettingsModel. 유효해야 합니다; 함수는 `settings.validate_settings()` 를 호출합니다.
  - file: str | pathlib.Path. 번역할 단일 PDF. 존재해야 합니다.
- 반환: AsyncGenerator[TranslateEvent, None]. 이벤트는 다음과 같습니다:
  - `StartEvent`: 번역이 시작될 때 발생합니다.
  - `PageTranslateProgressEvent`: 각 페이지의 번역 진행 상황에 대해 발생합니다. 포함 사항:
    - `page_number: int`
    - `progress: float` (0.0 에서 1.0)
  - `PageTranslatedEvent`: 페이지가 번역되면 발생합니다. 포함 사항:
    - `page_number: int`
    - `translated_page: TranslatedPage`
  - `PageTranslateFailedEvent`: 페이지 번역이 실패하면 발생합니다. 포함 사항:
    - `page_number: int`
    - `error: Exception`
  - `EndEvent`: 번역이 끝나면 발생합니다. 포함 사항:
    - `output_file: str | None` (`settings.output_file` 이 설정된 경우)
    - `total_pages: int`
    - `translated_pages: int`
    - `failed_pages: int`
- 예외:
  - `FileNotFoundError`: 파일이 존재하지 않는 경우.
  - `ValidationError`: 설정이 유효하지 않은 경우.

If you encounter a `403 Forbidden` error when accessing the website, it might be due to your network environment. You can try the following methods to resolve it:

1. **Use a VPN**: Connect to a VPN service to change your IP address.
2. **Use a proxy**: Configure a proxy server in your browser or system settings.
3. **Contact Support**: If the issue persists, contact our support team at [support@pdf2zh.com](mailto:support@pdf2zh.com).

---

### TRANSLATION RESULT

참고: 웹사이트에 접근할 때 `403 Forbidden` 오류가 발생하면 네트워크 환경 때문일 수 있습니다. 다음 방법들을 시도해 해결할 수 있습니다:

1. **VPN 사용**: VPN 서비스에 연결하여 IP 주소를 변경하세요.
2. **프록시 사용**: 브라우저나 시스템 설정에서 프록시 서버를 구성하세요.
3. **지원팀에 문의**: 문제가 지속되면 [support@pdf2zh.com](mailto:support@pdf2zh.com) 으로 지원팀에 문의하세요.
- ### Event Stream Contract: The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATED TEXT

### 이벤트 스트림 계약

이벤트 스트림 계약은 서버가 장기 실행 HTTP 연결을 통해 클라이언트에 이벤트를 보낼 수 있도록 하는 서버와 클라이언트 간의 계약입니다. 이는 장기 실행 작업 중 진행 상황 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 이벤트의 스트림이며, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 줄바꿈으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 반드시 포함해야 하며 다른 필드를 포함할 수 있는 JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 과 1 사이의 숫자인 `progress` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되었을 때 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생했을 때 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트가 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```
- ### Notes & Best Practices: #### Notes

- The translation speed depends on the model speed and the number of pages in the PDF. For large PDFs, it may take a while.
- The quality of translation depends on the translation service and the model. You might need to adjust the prompt for better results, especially for non-English to Chinese translations.
- Some PDFs might not be parsed correctly, leading to poor translation quality. In such cases, consider using other tools to convert the PDF to a more parse-friendly format (like HTML) first.

#### Best Practices

- For the best quality, use the `gpt-4` model (default). If you're on a budget, consider `gpt-3.5-turbo`.
- For better formatting, use the `markdown` output format (default). If you prefer a more WYSIWYG approach, use `html`.
- If the translation quality is not satisfactory, try adjusting the prompt. For example, you can ask the model to be more literal or more liberal in its translation.
- For PDFs with complex layouts, consider using the `--no-layout` option to ignore the layout and extract text only. This might improve translation quality but will lose formatting.
- For PDFs with many images, consider using OCR tools first to extract text from images.

---

Let's start!

---

### TRANSLATION RESULT

### 참고사항 및 모범 사례

#### 참고사항

- 번역 속도는 모델 속도와 PDF 의 페이지 수에 따라 다릅니다. 대형 PDF 의 경우 시간이 다소 걸릴 수 있습니다.
- 번역 품질은 번역 서비스와 모델에 따라 다릅니다. 특히 비영어에서 중국어 번역의 경우 더 나은 결과를 위해 프롬프트를 조정해야 할 수 있습니다.
- 일부 PDF 는 올바르게 구문 분석되지 않아 번역 품질이 떨어질 수 있습니다. 이러한 경우 먼저 PDF 를 더 구문 분석하기 쉬운 형식 (예: HTML) 으로 변환하는 다른 도구를 사용하는 것을 고려하세요.

#### 모범 사례

- 최상의 품질을 위해 `gpt-4` 모델 (기본값) 을 사용하세요. 예산이 제한된 경우 `gpt-3.5-turbo` 를 고려하세요.
- 더 나은 서식을 위해 `markdown` 출력 형식 (기본값) 을 사용하세요. 더 WYSIWYG 방식을 선호한다면 `html` 을 사용하세요.
- 번역 품질이 만족스럽지 않다면 프롬프트를 조정해 보세요. 예를 들어 모델에게 더 문자 그대로 또는 더 자유롭게 번역하도록 요청할 수 있습니다.
- 복잡한 레이아웃의 PDF 의 경우 레이아웃을 무시하고 텍스트만 추출하는 `--no-layout` 옵션을 사용하는 것을 고려하세요. 이는 번역 품질을 향상시킬 수 있지만 서식을 잃을 수 있습니다.
- 이미지가 많은 PDF 의 경우 먼저 OCR 도구를 사용하여 이미지에서 텍스트를 추출하는 것을 고려하세요.

---

시작하세요!
- The `callback` function receives events with the following schema:

```json
{
    "type": "progress",
    "progress": 0.5
}
```

```json
{
    "type": "translated",
    "page": 1,
    "content": "Translated content for page 1"
}
```

```json
{
    "type": "completed",
    "file": "translated.pdf"
}
```

```json
{
    "type": "error",
    "error": "Error message"
}
```

- The `callback` function is called in the main process, so it can be used to update the UI.
- The function returns the path to the translated file if successful, or raises an exception if an error occurs.
- The function is synchronous and blocks until the translation is complete.

---

### TRANSLATION RESULT

- `settings.basic.input_files` 는 이 함수에서 무시됩니다; 주어진 `file` 만 번역됩니다.
- `settings.basic.debug` 가 True 이면 번역은 메인 프로세스에서 실행됩니다; 그렇지 않으면 서브프로세스에서 실행됩니다. 두 경우 모두 이벤트 스키마는 동일합니다.
- `callback` 함수는 다음 스키마를 가진 이벤트를 수신합니다:

```json
{
    "type": "progress",
    "progress": 0.5
}
```

```json
{
    "type": "translated",
    "page": 1,
    "content": "1 페이지에 대한 번역된 내용"
}
```

```json
{
    "type": "completed",
    "file": "translated.pdf"
}
```

```json
{
    "type": "error",
    "error": "오류 메시지"
}
```

- `callback` 함수는 메인 프로세스에서 호출되므로 UI 업데이트에 사용할 수 있습니다.
- 함수는 성공 시 번역된 파일의 경로를 반환하거나 오류가 발생하면 예외를 발생시킵니다.
- 이 함수는 동기식이며 번역이 완료될 때까지 블록킹됩니다.

The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATED TEXT
- `start`: Emitted when the translation starts. The event data contains the total number of pages.
  ```json
  {"type": "start", "total_pages": 100}
  ```
- `page_start`: Emitted when starting to translate a page. The event data contains the page number and the page content.
  ```json
  {"type": "page_start", "page": 1, "content": "This is the content of page 1."}
  ```
- `page_progress`: Emitted when a page is partially translated. The event data contains the page number and the progress (a float between 0 and 1).
  ```json
  {"type": "page_progress", "page": 1, "progress": 0.5}
  ```
- `page_complete`: Emitted when a page is fully translated. The event data contains the page number and the translated content.
  ```json
  {"type": "page_complete", "page": 1, "translated_content": "这是第 1 页的内容。"}
  ```
- `page_error`: Emitted when a page fails to translate. The event data contains the page number and the error message.
  ```json
  {"type": "page_error", "page": 1, "error": "Translation failed due to network error."}
  ```
- `complete`: Emitted when the entire translation is complete. The event data contains the total number of pages translated and any summary information.
  ```json
  {"type": "complete", "total_translated": 100, "summary": "Translation completed successfully."}
  ```
- `error`: Emitted when a fatal error occurs that stops the translation. The event data contains the error message.
  ```json
  {"type": "error", "error": "Fatal error: API key invalid."}
  ```

The async generator is designed to be used with async for loops. Here's an example of how to use it:

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for event in do_translate_async_stream(
        pdf_file="document.pdf",
        target_lang="zh",
        translator="google"
    ):
        if event["type"] == "start":
            print(f"Starting translation of {event['total_pages']} pages.")
        elif event["type"] == "page_start":
            print(f"Starting page {event['page']}.")
        elif event["type"] == "page_progress":
            print(f"Page {event['page']} is {event['progress'] * 100}% complete.")
        elif event["type"] == "page_complete":
            print(f"Page {event['page']} translated: {event['translated_content']}")
        elif event["type"] == "page_error":
            print(f"Page {event['page']} failed: {event['error']}")
        elif event["type"] == "complete":
            print(f"Translation complete. Translated {event['total_translated']} pages.")
        elif event["type"] == "error":
            print(f"Fatal error: {event['error']}")

asyncio.run(main())
```

### Notes

- The events are emitted in the order they occur.
- The `page_progress` event may be emitted multiple times for a single page, depending on the translation service.
- The `page_error` event does not stop the translation. The translation will continue with the next page.
- The `error` event is fatal and will stop the translation. No more events will be emitted after an `error` event.

---

### TRANSLATION RESULT

비동기 생성자는 다음과 같은 유형의 JSON 형식의 딕셔너리 이벤트를 생성합니다:
- `start`: 번역이 시작될 때 발생합니다. 이벤트 데이터는 총 페이지 수를 포함합니다.
  ```json
  {"type": "start", "total_pages": 100}
  ```
- `page_start`: 페이지 번역을 시작할 때 발생합니다. 이벤트 데이터는 페이지 번호와 페이지 내용을 포함합니다.
  ```json
  {"type": "page_start", "page": 1, "content": "This is the content of page 1."}
  ```
- `page_progress`: 페이지가 부분적으로 번역될 때 발생합니다. 이벤트 데이터는 페이지 번호와 진행률 (0 에서 1 사이의 부동 소수점) 을 포함합니다.
  ```json
  {"type": "page_progress", "page": 1, "progress": 0.5}
  ```
- `page_complete`: 페이지가 완전히 번역될 때 발생합니다. 이벤트 데이터는 페이지 번호와 번역된 내용을 포함합니다.
  ```json
  {"type": "page_complete", "page": 1, "translated_content": "这是第 1 页的内容。"}
  ```
- `page_error`: 페이지 번역이 실패할 때 발생합니다. 이벤트 데이터는 페이지 번호와 오류 메시지를 포함합니다.
  ```json
  {"type": "page_error", "page": 1, "error": "Translation failed due to network error."}
  ```
- `complete`: 전체 번역이 완료될 때 발생합니다. 이벤트 데이터는 번역된 총 페이지 수와 요약 정보를 포함합니다.
  ```json
  {"type": "complete", "total_translated": 100, "summary": "Translation completed successfully."}
  ```
- `error`: 번역을 중단하는 치명적인 오류가 발생할 때 발생합니다. 이벤트 데이터는 오류 메시지를 포함합니다.
  ```json
  {"type": "error", "error": "Fatal error: API key invalid."}
  ```

비동기 생성자는 async for 루프와 함께 사용하도록 설계되었습니다. 사용 방법의 예시는 다음과 같습니다:

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    async for event in do_translate_async_stream(
        pdf_file="document.pdf",
        target_lang="zh",
        translator="google"
    ):
        if event["type"] == "start":
            print(f"Starting translation of {event['total_pages']} pages.")
        elif event["type"] == "page_start":
            print(f"Starting page {event['page']}.")
        elif event["type"] == "page_progress":
            print(f"Page {event['page']} is {event['progress'] * 100}% complete.")
        elif event["type"] == "page_complete":
            print(f"Page {event['page']} translated: {event['translated_content']}")
        elif event["type"] == "page_error":
            print(f"Page {event['page']} failed: {event['error']}")
        elif event["type"] == "complete":
            print(f"Translation complete. Translated {event['total_translated']} pages.")
        elif event["type"] == "error":
            print(f"Fatal error: {event['error']}")

asyncio.run(main())
```

### 참고사항

- 이벤트는 발생 순서대로 발생합니다.
- `page_progress` 이벤트는 번역 서비스에 따라 단일 페이지에 대해 여러 번 발생할 수 있습니다.
- `page_error` 이벤트는 번역을 중단하지 않습니다. 번역은 다음 페이지로 계속됩니다.
- `error` 이벤트는 치명적이며 번역을 중단합니다. `error` 이벤트 이후에는 더 이상 이벤트가 발생하지 않습니다.
- ### Event Stream Contract: The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATED TEXT

### 이벤트 스트림 계약

이벤트 스트림 계약은 서버와 클라이언트 간의 계약으로, 서버가 장기간 HTTP 연결을 통해 클라이언트로 이벤트를 보낼 수 있게 합니다. 이는 장기 실행 작업 중 진행 상황 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 이벤트 스트림으로, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 새 줄로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 반드시 포함해야 하며 다른 필드를 포함할 수도 있는 JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 에서 1 사이의 숫자인 `progress` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료될 때 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생할 때 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트가 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

- `part_index`: part index where error occurred (if applicable)
    - `stage`: stage where error occurred (if applicable)

---

### OUTPUT

- 단계 요약 이벤트: `stage_summary` (선택 사항, 먼저 나타날 수 있음)
  - 필드
    - `type`: "stage_summary"
    - `stages`: 예상 작업 분포를 설명하는 객체 `{ "name": str, "percent": float }`의 목록
    - `part_index`: 이 요약 이벤트의 경우 0 일 수 있음
    - `total_parts`: 전체 파트 수 (>= 1)

- 진행 상황 이벤트: `progress_start`, `progress_update`, `progress_end`
  - 공통 필드
    - `type`: 위 중 하나
    - `stage`: 사람이 읽을 수 있는 단계 이름 (예: "PDF 구문 분석 및 중간 표현 생성", "단락 번역", "PDF 저장")
    - `stage_progress`: 현재 단계 내 진행률을 나타내는 [0, 100] 범위의 float
    - `overall_progress`: 전체 진행률을 나타내는 [0, 100] 범위의 float
    - `part_index`: 현재 파트 인덱스 (일반적으로 진행 이벤트의 경우 1 부터 시작)
    - `total_parts`: 전체 파트 수 (>= 1). 큰 문서는 자동으로 분할될 수 있음
    - `stage_current`: 단계 내 현재 단계
    - `stage_total`: 단계 내 전체 단계 수

- 완료 이벤트: `finish`
  - 필드
    - `type`: "finish"
    - `translate_result`: 최종 출력을 제공하는 **객체** (참고: 딕셔너리가 아닌 클래스 인스턴스)
      - `original_pdf_path`: 입력 PDF 의 경로
      - `mono_pdf_path`: 단일 언어 번역 PDF 의 경로 (또는 None)
      - `dual_pdf_path`: 이중 언어 번역 PDF 의 경로 (또는 None)
      - `no_watermark_mono_pdf_path`: 워터마크가 없는 단일 언어 출력의 경로 (생성된 경우), 그렇지 않으면 None
      - `no_watermark_dual_pdf_path`: 워터마크가 없는 이중 언어 출력의 경로 (생성된 경우), 그렇지 않으면 None
      - `auto_extracted_glossary_path`: 자동 추출 용어집 CSV 의 경로 (또는 None)
      - `total_seconds`: 경과 시간 (초, float)
      - `peak_memory_usage`: 번역 중 대략적인 최대 메모리 사용량 (float; 구현에 따른 단위)

- 오류 이벤트: `error`
  - 필드
    - `type`: "error"
    - `error`: 사람이 읽을 수 있는 오류 메시지
    - `error_type`: `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError` 등 중 하나
    - `details`: 선택적 세부 정보 (예: 원본 오류 또는 트레이스백)
    - `part_index`: 오류가 발생한 파트 인덱스 (해당하는 경우)
    - `stage`: 오류가 발생한 단계 (해당하는 경우)

The `pdf2zh` tool uses a two-step process for translation:

1. **Extraction**: First, it extracts text and layout information from the PDF using `pdfplumber`.
2. **Translation**: Then, it sends the extracted content to the translation service (like OpenAI's GPT models) for translation.

Because of this two-step process, the quality of the source PDF greatly affects the translation quality. PDFs with clear text and simple layouts will yield the best results.

---

### TRANSLATION RESULT

중요한 동작: `pdf2zh` 도구는 번역을 위해 두 단계 프로세스를 사용합니다:

1. **추출**: 먼저 `pdfplumber` 를 사용하여 PDF 에서 텍스트와 레이아웃 정보를 추출합니다.
2. **번역**: 그런 다음 추출된 콘텐츠를 번역 서비스 (예: OpenAI 의 GPT 모델) 로 보내 번역합니다.

이 두 단계 프로세스 때문에 원본 PDF 의 품질이 번역 품질에 큰 영향을 미칩니다. 텍스트가 명확하고 레이아웃이 단순한 PDF 가 가장 좋은 결과를 제공합니다.
- The `finish` event is guaranteed to be the last event emitted by the generator.

---

### TRANSLATION RESULT

- 선택적으로 `stage_summary` 가 진행이 시작되기 전에 발생될 수 있습니다.
- 특정 실패 시, 생성자는 먼저 `error` 이벤트를 생성한 다음 `TranslationError` 에서 파생된 예외를 발생시킵니다. 오류 이벤트를 확인하고 예외를 잡을 준비를 모두 해야 합니다.
- `progress_update` 이벤트는 동일한 값으로 반복될 수 있습니다; 소비자는 필요한 경우 디바운스를 적용해야 합니다.
- `finish` 이벤트를 받으면 스트림 소비를 중지하세요.
- `finish` 이벤트는 생성자가 발생시키는 마지막 이벤트임이 보장됩니다.

{#minimal-usage-example-async}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # Initialize the translator
    translator = pdf2zh.Translator()

    # Translate a PDF file
    await translator.translate_pdf(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_language="zh-cn"
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### Minimal Usage Example (Sync) {#minimal-usage-example-sync}

```python
from pdf2zh import pdf2zh

# Initialize the translator
translator = pdf2zh.Translator()

# Translate a PDF file
translator.translate_pdf_sync(
    input_pdf="input.pdf",
    output_pdf="output.pdf",
    target_language="zh-cn"
)
```

### Advanced Usage Example {#advanced-usage-example}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # Initialize the translator with custom options
    translator = pdf2zh.Translator(
        # Specify the translation service
        service="google",
        
        # Set API key if required (for services like DeepL, OpenAI)
        api_key="your_api_key_here",
        
        # Configure processing options
        options={
            "ocr": True,           # Enable OCR for scanned PDFs
            "concurrency": 4,      # Number of concurrent translations
            "timeout": 30,         # Timeout per translation request (seconds)
        }
    )

    try:
        # Translate with detailed progress tracking
        result = await translator.translate_pdf(
            input_pdf="document.pdf",
            output_pdf="translated_document.pdf",
            target_language="ja",  # Japanese
            callback=lambda progress: print(f"Progress: {progress}%")
        )
        
        print("Translation completed!")
        print(f"Translated pages: {result.translated_pages}")
        print(f"Total characters: {result.total_characters}")
        
    except Exception as e:
        print(f"Translation failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Handling Large Documents {#handling-large-documents}

For large PDF documents, you may want to process them in chunks:

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    translator = pdf2zh.Translator()
    
    # Process specific page ranges
    await translator.translate_pdf(
        input_pdf="large_document.pdf",
        output_pdf="part1.pdf",
        target_language="zh-cn",
        page_range=(1, 50)  # Translate pages 1-50
    )
    
    await translator.translate_pdf(
        input_pdf="large_document.pdf",
        output_pdf="part2.pdf",
        target_language="zh-cn",
        page_range=(51, 100)  # Translate pages 51-100
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### Error Handling {#error-handling}

```python
import asyncio
from pdf2zh import pdf2zh
from pdf2zh.exceptions import TranslationError, PDFError

async def main():
    translator = pdf2zh.Translator()
    
    try:
        await translator.translate_pdf(
            input_pdf="document.pdf",
            output_pdf="translated.pdf",
            target_language="zh-cn"
        )
    except TranslationError as e:
        print(f"Translation error: {e}")
    except PDFError as e:
        print(f"PDF processing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Using Different Translation Services {#using-different-translation-services}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # Using Google Translate (free)
    google_translator = pdf2zh.Translator(service="google")
    await google_translator.translate_pdf(
        input_pdf="doc.pdf",
        output_pdf="doc_google.pdf",
        target_language="es"  # Spanish
    )
    
    # Using DeepL (requires API key)
    deepl_translator = pdf2zh.Translator(
        service="deepl",
        api_key="your_deepl_api_key"
    )
    await deepl_translator.translate_pdf(
        input_pdf="doc.pdf",
        output_pdf="doc_deepl.pdf",
        target_language="fr"  # French
    )
    
    # Using OpenAI GPT (requires API key)
    openai_translator = pdf2zh.Translator(
        service="openai",
        api_key="your_openai_api_key"
    )
    await openai_translator.translate_pdf(
        input_pdf="doc.pdf",
        output_pdf="doc_openai.pdf",
        target_language="de"  # German
    )

if __name__ == "__main__":
    asyncio.run(main())
```

---

### OUTPUT

### 최소 사용 예제 (비동기) {#최소 - 사용 - 예제 - 비동기}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # 번역기 초기화
    translator = pdf2zh.Translator()

    # PDF 파일 번역
    await translator.translate_pdf(
        input_pdf="input.pdf",
        output_pdf="output.pdf",
        target_language="zh-cn"
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### 최소 사용 예제 (동기) {#최소 - 사용 - 예제 - 동기}

```python
from pdf2zh import pdf2zh

# 번역기 초기화
translator = pdf2zh.Translator()

# PDF 파일 번역
translator.translate_pdf_sync(
    input_pdf="input.pdf",
    output_pdf="output.pdf",
    target_language="zh-cn"
)
```

### 고급 사용 예제 {#고급 - 사용 - 예제}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # 사용자 정의 옵션으로 번역기 초기화
    translator = pdf2zh.Translator(
        # 번역 서비스 지정
        service="google",
        
        # 필요한 경우 API 키 설정 (DeepL, OpenAI 등의 서비스용)
        api_key="your_api_key_here",
        
        # 처리 옵션 구성
        options={
            "ocr": True,           # 스캔된 PDF 에 대해 OCR 활성화
            "concurrency": 4,      # 동시 번역 수
            "timeout": 30,         # 번역 요청당 타임아웃 (초)
        }
    )

    try:
        # 자세한 진행 상황 추적과 함께 번역
        result = await translator.translate_pdf(
            input_pdf="document.pdf",
            output_pdf="translated_document.pdf",
            target_language="ja",  # 일본어
            callback=lambda progress: print(f"Progress: {progress}%")
        )
        
        print("번역 완료!")
        print(f"번역된 페이지: {result.translated_pages}")
        print(f"총 문자 수: {result.total_characters}")
        
    except Exception as e:
        print(f"번역 실패: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 대형 문서 처리 {#대형 - 문서 - 처리}

대형 PDF 문서의 경우 청크 단위로 처리할 수 있습니다:

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    translator = pdf2zh.Translator()
    
    # 특정 페이지 범위 처리
    await translator.translate_pdf(
        input_pdf="large_document.pdf",
        output_pdf="part1.pdf",
        target_language="zh-cn",
        page_range=(1, 50)  # 1-50 페이지 번역
    )
    
    await translator.translate_pdf(
        input_pdf="large_document.pdf",
        output_pdf="part2.pdf",
        target_language="zh-cn",
        page_range=(51, 100)  # 51-100 페이지 번역
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### 오류 처리 {#오류 - 처리}

```python
import asyncio
from pdf2zh import pdf2zh
from pdf2zh.exceptions import TranslationError, PDFError

async def main():
    translator = pdf2zh.Translator()
    
    try:
        await translator.translate_pdf(
            input_pdf="document.pdf",
            output_pdf="translated.pdf",
            target_language="zh-cn"
        )
    except TranslationError as e:
        print(f"번역 오류: {e}")
    except PDFError as e:
        print(f"PDF 처리 오류: {e}")
    except Exception as e:
        print(f"예기치 않은 오류: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 다른 번역 서비스 사용 {#다른 - 번역 - 서비스 - 사용}

```python
import asyncio
from pdf2zh import pdf2zh

async def main():
    # Google Translate 사용 (무료)
    google_translator = pdf2zh.Translator(service="google")
    await google_translator.translate_pdf(
        input_pdf="doc.pdf",
        output_pdf="doc_google.pdf",
        target_language="es"  # 스페인어
    )
    
    # DeepL 사용 (API 키 필요)
    deepl_translator = pdf2zh.Translator(
        service="deepl",
        api_key="your_deepl_api_key"
    )
    await deepl_translator.translate_pdf(
        input_pdf="doc.pdf",
        output_pdf="doc_deepl.pdf",
        target_language="fr"  # 프랑스어
    )
    
    # OpenAI GPT 사용 (API 키 필요)
    openai_translator = pdf2zh.Translator(
        service="openai",
        api_key="your_openai_api_key"
    )
    await openai_translator.translate_pdf(
        input_pdf="doc.pdf",
        output_pdf="doc_openai.pdf",
        target_language="de"  # 독일어
    )

if __name__ == "__main__":
    asyncio.run(main())
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

**Last updated: February 21, 2025**

#### Cancellation

You can cancel your subscription at any time. Your cancellation will take effect at the end of the current paid term.

#### Refunds

If you are not 100% satisfied with your purchase, we will refund your payment if the refund request is made within 14 days of the original purchase. No questions asked.

If you have any questions about our Cancellation and Refund Policy, please contact us:

- By email: pdf2zh@gmail.com

---

### TRANSLATION RESULT
python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    task = asyncio.create_task(
        do_translate_async_stream(
            pdf_file="document.pdf",
            output_file="translated_document.docx",
            target_lang="ko"
        )
    )
    
    # Cancel the task after 5 seconds
    await asyncio.sleep(5)
    task.cancel()
    
    try:
        async for status, result in task:
            print(f"Status: {status}, Result: {result}")
    except asyncio.CancelledError:
        print("Task was cancelled")

asyncio.run(main())
```

---

### TRANSLATION RESULT

스트림을 소비하는 작업을 취소할 수 있습니다. 취소는 기본 번역 과정으로 전파됩니다.

```python
import asyncio
from pdf2zh import do_translate_async_stream

async def main():
    task = asyncio.create_task(
        do_translate_async_stream(
            pdf_file="document.pdf",
            output_file="translated_document.docx",
            target_lang="ko"
        )
    )
    
    # 5 초 후 작업 취소
    await asyncio.sleep(5)
    task.cancel()
    
    try:
        async for status, result in task:
            print(f"Status: {status}, Result: {result}")
    except asyncio.CancelledError:
        print("작업이 취소되었습니다")

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

Below are some examples of event shapes that can be used in your game.

#### Basic Shapes

- **Circle**: `Circle(radius: 10)`
- **Rectangle**: `Rectangle(width: 20, height: 30)`
- **Polygon**: `Polygon(points: [Vector2(0, 0), Vector2(10, 0), Vector2(10, 10)])`

#### Compound Shapes

- **Union**: `Union(shape1, shape2)`
- **Difference**: `Difference(shape1, shape2)`
- **Intersection**: `Intersection(shape1, shape2)`

#### Transformations

- **Translate**: `Translate(shape, offset: Vector2(5, 5))`
- **Rotate**: `Rotate(shape, angle: 45)`
- **Scale**: `Scale(shape, factor: 2)`

---

### TRANSLATION

### 이벤트 도형 예시

다음은 게임에서 사용할 수 있는 이벤트 도형의 몇 가지 예시입니다.

#### 기본 도형

- **원**: `Circle(radius: 10)`
- **사각형**: `Rectangle(width: 20, height: 30)`
- **다각형**: `Polygon(points: [Vector2(0, 0), Vector2(10, 0), Vector2(10, 10)])`

#### 복합 도형

- **합집합**: `Union(shape1, shape2)`
- **차집합**: `Difference(shape1, shape2)`
- **교집합**: `Intersection(shape1, shape2)`

#### 변환

- **이동**: `Translate(shape, offset: Vector2(5, 5))`
- **회전**: `Rotate(shape, angle: 45)`
- **크기 조절**: `Scale(shape, factor: 2)`
```json
{
  "type": "stage_summary",
  "stage": "translation",
  "status": "completed",
  "progress": 1.0,
  "details": {
    "translated_pages": 10,
    "total_pages": 10,
    "translated_characters": 5000,
    "total_characters": 5000
  }
}
```

---

### TRANSLATION RESULT

단계 요약 이벤트 (예시):

```json
{
  "type": "stage_summary",
  "stage": "translation",
  "status": "completed",
  "progress": 1.0,
  "details": {
    "translated_pages": 10,
    "total_pages": 10,
    "translated_characters": 5000,
    "total_characters": 5000
  }
}
```
- ### Event Stream Contract: The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATED TEXT

### 이벤트 스트림 계약

이벤트 스트림 계약은 서버가 장기간 지속되는 HTTP 연결을 통해 클라이언트에 이벤트를 보낼 수 있도록 하는 서버와 클라이언트 간의 계약입니다. 이는 장기 실행 작업 중 진행 상황 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 이벤트의 스트림으로, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 줄바꿈으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 반드시 포함해야 하며 다른 필드를 포함할 수 있는 JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 에서 1 사이의 숫자인 `progress` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되었을 때 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생했을 때 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트가 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```
- ### Notes & Best Practices: #### Notes

- The translation speed depends on the model speed and the number of pages in the PDF. For large PDFs, it may take a while.
- The quality of translation depends on the translation service and the model. You might need to adjust the prompt for better results, especially for non-English to Chinese translations.
- Some PDFs might not be parsed correctly, leading to poor translation quality. In such cases, consider using other tools to convert the PDF to a more parse-friendly format (like HTML) first.

#### Best Practices

- For the best quality, use the `gpt-4` model (default). If you're on a budget, consider `gpt-3.5-turbo`.
- For better formatting, use the `markdown` output format (default). If you prefer a more WYSIWYG approach, use `html`.
- If the translation quality is not satisfactory, try adjusting the prompt. For example, you can ask the model to be more literal or more liberal in its translation.
- For PDFs with complex layouts, consider using the `--no-layout` option to ignore the layout and extract text only. This might improve translation quality but will lose formatting.
- For PDFs with many images, consider using OCR tools first to extract text from images.

---

Let's start!

---

### BYPASS LIST

- pdf2zh
- PDFMathTranslate
- ---

---

### TRANSLATION RESULT

### 참고사항 및 모범 사례

#### 참고사항

- 번역 속도는 모델 속도와 PDF 의 페이지 수에 따라 달라집니다. 큰 PDF 의 경우 시간이 좀 걸릴 수 있습니다.
- 번역 품질은 번역 서비스와 모델에 따라 달라집니다. 특히 비영어에서 중국어 번역의 경우 더 나은 결과를 위해 프롬프트를 조정해야 할 수 있습니다.
- 일부 PDF 는 올바르게 구문 분석되지 않아 번역 품질이 떨어질 수 있습니다. 이러한 경우 먼저 PDF 를 더 구문 분석하기 쉬운 형식 (예: HTML) 으로 변환하는 다른 도구를 사용하는 것을 고려하세요.

#### 모범 사례

- 최고 품질을 위해 `gpt-4` 모델 (기본값) 을 사용하세요. 예산이 부족하다면 `gpt-3.5-turbo` 를 고려하세요.
- 더 나은 서식을 위해 `markdown` 출력 형식 (기본값) 을 사용하세요. 더 WYSIWYG 접근 방식을 선호한다면 `html` 을 사용하세요.
- 번역 품질이 만족스럽지 않다면 프롬프트를 조정해 보세요. 예를 들어 모델에게 더 문자 그대로 또는 더 자유롭게 번역하도록 요청할 수 있습니다.
- 복잡한 레이아웃의 PDF 의 경우 레이아웃을 무시하고 텍스트만 추출하는 `--no-layout` 옵션을 사용하는 것을 고려하세요. 이렇게 하면 번역 품질은 향상될 수 있지만 서식은 잃게 됩니다.
- 이미지가 많은 PDF 의 경우 먼저 OCR 도구를 사용하여 이미지에서 텍스트를 추출하는 것을 고려하세요.

---

시작합시다!

---

### 우회 목록

- pdf2zh
- PDFMathTranslate
- ---
- ### Cancellation: and Refund Policy

**Last updated: February 21, 2025**

#### Cancellation

You can cancel your subscription at any time. Your cancellation will take effect at the end of the current paid term.

#### Refunds

If you are not 100% satisfied with your purchase, we will refund your payment if the refund request is made within 14 days of the original purchase. No questions asked.

If you have any questions about our Cancellation and Refund Policy, please contact us:

- By email: pdf2zh@gmail.com

---

### TRANSLATION RESULT

### 취소 및 환불 정책

**최종 업데이트: 2025 년 2 월 21 일**

#### 취소

구독은 언제든지 취소할 수 있습니다. 취소는 현재 유료 기간이 끝날 때 효력이 발생합니다.

#### 환불

구매에 100% 만족하지 못하는 경우, 원래 구매일로부터 14 일 이내에 환불 요청을 하면 환불해 드립니다. 별도의 질문 없이 처리됩니다.

취소 및 환불 정책에 대한 질문이 있으시면 다음으로 문의하세요:

- 이메일: pdf2zh@gmail.com
- ### Example Event Shapes: Below are some examples of event shapes that can be used in your game.

#### Basic Shapes

- **Circle**: `Circle(radius: 10)`
- **Rectangle**: `Rectangle(width: 20, height: 30)`
- **Polygon**: `Polygon(points: [Vector2(0, 0), Vector2(10, 0), Vector2(10, 10)])`

#### Compound Shapes

- **Union**: `Union(shape1, shape2)`
- **Difference**: `Difference(shape1, shape2)`
- **Intersection**: `Intersection(shape1, shape2)`

#### Transformations

- **Translate**: `Translate(shape, offset: Vector2(5, 5))`
- **Rotate**: `Rotate(shape, angle: 45)`
- **Scale**: `Scale(shape, factor: 2)`

---

### TRANSLATION

### 이벤트 도형 예시

다음은 게임에서 사용할 수 있는 이벤트 도형의 몇 가지 예시입니다.

#### 기본 도형

- **원**: `Circle(radius: 10)`
- **사각형**: `Rectangle(width: 20, height: 30)`
- **다각형**: `Polygon(points: [Vector2(0, 0), Vector2(10, 0), Vector2(10, 10)])`

#### 복합 도형

- **합집합**: `Union(shape1, shape2)`
- **차집합**: `Difference(shape1, shape2)`
- **교집합**: `Intersection(shape1, shape2)`

#### 변환

- **이동**: `Translate(shape, offset: Vector2(5, 5))`
- **회전**: `Rotate(shape, angle: 45)`
- **크기 조절**: `Scale(shape, factor: 2)`
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

```json
{"type": "progress", "progress": 0.5}
```

Complete event (example): 

```json
{"type": "complete", "result": "..."}
```

Error event (example): 

```json
{"type": "error", "error": "An error occurred"}
```

---

### TRANSLATION RESULT

진행 이벤트 (예시): 

```json
{"type": "progress", "progress": 0.5}
```

완료 이벤트 (예시): 

```json
{"type": "complete", "result": "..."}
```

오류 이벤트 (예시): 

```json
{"type": "error", "error": "An error occurred"}
```

---

### ORIGINAL TEXT

### Event Stream Contract

The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATION RESULT

### 이벤트 스트림 계약

이벤트 스트림 계약은 서버가 장기간 지속되는 HTTP 연결을 통해 클라이언트에 이벤트를 보낼 수 있도록 하는 서버와 클라이언트 간의 계약입니다. 이는 장기 실행 작업 중 진행 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 각 이벤트가 JSON 객체인 이벤트 스트림입니다. 이벤트 스트림은 줄바꿈으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 **반드시** 포함해야 하며 다른 필드를 **포함할 수 있는** JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 과 1 사이의 숫자인 `progress` 필드를 **반드시** 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되면 전송됩니다. 작업 결과를 포함하는 `result` 필드를 **포함할 수 있습니다**.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생하면 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 **반드시** 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트가 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### ORIGINAL TEXT

### Notes & Best Practices

#### Notes

- The translation speed depends on the model speed and the number of pages in the PDF. For large PDFs, it may take a while.
- The quality of translation depends on the translation service and the model. You might need to adjust the prompt for better results, especially for non-English to Chinese translations.
- Some PDFs might not be parsed correctly, leading to poor translation quality. In such cases, consider using other tools to convert the PDF to a more parse-friendly format (like HTML) first.

#### Best Practices

- For the best quality, use the `gpt-4` model (default). If you're on a budget, consider `gpt-3.5-turbo`.
- For better formatting, use the `markdown` output format (default). If you prefer a more WYSIWYG approach, use `html`.
- If the translation quality is not satisfactory, try adjusting the prompt. For example, you can ask the model to be more literal or more liberal in its translation.
- For PDFs with complex layouts, consider using the `--no-layout` option to ignore the layout and extract text only. This might improve translation quality but will lose formatting.
- For PDFs with many images, consider using OCR tools first to extract text from images.

---

### TRANSLATION RESULT

### 참고사항 및 모범 사례

#### 참고사항

- 번역 속도는 모델 속도와 PDF 의 페이지 수에 따라 다릅니다. 대형 PDF 의 경우 시간이 좀 걸릴 수 있습니다.
- 번역 품질은 번역 서비스와 모델에 따라 다릅니다. 특히 비영어에서 중국어 번역의 경우 더 나은 결과를 위해 프롬프트를 조정해야 할 수 있습니다.
- 일부 PDF 는 올바르게 구문 분석되지 않아 번역 품질이 낮아질 수 있습니다. 이런 경우 먼저 PDF 를 더 구문 분석하기 쉬운 형식 (예: HTML) 으로 변환하는 다른 도구를 사용하는 것을 고려하세요.

#### 모범 사례

- 최고의 품질을 위해 `gpt-4` 모델 (기본값) 을 사용하세요. 예산이 부담된다면 `gpt-3.5-turbo` 를 고려하세요.
- 더 나은 서식을 위해 `markdown` 출력 형식 (기본값) 을 사용하세요. 더 WYSIWYG 방식을 선호한다면 `html` 을 사용하세요.
- 번역 품질이 만족스럽지 않다면 프롬프트를 조정해 보세요. 예를 들어, 모델에게 더 직역하거나 더 의역하도록 요청할 수 있습니다.
- 복잡한 레이아웃의 PDF 의 경우 레이아웃을 무시하고 텍스트만 추출하는 `--no-layout` 옵션 사용을 고려하세요. 이는 번역 품질을 향상시킬 수 있지만 서식을 잃을 수 있습니다.
- 이미지가 많은 PDF 의 경우 먼저 OCR 도구를 사용하여 이미지에서 텍스트를 추출하는 것을 고려하세요.

---

### ORIGINAL TEXT

### Cancellation and Refund Policy

**Last updated: February 21, 2025**

#### Cancellation

You can cancel your subscription at any time. Your cancellation will take effect at the end of the current paid term.

#### Refunds

If you are not 100% satisfied with your purchase, we will refund your payment if the refund request is made within 14 days of the original purchase. No questions asked.

If you have any questions about our Cancellation and Refund Policy, please contact us:

- By email: pdf2zh@gmail.com

---

### TRANSLATION RESULT

### 취소 및 환불 정책

**최종 업데이트: 2025 년 2 월 21 일**

#### 취소

구독은 언제든지 취소할 수 있습니다. 취소는 현재 유료 기간이 끝날 때 효력이 발생합니다.

#### 환불

구매에 100% 만족하지 못하는 경우, 원래 구매일로부터 14 일 이내에 환불 요청을 하면 결제 금액을 환불해 드립니다. 별도의 질문 없이 환불해 드립니다.

취소 및 환불 정책에 대한 질문이 있으시면 다음으로 문의해 주세요:

- 이메일: pdf2zh@gmail.com
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

This event is emitted when the translation is complete.

```json
{
    "type": "finish",
    "data": {
        "text": "The translated text",
        "source_language": "en",
        "target_language": "zh"
    }
}
```

### Event Stream Contract: The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATED TEXT
### 완료 이벤트 (예시): 이 이벤트는 번역이 완료되었을 때 발생합니다.

```json
{
    "type": "finish",
    "data": {
        "text": "번역된 텍스트",
        "source_language": "en",
        "target_language": "zh"
    }
}
```

### 이벤트 스트림 계약: 이벤트 스트림 계약은 서버가 장기 실행 HTTP 연결을 통해 클라이언트에게 이벤트를 보낼 수 있게 하는 서버와 클라이언트 간의 계약입니다. 이는 장기 실행 작업 중 진행 상황 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 이벤트의 스트림이며, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 줄바꿈으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 반드시 포함해야 하며 다른 필드를 포함할 수 있는 JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 과 1 사이의 숫자인 `progress` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되었을 때 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생했을 때 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트가 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
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

`{"type": "error", "error": "An error occurred"}`

---

### TRANSLATION RESULT

오류 이벤트 (예시): `{"type": "error", "error": "An error occurred"}`

---

### ORIGINAL TEXT

### Event Stream Contract

The event stream contract is a contract between the server and client that allows the server to send events to the client over a long-lived HTTP connection. This is useful for real-time updates, such as progress updates during a long-running operation.

### Event Stream Format

The event stream is a stream of events, each event is a JSON object. The event stream is sent as a stream of newline-separated JSON objects. Each event is a JSON object that MUST contain a `type` field and MAY contain other fields.

Example:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### Event Types

#### `progress`

The `progress` event is sent to indicate the progress of a long-running operation. It MUST contain a `progress` field that is a number between 0 and 1.

Example:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

The `complete` event is sent when the operation is complete. It MAY contain a `result` field that contains the result of the operation.

Example:

```json
{"type": "complete", "result": "..."}
```

#### `error`

The `error` event is sent when an error occurs. It MUST contain an `error` field that contains the error message.

Example:

```json
{"type": "error", "error": "An error occurred"}
```

### Usage

To use the event stream, the client should make a request to the server with the `Accept` header set to `application/x-ndjson`. The server will then stream events as they occur.

Example using `curl`:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

Example using JavaScript:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```

---

### TRANSLATION RESULT

### 이벤트 스트림 계약

이벤트 스트림 계약은 서버가 장기간 지속되는 HTTP 연결을 통해 클라이언트에 이벤트를 보낼 수 있도록 하는 서버와 클라이언트 간의 계약입니다. 이는 장기 실행 작업 중 진행 업데이트와 같은 실시간 업데이트에 유용합니다.

### 이벤트 스트림 형식

이벤트 스트림은 이벤트의 스트림이며, 각 이벤트는 JSON 객체입니다. 이벤트 스트림은 개행으로 구분된 JSON 객체 스트림으로 전송됩니다. 각 이벤트는 `type` 필드를 반드시 포함해야 하고 다른 필드를 포함할 수 있는 JSON 객체입니다.

예시:

```json
{"type": "progress", "progress": 0.5}
{"type": "progress", "progress": 0.75}
{"type": "progress", "progress": 1.0}
{"type": "complete", "result": "..."}
```

### 이벤트 유형

#### `progress`

`progress` 이벤트는 장기 실행 작업의 진행 상황을 나타내기 위해 전송됩니다. 0 과 1 사이의 숫자인 `progress` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "progress", "progress": 0.5}
```

#### `complete`

`complete` 이벤트는 작업이 완료되면 전송됩니다. 작업 결과를 포함하는 `result` 필드를 포함할 수 있습니다.

예시:

```json
{"type": "complete", "result": "..."}
```

#### `error`

`error` 이벤트는 오류가 발생하면 전송됩니다. 오류 메시지를 포함하는 `error` 필드를 반드시 포함해야 합니다.

예시:

```json
{"type": "error", "error": "An error occurred"}
```

### 사용법

이벤트 스트림을 사용하려면 클라이언트가 `Accept` 헤더를 `application/x-ndjson` 으로 설정하여 서버에 요청해야 합니다. 그러면 서버는 이벤트가 발생할 때 스트리밍합니다.

`curl` 사용 예시:

```bash
curl -H "Accept: application/x-ndjson" https://pdf2zh-next.com/api/translate
```

JavaScript 사용 예시:

```javascript
const eventSource = new EventSource('/api/translate');

eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  if (data.type === 'progress') {
    console.log(`Progress: ${data.progress}`);
  } else if (data.type === 'complete') {
    console.log(`Result: ${data.result}`);
  } else if (data.type === 'error') {
    console.error(`Error: ${data.error}`);
  }
};
```
- ### Notes & Best Practices: #### Notes

- The translation speed depends on the model speed and the number of pages in the PDF. For large PDFs, it may take a while.
- The quality of translation depends on the translation service and the model. You might need to adjust the prompt for better results, especially for non-English to Chinese translations.
- Some PDFs might not be parsed correctly, leading to poor translation quality. In such cases, consider using other tools to convert the PDF to a more parse-friendly format (like HTML) first.

#### Best Practices

- For the best quality, use the `gpt-4` model (default). If you're on a budget, consider `gpt-3.5-turbo`.
- For better formatting, use the `markdown` output format (default). If you prefer a more WYSIWYG approach, use `html`.
- If the translation quality is not satisfactory, try adjusting the prompt. For example, you can ask the model to be more literal or more liberal in its translation.
- For PDFs with complex layouts, consider using the `--no-layout` option to ignore the layout and extract text only. This might improve translation quality but will lose formatting.
- For PDFs with many images, consider using OCR tools first to extract text from images.

---

Let's start!

---

### BYPASS LIST

- pdf2zh
- PDFMathTranslate
- ---

---

### TRANSLATION RESULT

### 참고사항 및 모범 사례

#### 참고사항

- 번역 속도는 모델 속도와 PDF 의 페이지 수에 따라 달라집니다. 큰 PDF 의 경우 시간이 걸릴 수 있습니다.
- 번역 품질은 번역 서비스와 모델에 따라 달라집니다. 특히 비영어에서 중국어 번역의 경우 더 나은 결과를 위해 프롬프트를 조정해야 할 수 있습니다.
- 일부 PDF 는 올바르게 구문 분석되지 않아 번역 품질이 낮아질 수 있습니다. 이러한 경우 먼저 PDF 를 더 구문 분석하기 쉬운 형식 (예: HTML) 으로 변환하는 다른 도구를 사용하는 것을 고려하세요.

#### 모범 사례

- 최고 품질을 위해 `gpt-4` 모델 (기본값) 을 사용하세요. 예산이 부족하다면 `gpt-3.5-turbo` 를 고려하세요.
- 더 나은 서식을 위해 `markdown` 출력 형식 (기본값) 을 사용하세요. 더 WYSIWYG 접근 방식을 선호한다면 `html` 을 사용하세요.
- 번역 품질이 만족스럽지 않다면 프롬프트를 조정해 보세요. 예를 들어 모델에게 더 직역하거나 더 자유롭게 번역하도록 요청할 수 있습니다.
- 복잡한 레이아웃의 PDF 의 경우 레이아웃을 무시하고 텍스트만 추출하는 `--no-layout` 옵션을 사용하는 것을 고려하세요. 이는 번역 품질을 향상시킬 수 있지만 서식을 잃을 수 있습니다.
- 이미지가 많은 PDF 의 경우 먼저 OCR 도구를 사용하여 이미지에서 텍스트를 추출하는 것을 고려하세요.

---

시작합시다!

---

### 우회 목록

- pdf2zh
- PDFMathTranslate
- ---
- ### Cancellation and Refund Policy

**Last updated: February 21, 2025**

#### Cancellation

You can cancel your subscription at any time. Your cancellation will take effect at the end of the current paid term.

#### Refunds

If you are not 100% satisfied with your purchase, we will refund your payment if the refund request is made within 14 days of the original purchase. No questions asked.

If you have any questions about our Cancellation and Refund Policy, please contact us:

- By email: pdf2zh@gmail.com

---

### TRANSLATION RESULT

### 취소 및 환불 정책

**최종 업데이트: 2025 년 2 월 21 일**

#### 취소

구독은 언제든지 취소할 수 있습니다. 취소는 현재 유료 기간이 끝날 때 효력이 발생합니다.

#### 환불

구매에 100% 만족하지 못하는 경우, 원래 구매일로부터 14 일 이내에 환불 요청을 하면 환불해 드립니다. 별도의 질문 없이 처리합니다.

취소 및 환불 정책에 대한 질문이 있으면 다음으로 문의하세요:

- 이메일: pdf2zh@gmail.com
- ### Example Event Shapes: Below are some examples of event shapes that can be used in your game.

#### Basic Shapes

- **Circle**: `Circle(radius: 10)`
- **Rectangle**: `Rectangle(width: 20, height: 30)`
- **Polygon**: `Polygon(points: [Vector2(0, 0), Vector2(10, 0), Vector2(10, 10)])`

#### Compound Shapes

- **Union**: `Union(shape1, shape2)`
- **Difference**: `Difference(shape1, shape2)`
- **Intersection**: `Intersection(shape1, shape2)`

#### Transformations

- **Translate**: `Translate(shape, offset: Vector2(5, 5))`
- **Rotate**: `Rotate(shape, angle: 45)`
- **Scale**: `Scale(shape, factor: 2)`

---

### TRANSLATION RESULT

### 이벤트 도형 예시

다음은 게임에서 사용할 수 있는 이벤트 도형의 몇 가지 예시입니다.

#### 기본 도형

- **원**: `Circle(radius: 10)`
- **사각형**: `Rectangle(width: 20, height: 30)`
- **다각형**: `Polygon(points: [Vector2(0, 0), Vector2(10, 0), Vector2(10, 10)])`

#### 복합 도형

- **합집합**: `Union(shape1, shape2)`
- **차집합**: `Difference(shape1, shape2)`
- **교집합**: `Intersection(shape1, shape2)`

#### 변환

- **이동**: `Translate(shape, offset: Vector2(5, 5))`
- **회전**: `Rotate(shape, angle: 45)`
- **크기 조절**: `Scale(shape, factor: 2)`
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

#### Notes

- The translation speed depends on the model speed and the number of pages in the PDF. For large PDFs, it may take a while.
- The quality of translation depends on the translation service and the model. You might need to adjust the prompt for better results, especially for non-English to Chinese translations.
- Some PDFs might not be parsed correctly, leading to poor translation quality. In such cases, consider using other tools to convert the PDF to a more parse-friendly format (like HTML) first.

#### Best Practices

- For the best quality, use the `gpt-4` model (default). If you're on a budget, consider `gpt-3.5-turbo`.
- For better formatting, use the `markdown` output format (default). If you prefer a more WYSIWYG approach, use `html`.
- If the translation quality is not satisfactory, try adjusting the prompt. For example, you can ask the model to be more literal or more liberal in its translation.
- For PDFs with complex layouts, consider using the `--no-layout` option to ignore the layout and extract text only. This might improve translation quality but will lose formatting.
- For PDFs with many images, consider using OCR tools first to extract text from images.

---

Let's start!
---

### TRANSLATION

- 생성자에서 발생하는 오류 이벤트와 예외를 모두 처리하세요.
- 불필요한 작업을 피하기 위해 `finish` 에서 루프를 종료하세요.
- 호출하기 전에 `file` 이 존재하고 `settings.validate_settings()` 가 통과하는지 확인하세요.
- 대형 문서는 분할될 수 있습니다; `part_index/total_parts` 와 `overall_progress` 를 사용하여 UI 를 구동하세요.
- UI 가 반복적이고 동일한 업데이트에 민감한 경우 `progress_update` 를 디바운스하세요.
- `report_interval` (SettingsModel): `progress_update` 이벤트의 방출 속도만 제어합니다. `stage_summary`, `progress_start`, `progress_end` 또는 `finish` 에는 영향을 미치지 않습니다. 기본값은 0.1 초이며 허용되는 최소값은 0.05 초입니다. 진행 모니터 로직에 따라 `stage_total <= 3`일 때 업데이트는 `report_interval` 에 의해 조절되지 않습니다.

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>