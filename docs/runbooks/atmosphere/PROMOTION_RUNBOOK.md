<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/atmosphere/promotion
title: Atmosphere Promotion Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v2.0.0
prior_version: v1
status: draft; repository-grounded; bounded-promotion-readiness-validator-present; no-atmosphere-candidate; source-authority-empty; atmosphere-policy-inactive; evidence-proof-release-hold; non-publisher; not-for-life-safety
owners:
  - "@bartytime4life — verified GitHub review route only"
  - "NEEDS VERIFICATION — accountable Atmosphere, source, scientific, rights, sensitivity, evidence, policy, validation, review, promotion, release, correction, rollback, operations, public-surface, and independent-review assignments"
created: 2026-05-13
updated: 2026-08-25
policy_label: restricted-review; atmosphere; promotion-readiness; fail-closed; no-release-authority; no-publication-authority; not-for-life-safety
current_path: docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Provide the repository-grounded human procedure for evaluating one
  specifically identified Atmosphere candidate for bounded final promotion
  readiness and preparing an accountable review handoff without admitting a
  source, authenticating evidence, activating policy, applying a lifecycle
  transition, releasing, deploying, or publishing.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path update; no new or parallel authority
path_posture: PLACE
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  initial_base_commit: df6c3f5dadd2800fdc2356ceb540ca4e448f6c7a
  reconciled_base_commit: 218363515d5f477cb4005491e22945130b84eebc
  target_prior_blob: c19719a1014db3b1217c8d2fad1d4315a3bb0d99
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  atmosphere_runbook_index_blob: ed9d6588dbd7400ac78eb65a897b008399d4307e
  atmosphere_release_rollback_runbook_blob: 9054c5a584f06f065b94960491de28a0c6941217
  atmosphere_candidate_readme_blob: 2cff863a65c035cc167583ecae481c03580fc24a
  atmosphere_workflow_blob: fccba4b6e2cdae561ec8a4904446ed5dbe6ec8ce
  promotion_gate_readme_blob: e729df0cc007e8cf0d9811afc25ec1f5ffbdffdd
  promotion_policy_readme_blob: 79287df1d828010d716ed43d2e24d6dbd610305b
  atmosphere_policy_readme_blob: a300dfd5abda1b58a07fd978935dd40ef232ec71
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  atmosphere_proof_readme_blob: c85bea4e5524b934eef66fa7d8bc65f7036d0726
  atmosphere_published_readme_blob: 25f26ea54c3c298175c510191427e5cef8eaa4cd
  atmosphere_review_readme_blob: 4e2a478e5ef2c631cee48a0b44254d5383055c57
  promotion_decision_contract_blob: 42295bfc83a621cf125d33aa821912b426f70bd2
  promotion_receipt_contract_blob: ed432f8e3e02d170589c9e04d78087a69346909d
  atmosphere_release_runbook_blob: 5d730d218094fb9fc7f89ddc20480b3ad63783e6
inspection_boundary: >-
  Current-session GitHub reads of the exact target, accepted Directory Rules
  decision, Atmosphere runbook index, domain workflow, candidate, source,
  proof, policy, review, published-carrier, promotion-gate, decision, receipt,
  release, correction, and rollback boundaries. Repository-native commands
  were not executed in a mounted checkout during authoring. No live source,
  protected payload, current-condition endpoint, credential, policy evaluator,
  evidence resolver, reviewer authority service, release service, deployed
  consumer, or public surface was exercised. No candidate, decision, receipt,
  manifest, lifecycle transition, release, deployment, promotion, correction,
  rollback, alert, medical determination, regulatory determination, or
  publication was created or performed. Main advanced after initial authoring
  through the current-session checkpoint. This reconciliation reverified the
  pinned authority and object-family surfaces, preserved intervening main
  ancestry, and refreshed the Atmosphere index and combined release/rollback
  evidence bindings without expanding the two-file pull-request scope.
related:
  - ../README.md
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./VALIDATION_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./STALE_STATE_RUNBOOK.md
  - ./CORRECTION_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ./RELEASE_RUNBOOK.md
  - ../../adr/ADR-0018-promotion-gate-sequence.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../domains/atmosphere/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/atmosphere/README.md
  - ../../../data/proofs/atmosphere/README.md
  - ../../../data/published/atmosphere/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/promotion_receipt.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/release/rollback_card.md
  - ../../../schemas/contracts/v1/release/promotion_decision.schema.json
  - ../../../schemas/contracts/v1/release/promotion_receipt.schema.json
  - ../../../policy/promotion/README.md
  - ../../../policy/domains/atmosphere/README.md
  - ../../../release/candidates/atmosphere/README.md
  - ../../../release/promotion_decisions/README.md
  - ../../../release/reviews/atmosphere/README.md
  - ../../../release/manifests/README.md
  - ../../../release/rollback_cards/rel-atmosphere-pm25-2026-001.card.json
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../tools/validators/release/validate_promotion_receipt.py
  - ../../../tests/release/test_promotion_gate.py
  - ../../../tests/release/test_promotion_receipt.py
  - ../../../.github/workflows/promotion-gate.yml
  - ../../../.github/workflows/promotion-receipt.yml
  - ../../../.github/workflows/domain-atmosphere.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, atmosphere, air, runbook, promotion, readiness, source-role, knowledge-character, time, freshness, evidence, policy, review, rollback, fail-closed, no-network, not-for-life-safety]
notes:
  - "v2.0.0 replaces proposal-era no-mounted-repository assumptions, guessed paths, speculative commands, lifecycle-wide A-G claims, and implied release machinery with current repository evidence and bounded procedures."
  - "The shared A-G validator is executable, deterministic, no-network, read-only, and non-publishing. PASS means APPROVE_READY for accountable review only."
  - "The current Atmosphere candidate lane has no verified child candidate dossier; the source-authority projection is empty; Atmosphere and promotion policy sources are inactive; and no accepted Atmosphere proof packet, review, PromotionDecision, ReleaseManifest, applied transition, or released carrier was established."
  - "The proposed ADR-0018 sequence is not accepted, and repository documentation still contains materially different A-G vocabularies. This runbook uses the implemented bounded validator names only when describing that validator."
  - "KFM Atmosphere is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority."
  - "The combined Atmosphere release/rollback procedure is now substantive coordination-only guidance; it does not change the operational promotion hold or supersede the separate release and rollback procedures."
  - "This document changes no source, candidate, data, contract, schema, policy, fixture, validator, workflow, evidence object, receipt, proof, review, release record, deployment, lifecycle state, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Promotion Runbook

