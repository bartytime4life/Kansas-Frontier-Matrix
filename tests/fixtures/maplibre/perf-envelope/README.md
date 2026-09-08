<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/maplibre/perf-envelope/v1
title: MapLibre performance-envelope fixtures
type: test-fixture-readme
version: v1.0.0
status: implemented; synthetic; no-network; non-authoritative
owners: OWNER_TBD — MapLibre steward · Configuration steward · Validation steward
created: 2026-09-08
updated: 2026-09-08
policy_label: public; synthetic-only; configuration-validation; no-release-authority
owning_root: tests/
responsibility: provide deterministic positive and negative inputs for the MapLibre PerfEnvelope v1 machine contract
truth_posture: CONFIRMED synthetic fixture polarity and local validator execution; HOLD benchmark, runtime, policy, release, and publication claims
related:
  - ../README.md
  - ../../../maplibre/test_perf_envelope_contract.py
  - ../../../../configs/maplibre/perf-envelope.v1.json
  - ../../../../schemas/maplibre/perf-envelope.schema.json
  - ../../../../tools/validators/maplibre/validate_perf_envelope.py
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, maplibre, performance, configuration, fixtures, negative-tests, no-network]
notes:
  - "These examples validate configuration machine shape only; they are not measurements, baselines, proof, policy decisions, release records, or publication authority."
[/KFM_META_BLOCK_V2] -->

# MapLibre performance-envelope fixtures

Synthetic, no-network examples for the repository-owned `PerfEnvelope` v1
configuration contract. `valid/` contains accepted boundary and representative
payloads; `invalid/` contains one or more deliberate contract violations per
file.

Run from any working directory:

```bash
python tools/validators/maplibre/validate_perf_envelope.py --fixtures
```

The validator must report every valid example as `OK`, every invalid example as
`EXPECTED_FAIL`, and return zero only when both fixture lanes are nonempty and
their polarity is preserved.

Passing this fixture pack proves only deterministic JSON parsing and the tested
machine constraints. It does not run a browser, establish threshold authority,
measure MapLibre, approve a policy decision, release an artifact, or publish a
map.

## Maintenance rules

- Keep examples synthetic, compact, public-safe, deterministic, and offline.
- Add a focused test assertion when a new normative constraint is introduced.
- Do not add screenshots, captured metrics, source data, secrets, receipts,
  proofs, releases, or production endpoints.
- Change schema, validator binding, fixtures, tests, workflow inventory, and
  boundary documentation together.

## Rollback

Revert the schema, validator binding, fixtures, tests, workflow wiring, and
documentation as one dependency-closed change. No runtime or published object
requires restoration because this lane performs no live or lifecycle writes.
