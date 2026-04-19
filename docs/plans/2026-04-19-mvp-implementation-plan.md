# Ashare MVP Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build the first working research-to-backtest slice for A-share daily-bar strategies.

**Architecture:** Start with a lightweight Python package that separates data ingestion, normalized storage, strategy generation, and backtest evaluation. Prioritize offline reproducibility and simple interfaces before framework-heavy abstractions.

**Tech Stack:** Python 3.11+, pandas, numpy, pytest, local parquet/csv storage, optional Backtrader evaluation wrapper.

---

### Task 1: Create package skeleton
**Objective:** Establish the initial module boundaries for the MVP.

**Files:**
- Create: `src/ashare/config/__init__.py`
- Create: `src/ashare/data_sources/__init__.py`
- Create: `src/ashare/data_store/__init__.py`
- Create: `src/ashare/features/__init__.py`
- Create: `src/ashare/strategies/__init__.py`
- Create: `src/ashare/backtest/__init__.py`
- Create: `src/ashare/analytics/__init__.py`
- Create: `tests/test_package_layout.py`

**Verification:**
Run: `pytest -q`
Expected: package layout test passes.

### Task 2: Add market data model and loader contract
**Objective:** Define the normalized dataframe schema and source adapter interface.

**Files:**
- Create: `src/ashare/data_sources/base.py`
- Create: `src/ashare/data_store/schema.py`
- Create: `tests/data_sources/test_base_adapter.py`

**Verification:**
Run: `pytest tests/data_sources/test_base_adapter.py -q`
Expected: interface tests pass.

### Task 3: Implement first data adapter
**Objective:** Add one practical A-share daily-bar data adapter behind the base interface.

**Files:**
- Create: `src/ashare/data_sources/akshare_adapter.py`
- Create: `tests/data_sources/test_akshare_adapter.py`
- Modify: `pyproject.toml`

**Verification:**
Run: `pytest tests/data_sources/test_akshare_adapter.py -q`
Expected: adapter contract tests pass.

### Task 4: Add local storage workflow
**Objective:** Persist normalized daily-bar data for repeatable backtests.

**Files:**
- Create: `src/ashare/data_store/local_store.py`
- Create: `tests/data_store/test_local_store.py`

**Verification:**
Run: `pytest tests/data_store/test_local_store.py -q`
Expected: read/write tests pass.

### Task 5: Implement baseline strategy
**Objective:** Add one fully documented baseline timing or ranking strategy.

**Files:**
- Create: `src/ashare/strategies/base.py`
- Create: `src/ashare/strategies/moving_average.py`
- Create: `tests/strategies/test_moving_average.py`

**Verification:**
Run: `pytest tests/strategies/test_moving_average.py -q`
Expected: signal-generation tests pass.

### Task 6: Implement minimal backtest runner
**Objective:** Turn strategy signals into portfolio equity curves and metrics.

**Files:**
- Create: `src/ashare/backtest/runner.py`
- Create: `src/ashare/analytics/metrics.py`
- Create: `tests/backtest/test_runner.py`

**Verification:**
Run: `pytest tests/backtest/test_runner.py -q`
Expected: backtest and metric tests pass.

### Task 7: Add end-to-end example script
**Objective:** Provide a reproducible MVP workflow from local data to result output.

**Files:**
- Create: `scripts/run_baseline_backtest.py`
- Create: `tests/integration/test_baseline_workflow.py`
- Modify: `README.md`

**Verification:**
Run: `pytest tests/integration/test_baseline_workflow.py -q`
Expected: integration flow passes.

### Task 8: Add experiment documentation
**Objective:** Document how to run, compare, and record strategy experiments.

**Files:**
- Create: `docs/research/experiment-log-template.md`
- Modify: `docs/research/learning-roadmap.md`
- Modify: `README.md`

**Verification:**
Manual check: repository documents the research loop clearly.
