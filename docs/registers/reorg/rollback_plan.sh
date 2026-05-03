#!/usr/bin/env bash
set -euo pipefail
# Whole-run rollback:
git reset --hard HEAD~1

# Targeted rollback (pre-commit):
# git checkout -- docs/registers/reorg docs/registers/schema_authority_map.md docs/registers/policy_authority_map.md tools/repo_inventory tests/repo_inventory
