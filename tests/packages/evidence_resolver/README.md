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
└── test_timestamp_boundary.py          # RFC 3339 offsets and safe runtime errors
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
