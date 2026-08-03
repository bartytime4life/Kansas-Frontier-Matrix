# Evidence resolution helper module

Internal Python module for the package-local
`kfm/evidence-ref-bundle-candidate/v1alpha1` profile. It inherits all
authority limits from the [package README](../../README.md).

## Current tree

```text
packages/evidence-resolver/src/evidence_resolver/
├── README.md
├── __init__.py   # intentionally empty; no supported public exports
└── core.py       # pure bounded candidate evaluation
```

## Implemented checks

`core.py` provides:

- bounded JSON parsing with byte, duplicate-key, non-finite-number, depth,
  collection, and string limits;
- closed validation of the current proposed `EvidenceRef` and
  `EvidenceBundle` field shapes used by this profile;
- exact bundle-reference, lookup-ID, and member-reference comparisons;
- explicit caller-supplied current-head, canonical policy-outcome projection,
  and correction context;
- deterministic issue ordering and serialization; and
- fixed diagnostics that never echo candidate values.

It does not fetch, cache, infer, canonicalize, sign, persist, review, release,
or publish anything. It does not evaluate claim scope, citations, rights,
sensitivity, policy, or evidence truth. Shape checks for those fields prevent
accidental omission but do not establish their semantics.

## Input and output posture

The caller supplies one closed object containing `profile`, `evidence_ref`,
`bundle_candidate`, and `lookup_context`. Results always include
`authoritative: false`, stable `checks_performed`, fixed issue codes, and
explicit limitations. `bundle_id` is exposed only for a `RESOLVED` candidate.

The result is an internal value, not a contract or governed runtime envelope.
No consumer may map it directly to public delivery without accepted evidence,
policy, review, release, correction, and runtime boundaries.

## Validation and open work

Tests live under
[`tests/packages/evidence_resolver/`](../../../../tests/packages/evidence_resolver/README.md)
and fixtures under
[`fixtures/packages/evidence_resolver/v1alpha1/`](../../../../fixtures/packages/evidence_resolver/v1alpha1/README.md).
The CLI wrapper lives under
[`tools/validators/evidence_resolver/`](../../../../tools/validators/evidence_resolver/README.md).

Named ownership, a stable API, accepted public contracts, consumer wiring,
canonical claim-scope comparison, authoritative lookup/correction records,
and runtime outcome mapping remain **PROPOSED / NEEDS VERIFICATION**.
