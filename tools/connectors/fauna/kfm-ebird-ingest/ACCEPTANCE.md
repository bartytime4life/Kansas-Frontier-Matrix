# eBird Layer 10

This document covers Layer 10 productization for `kfm-ebird`.

- No download/credentials/network calls.
- No public exact coordinates.
- Governed filter: `complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10`.
- Contract hash recipe: canonical JSON sha256 excluding `generated_at` and `contract_hash`.
- CLIs: ingest, aggregate, promote, build-public-view, run-pipeline, release-ops, observe, doctor, conformance.

## Smoke
`tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-doctor --strict --json`

`tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-conformance --aggregate both --format jsonl --json`
