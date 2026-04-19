# Telegram Bot Integration Requirements

## Goal
Add Telegram as the first external notification channel for the Ashare project.

## Why this matters
- Receive long-running task status without watching the terminal
- Deliver backtest completion summaries to mobile
- Build a future path toward lightweight remote control, while keeping the current stage simple

## Stage 1 scope
- Notification-only
- Single bot token
- Single chat target by default
- Plain-text messages first
- Configuration via environment variables

## Functional requirements
1. The system must support enabling or disabling Telegram delivery by configuration.
2. The system must read bot token and chat ID from environment variables.
3. The system must support sending text messages for:
   - task started
   - task succeeded
   - task failed
   - backtest summary ready
4. The notification layer must be optional; research and backtest code must still run if Telegram is disabled.
5. Network calls must be isolated so tests can validate payload generation without hitting Telegram.

## Non-functional requirements
- Secrets must not be committed to git.
- Failures in Telegram delivery must not crash the core research workflow by default.
- The integration should be simple enough to debug manually with curl or Python standard library requests.

## Future extensions
- markdown formatting
- image/file delivery
- multiple chats and routing rules
- inbound Telegram commands
- scheduled daily/weekly strategy reports
