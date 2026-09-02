<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/settlements-infrastructure/rollback
title: Settlements and Infrastructure — Rollback Readiness Runbook
type: runbook
version: v2.0
prior_state: proposal-heavy May 2026 procedure with unverified release records, commands, roles, public surfaces, and live rollback capability
status: draft; repository-grounded; BOUNDED_ROLLBACK_CANDIDATE_VALIDATION; GENERIC_SYNTHETIC_REHEARSAL_ONLY; SETTLEMENTS_INFRASTRUCTURE_ROLLBACK_EXECUTION_HELD; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Settlements/Infrastructure, municipal-source, infrastructure-security, cultural, sovereignty, evidence, policy, correction, rollback, and release assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; critical-infrastructure-sensitive; cultural-and-sovereignty-sensitive; fail-closed
current_path: docs/runbooks/settlements-infrastructure/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: human incident classification, rollback-candidate validation, and accountable-review handoff for the Settlements/Infrastructure lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, evidence, policy, review, release records, correction and withdrawal records, signatures, receipts, proofs, and competent official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 83ace64d7451eca641cbe9f3b6fe86eb0867cb0e
  target_before_update_blob: 9ac8e114bc18ac5b7a63033e60fdf3559e87ee2b
  local_runbook_boundary_blob: 902ff42959d8ec60391b643acca0b660276125fc
  domain_workflow_blob: a47d89c40efd58ac31bc44dbc56bdfb1ccc3a325
  convergence_workflow_blob: 584ac26dcaf5791b1a560cb71bd059e889f55791
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_card_tests_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  rollback_card_workflow_blob: 1980b6e914532c1478d6f14310b916b69a0fb1c4
  rollback_drill_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  production_rollback_pipeline_blob: 2afd3a3d859318e05dcb3e1b2763e4e375b790b6
  release_candidate_readme_blob: 3594fb43ab481d39697deb41790d484f9782fec2
  release_manifest_readme_blob: d21bbf47121228e204f0668f815ab3e9e4581ef7
  release_rollback_card_readme_blob: 00679f017ad8515325f91c972f6e613599eb53b7
  proof_readme_blob: 08c0f3bd93a81f7960d7de77d2b8087a213e67ed
  rollback_data_readme_blob: 9eacbdd177f82867ebf8c6f8184260e00bddbf10
  published_readme_blob: 27507202e391d742351163a174deb1b3ec6585e9
  policy_readme_blob: 792a67caab14d119cf4a21dee1365216bfaefb11
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  lane_candidate_records_observed: 0
  lane_release_manifest_records_observed: 0
  lane_rollback_card_records_observed: 0
  lane_proof_artifacts_observed: 0
  lane_rollback_support_records_observed: 0
  lane_published_payloads_observed: 0
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ../../domains/settlements-infrastructure/README.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-settlements-infrastructure.yml
  - ../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml
  - ../../../.github/workflows/rollback-card.yml
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../fixtures/release/rollback_card/
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../pipelines/rollback/main.py
  - ../../../policy/domains/settlements-infrastructure/README.md
  - ../../../release/candidates/settlements-infrastructure/README.md
  - ../../../release/manifests/settlements-infrastructure/README.md
  - ../../../release/rollback_cards/settlements-infrastructure/README.md
  - ../../../data/proofs/settlements-infrastructure/README.md
  - ../../../data/rollback/settlements-infrastructure/README.md
  - ../../../data/published/settlements-infrastructure/README.md
notes:
  - "v2.0 replaces proposed live rollback steps with a current-repository readiness procedure and accountable-review handoff."
  - "The generic RollbackCard profile is closed, fixture-validated, and explicitly non-executing; its schema status remains PROPOSED."
  - "The repository rollback drill is read-only. The only apply helper is marker-protected, synthetic-only, and incapable of creating production authority."
  - "The Settlements/Infrastructure candidate, manifest, rollback-card, proof, rollback-support, and published lanes contain guidance only; no lane instance record or public payload was observed."
  - "Production target selection, signature and review verification, policy evaluation, receipt flow, external invalidation, alias mutation, release transition, deployment, and publication remain held."
  - "Connected Google Drive material was consulted as planning lineage and Notion as coordination context; current GitHub evidence controls current-behavior claims."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements and Infrastructure — Rollback Readiness Runbook

