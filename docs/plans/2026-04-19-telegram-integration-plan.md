# Telegram Integration Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Prepare and implement a first Telegram notification path for the Ashare project without coupling it to the core research engine.

**Architecture:** Keep Telegram as an outbound adapter behind a notifier interface. Configuration lives in environment variables, message construction stays deterministic, and delivery failures remain isolated from the core workflow.

**Tech Stack:** Python 3.11+, stdlib `urllib`, pytest, environment-based config.

---

### Task 1: Add configuration loader
**Objective:** Define and validate Telegram-related environment settings.

**Files:**
- Create: `src/ashare/config/settings.py`
- Create: `tests/config/test_settings.py`

**Verification:**
Run: `pytest tests/config/test_settings.py -q`
Expected: settings tests pass.

### Task 2: Add notifier abstraction
**Objective:** Define a small contract for outbound notification transports.

**Files:**
- Create: `src/ashare/notifications/base.py`
- Modify: `src/ashare/notifications/__init__.py`
- Create: `tests/notifications/test_notifier_contract.py`

**Verification:**
Run: `pytest tests/notifications/test_notifier_contract.py -q`
Expected: contract tests pass.

### Task 3: Implement Telegram notifier
**Objective:** Build the first concrete notifier that can send text messages through the Telegram Bot API.

**Files:**
- Create: `src/ashare/notifications/telegram.py`
- Create: `tests/notifications/test_telegram.py`

**Verification:**
Run: `pytest tests/notifications/test_telegram.py -q`
Expected: payload and URL tests pass.

### Task 4: Add workflow helper script
**Objective:** Provide a small executable path to verify bot connectivity manually.

**Files:**
- Create: `scripts/send_telegram_test_message.py`
- Modify: `README.md`

**Verification:**
Run: `python scripts/send_telegram_test_message.py --message "hello"`
Expected: message is sent when environment is configured.

### Task 5: Wire Telegram into the first backtest/report workflow
**Objective:** Add a thin integration point for completion notifications.

**Files:**
- Modify: future backtest runner module
- Modify: future report workflow module
- Add tests for integration hook

**Verification:**
Run: relevant workflow tests
Expected: research workflow can emit a Telegram notification when enabled.
