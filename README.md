# CCE_PLUS — Conscious Context Engine Plus (Private Prototype)

This repository is the private, minimal, auditable scaffold for **CCE+** (Conscious Context Engine Plus).
It's intentionally small so you and I (your AI partner) can iterate privately.

## Goals
- Capture inputs as claims
- Build a reasoning graph with provenance
- Store and test user theories
- Run tiny simulations ("what-if" sandbox)
- Provide reflection/explanations for inferences
- Keep everything local & private

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate      # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python cli.py
```

## Structure
See folder `cce/` for modules.
