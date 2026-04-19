# A-share Quant Learning Roadmap

## Phase 1: Core foundations (1-2 weeks)
Goal: understand the minimum viable knowledge needed to build and evaluate simple strategies.

Study topics:
- market microstructure of A-shares
- OHLCV data, ex-rights/ex-dividend adjustments, suspension handling
- basic statistics for trading: returns, volatility, drawdown, correlation
- backtest pitfalls: look-ahead bias, survivorship bias, overfitting

Recommended references:
- Ernest Chan - Quantitative Trading
- Ernest Chan - Algorithmic Trading
- Tucker Balch style backtesting lectures / blog resources
- official docs of pandas, numpy, matplotlib

## Phase 2: Research workflow (1-2 weeks)
Goal: learn how to go from idea to data to result.

Study topics:
- factor and indicator construction
- benchmark and universe definition
- train/validation/test split for time series
- parameter sensitivity and robustness checks

Recommended resources:
- Backtrader documentation
- vectorbt documentation
- AkShare documentation
- Tushare documentation

## Phase 3: Strategy patterns for A-shares (2-4 weeks)
Goal: learn from common existing quantitative modes and extract reusable templates.

Suggested strategy families to study:
- trend following / moving average crossover
- momentum ranking
- mean reversion
- breakout strategies
- multi-factor stock selection
- regime filter + timing overlay

## Phase 4: System building (2-4 weeks)
Goal: build your own repeatable research system.

Deliverables:
- data ingestion scripts
- feature pipeline
- standard strategy interface
- backtest runner
- metrics report
- experiment log template

## Phase 5: Robustness and deployment preparation
Goal: move from toy backtest to decision-grade research process.

Study topics:
- walk-forward testing
- rolling re-optimization
- transaction cost modeling
- portfolio constraints
- paper trading architecture

## Open-source references to inspect
- Backtrader
- vectorbt
- Zipline / Zipline Reloaded
- Qlib (for ideas, not necessarily as first framework)
- AkShare example projects

## Practical advice
- start with one simple strategy and make the pipeline reproducible
- do not start with machine learning first
- treat every good backtest result as suspicious until biases are checked
- keep a research log for every experiment
