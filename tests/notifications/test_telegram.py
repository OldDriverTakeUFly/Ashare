from ashare.config.settings import TelegramSettings
from ashare.notifications.telegram import TelegramNotifier


def test_build_url_uses_token():
    notifier = TelegramNotifier(
        TelegramSettings(enabled=True, bot_token="abc123", chat_id="999")
    )

    assert notifier.build_url().endswith("/botabc123/sendMessage")


def test_build_payload_contains_required_fields():
    notifier = TelegramNotifier(
        TelegramSettings(enabled=True, bot_token="abc123", chat_id="999", parse_mode="Markdown")
    )

    payload = notifier.build_payload("Backtest done")

    assert payload == {
        "chat_id": "999",
        "text": "Backtest done",
        "parse_mode": "Markdown",
    }


def test_send_text_returns_early_when_disabled():
    notifier = TelegramNotifier(TelegramSettings(enabled=False, bot_token="", chat_id=""))

    notifier.send_text("ignored")
