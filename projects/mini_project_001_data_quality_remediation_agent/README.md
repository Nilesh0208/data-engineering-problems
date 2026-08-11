# Mini Project 001: Data Quality Remediation Agent

## Project Objective

Build a small data engineering agent that reads raw customer order data, applies data quality checks, performs safe remediation, quarantines invalid records, and writes audit and summary outputs.

## Architecture

- `src/config.py`: configuration constants and file locations.
- `src/data_loader.py`: loads raw CSV input from `data/input/`.
- `src/quality_rules.py`: defines data quality checks for order data.
- `src/audit_logger.py`: logs remediation actions and rule violations.
- `src/remediation_agent.py`: applies remediation logic, deduplication, quarantine, and writes final outputs.
- `src/main.py`: orchestrates the pipeline.

## Folder Structure

- `data/input/`: sample raw CSV input with valid and invalid records.
- `data/output/`: cleaned order output.
- `data/quarantine/`: rejected records.
- `src/`: project code modules.
- `sql/`: SQL report templates.
- `tests/`: pytest tests for rules and remediation.

## How to Run

1. Install dependencies:

   ```powershell
   python -m pip install -r projects/mini_project_001_data_quality_remediation_agent/requirements.txt
   ```

2. Run the project:

   ```powershell
   python projects/mini_project_001_data_quality_remediation_agent/src/main.py
   ```

3. Run tests:

   ```powershell
   python -m pytest projects/mini_project_001_data_quality_remediation_agent/tests
   ```

## Expected Outputs

- `data/output/clean_orders.csv`: cleaned, deduplicated records.
- `data/quarantine/quarantined_orders.csv`: records rejected for critical data quality issues.
- `data/output/audit_log.csv`: remediation actions, rule names, reasons, and timestamps.

## Explanation

This mini project demonstrates a data engineering pipeline with validation, remediation, quarantine, and audit reporting. It shows an ability to define business rules, build safe remediation logic, and preserve traceability for bad data while producing a clean output dataset.
