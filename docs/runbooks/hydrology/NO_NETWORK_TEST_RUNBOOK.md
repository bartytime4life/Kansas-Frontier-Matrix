<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/hydrology/no-network-test
title: Hydrology No-Network Test Runbook
type: runbook
version: v1.2.0
prior_version: v1.1.0
prior_state: repository-grounded procedure with test-local guards but no shared startup enforcement across the accepted Python command group
status: DRAFT_REPOSITORY_GROUNDED; BOUNDED_PYTHON_PROCESS_EGRESS_DENIAL_EXECUTABLE; RUNNER_WIDE_AND_NON_PYTHON_EGRESS_DENIAL_HELD; BROADER_HYDROLOGY_AUTHORITY_HELD; NOT_FOR_LIFE_SAFETY
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Hydrology, QA, evidence, source, policy, safety, proof, release, and operations assignments"
created: 2026-05-12
updated: 2026-08-28
policy_label: repository-facing; validation-sensitive; fail-closed
current_path: docs/runbooks/hydrology/NO_NETWORK_TEST_RUNBOOK.md
owning_root: docs/
responsibility: Human procedure for reproducing and interpreting the Hydrology lane's current bounded Python-process no-network test behavior without claiming runner-wide or non-Python isolation, live-source truth, evidence closure, policy approval, proof, release, deployment, publication, or life-safety authority.
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source and evidence authority, executable validators and tests, workflow definitions, policy, review, lifecycle, proof, release, correction, rollback, and official authorities
current_disposition: BOUNDED_PYTHON_PROCESS_EGRESS_DENIAL_AVAILABLE / RUNNER_WIDE_NON_PYTHON_EGRESS_AND_BROADER_TRUST_SPINE_HELD
reason_codes:
  - HYD_NO_NETWORK_EXACT_SHA_REQUIRED
  - HYD_NO_NETWORK_PYTHON_PROCESS_GUARD_ONLY
  - HYD_NO_NETWORK_RUNNER_EGRESS_NEEDS_VERIFICATION
  - HYD_NO_NETWORK_FIXTURE_PROFILE_ONLY
  - HYD_NO_NETWORK_LIVE_SOURCE_AND_LIFECYCLE_HELD
  - HYD_NO_NETWORK_PROOF_RELEASE_AND_PUBLICATION_HELD
  - HYD_NO_NETWORK_LIFE_SAFETY_AUTHORITY_DENIED
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1f0f1cff72abd610e9e80c5c894987eb7b9d568b
  target_prior_blob: 1a2a1480b7f2fe3d52aabd815395ac1b8fb97395
  lane_readme_blob: 02e9afe9558eea339613077d01b74bd76a726e4e
  validation_runbook_blob: 53dd6e7be472d514106475ffe004fc6f98413af6
  domain_workflow_blob: 36a0287be04639cb75dc77ae2c274fee626f6a00
  tests_parent_readme_blob: 8af73abbe4874578473161cf9368699733d46ddb
  validators_parent_readme_blob: b3fea3126e01d95996f8234f8670a6896992817a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - docs/runbooks/hydrology/README.md
  - docs/runbooks/hydrology/VALIDATION.md
  - docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md
  - docs/domains/hydrology/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - .github/workflows/domain-hydrology.yml
  - tests/domains/hydrology/README.md
  - tests/domains/hydrology/test_no_network_proof.py
  - tools/ci/kfm_no_network/README.md
  - tools/ci/kfm_no_network/sitecustomize.py
  - tools/validators/domains/hydrology/README.md
  - fixtures/domains/hydrology/README.md
  - data/registry/sources/hydrology/README.md
  - data/proofs/hydrology/README.md
  - release/candidates/hydrology/README.md
non_effects:
  - does_not_contact_live_sources
  - does_not_establish_runner_wide_egress_denial
  - does_not_establish_non_python_egress_denial
  - does_not_read_credentials
  - does_not_activate_or_admit_sources
  - does_not_write_raw_work_quarantine_processed_catalog_triplet_or_published_state
  - does_not_resolve_real_evidence_refs
  - does_not_create_evidence_or_proof
  - does_not_approve_policy_or_review
  - does_not_promote_release_deploy_or_publish
  - does_not_issue_life_safety_guidance
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology No-Network Test Runbook

