# SourceArtifact local verification helpers

This directory contains a fixture/reference content-addressed store for exact byte streams that already pass the proposed `SourceArtifact` validator.

```bash
python tools/source_artifacts/content_addressed_store.py store \
  METADATA.json PAYLOAD STORE_ROOT
python tools/source_artifacts/content_addressed_store.py verify \
  METADATA.json STORE_ROOT
```

The helper is deterministic and no-network. It writes only beneath the caller-supplied temporary or local store root. It does not define production object storage, retention, credentials, legal hold, evidence admissibility, lifecycle promotion, release, or public delivery. A passing store or verify operation proves only that local bytes match the declared SHA-256 and byte length.

## Captured-input binding

`store` uses the strict, bounded metadata and payload reads from
`load_validated_artifact`, then addresses and writes the object using those same
captured values. It does not reopen either input path after validation.
Replacement, growth, removal, or a symlink substituted after capture cannot
supply different stored bytes. Invalid pairs are refused before creating the
store root. An existing corrupt object is an error, not a silent repair.

This is not an atomic filesystem snapshot or a concurrency-safe production store.
A file can change while it is being read; the captured bytes must still match the
captured metadata's digest and length. The caller must control the destination
root. Concurrent destination changes and ancestor-symlink races are outside this
reference helper's guarantee. `verify` remains a separate check of stored bytes,
not source admission or publication approval.

Run the fixture profile and its no-network regressions from the repository root:

```bash
python -m unittest discover -s tests/validators -p test_validate_source_artifact.py -v
python -m unittest discover -s tests/validators -p test_artifact_reader_short_reads.py -v
python -m tools.validators.validate_source_artifact --fixtures
```

The existing `source-artifact-validation` workflow watches and runs the first
module, including the captured-input regressions. No new workflow is required.
