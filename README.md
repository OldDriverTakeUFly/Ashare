# Ashare

A-share quantitative trading research and system-building workspace.

## Project goals
- Learn practical quantitative trading with an A-share focus
- Study existing strategy patterns and distill reusable design principles
- Build a personal research-to-backtest workflow
- Evolve toward a maintainable live-trading-ready system

## Development principles
- Project-local documentation under version control
- Requirements and architecture written before implementation
- Independent commits per completed requirement
- Milestone-based pushes to remote
- Prefer small, testable increments

## Repository layout
- `docs/requirements/` — product and scope definition
- `docs/architecture/` — system architecture and technical decisions
- `docs/research/` — learning notes, references, and strategy research
- `docs/plans/` — implementation plans
- `src/` — application and research code
- `tests/` — automated tests
- `scripts/` — utility and workflow scripts
- `data/` — local data directories (ignored except placeholders)

## Initial focus
1. Define the first MVP for offline research + backtesting
2. Choose a reliable A-share data acquisition path
3. Build a strategy interface and backtest engine wrapper
4. Add evaluation metrics and reporting
5. Validate one baseline strategy end-to-end

## Next milestone
Draft the MVP requirements, architecture, and first implementation plan before writing production code.