> **Evaluate whether one specifically identified Atmosphere candidate has enough declared, public-safe support to be handed to accountable promotion review. Never translate documentation, a synthetic fixture pass, a green workflow, a schema-valid object, or an `APPROVE_READY` result into promotion, release, deployment, or publication.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![A–G readiness validator: present](https://img.shields.io/badge/A--G%20validator-present-1f883d?style=flat-square)](#current-executable-validation)
[![Atmosphere candidate: absent](https://img.shields.io/badge/Atmosphere%20candidate-NOT__ESTABLISHED-b42318?style=flat-square)](#current-repository-posture)
[![Promotion policy: inactive](https://img.shields.io/badge/promotion%20policy-inactive-d4a72c?style=flat-square)](#current-repository-posture)
[![Operational promotion: hold](https://img.shields.io/badge/operational%20promotion-HOLD-b42318?style=flat-square)](#finite-outcomes-and-current-holds)
[![Life safety: not an authority](https://img.shields.io/badge/life%20safety-not%20an%20authority-b42318?style=flat-square)](#atmosphere-specific-gates)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary-and-handoff)

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move, commit, pull request, merge, workflow result, badge, fixture, candidate folder, decision-shaped file, receipt, manifest, deployment, alias update, map-layer toggle, or generated summary.** The current procedure stops at a reviewable readiness or hold packet.

> [!CAUTION]
> **Current Atmosphere promotion is `HOLD`.** The repository has a bounded generic A–G readiness validator and several deterministic Atmosphere fixture profiles, but the Atmosphere candidate lane has no verified child dossier; the central source-authority projection is empty; Atmosphere and promotion policy sources are inactive; and no accepted Atmosphere proof packet, accountable review, promotion decision, release manifest, applied transition, or released carrier was established by the bounded inspection.

> [!WARNING]
> **KFM Atmosphere is not an official AQI, medical, regulatory, emergency-alerting, or life-safety authority.** Do not use this runbook to declare current conditions safe or unsafe, issue health advice, certify a sensor or concentration, replace an agency advisory, or originate operational instructions. Advisory context must preserve the official issuer and route life-safety interpretation to the Hazards lane and the issuing authority.

**Quick navigation:** [Purpose](#purpose-and-terminal-boundary) · [Posture](#current-repository-posture) · [Placement](#directory-rules-basis) · [Scope](#scope-and-non-goals) · [Roles](#roles-and-separation-of-duties) · [Boundaries](#lifecycle-and-object-family-boundaries) · [Preflight](#preflight-and-mandatory-stop-conditions) · [Procedure](#promotion-readiness-procedure) · [Atmosphere gates](#atmosphere-specific-gates) · [A–G profile](#implemented-a-g-readiness-profile) · [Validation](#current-executable-validation) · [Packet](#candidate-review-packet) · [Outcomes](#finite-outcomes-and-current-holds) · [Authority](#authority-boundary-and-handoff) · [Recovery](#correction-withdrawal-and-rollback) · [Audit](#audit-and-join-keys) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback) · [Checklist](#appendix-a-operator-checklist) · [Commands](#appendix-b-current-command-and-surface-matrix)

---

<a id="purpose-and-terminal-boundary"></a>

## Purpose and terminal boundary

Use this runbook only when an identifiable Atmosphere candidate is claimed to be at `CATALOG` or `TRIPLET` and someone is asking whether it is ready for a separately governed transition toward `PUBLISHED`.

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This procedure evaluates the **final promotion-readiness boundary**. It does not govern source admission, RAW capture, normalization, quarantine exit, processed-object validation, catalog creation, or triplet generation as though they were the same operation. Those upstream transitions keep their own contracts, policy, validation, receipts, evidence, review, and correction requirements.

The operator's responsibilities are to:

1. freeze the exact repository revision, candidate identity, requested lifecycle boundary, audience, spatial scope, temporal scope, and affected carriers;
2. verify that the candidate exists and is not merely a README, roadmap item, proof placeholder, test fixture, generated example, or stale index row;
3. preserve source role, knowledge character, units, averaging window, time, freshness, rights, sensitivity, evidence, policy, review, correction, and rollback distinctions;
4. run only the repository-owned checks that apply to the declared packet;
5. interpret each result within its actual fixture, shape, or readiness boundary;
6. prepare a public-safe handoff for accountable review; and
7. stop before any lifecycle mutation, release, deployment, alias change, cache invalidation, public read-back, or publication.

### Permitted terminal dispositions

This runbook may end with:

- `NO_ACTIVE_CANDIDATE_VERIFIED`;
- `READY_FOR_ACCOUNTABLE_REVIEW`;
- `HOLD_FOR_<DEPENDENCY>`;
- `ABSTAIN`;
- `DENY`; or
- `ERROR`.

It may not end with `PROMOTED`, `RELEASED`, `DEPLOYED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The following conclusions are bounded to reconciled `main@218363515d5f477cb4005491e22945130b84eebc`.

| Surface | Status | Safe conclusion |
|---|---|---|
| This runbook path | **CONFIRMED** | `docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md` is tracked. This revision is a same-path documentation modernization. |
| Directory governance | **CONFIRMED / accepted** | ADR-0029 adopts Directory Rules v2; `docs/runbooks/` owns human operational procedures. |
| Prior runbook | **CONFIRMED / proposal-era** | The v1 document mixed lifecycle-wide gates, guessed paths, proposed reason codes, speculative signing commands, and unverified release behavior. It was not current implementation proof. |
| Atmosphere candidate lane | **CONFIRMED guidance / no child candidate** | `release/candidates/atmosphere/` contains the parent README and no verified child candidate dossier. “A candidate is not a release.” |
| Central source authority | **CONFIRMED / empty projection** | `control_plane/source_authority_register.yaml` is `PROPOSED`, `projection_only`, `implementation_status: ABSENT`, and has `entries: []`. It admits and activates no source. |
| Atmosphere source registry | **CONFIRMED guidance / descriptors unestablished** | The lane documents routing, rights, sensitivity, role, cadence, time, and stale-state requirements; concrete admitted descriptors were not established by the bounded inspection. |
| Atmosphere domain validation | **CONFIRMED / bounded synthetic profiles** | The domain workflow executes several no-network fixture profiles and explicitly retains broader evidence, proof, policy, and release holds. |
| Generic promotion readiness | **CONFIRMED / bounded executable** | The shared validator checks a declared `CATALOG`/`TRIPLET` to `PUBLISHED` packet through A–G gates without network access or writes. |
| Generic readiness result | **CONFIRMED / non-authoritative** | `PASS` maps to `APPROVE_READY` for accountable review only. It is not `APPROVE`, an applied transition, release, deployment, or publication. |
| Promotion gate sequence | **CONFLICTED / proposed** | ADR-0018 remains proposed, and lifecycle-wide guidance, older runbooks, and the bounded validator use materially different A–G names or responsibilities. |
| Promotion policy | **CONFIRMED / inactive** | `policy/promotion/` contains two no-op proposed Rego stubs and no accepted bundle, evaluator, selector, required-check binding, or governed consumer. |
| Atmosphere policy | **CONFIRMED / inactive and conflicted** | Thirteen default-only Rego scaffolds have mixed packages and result relations; no accepted bundle, evaluator, native Rego suite, or runtime binding was established. |
| `PromotionDecision` family | **CONFIRMED / proposed contract and shape** | The release contract and paired schema define `APPROVE`, `DENY`, or `ABSTAIN`; no Atmosphere instance or authenticated decision was established. |
| `PromotionReceipt` family | **CONFIRMED / proposed fixture-first** | Contract, schema, validator, fixtures, tests, and read-only workflow exist. Internal consistency does not prove that a transition occurred. |
| Atmosphere proof support | **CONFIRMED draft / release hold** | The parent proof lane and a PM2.5 child README exist, but no accepted Atmosphere proof packet, resolver binding, domain-wide proof validator, or release linkage was established. |
| Atmosphere review lane | **CONFIRMED draft guidance** | A review README exists; an accountable, subject-bound Atmosphere review record and verified reviewer authority were not established. |
| Atmosphere release readiness | **CONFIRMED fixture-first / operational hold** | The release runbook documents no active candidate, no Atmosphere ReleaseManifest, no accepted release evaluator, no authenticated release authority, and no public write. |
| Published Atmosphere carriers | **CONFIRMED directory guidance / payload unverified** | `data/published/atmosphere/README.md` exists, but no released payload or public carrier was established by the bounded inspection. |
| Rollback support | **CONFIRMED bounded candidate/rehearsal surfaces** | Shared `RollbackCard` checks and synthetic rehearsal exist; operational Atmosphere rollback remains held. |
| Release/rollback coordination | **CONFIRMED substantive coordination / operational hold** | The combined procedure binds release-readiness and rollback-assurance handoffs without superseding the separate procedures or authorizing action. |
| Functional stewards | **NEEDS VERIFICATION** | `@bartytime4life` is a verified GitHub review route. CODEOWNERS routing does not establish scientific, source, evidence, policy, release, or independent-review authority. |
| Deployment and public state | **UNKNOWN** | No deployed endpoint, cache topology, alias state, public read-back, monitoring, or operational SLO evidence was inspected. |

### What this posture means

The repository has useful **readiness mechanics**, not an operational Atmosphere promotion path. The strongest truthful current action is to validate declared synthetic or candidate packets, expose missing support, and prepare a review handoff. Missing authority cannot be manufactured through a complete checklist.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This file is a human operational procedure at an already tracked path:

```text
docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
```

The placement outcome is `PLACE`: update the existing file in place under the `docs/` responsibility root. Do not create a second Atmosphere promotion authority under `release/`, `data/`, `policy/`, `pipelines/`, `schemas/`, or `contracts/`.

| Responsibility | Owning surface | Relationship to this runbook |
|---|---|---|
| Human Atmosphere promotion-readiness procedure | `docs/runbooks/atmosphere/` | **Owned here** |
| Domain explanation and language | `docs/domains/atmosphere/` | Referenced; not redefined |
| Source identity and admission | `data/registry/sources/atmosphere/` and accepted source-authority objects | Required input; not owned here |
| Contract meaning | `contracts/` | Referenced; not redefined |
| Machine shape | `schemas/` | Referenced; validation is not approval |
| Admissibility rules | `policy/` | Separate; currently inactive for the relevant promotion path |
| Reusable synthetic inputs | `fixtures/` | Test material only |
| Executable validation | `tools/validators/`, `tests/`, workflows | Bounded behavior only |
| Evidence and proof | `data/proofs/` | Separate from validation and release decisions |
| Candidate, review, decision, manifest, correction, and rollback records | `release/` | Separate object families and authority |
| Public-safe carriers | `data/published/` and governed delivery surfaces | Downstream; not mutated here |

A new path, moved authority, or parallel object-family home would require a separately justified Directory Rules decision and, where necessary, an ADR or migration note. This update creates neither.

[Back to top](#top)

---

<a id="scope-and-non-goals"></a>

## Scope and non-goals

### In scope

- One specifically identified Atmosphere candidate already declared at `CATALOG` or `TRIPLET`.
- Exact candidate identity, artifact digests, lifecycle boundary, public audience, geography, and time scope.
- Source-role and knowledge-character preservation.
- Pollutant, variable, units, averaging window, method, uncertainty, QA, and caveat checks.
- Observation, model-run, forecast, issue, valid, retrieval, correction, expiry, and freshness distinctions.
- Rights, attribution, sensitivity, harmful precision, and public-surface obligations.
- EvidenceRef, EvidenceBundle, proof, attestation, catalog, validation, policy-context, review, correction, and rollback pointers.
- The current deterministic A–G readiness validator and its finite outcomes.
- Current Atmosphere fixture profiles as bounded domain evidence.
- Public-safe review handoff and named holds.

### Out of scope

This runbook does not:

- discover, admit, activate, fetch, scrape, or refresh a source;
- contact EPA, KDHE, NOAA/NWS, Kansas Mesonet, AirNow, AQS, community-sensor, satellite, forecast, model, or other live services;
- decide that an observation, forecast, model field, AQI report, AOD product, smoke context, climate product, or advisory is true;
- certify sensor equivalence, calibration fitness, regulatory status, health impact, or current conditions;
- create a candidate when the candidate lane is empty;
- resolve an EvidenceRef or manufacture an EvidenceBundle;
- activate the current Rego scaffolds or substitute declared policy context for executed policy;
- authenticate a reviewer, steward, signer, or authority assignment;
- emit an operational `PromotionDecision`, `PromotionReceipt`, `ReleaseManifest`, `CorrectionNotice`, or `RollbackCard`;
- apply a lifecycle transition or write to `data/published/`;
- mutate an alias, CDN, cache, search index, vector index, graph projection, tile service, API route, map layer, dashboard, export, or AI cache;
- release, deploy, promote, publish, correct, withdraw, or roll back; or
- issue medical, regulatory, emergency, or life-safety guidance.

### Subject exclusions

Do not use this procedure on:

- a synthetic fixture while describing it as a live candidate;
- a source descriptor while describing it as evidence or release state;
- a proof-lane README while describing it as a proof packet;
- a candidate README while describing it as an active candidate;
- a path under `data/published/` while describing path presence as publication;
- a map, tile, graph, screenshot, dashboard, or AI answer while describing it as root truth; or
- an emergency alert or official advisory whose issuance and operational interpretation belong elsewhere.

[Back to top](#top)

---

<a id="roles-and-separation-of-duties"></a>

## Roles and separation of duties

Only `@bartytime4life` was verified as a GitHub review route in the bounded repository evidence. The functional roles below remain **NEEDS VERIFICATION** until a governed authority record establishes actor identity, scope, effective interval, independence, revocation, and accountability.

| Role | Required responsibility | Must not be inferred from |
|---|---|---|
| Atmosphere domain steward | Knowledge character, source-role boundaries, scientific scope, units, averaging window, uncertainty, and caveats | A username, CODEOWNERS route, README owner list, or passing test |
| Source steward | SourceDescriptor identity, admission state, role, rights, cadence, freshness, and correction path | Public endpoint availability or a connector directory |
| Rights and sensitivity steward | Redistribution, attribution, consent, public audience, precision, and restricted joins | A public URL or permissive-looking metadata |
| Evidence steward | EvidenceRef resolution, EvidenceBundle scope, proof limitations, citation closure, and conflict handling | Presence of a proof folder or reference string |
| Validation steward | Exact profile, fixture polarity, deterministic execution, result integrity, and limitation statement | A green workflow outside the declared profile |
| Policy steward | Accepted policy source, bundle, selector, evaluator, outcome mapping, obligations, and correction/rollback | Current default-only Rego scaffolds |
| Accountable reviewer | Subject-bound review, authority interval, scope, obligations, independence, expiry, and supersession | Review-request assignment or PR approval alone |
| Promotion authority | `PromotionDecision` accountability for the exact candidate and boundary | A readiness `PASS`, receipt, manifest, merge, or deployment |
| Release steward | ReleaseManifest, signatures/attestations, public transition, correction, withdrawal, and release history | A PromotionDecision alone |
| Rollback/correction steward | Safe target, affected consumers, invalidation, restoration, read-back, and audit | A rollback-card-shaped fixture |
| Operations/public-surface steward | Deployment, aliases, caches, APIs, maps, monitoring, and public read-back | Repository paths or documentation |
| AI assistant | May summarize released evidence and draft bounded handoff prose | Never truth, policy, review, promotion, release, or publication authority |

### Separation requirements

For a policy-significant or public-facing candidate:

1. candidate author and accountable reviewer must be different actors;
2. source admission, evidence assessment, policy evaluation, promotion decision, and release application must remain distinguishable;
3. a reviewer must have verified subject and scope authority at the relevant times;
4. unresolved obligations, expired authority, self-review, or superseded review blocks readiness;
5. GitHub routing, branch ownership, and repository administration do not substitute for domain or release authority; and
6. AI-generated language may assist drafting but cannot approve or complete a gate.

When required actors are not verifiable, return `HOLD_FOR_REVIEW_AUTHORITY` or `ABSTAIN`; do not invent names or roles.

[Back to top](#top)

---

<a id="lifecycle-and-object-family-boundaries"></a>

## Lifecycle and object-family boundaries

### Final-readiness boundary

The implemented shared validator accepts only a declared final boundary:

```text
CATALOG or TRIPLET -> PUBLISHED
```

It does not prove the earlier lifecycle stages. An upstream object cannot skip admission, normalization, validation, catalog, proof, or review because the final-readiness packet is internally consistent.

### Object-family separation

| Object or surface | What it records | What it does not prove or authorize |
|---|---|---|
| `SourceDescriptor` | Source identity, role, rights, cadence, sensitivity, and admission context | Evidence truth, candidate readiness, or public use |
| `RunReceipt` | What a process declared it ran and emitted | Scientific truth, proof closure, policy approval, or release |
| `ValidationReport` | Findings within a named validation profile | Evidence authenticity, reviewer authority, or promotion |
| `EvidenceRef` | Pointer to governed support | Resolution or sufficiency by itself |
| `EvidenceBundle` | Resolved evidence scope, citations, limitations, and support | Policy permission, review, release, or public serving by itself |
| Catalog/STAC/DCAT/PROV record | Discovery, lineage, assets, and metadata | Release authority or claim truth |
| Readiness result | Bounded A–G validator outcome | `PromotionDecision` or transition application |
| `ReviewRecord` | Subject-bound accountable review | Policy, promotion, or release by itself |
| `PromotionDecision` | Accountable `APPROVE`, `DENY`, or `ABSTAIN` decision for a governed boundary | ReleaseManifest, deployment, publication, or public permission by itself |
| `PromotionReceipt` | Declared inputs, gate outcomes, integrity binding, decision pointer, and transition claim for one attempt | Authenticity of support or proof that a transition occurred |
| `ReleaseManifest` | Released artifact inventory, identities, digests, and release linkage | Evidence truth or policy authority by itself |
| `RollbackCard` | Prior target, affected scope, restoration intent, and rollback support | Executable or successful rollback without drill and read-back |
| `CorrectionNotice` / withdrawal record | Supersession, correction, invalidation, and affected scope | Automatic propagation or restored public state |
| `data/published/` carrier | Downstream released public-safe bytes when governed records close | Publication merely because the file path exists |
| Governed API / map / Evidence Drawer / Focus Mode | Released presentation and finite consumer outcomes | Canonical truth, source authority, or release authority |

### Readiness, decision, transition, release, and publication are separate

A safe sequence is:

```text
candidate packet
  -> bounded readiness validation
  -> candidate ReleaseManifest preparation and immutable binding
  -> accountable review
  -> PromotionDecision
  -> authorized transition execution and PromotionReceipt
  -> release authorization / application
  -> deployed public-safe carrier
  -> public read-back and monitoring
```

Each arrow is independently governed. A later step must not be inferred from an earlier artifact.

[Back to top](#top)

---

<a id="preflight-and-mandatory-stop-conditions"></a>

## Preflight and mandatory stop conditions

### Authority freeze

Before running a check, record:

- exact repository commit;
- candidate path and immutable candidate ID;
- current and requested lifecycle states;
- candidate author;
- artifact set and digests;
- pollutant or variable;
- source role and knowledge character;
- spatial scope and precision;
- temporal scope and freshness basis;
- target audience and public-use claim;
- applicable contract/schema/profile versions;
- evidence, policy, review, correction, and rollback references;
- affected carriers and consumers; and
- the explicit non-goals of the run.

Do not proceed from a branch name, latest-file assumption, mutable URL, unpinned generated output, or copied example.

### Candidate existence check

The candidate must be a readable child dossier under the accepted candidate lane or another accepted candidate home. A parent README, empty directory, proof README, release index, fixture, test case, or historical example is not a candidate.

Current bounded evidence shows **no verified child Atmosphere candidate dossier**. Unless newer pinned evidence establishes one, stop with:

```text
NO_ACTIVE_CANDIDATE_VERIFIED
```

### Required support before readiness evaluation

A real candidate packet must at minimum declare:

- stable candidate ID, author, profile, and specification hash;
- exact `CATALOG` or `TRIPLET` current state and `PUBLISHED` target;
- immutable artifact digests and manifest identity;
- source descriptors and immutable source roles;
- knowledge-character labels;
- geometry/CRS and public precision posture;
- complete material time fields and freshness evaluation;
- rights, sensitivity, audience, and policy-context declarations;
- EvidenceRefs and resolvable EvidenceBundle/proof references;
- catalog and attestation references;
- validation profile and exact results;
- subject-bound review and authority references;
- correction lineage; and
- a successor rollback target, or explicit first-release withdrawal/hold assurance, with scope.

The shared validator can inspect declared fields, but it does not authenticate them.

### Mandatory stop conditions

Stop and emit a named hold, abstention, denial, or error when any of these applies:

- no active candidate exists;
- source admission or source role is unknown;
- the central or domain source authority required by the candidate cannot be resolved;
- AQI, concentration, AOD, PM2.5, model, forecast, observation, advisory, regulatory, aggregate, or synthetic roles would collapse;
- units, averaging windows, methods, QA, uncertainty, or caveats are missing or contradictory;
- observation, model-run, issue, valid, retrieval, correction, expiry, or freshness semantics are missing or stale;
- rights, attribution, license/terms, sensitivity, consent, audience, or precision are unknown;
- evidence references do not resolve or proof scope is insufficient;
- the policy source, bundle, selector, evaluator, or outcome cannot be verified;
- reviewer identity, authority, scope, separation, expiry, or obligations cannot be verified;
- correction lineage is missing; a successor lacks a rollback target; or a first-release candidate lacks withdrawal/hold assurance;
- the packet requests live source access, credentials, protected data, current-condition advice, or public writes;
- an exact-location, infrastructure, private-network, or re-identifying join exceeds the public need;
- a required path or command does not match the pinned repository;
- the requested outcome depends on a proposed ADR as though accepted;
- an overlapping active change owns the same candidate or release surface; or
- a result would be reported as release, deployment, promotion, publication, or life-safety guidance.

[Back to top](#top)

---

<a id="promotion-readiness-procedure"></a>

## Promotion-readiness procedure

### Step 1 — Pin the subject and requested boundary

Record the exact commit and candidate packet. Confirm that the requested transition is:

```text
CATALOG -> PUBLISHED
```

or:

```text
TRIPLET -> PUBLISHED
```

Any other lifecycle transition is outside the current shared A–G profile. Route it to the owning upstream procedure rather than renaming it “promotion.”

**Output:** frozen subject record or `ERROR` with reason code `UNSUPPORTED_BOUNDARY`.

### Step 2 — Verify candidate inventory and identity

Inspect the accepted Atmosphere candidate lane and candidate dossier.

Confirm:

- the child dossier exists;
- its ID is stable and unique;
- the packet identifies the author and exact artifact set;
- the dossier is not merely a README template or fixture;
- its declared state is not already withdrawn, superseded, expired, or corrected without re-review; and
- every path is within the accepted responsibility boundary.

At the pinned evidence snapshot, no child candidate exists. The current truthful result is `NO_ACTIVE_CANDIDATE_VERIFIED`.

**Output:** candidate identity record or named hold.

### Step 3 — Resolve source, role, and knowledge character

For each input and consequential claim:

1. resolve the source descriptor and admission posture;
2. preserve the immutable source role;
3. identify knowledge character;
4. verify pollutant/variable, method, units, and averaging window;
5. preserve QA, provisional/final, calibration, correction, uncertainty, and caveats;
6. verify official issuer and advisory role where applicable; and
7. prevent downcasting or cross-role substitution.

Do not infer an admitted source from a connector, registry README, external URL, or source-family name.

**Output:** role/character matrix or `HOLD_FOR_SOURCE_ADMISSION`, `HOLD_FOR_SOURCE_ROLE`, or `DENY`.

### Step 4 — Verify spatial, temporal, freshness, rights, and sensitivity scope

Confirm:

- geometry is valid under the applicable profile;
- CRS and bbox declarations are deterministic and consistent;
- public precision is justified;
- station/network coordinates and joins do not expose harmful detail;
- observed, model-run, forecast, issue, valid, retrieval, correction, expiry, and release times remain distinct;
- freshness is evaluated for the requested audience and use;
- rights, redistribution, attribution, and terms are current;
- sensitivity and public audience are explicitly evaluated; and
- official context has not been transformed into KFM-issued advice.

**Output:** scope matrix or a named hold/denial.

### Step 5 — Verify evidence, proof, catalog, and validation support

For each consequential claim or carrier:

- resolve EvidenceRef to EvidenceBundle;
- verify claim, spatial, temporal, source-role, method, and limitation scope;
- verify proof/citation and conflict handling;
- bind validation results to the exact candidate and profile;
- verify catalog/STAC/DCAT/PROV references as required;
- verify attestation and process-receipt declarations;
- preserve unresolved support as `ABSTAIN`; and
- reject reference presence as a substitute for authenticity.

Current repository evidence does not establish an accepted Atmosphere proof packet or release linkage.

**Output:** support-closure matrix or `HOLD_FOR_EVIDENCE`, `ABSTAIN`, `DENY`, or `ERROR`.

### Step 6 — Run Atmosphere-specific bounded validation

Follow [`VALIDATION_RUNBOOK.md`](VALIDATION_RUNBOOK.md) for the exact no-network profiles affected by the candidate.

Relevant current bounded families include:

- public-safe precipitation;
- knowledge character;
- low-cost-sensor caveat and calibration;
- observed-versus-modeled separation;
- AirNow-to-AQS reconciliation;
- prescribed-burn quality flags;
- PM2.5 trigger candidate assessment;
- PM sensor trust and colocation profiles;
- correctable environmental-event assessment; and
- cross-domain environmental-observation boundaries.

A profile may prove fixture polarity, shape, or a declared semantic invariant. It cannot establish source truth, proof closure, policy activation, release readiness, or public safety.

**Output:** exact profile results and limitations.

### Step 7 — Run the shared bounded A–G readiness check

Use the current repository command only on:

- the checked-in synthetic fixture matrix; or
- an explicit candidate JSON packet that genuinely conforms to the implemented input profile.

Do not fabricate a candidate packet to obtain `PASS`.

For a first release with no legitimate predecessor, the current Gate G profile
cannot represent withdrawal-only recovery: it requires a rollback card and a
`target_spec_hash` distinct from the candidate hash. Do not invent a target.
Record the bounded A–G readiness check as `NOT_RUN` and return
`HOLD_FOR_FIRST_RELEASE_RECOVERY_PROFILE` until an accepted withdrawal-only
profile exists.

The validator:

- performs no network access;
- writes no artifact;
- checks declared references rather than dereferencing them;
- does not execute the promotion Rego stubs;
- does not authenticate actors or assignments;
- does not verify DSSE/cosign or transparency logs;
- does not resolve EvidenceBundles; and
- does not inspect a public surface.

**Output:** deterministic `PASS`, `ABSTAIN`, `DENY`, or `ERROR` result with `APPROVE_READY` or `BLOCKED` readiness.

### Step 8 — Reconcile policy and review authority

A declared Gate E or Gate G value is not an operational policy decision or authenticated review.

Before a real candidate can advance beyond readiness:

- accepted policy source, bundle, selector, evaluator, entrypoint, outcome mapping, and obligations must be verified;
- accountable reviewer identity and authority must be verified;
- subject, scope, time, separation, expiry, supersession, and obligations must close; and
- review must be preserved as a separate record.

Current Atmosphere and promotion policy sources are inactive. Functional authority assignments remain unverified.

**Output:** `HOLD_FOR_POLICY`, `HOLD_FOR_REVIEW_AUTHORITY`, `ABSTAIN`, or a review-ready support statement.

### Step 9 — Prepare the candidate review packet

Prepare a public-safe packet using [Candidate review packet](#candidate-review-packet).

Do not include:

- credentials, tokens, private tickets, signing keys, internal hostnames, or restricted operational details;
- raw or reconstructable sensitive coordinates;
- private-network or facility joins;
- proprietary calibration internals;
- protected source payloads;
- current-condition health or safety interpretation; or
- unbounded generated prose.

**Output:** immutable review handoff or a safe hold report.

### Step 10 — Stop at the authority boundary

Only when every preceding source, evidence, policy, authority, sensitivity,
correction, rollback, and profile check has closed without a retained hold,
abstention, denial, error, or `NOT_RUN` result does readiness `PASS` yield:

```text
READY_FOR_ACCOUNTABLE_REVIEW
```

This is the runbook handoff label for the validator's equal readiness value:

```text
APPROVE_READY
```

A declaration-only validator `PASS` must not overwrite an earlier substantive
hold. Neither readiness label yields `APPROVE`.

The next steps—candidate `ReleaseManifest` preparation and binding, accountable review, `PromotionDecision`, authorized transition application and `PromotionReceipt`, release authorization/application, deployment, publication, and public read-back—belong to separate authorities and procedures.

[Back to top](#top)

---

<a id="atmosphere-specific-gates"></a>

## Atmosphere-specific gates

The implemented A–G profile is generic. Atmosphere readiness must overlay the following domain constraints without inventing a second machine gate sequence.

| Constraint | Required posture | Fail-closed result |
|---|---|---|
| AQI is not concentration | Preserve AQI/report character, concentration units, breakpoint/method, averaging window, and official context separately. | `DENY` when AQI is substituted for measured concentration. |
| AOD is not PM2.5 | Preserve column optical property, algorithm, resolution, QA, cloud/surface limitations, model/fusion method, and uncertainty. | `DENY` when AOD is presented as surface PM2.5 without governed derivation and labeling. |
| Model fields are not observations | Preserve model, run, forecast hour, inputs, version, skill/validation, uncertainty, and reality boundary. | `DENY` when modeled or forecast values are presented as observed sensor truth. |
| Low-cost sensors require caveats | Preserve sensor type, calibration/correction profile, QA, confidence, limitations, owner/terms, and public-use limits. | `DENY` or `HOLD` when caveat/correction support is missing. |
| Regulatory/archive is not real-time public reporting | Preserve archive, certification, provisional/final, revision, and currentness posture. | `HOLD` or `DENY` when archival or provisional status is misrepresented. |
| Advisory context is not KFM-issued instruction | Preserve official issuer, issue/valid/expiry time, source link, and referral-only posture. | `DENY` when KFM originates or rewrites life-safety instructions as its authority. |
| Observed, modeled, aggregate, regulatory, contextual, candidate, synthetic, and restricted roles remain distinct | Carry source role through evidence, catalog, map, export, graph, and AI surfaces. | `DENY` on role downcasting or substitution. |
| Pollutant, variable, units, method, and averaging window are load-bearing | Bind them to the candidate, evidence, validation, and carrier. | `DENY` or `ABSTAIN` when they are missing, incompatible, or ambiguous. |
| Time and freshness are claim-specific | Preserve observation, model-run, issue, valid, retrieval, correction, expiry, release, and stale state. | `HOLD`, `ABSTAIN`, or `DENY` when stale or temporally ambiguous. |
| Station and network precision is audience-aware | Expose only the precision needed for the released claim; review sensitive joins. | `HOLD_FOR_SENSITIVITY` or `DENY` when precision or joins create harm. |
| Cross-domain impacts retain owner authority | Atmosphere may provide forcing or context; Hazards, Hydrology, Agriculture, Habitat, Fauna, Flora, Roads, and Settlements retain their canonical claims. | `ABSTAIN` or route to the owning lane. |
| AI is interpretive | AI may summarize released EvidenceBundles under policy and citation checks. | `ABSTAIN`, `DENY`, or `ERROR` when support, policy, or citation closure fails. |

### Public-surface minimums

A proposed public Atmosphere carrier must keep visible, as applicable:

- source and source role;
- knowledge character;
- pollutant/variable and units;
- averaging window and method;
- observation/model-run/issue/valid/retrieval/release time;
- freshness or stale state;
- QA, provisional/final, calibration/correction, uncertainty, and caveats;
- official issuer or authority limitation;
- EvidenceBundle and correction references;
- review/release state; and
- rollback or supersession posture.

A style filter, hidden property, rounded coordinate, or client-side badge is not a substitute for upstream public-safe transformation and release control.

[Back to top](#top)

---

<a id="implemented-a-g-readiness-profile"></a>

## Implemented A–G readiness profile

The table below describes the **current bounded validator**, not an accepted whole-lifecycle promotion doctrine.

| Gate | Implemented name | Declared check | Atmosphere application |
|:---:|---|---|---|
| A | `identity_and_closure` | Profile, candidate, author, specification hash, lifecycle boundary, and minimal manifest identity | Candidate ID, exact `CATALOG`/`TRIPLET` source state, Atmosphere scope, and declared manifest closure |
| B | `asset_integrity` | Candidate, manifest, and receipt hash agreement; non-empty unique digest-set equality | Public-safe carrier set, derived products, reports, tiles, and supporting artifacts bind to one candidate |
| C | `geometry_and_crs` | Declared validity, deterministic processing, CRS, and finite ordered bbox | Point/network/grid/region geometry, generalization, station precision, and representation scope |
| D | `temporal_semantics` | Strict UTC-second instants, ordered interval, and declared evaluation time | Observation, model-run, valid, issue, retrieval, correction, expiry, and freshness posture |
| E | `rights_and_sensitivity` | Known profile/labels, public-safe label discipline, and finite declared policy outcome | Rights, attribution, source terms, audience, sensitivity, harmful precision, and official-authority limitations |
| F | `proof_and_catalog_support` | Evidence, attestation, run receipt, catalog, and conditional AI support declarations | EvidenceBundle/proof scope, citations, STAC/DCAT/PROV closure, limitations, and AI mediation where applicable |
| G | `review_and_rollback` | Fixture-only review shape, identity/authority declarations, separation, obligations, scope/hash binding, correction, and rollback | Accountable Atmosphere review, correction lineage, prior target, and public-surface recovery scope |

### Finite results

| Status | Validator meaning | Exit | This runbook's safe interpretation |
|---|---|---:|---|
| `PASS` | Every bounded declaration passed; readiness is `APPROVE_READY` | `0` | Ready for accountable review only |
| `ABSTAIN` | Support is insufficient without a contradictory unsafe claim | `1` | Preserve prior state and resolve support |
| `DENY` | A mandatory, unsafe, or contradictory condition blocks readiness | `1` | Preserve prior state and record safe reason |
| `ERROR` | Input or declared policy evaluation could not be completed safely | `2` | Preserve prior state; repair evaluation context |

Precedence is:

```text
ERROR > DENY > ABSTAIN > PASS
```

### Known conflict

ADR-0018 remains proposed. Older lifecycle and publication documents use other A–G names and scopes. This runbook does not accept ADR-0018, rename those other profiles, or claim convergence. It uses the names above only because they match the current executable and `PromotionReceipt` fixture profile.

Any proposal to make this sequence authoritative must separately reconcile:

- lifecycle-wide versus final-readiness scope;
- policy evaluation and runtime parity;
- decision and receipt semantics;
- review authority;
- evidence and attestation resolution;
- rollback execution;
- release application; and
- required-check/public-consumer integration.

[Back to top](#top)

---

<a id="current-executable-validation"></a>

## Current executable validation

### Shared promotion readiness

| Surface | Current status | What it proves |
|---|---|---|
| `tools/validators/validate_promotion_gate.py` | **CONFIRMED executable** | Deterministic declared-packet A–G findings; no network, writes, or transition |
| `tools/validators/validate_review_record.py` | **CONFIRMED fixture-only** | Shape and internal identity/authority/time/scope/hash declarations; no live authentication |
| `fixtures/release/promotion_gate/` | **CONFIRMED synthetic matrix** | One PASS, twelve DENY, three ABSTAIN, and two ERROR cases |
| `tests/release/test_promotion_gate.py` | **CONFIRMED focused tests** | Outcomes, precedence, parser, CLI, determinism, no-emission, and no-network behavior |
| `.github/workflows/promotion-gate.yml` | **CONFIRMED orchestration** | Bounded fixture-only check; governed-record and promoter integration remain held |
| `make publish-check` | **CONFIRMED repository target** | Fixture matrix and focused standard-library suite |

### PromotionReceipt validation

| Surface | Current status | Boundary |
|---|---|---|
| `contracts/release/promotion_receipt.md` | **PROPOSED** | Meaning for one declared promotion-attempt receipt |
| paired schema/validator/fixtures/tests | **CONFIRMED fixture-first** | Shape, finite-outcome consistency, transition declarations, and digest integrity |
| `.github/workflows/promotion-receipt.yml` | **CONFIRMED read-only workflow family** | Fixture validation only; no operational receipt or transition |

A schema-valid receipt with `transition.applied: true` is still a declaration. The validator does not authenticate support or prove that the transition occurred.

### Atmosphere domain validation

The `domain-atmosphere` workflow is read-only and runs bounded synthetic profiles with no-network guards. It explicitly records that broader Atmosphere semantics, evidence closure, proof, and release remain unestablished.

Use [`VALIDATION_RUNBOOK.md`](VALIDATION_RUNBOOK.md) for exact profile commands, inputs, expected rejection behavior, and current placeholder inventory. Do not convert a specialty-profile success into domain-wide promotion readiness.

### Release dry run

The shared release dry run is synthetic and no-public-write. It exercises denial/readiness and rollback-card candidate behavior but does not create an Atmosphere candidate, evaluate the inactive Atmosphere policy source, assemble an operational manifest, authenticate release authority, or mutate public state.

### Current-session validation limit

Repository-native commands were **not run in a mounted checkout during this documentation update**. The commands below are repository evidence, not current-session execution claims. Hosted exact-head results for the eventual pull-request head must be reported separately from authoring checks, review, merge, release, deployment, promotion, and publication.

[Back to top](#top)

---

<a id="candidate-review-packet"></a>

## Candidate review packet

A review handoff should be immutable, public-safe, and bounded to one candidate.

### Required fields

| Field | Requirement |
|---|---|
| Repository checkpoint | Exact commit and branch/base relationship |
| Candidate identity | Stable candidate ID, author, dossier path, current state, requested state |
| Scope | Pollutant/variable, source role, knowledge character, geography, time, audience, artifact family |
| Artifact inventory | Immutable paths/URIs and SHA-256 digests |
| Source support | SourceDescriptor refs, admission posture, rights, cadence, correction/supersession |
| Domain semantics | Units, averaging window, method, QA, uncertainty, caveats, official-authority posture |
| Time/freshness | Observation, model-run, issue, valid, retrieval, correction, expiry, evaluation, and stale-state result |
| Rights/sensitivity | Rights, attribution, terms, audience, sensitivity, precision, transforms, obligations |
| Evidence/proof | EvidenceRefs, EvidenceBundles, proof limitations, conflicts, catalog/attestation refs |
| Validation | Exact profiles, revisions, commands/workflows, outcomes, expected rejection, limitations |
| Readiness | A–G result, finite status, readiness, and public-safe findings |
| Policy | Exact accepted bundle/evaluator result—or explicit hold because current policy is inactive |
| Review authority | Reviewer/assignment refs, scope, time interval, independence, obligations, supersession |
| Correction/rollback | Correction lineage, affected consumers, prior target, drill/read-back posture |
| Open holds | Named unresolved dependencies and owning authority |
| Terminal statement | Explicitly state that no transition, release, deployment, promotion, or publication occurred |

### Minimal handoff template

```markdown
# Atmosphere promotion-readiness handoff

## Subject
- Repository commit: <sha>
- Candidate ID: <stable-id>
- Candidate path: <accepted candidate path>
- Current state: CATALOG | TRIPLET
- Requested state: PUBLISHED
- Candidate author: <actor ref>

## Scope
- Pollutant or variable: <value>
- Source role: <value>
- Knowledge character: <value>
- Units and averaging window: <value>
- Spatial scope and precision: <value>
- Temporal scope and freshness: <value>
- Audience and intended carrier: <value>

## Governed support
- SourceDescriptor refs: <refs or unresolved>
- EvidenceBundle refs: <refs or unresolved>
- Validation refs: <refs>
- Policy bundle/evaluation: <ref or HOLD>
- Review/authority refs: <refs or HOLD>
- Correction lineage: <refs or unresolved>
- Rollback target: <ref or unresolved>

## Results
- Atmosphere profile outcomes: <finite results>
- A–G status: PASS | ABSTAIN | DENY | ERROR | NOT_RUN
- Readiness: APPROVE_READY | BLOCKED | NOT_EVALUATED
- Introduced failures: <list or none established>
- Inherited failures: <list or none established>
- Pending checks: <list>

## Terminal disposition
READY_FOR_ACCOUNTABLE_REVIEW | HOLD_FOR_<DEPENDENCY> |
NO_ACTIVE_CANDIDATE_VERIFIED | ABSTAIN | DENY | ERROR

No lifecycle transition, release, deployment, promotion, or publication occurred.
```

### Redaction and disclosure

The packet may reveal safe reason codes and missing-object families. It must not reveal:

- credentials or signing material;
- private authority-system details;
- restricted source terms;
- exact harmful locations or private-network joins;
- proprietary calibration internals;
- confidential reviewer or ticket content;
- protected source payloads; or
- operational attack surface.

[Back to top](#top)

---

<a id="finite-outcomes-and-current-holds"></a>

## Finite outcomes and current holds

### Runbook outcomes

| Outcome | Use when | Next accountable step |
|---|---|---|
| `NO_ACTIVE_CANDIDATE_VERIFIED` | No readable child candidate dossier exists | Create or authorize candidate work separately; do not fabricate one here |
| `READY_FOR_ACCOUNTABLE_REVIEW` | Bounded checks and support declarations are complete enough for review | Hand off; do not apply transition |
| `HOLD_FOR_<DEPENDENCY>` | A named support or authority gap blocks safe evaluation | Route to the owning responsibility |
| `ABSTAIN` | Evidence or context is insufficient without a contradictory unsafe claim | Narrow scope or resolve support |
| `DENY` | A mandatory, unsafe, or contradictory condition blocks readiness | Preserve prior state and record safe reason |
| `ERROR` | The packet or evaluator context cannot be processed safely | Repair input/tooling; preserve prior state |

### Current Atmosphere holds

At the evidence snapshot, the following remain load-bearing:

- `HOLD_FOR_CANDIDATE` — no verified child candidate dossier;
- `HOLD_FOR_SOURCE_ADMISSION` — central source-authority projection is empty and concrete admitted Atmosphere descriptors were not established;
- `HOLD_FOR_EVIDENCE` — no accepted Atmosphere proof packet/resolver/release linkage was established;
- `HOLD_FOR_POLICY` — Atmosphere and promotion policy source is inactive and unbound;
- `HOLD_FOR_REVIEW_AUTHORITY` — accountable roles, authority intervals, and independence are unverified;
- `HOLD_FOR_PROMOTION_DECISION` — no authenticated Atmosphere `PromotionDecision` instance was established;
- `HOLD_FOR_TRANSITION_EXECUTION` — no accepted Atmosphere promotion executor or applied transition proof was established;
- `HOLD_FOR_RELEASE_MANIFEST` — no Atmosphere ReleaseManifest was established;
- `HOLD_FOR_PUBLIC_READ_BACK` — deployed carriers, aliases, caches, endpoints, monitoring, and public state remain unknown; and
- `HOLD_FOR_OPERATIONAL_ROLLBACK` — bounded card validation/rehearsal does not establish operational rollback; and
- `HOLD_FOR_FIRST_RELEASE_RECOVERY_PROFILE` — a future first release with no predecessor cannot use the current Gate G rollback shape without inventing a target.

### Current default result

Unless newer pinned evidence changes the candidate inventory, the correct disposition is:

```text
NO_ACTIVE_CANDIDATE_VERIFIED
```

No synthetic packet should be promoted to “active candidate” to bypass this result.

[Back to top](#top)

---

<a id="authority-boundary-and-handoff"></a>

## Authority boundary and handoff

This runbook ends before authority-bearing state change.

### What may be handed off

- exact candidate identity and frozen scope;
- immutable artifact digests;
- source-role and knowledge-character matrix;
- time/freshness and public-safety matrix;
- EvidenceRef/EvidenceBundle/proof/catalog status;
- exact validation and A–G outcomes;
- policy and reviewer-authority holds;
- correction and rollback status;
- affected consumer inventory;
- public-safe findings and limitations; and
- the smallest named next dependency.

### What the receiving authority must still establish

A separately governed process must establish, as applicable:

1. admitted and current source authority;
2. authentic, sufficient EvidenceBundle support;
3. correction and rollback readiness;
4. candidate `ReleaseManifest` and signer/attestation custody;
5. accepted and executed policy;
6. accountable independent review;
7. `PromotionDecision`;
8. authorized transition execution and authoritative receipt;
9. release authorization/application;
10. deployment and public-safe carrier activation;
11. cache/index/alias propagation;
12. public read-back and monitoring; and
13. correction, withdrawal, or rollback triggers.

### No implied transitions

The following are not interchangeable:

```text
profile validation PASS
!= readiness PASS = APPROVE_READY
!= review approval
!= PromotionDecision APPROVE
!= transition applied
!= release authorized
!= deployed
!= published
```

No reviewer, tool, workflow, assistant, or document may collapse these states through wording.

[Back to top](#top)

---

<a id="correction-withdrawal-and-rollback"></a>

## Correction, withdrawal, and rollback

Promotion readiness must be reversible before any public transition is considered.
A successor candidate requires a verified prior target. A first-release candidate
has no legitimate predecessor; while Gate G requires one, record readiness as
`NOT_RUN` and retain `HOLD_FOR_FIRST_RELEASE_RECOVERY_PROFILE` unless an
accepted withdrawal-only recovery profile closes that gap.

### Before handoff

Confirm that the packet identifies:

- the prior release or explicit no-prior-release state;
- the exact affected candidate and artifacts;
- correction and supersession lineage;
- affected APIs, layers, tiles, reports, indexes, graphs, AI caches, exports, and downstream derivatives;
- invalidation and restoration scope;
- public stale/withdrawn state;
- verification and read-back requirements; and
- the accountable rollback/correction authority.

### When a defect is found before transition

- preserve the current candidate and findings;
- return the defect to its owning source, work, quarantine, processed, catalog, proof, policy, or review lane;
- record `REPAIR_REQUIRED`, `HOLD`, `ABSTAIN`, `DENY`, or `ERROR`;
- do not create a release correction for a release that never occurred; and
- re-run readiness only after the owning support changes.

### When a defect is found after public release

Use the separate [`CORRECTION_RUNBOOK.md`](CORRECTION_RUNBOOK.md), [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md), [`STALE_STATE_RUNBOOK.md`](STALE_STATE_RUNBOOK.md), and release procedures. Preserve:

- original release records;
- correction or withdrawal notice;
- superseding evidence and release lineage;
- invalidation and cache propagation;
- affected-consumer accounting;
- public stale/withdrawn markers;
- rollback target verification; and
- post-action read-back.

This runbook does not execute those actions.

### Rollback-card caution

A shape-valid or synthetic `RollbackCard` is not an operational rollback. Operational trust requires a safe target, executable procedure, affected-consumer inventory, invalidation/restoration behavior, accountable authority, drill evidence, and public read-back.

[Back to top](#top)

---

<a id="audit-and-join-keys"></a>

## Audit and join keys

A reviewable promotion packet should preserve deterministic joins where practical.

| Join key | Binds |
|---|---|
| repository commit | Documentation, code, contracts, schemas, policy, fixtures, tests, workflows, and candidate evidence snapshot |
| candidate ID | Dossier, artifacts, validation, review, decision, receipt, manifest, correction, and rollback |
| specification hash | Candidate semantics and exact profile |
| artifact digests | Candidate, manifest, run receipt, receipt, and released carriers |
| source ID / descriptor version | Candidate claims to admitted source identity and role |
| EvidenceRef / EvidenceBundle ID | Claim and carrier to resolved support |
| validation profile/result ID | Candidate to exact validator scope and findings |
| policy bundle/evaluation ID | Candidate to exact policy source and evaluator context |
| review ID / assignment ID | Subject to accountable reviewer authority and time |
| PromotionDecision ID | Candidate and review to transition decision |
| PromotionReceipt ID | Attempt, A–G outcomes, integrity, decision, and declared transition |
| ReleaseManifest ID | Release artifact inventory and rollback/correction linkage |
| correction/withdrawal ID | Prior and superseding public state |
| RollbackCard ID | Failed release, prior target, affected scope, and recovery |
| public carrier/release ID | Deployed map/API/report/tile/index bytes to release records |

Do not use mutable “current,” “latest,” branch names, display labels, filenames alone, map layer names, or generated prose as the only join.

### Audit minimum

Record:

- who ran or reviewed each step;
- when, under which effective authority interval;
- exact inputs, outputs, versions, digests, and finite outcomes;
- which checks were run, not run, pending, introduced, inherited, or expected;
- which obligations remain;
- why scope was narrowed, held, denied, or abstained;
- which public surfaces would be affected; and
- the rollback/correction target.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| Item | Current status | Evidence required before relying on it |
|---|---|---|
| Active Atmosphere candidate | `ABSENT / HOLD` | Verified child dossier with stable identity, immutable artifact set, and explicit non-release state |
| Source admission and authority | `ABSENT / HOLD` | Accepted SourceDescriptor instances, authority registry entries, rights/sensitivity review, and activation state |
| Atmosphere proof closure | `UNKNOWN / HOLD` | Accepted proof profile, emitted EvidenceBundle/proof packet, resolver, validator, and candidate/release binding |
| A–G authority | `CONFLICTED / proposed` | Accepted decision reconciling lifecycle-wide and final-readiness vocabularies and compatibility obligations |
| Promotion policy | `INACTIVE / HOLD` | Accepted rules, input/outcome contract, native tests, immutable bundle, selector, evaluator, governed consumer, and correction/rollback |
| Atmosphere policy | `INACTIVE / CONFLICTED` | Consolidated packages/entrypoints, operative rules, tests, bundle, evaluator, consumer, and domain steward approval |
| Reviewer and promotion authority | `NEEDS VERIFICATION` | Authenticated identities, assignments, scope, intervals, separation, obligations, expiry, revocation, and independent capacity |
| Atmosphere `PromotionDecision` | `NOT ESTABLISHED` | Subject-bound reviewed instance validated under accepted profile and authority |
| Operational `PromotionReceipt` | `NOT ESTABLISHED` | Authoritative emitter, reference authentication, transition executor, integrity, and durable storage |
| Atmosphere ReleaseManifest | `NOT ESTABLISHED` | Candidate-bound manifest, artifact inventory, support, signatures/attestations, correction, and rollback |
| Published carrier inventory | `UNKNOWN` | Pinned emitted artifacts, release IDs, governed endpoints, aliases, caches, indexes, maps, exports, and public read-back |
| Operational rollback | `HOLD` | Accepted card/profile, safe target, executor, drill, invalidation/restoration, public read-back, and accountable authority |
| Required-check significance | `NEEDS VERIFICATION` | Exact-head hosted results plus repository ruleset/branch-protection evidence |
| Live-source and current-condition behavior | `HOLD / UNKNOWN` | Separate source admission, connector, operational validation, monitoring, and official-authority evidence |
| Atmosphere/Hazards seam | `NEEDS VERIFICATION` | Accepted cross-domain policy, issuer redirection, consumer behavior, and negative tests |
| Air/Atmosphere namespace drift | `CONFLICTED` | Accepted ADR or migration record and consumer closure |
| Complete consumer inventory | `UNKNOWN` | Governed API, UI, map, Evidence Drawer, Focus Mode, export, graph, search, cache, tile, and downstream derivative inventory |

Unknowns narrow scope and block higher-risk transitions. They do not invite plausible defaults.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

This revision is grounded in current repository files, not in the proposal-era runbook's assumptions.

| Evidence class | Inspected surface | Supported conclusion |
|---|---|---|
| Placement authority | ADR-0029 and Directory Rules v2 | Same-path `PLACE` under `docs/runbooks/atmosphere/` |
| Runbook maturity | Atmosphere runbook README and current child procedures | Promotion was the remaining substantive proposal-era procedure |
| Candidate inventory | `release/candidates/atmosphere/README.md` | No verified child candidate dossier |
| Source authority | central register and Atmosphere source README | Empty projection; routing guidance does not admit sources |
| Domain validation | `domain-atmosphere` workflow and validation runbook | Multiple bounded no-network profiles; broader proof/release hold |
| Promotion readiness | validator README, fixtures, tests, workflow | Executable deterministic A–G declared-packet checks |
| Policy | promotion and Atmosphere policy READMEs | Current Rego sources are proposed, inactive, unbound, and no-op/default-only |
| Evidence/proof | Atmosphere proof README | Proof lane exists; accepted packet/resolver/release binding unestablished |
| Review | Atmosphere review README | Guidance exists; accountable review and authority unestablished |
| Decision/receipt | PromotionDecision and PromotionReceipt contracts | Proposed separate object families; no Atmosphere operational instance |
| Release/public state | Atmosphere release runbook and published README | No active candidate, manifest, public write, or released carrier established |
| Recovery | correction, rollback, and combined release/rollback runbooks | Bounded preparation, rehearsal, and coordination exist; operational mutation remains held |

### Evidence limit

A Git commit proves bytes existed at a revision. It does not prove runtime behavior, source authority, scientific validity, policy enforcement, review authority, transition application, release, deployment, publication, or public read-back. Current hosted checks for this change must be assessed at the exact pull-request head and reported separately.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This is a documentation-only modernization.

### Before merge

Close or abandon the draft pull request and delete only its scoped branch if the change should not proceed.

### After merge

Revert the documentation commit through a reviewed pull request or submit a smaller forward correction. The prior target blob is:

```text
c19719a1014db3b1217c8d2fad1d4315a3bb0d99
```

Restoring that blob would restore the proposal-era v1 document. It would not undo or change source admission, evidence, policy, candidate, review, lifecycle, release, deployment, promotion, rollback, or publication state because this revision changes none of those surfaces.

### Maintenance triggers

Re-review this runbook when:

- a child Atmosphere candidate appears;
- source authority or admitted descriptors change;
- the A–G sequence is accepted or materially revised;
- promotion or Atmosphere policy becomes operative;
- an Atmosphere proof packet/resolver is established;
- reviewer or promotion authority is assigned;
- an Atmosphere PromotionDecision, receipt, manifest, or public carrier is emitted;
- correction/rollback topology changes;
- the Atmosphere/Hazards seam changes;
- public consumers or cache/index topology change; or
- repository commands, workflows, paths, or object profiles drift.

[Back to top](#top)

---

<a id="appendix-a-operator-checklist"></a>

## Appendix A — Operator checklist

### Freeze

- [ ] Exact repository commit recorded.
- [ ] Candidate child dossier verified.
- [ ] Candidate ID, author, state, target, audience, geography, time, and artifacts pinned.
- [ ] No overlapping active change owns the same candidate or release surface.

### Source and domain meaning

- [ ] SourceDescriptor refs resolve under accepted authority.
- [ ] Source roles remain immutable and explicit.
- [ ] Knowledge character is explicit.
- [ ] Pollutant/variable, units, method, and averaging window are explicit.
- [ ] AQI, concentration, AOD, PM2.5, model, observation, advisory, regulatory, aggregate, and synthetic roles do not collapse.
- [ ] QA, provisional/final, calibration/correction, uncertainty, and caveats are explicit.

### Space, time, rights, and sensitivity

- [ ] Geometry/CRS and public precision are justified.
- [ ] Sensitive joins and harmful precision fail closed.
- [ ] Observation, model-run, issue, valid, retrieval, correction, expiry, and evaluation times are distinct.
- [ ] Freshness is evaluated for the intended use.
- [ ] Rights, attribution, terms, audience, and sensitivity are current.
- [ ] Advisory context preserves official issuer and referral-only posture.

### Evidence, validation, policy, and review

- [ ] EvidenceRefs resolve to claim-scoped EvidenceBundles.
- [ ] Proof limitations and conflicts are visible.
- [ ] Catalog and attestation references are present where required.
- [ ] Exact Atmosphere profiles ran with positive/negative polarity.
- [ ] A–G result is recorded within its bounded meaning.
- [ ] Accepted policy bundle/evaluator exists—or `HOLD_FOR_POLICY` is recorded.
- [ ] Reviewer identity, authority, scope, separation, interval, obligations, expiry, and supersession are verified—or held.

### Recovery and handoff

- [ ] Correction lineage is present.
- [ ] Rollback target and affected consumers are identified.
- [ ] No secret, restricted payload, or harmful precision enters the packet.
- [ ] Introduced, inherited, expected, pending, and not-run checks are distinguished.
- [ ] Terminal outcome is finite and truthful.
- [ ] Handoff explicitly says no transition, release, deployment, promotion, or publication occurred.

[Back to top](#top)

---

<a id="appendix-b-current-command-and-surface-matrix"></a>

## Appendix B — Current command and surface matrix

Run these only from a trusted checkout pinned to the intended revision. They are read-only fixture/readiness checks, not promotion commands.

### Shared promotion readiness

```bash
make publish-check
```

```bash
python tools/validators/validate_promotion_gate.py --fixtures
python tools/validators/validate_review_record.py --fixtures
```

For a real, accepted explicit packet:

```bash
python tools/validators/validate_promotion_gate.py path/to/candidate.json
```

Do not create an ad hoc packet merely to force a pass.

### PromotionReceipt fixture profile

```bash
python tools/validators/release/validate_promotion_receipt.py --fixtures
python -m unittest -q tests.release.test_promotion_receipt
```

### Atmosphere domain profiles

Use the exact commands and expected-rejection rules in:

```text
docs/runbooks/atmosphere/VALIDATION_RUNBOOK.md
```

The primary hosted orchestration surface is:

```text
.github/workflows/domain-atmosphere.yml
```

Specialty profiles retain their dedicated workflows and declared fixture boundaries.

### Release and rollback readiness

Use:

```text
docs/runbooks/atmosphere/RELEASE_RUNBOOK.md
docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md
```

The shared workflow surfaces are:

```text
.github/workflows/release-dry-run.yml
.github/workflows/release-manifest.yml
```

They do not release, deploy, promote, or publish.

### Result interpretation

| Command/profile result | Safe statement |
|---|---|
| Atmosphere fixture pass | The named synthetic profile executed and its declared conditions passed |
| Promotion-gate `PASS` | The declared packet is `APPROVE_READY` for accountable review only |
| PromotionReceipt fixture pass | The fixture is internally consistent under the proposed receipt profile |
| Green hosted workflow | The exact workflow/job passed at that exact head within its declared scope |
| Any of the above | **Not** source truth, evidence proof, policy activation, review authority, transition application, release, deployment, promotion, or publication |

[Back to top](#top)

---

**Last updated:** 2026-08-25 · **Version:** v2.0.0 · **Terminal boundary:** accountable review handoff only · [Back to top](#top)
