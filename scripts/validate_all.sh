#!/usr/bin/env bash
set -euo pipefail
python tools/validate_repo.py
python tools/validate_fixtures.py
python tools/check_directory_rules.py
python tools/check_no_public_internal_paths.py
python -m unittest discover -s tests
