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
    # Based on DeepLX API documentation and PDF2ZH-Next supported languages
    # DeepLX uses uppercase codes and maps all Chinese variants to ZH
    lang_map = {
        "zh": "ZH",
        "zh-hans": "ZH",
        "zh-cn": "ZH",
        "zh-hk": "ZH",  # Add missing Hong Kong Chinese
        "zh-tw": "ZH",  # Add missing Taiwan Chinese
        "en": "EN",
        "auto": "AUTO",
    }

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

        # Handle language code mapping using class lang_map
        source_lang = self.lang_in or "AUTO"
        target_lang = self.lang_out

        # Apply language mapping from class attribute, fallback to uppercase
        source_lang = self.lang_map.get(source_lang.lower(), source_lang.upper())
        target_lang = self.lang_map.get(target_lang.lower(), target_lang.upper())

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
