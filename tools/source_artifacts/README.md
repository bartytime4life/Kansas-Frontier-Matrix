# SourceArtifact local verification helpers

This directory contains a fixture/reference content-addressed store for exact byte streams that already pass the proposed `SourceArtifact` validator.

```bash
python tools/source_artifacts/content_addressed_store.py store \
  METADATA.json PAYLOAD STORE_ROOT
python tools/source_artifacts/content_addressed_store.py verify \
  METADATA.json STORE_ROOT
```

The helper is deterministic and no-network. It writes only beneath the caller-supplied temporary or local store root. It does not define production object storage, retention, credentials, legal hold, evidence admissibility, lifecycle promotion, release, or public delivery. A passing store or verify operation proves only that local bytes match the declared SHA-256 and byte length.