Repository-grounded procedure for reproducing and interpreting the Hydrology
lane's current deterministic, fixture-only checks at an exact repository
revision. The current proof is bounded to Python processes in the accepted
validation step: they load one reviewed startup guard before application
imports, and a fresh-interpreter negative test exercises the named denial paths.
It is not evidence of a runner-wide or non-Python network sandbox.

> [!WARNING]
> KFM is not a flood-warning, emergency-response, navigation, engineering,
> insurance, dam-operation, water-rights, legal, or regulatory authority. FEMA
> NFHL is regulatory flood-hazard context, not observed inundation. Use the
> responsible official source for current conditions and life-safety decisions.

> [!IMPORTANT]
> `KFM_NO_NETWORK=1` alone records posture and does not block access. The
> Hydrology validation step now combines it with the reviewed
> `tools/ci/kfm_no_network/sitecustomize.py` startup path, so every Python
> process in that step installs the same guard before application imports. The
> workflow still does not establish operating-system, container, namespace,
> non-Python, dependency-install, or job-wide egress denial.

**Quick navigation:** [Scope](#1-purpose-authority-and-scope) ·
[Current evidence](#2-current-no-network-evidence) ·
[Preflight](#3-preflight) ·
[Procedure](#4-execution-procedure) ·
[Interpretation](#5-interpretation) ·
[Failures](#6-failure-classification-and-stop-conditions) ·
[Record](#7-result-record) ·
[Maintenance](#8-maintenance-and-documentation-rollback)

## 1. Purpose, authority, and scope

Use this runbook to answer three bounded questions:

1. Did the named Hydrology fixture profiles execute without permitted network
   access at the exact revision under review?
2. Did their valid and expected-invalid cases preserve the recorded polarity?
3. What does the result prove, and which broader claims remain held?

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
and the adopted [Directory Rules](../../doctrine/directory-rules.md) place human
procedures under `docs/runbooks/`. Tests remain under `tests/`, validators under
`tools/validators/`, fixtures under `fixtures/`, semantic meaning under
`contracts/`, machine shape under `schemas/`, policy under `policy/`, source
admission under governed source surfaces, proof under proof-bearing stores, and
release decisions under `release/`.

This file explains current executable evidence. It does not create or amend a
contract, schema, source descriptor, activation decision, validator, policy,
workflow, EvidenceBundle, proof, PromotionDecision, ReleaseManifest,
CorrectionNotice, rollback object, deployment, or publication state.

### In scope

- The bounded no-network commands in the current `domain-hydrology` workflow.
- Synthetic or captured local fixtures named by those commands.
- Startup-time IPv4/IPv6 socket connection, DNS, `urllib` URL-open, and
  datagram-send denial for every Python process in the bounded validation step.
- Positive and expected-negative fixture polarity.
- Exact-SHA result identity and truthful failure attribution.

### Out of scope

- Live USGS, WBD, NHDPlus, FEMA, NOAA, NRCS, state, local, tile, object-store,
  catalog, or other remote requests.
- Credentials, source activation, source admission, or endpoint authorization.
- Runner-wide firewall, namespace, container, or operating-system egress proof.
- Writes to `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, or
  `PUBLISHED`.
- Current hydrologic truth, real EvidenceRef resolution, EvidenceBundle closure,
  policy approval, proof production, promotion, release, deployment,
  publication, or public-use authority.

[Back to top](#top)

## 2. Current no-network evidence

The current [Hydrology workflow](../../../.github/workflows/domain-hydrology.yml)
sets `KFM_NO_NETWORK=1` and runs a bounded group of repository modules and
validators. The workflow also inventories Hydrology tests and validators so a
new substantive file cannot silently enter the accepted set.

| Surface | Current evidence | Bounded conclusion | Not established |
|---|---|---|---|
| `test_no_network_proof.py` and `tools/ci/kfm_no_network/sitecustomize.py` | Fresh Python interpreters require explicit activation and exercise IPv4/IPv6 connect, connect-ex, connection creation, DNS, datagram-send, and `urllib` URL-open paths | Shared startup enforcement for Python processes in the bounded validation step | Runner-wide, non-Python, dependency-install, operating-system, container, or namespace isolation |
| `test_hydrology_smoke.py` | Autouse fixture patches socket connect, connection creation, DNS resolution, and `urllib.request.urlopen`; a negative assertion exercises the guard | Process-level guard and EvidenceBundle alias fixture polarity | Runner-wide egress denial, evidence resolution, or evidence authenticity |
| `test_aquifer_observation.py` and `test_aquifer_context_link.py` | Process-level socket/DNS/URL guards plus valid/invalid local schema fixtures | Closed local shapes, fixture polarity, optional links, and responsibility separation | Endpoint resolution, aquifer membership, real observations, or source validity |
| `test_public_safe_flow_fixture.py` | Process-level network patches plus a frozen valid fixture and a known-invalid role/location/time/governance-collapse fixture | Bounded FlowObservation shape, limitations, and rejection behavior | A real gauge observation, warning, policy, proof, or release |
| `test_nhdplus_hr_ambiguity.py` | Network dependency denial plus eight synthetic crosswalk fixtures | Version-bound waterbody crosswalk identity and finite ambiguity behavior | Live NHDPlus rows, flowline/reach/HUC identity closure, or source admission |
| `test_adaptive_threshold_proposal.py` | Validator authority output states no network fetch; the test preserves finite proposal outcomes | Deterministic review-routing profile without threshold mutation | Drought extent, percentile computation, threshold computation, or event calling |
| `test_hydro_identity_bridge.py` | Source scan denies network-client imports; fixtures preserve current and legacy identity families | Deterministic bridge and abstention/deny behavior | Geometry comparison, source activation, real identity resolution, or release |
| `test_streamflow_qc_context_assessment.py` | Test replaces `socket.socket` during validator execution | Fixture-only QC context routing without a network call | Percentile computation, sensor invalidation, hydrologic event declaration, or policy decision |
| `test_environmental_observation_boundaries.py` | Local cross-domain ownership-isolation test | Soil, Atmosphere, and Hydrology observation roles stay separated for its fixtures | Scientific truth or complete cross-domain policy enforcement |

The workflow separately validates the local EvidenceBundle alias,
AquiferObservation, AquiferContextLink, public-safe FlowObservation, and
NHDPlus waterbody-crosswalk fixtures. It expects the known-invalid EvidenceBundle
and public-safe-flow fixtures to be rejected.

### What `KFM_NO_NETWORK=1` means here

The variable remains only a declared posture by itself. In the current bounded
Hydrology validation step, `PYTHONPATH` also names the reviewed startup-guard
directory. Python imports `sitecustomize.py` before application code, and the
guard activates only when `KFM_NO_NETWORK` is exactly `1`. The accepted negative
proof starts fresh interpreters so a test-local monkeypatch cannot satisfy the
claim accidentally.

A claim of runner-wide or non-Python isolation still needs separate current
evidence, such as a deny-all network namespace, firewall, or equivalent
job-level control plus failing probes for every relevant runtime. No such proof
is established here.

[Back to top](#top)

## 3. Preflight

Run from a clean checkout at the exact revision under review.

1. Record the full current `main` SHA, branch head SHA, merge base, workflow
   run URL, run attempt, and changed paths.
2. Confirm the checked-out SHA with `git rev-parse HEAD`. A pull-request merge
   ref is `MERGE_RESULT` evidence, not branch-head evidence.
3. Use the workflow's Python 3.11 toolchain and repository dependency installer:

   ```bash
   python tools/ci/install_python_ci.py project-test
   ```

4. Export the current deterministic posture:

   ```bash
   set -euo pipefail
   export KFM_NO_NETWORK=1
   export PYTHONDONTWRITEBYTECODE=1
   export PYTHONHASHSEED=0
   export PYTHONUNBUFFERED=1
   export PYTHONPATH="$PWD/tools/ci/kfm_no_network:$PWD"
   export TZ=UTC
   ```

5. Confirm the files named in section 4 exist and remain local fixtures,
   tests, validators, contracts, and schemas. Stop if a symlink, unexpected
   substantive module, live endpoint, credential requirement, or lifecycle
   write enters the selected surface.

Do not install dependencies during the test commands and describe the result
as wholly no-network. Dependency installation is a separate precondition and
may use network access unless satisfied from an already provisioned environment.

[Back to top](#top)

## 4. Execution procedure

### 4.1 Narrow guard and schema smoke

Run the smallest guard-bearing slice first:

```bash
set -euo pipefail
python -c 'import sitecustomize; assert sitecustomize.GUARD_ACTIVE'
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_no_network_proof.py \
  tests/domains/hydrology/test_hydrology_smoke.py \
  tests/domains/hydrology/test_aquifer_observation.py \
  tests/domains/hydrology/test_aquifer_context_link.py
```

Expected result: the selected modules pass their local shape, valid/invalid
polarity, and process-level network-guard assertions. Stop on any attempted
network access, accepted invalid fixture, missing fixture, or changed schema
binding.

### 4.2 Reproduce the current bounded domain group

```bash
set -euo pipefail
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_no_network_proof.py \
  tests/domains/hydrology/test_hydrology_smoke.py \
  tests/domains/hydrology/test_aquifer_observation.py \
  tests/domains/hydrology/test_aquifer_context_link.py \
  tests/domains/hydrology/test_nhdplus_hr_ambiguity.py \
  tests/domains/hydrology/test_adaptive_threshold_proposal.py \
  tests/domains/hydrology/test_hydro_identity_bridge.py \
  tests/domains/hydrology/test_streamflow_qc_context_assessment.py

python tests/domains/hydrology/test_public_safe_flow_fixture.py --verbose
python tests/cross_domain/test_environmental_observation_boundaries.py --verbose
```

These are the nine accepted Hydrology modules plus the cross-domain ownership
test currently invoked by `validate-hydrology`. Passing them does not establish
coverage for the proposal-only modules inventoried elsewhere under
`tests/domains/hydrology/`.

### 4.3 Reproduce explicit fixture polarity

```bash
set -euo pipefail
python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/valid/valid_1.json

if python tools/validators/domains/hydrology/validate_evidence_bundle.py \
  fixtures/domains/hydrology/evidence_bundle/invalid/invalid_1.json; then
  echo "ERROR: known-invalid Hydrology EvidenceBundle was accepted" >&2
  exit 1
fi

python tools/validators/domains/hydrology/validate_aquifer_observation.py \
  --fixtures

python tools/validators/domains/hydrology/validate_aquifer_context_link.py \
  --fixtures

python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/valid/public_safe_flow.json

if python tools/validators/domains/hydrology/validate_public_safe_flow_fixture.py \
  fixtures/domains/hydrology/public_safe_flow/invalid/role_location_time_governance_collapse.json; then
  echo "ERROR: known-invalid Hydrology flow fixture was accepted" >&2
  exit 1
fi

python tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py \
  --fixtures
```

The two `if` blocks succeed only when the validators reject their known-invalid
fixtures. Rejection is expected-negative evidence, not a skipped or failed test.

### 4.4 Hosted evidence

Use the exact-head `domain-hydrology` workflow result for hosted evidence. The
`validate-hydrology` job is the bounded executable lane. In the same workflow,
`build-proof-hydrology` and `publish-dry-run-hydrology` are readiness inspections
that deliberately record explicit holds; they are not successful proof or
release jobs.

[Back to top](#top)

## 5. Interpretation

| Observation | Classification | Supported statement |
|---|---|---|
| The fresh-interpreter negative proof passes and every section 4 Python command loads the active startup guard | `PASS` for bounded Python-process denial | The named Python-process egress paths were denied for the accepted command environment at that SHA |
| All section 4 commands pass at the recorded SHA | `PASS` for the named bounded profiles | The selected local fixtures, tests, validators, expected-negative polarity, startup guard, and test-local guards behaved as recorded at that SHA |
| A network guard raises before socket, DNS, or URL access | Expected denial | The selected process blocked that attempted call |
| A known-invalid fixture exits nonzero | Expected rejection | The validator preserved the named negative polarity |
| A known-invalid fixture exits zero | `FAIL` | The validator accepted an invalid profile; do not continue or weaken the fixture |
| Proof or release job records `WORKFLOW_SKIPPED_EXPLICIT` and its hold | `SKIPPED` with enforced hold | The unimplemented boundary stayed fail-closed |
| No exact-head hosted run exists | `NOT_RUN` | Hosted status is unknown; local evidence cannot be relabeled as hosted evidence |
| A runner-wide firewall or namespace was not tested | `NEEDS_VERIFICATION` | Do not claim job-wide egress denial |
| Evidence, source, time, rights, sensitivity, or identity is insufficient for a requested real-world claim | `ABSTAIN` or `HOLD` according to the owning interface | No current Hydrology answer or lifecycle transition is supported |

A passing result is not a source receipt, EvidenceBundle, ProofPack, policy
decision, PromotionDecision, ReleaseManifest, deployment receipt, publication
record, or current-condition observation.

[Back to top](#top)

## 6. Failure classification and stop conditions

For pull-request evidence, classify a failure only after comparing the exact
head, exact base, and changed paths:

- `INTRODUCED` — reproduced at the exact head and absent at the exact base, with
  a causal changed-path relationship.
- `INHERITED` — reproduced unchanged at the exact base or demonstrably outside
  the change's causal surface.
- `SKIPPED` — the workflow explicitly did not execute the held capability.
- `NOT_RUN` — no result exists for the exact revision or command.
- `UNKNOWN` — evidence is insufficient for attribution.

Stop immediately when any of the following occurs:

- a selected test or validator attempts an unguarded live request;
- credentials, sensitive payloads, exact protected locations, or production
  data are required;
- a known-invalid fixture is accepted;
- a source-role collapse treats regulatory, modeled, forecast, alert, or
  derived material as a direct observation;
- the tested SHA, fixture identity, command, or workflow inventory cannot be
  established;
- a test writes lifecycle, source, proof, release, or published state;
- a passing result is being used to justify source admission, promotion,
  release, deployment, publication, or life-safety advice.

Do not disable a guard, remove a negative fixture, broaden an allow list, or
rebaseline a warning merely to obtain green output.

[Back to top](#top)

## 7. Result record

Record at minimum:

```text
repository: bartytime4life/Kansas-Frontier-Matrix
tested_sha: <40-character SHA>
result_kind: HEAD | BASELINE | MERGE_RESULT
python_version: <version>
commands: <exact commands from section 4 that ran>
network_posture: KFM_NO_NETWORK=1 plus reviewed Python startup guard and named test-local guards
python_process_egress_proof: NOT_RUN | PASS at exact SHA
runner_wide_egress_proof: NOT_RUN | PASS with evidence URL
valid_fixture_results: <path and exit status>
expected_negative_results: <path and expected rejection>
hosted_run: <URL or NOT_RUN>
failures: <INTRODUCED | INHERITED | SKIPPED | NOT_RUN | UNKNOWN>
holds: live source, evidence, policy, proof, promotion, release, deployment, publication
```

Do not include credentials, restricted payloads, exact sensitive locations,
temporary links, or unreviewed source excerpts in the record.

[Back to top](#top)

## 8. Maintenance and documentation rollback

Update this runbook when the accepted Hydrology module inventory, workflow
commands, network guards, fixture polarity, dependency installer, aggregate
target, proof posture, or release posture changes. Re-pin all executable claims
to current repository bytes before editing.

The remaining enforcement gap is runner-wide and non-Python no-egress proof,
including dependency installation and any shell-native client. That remains
`PROPOSED` and requires a separately reviewed host, container, or namespace
control with exact-head negative probes. Do not relabel the current Python
startup guard as that broader proof.

Before merge, close the draft pull request and discard only its feature branch.
After an authorized merge, revert this documentation commit or submit a reviewed
forward correction. Neither action changes source admission, evidence, policy,
lifecycle, proof, release, deployment, publication, or external conditions.

Related procedures: [Hydrology validation](./VALIDATION.md) ·
[source-refresh preflight](./SOURCE_REFRESH_RUNBOOK.md) ·
[promotion preflight](./PROMOTION_RUNBOOK.md) ·
[rollback readiness](./ROLLBACK_RUNBOOK.md) ·
[lane index](./README.md)

[Back to top](#top)
