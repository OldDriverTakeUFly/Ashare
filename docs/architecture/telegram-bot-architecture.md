# Telegram Bot Integration Architecture

## Overview
Telegram is introduced as an outbound adapter, not as the center of the application. Core trading research logic should publish events or summaries, and a notifier should decide whether and how to deliver them.

## Data flow
```text
Research/Backtest Job
  -> Summary/Event Payload
  -> Notification Interface
  -> Telegram Notifier
  -> Telegram Bot API
  -> Telegram Chat
```

## Configuration model
Environment variables:
- `ASHARE_TELEGRAM_ENABLED`
- `ASHARE_TELEGRAM_BOT_TOKEN`
- `ASHARE_TELEGRAM_CHAT_ID`
- `ASHARE_TELEGRAM_PARSE_MODE` (optional)

## Module boundaries
- `src/ashare/config/settings.py`
  - reads and validates environment variables
- `src/ashare/notifications/base.py`
  - defines the notifier contract
- `src/ashare/notifications/telegram.py`
  - implements payload construction and HTTP delivery

## Error handling policy
- If Telegram is disabled: no-op
- If Telegram is enabled but misconfigured: fail fast at configuration validation
- If Telegram delivery fails during a workflow: raise a transport-specific error that the caller can catch and log without aborting the whole research process

## Testing strategy
- unit test environment parsing
- unit test message payload generation
- unit test send path with HTTP mocking/stubbing in later stages

## First implementation checkpoint
- configuration loader exists
- notifier interface exists
- Telegram notifier can build a valid request and send plain text
- tests cover config and payload generation
