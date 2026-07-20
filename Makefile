# KFM repository orchestration surface.
#
# Implemented targets below invoke repository-owned commands. Readiness-marker
# targets print TODO output and are intentionally non-enforcing; their zero exit
# status is not validation evidence. Several CI workflows inspect those marker
# bodies to detect when an implementation has landed and must be wired through
# a separately reviewed change.

.DEFAULT_GOAL := help

.PHONY: help validate test schemas policy fixtures release-dry-run proof-slice catalog publish-check deny-test ui-build api-run governed-api-dev governed-api-smoke governed-api-verify boundary-guards boundary-guards-ci maplibre-perf maplibre-govern maplibre-proof maplibre-clean

help:
	@echo "KFM repository targets"
	@echo
	@echo "Implemented validation and test targets:"
	@echo "  validate              Run aggregate schema validators and schema/contract tests"
	@echo "  schemas               Run configured aggregate validators against fixtures"
	@echo "  test                  Run repository schema and contract tests"
	@echo "  governed-api-smoke    Run governed API tests"
	@echo "  governed-api-verify   Run governed API tests and enforce its import boundary"
	@echo "  boundary-guards       Run policy/API boundary tests"
	@echo "  boundary-guards-ci    Run boundary tests with JUnit output"
	@echo "  maplibre-perf         Run MapLibre performance smoke and build artifacts"
	@echo "  maplibre-govern       Validate MapLibre performance governance"
	@echo "  maplibre-proof        Build and validate the MapLibre performance ProofPack"
	@echo
	@echo "Implemented local runtime targets:"
	@echo "  api-run               Start the governed API locally (alias of governed-api-dev)"
	@echo "  governed-api-dev      Start the governed API module directly"
	@echo
	@echo "Readiness markers (print TODO; do not enforce readiness):"
	@echo "  policy                Policy-engine test lane"
	@echo "  fixtures              Deterministic fixture regeneration"
	@echo "  proof-slice           Hydrology proof-slice pipeline"
	@echo "  catalog               Catalog record builder"
	@echo "  release-dry-run       Candidate release assembly"
	@echo "  publish-check         Promotion gate"
	@echo "  deny-test             Public-boundary deny suite"
	@echo "  ui-build              Explorer Web build"
	@echo
	@echo "Cleanup targets:"
	@echo "  maplibre-clean        Remove artifacts/perf"

validate:
	$(MAKE) schemas test

schemas:
	python tools/validators/_common/run_all.py

test:
	python -m pytest tests/schemas tests/contracts -q

# Readiness markers preserve exact TODO bodies consumed by repository workflows.
# They are discovery surfaces only and must not be cited as executable proof.
policy:
	@echo "TODO: opa test policy/ -v"

fixtures:
	@echo "TODO: regenerate deterministic fixtures"

proof-slice:
	@echo "TODO: pipelines/hydrology proof slice"

catalog:
	@echo "TODO: tools/catalog_builders build catalog records from validated processed outputs"

release-dry-run:
	@echo "TODO: tools/release dry-run"

publish-check:
	@echo "TODO: tools/validators/promotion_gate"

deny-test:
	@echo "TODO: tests/api deny suite"

ui-build:
	@echo "TODO: pnpm --filter explorer-web build"

api-run: governed-api-dev

governed-api-dev:
	PYTHONPATH=apps/governed-api/src python -m governed_api.main

governed-api-smoke:
	python -m pytest apps/governed-api/tests -q

governed-api-verify:
	python -m pytest apps/governed-api/tests -q
	@if git grep -nE "^(import|from) (maplibre|cesium|ollama)" apps/governed-api/; then \
		echo "DENY: governed API imports a forbidden renderer or model client" >&2; \
		exit 1; \
	else \
		status=$$?; \
		if [ "$$status" -ne 1 ]; then exit "$$status"; fi; \
		echo "PASS: governed API import boundary is intact"; \
	fi

boundary-guards:
	python -m pytest -q tests/policy/test_control_plane_register_meta_contract.py tests/policy/test_explorer_web_adapter_boundary.py tests/policy/test_pipeline_connector_non_publisher.py apps/governed-api/tests/test_boundary_guards.py

boundary-guards-ci:
	mkdir -p artifacts/qa
	python -m pytest -q --junitxml=artifacts/qa/policy-boundary-guards.xml tests/policy/test_control_plane_register_meta_contract.py tests/policy/test_explorer_web_adapter_boundary.py tests/policy/test_pipeline_connector_non_publisher.py apps/governed-api/tests/test_boundary_guards.py

maplibre-perf:
	node scripts/maplibre-smoke-perf.mjs
	node scripts/build-maplibre-render-diff.mjs
	node scripts/attest-maplibre-perf.mjs
	node scripts/build-maplibre-perf-release-manifest.mjs

maplibre-govern:
	python3 tools/validators/maplibre/validate_perf_governance.py

maplibre-proof:
	node scripts/build-maplibre-perf-proof-pack.mjs
	python3 tools/validators/maplibre/validate_perf_proof_pack.py \
		artifacts/perf/proof-pack.maplibre-perf.json
	node scripts/build-maplibre-perf-release-manifest.mjs
	python3 tools/validators/maplibre/validate_perf_governance.py

maplibre-clean:
	rm -rf -- artifacts/perf
