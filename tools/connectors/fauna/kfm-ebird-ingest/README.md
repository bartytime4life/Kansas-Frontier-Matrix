# kfm-ebird-ingest (Layer 2 scaffold)

This connector remains dry-run only and does not ingest, download, or publish exact points.

## Dry-run

```bash
kfm-ebird-ingest \
  --ebd-file /data/ebd-EBD.txt \
  --source-uri "https://ebird.org/data?request_id=..." \
  --filter "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10" \
  --aggregate huc12 \
  --suppression 10 \
  --emit /tmp/evidencebundle.json \
  --dry-run
```

## Validator

```bash
python3 tools/validators/fauna/validate_evidencebundle.py /tmp/evidencebundle.json
```

## Hash recipe

The emitted `kfm:spec_hash` uses canonical JSON and SHA-256 from `packages/evidence/evidencebundle_hash.py`.
If `spec` exists it is hashed directly; otherwise hash input is derived from governance-critical fields.

## Governance gates

Promotion checks in `policy/fauna/ebird.rego` enforce:
- public-safe posture (`exact_points=restricted`, no exact coordinate fields)
- suppression floor `>=10`
- aggregate only `county|huc12`
- best-effort checklist QA constraints in query predicates
