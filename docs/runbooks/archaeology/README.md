<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/archaeology/readme
title: Archaeology Runbooks — Operational Procedure and Sensitive-Domain Boundary
type: readme
subtype: domain-runbook-boundary
version: v0.1
status: draft; repository-grounded; mixed-child-maturity; sensitive-domain; documentation-only; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
  - "NEEDS VERIFICATION — accountable Archaeology, cultural/sovereignty, rights-holder, sensitivity, evidence, policy, release, rollback, and independent-review authorities"
created: 2026-08-24
updated: 2026-08-24
policy_label: public-review; archaeology; cultural-heritage; exact-location-denied; fail-closed; no-publication-authority
current_path: docs/runbooks/archaeology/README.md
owning_root: docs/
responsibility: "Define the human-facing boundary, navigation, inheritance, current maturity, safety posture, maintenance contract, and non-effects for Archaeology operational procedures without granting cultural, source, evidence, policy, review, lifecycle, release, deployment, promotion, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational-documentation index
canonical_relationship: same-path completion of an existing tracked one-byte file; local boundary for the canonical docs/runbooks/archaeology procedure lane; no sibling authority created
repository: bartytime4life/Kansas-Frontier-Matrix
base_ref: main
base_commit: f83c290dd7b6ed2e86262a1b483b76c60de350e6
target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
parent_runbooks_readme_blob: 7b6f266a41f7723cba50ea3c093d341063c08f4d
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
domain_workflow_blob: d51ba3b1244844a83d857a34305e1a167e20dadb
domain_orientation_readme_blob: ed0c3a1917c8669b722b5be4bbddac1e89b23530
domain_orientation_rollback_drill_blob: eb559611a62bf7fa3ee76f6b45e0e1ce171ca3f0
no_network_test_runbook_blob: 6a57abe60da8f3acd4ada0eda255fc827b41cdca
promotion_runbook_blob: 6c746a4fc2977f0081025c55f6ddc08feba820f7
rollback_runbook_blob: 9e59120c3b15fe5ac96c22bf5c5492cc03232a70
source_refresh_runbook_blob: c50bcf2f484d670f2c91745550304445852f0ffa
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
related:
  - docs/runbooks/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ARCHITECTURE.md
  - docs/domains/archaeology/DATA_LIFECYCLE.md
  - docs/domains/archaeology/SENSITIVITY.md
  - docs/domains/archaeology/CULTURAL_REVIEW.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - docs/domains/archaeology/RELEASE_INDEX.md
  - docs/domains/archaeology/VERIFICATION_BACKLOG.md
  - docs/domains/archaeology/runbooks/README.md
  - docs/domains/archaeology/runbooks/rollback-drill.md
  - docs/runbooks/archaeology/NO_NETWORK_TEST_RUNBOOK.md
  - docs/runbooks/archaeology/PROMOTION_RUNBOOK.md
  - docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md
  - docs/runbooks/archaeology/SOURCE_REFRESH_RUNBOOK.md
  - contracts/domains/archaeology/README.md
  - schemas/contracts/v1/domains/archaeology/README.md
  - fixtures/domains/archaeology/README.md
  - policy/domains/archaeology/README.md
  - tests/domains/archaeology/README.md
  - tools/validators/domains/archaeology/README.md
  - release/candidates/archaeology/README.md
  - data/proofs/archaeology/README.md
  - .github/workflows/domain-archaeology.yml
  - .github/CODEOWNERS
notes:
  - "The prior target was a tracked one-byte file containing only a newline. This edition adds the missing local boundary without moving or renaming any procedure."
  - "NO_NETWORK_TEST_RUNBOOK.md, PROMOTION_RUNBOOK.md, and ROLLBACK_RUNBOOK.md are repository-grounded drafts with deliberately bounded executable evidence; SOURCE_REFRESH_RUNBOOK.md retains proposal-era assumptions and remains planning-only."
  - "docs/domains/archaeology/runbooks/ is retained as domain-dossier lineage and orientation. It does not become a second writable operational-procedure authority."
  - "No exact or reverse-engineerable archaeological location, burial or human-remains detail, sacred-site information, culturally restricted knowledge, consent secret, collection-security detail, or private landowner record is included."
  - "This document changes no source, connector, contract, schema, policy, fixture, validator, workflow, evidence object, lifecycle object, review, release record, deployment, promotion, rollback execution, publication, or repository setting."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Runbooks — Operational Procedure and Sensitive-Domain Boundary

