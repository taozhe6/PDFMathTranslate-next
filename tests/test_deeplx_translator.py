# DeepLX translator test file
# This file is used to test various features of the DeepLX translator

from unittest.mock import Mock

import pytest
from pdf2zh_next.config.model import SettingsModel
from pdf2zh_next.config.translate_engine_model import DeepLXSettings
from pdf2zh_next.translator.base_rate_limiter import BaseRateLimiter
from pdf2zh_next.translator.translator_impl.deeplx import DeepLXTranslator


class TestDeepLXTranslator:
    """DeepLX translator test class"""

    def setup_method(self):
        """Setup before each test"""
        # Create mock settings
        self.deeplx_settings = DeepLXSettings(
            deeplx_base_url="https://test-deeplx.com", deeplx_timeout="30"
        )

        # Create mock SettingsModel
        self.settings = Mock(spec=SettingsModel)
        self.settings.translate_engine_settings = self.deeplx_settings
        self.settings.translation = Mock()
        self.settings.translation.lang_in = "en"
        self.settings.translation.lang_out = "zh"
        self.settings.translation.ignore_cache = False

        # Create mock rate limiter
        self.rate_limiter = Mock(spec=BaseRateLimiter)

    def test_translator_initialization(self):
        """Test translator initialization"""
        translator = DeepLXTranslator(self.settings, self.rate_limiter)

        # Verify basic attributes
        assert translator.name == "deeplx"
        assert translator.base_url == "https://test-deeplx.com"
        assert translator.timeout == 30.0
        assert hasattr(translator, "session")

    def test_language_mapping(self):
        """Test language code mapping"""
        translator = DeepLXTranslator(self.settings, self.rate_limiter)

        # Test Chinese mapping
        assert "zh" in translator.lang_map
        assert translator.lang_map["zh"] == "ZH"
        assert translator.lang_map["zh-hans"] == "ZH"
        assert translator.lang_map["zh-cn"] == "ZH"

    def test_successful_translation_deepl_endpoint(self, requests_mock):
        """Test successful translation using /deepl endpoint"""
        # Mock successful API response
        requests_mock.post(
            "https://test-deeplx.com/deepl",
            json={
                "code": 200,
                "data": "你好，世界！",
                "source_lang": "EN",
                "target_lang": "ZH",
            },
        )

        translator = DeepLXTranslator(self.settings, self.rate_limiter)
        result = translator.do_translate("Hello, world!")

        assert result == "你好，世界！"
        # Verify request parameters
        request_json = requests_mock.last_request.json()
        assert request_json["text"] == "Hello, world!"
        assert request_json["source_lang"] == "EN"
        assert request_json["target_lang"] == "ZH"

    def test_fallback_to_translate_endpoint(self, requests_mock):
        """Test fallback from /deepl endpoint to /translate endpoint"""
        # /deepl endpoint returns error
        requests_mock.post("https://test-deeplx.com/deepl", status_code=404)

        # /translate endpoint returns success
        requests_mock.post(
            "https://test-deeplx.com/translate",
            json={"code": 200, "data": "你好，世界！"},
        )

        translator = DeepLXTranslator(self.settings, self.rate_limiter)
        result = translator.do_translate("Hello, world!")

        assert result == "你好，世界！"
        # Verify both endpoints were called
        assert len(requests_mock.request_history) == 2
        assert requests_mock.request_history[0].url == "https://test-deeplx.com/deepl"
        assert (
            requests_mock.request_history[1].url == "https://test-deeplx.com/translate"
        )

    def test_api_error_handling(self, requests_mock):
        """Test API error handling"""
        # Mock API error response
        requests_mock.post(
            "https://test-deeplx.com/deepl",
            json={"code": 429, "message": "Too many requests"},
        )
        requests_mock.post(
            "https://test-deeplx.com/translate",
            json={"code": 429, "message": "Too many requests"},
        )

        translator = DeepLXTranslator(self.settings, self.rate_limiter)

        # Expect RetryError after exhausting all retry attempts
        from tenacity import RetryError

        with pytest.raises(RetryError):
            translator.do_translate("Hello, world!")

    def test_empty_text_handling(self):
        """Test empty text handling"""
        translator = DeepLXTranslator(self.settings, self.rate_limiter)

        # Test empty strings
        assert translator.do_translate("") == ""
        assert translator.do_translate("   ") == ""
        assert translator.do_translate(None) == ""

    def test_timeout_configuration(self):
        """Test timeout configuration"""
        # Test valid timeout value
        settings = DeepLXSettings(
            deeplx_base_url="https://test.com", deeplx_timeout="45"
        )
        self.settings.translate_engine_settings = settings

        translator = DeepLXTranslator(self.settings, self.rate_limiter)
        assert translator.timeout == 45.0

        # Test invalid timeout value
        settings.deeplx_timeout = "invalid"
        translator = DeepLXTranslator(self.settings, self.rate_limiter)
        assert translator.timeout == 30.0  # Should fallback to default

    def test_url_cleanup(self):
        """Test URL cleanup"""
        settings = DeepLXSettings(
            deeplx_base_url="https://test.com/",  # With trailing slash
            deeplx_timeout="30",
        )
        self.settings.translate_engine_settings = settings

        translator = DeepLXTranslator(self.settings, self.rate_limiter)
        assert translator.base_url == "https://test.com"  # Slash should be removed


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
