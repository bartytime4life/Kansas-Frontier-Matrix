#!/usr/bin/env bash
set -euo pipefail

python tools/validate_fixtures.py
python tools/validators/validate_source_terms.py
python tools/validators/validate_activation_decisions.py
python tools/validators/validate_evidence_closure.py
python tools/validators/validate_public_path_guards.py
python tools/synthetic_release_dry_run.py

echo "PASS local synthetic release checks completed (publish remains refused by dry-run policy)"
