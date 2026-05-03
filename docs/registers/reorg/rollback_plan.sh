#!/usr/bin/env bash
set -euo pipefail
# Whole-run rollback
# git reset --hard HEAD~1
# Targeted rollback for moves:
while IFS=$'\t' read -r old new reason; do
  [[ "$old" == "old_path" ]] && continue
  git mv "$new" "$old"
done < docs/registers/reorg/move_plan.tsv
# Remove new files
git rm -f docs/registers/reorg/REORG_SPRINT_MANIFEST.md docs/registers/reorg/path_inventory.tsv docs/registers/reorg/move_plan.tsv docs/registers/reorg/reference_update_plan.tsv docs/registers/reorg/authority_conflicts.md docs/registers/reorg/validation_report.md docs/registers/reorg/rollback_plan.sh docs/registers/domain_doc_index.md docs/registers/domain_file_index.md docs/registers/schema_authority_map.md docs/registers/policy_authority_map.md tools/repo_inventory/classify_paths.py tools/repo_inventory/check_reorg_manifest.py tools/repo_inventory/check_doc_orphans.py tools/repo_inventory/check_public_path_boundaries.py tests/repo_inventory/test_classify_paths.py tests/repo_inventory/test_check_reorg_manifest.py tests/repo_inventory/test_check_doc_orphans.py tests/repo_inventory/test_check_public_path_boundaries.py || true
