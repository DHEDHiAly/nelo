# Developer Setup

## Prerequisites
- Python 3.11+
- `pip`

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]
```

## Validation commands
```bash
ruff check .
pytest -q
```

## Repository map
- Source code: `src/nelo/`
- Tests: `tests/`
- Docs: `docs/`
- CI: `.github/workflows/`
