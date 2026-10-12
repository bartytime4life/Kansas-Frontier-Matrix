<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-hazards-readme
title: Hazards Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; time-aware; not-for-life-safety; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
domain: hazards
lane_role: hazards candidate dossier index and time-sensitive pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 24665041c26b914d0916ec60f56a48771484bd75
  prior_blob: 598728cb3e8ea49ca87e12e1320b83ebb73b7536
  bounded_candidate_inventory: parent README only; no child candidate dossier or non-README candidate record established
related:
  - ../README.md
  - ../../README.md
  - ../../manifests/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/RELEASE_INDEX.md
  - ../../../docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/PRESERVATION_MATRIX.md
  - ../../../docs/domains/hazards/DATA_LIFECYCLE.md
  - ../../../docs/domains/hazards/API_CONTRACTS.md
  - ../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/hazards/SOURCE_REFRESH_RUNBOOK.md
  - ../../../docs/runbooks/hazards/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../pipeline_specs/hazards/README.md
  - ../../../pipelines/domains/hazards/README.md
  - ../../../contracts/domains/hazards/README.md
  - ../../../schemas/contracts/v1/domains/hazards/README.md
  - ../../../data/registry/sources/hazards/README.md
  - ../../../data/proofs/hazards/README.md
  - ../../../data/processed/hazards/README.md
  - ../../../data/published/hazards/README.md
  - ../../../fixtures/domains/hazards/README.md
  - ../../../tests/domains/hazards/README.md
  - ../../../policy/domains/hazards/README.md
  - ../../../tools/validators/domains/hazards/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-hazards.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, hazards, time, freshness, expiry, official-referral, not-for-life-safety, evidence, correction, rollback]
notes:
  - "This README indexes Hazards release-candidate dossiers and defines their pre-publication review boundary. It is not a live hazard feed, warning, alert, regulatory determination, emergency instruction, EvidenceBundle, policy decision, release decision, or publication authority."
  - "Bounded repository inspection establishes this README as the only directly indexed file in the candidate lane and establishes no non-README candidate record."
  - "The literal sentence 'A candidate is not a release.' is retained for the current domain-hazards readiness workflow; it is a compatibility signal, not release proof."
  - "KFM Hazards is planning, history, evidence, and resilience context. KFM-as-alert-authority remains denied; official issuers retain warning, advisory, emergency, evacuation, rescue, and regulatory authority."
  - "CODEOWNERS routing is not source admission, hazards stewardship, operational review, independent approval, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/hazards/` — Hazards Release Candidate Review Lane

