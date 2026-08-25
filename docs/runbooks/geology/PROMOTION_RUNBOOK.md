<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/geology/promotion
title: Geology Promotion Runbook
type: runbook; operational-procedure; domain-lane; non-authoritative
version: v2.0.0
prior_version: v1
status: draft; repository-grounded; bounded-promotion-readiness-validator-present; no-geology-candidate; source-authority-empty; geology-policy-inactive; geology-proof-empty; operational-promotion-hold; non-publisher; not-scientific-regulatory-resource-or-engineering-authority
owners:
  - "@bartytime4life — verified GitHub CODEOWNERS review route only"
  - "NEEDS VERIFICATION — accountable Geology, source, scientific, rights, sensitivity, evidence, policy, validation, review, promotion, release, correction, rollback, operations, public-surface, and independent-review assignments"
created: NEEDS VERIFICATION — prior v1 did not record a reliable creation date
updated: 2026-08-25
policy_label: restricted-review; geology; natural-resources; promotion-readiness; fail-closed; source-role-aware; claim-class-aware; exact-subsurface-deny-by-default; no-release-authority; no-publication-authority
current_path: docs/runbooks/geology/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: >-
  Provide the repository-grounded human procedure for evaluating one
  specifically identified Geology and Natural Resources candidate for bounded
  final promotion readiness and preparing an accountable review handoff without
  admitting a source, authenticating evidence, activating policy, applying a
  lifecycle transition, releasing, deploying, or publishing.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path update; no new or parallel authority
path_posture: PLACE
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 889c3c609b4c3a1a79012cb6a00b0c0a5f00e87b
  target_prior_blob: 682e144d96d28f1ab64419eb0b7dcf352545ef3e
  geology_runbooks_readme_blob: 62d96d10a9ca0831b9847fb325cd2604c97ba1c1
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  geology_candidate_readme_blob: f0313cafc641c049d367af82418212e0bad1fc35
  geology_proof_readme_blob: fc07012855bb4019008a3b0dce035dc8088156f6
  geology_published_readme_blob: 543b117c031df125005bd2437cc30d1852c05bb1
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  promotion_gate_readme_blob: e729df0cc007e8cf0d9811afc25ec1f5ffbdffdd
  promotion_policy_readme_blob: 79287df1d828010d716ed43d2e24d6dbd610305b
  promotion_decisions_readme_blob: 18c6342f93212992f98d0e354390a36a79749858
  release_manifests_readme_blob: c699a527ff11bebad6a874ed1a37aa3a8213b86c
inspection_boundary: >-
  Current-session GitHub reads covered the exact target, the Geology runbook
  lane README, accepted Directory Rules compatibility and canonical paths,
  CODEOWNERS, Geology candidate,
  proof, published-carrier, policy, tests, workflow, shared promotion-readiness,
  source-authority, PromotionDecision, PromotionReceipt, release-manifest,
  correction, and rollback boundaries. Google Drive and attached Geology
  architecture documents were treated as read-only lineage and design input,
  not current implementation proof. No mounted repository checkout, live source,
  protected payload, exact subsurface record, credential, policy evaluator,
  evidence resolver, authenticated reviewer authority, release service,
  deployment, public endpoint, correction propagation, rollback execution, or
  public read-back was exercised. No source, candidate, decision, receipt,
  manifest, lifecycle transition, release, deployment, promotion, correction,
  rollback, or publication was created or performed.
related:
  - ./README.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./ROLLBACK_RUNBOOK.md
  - ./BEDROCK_REVIEW.md
  - ../../adr/ADR-0018-promotion-gate-sequence.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../domains/geology/README.md
  - ../../domains/geology/SENSITIVITY.md
  - ../../domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../data/registry/sources/geology/README.md
  - ../../../data/registry/sensitivity/geology/README.md
  - ../../../data/proofs/geology/README.md
  - ../../../data/published/geology/README.md
  - ../../../contracts/release/promotion_decision.md
  - ../../../contracts/release/promotion_receipt.md
  - ../../../contracts/release/release_manifest.md
  - ../../../policy/promotion/README.md
  - ../../../policy/domains/geology/README.md
  - ../../../release/candidates/geology/README.md
  - ../../../release/promotion_decisions/README.md
  - ../../../release/manifests/README.md
  - ../../../release/correction_notices/README.md
  - ../../../release/rollback_cards/README.md
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../.github/workflows/promotion-gate.yml
  - ../../../.github/workflows/domain-geology.yml
tags: [kfm, geology, natural-resources, runbook, promotion, readiness, evidence-character, source-role, claim-class, scale, depth, datum, sensitivity, rollback, fail-closed, no-network]
notes:
  - "v2.0.0 replaces proposal-era no-mounted-repository assumptions, guessed paths, illustrative release objects, lifecycle-wide A–G claims, and implied release machinery with current repository evidence and bounded procedures."
  - "The shared A–G validator is executable, deterministic, no-network, read-only, and non-publishing. PASS means APPROVE_READY for accountable review only."
  - "The current Geology candidate lane has no child candidate dossier; the source-authority projection is empty; Geology and promotion policy are inactive; the Geology proof and published lanes contain no release payload beyond their README and .gitkeep; and no Geology PromotionDecision or ReleaseManifest was established by the bounded inspection."
  - "The proposed ADR-0018 sequence is not accepted, and repository documentation still contains materially different A–G vocabularies. This runbook uses the implemented bounded validator names only when describing that validator."
  - "KFM is not an official geologic survey, regulator, mineral-property authority, reserve certifier, engineering authority, investment adviser, extraction authority, emergency service, or title authority."
  - "This document changes no source, candidate, data, contract, schema, policy, fixture, validator, workflow, evidence object, receipt, proof, review, release record, deployment, lifecycle state, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Promotion Runbook

> **Evaluate whether one specifically identified Geology and Natural Resources candidate has enough declared, public-safe support to be handed to accountable promotion review. Never translate documentation, a synthetic fixture pass, a green workflow, a schema-valid object, a map preview, or an `APPROVE_READY` result into promotion, release, deployment, or publication.**

> [!IMPORTANT]
> **Promotion is a governed state transition, not a file move, commit, pull request, merge, workflow result, candidate folder, decision-shaped file, receipt, manifest, alias change, map-layer toggle, or generated summary.** This procedure stops at a reviewable readiness or hold packet.

> [!CAUTION]
> **Current Geology promotion is `HOLD`.** At the evidence snapshot above, `release/candidates/geology/` contains only its README; the central source-authority projection has `entries: []`; Geology and shared promotion policy are inactive; the Geology proof and published lanes contain no payload beyond their README and `.gitkeep`; and no Geology `PromotionDecision` or `ReleaseManifest` was established by the bounded inspection.

> [!WARNING]
> **KFM is not an official geologic survey, regulator, mineral-property authority, reserve certifier, engineering authority, investment adviser, extraction authority, emergency service, or title authority.** This runbook cannot certify a geologic interpretation, deposit, reserve, permit, production record, legal right, engineering suitability, economic viability, extraction target, private-well condition, or life-safety conclusion.

