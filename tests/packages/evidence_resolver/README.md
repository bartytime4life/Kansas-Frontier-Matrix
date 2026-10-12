# Evidence resolver package tests

Tests for the internal
`kfm/evidence-ref-bundle-candidate/v1alpha1` implementation under
[`packages/evidence-resolver/`](../../../packages/evidence-resolver/README.md).

## Scope

- Owner: `@bartytime4life` is provisional accountable maintainer for the first
  #2975 fixture packet; package-wide `OWNER_TBD` remains.
- Inputs: synthetic fixtures under
  [`fixtures/packages/evidence_resolver/v1alpha1/`](../../../fixtures/packages/evidence_resolver/v1alpha1/README.md).
- Outputs: unittest pass/fail state and bounded subprocess output.
- Exposure/retention: public-safe test material only; no production state.
- Prohibited: live registry/network access, real evidence, source activation,
  policy inference, review/release actions, public responses, or publication.

## Current tree

```text
tests/packages/evidence_resolver/
├── README.md
├── test_cli.py                         # command and fixture inventory
├── test_core.py                        # candidate bounds and finite outcomes
├── test_hydrology_fixture_adapter.py   # lookup, digest, paths, and no-I/O proof
├── test_result_schema.py               # existing result-contract conformance
├── test_runtime_projection.py          # finite internal runtime map
├── test_runtime_projection_fixtures.py # candidate-to-runtime integration
├── test_timestamp_boundary.py          # RFC 3339 offsets and safe runtime errors
└── test_verification_query_timestamps.py # strict replay-query grammar
```

Run:

```bash
make evidence-resolver
make evidence-resolver-deny
```

The suite checks exact candidate outcomes, deterministic serialization,
non-authority, safe diagnostics, duplicate/non-finite/size/depth rejection,
standard-library-only imports, history-shape pinning, bitemporal replay,
subject binding, finite-outcome precedence, complete-object digest binding,
manifest misses, duplicate IDs, profile and schema failure, tamper detection,
absolute/traversal/outside-root/non-allowlisted paths, symlinks, caller-bundle
injection, no negative fall-through, and active denial of network, URL, and
process access. Static imports exclude model clients.

The timestamp boundary regressions reject overflowing numeric UTC offsets before
Python can normalize them. They exercise direct candidates, every existing policy
posture, and the manifest adapter after a matching test-only digest, while
preserving valid timestamp forms and non-authoritative runtime behavior.

## Verification replay query regression

Both `effective_as_of` and `recorded_as_of` use the verification-history
profile's exact `YYYY-MM-DDTHH:MM:SSZ` grammar and real calendar values.
Unpadded fields and lowercase `t`/`z` must not be normalized by the parser.
They produce `verification/query-invalid` and an internal `ERROR`, without
retaining a bundle ID or granting render or answer authority.

The focused tests reuse the existing positive synthetic fixture and exercise
the actual shared parser, replay, candidate evaluator, and runtime projection.
They also preserve valid calendar boundaries, independent correction cutoffs,
finite policy outcomes, safe diagnostics, and non-mutating no-network behavior.

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  python -m unittest discover -s tests/packages/evidence_resolver \
  -p 'test_verification_query_timestamps.py' -v
```

This focused command supplements, rather than replaces, both Make targets
above. A passing regression run does not establish whole-repository, hosted CI,
public consumer, review, or release closure.
