# SourceAdapter protocol boundary

`connectors_core.source_adapter` supplies pure, source-agnostic types for future source-specific KFM adapters. The module is executable infrastructure, not source admission or publication authority.

## Public module surface

- `DiscoveryCursor` — explicit profile, observation time, cursor, and bounded result limit.
- `SourceLocator` — canonical secret-safe locator and deterministic locator digest.
- `SourceArtifactView` — structural parser input over immutable artifact bytes and metadata.
- `ParseFinding` and `ParseResult` — finite parser diagnostics and deeply immutable records.
- `SourceHealth` — bounded source-health observation with false-clear prevention.
- `SourceAdapter` — runtime-checkable discover/fetch/parse/health protocol.
- `assert_source_adapter_boundary` — non-invoking structural and forbidden-capability check.

## Authority boundary

The module performs no network, filesystem, environment, clock, registry, lifecycle, evidence, policy, review, receipt, release, publication, or GitHub operation. All authority-bearing flags in parser and health values are fixed false.

A structural protocol check is not source approval. Concrete adapters still need source-specific transport profiles, rights and sensitivity review, parser fixtures, correction behavior, stable identity, secret handling, and separate source activation.

## False-clear rule

Source health is not domain-event status. `clear_signal_allowed` is always false. Missing, failed, stale, unauthorized, or rate-limited source checks retain uncertainty; only the accepted domain contract and authoritative source semantics may establish rescission or clearance.

## Validation

```bash
python -m pytest tests/packages/connectors_core/test_source_adapter.py -q --strict-config --strict-markers
```

The focused suite checks canonical identity, secret rejection, deep immutability, finite parser outcomes, time ordering, false-clear prevention, protocol conformance, forbidden capabilities, and import-time no-network behavior.
