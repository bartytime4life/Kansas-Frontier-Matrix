#!/usr/bin/env bash
set -euo pipefail
git mv docs/domains/roads_rail_trade_routes/README.md docs/domains/roads-rail-trade-routes/README.md
git mv docs/domains/roads_rail_trade_routes/registers/api_surface.md docs/domains/roads-rail-trade-routes/registers/api_surface.md
git mv docs/domains/roads_rail_trade_routes/registers/architecture.md docs/domains/roads-rail-trade-routes/registers/architecture.md
git mv docs/domains/roads_rail_trade_routes/registers/catalog_and_proof_objects.md docs/domains/roads-rail-trade-routes/registers/catalog_and_proof_objects.md
git mv docs/domains/roads_rail_trade_routes/registers/change_log.md docs/domains/roads-rail-trade-routes/registers/change_log.md
git mv docs/domains/roads_rail_trade_routes/registers/ci_gate_matrix.md docs/domains/roads-rail-trade-routes/registers/ci_gate_matrix.md
git mv docs/domains/roads_rail_trade_routes/registers/data_model.md docs/domains/roads-rail-trade-routes/registers/data_model.md
git mv docs/domains/roads_rail_trade_routes/registers/evidence_drawer_payloads.md docs/domains/roads-rail-trade-routes/registers/evidence_drawer_payloads.md
git mv docs/domains/roads_rail_trade_routes/registers/extension_points.md docs/domains/roads-rail-trade-routes/registers/extension_points.md
git mv docs/domains/roads_rail_trade_routes/registers/file_inventory.md docs/domains/roads-rail-trade-routes/registers/file_inventory.md
git mv docs/domains/roads_rail_trade_routes/registers/fixture_inventory.md docs/domains/roads-rail-trade-routes/registers/fixture_inventory.md
git mv docs/domains/roads_rail_trade_routes/registers/focus_mode_behavior.md docs/domains/roads-rail-trade-routes/registers/focus_mode_behavior.md
git mv docs/domains/roads_rail_trade_routes/registers/lifecycle_and_promotion.md docs/domains/roads-rail-trade-routes/registers/lifecycle_and_promotion.md
git mv docs/domains/roads_rail_trade_routes/registers/pipeline_inventory.md docs/domains/roads-rail-trade-routes/registers/pipeline_inventory.md
git mv docs/domains/roads_rail_trade_routes/registers/rollback_and_corrections.md docs/domains/roads-rail-trade-routes/registers/rollback_and_corrections.md
git mv docs/domains/roads_rail_trade_routes/registers/schema_index.md docs/domains/roads-rail-trade-routes/registers/schema_index.md
git mv docs/domains/roads_rail_trade_routes/registers/source_registry.md docs/domains/roads-rail-trade-routes/registers/source_registry.md
git mv docs/domains/roads_rail_trade_routes/registers/test_matrix.md docs/domains/roads-rail-trade-routes/registers/test_matrix.md
git mv docs/domains/roads_rail_trade_routes/registers/ui_layer_inventory.md docs/domains/roads-rail-trade-routes/registers/ui_layer_inventory.md
git mv docs/domains/roads_rail_trade_routes/registers/verification_backlog.md docs/domains/roads-rail-trade-routes/registers/verification_backlog.md
git checkout -- docs/registers/reorg docs/registers/domain_doc_index.md docs/registers/domain_file_index.md docs/registers/README.md
