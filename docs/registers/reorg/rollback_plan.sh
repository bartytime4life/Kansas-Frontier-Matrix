#!/usr/bin/env bash
set -euo pipefail

# Whole-run rollback (preferred)
# git reset --hard HEAD~1

# Targeted rollback for this sprint
# 1) Revert explicit ignore hygiene
# git checkout -- .gitignore

# 2) Revert validator/test hardening
# git checkout -- tools/repo_inventory/check_public_path_boundaries.py
# git checkout -- tests/repo_inventory/test_check_public_path_boundaries.py

# 3) Revert reorg control docs
# git checkout -- docs/registers/reorg/REORG_SPRINT_MANIFEST.md
# git checkout -- docs/registers/reorg/validation_report.md
# git checkout -- docs/registers/reorg/path_inventory.tsv
# git checkout -- docs/registers/reorg/rollback_plan.sh
