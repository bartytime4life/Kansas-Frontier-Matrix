# connectors_core injected transport boundary

## Status

**PROPOSED internal implementation; no live transport and no public package exports.**

This module is the next dependency-closed step after the pure connector primitives. It lets a
governed caller inject transport, time, sleep, jitter, and cancellation effects while the package
performs deterministic profile checks, bounded retries, exact-byte validation, and value-minimized
result construction.

## Directory Rules basis

The owning responsibility is reusable implementation, so the module remains under
`packages/connectors-core/src/connectors_core/`. Source-specific endpoints and adapters remain
under `connectors/`; semantic meaning remains under `contracts/source/`; behavior proof remains
under `tests/packages/connectors_core/`; and synthetic values remain under
`fixtures/packages/connectors_core/`.

No root, source registry, schema home, policy home, lifecycle stage, receipt authority, proof home,
release home, or public route is created.

## Implemented boundary

The internal module provides:

- an injected `Transport` protocol with no concrete HTTP implementation; the executor passes a bounded timeout, response-byte budget, and `allow_redirects=false`;
- caller-owned `Clock`, `Sleeper`, `JitterSource`, and `CancellationToken` protocols;
- immutable request, response, profile, attempt, payload, and retrieval-result records;
- exact HTTPS host, port, media-type, timeout, and response-size admission profiles;
- GET and HEAD execution with redirects disabled by contract;
- deterministic retries using the existing `RetryPolicy` and caller-injected jitter;
- delta-seconds and HTTP-date `Retry-After` handling against an injected clock;
- response size, declared/observed length, exact streaming SHA-256, and expected-digest checks;
- metadata-only HEAD and `NOT_MODIFIED` behavior without fake zero-byte artifacts;
- secret-safe request/response representation and value-minimized failure records; and
- fixed `authority_created=false` and `repository_mutation_allowed=false` results.

Package-level `connectors_core/__init__.py` remains empty. Consumers must import
`connectors_core.transport` explicitly until ownership, consumer evidence, compatibility tests,
and API review justify stable exports.

## Finite behavior

| Condition | Internal result |
|---|---|
| Complete admitted GET with matching length, media type, and digest | `SUCCESS` with exact in-memory payload and source-head observation |
| Admitted HEAD | `SUCCESS` with source-head observation and no payload |
| HTTP 304 with no body | `NOT_MODIFIED`; prior artifact retained; no payload |
| Timeout, rate limit, HTTP 206, incomplete response, or transport error | Retry only when `RetryPolicy` permits |
| Attempts or deadline exhausted | `RETRY_EXHAUSTED` |
| Authentication required, access denied, or not found | Terminal failure; no blind retry |
| Redirect or final-target change | `UNSAFE_METADATA / REDIRECT_BLOCKED` |
| Unadmitted or malformed media type | `INVALID_RESPONSE_METADATA` |
| Declared or observed byte budget exceeded | `RESPONSE_TOO_LARGE` |
| Expected digest differs from captured bytes | `INTEGRITY_MISMATCH` |
| Caller or transport cancellation | `CANCELLED` |

These are package transport observations. A source-specific adapter later maps them into the
SourceAdapter vocabulary. This module does not assign `FETCHED`, `MALFORMED`,
`SOURCE_CONFLICT`, source admission, evidence, or release meaning.

## Trust boundary

The module contains no live client and imports no network library. All effects are supplied by
the caller. The executor caps each transport timeout by the remaining retry deadline and passes the
response byte budget before any body is returned. The module does not:

- discover or select an endpoint;
- resolve or activate a SourceDescriptor;
- read credentials or environment variables;
- follow redirects or bypass access controls; the injected transport is required to honor `allow_redirects=false`;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLETS, or PUBLISHED state;
- store captured bytes or mint SourceArtifact metadata;
- emit an authoritative receipt, EvidenceBundle, proof, policy decision, or release object;
- expose a public API; or
- convert transport success, ETag equality, timestamps, content length, or digest equality into truth.

## Validation

```bash
python -m compileall -q packages/connectors-core/src/connectors_core
PYTHONPATH=packages/connectors-core/src python -c \
  "import connectors_core.core; import connectors_core.transport"
PYTHONPATH=packages/connectors-core/src \
  python -m pytest tests/packages/connectors_core -q --strict-config --strict-markers
```

Tests use caller-injected synthetic responses and block ambient network access during import.
A green result proves only the declared internal protocol, retry, integrity, redaction, and
fail-closed behavior. It does not prove a live connector, source rights, source admission,
SourceArtifact persistence, receipt correspondence, evidence closure, policy, release, or
publication.

## Rollback

Revert the bounded implementation commit. No live source, external object, lifecycle record,
authoritative receipt, cache, deployment, release, or public product is created by this slice.
