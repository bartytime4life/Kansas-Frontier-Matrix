#!/usr/bin/env bash
set -euo pipefail
python tools/validate_repo.py
python tools/validate_fixtures.py
python tools/validate_schema_conformance.py
python tools/validate_fixture_schema_mapping.py
python tools/check_directory_rules.py
python tools/check_no_public_internal_paths.py
python tools/validate_api_contracts.py
python tools/check_source_ledger.py
python tools/promotion_dry_run.py
python tools/check_promotion_receipt_determinism.py
python -m unittest discover -s tests
