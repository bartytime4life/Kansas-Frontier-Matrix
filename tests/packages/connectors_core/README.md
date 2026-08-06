# connectors_core tests

Deterministic, no-network tests for the internal `kfm-connectors-core` pure-primitives slice.

These tests exercise import safety, ETag/source-head distinctions, bounded retry decisions,
exact streaming SHA-256, first-class integrity mismatch, allowlisted response metadata,
and diagnostic redaction. They do not run a connector, fetch a source, admit data, emit an
authoritative receipt, write a lifecycle stage, resolve evidence, make policy, release, or
publish.

Run from the repository root:

```bash
PYTHONPATH=packages/connectors-core/src \
  python -m pytest tests/packages/connectors_core -q --strict-config --strict-markers
```
