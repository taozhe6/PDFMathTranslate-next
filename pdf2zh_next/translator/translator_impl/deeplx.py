import logging

import requests
from pdf2zh_next.config.model import SettingsModel
from pdf2zh_next.translator.base_rate_limiter import BaseRateLimiter
from pdf2zh_next.translator.base_translator import BaseTranslator
from tenacity import before_sleep_log
from tenacity import retry
from tenacity import retry_if_exception_type
from tenacity import stop_after_attempt
from tenacity import wait_exponential

logger = logging.getLogger(__name__)


class DeepLXTranslator(BaseTranslator):
    """DeepLX translator implementation"""

    name = "deeplx"
    lang_map = {"zh": "ZH", "zh-hans": "ZH", "zh-cn": "ZH"}

    def __init__(
        self,
        settings: SettingsModel,
        rate_limiter: BaseRateLimiter,
    ):
        super().__init__(settings, rate_limiter)

        # Get DeepLX configuration - following project pattern
        config = settings.translate_engine_settings

        # Direct attribute access like OpenAI pattern
        self.base_url = config.deeplx_base_url
        if self.base_url:
            self.base_url = self.base_url.rstrip("/")

        # Timeout handling with type conversion
        self.timeout = config.deeplx_timeout
        if self.timeout:
            try:
                self.timeout = float(self.timeout)
            except (ValueError, TypeError):
                self.timeout = 30.0
                logger.warning("Invalid timeout value, using default 30 seconds")
        else:
            self.timeout = 30.0

        # Create session for connection reuse
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json",
                "User-Agent": "PDFMathTranslate-next/DeepLX-Client",
            }
        )

    @retry(
        retry=retry_if_exception_type(Exception),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
    )
    def do_translate(self, text, rate_limit_params: dict = None):
        """Execute translation request"""
        if not text or not text.strip():
            return ""

        # Handle language code mapping
        source_lang = self.lang_in or "AUTO"
        target_lang = self.lang_out

        # DeepLX language code mapping
        lang_mapping = {
            "zh": "ZH",
            "zh-hans": "ZH",
            "zh-cn": "ZH",
            "en": "EN",
            "auto": "AUTO",
        }

        # Apply language mapping
        if source_lang.lower() in lang_mapping:
            source_lang = lang_mapping[source_lang.lower()]
        else:
            source_lang = source_lang.upper()

        if target_lang.lower() in lang_mapping:
            target_lang = lang_mapping[target_lang.lower()]
        else:
            target_lang = target_lang.upper()

        # Construct request payload
        payload = {"text": text, "source_lang": source_lang, "target_lang": target_lang}

        # Try /deepl endpoint first (recommended), fallback to /translate
        endpoints = ["/deepl", "/translate"]
        last_error = None

        for endpoint in endpoints:
            try:
                response = self.session.post(
                    f"{self.base_url}{endpoint}", json=payload, timeout=self.timeout
                )

                # Check HTTP status code
                response.raise_for_status()

                # Parse response
                result = response.json()

                # Check DeepLX API response format
                if not isinstance(result, dict):
                    raise ValueError("Invalid response format from DeepLX API")

                if result.get("code") == 200 and "data" in result:
                    return result["data"]
                else:
                    error_msg = result.get("message", "Unknown error")
                    error_code = result.get("code", "unknown")
                    raise Exception(
                        f"DeepLX API error (code: {error_code}): {error_msg}"
                    )

            except requests.exceptions.Timeout:
                last_error = Exception(
                    f"DeepLX request timeout after {self.timeout} seconds"
                )
                continue
            except requests.exceptions.ConnectionError:
                last_error = Exception(
                    f"Cannot connect to DeepLX service at {self.base_url}{endpoint}"
                )
                continue
            except requests.exceptions.HTTPError as e:
                last_error = Exception(f"DeepLX HTTP error on {endpoint}: {e}")
                continue
            except (ValueError, KeyError) as e:
                last_error = Exception(
                    f"DeepLX response parsing error on {endpoint}: {e}"
                )
                continue

        # If all endpoints failed, raise the last error
        if last_error:
            raise last_error
        else:
            raise Exception("All DeepLX endpoints failed")

    def __del__(self):
        """Clean up resources"""
        if hasattr(self, "session"):
            self.session.close()
