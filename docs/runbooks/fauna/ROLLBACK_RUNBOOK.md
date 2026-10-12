<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/rollback
title: Fauna Rollback Runbook
type: operational-runbook
version: v2.0.0
status: DRAFT_REPOSITORY_GROUNDED; DECISION_AND_REVIEW_HANDOFF_ONLY; SHARED_SYNTHETIC_REHEARSAL_AVAILABLE; FAUNA_TABLETOP_AVAILABLE; FAUNA_INTEGRATED_REHEARSAL_ABSENT; OPERATIONAL_ROLLBACK_HELD; SENSITIVE_LOCATION_FAIL_CLOSED; NON_RELEASE; NON_PUBLICATION; NOT_FOR_LIFE_SAFETY
owners: "@bartytime4life — verified CODEOWNERS route only; accountable Fauna, taxonomy, source, rights, sensitivity, geoprivacy, evidence, policy, review, correction, rollback, release, operations, security, and public-recovery assignments NEEDS VERIFICATION"
created: 2026-05-13
updated: 2026-08-28
policy_label: repository-facing; fauna; rollback; withdrawal; correction-aware; sensitive-location; synthetic-proof-bounded; fail-closed; non-publisher
current_path: docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
owning_root: docs/
path_authority: same-path modernization under accepted ADR-0029 and Directory Rules v2
responsibility: Classify a defective Fauna release-facing surface, prepare a bounded rollback, withdrawal, hold, error, or forward-correction review handoff, and stop before any operational or public mutation.
truth_posture: cite-or-abstain
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 6e02ced04834c8f9f2210da8c655cdef626a3b08
  target_path: docs/runbooks/fauna/ROLLBACK_RUNBOOK.md
  target_prior_blob: d8d7d3bb9c40d3de50d484e6d13640bee5baaa58
  lane_readme_prior_blob: 5989e996d317cace6d63c0fc6b22c2cdf9f0c207
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  rollback_drill_blob: 78a0c3663ef30e5edb9260c0c5ab58d6e7f860fb
  rollback_card_contract_blob: c6d3c35c56b064e04c3a2532f4709d938d7b0c1a
  rollback_card_schema_blob: e0a9edf02dd5d6997eda60a054a5bf19636c3dd4
  rollback_card_validator_blob: 9e9ed5a92851935b41a36698e4bead13ef4edf57
  rollback_card_validator_test_blob: c8aeac6348127fb768981e2b5b5588c6a7bdeb78
  synthetic_rehearsal_helper_blob: a8f6bff350e79b453f425ebce9a9ded6801f8944
  synthetic_rehearsal_test_blob: b644ca6c4185b3f81bc339c077eae85299833261
  rollback_drill_workflow_blob: 2d0c39fc6ff8e44bd9cf753ce546475079e8ffd5
  fauna_rollback_schema_stub_blob: 08b82778b3654ab7643a12770bdcb976eb12e9ff
  fauna_rollback_test_lane_blob: 28853dc37d00981a405613f43b1860d5500db6bb
  fauna_release_candidate_lane_blob: 653277efe3a44a96c29af481a73d7d90c41443ce
  fauna_release_rollback_lane_blob: 7dbf5b5b93cb9a4b90b1f2270691a4069389e50f
  fauna_data_rollback_lane_blob: e25a89750b448d902271d824fdad9273929c2748
  fauna_proof_lane_blob: 70c2501e6d7c8ff4beeae7577fde9acd6b720b2e
  fauna_receipt_lane_blob: c201b0d9c5882451ac31bd7c1ad725b98b635aad
  fauna_published_layer_lane_blob: 571f90883e51558971ef639400bc6fef4b77405b
  fauna_rollback_pipeline_lane_blob: 0eeeab638bbfcced8da7afddf3c8b076442ae96f
source_lineage:
  - title: KFM_Fauna_Architecture_PDF_Only_Report.pdf
    source_class: PLANNING_LINEAGE
    use: Preserve fauna source-role, sensitivity, geoprivacy, evidence, correction, and rollback framing only; its no-repository assumptions do not describe current implementation.
  - title: KFM Evidence, Documentation & Ideas Atlas — 2026-08-24
    source_class: NOTION_COORDINATION_ONLY
    use: Keep implementation, review, merge, rollback authorization, execution, release, deployment, promotion, and publication as separate states.
  - title: KFM Markdown Update & Modernization Agent v1.0
    source_class: CURRENT_TASK_GUIDANCE
    use: Same-path repository-grounded Markdown modernization and focused draft-pull-request delivery.
related:
  - docs/runbooks/fauna/README.md
  - docs/runbooks/fauna/ROLLBACK_DRILL.md
  - docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - docs/runbooks/fauna/PUBLICATION_GATE_DRY_RUN.md
  - docs/runbooks/fauna/SENSITIVE_OCCURRENCE_REVIEW.md
  - docs/runbooks/fauna/NO_NETWORK_TEST_RUNBOOK.md
  - docs/domains/fauna/README.md
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/POLICY.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/runbooks/rollback-rehearsal.md
  - contracts/release/rollback_card.md
  - schemas/contracts/v1/release/rollback_card.schema.json
  - schemas/contracts/v1/domains/fauna/rollback_card.schema.json
  - fixtures/release/rollback_card/
  - tools/validators/release/validate_rollback_card.py
  - tools/release/rollback_apply.py
  - tests/validators/test_validate_rollback_card.py
  - tests/release/test_synthetic_rollback_rehearsal.py
  - tests/domains/fauna/release/rollback/README.md
  - .github/workflows/rollback-drill.yml
  - release/candidates/fauna/README.md
  - release/rollback/fauna/README.md
  - release/rollback_cards/README.md
  - data/rollback/fauna/README.md
  - data/proofs/fauna/README.md
  - data/receipts/fauna/README.md
  - data/published/layers/fauna/README.md
  - pipelines/rollback/fauna/README.md
