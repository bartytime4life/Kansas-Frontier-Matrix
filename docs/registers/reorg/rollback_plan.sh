#!/usr/bin/env bash
set -euo pipefail

# Rollback plan for 2026-05-03 reorg sprint subset.
# This run only edited manifest/register artifacts and regenerated inventory.

git checkout -- \
  docs/registers/reorg/REORG_SPRINT_MANIFEST.md \
  docs/registers/reorg/path_inventory.tsv \
  docs/registers/reorg/authority_conflicts.md \
  docs/registers/reorg/validation_report.md \
  docs/registers/reorg/rollback_plan.sh

echo "Rollback complete for reorg manifest subset."
