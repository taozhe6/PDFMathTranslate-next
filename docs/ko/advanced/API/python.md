> [!NOTE]
> 이 문서에는 AI 생성 콘텐츠가 포함될 수 있습니다. 정확성을 위해 노력하고 있지만 부정확한 내용이 있을 수 있습니다. 문제가 발견되면 다음을 통해 신고해 주세요:
>
> - [GitHub Issues](https://github.com/PDFMathTranslate-next/PDFMathTranslate-next/issues)
> - 커뮤니티 기여 (PR 환영합니다!)

## Python API: do_translate_async_stream

### 개요
- do_translate_async_stream 은 단일 PDF 를 번역하고 이벤트 (진행 상황/오류/완료) 스트림을 생성하는 저수준 비동기 진입점입니다.
- 실시간 진행 상황과 결과에 대한 완전한 제어를 원하는 사용자 정의 UI 나 CLI 를 구축하는 데 적합합니다.
- 유효성이 검증된 SettingsModel 과 파일 경로를 수락하고, dict 이벤트의 비동기 생성기를 반환합니다.

### 서명
- Import: `from pdf2zh_next.high_level import do_translate_async_stream`
- Call: `async for event in do_translate_async_stream(settings, file): ...`
- Parameters:
  - settings: SettingsModel. 유효해야 합니다; 함수는 `settings.validate_settings()` 를 호출합니다.
  - file: str | pathlib.Path. 번역할 단일 PDF 파일입니다. 존재해야 합니다.

참고:

- `settings.basic.input_files` 는 이 함수에서 무시됩니다; 주어진 `file` 만 번역됩니다.
- `settings.basic.debug` 가 True 인 경우, 번역은 메인 프로세스에서 실행됩니다; 그렇지 않으면 하위 프로세스에서 실행됩니다. 두 경우 모두 이벤트 스키마는 동일합니다.

### 이벤트 스트림 계약
비동기 생성자는 다음과 같은 유형의 JSON 형식 dict 이벤트를 생성합니다:

- 단계 요약 이벤트: `stage_summary` (선택 사항, 처음 나타날 수 있음)
  - 필드
    - `type`: "stage_summary"
    - `stages`: 예상 작업 분포를 설명하는 객체 `{ "name": str, "percent": float }`의 목록
    - `part_index`: 이 요약 이벤트의 경우 0 일 수 있음
    - `total_parts`: 전체 부분 수 (>= 1)

- 진행 상황 이벤트: `progress_start`, `progress_update`, `progress_end`
  - 공통 필드
    - `type`: 위 중 하나
    - `stage`: 사람이 읽을 수 있는 단계 이름 (예: "PDF 구문 분석 및 중간 표현 생성", "단락 번역", "PDF 저장")
    - `stage_progress`: 현재 단계 내 진행률을 나타내는 [0, 100] 범위의 float
    - `overall_progress`: 전체 진행률을 나타내는 [0, 100] 범위의 float
    - `part_index`: 현재 부분 인덱스 (일반적으로 진행 상황 이벤트의 경우 1 부터 시작)
    - `total_parts`: 전체 부분 수 (>= 1). 큰 문서는 자동으로 분할될 수 있음.
    - `stage_current`: 단계 내 현재 단계
    - `stage_total`: 단계 내 전체 단계 수

- 완료 이벤트: `finish`
  - 필드
    - `type`: "finish"
    - `translate_result`: 최종 출력을 제공하는 **객체** (참고: 사전이 아닌 클래스 인스턴스)
      - `original_pdf_path`: 입력 PDF 경로
      - `mono_pdf_path`: 단일 언어 번역 PDF 경로 (또는 None)
      - `dual_pdf_path`: 이중 언어 번역 PDF 경로 (또는 None)
      - `no_watermark_mono_pdf_path`: 워터마크가 없는 단일 언어 출력 경로 (생성된 경우), 그렇지 않으면 None
      - `no_watermark_dual_pdf_path`: 워터마크가 없는 이중 언어 출력 경로 (생성된 경우), 그렇지 않으면 None
      - `auto_extracted_glossary_path`: 자동 추출 용어집 CSV 경로 (또는 None)
      - `total_seconds`: 경과 시간 (초, float)
      - `peak_memory_usage`: 번역 중 대략적인 최대 메모리 사용량 (float; 구현에 따른 단위)

- 오류 이벤트: `error`
  - 필드
    - `type`: "error"
    - `error`: 사람이 읽을 수 있는 오류 메시지
    - `error_type`: `BabeldocError`, `SubprocessError`, `IPCError`, `SubprocessCrashError` 등 중 하나
    - `details`: 선택적 세부 정보 (예: 원본 오류 또는 트레이스백)

중요한 동작:
- 선택적으로 `stage_summary` 가 진행률이 시작되기 전에 발생할 수 있습니다.
- 특정 실패 시, 생성기는 먼저 `error` 이벤트를 yield 한 다음 `TranslationError` 에서 파생된 예외를 발생시킵니다. 오류 이벤트를 확인하고 예외를 catch 할 준비를 모두 해야 합니다.
- `progress_update` 이벤트는 동일한 값으로 반복될 수 있습니다; 필요하다면 소비자는 디바운싱을 해야 합니다.
- `finish` 이벤트를 수신하면 스트림 소비를 중지하세요.

### 최소 사용 예시 (비동기)
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

### 취소
작업을 취소하면 스트림을 소비하는 작업이 취소됩니다. 취소는 기본 번역 프로세스로 전파됩니다.

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

### 이벤트 모양 예시
단계 요약 이벤트 (예시):
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

Progress event (예시):
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

Finish event (예시):
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

Error event (example):
```json
{
  "type": "error",
  "error": "Babeldoc translation error: <message>",
  "error_type": "BabeldocError",
  "details": "<optional original error or traceback>"
}
```

### 참고 사항 및 모범 사례
- 항상 생성기에서 발생하는 오류 이벤트와 예외를 모두 처리하십시오.
- 불필요한 작업을 피하기 위해 `finish` 이벤트에서 루프를 중단하십시오.
- 호출하기 전에 `file` 이 존재하고 `settings.validate_settings()` 가 통과하는지 확인하십시오.
- 대형 문서는 분할될 수 있습니다. `part_index/total_parts` 와 `overall_progress` 를 사용하여 UI 를 구동하십시오.
- UI 가 반복적이고 동일한 업데이트에 민감한 경우 `progress_update` 이벤트를 디바운스하십시오.
- `report_interval` (SettingsModel): `progress_update` 이벤트의 발생 빈도만 제어합니다. `stage_summary`, `progress_start`, `progress_end` 또는 `finish` 에는 영향을 미치지 않습니다. 기본값은 0.1 초이며 허용되는 최소값은 0.05 초입니다. 진행률 모니터 로직에 따라, `stage_total <= 3`일 때 업데이트는 `report_interval` 에 의해 제한되지 않습니다.

<div align="right"> 
<h6><small>이 페이지의 일부 내용은 GPT 에 의해 번역되었으며 오류가 포함될 수 있습니다.</small></h6>