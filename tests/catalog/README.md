# tests/catalog

Catalog-focused tests for `tools/catalog/catalog_crosslink.py`.

## Scope

This folder validates STAC/DCAT/PROV cross-link behavior with deterministic fixtures:

- pass path (aligned triplet)
- subject mismatch failures
- release-ref mismatch failures
- missing catalog ref failures

Authoritative metadata still lives under `data/catalog/`. These tests only validate helper behavior.

## Layout

```text
tests/catalog/
├── README.md
├── test_catalog_crosslink.py
└── fixtures/
    ├── README.md
    ├── aligned-decision.json
    ├── aligned-record.json
    ├── missing-prov-decision.json
    ├── promotion-record-mismatch.json
    └── prov-mismatch.json
```

## Run

From repository root:

```bash
pytest -q tests/catalog/test_catalog_crosslink.py
```

Optional direct helper run:

```bash
python3 tools/catalog/catalog_crosslink.py \
  --decision tests/catalog/fixtures/aligned-decision.json \
  --record tests/catalog/fixtures/aligned-record.json \
  --output /tmp/catalog-crosslink-report.json
```
