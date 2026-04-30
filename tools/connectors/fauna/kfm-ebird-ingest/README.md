# kfm-ebird-ingest (Layer 3)

Layer 3 implements **local streaming EBD TSV ingest** with a restricted-output posture.

## Non-dry-run example

```bash
kfm-ebird-ingest \
  --ebd-file fixtures/ebird/sample_ebd.tsv \
  --source-uri "https://ebird.org/data?request_id=..." \
  --filter "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10" \
  --aggregate huc12 \
  --suppression 10 \
  --emit /tmp/evidencebundle.json \
  --out /tmp/ebird_observations.restricted.jsonl \
  --quarantine /tmp/ebird_quarantine.restricted.jsonl \
  --manifest /tmp/ebird_ingest_manifest.json
```

## Notes

- Only `governed_ebird_checklist_qa_v1` is executable.
- Exact coordinate output is labeled `policy_label=restricted`.
- `--out` and `--quarantine` paths under `data/published` are rejected.
- Dry-run still emits the same EvidenceBundle contract as Layer 2.

## Layer 4 aggregation
Use `kfm-ebird-aggregate` to create public-safe county/HUC12 aggregates, restricted suppression receipts, and aggregate manifests. Public outputs must never contain exact coordinates. Suppression rule: `checklist_count >= suppression_min_n`.

## Layer 5 Promotion (`kfm-ebird-promote`)
Promotes Layer 4 public-safe aggregates into governed public/catalog artifacts.

Example:
```bash
kfm-ebird-promote \
  --aggregate-file tests/fixtures/fauna/ebird/ebird_agg_huc12.public.jsonl \
  --aggregate-manifest tests/fixtures/fauna/ebird/ebird_agg_huc12_manifest.json \
  --evidencebundle tests/fixtures/fauna/ebird/evidencebundle.valid.json \
  --aggregate huc12
```

Safety guarantees:
- never publishes exact coordinates/geometry
- requires `policy_label=public_aggregate`, `exact_points=restricted`, and `public_safe=true`
- refuses to publish suppression receipts or restricted raw rows
- deterministic run id from canonical hash inputs


## Layer 6 Public View (`kfm-ebird-build-public-view`)
Builds public-safe API artifacts from a promoted Layer 5 run: `features.jsonl/csv`, `feature_evidence_drawers.jsonl`, `layer_api_descriptor.json`, `api_manifest.json`, and aggregate-only MapLibre config. It validates spec-hash consistency, suppression/public-safe posture, and denies coordinate/geometry fields.

Example (HUC12):
```bash
kfm-ebird-build-public-view --promotion-dir <promoted_run_dir> --aggregate huc12 --out-dir <promoted_run_dir>/api --maplibre-out data/published/fauna/maplibre/ebird_agg_huc12.json
```

Example (county):
```bash
kfm-ebird-build-public-view --promotion-dir <promoted_run_dir> --aggregate county --out-dir <promoted_run_dir>/api --maplibre-out data/published/fauna/maplibre/ebird_agg_county.json
```

Public API/UI artifacts never expose exact eBird coordinates and never serve restricted observations, quarantines, or suppression receipts.

## Layer 7 Pipeline Runner (`kfm-ebird-run-pipeline`)
Adds governed orchestration ingest → aggregate → promote → public-view with deterministic `run_id`, audit ledger, validation report, and replay artifact.

Default governed predicate (only executable predicate family):
`complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10`

Examples:
- Plan only: `kfm-ebird-run-pipeline --ebd-file tests/fixtures/fauna/ebird/sample_ebd.tsv --plan`
- Execute HUC12: `kfm-ebird-run-pipeline --ebd-file tests/fixtures/fauna/ebird/sample_ebd.tsv --aggregate huc12 --execute`
- Execute county: `... --aggregate county --execute`
- Execute both: `... --aggregate both --execute`
- Resume: `... --execute --resume`
- Force rerun: `... --execute --force`

Safety: no downloads/credentials, no public exact coordinates, no restricted outputs under `data/published`, no suppression receipts in public outputs.

## Layer 8 release operations
Use `kfm-ebird-release-ops` for candidate/compare/approve/rollback/retention governance on completed pipeline runs. This layer does not download eBird data, does not use credentials, and public artifacts never include exact coordinates or restricted/quarantine/suppression details.

## Layer 9 observability
Use `kfm-ebird-observe` for scan/trend/attest/evidence-pack/incident/report flows. See `docs/runbooks/fauna/EBIRD_OPERATIONS.md`.

## Layer 11 maintenance
Use `kfm-ebird-maintain` and `kfm-ebird-migrate` for contract evolution and copy-on-write migrations.


## Layer 12 federation/export
See `docs/domains/fauna/EBIRD_FEDERATION.md` for federation index, discovery, semantic graph, STAC-lite/RO-Crate-lite/warehouse/search exports, and public-safety constraints.

## Layer 13 analytics/insights
Use `kfm-ebird-analytics` and `kfm-ebird-insights` for public-safe descriptive indicator and insight artifacts built from public aggregate/federation outputs only.
