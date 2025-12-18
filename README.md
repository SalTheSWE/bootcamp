# CSV Pro

Generate a profiling report for a CSV file.

## Features
- CLI: JSON + Markdown report
- Streamlit GUI: upload CSV + export reports

## Setup
    uv venv -p 3.11
    uv pip install -r requirements.txt

## Run CLI
    # If you have a src/ folder:
    #   Mac/Linux: export PYTHONPATH=src
    #   Windows:   $env:PYTHONPATH="src"
    uv run python -m csv_profiler.cli .\data\sample.csv

## Run GUI
    # If you have a src/ folder:
    #   Mac/Linux: export PYTHONPATH=src
    #   Windows:   $env:PYTHONPATH="src"
    uv run streamlit run app.py

## Output Files

The CLI writes:
- `outputs/report.json`
- `outputs/report.md`

The Streamlit app can:
- preview the report
- download JSON + Markdown

## Manual Test Plan

1. Setup:
   - `uv venv -p 3.11`
   - `uv pip install -r requirements.txt`

2. CLI:
   - (If you have a `src/` folder: set `PYTHONPATH=src` first)
   - `uv run python -m csv_profiler.cli profile data/sample.csv --out-dir outputs`

3. Verify:
   - `outputs/report.json` and `outputs/report.md` exist

4. GUI:
   - (If you have a `src/` folder: set `PYTHONPATH=src` first)
   - `uv run streamlit run app.py`

5. Export:
   - download JSON + Markdown from the UI
