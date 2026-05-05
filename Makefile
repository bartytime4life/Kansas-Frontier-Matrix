PYTHON ?= python3
ROOT ?= .

VALIDATOR := tools/validators/ecology/validate_run.py
SIGNER := tools/validators/ecology/sign_and_verify.sh

CONFIG ?= config/sources.example.json
DEMO_ROOT ?= .demo
RECEIPTS ?= receipts

# Governed run defaults.
MAX_CHANGES_PER_RUN ?= 10
BATCH_SIZE ?= 5
WORKER_CONCURRENCY ?= 4
SOURCE_RATE ?= 1/s
SOURCE_BURST ?= 5
RETRIES ?= 3
BACKOFF_BASE ?= 2s
BACKOFF_MAX ?= 60s

.PHONY: all install-dev test watch run run-signed \
	demo-unsigned demo-signed \
	validate validate-ecology validate-basic negative refresh fingerprint \
	sign verify-signatures promote-guard print-run-profile clean-dlq clean

all: validate-ecology negative fingerprint

install-dev:
	$(PYTHON) -m pip install -e '.[dev]'

test:
	$(PYTHON) -m pytest -q

watch:
	$(PYTHON) -m tools.ingest.watcher --config $(CONFIG)

run:
	$(PYTHON) -m tools.ingest.runner --config $(CONFIG) --no-sign

run-signed:
	$(PYTHON) -m tools.ingest.runner --config $(CONFIG) --sign

# Aggregate validation target.
validate: validate-ecology validate-basic

validate-ecology:
	$(PYTHON) $(VALIDATOR) validate --root $(ROOT) --allow-unsigned

validate-basic:
	$(PYTHON) -m tools.validators.basic $(RECEIPTS)

negative:
	$(PYTHON) $(VALIDATOR) negative --root $(ROOT)

refresh:
	$(PYTHON) $(VALIDATOR) refresh --root $(ROOT)

fingerprint:
	$(PYTHON) $(VALIDATOR) fingerprint --root $(ROOT)

sign:
	$(SIGNER) sign $(ROOT)

verify-signatures:
	$(SIGNER) verify $(ROOT)

# Local HTTP server demo with HUC12⇄COMID and one PMTiles delta fixture.
demo-unsigned:
	$(PYTHON) -m tools.ingest.demo_local --root $(DEMO_ROOT) --clean
	$(PYTHON) -m tools.validators.basic $(DEMO_ROOT)/receipts

# Requires cosign. In GitHub Actions, id-token: write is required for keyless signing.
demo-signed:
	$(PYTHON) -m tools.ingest.demo_local --root $(DEMO_ROOT) --clean --sign
	$(PYTHON) -m tools.validators.basic $(DEMO_ROOT)/receipts
	./scripts/verify_receipts.sh $(DEMO_ROOT)/receipts
	$(PYTHON) -m tools.ingest.promote_guard $(DEMO_ROOT)/receipts --require-signatures

promote-guard:
	$(PYTHON) -m tools.ingest.promote_guard $(RECEIPTS) --require-signatures

print-run-profile:
	@echo "max_changes_per_run=$(MAX_CHANGES_PER_RUN)"
	@echo "batch_size=$(BATCH_SIZE)"
	@echo "worker_concurrency=$(WORKER_CONCURRENCY)"
	@echo "per_source_token_bucket=$(SOURCE_RATE),burst=$(SOURCE_BURST)"
	@echo "retries=$(RETRIES),base=$(BACKOFF_BASE),max=$(BACKOFF_MAX)"

clean-dlq:
	rm -f data/dlq/dlq_report.json

clean: clean-dlq
	rm -rf WORK receipts .last_meta .queue .state .demo .pytest_cache
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
