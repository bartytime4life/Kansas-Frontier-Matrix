<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-runtime-proof-readme
title: tests/runtime_proof/ — Runtime-Proof Test Inventory and Evidence Boundary
type: readme; directory-readme; test-inventory; runtime-proof-boundary
version: v0.5
status: draft; canonical-directory-readme; executable-partial; non-authoritative
policy_label: public-doc; restricted-review-when-sensitive-domain-or-private-runtime-state-is-in-scope
created: 2026-07-07
updated: 2026-08-30
current_path: tests/runtime_proof/README.md
authoring: authored repository documentation; not generated or mirrored
review_route: "@bartytime4life via .github/CODEOWNERS; routing is not evidence of review or stewardship"
truth_posture: CONFIRMED inventory, commands, workflow bindings, and source-level boundaries at the pinned snapshot / UNKNOWN required-check status, complete runtime composition, production consumers, deployed behavior, and operational stewardship
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1ea6593ede80d5ce10f561c7eec72135d6ccf806
  prior_blob: 23a259513a25ec43922f4767de8d5c05c8302ee6
related:
  - ../README.md
  - ./domains/README.md
  - ./domains/soil/soil_moisture/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../.github/workflows/focus-mock-test.yml
  - ../../.github/workflows/soil-moisture-runtime-proof.yml
tags: [kfm, tests, runtime-proof, finite-outcomes, soil-moisture, no-network, evidence-boundary]
notes:
  - "v0.5 replaces a stale proposal-heavy inventory with the executable suite and workflow bindings present on the pinned main snapshot."
  - "Passing tests establish bounded repository behavior only; they do not establish evidence truth, policy approval, source admission, release, deployment, publication, or operational health."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/runtime_proof/` — Runtime-Proof Test Inventory and Evidence Boundary

This directory contains bounded tests for finite runtime envelopes and one
synthetic soil-moisture mapping profile. It is an enforceability test lane, not
runtime implementation or authority to admit evidence, activate a source,
approve policy, release, deploy, or publish.

At the pinned `main` snapshot, the lane contains **three test modules with 20
source-defined tests**. Two supporting modules construct and report the
soil-moisture test profile. The previous README omitted that executable domain
lane and incorrectly described the repository as lacking a dedicated
runtime-proof workflow.

## Current inventory

| Path | Tests | Confirmed responsibility |
|---|---:|---|
| [`test_envelope_finite_outcomes.py`](./test_envelope_finite_outcomes.py) | 6 | Standard-library checks for the closed four-outcome `RuntimeResponseEnvelope` shape, compatibility aliasing, valid and invalid fixtures, precision findings, and canonical validator wiring. |
| [`test_mock_adapter_finite_outcomes.py`](./test_mock_adapter_finite_outcomes.py) | 7 | Deterministic fixture-backed `MockAdapter` selection, copy isolation, complete outcome configuration, bounded lookup failures, and a source-level no-I/O import guard. |
| [`domains/soil/soil_moisture/test_runtime_mapper.py`](./domains/soil/soil_moisture/test_runtime_mapper.py) | 7 | Schema-valid, deterministic fixture-only mapping to `ABSTAIN`, `DENY`, or `ERROR`, plus safe report generation. The profile intentionally never returns `ANSWER`. |
| [`domains/soil/soil_moisture/runtime_mapper.py`](./domains/soil/soil_moisture/runtime_mapper.py) | — | Test-only mapper using the repository envelope candidate builder and soil-moisture validator. |
| [`domains/soil/soil_moisture/emit_runtime_proof_report.py`](./domains/soil/soil_moisture/emit_runtime_proof_report.py) | — | Emits deterministic reviewer-only JSON containing expected outcomes and closed outward envelopes. |
| [`domains/soil/soil_moisture/README.md`](./domains/soil/soil_moisture/README.md) | — | Focused commands and safety boundary for the soil-moisture profile. |
| [`domains/README.md`](./domains/README.md) | — | Domain placement and migration index. |
| [`domains/roads-rail-trade/README.md`](./domains/roads-rail-trade/README.md) | — | Documentation-only domain child; no executable module is present in that directory. |

`__init__.py`, `conftest.py`, and `.gitkeep` files support import or directory
structure and are not test modules.

## Run the tests

Run the two dependency-free shared modules from the repository root:

```bash
python -m unittest \
  tests.runtime_proof.test_mock_adapter_finite_outcomes \
  tests.runtime_proof.test_envelope_finite_outcomes \
  --verbose
```

Run the dependency-backed soil-moisture proof and its direct package/report
dependencies with the same command used by its workflow:

```bash
python -m pytest \
  tests/packages/envelopes/test_runtime_response_candidate.py \
  tests/runtime_proof/domains/soil/soil_moisture/test_runtime_mapper.py \
  tests/ci/test_render_runtime_proof_summary.py \
  -q --strict-config --strict-markers
