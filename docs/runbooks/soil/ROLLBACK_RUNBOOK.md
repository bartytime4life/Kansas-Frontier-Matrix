<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/soil/rollback
title: Soil — Rollback Readiness Runbook
type: runbook
version: v2.0
prior_state: proposal-heavy May 2026 procedure with unverified live rollback actions, fields, roles, public surfaces, and release inventory
status: draft; repository-grounded; BOUNDED_ROLLBACK_CANDIDATE_VALIDATION; SOIL_FIXTURE_VALIDATION_ONLY; SYNTHETIC_REHEARSAL_ONLY; PRODUCTION_ROLLBACK_EXECUTION_HELD; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable Soil, source, scientific, evidence, rights, sensitivity, policy, correction, release, rollback, public-surface, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; soil and land context; potentially precision-sensitive; consequential-use-sensitive; fail-closed
current_path: docs/runbooks/soil/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: human incident classification, rollback-readiness validation, and accountable-review handoff for the Soil lane
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, source records, evidence, policy, review, release records, correction and withdrawal records, signatures, receipts, proofs, and official authorities
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 349d0097e5f7533abe6cd8253f4bd7a30eccd003
  target_before_update_blob: 60ff25bf877a610627ff36430227382a68228a7e
  local_runbook_boundary_blob: d50303c8f4edc6a9427d61135ba2048b0ba01a03
  soil_domain_readme_blob: 06cfbebc3ce130753d4aff766645765747e1dae6
  domain_workflow_blob: e009e00d5743d907461289c1c6571cab69ea2672
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_card_tests_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  rollback_card_workflow_blob: 1980b6e914532c1478d6f14310b916b69a0fb1c4
  rollback_drill_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  soil_candidate_readme_blob: f0f5a002ef3085790a0fcc991fc61788c9e04c4f
  soil_data_rollback_readme_blob: b5db1549ca0fb3508d07280b3ad367c0f066d805
  soil_proof_readme_blob: 1d67e180326b283e33b04cbdee283520ef3b2fad
  soil_published_readme_blob: c70312dacedf4e367d8db2607a780b088677e30d
  soil_published_layers_readme_blob: 6b7d7873a1264f1d927aaa4518353009b2f0fd0c
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  soil_candidate_records_observed: 0
  soil_release_grade_manifest_records_observed: 0
  soil_rollback_card_records_observed: 0
  soil_data_plane_rollback_records_observed: 0
  soil_proof_artifacts_observed: 0
  soil_published_payloads_observed: 0
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ../../domains/soil/README.md
  - ../../doctrine/directory-rules.md
  - ../../doctrine/lifecycle-law.md
  - ../../doctrine/trust-membrane.md
  - ../../adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md
  - ../../adr/ADR-0024-steward-separation-of-duties-for-release.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/workflows/domain-soil.yml
  - ../../../.github/workflows/rollback-card.yml
  - ../../../.github/workflows/rollback-drill.yml
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/rollback_card.schema.json
  - ../../../fixtures/release/rollback_card/
  - ../../../tools/validators/release/validate_rollback_card.py
  - ../../../tests/validators/test_validate_rollback_card.py
  - ../../../tools/release/rollback_apply.py
  - ../../../release/candidates/soil/README.md
  - ../../../release/manifests/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../release/rollback/README.md
  - ../../../data/rollback/soil/README.md
  - ../../../data/proofs/soil/README.md
  - ../../../data/published/soil/README.md
  - ../../../data/published/layers/soil/README.md
notes:
  - "v2.0 replaces proposed live mutation steps with a current-repository readiness procedure and accountable-review handoff."
  - "The generic RollbackCard profile is closed, fixture-validated, and explicitly non-executing; its schema status remains PROPOSED."
  - "The active Soil workflow runs three bounded Soil fixture profiles and one fixture-only SSURGO package-drift comparator; Soil proof and release-dry-run jobs remain explicit holds."
  - "The generic rollback drill is read-only readiness evidence. Its apply helper is marker-protected and synthetic-only; the production rollback pipeline remains a placeholder."
  - "No release-grade Soil manifest, Soil RollbackCard instance, Soil proof artifact, Soil published payload, current resolver, production executor, or operational rollback authority was verified at the pinned snapshot."
  - "A root manifest-like file named agri-soil-crop-suitability-v1-001.json is a PROPOSED documentation-inventory placeholder and is not treated as a Soil ReleaseManifest."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="soil-rollback-runbook"></a>

