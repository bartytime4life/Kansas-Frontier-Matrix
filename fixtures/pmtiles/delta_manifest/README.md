# Synthetic PMTiles Delta Manifest Fixtures

These no-network fixtures prove only the proposed delta-manifest shape,
canonical hash, archive digest binding, per-tile lineage, coordinate/quadkey
identity, count reconciliation, and declared QC outcome.

## Fixture lanes

- `valid/` contains a mixed add/modify/remove delta and a valid review-state
  delta.
- `invalid/invalid_schema.json` proves malformed shape denial.
- `invalid/invalid_*.json` semantic cases each isolate one fail-closed
  invariant.
- `expected_findings_manifest.json` binds every semantic-invalid filename to
  its exact value-free finding code and JSON path.

## Semantic negative matrix

| Fixture | Exact finding |
|---|---|
| `invalid_archive_digest_placeholder.json` | `PMTILES_DELTA_ARCHIVE_DIGEST_PLACEHOLDER` |
| `invalid_artifact_ref_digest_mismatch.json` | `PMTILES_DELTA_ARTIFACT_REF_DIGEST_MISMATCH` |
| `invalid_coverage_balance.json` | `PMTILES_DELTA_COVERAGE_BALANCE_INVALID` |
| `invalid_duplicate_tile_identity.json` | `PMTILES_DELTA_TILE_DUPLICATE` |
| `invalid_internal_lifecycle_receipt_ref.json` | `PMTILES_DELTA_INTERNAL_LIFECYCLE_REF_DENIED` |
| `invalid_modified_lineage_missing_prior.json` | `PMTILES_DELTA_MODIFIED_LINEAGE_INVALID` |
| `invalid_qc_average_bytes_mismatch.json` | `PMTILES_DELTA_QC_AVERAGE_BYTES_MISMATCH` |
| `invalid_qc_decision_mismatch.json` | `PMTILES_DELTA_QC_DECISION_MISMATCH` |
| `invalid_removed_lineage.json` | `PMTILES_DELTA_REMOVED_LINEAGE_INVALID` |
| `invalid_spec_hash_mismatch.json` | `PMTILES_DELTA_MANIFEST_HASH_MISMATCH` |
| `invalid_tile_coordinate_out_of_range.json` | `PMTILES_DELTA_TILE_COORDINATE_INVALID` |
| `invalid_tile_digest_placeholder.json` | `PMTILES_DELTA_TILE_DIGEST_PLACEHOLDER` |

All archives, tiles, receipts, source manifests, attestations, hashes, counts,
and dates are synthetic. A passing fixture suite does not verify an archive,
authenticate a byte range, validate a PMSIG/DSSE signature, resolve an
EvidenceBundle, evaluate policy, authorize release, deploy an artifact, or
publish a map layer.
