<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-policy-readme
title: tests/policy/README.md — Policy and Doctrine Boundary Tests
type: README
version: v0.6
status: draft; repository-grounded; authored; non-authoritative
owner: "@bartytime4life — CONFIRMED CODEOWNERS review route; independent policy, QA, doctrine, and release stewardship remain NEEDS VERIFICATION"
created: 2026-07-06
updated: 2026-08-31
supersedes: v0.5 documentation at the same path; no test, script, policy, workflow, receipt, review, release, or publication state is superseded
policy_label: public; tests; policy-boundary; doctrine-preflight; no-network-default; fail-closed
owning_root: tests/
responsibility: document executable policy and doctrine boundary tests, their implementation and workflow bindings, failure interpretation, maintenance obligations, and authority limits
truth_posture: CONFIRMED eighteen direct test modules and sixty-one source-defined tests at the pinned main snapshot / UNKNOWN complete collection, coverage, required-check status, production enforcement, independent stewardship, correction propagation, and operational rollback
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_target_prior_blob: 2eec647f0698e6dea0277dbf06d1ba94597b8265
direct_test_modules: 18
source_defined_tests: 61
related:
  - ../README.md
  - ../../policy/README.md
  - ../../policy/source/README.md
  - ../../docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../.github/workflows/policy-boundary-guards.yml
  - ../../.github/workflows/policy-test.yml
  - ../../.github/workflows/promotion-gate.yml
  - ../../Makefile
notes:
  - "v0.6 conforms the metadata envelope and re-pins unchanged policy-test and workflow evidence to current main."
  - "This file remains authored Markdown at its canonical same-path location; it is not generated or mirrored."
  - "Source-defined counts are static source inventory, not a pytest collection report or current pass result."
[/KFM_META_BLOCK_V2] -->

# `tests/policy/` — Policy and Doctrine Boundary Tests

<a id="top"></a>

`tests/policy/` contains executable tests for two bounded responsibilities:

1. cross-cutting policy, governance, client, connector, and pipeline boundaries;
2. the repository's doctrine-artifact registry and preflight helpers.

It does not own policy meaning, activate a policy bundle, approve doctrine, admit a
source, promote lifecycle state, or authorize review, merge, release, deployment,
publication, correction, or rollback.

> [!IMPORTANT]
> A passing test is evidence for its named assertion at the tested revision. It
> is not a `PolicyDecision`, proof that rights or sensitivity review is complete,
> proof that production enforcement is active, or release authority.

## Status

At `main@5d835798e09a4dd14735779cb44206a8a3e8b2d3`, the lane contains
[`boundary_constants.py`](boundary_constants.py) and 18 direct `test_*.py`
modules with 61 source-defined test functions.

The preceding README described three direct test modules and a TODO-only generic
policy workflow. Both claims became stale:

- 15 doctrine-artifact and preflight modules now sit beside the three boundary
  modules;
- [the generic policy workflow](../../.github/workflows/policy-test.yml) now
  performs substantive readiness checks and recognizes one separately governed
  release-gate Rego test lane, although it still does not run the complete direct
  Python lane or establish a repository-wide evaluator binding.

This README is an authored directory contract. It is neither generated nor a
mirror of Drive, Notion, test output, or workflow state.

## Authority and placement

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
makes [Directory Rules](../../docs/doctrine/directory-rules.md) the writable
human placement authority. The canonical [`tests/` root contract](../README.md)
places authored executable conformance evidence under `tests/` and keeps it
subordinate to the roots that own meaning and state.

| Responsibility | Authority home | Role of this lane |
|---|---|---|
| Policy meaning and rules | [`policy/`](../../policy/README.md) | Exercise bounded rules or readiness; never define or activate them. |
| Contract meaning | [`contracts/`](../../contracts/README.md) | Assert against accepted semantics; never replace them. |
| Machine shape | [`schemas/`](../../schemas/README.md) | Validate inputs and outputs; never become schema authority. |
| Doctrine and placement | [`docs/doctrine/`](../../docs/doctrine/README.md) and accepted ADRs | Test machine projections and references; never adopt doctrine. |
| Registers | [`control_plane/`](../../control_plane/README.md) | Exercise selected structure and alignment; never create governance status. |
| Operational helpers | [`scripts/maintenance/`](../../scripts/maintenance/README.md) | Test local subprocess behavior and structured output. |
| Validation implementation | [`tools/validators/`](../../tools/validators/README.md) | Exercise validators; never duplicate their implementation here. |
| Release decisions | [`release/`](../../release/README.md) | Prove bounded denial/readiness conditions; never approve or publish. |

The same-path documentation update creates no new root or authority relationship.
Current CODEOWNERS routes `/tests/` review to `@bartytime4life`; independent QA,
policy, doctrine, rights/sensitivity, and release stewardship is not established by
that routing rule.

## Executable inventory

The counts below are defined by Python source at the pinned revision. They are not
pytest collection or execution results.

### Boundary modules

