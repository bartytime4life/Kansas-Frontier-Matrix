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
