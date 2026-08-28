<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-atmosphere-readme
title: Atmosphere Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; pre-publication; freshness-aware
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
lane_role: atmosphere candidate dossier index and time-aware pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 0c28949d97cc718bd25b9cfa2a6470d46dc67f8d
  prior_blob: 9a454a6a77f2393583d505c7a84f2828a236fced
  bounded_candidate_inventory: parent README only; no child candidate dossier established
related:
  - ../README.md
  - ../../README.md
  - ../../reviews/README.md
  - ../../reviews/atmosphere/README.md
  - ../../manifests/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ../../../data/processed/atmosphere/README.md
  - ../../../data/published/atmosphere/README.md
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../data/proofs/atmosphere/README.md
  - ../../../data/proofs/atmosphere/pm25_2026/README.md
  - ../../../contracts/domains/atmosphere/README.md
  - ../../../schemas/contracts/v1/domains/atmosphere/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../tests/domains/atmosphere/README.md
  - ../../../fixtures/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
  - ../../../docs/domains/atmosphere/RELEASE_INDEX.md
  - ../../../docs/domains/atmosphere/PIPELINE.md
  - ../../../docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, atmosphere, air, time-validity, freshness, source-role, evidence, review, rollback]
notes:
  - "This README indexes Atmosphere release-candidate dossiers and defines their pre-publication review boundary. It is not a candidate, source, evidence, policy, review, release, regulatory, medical, emergency, or publication authority record."
  - "The bounded repository search and current Atmosphere workflow establish no child candidate dossier under this lane."
  - "The literal sentence 'A candidate is not a release.' is retained for the current domain-atmosphere readiness workflow; it is a compatibility signal, not release proof."
  - "Atmosphere candidates must preserve pollutant, source-role, knowledge-character, unit, averaging-window, time-validity, freshness, caveat, correction, and official-authority boundaries."
  - "CODEOWNERS review routing is not a stewardship assignment, independent review, release approval, medical or regulatory authority, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/atmosphere/` — Atmosphere Release Candidate Review Lane

