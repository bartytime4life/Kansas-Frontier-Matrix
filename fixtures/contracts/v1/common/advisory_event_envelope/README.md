# AdvisoryEventEnvelope fixtures

This fixture family is synthetic, deterministic, and no-network. It wraps
repository-local `KdheHabAdvisorySnapshot` fixtures only; it does not represent
current KDHE status and must not be used as a public advisory.

`cases.json` is the fixture manifest. It names six immutable positive envelopes
under `bases/` and fifteen cases. Negative cases are derived from one base by a
small, deterministic `replace` or `remove` JSON-pointer patch. The validator
loads each base safely, materializes each case in memory, rejects malformed
manifests, base paths, or patches, and then checks declared polarity.

## Positive bases

- active whole-water-body watch;
- failed source check retaining the last confirmed state;
- stale source producing status-unconfirmed;
- authoritative lifted/rescinded status;
- duplicate-name identity conflict with no geometry; and
- zoned warning preserving zone scope.

## Negative polarity

Structural cases prove missing issuing authority and public-use permission fail
schema validation. Semantic cases prove false clears, zone collapse, missing
rescission, source-role collapse, stale-as-active status, invalid time ordering,
and geometry exposure during identity conflict fail closed.

For every materialized case, the validator also resolves the local payload,
validates its existing schema, recomputes its canonical record digest, binds its
declared source-content digest, and recomputes the wrapper event ID. It performs
no source fetch, source activation, alerting, lifecycle write, release,
deployment, publication, or public-use decision.
