# connectors_core retrieval-to-SourceArtifact handoff

## Status

**PROPOSED internal implementation; fixture-first; no live transport, storage, receipt emitter, lifecycle writer, or public export.**

`artifact_handoff.py` joins the internal injected transport result to the existing fixture-first `SourceArtifact` metadata profile without collapsing their responsibilities.

## API

```python
from connectors_core.artifact_handoff import (
    ArtifactHandoffContext,
    ParserIdentity,
    RightsSnapshot,
    build_source_artifact_handoff,
)

handoff = build_source_artifact_handoff(result, context)
metadata = handoff.metadata_dict()
bytes_to_validate = handoff.payload_bytes()
```

The package-level `connectors_core/__init__.py` remains empty. Consumers must import the internal module explicitly until ownership, consumer evidence, compatibility tests, and API review justify stable exports.

## Admitted result

Only one complete, successful, injected `GET` retrieval with non-empty exact bytes can produce a handoff. The builder rejects:

- `HEAD` and `NOT_MODIFIED`;
- timeout, rate limit, access denial, not found, cancellation, partial, unsafe, oversized, integrity-mismatched, exhausted, or transport-error results;
- missing or mismatched source-head digest or length;
- missing final HTTP status;
- self-supersession or invalid conflict/correction lineage; and
- authority-bearing or repository-mutation-bearing results.

## Output boundary

The handoff carries exact immutable payload chunks and deep-frozen metadata shaped for the current SourceArtifact schema. Its fixed non-effects are:

- `authority_created=false`
- `lifecycle_write_allowed=false`
- `receipt_created=false`
- `repository_mutation_allowed=false`
- SourceArtifact `public_use_allowed=false`
- SourceArtifact `release_ref=null`

The caller must still validate metadata and payload, prove `SourceDescriptor` and `IngestReceipt` correspondence, decide storage, and perform any lifecycle transition through the accepted owning boundary.

## Directory Rules basis

The owning responsibility is reusable source-agnostic implementation, so code remains in `packages/connectors-core/src/connectors_core/`. The semantic contract, tests, fixtures, workflow, and provenance remain in their own established responsibility roots. No source-specific adapter or lifecycle lane is created.

## Validation

```bash
python -m compileall -q packages/connectors-core/src/connectors_core
PYTHONPATH=packages/connectors-core/src \
  python -m pytest tests/packages/connectors_core/test_artifact_handoff.py \
  -q --strict-config --strict-markers
```

A green result proves only the internal exact-byte and metadata-candidate boundary. It does not prove a live source, source admission, receipt correspondence, storage, lifecycle promotion, evidence, policy, release, or publication.

## Rollback

Revert the bounded implementation. The module produces no external or governed lifecycle state.
