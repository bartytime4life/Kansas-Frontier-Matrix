# Evidence resolution helper module

Internal Python modules for the package-local
`kfm/evidence-ref-bundle-candidate/v1alpha1` profile. They inherit all
authority limits from the [package README](../../README.md).

## Current tree

```text
packages/evidence-resolver/src/evidence_resolver/
├── README.md
├── __init__.py             # intentionally empty; no supported public exports
├── core.py                 # pure bounded candidate evaluation
├── hydrology_fixture_adapter.py # fixed internal manifest lookup and digest gate
├── runtime_projection.py   # conservative internal next-step projection
└── verification_history.py # shared standard-library validation and replay
```

## Implemented checks

`core.py` provides:

- bounded JSON parsing with byte, duplicate-key, non-finite-number, depth,
  collection, and string limits;
- closed validation of the current proposed `EvidenceRef` and
  `EvidenceBundle` field shapes used by this profile;
- exact bundle-reference, lookup-ID, and member-reference comparisons;
- closed `VerificationStateHistory` shape and semantic validation shared with
  its repository validator;
- bitemporal replay, exact EvidenceRef-subject binding, and fail-closed
  corrected, superseded, revoked, unknown, and inconsistent-history outcomes;
- explicit caller-supplied current-head, canonical policy-outcome projection,
  and correction context;
- deterministic issue ordering and serialization; and
- fixed diagnostics that never echo candidate values.

`hydrology_fixture_adapter.py` adds only the first maintainer-authorized #2975
fixture packet:

- accepts one stable bundle ID and rejects path-like IDs or caller bundles;
- reads the closed repository manifest without scanning or consulting an
  environment-selected root;
- permits only
  `fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json`;
- rejects absolute paths, traversal, non-allowlisted paths, symlinks, duplicate
  IDs, unsupported profiles, malformed or oversized JSON, digest drift, schema
  failure, and bundle-ID mismatch with fixed safe codes;
- digests the entire bounded parsed object with sorted keys, compact separators,
  ASCII escaping, finite JSON numbers, and SHA-256 under the packet-local
  `kfm/evidence-bundle-fixture-digest/v1alpha1` profile; and
- feeds only a verified candidate into `core.py`, then immediately applies the
  existing runtime projection.

The selected fixture uses a synthetic `kfm://` EvidenceRef so the existing
mandatory verification-history subject binding can be satisfied exactly. The
manifest binds the resulting checked-in bytes; this is not a universal content
identity, RFC 8785 claim, `spec_hash` reinterpretation, registry, or production
store.

`runtime_projection.py` converts only the finite candidate status into a
non-authoritative next-step posture:

| Candidate status | Internal disposition |
|---|---|
| `RESOLVED` | `CONTINUE_GOVERNED_CHECKS` |
| `UNRESOLVED` | `ABSTAIN` |
| `DENIED` | `DENY` |
| `ERROR` | `ERROR` |

The projection deliberately has no `ANSWER` state. It always emits
`authoritative: false` and `renderable: false`. A resolved candidate must still
pass evidence-authority, rights, sensitivity, policy, review, release,
citation, and correction checks. Non-resolved candidates cannot carry a
`bundle_id`; inconsistent shapes fail closed with `ValueError`.

These modules do not fetch remotely, cache, infer, sign, persist, activate,
review, release, deploy, or publish anything. They do not evaluate claim scope,
citations, rights, sensitivity, policy, or evidence truth. Shape checks for
those fields prevent accidental omission but do not establish their semantics.

## Input and output posture

The caller supplies one closed object containing `profile`, `evidence_ref`,
`bundle_candidate`, `lookup_context`, `verification_history`, and
`verification_as_of`. The history subject must equal the EvidenceRef value,
and the replayed state must be `ACTIVE`. Candidate results always include
`authoritative: false`, stable `checks_performed`, fixed issue codes, and
explicit limitations. `bundle_id` is exposed only for a `RESOLVED` candidate.

The runtime projection is still an internal value, not a public
`DecisionEnvelope`, `RuntimeResponseEnvelope`, Evidence Drawer payload, or
StoryNode. No consumer may map it directly to public delivery without accepted
evidence, policy, review, release, correction, citation, and runtime boundaries.

## Validation and open work

Tests live under
[`tests/packages/evidence_resolver/`](../../../../tests/packages/evidence_resolver/README.md)
and fixtures under
[`fixtures/packages/evidence_resolver/v1alpha1/`](../../../../fixtures/packages/evidence_resolver/v1alpha1/README.md).
The CLI wrapper lives under
[`tools/validators/evidence_resolver/`](../../../../tools/validators/evidence_resolver/README.md).

Permanent named ownership, a stable public API, accepted public contracts,
production repository or registry wiring, canonical claim-scope comparison,
authoritative lookup/correction/release records, and public runtime envelope
construction remain **PROPOSED / NEEDS VERIFICATION**.
