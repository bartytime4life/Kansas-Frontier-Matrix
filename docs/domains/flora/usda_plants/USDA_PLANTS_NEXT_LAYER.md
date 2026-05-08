# USDA PLANTS Next Layer

## 1. Purpose
This layer adds deterministic, no-network fixture loading for USDA PLANTS Flora datasets with receipts, proof manifesting, and policy gates.

## 2. Lifecycle placement
This layer bridges fixture-backed inputs toward governed PROCESSED outputs and policy/proof checks, without enabling publication.

## 3. No-network fixture posture
- This layer does not download USDA PLANTS data.
- This layer only reads local fixture CSV files.
- CI remains no-network and deterministic.

## 4. Loader contract
The fixture loader transforms checklist/state/county fixture CSVs into USDA PLANTS dataset JSON objects under `processed/flora/usda_plants/` with deterministic ordering and canonical spec hashing.

## 5. Receipt contract
The loader writes:
- `receipts/flora/usda_plants/ingest_receipt.json`
- `receipts/flora/usda_plants/validation_receipt.json`

These document inputs, outputs, counts, validation details, and pass/fail status.

## 6. Proof manifest contract
`tools/proofs/flora/usda_plants_proof_manifest.py` generates `proofs/flora/usda_plants/spec_hash_manifest.json` with per-dataset `spec_hash` entries and a deterministic `manifest_hash`.

## 7. Policy gate contract
OPA policy `policy/flora/usda_plants.rego` enforces fail-closed governance checks for spec hash consistency, public policy label, licensing/rights holder, provenance presence, raw/work/quarantine closure, FIPS shape, and scientific authorship token requirements.

## 8. CI expectations
- Run fixture loader CLI.
- Run proof manifest CLI.
- Run pytest coverage for loader/proof slices.
- Optionally run `opa test policy/flora/usda_plants.rego policy/flora/usda_plants_test.rego` when OPA is available.

## 9. What is intentionally not implemented yet
- This layer does not publish public map layers.
- This layer does not promote datasets.
- This layer does not perform live USDA endpoint fetching.
- This layer does not execute catalog/triplet promotion workflows.

## 10. Future live-USDA ingestion path
A future governed layer may add live USDA ingestion only after source terms verification, controlled networking posture, stronger provenance contracts, expanded policy gates, and promotion controls.

This layer only proves that USDA PLANTS records can move through a deterministic, governed, fixture-backed path.