# Soil — Rollback Readiness Runbook

Use this runbook to classify a suspected post-release Soil defect, determine
whether a governed release actually exists, assemble a non-executing rollback,
withdrawal, or hold candidate, run bounded no-network checks, and hand the
result to accountable reviewers. It does **not** execute a production rollback.

> [!WARNING]
> Current repository evidence does not establish a release-grade Soil release
> to roll back. The Soil candidate, proof, data-plane rollback, and published
> lanes contain guidance and keep files but no verified instance records or
> public payloads. Soil-specific manifest and rollback-card sublanes were not
> present at the pinned snapshot. Stop at `HOLD` unless an exact affected
> release, current governed resolver, and complete support packet are
> independently identified.

> [!CAUTION]
> `release/manifests/agri-soil-crop-suitability-v1-001.json` is marked
> `PROPOSED` and says it was created from documentation inventory. Its filename
> is not release evidence. A branch, pull request, README, candidate, map,
> screenshot, test fixture, generated answer, or file named `current` or
> `latest` is not proof of publication.

> [!IMPORTANT]
> KFM Soil material is not agronomic, engineering, conservation-compliance,
> land-value, title, regulatory, emergency, or safety advice. Route
> consequential decisions to the relevant qualified professional and official
> authority.

**Quick navigation:** [Current capability](#current-capability) ·
[When to use this runbook](#when-to-use-this-runbook) ·
[Inputs and stop conditions](#inputs-and-stop-conditions) ·
[Soil anti-collapse controls](#soil-anti-collapse-controls) ·
[Procedure](#procedure) · [Validation commands](#validation-commands) ·
[Handoff packet](#handoff-packet) ·
[Rollback of this document](#rollback-of-this-document)

## Purpose and authority boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../doctrine/directory-rules.md), which place
human operational procedures under `docs/runbooks/`. This same-path update
therefore remains in the `docs/` responsibility root. It creates no source,
evidence, policy, lifecycle, release, rollback, deployment, or publication
authority.

Rollback is a governed state transition. It is not deletion, erasure, a file
move, a branch merge, an undocumented alias change, or a direct edit to a map,
catalog, API, cache, or published carrier. Prior evidence, manifests, artifacts,
receipts, decisions, corrections, and lineage remain inspectable unless a
separate lawful retention or erasure process applies.

| Concern | Owning surface | This runbook's limit |
|---|---|---|
| Incident procedure and handoff | `docs/runbooks/soil/` | Explains bounded human steps and stop conditions |
| Rollback candidate meaning | [`contracts/release/rollback_card.md`](../../../contracts/release/rollback_card.md) | Cites the proposed semantic profile; cannot accept or activate it |
| Rollback candidate shape | [`schemas/contracts/v1/release/rollback_card.schema.json`](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Uses the current closed `1.0.0` shape; cannot create authority |
| Candidate validation | [`tools/validators/release/validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | Proves bounded shape and local consistency only |
| Release-plane records | `release/manifests/`, `release/rollback_cards/`, correction and withdrawal lanes | Requires immutable governed pointers; cannot manufacture a decision |
| Soil data-plane support | [`data/rollback/soil/`](../../../data/rollback/soil/README.md) | May support a future executed transition; is not release authority |
| Evidence and proof | [`data/proofs/soil/`](../../../data/proofs/soil/README.md) and accepted evidence contracts | Evidence outranks this runbook, maps, tests, and generated language |
| Policy and sensitivity | `policy/` plus accountable review | Missing or inactive evaluation fails closed |
| Public state | Governed resolvers and released public-safe carriers | No direct mutation or read path is authorized here |

Public clients and ordinary UI surfaces use governed interfaces and released
public-safe artifacts. They do not read `RAW`, `WORK`, `QUARANTINE`,
`PROCESSED`, canonical stores, source registries, proof stores, or direct model
output during rollback.

## Current capability

| Surface | Confirmed repository state | Safe conclusion |
|---|---|---|
| Soil release inventory | `release/candidates/soil/` has only its README; no `release/manifests/soil/`, `release/rollback_cards/soil/`, or `release/rollback/soil/` sublane was present | No in-repository Soil release or Soil rollback record is available for production action |
| Soil published inventory | `data/published/soil/` has only a README and `.gitkeep`; each documented Soil layer-family sublane has only a README and `.gitkeep` | No Soil public payload was verified |
| Soil proof inventory | `data/proofs/soil/` has only a README and `.gitkeep` | No Soil ProofPack or release-closing proof was verified |
| Soil data-plane rollback inventory | `data/rollback/soil/` has only a README and `.gitkeep` | No alias-revert, invalidation, or execution receipt was verified |
| Bounded Soil validation | The active Soil workflow runs three deterministic Soil fixture suites and one fixture-only SSURGO drift comparator | Exact synthetic profiles can be checked; Soil truth, source admission, proof, policy, release, and rollback are not established |
| Generic `RollbackCard` profile | Closed proposed schema, semantic validator, three valid fixtures, six invalid fixture families, focused tests, and a read-only workflow | Candidate shape and local consistency can be checked; validation cannot approve or execute rollback |
| Generic rollback drill | Read-only workflow runs twelve non-vacuous generic and Hazards synthetic rehearsal tests and confirms production holds | Useful regression evidence only; there is no Soil-specific or production rollback proof |
| Synthetic apply helper | `tools/release/rollback_apply.py` requires an exact synthetic marker and `synthetic: true` inside an isolated workspace | Test helper only; deny repository, staging, production, published, or external use |
| Production rollback pipeline | `pipelines/rollback/main.py` remains a greenfield placeholder, as asserted by the rollback-drill workflow | Production execution remains held |
| Reviewer routing | CODEOWNERS routes repository review to `@bartytime4life` | Review routing is not an accepted stewardship assignment, independent approval, policy decision, or release authority |

A green test or workflow result belongs to the exact tested SHA and proves only
the named bounded scope. It is not a `PolicyDecision`, `ReviewRecord`,
`ReleaseManifest`, approved `RollbackCard`, signature, release transition,
deployment, correction, withdrawal, or publication event.

## When to use this runbook

Use this procedure after a defect is reported against material believed to be a
released Soil claim or carrier. First establish whether the report names an
exact governed release. When it names only a source capture, map view, layer
configuration, candidate, fixture, branch, pull request, report, cache entry,
screenshot, or AI answer, do not infer that a Soil release exists.

### Candidate dispositions

Use the exact finite dispositions defined by the current generic
`RollbackCard` schema.

| Disposition | Use only when | Required posture |
|---|---|---|
| `ROLLBACK_CANDIDATE` | The affected release is exact and a different prior safe release is exact, immutable, digest-verified, evidence-supported, policy-eligible, reviewed, and complete | Prepare a candidate and accountable handoff; do not mutate public state |
| `WITHDRAWAL_CANDIDATE` | Continued exposure is potentially unsafe and no verified safe target is available | Prepare fail-closed withdrawal review; this runbook does not perform withdrawal |
| `HOLD` | Release identity, resolver state, target, evidence, rights, sensitivity, policy, review, correction, signature, invalidation, or authority is unresolved | Preserve uncertainty and escalate |
| `ERROR` | Inputs are malformed, conflicting, unreadable, or cannot be evaluated deterministically | Repair evidence or tooling before relying on a result |

Do not substitute the separate review-card outcomes documented in
`release/rollback_cards/README.md` for these schema dispositions. The review
index and the machine candidate profile are different maturity surfaces.

### Trigger reason codes

These are the current schema's finite trigger codes. The Soil examples are
classification guidance, not proof that a release or defect exists.

| Reason code | Soil-oriented example | Earliest safe response |
|---|---|---|
| `RELEASE_DEFECT` | A released carrier differs from its manifest or declared support | Pin the affected release and assess rollback or withdrawal |
| `EVIDENCE_CONTRADICTION` | A consequential claim conflicts with its resolved evidence | `HOLD` or withdrawal review until the contradiction is resolved |
| `RIGHTS_CHANGE` | Source terms no longer permit the released use | Fail closed and route to rights and release review |
| `SENSITIVITY_DISCOVERY` | Public material exposes private field, station, Tribal, cultural, or harmful-precision context | Escalate to an authorized containment operator; prepare withdrawal review |
| `VALIDATION_FAILURE` | A release-significant invariant fails after publication | Preserve the failure evidence and assess target safety |
| `SOURCE_WITHDRAWAL` | A source steward or authority withdraws the supporting product | Assess every dependent claim and carrier |
| `POLICY_FAILURE` | Required policy evaluation is absent, stale, or denies exposure | Do not advance or restore public state |
| `SECURITY_ISSUE` | Artifact or delivery integrity is compromised | Use the applicable security incident path and hold this procedure |
| `OPERATIONAL_FAILURE` | A governed resolver or immutable carrier cannot serve the declared release | Distinguish service restoration from a truth rollback |
| `EMERGENCY_HOLD` | An authorized incident process requires immediate fail-closed containment | This document records and hands off; it does not authorize the live action |
| `INSUFFICIENT_EVIDENCE` | Release or target support cannot be resolved | `HOLD` or `WITHDRAWAL_CANDIDATE`; never guess |
| `INPUT_INVALID` | Candidate structure, identifiers, digests, or times are invalid | Return `ERROR` and repair the packet |

## Inputs and stop conditions

### Required incident inputs

- [ ] Exact repository revision, incident identifier, reporter evidence, and
      observation time.
- [ ] Exact affected `ReleaseManifest` reference and immutable manifest digest.
- [ ] Evidence that the governed public resolver currently selects that exact
      release; do not infer selection from a filename.
- [ ] Complete affected artifact inventory and digest closure.
- [ ] Defect reason code, affected object families, support profiles, geography,
      time interval, depth interval, carriers, and public surfaces.
- [ ] Resolvable source, EvidenceBundle, policy, review, rights, sensitivity,
      validation, proof, correction, and withdrawal references appropriate to
      the defect.
- [ ] Complete invalidation inventory for every affected carrier and derivative.
- [ ] Accountable reviewer identities and current scoped authority; add no
      invented role holders to the packet.

### Additional inputs for `ROLLBACK_CANDIDATE`

- [ ] Exact prior `ReleaseManifest` reference that differs from the affected
      release.
- [ ] Target artifact inventory and digest closure.
- [ ] Evidence that target source roles, rights, sensitivity, policy, review,
      time validity, correction status, and public-safe transforms remain valid
      now.
- [ ] Preserved lineage from the target through the affected release and the
      proposed correction.
- [ ] Restoration verification and rollback-of-rollback plan.

### Mandatory stop conditions

Return the supported negative disposition when any of these conditions applies:

- no exact release or current governed resolver can be verified;
- the only candidate is a README, fixture, branch, PR, generated record, or
  `status: PROPOSED` documentation placeholder;
- the target is absent, equal to the affected release, mutable, stale,
  digest-invalid, unreviewed, incomplete, or no longer policy-eligible;
- MUKEY/COKEY/CHKEY lineage, source vintage, support profile, depth, units,
  datum, scale, spatial support, valid time, source time, retrieval time,
  release time, quality control, or uncertainty is missing or contradictory;
- rights, consent, sovereignty, private-property context, sensitive station or
  field detail, or harmful precision is unresolved;
- evidence, proof, policy, review, signature, correction, withdrawal, receipt,
  invalidation, or public-notice closure is incomplete;
- a cross-lane action would absorb Agriculture, Hydrology, Geology, Habitat,
  Flora, Fauna, Hazards, People/Land, or another lane's authority;
- the proposed action depends on the synthetic helper, placeholder production
  pipeline, fixture-only policy, or documentation as live authority;
- the procedure would require a direct CDN, alias, catalog, API, map, cache,
  lifecycle, source, deployment, or public-state mutation; or
- a material transition lacks accountable independent review and no accepted
  exception can be resolved.

For an active exposure or security incident, escalate to the applicable
authorized incident and containment authority. This runbook neither delays a
lawful fail-closed response nor supplies the missing authority or command.

## Soil anti-collapse controls

The active repository has several **profile-local** Soil support identities.
They are not one accepted global enum.

| Profile or family | Current identity | Must preserve | Must not become |
|---|---|---|---|
| Public-safe smoke profile | `static_survey` | Survey/source identity, MUKEY/COKEY/CHKEY lineage where applicable, vintage, scale, geometry support, and evidence references | Current field condition, parcel truth, station reading, satellite grid, or modeled output |
| Public-safe smoke profile | `station_observation` | Station identity at an approved public-safe precision, depth, unit, observation time, source timezone, QA/QC, uncertainty, and deduplication identity | Area-wide or parcel-wide condition |
| Station moisture profile | `station_soil_moisture` | The station-specific requirements above and the profile's exact finite validation behavior | An alias for every station or moisture support type |
| Public-safe smoke profile | `satellite_grid` | Grid and source identity, spatial support, acquisition/valid time, quality, uncertainty, and released transform | Station, field, in-situ, or raw observation truth |
| SMAP L4 profile | `satellite_grid_soil_moisture` | Model-assimilation role, grid identity, surface/root-zone distinction, cadence, QA, uncertainty, and non-release posture | Raw satellite observation or station truth |
| Public-safe smoke profile | `modeled_derivative` | Derivation specification, upstream digests, method, units, uncertainty, version, and temporal scope | Observation, authoritative static survey, or professional determination |

Existing Soil documentation also uses richer terms for gridded derivatives,
profiles, pedons, reference stations, and interpretations. Until one semantic
contract, canonical schema, compatibility mapping, fixtures, and finite
invalid-value behavior are accepted, do not invent aliases or collapse the
active profiles into a new public vocabulary.

Cross-lane impact must remain explicit:

| Soil change | Potential dependent lane | Required review question |
|---|---|---|
| Static survey or MUKEY-bearing support | Agriculture, Hydrology, Geology | Do dependent joins preserve identity, source role, time, and evidence? |
| Station or satellite moisture support | Agriculture, Hydrology, Habitat | Are station, grid, model, and area claims still separated? |
| Soil substrate or profile context | Habitat, Flora, Fauna, Archaeology | Could restoration expose sensitive or overly precise location context? |
| Suitability or erosion derivative | Agriculture, Hazards, Settlements/Infrastructure | Is the derivative being mistaken for advice, compliance, hazard, or engineering authority? |
| Private field, parcel, operator, or ownership join | People/Land and public UI | Should the material remain denied, redacted, generalized, or withdrawn? |

## Procedure

### 1. Pin the evidence boundary

Record the exact commit, incident ID, affected paths, reported public surface,
time of observation, and any restricted evidence handling requirements.

The following inventory is read-only. Run it from the repository root at the
exact revision under review:

```bash
set -euo pipefail

git rev-parse HEAD

for path in \
  release/candidates/soil \
  release/manifests/soil \
  release/rollback_cards/soil \
  release/rollback/soil \
  data/proofs/soil \
  data/rollback/soil \
  data/published/soil \
  data/published/layers/soil
do
  if [[ -e "$path" ]]; then
    printf 'PRESENT\t%s\n' "$path"
    find "$path" -mindepth 1 -type f \
      ! -name README.md ! -name .gitkeep -print
  else
    printf 'MISSING\t%s\n' "$path"
  fi
done

find release/manifests -maxdepth 1 -type f \
  ! -name README.md ! -name .gitkeep -print
```

Empty output is not proof that no external deployment exists. It blocks an
in-repository release claim until external identity, resolver state, and
governed records are reconciled.

### 2. Confirm release status

Before classifying rollback, verify all of the following:

1. the affected reference resolves to the accepted `ReleaseManifest` profile;
2. the manifest is not a documentation-inventory placeholder;
3. every declared artifact exists and matches its digest;
4. the governed resolver is proven to select this exact immutable release;
5. the public surface observed by the reporter is downstream of that resolver;
6. source, evidence, policy, review, rights, sensitivity, correction, and
   rollback references resolve at the required consequence level.

When any item is unresolved, select `HOLD`, `WITHDRAWAL_CANDIDATE`, or `ERROR`
as supported. Do not continue as though a release was proven.

### 3. Classify the defect and blast radius

Select one schema reason code. Record affected Soil identities, support
profiles, geography, depth, time kinds, artifacts, and consumers without
including restricted coordinates or private operational detail in public logs.

For the current candidate profile, classify each affected carrier using one or
more of:

- `API_CACHE`
- `CDN`
- `TILES`
- `CATALOG`
- `TRIPLETS`
- `SEARCH_INDEX`
- `VECTOR_INDEX`
- `AI_CACHE`
- `DOWNSTREAM_DERIVATIVES`

The list must be sorted and unique. When current deployment evidence identifies
a carrier that the profile cannot represent, stop and change the governed
contract rather than silently omitting it.

### 4. Select rollback, withdrawal, hold, or error

Choose `ROLLBACK_CANDIDATE` only after the affected and target releases verify
independently. When no safe prior target exists, use
`WITHDRAWAL_CANDIDATE` or `HOLD`; do not restore an unverified version.

For rights, sensitivity, security, private-property, Tribal or cultural,
harmful-precision, or active exposure concerns, route immediate containment to
the applicable authorized incident process. This runbook prepares the
governed record and review handoff but performs no live disablement.

### 5. Assemble a non-executing `RollbackCard` candidate

Use the current generic contract, schema, valid fixtures, and validator as the
candidate profile. A schema-valid `RollbackCard` requires all of these
top-level fields:

- `object_type`
- `schema_version`
- `id`
- `version`
- `spec_hash`
- `disposition`
- `trigger`
- `affected_release_ref`
- `target`
- `evidence_bundle_refs`
- `policy_decision_refs`
- `review_record_refs`
- `correction_notice_ref`
- `invalidations`
- `restoration`
- `timing`
- `lineage`
- `governance`

Preserve these current invariants:

- `object_type` is `RollbackCard` and `schema_version` is `1.0.0`;
- `spec_hash` is a non-placeholder `sha256:` digest;
- populated reference and invalidation arrays are sorted and unique;
- a rollback candidate uses target mode `PRIOR_RELEASE`, names a distinct prior
  release, and has non-empty evidence and policy references;
- withdrawal uses target mode `WITHDRAWAL`; hold and error use the profile's
  required hold target semantics;
- the restoration reference matches the prior-release target;
- a required public notice has a correction reference;
- detection, decision, and effective times are timezone-aware and ordered;
- lineage does not self-reference; and
- all candidate governance effects remain false, with
  `governance.release_ref: null`.

No Soil-specific rollback-card location is established at the pinned snapshot.
Use a review location approved by the owning release steward or validate a
local review file without adding it to a canonical lane. Do not create a new
parallel release, schema, policy, proof, or receipt home from this runbook.

### 6. Run bounded validation

Run the exact commands in [Validation commands](#validation-commands). Record:

- repository SHA;
- command;
- environment boundary;
- exit code;
- finite result;
- complete findings;
- skipped or held checks; and
- confirmation that no live action occurred.

`PASS` means only that the exact bounded profile passed. Preserve `FAIL`,
`HOLD`, `ABSTAIN`, `DENY`, and `ERROR` without rewriting them as success.

### 7. Prepare the accountable handoff and stop

Attach the packet below to accountable reviewers. CODEOWNERS routes GitHub
review but does not prove Soil, evidence, rights, sensitivity, policy,
correction, release, rollback, public-surface, or independent approval.

Stop here. No command in this runbook authorizes source activation, policy
activation, target selection, signature creation, correction publication,
external invalidation, alias mutation, release transition, deployment,
republication, or public communication.

## Validation commands

Run from the repository root at the exact revision under review.

### Bounded Soil fixture profiles

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_smoke.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_soil_moisture_qc.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/soil/test_smap_l4_anti_collapse.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest tests.ingest.ssurgo_watch.test_ssurgo_watch --verbose
```

These commands exercise synthetic public-safe, station, SMAP L4, and SSURGO
package-drift fixtures only. They do not validate a release or rollback.

### Generic `RollbackCard` candidate profile

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose

python tools/validators/release/validate_rollback_card.py --fixtures
```

To validate one proposed card without mutating state:

```bash
python tools/validators/release/validate_rollback_card.py \
  <path-to-proposed-rollback-card.json>
```

The validator emits `PASS` or `FAIL` for candidate shape and local consistency.
It does not resolve live references, authenticate actors, evaluate operational
policy, select a target, execute rollback, or publish.

### Generic synthetic rehearsal regression

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal \
  tests.domains.hazards.test_synthetic_rollback_rehearsal
```

The current rollback-drill workflow expects twelve non-vacuous tests. This is a
generic and Hazards rehearsal, not a Soil rollback drill. Its helper is
deliberately restricted to marker-protected synthetic workspaces. Do not run
the helper against the repository, staging, production, published, or
externally mounted state, and do not generalize its `--apply` behavior to a
production procedure.

## Result interpretation

| Observation | Meaning | Required response |
|---|---|---|
| Soil fixture command passes | The named synthetic Soil profile passed at the recorded SHA | Keep truth, admission, proof, policy, release, and rollback claims bounded |
| `RollbackCard` validator `PASS` | Candidate shape and local consistency passed | Continue accountable review; do not mutate state |
| Validator `FAIL` | One or more schema or semantic findings exist | Correct the packet or select a truthful negative disposition |
| `ROLLBACK_CANDIDATE` | A distinct prior safe release is proposed | Handoff only; no execution |
| `WITHDRAWAL_CANDIDATE` | Public exposure should be reviewed for withdrawal without a safe target | Handoff to authorized operators and reviewers |
| `HOLD` | A required fact, support object, or authority is unresolved | Preserve uncertainty and stop |
| `ERROR` | Inputs or tooling could not produce a valid evaluation | Repair before reliance |
| Generic synthetic rehearsal passes | Isolated history-preservation and invalidation behavior passed | Do not claim Soil or production readiness |
| `rollback-drill` is green | The workflow's current holds and synthetic checks matched expectations | Production rollback remains held |
| `domain-soil` is green | The four bounded Soil profiles and explicit proof/release holds matched expectations | No Soil release, proof, or rollback is established |

## Handoff packet

The review packet must contain:

- [ ] incident ID, author, timestamp, exact Git revision, and handling class;
- [ ] affected release reference, manifest digest, artifact inventory, and proof
      that the governed public resolver selects it;
- [ ] trigger reason code, defect scope, Soil identities, support profiles,
      geography, depth, time, quality, and uncertainty;
- [ ] source, EvidenceBundle, rights, sensitivity, policy, validation, proof,
      and review references;
- [ ] exact target release and digest closure, or an explicit withdrawal/hold
      reason;
- [ ] proposed `RollbackCard` candidate and complete validator output;
- [ ] correction or withdrawal reference and public-notice requirement;
- [ ] affected carrier and cross-lane derivative inventory;
- [ ] invalidation, stale-state, correction-display, and post-change
      verification plan;
- [ ] preservation plan for affected and target manifests, artifacts, evidence,
      and lineage;
- [ ] accountable reviewer identities, scoped authority evidence, recusal, and
      separation-of-duties status;
- [ ] public-safe communication plan that exposes no restricted detail;
- [ ] finite disposition: `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`,
      or `ERROR`; and
- [ ] explicit statement that no live mutation occurred during this procedure.

## Definition of done

This readiness pass is complete when:

1. the exact evidence boundary is pinned;
2. release status is proven or the absence is recorded;
3. the defect, support profiles, carriers, and cross-lane dependencies are
   classified;
4. the candidate passes bounded validation or returns a truthful negative
   result;
5. the accountable handoff packet is complete; and
6. no unauthorized source, lifecycle, release, correction, rollback,
   deployment, or publication action occurred.

A production rollback is **not** complete merely because this runbook was
followed. Production completion remains held until an accepted executor,
authenticated actors and target, active policy evaluation, accountable review,
durable execution and invalidation receipts, governed resolver transition,
post-change verification, correction visibility, and rollback-of-rollback path
are independently implemented and proven.

## Open verification register

| ID | Question | Current status |
|---|---|---|
| SOIL-RB-001 | Which exact Soil release and governed public resolver would be affected? | No release-grade Soil instance observed; `HOLD` |
| SOIL-RB-002 | Who holds accountable Soil, source, scientific, evidence, rights, sensitivity, policy, correction, release, rollback, and independent-review authority? | `NEEDS VERIFICATION` |
| SOIL-RB-003 | Which accepted policy bundle and governed consumers enforce Soil rollback obligations? | Policy and runtime binding not established |
| SOIL-RB-004 | Where should a Soil-specific RollbackCard instance live under the accepted release responsibility root? | No Soil sublane observed; do not create one from this runbook |
| SOIL-RB-005 | Which accepted signature, actor-identity, and review mechanism authorizes a live transition? | Candidate-only and proposed governance surfaces; operational authority held |
| SOIL-RB-006 | Which production executor writes rollback and invalidation receipts and changes the governed resolver atomically? | Production pipeline placeholder |
| SOIL-RB-007 | Which Soil-specific fixtures prove manifest, MUKEY/COKEY/CHKEY, station, SMAP, map, API, Evidence Drawer, export, search, and AI invalidation? | No Soil-specific rollback rehearsal verified |
| SOIL-RB-008 | How are dependent Agriculture, Hydrology, Geology, Habitat, Flora, Fauna, Hazards, and People/Land releases located and marked? | `NEEDS VERIFICATION` |
| SOIL-RB-009 | Which support-type vocabulary and compatibility mapping are accepted across the active Soil profiles? | Profile-local vocabularies remain distinct |
| SOIL-RB-010 | Which checks and independent approvals are required by repository rules for a rollback-significant change? | `NEEDS VERIFICATION` |

## Documentation maintenance

Re-review this runbook when any of these facts change:

- a release-grade Soil candidate, manifest, rollback card, proof artifact,
  published payload, correction, withdrawal, or execution receipt appears;
- the generic `RollbackCard` contract, schema, validator, fixtures, tests, or
  workflow changes;
- a Soil-specific rollback rehearsal or accepted production executor appears;
- source-role, support-profile, MUKEY/COKEY/CHKEY, time, depth, quality,
  uncertainty, rights, sensitivity, or public-safe scale rules change;
- an accepted policy, actor identity, stewardship assignment, signature, or
  separation-of-duties mechanism becomes operational;
- a governed resolver, invalidation adapter, deployment path, or public carrier
  is proven; or
- related paths move or are superseded under an accepted ADR or migration.

Update current-state claims from exact repository evidence. Do not promote a
README, fixture, placeholder, workflow, green check, or generated record into
release authority.

## Rollback of this document

Before merge, close the draft pull request and discard only its feature branch.
After merge, revert the documentation commit or submit a reviewed forward
correction. Either action changes documentation only; it does not select a
release target, restore data, invalidate a cache, mutate a resolver, execute a
rollback, deploy, publish, communicate an incident, or activate a source.

## Related responsibility roots

- [Local Soil runbook boundary](./README.md)
- [Bounded Soil validation](./NO_NETWORK_TEST_RUNBOOK.md)
- [Soil promotion preflight](./PROMOTION_RUNBOOK.md)
- [Soil source-refresh planning](./SOURCE_REFRESH_RUNBOOK.md)
- [Soil domain boundary](../../domains/soil/README.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Lifecycle law](../../doctrine/lifecycle-law.md)
- [Trust membrane](../../doctrine/trust-membrane.md)
- [Generic `RollbackCard` contract](../../../contracts/release/rollback_card.md)
- [Generic `RollbackCard` schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Generic `RollbackCard` fixtures](../../../fixtures/release/rollback_card/)
- [Generic `RollbackCard` validator](../../../tools/validators/release/validate_rollback_card.py)
- [Generic `RollbackCard` tests](../../../tests/validators/test_validate_rollback_card.py)
- [Soil domain workflow](../../../.github/workflows/domain-soil.yml)
- [`RollbackCard` workflow](../../../.github/workflows/rollback-card.yml)
- [Rollback-drill readiness workflow](../../../.github/workflows/rollback-drill.yml)
- [Soil candidate boundary](../../../release/candidates/soil/README.md)
- [Release manifest boundary](../../../release/manifests/README.md)
- [Rollback-card boundary](../../../release/rollback_cards/README.md)
- [Rollback review boundary](../../../release/rollback/README.md)
- [Soil data-plane rollback boundary](../../../data/rollback/soil/README.md)
- [Soil proof boundary](../../../data/proofs/soil/README.md)
- [Soil published-data boundary](../../../data/published/soil/README.md)
- [Soil published-layer boundary](../../../data/published/layers/soil/README.md)

[Back to top](#top)
