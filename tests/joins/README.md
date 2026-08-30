<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://tests/joins/readme
title: Join Assessment Test Lane
type: test-lane-readme
version: v0.2.0
status: draft; repository-grounded; synthetic-only; no-network; two-executable-modules-confirmed; 20-source-defined-tests
owners: @bartytime4life — CONFIRMED CODEOWNERS review route; accountable join, validation, sensitivity, and historical-context stewardship UNKNOWN
created: 2026-08-09
updated: 2026-08-30
policy_label: repository-facing; tests; joins; non-publisher
owning_root: tests/
responsibility: Document the bounded synthetic proof surface for generic cross-lane and historical-network proximity assessment helpers.
truth_posture: cite-or-abstain
evidence_base: 31f5ade589b9f20d87a59ce83be228e577f51cca
prior_blob: ec529c0701820da8a243a21529bf74f06cb28b78
[/KFM_META_BLOCK_V2] -->

# Join assessment test lane

`tests/joins/` contains two executable modules with 20 source-defined tests
over 39 synthetic fixture cases. One module assesses generic cross-lane join
candidates; the other assesses bounded historical-network proximity candidates.

Passing this lane shows only that the repository helpers behave deterministically
against their stored contracts, schemas, and fixtures. It does not establish a
real-world relationship, identify a person, grant authority, approve a source,
resolve rights or sensitivity, release an artifact, or publish a join.

## Inventory

| Test module | Helper under test | Fixture family | Source-defined tests |
| --- | --- | --- | ---: |
| [`test_join_candidates.py`](test_join_candidates.py) | [`tools/joins/join_candidates.py`](../../tools/joins/join_candidates.py) | [`cross_lane_join_assessment`](../../fixtures/contracts/v1/joins/cross_lane_join_assessment/cases.json) | 10 |
| [`test_historical_network_proximity.py`](test_historical_network_proximity.py) | [`tools/joins/historical_network_proximity.py`](../../tools/joins/historical_network_proximity.py) | [`historical_network_proximity_assessment`](../../fixtures/contracts/v1/joins/historical_network_proximity_assessment/cases.json) | 10 |

The counts above describe test functions or `unittest` methods in the two source
modules. They are not a claim about every case collected by a broader repository
test command.

## Generic cross-lane candidate coverage

`test_join_candidates.py` checks the generic helper against the
[cross-lane join contract](../../contracts/joins/cross_lane_join_assessment.md),
[schema](../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json),
and 19-case fixture matrix:

- 13 cases expect contract validation `PASS` and six expect `FAIL`;
- exact-key candidates use parameterized, in-memory SQLite;
- spatial-temporal examples cover bounded match and mismatch behavior;
- missing evidence, source-role conflict, restricted exact geometry,
  living-person risk, and dependency failure remain non-allow outcomes;
- SQL metacharacters are treated as values;
- rule, source-role, sensitivity, and decision details remain inspectable;
- decision, identity, duplicate-key, schema, and interval tampering fail closed;
- symlinked fixture inputs are denied without echoing fixture values; and
- the helper source contains no known network client or file-write token.

The finite helper outcomes are `ALLOW`, `ABSTAIN`, `DENY`, and `ERROR`.
`ALLOW` authorizes only candidate-report emission. All publisher-effect fields
remain false.

## Historical-network proximity coverage

`test_historical_network_proximity.py` checks the historical helper against the
[historical-network contract](../../contracts/joins/historical_network_proximity_assessment.md),
[schema](../../schemas/contracts/v1/joins/historical_network_proximity_assessment.schema.json),
and 20-case fixture matrix:

- seven cases expect `PASS`, ten expect `DENY`, and three expect `ERROR`;
- the schema is closed and carries `PROPOSED_INACTIVE` status, `NONE` authority,
  and false network, geometry, real-location, and release flags;
- candidate, no-overlap, ambiguous, unsupported, and context-only
  interpretations remain distinct;
- temporal overlap is half-open, with per-side and combined uncertainty kept
  separate;
- distance, time, source-role, approximation, and uncertainty mismatches retain
  exact negative reason codes;
- outputs do not assert a relationship, identity, or authority;
- the profile hash is deterministic and changes with governed inputs;
- duplicate keys, non-finite values, and symlinked fixtures fail closed while
  mocked socket access is denied; and