```

For discovery during maintenance, collect the directory without executing it:

```bash
python -m pytest --collect-only tests/runtime_proof -q
```

The root [`Makefile`](../../Makefile) `test` target runs only `tests/schemas`
and `tests/contracts`; it does **not** collect this directory. There is no
directory-wide runtime-proof Make target at the pinned snapshot.

## Workflow bindings

| Workflow and job | Collected coverage | Trigger boundary |
|---|---|---|
| [`focus-mock-test.yml`](../../.github/workflows/focus-mock-test.yml), `finite-envelope-shape` | Both shared `unittest` modules, plus workflow-owned fixture and source checks | Runs on every pull request and pushes to `main`; it is not a complete runtime-proof gate. |
| [`soil-moisture-runtime-proof.yml`](../../.github/workflows/soil-moisture-runtime-proof.yml), `validate-soil-moisture-runtime-proof` | Soil mapper tests plus the envelope-candidate and report-renderer dependencies; emits bounded QA artifacts and verifies the recorded authoring receipt | Path-scoped to the soil profile and named dependencies. The root `tests/runtime_proof/README.md` is not in its pull-request path filter. |

Other workflows whose names mention runtime or proof validate different
contracts, artifacts, or application surfaces. Their existence does not imply
collection of this directory.

Hosted workflow success proves only the commands executed at that exact commit.
This README does not establish that either job is a required check.

## What the suites prove

### Shared finite-outcome boundary

The two shared modules establish bounded behavior around the four schema
outcomes:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

They check fixture shape and deterministic adapter behavior without starting a
service. The standard-library shape suite intentionally does not import the
repository's `jsonschema` validator; complete JSON Schema behavior remains with
the schema and validator suites.

The adapter suite inspects its source import surface and exercises isolated
copies. That is useful no-I/O evidence for the adapter module, not proof that
the whole test process, dependency installation, or a deployed runtime cannot
access the network.

### Soil-moisture profile

The soil mapper consumes repository-local synthetic fixtures and validator
findings. Its current mapping is deliberately fail-closed:

| Input posture | Expected outcome |
|---|---|
| Validator-clean fixture marked fixture-only and not released | `ABSTAIN` |
| Missing evidence, source-descriptor, or run-receipt support | `ABSTAIN` |
| Semantic or public-safety validation finding | `DENY` |
| Non-object input | `ERROR` |

The tests validate the outward object against the closed
[`RuntimeResponseEnvelope` schema](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json),
check deterministic replay, and reject leakage of readings, station identifiers,
source/run references, proof material, catalog entries, promotion decisions,
release manifests, and publication objects.

The emitted JSON and rendered Markdown are temporary QA artifacts. They are not
canonical evidence, accepted receipts or proofs, policy decisions, release
records, publication records, or public API responses.

## Evidence and authority limits

A passing result may support a claim only about the assertions in the collected
tests. In particular:

- fixture validity is not real-world truth or source admission;
- an envelope-shaped object is not evidence resolution or policy evaluation;
- the soil test mapper is not a production route, source adapter, publisher, or
  public client;
- a stored authoring receipt is not live receipt acquisition or release
  approval;
- generated summaries and QA artifacts are not sovereign evidence;
- review, merge, release, deployment, promotion, and publication remain
  distinct states;
- workflow success is not proof of deployed behavior or operational health.

Public clients must continue to use governed interfaces or released public-safe
artifacts. Tests and fixtures must not read or publish canonical internal stores
as though test success authorized that access.

## Failure interpretation

| Failure | First place to investigate | Do not conclude |
|---|---|---|
| Shared envelope test | Runtime schema/fixture bytes, Focus compatibility alias, validator wiring, or the test's bounded shape logic | That production runtime behavior failed. |
| Mock adapter test | Scenario matrix, copy isolation, lookup handling, or adapter import surface | That evidence or policy execution failed. |
| Soil mapper test | Soil fixture, validator findings, envelope candidate builder, schema compatibility, or report safety | That a live soil source or deployed API failed. |
| Zero tests collected | Test path, imports, collection configuration, or workflow command | A green or intentionally empty runtime-proof lane. |
| Dependency installation fails | Repository dependency policy and bootstrap logs | That the substantive runtime-proof assertions ran. |
| Workflow skipped by path filters | Workflow trigger configuration | That the covered suite passed at the current commit. |

Record the exact tested commit and distinguish an introduced failure from an
inherited, unrelated, unavailable, skipped, or unknown result.

## Maintenance

When implementation changes, update this README in the same documentation
slice if any of these facts change:

1. executable module or source-defined test inventory;
2. focused command or dependency set;
3. workflow name, job, command, or path filter;
4. supported finite outcomes or failure mapping;
5. fixture, schema, validator, mapper, or report boundary;
6. domain placement under the accepted Directory Rules decision;
7. authority, sensitivity, leakage, correction, or rollback limitation.

Use accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the canonical [Directory Rules](../../docs/doctrine/directory-rules.md) for
placement decisions. The current domain index records competing domain-first
and capability-first layouts; do not create or move a domain runtime-proof lane
by README assertion alone.

CODEOWNERS routes `/tests/` review requests to `@bartytime4life`. That routing
does not prove review, independent approval, accountable operational
stewardship, or required-check status.

Before merging a documentation change, inspect the complete base-to-head diff,
verify every referenced path and command, and preserve the prior blob shown in
the metadata as the rollback point. Before merge, rollback is closing the pull
request; after merge, use a normal revert rather than rewriting shared history.

## Unresolved gaps

- Complete evidence-resolution, policy, freshness, correction, release, client,
  leakage, and rollback composition is not covered by these three modules.
- The shared workflow covers bounded shape and adapter behavior, not the soil
  mapper or a directory-wide runtime-proof matrix.
- The soil workflow does not trigger when only this root README changes.
- `make test` and `make validate` do not collect this directory.
- Required-check status and accountable operational stewardship are unknown.
- Production consumers, routes, deployed controls, and operational health are
  not established by repository tests.
- Domain runtime-proof placement remains governed by the existing migration
  hold; this README does not choose a winning layout.

[Back to top](#top)