| Module | Source-defined tests | Bounded responsibility |
|---|---:|---|
| [`test_control_plane_register_meta_contract.py`](test_control_plane_register_meta_contract.py) | 9 | Required register presence plus selected metadata, date, status, owner, doctrine-reference, and object-family schema/validator checks. |
| [`test_explorer_web_adapter_boundary.py`](test_explorer_web_adapter_boundary.py) | 2 | Static renderer-import placement and forbidden internal-store path literals in Explorer Web source. |
| [`test_pipeline_connector_non_publisher.py`](test_pipeline_connector_non_publisher.py) | 2 | Selected connector output allowlists and bounded connector/pipeline publication-target canaries. |

These 13 tests are structural or static. They do not prove complete YAML meaning,
runtime filesystem or network confinement, deployed client behavior, or publication
safety.

### Doctrine-artifact and preflight modules

| Module | Tests | Primary implementation under test |
|---|---:|---|
| [`test_doctrine_artifact_presence_input.py`](test_doctrine_artifact_presence_input.py) | 1 | Required-artifact check output rendered as a presence map. |
| [`test_doctrine_artifact_provenance.py`](test_doctrine_artifact_provenance.py) | 2 | Provenance checker rejection and receipt output. |
| [`test_doctrine_artifact_provenance_snapshots.py`](test_doctrine_artifact_provenance_snapshots.py) | 3 | Stored checker/synchronizer output snapshots. |
| [`test_doctrine_artifact_registry_status_alignment.py`](test_doctrine_artifact_registry_status_alignment.py) | 1 | Registry `present` status mismatch failure. |
| [`test_doctrine_artifact_registry_validation.py`](test_doctrine_artifact_registry_validation.py) | 7 | Duplicate, malformed, empty, invalid-status, comment, and missing-file registry cases. |
| [`test_doctrine_artifact_required.py`](test_doctrine_artifact_required.py) | 3 | Required Rego source presence, fail-closed missing-artifact posture, and receipt output. |
| [`test_doctrine_artifact_test_bundle.py`](test_doctrine_artifact_test_bundle.py) | 1 | Focused shell test-bundle orchestration. |
| [`test_doctrine_registry_alignment.py`](test_doctrine_registry_alignment.py) | 2 | Required-artifact and provenance registry filename alignment. |
| [`test_enforce_doctrine_preflight_gates.py`](test_enforce_doctrine_preflight_gates.py) | 3 | Strict wrapper failure propagation and argument forwarding. |
| [`test_normalized_summary_consumer_readiness.py`](test_normalized_summary_consumer_readiness.py) | 3 | Consumer-readiness registry validation and all-validated mode. |
| [`test_preflight_summary_consistency.py`](test_preflight_summary_consistency.py) | 5 | Legacy/normalized summary consistency and normalized-only behavior. |
| [`test_preflight_summary_schema_contract.py`](test_preflight_summary_schema_contract.py) | 2 | Fail/error summaries against the Draft 2020-12 summary schema. |
| [`test_run_doctrine_artifact_preflight.py`](test_run_doctrine_artifact_preflight.py) | 8 | Orchestrator outputs, strict gates, stable names, error handling, provenance, normalized-only output, and consumer readiness. |
| [`test_sync_doctrine_artifact_provenance_status.py`](test_sync_doctrine_artifact_provenance_status.py) | 3 | No-change/write behavior and synchronization receipt output. |
| [`test_sync_doctrine_artifact_registry_status.py`](test_sync_doctrine_artifact_registry_status.py) | 4 | Present-state synchronization, dry-run, fail-on-change, and missing-registry behavior. |

These 48 tests primarily exercise local files, temporary directories, subprocess
exit codes, and structured JSON. Several tests intentionally prove a hold or failure
is visible. A green test in that family does not mean a doctrine artifact is present,
authoritative, rights-cleared, reviewed, adopted, or publishable.

## Implementation bindings

The doctrine/preflight tests call or inspect the following repository surfaces:

- `scripts/maintenance/check_required_doctrine_artifacts.py`
- `scripts/maintenance/render_doctrine_presence_input.py`
- `scripts/maintenance/check_doctrine_artifact_provenance.py`
- `scripts/maintenance/sync_doctrine_artifact_provenance_status.py`
- `scripts/maintenance/sync_doctrine_artifact_registry_status.py`
- `scripts/maintenance/check_doctrine_registry_alignment.py`
- `scripts/maintenance/check_normalized_summary_consumer_readiness.py`
- `scripts/maintenance/run_doctrine_artifact_preflight.py`
- `scripts/maintenance/enforce_doctrine_preflight_gates.sh`
- `scripts/maintenance/run_doctrine_artifact_test_suite.sh`
- `tools/validators/source/validate_doctrine_preflight_summary_consistency.py`
- `schemas/contracts/v1/source/doctrine_artifact_preflight_summary.schema.json`
- `policy/source/doctrine_artifact_required.rego`

