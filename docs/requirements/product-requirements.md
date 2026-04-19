# Ashare MVP Product Requirements

## 1. Objective
Build a first-stage A-share quantitative research system that supports:
- market data collection and local storage
- factor/indicator generation
- strategy signal generation
- historical backtesting
- performance analysis and comparison
- Telegram-based delivery of run status and selected reports

This MVP is for research and validation first, not live auto-trading.

## 2. Target user
Primary user: the repository owner, an individual trader/developer learning and building a personal quantitative system for A-shares.

## 3. Market scope
- Market: China A-shares
- Holding horizon: short-to-medium term
- Frequency: daily bar first, then optional intraday extension
- Stage 1 excludes options, futures, and high-frequency execution

## 4. MVP capabilities
### 4.1 Data layer
- ingest daily OHLCV data
- ingest basic fundamental or descriptive metadata when available
- normalize symbols, calendar, and adjustment mode
- persist data locally for repeatable backtests

### 4.2 Research layer
- compute common technical indicators
- support factor/feature engineering from price-volume data
- provide notebook/script friendly analysis workflow

### 4.3 Strategy layer
- define a standard strategy interface
- support at least one benchmark strategy and one candidate strategy
- output entry, exit, rebalance, and position-sizing instructions

### 4.4 Backtest layer
- portfolio-level backtesting
- configurable transaction cost, slippage, and stamp duty assumptions
- benchmark comparison
- support single-strategy parameter iteration

### 4.5 Evaluation layer
- annualized return
- max drawdown
- Sharpe ratio
- win rate
- turnover
- excess return vs benchmark

### 4.6 Notification layer
- support Telegram bot delivery for run lifecycle events
- support plain-text summary messages for research and backtest completion
- allow the notification channel to be enabled/disabled by configuration
- keep bot credentials outside version control

## 5. Non-goals for MVP
- broker integration
- automated live execution
- real-time streaming engine
- distributed compute
- multi-user service deployment
- interactive Telegram command bot for full strategy control

## 6. Success criteria
- one reproducible command or workflow runs a full backtest
- at least one documented baseline strategy is implemented
- metrics and plots are generated consistently
- code and docs are organized enough for iterative strategy research
- the system can send a Telegram message when a configured research or backtest job finishes

## 7. Open decisions
- data source priority: AkShare / Tushare / BaoStock / local vendor exports
- backtest framework choice: Backtrader vs vectorbt vs custom engine
- symbol universe definition: broad market, index constituents, or filtered universe
- Telegram integration scope: notification-only first, command interaction later
