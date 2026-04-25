SHELL := /bin/bash

# ----------------------------
# Paths
# ----------------------------

PIPELINE_ROOT := .
DATA_ROOT := ../../data

RUN_DATE := 20260425
SINCE := 2026-04-01T00:00:00Z
STATE := Kansas
MAX_RECORDS := 1000

RAW_DIR := $(DATA_ROOT)/raw/kansas_biodiversity_etl/$(RUN_DATE)
WORK_DIR := $(DATA_ROOT)/work/kansas_biodiversity_etl
PROCESSED_DIR := $(DATA_ROOT)/processed/kansas_occurrences
RECEIPTS_DIR := $(DATA_ROOT)/receipts/kansas_biodiversity_etl/$(RUN_DATE)
PROOFS_DIR := $(DATA_ROOT)/proofs/kansas_biodiversity_etl/$(RUN_DATE)

CATALOG_STAC_DIR := $(DATA_ROOT)/catalog/stac
CATALOG_DCAT_DIR := $(DATA_ROOT)/catalog/dcat
CATALOG_PROV_DIR := $(DATA_ROOT)/catalog/prov

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
PROOF := $(PROOFS_DIR)/receipt_proof.json

CATALOG_STAC_ROOT := $(CATALOG_STAC_DIR)/kansas_biodiversity_occurrences
CATALOG_STAC_COLLECTION := $(CATALOG_STAC_ROOT)/collection.json
CATALOG_DCAT := $(CATALOG_DCAT_DIR)/kansas_biodiversity_occurrences.dataset.json
CATALOG_PROV := $(CATALOG_PROV_DIR)/kansas_biodiversity_occurrences.prov.json

LICENSE_MAP := license/license_map.json
SENSITIVE_TAXA := sensitivity/sensitive_taxa_sample.txt

# ----------------------------
# Targets
# ----------------------------

.PHONY: all harvest normalize dedupe publish sign verify-proof gate catalog validate-catalog clean sample check-inputs check-catalog

# Full governed run
all: harvest normalize dedupe publish sign gate catalog validate-catalog

# ----------------------------
# Preflight
# ----------------------------

check-inputs:
	@echo "=== Preflight: required local files ==="
	@test -f $(LICENSE_MAP) || (echo "Missing $(LICENSE_MAP)" && exit 1)
	@test -f $(SENSITIVE_TAXA) || (echo "Missing $(SENSITIVE_TAXA)" && exit 1)

check-catalog:
	@echo "=== Catalog Smoke Check ==="
	@test -f $(CATALOG_STAC_COLLECTION) || (echo "Missing $(CATALOG_STAC_COLLECTION)" && exit 1)
	@test -f $(CATALOG_DCAT) || (echo "Missing $(CATALOG_DCAT)" && exit 1)
	@test -f $(CATALOG_PROV) || (echo "Missing $(CATALOG_PROV)" && exit 1)
	python -m json.tool $(CATALOG_STAC_COLLECTION) >/dev/null
	python -m json.tool $(CATALOG_DCAT) >/dev/null
	python -m json.tool $(CATALOG_PROV) >/dev/null

# ----------------------------
# Harvest (GBIF)
# ----------------------------

harvest:
	@echo "=== Harvest: GBIF $(STATE) occurrences ==="
	python harvest/harvest_gbif.py \
		--state $(STATE) \
		--since $(SINCE) \
		--output $(RAW_GBIF) \
		--receipt-output $(HARVEST_RECEIPT) \
		--max-records $(MAX_RECORDS)

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

dedupe: check-inputs
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
		--source-uri "https://api.gbif.org/v1/occurrence/search?stateProvince=$(STATE)"

# ----------------------------
# Sign receipt (local proof shim)
# ----------------------------

sign:
	@echo "=== Sign Receipt: Local Proof Shim ==="
	python attest/sign_receipt.py \
		--receipt $(RECEIPT) \
		--proof-output $(PROOF) \
		--signer "@bartytime4life"

verify-proof:
	@echo "=== Verify Receipt Proof ==="
	python attest/verify_receipt_proof.py \
		--receipt $(RECEIPT) \
		--proof $(PROOF)

# ----------------------------
# Promotion Gate (A–H)
# ----------------------------

gate:
	@echo "=== Promotion Gate (fail-closed) ==="
	python validate/promotion_gate_full.py \
		--dataset $(DATASET_ROOT) \
		--metadata $(METADATA) \
		--evidence $(EVIDENCE) \
		--receipt $(RECEIPT) \
		--proof $(PROOF)

# ----------------------------
# Catalog closure (STAC Collection + Items, DCAT, PROV)
# ----------------------------

catalog:
	@echo "=== Catalog Closure: STAC Collection + Items, DCAT + PROV ==="
	python catalog/emit_catalog.py \
		--dataset-root $(DATASET_ROOT) \
		--metadata $(METADATA) \
		--evidence $(EVIDENCE) \
		--receipt $(RECEIPT) \
		--stac-output-root $(CATALOG_STAC_ROOT) \
		--dcat-output $(CATALOG_DCAT) \
		--prov-output $(CATALOG_PROV)
	$(MAKE) check-catalog

# ----------------------------
# Catalog validation
# ----------------------------

validate-catalog:
	@echo "=== Validate Catalog Closure ==="
	python catalog/validate_catalog.py \
		--metadata $(METADATA) \
		--stac-root $(CATALOG_STAC_ROOT) \
		--dcat $(CATALOG_DCAT) \
		--prov $(CATALOG_PROV)

# ----------------------------
# Sample mode (offline testing)
# ----------------------------

sample: check-inputs
	@echo "=== Sample Mode (offline) ==="
	python normalize/normalize_dwc.py \
		--input samples/dwc_occurrences_sample.jsonl \
		--output $(NORMALIZED)
	$(MAKE) dedupe
	$(MAKE) publish
	$(MAKE) sign
	$(MAKE) gate
	$(MAKE) catalog
	$(MAKE) validate-catalog

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
	rm -rf $(CATALOG_STAC_ROOT)
	rm -f $(CATALOG_DCAT)
	rm -f $(CATALOG_PROV)
