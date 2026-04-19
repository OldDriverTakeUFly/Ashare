import pytest

from ashare.config.settings import SettingsError, TelegramSettings


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("true", True),
        ("1", True),
        ("yes", True),
        ("on", True),
        ("false", False),
    ],
)
def test_from_env_parses_enabled_flag(monkeypatch, raw, expected):
    monkeypatch.setenv("ASHARE_TELEGRAM_ENABLED", raw)
    if expected:
        monkeypatch.setenv("ASHARE_TELEGRAM_BOT_TOKEN", "token")
        monkeypatch.setenv("ASHARE_TELEGRAM_CHAT_ID", "123")

    settings = TelegramSettings.from_env()

    assert settings.enabled is expected


def test_enabled_requires_bot_token(monkeypatch):
    monkeypatch.setenv("ASHARE_TELEGRAM_ENABLED", "true")
    monkeypatch.delenv("ASHARE_TELEGRAM_BOT_TOKEN", raising=False)
    monkeypatch.setenv("ASHARE_TELEGRAM_CHAT_ID", "123")

    with pytest.raises(SettingsError):
        TelegramSettings.from_env()


def test_enabled_requires_chat_id(monkeypatch):
    monkeypatch.setenv("ASHARE_TELEGRAM_ENABLED", "true")
    monkeypatch.setenv("ASHARE_TELEGRAM_BOT_TOKEN", "token")
    monkeypatch.delenv("ASHARE_TELEGRAM_CHAT_ID", raising=False)

    with pytest.raises(SettingsError):
        TelegramSettings.from_env()