notes:
  - The repository implements a closed, fixture-first shared RollbackCard candidate profile and a deterministic marker-protected synthetic rollback/withdrawal rehearsal.
  - The shared profile proves candidate shape and local consistency only. Its governance flags remain false and release_ref remains null.
  - The Fauna Rollback Drill adds a domain tabletop and public-safety review, but direct Fauna rollback fixtures, tests, an executor, an accepted target, and operational authority remain absent.
  - The Fauna-specific rollback-card schema remains a permissive id-only greenfield stub and must not be used as operational proof.
  - The helper's optional report path is caller-controlled and is not confined to the synthetic workspace.
  - Scenario-derived correction and invalidation paths can replace existing files on collision; append-only synthetic history is not established.
  - Fauna candidate, rollback, proof, and data-plane rollback roots contain README or placeholder material rather than an accepted Fauna rollback instance.
  - Published Fauna delivery lanes exist in the repository; their presence does not prove current public deployment, safe target identity, or operational read-back.
  - This runbook prepares classification and review evidence only. It never performs containment, withdrawal, rollback, correction, alias mutation, invalidation, release, deployment, promotion, or publication.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Rollback Runbook

> **One-line purpose.** Classify a defective Fauna release-facing surface, prepare a public-safe rollback, withdrawal, hold, error, or forward-correction handoff, and stop before any source, lifecycle, alias, consumer, release, deployment, promotion, or publication mutation.

