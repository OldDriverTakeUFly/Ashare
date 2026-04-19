# Ashare System Architecture (Stage 1)

## 1. Design goals
- start simple, but keep module boundaries clean
- optimize for research reproducibility over premature complexity
- keep data, strategy logic, evaluation, and notification delivery separable
- make future live-trading extension possible without rewriting the research core

## 2. Proposed layers

### 2.1 Data source adapters
Responsibility:
- pull data from upstream providers
- translate raw provider schemas into internal models

Examples:
- `src/ashare/data_sources/akshare_adapter.py`
- `src/ashare/data_sources/tushare_adapter.py`

### 2.2 Data storage and catalog
Responsibility:
- store normalized market data locally
- manage symbol metadata, trading calendar, and cached datasets

Possible storage path:
- parquet/csv for early stage simplicity
- sqlite/duckdb metadata if needed later

### 2.3 Feature and factor pipeline
Responsibility:
- compute indicators and engineered features
- produce analysis-ready tables indexed by date and symbol

### 2.4 Strategy interface
Responsibility:
- standardize how strategies consume data and emit signals

Suggested contract:
- input: normalized feature dataframe(s) + config
- output: target positions or order signals by date

### 2.5 Portfolio and backtest engine
Responsibility:
- apply position-sizing rules
- simulate trades and cash changes
- include transaction costs and benchmark comparison

### 2.6 Analytics and reporting
Responsibility:
- compute metrics
- render tables and charts
- save reports for comparison between runs

### 2.7 Notification adapters
Responsibility:
- deliver run status, summaries, and alerts to external channels
- keep transport-specific concerns separate from research and backtest logic
- start with Telegram, leave room for email/Feishu/Discord later

## 3. Suggested package layout
- `src/ashare/config/`
- `src/ashare/data_sources/`
- `src/ashare/data_store/`
- `src/ashare/features/`
- `src/ashare/strategies/`
- `src/ashare/backtest/`
- `src/ashare/analytics/`
- `src/ashare/notifications/`
- `src/ashare/reports/`

## 4. First technical choices
Recommended default path for MVP:
- language: Python
- analysis stack: pandas + numpy
- storage: local parquet/csv
- initial backtesting path: Backtrader or a thin custom daily-bar engine
- visualization: matplotlib / plotly
- test framework: pytest
- notification transport: Telegram Bot API over HTTPS

## 5. Decision rule for framework selection
Choose the simplest tool that can:
- model A-share daily-bar backtests correctly
- support transaction costs and benchmark comparison
- remain debuggable by a solo developer

For Telegram integration, choose the simplest path that can:
- send deterministic text messages
- keep credentials out of git
- be tested without real network calls

## 6. Telegram integration design
### 6.1 Scope in the first cut
- outgoing notifications only
- no interactive command handling yet
- no dependence on Telegram as a core runtime control plane

### 6.2 Integration points
- backtest completion events
- data refresh completion/failure events
- milestone alerts for long-running jobs

### 6.3 Components
- `config.settings` for environment-based configuration
- `notifications.base` for transport abstraction
- `notifications.telegram` for Telegram-specific implementation
- future report generator can pass text summaries or file references

## 7. Evolution path
Stage 1: offline research + daily-bar backtest + notification hooks
Stage 2: richer universe selection + factor library + walk-forward validation
Stage 3: paper-trading/live-trading gateway abstraction + richer bot workflows
