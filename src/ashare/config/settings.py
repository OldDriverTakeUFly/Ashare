from __future__ import annotations

from dataclasses import dataclass
from os import getenv


class SettingsError(ValueError):
    """Raised when required application settings are invalid."""


@dataclass(frozen=True)
class TelegramSettings:
    enabled: bool = False
    bot_token: str = ""
    chat_id: str = ""
    parse_mode: str | None = None

    @classmethod
    def from_env(cls) -> "TelegramSettings":
        enabled = getenv("ASHARE_TELEGRAM_ENABLED", "false").strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }
        bot_token = getenv("ASHARE_TELEGRAM_BOT_TOKEN", "").strip()
        chat_id = getenv("ASHARE_TELEGRAM_CHAT_ID", "").strip()
        parse_mode = getenv("ASHARE_TELEGRAM_PARSE_MODE", "").strip() or None

        settings = cls(
            enabled=enabled,
            bot_token=bot_token,
            chat_id=chat_id,
            parse_mode=parse_mode,
        )
        settings.validate()
        return settings

    def validate(self) -> None:
        if not self.enabled:
            return
        if not self.bot_token:
            raise SettingsError("ASHARE_TELEGRAM_BOT_TOKEN is required when Telegram is enabled")
        if not self.chat_id:
            raise SettingsError("ASHARE_TELEGRAM_CHAT_ID is required when Telegram is enabled")


@dataclass(frozen=True)
class AppSettings:
    telegram: TelegramSettings

    @classmethod
    def from_env(cls) -> "AppSettings":
        return cls(telegram=TelegramSettings.from_env())
