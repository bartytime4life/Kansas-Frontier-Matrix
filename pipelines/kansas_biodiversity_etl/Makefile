```makefile
SHELL := /bin/bash

# ----------------------------
# Paths
# ----------------------------

PIPELINE_ROOT := .
DATA_ROOT := ../../data

RAW_DIR := $(DATA_ROOT)/raw/kansas_biodiversity_etl/20260425
WORK_DIR := $(DATA_ROOT)/work/kansas_biodiversity_etl
PROCESSED_DIR := $(DATA_ROOT)/processed/kansas_occurrences
RECEIPTS_DIR := $(DATA_ROOT)/receipts/kansas_biodiversity_etl/20260425
PROOFS_DIR := $(DATA_ROOT)/proofs/kansas_biodiversity_etl/20260425

# ----------------------------
# Files
# ----------------------------

RAW_GBIF := $(RAW_DIR)/gbif_occurrences.jsonl
HARVEST_RECEIPT := $(RAW_DIR)/harvest_receipt.json

NORMALIZED := $(WORK_DIR)/normalized.jsonl
DEDUPED := $(WORK_DIR)/deduped.jsonl

DATASET_ROOT := $(PROCESSED_DIR)
METADATA := $(PROCESSED_DIR)/_dataset_metadata.json

EVIDENCE := $(PROOFS_DIR)/evidence_bundle.json
RECEIPT := $(RECEIPTS_DIR)/run_receipt.json

LICENSE_MAP := license/license_map.json
SENSITIVE_TAXA := sensitivity/sensitive_taxa_sample.txt

# ----------------------------
# Targets
# ----------------------------

.PHONY: all harvest normalize dedupe publish gate clean sample

# Full governed run
all: harvest normalize dedupe publish gate

# ----------------------------
# Harvest (GBIF)
# ----------------------------

harvest:
	@echo "=== Harvest: GBIF Kansas occurrences ==="
	python harvest/harvest_gbif.py \
		--state Kansas \
		--since 2026-04-01T00:00:00Z \
		--output $(RAW_GBIF) \
		--receipt-output $(HARVEST_RECEIPT) \
		--max-records 1000

# ----------------------------
# Normalize (DwC → canonical)
# ----------------------------

normalize:
	@echo "=== Normalize: DwC → canonical ==="
	python normalize/normalize_dwc.py \
		--input $(RAW_GBIF) \
		--output $(NORMALIZED)

# ----------------------------
# Dedupe + license + sensitivity
# ----------------------------

dedupe:
	@echo "=== Dedupe + License + Sensitivity ==="
	python dedupe/dedupe_occurrences.py \
		--input $(NORMALIZED) \
		--output $(DEDUPED) \
		--license-map $(LICENSE_MAP) \
		--sensitive-taxa $(SENSITIVE_TAXA)

# ----------------------------
# Publish (partitioned parquet)
# ----------------------------

publish:
	@echo "=== Publish: Partitioned Parquet + EvidenceBundle ==="
	python publish/publish.py \
		--input $(DEDUPED) \
		--dataset-root $(DATASET_ROOT) \
		--metadata-output $(METADATA) \
		--evidence-output $(EVIDENCE) \
		--receipt-output $(RECEIPT) \
		--source-uri "https://api.gbif.org/v1/occurrence/search?stateProvince=Kansas"

# ----------------------------
# Promotion Gate (A–G)
# ----------------------------

gate:
	@echo "=== Promotion Gate (fail-closed) ==="
	python validate/promotion_gate_full.py \
		--dataset $(DATASET_ROOT) \
		--metadata $(METADATA) \
		--evidence $(EVIDENCE)

# ----------------------------
# Sample mode (offline testing)
# ----------------------------

sample:
	@echo "=== Sample Mode (offline) ==="
	python normalize/normalize_dwc.py \
		--input samples/dwc_occurrences_sample.jsonl \
		--output $(NORMALIZED)
	$(MAKE) dedupe
	$(MAKE) publish
	$(MAKE) gate

# ----------------------------
# Clean
# ----------------------------

clean:
	@echo "=== Cleaning pipeline outputs ==="
	rm -rf $(WORK_DIR)
	rm -rf $(PROCESSED_DIR)
	rm -rf $(RECEIPTS_DIR)
	rm -rf $(PROOFS_DIR)
	rm -rf $(RAW_DIR)
```
