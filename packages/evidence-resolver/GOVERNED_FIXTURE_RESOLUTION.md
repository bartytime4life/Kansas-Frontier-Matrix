# Governed fixture resolution profile

## Status and authority

This profile is a deterministic, no-network proof slice for issue #2975. It
extends the existing `packages/evidence-resolver` ownership instead of creating
a second resolver, evidence store, response envelope, or outcome vocabulary.

The profile is **fixture-only**. Its `ANSWER` outcome means that one configured
synthetic Hydrology fixture supports one synthetic test request. It does not
admit a source, authenticate a real release, authorize public use, publish data,
or make the fixture an EvidenceBundle proof record.

The implementation composes, without changing:

- the current EvidenceRef and EvidenceBundle contracts and schemas;
- `evidence_resolver.core.evaluate_resolution_candidate`;
- the shared VerificationStateHistory validator and replay semantics consumed by
  that evaluator; and
- `envelopes.runtime_response.build_runtime_response_candidate` and the finite
  `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` vocabulary.

## Allowed store boundary

`ConfiguredFixtureStore` accepts only `StoredBundleRecord` objects supplied by
its caller. It has no path, URL, environment, registry, database, arbitrary-key,
or lifecycle-root API. The resolver performs no reads from `RAW`, `WORK`,
`QUARANTINE`, `data/proofs/`, release roots, or any unconfigured store.

The resolver returns only a RuntimeResponseEnvelope-shaped mapping. It never
returns the store, a stored record, an EvidenceBundle, source records, citation
text, checksums, review/policy/release metadata, or internal paths.

A request marked `DIRECT_STORE` is denied before lookup. A `PUBLIC` consumer is
also denied because the current strict ReleaseManifest profile is
`PROPOSED_INACTIVE`, `FIXTURE_ONLY`, and does not grant public-use authority.

## Typed inputs

The module exposes typed immutable records for:

- `EvidenceRef`;
- the governed fixture request;
- spatial, temporal, and attribute support;
- fixture trust posture; and
- the configured stored-bundle record.

The EvidenceRef remains the current `{ref, kind, bundle_ref?}` shape. No new
public EvidenceRef or EvidenceBundle fields are introduced.

## Resolution and trust checks

For the selected synthetic Hydrology profile, the resolver checks the following
in deterministic order:

1. request shape, supported access path, consumer class, and EvidenceRef kind;
2. exact lookup by `EvidenceRef.bundle_ref`, with duplicate identities treated
   as `ERROR`;
3. exact fixture profile/schema version and the inactive fixture-only release
   posture;
4. canonical full-bundle SHA-256 content digest and the expected bundle
   `spec_hash` value;
5. current EvidenceRef/EvidenceBundle shape, identity, membership, verification
   history, current-head, policy, and correction checks through the existing
   candidate evaluator;
6. active/current evidence state and freshness;
7. rights posture and the bundle's sensitivity level;
8. policy, review, and fixture release references without treating those
   references as authenticated authority;
9. source identity and source-role match;
10. exact claim scope plus spatial and temporal support; and
11. non-empty citation support.

The full-bundle digest canonicalization is UTF-8 JSON with ASCII escaping,
non-finite values forbidden, keys sorted, and compact separators. This digest is
stored beside the bundle rather than inside it, avoiding a self-referential
content hash. The bundle's current `spec_hash.value` is separately compared to
its configured expected value; the profile does not invent a new canonical
EvidenceBundle spec-hash algorithm.

## Finite outcomes

| Outcome | Examples in this slice | Outward evidence |
|---|---|---|
| `ANSWER` | Exact synthetic ref, bundle, digest, support, and fixture trust posture pass | Typed EvidenceRef plus supported precision only |
| `ABSTAIN` | Bundle missing, stale/superseded, unresolved rights/review/release reference, source/scope/time mismatch, citation missing | Empty `evidence_refs`; no precision or stored content |
| `DENY` | Direct-store attempt, public consumer, rights/sensitivity/policy/review denial, withdrawal | Empty `evidence_refs`; no precision or stored content |
| `ERROR` | Malformed input/bundle, digest or spec-hash mismatch, duplicate identity, unsupported profile/version, envelope-build failure | Empty `evidence_refs`; no precision or stored content |

Reason codes are fixed profile vocabulary and do not reflect fixture values.
Negative outcomes cannot fall through to `ANSWER`.

## Correction and freshness behavior

The existing candidate evaluator remains authoritative for verification-history
replay, current-head, policy passthrough, and correction-state checks. This
profile additionally maps stale and superseded fixture evidence to `ABSTAIN`,
withdrawn evidence to `DENY`, and malformed or contradictory state to `ERROR`.
It performs no correction, supersession, withdrawal, or rollback mutation.

## Receipts and publication

No receipt is emitted. The slice is an in-memory fixture consumer and does not
create a validation receipt, review record, release manifest, proof, or
publication artifact. Existing trust-object references are checked only as
bounded fixture posture; a reference is not authentication or approval.

No source, model, network client, secret, release, deployment, publication,
public route, browser surface, or access expansion is introduced.

## Validation

Focused proof lives in:

```text
tests/packages/evidence_resolver/test_governed_fixture.py
```

The representative fixture lives in:

```text
fixtures/packages/evidence_resolver/governed/v1/hydrology_measurement.json
```

The tests cover deterministic supported, `ABSTAIN`, `DENY`, and `ERROR`
outcomes; identity/digest/profile/store conflicts; stale, scope, review, and
public-use failures; no-network execution; composition with the existing
candidate evaluator and response builder; and no raw-store leakage.

## Rollback

Revert this additive module, fixture, test, and document. Existing resolver,
envelope, schema, policy, review, release, correction, and domain surfaces are
unchanged, so rollback requires no migration, source deactivation, public
correction, release withdrawal, deployment rollback, or cache invalidation.
