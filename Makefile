.PHONY: test watch run demo-unsigned demo-signed validate promote-guard clean

CONFIG ?= config/sources.example.json
DEMO_ROOT ?= .demo

install-dev:
	python -m pip install -e '.[dev]'

test:
	python -m pytest -q

watch:
	python -m tools.ingest.watcher --config $(CONFIG)

run:
	python -m tools.ingest.runner --config $(CONFIG) --no-sign

run-signed:
	python -m tools.ingest.runner --config $(CONFIG) --sign

# Local HTTP server demo with HUC12⇄COMID and one PMTiles delta fixture.
demo-unsigned:
	python -m tools.ingest.demo_local --root $(DEMO_ROOT) --clean
	python -m tools.validators.basic $(DEMO_ROOT)/receipts

# Requires cosign. In GitHub Actions, id-token: write is required for keyless signing.
demo-signed:
	python -m tools.ingest.demo_local --root $(DEMO_ROOT) --clean --sign
	python -m tools.validators.basic $(DEMO_ROOT)/receipts
	./scripts/verify_receipts.sh $(DEMO_ROOT)/receipts
	python -m tools.ingest.promote_guard $(DEMO_ROOT)/receipts --require-signatures

validate:
	python -m tools.validators.basic receipts

promote-guard:
	python -m tools.ingest.promote_guard receipts --require-signatures

clean:
	rm -rf WORK receipts .last_meta .queue .state .demo .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
