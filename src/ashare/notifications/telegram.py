from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from ashare.config.settings import TelegramSettings


class TelegramNotificationError(RuntimeError):
    """Raised when Telegram delivery fails."""


@dataclass(frozen=True)
class TelegramNotifier:
    settings: TelegramSettings
    api_base: str = "https://api.telegram.org"
    timeout_seconds: int = 10

    def build_url(self) -> str:
        self.settings.validate()
        return f"{self.api_base}/bot{self.settings.bot_token}/sendMessage"

    def build_payload(self, message: str) -> dict[str, str]:
        payload: dict[str, str] = {
            "chat_id": self.settings.chat_id,
            "text": message,
        }
        if self.settings.parse_mode:
            payload["parse_mode"] = self.settings.parse_mode
        return payload

    def send_text(self, message: str) -> None:
        if not self.settings.enabled:
            return

        payload = json.dumps(self.build_payload(message)).encode("utf-8")
        request = Request(
            self.build_url(),
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=self.timeout_seconds) as response:
                response.read()
        except (HTTPError, URLError) as exc:
            raise TelegramNotificationError(f"Telegram send failed: {exc}") from exc
