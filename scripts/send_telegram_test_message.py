from __future__ import annotations

import argparse

from ashare.config.settings import TelegramSettings
from ashare.notifications.telegram import TelegramNotifier


def main() -> None:
    parser = argparse.ArgumentParser(description="Send a Telegram test message")
    parser.add_argument("--message", default="Ashare Telegram test message")
    args = parser.parse_args()

    settings = TelegramSettings.from_env()
    notifier = TelegramNotifier(settings)
    notifier.send_text(args.message)
    print("Telegram message handled")


if __name__ == "__main__":
    main()