> Index Hazards release-candidate dossiers, preserve blockers and safe support pointers, and prevent historical events, observations, detections, models, forecasts, warning or advisory context, disaster declarations, exposure summaries, maps, reports, timelines, or generated explanations from being treated as current life-safety guidance, regulatory determinations, evidence closure, or released truth before source, time, freshness, expiry, official-referral, rights, evidence, policy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-hazards-7E2F2F)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![safety](https://img.shields.io/badge/boundary-not__for__life--safety-critical)
![time](https://img.shields.io/badge/time-validity__and__expiry-important)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@24665041c2…`:** bounded repository inspection establishes this README as the only directly indexed file under `release/candidates/hazards/`. No child candidate dossier, non-README candidate record, accepted candidate-manifest contract, emitted Hazards proof, approved `PromotionDecision`, `ReleaseManifest`, or released Hazards artifact was established. The Hazards release index contains explicitly proposed and illustrative release/candidate rows rather than verified release instances. The proof lane reports implementation depth as unknown, policy remains a greenfield scaffold, sampled direct tests are placeholder docstrings, and current domain automation is a readiness/maturity workflow rather than Hazards validation, alerting, or release authority.
>
> Differently named, unindexed, generated, history-only, external, restricted-system, or runtime-only material remains **UNKNOWN** until directly verified.

## Quick navigation

[Purpose](#purpose) ·
[Status](#status-and-evidence-boundary) ·
[Authority](#authority-and-repository-fit) ·
[Inventory](#current-candidate-inventory) ·
[Families](#hazards-candidate-families-and-routing) ·
[Lifecycle](#candidate-lifecycle) ·
[Contents](#what-belongs-here) ·
[Exclusions](#what-does-not-belong-here) ·
[Admission](#candidate-admission-contract) ·
[Identity](#hazard-identity-product-class-and-source-role) ·
[Safety](#life-safety-official-referral-and-authority-boundary) ·
[Time](#time-validity-freshness-expiry-and-stale-state) ·
[Space](#spatial-sensitivity-and-cross-lane-boundaries) ·
[Gates](#hazards-release-gates) ·
[Dossier](#required-dossier-structure) ·
[Validation](#validation-proof-fixture-schema-and-policy-posture) ·
[Automation](#automation-posture) ·
[Handoff](#review-and-release-handoff) ·
[Correction](#correction-withdrawal-supersession-and-rollback) ·
[Public boundary](#public-api-map-export-search-graph-and-ai-boundary) ·
[Maintenance](#maintenance-and-definition-of-done) ·
[Evidence](#evidence-ledger) ·
[Open items](#open-verification) ·
[Rollback](#rollback-for-this-readme)

---

## Purpose

`release/candidates/hazards/` is the Hazards pre-publication review lane under the `release/` responsibility root.

It exists to answer bounded questions:

1. Which Hazards candidate dossiers are currently indexed?
2. What hazard family, object family, product class, geography, scale, and intended audience does each candidate cover?
3. Which admitted sources, source roles, rights, evidence, policy, validation, review, catalog, and release records support it?
4. Which event, issue, valid, expiry, retrieval, processing, release, correction, and stale-state times govern interpretation?
5. Does the candidate preserve observation, detection, model, forecast, regulatory, administrative, aggregate, candidate, and synthetic distinctions?
6. Does the candidate remain planning or evidence context rather than warning, alert, evacuation, rescue, regulatory, or life-safety authority?
7. Does every urgent-use surface refer users to the applicable official source rather than substitute KFM judgment?
8. Can the candidate be corrected, withdrawn, superseded, and rolled back without preserving stale public aliases, caches, tiles, exports, search entries, or generated summaries?

**A candidate is not a release.**

A candidate dossier is a review packet. It does not create a source admission, current-conditions determination, warning, advisory, alert, regulatory decision, EvidenceBundle, `PolicyDecision`, `PromotionDecision`, `ReleaseManifest`, public layer, or governed API authority.

The lifecycle boundary remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, schema parse, test pass, source fetch, model run, warning receipt, branch merge, map render, tile build, catalog entry, graph projection, or generated narrative.

[Back to top](#top)

---

## Status and evidence boundary

| Question | Repository-grounded answer |
|---|---|
| Does the parent candidate README exist? | **CONFIRMED.** This file existed at the pinned base and is revised in place. |
| Are child candidate directories established? | **Not established by bounded indexed search.** No child candidate README or dossier surfaced. |
| Are non-README candidate records established? | **No.** Bounded search and the current domain workflow both support a no-record posture. |
| Is an active Hazards candidate established? | **No.** No accepted dossier, candidate manifest, or promotion handoff was verified. |
| Is a released Hazards artifact established? | **No.** The release index says its rows are proposed templates and that no live Hazards release was confirmed in its evidence session. |
| Is the release index authoritative? | **No.** It is a docs-side navigation mirror; shared release records outrank it. |
| Is a concrete Hazards proof inventory established? | **No.** The proof README says implementation depth remains `UNKNOWN`; the workflow expects no non-README proof artifact. |
| Is executable Hazards policy established? | **No.** `policy/domains/hazards/README.md` remains a greenfield scaffold. |
| Are direct Hazards test modules present? | **Yes, as surfaced paths.** Sampled modules contain only `PROPOSED` placeholder docstrings; accepted suite ownership, collection, and pass rate are not established. |
| Are concrete Hazards schemas present? | **Yes, as `PROPOSED` stubs.** The sampled release-manifest schema is permissive and field-incomplete. |
| Is domain automation present? | **Yes.** It is an explicit readiness workflow with validation, proof, and release-dry-run maturity detectors. |
| Does a green hold prove Hazards correctness or release readiness? | **No.** It proves only that the expected hold posture was observed. |
| Can this README establish current hazard conditions? | **No.** Current conditions require admitted, current, time-valid, source-bound evidence and governed serving. |
| Can this README authorize emergency or regulatory action? | **No.** KFM is not alert, warning, evacuation, rescue, emergency, legal, or regulatory authority. |

### Truth labels used here

| Label | Meaning in this lane |
|---|---|
| **CONFIRMED** | Verified in this session from repository files, workflow definitions, current blobs, or generated artifacts. |
| **PROPOSED** | A design, contract, field, state, routing rule, or implementation expectation not yet proven as accepted executable behavior. |
| **UNKNOWN** | Not established strongly enough by bounded inspection. |
| **NEEDS VERIFICATION** | Checkable through further repository, workflow, runtime, review, source, or release evidence. |
| **CONFLICTED** | Multiple documented terms, homes, roles, or behaviors exist without an accepted reconciliation. |
| **STALE** | Previously supported content is outside its declared validity or freshness tolerance. |

Absence from indexed search is not proof of nonexistence outside the search boundary. It is sufficient only for this README's bounded conclusion: **no active, directly indexed Hazards candidate is established.**

[Back to top](#top)

---

## Authority and repository fit

### Directory Rules basis

`release/candidates/hazards/README.md` remains under the existing `release/` responsibility root because its job is candidate review and release-decision support.

The repository responsibility split is:

```text
docs/domains/hazards/                 # doctrine, explanation, registers, runbooks
contracts/domains/hazards/            # semantic meaning
schemas/contracts/v1/domains/hazards/ # machine shape
data/registry/sources/hazards/        # source identity, role, rights, cadence
data/raw|work|quarantine|processed/   # lifecycle data
data/catalog/ and data/triplets/      # discovery and derived relationship carriers
data/proofs/hazards/                  # proof support
data/receipts/                        # process memory
release/candidates/hazards/           # this review lane
release/manifests/                    # release manifests
release/promotion_decisions/          # promotion decisions
release/correction_notices/           # corrections
release/withdrawal_notices/           # withdrawals
release/rollback_cards/               # rollback decisions
data/published/hazards/               # released public carriers
```

Directory Rules distinguish:

- `data/published/` as the home of released **artifacts**;
- `release/` as the home of release **decisions**;
- `data/receipts/` as process memory, not release proof;
- `data/proofs/` as evidence/proof support, not publication authority;
- public clients as consumers of governed APIs and released carriers, not internal stores.

### Authority order for a candidate review

1. accepted doctrine and ADRs;
2. source admission, rights, sensitivity, and policy authority;
3. accepted semantic contracts and machine schemas;
4. immutable artifact identity and lifecycle state;
5. resolvable evidence and proof support;
6. deterministic validation and receipts;
7. named review state;
8. `PromotionDecision`;
9. `ReleaseManifest`, correction, withdrawal, and rollback records;
10. public carrier registration and governed serving.

This README may summarize and route. It cannot satisfy a gate merely by naming it.

### CODEOWNERS boundary

CODEOWNERS may route review requests. It does not establish:

- source authority;
- hazard or emergency expertise;
- operational-source review;
- policy disposition;
- regulator or issuer status;
- independent approval;
- separation of duties;
- promotion authority;
- release approval;
- life-safety authority.

Those require their own accepted records and review evidence.

[Back to top](#top)

---

## Current candidate inventory

### Directly established lane inventory

| Path | Kind | Status | Safe conclusion |
|---|---|---|---|
| `release/candidates/hazards/README.md` | Parent candidate index | **CONFIRMED present** | This document is guidance and inventory, not a candidate. |
| `release/candidates/hazards/<candidate-id>/` | Child dossier | **Not established** | Do not invent a candidate ID or dossier. |
| Non-README candidate record | Candidate payload or sidecar | **Not established** | No active candidate or manifest-ready dossier is established. |

### Candidate register

| Candidate ID | Hazard family | Product class | Validity | Sensitivity | State | Blocking reason | Evidence |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | `NO_ACTIVE_CANDIDATE` | No child dossier or non-README candidate record established | Bounded repository inspection |

### What does not count as a candidate

None of the following becomes a Hazards candidate merely by existing:

- this README;
- a release-index example row;
- a plan, backlog, blueprint, or runbook;
- a `PROPOSED` schema stub;
- a placeholder test module;
- a validator README;
- a fixture README;
- a source descriptor draft;
- a source-head or watcher notification;
- a processed artifact;
- a catalog record;
- a proof README;
- a receipt;
- a model output;
- a warning or advisory retrieved from an official source;
- a map, tile, chart, dashboard, report, export, screenshot, or graph projection;
- an AI-generated summary;
- a branch, commit, pull request, or green workflow hold.

### Empty inventory behavior

When no candidate is established:

- keep the register empty;
- do not mint a candidate ID;
- do not create a release window;
- do not infer readiness from source availability or apparent urgency;
- do not populate an illustrative release-index row as fact;
- do not create a public alias or `latest` pointer;
- keep public clients on the last governed released state, or abstain if no released state exists.

[Back to top](#top)

---

## Hazards candidate families and routing

This parent lane is currently flat. No child candidate sublane is verified.

Potential candidate families are **routing categories**, not verified directories:

| Family | Examples | Required distinction | Routing posture |
|---|---|---|---|
| Historical events | storm events, flood events, wildfire history, earthquake history | historical record, not current warning | Parent lane until an accepted child exists |
| Observations and detections | gauges, stations, remote-sensing detections, reports | observation/detection, not forecast or confirmed impact | Parent lane |
| Warning/advisory context | watches, warnings, advisories, statements | official context with issue/valid/expiry and referral | Parent lane; restricted operational review may be required |
| Regulatory context | NFHL, declarations, designated zones | issuing authority and effective vintage remain visible | Parent lane |
| Modeled or forecast context | flood, fire, smoke, heat, drought, severe-weather models | model/forecast, not observation or instruction | Parent lane |
| Exposure summaries | population, infrastructure, ecological, agricultural exposure | aggregate planning context, not person/asset-level danger instruction | Parent lane |
| Resilience or scenario summaries | planning scenarios, sensitivity analyses | scenario/assumption surface, not capability certification | Parent lane |
| Timelines and compilations | event timelines, archive summaries | source-role and time semantics remain per item | Parent lane |
| Cross-domain derivatives | Atmosphere, Hydrology, Geology, Infrastructure, Roads, Habitat, Agriculture joins | owning-domain truth remains separate; most restrictive policy wins | Parent lane or accepted cross-domain lane after review |

Create a child lane only when repository evidence establishes:

- a durable candidate family;
- a distinct review burden;
- accepted ownership;
- placement consistent with Directory Rules;
- no duplicate contract, schema, policy, source, proof, or release authority;
- a migration or ADR when an existing topology would conflict.

Until then, keep candidate dossiers under the parent lane only after their exact path is reviewed.

[Back to top](#top)

---

## Candidate lifecycle

### Finite candidate states

| State | Meaning | Public eligibility |
|---|---|---|
| `PROPOSED` | Candidate intent exists; closure is incomplete. | None |
| `ASSEMBLING` | Immutable pointers and support records are being gathered. | None |
| `READY_FOR_REVIEW` | Required dossier fields are present for reviewer evaluation. | None |
| `RESTRICTED_REVIEW` | Review requires controlled operational, infrastructure, rights, or sensitivity context. | None |
| `BLOCKED` | One or more mandatory gates cannot run or failed. | None |
| `REPAIR_REQUIRED` | Candidate may continue after recorded remediation. | None |
| `STALE` | Source, model, warning/advisory, policy, review, or evidence state aged beyond tolerance. | None |
| `DEFERRED` | Review intentionally paused without approval. | None |
| `APPROVED_FOR_MANIFEST` | Review recommends handoff to shared release authority. | None; not yet released |
| `PROMOTED` | A separate accepted promotion and manifest process completed. | Only through released carriers |
| `SUPERSEDED` | A newer candidate or release replaces this version. | Historical review only |
| `WITHDRAWN` | Candidate removed from consideration with reason preserved. | None |

`APPROVED_FOR_MANIFEST` is not `PROMOTED`. `PROMOTED` must resolve to canonical shared release records.

### Explicit hold outcomes

Use a structured hold rather than vague prose:

| Hold | Meaning |
|---|---|
| `HOLD_FOR_ARTIFACT` | Immutable candidate bytes or manifest pointer is missing. |
| `HOLD_FOR_SOURCE_ADMISSION` | A source is not admitted or activation state is unresolved. |
| `HOLD_FOR_SOURCE_ROLE` | Source role or product character is unresolved or collapsed. |
| `HOLD_FOR_RIGHTS` | License, terms, redistribution, attribution, or derivative rights are unresolved. |
| `HOLD_FOR_EVIDENCE` | Material claims do not resolve to inspectable evidence. |
| `HOLD_FOR_IDENTITY` | Hazard/event/product identity or supersession lineage is ambiguous. |
| `HOLD_FOR_TIME_SEMANTICS` | Event, issue, valid, expiry, retrieval, release, or correction times are missing or conflated. |
| `HOLD_FOR_FRESHNESS` | Source, model, observation, warning/advisory, review, or evidence state is stale. |
| `HOLD_FOR_EXPIRY` | Operational context is expired or expiry behavior is not enforced. |
| `HOLD_FOR_OFFICIAL_REFERRAL` | Urgent-use public surfaces do not identify the official issuer or referral route. |
| `HOLD_FOR_LIFE_SAFETY_BOUNDARY` | Candidate could be read as KFM alert, warning, evacuation, rescue, or emergency authority. |
| `HOLD_FOR_KNOWLEDGE_CHARACTER` | Observation, detection, model, forecast, declaration, aggregate, or synthetic character is unclear. |
| `HOLD_FOR_GEOMETRY` | CRS, datum, spatial support, scale, uncertainty, precision, or topology is unresolved. |
| `HOLD_FOR_SENSITIVITY` | Infrastructure, private, cultural, ecological, or other sensitive exposure is unresolved. |
| `HOLD_FOR_CAVEATS` | Public limitations, uncertainty, provisional status, or not-for-life-safety labeling is incomplete. |
| `HOLD_FOR_POLICY` | Policy decision is missing, unavailable, stale, or non-allowing. |
| `HOLD_FOR_VALIDATION` | Required deterministic checks have not passed or cannot run. |
| `HOLD_FOR_REVIEW` | Required domain, time, source, policy, operational, or independent review is missing. |
| `HOLD_FOR_RELEASE_TOPOLOGY` | Candidate cannot resolve accepted promotion and manifest records. |
| `HOLD_FOR_CORRECTION_PATH` | Correction, withdrawal, supersession, or derivative invalidation is incomplete. |
| `HOLD_FOR_ROLLBACK` | A tested rollback target or safe public-state restoration plan is missing. |

A hold is a governed result. It must not be converted to approval by changing wording or hiding the blocker.

### State transition rules

```text
PROPOSED
  -> ASSEMBLING
  -> READY_FOR_REVIEW
  -> APPROVED_FOR_MANIFEST
  -> PROMOTED
```

Permitted side transitions:

```text
ASSEMBLING / READY_FOR_REVIEW
  -> RESTRICTED_REVIEW
  -> BLOCKED
  -> REPAIR_REQUIRED
  -> STALE
  -> DEFERRED
  -> WITHDRAWN
```

Post-decision lineage:

```text
APPROVED_FOR_MANIFEST
  -> BLOCKED          # shared release gate fails
  -> STALE            # support ages before promotion
  -> WITHDRAWN
  -> PROMOTED

PROMOTED
  -> SUPERSEDED
  -> corrected / withdrawn / rolled back through canonical release records
```

No transition is inferred from file placement, pull-request status, merge state, workflow color, or elapsed time.

[Back to top](#top)

---

## What belongs here

This lane may contain small, review-oriented materials whose primary responsibility is Hazards release-candidate evaluation:

- this parent README;
- one candidate dossier directory per accepted candidate identity;
- public-safe review summaries;
- immutable artifact-manifest pointers and digests;
- source descriptor, source-head, rights, and admission references;
- evidence and proof references;
- time, validity, freshness, expiry, and stale-state summaries;
- source-role and product-character summaries;
- policy-decision references and public caveat summaries;
- validation-report and receipt pointers;
- official-issuer and official-referral metadata;
- public-surface inventory and no-alert-authority checks;
- correction, withdrawal, supersession, invalidation, and rollback plans;
- finite review decisions with reason codes;
- references to canonical shared release records after handoff.

Review content stored here must be safe for its repository audience. Restricted source material, precise infrastructure details, credentials, or internal emergency-review substance belongs in an accepted controlled system, not public Markdown.

[Back to top](#top)

---

## What does not belong here

Do not store:

| Material | Correct responsibility home |
|---|---|
| Live source feeds, warning streams, source API responses, or archives | Connectors and `data/raw/` after source admission |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | Their dedicated lifecycle roots |
| Source descriptors or activation decisions | Accepted source-registry and admission homes |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/` |
| Policy rules | `policy/` |
| Executable validators or pipelines | `tools/`, `pipelines/`, or accepted packages |
| Synthetic fixtures and test modules | `fixtures/` and `tests/` |
| EvidenceBundles, ProofPacks, or validation proofs | Accepted `data/proofs/` homes |
| Runtime, validation, transform, AI, release, or watcher receipts | `data/receipts/` |
| Canonical catalog or graph records | `data/catalog/` and `data/triplets/` |
| Release manifests and promotion decisions | `release/manifests/` and `release/promotion_decisions/` |
| Correction, withdrawal, and rollback authority records | Their canonical `release/` lanes |
| Published layers, APIs, reports, timelines, or exports | `data/published/` after release |
| Credentials, tokens, internal endpoints, or privileged incident notes | Approved secret or restricted operational systems |
| Emergency instructions, evacuation routing, rescue guidance, or official warning language authored by KFM | Outside KFM authority |
| Generated text used as evidence, policy, validation, or release proof | Never acceptable as root authority |

This lane must not become an operational alert console, incident-command surface, regulator interface, source-of-record archive, or public-serving endpoint.

[Back to top](#top)

---

## Candidate admission contract

A candidate is eligible for `READY_FOR_REVIEW` only when every applicable field is present, resolvable, and internally consistent.

### Identity and artifact

- stable candidate ID;
- immutable candidate version;
- candidate title and bounded purpose;
- owner and review coordinator;
- hazard family and object families;
- product class and knowledge character;
- artifact kind and lifecycle state;
- immutable artifact pointer;
- artifact digest;
- artifact manifest or equivalent content inventory;
- proposed public carrier and audience;
- predecessor, supersession, or derivation lineage;
- exact candidate scope and explicit exclusions.

### Sources and rights

- admitted source descriptor IDs;
- source-head or source-version references;
- canonical source role for every material input;
- issuing authority where applicable;
- authority scope and known limits;
- rights, license, terms, attribution, redistribution, and derivative-use posture;
- retrieval method and retrieval time;
- source cadence and watcher posture;
- source deprecation, correction, retraction, or supersession state;
- external access or controlled-source restrictions.

### Hazard and product semantics

- event, observation, detection, declaration, warning/advisory context, model, forecast, indicator, aggregate, scenario, or synthetic classification;
- hazard type vocabulary and version;
- severity/intensity/magnitude vocabulary and authority;
- confidence, probability, uncertainty, quality, or provisional flags;
- observation-versus-model-versus-forecast boundary;
- warning/advisory context versus KFM instruction boundary;
- regulatory-context versus KFM determination boundary;
- cross-domain ownership and dependency references;
- known false-positive, latency, incompleteness, and scale limitations.

### Time and freshness

- event start/end or observation time;
- source publication time;
- issue time;
- valid-from and valid-through;
- expiry time;
- forecast/model initialization and lead time when applicable;
- retrieval time;
- processing time;
- evidence time;
- review time;
- release time;
- stale-after rule;
- correction and supersession effective time;
- clock/time-zone semantics;
- behavior after expiry, supersession, source outage, or missing refresh.

### Space and representation

- source CRS and datum;
- processing CRS;
- vertical or depth reference where applicable;
- geometry type and spatial support;
- scale, resolution, precision, uncertainty, and topology;
- observed footprint versus modeled or administrative extent;
- public geometry and field allowlist;
- generalization, suppression, aggregation, or withholding posture;
- infrastructure, private, ecological, archaeological, cultural, or sovereignty sensitivity checks;
- reconstruction-risk assessment across map, export, search, graph, logs, cache, and AI surfaces.

### Evidence and proof

- `EvidenceRef` values for material claims;
- resolvable `EvidenceBundle` support;
- source excerpts or references within rights limits;
- input/output digests;
- validation-report references;
- freshness/expiry proof;
- source-role anti-collapse proof;
- official-referral proof where urgent-use context exists;
- life-safety-boundary proof;
- catalog closure;
- proof status and review state;
- explicit abstention or denial when support cannot close.

### Policy and review

- policy version and digest;
- `PolicyDecision` reference and finite outcome;
- not-for-life-safety decision;
- audience and access class;
- caveat/disclaimer review;
- official-source referral review;
- domain steward review;
- source/rights review;
- temporal/freshness review;
- sensitivity and infrastructure review when applicable;
- operational-context review when applicable;
- independent release review when materiality requires separation;
- unresolved conflicts and waivers, if waivers are allowed at all.

### Release and reversibility

- proposed `PromotionDecision` handoff;
- proposed `ReleaseManifest` content inventory;
- correction path;
- withdrawal path;
- supersession path;
- rollback target;
- derivative invalidation plan;
- cache, tile, export, search, graph, Evidence Drawer, and AI invalidation plan;
- owner and completion evidence for rollback rehearsal;
- public notice posture for stale, corrected, withdrawn, or rolled-back content.

Missing a required field produces a hold, not an inferred default.

[Back to top](#top)

---

## Hazard identity, product class, and source role

### Object-family boundaries

A candidate must identify the object family it carries.

| Object family | Safe interpretation | Disallowed upgrade |
|---|---|---|
| `HazardEvent` | Evidence-supported historical or bounded event record | Current warning, impact forecast, or emergency instruction |
| `HazardObservation` | Measurement, report, or observation with source and quality state | Forecast, verified damage, or regulatory determination |
| `WarningContext` | Officially issued warning context with issue/valid/expiry metadata | KFM warning authority or user-specific safety advice |
| `AdvisoryContext` | Official advisory context and limitations | KFM advisory authority |
| `DisasterDeclaration` | Administrative/regulatory declaration record | Proof of event magnitude, individual eligibility, or legal advice |
| `FloodContext` | Regulatory, historical, observed, modeled, or planning flood context as labeled | Current inundation, forecast certainty, insurance determination, or evacuation guidance |
| `WildfireDetection` | Remote-sensing or reported detection with latency/confidence | Confirmed perimeter, containment, public danger, or evacuation order |
| `SmokeContext` | Observed/modeled smoke context with Atmosphere dependency and freshness | Health diagnosis, exposure instruction, or local measured concentration without evidence |
| `DroughtIndicator` | Named indicator/classification over a time window | Direct farm outcome, water-right determination, or forecast certainty |
| `EarthquakeEvent` | Source-reported event with magnitude/depth/time uncertainty | Structural safety determination or aftershock prediction |
| `HeatColdEvent` | Observation/model/advisory context with time and source role | Medical advice or emergency instruction |
| `ExposureSummary` | Reviewed aggregate exposure context | Individual, household, facility, or exact critical-asset risk determination |
| `ResilienceSummary` | Assumption-bound planning/scenario output | Capability certification, guarantee, or regulatory compliance |
| `HazardTimeline` | Role-aware ordering of events and updates | Live command feed or canonical replacement of source history |
| `ImpactArea` | Observed, modeled, administrative, or aggregate impact geometry as labeled | Exact damage, current danger, or access instruction without direct support |

### Canonical source-role posture

Hazards candidates should use the accepted seven-class source-role vocabulary where applicable:

```text
observed
regulatory
modeled
aggregate
administrative
candidate
synthetic
```

Terms such as `authority`, `context`, `official`, `forecast`, `operational`, `detection`, and `report` may describe issuer, product family, or knowledge character. They must not silently create an eighth source role.

### Required anti-collapse rules

```text
official source -> KFM authority
warning context -> KFM warning
advisory context -> KFM instruction
observation -> forecast
forecast -> observation
model -> observation
detection -> confirmed event perimeter
regulatory context -> KFM regulatory determination
declaration -> event magnitude or individual eligibility
historical event -> current condition
source retrieval -> current validity
issue time -> valid time
valid time -> expiry time
source publication -> KFM release
candidate -> released
schema valid -> semantically valid
test pass -> evidence closure
proof receipt -> EvidenceBundle
catalog entry -> release approval
map or tile -> canonical truth
graph edge -> canonical relation
AI summary -> evidence
```

Every candidate must preserve the original source role and product character through processing, catalog, release, map, export, search, graph, Evidence Drawer, and AI projections.

### Cross-domain ownership

Hazards may cite but must not absorb:

- Atmosphere observations and models;
- Hydrology water, flood, watershed, gauge, and inundation truth;
- Geology faults, subsurface, landslide, and seismic context;
- Settlements/Infrastructure facilities and system status;
- Roads/Rail/Trade access, closure, restriction, bridge, and route truth;
- Agriculture crop, land-use, and operational truth;
- Soil substrate and erosion truth;
- Habitat, Fauna, and Flora ecological truth;
- Archaeology and cultural-resource sensitivity;
- People/Land private, ownership, identity, consent, and living-person truth.

Owner publishes; Hazards cites the released, policy-allowed surface.

[Back to top](#top)

---

## Life-safety, official-referral, and authority boundary

### Non-negotiable boundary

KFM Hazards supports:

- historical review;
- evidence-backed explanation;
- resilience and planning context;
- source comparison;
- public-safe mapping;
- archive and timeline exploration;
- uncertainty and limitation communication.

KFM Hazards does **not** provide:

- emergency alerts;
- watches or warnings authored by KFM;
- evacuation or shelter instructions;
- rescue or incident-command guidance;
- personalized danger assessment;
- route-safety assurance;
- medical or exposure advice;
- structural safety certification;
- insurance, permit, eligibility, or regulatory determinations;
- legal conclusions;
- guaranteed current conditions.

The presence of an official warning, watch, advisory, declaration, or bulletin in a candidate does not transfer issuing authority to KFM.

### Official-source referral contract

Any candidate that contains current-sensitive warning, advisory, forecast, or operational context must define a public referral contract:

- name the official issuer;
- preserve the official source identifier and public reference;
- show issue, valid, expiry, and retrieval times;
- label KFM content as context, not instruction;
- direct urgent decisions to official authorities;
- avoid paraphrasing that changes severity or required action;
- abstain when official state cannot be verified;
- deny personalized life-safety instructions;
- remove or mark expired context;
- record correction and supersession behavior.

Do not store emergency phone numbers or issuer URLs as hard-coded truth in this README. Public referral details belong in reviewed, current, governed configuration or released metadata.

### Finite public outcomes

| Condition | Required outcome |
|---|---|
| Released historical/planning context with evidence and policy closure | `ANSWER` with citation and limitation |
| Evidence insufficient or current state unverifiable | `ABSTAIN` |
| User requests KFM emergency, evacuation, rescue, or life-safety instruction | `DENY` with official-source referral behavior |
| Policy or sensitivity blocks disclosure | `DENY` or `RESTRICT` |
| Required service, policy, evidence resolver, or time validation unavailable | `ERROR` or `ABSTAIN`; never unsafe guidance |
| Candidate, stale, expired, withdrawn, or rolled-back state | No current public answer from that state |

The exact runtime envelope and reason codes remain **NEEDS VERIFICATION** until accepted contracts and executable behavior are verified.

[Back to top](#top)

---

## Time, validity, freshness, expiry, and stale state

Hazards content is unusually time-sensitive. A candidate cannot use a single ambiguous `timestamp`.

### Required time kinds

Record all applicable fields distinctly:

| Time kind | Meaning |
|---|---|
| `event_start` / `event_end` | When the underlying event occurred |
| `observation_time` | When a measurement or observation applies |
| `source_publication_time` | When the source published or updated the record |
| `issue_time` | When a warning, advisory, forecast, bulletin, or declaration was issued |
| `valid_from` / `valid_through` | Intended validity interval |
| `expiry_time` | When operational context must no longer be treated as current |
| `model_initialization_time` | Forecast/model cycle time |
| `forecast_lead_time` | Offset from model initialization to validity |
| `retrieval_time` | When KFM obtained the source state |
| `processing_time` | When KFM transformed or validated it |
| `evidence_time` | Time represented by supporting evidence |
| `review_time` | When human or governed review occurred |
| `release_time` | When a governed public release took effect |
| `correction_effective_time` | When a correction applies |
| `supersession_time` | When a newer source, model, bulletin, or release replaces it |
| `stale_after` | Declared tolerance after which review or refresh is required |

### Time anti-collapse

Do not equate:

```text
event time = issue time
issue time = valid time
valid time = expiry time
retrieval time = current time
source update = KFM release
model initialization = observation time
release time = event time
correction time = silent overwrite time
```

### Stale-state triggers

A candidate becomes `STALE` or blocked when any applicable condition occurs:

- `stale_after` or expiry is reached;
- a newer source record, warning, advisory, forecast cycle, model version, declaration, correction, or release exists;
- source cadence is missed;
- source status is unavailable or revoked;
- rights or terms change;
- source role or authority scope changes;
- evidence is withdrawn, contradicted, or no longer resolves;
- review age exceeds policy tolerance;
- schema, contract, policy, caveat, or public-field profile changes materially;
- a dependency release is corrected, withdrawn, superseded, or rolled back;
- geometry, station, sensor, model, aggregation, or classification methods change;
- current-sensitive content is used outside its valid interval.

### Stale-state behavior

A stale candidate must not:

- silently feed a current map;
- remain behind a `latest` alias;
- answer “now,” “current,” or “safe” questions;
- retain active warning/advisory styling;
- remain in search or graph projections as current;
- support generated current-condition summaries;
- bypass review because the underlying source is official.

Required response:

1. mark candidate and derivatives stale;
2. stop current/public promotion;
3. invalidate affected aliases, caches, tiles, exports, search entries, graph edges, drawer payloads, and AI context;
4. identify the superseding or missing source state;
5. record review, correction, withdrawal, or rebuild action;
6. preserve historical lineage.

### Watchers

Watchers may detect change and queue review. They do not:

- admit a source;
- validate current conditions;
- promote a candidate;
- publish a warning;
- overwrite a release;
- decide policy;
- issue a correction;
- activate a public alias.

[Back to top](#top)

---

## Spatial, sensitivity, and cross-lane boundaries

### Spatial support

Each candidate must declare:

- source geometry versus derived geometry;
- geometry type;
- CRS and datum;
- vertical/depth reference where applicable;
- scale, resolution, precision, and uncertainty;
- bounds and coverage;
- topology requirements;
- observed, modeled, forecast, administrative, regulatory, or aggregate spatial character;
- public generalization and field allowlist;
- out-of-area and edge behavior.

A polygon does not prove uniform conditions inside it. A detection point does not prove a perimeter. An administrative boundary does not prove physical impact. A model grid does not become an observation.

### Sensitivity surfaces

Hazards candidates may expose or help infer:

- critical infrastructure and vulnerabilities;
- shelters, emergency operations, or response capability;
- private properties, facilities, or living-person detail;
- archaeological or cultural sites;
- rare species or sensitive habitat;
- regulated or controlled facility information;
- access routes to restricted areas;
- system weaknesses or outage dependencies;
- precise resource locations;
- source or transform parameters that enable reconstruction.

When sensitivity is unresolved, prefer:

- quarantine;
- aggregation;
- generalization;
- suppression;
- delayed publication;
- reviewer-only access;
- restricted release;
- denial.

This README must not disclose operational transform seeds, offsets, masks, thresholds, hidden precision rules, internal join keys, or reversal aids.

### Cross-lane joins

A joined product inherits:

- the most restrictive sensitivity;
- the narrowest rights posture;
- the least permissive audience;
- the strictest time/expiry requirement;
- the owning domain's truth boundary;
- correction and rollback dependencies from every material input.

A Hazards exposure summary does not own the infrastructure, people, land, ecology, hydrology, atmosphere, geology, roads, agriculture, or cultural truth it cites.

### Reconstruction review

Review all public surfaces together:

```text
map + labels + popups + tiles + exports + search + graph +
Evidence Drawer + logs + caches + screenshots + AI summaries
```

Field removal from one surface is insufficient when the remaining surfaces reconstruct restricted facts.

[Back to top](#top)

---

## Hazards release gates

All applicable gates must close. A green gate cannot override a failing or unavailable gate.

### Gate 1 — candidate identity and immutable artifact

Required:

- stable candidate ID and version;
- immutable artifact pointer;
- digest and content inventory;
- object/product family;
- predecessor and supersession lineage;
- target audience and public surface.

Failure: `HOLD_FOR_ARTIFACT` or `HOLD_FOR_IDENTITY`.

### Gate 2 — source admission, role, rights, and issuer scope

Required:

- admitted source descriptors;
- source versions and heads;
- canonical source roles;
- issuer/authority scope;
- rights and terms;
- retrieval and cadence state;
- source correction/retraction posture.

Failure: `HOLD_FOR_SOURCE_ADMISSION`, `HOLD_FOR_SOURCE_ROLE`, or `HOLD_FOR_RIGHTS`.

### Gate 3 — semantic and knowledge-character integrity

Required:

- event/observation/detection/model/forecast/declaration/context/aggregate/synthetic distinction;
- hazard vocabulary and version;
- confidence and uncertainty;
- cross-domain ownership;
- anti-collapse checks.

Failure: `HOLD_FOR_KNOWLEDGE_CHARACTER`.

### Gate 4 — time, validity, freshness, and expiry

Required:

- applicable time kinds;
- validity and expiry logic;
- stale tolerance;
- source/model cycle;
- supersession handling;
- current-use denial behavior.

Failure: `HOLD_FOR_TIME_SEMANTICS`, `HOLD_FOR_FRESHNESS`, or `HOLD_FOR_EXPIRY`.

### Gate 5 — evidence and proof closure

Required:

- resolvable `EvidenceRef -> EvidenceBundle`;
- claim-to-evidence mapping;
- digests;
- source-role proof;
- freshness/expiry proof;
- life-safety-boundary proof;
- official-referral proof where applicable;
- catalog closure.

Failure: `HOLD_FOR_EVIDENCE`.

### Gate 6 — rights, sensitivity, geometry, and public representation

Required:

- policy-allowed rights;
- sensitivity and cross-lane assessment;
- spatial support and uncertainty;
- public field allowlist;
- generalization/suppression posture;
- all-surface reconstruction review;
- no internal or restricted details.

Failure: `HOLD_FOR_RIGHTS`, `HOLD_FOR_GEOMETRY`, or `HOLD_FOR_SENSITIVITY`.

### Gate 7 — life-safety, regulatory, caveat, and official-referral boundary

Required:

- not-for-life-safety posture;
- no KFM warning/alert/evacuation/rescue authority;
- issuing authority preserved;
- official referral defined;
- regulatory limits visible;
- provisional, model, detection, and uncertainty caveats;
- urgent-use denial behavior.

Failure: `HOLD_FOR_OFFICIAL_REFERRAL`, `HOLD_FOR_LIFE_SAFETY_BOUNDARY`, or `HOLD_FOR_CAVEATS`.

### Gate 8 — deterministic validation and finite outcomes

Required:

- accepted contracts and schemas;
- deterministic no-network fixtures;
- positive and negative-path tests;
- source-role, time, expiry, disclaimer, public-membrane, correction, and rollback checks;
- finite validation results;
- validation report and receipts.

Failure: `HOLD_FOR_VALIDATION`.

### Gate 9 — policy and review

Required:

- accepted policy version/digest;
- finite `PolicyDecision`;
- hazards steward review;
- source/rights review;
- time/freshness review;
- sensitivity/infrastructure review where applicable;
- operational-context review where applicable;
- independent release review where required;
- unresolved conflicts recorded.

Failure: `HOLD_FOR_POLICY` or `HOLD_FOR_REVIEW`.

### Gate 10 — shared release handoff and reversibility

Required:

- accepted `PromotionDecision` path;
- `ReleaseManifest` content and digest closure;
- correction, withdrawal, and supersession paths;
- tested rollback target;
- derivative and cache invalidation;
- public notice behavior;
- governed carrier registration.

Failure: `HOLD_FOR_RELEASE_TOPOLOGY`, `HOLD_FOR_CORRECTION_PATH`, or `HOLD_FOR_ROLLBACK`.

### Gate result

```text
all applicable gates pass
  -> APPROVED_FOR_MANIFEST

any gate fails or cannot run
  -> explicit HOLD / BLOCKED / RESTRICTED_REVIEW / STALE / WITHDRAWN
```

This README cannot promote a candidate. It can only document readiness or blockers for handoff.

[Back to top](#top)

---

## Required dossier structure

The following is a **PROPOSED review structure**, not proof that these files or a canonical candidate schema exist.

```text
release/candidates/hazards/<candidate-id>/
├── README.md
├── candidate.summary.json
├── artifact.manifest.json
├── source.closure.json
├── evidence.closure.json
├── time.validity.json
├── public.representation.json
├── validation.summary.json
├── policy.summary.json
├── review.summary.json
├── correction.plan.json
└── rollback.plan.json
```

Before creating these paths, verify the accepted candidate contract, schema home, naming convention, and shared release topology. Avoid parallel authority.

### Public-safe dossier fields

A public or repository-visible child README should contain only safe summaries:

```markdown
# <candidate title>

## Status
<finite candidate state>

## Candidate identity
- Candidate ID:
- Version:
- Hazard family:
- Object/product families:
- Artifact kind:
- Immutable artifact ref:
- Artifact digest:
- Proposed audience and carrier:

## Scope and non-authority boundary
- Geography:
- Scale:
- Event/observation/model/forecast/context scope:
- Explicit exclusions:
- Not-for-life-safety statement:
- Regulatory/issuer limitations:

## Source and rights closure
- Admitted source refs:
- Source roles:
- Issuer/authority scope:
- Rights and terms:
- Source version/head:
- Retrieval/cadence state:

## Time, freshness, and expiry
- Event/observation time:
- Issue time:
- Valid interval:
- Expiry:
- Retrieval/processing:
- Stale-after:
- Supersession behavior:

## Evidence and proof
- Evidence refs:
- Validation refs:
- Freshness/expiry proof:
- Source-role proof:
- Life-safety-boundary proof:
- Official-referral proof:
- Catalog closure:

## Public-safe representation
- Geometry/CRS/scale:
- Field allowlist:
- Sensitivity and cross-lane posture:
- Reconstruction review:
- Caveats and uncertainty:

## Policy and review
- Policy decision:
- Required reviewers:
- Completed reviews:
- Holds and reason codes:

## Release handoff
- Proposed PromotionDecision:
- Proposed ReleaseManifest:
- Correction path:
- Withdrawal/supersession path:
- Rollback target:
- Derivative invalidation:

## Decision
<READY_FOR_REVIEW / HOLD / RESTRICTED_REVIEW / DEFERRED / WITHDRAWN>
```

Do not include restricted locations, facility vulnerabilities, credentials, privileged incident details, operational transform parameters, or unpublished emergency-management content.

[Back to top](#top)

---

## Validation, proof, fixture, schema, and policy posture

### Current bounded maturity

| Surface | Current evidence | Safe interpretation |
|---|---|---|
| Candidate lane | Parent README only | No active candidate established |
| Release index | Draft with proposed/illustrative rows | No live release established |
| Proof lane | README says implementation depth remains `UNKNOWN` | No accepted proof inventory or producer established |
| Policy lane | Greenfield scaffold | No executable Hazards policy enforcement established |
| Test parent | Detailed README | Documentation does not establish executable coverage |
| Direct test modules | Surfaced paths; sampled files are placeholder docstrings | No semantic pass rate or suite ownership established |
| Validator parent | README says it does not confirm executables | No accepted validator command established |
| Domain schemas | Concrete `PROPOSED` stubs exist | Shape scaffolding is not accepted semantic validation |
| Sample release-manifest schema | Field-incomplete, permissive, `additionalProperties: true` | Cannot establish candidate/release closure |
| Domain workflow | Readiness detectors and explicit holds | Maturity evidence only |
| Shared release dry run | Recent observed jobs are TODO-only | No candidate assembly, gate enforcement, or rollback proof |

### Required validation families

A future accepted suite should cover:

- candidate identity and digest closure;
- source admission, rights, issuer, and source-role preservation;
- event versus observation versus detection versus model versus forecast versus declaration;
- issue, valid, expiry, retrieval, release, and stale-state semantics;
- warning/advisory official-referral behavior;
- emergency-alert and life-safety denial behavior;
- regulatory-context limitations;
- geometry, scale, uncertainty, and public fields;
- infrastructure and cross-lane sensitivity;
- EvidenceRef-to-EvidenceBundle resolution;
- catalog closure;
- policy finite outcomes;
- public API/map/export/search/graph/Evidence Drawer/AI trust membrane;
- correction, withdrawal, supersession, and rollback;
- deterministic no-network execution;
- no sensitive fixture leakage;
- no current-condition overclaim.

### Minimum negative cases

- missing source role;
- unadmitted source;
- unclear rights;
- model represented as observation;
- forecast represented as current measurement;
- detection represented as confirmed perimeter;
- historical event represented as current condition;
- expired warning/advisory context;
- missing official issuer or referral;
- KFM-authored emergency instruction;
- regulatory context represented as KFM determination;
- missing EvidenceBundle;
- unresolved policy;
- sensitive infrastructure exposure;
- missing public field allowlist;
- stale dependency;
- missing correction or rollback target;
- candidate represented as released;
- withdrawn or rolled-back content remaining public.

### Validation result vocabulary

A validator should emit deterministic structured outcomes such as:

```text
PASS
FAIL
ABSTAIN
DENY
RESTRICT
ERROR
REVIEW_REQUIRED
STALE
EXPIRED
```

The accepted vocabulary and report schema remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Automation posture

### Current `domain-hazards` workflow

The inspected workflow:

- runs on pull requests, pushes to `main`, and manual dispatch;
- uses read-only contents permissions;
- checks required Hazards responsibility boundaries;
- scans direct tests for collected test functions/classes;
- scans selected validator roots for executable bodies;
- expects no accepted validation target;
- expects no non-README proof artifact or proof producer;
- expects no non-README candidate record or release-dry-run target;
- emits explicit readiness holds;
- performs no live source access, warning issuance, policy decision, promotion, deployment, or publication.

Safe interpretation:

- `validate-hazards` success would mean the expected no-executable hold posture was observed;
- `build-proof-hazards` success would mean no accepted proof producer was detected;
- `publish-dry-run-hazards` success would mean no accepted candidate/release command was detected;
- none of these results proves current conditions, accuracy, warning validity, regulatory status, evidence closure, release readiness, or life-safety authority.

### Graduation rule

Replace a readiness hold only when repository evidence establishes:

- an accepted command and owner;
- accepted contracts and schemas;
- deterministic synthetic fixtures;
- positive and negative tests;
- no-network default behavior;
- time/freshness/expiry enforcement;
- official-referral and life-safety denial enforcement;
- evidence and policy integration;
- sensitivity/no-leak review;
- receipt and proof destinations;
- release, correction, and rollback integration;
- documentation updated to reflect actual behavior.

Do not silence a detector merely to make CI green. Do not make placeholder files look executable. Do not convert a green hold into release proof.

### Shared `release-dry-run`

The inspected shared workflow is not established here as a substantive Hazards release mechanism. Recent observed runs used TODO echo steps for candidate assembly, promotion checking, and rollback-card presence.

A green TODO-only run does not prove:

- candidate assembly;
- promotion-gate enforcement;
- manifest validity;
- evidence closure;
- independent review;
- rollback readiness;
- public safety;
- release.

[Back to top](#top)

---

## Review and release handoff

### Required review roles

Assign actual people or accepted reviewer groups before approval:

| Review concern | Required capability |
|---|---|
| Hazards semantics | Hazard family, object, and limitation review |
| Source and issuer | Source identity, authority scope, cadence, and correction review |
| Rights | License, terms, attribution, redistribution, derivative rights |
| Time | Event/issue/valid/expiry/retrieval/stale-state review |
| Evidence | Claim-to-EvidenceBundle closure |
| Policy | Audience, not-for-life-safety, regulatory, sensitivity, and denial posture |
| Spatial | CRS, scale, uncertainty, geometry, topology, public representation |
| Cross-domain | Owning-domain truth and dependency review |
| Operational context | Warning/advisory interpretation and official-referral review |
| Validation | Deterministic suite and report review |
| Release | Promotion, manifest, correction, withdrawal, supersession, rollback |
| Public surfaces | Map/API/export/search/graph/drawer/AI no-leak and caveat review |

Placeholder owner names do not satisfy review.

### Separation of duties

For material or current-sensitive Hazards releases:

- candidate author should not be the sole approver;
- source admission should remain separate from release approval;
- policy authoring should remain separate from policy outcome evidence;
- validation producer should not silently waive its own failure;
- emergency or regulatory source expertise should be represented where applicable;
- release authority should verify correction and rollback support;
- public carrier activation should follow accepted release records.

### Handoff packet

`APPROVED_FOR_MANIFEST` should resolve:

- candidate ID and digest;
- object/product family;
- source descriptors and source roles;
- rights and issuer scope;
- time/freshness/expiry closure;
- evidence and proof refs;
- policy decision;
- review records;
- validation report;
- public representation;
- official referral and caveats;
- catalog closure;
- correction, withdrawal, supersession, and rollback;
- proposed public carriers and invalidation targets.

The shared release authority may still deny or hold promotion.

[Back to top](#top)

---

## Correction, withdrawal, supersession, and rollback

### Correction triggers

Initiate correction review when:

- event identity, geometry, magnitude, severity, time, issuer, or source role is wrong;
- a model/forecast/detection was mislabeled;
- a warning/advisory remained visible after expiry;
- official source correction or retraction occurs;
- evidence changes;
- a rights or policy error is discovered;
- sensitive or infrastructure detail leaked;
- a public caveat or referral was missing;
- a public carrier, search entry, graph edge, or AI summary diverged from release state;
- a dependency release was corrected;
- a public alias points to stale or superseded content.

### Withdrawal triggers

Withdraw when:

- rights no longer allow distribution;
- source or evidence is retracted;
- safety or sensitivity risk cannot be repaired promptly;
- current-sensitive content cannot be reliably expired;
- issuer/authority attribution is materially wrong;
- the candidate or release could cause life-safety misuse;
- required correction or rollback cannot close.

### Supersession

A successor must:

- identify the prior candidate/release;
- explain changed sources, methods, time, policy, fields, geometry, or caveats;
- preserve historical lineage;
- invalidate current pointers to the predecessor;
- avoid silently rewriting prior evidence;
- retain correction and rollback links.

### Rollback plan

Before promotion, identify:

- exact prior safe release or no-public-state target;
- manifest and artifact digests;
- alias changes;
- cache and CDN invalidation;
- map/tile source invalidation;
- API and export invalidation;
- search and graph invalidation;
- Evidence Drawer and report invalidation;
- AI/vector/index invalidation;
- public notice behavior;
- source/watcher state;
- validation of restored state;
- rollback receipt and responsible owner.

Rollback must not restore expired warning/advisory styling, stale current-condition claims, leaked sensitive detail, or a broken official-referral path.

### Documentation correction

When implementation or release evidence conflicts with this README:

1. preserve the stronger authority;
2. label the conflict;
3. update the evidence ledger;
4. correct this README through review;
5. record a receipt;
6. avoid rewriting historical receipts to make the earlier state appear correct.

[Back to top](#top)

---

## Public API, map, export, search, graph, and AI boundary

### Normal public path

```text
released public-safe Hazards artifact
  -> release and layer/dataset registry
  -> governed API or approved released-artifact resolver
  -> map / report / export / timeline / Evidence Drawer / AI surface
```

### Forbidden shortcuts

```text
live source feed -> public KFM alert
RAW / WORK / QUARANTINE -> public client
processed candidate -> public map
candidate README -> API authority
warning/advisory text -> KFM instruction
model output -> observed current condition
source official status -> KFM regulatory authority
catalog or graph -> sovereign truth
proof or receipt -> release approval
AI summary -> evidence
```

### Public carrier requirements

Every public carrier must preserve applicable:

- release ID and state;
- artifact digest;
- source and issuer;
- canonical source role;
- product character;
- event/issue/valid/expiry/retrieval/release times;
- freshness and stale state;
- uncertainty and provisional status;
- not-for-life-safety label;
- official-source referral;
- regulatory limitations;
- evidence references;
- policy outcome;
- correction, withdrawal, supersession, and rollback state.

### Map and tile behavior

Maps must not:

- use urgent visual styling for expired or historical context without explicit labeling;
- hide model/forecast/detection character;
- show candidate or withdrawn layers as active;
- imply safe passage, shelter, evacuation, or facility status;
- expose restricted infrastructure or sensitive cross-lane detail;
- treat a style filter as data security;
- retain stale cached tiles after correction or rollback.

### Search and graph behavior

Search indexes and graph projections are derived carriers. They must:

- preserve release and time state;
- not merge events, warnings, models, declarations, and observations into one undifferentiated object;
- remove or mark stale/withdrawn/rolled-back entries;
- preserve owning-domain references;
- not expose hidden fields through snippets or relationship traversal.

### AI behavior

AI may:

- summarize released evidence;
- explain limitations and uncertainty;
- compare released historical or planning context;
- draft review notes;
- abstain or deny with bounded reasons.

AI may not:

- issue alerts, warnings, evacuation, rescue, or medical instructions;
- infer current safety from stale, expired, candidate, or incomplete context;
- replace official sources;
- invent source, time, severity, geometry, or evidence;
- expose restricted infrastructure or sensitive details;
- turn model/detection/aggregate context into observation;
- treat the candidate index as proof.

EvidenceBundle and release state outrank generated language.

[Back to top](#top)

---

## Maintenance and definition of done

### Update this README when

- a candidate dossier is added, renamed, moved, corrected, superseded, or withdrawn;
- a child candidate family is accepted;
- candidate identity or schema contracts are accepted;
- source-role or product-character vocabulary changes;
- time/freshness/expiry requirements change;
- policy or life-safety boundary changes;
- executable validation or proof production is established;
- release topology changes;
- a correction or rollback exposes a documentation gap;
- workflow detector behavior changes;
- Directory Rules or an ADR changes placement.

### Definition of done for this parent lane

- bounded candidate inventory is reproducible;
- each indexed candidate has immutable identity and digest;
- no README is counted as a candidate;
- source admission, role, issuer, rights, and cadence resolve;
- event/observation/model/forecast/declaration distinctions are enforced;
- event/issue/valid/expiry/retrieval/release times are explicit;
- current-sensitive content fails closed when stale or expired;
- not-for-life-safety and official-referral behavior is enforced;
- evidence, proof, policy, validation, and review references resolve;
- spatial, sensitivity, and reconstruction review is complete;
- release, correction, withdrawal, supersession, and rollback topology is accepted;
- public carrier and invalidation behavior is tested;
- docs match implementation;
- generated indexes are derived and non-authoritative;
- human review is recorded.

### Parent-lane maintenance rule

Do not add placeholder candidate rows “for future use.” Use examples only when they are unmistakably labeled illustrative and cannot be mistaken for current release state.

[Back to top](#top)

---

## Evidence ledger

| Evidence inspected | Status | Supports | Limit |
|---|---|---|---|
| `release/candidates/hazards/README.md` prior blob `598728cb…` | **CONFIRMED** | Existing parent candidate guidance and workflow sentence | Did not establish an active candidate |
| Bounded search for `release/candidates/hazards/` | **CONFIRMED bounded result** | Parent README was the only directly indexed candidate-lane file | Search-limited; unindexed/restricted/runtime material remains unknown |
| `docs/doctrine/directory-rules.md` | **CONFIRMED** | `release/` owns release decisions; lifecycle roots remain separate | Does not prove candidate instances |
| `docs/domains/hazards/RELEASE_INDEX.md` | **CONFIRMED draft doc** | Life-safety boundary, candidate/release templates, proposed rows, no live release confirmed in its session | Illustrative rows are not release evidence |
| `docs/domains/hazards/LIFE_SAFETY_BOUNDARY.md` and publication docs referenced by workflow | **CONFIRMED path evidence** | Not-for-life-safety and official-authority boundary | Runtime enforcement remains to be proven |
| `data/proofs/hazards/README.md` | **CONFIRMED** | Proof responsibilities and explicit unknown implementation depth | Not a proof artifact or emitted inventory |
| `policy/domains/hazards/README.md` | **CONFIRMED scaffold** | Policy responsibility home | No executable policy enforcement |
| `tests/domains/hazards/README.md` | **CONFIRMED detailed test index** | Expected deterministic no-network trust families | Does not establish executable test coverage |
| Direct test paths surfaced by search | **CONFIRMED paths** | Test-file inventory signal | Exhaustive recursive inventory not proven |
| `test_emergency_alert_denial.py` | **CONFIRMED placeholder** | Direct sampled test is a `PROPOSED` docstring-only placeholder | Does not prove all test files are placeholders |
| `test_operational_expiry_freshness.py` | **CONFIRMED placeholder** | Direct sampled test is a `PROPOSED` docstring-only placeholder | Does not prove all test files are placeholders |
| `tools/validators/domains/hazards/README.md` | **CONFIRMED index** | Validator ownership and boundary guidance | Explicitly does not confirm executables |
| `schemas/contracts/v1/domains/hazards/release_manifest.schema.json` | **CONFIRMED `PROPOSED` stub** | Concrete schema path exists | Field-incomplete and permissive; not release closure |
| `data/published/hazards/README.md` | **CONFIRMED draft carrier guide** | Published-carrier and no-alert boundary | Does not establish emitted released artifacts |
| `.github/workflows/domain-hazards.yml` | **CONFIRMED workflow** | Readiness detectors, explicit holds, required workflow sentence | Not semantic validation, proof, or release |
| `.github/workflows/release-dry-run.yml` and recent job observations | **CONFIRMED TODO posture from recent runs** | Shared workflow exists | Green TODO steps are not release proof |
| `.github/CODEOWNERS` | **CONFIRMED repository routing surface** | Review routing may exist | Does not establish domain, safety, policy, or release approval |

### Bounded conclusion

**CONFIRMED:** this README can safely state that no directly indexed active Hazards candidate is established at the evidence snapshot.

**PROPOSED:** this lane should operate as the time-aware, not-for-life-safety candidate index and review contract described here.

**UNKNOWN / NEEDS VERIFICATION:** exhaustive candidate inventory, active contracts, admitted sources, executable policy, accepted tests/validators, proof production, current runtime behavior, branch-protection dependencies, independent reviewer assignment, and release execution.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive recursive inventory under `release/candidates/hazards/`.
- [ ] Confirm canonical candidate ID and directory naming.
- [ ] Confirm whether durable child candidate families are needed.
- [ ] Confirm candidate summary, artifact-manifest, and dossier contracts.
- [ ] Confirm accepted Hazards object and product-character vocabularies.
- [ ] Confirm canonical seven-role mapping for official, context, warning, forecast, and detection terminology.
- [ ] Confirm admitted source descriptors, issuer scope, rights, terms, cadence, and source-head records.
- [ ] Confirm event, issue, valid, expiry, retrieval, release, correction, and stale-state schemas.
- [ ] Confirm model-cycle, forecast-lead, update, and supersession behavior.
- [ ] Confirm official-source referral contract and current configuration ownership.
- [ ] Confirm not-for-life-safety policy and finite runtime outcomes.
- [ ] Confirm regulatory-context limitations and issuer attribution.
- [ ] Confirm concrete semantic contracts beyond README scaffolding.
- [ ] Confirm which `PROPOSED` schemas may graduate and remove permissive closure gaps.
- [ ] Confirm fixture payload inventory and golden negative cases.
- [ ] Confirm direct test inventory, collection behavior, ownership, and pass rate.
- [ ] Confirm accepted validator roots, commands, report schema, and receipt destinations.
- [ ] Confirm EvidenceRef-to-EvidenceBundle resolution and proof producer.
- [ ] Confirm freshness, expiry, stale, official-referral, and life-safety-boundary proofs.
- [ ] Confirm public field allowlists, geometry, uncertainty, and reconstruction review.
- [ ] Confirm infrastructure, private, cultural, archaeological, ecological, and sovereignty sensitivity rules.
- [ ] Confirm candidate-to-review-to-`PromotionDecision`-to-`ReleaseManifest` handoff.
- [ ] Confirm correction, withdrawal, supersession, rollback, and derivative invalidation.
- [ ] Confirm public map/API/export/search/graph/Evidence Drawer/AI consumption through governed routes only.
- [ ] Confirm cache, tile, alias, index, vector, and generated-summary invalidation.
- [ ] Confirm workflow maturity-detector behavior and remove false positives only through separate evidence-backed changes.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewers.
- [ ] Confirm generated candidate indexes never become sovereign truth.
- [ ] Confirm human review of this v2 revision.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced generic Hazards candidate guidance with a repository-grounded, time-aware, not-for-life-safety candidate index and pre-publication review contract.
- Recorded the README-only bounded candidate inventory and no-active-candidate posture.
- Preserved the exact candidate-not-release sentence and `publication-not_yet`.
- Added candidate families and routing, finite states and holds, admission requirements, object/product/source-role anti-collapse, official-referral and life-safety boundaries, time/freshness/expiry discipline, spatial and sensitivity controls, ten release gates, a public-safe dossier template, validation and automation posture, review handoff, correction and rollback discipline, public-client boundaries, evidence ledger, definition of done, and open verification.
- Added `CONTRACT_VERSION = "3.0.0"` and commit-pinned evidence metadata.

### v1 — prior state

- Draft candidate-lane README replacing a greenfield stub.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
598728cb3e8ea49ca87e12e1320b83ebb73b7536
```

Then verify:

- the prior README is restored;
- no candidate record, release record, or published artifact was changed;
- generated receipt history remains auditable;
- public documentation does not retain incompatible references.

No Hazards event, observation, detection, model, forecast, warning/advisory context, declaration, source, evidence, policy decision, candidate, release manifest, public artifact, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
