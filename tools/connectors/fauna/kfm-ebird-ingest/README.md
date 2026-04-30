# kfm-ebird-ingest (Layer 1 scaffold)

This connector is the first scaffold layer for KFM eBird ingest. It intentionally does **not** implement full EBD parsing, downloading, publishing, or public exact-point outputs.

## CLI

Run via:

```bash
python tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_ingest.py --help
```

### Example

```bash
kfm-ebird-ingest \
  --ebd-file /data/ebd-EBD.txt \
  --source-uri "https://ebird.org/data?request_id=..." \
  --filter "complete==TRUE && protocol_type!='Incidental' && duration_min>=5 && distance_km<=5 && number_observers<=10" \
  --aggregate huc12 \
  --suppression 10 \
  --emit evidencebundle.json \
  --dry-run
```

## Behavior

- Required arguments are validated (`--ebd-file`, `--filter`, `--aggregate`, `--emit`).
- `--aggregate` must be `county` or `huc12`.
- `--suppression` must be at least 10.
- `--source-uri` defaults to `file://<ebd-file>`.
- In `--dry-run`, the command emits an EvidenceBundle JSON scaffold to `--emit` and does not read the EBD file.

## EvidenceBundle (v1)

Dry-run output contains:

- `source_uri`
- `query_predicate`
- `mapping`
- `kfm:spec_hash`

`kfm:spec_hash` is a `sha256:` hash over a canonicalized normalized spec JSON (sorted keys, compact separators, and no volatile timestamp fields).

## eBird mapping

- `sampling_event_identifier` -> `kfm:dataset_key`
- `observation_date` -> `occurrenceDate`
- `latitude` -> `decimalLatitude`
- `longitude` -> `decimalLongitude`
- `observation_count` -> `individualCount`
- `species_taxon_id` -> `taxonKey`
- `basisOfRecord` -> `HumanObservation`