> Index Atmosphere release-candidate dossiers, preserve their blockers and governed support pointers, and prevent weather, climate, air-quality, smoke, aerosol, forecast, model, or advisory-context material from being treated as current, authoritative, released, medically actionable, or emergency-authoritative before evidence, time, policy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-atmosphere%2Fair-0aa)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![freshness](https://img.shields.io/badge/freshness-load--bearing-blue)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@0c28949d…`:** the bounded Atmosphere candidate inventory contains this parent README and no verified child candidate dossier. The Atmosphere release register is intentionally empty, emitted published artifacts remain unverified, and the current workflows are readiness holds or TODO scaffolds. No inspected candidate, proof README, policy scaffold, workflow result, merge, or generated receipt establishes an Atmosphere release.
>
> Differently named, unindexed, generated, history-only, external, restricted-system, or runtime-only material remains **UNKNOWN** until directly verified.

## Quick navigation

[Purpose](#purpose) ·
[Status](#status-and-evidence-boundary) ·
[Authority](#authority-and-repository-fit) ·
[Inventory](#current-candidate-inventory) ·
[Lifecycle](#candidate-lifecycle) ·
[Contents](#what-belongs-here) ·
[Exclusions](#what-does-not-belong-here) ·
[Admission](#candidate-admission-contract) ·
[Identity](#atmosphere-identity-and-anti-collapse) ·
[Time](#time-validity-freshness-and-stale-state) ·
[Gates](#atmosphere-release-gates) ·
[Dossier](#required-dossier-structure) ·
[Validation](#validation-proof-and-fixture-posture) ·
[Automation](#automation-posture) ·
[Handoff](#review-and-release-handoff) ·
[Correction](#correction-withdrawal-and-rollback) ·
[Public boundary](#public-api-map-and-ai-boundary) ·
[Maintenance](#maintenance-and-definition-of-done) ·
[Evidence](#evidence-ledger) ·
[Open items](#open-verification) ·
[Rollback](#rollback-for-this-readme)

---

## Purpose

`release/candidates/atmosphere/` is the Atmosphere/Air pre-publication review lane under the `release/` responsibility root.

It exists to answer these bounded questions:

1. Which Atmosphere candidate dossiers are currently indexed?
2. What object, pollutant, source-role, knowledge-character, spatial, temporal, audience, and artifact scope does each candidate claim?
3. Which source, evidence, rights, policy, validation, review, correction, and rollback records support it?
4. Is the candidate current for the requested time and use, or stale, expired, superseded, corrected, or withdrawn?
5. Which shared release lane owns the next governed record?

**A candidate is not a release.** A candidate folder, README, workflow result, proof index, schema pass, review note, pull request, merge, generated receipt, public URL, or file under `data/published/` does not by itself authorize public use.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or repository event.

[Back to top](#top)

---

## Status and evidence boundary

| Field | Current posture |
|---|---|
| Document type | Atmosphere candidate-lane index and review contract |
| Owning root | `release/` |
| Candidate lane | `release/candidates/atmosphere/` |
| Bounded child inventory | No child candidate dossier established |
| Active candidate | None verified |
| Manifest-ready candidate | None verified |
| Published Atmosphere release | None verified by the inspected release register |
| Candidate artifact inventory | **UNKNOWN** beyond README-level records |
| Executable candidate validation | Not established |
| Proof support | Draft parent plus documented `pm25_2026/` child; concrete proof artifacts unverified |
| Policy enforcement | Greenfield scaffold; runtime enforcement unknown |
| Public/release effect of this README | None |
| Default posture | Hold, narrow, abstain, deny, or error rather than infer authority or freshness |

### Truth labels

| Label | Meaning here |
|---|---|
| `CONFIRMED` | Verified from a repository file, immutable ref/blob, workflow definition/run, or generated artifact in the current session |
| `PROPOSED` | Candidate meaning, path, rule, gate, or implementation direction not yet accepted or enforced |
| `UNKNOWN` | Not resolved by the bounded inspection |
| `NEEDS VERIFICATION` | Checkable, but not verified strongly enough to act as fact |
| `CONFLICTED` | Current repository or doctrine sources disagree and no accepted decision resolves the difference |
| `LINEAGE` | Historical or planning material retained for traceability, not current authority by itself |

Finite outcomes such as `HOLD_FOR_FRESHNESS`, `ABSTAIN`, `DENY`, or `PROMOTE_TO_MANIFEST` are operational states, not replacements for these truth labels.

[Back to top](#top)

---

## Authority and repository fit

Directory Rules assign each concern to its responsibility root. This lane owns candidate review state and safe pointers only.

| Responsibility | Owning lane |
|---|---|
| Atmosphere candidate dossiers and blockers | This lane |
| Cross-domain candidate policy | [`release/candidates/`](../README.md) |
| Atmosphere release-review records | [`release/reviews/atmosphere/`](../../reviews/atmosphere/README.md) |
| Candidate artifacts | [`data/processed/atmosphere/`](../../../data/processed/atmosphere/README.md) or accepted staging lane |
| Source admission, cadence, rights, and source role | [`data/registry/sources/atmosphere/`](../../../data/registry/sources/atmosphere/README.md) |
| Evidence and proof support | [`data/proofs/atmosphere/`](../../../data/proofs/atmosphere/README.md) |
| Semantic meaning | `contracts/domains/atmosphere/` |
| Machine-checkable shape | `schemas/contracts/v1/domains/atmosphere/` |
| Admissibility, public-use obligations, and denial | `policy/domains/atmosphere/` |
| Executable tests and fixtures | `tests/domains/atmosphere/` and `fixtures/domains/atmosphere/` |
| Validators | `tools/validators/` |
| Promotion decision | [`release/promotion_decisions/`](../../promotion_decisions/README.md) |
| Release manifest | [`release/manifests/`](../../manifests/README.md) or accepted successor |
| Correction, withdrawal, and rollback records | Shared release-governance lanes |
| Published public-safe carriers | [`data/published/atmosphere/`](../../../data/published/atmosphere/README.md) |
| Public client access | Governed APIs and released carriers only |

The lane must not become a parallel source registry, proof store, policy home, review authority, manifest store, published-data store, AQI service, alerting service, or medical guidance surface.

[Back to top](#top)

---

## Current candidate inventory

The bounded repository search and the `domain-atmosphere` workflow establish no child candidate dossier under this lane.

| Candidate | Scope | Status | Manifest readiness | Public effect |
|---|---|---|---|---|
| *(none verified)* | — | `NO_ACTIVE_CANDIDATE_VERIFIED` | Not approved | None |

The documented `data/proofs/atmosphere/pm25_2026/` child is a proof-lane README, not an Atmosphere release candidate, candidate artifact, release manifest, AQI product, regulatory determination, or public advisory.

### Inventory limits

Code search is not a recursive filesystem proof. Other candidates, ignored files, generated workspaces, history-only records, external systems, restricted stores, or differently named paths remain **UNKNOWN** until directly inspected.

Add an inventory row only after:

- the child path exists;
- its dossier can be read safely without exposing restricted or operational detail;
- its stable identity and explicit non-release state are verified; and
- its evidence snapshot is immutable enough to support the claim.

Do not add roadmap ideas, source families, proof children, model runs, or release-index examples as active candidates.

[Back to top](#top)

---

## Candidate lifecycle

Use finite states and preserve the distinction between dossier maturity, currentness, and release authority.

| Candidate state | Meaning | Permitted next step |
|---|---|---|
| `PROPOSED` | Candidate identity exists; packet is incomplete | Assemble governed support |
| `ASSEMBLING` | Artifact and review packet are being gathered | Continue closure |
| `READY_FOR_REVIEW` | Packet is complete enough for formal review | Open a governed release review |
| `BLOCKED` | One or more named gates are unresolved | Hold and remediate |
| `REPAIR_REQUIRED` | Candidate or support records are defective | Return to owning upstream lane |
| `STALE` | Candidate no longer satisfies freshness or validity requirements | Refresh, supersede, withdraw, or re-review |
| `DEFERRED` | Candidate remains eligible but is not advancing | Preserve review trigger |
| `APPROVED_FOR_MANIFEST` | A governed decision permits manifest preparation | Prepare manifest in accepted lane |
| `PROMOTED` | Candidate is bound into an approved release path | Preserve release lineage |
| `SUPERSEDED` | A newer candidate replaces it | Link replacement; retain history |
| `WITHDRAWN` | Candidate is removed from consideration | Record reason and affected pointers |

`APPROVED_FOR_MANIFEST` does not mean `PUBLISHED`. `PROMOTE_TO_MANIFEST` authorizes manifest preparation only.

### Explicit hold outcomes

Prefer named holds:

- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_SOURCE_ROLE`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_TIME_SEMANTICS`
- `HOLD_FOR_FRESHNESS`
- `HOLD_FOR_UNITS`
- `HOLD_FOR_KNOWLEDGE_CHARACTER`
- `HOLD_FOR_CAVEATS`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`

[Back to top](#top)

---

## What belongs here

- This parent README and public-safe candidate index.
- One child directory per distinct Atmosphere release candidate.
- Candidate dossiers recording stable identity, scope, time posture, blockers, review state, and finite decision.
- Immutable pointers to processed or staged artifacts without duplicating payloads.
- Public-safe pointers to source admission, EvidenceBundle support, validation, policy, review, correction, withdrawal, supersession, and rollback records.
- Candidate version and supersession notes.
- Freshness, stale-state, update-cadence, model-run, and correction notes.
- Safe summaries explaining why a candidate is held, repaired, deferred, approved for manifest preparation, superseded, or withdrawn.
- Migration notes when accepted release topology changes.

Candidate records should be compact, pointer-based, non-operational, and safe for repository review.

[Back to top](#top)

---

## What does not belong here

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads.
- Sensor feeds, station dumps, advisory text captures, model grids, forecast files, rasters, tiles, COGs, PMTiles, Parquet, CSV, GeoJSON, API payloads, or reports by value.
- Source descriptors, API keys, service credentials, private endpoints, operational tokens, or source dumps.
- EvidenceBundle or proof content as the primary record.
- Contracts, schemas, policy modules, validators, tests, fixtures, pipelines, or packages.
- Final `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard` records when shared lanes own them.
- Mutable “latest” pointers offered as candidate identity.
- Medical diagnosis, exposure advice, public-health direction, evacuation direction, emergency alerting, regulatory enforcement, permit decisions, or life-safety instructions.
- AQI values presented as pollutant concentration.
- AOD presented as surface PM2.5 concentration.
- Model or forecast fields presented as observation.
- Preliminary reporting presented as final regulatory quality.
- Low-cost sensor output without visible correction and caveat posture.
- Stale observations, forecasts, models, advisories, or rights state presented as current.
- Generated prose presented as evidence, validation, review, regulatory authority, or release approval.

[Back to top](#top)

---

## Candidate admission contract

A child candidate may be indexed only when it has a stable identity and an explicit non-release state.

### Minimum fields at candidate creation

| Field | Requirement |
|---|---|
| Candidate ID and version | Stable and distinct from release, run, source, layer, and manifest IDs |
| Candidate owner | Verified GitHub identity or `OWNER_TBD`; never invent a team |
| Candidate family | Observation, station, AQI/report context, AOD, smoke, model, forecast, advisory context, climate, or other accepted family |
| Pollutant or variable | Explicit; no pollutant-family collapse |
| Source role | Authority, observation, context, model, or other accepted role |
| Knowledge character | Observed, preliminary, corrected, derived, modeled, forecast, proxy, advisory context, or other accepted value |
| Artifact pointer and digest | Immutable pointer or `NOT ESTABLISHED` |
| Geography/grid | CRS, geometry/grid semantics, extent, resolution, and public-surface posture |
| Units and averaging window | Explicit and contract-bound |
| Time semantics | Observed, valid, issued, model-run, retrieval, processing, correction, expiry, and stale markers as applicable |
| Source/evidence state | Explicit closure or blocker |
| Rights and redistribution | Explicit posture or blocker |
| Caveat/disclosure state | Visible and versioned where required |
| Validation and review | Performed checks, failures, and not-run checks |
| Proposed release target | Pointer or `NOT ESTABLISHED` |
| Correction/rollback state | Pointer or explicit blocker |
| Finite decision | Proposed, hold, repair, defer, approve-for-manifest, supersede, or withdraw |
| Immutable evidence snapshot | Required for repository-state claims |

### Candidate identity rules

- Do not derive meaning solely from a folder name.
- Do not reuse an ID after material changes to pollutant, measure, source set, knowledge character, grid, units, time basis, correction, public audience, or artifact bytes.
- Do not mutate an approved packet in place; supersede it with traceable lineage.
- Preserve content digests and source/model/run identities where practical.
- Do not use floating “current” or “latest” without a resolved immutable version and freshness state.
- Keep candidate identity distinct from source, observation, model run, forecast, advisory, release, manifest, layer, and proof identity.

[Back to top](#top)

---

## Atmosphere identity and anti-collapse

Atmosphere candidates are especially vulnerable to semantic and source-role collapse.

### Knowledge-character rules

| Boundary | Required posture |
|---|---|
| AQI vs concentration | AQI is an index/reporting construct, not a concentration unit |
| AOD vs surface PM2.5 | AOD is a column aerosol proxy, not direct surface concentration |
| Model vs observation | Forecast/model fields must remain modeled |
| Preliminary vs regulatory-final | Near-real-time or preliminary reports must not be presented as final regulatory determinations |
| Low-cost vs reference-grade sensor | Preserve sensor class, correction method, uncertainty, and caveats |
| Smoke analysis vs measured pollutant | Analyst polygons/context do not prove local concentration |
| Advisory context vs emergency authority | Redirect to official issuing authority; do not issue independent instructions |
| Climate normal/anomaly vs current weather | Preserve temporal basis and interpretation boundary |

### Source-role rules

| Source role | Candidate rule |
|---|---|
| `authority` | Preserve legal, reporting, and validity scope; authority does not make every value current or final |
| `observation` | Preserve instrument/network, QA, calibration, units, averaging, and observation time |
| `context` | May frame a claim; cannot prove concentration, exposure, or regulatory status alone |
| `model` | Preserve model, version, run time, valid time, lead time, uncertainty, and forecast character |
| `proxy` | Preserve inference limits and prohibit direct-equivalence claims |
| `aggregate` | Do not infer point, household, facility, or person-level exposure |
| `candidate` | Remains unreleased until governed promotion |
| `synthetic` | Must remain visibly non-real and excluded from real-world evidence claims |
| `restricted` | Defaults to hold, restrict, generalize, redact, or deny |

Role collapse is release-blocking. A candidate must not upcast observation to authority, model to observation, context to authority, proxy to measurement, aggregate to individual exposure, or candidate to released truth.

[Back to top](#top)

---

## Time validity, freshness, and stale state

Atmosphere candidates are time-aware by default. A timestamp without a time kind is insufficient.

### Required time facets

Record the applicable fields:

- observation start and end;
- averaging period;
- issue/publication time;
- forecast reference or model initialization time;
- valid-from and valid-through;
- forecast lead time;
- retrieval time;
- source-admission time;
- processing time;
- QA/correction time;
- release-review time;
- expiry or stale-after time;
- source cadence and expected next update;
- supersession, withdrawal, or correction effective time.

### Freshness rules

A candidate must be held or marked stale when:

- source cadence expires without a verified refresh;
- a newer source revision, model run, forecast, advisory, calibration, or QA state supersedes it;
- rights or redistribution terms change;
- a review ages out;
- schema, contract, policy, or correction logic changes materially;
- a station, sensor, model, or aggregation definition changes;
- evidence is withdrawn, contradicted, or no longer resolvable; or
- the intended public use is outside the candidate’s validity interval.

### Stale-state behavior

`STALE` is not “probably current.” Stale candidates must not silently feed current maps, APIs, reports, alerts, AI answers, or “latest” indexes.

Required responses include:

- refresh and revalidate;
- narrow the temporal claim;
- display stale/superseded state;
- abstain;
- hold;
- correct;
- withdraw; or
- supersede with a governed replacement.

[Back to top](#top)

---

## Atmosphere release gates

Every candidate fails closed when a load-bearing gate is unresolved.

| Gate | Required question | Failure posture |
|---|---|---|
| Identity | Is the candidate stable, versioned, scoped, and owned? | `HOLD_FOR_ARTIFACT` |
| Artifact | Is there an immutable pointer and digest? | `HOLD_FOR_ARTIFACT` |
| Meaning and shape | Are object family, pollutant/variable, fields, units, averaging, grid, and schema defined? | Repair or hold |
| Source admission | Do all sources resolve to admitted records with role, cadence, rights, and QA posture? | `HOLD_FOR_SOURCE_ADMISSION` |
| Knowledge character | Are observation, model, forecast, proxy, authority, preliminary, and advisory roles preserved? | `HOLD_FOR_KNOWLEDGE_CHARACTER` |
| Evidence | Do claim/field `EvidenceRef` values resolve to admissible `EvidenceBundle` support? | `HOLD_FOR_EVIDENCE` / `ABSTAIN` |
| Time semantics | Are time kinds and validity intervals explicit? | `HOLD_FOR_TIME_SEMANTICS` |
| Freshness | Is the candidate current for the requested use and audience? | `HOLD_FOR_FRESHNESS` |
| Rights and sensitivity | Is redistribution and requested precision allowed? | Deny, restrict, redact, generalize, or hold |
| Caveats | Are correction, uncertainty, proxy, low-cost, preliminary, and model caveats visible? | `HOLD_FOR_CAVEATS` |
| Policy | Is a versioned `PolicyDecision` present with obligations and reason codes? | `HOLD_FOR_POLICY` |
| Validation | Do deterministic positive and negative checks pass? | `HOLD_FOR_VALIDATION` |
| Review | Are required, distinct reviewers recorded? | `HOLD_FOR_REVIEW` |
| Release topology | Are review, decision, manifest, correction, and rollback homes accepted? | `HOLD_FOR_RELEASE_TOPOLOGY` |
| Correction | Can errors and stale state propagate to all consumers? | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Is a prior safe target or withdrawal plan defined and drilled? | `HOLD_FOR_ROLLBACK` |

`PROMOTE_TO_MANIFEST` permits manifest preparation only. It does not authorize public rendering, medical use, regulatory use, emergency use, or publication.

[Back to top](#top)

---

## Required dossier structure

A child README should include at least:

```markdown
# <candidate-id> — <candidate title>

## Candidate status
PROPOSED / ASSEMBLING / READY_FOR_REVIEW / BLOCKED / REPAIR_REQUIRED /
STALE / DEFERRED / APPROVED_FOR_MANIFEST / PROMOTED / SUPERSEDED / WITHDRAWN

## Candidate identity
<id, version, family, pollutant/variable, owner, date, immutable evidence snapshot>

## Proposed scope
<geography/grid, time, audience, artifact family, public surface, intended use>

## Candidate artifact
<immutable pointer, digest, artifact manifest, or NOT ESTABLISHED>

## Meaning and knowledge character
<object family, source role, observed/model/proxy/forecast/advisory character>

## Units and time semantics
<units, averaging period, observed/issued/model-run/valid/retrieved/processed times,
cadence, expiry, stale-state rules>

## Source and rights closure
<SourceDescriptor refs, roles, rights, QA, correction/calibration, blockers>

## Evidence closure
<EvidenceRef-to-EvidenceBundle mapping and unresolved claims>

## Policy, sensitivity, and caveats
<PolicyDecision, audience, obligations, generalization/redaction, caveat strings>

## Validation
<schema, units, time, grid, source role, knowledge character, evidence,
freshness, public boundary, correction, rollback, no-network checks>

## Review
<review record, distinct reviewers, states, dates, unresolved issues>

## Release handoff
<PromotionDecision and ReleaseManifest pointers or explicit blockers>

## Correction and rollback
<correction consumers, stale/supersession path, withdrawal path, rollback target>

## Current decision
<finite outcome plus evidence-grounded reason>
```

Candidate payloads, proof objects, policy code, tests, fixtures, review records, and final release records remain in their owning roots.

[Back to top](#top)

---

## Validation, proof, and fixture posture

Current repository evidence does not establish a complete Atmosphere candidate-validation or release-governance suite.

| Surface | Current safe interpretation |
|---|---|
| [`tests/domains/atmosphere/`](../../../tests/domains/atmosphere/README.md) | Draft scaffold; executable tests, fixture inventory, validators, and CI binding remain unverified |
| `fixtures/domains/atmosphere/` | Required boundary exists; direct payload completeness and consumer coverage remain unverified |
| `tools/validators/domains/atmosphere/` and cross-domain Atmosphere validators | README-backed in current workflow posture; accepted executable command not established |
| [`data/proofs/atmosphere/`](../../../data/proofs/atmosphere/README.md) | Draft proof-lane guide; concrete inventory, schemas, validators, fixtures, access controls, and release linkage unverified |
| [`data/proofs/atmosphere/pm25_2026/`](../../../data/proofs/atmosphere/pm25_2026/README.md) | Documented proof child; not a candidate, AQI service, release, or public advisory |
| `policy/domains/atmosphere/` | Greenfield scaffold; current text over-broadly lists materials that belong in other roots; executable policy unknown |
| [`data/published/atmosphere/`](../../../data/published/atmosphere/README.md) | Draft public-carrier boundary; emitted artifacts, manifests, routes, and release binding remain unverified |
| Atmosphere release register | Intentionally empty; no release entry verified |

### Required negative cases

A mature no-network suite should reject:

- missing or mutable artifact pointers;
- unresolved source identity, role, rights, QA, correction, or cadence;
- AQI/concentration, AOD/PM2.5, model/observation, preliminary/final, or context/authority collapse;
- pollutant-family or unit collapse;
- missing averaging windows;
- ambiguous time kinds or invalid validity intervals;
- stale, superseded, corrected, withdrawn, or expired material presented as current;
- missing low-cost sensor correction and caveats;
- unresolved EvidenceRefs;
- missing policy, review, correction, or rollback support;
- direct public access to candidate, processed, catalog, proof, or internal stores;
- medical, exposure, regulatory, emergency, or life-safety claims without proper external authority; and
- AI prose offered as evidence or approval.

A passing test proves only its declared test scope. It does not approve a candidate or release.

[Back to top](#top)

---

## Automation posture

| Workflow | Current boundary |
|---|---|
| [`domain-atmosphere`](../../../.github/workflows/domain-atmosphere.yml) | Read-only explicit readiness holds for validation, proof, and release-dry-run maturity |
| [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) | TODO-only candidate, promotion-gate, and rollback-card echo jobs |

The Atmosphere workflow:

- uses ordinary pull-request, push, and manual triggers;
- grants `contents: read`;
- uses GitHub-hosted runners;
- disables persisted checkout credentials;
- checks required responsibility boundaries;
- scans for executable tests, validators, proof artifacts/producers, Make targets, and child candidate records; and
- deliberately holds rather than claiming validation, proof, or release.

The release-dry-run workflow still succeeds by executing TODO echoes. That is not candidate assembly, manifest validation, promotion-gate enforcement, rollback verification, release approval, or publication authority.

A green readiness hold means only that the expected scaffold boundary still matches. A failed readiness hold means repository maturity or detector assumptions changed and must be inspected; it does not automatically mean the new material is valid or invalid.

[Back to top](#top)

---

## Review and release handoff

Atmosphere review records have a separate domain lane under [`release/reviews/atmosphere/`](../../reviews/atmosphere/README.md). Review is not release.

Use the narrowest accepted lane for each record:

| Record or action | Route | Candidate-lane boundary |
|---|---|---|
| Candidate dossier | This lane | Pre-publication review packet |
| Release review | `release/reviews/atmosphere/` | Review recommendation; no publication authority |
| Promotion decision | `release/promotion_decisions/` | May permit manifest preparation |
| Release manifest | `release/manifests/` or accepted successor | Release decision record; not payload |
| Correction notice | `release/correction_notices/` | Public communication linked to governed correction |
| Rollback/review card | `release/rollback_cards/` or accepted successor | Current semantics remain draft |
| Withdrawal notice | `release/withdrawal_notices/` | Communication linked to governed withdrawal |
| Release history | `release/changelog/` | Narrative companion, not sovereign state |
| Published carrier | `data/published/atmosphere/` | Downstream after release only |

Before manifest preparation, verify distinct responsibility for:

- domain meaning and pollutant/variable scope;
- artifact production and pipeline operation;
- source admission, rights, QA, correction, and role;
- evidence closure;
- units, time semantics, freshness, and stale-state policy;
- knowledge-character and caveat review;
- validation and adversarial negative cases;
- release review and decision;
- correction, withdrawal, supersession, and rollback; and
- public/API/map/AI safety.

[`CODEOWNERS`](../../../.github/CODEOWNERS) routes `/release/` to `@bartytime4life`. Routing is not a StewardshipAssignment, independent review, release approval, or public-health authority.

[Back to top](#top)

---

## Correction, withdrawal, and rollback

Atmosphere corrections are time-sensitive and must propagate beyond prose.

### Correction triggers

Examples include:

- source correction or invalidation;
- station or sensor QA/calibration change;
- pollutant/unit/averaging error;
- AQI/concentration mapping error;
- revised model run or forecast;
- stale or expired validity;
- rights or redistribution change;
- incorrect advisory-authority framing;
- evidence withdrawal or contradiction;
- public carrier mismatch; or
- policy, schema, contract, or review drift.

### Required correction behavior

A governed correction should identify:

- affected candidate, release, artifact, claim, field, time range, and consumers;
- corrected or superseding artifact;
- effective time;
- evidence and source changes;
- policy/review effect;
- cache, tile, API, search, graph, report, and AI invalidation needs;
- public notice or withdrawal need;
- rollback target; and
- proof that the correction propagated without silently rewriting history.

### Rollback posture

The [`Atmosphere Rollback Runbook`](../../../docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md) is draft and implementation remains unverified. A README rollback is not an operational release rollback.

A candidate is not manifest-ready without a rollback or safe withdrawal plan appropriate to its public consequence.

[Back to top](#top)

---

## Public API, map, and AI boundary

Candidates are internal pre-publication records. Standard clients must not read this lane or canonical/internal stores directly.

Public Atmosphere surfaces must:

- use governed APIs and released carriers;
- preserve source role and knowledge character;
- display pollutant, units, averaging window, observation/issue/valid time, freshness, caveats, and correction state;
- distinguish AQI, concentration, observation, model, forecast, proxy, and advisory context;
- redirect emergency or advisory action to the official issuing authority;
- cite evidence or abstain;
- avoid individual exposure inference from aggregate or station-level data;
- avoid presenting model output as measured truth;
- avoid medical, regulatory, permit, emergency, or life-safety conclusions outside accepted authority; and
- preserve correction, stale-state, supersession, and withdrawal signals.

AI is interpretive, not root truth. A generated explanation cannot create freshness, evidence closure, review, release, or authority.

[Back to top](#top)

---

## Maintenance and definition of done

Update this README when:

- a child candidate is added, renamed, superseded, withdrawn, or removed;
- a candidate changes finite state;
- time, freshness, source-role, pollutant, unit, caveat, or public-surface policy changes;
- Atmosphere tests, fixtures, validators, proofs, policies, review records, or CI mature;
- release-review, manifest, correction, withdrawal, or rollback topology changes;
- CODEOWNERS or stewardship assignments change; or
- a correction reveals that this index overstated repository maturity.

### Definition of done

This lane may graduate beyond draft only when:

- [ ] exhaustive child inventory is deterministically verified;
- [ ] every child exposes stable identity, version, state, decision, and immutable evidence snapshot;
- [ ] object, pollutant, source-role, knowledge-character, units, averaging, and time semantics are machine-checkable;
- [ ] source admission, rights, cadence, QA, correction, and EvidenceBundle closure are enforceable;
- [ ] freshness and stale-state rules are deterministic and tested;
- [ ] candidate schemas, validators, fixtures, and positive/negative tests exist;
- [ ] policy enforces caveats, public boundaries, official-authority redirection, and finite outcomes;
- [ ] candidate validation and release dry-run commands are deterministic and no-network by default;
- [ ] CI invokes accepted commands and cannot turn missing coverage into success;
- [ ] review, promotion, manifest, correction, withdrawal, and rollback topology is accepted;
- [ ] branch protection, required checks, immutable action pinning, and independent reviewers are verified;
- [ ] correction and rollback drills produce safe evidence; and
- [ ] public clients remain downstream of governed APIs and released artifacts.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior README, blob `9a454a6a…` | `CONFIRMED` | Existing generic candidate purpose and workflow marker | Did not record current inventory or implementation maturity |
| [`release/candidates/README.md`](../README.md) | `CONFIRMED file / draft guidance` | Cross-domain candidate states and review fields | Does not establish Atmosphere readiness |
| Bounded candidate-lane search | `CONFIRMED search` | Parent README surfaced; no child dossier established | Not a recursive filesystem proof |
| [`RELEASE_INDEX.md`](../../../docs/domains/atmosphere/RELEASE_INDEX.md) | `CONFIRMED file / draft index` | Release routing, source-role, freshness, anti-collapse rules, empty register | Index is not release authority; examples are illustrative |
| [`data/proofs/atmosphere/`](../../../data/proofs/atmosphere/README.md) | `CONFIRMED draft proof guide` | Proof boundary and `pm25_2026` child existence | Concrete proof inventory and enforcement unresolved |
| [`tests/domains/atmosphere/`](../../../tests/domains/atmosphere/README.md) | `CONFIRMED scaffold` | Intended test responsibilities and no-network posture | Executable enforcement unverified |
| [`policy/domains/atmosphere/README.md`](../../../policy/domains/atmosphere/README.md) | `CONFIRMED greenfield scaffold` | Policy path exists | Current content is not substantive executable policy |
| [`data/published/atmosphere/README.md`](../../../data/published/atmosphere/README.md) | `CONFIRMED published-carrier boundary` | Release-gated public-carrier rules | Emitted artifact and route inventory unverified |
| [`release/reviews/atmosphere/`](../../reviews/atmosphere/README.md) | `CONFIRMED draft review lane` | Domain-specific review fields and outcomes | Review is not release |
| [`domain-atmosphere`](../../../.github/workflows/domain-atmosphere.yml) | `CONFIRMED readiness workflow` | Current structural hold and graduation detectors | Does not validate truth or release |
| [`release-dry-run`](../../../.github/workflows/release-dry-run.yml) | `CONFIRMED TODO scaffold` | Current orchestration placeholder | Green result is not release proof |
| Directory Rules | `CONFIRMED placement doctrine` | Responsibility-root separation and lifecycle invariant | Does not prove implementation completeness |
| CODEOWNERS | `CONFIRMED routing` | Current GitHub review route | Not stewardship, independence, or approval |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive child inventory under `release/candidates/atmosphere/`.
- [ ] Confirm candidate naming, identity, and versioning convention.
- [ ] Confirm accepted candidate artifact/staging and artifact-manifest contracts.
- [ ] Confirm object-family, pollutant, unit, averaging-window, grid, and time schemas.
- [ ] Confirm source admission, source roles, rights, cadence, QA, calibration/correction, and revision identity.
- [ ] Confirm EvidenceRef-to-EvidenceBundle and proof-manifest contracts.
- [ ] Confirm knowledge-character, caveat, preliminary/final, proxy, forecast, model, and advisory-context rules.
- [ ] Confirm deterministic freshness, stale-state, expiry, and supersession behavior.
- [ ] Confirm low-cost sensor correction receipts and public caveat contract.
- [ ] Confirm executable policy and safe reason codes.
- [ ] Confirm deterministic positive/negative fixtures and no-network enforcement.
- [ ] Confirm candidate-specific validator and release-dry-run commands.
- [ ] Confirm candidate-to-review, PromotionDecision, and ReleaseManifest handoff.
- [ ] Resolve singular/plural manifest and rollback/review-card topology.
- [ ] Confirm correction consumers, cache invalidation, withdrawal/supersession, rollback target, and drill.
- [ ] Confirm public API/map/report/AI obligations and official-authority redirection.
- [ ] Confirm branch protection, required checks, action pinning, and independent reviewer assignments.
- [ ] Confirm whether candidate inventory can be generated from machine-readable records without making generated output sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced generic Atmosphere candidate guidance with a repository-grounded, freshness-aware candidate index and review contract.
- Recorded that no child candidate dossier or active candidate is established by the bounded inspection.
- Preserved the exact `A candidate is not a release.` workflow compatibility sentence and the `publication-not_yet` marker.
- Added finite states and holds, admission and identity rules, anti-collapse controls, time/freshness requirements, release gates, dossier structure, validation maturity, automation posture, review handoff, correction/rollback discipline, public-boundary rules, evidence ledger, definition of done, and open verification.
- Added `CONTRACT_VERSION = "3.0.0"` and a bounded evidence snapshot.

### v1 — 2026-07-03

- Replaced the original greenfield stub with initial Atmosphere candidate-lane guidance.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
9a454a6a77f2393583d505c7a84f2828a236fced
```

No candidate artifact, source admission, evidence, policy, validation, review, manifest, release, public carrier, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
