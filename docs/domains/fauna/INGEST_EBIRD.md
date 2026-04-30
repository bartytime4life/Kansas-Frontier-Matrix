# eBird ingest (Layer 2)

## EvidenceBundle contract

Layer 2 uses `schemas/contracts/v1/fauna/evidence_bundle.schema.json` with required fields:
`schema_version`, `object_type`, `domain`, `source`, `source_uri`, `query_predicate`, `mapping`, and `kfm:spec_hash`.

## Deterministic hash recipe

`kfm:spec_hash` is computed as:

`sha256:` + SHA-256 of canonical JSON (sorted keys, compact separators, no timestamps).

Hash input:
- `EvidenceBundle.spec` when present, else a derived object with
  `schema_version`, `object_type`, `domain`, `source`, `source_uri`, `query_predicate`,
  `aggregate`, `suppression_min_n`, and `mapping`.

## Validator

```bash
python3 tools/validators/fauna/validate_evidencebundle.py --file /tmp/evidencebundle.json
```

## Policy gate summary

`policy/fauna/ebird.rego` denies promotion when public-safety or governance controls fail:
- missing `source_uri`, `query_predicate`, or malformed `kfm:spec_hash`
- suppression threshold under 10
- unsupported aggregate
- public layers exposing exact coordinates
- `exact_points` not `restricted`
- best-effort query predicate quality checks for checklist completeness and effort filters

## Public-safe posture

- Exact points are restricted.
- Aggregates require `suppression_min_n >= 10`.
- Public eBird layers must not expose exact coordinate fields.
