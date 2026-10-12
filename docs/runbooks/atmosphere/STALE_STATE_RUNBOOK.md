<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-atmosphere-stale-state
title: Atmosphere / Air Stale-State Runbook
type: standard
profile: repository-grounded-stale-assessment-and-handoff
version: v1.0
prior_version: proposed-scaffold
status: draft; repository-grounded; documentation-only; fixture-first; live-propagation-hold; non-authoritative; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Atmosphere, source, evidence, policy, review, correction, release, cache, public-surface, Hazards-seam, and operations assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-08-24
updated: 2026-08-24
policy_label: public; atmosphere; stale-state; supersession; fixture-first; no-network; non-release; not-for-life-safety
current_path: docs/runbooks/atmosphere/STALE_STATE_RUNBOOK.md
owning_root: docs/
responsibility: "Document how to detect, classify, contain, assess, review, and hand off stale Atmosphere state without silently changing claim scope, treating stale as wrong, bypassing evidence or policy, issuing life-safety guidance, mutating release state, or publishing data."
truth_posture: >-
  CONFIRMED same-path repository placement, accepted Directory Rules basis,
  shared fixture-only StaleStateSupersessionAssessment contract/schema/validator,
  deterministic negative fixtures, read-only focused workflow, Atmosphere source
  registry and connector boundary documentation, bounded Atmosphere fixture CI,
  placeholder Atmosphere freshness policy, absent executable Atmosphere connector,
  and substantive correction/validation sibling runbooks / PROPOSED operational
  carrier inventory, steward handoff, future Atmosphere freshness profiles, active
  policy evaluator, stale-state propagation engine, public UI behavior, cache
  invalidation, and live-source execution / UNKNOWN deployed consumers, actual
  public Atmosphere releases, current source admission, runtime policy enforcement,
  external caches, operational thresholds, and public-serving state / NEEDS
  VERIFICATION accountable owners, exact source cadences, review cycles, rights
  posture, release authority, rollback targets, and cross-lane propagation;
  cite-or-abstain
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 1012d9f6b605656d3e994801581ff3ccbe212556
  target_prior_blob: 9aa07e8cb10167f37988f55f4b5ac2afee3da42e
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  stale_assessment_contract_blob: a013a2dc2ef1af93f6e91fc967435f60ee2a0c8b
  stale_assessment_schema_blob: 8a7336a2dc37f51b03dc6a531e6cef5feca450f8
  stale_assessment_fixture_blob: a45955630e37136e0a8d46b09b9b26f68e245233
  stale_assessment_workflow_blob: b68dc9c1778cbbb342a91913ef23db7b1e32c99e
  atmosphere_freshness_policy_blob: 824a94a772999f869f950d8e281701e0724204da
  atmosphere_source_registry_readme_blob: 6a50dd496225cd9e4c3165dead10cde3d0f23959
  atmosphere_aqs_placeholder_blob: 2899950cd366d9afe7c468baa45cacc65da139e9
  atmosphere_connector_readme_blob: 4acc06114ecab9d360f64298cd1b6f6ae27ecb75
  atmosphere_correction_runbook_blob: f04b6a5904be2b060f70637af8caddaf4511a227
inspection_boundary: >-
  Current-session GitHub reads of the target scaffold, accepted Directory Rules
  decision, shared stale-state and supersession packet, navigational stale-state
  reference, Atmosphere source registry, connector boundary, freshness policy,
  domain workflow, tests, reconciliation contract, and correction/validation
  runbooks. Repository-native commands were not executed in a mounted checkout
  during authoring. No source was contacted; no object was marked stale, corrected,
  superseded, withdrawn, rolled back, released, deployed, promoted, published, or
  exposed to a public client.
related:
  - docs/runbooks/README.md
  - docs/runbooks/atmosphere/README.md
  - docs/runbooks/atmosphere/SOURCE_REFRESH_RUNBOOK.md
  - docs/runbooks/atmosphere/VALIDATION_RUNBOOK.md
  - docs/runbooks/atmosphere/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - docs/runbooks/atmosphere/CORRECTION_RUNBOOK.md
  - docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/atlases/stale-state-reference.md
  - docs/domains/atmosphere/README.md
  - contracts/common/stale_state_supersession_assessment.md
  - schemas/contracts/v1/common/stale_state_supersession_assessment.schema.json
  - fixtures/contracts/v1/common/stale_state_supersession_assessment/cases.json
  - tools/validators/governance/validate_stale_state_supersession_assessment.py
  - tests/validators/governance/test_validate_stale_state_supersession_assessment.py
  - tools/validators/freshness/README.md
  - policy/domains/atmosphere/freshness_gate.rego
  - data/registry/sources/atmosphere/README.md
  - connectors/atmosphere/README.md
  - .github/workflows/stale-state-supersession-assessment.yml
  - .github/workflows/domain-atmosphere.yml
tags: [kfm, runbook, atmosphere, air, stale-state, freshness, expiry, supersession, lineage, correction, rollback, evidence, policy, no-network, not-for-life-safety]
notes:
  - "The prior scaffold's original creation date remains UNKNOWN; 2026-08-24 records the first substantive repository-grounded edition."
  - "Same-path documentation modernization under accepted ADR-0029; no root, lane, contract, schema, policy, fixture, validator, test, workflow, receipt, proof, release object, or public state is created or moved."
  - "The shared stale-state assessment is fixture-only and review-required. It does not decide actual freshness or mutate any object."
  - "The Atmosphere freshness Rego file remains a proposed default-deny scaffold, and no executable Atmosphere connector was verified."
  - "Stale means support has aged beyond a declared condition; it does not by itself mean the substance is incorrect."
  - "KFM Atmosphere is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Stale-State Runbook

> **Repository-grounded procedure for detecting, classifying, containing, assessing, and handing off stale Atmosphere state while preserving time semantics, source role, evidence, lineage, correction, rollback, and public-safety boundaries.**

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere-1f8fff">
  <img alt="Assessment: fixture first" src="https://img.shields.io/badge/assessment-fixture%20first-8250df">
  <img alt="Live propagation: hold" src="https://img.shields.io/badge/live%20propagation-HOLD-b42318">
  <img alt="Alerting: not official" src="https://img.shields.io/badge/alerting-not%20official-b42318">
  <img alt="Publication: none" src="https://img.shields.io/badge/publication-none-6e7781">
</p>

> [!IMPORTANT]
> **Stale is not the same as wrong.** A stale object has aged beyond a declared support condition or current-use tolerance. Its substance may still be accurate for its original time scope. An incorrect object requires correction or withdrawal support; do not disguise a substantive defect as a freshness badge.

> [!WARNING]
> **KFM Atmosphere is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** Stale or current labels in KFM must not be used to issue health guidance, declare safety, replace an official warning, or imply that an expired KFM surface cancels or supersedes an issuing agency's record. Route current-sensitive advisory use to the Hazards lane and the official issuing authority.

> [!CAUTION]
> **Live Atmosphere stale-state propagation is `HOLD`.** The repository has a substantive shared fixture-only assessment profile, but the Atmosphere freshness policy is still a scaffold, the broad freshness-validator lane is documentation-only, concrete Atmosphere source descriptors are incomplete, and the Atmosphere connector lane contains no executable connector module. This runbook does not turn those surfaces into operational authority.

