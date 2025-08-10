# ERP/CRM Language Model Evaluation — Practical Demo

This repository is a small, self-contained evaluation of language-model style components for common ERP/CRM tasks.
It uses mock, anonymised data to avoid any operational dependencies.

## Use-cases
1. Contract clause extraction (payment terms, warranty, termination) to speed contract/quote checks.
2. Lead qualification triage from profile + notes for faster routing.
3. Summarising CRM notes to create action-oriented handovers.

## What’s included
- `data/` — small labelled datasets.
- `src/` — evaluation scripts and helpers.
- `notebooks/` — a short walkthrough to run locally.
- `docs/` — governance checklist and a report template.

## How to run (local)
```bash
pip install -r requirements.txt
python src/eval_contracts.py
python src/eval_leads.py
python src/eval_notes.py
# or open: notebooks/walkthrough.ipynb
```

## Evaluation approach
- Accuracy-style metrics (precision/recall/F1 for extraction; simple accuracy for triage).
- Utility signals (accept/override rate, cycle-time reduction) — captured during pilot.
- Cost/latency placeholders to estimate real-world feasibility.