- the helper source contains no known network or file-write token.

These checks describe a candidate-assessment envelope only. They do not activate
the proposed contract or turn proximity into evidence of association.

## Run locally

From the repository root, run the generic lane exactly as its hosted workflow:

```bash
python tools/joins/join_candidates.py --fixtures
python -m pytest tests/joins/test_join_candidates.py -q --strict-config --strict-markers
```

Run the historical-network lane exactly as its hosted workflow:

```bash
python -m py_compile \
  tools/joins/historical_network_proximity.py \
  tests/joins/test_historical_network_proximity.py
python tests/joins/test_historical_network_proximity.py --verbose
python tools/joins/historical_network_proximity.py --fixtures
```

The repository `Makefile` has no join-specific target. Use the focused commands
above when changing this directory or either helper.

## Hosted workflow coverage

| Workflow | Direct test command | README edit triggers it? |
| --- | --- | --- |
| [`cross-lane-join-assessment`](../../.github/workflows/cross-lane-join-assessment.yml) | `pytest tests/joins/test_join_candidates.py` plus the generic fixture runner | Yes; its path filter includes `tests/joins/**` |
| [`historical-network-proximity-assessment`](../../.github/workflows/historical-network-proximity-assessment.yml) | `python tests/joins/test_historical_network_proximity.py --verbose` plus compile and fixture checks | No; its path filter names the historical test, helper, fixture, schema, contract, and receipt but not this README |

Both workflows use Python 3.11, read-only repository permissions, and
`KFM_NO_NETWORK=1`. Each also validates a stored generated receipt. A successful
receipt check confirms agreement with the checked-in expected artifact; it is not
live acquisition, production execution, release evidence, or publication.

Because this README does not trigger the historical workflow, a documentation-only
change here can receive direct hosted evidence for the generic lane while leaving
the historical lane uncollected. That path-filter gap is implementation work
outside this Markdown change.

## Safety and authority boundary

| Evidence from this lane | What it does not establish |
| --- | --- |
| Synthetic fixtures parse and produce expected finite outcomes | Truth of any real-world link, identity, event, or location |
| Helpers remain deterministic for the covered inputs | Complete semantic coverage or production parity |
| Network and publisher effects are absent from the checked helper surface | Runtime confinement outside the tested process |
| Schemas, contracts, and stored receipts agree for covered cases | Adoption, activation, approval, release, or publication |
| Fail-closed cases reject covered malformed or unsafe inputs | Rights clearance, consent, sovereignty, privacy, or harmful-precision resolution |

Evidence outranks the generated candidate language. Downstream evidence,
provenance, rights, sensitivity, policy, correction, review, and release controls
remain required before any candidate can affect a governed artifact.

## Interpreting failures

1. Treat a fixture-runner failure as a contract, schema, fixture, or helper
   disagreement. Do not rewrite the expected outcome until the governing evidence
   and intended boundary are confirmed.
2. Treat a test failure as a regression in the named invariant. Inspect the
   smallest relevant helper, contract, schema, and fixture case together.
3. Treat an unexpected `ALLOW` or `PASS` as safety-significant. Hold downstream
   use and verify evidence, role, sensitivity, identity, temporal, and uncertainty
   inputs.
4. Treat a workflow that did not run as unavailable evidence, not a pass.
5. Preserve synthetic values in failures and reviews; do not substitute real
   people, precise locations, or restricted source material.

## Maintenance

When either join assessment changes:

- keep the test-module, helper, contract, schema, fixture, and workflow links in
  this inventory synchronized;
- update counts only from current source and fixture evidence;
- preserve finite outcomes, non-publisher effects, and fail-closed behavior;
- add synthetic cases for new branches without introducing real identities or
  harmful precision; and
- record workflow collection gaps explicitly rather than implying hosted
  coverage.

Current unresolved gaps are accountable join stewardship beyond the confirmed
CODEOWNERS review route, required-check status, complete cross-lane coverage,
production confinement, correction propagation, operational rollback, and the
historical workflow's parent-README path filter.

## Rollback

This document changes no helper, contract, schema, fixture, workflow, receipt, or
runtime behavior. Before merge, rollback is closing the pull request or reverting
its documentation commit.
