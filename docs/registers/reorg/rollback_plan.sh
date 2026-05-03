#!/usr/bin/env bash
set -euo pipefail

# Whole-run rollback
git reset --hard HEAD~1

# Targeted rollback for moved hydrology docs
git mv docs/domains/hydrology/architecture/API_CONTRACTS.md docs/domains/hydrology/API_CONTRACTS.md
git mv docs/domains/hydrology/architecture/ARCHITECTURE.md docs/domains/hydrology/ARCHITECTURE.md
git mv docs/domains/hydrology/architecture/IDENTITY_MODEL.md docs/domains/hydrology/IDENTITY_MODEL.md
git mv docs/domains/hydrology/architecture/MAP_UI_CONTRACTS.md docs/domains/hydrology/MAP_UI_CONTRACTS.md
git mv docs/domains/hydrology/registers/DATA_LIFECYCLE.md docs/domains/hydrology/DATA_LIFECYCLE.md
git mv docs/domains/hydrology/registers/HUC12_COMID_CROSSWALK_MANIFEST.md docs/domains/hydrology/HUC12_COMID_CROSSWALK_MANIFEST.md
git mv docs/domains/hydrology/registers/HUC12_COMID_RELEASE_CATALOG_AND_RESOLUTION.md docs/domains/hydrology/HUC12_COMID_RELEASE_CATALOG_AND_RESOLUTION.md
git mv docs/domains/hydrology/registers/RELEASE_INDEX.md docs/domains/hydrology/RELEASE_INDEX.md
git mv docs/domains/hydrology/registers/SOURCE_REGISTRY.md docs/domains/hydrology/SOURCE_REGISTRY.md
git mv docs/domains/hydrology/tracking/EXPANSION_BACKLOG.md docs/domains/hydrology/EXPANSION_BACKLOG.md
git mv docs/domains/hydrology/tracking/HYDROLOGY_CHANGELOG.md docs/domains/hydrology/HYDROLOGY_CHANGELOG.md
git mv docs/domains/hydrology/tracking/VERIFICATION_BACKLOG.md docs/domains/hydrology/VERIFICATION_BACKLOG.md

# Remove generated reorg artifacts
rm -f docs/registers/reorg/REORG_SPRINT_MANIFEST.md docs/registers/reorg/path_inventory.tsv docs/registers/reorg/move_plan.tsv docs/registers/reorg/reference_update_plan.tsv docs/registers/reorg/authority_conflicts.md docs/registers/reorg/validation_report.md
