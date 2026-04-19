from __future__ import annotations

from typing import Protocol


class Notifier(Protocol):
    def send_text(self, message: str) -> None:
        """Deliver a plain-text message to an external notification channel."""
