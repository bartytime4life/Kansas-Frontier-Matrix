# KFM Makefile — greenfield scaffold.
# Commands should be repo-native; replace placeholders as packages land.
#
# Status: repo-facing convenience surface. Targets with TODO output are
# intentionally non-authoritative placeholders until the corresponding
# package, validator, watcher, pipeline, test, release, or CI evidence is
# verified in the repository.

.DEFAULT_GOAL := help

.PHONY: help validate test schemas policy fixtures release-dry-run proof-slice catalog publish-check deny-test ui-build api-run governed-api-dev governed-api-smoke governed-api-verify boundary-guards boundary-guards-ci maplibre-perf maplibre-govern maplibre-proof maplibre-clean

help:
	@echo "KFM make targets (greenfield):"
	@echo "  validate              Run all validators"
	@echo "  schemas               Validate fixtures against schemas"
	@echo "  policy                Run policy-as-code tests"
	@echo "  fixtures              Refresh deterministic fixtures"
	@echo "  test                  Run full test suite"
	@echo "  proof-slice           Build the hydrology proof slice end-to-end"
	@echo "  catalog               Build catalog records from validated outputs"
	@echo "  release-dry-run       Assemble a candidate release manifest without publishing"
	@echo "  publish-check         Run promotion gates without side effects"
	@echo "  deny-test             Verify public boundary deny tests"
	@echo "  ui-build              Build apps/explorer-web"
	@echo "  api-run               Start apps/governed-api locally"
	@echo "  governed-api-dev      Start governed-api module directly"
	@echo "  governed-api-smoke    Run governed-api smoke tests"
	@echo "  governed-api-verify   Run governed-api tests and boundary grep"
	@echo "  boundary-guards       Run boundary policy + governed-api guard tests"
	@echo "  boundary-guards-ci    Run boundary suite with JUnit output"
	@echo "  maplibre-perf         Run MapLibre perf smoke + artifacts"
	@echo "  maplibre-govern       Validate MapLibre perf governance"
	@echo "  maplibre-proof        Build and validate MapLibre perf ProofPack"
	@echo "  maplibre-clean        Remove MapLibre perf artifacts"

validate:
	$(MAKE) schemas test

schemas:
	python tools/validators/_common/run_all.py

policy:
	@echo "TODO: opa test policy/ -v"

fixtures:
	@echo "TODO: regenerate deterministic fixtures"

test:
	python -m pytest tests/schemas tests/contracts -q

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

api-run:
	@echo "TODO: uvicorn apps.governed_api.main:app"

governed-api-dev:
	PYTHONPATH=apps/governed-api/src python -m governed_api.main

governed-api-smoke:
	python -m pytest apps/governed-api/tests -q

governed-api-verify:
	python -m pytest apps/governed-api/tests -q
	git grep -E "^(import|from) (maplibre|cesium|ollama)" apps/governed-api/ || true

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
	rm -rf artifacts/perf