The current operator interpretation and known placement conflict for preflight
output are documented in the
[Doctrine Artifact Preflight runbook](../../docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md).
That runbook is guidance; executable files and exact-head results remain the
implementation evidence.

## Run the tests

From the repository root with the test dependencies declared in
[`pyproject.toml`](../../pyproject.toml):

```bash
python -m pytest -q tests/policy
```

Focused commands:

```bash
python -m pytest -q \
  tests/policy/test_control_plane_register_meta_contract.py \
  tests/policy/test_explorer_web_adapter_boundary.py \
  tests/policy/test_pipeline_connector_non_publisher.py

python -m pytest -q tests/policy/test_doctrine_artifact*.py

python -m pytest -q \
  tests/policy/test_doctrine_registry_alignment.py \
  tests/policy/test_enforce_doctrine_preflight_gates.py \
  tests/policy/test_normalized_summary_consumer_readiness.py \
  tests/policy/test_preflight_summary_consistency.py \
  tests/policy/test_preflight_summary_schema_contract.py \
  tests/policy/test_run_doctrine_artifact_preflight.py \
  tests/policy/test_sync_doctrine_artifact_provenance_status.py \
  tests/policy/test_sync_doctrine_artifact_registry_status.py
```

`make boundary-guards` and `make boundary-guards-ci` are narrower. They run the
three boundary modules plus
`apps/governed-api/tests/test_boundary_guards.py`; they do not collect all of
`tests/policy/`. `make test` and `make validate` also do not establish complete
collection of this lane.

## Hosted workflow coverage

| Workflow | Direct binding at the pinned revision | Limit |
|---|---|---|
| [`policy-boundary-guards.yml`](../../.github/workflows/policy-boundary-guards.yml) | Runs the three boundary modules plus the governed-API companion through `make boundary-guards-ci`; its reviewed four-module inventory is 18 tests. | Does not collect the 15 doctrine/preflight modules or evaluate a policy bundle. |
| [`promotion-gate.yml`](../../.github/workflows/promotion-gate.yml) | Directly runs `test_doctrine_artifact_required.py` before promotion-readiness checks. | A pass proves the known missing-artifact condition fails closed; it does not satisfy the prerequisite. |
| [`policy-test.yml`](../../.github/workflows/policy-test.yml) | Performs policy-readiness and PolicyDecision-fixture drift checks and recognizes a separately governed release-gate Rego lane. | It does not run `python -m pytest tests/policy`, establish a repository-wide bundle/evaluator, or emit a PolicyDecision. |

Direct hosted collection is not established for the remaining 14 doctrine/preflight
modules. Workflow presence, PR success, and source-defined test counts are not a
substitute for collection evidence. Required-check and branch-protection status are
also separate and remain `UNKNOWN` here.

## Failure interpretation

1. Re-run the smallest failing module at the exact revision.
2. Classify the failure before changing code or data:
   - test regression;
   - implementation or fixture drift;
   - intentional fail-closed hold;
   - dependency/setup failure before collection;
   - stale documentation;
   - inherited or unrelated hosted failure.
3. Inspect structured stdout, stderr, temporary inputs, and snapshots without
   replacing a real negative outcome with a placeholder `present` or `verified`
   status.
4. Correct the authority-owning file. Do not weaken a test merely to obtain green
   output.
5. Re-run the focused command and any directly bound workflow.

The current doctrine-artifact registries and source/provenance claims must not be
promoted based on fixture success. Preserve rights, sensitivity, privacy,
sovereignty, harmful-precision, provenance, correction, and rollback review when
real artifacts or source records enter scope.

## Maintenance

When adding, removing, renaming, or moving a direct module:

- update the inventory and source-defined count here;
- update imports, fixtures, scripts, schemas, and runbook links that bind it;
- update the exact Make target or workflow if hosted collection is intended;
- make zero-file or zero-test collection fail rather than pass silently;
- keep tests local and deterministic unless a separately reviewed network profile
  explicitly requires otherwise;
- use synthetic, minimized, public-safe fixtures;
- document what the new assertion cannot prove;
- preserve correction and rollback behavior for generated receipts or snapshots.

## Known gaps

- No repository-native Make target composes all 18 direct modules.
- Direct hosted collection is unverified for 14 doctrine/preflight modules.
- Complete collected-case count, runtime, coverage, mutation score, and flake rate
  are not established by this source inventory.
- Required-check status and accountable independent stewardship are unverified.
- The repository-wide policy bundle, evaluator selection, runtime binding, reason
  codes, obligations, and normalization contract are not established by this lane.
- Tests do not prove rights clearance, sensitivity decisions, doctrine adoption,
  source admission, review, release, deployment, or publication.

## Documentation rollback

Before merge, close the draft pull request to abandon this documentation change.
After merge, use a focused reviewed revert of this file. Do not rewrite shared
history, remove test coverage, change registry state, or treat documentation
rollback as policy, review, release, or publication rollback.

[Back to top](#top)
