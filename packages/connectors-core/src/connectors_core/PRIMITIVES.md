# connectors_core pure primitives

## Status

**PROPOSED internal implementation; no public package exports.** This slice replaces the
comment-only `core.py` placeholder with deterministic, standard-library-only primitives for
governed callers. It does not implement a live transport or source-specific connector.

## Directory Rules basis

The owning responsibility is reusable implementation, so the code remains under
`packages/connectors-core/src/connectors_core/`. Source-specific endpoint behavior remains
under `connectors/`; semantic meaning remains under `contracts/source/`; machine shape
remains under `schemas/contracts/v1/source/`; validation and behavior proof remain under
`tests/` and `.github/workflows/`. No root, schema home, policy home, source registry,
receipt store, release home, or proof home is created.

## Implemented surface

`core.py` provides internal primitives for:

- strong and weak ETag parsing without treating an ETag as a content digest;
- immutable source-head observations that preserve observed time, Last-Modified,
  content length, upstream revision, and an independently computed SHA-256 digest;
- allowlisted response-header projection that drops credential-bearing and unknown fields;
- bounded retry decisions controlled by attempts, elapsed time, deadline, response delay,
  and caller-injected deterministic jitter;
- exact streaming SHA-256 with caller-supplied byte limits;
- first-class integrity `MATCH` and `MISMATCH` outcomes that preserve the expected digest;
- diagnostic URL and message redaction; and
- finite, value-minimized failure details.

The package initializer intentionally exports none of these symbols. Consumers must import
`connectors_core.core` until consumer evidence, compatibility tests, ownership, and API review
support a stable package-level export.

## Trust boundary

The module performs no network, filesystem, environment, credential, registry, lifecycle,
receipt, evidence, policy, review, release, publication, or clock work at import time.

A result from this module is only a transport/integrity observation. It cannot:

- admit or activate a source;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- mint an authoritative `IngestReceipt` or `RunReceipt`;
- resolve an `EvidenceRef` or close an `EvidenceBundle`;
- decide rights, sensitivity, policy, review, correction, rollback, release, or publication;
- serve a public client; or
- convert fetch success, ETag equality, or digest equality into source truth.

## Failure posture

Only `PARTIAL`, `TIMEOUT`, `RATE_LIMITED`, and `TRANSPORT_ERROR` are retry candidates in
this first profile. Authentication, access denial, not-found, cancellation, excessive size,
integrity mismatch, invalid metadata, unsafe metadata, and exhausted retry are terminal.
Every retry is bounded by attempt count and deadline; permanent governance or access
failure is never reclassified as a transient transport error.

## Validation

```bash
python -m compileall -q packages/connectors-core/src/connectors_core
PYTHONPATH=packages/connectors-core/src python -c "import connectors_core.core"
PYTHONPATH=packages/connectors-core/src \
  python -m pytest tests/packages/connectors_core -q --strict-config --strict-markers
```

The connector-gate workflow also installs the package, imports it, and runs the focused suite.
A green check proves only the declared pure-function and boundary behavior. It does not prove
a connector run, source rights, source admission, receipt correspondence, lifecycle routing,
evidence closure, release, or publication.

## Rollback

Revert the implementation commit. No source, source artifact, lifecycle record, receipt,
proof, release, cache, deployment, or public product is created by this slice.
