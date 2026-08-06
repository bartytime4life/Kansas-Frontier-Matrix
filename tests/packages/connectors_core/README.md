# connectors_core tests

Deterministic, no-network tests for the internal `kfm-connectors-core` package.

The suite is split by responsibility:

- `test_core.py`: import safety, ETag/source-head distinctions, bounded retry decisions, exact streaming SHA-256, first-class integrity mismatch, allowlisted response metadata, and diagnostic redaction;
- `test_transport_safety.py`: exact-host profiles, immutable secret-safe requests, and source/lifecycle dependency scans;
- `test_transport_success.py`: fake GET, HEAD, and `NOT_MODIFIED` exchange behavior;
- `test_transport_retry.py`: `Retry-After`, timeout exhaustion, injected jitter, cancellation, and remaining-deadline timeout caps; and
- `test_transport_failures.py`: access denial, redirect blocking, media-type enforcement, partial bodies, response budgets, declared/observed length, and digest mismatch.

The tests do not run a live connector, fetch a source, activate or admit data, persist a `SourceArtifact`, emit an authoritative receipt, write a lifecycle stage, resolve evidence, make policy, release, deploy, or publish.

Run from the repository root:

```bash
PYTHONPATH=packages/connectors-core/src \
  python -m pytest tests/packages/connectors_core -q --strict-config --strict-markers
```