> **Start here for Archaeology no-network validation, source-refresh planning, promotion-readiness assessment, rollback-candidate preparation, synthetic recovery rehearsal, and governed handoff.** This directory explains how an authorized actor should proceed; it does not grant cultural authority, source admission, evidence closure, policy approval, review authority, release authority, or public permission.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![Procedure files: 4](https://img.shields.io/badge/procedure%20files-4-0969da?style=flat-square)](#direct-child-map)
[![Substantive no-network profiles: 3](https://img.shields.io/badge/no--network%20profiles-3-1f883d?style=flat-square)](#current-repository-state)
[![Operational promotion and rollback: HOLD](https://img.shields.io/badge/operational%20transitions-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Exact location: denied](https://img.shields.io/badge/exact%20location-denied-b42318?style=flat-square)](#archaeology-specific-safety-rules)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Runbooks are instruction and handoff surfaces, not authority surfaces.** A runbook may cite a `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `ValidationReport`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard`. It cannot create, approve, replace, or execute those objects by prose alone.

> [!CAUTION]
> **This lane has mixed maturity.** The no-network, promotion, and rollback runbooks have been reconciled against repository evidence, but each proves only a bounded fixture, readiness, candidate-preparation, or synthetic-rehearsal profile. The source-refresh runbook still contains proposal-era paths, roles, commands, source families, and no-mounted-repository assumptions. Treat it as planning guidance until it receives its own repository-grounded reconciliation.

> [!WARNING]
> **Do not put sensitive Archaeology content in public operational artifacts.** Exact or reverse-engineerable site geometry, burial or human-remains context, sacred or culturally restricted knowledge, oral-history substance, consent secrets, collection-security detail, looting-risk detail, and private landowner information do not belong in public runbooks, issues, pull requests, fixtures, test names, logs, workflow summaries, screenshots, exports, or generated text.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Placement](#placement-and-canonical-relationship) · [State](#current-repository-state) · [Children](#direct-child-map) · [Start here](#start-here) · [Lifecycle](#lifecycle-and-state-separation) · [Boundaries](#what-belongs-here) · [Inputs and outputs](#inputs-outputs-and-permitted-actors) · [Safety](#archaeology-specific-safety-rules) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Procedure](#how-to-use-this-lane) · [Validation](#validation-and-rehearsal-boundary) · [Maintenance](#maintenance-review-and-correction-triggers) · [Open work](#open-verification-backlog) · [Related](#related-surfaces) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

<a id="purpose"></a>

## Purpose

`docs/runbooks/archaeology/` is the Archaeology and Cultural Heritage domain lane inside KFM's human-readable operational-procedure root. It helps maintainers, reviewers, stewards, developers, and operators answer bounded questions such as:

- Which procedure applies to the present validation, refresh, promotion, correction, withdrawal, rollback, or recovery state?
- Is the named procedure repository-grounded, fixture-backed, CI-wired, planning-only, held, or unverified?
- Which source identity, rights, sensitivity, cultural or sovereignty review, evidence, policy, validation, release, correction, and rollback prerequisites must close before an action may continue?
- Which operation belongs to a validator, policy engine, source registry, lifecycle store, release plane, or accountable human authority rather than Markdown?
- What must remain withheld from public artifacts even when a synthetic test, schema check, or map rendering succeeds?
- Which finite result requires continuation, quarantine, abstention, denial, escalation, correction, or a governed hold?
- Which records must remain inspectable after a correction, withdrawal, synthetic rehearsal, or authorized rollback?

The directory is documentation-first. Executable behavior and trust-bearing objects remain in their owning responsibility roots. These runbooks should make the governed path usable without embedding a second source registry, contract system, schema authority, policy engine, cultural-review authority, evidence store, release plane, or publication mechanism in documentation.

[Back to top](#top)

---

<a id="authority-and-negative-authority"></a>

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md). The adopted rules place human operational procedures under `docs/runbooks/` and require README boundaries to explain ownership, inheritance, exposure, mutation, lifecycle behavior, and non-effects without creating parallel authority.

| Concern | Owning authority | This directory's role |
|---|---|---|
| Documentation placement and inheritance | Accepted Directory Rules plus the parent [`docs/runbooks/` contract](../README.md) | Define the Archaeology procedure boundary and disclose drift |
| Archaeology domain meaning | [`docs/domains/archaeology/`](../../domains/archaeology/) plus accepted semantic contracts | Orient readers; do not redefine the domain |
| Object meaning | `contracts/` | Cite semantics; do not restate a competing contract |
| Machine shape | `schemas/` | Cite versions and required fields; do not host schema authority |
| Allow, deny, restrict, hold, or abstain | `policy/` plus required accountable review | Explain how to obtain and respond to a decision |
| Cultural, sovereignty, rights-holder, and consent authority | Verified human and institutional authority records | Require the appropriate decision; do not infer or appoint authority |
| Source identity and admission | `SourceDescriptor` and source-registry authorities | Describe safe handling; do not admit or activate a source |
| Evidence and citations | `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | Require support; do not manufacture evidence |
| Executable behavior | `tools/`, `pipelines/`, `connectors/`, packages, applications, runtime, and workflows according to role | Point to reviewed entry points and interpret bounded outcomes |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe a transition; do not perform one by file movement |
| Promotion, release, correction, withdrawal, rollback | `release/` and linked accountability objects | Explain preparation and handoff; do not approve or execute |
| Public delivery | Governed APIs and released public-safe carriers | State the public boundary; do not expose internal or unreleased stores |
| This README | Human navigation, inheritance, maturity disclosure, safety posture, and maintenance contract | No source, evidence, policy, cultural-review, release, deployment, promotion, rollback-execution, or publication authority |

A procedure must stop when its named identity, authority, permission, evidence, policy, review, release decision, correction path, or rollback target is unresolved. A README cannot convert `UNKNOWN`, `NEEDS VERIFICATION`, `CONFLICTED`, or `HOLD` into permission.

[Back to top](#top)

---

<a id="placement-and-canonical-relationship"></a>

## Placement and canonical relationship

**Placement outcome: `PLACE` — CONFIRMED for this same-path additive update.**

| Property | Current result |
|---|---|
| Path | `docs/runbooks/archaeology/README.md` |
| Owning root | `docs/` — human-readable operational documentation |
| Scope | Archaeology and Cultural Heritage domain runbook lane |
| Prior path state | Existing tracked one-byte file at blob `8b137891…` |
| Structural effect | None; no create, move, rename, split, mirror, compatibility lane, or delete |
| Authority effect | None; documents current boundaries and evidence |
| GitHub review route | `@bartytime4life` through the repository default CODEOWNERS rule |
| Accountable and independent stewardship | `NEEDS VERIFICATION` |
| Release and publication effect | None |

This README is the local boundary for the procedure files in this directory. The separate [`docs/domains/archaeology/runbooks/README.md`](../../domains/archaeology/runbooks/README.md) is retained as domain-dossier lineage and orientation. It describes this canonical lane but remains physically located under the domain dossier and contains proposal-era ownership, sensitivity, placement, and planned-runbook statements. It does not become a second writable operational-procedure authority. Its sibling [`rollback-drill.md`](../../domains/archaeology/runbooks/rollback-drill.md) is likewise domain-side planning and rehearsal lineage; current executable synthetic rollback evidence remains owned by the tools, tests, workflow, and canonical rollback runbook that actually describe it.

When these surfaces disagree, use the current procedure files in this lane for their bounded operational-description claims, subject to higher accepted doctrine, contracts, schemas, policy, evidence, cultural and sovereignty review, release, correction, and rollback authorities. Reconcile the domain-side copies through a separate no-loss migration or correction; do not silently delete or treat them as equivalent authorities.

The parent [`docs/runbooks/README.md`](../README.md) retains a repository-wide inventory snapshot pinned to an earlier commit. Its historical statement that no direct domain lane had a populated boundary README predates this completion and should be refreshed only through a later full inventory reconciliation.

[Back to top](#top)

---

<a id="current-repository-state"></a>

## Current repository state

The observations below are pinned to `main@f83c290dd7b6ed2e86262a1b483b76c60de350e6`. They describe tracked bytes and bounded executable evidence. They do not establish live-source operation, operational admission, authenticated cultural authority, release readiness, deployment, or publication.

| Surface | CONFIRMED evidence at the pinned revision | Bounded conclusion |
|---|---|---|
| This README | Existing tracked file contained only a newline | Local lane boundary was absent in substance |
| Direct procedure packet | Four tracked procedure files plus this README | The canonical lane has a stable four-procedure documentation packet |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Repository-grounded v0.2 draft; three substantive synthetic profiles; one profile wired to dedicated CI; direct domain suite remains placeholder-heavy | Useful for the named deterministic checks only; broad Archaeology validation, proof, and release remain `HOLD` |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Repository-grounded v2.0 draft; bounded A–G readiness validator; inactive promotion and domain policy; empty candidate lane; exact-location ADR candidate remains proposed | May prepare and classify readiness; cannot promote, release, deploy, or publish |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Repository-grounded v0.2 draft; generic `RollbackCard` candidate profile; synthetic-workspace rehearsal helper and tests; Archaeology-domain schema stub remains conflicted | Candidate validation and synthetic rehearsal exist; operational rollback and public invalidation remain `HOLD` |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Proposal-era v0.1 draft with placeholder roles, proposed source families, unverified paths and commands, and no-mounted-repository assumptions | Planning reference only; no source is admitted, activated, scheduled, fetched, transformed, or published by this file |
| [`domain-archaeology`](../../../.github/workflows/domain-archaeology.yml) | Read-only pull-request/main workflow; one substantive Three-Dimensional Documentation fixture profile; explicit proof and release-dry-run hold jobs | Workflow presence is bounded orchestration evidence, not Archaeology truth, cultural authority, policy approval, release, or publication |
| Domain-side runbook folder | Orientation README and rollback-drill lineage exist under `docs/domains/archaeology/runbooks/` | Presence is not a second canonical procedure authority or production recovery proof |
| CODEOWNERS | Default GitHub review route is `@bartytime4life`; an explicit sensitive-domain route covers `docs/domains/archaeology/`, not this nested canonical runbook lane | Review routing exists; accountable stewardship, rights-holder representation, and independent approval remain unverified |
| Live sources, operational promotion, operational rollback, deployment, publication | Not established by this directory | `UNKNOWN` or `HOLD` until owning surfaces provide exact-revision evidence |

### Bounded executable profiles currently documented

The no-network runbook identifies three substantive, synthetic, coordinate-free profiles:

1. Archaeological Volume Measurement Assessment.
2. Three-Dimensional Documentation paradata validation.
3. Three-Dimensional Visibility Assumption Disclosure.

Only the Three-Dimensional Documentation profile is wired into the dedicated Archaeology workflow at the pinned revision. The other two have paired contracts, schemas, fixture manifests, validators, and unit tests but remain outside that dedicated job.

The rollback runbook separately identifies a generic `RollbackCard` candidate validator and a marker-protected synthetic-workspace rehearsal. Those checks are not equivalent to live rollback authority, production alias mutation, public carrier invalidation, external cache invalidation, correction publication, or release transition.

[Back to top](#top)

---

<a id="direct-child-map"></a>

## Direct-child map

Directory Rules require a lane README to show the directory it governs and its direct children, not a speculative repository tree.

```text
docs/runbooks/archaeology/
├── README.md
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── ROLBACK_RUNBOOK.md
└── SOURCE_REFRESH_RUNBOOK.md
```

| Child | Primary question | Current documentation posture | Use boundary |
|---|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Which Archaeology checks can run deterministically without network or sensitive payload access, and what do their outcomes prove? | `CONFIRMED` repository-grounded v0.2 draft | Use only for the named synthetic profiles and declared commands |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | How should an admitted source vintage be refreshed through the lifecycle? | `NEEDS VERIFICATION`; proposal-era v0.1 draft | Do not use to admit, activate, schedule, fetch, or publish a live source |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Which evidence, policy, cultural-review, sensitivity, release, correction, and rollback gates must close before accountable release review? | `CONFIRMED` repository-grounded v2.0 draft with explicit holds | Use for readiness preparation; do not translate readiness into promotion or publication |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | How should a suspected release defect be classified, a candidate card prepared, and a synthetic rehearsal run safely? | `CONFIRMED` repository-grounded v0.2 draft | Use for candidate preparation and synthetic rehearsal only; operational rollback remains held |

[Back to top](#top)

---

<a id="start-here"></a>

## Start here

Select the narrowest procedure that matches the work. Do not chain all four merely because they share a directory.

| Situation | Start with | Required companion or stop |
|---|---|---|
| Reproduce one of the named synthetic Archaeology validator profiles | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Stop at the declared fixture result; do not infer site truth, cultural authority, or public permission |
| Investigate why a synthetic fixture produced `PASS`, `ABSTAIN`, `DENY`, or `ERROR` | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Preserve test revision, profile, fixture identity, and public-safe failure output |
| Plan a refresh of an already-admitted source | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | `HOLD` before live work until paths, source descriptor, rights, cadence, policy, operators, and commands are reverified |
| Evaluate a public-safe candidate for accountable release review | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Require bounded A–G support plus separate evidence, policy, cultural/sensitivity review, release, correction, and rollback closure |
| Suspect that a released Archaeology carrier or claim is defective | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Classify without sensitive detail; prepare a candidate card and governed handoff |
| Rehearse rollback mechanics in a temporary synthetic root | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Preserve marker guards; never point the helper at real repository, release, cache, storage, or deployment paths |
| Correct or withdraw public state | Owning `release/` correction and withdrawal procedures, using the rollback runbook for preparation | A runbook alone cannot mutate public state |
| Respond to a suspected exact-location or protected-knowledge leak | Restricted incident and sensitivity escalation path | Do not place the sensitive detail in a public issue, PR, log, or screenshot |
| Decide who has cultural, sovereignty, rights-holder, policy, or release authority | Governance and verified authority records | Never infer authority from CODEOWNERS, file authorship, a generic review, or absence of objection |
| Publish an Archaeology map, 3D scene, export, search result, AI answer, or API response | Governed release and public-delivery authorities | No direct path from this directory to publication |

[Back to top](#top)

---

<a id="lifecycle-and-state-separation"></a>

## Lifecycle and state separation

The canonical lifecycle remains:

```text
SOURCE EDGE
  -> admission decision
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLETS
  -> accountable release decision
  -> PUBLISHED public-safe carrier
  -> correction / withdrawal / rollback / recompile
```

Promotion is a governed state transition, not a file move, command exit code, commit, pull request, merge, badge, manifest-shaped document, map toggle, or successful rehearsal.

### Do not collapse these states

| State axis | Example | What it cannot prove |
|---|---|---|
| File presence | A runbook or schema is tracked | Correctness, acceptance, or operational admission |
| Documentation state | Proposal-era, repository-grounded, corrected, or stale at a pinned revision | Executable behavior or authority |
| Fixture state | Synthetic case exists | Real-world truth, source authority, or consent |
| Validator state | A declared profile returns a finite outcome | Cultural review, policy approval, evidence closure, or release |
| Workflow state | Exact-head job succeeds | Independent review, source activation, promotion, deployment, or publication |
| Candidate state | A card or dossier is shape-valid | Decision authority or applied transition |
| Evidence state | `EvidenceRef` resolves to an admissible `EvidenceBundle` | Policy permission or cultural authority |
| Review state | A scoped review record exists | Release unless the release profile explicitly grants that effect |
| Readiness state | Bounded A–G packet produces `APPROVE_READY` | Promotion, release, deployment, or publication |
| Synthetic rehearsal state | Temporary marked workspace behaves deterministically | Production rollback or public invalidation |
| Release state | Accountable authority approves an immutable release | Deployment or exposure unless separately applied |
| Publication state | A governed public-safe carrier is exposed | Truth beyond its evidence, scope, time, policy, and correction lineage |

### Object-family separation

Receipts, proofs, evidence bundles, policy decisions, review records, promotion decisions, release manifests, correction notices, withdrawal notices, rollback cards, redaction or representation receipts, catalogs, and published carriers remain distinct. A convenient JSON shape or shared identifier must not collapse their responsibilities.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

This lane should contain human-readable procedures that are specific to Archaeology operations and that depend on shared KFM authorities without replacing them.

### Belongs

- This local boundary README.
- Deterministic no-network test instructions for accepted synthetic profiles.
- Source-refresh procedure after source admission and current-path verification.
- Promotion-readiness preparation and stop conditions.
- Rollback-candidate preparation, synthetic rehearsal, correction/withdrawal handoff, and public-safe incident guidance.
- Archaeology-specific sensitivity, cultural-review, source-role, candidate-versus-confirmed, and cross-carrier exposure checkpoints.
- Exact commands only when they are tied to current repository files and bounded validation claims.
- Finite result interpretation, escalation, audit keys, correction paths, and documentation rollback.

### Does not belong

- Source payloads, exact coordinates, site identifiers, burial or human-remains records, sacred-site detail, oral-history transcripts, consent tokens, cultural-review substance, private landowner data, collection-security detail, or looting-risk detail.
- Normative object semantics, JSON Schema, Rego policy, redaction profiles, source registry entries, fixtures, validator implementation, tests, pipeline code, connectors, lifecycle instances, evidence bundles, proofs, review records, release decisions, or published artifacts.
- Universal public-geometry thresholds or transformation parameters chosen by documentation.
- Credentials, private endpoints, signed URLs, operational secrets, or access instructions for restricted systems.
- A second copy of shared doctrine, contracts, schemas, policy, or release semantics.
- Generated text presented as cultural authority, site confirmation, or root truth.
- A direct public path to `RAW`, `WORK`, `QUARANTINE`, candidates, proof internals, restricted stores, or model runtimes.
- A procedure that silently converts a candidate anomaly, model output, remote-sensing feature, or 3D reconstruction into a confirmed archaeological site or interpretation.

[Back to top](#top)

---

<a id="inputs-outputs-and-permitted-actors"></a>

## Inputs, outputs, and permitted actors

### Inputs

A procedure may begin only with the minimum inputs appropriate to its scope:

| Input class | Minimum requirement |
|---|---|
| Repository identity | Exact repository, base/head revision, target path, and current file bytes |
| Procedure identity | Runbook version, declared profile, current command or handoff path |
| Source identity | Current admitted `SourceDescriptor`, source role, rights, sensitivity, cadence, citation, and content identity where live-source work is requested |
| Evidence | Resolvable support and limitations appropriate to the claim or candidate |
| Policy | Accepted profile, evaluator identity, normalized outcome, and obligations where policy is required |
| Cultural, sovereignty, rights-holder, or consent review | Verified scope and authority record appropriate to the material and audience |
| Validation | Named validator or test profile, fixture identity, expected finite outcomes, and revision |
| Release support | Candidate identity, review state, correction path, invalidation plan, and rollback target where public state is implicated |
| Environment | Approved no-network, synthetic, review, or operational environment; least privilege; public-safe logs |
| Actor | Authenticated operator or reviewer acting within a verified responsibility assignment |

Missing a required input produces `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` according to the owning contract. It does not produce an implied default allow.

### Outputs

A procedure should emit only the records its owning authority defines. Examples include:

- a public-safe run record;
- a fixture or validator result;
- a `ValidationReport`;
- a review request or escalation record;
- a candidate `RollbackCard`;
- a correction, withdrawal, or release handoff packet;
- a rollback target reference;
- a documentation drift or verification item.

The output must state its authority limit. A test result is not evidence authority; a candidate card is not a rollback decision; a handoff is not approval; a receipt is not proof; a merge is not publication.

### Permitted actors and role discipline

The only verified GitHub route in current repository evidence is `@bartytime4life`. Functional roles remain assignments to verify, not identities to invent:

- Archaeology domain steward.
- Source and evidence steward.
- Cultural, sovereignty, rights-holder, consent, or community reviewer.
- Sensitivity and reverse-inference reviewer.
- Policy steward.
- Validation and fixture steward.
- Independent reviewer where materiality requires separation.
- Release authority.
- Correction and rollback steward.
- Operator for the named environment.

When required authority or separation cannot be established, use `HOLD`. Do not lower the review burden to fit available staffing, and do not treat CODEOWNERS routing as cultural, sovereignty, policy, or release authority.

[Back to top](#top)

---

<a id="archaeology-specific-safety-rules"></a>

## Archaeology-specific safety rules

Archaeology is deny-by-default where disclosure can harm sites, communities, cultural interests, human remains, collections, landholders, or future stewardship. These rules apply across documents, data, code, maps, APIs, search, graphs, AI, logs, caches, exports, and 3D products.

### 1. Location protection is cross-carrier

Removing a coordinate column is not enough. A protected place can be narrowed through:

- tile boundaries, clipping artifacts, centroids, labels, feature IDs, source-layer names, or zoom behavior;
- joins with parcels, roads, hydrology, geology, LiDAR, imagery, collections, or survey coverage;
- search facets, counts, graph edges, timestamps, cache keys, screenshots, errors, or downloadable files;
- camera paths, terrain, point clouds, meshes, textures, 3D scenes, or representation metadata;
- model explanations, summaries, refusals, or repeated queries.

Review the combined public surface, not one field in isolation. Styling, hidden layers, client-side filters, and coarse default zoom are not security transforms.

### 2. Cultural and sovereignty authority cannot be inferred

File ownership, agency publication, generic consent, a public URL, or absence of objection does not establish authority to disclose culturally restricted knowledge. Use the scoped review and rights-holder process required by the material. Keep the substantive review record outside public runbook prose.

### 3. Human remains, burials, sacred places, and restricted knowledge fail closed

No public operational document may imply that a generic transform automatically makes these categories releasable. Where policy or authority is unresolved, deny or hold exposure. Do not publish the protective transform parameters in a way that enables reversal or targeting.

### 4. Candidate and confirmed states remain distinct

Remote-sensing anomalies, LiDAR features, geophysical signals, model classifications, 3D interpretations, historical-map hints, and AI suggestions are candidates or interpretations until evidence and review support a more specific status. A validator may check paradata or assumptions without confirming the underlying archaeology.

### 5. Representation is a claim

A map, 3D scene, reconstruction, volume estimate, visibility analysis, chronology, or generalized geometry carries interpretive and evidentiary implications. Preserve source role, method, uncertainty, scale, time, limitations, and representation lineage. Derived products never overwrite or masquerade as source evidence.

### 6. Rights and terms are checked per source and per use

Public availability does not settle redistribution, derivative-display, model-training, commercial-use, attribution, embargo, or culturally appropriate use. Unknown terms route to quarantine or hold.

### 7. AI remains evidence-subordinate

AI may summarize already governed, released evidence or draft public-safe review notes. It does not decide site identity, affiliation, cultural authority, consent, sensitivity, policy, release, or exact-location disclosure. No direct browser-to-model path bypasses the governed API and evidence boundary.

### 8. Emergency and law-enforcement implications are outside normal public guidance

KFM runbooks do not direct field response, enforcement, excavation, recovery, access, or emergency operations. Redirect to the accountable authority and preserve a public-safe audit trail.

[Back to top](#top)

---

<a id="finite-outcomes-and-stop-conditions"></a>

## Finite outcomes and stop conditions

Use the outcome vocabulary owned by the operation. Do not collapse validator, workflow, runtime, review, and release states into one status word.

### Outcome matrix

| Context | Finite outcomes | Interpretation |
|---|---|---|
| Bounded Archaeology fixture validators | `PASS`, `ABSTAIN`, `DENY`, `ERROR` | Result for the named synthetic profile only |
| Readiness or work coordination | `PASS`, `HOLD`, `FAIL`, `ERROR` as declared by the owning procedure | `PASS` may mean ready for a next review step, not public approval |
| Governed outward response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Public-safe response envelope; evidence and policy still govern |
| Review | pending, approved, changes requested, rejected, expired, conflicted, or equivalent accepted vocabulary | Review state only |
| Promotion and release | Candidate and decision states defined by accepted release contracts | Separate from validation and merge |
| Correction and rollback | Candidate, approved, applied, failed, superseded, withdrawn, or equivalent accepted vocabulary | Separate authority and execution records |

### Hard stop conditions

Stop, retain state, and create a public-safe handoff when any of these is true:

1. Exact or reverse-engineerable protected location or restricted knowledge appears in a public artifact, log, fixture, or review surface.
2. Source identity, source role, rights, terms, sensitivity, citation, time, or content identity is missing or stale.
3. Cultural, sovereignty, rights-holder, consent, or required independent authority is absent, expired, conflicted, or unverifiable.
4. A candidate anomaly, modeled feature, or reconstruction is being presented as a confirmed site or observation.
5. `EvidenceRef` cannot resolve to support appropriate to the consequential claim.
6. The accepted policy profile, evaluator, obligations, or consumer binding is missing.
7. A runbook path, command, schema, fixture, validator, workflow, or release object named by a proposal-era document does not match current repository evidence.
8. A public client would read `RAW`, `WORK`, `QUARANTINE`, candidate, restricted, proof-internal, or direct-model state.
9. A public-safe transform has no attributable profile, receipt, review, or reverse-inference assessment.
10. A correction, withdrawal, invalidation, or rollback target is missing where public state may change.
11. The requested operation would weaken a synthetic-workspace marker, no-network guard, least-privilege permission, or fail-closed test.
12. The same path or behavior is owned by overlapping active work and no survivor or dependency order is established.
13. A workflow or command would expose secrets, restricted payloads, or protected details through output.
14. Repository, base/head identity, target bytes, or review scope drifted after preflight.
15. The operator cannot state what the result proves and what remains unproved.

### Escalation record

A public escalation record should include only:

- stable task or incident ID;
- affected public-safe artifact or claim reference;
- category-level reason code;
- current hold or denial state;
- accountable review roles required;
- evidence and policy references safe to expose;
- correction or rollback target reference where available;
- next verification step;
- timestamp and repository revision.

Never include the sensitive detail that caused the escalation.

[Back to top](#top)

---

<a id="how-to-use-this-lane"></a>

## How to use this lane

### Step 1 — Freeze identity and scope

Record the exact repository, base/head SHA, target procedure, current blob, requested action, permitted environment, actor class, and non-goals. Search current pull requests and branches for the same path or behavior.

### Step 2 — Classify procedure maturity

Read the child runbook metadata and current repository companions. Determine whether the needed path is:

- repository-grounded and fixture-backed;
- repository-grounded but held beyond a bounded readiness profile;
- proposal-era and requiring reconciliation;
- conflicted with another schema, policy, or authority surface; or
- unknown.

Do not skip this step because the file is long or contains commands.

### Step 3 — Resolve authority and sensitivity before payload access

Confirm source admission, rights, sensitivity, cultural or sovereignty review, operator permission, and environment. For no-network work, use only the named synthetic fixtures. For public review, expose only minimum-necessary public-safe metadata.

### Step 4 — Run the narrowest valid procedure

Use the exact current command and fixture profile from the repository-grounded child. Do not substitute a nearby command, invent an aggregate target, broaden a fixture into a live source, or copy a synthetic helper into production use.

### Step 5 — Interpret the result within its boundary

Record revision, profile, inputs, finite outcome, output digest where applicable, and limitations. A green result proves only its declared scope.

### Step 6 — Hand off rather than self-authorize

When the next transition requires evidence, policy, cultural review, independent review, release, correction, withdrawal, or rollback authority, create the appropriate handoff. Do not manufacture an approval from file presence or operator confidence.

### Step 7 — Preserve correction and rollback lineage

Keep the prior state, reason, target, invalidation scope, and public-safe audit record. Do not erase a sensitive incident from history by silently rewriting documentation; use the appropriate restricted record plus public-safe correction or tombstone.

[Back to top](#top)

---

<a id="validation-and-rehearsal-boundary"></a>

## Validation and rehearsal boundary

### Documentation validation

A change to this lane should verify:

- one valid `KFM_META_BLOCK_V2` where required;
- one H1 and stable navigation;
- balanced fences, valid tables, supported GitHub alerts, UTF-8, LF endings, and final newline;
- repository-relative links and current path identities;
- claim labels and evidence snapshot;
- direct-child inventory;
- no sensitive records, protected coordinates, consent secrets, credentials, private endpoints, or harmful transform detail;
- no invented owners, source admission, policy activation, review, release, deployment, or publication state;
- no silent authority duplication or path migration;
- reversible diff and explicit rollback.

### Executable validation

Use current repository-native commands from the child runbook. At this checkpoint:

- the no-network runbook documents three substantive synthetic profiles;
- the dedicated domain workflow executes one of those profiles;
- the promotion runbook documents a bounded A–G readiness validator but keeps policy, candidate, proof, release, and transition authority separate;
- the rollback runbook documents candidate validation and marker-protected synthetic rehearsal, while operational rollback remains held;
- the source-refresh runbook does not establish a current executable live-source path.

### Workflow interpretation

A hosted result must belong to the exact head SHA and relevant event before it is cited. Distinguish:

- completed success;
- expected or explicit skip/hold;
- pending or queued;
- cancellation;
- introduced failure;
- inherited or unrelated failure;
- not run.

A green workflow does not authenticate cultural authority, prove independent review, admit a source, create an EvidenceBundle, approve policy, promote lifecycle state, release, deploy, or publish.

### Rehearsal safety

Synthetic rollback rehearsal is permitted only in the marker-protected temporary workspace described by the current rollback runbook and helper. Do not weaken the marker or `synthetic: true` checks. No current evidence authorizes pointing that helper at real `data/`, `release/`, storage, cache, deployment, or public paths.

[Back to top](#top)

---

<a id="maintenance-review-and-correction-triggers"></a>

## Maintenance, review, and correction triggers

Update this README or a child procedure when any of the following changes materially:

- a child runbook is added, removed, renamed, moved, superseded, or reconciled;
- the source-refresh runbook gains verified repository paths and executable commands;
- a substantive Archaeology validator profile is added, removed, or wired into CI;
- proof or release hold jobs graduate or change their exact boundary;
- an Archaeology candidate dossier, accepted policy profile, evaluator binding, release dry run, or transition executor appears;
- `RollbackCard` authority, schema selection, validator behavior, rehearsal guard, or operational rollback support changes;
- cultural, sovereignty, rights-holder, consent, sensitivity, exact-location, representation, or reverse-inference policy changes;
- Directory Rules, ADRs, canonical path decisions, CODEOWNERS routing, or stewardship assignments change;
- public API, map, 3D, search, graph, export, Evidence Drawer, Focus Mode, cache, or model surfaces change;
- a correction, withdrawal, rollback, sensitivity incident, or public exposure reveals a missing procedure;
- repository topology or parent/domain indexes become stale relative to this lane.

### Review burden

At minimum, changes need the verified GitHub review route. Changes that alter sensitive-domain procedure semantics also require the applicable accountable roles, which remain `NEEDS VERIFICATION`. The author or generator must not be treated as the sole approver for policy-significant work.

### Correction posture

Correct documentation through a reviewable commit or forward fix. Preserve the prior bytes, reason, evidence, and changed-path scope. A documentation correction does not correct a separately released public artifact; public correction, withdrawal, invalidation, and rollback follow their owning procedures.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

| Item | Current status | Evidence needed before closure |
|---|---|---|
| Accountable Archaeology steward | `UNKNOWN / NEEDS VERIFICATION` | Verified responsibility assignment and scope |
| Cultural, sovereignty, rights-holder, consent, and community review routes | `UNKNOWN / HOLD` | Named accountable authorities, authority intervals, scope, confidentiality, and revocation process |
| Independent review capacity | `UNKNOWN / HOLD` where required | Verified reviewer route separate from author/generator and release authority |
| Source-refresh modernization | `NEEDS VERIFICATION` | Current source registry, contracts, paths, commands, rights, cadence, fixtures, workflow, and rollback evidence |
| Live Archaeology source admission | `UNKNOWN / HOLD` | Accepted source descriptors, rights, policy, activation decisions, and receipts |
| Broad direct-domain test suite | `PARTIAL / HOLD` | Replace placeholder and vacuous modules with substantive, negative, no-network proof |
| Dedicated CI coverage for all three substantive no-network profiles | `PARTIAL` | Deliberate workflow wiring and exact-head results |
| EvidenceBundle and proof closure | `HOLD` | Accepted producer, resolver, fixtures, proof schema, validation, policy, review, correction, and rollback |
| Archaeology policy bundle and evaluator | `HOLD` | Accepted policy, input profile, evaluator binding, obligations, negative fixtures, and governed consumer |
| Candidate dossier and release dry run | `HOLD` | Immutable candidate, evidence, policy, review, proof, manifest, correction, and rollback support |
| Exact-location and public-safe transform decision | `PROPOSED / HOLD` | Accepted policy/ADR and accountable sensitivity, cultural, and rights-holder review; no reversible disclosure |
| Operational rollback | `HOLD` | Authenticated actor, selected schema/contract authority, production-safe executor, alias/carrier/cache invalidation, rehearsal evidence, correction, and release authority |
| Archaeology-domain rollback schema conflict | `CONFLICTED` | Accepted convergence or supersession decision relative to the generic release profile |
| Domain-side runbook orientation and rollback-drill lineage | `NEEDS VERIFICATION / CONFLICTED` | No-loss reconciliation with the canonical procedure lane and current executable evidence |
| Parent runbook inventory | `STALE / NEEDS VERIFICATION` | Full current subtree recomputation rather than one-row editing |
| CODEOWNERS and steward alignment | `PARTIAL` | Explicit path route where desired plus independent authority assignments; routing alone remains non-authoritative |
| Public API, UI, map, 3D, search, graph, export, Focus Mode, and AI parity | `UNKNOWN / HOLD` | Governed interface tests showing no sensitive leakage, evidence closure, policy enforcement, correction, and rollback |
| Deployment and publication state | `UNKNOWN` | Current runtime, release, deployment, public endpoint, and monitoring evidence |

This README must not close these items by assertion. Each requires its owning evidence and reviewed state transition.

[Back to top](#top)

---

<a id="related-surfaces"></a>

## Related surfaces

### Governing documentation

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted adoption decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- Deny-by-default proposal lineage: [`ADR-0010`](../../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md)

### Archaeology domain context

- Domain README: [`docs/domains/archaeology/README.md`](../../domains/archaeology/README.md)
- Architecture: [`ARCHITECTURE.md`](../../domains/archaeology/ARCHITECTURE.md)
- Data lifecycle: [`DATA_LIFECYCLE.md`](../../domains/archaeology/DATA_LIFECYCLE.md)
- Sensitivity catalogue: [`SENSITIVITY.md`](../../domains/archaeology/SENSITIVITY.md)
- Cultural review: [`CULTURAL_REVIEW.md`](../../domains/archaeology/CULTURAL_REVIEW.md)
- Publication and policy: [`PUBLICATION_AND_POLICY.md`](../../domains/archaeology/PUBLICATION_AND_POLICY.md)
- Release index: [`RELEASE_INDEX.md`](../../domains/archaeology/RELEASE_INDEX.md)
- Verification backlog: [`VERIFICATION_BACKLOG.md`](../../domains/archaeology/VERIFICATION_BACKLOG.md)
- Domain-side runbook orientation: [`docs/domains/archaeology/runbooks/README.md`](../../domains/archaeology/runbooks/README.md)
- Domain-side rollback-drill lineage: [`rollback-drill.md`](../../domains/archaeology/runbooks/rollback-drill.md)

### Semantic, machine, policy, fixture, and proof boundaries

- Archaeology contracts index: [`contracts/domains/archaeology/README.md`](../../../contracts/domains/archaeology/README.md)
- Archaeology schemas index: [`schemas/contracts/v1/domains/archaeology/README.md`](../../../schemas/contracts/v1/domains/archaeology/README.md)
- Archaeology fixture boundary: [`fixtures/domains/archaeology/README.md`](../../../fixtures/domains/archaeology/README.md)
- Archaeology policy boundary: [`policy/domains/archaeology/README.md`](../../../policy/domains/archaeology/README.md)
- Archaeology tests index: [`tests/domains/archaeology/README.md`](../../../tests/domains/archaeology/README.md)
- Archaeology validators index: [`tools/validators/domains/archaeology/README.md`](../../../tools/validators/domains/archaeology/README.md)
- Archaeology proof boundary: [`data/proofs/archaeology/README.md`](../../../data/proofs/archaeology/README.md)
- Archaeology candidate boundary: [`release/candidates/archaeology/README.md`](../../../release/candidates/archaeology/README.md)

### Automation and review routing

- Dedicated domain workflow: [`.github/workflows/domain-archaeology.yml`](../../../.github/workflows/domain-archaeology.yml)
- Review routing: [`.github/CODEOWNERS`](../../../.github/CODEOWNERS)

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Evidence | What it supports | What it cannot prove |
|---|---|---|
| `main@f83c290dd7b6ed2e86262a1b483b76c60de350e6` | Immutable repository checkpoint for this review | Runtime or public behavior by commit alone |
| Target prior blob `8b137891…` | The target was tracked but blank in substance | Why it was blank or whether an external consumer depended on that state |
| Direct child blobs recorded in metadata | Exact five-child inventory and current child document bytes | Live-source, cultural-review, policy, release, deployment, or publication state beyond their support |
| `NO_NETWORK_TEST_RUNBOOK.md` blob `6a57abe6…` | Three substantive synthetic profiles, one dedicated CI binding, and explicit broader holds | Archaeological truth, source authority, cultural authority, or public permission |
| `PROMOTION_RUNBOOK.md` blob `6c746a4f…` | Bounded readiness procedure and current policy/candidate/release holds | Applied promotion, release, deployment, or publication |
| `ROLLBACK_RUNBOOK.md` blob `9e59120c…` | Candidate profile, schema conflict disclosure, and synthetic-rehearsal boundary | Operational rollback, public invalidation, or release authority |
| `SOURCE_REFRESH_RUNBOOK.md` blob `c50bcf2f…` | Proposal lineage and intended source-refresh concerns | Current paths, commands, source admission, or live execution |
| `domain-archaeology.yml` blob `d51ba3b1…` | One executable no-network profile and explicit proof/release readiness holds | Broad domain correctness or public release |
| Accepted ADR-0029 and Directory Rules blob | Placement, one-owner, README inheritance, and non-authority rules | Operational approval |
| CODEOWNERS blob `dd2a84aa…` | Verified GitHub review route and explicit authority limitation | Cultural, sovereignty, rights-holder, independent-review, policy, or release authority |
| Domain-side runbook blobs | Current orientation and rollback-drill lineage | Canonical procedure authority or operational recovery proof |

Memory, generic best practice, document length, repeated proposal language, badges, and file names are not implementation evidence.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This file is documentation-only and has no source, evidence, policy, cultural-review, lifecycle, release, deployment, promotion, rollback-execution, or publication side effect.

- **Before merge:** close or abandon the draft pull request. No governed or public data state needs reversal.
- **After merge:** revert the implementation commit or submit a smaller forward-fix pull request against the actual merged head. Do not rewrite shared history.
- **If child responsibilities or links changed after merge:** prefer a forward fix that preserves one writable local boundary rather than restoring parallel or ambiguous authority.
- **Historical preimage:** blob `8b137891791fe96927ad78e64b0aad7bded08bdc` restores the exact prior one-byte file.

A Git revert of this README would not correct any separate source, sensitive record, evidence, policy, review, release, deployment, or publication state. Those transitions require their own owning correction and rollback paths.

[Back to top](#top)