**Quick navigation:** [Purpose](#1-purpose-scope-and-non-goals) · [Authority](#2-authority-placement-and-current-evidence) · [Vocabulary](#3-state-time-and-source-role-vocabulary) · [Roles](#4-roles-and-separation-of-duties) · [Preflight](#5-authority-freeze-and-stop-conditions) · [Markers](#6-stale-state-markers-and-atmosphere-interpretation) · [Outcomes](#7-finite-assessment-outcomes-and-dispositions) · [Procedure](#8-stale-state-procedure) · [Surfaces](#9-affected-surface-and-carrier-review) · [Cases](#10-atmosphere-specific-case-guidance) · [Validation](#11-current-executable-validation) · [Reasons](#12-reason-codes-and-evidence-labels) · [Correction](#13-correction-withdrawal-supersession-and-rollback) · [Packet](#14-review-handoff-packet) · [Checklist](#15-operator-checklist) · [Open work](#16-current-holds-and-open-verification) · [Maintenance](#17-maintenance-and-document-rollback) · [References](#18-related-current-surfaces)

---

## 1. Purpose, scope, and non-goals

### 1.1 Purpose

Use this runbook when an Atmosphere source, evidence object, release support object, or public-facing carrier may no longer be current enough for its requested use. The procedure helps an operator:

1. freeze the exact subject, version, source, time scope, exposure, and requested use;
2. detect a bounded stale-state signal without treating elapsed time alone as proof;
3. distinguish stale, incorrect, superseded, withdrawn, delayed, provisional, and unknown states;
4. preserve observation, source, retrieval, model, validity, release, and correction times as separate facts;
5. contain current-sensitive use without deleting history or silently rebinding the object;
6. prepare a deterministic fixture-only assessment when the shared profile applies;
7. route substantive defects to correction, public withdrawals to release authority, and operational reversals to rollback review;
8. produce a public-safe handoff that states exactly what remains unverified.

### 1.2 In scope

- source-freshness expiry and missing cadence support;
- expired forecast, advisory-context, model-run, or temporary-validity windows;
- time-scope support gaps;
- schema, geography, model, policy, rights, and review drift;
- provisional-versus-final or predecessor-versus-successor lineage;
- affected API, map, tile, search, graph, export, AI, cache, dashboard, and documentation inventory;
- no-network fixture validation of stale-state and supersession declarations;
- review, correction, withdrawal, rollback, and release handoff;
- Atmosphere anti-collapse checks such as AQI versus concentration, AOD versus PM2.5, model versus observation, and advisory context versus official instruction.

### 1.3 Out of scope

This runbook does not:

- invent a source cadence, stale threshold, review interval, policy version, rights decision, reviewer, release ID, or rollback target;
- contact a live source or activate a connector;
- determine that current air quality, weather, smoke, climate, forecast, or sensor conditions are safe or unsafe;
- mark an object stale merely because a file is old or a newer file exists;
- silently change a claim's valid time, geography, units, source role, object family, or audience;
- mutate a `SourceDescriptor`, `EvidenceBundle`, schema, policy, release manifest, AI receipt, or public carrier;
- issue a `CorrectionNotice`, `WithdrawalNotice`, `PromotionDecision`, `ReleaseManifest`, or `RollbackCard`;
- invalidate caches, alter an alias, deploy, release, promote, publish, or change repository settings;
- treat generated language, a map style, a badge, a green workflow, or schema validity as evidence that a live object is current.

### 1.4 Terminal boundary

The maximum output of this runbook is one of:

- a no-action record supported by evidence;
- a no-change/heartbeat record from the owning source-refresh process;
- a `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` handoff;
- a fixture-only `StaleStateSupersessionAssessmentCandidate` result requiring review;
- a public-safe request for correction, supersession, withdrawal, rollback, or release review.

No result from this runbook means that an object has actually been changed on a governed or public surface.

[Back to top](#top)

---

## 2. Authority, placement, and current evidence

### 2.1 Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This file is a human operational procedure at an already tracked path:

```text
docs/runbooks/atmosphere/STALE_STATE_RUNBOOK.md
```

The placement outcome is `PLACE`: update the existing file in place. Do not create a second stale-state runbook under a domain docs folder, policy root, release root, or application root.

| Responsibility | Owning surface | Relationship to this runbook |
|---|---|---|
| Human Atmosphere stale-state procedure | `docs/runbooks/atmosphere/` | **Owned here** |
| Cross-family stale/supersession meaning | [`contracts/common/stale_state_supersession_assessment.md`](../../../contracts/common/stale_state_supersession_assessment.md) | Referenced; proposed-inactive fixture profile |
| Machine shape | [`schemas/contracts/v1/common/stale_state_supersession_assessment.schema.json`](../../../schemas/contracts/v1/common/stale_state_supersession_assessment.schema.json) | Closed fixture shape; not live state authority |
| Atmosphere domain meaning | [`docs/domains/atmosphere/`](../../domains/atmosphere/README.md) and contracts | Referenced; not redefined |
| Source cadence and admission | `data/registry/sources/` plus source decisions | Referenced; currently incomplete for Atmosphere |
| Freshness policy | `policy/` | Atmosphere file is a default-deny scaffold, not active policy proof |
| Executable assessment | `tools/validators/`, `tests/`, workflows | Fixture coherence only |
| Evidence and proof | `data/proofs/` and EvidenceBundle authority | Separate from stale assessment |
| Process memory | `data/receipts/` | Separate from truth and release state |
| Correction, release, withdrawal, rollback | `release/` and owning records | Separate decisions and mutations |
| Public delivery | Governed APIs and released public-safe carriers | Not exercised by this runbook |

### 2.2 Current repository posture

| Surface | CONFIRMED repository evidence | Safe conclusion |
|---|---|---|
| Target file | Short `PROPOSED scaffold`, prior blob `9aa07e8c...` | A substantive same-path replacement is needed; the scaffold is not an operating procedure |
| Directory governance | ADR-0029 is accepted and pins Directory Rules v2 | Same-path documentation work is supported |
| Shared stale assessment | Contract, closed schema, fixtures, validator, tests, receipt, and read-only workflow exist | KFM can validate a fixture-only declaration; it cannot determine actual freshness or apply state |
| Shared assessment outcomes | `REVIEW_REQUIRED`, `ABSTAIN`, `DENY`, `ERROR` | No fixture result is automatic approval or lifecycle mutation |
| Navigational stale reference | Repository document distinguishes stale from wrong and lists marker/lineage concepts | Useful orientation; it is not the machine or release authority and does not settle cross-lane propagation |
| Atmosphere freshness policy | `policy/domains/atmosphere/freshness_gate.rego` is a proposed default-deny scaffold | No accepted Atmosphere policy bundle or evaluator is established by that file |
| Shared freshness validator | `tools/validators/freshness/README.md` describes a proposed lane | Broad executable freshness validation remains `NEEDS VERIFICATION` |
| Atmosphere source registry | README plus small proposal records are tracked; inspected AQS record is placeholder-only | No complete admitted AQS descriptor, cadence, rights, or activation decision is proved by the record |
| Atmosphere connector | `.gitkeep` and README only | No executable Atmosphere connector or live retrieval entry point was verified |
| Atmosphere domain CI | Read-only workflow runs several bounded synthetic profiles and records broader proof/release holds | Useful fixture evidence; not end-to-end stale-state propagation |
| AirNow/AQS reconciliation | Fixture-only contract preserves provisional AirNow versus regulatory AQS roles | May inform lineage review; it does not replace a live source record or release |
| Correction procedure | Substantive repository-grounded sibling runbook exists | Incorrect or defective published material has a documented handoff, but execution maturity remains bounded |
| Public runtime | Exact deployed stale badges, API envelopes, carrier invalidation, and cache behavior were not verified | Treat public propagation as `UNKNOWN / HOLD` |

### 2.3 Operational determination

The repository is mature enough to support a truthful assessment-and-handoff runbook, but not to claim an operational Atmosphere stale-state service. Until the open controls close:

- use the shared fixture profile only for local coherence;
- require external evidence and accountable review for real objects;
- preserve `HOLD` for live propagation;
- do not infer public state from repository files, workflow results, or documentation.

[Back to top](#top)

---

## 3. State, time, and source-role vocabulary

### 3.1 State vocabulary

| Term | Meaning in this runbook | Must not be collapsed into |
|---|---|---|
| `CURRENT` | Declared support is sufficient for the exact requested use at the evaluated time | Eternal truth or policy approval |
| `STALE` | Support has aged beyond a declared condition, tolerance, review period, or valid-use window | Incorrect substance |
| `SUPERSEDED` | A retained successor relationship is declared and supported | Deletion of the prior object |
| `WITHDRAWN` | The object is no longer offered for the relevant use under an explicit governed record | Erasure of audit history |
| `UNKNOWN` | Evidence is insufficient to classify current state safely | Current by default |
| Incorrect | Substance is known to be wrong or materially unsupported | A simple stale badge |
| Provisional | Upstream or KFM review state is explicitly preliminary | Regulatory/final authority |
| Delayed or late | An expected update has not arrived on schedule | Proof that the prior object is wrong |
| `NO_CHANGE` | A governed comparison proves no material source change | Freshness forever or a new release |
| Expired | A declared validity or effective window ended | Automatic deletion or correction |

The shared candidate schema uses the declared states `CURRENT`, `STALE`, `SUPERSEDED`, `WITHDRAWN`, and `UNKNOWN`. Do not add a new state token in this runbook and then imply machine support.

### 3.2 Time kinds

Atmosphere material is especially vulnerable to time collapse. Preserve the time kinds that apply to the object:

| Time kind | Example | It is not |
|---|---|---|
| Observation time | When a station measurement was made | Retrieval time |
| Source publication/update time | When the upstream published or revised a product | Observation time by default |
| Retrieval time | When KFM fetched or received bytes | Proof that the source is current |
| Model initialization time | When a forecast/model run began | Forecast-valid time |
| Forecast-valid time | The interval or instant the forecast represents | An observation |
| Issue time | When an advisory-context product was issued | Open-ended validity |
| Valid/effective time | When a product, rule, normal, or advisory applies | Release approval |
| Expiration time | When temporary support ends | Proof of incorrect substance |
| Release time | When an authorized KFM release became effective | Source time or policy approval by itself |
| Correction time | When a correction or supersession became effective | Permission to rewrite prior receipts |

> [!IMPORTANT]
> A successful retrieval cannot silently replace observation time, model time, validity, or source publication time. A stale operational product does not become current because its URL still returns `200`.

### 3.3 Source-role boundaries

Stale-state assessment does not weaken Atmosphere anti-collapse rules:

- AQI is not a pollutant concentration.
- AOD is not surface PM2.5.
- A model, reanalysis, interpolation, or forecast field is not a direct observation.
- A low-cost sensor is not a regulatory-grade monitor merely because it reports recently.
- Advisory context is not KFM-issued instruction.
- A final archive may supersede provisional context for a bounded claim without erasing the provisional record's lineage.

A newer object with a different source role is not automatically a like-for-like successor. Review semantic compatibility before declaring supersession.

[Back to top](#top)

---

## 4. Roles and separation of duties

Only the GitHub review route is verified for this document. The roles below describe required functions, not current appointments.

| Role | Responsibilities | Must not be inferred from |
|---|---|---|
| Atmosphere domain steward | Confirms object meaning, source-role compatibility, temporal interpretation, and Atmosphere/Hazards boundary | Repository ownership alone |
| Source steward | Confirms source identity, descriptor, cadence, source-head evidence, revision status, and successor relationship | URL availability or a placeholder registry file |
| Evidence steward | Confirms basis references resolve and the stale/incorrect conclusion is supported | Validator success alone |
| Policy steward | Owns the accepted freshness/admissibility profile, evaluator binding, obligations, and failure posture | A Rego filename or default rule |
| Rights/sensitivity reviewer | Evaluates changed rights, access, redistribution, facility/sensor privacy, and restricted joins | Public availability alone |
| Independent reviewer | Reviews the assessment, lineage, affected surfaces, and non-authority boundary where material | CODEOWNERS routing or self-review |
| Correction reviewer | Decides whether a substantive defect requires correction or withdrawal handling | A stale marker alone |
| Release authority | Decides whether public release state may be marked, superseded, withdrawn, or restored | A green workflow, merge, or candidate file |
| Operations/cache steward | Executes authorized alias, cache, serving, and monitoring changes | Documentation or a propagation plan alone |
| Hazards liaison | Confirms official-source redirect and non-life-safety treatment for advisory context | Atmosphere domain ownership |

> [!CAUTION]
> If an accountable reviewer or authority required for the exact object and exposure cannot be identified, the result is `HOLD` or `ABSTAIN`. Do not assign authority to the operator, model, connector, workflow, or document by convenience.

[Back to top](#top)

---

## 5. Authority freeze and stop conditions

### 5.1 Required preflight record

Before evaluating a real object, record:

```yaml
case_id: "<stable public-safe case identity>"
evaluated_at: "<UTC timestamp>"
operator: "<authenticated actor reference>"
subject:
  object_ref: "<stable governed reference>"
  object_family: "<actual family>"
  version: "<exact version>"
  declared_state: "<CURRENT|STALE|SUPERSEDED|WITHDRAWN|UNKNOWN>"
  exposure: "<INTERNAL|NONE|PUBLIC_CANDIDATE|PUBLISHED>"
requested_use:
  operation: "<map|api|search|export|analysis|focus|release-review|other>"
  audience: "<public-safe audience or governed class>"
  time_scope: "<exact requested support window>"
source_support:
  descriptor_ref: "<governed SourceDescriptor reference or null>"
  cadence_or_support_ref: "<governed reference or null>"
  source_head_refs: []
evidence_refs: []
release_refs: []
review_refs: []
correction_ref: null
withdrawal_ref: null
rollback_ref: null
affected_surface_refs: []
```

This is an illustrative operator template, not a machine contract. Use the accepted object shapes and record homes when they exist.

### 5.2 Mandatory stop conditions

Stop before state classification when any of these is unresolved:

- subject identity, object family, version, declared state, or exposure;
- requested operation, audience, or time scope;
- source descriptor, source role, cadence/support condition, or source-head identity where required;
- observation/source/retrieval/model/validity/expiry time needed to evaluate the request;
- EvidenceRef or basis reference needed for the stale signal;
- rights, sensitivity, access, or official-source redirect obligations;
- review authority, release authority, or separation-of-duties requirement;
- public affected-surface inventory;
- correction or withdrawal support when substance may be incorrect;
- rollback support when a published object may be superseded or withdrawn;
- concurrent correction, release, rollback, migration, or PR ownership of the same object.

### 5.3 Safe stop outcomes

| Condition | Safe result |
|---|---|
| Marker or basis unresolved | `ABSTAIN` / `SOURCE_BASIS_UNRESOLVED` |
| Subject state unresolved | `ABSTAIN` / `SUBJECT_STATE_UNKNOWN` |
| Review pending or unknown | `ABSTAIN` or work-state `HOLD` |
| Contradictory state/marker or unsafe lineage | `DENY` |
| Invalid or unparseable candidate | `ERROR` |
| Live propagation authority absent | `HOLD`; no public mutation |

[Back to top](#top)

---

## 6. Stale-state markers and Atmosphere interpretation

The shared fixture schema recognizes these marker tokens. Their presence in the schema makes them valid candidate values; it does not prove that an operational detector has fired.

| Marker | Bounded meaning | Atmosphere application | Required evidence before relying on it |
|---|---|---|---|
| `SOURCE_FRESHNESS_EXPIRED` | Declared source support/cadence was exceeded | Expected observation, forecast, model, archive, or advisory update did not arrive within the accepted source profile | Complete descriptor, cadence/support rule, source-head evidence, evaluation time, and requested use |
| `SCHEMA_VERSION_DRIFT` | Subject shape/version no longer matches the governed current profile for the use | Published Atmosphere object remains on an older schema profile | Exact schema identities, migration/revalidation posture, compatibility decision |
| `GEOGRAPHY_VERSION_DRIFT` | Spatial support reference was superseded | Station, grid, county, footprint, or generalized support changed | Old/new geography identities, crosswalk, effect on claim, lineage |
| `TIME_SCOPE_OUTSIDE_SUPPORT` | Requested temporal scope exceeds the object's declared support | A user asks for “current” conditions from an historical record, expired forecast, old normal period, or completed event context | Original claim scope, requested scope, validity/support interval; do not silently rebind |
| `MODEL_VERSION_SUPERSEDED` | A model or run family was replaced for the relevant use | Forecast/reanalysis or correction model version is no longer the selected profile | Model/run identity, version lineage, validation/review state, requested operation |
| `REVIEW_AGED_OUT` | Required review interval elapsed | Sensor qualification, caveat profile, sensitive join, or release review is older than its accepted cycle | Accepted review-cycle rule, prior review record, current reviewer authority |
| `RIGHTS_STATUS_CHANGED` | Rights or permitted-use posture changed | Upstream terms, redistribution, attribution, sensor-owner, or restricted-access posture changed | Current rights evidence, prior rights state, affected carriers, policy/review decision |
| `POLICY_VERSION_CHANGED` | Referenced policy profile was superseded | Atmosphere freshness, release, advisory, privacy, or source-role rules changed | Exact old/new policy identity, accepted decision, evaluator binding, re-evaluation result |
| `NONE` | No supported marker is declared | Current/no-action candidate only when state and lineage agree | Evidence that the exact requested use remains supported |
| `UNKNOWN` | Marker cannot be resolved safely | Missing source profile, ambiguous time semantics, or incomplete evidence | Produces `ABSTAIN`; never defaults to current |

### 6.1 Operational signals that are not automatically stale markers

These may initiate review but do not decide state by themselves:

- HTTP error, timeout, or source outage;
- rate limit;
- late delivery;
- a newer filename or timestamp;
- different byte digest;
- changed ETag;
- missing station or grid cell;
- revised quality flag;
- provisional/final status change;
- correction notice from upstream;
- a new model run;
- a map-rendering error;
- a user report;
- a dashboard alarm.

Each signal requires subject, time, source-role, evidence, and requested-use resolution. A failed fetch may mean the current object is stale, temporarily unverifiable, or still valid under its support window. Record what the evidence supports.

### 6.2 Silent refresh prohibition

Do not silently:

- replace the subject version;
- extend its valid time;
- change its geography;
- relabel provisional as final;
- swap a model for an observation;
- change AQI into concentration;
- reissue an AI answer in place;
- redirect an alias to a successor;
- remove the stale badge;
- clear a cache;
- rewrite an EvidenceBundle.

A changed claim needs a new supported object or a governed correction/supersession transition with explicit lineage.

[Back to top](#top)

---

## 7. Finite assessment outcomes and dispositions

### 7.1 Shared fixture outcomes

| Outcome | Meaning | Authority effect |
|---|---|---|
| `REVIEW_REQUIRED` | Candidate declaration is locally coherent under the fixture profile | None; accountable review and every referenced authority object remain required |
| `ABSTAIN` | Marker, basis, lineage, state, action, or review posture is unresolved | No mutation; narrow or hold the request |
| `DENY` | Candidate contradicts state, erases lineage, lacks required support, crosses the trust membrane, or proposes an unsafe action | No mutation; record bounded reasons |
| `ERROR` | Candidate cannot be safely parsed or checked under the closed schema | No partial result or permissive fallback |

`HOLD` is a governed work-state used by this runbook when operational prerequisites are absent. In the shared candidate, action `HOLD` leads to an abstaining result rather than approval.

### 7.2 Proposed operational dispositions

These are handoff categories, not proof that the repository executes them:

| Disposition | Use when | Next owning process |
|---|---|---|
| `NO_ACTION` | Evidence supports current state for the exact requested use | Record evaluation; continue monitoring |
| `NO_CHANGE` | Governed source comparison proves no material change | Source-refresh heartbeat/receipt; no release churn |
| `MARK_STALE` | State and supported marker agree, substance is not identified as wrong | Review and separately authorized public-state propagation |
| `HOLD` | Authority, evidence, review, policy, source, or implementation is incomplete | Bounded follow-up; no fetch/public mutation |
| `SUPERSEDE` | Supported successor and retained lineage exist | Promotion/release review; rollback support if published |
| `WITHDRAW` | Continued use is impermissible and no successor is available | Release/correction/withdrawal authority |
| `CORRECT` | Substance is incorrect or materially unsupported | [Correction Runbook](./CORRECTION_RUNBOOK.md) |
| `ROLLBACK_REVIEW` | A released change needs reversal to a known safe target | [Rollback Runbook](./ROLLBACK_RUNBOOK.md) |
| `REISSUE_AS_NEW` | A governed AI answer or receipt must be replaced without retroactive rewrite | New receipt/object plus cross-reference; no in-place mutation |

[Back to top](#top)

---

## 8. Stale-state procedure

### Step 0 — Open a public-safe case

- Assign a stable case identity that contains no credentials, private endpoint details, source payloads, or sensitive location information.
- Record the exact repository/release/object revisions being inspected.
- State whether the case concerns internal, public-candidate, or published exposure.
- Separate the observation about staleness from the conclusion.

**Output:** bounded case record with `UNKNOWN` or `HOLD` posture until evidence closes.

### Step 1 — Freeze subject and requested use

- Pin `object_ref`, object family, version, declared state, and exposure.
- Pin the requested operation, audience, geography, and time scope.
- Record current release, correction, withdrawal, and rollback references where applicable.
- Search for active correction, release, rollback, migration, issue, or PR work over the same subject.

**Stop:** identity or overlap unresolved.

### Step 2 — Resolve source and support condition

- Resolve the actual SourceDescriptor and activation/admission state; do not use a placeholder record as authority.
- Record source role, rights, sensitivity, cadence/support condition, source-head identity, and update/revision posture.
- Preserve source-native provisional, validated, certified, corrected, or superseded state.
- Confirm whether the requested use depends on the source being current, merely historically accurate, or both.

**Stop:** descriptor, cadence, role, rights, or source-head evidence absent.

### Step 3 — Reconstruct time semantics

Record every material time kind separately. Check:

- observation versus retrieval;
- publication/update versus issue;
- model initialization versus forecast-valid;
- validity versus release;
- expiration versus correction;
- timezone and UTC normalization;
- open-ended or ambiguous support windows.

**Stop:** required time cannot be reconstructed without inference.

### Step 4 — Resolve evidence and classify the signal

- Resolve every basis reference needed to support the marker.
- Select one supported marker or `UNKNOWN`; do not combine unrelated reasons into a vague “old data” label.
- Record `detected_at` in UTC and ensure it does not occur after the evaluation time.
- Classify substance as `NO_ERROR_IDENTIFIED`, `NOT_ASSESSED`, `POSSIBLY_INCORRECT`, or `INCORRECT` only when evidence supports that classification.

**Decision:** stale support and substantive correctness are independent axes.

### Step 5 — Choose containment

Until review closes:

- prevent new current-sensitive claims from treating the object as current;
- preserve historical access when rights, sensitivity, and release policy permit;
- do not delete the prior object;
- do not silently update aliases or map sources;
- do not issue a public correction merely from an unreviewed stale signal;
- preserve official-source redirection for advisory context;
- use `ABSTAIN`, `DENY`, or `HOLD` on governed response surfaces where support is insufficient.

Containment is not final public propagation. Record who owns the next transition.

### Step 6 — Assess lineage

For a proposed successor or withdrawal:

- identify predecessor and successor separately;
- prohibit self-links;
- retain the prior artifact;
- record effective time and lineage references;
- prohibit silent rebinds;
- require an ADR reference for schema or policy supersession under the shared fixture profile;
- never retroactively supersede an AI receipt; issue a new receipt with a cross-reference;
- require a rollback reference when a published object would be superseded or withdrawn.

### Step 7 — Inventory affected surfaces

Use [§9](#9-affected-surface-and-carrier-review). The inventory must include every released derivative or public-facing carrier whose current-state interpretation depends on the subject. Do not assume that updating one source file updates tiles, caches, APIs, search, exports, AI responses, or documentation.

### Step 8 — Run bounded fixture validation where applicable

Run the shared commands in [§11](#11-current-executable-validation) only when the candidate uses the shared fixture profile. Record exact commit, environment, command, result, and limitations.

A passing candidate remains `REVIEW_REQUIRED`.

### Step 9 — Route the owning decision

| Finding | Route |
|---|---|
| Support aged, no substantive error identified | Stale-state review and authorized marker/serving decision |
| Substance possibly incorrect | Evidence review; hold current-sensitive use |
| Substance incorrect | Correction or withdrawal process |
| Successor complete | Promotion/release review with retained lineage |
| Continued public exposure impermissible | Withdrawal/release authority; rollback support |
| Operational state cannot be changed safely | `HOLD`; open implementation or incident follow-up |

### Step 10 — Verify a separately authorized transition

After another authority applies a decision, independently verify:

- authoritative object/release state;
- predecessor retention and successor linkage;
- governed API output;
- map/layer, Evidence Drawer, time/trust indicators, and official-source redirect;
- tiles, archives, downloads, search, graph, exports, AI responses, caches, dashboards, and documentation as applicable;
- affected digest/version identity;
- correction/withdrawal/rollback references;
- no direct internal-store path was introduced;
- no stale object is presented as current in a derived surface.

Do not infer deployment or publication from merge or release-record presence. Verify actual serving state.

[Back to top](#top)

---

## 9. Affected-surface and carrier review

The following is a **PROPOSED review inventory**. Current implementation of each surface remains `NEEDS VERIFICATION` or `UNKNOWN` unless exact runtime evidence is supplied.

| Surface | Review question | Fail-closed posture |
|---|---|---|
| Governed API | Does the response expose state, time scope, evidence, limitations, official redirect, and correction lineage appropriate to the operation? | `ABSTAIN`, `DENY`, or explicit stale context; never raw-store fallback |
| Map/layer | Can the map still visually imply current conditions from a stale carrier? | Remove from current view or visibly mark through governed state; style-only hiding is insufficient |
| Evidence Drawer | Are source time, observation time, support window, stale basis, evidence links, and limitations visible? | Do not present unsupported “current” status |
| Time/trust banner | Is stale state distinguishable from error, denied, superseded, provisional, and historical? | Use a finite visible state; no silent omission |
| Tiles/PMTiles/COG/GeoParquet | Does the immutable carrier bind to the affected release/object version? | Build or select only through governed release; retain old digest for audit |
| Search/index | Can stale content still rank or appear as current? | Mark, filter, or withdraw through governed index policy; rebuild from authorized state |
| Graph/triplets | Do edges imply an active/current relationship after the subject changed? | Rebuild projection from governed canonical state; graph is not sovereign truth |
| Export/download | Does the package include state, time, source, evidence, release, and correction metadata? | Deny current-sensitive export when closure is missing |
| Focus Mode / generated answer | Can a model describe stale context as current? | Evidence-bounded `ABSTAIN`/`DENY`; new receipt for corrected answer |
| Cache/CDN/service worker | Could an authorized state change be hidden by retained bytes? | Invalidate only under an approved propagation plan; verify read-back |
| Dashboard/monitor | Does an operational widget distinguish source outage, late update, stale object, and wrong data? | Preserve separate states and evidence |
| Documentation/story | Does prose still make a current claim from superseded support? | Correct or qualify through documentation/correction process; retain history |

### 9.1 Public-safe logging

Do not place in public logs or handoff packets:

- credentials or tokens;
- private sensor endpoints;
- oversized source payloads;
- restricted facility or station details;
- personal or private-network metadata;
- raw query text against internal stores;
- direct RAW, WORK, or QUARANTINE locators;
- health or life-safety conclusions not issued by the official authority.

Use governed references and bounded reason codes instead.

[Back to top](#top)

---

## 10. Atmosphere-specific case guidance

### 10.1 Observation feed stops updating

**Signal:** expected station observations stop arriving.

**Do:** verify descriptor cadence, last admitted source head, observation times, upstream status, and requested use. Distinguish source outage from a station legitimately reporting no data. Mark current-sensitive support stale only with an accountable basis.

**Do not:** use retrieval time as observation time, repeat the last value as current, or infer safe conditions from silence.

### 10.2 Forecast or model validity expires

**Signal:** forecast-valid time ends or a model run is superseded.

**Do:** preserve model identity, initialization time, forecast-valid time, version, uncertainty, and successor lineage. Evaluate whether the historical forecast remains useful for retrospective analysis.

**Do not:** turn the forecast into an observation, extend its validity, or replace it in place.

### 10.3 Advisory context expires

**Signal:** the official issuer's validity window ends or the record is superseded.

**Do:** preserve issuer, issue/effective/expiration time, source link, and official redirect. Route emergency/life-safety interpretation to Hazards and the official authority.

**Do not:** declare the real-world condition ended merely because an advisory expired, or issue KFM instructions.

### 10.4 AirNow provisional context and AQS archive

**Signal:** a validated/certified AQS concentration becomes available after provisional AirNow context.

**Do:** preserve canonical monitor identity, distinct source roles, source states, and lineage. The existing fixture-only reconciliation profile may support a review candidate.

**Do not:** erase AirNow history, relabel NowCast as concentration, or treat a fixture result as regulatory certification or live replacement.

### 10.5 Climate normal or historical archive

**Signal:** the baseline period or archive vintage is older than the present year.

**PROPOSED operational interpretation:** age alone is not enough. A climate normal can remain current for a defined baseline and method while being inappropriate for a “current observation” claim. Evaluate the object's declared period, requested use, and successor policy.

**Do not:** classify all historical material as stale or silently substitute a newer normal into a claim about the prior baseline.

### 10.6 Satellite AOD or smoke context

**Signal:** a raster is delayed, revised, cloud-obscured, or outside its support window.

**Do:** preserve algorithm/product version, observation/retrieval time, spatial resolution, QA flags, limitations, and modeled/derived role.

**Do not:** present AOD as PM2.5, smoke plume as personal exposure, or recent imagery as direct ground observation.

### 10.7 Low-cost sensor review ages out

**Signal:** calibration/correction or qualification review is older than the accepted review cycle.

**Do:** require the accepted review-cycle rule, prior review, sensor/correction identity, confidence and limitations, transferability/drift posture, and new review evidence.

**Do not:** invent a review interval in this runbook or treat recent sensor timestamps as calibration proof.

### 10.8 Rights or access changes

**Signal:** upstream terms, redistribution rights, attribution, sensor-owner terms, or access class changes.

**Do:** hold public use, inventory affected carriers, resolve rights/policy/review, and use correction or withdrawal when the released representation is no longer permitted.

**Do not:** keep serving because the bytes were previously public or because a cached copy exists.

[Back to top](#top)

---

## 11. Current executable validation

### 11.1 Shared stale-state fixture profile

The current repository provides a deterministic, no-network profile for declaration coherence:

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  python -m unittest \
    tests.validators.governance.test_validate_stale_state_supersession_assessment \
    --verbose

PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 KFM_NO_NETWORK=1 \
  python tools/validators/governance/validate_stale_state_supersession_assessment.py \
    --fixtures
```

The validator checks, among other things:

- closed Draft 2020-12 shape;
- deterministic profile hash and assessment identity;
- UTC evaluation, detection, and effective-time coherence;
- canonical, bounded references;
- supported marker and basis posture;
- predecessor/successor lineage and prior retention;
- self-link and silent-rebind denial;
- AI receipt non-retroactivity;
- ADR reference for schema/policy supersession candidates;
- correction/withdrawal support for incorrect substance;
- rollback and affected surfaces for published supersession/withdrawal candidates;
- review records;
- direct-store and embedded-query denial;
- finite `REVIEW_REQUIRED`, `ABSTAIN`, `DENY`, and `ERROR` outcomes.

### 11.2 Focused hosted workflow

The read-only workflow is:

```text
.github/workflows/stale-state-supersession-assessment.yml
```

It runs the focused test, fixture validator, and generated-authoring-receipt integrity check with no-network environment variables and read-only contents permission.

> [!NOTE]
> The workflow's current pull-request path filter does **not** include this runbook. A documentation-only change to `docs/runbooks/atmosphere/STALE_STATE_RUNBOOK.md` therefore does not, by itself, prove that the focused workflow executed at the PR head. Record any workflow result only when GitHub actually reports a run for the exact head or when an authorized manual dispatch is separately performed.

### 11.3 Atmosphere domain workflow

`.github/workflows/domain-atmosphere.yml` executes several bounded synthetic Atmosphere profiles, including observation/model separation and AirNow/AQS reconciliation. It explicitly retains broader semantics, evidence, proof, and release holds. It does not apply stale state to a live object or public surface.

### 11.4 Validation claim boundary

A passing check does not:

- decide actual source freshness;
- prove a live descriptor, rights grant, cadence, or source-head identity;
- resolve EvidenceRefs or EvidenceBundles;
- apply Atmosphere freshness policy;
- authenticate review or release authority;
- mark, correct, supersede, withdraw, or roll back an object;
- update APIs, maps, tiles, search, graphs, AI, caches, or documentation;
- deploy, release, promote, publish, or authorize public use.

[Back to top](#top)

---

## 12. Reason codes and evidence labels

### 12.1 Shared marker tokens

Use the exact shared marker vocabulary when authoring a candidate:

```text
GEOGRAPHY_VERSION_DRIFT
MODEL_VERSION_SUPERSEDED
NONE
POLICY_VERSION_CHANGED
REVIEW_AGED_OUT
RIGHTS_STATUS_CHANGED
SCHEMA_VERSION_DRIFT
SOURCE_FRESHNESS_EXPIRED
TIME_SCOPE_OUTSIDE_SUPPORT
UNKNOWN
```

### 12.2 Selected validator reason codes

| Code | Meaning for handoff |
|---|---|
| `MARKER_UNKNOWN` | Marker cannot be selected safely |
| `SOURCE_BASIS_UNRESOLVED` | No admissible basis reference supports the marker |
| `SUBJECT_STATE_UNKNOWN` | Subject state is unresolved |
| `REVIEW_PENDING` / `REVIEW_UNKNOWN` | Accountable review has not closed |
| `ACTION_HELD` | Candidate deliberately remains held |
| `STATE_MARKER_CONTRADICTION` | Declared state and marker disagree |
| `MARKER_DETECTED_AT_REQUIRED` | A supported marker lacks detection time |
| `DETECTED_AFTER_EVALUATION` | Temporal order is impossible |
| `SUCCESSOR_REQUIRED` | A supersession relation lacks a successor |
| `LINEAGE_SELF_REFERENCE` | Subject/predecessor/successor relationship is self-referential |
| `PRIOR_ARTIFACT_NOT_RETAINED` | Proposed lineage would erase prior audit state |
| `SILENT_REBIND_DENIED` | Proposed action changes binding without explicit lineage |
| `AI_RECEIPT_RETROACTIVE_SUPERSESSION_DENIED` | Prior AI receipt would be rewritten in place |
| `INCORRECT_WITHOUT_CORRECTION` | Incorrect substance lacks correction/withdrawal support |
| `PUBLISHED_ROLLBACK_REQUIRED` | Published supersession/withdrawal lacks rollback support |
| `PUBLISHED_SURFACES_REQUIRED` | Published stale state lacks an affected-surface inventory |
| `ADR_REFERENCE_REQUIRED` | Schema/policy supersession lacks an ADR reference |
| `DIRECT_STORE_REFERENCE_DENIED` | Candidate attempts to expose an internal lifecycle/store shortcut |
| `EMBEDDED_QUERY_DENIED` | Candidate embeds internal query text |
| `REVIEW_RECORD_REQUIRED` | Declared completed review lacks record references |
| `PROFILE_SPEC_HASH_MISMATCH` / `ASSESSMENT_ID_MISMATCH` | Deterministic identity was altered or miscomputed |
| `SCHEMA_INVALID` | Candidate does not satisfy the closed fixture schema |

This list is explanatory. The validator implementation is the executable source for emitted codes under the fixture profile.

### 12.3 Truth and work labels

Use KFM truth labels independently of operational outcomes:

- `CONFIRMED` — verified from pinned evidence.
- `PROPOSED` — design or candidate, not current fact.
- `UNKNOWN` — evidence insufficient.
- `NEEDS VERIFICATION` — a concrete check remains.
- `CONFLICTED` — admissible sources disagree.
- `HOLD` — governed work cannot advance.

Do not translate `REVIEW_REQUIRED` into `CONFIRMED`, or a stale marker into `INCORRECT`.

[Back to top](#top)

---

## 13. Correction, withdrawal, supersession, and rollback

### 13.1 Decision guide

| Finding | Primary posture |
|---|---|
| Support aged; substance not identified as wrong | Mark stale after review; preserve historical scope |
| Support unresolved | `ABSTAIN` or `HOLD` |
| Substance possibly incorrect | Hold current-sensitive use and investigate evidence |
| Substance incorrect | Open correction or withdrawal case |
| Rights prohibit continued exposure | Hold or withdraw through authorized release/correction path |
| Valid successor exists | Supersede with explicit lineage and retained predecessor |
| No safe successor exists | Withdraw with explicit reason and affected-surface handling |
| New release caused unsafe state | Rollback review against a verified prior target |
| AI answer needs updating | New receipt and cross-reference; never retroactive edit |

### 13.2 Correction handoff

Use [CORRECTION_RUNBOOK.md](./CORRECTION_RUNBOOK.md) when the substance, units, source role, evidence, geometry, time, rights, sensitivity, release support, or public representation is wrong or materially unsupported.

A stale badge is insufficient when:

- a value or assertion was incorrect;
- AQI was represented as concentration;
- AOD was represented as PM2.5;
- model output was represented as observation;
- a provisional product was represented as certified/final;
- a public statement lacks evidence or cites the wrong source/version;
- rights or sensitivity make the released representation impermissible;
- the wrong artifact was served.

### 13.3 Supersession invariants

- retain the prior object for audit and time-bound use where permitted;
- record explicit predecessor/successor links;
- record effective time;
- preserve object-family and source-role meaning;
- require correction/withdrawal support for incorrect substance;
- require affected-surface and rollback support for published state;
- do not use a newer version as permission to erase history;
- do not rewrite AI receipts.

### 13.4 Rollback handoff

Use [ROLLBACK_RUNBOOK.md](./ROLLBACK_RUNBOOK.md) only after identifying a verified target and authorized rollback decision. A stale-state finding alone is not rollback authority.

### 13.5 Release and promotion

A refreshed or corrected successor follows the normal governed path. Use [PROMOTION_RUNBOOK.md](./PROMOTION_RUNBOOK.md) for readiness evaluation. Merge, green CI, and file placement do not promote or publish the successor.

[Back to top](#top)

---

## 14. Review handoff packet

A public-safe packet should contain:

```yaml
case_id: "<stable case identity>"
repository_revision: "<exact commit>"
subject:
  object_ref: "<governed reference>"
  object_family: "<family>"
  version: "<version>"
  declared_state: "<state>"
  exposure: "<exposure>"
requested_use:
  operation: "<operation>"
  audience: "<audience>"
  time_scope: "<scope>"
stale_evaluation:
  marker: "<shared marker>"
  detected_at: "<UTC or null>"
  basis_refs: []
  substance_status: "<status>"
time_posture:
  observed_at: null
  source_updated_at: null
  retrieved_at: null
  model_initialized_at: null
  valid_from: null
  valid_to: null
  expires_at: null
  released_at: null
  corrected_at: null
lineage:
  predecessor_ref: null
  successor_ref: null
  relation: "<relation>"
  effective_at: null
  prior_retained: true
  silent_rebind: false
proposed_response:
  action: "<action>"
  correction_ref: null
  withdrawal_ref: null
  rollback_ref: null
  decision_refs: []
  affected_surface_refs: []
review:
  state: "<PENDING|UNKNOWN|COMPLETE_FOR_DECLARED_SCOPE>"
  record_refs: []
validation:
  commands: []
  exact_head: "<commit>"
  result: "<PASS|FAIL|NOT_RUN|PENDING>"
  limitations: []
non_effects:
  - no_live_source_activation
  - no_object_mutation
  - no_policy_or_review_authority
  - no_release_deployment_or_publication
```

Do not copy this illustrative shape into a trust-bearing store as though it were an accepted schema. Where the shared candidate profile applies, use its exact contract and schema.

### Minimum narrative

The handoff must say:

- what was observed;
- what is confirmed versus proposed or unknown;
- why stale is or is not supported;
- whether substance was assessed;
- which source/evidence/time/lineage references support the conclusion;
- what public or internal surfaces may be affected;
- which authority owns the next action;
- what validation ran at which exact revision;
- what did not occur.

[Back to top](#top)

---

## 15. Operator checklist

### Before assessment

- [ ] Exact subject reference, family, version, state, and exposure are pinned.
- [ ] Requested operation, audience, geography, and time scope are explicit.
- [ ] Actual SourceDescriptor and activation/admission posture resolve; placeholders are not treated as admitted sources.
- [ ] Source role, rights, sensitivity, cadence/support condition, and source-head identity are reviewable.
- [ ] Observation, source, retrieval, model, validity, expiry, release, and correction times remain distinct.
- [ ] Evidence/basis references resolve or the case remains `ABSTAIN`/`HOLD`.
- [ ] Active correction, release, rollback, migration, issue, and PR overlap is checked.
- [ ] Required reviewer and release authority are identified without inferring authority from CODEOWNERS.
- [ ] No credentials, private endpoints, restricted details, raw queries, or life-safety advice are in the public packet.

### During assessment

- [ ] Exactly one supported marker or `UNKNOWN` is recorded.
- [ ] Detection time is UTC and does not postdate evaluation.
- [ ] Substance status is evaluated separately from stale state.
- [ ] AQI/concentration, AOD/PM2.5, model/observation, provisional/final, and advisory/official-instruction boundaries are preserved.
- [ ] Prior object is retained; no self-link or silent rebind is proposed.
- [ ] AI receipts are not retroactively edited.
- [ ] Published supersession/withdrawal includes rollback and affected-surface references.
- [ ] Incorrect substance includes correction or withdrawal support.
- [ ] Fixture validation, when applicable, records exact head, commands, result, and limitations.

### Before handoff

- [ ] Outcome is one of `REVIEW_REQUIRED`, `ABSTAIN`, `DENY`, `ERROR`, or an explicit work-state `HOLD`.
- [ ] No fixture result is labeled approval.
- [ ] Affected API/map/tile/search/graph/export/AI/cache/documentation surfaces are inventoried.
- [ ] Official-source redirection is retained for current-sensitive advisory context.
- [ ] Correction, withdrawal, supersession, rollback, and release responsibilities remain separate.
- [ ] Packet states that no object, release, deployment, promotion, or publication changed.

### After a separately authorized change

- [ ] Authoritative object/release state is read back.
- [ ] Prior lineage remains inspectable.
- [ ] Served carrier digests/versions match the authorized state.
- [ ] Governed API and every affected derivative expose the correct state and time scope.
- [ ] Cache invalidation and monitoring are verified rather than assumed.
- [ ] Corrected generated answers are new receipts with cross-references.
- [ ] Official-source redirect and non-life-safety boundary remain visible.

[Back to top](#top)

---

## 16. Current holds and open verification

| Item | Status | Evidence required before relying on it |
|---|---|---|
| Accountable Atmosphere/source/evidence/policy/review/release/cache owners | `NEEDS VERIFICATION` | Accepted assignments, authority scope, expiry/revocation, and separation rules |
| Concrete admitted Atmosphere SourceDescriptors | `HOLD / incomplete` | Complete descriptors, rights/sensitivity review, cadence/support rules, activation decisions, and registry resolution |
| Exact source cadences and stale tolerances | `UNKNOWN` | Source-specific accepted profiles; do not place universal numbers in this runbook |
| Executable Atmosphere connector | `ABSENT at inspected lane` | Connector modules, tests, fixtures, admission binding, receipts, safe destinations, and no-network import behavior |
| Active Atmosphere freshness policy | `PROPOSED scaffold` | Accepted bundle, input contract, evaluator, version, obligations, negative fixtures, activation record, and rollback |
| Broad shared freshness validator | `README-only / NEEDS VERIFICATION` | Executable implementation, closed inputs, fixtures, tests, CI, report/receipt routing, and policy/release integration |
| Shared stale-state assessment | `CONFIRMED fixture-only` | Operational graduation still requires real-object binding, authenticated review, policy, persistence, and transition executor |
| Cross-lane stale propagation | `UNKNOWN / unresolved` | Accepted decision for Atmosphere-to-Hazards/Agriculture/Hydrology/Biodiversity and shared carrier behavior |
| Public UI/API stale indicators | `UNKNOWN` | Exact runtime code, governed envelope contracts, accessibility tests, screenshots/read-back, and release evidence |
| Carrier/cache invalidation | `UNKNOWN` | Accepted propagation plan, authoritative carrier inventory, execution receipts, and post-change read-back |
| Operational correction/withdrawal/rollback | `PARTIAL documentation / HOLD execution` | Complete contracts/schemas/policy, authenticated authority, tested executors, drills, and release-bound evidence |
| Actual Atmosphere published releases | `UNKNOWN` | Release manifests, proofs, policy/review records, serving evidence, correction path, and rollback targets |
| Deployment/publication state | `UNKNOWN` | Runtime, hosting, release, monitoring, correction, and rollback evidence—not merge or documentation state |
| Required-check coupling | `NEEDS VERIFICATION` | Ruleset evidence that exact checks are required for the relevant transition |

Do not close an item by adding prose. Close it only with current, pinned evidence from the owning authority.

[Back to top](#top)

---

## 17. Maintenance and document rollback

### 17.1 Updating this runbook

Update this file when repository evidence materially changes, including:

- an Atmosphere source is admitted with an accepted cadence/support profile;
- an active Atmosphere freshness policy and evaluator are accepted;
- the broad freshness validator becomes executable;
- a stale-state propagation decision is accepted;
- a governed public envelope or UI behavior is implemented and tested;
- correction, withdrawal, rollback, cache invalidation, or release execution graduates;
- accountable owners are assigned;
- a real Atmosphere stale-state drill produces reviewable evidence.

For every update, pin the evidence revision, preserve prior limitations, and separate repository implementation from release/deployment/publication state.

### 17.2 Rolling back this documentation change

Before merge, close the pull request and delete the scoped branch. After an authorized merge, use a transparent revert or forward-fix pull request against the actual merged commit. Do not rewrite shared history.

Document rollback changes guidance only. It does not restore or alter a source, EvidenceBundle, release, public carrier, cache, deployment, or publication state.

[Back to top](#top)

---

## 18. Related current surfaces

### Governing and cross-cutting

- [Directory Rules v2](../../doctrine/directory-rules.md)
- [ADR-0029 — Adopt Directory Governance Standard v2](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Stale-state and supersession navigational reference](../../atlases/stale-state-reference.md)
- [Shared stale-state assessment contract](../../../contracts/common/stale_state_supersession_assessment.md)
- [Shared stale-state assessment schema](../../../schemas/contracts/v1/common/stale_state_supersession_assessment.schema.json)
- [Shared stale-state fixture cases](../../../fixtures/contracts/v1/common/stale_state_supersession_assessment/cases.json)
- [Shared stale-state validator](../../../tools/validators/governance/validate_stale_state_supersession_assessment.py)
- [Shared stale-state workflow](../../../.github/workflows/stale-state-supersession-assessment.yml)
- [Freshness validator lane](../../../tools/validators/freshness/README.md)

### Atmosphere

- [Atmosphere domain README](../../domains/atmosphere/README.md)
- [Atmosphere source registry lane](../../../data/registry/sources/atmosphere/README.md)
- [Atmosphere connector boundary](../../../connectors/atmosphere/README.md)
- [Atmosphere freshness policy scaffold](../../../policy/domains/atmosphere/freshness_gate.rego)
- [Atmosphere domain workflow](../../../.github/workflows/domain-atmosphere.yml)
- [Atmosphere source-refresh runbook](./SOURCE_REFRESH_RUNBOOK.md)
- [Atmosphere validation runbook](./VALIDATION_RUNBOOK.md)
- [Atmosphere no-network test runbook](./NO_NETWORK_TEST_RUNBOOK.md)
- [Atmosphere promotion runbook](./PROMOTION_RUNBOOK.md)
- [Atmosphere correction runbook](./CORRECTION_RUNBOOK.md)
- [Atmosphere rollback runbook](./ROLLBACK_RUNBOOK.md)

---

## Change history

| Date | Version | Change | Effect |
|---|---|---|---|
| Prior to 2026-08-24 | scaffold | Placeholder pointed to the domain missing/planned-file inventory. | No operational procedure. |
| 2026-08-24 | v1.0 | Replaced scaffold with a repository-grounded stale-state assessment, containment, validation, lineage, carrier-review, correction/rollback handoff, checklist, and open-verification procedure. | Documentation only; no source, object, policy, review, release, deployment, promotion, publication, alert, or public state changed. |

[Back to top](#top)