[![Operational rollback: held](https://img.shields.io/badge/operational%20rollback-HOLD-b42318?style=flat-square)](#current-disposition)
[![Shared synthetic rehearsal: available](https://img.shields.io/badge/shared%20synthetic%20rehearsal-available-8250df?style=flat-square)](#shared-synthetic-rehearsal)
[![Fauna integrated proof: absent](https://img.shields.io/badge/Fauna%20integrated%20proof-absent-b42318?style=flat-square)](#fauna-integrated-rehearsal-gap)
[![Sensitive locations: fail closed](https://img.shields.io/badge/sensitive%20locations-fail%20closed-b42318?style=flat-square)](#fauna-safety-and-source-role-boundary)
[![Public effect: none](https://img.shields.io/badge/public%20effect-none-6e7781?style=flat-square)](#authority-and-terminal-boundary)

> [!WARNING]
> **KFM is not an official wildlife, law-enforcement, hunting, veterinary, legal-status, regulatory, disease-response, emergency, or life-safety authority.** Do not use this procedure to issue or replace agency determinations, operational instructions, enforcement actions, disease-control directions, harvest rules, or protective guidance. Direct current and authoritative decisions to the responsible issuing agency or steward.

<a id="current-disposition"></a>

> [!IMPORTANT]
> **Current disposition: `SHARED_SYNTHETIC_REHEARSAL_AVAILABLE / FAUNA_TABLETOP_AVAILABLE / FAUNA_INTEGRATED_REHEARSAL_ABSENT / OPERATIONAL_FAUNA_ROLLBACK_HOLD`.** The repository can validate shared `RollbackCard` candidates, run eight generic marker-protected synthetic rollback and withdrawal tests, and perform the public-safe Fauna tabletop defined in [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md). It does not establish an affected Fauna release, a safe prior target, a schema-valid Fauna `RollbackCard` instance, accepted Fauna rollback policy, accountable approval, an operational executor, public-alias mutation, downstream invalidation adapters, or independent public read-back.

```yaml
work_state: HOLD
available_evidence:
  - SHARED_ROLLBACKCARD_FIXTURE_PROFILE
  - SHARED_ROLLBACKCARD_EXPLICIT_CANDIDATE_VALIDATION
  - SHARED_MARKER_PROTECTED_SYNTHETIC_PLAN_AND_APPLY
  - EIGHT_GENERIC_ROLLBACK_AND_WITHDRAWAL_TESTS
  - FAUNA_PUBLIC_SAFE_TABLETOP_AND_HANDOFF
missing_evidence:
  - FAUNA_AFFECTED_RELEASE_NOT_ESTABLISHED
  - FAUNA_PRIOR_SAFE_TARGET_NOT_ESTABLISHED
  - FAUNA_ROLLBACKCARD_INSTANCE_NOT_ESTABLISHED
  - FAUNA_POLICY_EXECUTION_NOT_BOUND
  - FAUNA_ACCOUNTABLE_REVIEW_NOT_ESTABLISHED
  - FAUNA_INTEGRATED_FIXTURE_AND_TEST_PROFILE_ABSENT
  - FAUNA_OPERATIONAL_EXECUTOR_ABSENT
  - FAUNA_PUBLIC_ALIAS_AUDITOR_NOT_OPERATIONAL
  - FAUNA_INVALIDATION_ADAPTERS_NOT_ESTABLISHED
  - FAUNA_PUBLIC_RECOVERY_READBACK_NOT_ESTABLISHED
  - SYNTHETIC_REPORT_PATH_CONFINEMENT_ABSENT
  - SYNTHETIC_COLLISION_SAFE_PERSISTENCE_ABSENT
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
```

**Quick navigation:** [Goal](#goal-and-scope) · [Authority](#authority-and-terminal-boundary) · [Evidence](#current-repository-evidence) · [Vocabulary](#state-and-vocabulary-separation) · [Safety](#fauna-safety-and-source-role-boundary) · [Decision](#rollback-decision-model) · [Preconditions](#preconditions) · [Procedure](#rollback-preflight-and-review-handoff) · [Target](#prior-target-safety) · [Invalidation](#invalidation-and-cross-lane-impact) · [Synthetic rehearsal](#shared-synthetic-rehearsal) · [Results](#interpret-the-results) · [Handoff](#accountable-review-handoff-packet) · [Gap](#fauna-integrated-rehearsal-gap) · [Graduation](#operational-graduation-gate) · [Validation](#documentation-validation) · [Related](#related-repository-surfaces) · [Maintenance](#maintenance-and-document-rollback)

---

<a id="goal-and-scope"></a>

## Goal and scope

Use this runbook when a released or release-facing Fauna carrier may be defective and maintainers need a bounded answer to this question:

> Is there enough exact, current, public-safe support to prepare a rollback candidate, withdrawal candidate, hold, error record, or forward-correction handoff—and what must remain unchanged until accountable review and operational authority exist?

The intended governed circle is:

```text
defect signal
  -> public-safe incident summary and containment request
  -> exact affected release, artifact, claim, source-role, time, and consumer freeze
  -> rollback / withdrawal / hold / error / forward-correction classification
  -> evidence, taxonomy, identity, rights, sensitivity, policy, review, and target assessment
  -> RollbackCard candidate validation where applicable
  -> shared synthetic-mechanics rehearsal
  -> Fauna tabletop and accountable review handoff
  -> separately authorized operational execution
  -> invalidation, read-back, correction, receipts, proofs, and closure
```

Current repository evidence supports classification, shared candidate validation, generic synthetic mechanics, a Fauna tabletop, and review handoff only.

### In scope

- Pin the exact repository revision and identify the affected release reference, artifact digests, public claims, source roles, spatial and temporal scope, and known consumers.
- Distinguish rollback, withdrawal, hold, error, and forward correction without silently translating between them.
- Preserve public versus restricted occurrence separation and prevent exact or reverse-engineerable sensitive wildlife detail from entering review packets.
- Recheck the prior target under current taxonomy, source, rights, sensitivity, geoprivacy, evidence, policy, review, and compatibility controls.
- Validate the shared `RollbackCard` fixture matrix and the actual candidate file prepared for review.
- Run the repository's shared marker-protected synthetic rehearsal as a mechanics check.
- Inventory all invalidation classes and cross-lane effects without executing them.
- Produce a public-safe handoff that keeps review, authorization, execution, release, deployment, promotion, and publication separate.

### Out of scope

This runbook does not:

- expose or process real exact sensitive locations, telemetry paths, observer identity, private-land joins, steward-restricted records, transform parameters, credentials, or protected source excerpts;
- issue or interpret a legal, regulatory, conservation-status, hunting, disease-response, emergency, or life-safety determination;
- activate, admit, fetch, alter, or withdraw a live source;
- create a Fauna release, prior safe target, EvidenceBundle, proof, receipt, policy decision, review record, correction notice, or operational rollback authority;
- mutate `data/published/`, an alias, API route, CDN, tile store, catalog, triplet store, search index, vector index, AI cache, Evidence Drawer, Focus Mode response, or deployed runtime;
- treat the shared helper, the Hazards workflow extension, or a green workflow as integrated Fauna rollback proof;
- execute repository revert, database recovery, infrastructure failover, source deactivation, secret rotation, incident command, release, deployment, promotion, or publication.

[Back to top](#top)

---

<a id="authority-and-terminal-boundary"></a>

## Authority and terminal boundary

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../doctrine/directory-rules.md) bytes. Human procedures remain under `docs/runbooks/`; semantic meaning remains under `contracts/`; machine shape under `schemas/`; policy under `policy/`; executable helpers under `tools/` and `pipelines/`; behavioral evidence under `tests/`; lifecycle, receipt, and proof artifacts under `data/`; and release decisions under `release/`.

This is a same-path modernization of an established file. It creates no new root, schema home, release family, rollback record, proof home, receipt home, pipeline, public carrier, or authority surface.

| Responsibility | Owning surface | Current bounded role |
|---|---|---|
| Human Fauna rollback procedure | This file | Classification, prerequisites, bounded commands, result interpretation, and review handoff |
| Fauna rollback tabletop | [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) | Domain safety review layered over shared synthetic controls |
| Shared rollback meaning | [`RollbackCard` contract](../../../contracts/release/rollback_card.md) | Candidate plan and explicit non-authority semantics |
| Shared machine shape | [release `RollbackCard` schema](../../../schemas/contracts/v1/release/rollback_card.schema.json) | Closed `1.0.0` candidate shape |
| Fauna schema stub | [Fauna `rollback_card` schema](../../../schemas/contracts/v1/domains/fauna/rollback_card.schema.json) | Permissive greenfield stub; not operational proof |
| Shared candidate validator | [`validate_rollback_card.py`](../../../tools/validators/release/validate_rollback_card.py) | Fixture profile or explicit candidate validation |
| Shared synthetic mechanics | [`rollback_apply.py`](../../../tools/release/rollback_apply.py) | Plan/apply inside marker-protected synthetic roots; optional report path is caller-controlled |
| Generic behavioral evidence | [`test_synthetic_rollback_rehearsal.py`](../../../tests/release/test_synthetic_rollback_rehearsal.py) | Eight generic rollback, withdrawal, integrity, and fail-closed tests |
| Fauna direct test lane | [`tests/domains/fauna/release/rollback/README.md`](../../../tests/domains/fauna/release/rollback/README.md) | Guidance/scaffold only; direct executable Fauna rollback proof absent |
| Fauna candidate and rollback roots | [`release/candidates/fauna/`](../../../release/candidates/fauna/README.md) and [`release/rollback/fauna/`](../../../release/rollback/fauna/README.md) | Boundary documentation; no accepted candidate or execution record established |
| Data-plane rollback support | [`data/rollback/fauna/`](../../../data/rollback/fauna/README.md) | Support-lane documentation; no operational alias mutation authority |
| Public delivery | Governed APIs and released public-safe carriers | No mutation or direct access under this procedure |

The terminal result of this runbook is one of:

```text
REVIEW_HANDOFF_READY
HOLD
ERROR
NO_ACTION
```

`REVIEW_HANDOFF_READY` means the candidate assessment is complete enough for accountable review. It does not mean rollback approved, rollback executed, public state restored, released, deployed, promoted, or published.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

This checkpoint is pinned to `main@6e02ced04834c8f9f2210da8c655cdef626a3b08`. Re-read every named surface if the revision changes.

| Surface | Confirmed repository state | Bounded conclusion |
|---|---|---|
| Target runbook before this change | Proposal-era v0.1 with placeholder owners, proposed paths, an absent `VALIDATION_RUNBOOK.md` link, and operational instructions not supported by current implementation | Requires same-path grounding |
| Fauna runbook index | Repository-grounded and explicitly identifies this file as the lone proposal-era substantive child | Index must be reconciled with this modernization |
| Shared `RollbackCard` profile | Contract, closed schema, three valid fixtures, six invalid fixtures, expected findings, implemented validator, and tests exist | Candidate shape and local consistency only |
| Shared synthetic helper | Marker-protected, synthetic-only plan/apply support with complete invalidation declaration and affected-history digest checks | Deterministic synthetic mechanics only |
| Helper write boundary | Plan has no scenario-workspace mutation; apply replaces the synthetic alias and writes correction/invalidation records; optional `--report` accepts a caller-selected path | Report-path confinement is absent; operational use prohibited |
| Synthetic record persistence | Scenario-derived correction and invalidation paths use atomic replacement | Append-only or collision-safe rehearsal history is not proved |
| Hosted rollback workflow | Runs the shared fixture profile and twelve generic-plus-Hazards tests; contains no integrated Fauna rehearsal | Hosted success is not Fauna rollback proof |
| Fauna rollback drill | Repository-grounded tabletop and shared-rehearsal procedure | Bounded `DRILL_HANDOFF_READY` evidence only |
| Fauna direct rollback test lane | README/scaffold; direct Fauna rollback tests and reusable fixtures are not established | Integrated domain proof absent |
| Fauna-specific rollback schema | `id`-required, `additionalProperties: true` greenfield stub with absent declared contract/fixtures/validator | Do not use as operational shape |
| Fauna candidate, release-rollback, data-rollback, proof, and pipeline lanes | README or placeholder-oriented lane surfaces exist | Lane presence is not a candidate, proof, execution record, or runtime |
| Root rollback-card inventory | Tracked root JSON placeholders are Agriculture and Atmosphere oriented; no Fauna card is present in the inspected root | Fauna `RollbackCard` instance absent |
| Published Fauna layer lanes | Repository paths exist for Fauna delivery families | Presence does not prove deployment, current public state, or a safe rollback target |
| Accountable authority | `@bartytime4life` is the verified GitHub route; functional roles remain unverified | Routing is not approval or rollback authority |

> [!WARNING]
> Repository-tracked absence of a Fauna rollback record does not prove that no external, deployed, cached, or otherwise operational Fauna state exists. Deployed-state inventory and independent read-back remain separate evidence requirements.

[Back to top](#top)

---

<a id="state-and-vocabulary-separation"></a>

## State and vocabulary separation

Do not collapse the vocabularies below.

| Vocabulary | Finite values | Meaning |
|---|---|---|
| `RollbackCard.disposition` | `ROLLBACK_CANDIDATE`, `WITHDRAWAL_CANDIDATE`, `HOLD`, `ERROR` | Candidate recovery classification |
| Work state | `HOLD`, `READY_FOR_REVIEW`, `BLOCKED`, `NO_ACTION` | Coordination state, not a schema field unless an owning contract says so |
| Validator result | `PASS`, `FAIL` | Bounded check result |
| Shared rehearsal result | `PASS` or helper `HOLD` with reason code | Synthetic mechanics result |
| Governed runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Public/API response behavior; not a rollback disposition |
| Drill result | `DRILL_HANDOFF_READY`, `HOLD`, `ERROR` | Fauna tabletop/rehearsal handoff state |
| Lifecycle/release state | Candidate, reviewed, released, withdrawn, superseded, or other owning-contract value | Governed state outside this runbook |

A sensitivity or rights issue may require an operational `DENY` response while the rollback candidate remains `HOLD` or `WITHDRAWAL_CANDIDATE`. Those facts can coexist; they must not be normalized into one invented vocabulary.

[Back to top](#top)

---

<a id="fauna-safety-and-source-role-boundary"></a>

## Fauna safety and source-role boundary

Fauna rollback is high-consequence because a recovery target can reintroduce an older sensitivity, rights, taxonomy, or role defect.

Preserve these boundaries:

- A taxonomic mapping is not an occurrence, legal status, conservation status, range, abundance estimate, habitat assignment, or release decision.
- An occurrence is not a range polygon, absence claim, population estimate, habitat-suitability claim, disease conclusion, mortality cause, or regulatory determination.
- Public and restricted occurrence families remain distinct.
- Exact or reverse-engineerable nests, dens, roosts, hibernacula, spawning/breeding or aggregation sites, telemetry and movement traces, observer-linked records, steward-controlled detail, private-land joins, and transform parameters fail closed.
- Style filters, opacity, popup suppression, or client-only hiding are not geoprivacy transforms. Sensitive bytes must not be present in a public-safe carrier.
- Source roles remain explicit across direct observation, checklist/event data, specimen or collection record, agency/legal record, model or derived surface, and contextual material.
- A public endpoint or public repository path does not establish redistribution rights.
- Historical review, rights, or sensitivity clearance does not automatically remain valid for a prior target.
- AI, maps, tiles, indexes, graphs, receipts, tests, and prose remain subordinate to evidence, policy, review, and release state.

During a suspected exposure, prepare a public-safe containment request through the responsible operational and official-authority path. This runbook records the request and the known scope; it does not execute disablement.

[Back to top](#top)

---

<a id="rollback-decision-model"></a>

## Rollback decision model

Use the strongest supported classification without forcing a rollback.

| Condition | Candidate posture | Required next step |
|---|---|---|
| Corrected successor can use the normal governed promotion path and current public state can remain safely held | Forward correction | Use the promotion/correction path; preserve rollback readiness |
| Distinct prior release is immutable, digest-verifiable, currently admissible, evidence-supported, taxonomy-compatible, rights-cleared, sensitivity-safe, reviewable, and consumer-compatible | `ROLLBACK_CANDIDATE` | Prepare and validate the exact candidate; stop before execution |
| Current carrier must leave public use and no safe prior target exists | `WITHDRAWAL_CANDIDATE` | Prepare withdrawal/correction review and expected public non-answer |
| Evidence, target, rights, sensitivity, taxonomy, policy, review, actor, executor, alias, invalidation, or read-back is unresolved | `HOLD` | Name every blocker and preserve history |
| Input is malformed, contradictory, unsafe to inspect, or cannot produce a valid evaluation | `ERROR` | Record a public-safe reason code and no state change |
| The signal is stale-only, already corrected, outside Fauna ownership, or produces no affected public state | `NO_ACTION` or route elsewhere | Record why rollback is not the correct mechanism |

Use the trigger reason codes defined by the shared contract rather than the proposal-era custom enumeration. Current codes include `RELEASE_DEFECT`, `EVIDENCE_CONTRADICTION`, `RIGHTS_CHANGE`, `SENSITIVITY_DISCOVERY`, `VALIDATION_FAILURE`, `SOURCE_WITHDRAWAL`, `POLICY_FAILURE`, `SECURITY_ISSUE`, `OPERATIONAL_FAILURE`, `EMERGENCY_HOLD`, `INSUFFICIENT_EVIDENCE`, and `INPUT_INVALID`.

[Back to top](#top)

---

<a id="preconditions"></a>

## Preconditions

Before preparing a candidate, establish the following for one exact affected release and one exact repository revision.

### Affected state

- [ ] Affected release reference and immutable manifest identity.
- [ ] Artifact digests, public audience, release time, spatial/time scope, and source-role inventory.
- [ ] Exact affected claims, layer IDs, API surfaces, Evidence Drawer payloads, Focus Mode support, exports, caches, indexes, and cross-lane derivatives.
- [ ] Public-safe incident summary that contains no protected detail.
- [ ] Defect signal, detection time, reporter channel, and source of authority.

### Support and policy

- [ ] Evidence references resolve through the accepted evidence path.
- [ ] Source IDs, product versions, native identifiers, taxonomy snapshot, and source roles are explicit.
- [ ] Current rights, terms, attribution, access, and approved-purpose constraints are established.
- [ ] Current sensitivity, geoprivacy transform, harmful-precision, and public/restricted conversion controls are established.
- [ ] Current policy bundle and accountable review requirements are identified.
- [ ] Correction/notice requirements and public status behavior are identified.

### Target and execution boundary

- [ ] Distinct prior target identified, or withdrawal/hold selected explicitly.
- [ ] Prior target rechecked under current evidence, taxonomy, rights, sensitivity, policy, review, and consumer compatibility.
- [ ] Required invalidation classes and downstream owners enumerated.
- [ ] Qualified accountable roles and separation of duties identified.
- [ ] Operational executor, alias profile, concurrency control, receipt, and read-back path identified—or named as blockers.
- [ ] Rollback of the documentation change is separate from operational rollback.

If a prerequisite is missing, stop at `HOLD`. Do not fill the gap with a plausible path, owner, source role, sensitivity transform, or prior release.

[Back to top](#top)

---

<a id="rollback-preflight-and-review-handoff"></a>

## Rollback preflight and review handoff

### Step 1 — Freeze the exact question and evidence

Record:

- repository and exact commit;
- affected release reference and manifest digest;
- public-safe description of the suspected defect;
- affected object families, source roles, time and geography;
- known public carriers and governed consumers;
- overlap with open branches or pull requests;
- requested terminal boundary.

Do not copy restricted payloads, exact locations, private review content, credentials, or secret-bearing URLs into the issue, pull request, candidate, log, or handoff.

### Step 2 — Request containment where required

For a sensitivity, rights, security, or policy signal, record the required operational containment and route it to the accountable operational/official authority. Until execution is proven, describe containment as `REQUESTED`, `UNKNOWN`, or `HOLD`—never as completed.

### Step 3 — Classify the candidate posture

Apply the decision model above. Record one `RollbackCard` disposition only when preparing a `RollbackCard`. Keep forward correction, runtime `DENY`/`ABSTAIN`, incident severity, and work-state labels in their own fields.

### Step 4 — Assess the prior target under current controls

Use [Prior target safety](#prior-target-safety). A target that passed an older policy or review is not automatically safe today. Missing current support yields `HOLD`; a target prohibited by current policy yields withdrawal or denial through the owning policy/runtime surface, not a fabricated rollback disposition.

### Step 5 — Prepare the actual candidate

Use the shared [`RollbackCard` contract](../../../contracts/release/rollback_card.md) and closed schema. Do not use the permissive Fauna schema stub.

A review candidate must:

- use one finite disposition;
- name the exact affected release;
- name a distinct prior release only for `ROLLBACK_CANDIDATE`;
- include sorted, unique evidence, policy, review, and invalidation references;
- require validation of the restored target;
- link a correction notice when public notice is required;
- preserve time ordering and non-self lineage; and
- keep every governance flag false with `release_ref: null`.

### Step 6 — Validate fixtures and the actual candidate

From a clean checkout at the exact revision:

```bash
python tools/validators/release/validate_rollback_card.py --fixtures

python tools/validators/release/validate_rollback_card.py \
  <path-to-actual-candidate.json>

python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_rollback_card.py' \
  --verbose
```

The fixture command proves the tracked positive/negative profile. It does not validate a newly prepared candidate. Run both.

### Step 7 — Run the shared synthetic mechanics check

```bash
python -m unittest -q \
  tests.release.test_synthetic_rollback_rehearsal
```

Expected current result: eight generic tests. A hosted `rollback-drill` result currently exercises twelve generic-plus-Hazards tests. Neither result proves Fauna integration.

Use [`ROLLBACK_DRILL.md`](ROLLBACK_DRILL.md) for the Fauna tabletop, public-safety review, and handoff requirements. Do not point the helper at repository lifecycle, release, or public paths.

### Step 8 — Inventory invalidations and dependencies

Use the exact shared invalidation vocabulary:

```text
API_CACHE
CDN
TILES
CATALOG
TRIPLETS
SEARCH_INDEX
VECTOR_INDEX
AI_CACHE
DOWNSTREAM_DERIVATIVES
```

For each class, identify the responsible implementation, expected action, verification/read-back, failure posture, and owner. Listing an invalidation is not executing it.

### Step 9 — Prepare accountable review handoff

Attach:

- exact revision, candidate path/digest, commands, results, and logs;
- affected and target release identities;
- public-safe defect classification;
- evidence, policy, review, correction, rights, sensitivity, taxonomy, time, and consumer analysis;
- invalidation matrix and cross-lane effects;
- unresolved blockers;
- requested reviewer roles and separation;
- explicit non-effects.

Then stop. Operational execution requires a separate authorized transition.

[Back to top](#top)

---

<a id="prior-target-safety"></a>

## Prior target safety

A prior release is a candidate, not a trusted backup.

| Target question | Required evidence | Failure posture |
|---|---|---|
| Is the target distinct and immutable? | Stable release identity, manifest digest, artifact digests, no self-target | `HOLD` or `ERROR` |
| Does evidence still resolve? | Current EvidenceRef-to-EvidenceBundle resolution and limitations | `HOLD` or withdrawal |
| Are source roles still valid? | Source/product/version and claim-relative authority | `HOLD` |
| Are rights and approved purpose current? | Current terms, attribution, license/access class, purpose constraints | `HOLD` or policy/runtime denial |
| Is taxonomy identity still usable? | Version-pinned authority, crosswalk, ambiguity and synonym treatment | `HOLD` |
| Is sensitive precision currently safe? | Current classification, geoprivacy transform support, public/restricted split, traceable review | `HOLD` or withdrawal |
| Are time and geography correct? | Observation/source/retrieval/release/correction time and geography/version bindings | `HOLD` |
| Does current policy permit the target? | Applicable policy evaluation and obligations | `HOLD` until separately evaluated |
| Is accountable review possible? | Verified roles, scope, independence/separation, revocation path | `HOLD` |
| Are consumers compatible? | API, map, Evidence Drawer, Focus Mode, export, cache, index, graph, and downstream derivative inventory | `HOLD` |
| Is correction/public notice defined? | Correction/withdrawal relation and public status requirements | `HOLD` |
| Can recovery be read back independently? | Governed public/API read-back and expected finite outcomes | `HOLD` |

Never restore exact or reconstructable sensitive detail merely because it existed in an older release.

[Back to top](#top)

---

<a id="invalidation-and-cross-lane-impact"></a>

## Invalidation and cross-lane impact

| Carrier or consumer | Candidate review question | Current implementation result |
|---|---|---|
| Governed API cache | Which exact resource/envelope keys use the affected release? | Adapter and completion proof not established |
| CDN and static delivery | Which immutable objects and aliases are exposed? | Operational inventory/read-back not established |
| Map tiles and layer manifests | Could old bytes expose sensitive detail or stale evidence? | Repository lanes exist; operational invalidation not established |
| Catalog and triplets | Which projections reference the affected release or EvidenceBundle? | Invalidation adapter not established |
| Search and vector indexes | Which entries can continue surfacing withdrawn support? | Invalidation and rebuild proof not established |
| AI cache and Focus Mode | Which answers or prompts resolve through invalidated evidence? | Cache invalidation/read-back not established |
| Evidence Drawer and species pages | Which public states must become withdrawn, corrected, stale, denied, or abstaining? | Consumer-specific recovery proof not established |
| Habitat–Fauna and other derivatives | Which downstream products inherit the affected occurrence/range support? | Each sibling lane requires its own accountable decision |
| Exports and offline bundles | Which downloaded/public artifacts cannot be recalled? | Correction and status strategy required |
| Monitoring and audit | How will maintainers prove the old state is no longer served? | Independent public read-back absent |

A style change, hidden layer, popup change, client-side filter, or AI prompt update is not sufficient containment when sensitive bytes remain in a public carrier.

[Back to top](#top)

---

<a id="shared-synthetic-rehearsal"></a>

## Shared synthetic rehearsal

The shared helper is useful only inside its bounded synthetic contract.

### Confirmed guards

- the workspace must contain `.kfm-synthetic-rollback-rehearsal` as a regular file with exact marker content;
- the scenario must set `synthetic: true`;
- absolute paths, `..`, and symlink traversal are denied;
- the current alias and affected/target manifest and artifact digests must match;
- rollback requires a distinct target; withdrawal forbids a target;
- all nine invalidation classes are required;
- plan mode returns a deterministic report without scenario-workspace mutation;
- apply mode changes only the marker-protected synthetic workspace and preserves affected release bytes.

### Important limitations

- `--report` accepts a caller-selected path and is not confined to the synthetic workspace.
- Correction and invalidation files are written with atomic replacement; colliding scenario-derived IDs can replace existing synthetic records.
- The report's `append_only_correction` field does not prove collision-safe append-only storage.
- The helper does not resolve evidence, execute policy, authenticate reviewers, verify release signatures, contact external systems, mutate production aliases, invalidate real consumers, issue public notice, or read back public recovery.
- The hosted workflow adds Hazards-specific tests, not a Fauna integrated fixture.

Treat the helper as a mechanics rehearsal and negative-control surface only.

[Back to top](#top)

---

<a id="interpret-the-results"></a>

## Interpret the results

| Result | What it proves | What it does not prove |
|---|---|---|
| Fixture validator `PASS` | Tracked valid/invalid candidates match the shared profile | Actual candidate validity, reference resolution, policy, review, target safety |
| Actual candidate validator `PASS` | Candidate shape and local cross-field consistency | Approval, execution, release, public mutation |
| Eight generic tests `OK` | Generic synthetic rollback/withdrawal mechanics and selected negative cases | Fauna integration or operational recovery |
| Fauna drill `DRILL_HANDOFF_READY` | Shared checks plus public-safe Fauna tabletop completed at an exact revision | Rollback approval or execution |
| Helper `HOLD` | A bounded synthetic prerequisite failed, with reason code | Operational incident result |
| Hosted `rollback-drill` success | Shared fixture profile and generic-plus-Hazards workflow assertions passed at that SHA | Fauna proof, current-main proof, human approval, deployment, publication |
| Documentation checks `PASS` | Markdown structure, links, and named repository paths are coherent | Scientific correctness, current wildlife conditions, safe target, operational authority |

Classify unavailable, inherited, skipped, and not-run checks separately. Never convert a skipped job into a pass.

[Back to top](#top)

---

<a id="accountable-review-handoff-packet"></a>

## Accountable review handoff packet

The following is an illustrative review packet, not a schema or authority object:

```yaml
fauna_rollback_handoff:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_ref: <exact-commit>
  affected_release_ref: <exact-release-ref-or-UNKNOWN>
  affected_manifest_digest: <sha256-or-UNKNOWN>
  public_safe_defect_summary: <no-sensitive-detail>
  work_state: <READY_FOR_REVIEW|HOLD|ERROR|NO_ACTION>
  proposed_path: <FORWARD_CORRECTION|ROLLBACK_CANDIDATE|WITHDRAWAL_CANDIDATE|HOLD|ERROR>
  rollback_card:
    path: <candidate-path-or-NOT_APPLICABLE>
    digest: <sha256-or-UNKNOWN>
    disposition: <ROLLBACK_CANDIDATE|WITHDRAWAL_CANDIDATE|HOLD|ERROR|NOT_APPLICABLE>
  target:
    release_ref: <prior-release-ref-or-null>
    current_evidence_check: <PASS|FAIL|NOT_RUN>
    current_rights_check: <PASS|FAIL|NOT_RUN>
    current_sensitivity_check: <PASS|FAIL|NOT_RUN>
    current_taxonomy_check: <PASS|FAIL|NOT_RUN>
    current_policy_check: <PASS|FAIL|NOT_RUN>
    current_review_check: <PASS|FAIL|NOT_RUN>
  affected_scope:
    object_families: []
    source_roles: []
    time_scope: <public-safe-summary>
    geography_scope: <generalized-public-safe-summary>
    sensitive_detail_in_packet: false
  commands_run: []
  results: []
  invalidations:
    - class: <shared-invalidation-class>
      implementation: <path-or-UNKNOWN>
      verification: <path-or-UNKNOWN>
      owner_role: <role-or-NEEDS_VERIFICATION>
  cross_lane_impacts: []
  evidence_refs: []
  policy_refs: []
  review_refs: []
  correction_notice_ref: <ref-or-null>
  blockers: []
  requested_review_roles: []
  non_effects:
    containment_executed: false
    source_activated_or_withdrawn: false
    lifecycle_written: false
    rollback_executed: false
    public_state_mutated: false
    release_authorized: false
    deployment_authorized: false
    promotion_authorized: false
    publication_authorized: false
```

Protected locations, private review text, credentials, secret URLs, vulnerable-source details, or unreviewed source excerpts do not belong in the packet.

[Back to top](#top)

---

<a id="fauna-integrated-rehearsal-gap"></a>

## Fauna integrated rehearsal gap

The current repository does not establish a direct executable Fauna rollback proof.

Missing dependency-closed evidence includes:

- public-safe synthetic affected and prior-target Fauna releases;
- a domain binding to the shared `RollbackCard` profile or an accepted successor;
- direct Fauna positive and expected-negative rollback fixtures;
- executable tests under the Fauna rollback test lane;
- current-rights, current-sensitivity, taxonomy, geoprivacy, evidence, and policy integration;
- public/restricted carrier assertions;
- Habitat–Fauna and other downstream invalidation assertions;
- an accepted operational executor and target/alias profile;
- idempotency, concurrency, collision, report-path, safe-path, digest, signature/review, and recovery tests;
- execution receipt and independent public read-back.

The smallest useful next implementation slice is a **public-safe, no-network Fauna integrated rehearsal** that reuses the shared candidate profile and helper while adding domain-specific target, sensitivity, taxonomy, and downstream-consumer assertions. It should remain synthetic and non-publishing.

[Back to top](#top)

---

<a id="operational-graduation-gate"></a>

## Operational graduation gate

Operational rollback remains held until all applicable gates close for one exact affected release.

### Authority and release identity

- [ ] Accepted affected-release, target-release, manifest, alias, correction, rollback, receipt, and read-back contracts.
- [ ] Authenticated Fauna, taxonomy, source-rights, sensitivity/geoprivacy, evidence, policy, correction, release, operations, security, and independent-review roles.
- [ ] Separation of generation, review, authorization, execution, and verification appropriate to consequence.

### Policy, evidence, and target safety

- [ ] Evidence resolution and limitations appropriate to the affected public claim.
- [ ] Current source role, rights, approved purpose, attribution, taxonomy, time, geography, and sensitivity support.
- [ ] Current policy evaluation and consumer obligations.
- [ ] Distinct safe target or explicit withdrawal behavior.
- [ ] Correction/public notice and immutable history.

### Execution and invalidation

- [ ] Accepted production plan/apply operator with no-write planning, safe paths, target and digest checks, policy/review verification, idempotency, concurrency control, recovery, and negative tests.
- [ ] Collision-safe correction/invalidation persistence and confined report/output paths.
- [ ] Least-privilege adapters for every required invalidation class.
- [ ] Append-only or otherwise accepted execution receipt with before/after identity and result.
- [ ] No direct browser, map, AI, or watcher authority over rollback.

### Independent recovery proof

- [ ] Public-safe synthetic Fauna rehearsal and negative cases.
- [ ] Candidate-specific pre-production rehearsal.
- [ ] Governed API, map, Evidence Drawer, Focus Mode, export, cache, catalog, search, vector, and cross-lane read-back.
- [ ] Monitoring and correction behavior for partial invalidation or failed recovery.
- [ ] Separate release, deployment, promotion, and publication authorization where applicable.

No score, deadline, green workflow, or feature value compensates for a missing non-compensable gate.

[Back to top](#top)

---

<a id="documentation-validation"></a>

## Documentation validation

For a change to this runbook:

1. Freeze the target bytes, current `main`, open same-path work, and the accepted placement authority.
2. Review the complete diff for stale commands, unsupported capability claims, sensitive-detail leakage, and unrelated churn.
3. Check one H1, heading order, explicit anchors, quick navigation, code-fence balance, tables, alerts, and final newline.
4. Resolve every changed relative link and verify every named contract, schema, validator, test, helper, workflow, lane, and command.
5. Run the shared fixture validator, actual-candidate validator when a candidate exists, validator tests, and generic rehearsal tests in the repository's declared environment.
6. Run the repository's focused Markdown, metadata, document-graph, link, and domain checks when available.
7. Classify hosted checks at the exact head; keep skipped, inherited, unavailable, and pending results separate.
8. Verify branch, changed paths, pull-request base/head, and draft state.
9. Keep review, merge, rollback authorization, execution, release, deployment, promotion, and publication separate.

Documentation acceptance criteria:

- [ ] Current capability claims link to repository evidence.
- [ ] Operational rollback remains explicitly held.
- [ ] The shared candidate and rehearsal boundaries are accurate.
- [ ] The permissive Fauna schema stub is not treated as proof.
- [ ] Runtime outcomes and `RollbackCard` dispositions remain separate.
- [ ] No protected wildlife detail appears.
- [ ] The absent `VALIDATION_RUNBOOK.md` reference is removed.
- [ ] The Fauna runbook index reflects this document's maturity without implying execution authority.

[Back to top](#top)

---

<a id="related-repository-surfaces"></a>

## Related repository surfaces

### Fauna procedures and doctrine

- [Fauna runbook index](README.md)
- [Fauna rollback drill](ROLLBACK_DRILL.md)
- [Fauna promotion preflight](PROMOTION_RUNBOOK.md)
- [Fauna publication-gate dry run](PUBLICATION_GATE_DRY_RUN.md)
- [Fauna sensitive-occurrence review](SENSITIVE_OCCURRENCE_REVIEW.md)
- [Fauna no-network testing](NO_NETWORK_TEST_RUNBOOK.md)
- [Fauna domain boundary](../../domains/fauna/README.md)
- [Fauna sensitivity doctrine](../../domains/fauna/SENSITIVITY.md)
- [Fauna policy documentation](../../domains/fauna/POLICY.md)

### Governance and shared rollback controls

- [Accepted Directory Rules decision](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules](../../doctrine/directory-rules.md)
- [Shared rollback rehearsal](../rollback-rehearsal.md)
- [`RollbackCard` contract](../../../contracts/release/rollback_card.md)
- [`RollbackCard` schema](../../../schemas/contracts/v1/release/rollback_card.schema.json)
- [Fauna rollback-card schema stub](../../../schemas/contracts/v1/domains/fauna/rollback_card.schema.json)
- [Shared fixtures](../../../fixtures/release/rollback_card/)
- [Shared validator](../../../tools/validators/release/validate_rollback_card.py)
- [Shared helper](../../../tools/release/rollback_apply.py)
- [Validator tests](../../../tests/validators/test_validate_rollback_card.py)
- [Generic rehearsal tests](../../../tests/release/test_synthetic_rollback_rehearsal.py)
- [Hosted rollback workflow](../../../.github/workflows/rollback-drill.yml)

### Fauna release, recovery, and data lanes

- [Fauna release candidates](../../../release/candidates/fauna/README.md)
- [Fauna rollback decision lane](../../../release/rollback/fauna/README.md)
- [Shared rollback-card root](../../../release/rollback_cards/README.md)
- [Fauna data-plane rollback lane](../../../data/rollback/fauna/README.md)
- [Fauna proof lane](../../../data/proofs/fauna/README.md)
- [Fauna receipt lane](../../../data/receipts/fauna/README.md)
- [Fauna published layer lane](../../../data/published/layers/fauna/README.md)
- [Fauna rollback pipeline lane](../../../pipelines/rollback/fauna/README.md)
- [Fauna rollback test lane](../../../tests/domains/fauna/release/rollback/README.md)

GitHub review is routed through repository ownership controls. That route does not prove specialist assignment, independent review, rollback authorization, release, deployment, promotion, or publication authority.

[Back to top](#top)

---

<a id="maintenance-and-document-rollback"></a>

## Maintenance and document rollback

Update this runbook when any of the following materially changes:

- the shared `RollbackCard` contract, schema, fixtures, validator, or finite vocabularies;
- the synthetic helper, its write boundary, collision behavior, tests, or hosted workflow;
- Fauna release, rollback, published-carrier, proof, receipt, pipeline, policy, sensitivity, taxonomy, or test-lane maturity;
- operational actor, alias, invalidation, receipt, monitoring, or public read-back implementation;
- rights, sensitivity, geoprivacy, taxonomy, source-role, correction, or public-status requirements.

When behavior changes, update the owning implementation and tests first or in the same dependency-closed change. Documentation must not manufacture maturity.

### Correction path

If a statement is false or stale:

1. stop using the affected instruction;
2. pin the exact revision and text at issue;
3. assess whether prior handoffs or reviews relied on it;
4. open the smallest forward correction or revert;
5. update the Fauna runbook index when the maturity classification changes; and
6. preserve prior documentation in Git history.

### Documentation rollback

If this documentation change is abandoned before merge, close the draft and remove only its task-owned branch. After an authorized merge, revert the documentation commits or submit a smaller reviewed forward correction. Documentation rollback does not reverse source, evidence, policy, release, deployed, public, or wildlife-management state.

[Back to top](#top)
