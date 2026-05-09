# KFM Makefile — greenfield scaffold.
# Commands should be repo-native; replace placeholders as packages land.

.PHONY: help validate test schemas policy fixtures release-dry-run             proof-slice catalog publish-check deny-test ui-build api-run governed-api-dev governed-api-smoke governed-api-verify

help:
	@echo "KFM make targets (greenfield):"
	@echo "  validate         Run all validators"
	@echo "  schemas          Validate fixtures against schemas"
	@echo "  policy           Run policy-as-code tests"
	@echo "  fixtures         Refresh deterministic fixtures"
	@echo "  test             Run full test suite"
	@echo "  proof-slice      Build the hydrology proof slice end-to-end"
	@echo "  release-dry-run  Assemble a candidate release manifest without publishing"
	@echo "  publish-check    Run promotion gates without side effects"
	@echo "  deny-test        Verify public boundary deny tests"
	@echo "  ui-build         Build apps/explorer-web"
	@echo "  api-run          Start apps/governed-api locally"

validate:
	@echo "TODO: invoke tools/validators/*"

schemas:
	@echo "TODO: jsonschema validate fixtures/ against schemas/"

policy:
	@echo "TODO: opa test policy/ -v"

fixtures:
	@echo "TODO: regenerate deterministic fixtures"

test:
	@echo "TODO: pytest tests/"

proof-slice:
	@echo "TODO: pipelines/hydrology proof slice"

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