Use this runbook to classify a suspected defect in material believed to have
been released through the Settlements/Infrastructure lane, assemble a rollback,
withdrawal, hold, or error candidate, run the repository's bounded no-network
checks, and hand the result to accountable reviewers. It does not execute a
production rollback.

> [!WARNING]
> Current repository evidence does not establish a Settlements/Infrastructure
> release to roll back. The lane-specific candidate, manifest, rollback-card,
> proof, rollback-support, and published directories contain only their README
> files and, where present, `.gitkeep` markers. Stop at `HOLD` unless an exact
> affected release and every required governed support record are independently
> identified and verified.

> [!CAUTION]
> KFM is not an emergency, public-safety, utility-service, infrastructure-
> condition, municipal-law, land-use, planning, inspection, security, legal, or
> regulatory authority. A rollback check cannot establish that a place is
> legally incorporated, a facility is safe, a service is available, or an
> infrastructure asset, dependency, condition, access route, or operating state
> is current, complete, lawful, or suitable for action.

**Quick navigation:** [purpose](#purpose-and-authority-boundary) ·
[current capability](#current-capability) ·
[when to use this runbook](#when-to-use-this-runbook) ·
[inputs and stop conditions](#inputs-and-stop-conditions) ·
[procedure](#procedure) · [validation](#validation-commands) ·
[handoff](#accountable-review-handoff) ·
[open verification](#open-verification-backlog) ·
[document rollback](#documentation-rollback)

## Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures below `docs/runbooks/`. This same-path update
therefore remains under the `docs/` responsibility root. It does not create a
new release, policy, proof, data, execution, or public authority.

The controlling responsibility split is:

| Concern | Owning surface | This runbook's limit |
|---|---|---|
| Incident procedure and review handoff | `docs/runbooks/settlements-infrastructure/` | Explain and record bounded human steps |
| Rollback candidate meaning and shape | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) and its [paired schema](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Cite the proposed candidate profile; never activate or approve it |
| Release-plane records | `release/candidates/`, `release/manifests/`, `release/rollback_cards/`, correction, withdrawal, and decision families | Require immutable references; never manufacture a decision from prose |
| Data-plane support and public carriers | `data/proofs/`, `data/rollback/`, and `data/published/` | Inspect governed records; never mutate public state from a runbook |
| Evidence, rights, and policy | Evidence contracts, source records, `policy/`, and accountable review | Missing or inactive support fails closed |
| Execution mechanics | [`tools/release/rollback_apply.py`](../../../tools/release/rollback_apply.py) and [`pipelines/rollback/main.py`](../../../pipelines/rollback/main.py) | The helper is synthetic-only and the production pipeline is a placeholder |
| Public state | Governed release resolvers and released public-safe artifacts | No direct read or write path is authorized here |

Rollback is a governed state transition. It is not deletion, erasure, a file
move, a branch merge, a cache purge performed from documentation, or an
undocumented edit to a mutable `current` or `latest` alias. Prior manifests,
artifacts, evidence, decisions, receipts, proofs, corrections, and lineage must
remain inspectable unless a separate lawful and policy-governed retention or
erasure process applies.

## Current capability

The conclusions below are bound to the commit and blobs in the metadata block.
Re-inspect them before relying on this procedure at another revision.

| Surface | Current repository evidence | Safe conclusion |
|---|---|---|
| Settlements/Infrastructure release inventory | Candidate lane contains `README.md`; manifest, rollback-card, proof, rollback-support, and published lanes contain `README.md` plus `.gitkeep` where present | No in-repository lane release, rollback target, rollback card, proof, recovery record, or public payload is available for an operational rollback |
| Domain readiness workflow | Three read-only jobs inspect validation, proof, and release-readiness boundaries and emit explicit holds | Structural readiness is checked; semantic validation, proof production, and release dry-run are not established |
| EvidenceBundle projection convergence | Separate workflow runs three focused tests and a shared-fixture validator | Shape delegation and selected shared fixture behavior are bounded evidence only; no domain evidence closure is established |
| Generic `RollbackCard` profile | Closed proposed schema, semantic validator, three valid fixtures, six invalid fixtures, focused tests, and read-only workflow | Candidate shape and local consistency can be checked; validation does not resolve references, authenticate reviewers, execute policy, or mutate release state |
| Generic rollback drill | Read-only workflow inspects held surfaces and runs twelve generic and Hazards synthetic rehearsal tests | Non-vacuous synthetic readiness evidence only; no Settlements/Infrastructure target or public state is selected or mutated |
| Synthetic apply helper | Requires a marker-protected temporary root and a scenario with `synthetic: true`; all governance authority flags remain false | Safe only for isolated rehearsal fixtures; deny production, external, or real-data use |
| Production rollback pipeline | `pipelines/rollback/main.py` contains only `# rollback stage — greenfield placeholder` | Production rollback execution is not implemented |
| Direct lane rollback tests | Repository search found no rollback-specific module below `tests/domains/settlements-infrastructure/` | No lane-specific executable rollback proof is established |
| Domain policy | Experimental source scaffolds remain evaluator-unbound | No accepted candidate-bound policy result or obligation enforcement is established |
| GitHub review route | `CODEOWNERS` routes repository review to `@bartytime4life` | Routing is not domain expertise, independent approval, policy authority, rollback authority, release authority, or authentication of an accountable reviewer |

A green workflow proves only the exact bounded checks it runs at the tested
revision. It is not a `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`,
approved `RollbackCard`, execution receipt, correction completion, release
transition, deployment, promotion, or publication event.

### Current finite result

```yaml
work_state: HOLD
reason_codes:
  - SI_AFFECTED_RELEASE_UNVERIFIED
  - SI_ROLLBACK_TARGET_UNVERIFIED
  - SI_LANE_RELEASE_RECORD_ABSENT
  - SI_DOMAIN_SEMANTIC_VALIDATION_UNESTABLISHED
  - SI_PROOF_PRODUCER_UNESTABLISHED
  - SI_POLICY_RUNTIME_UNVERIFIED
  - SI_ACCOUNTABLE_ROLLBACK_AUTHORITY_UNVERIFIED
  - SI_PRODUCTION_ROLLBACK_ENGINE_UNESTABLISHED
terminal_boundary: ACCOUNTABLE_ROLLBACK_REVIEW_HANDOFF_ONLY
rollback_execution: NOT_PERFORMED
release: NOT_PERFORMED
deployment: NOT_PERFORMED
publication: NOT_PERFORMED
```

These reason codes summarize this documentation review. They are not an
accepted machine enum and do not amend the `RollbackCard` contract.

## Outcome vocabulary

Keep validation results, candidate disposition, review state, release state,
deployment state, and publication state separate.

The current generic `RollbackCard` profile defines four candidate dispositions:

| Disposition | Meaning | Authority effect |
|---|---|---|
| `ROLLBACK_CANDIDATE` | Proposes restoring one distinct prior release | Candidate only; no approval or mutation |
| `WITHDRAWAL_CANDIDATE` | Proposes withdrawal without selecting a prior release | Candidate only; no withdrawal executed |
| `HOLD` | Records unresolved support or a stop condition | Preserve current state and escalate |
| `ERROR` | Records malformed, conflicting, unreadable, or unevaluable input | Repair evidence or tooling before relying on a result |

A validator `PASS` means only that the candidate satisfied the declared bounded
profile. It does not convert a candidate disposition into approval. Likewise,
`READY_FOR_ACCOUNTABLE_ROLLBACK_REVIEW` is a human handoff description used by
this runbook, not a schema value, release decision, or public state.

## When to use this runbook

Use it after a suspected defect is reported against material believed to be
released through the Settlements/Infrastructure lane. First determine whether
the report identifies an exact governed release record. A map view, branch,
pull request, generated answer, screenshot, cache entry, candidate, internal
file, or directory named `published` is not by itself proof of publication.

### Candidate trigger mapping

The generic profile provides these public-safe trigger reason codes. Choose the
narrowest supported code and keep sensitive incident detail in the appropriate
protected system rather than in a public card or pull request.

| Defect class | Candidate reason code | Settlements/Infrastructure examples |
|---|---|---|
| General released-state defect | `RELEASE_DEFECT` | Wrong carrier or manifest association after a release is independently proven |
| Contradicted or unsupported evidence | `EVIDENCE_CONTRADICTION` or `INSUFFICIENT_EVIDENCE` | Municipality/census-place collapse, unsupported facility status, missing EvidenceBundle support |
| Rights or license change | `RIGHTS_CHANGE` | A source no longer permits the exposed use or precision |
| Harmful precision or newly sensitive detail | `SENSITIVITY_DISCOVERY` or `SECURITY_ISSUE` | Facility interiors, dependency topology, exploitable condition detail, protected cultural or sovereignty-bearing geometry |
| Bounded validator failure | `VALIDATION_FAILURE` | Candidate, schema, digest, time, or public-safe transform fails its accepted profile |
| Source removal | `SOURCE_WITHDRAWAL` | A source withdraws or invalidates the material on which the release depends |
| Policy failure | `POLICY_FAILURE` | Required policy result is absent, stale, inapplicable, or contradicted |
| Runtime or delivery failure | `OPERATIONAL_FAILURE` | Governed resolver, carrier, or cache serves a different release than its verified manifest |
| Immediate fail-closed review | `EMERGENCY_HOLD` | Continued exposure may be harmful while evidence and accountable authority are being established |
| Malformed incident input | `INPUT_INVALID` | Missing, conflicting, or non-resolving release, target, digest, time, or support references |

`EMERGENCY_HOLD` is a candidate classification, not an emergency-service,
utility-control, public-warning, dispatch, shutdown, or infrastructure-
operations instruction. Contact the competent authority through its established
channels for real-world urgent action.

## Inputs and stop conditions

### Required incident inputs

- [ ] Exact repository revision and incident identifier.
- [ ] Exact affected `ReleaseManifest` reference and immutable digest.
- [ ] Evidence that the affected release is the state resolved by the governed
      public surface; do not infer this from an alias named `current` or `latest`.
- [ ] Exact defect class, affected object families, geography, valid time,
      observed time, carriers, and public surfaces.
- [ ] Resolvable EvidenceBundle, source-role, rights, sensitivity, policy,
      validation, proof, and review references appropriate to the defect.
- [ ] Correction or withdrawal record reference when public notice or public
      state correction is required.
- [ ] Complete invalidation inventory covering every affected carrier and
      downstream derivative.
- [ ] Accountable domain and release reviewers, plus infrastructure-security,
      rights, cultural, sovereignty, privacy, or legal review when implicated.

### Additional inputs for `ROLLBACK_CANDIDATE`

- [ ] Exact target `ReleaseManifest` reference that differs from the affected
      release.
- [ ] Target artifact inventory and digest closure.
- [ ] Evidence that the target's source role, rights, sensitivity, time,
      policy, review, proof, correction, and public-safe posture remain valid
      now.
- [ ] Preserved lineage from the target through the affected release and the
      proposed correction.
- [ ] Restoration validation plan and post-change observation plan.

### Mandatory stop conditions

Return `HOLD`, `WITHDRAWAL_CANDIDATE`, or `ERROR` as supported when any required
item is unresolved or unsafe:

- no exact affected release or governed public resolver can be verified;
- the target is absent, equal to the affected release, mutable, stale,
  digest-invalid, unreviewed, or no longer policy-eligible;
- municipality, census place, historic townsite, community, facility, operator,
  condition, service, dependency, geometry, or cross-domain identity is
  conflated or unresolved;
- source role, rights, license, consent, sensitivity, sovereignty, harmful
  precision, freshness, valid time, or correction status is unclear;
- evidence, proof, policy, review, signature, correction, withdrawal, receipt,
  invalidation, or restoration closure is incomplete;
- the candidate would expose restricted geometry, infrastructure detail,
  private-person context, protected cultural information, credentials, or
  exploit-relevant incident text;
- a cross-domain response would absorb Roads/Rail/Trade, Hydrology, Hazards,
  Archaeology, People/DNA/Land, legal, safety, emergency, or regulatory
  authority;
- the proposed action depends on the synthetic helper, placeholder production
  pipeline, placeholder domain tests, or experimental policy as live authority;
- the only evidence of release is a path, filename, green workflow, merged pull
  request, deployment, map layer, generated summary, or mutable alias; or
- one actor would author and solely approve a policy- or release-significant
  transition without an accepted exception.

Do not weaken a validator, fixture polarity, no-network boundary, policy hold,
proof hold, release hold, sensitivity transform, review requirement, or
invalidation requirement to obtain a passing result.

## Procedure

### 1. Pin the evidence boundary

From a clean, dedicated checkout or worktree, record:

```bash
git remote get-url origin
git rev-parse HEAD
git status --short
```

Record the incident ID, time of observation, affected repository paths, claimed
public surface, and the evidence supporting that claim. Keep restricted or
exploit-relevant reports out of public GitHub issues, pull requests, fixtures,
logs, and candidate cards.

### 2. Inventory the lane before making a release claim

```bash
find release/candidates/settlements-infrastructure \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
find release/manifests/settlements-infrastructure \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
find release/rollback_cards/settlements-infrastructure \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
find data/proofs/settlements-infrastructure \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
find data/rollback/settlements-infrastructure \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
find data/published/settlements-infrastructure \
  -mindepth 1 -type f ! -name README.md ! -name .gitkeep -print
```

At the evidence snapshot, every command is empty. Empty output supports only the
absence of in-repository instance files in these lanes. It does not prove that
no external release or deployment exists. It blocks an in-repository rollback
claim until external state is reconciled to governed records.

### 3. Classify the defect and affected carriers

Keep these identities and support roles separate:

- legal municipality, census place, named place, historic townsite, community,
  and map label;
- facility identity, operator, ownership, operation, condition, capacity,
  service, access, and safety claims;
- infrastructure node, segment, network, service area, and dependency relation;
- source observation, legal or regulatory record, model, classification,
  aggregate, interpretation, and generated summary;
- restricted canonical geometry and generalized public geometry; and
- catalog, triplet, API, tile, PMTiles, search, vector, Evidence Drawer, export,
  report, and AI-cache derivatives.

List each affected carrier explicitly. A correction may require invalidating
more than the visible map layer.

### 4. Select the earliest supported disposition

Use `ROLLBACK_CANDIDATE` only when a distinct prior release is exact,
digest-verified, evidence-supported, policy-eligible, reviewed, and complete.
Use `WITHDRAWAL_CANDIDATE` when continued exposure is unsafe and no verified
safe target is available. Use `HOLD` when support is incomplete. Use `ERROR`
when trustworthy evaluation cannot complete.

Do not substitute a branch, commit, artifact directory, map style, tile archive,
or remembered prior state for a target `ReleaseManifest`.

### 5. Prepare a minimized candidate

Use the [RollbackCard contract](../../../contracts/release/rollback_card.md) and
[paired schema](../../../schemas/contracts/v1/release/rollback_card.schema.json).
The schema requires all eighteen top-level fields and keeps every governance
flag false. A valid card remains a candidate.

Prepare incident candidates in a protected temporary workspace. Do not commit
restricted coordinates, facility interiors, dependency maps, credentials,
private-person detail, unreviewed source excerpts, or exploit-relevant findings.
The existing lane-specific rollback-card README does not yet establish a
reviewed machine-record binding for this generic schema; if a tracked candidate
home is required, stop and obtain the applicable release-governance review.

### 6. Run bounded RollbackCard validation

Dependency installation is a separate network and supply-chain boundary. The
focused workflow installs the repository's `project-runtime` profile before
validation:

```bash
python tools/ci/install_python_ci.py project-runtime
```

Then run the fixture profile, focused tests, and the candidate validator:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
python tools/validators/release/validate_rollback_card.py \
  /protected/path/to/rollback-card.json
```

The last path is illustrative and must point to the protected candidate being
reviewed. Run these Python commands inside the guarded local window described
by [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) when no-network
startup enforcement is required. A green result proves candidate shape and
local consistency only.

### 7. Use synthetic rehearsal only for tool mechanics

The repository's generic and Hazards rehearsal tests copy synthetic workspaces
to temporary roots before invoking the marker-protected helper:

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

At the evidence snapshot, this profile runs twelve tests. It does not use
Settlements/Infrastructure data and does not prove lane-specific recovery. Do
not invoke `tools/release/rollback_apply.py` against a repository checkout,
production directory, external store, real release, or non-synthetic scenario.

### 8. Re-run bounded domain checks

Run the exact guarded schema-convergence procedure in
[`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md). The domain workflow
also classifies static readiness, but its green state retains explicit semantic,
proof, and release holds.

A rollback packet must not claim that these checks validate real settlement,
municipal, facility, condition, service, dependency, geometry, policy, proof,
release, or public behavior.

### 9. Assemble the review packet

Record:

- exact affected and target release references and digests;
- the candidate card and validation output;
- incident scope, public-safe reason code, geography, valid time, observed time,
  and affected carrier inventory;
- EvidenceBundle, source, rights, sensitivity, policy, proof, review,
  correction, withdrawal, invalidation, and restoration references;
- every unresolved item and the finite result it caused;
- accountable reviewer identities and separation of duties;
- a post-change verification plan; and
- an explicit statement that no rollback, release, deployment, promotion, or
  publication was performed.

### 10. Stop at accountable review handoff

A complete packet may be described as
`READY_FOR_ACCOUNTABLE_ROLLBACK_REVIEW`. That description authorizes no public
mutation. The accountable release and rollback process must independently
verify actors, policy, signatures, exact target, invalidations, correction,
execution receipts, and observed post-change state.

This runbook never issues `APPROVED`, executes rollback, changes an alias,
invalidates an external cache, withdraws a release, deploys, promotes, or
publishes.

## Validation commands

### Generic RollbackCard profile

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
python tools/validators/release/validate_rollback_card.py --fixtures
python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-rollback-card-contract-current-binding-20260815.json \
  --repo-root .
```

Expected bounded fixture inventory at the evidence snapshot:

- three valid candidates;
- six invalid candidates with an expected-findings manifest; and
- explicit rejection of missing targets, equal affected/target releases,
  missing correction notice, invalid time order, placeholder digest, and
  governance-authority claims.

### Cross-cutting synthetic rehearsal

```bash
KFM_NO_NETWORK=1 PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 TZ=UTC \
  python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

Expected bounded result at the evidence snapshot: twelve passing tests in
isolated synthetic roots. A different count is a review trigger; inspect the
exact test inventory before changing this document.

### Settlements/Infrastructure readiness

```bash
python tools/validators/ci_readiness.py \
  --label "Settlements/Infrastructure" \
  --test-root tests/domains/settlements-infrastructure \
  --validator-root tools/validators/domains/settlements-infrastructure \
  --validator-root tools/validators/facilities \
  --validator-root tools/validators/hazard-exposure
```

This helper classifies known placeholder and readiness surfaces. It does not run
placeholder test modules or validator implementations. Use the exact
[domain workflow](../../../.github/workflows/domain-settlements-infrastructure.yml)
for the full read-only orchestration and its explicit holds.

## Failure interpretation

| Observation | Bounded interpretation | Required response |
|---|---|---|
| Lane inventory is empty | No tracked lane instance supports an in-repository release claim | Return `HOLD`; reconcile any claimed external release |
| RollbackCard fixture profile is green | Generic candidate shape and reviewed fixture polarity passed | Do not claim reference resolution, policy, review, execution, or release |
| Candidate validation is green | One card is shape-valid and locally consistent | Hand off for accountable review; do not mutate public state |
| Candidate names the affected release as its target | Validator should report `ROLLBACK_TARGET_NOT_PRIOR` | Reject the candidate and select a distinct verified target or another disposition |
| Required public notice lacks a correction reference | Validator should report `CORRECTION_NOTICE_REQUIRED` | Add the governed reference or hold the candidate; do not invent one |
| Governance flags claim authority or execution | Validator should report `GOVERNANCE_BOUNDARY_VIOLATION` | Reject the candidate; candidate validation is intentionally non-authoritative |
| Synthetic rehearsal passes | Temporary synthetic alias, correction, invalidation, and history-preservation mechanics behaved as tested | Do not generalize to Settlements/Infrastructure or production recovery |
| Synthetic helper rejects the root or scenario | Marker or `synthetic: true` guard blocked use | Preserve the denial; do not weaken the guard |
| Domain readiness is green | Expected structural and held-state checks completed at one SHA | Report the holds; do not claim semantic or operational readiness |
| A proposal-era command happens to run | One unaccepted command executed in one environment | Do not upgrade it to a supported production procedure |

## Accountable review handoff

The packet should be complete enough that reviewers can reproduce every bounded
claim without receiving restricted material they are not authorized to see.

### Minimum handoff record

```yaml
incident_id: <stable incident reference>
repository_ref: <exact commit SHA>
affected_release_ref: <immutable release reference>
affected_release_digest: <sha256 digest>
disposition: ROLLBACK_CANDIDATE | WITHDRAWAL_CANDIDATE | HOLD | ERROR
target_release_ref: <distinct immutable release reference or null>
rollback_card_ref: <protected candidate reference>
validation:
  rollback_card_profile: PASS | FAIL | NOT_RUN
  synthetic_rehearsal: PASS | FAIL | NOT_APPLICABLE
  settlements_readiness: PASS_WITH_HOLDS | FAIL | NOT_RUN
support:
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  correction_notice_ref: null
invalidations: []
open_holds: []
accountable_reviewers: []
execution_performed: false
public_state_mutated: false
release_performed: false
deployment_performed: false
publication_performed: false
```

This is an illustrative handoff summary, not the `RollbackCard` schema. Do not
store secrets or protected incident detail in it.

### Review and separation of duties

GitHub review is routed through
[`CODEOWNERS`](../../../.github/CODEOWNERS) to `@bartytime4life`. That is the
only verified named repository review route in this evidence snapshot. It does
not establish Settlements/Infrastructure expertise, source-rights approval,
infrastructure-security review, cultural or sovereignty review, policy
approval, rollback authority, release authority, or independent approval.

A policy- or release-significant transition needs the accountable roles required
by the accepted governance for that exact scope. Missing assignments keep the
candidate at `HOLD`.

## Domain-specific incident boundaries

### Legal municipality or census-place collapse

Do not roll back to a record that repeats the same identity error. Verify legal,
statistical, historical, colloquial, and map-label roles separately, with their
source and valid-time support. If no safe prior release is proven, use
`WITHDRAWAL_CANDIDATE` or `HOLD` rather than guessing.

### Facility condition, service, access, or safety claim

A stale or contradicted condition observation does not establish present safety,
availability, access, ownership, capacity, or operation. Keep the report public-
safe, route urgent real-world questions to the competent authority, and require
source time, observation time, evidence, policy, and correction closure.

### Critical-infrastructure or dependency exposure

Do not copy exact geometry, interiors, topology, vulnerabilities, credentials,
or exploitable condition detail into a public candidate or PR. Prepare a
minimized `WITHDRAWAL_CANDIDATE` or `HOLD`, preserve the protected report in its
authorized system, and obtain infrastructure-security and sensitivity review.

### Cultural, sovereignty, archaeology, or living-person impact

Use the most restrictive supported exposure. Generalized public geometry does
not replace restricted canonical geometry. Cross-domain reviewers retain their
own authority; this lane cannot approve archaeology, cultural, sovereignty,
privacy, land, or living-person disclosure.

### Downstream derivative mismatch

A corrected source or record does not automatically repair tiles, PMTiles,
catalogs, triplets, search indexes, vector indexes, caches, Evidence Drawer
payloads, exports, reports, or AI answers. Enumerate every applicable
`invalidations` class and require observed completion through a separately
accepted execution and receipt path.

## Acceptance and negative cases

A review packet is complete enough for accountable review only when every
applicable input is exact, resolvable, public-safe for the handoff channel, and
reproducible. Current repository state does not meet that condition for a real
Settlements/Infrastructure release.

Required negative cases include:

- no affected release reference;
- affected and target release are identical;
- target release is mutable, unverified, stale, or policy-ineligible;
- missing EvidenceBundle or policy references for a rollback candidate;
- required public notice without a correction reference;
- incomplete invalidation inventory;
- out-of-order detection, decision, and effective times;
- self-referential lineage;
- any candidate claim that policy, review, rollback, public mutation, or release
  already occurred;
- non-synthetic input or missing synthetic marker passed to the rehearsal helper;
- restricted or exploit-relevant detail in public repository surfaces; and
- an attempt to treat a green workflow, path, map, file move, deployment, or
  generated answer as release or rollback authority.

## Open verification backlog

Before production rollback can be documented as executable, verify or adopt:

- an exact current-release resolver and immutable Settlements/Infrastructure
  release inventory;
- the accepted `ReleaseManifest` and lane-specific candidate bindings;
- accountable domain, source-rights, infrastructure-security, cultural,
  sovereignty, policy, rollback, and release roles with separation of duties;
- operational policy evaluation and candidate-bound decision records;
- reference resolution for evidence, review, correction, proof, and release
  support;
- signature or attestation requirements for rollback decisions and execution
  receipts;
- an accepted invalidation executor and completion receipts for every carrier;
- a production rollback engine with no-write, authorization, target-integrity,
  rollback, correction, and failure-recovery tests;
- a Settlements/Infrastructure-specific synthetic rehearsal with public-safe,
  non-operational fixtures before any real-data exercise;
- monitored post-change verification and correction propagation; and
- reconciliation of the lane-specific rollback-card README with the generic
  machine `RollbackCard` contract and schema.

Until those gaps are closed by accepted controls and current implementation
evidence, production rollback remains held.

## Related repository surfaces

- [Local runbook boundary](./README.md)
- [Promotion preflight](./PROMOTION_RUNBOOK.md)
- [Guarded no-network procedure](./NO_NETWORK_TEST_RUNBOOK.md)
- [Source-refresh proposal](./SOURCE_REFRESH_RUNBOOK.md)
- [Settlements/Infrastructure domain boundary](../../domains/settlements-infrastructure/README.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Domain readiness workflow](../../../.github/workflows/domain-settlements-infrastructure.yml)
- [EvidenceBundle convergence workflow](../../../.github/workflows/settlements-infrastructure-evidence-bundle-convergence.yml)
- [RollbackCard workflow](../../../.github/workflows/rollback-card.yml)
- [Rollback drill workflow](../../../.github/workflows/rollback-drill.yml)
- [RollbackCard contract](../../../contracts/release/rollback_card.md)
- [RollbackCard schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [RollbackCard fixtures](../../../fixtures/release/rollback_card/README.md)
- [RollbackCard validator](../../../tools/validators/release/validate_rollback_card.py)
- [RollbackCard tests](../../../tests/validators/test_validate_rollback_card.py)
- [Synthetic rehearsal helper](../../../tools/release/rollback_apply.py)
- [Production rollback placeholder](../../../pipelines/rollback/main.py)
- [Domain policy boundary](../../../policy/domains/settlements-infrastructure/README.md)
- [Candidate boundary](../../../release/candidates/settlements-infrastructure/README.md)
- [Manifest boundary](../../../release/manifests/settlements-infrastructure/README.md)
- [Rollback-card boundary](../../../release/rollback_cards/settlements-infrastructure/README.md)
- [Proof boundary](../../../data/proofs/settlements-infrastructure/README.md)
- [Rollback-support boundary](../../../data/rollback/settlements-infrastructure/README.md)
- [Published-data boundary](../../../data/published/settlements-infrastructure/README.md)

## Documentation rollback

Before merge, close the draft pull request and discard only its feature branch.
After merge, revert the documentation commits or submit a reviewed forward
correction. Either action changes documentation only. It does not undo source
admission, evidence, policy, lifecycle, release, deployment, promotion,
publication, correction, cache, alias, or external system state.

[Back to top](#top)