**Quick navigation:** [Purpose](#purpose-and-terminal-boundary) · [Posture](#current-repository-posture) · [Placement](#directory-rules-basis) · [Scope](#scope-and-non-goals) · [Roles](#roles-and-separation-of-duties) · [Boundaries](#lifecycle-and-object-family-boundaries) · [Preflight](#preflight-and-mandatory-stop-conditions) · [Procedure](#promotion-readiness-procedure) · [Geology gates](#geology-specific-gates) · [A–G profile](#implemented-a-g-readiness-profile) · [Validation](#current-executable-validation) · [Packet](#candidate-review-packet) · [Outcomes](#finite-outcomes-and-current-holds) · [Authority](#authority-boundary-and-handoff) · [Recovery](#correction-withdrawal-and-rollback) · [Audit](#audit-and-join-keys) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback) · [Checklist](#appendix-a-operator-checklist) · [Commands](#appendix-b-current-command-and-surface-matrix)

---

<a id="purpose-and-terminal-boundary"></a>

## Purpose and terminal boundary

Use this runbook only when an identifiable Geology candidate is claimed to be at `CATALOG` or `TRIPLET` and someone is asking whether it is ready for a separately governed transition toward `PUBLISHED`.

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This procedure evaluates the **final promotion-readiness boundary**. It does not treat source admission, RAW capture, normalization, quarantine exit, processed-object validation, catalog creation, triplet generation, accountable review, transition application, release, deployment, and publication as one operation.

The operator must:

1. freeze the exact repository revision, candidate identity, requested lifecycle boundary, audience, spatial scope, temporal scope, depth/vertical reference, scale, and affected carriers;
2. verify that the candidate exists and is not merely a README, roadmap item, planning packet, fixture, generated example, stale index row, map preview, or model output;
3. preserve evidence character, source role, claim class, rights, sensitivity, spatial precision, time/vintage, scale, depth, datum, uncertainty, interpretation version, correction, and rollback distinctions;
4. run only repository-owned checks that apply to the pinned packet;
5. interpret each result within its actual fixture, schema, declared-reference, or readiness boundary;
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

The following conclusions are bounded to `main@889c3c609b4c3a1a79012cb6a00b0c0a5f00e87b`.

| Surface | Status | Safe conclusion |
|---|---|---|
| This runbook path | **CONFIRMED** | `docs/runbooks/geology/PROMOTION_RUNBOOK.md` is tracked. This is a same-path documentation modernization. |
| Directory governance | **CONFIRMED / accepted** | ADR-0029 adopts Directory Rules v2; `docs/runbooks/` owns human operational procedures. |
| Prior runbook | **CONFIRMED / proposal-era** | The v1 document mixed lifecycle-wide gates, guessed paths, proposed reason codes, illustrative release records, and unverified release behavior. It was not current implementation proof. |
| Geology candidate lane | **CONFIRMED / no child candidate** | `release/candidates/geology/` contains only `README.md`. A README is not a candidate or release. |
| Central source authority | **CONFIRMED / empty projection** | `control_plane/source_authority_register.yaml` is `PROPOSED`, `projection_only`, `implementation_status: ABSENT`, and has `entries: []`. It admits and activates no source. |
| Geology source registry | **CONFIRMED guidance / authority unresolved** | The lane documents source identity, role, rights, sensitivity, cadence, and activation boundaries; it does not overcome the empty central authority projection. |
| Geology domain validation | **CONFIRMED / bounded fixture profiles** | `domain-geology.yml` invokes no-network resource-class, AEM campaign, public-safe geometry, and production-material-change checks while explicitly retaining broader semantics, evidence, proof, policy, and release holds. |
| Geology policy | **CONFIRMED / inactive** | The lane contains default-only Rego scaffolds and placeholders; no accepted bundle, evaluator, native Geology Rego test, authenticated decision emitter, or governed consumer was established. |
| Geology proof lane | **CONFIRMED / no proof payload** | `data/proofs/geology/` contains `.gitkeep` and `README.md`; no child proof packet or Geology `EvidenceBundle` instance was established. |
| Geology published lane | **CONFIRMED / no released payload** | `data/published/geology/` contains `.gitkeep` and `README.md`; no release-linked public carrier was established. |
| Generic promotion readiness | **CONFIRMED / bounded executable** | The shared validator checks a declared `CATALOG`/`TRIPLET` to `PUBLISHED` packet through A–G gates without network access or writes. |
| Generic readiness result | **CONFIRMED / non-authoritative** | `PASS` maps to `APPROVE_READY` for accountable review only. It is not `APPROVE`, an applied transition, release, deployment, or publication. |
| Promotion gate sequence | **CONFLICTED / proposed** | ADR-0018 remains proposed, and lifecycle-wide guidance, older runbooks, and the bounded validator use materially different A–G names or responsibilities. |
| Shared promotion policy | **CONFIRMED / inactive** | `policy/promotion/` contains two proposed no-op Rego stubs; the promotion workflow does not execute them. |
| Geology review record | **NOT ESTABLISHED by bounded inspection** | No Geology review record or authenticated independent review authority was established. CODEOWNERS routing is not reviewer qualification or approval. |
| Geology promotion decision | **NOT ESTABLISHED by bounded inspection** | No Geology decision surfaced under `release/promotion_decisions/`. Other-domain examples do not authorize Geology. |
| Geology release manifest | **NOT ESTABLISHED by bounded inspection** | No Geology manifest surfaced under `release/manifests/`. Other-domain examples do not authorize Geology. |
| Transition, deployment, and public read-back | **UNKNOWN / not exercised** | No release operator, deployed consumer, public endpoint, alias switch, cache invalidation, correction propagation, or rollback execution was exercised. |

### Current default disposition

```text
candidate search: no child dossier established
source authority: empty
proof payload: absent
active policy: absent
accountable review: absent
Geology decision/manifest: absent

=> NO_ACTIVE_CANDIDATE_VERIFIED
=> operational promotion remains HOLD
```

Do not keep evaluating an invented packet after this disposition. A future run may continue only after newer pinned evidence establishes an actual candidate and the missing authority surfaces.

[Back to top](#top)

---

<a id="directory-rules-basis"></a>

## Directory Rules basis

### Placement outcome: `PLACE`

This file is a human operational procedure. The accepted Directory Rules place that responsibility under `docs/`, and the repository already tracks the requested path under `docs/runbooks/geology/`.

| Responsibility axis | Classification |
|---|---|
| Artifact kind | Human runbook |
| Authority owner | Documentation / human operating procedure |
| Owning root | `docs/` |
| Existing sub-root | `docs/runbooks/` |
| Domain segment | `geology/` |
| Exposure | Public documentation; no restricted payload |
| Mutability | Versioned replacement through reviewed Git history |
| Placement result | `PLACE` at the existing path |

The change does not create a root, move a file, establish a parallel promotion authority, amend Directory Rules, accept ADR-0018, or relocate any release object.

### Responsibility boundaries

| Concern | Owning surface | Role of this runbook |
|---|---|---|
| Geology meaning and domain boundaries | `docs/domains/geology/`, `contracts/domains/geology/` | Reference; do not redefine scientific truth. |
| Machine shape | `schemas/contracts/v1/` | Reference accepted shapes; do not invent fields here. |
| Source authority and admission | `data/registry/`, source controls | Require explicit accepted references; do not admit sources. |
| Evidence and proof | `data/proofs/` and evidence contracts | Require resolution; do not create proof. |
| Policy | `policy/` | Require an accepted evaluated result; do not author or execute policy. |
| Tests and validators | `tests/`, `fixtures/`, `tools/validators/` | Invoke bounded checks; do not replace their outputs with prose. |
| Review, decision, manifest, correction, rollback | `release/` | Prepare handoff pointers; do not approve or emit authoritative records. |
| Lifecycle payloads and public carriers | `data/` lifecycle lanes | Never copy or move them. |
| API, UI, map, export, and AI behavior | governed implementation and released surfaces | Verify public-safe handoff only; do not serve or publish. |

[Back to top](#top)

---

<a id="scope-and-non-goals"></a>

## Scope and non-goals

### In scope

This runbook may assess final readiness for a public-safe candidate involving, for example:

- bedrock or surficial geologic units and boundary versions;
- lithology, stratigraphic intervals, geologic age, structures, and geomorphic context;
- borehole, well-log, core, sample, geophysics, or geochemistry references where public-safe handling is established;
- mineral occurrences, resource deposits, resource estimates, production context, extraction sites, or reclamation records when their claim classes remain explicit;
- cross-sections, interpolations, generalized layers, and other derived representations with visible reality boundaries; and
- released-carrier candidates such as public-safe vector, raster, catalog, or map artifacts when their canonical support remains elsewhere.

### Out of scope

This runbook does not:

- fetch or activate KGS, KCC, KDHE, USGS, or any other source;
- determine a source's current terms, rights, authority, or cadence;
- promote from discovery to RAW, RAW to WORK, QUARANTINE to WORK, WORK to PROCESSED, or PROCESSED to CATALOG/TRIPLET;
- create a candidate dossier, proof packet, `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `PromotionReceipt`, `ReleaseManifest`, correction notice, withdrawal notice, or rollback card;
- execute Rego, authenticate a reviewer, verify a signing key, apply a lifecycle transition, move data, switch an alias, invalidate a cache, deploy, or publish;
- certify reserves, mineral rights, title, permits, production completeness, engineering suitability, economic viability, reclamation compliance, groundwater conditions, hazard risk, or public safety;
- expose exact or reverse-engineerable borehole, private-well, well-log, core, sample, geochemistry, sensitive-resource, operator/parcel, extraction-targetable, infrastructure-sensitive, archaeological, paleontological, cave, cultural, or sovereign-sensitive detail; or
- let a map, cross-section, 3D scene, model, generalized geometry, catalog record, graph, AI answer, test, or workflow become sovereign truth.

### Upstream work is not silently repaired here

A final-readiness packet may reference upstream artifacts only after they have been created and reviewed by their owners. Missing source admission, evidence, rights, sensitivity, policy, or catalog closure is a `HOLD` or `ABSTAIN`, not an invitation for the promotion operator to improvise the missing authority.

[Back to top](#top)

---

<a id="roles-and-separation-of-duties"></a>

## Roles and separation of duties

The repository verifies one GitHub review route: `@bartytime4life`. That route is useful for code review but is not a `StewardshipAssignment`, reviewer qualification, independent approval, policy authority, source authority, or release authority.

| Role needed for a material Geology handoff | Responsibility | Current assignment |
|---|---|---|
| Candidate author / assembler | Freezes candidate identity and assembles references. | NEEDS VERIFICATION |
| Geology domain reviewer | Reviews semantic meaning, interpretation boundaries, scale, depth, datum, and uncertainty. | NEEDS VERIFICATION |
| Source / rights reviewer | Confirms admitted source role, terms, attribution, redistribution, and freshness. | NEEDS VERIFICATION |
| Sensitivity reviewer | Reviews exact and reconstructable subsurface/resource precision and harmful joins. | NEEDS VERIFICATION |
| Evidence / proof reviewer | Verifies claim-scoped support resolves and remains current. | NEEDS VERIFICATION |
| Policy reviewer | Confirms the accepted policy bundle and result apply to this subject and audience. | NEEDS VERIFICATION |
| Validation reviewer | Confirms applicable deterministic checks and negative fixtures ran at the pinned revision. | NEEDS VERIFICATION |
| Accountable promotion reviewer | Decides whether the packet may proceed to decision processing; must be independent where materiality requires. | NEEDS VERIFICATION |
| Release authority | Issues or authorizes the separate release record and transition. | NEEDS VERIFICATION |
| Correction / rollback reviewer | Confirms correction path and prior safe target are usable. | NEEDS VERIFICATION |
| Operations / public-surface reviewer | Verifies deployed state and public read-back after a separately authorized release. | NEEDS VERIFICATION |

### Separation rules

1. The candidate author must not self-approve a material or sensitive Geology release.
2. CODEOWNERS approval does not prove independent scientific, source, rights, sensitivity, policy, evidence, or release review.
3. A schema-valid identity or fixture-only assignment cannot authenticate a live actor or authority interval.
4. Open review obligations, expired review validity, supersession, self-review, scope mismatch, or unbound hashes block readiness.
5. When no accountable reviewer route is verified, return `HOLD_FOR_REVIEW_AUTHORITY`.

[Back to top](#top)

---

<a id="lifecycle-and-object-family-boundaries"></a>

## Lifecycle and object-family boundaries

Keep the following states and object families separate in every packet and handoff.

```text
source discovery / admission
  -> RAW capture
  -> WORK or QUARANTINE
  -> PROCESSED candidate
  -> CATALOG / TRIPLET candidate
  -> final readiness evaluation
  -> accountable review
  -> PromotionDecision
  -> transition application + PromotionReceipt
  -> ReleaseManifest
  -> released public-safe carrier
  -> deployment / public read-back
  -> correction / withdrawal / rollback
```

### Anti-collapse matrix

| Surface | What it records | Must not be treated as |
|---|---|---|
| `SourceDescriptor` / source authority | Source identity, role, rights, sensitivity, cadence, activation posture | Evidence truth, candidate approval, or release |
| Candidate dossier | Public-safe assembly and blockers for one proposed release subject | Proof, decision, manifest, or public carrier |
| `RunReceipt` / validation receipt | What bounded process ran | Evidence truth, policy approval, or transition proof |
| `EvidenceRef` / `EvidenceBundle` | Claim-scoped support and limitations | Policy, review, decision, or release authority |
| `PolicyDecision` | Admissibility result and obligations from an accepted policy evaluation | Evidence truth, reviewer authority, or transition application |
| `ReviewRecord` | Accountable human disposition for a bound subject | Policy, decision, receipt, manifest, or deployment proof |
| A–G readiness result | Declared packet consistency under the implemented bounded profile | `APPROVE`, promotion, release, or publication |
| `PromotionDecision` | Separate final decision vocabulary such as `APPROVE`, `DENY`, or `ABSTAIN` | Proof that a transition was applied |
| `PromotionReceipt` | Process record for a declared promotion attempt | Decision authority, proof, manifest, or public state |
| `ReleaseManifest` | Release-family record binding released artifacts and rollback/correction context | Deployment or public read-back by itself |
| Published carrier | Released public-safe bytes or service representation | Canonical evidence or source truth |
| Map / cross-section / scene / AI answer | Downstream interpretation or delivery | Sovereign truth, source authority, or release authority |
| Correction / withdrawal / rollback record | Governed change to public release state and lineage | Permission to erase prior audit history |

### Readiness is not state

The bounded validator's `APPROVE_READY` is a readiness projection. It does not change `CATALOG` or `TRIPLET` to `PUBLISHED`. A separately authorized decision, transition application, release record, delivery action, and public read-back remain required and are not implemented by this runbook.

[Back to top](#top)

---

<a id="preflight-and-mandatory-stop-conditions"></a>

## Preflight and mandatory stop conditions

Run these checks in order. Stop at the first unresolved authority or unsafe condition; do not fill gaps with examples from this document.

### Preflight 0 — freeze repository and overlap

- [ ] Pin the exact base commit and target candidate bytes.
- [ ] Confirm the candidate-related files have not changed since the review packet was assembled.
- [ ] Search open pull requests, branches, migrations, and current work for the same candidate, release ID, manifest, policy, source, or public carrier.
- [ ] Confirm accepted ADRs and Directory Rules have not changed the owning paths or vocabulary.

**Stop:** `HOLD_FOR_CONCURRENCY` or `HOLD_FOR_AUTHORITY` when overlap or controlling authority is unresolved.

### Preflight 1 — establish an actual candidate

- [ ] A child dossier exists under the governed Geology candidate lane or another accepted candidate home.
- [ ] It has a stable candidate ID and version.
- [ ] It points to immutable candidate bytes and digests.
- [ ] It names the requested `CATALOG` or `TRIPLET` to `PUBLISHED` boundary.
- [ ] It is not a README, fixture, source map, proposal, generated receipt, model preview, map screenshot, or stale index row.

**Current result:** no child dossier is present. Stop with `NO_ACTIVE_CANDIDATE_VERIFIED`.

### Preflight 2 — source authority and source role

- [ ] Every contributing source resolves to an admitted source record.
- [ ] Source role, authority class, rights, sensitivity, cadence, and stale/supersession posture are explicit.
- [ ] No modeled, interpreted, aggregate, administrative, regulatory, candidate, synthetic, or generated support is upgraded into observation or physical-geology truth.

**Current central result:** `entries: []`. Stop with `HOLD_FOR_SOURCE_AUTHORITY` unless newer accepted evidence supersedes that snapshot.

### Preflight 3 — public-safe support

- [ ] Every consequential claim resolves through claim-scoped evidence support.
- [ ] Rights and sensitivity are resolved for the requested audience and precision.
- [ ] No exact or reverse-engineerable protected detail appears in the public dossier, validator diagnostics, logs, receipts, or attachments.
- [ ] Cross-section, interpolation, model, classification, generalization, or 3D representation carries a visible representation/reality boundary.

**Stop:** `ABSTAIN`, `HOLD_FOR_EVIDENCE`, `HOLD_FOR_RIGHTS`, `HOLD_FOR_SENSITIVITY`, or `DENY`.

### Preflight 4 — validation, policy, review, correction, and rollback

- [ ] Applicable domain checks ran at the pinned revision and their limits are recorded.
- [ ] Accepted policy source, bundle, selector, evaluator, input digest, outcome, reasons, obligations, and evaluation time are known.
- [ ] Accountable reviewers are authenticated, qualified for the subject, independent where required, and current.
- [ ] Correction, withdrawal, and rollback references bind the same candidate/release subject and identify a safe prior target or an explicit first-release posture.

**Current policy/review result:** operational support is not established. Stop with the matching `HOLD_FOR_*` disposition.

### Non-compensable stop conditions

No score, deadline, map quality, apparent scientific plausibility, source reputation, green workflow, or UI polish compensates for:

- no actual candidate;
- empty or unresolved source authority;
- unknown rights or harmful precision;
- missing evidence closure;
- source-role, knowledge-character, or resource-claim collapse;
- missing or inactive policy;
- absent accountable review and separation of duties;
- missing correction or rollback path;
- direct public access to internal or unreleased stores;
- hidden model or AI authority; or
- overlapping work that owns the same release subject.

[Back to top](#top)

---

<a id="promotion-readiness-procedure"></a>

## Promotion-readiness procedure

This sequence begins only after the preflight establishes an actual candidate. The current repository snapshot stops at Step 1.

### Step 0 — open a bounded evaluation record

Record:

- repository and candidate commit;
- candidate ID, version, author, and immutable artifact digests;
- current and requested lifecycle state;
- object families and claim classes;
- source IDs and source roles;
- spatial scope, CRS, horizontal datum, vertical datum, depth reference, scale, resolution, and generalized/public bbox;
- valid, observed, source, retrieval, publication, effective, correction, and transaction times where applicable;
- audience, rights, sensitivity, review significance, and public-precision posture;
- affected catalog, map, export, API, Evidence Drawer, Focus Mode, and downstream derivative surfaces; and
- open overlap, authority, and verification findings.

Do not put restricted coordinates, offsets, access routes, proprietary log content, parcel/operator joins, or transform secrets in the ordinary review record.

### Step 1 — resolve candidate identity

1. Enumerate the candidate lane at the pinned commit.
2. Reject parent READMEs, `.gitkeep`, fixtures, examples, proposal packets, and planning rows as candidates.
3. Verify one stable candidate ID maps to one immutable artifact set.
4. Verify no second writable candidate home or conflicting candidate ID exists.

**Current result:** `NO_ACTIVE_CANDIDATE_VERIFIED`. The procedure stops here for the current snapshot.

### Step 2 — verify object, knowledge, and claim classes

For a future candidate:

1. list each Geology object family;
2. classify each claim as observation/source-native record, interpretation/correlation, model, aggregate, regulatory/administrative context, candidate, or synthetic/derived representation;
3. classify natural-resource statements as occurrence, deposit, estimate, permit, production, reserve, extraction, or reclamation context;
4. deny any stronger class inferred only from a weaker class; and
5. record cross-lane dependencies without transferring ownership.

### Step 3 — resolve source admission and authority

1. resolve every `source_id` against accepted source authority and source records;
2. verify rights, attribution, redistribution, sensitivity, cadence, version/vintage, and source-head identity;
3. verify the source supports the exact claim class, spatial scale, time, and public use requested; and
4. stop on missing, stale, conflicted, superseded, or inactive source support.

A familiar agency name, URL, connector directory, PDF, catalog page, or historical use does not substitute for accepted source admission.

### Step 4 — verify candidate bytes and declared integrity

1. retrieve candidate artifacts only through the governed review path;
2. compare actual bytes to the pinned digest set;
3. verify the candidate, manifest projection, run receipt, and specification hash refer to the same artifact set;
4. reject duplicate, missing, malformed, mutable, or inconsistent digests; and
5. keep integrity distinct from evidence truth and source authority.

### Step 5 — apply Geology-specific validation and safety review

Run only checks that match the candidate's object families and representation. At minimum, review:

- source-role and resource-class anti-collapse;
- public-safe geometry metadata and absence of coordinate leakage;
- scale, CRS, datum, depth, and vertical-reference consistency;
- temporal/vintage and stale-state support;
- uncertainty, completeness, interpretation version, and model/reality boundary;
- rights and sensitivity for boreholes, wells, logs, cores, samples, geochemistry, resources, extraction sites, infrastructure, and harmful joins;
- catalog/proof linkage; and
- public API/map/export/AI non-bypass.

A bounded synthetic pass proves only its fixture contract. It does not validate the future candidate unless the candidate is explicitly and safely bound to that accepted profile.

### Step 6 — resolve evidence and catalog support

1. resolve every `EvidenceRef` to a current, claim-scoped `EvidenceBundle` or accepted equivalent;
2. verify source, claim, spatial, temporal, scale, depth, uncertainty, rights, sensitivity, citation, correction, and limitation bindings;
3. verify catalog and optional triplet projections are downstream indexes, not canonical truth;
4. verify the proof packet references actual immutable support rather than README guidance; and
5. return `ABSTAIN` or `HOLD_FOR_EVIDENCE` when resolution or authenticity is incomplete.

### Step 7 — obtain accepted policy and accountable review context

1. identify the accepted policy bundle, version, digest, entrypoint, evaluator, input hash, evaluation time, result, reasons, and obligations;
2. verify the result applies to the exact candidate, audience, precision, and requested transition;
3. resolve reviewer identities and authority assignments outside the fixture-only validator;
4. enforce separation of duties and current validity; and
5. preserve open obligations as `HOLD` or `ABSTAIN`, never silent approval.

Current Geology and shared promotion policy sources are inactive. A current path, Rego package name, default value, or workflow does not create an accepted policy result.

### Step 8 — assemble the bounded A–G input

Only after Steps 1–7 close, prepare a duplicate-free UTF-8 JSON packet matching the implemented bounded promotion-readiness profile.

The packet must declare, at minimum:

- profile, candidate, author, specification hash, and evaluation time;
- exact `CATALOG` or `TRIPLET` to `PUBLISHED` boundary;
- minimal release-manifest and run-receipt projections;
- artifact digests;
- public-safe geometry/CRS declarations;
- temporal interval;
- policy context;
- evidence, attestation, catalog, and conditional AI references;
- fixture-profile review identity/authority declarations; and
- rollback and correction linkage.

This packet is validator input. It is not a new release object family and must not become a second candidate, review, decision, receipt, or manifest authority.

### Step 9 — run the bounded validator

Use the repository-owned commands in [Appendix B](#appendix-b-current-command-and-surface-matrix).

Interpret the aggregate result exactly:

| Result | Readiness | Operator action |
|---|---|---|
| `PASS` | `APPROVE_READY` | Prepare the accountable review handoff. Do not approve or mutate state. |
| `ABSTAIN` | `BLOCKED` | Record missing support and preserve prior state. |
| `DENY` | `BLOCKED` | Record the unsafe or contradictory condition; do not proceed. |
| `ERROR` | `BLOCKED` | Preserve prior state; resolve parser/evaluator/input failure before rerun. |

Precedence is `ERROR > DENY > ABSTAIN > PASS`.

### Step 10 — prepare the accountable review handoff

When and only when the bounded result is `PASS`, assemble the public-safe packet in [Candidate review packet](#candidate-review-packet). Mark it:

```text
READY_FOR_ACCOUNTABLE_REVIEW
not APPROVED
not PROMOTED
not RELEASED
not DEPLOYED
not PUBLISHED
```

The handoff must name every unresolved live check that the fixture-only validator cannot perform, including evidence resolution, source authority, policy execution, reviewer authentication and qualification, signature verification, transition application, rollback usability, and public read-back.

[Back to top](#top)

---

<a id="geology-specific-gates"></a>

## Geology-specific gates

These controls supplement, not replace, the shared A–G readiness profile.

### 1. Knowledge-character gate

Keep these distinct:

- source-native observation or record;
- interpreted/correlated geologic assignment;
- compiled or generalized map product;
- model or interpolation;
- regulatory or administrative context;
- aggregate or statistical summary;
- candidate or announcement-bound state; and
- synthetic, generated, or AI-mediated representation.

A derived cross-section, interpolated surface, predicted resource potential, generalized tile, or generated narrative must not be promoted as direct observation.

### 2. Geologic-object gate

Preserve distinct identities for:

- map unit versus polygon/geometry representation;
- bedrock versus surficial unit;
- lithology versus stratigraphic interval versus geologic age;
- fault/structure versus hazard or engineering risk;
- borehole versus well log versus picked top versus core/sample versus geophysical/geochemical observation;
- cross-section interpretation versus measured subsurface geometry; and
- hydrostratigraphic context versus Hydrology measurement truth.

### 3. Natural-resource claim gate

Never collapse:

```text
MineralOccurrence != ResourceDeposit != ResourceEstimate != Reserve
Permit != Production != PhysicalGeology
ExtractionSite != OwnershipOrTitle
ReclamationRecord != RegulatoryComplianceCertification
```

A permit, operator record, lease, parcel, production aggregate, or historical extraction record cannot by itself prove a deposit, estimate, reserve, ownership interest, current production, economic viability, or extraction recommendation.

### 4. Spatial, scale, and representation gate

Require explicit:

- source and output CRS;
- horizontal datum;
- map/source scale and output scale;
- resolution, tolerance, and completeness;
- geometry validity and deterministic processing where applicable;
- public bbox or withheld-geometry posture;
- generalization/aggregation/masking/withholding declaration;
- transform or representation receipt reference without exposing protected parameters; and
- `RealityBoundaryNote` or equivalent for 3D, cross-sections, interpolation, reconstruction, or synthetic surfaces where material.

A visually plausible map is not evidence that the geometry, scale, or interpretation is fit for the requested claim.

### 5. Depth and vertical-reference gate

For subsurface material, require explicit and compatible:

- depth reference (`ground_surface`, `kelly_bushing`, `mean_sea_level`, or accepted vocabulary);
- units;
- vertical datum;
- measured versus interpreted interval;
- uncertainty and completeness; and
- transformation lineage.

Missing or incompatible depth/vertical context is `HOLD_FOR_VERTICAL_REFERENCE`, not a reason to guess or normalize silently.

### 6. Time, vintage, and stale-state gate

Keep distinct where applicable:

- observation/collection time;
- source publication time;
- retrieval time;
- map or dataset vintage;
- effective and correction time;
- transaction time; and
- model/interpretation version.

Mark a candidate stale when source cadence, rights, schema, policy, review, geography, map vintage, or model/interpretation support aged out. Stale does not automatically mean wrong, but stale support cannot silently satisfy readiness.

### 7. Rights, sensitivity, and harmful-join gate

Fail closed for exact or reverse-engineerable:

- borehole, private-well, well-log, core, sample, geochemistry, or sensitive-resource locations;
- proprietary logs or licensed records;
- operator/parcel/owner or living-person joins;
- extraction-targetable resources and access routes;
- critical or storage infrastructure;
- archaeological, paleontological, cave, cultural, sacred, treaty, sovereign, or community-controlled locations; and
- redaction offsets, transform secrets, credentials, private endpoints, or reconstruction aids.

Public-safe handling must occur before delivery, not through a client-only style filter. Unknown rights, sovereignty, consent, sensitivity, or reconstruction risk yields `HOLD`, `RESTRICT`, `DENY`, or `ABSTAIN`.

### 8. Cross-lane ownership gate

A Geology candidate may relate to Soil, Hydrology, Hazards, Agriculture, Archaeology, Settlements/Infrastructure, or People/DNA/Land, but it may not replace those lanes' authority.

Examples:

- parent-material context does not become Soil map-unit truth;
- hydrostratigraphic context does not become a water-level or water-quality measurement;
- a fault or subsidence feature does not become current hazard or engineering advice;
- a parcel, operator, permit, or lease does not become title or mineral-right proof; and
- archaeological or cultural context does not authorize exact public location.

### 9. Public-surface gate

Before handoff, verify the intended carrier:

- is downstream of a release record and governed interface;
- contains only released public-safe fields and geometry;
- preserves evidence, time, source role, claim class, policy, review, stale, correction, and limitation cues;
- does not read RAW, WORK, QUARANTINE, unreleased candidate, canonical/internal, restricted, or direct-model stores; and
- makes AI abstain when evidence or policy closure is missing.

The runbook does not perform that public-surface verification; it records the requirement and holds the packet until an accountable operator can prove it.

[Back to top](#top)

---

<a id="implemented-a-g-readiness-profile"></a>

## Implemented A–G readiness profile

Use the exact implemented names below. Do not use a letter alone, because older repository documents use A–G for different lifecycle-wide concerns and ADR-0018 remains proposed.

| Gate | Exact name | Bounded check | Important non-proof |
|:---:|---|---|---|
| A | `identity_and_closure` | Profile, candidate/author/spec identity, declared lifecycle boundary, and minimal manifest identity. | Does not admit sources, resolve objects, or prove complete release closure. |
| B | `asset_integrity` | Candidate/manifest/run-receipt specification and digest-set agreement. | Does not retrieve bytes, prove provenance, immutability, or signature trust. |
| C | `geometry_and_crs` | Declared validity, deterministic processing, bounded CRS, and finite ordered bbox. | Does not prove Geology fitness, source scale, datum/depth correctness, or sensitivity transform. |
| D | `temporal_semantics` | Canonical UTC-second timestamps, interval ordering, and supplied evaluation time. | Does not prove freshness policy, bitemporal authority, or a trusted clock. |
| E | `rights_and_sensitivity` | Known policy profile/labels and finite declared policy result. | Does not execute accepted policy or prove rights, consent, sovereignty, or sensitivity truth. |
| F | `proof_and_catalog_support` | Declared evidence, attestation, run-receipt, STAC/DCAT/PROV, and conditional AI references. | Does not dereference support, prove `EvidenceBundle` truth, or verify signatures/catalog integrity. |
| G | `review_and_rollback` | Fixture-only review identity/authority/interval/binding, rollback, and correction declarations. | Does not authenticate people, qualifications, assignments, independence, rollback usability, or correction propagation. |

### Finite results

| Validator result | Readiness projection | Meaning |
|---|---|---|
| `PASS` | `APPROVE_READY` | Every bounded declared check passed. Accountable review remains required. |
| `ABSTAIN` | `BLOCKED` | Support is insufficient without a contradictory unsafe claim. |
| `DENY` | `BLOCKED` | A mandatory, unsafe, or contradictory condition blocks readiness. |
| `ERROR` | `BLOCKED` | Input or declared policy evaluation could not be completed safely. |

A `PASS` never emits or implies `APPROVE`, `PROMOTED`, `PUBLISHED`, `RELEASED`, or `DEPLOYED`.

[Back to top](#top)

---

<a id="current-executable-validation"></a>

## Current executable validation

### Shared promotion readiness

The repository confirms:

- a standard-library, duplicate-rejecting, no-network, non-writing A–G validator;
- synthetic valid/invalid/error fixtures;
- focused tests for finite outcomes, precedence, deterministic output, non-emission, no-network behavior, review bindings, and negative cases;
- `make publish-check` as the complete bounded local proof; and
- a read-only `promotion-gate` workflow that emits summaries only.

The shared workflow also preserves explicit holds: it does not authenticate evidence, execute the inactive promotion Rego sources, verify live actor authority, verify DSSE/cosign, apply a lifecycle transition, execute rollback, or emit an authoritative release-family object.

### Geology-domain checks

The current `domain-geology` workflow invokes bounded no-network profiles for:

1. **resource-class/source-role distinction** — protects occurrence, deposit, estimate, permit, production, reserve, modeled potential, and observation boundaries;
2. **announcement-bound AEM campaign candidate** — preserves sparse, time-scoped, current-state-unknown campaign context without treating an announcement as acquisition evidence;
3. **public-safe geometry metadata** — denies coordinate material and exact public geometry, requires restricted-source posture and generalized/withheld declarations, and still returns a hold because it performs no transform or release; and
4. **production material change** — compares version-pinned metadata and emits bounded change-review outcomes without treating production as physical-geology, deposit, estimate, or reserve truth.

The workflow explicitly holds broader Geology semantics, evidence closure, proof, policy, and release. These profiles are not candidate-specific release validation unless a future accepted integration binds the exact candidate, profile, source, evidence, policy, review, and artifact hashes.

### What current checks do not establish

They do not establish:

- source activation or current upstream facts;
- actual candidate existence;
- geologic interpretation truth;
- reserve, estimate, permit, production, title, mineral-right, engineering, or economic conclusions;
- exact subsurface safety;
- accepted policy evaluation;
- claim-scoped Geology proof closure;
- authenticated independent review;
- a Geology `PromotionDecision`, `PromotionReceipt`, or `ReleaseManifest`;
- transition application, released carrier, deployment, or publication; or
- rollback/correction execution.

[Back to top](#top)

---

<a id="candidate-review-packet"></a>

## Candidate review packet

When a future candidate reaches `READY_FOR_ACCOUNTABLE_REVIEW`, provide one public-safe packet containing:

### Identity and scope

- repository commit and evaluation profile;
- stable candidate ID/version and candidate author;
- exact current/requested lifecycle states;
- candidate specification hash and artifact digest set;
- object families, knowledge characters, source roles, and natural-resource claim classes;
- public spatial scope, scale, resolution, CRS, horizontal/vertical datum, depth reference, and uncertainty;
- temporal/vintage/freshness scope;
- intended audience and public carriers; and
- correction and rollback subject identity.

### Support references

- admitted source references and source-authority records;
- claim-scoped evidence/proof references;
- validation reports and exact tool/profile versions;
- policy bundle/evaluator/input/result references;
- public-safe geometry/representation findings and receipt references;
- accountable review identities/assignments and separation evidence;
- candidate manifest projection;
- rollback target and correction path; and
- downstream invalidation/public read-back plan for a separately authorized release.

### Findings

Include:

- the A–G deterministic JSON result;
- Geology-specific gate outcomes;
- all `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, stale, conflict, and open-obligation findings;
- every live/authenticity check not performed by the bounded validator;
- no-publication and no-release boundary statement; and
- explicit next owner for each unresolved item.

### Restricted appendix rule

Do not place protected coordinates, proprietary records, redaction offsets, access routes, private identities, credentials, or reverse-engineering aids in the ordinary packet. Reference an approved restricted review system and expose only the minimum public-safe finding needed for the decision.

[Back to top](#top)

---

<a id="finite-outcomes-and-current-holds"></a>

## Finite outcomes and current holds

### Runbook-level dispositions

| Disposition | Use when | Next action |
|---|---|---|
| `NO_ACTIVE_CANDIDATE_VERIFIED` | No actual child candidate dossier is established. | Stop. A candidate owner must create a governed dossier through the accepted process. |
| `READY_FOR_ACCOUNTABLE_REVIEW` | Actual candidate exists; required support is resolved; bounded A–G returns `PASS`; Geology-specific checks close. | Hand off to authenticated, qualified, independent review. Do not mutate state. |
| `HOLD_FOR_SOURCE_AUTHORITY` | Source admission, role, rights, cadence, or authority is unresolved. | Resolve under source governance. |
| `HOLD_FOR_EVIDENCE` | EvidenceRef cannot resolve to claim-scoped support. | Resolve or abstain; do not invent support. |
| `HOLD_FOR_RIGHTS` | Rights, attribution, redistribution, consent, sovereignty, or terms are unresolved. | Rights/steward review. |
| `HOLD_FOR_SENSITIVITY` | Public precision, harmful join, reconstruction risk, or restricted content is unresolved. | Restrict, generalize, redact, stage, or deny. |
| `HOLD_FOR_VERTICAL_REFERENCE` | Depth units, reference, or vertical datum is absent or incompatible. | Correct the candidate and rerun. |
| `HOLD_FOR_POLICY` | Accepted policy bundle/evaluator/result is absent, inactive, stale, or mismatched. | Policy owner must resolve; the runbook cannot substitute. |
| `HOLD_FOR_REVIEW_AUTHORITY` | Reviewer identity, qualification, assignment, independence, scope, or validity is unresolved. | Establish accountable review. |
| `HOLD_FOR_CORRECTION_PATH` | Correction, withdrawal, derivative invalidation, or public notification path is incomplete. | Release/correction owner resolves. |
| `HOLD_FOR_ROLLBACK` | No safe prior target or verified first-release rollback posture exists. | Release/rollback owner resolves. |
| `HOLD_FOR_CONCURRENCY` | Overlapping PR, candidate, decision, manifest, migration, or release is active. | Reconcile ownership and ordering. |
| `ABSTAIN` | Evidence/support is insufficient without an unsafe contradiction. | Preserve prior state and narrow the claim. |
| `DENY` | Unsafe, contradictory, prohibited, or rights/sensitivity-invalid condition exists. | Do not proceed; record reason and correction path. |
| `ERROR` | Packet, parser, validator, evaluator, or tool failed safely. | Preserve prior state and repair before replay. |

### Current hold register

| Hold | Current evidence |
|---|---|
| `NO_ACTIVE_CANDIDATE_VERIFIED` | Candidate lane contains only `README.md`. |
| `HOLD_FOR_SOURCE_AUTHORITY` | Central source-authority projection is empty and implementation status is absent. |
| `HOLD_FOR_EVIDENCE` | Geology proof lane contains no child proof payload. |
| `HOLD_FOR_POLICY` | Geology and shared promotion policy are inactive/unbound. |
| `HOLD_FOR_REVIEW_AUTHORITY` | No accountable Geology review record or independent authority is established. |
| `HOLD_FOR_DECISION` | No Geology `PromotionDecision` is established. |
| `HOLD_FOR_RELEASE_MANIFEST` | No Geology `ReleaseManifest` is established. |
| `HOLD_FOR_RELEASED_CARRIER` | Geology published lane contains no released payload beyond README and `.gitkeep`. |
| `HOLD_FOR_DEPLOYMENT_AND_PUBLIC_READBACK` | Not exercised or verified. |

No current hold may be cleared by editing this runbook.

[Back to top](#top)

---

<a id="authority-boundary-and-handoff"></a>

## Authority boundary and handoff

### What this runbook may hand off

- a pinned, public-safe candidate-readiness packet;
- bounded validator output;
- Geology-specific findings;
- unresolved holds, conflicts, and obligations;
- exact support references; and
- a recommendation to proceed to accountable review, hold, abstain, deny, or repair.

### What the next authority must still do

A separately governed process must:

1. authenticate evidence, policy, actors, assignments, and signatures;
2. resolve open obligations and separation of duties;
3. issue a valid decision through the accepted release contract;
4. apply or deny the lifecycle transition through an authorized operator;
5. emit the authoritative receipt/manifest/correction/rollback records;
6. deliver only released public-safe carriers through governed interfaces;
7. verify deployment and public read-back; and
8. preserve audit, correction, withdrawal, and rollback lineage.

### Explicit no-effects statement

Neither this runbook, a completed checklist, a `PASS`, an `APPROVE_READY` packet, a pull-request approval, nor a merge:

- admits a source;
- approves evidence or policy;
- authenticates review authority;
- creates a `PromotionDecision`;
- applies a lifecycle transition;
- creates a `PromotionReceipt` or `ReleaseManifest`;
- moves data into `PUBLISHED`;
- changes an alias, cache, API, map, export, or AI surface;
- deploys; or
- publishes.

[Back to top](#top)

---

<a id="correction-withdrawal-and-rollback"></a>

## Correction, withdrawal, and rollback

Promotion readiness is incomplete unless the future release can be corrected, withdrawn, and rolled back without erasing history.

### Before accountable review

Verify the packet declares:

- whether this is a first release or has a prior safe release;
- rollback subject and target identities;
- affected artifacts and public surfaces;
- correction and withdrawal route;
- downstream catalog, tile, map, export, search, graph, AI, and cache invalidation scope;
- reviewer/authority requirements; and
- stale-state and supersession behavior.

### When a candidate changes

Any material change to candidate bytes, specification, source set, evidence, rights, sensitivity, geometry, scale, depth, datum, time, model, policy, review, correction, rollback, or intended carrier invalidates the prior readiness packet. Re-pin, re-resolve, rerun, and re-review.

### After an authorized release

Use the separate [Geology rollback runbook](./ROLLBACK_RUNBOOK.md) and the governing release records. Do not perform a hidden file swap, pointer update, cache purge, or layer toggle from this runbook.

### Sensitive exposure

When a release exposes or enables reconstruction of protected Geology detail:

1. deny or disable affected public access through the authorized incident/release path;
2. preserve the failed release and audit records;
3. involve sensitivity, rights, correction, release, and operations reviewers;
4. issue the applicable withdrawal/correction/rollback records;
5. invalidate derived carriers and caches; and
6. verify the public surface no longer exposes the unsafe material.

This document does not claim that operational tooling for those steps is currently fielded.

[Back to top](#top)

---

<a id="audit-and-join-keys"></a>

## Audit and join keys

A promotion-review trail should join these identities without relying on filenames or prose similarity:

| Join | Required binding |
|---|---|
| Candidate → repository | exact commit, path, candidate ID/version, specification hash |
| Candidate → artifacts | complete unique digest set |
| Candidate → sources | accepted source IDs, roles, versions/vintages, rights/sensitivity refs |
| Candidate → claims | object family, knowledge character, resource claim class, spatial/time/depth/scale scope |
| Candidate → evidence | claim-scoped EvidenceRefs and resolved bundle IDs/digests |
| Candidate → validation | validator profile/version, input digest, output digest, finite result, execution time |
| Candidate → policy | bundle/evaluator/entrypoint/input/result identities and obligations |
| Candidate → review | reviewer identity/assignment, subject, scope, validity, separation, spec/artifact bindings |
| Candidate → decision | separate decision ID and candidate/spec/evidence/policy/review bindings |
| Decision → transition receipt | decision ID, before/after state, transition-applied evidence, operator authority |
| Transition → release manifest | release ID, artifact digests, evidence, policy, review, rollback/correction refs |
| Release → public carriers | immutable carrier IDs/digests, aliases, cache/deployment refs, public-readback result |
| Release → correction/rollback | supersession, invalidation, withdrawal, prior target, restoration verification |

A missing join yields `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` according to the owning control. Do not substitute a relative path, README link, or generated narrative for a stable governed identity.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Evidence required | Current posture |
|---|---|---|---|
| `GEO-PROM-01` | First actual Geology release candidate | Child dossier with stable identity, immutable artifacts, public-safe scope, blockers, and support refs | HOLD |
| `GEO-PROM-02` | Accepted Geology source authority | Populated accepted authority/source records with owner, role, rights, sensitivity, cadence, and activation state | HOLD |
| `GEO-PROM-03` | Geology proof packet/profile | Child proof material, accepted claim-closure profile, resolver integrity, validation, and ownership | HOLD |
| `GEO-PROM-04` | Active Geology policy | Accepted rules, input/output contracts, bundle, evaluator, tests, selector, consumer, and decision receipts | HOLD |
| `GEO-PROM-05` | Accepted shared promotion sequence | ADR-0018 or successor accepted with vocabulary and compatibility closure | HOLD / CONFLICTED |
| `GEO-PROM-06` | Candidate-specific domain validation | Exact candidate bound to accepted Geology checks and negative fixtures | HOLD |
| `GEO-PROM-07` | Accountable independent review | Verified actors, assignments, qualification, subject/scope binding, validity, separation, and obligations | HOLD |
| `GEO-PROM-08` | Production signature and attestation verification | Accepted trust roots, profiles, tooling, transparency, and replay evidence | HOLD |
| `GEO-PROM-09` | Transition application | Authorized operator, before/after state proof, idempotence, concurrency control, and authoritative receipt | HOLD |
| `GEO-PROM-10` | Geology release manifest and carrier | Accepted manifest linked to public-safe immutable carrier and rollback/correction context | HOLD |
| `GEO-PROM-11` | Deployment and public read-back | Governed consumer, alias/cache/deployment record, response verification, and observability | UNKNOWN / HOLD |
| `GEO-PROM-12` | Correction and rollback drill | Executable drill over a synthetic/public-safe Geology release with invalidation and restored public state | HOLD |
| `GEO-PROM-13` | Sensitive restricted-review system | Approved handling for exact subsurface/resource details without ordinary Git exposure | UNKNOWN / HOLD |
| `GEO-PROM-14` | Runbook index maturity | `docs/runbooks/geology/README.md` is now substantive but still classifies this runbook as proposal-era; synchronize that index after this replacement lands or through the smallest directly coupled follow-up | NEEDS VERIFICATION |
| `GEO-PROM-15` | Hosted exact-head validation | Exact-head docs, link, domain-geology, promotion-gate, security, and required-check results after repository mutation | NEEDS VERIFICATION |

Open items are not TODO placeholders to fill with guesses. Each must be resolved by the owning responsibility and recorded with pinned evidence.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

### Repository evidence used

| Evidence | Supports | Limitation |
|---|---|---|
| Existing target blob at the pinned main commit | Confirms the v1 file and proposal-era content being replaced. | Does not prove any described promotion behavior. |
| `docs/runbooks/geology/README.md` at blob `62d96d10…` | Confirms the local lane boundary, five-procedure inventory, and its current classification of this target as proposal-era. | The index predates this replacement and will require maturity synchronization after the target changes. |
| Accepted Directory Rules path and ADR-0029 compatibility record | Confirms same-path `PLACE` under the human documentation responsibility. | Does not approve release behavior. |
| CODEOWNERS | Confirms `@bartytime4life` as the repository review route. | Does not establish accountable or independent domain/release authority. |
| `release/candidates/geology/` tree and README | Confirms no child candidate at the snapshot and defines the pre-publication boundary. | Does not rule out external or later candidates. |
| Source-authority register | Confirms `PROPOSED`, `projection_only`, `implementation_status: ABSENT`, and `entries: []`. | Does not establish source authority. |
| Geology policy README and lane inventory | Confirms default-only/inactive source and missing evaluator/consumer closure. | Does not prove policy behavior. |
| Geology domain workflow | Confirms bounded no-network fixture checks and broader holds. | Does not validate a real candidate, evidence, policy, release, or public state. |
| Geology proof and published directory trees | Confirms `.gitkeep` plus README only at the snapshot. | Does not prove no external, generated, or later artifacts. |
| Shared promotion validator README/workflow | Confirms implemented A–G names, finite results, commands, no-network/no-write posture, and `APPROVE_READY` boundary. | Checks declared packet consistency; no live authentication or transition. |
| ADR-0018 | Confirms the sequence remains proposed and vocabulary conflict remains visible. | Not controlling architecture authority. |
| Promotion policy README | Confirms two proposed no-op Rego stubs and inactive integration. | Does not provide an operational policy result. |
| Promotion decision and manifest directories/searches | No Geology record surfaced in the bounded inspection. | Not a recursive proof of every external, history-only, or later object. |

### Attached and Drive source use

The supplied Geology architecture report supports the lane's semantic anti-collapse, public-safe geometry, evidence, rights, sensitivity, release, correction, and rollback design intent. Its own evidence boundary states that it was created without a mounted repository and that its paths and implementation details were proposed. This runbook therefore uses that report as lineage and design pressure only; current repository evidence controls implementation claims.

The attached implementation prompt controls working method, scope discipline, validation posture, and terminal limits. It does not by itself prove repository state or authorize release/publication transitions.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This change replaces only:

```text
docs/runbooks/geology/PROMOTION_RUNBOOK.md
```

### Before merge

Close the draft pull request or abandon its scoped branch through normal repository controls. Do not force-push shared history or change release/publication state.

### After merge

Revert the documentation commit or restore prior Git blob:

```text
682e144d96d28f1ab64419eb0b7dcf352545ef3e
```

Then rerun applicable docs, link, metadata, domain-geology, promotion-gate, security, and repository-native checks.

### Runtime and release rollback

None is expected from this Markdown-only change. It activates no source, policy, validator, candidate, decision, transition, manifest, carrier, deployment, or publication.

[Back to top](#top)

---

<a id="appendix-a-operator-checklist"></a>

## Appendix A — operator checklist

### Authority and concurrency

- [ ] Exact repository commit pinned.
- [ ] Candidate and target bytes unchanged since packet assembly.
- [ ] Open PRs, migrations, and release work checked for overlap.
- [ ] Accepted ADRs and Directory Rules rechecked.

### Candidate existence

- [ ] Actual child candidate dossier exists.
- [ ] Stable candidate ID and version established.
- [ ] Immutable artifact pointers and digests established.
- [ ] Requested boundary is exactly `CATALOG` or `TRIPLET` to `PUBLISHED`.
- [ ] Candidate is not a README, fixture, example, proposal, generated receipt, or preview.

### Geology semantics

- [ ] Object families explicit.
- [ ] Observation/record, interpretation, model, aggregate, regulatory/administrative, candidate, and synthetic roles explicit.
- [ ] Occurrence, deposit, estimate, reserve, permit, production, extraction, and reclamation classes remain distinct.
- [ ] Cross-lane ownership preserved.
- [ ] Scale, CRS, horizontal datum, vertical datum, depth reference, units, uncertainty, completeness, and interpretation version explicit.
- [ ] Time/vintage/freshness/stale state explicit.

### Source, rights, and sensitivity

- [ ] Every source resolves to accepted authority/admission.
- [ ] Rights, attribution, redistribution, consent/sovereignty, cadence, and source head resolved.
- [ ] Public precision is explicit.
- [ ] No protected coordinates, harmful joins, proprietary content, credentials, or reconstruction aids appear in the public packet.
- [ ] Representation/reality boundaries and transform receipt references are present where needed.

### Evidence, validation, policy, and review

- [ ] EvidenceRefs resolve to claim-scoped support.
- [ ] Applicable deterministic domain checks and negative fixtures ran at the pinned revision.
- [ ] Accepted policy bundle/evaluator/input/result/obligations resolved.
- [ ] Review actors and assignments authenticated outside fixture-only validation.
- [ ] Qualifications, subject/scope, validity, separation, and open obligations verified.

### Correction and rollback

- [ ] First-release or prior-safe-target posture explicit.
- [ ] Correction, withdrawal, and rollback refs bind the same subject.
- [ ] Downstream invalidation scope complete.
- [ ] Public read-back and restoration verification plan exists.

### Bounded validator and handoff

- [ ] Input is duplicate-free UTF-8 JSON and contains no restricted values.
- [ ] Implemented A–G profile used by exact name/version.
- [ ] Deterministic result and exit code captured.
- [ ] `PASS` interpreted only as `APPROVE_READY`.
- [ ] Live checks not performed by validator are listed.
- [ ] Final disposition uses only this runbook's permitted terminal states.
- [ ] No lifecycle mutation, release, deployment, or publication performed.

[Back to top](#top)

---

<a id="appendix-b-current-command-and-surface-matrix"></a>

## Appendix B — current command and surface matrix

### Shared bounded promotion readiness

Run the complete fixture-first local proof:

```bash
make publish-check
```

Run the readiness and fixture-only review matrices separately:

```bash
python tools/validators/validate_promotion_gate.py --fixtures
python tools/validators/validate_review_record.py --fixtures
```

Evaluate one explicit, public-safe packet:

```bash
python tools/validators/validate_promotion_gate.py candidate.json
```

These commands write no decision, receipt, proof, manifest, lifecycle object, or public artifact.

### Current bounded Geology checks

The current domain workflow invokes these families under no-network settings. Use repository-native workflow execution or the exact commands below only after confirming the pinned revision and dependencies.

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/geology/test_source_role_anti_collapse.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tests/domains/geology/test_aem_campaign.py --verbose

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python -m pytest -q -p no:cacheprovider \
  tests/domains/geology/test_public_safe_geometry.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python tools/validators/geology/public_safe_geometry/validate_public_safe_geometry.py \
  --fixtures

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 \
  python -m pytest -q -p no:cacheprovider \
  tests/domains/geology/test_production_material_change.py
```

For the resource-class fixtures, the workflow also executes:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/geology/validate_resource_class_distinction.py \
  fixtures/domains/geology/resource_class/valid/*.json
```

For the AEM campaign fixtures, the workflow also executes:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/domains/geology/validate_aem_campaign.py \
  fixtures/domains/geology/aem_survey_campaign/valid/*.json
```

A green result remains bounded to the selected synthetic fixtures and current code. It does not clear the current operational holds.

### Surface/status matrix

| Surface | Current use | Do not infer |
|---|---|---|
| `docs/runbooks/geology/PROMOTION_RUNBOOK.md` | Human procedure | Decision or transition authority |
| `release/candidates/geology/README.md` | Candidate-lane boundary | Active candidate |
| `control_plane/source_authority_register.yaml` | Empty proposed projection | Admitted source |
| `data/proofs/geology/README.md` | Proof-lane boundary | Geology proof packet |
| `data/published/geology/README.md` | Published-lane boundary | Released carrier |
| `policy/domains/geology/` | Proposed inactive policy source | Policy clearance |
| `policy/promotion/` | Proposed inactive promotion source | Promotion approval |
| `tools/validators/promotion_gate/` | Bounded declared-packet readiness | Live evidence/authentication or transition |
| `.github/workflows/domain-geology.yml` | Bounded fixture checks and holds | Geology truth, proof, release, or publication |
| `.github/workflows/promotion-gate.yml` | Read-only shared readiness checks | Promotion or release |
| `release/promotion_decisions/` | Shared decision-family home | Geology decision unless an exact record is verified |
| `release/manifests/` | Shared manifest-family home | Geology release unless an exact record is verified |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Effect |
|---|---|---|---|
| `v1` | NEEDS VERIFICATION | Proposal-era lifecycle-wide Geology promotion procedure with guessed paths and illustrative objects. | Documentation only; implementation not established. |
| `v2.0.0` | 2026-08-25 | Reconciled the same path against current repository evidence; narrowed scope to final readiness; recorded current no-candidate/source/policy/proof/release holds; adopted implemented A–G names only for the bounded validator; strengthened Geology anti-collapse, scale/depth/datum, sensitivity, review, audit, and handoff controls. | Documentation only; no source, candidate, decision, transition, release, deployment, or publication effect. |

[Back to top](#top)
