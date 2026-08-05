# USDA PLANTS Distribution Snapshot Normalizer

`normalize_distribution_snapshot.py` converts three bounded local CSV inputs into one deterministic `USDAPlantsDistributionSnapshotCandidate`.

## Boundary

This is a fixture-first normalization tool, not a live connector. It does not resolve the current `usda_plants` / `usda-plants` / `usda/plants` connector-placement drift and performs no network access.

The input headers are a KFM synthetic profile, not a claim about current USDA download headers.

## Command

```bash
python tools/ingest/usda_plants/normalize_distribution_snapshot.py \
  --taxa fixtures/domains/flora/usda_plants_distribution_snapshot/input/taxa.csv \
  --counties fixtures/domains/flora/usda_plants_distribution_snapshot/input/counties.csv \
  --distribution fixtures/domains/flora/usda_plants_distribution_snapshot/input/distribution.csv \
  --snapshot-date 2026-04-30 \
  --evidence-ref kfm://evidence/flora/usda-plants/synthetic-2026-04-30@sha256:<64-hex> \
  --out /tmp/usda-plants-distribution.json
```

## Semantics

The tool declares a complete `taxa × counties` matrix. An explicit source row may produce `reported_present` or `reported_absent`. A missing row always produces `not_reported` / `no_claim`.

## Exit codes

- `0`: candidate written.
- `1`: input or normalization denial.
- `2`: CLI or output failure.

A written candidate remains held for source-rights/currentness and rare-plant sensitivity review.
