#!/usr/bin/env bash
set -euo pipefail
# reverse moves
git mv docs/sources/catalog_profiles/KFM_DCAT_EXPORT_PROFILE.md docs/catalog/dcat/KFM_DCAT_EXPORT_PROFILE.md
git mv docs/sources/catalog_profiles/KFM_STAC_EXTENSION_PROFILE.md docs/catalog/stac/KFM_STAC_EXTENSION_PROFILE.md
git mv docs/tracking/governance/correction-withdrawal-rollback.md docs/governance/correction-withdrawal-rollback.md
git mv docs/tracking/governance/decision-log.md docs/governance/decision-log.md
git mv docs/control-plane/obligation-execution.md docs/governance/obligation-execution.md
git mv docs/registers/promotion-evidence-registry.md docs/governance/promotion-evidence-registry.md
git mv docs/architecture/tiles/tile-runtime-performance.md docs/runtime/tile-runtime-performance.md
# remove new reorg tooling/files
git rm -f tools/repo_inventory/classify_paths.py tools/repo_inventory/check_reorg_manifest.py tools/repo_inventory/check_doc_orphans.py tools/repo_inventory/check_public_path_boundaries.py
git rm -f tests/repo_inventory/test_classify_paths.py tests/repo_inventory/test_check_reorg_manifest.py
git rm -f docs/registers/reorg/REORG_SPRINT_MANIFEST.md docs/registers/reorg/path_inventory.tsv docs/registers/reorg/move_plan.tsv docs/registers/reorg/reference_update_plan.tsv docs/registers/reorg/authority_conflicts.md docs/registers/reorg/validation_report.md docs/registers/reorg/rollback_plan.sh
