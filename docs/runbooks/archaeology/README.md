<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/archaeology/readme
title: Archaeology Runbooks — Operational Procedure and Sensitive-Domain Boundary
type: readme
subtype: domain-runbook-boundary
version: v0.1
status: draft; repository-grounded; sensitive-domain; documentation-only; non-authoritative; non-publisher
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
base_commit: b1964d5f70834195c4e7d6c2824bdc35a409b697
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
source_refresh_runbook_blob: 0166f47872b9f0f7993b0265f38cc255f870ae43
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
  - "All four direct child runbooks are now repository-grounded drafts; current executable evidence remains bounded to synthetic fixtures, readiness checks, candidate validation, and synthetic rehearsal."
  - "Live source refresh, proof construction, accepted Archaeology policy evaluation, operational promotion, operational rollback, release, deployment, and publication remain HOLD or UNKNOWN."
  - "docs/domains/archaeology/runbooks/ is retained as domain-dossier lineage and orientation. It does not become a second writable operational-procedure authority."
  - "No exact or reverse-engineerable archaeological location, burial or human-remains detail, sacred-site information, culturally restricted knowledge, consent secret, collection-security detail, or private landowner record is included."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Runbooks — Operational Procedure and Sensitive-Domain Boundary

> **Start here for Archaeology no-network validation, source-refresh preparation, promotion-readiness assessment, rollback-candidate preparation, synthetic recovery rehearsal, and governed handoff.** This directory explains how an authorized actor should proceed; it does not grant cultural authority, source admission, evidence closure, policy approval, review authority, release authority, or public permission.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-state)
[![Procedure files: 4](https://img.shields.io/badge/procedure%20files-4-0969da?style=flat-square)](#direct-child-map)
[![Substantive no-network profiles: 3](https://img.shields.io/badge/no--network%20profiles-3-1f883d?style=flat-square)](#current-repository-state)
[![Live operations: HOLD](https://img.shields.io/badge/live%20operations-HOLD-d4a72c?style=flat-square)](#current-repository-state)
[![Exact location: denied](https://img.shields.io/badge/exact%20location-denied-b42318?style=flat-square)](#archaeology-specific-safety-rules)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-and-negative-authority)

> [!IMPORTANT]
> **Runbooks are instruction and handoff surfaces, not authority surfaces.** A runbook may cite a `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `ValidationReport`, `PolicyDecision`, `ReviewRecord`, `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, or `RollbackCard`. It cannot create, approve, replace, or execute those objects by prose alone.

> [!CAUTION]
> **Repository-grounded does not mean operationally admitted.** All four child runbooks now describe current repository evidence, but the live source-refresh path, accepted Archaeology policy evaluator, proof producer, candidate release dry run, operational promotion, operational rollback, deployment, and publication remain held or unverified.

> [!WARNING]
> **Do not put sensitive Archaeology content in public operational artifacts.** Exact or reverse-engineerable site geometry, burial or human-remains context, sacred or culturally restricted knowledge, oral-history substance, consent secrets, collection-security detail, looting-risk detail, and private landowner information do not belong in public runbooks, issues, pull requests, fixtures, test names, logs, workflow summaries, screenshots, exports, or generated text.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-and-negative-authority) · [Placement](#placement-and-canonical-relationship) · [State](#current-repository-state) · [Children](#direct-child-map) · [Start here](#start-here) · [Lifecycle](#lifecycle-and-state-separation) · [Boundaries](#what-belongs-here) · [Inputs and outputs](#inputs-outputs-and-permitted-actors) · [Safety](#archaeology-specific-safety-rules) · [Outcomes](#finite-outcomes-and-stop-conditions) · [Validation](#validation-and-rehearsal-boundary) · [Maintenance](#maintenance-review-and-correction-triggers) · [Open work](#open-verification-backlog) · [Related](#related-surfaces) · [Evidence](#evidence-basis) · [Rollback](#document-change-rollback)

---

<a id="purpose"></a>

## Purpose

`docs/runbooks/archaeology/` is the Archaeology and Cultural Heritage domain lane inside KFM's human-readable operational-procedure root. It helps maintainers, reviewers, stewards, developers, and operators answer bounded questions such as:

- Which procedure applies to the present validation, refresh, promotion, correction, withdrawal, rollback, or recovery state?
- What is implemented, fixture-backed, CI-wired, held, conflicted, or still unknown?
- Which source identity, rights, sensitivity, cultural or sovereignty review, evidence, policy, validation, release, correction, and rollback prerequisites must close before an action may continue?
- What must remain withheld even when a synthetic test, schema check, map rendering, or 3D validation succeeds?
- Which finite result requires continuation, quarantine, abstention, denial, escalation, correction, or a governed hold?

Executable behavior and trust-bearing objects remain in their owning responsibility roots. These runbooks should make the governed path usable without embedding a second source registry, contract system, schema authority, policy engine, cultural-review authority, evidence store, release plane, or publication mechanism in documentation.

[Back to top](#top)

---

<a id="authority-and-negative-authority"></a>

## Authority and negative authority

Accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact Directory Rules v2 bytes at [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md). The adopted rules place human operational procedures under `docs/runbooks/` and require README boundaries to explain ownership, inheritance, exposure, mutation, lifecycle behavior, and non-effects without creating parallel authority.

| Concern | Owning authority | This directory's role |
|---|---|---|
| Documentation placement and inheritance | Accepted Directory Rules plus the parent [`docs/runbooks/` contract](../README.md) | Define the Archaeology procedure boundary and disclose drift |
| Archaeology domain meaning | [`docs/domains/archaeology/`](../../domains/archaeology/) plus accepted semantic contracts | Orient readers; do not redefine the domain |
| Object meaning and machine shape | `contracts/` and `schemas/` | Cite meaning and versions; do not host competing authority |
| Allow, deny, restrict, hold, or abstain | `policy/` plus required accountable review | Explain how to obtain and respond to a decision |
| Cultural, sovereignty, rights-holder, and consent authority | Verified human and institutional authority records | Require the appropriate decision; do not infer or appoint authority |
| Source identity and admission | `SourceDescriptor`, source registry, and admission authorities | Describe safe handling; do not admit or activate a source |
| Evidence and citations | `EvidenceRef`, `EvidenceBundle`, receipts, and proofs | Require support; do not manufacture evidence |
| Executable behavior | `tools/`, `tests/`, `fixtures/`, `pipelines/`, `connectors/`, packages, applications, runtime, and workflows | Point to reviewed entry points and interpret bounded outcomes |
| Lifecycle instances | Governed `data/` phases and accountability families | Describe a transition; do not perform one by file movement |
| Promotion, release, correction, withdrawal, rollback | `release/` and linked accountability objects | Explain preparation and handoff; do not approve or execute |
| Public delivery | Governed APIs and released public-safe carriers | State the public boundary; do not expose internal or unreleased stores |
| This README | Human navigation, maturity disclosure, safety posture, and maintenance contract | No source, evidence, policy, cultural-review, release, deployment, promotion, rollback-execution, or publication authority |

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
| GitHub review route | `@bartytime4life` through the repository default CODEOWNERS rule |
| Accountable and independent stewardship | `NEEDS VERIFICATION` |
| Release and publication effect | None |

This README is the local boundary for the procedure files in this directory. The separate [`docs/domains/archaeology/runbooks/README.md`](../../domains/archaeology/runbooks/README.md) and [`rollback-drill.md`](../../domains/archaeology/runbooks/rollback-drill.md) are retained as domain-dossier orientation and planning lineage. They do not become a second writable operational-procedure authority or production recovery proof.

When those surfaces disagree with this lane, use current repository evidence and the current child procedure for the bounded operational-description claim, subject to higher accepted doctrine, contracts, schemas, policy, evidence, cultural and sovereignty review, release, correction, and rollback authorities. Reconcile the domain-side copies through a separate no-loss migration or correction; do not silently delete them.

The parent [`docs/runbooks/README.md`](../README.md) retains a repository-wide inventory snapshot pinned to an earlier commit. Its statement that no direct domain lane had a populated boundary README predates this completion and should be refreshed only through a later full inventory reconciliation.

[Back to top](#top)

---

<a id="current-repository-state"></a>

## Current repository state

The observations below are pinned to `main@b1964d5f70834195c4e7d6c2824bdc35a409b697`. They describe tracked bytes and bounded executable evidence. They do not establish authenticated cultural authority, live source operation, operational admission, release readiness, deployment, or publication.

| Surface | CONFIRMED evidence at the pinned revision | Bounded conclusion |
|---|---|---|
| This README | Existing tracked file contained only a newline | Local lane boundary was absent in substance |
| Direct procedure packet | Four tracked procedure files plus this README | The canonical lane has a stable four-procedure documentation packet |
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Repository-grounded v0.2 draft; three substantive synthetic profiles; one profile wired to dedicated CI; direct domain suite remains placeholder-heavy | Useful for the named deterministic checks only; broad Archaeology validation, proof, and release remain `HOLD` |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | Repository-grounded v1.0.0 draft; source-authority register empty at its snapshot; source YAMLs, connector lane, pipeline specs, policy, tests, and schema surfaces remain placeholders or incomplete | Use for fail-closed preparation and review; live source execution defaults to `HOLD` |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Repository-grounded v2.0 draft; bounded A–G readiness validator; inactive promotion and domain policy; empty candidate lane; exact-location ADR candidate remains proposed | May prepare and classify readiness; cannot promote, release, deploy, or publish |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Repository-grounded v0.2 draft; generic `RollbackCard` candidate profile; synthetic-workspace rehearsal helper and tests; Archaeology-domain schema stub remains conflicted | Candidate validation and synthetic rehearsal exist; operational rollback and public invalidation remain `HOLD` |
| [`domain-archaeology`](../../../.github/workflows/domain-archaeology.yml) | Read-only pull-request/main workflow; one substantive Three-Dimensional Documentation fixture profile; explicit proof and release-dry-run hold jobs | Workflow presence is bounded orchestration evidence, not Archaeology truth, cultural authority, policy approval, release, or publication |
| Domain-side runbook folder | Orientation README and rollback-drill lineage exist under `docs/domains/archaeology/runbooks/` | Presence is not a second canonical procedure authority or production recovery proof |
| CODEOWNERS | Default GitHub review route is `@bartytime4life`; an explicit sensitive-domain route covers `docs/domains/archaeology/`, not this nested canonical runbook lane | Review routing exists; accountable stewardship, rights-holder representation, and independent approval remain unverified |
| Live source refresh, proof, accepted policy evaluation, operational promotion, operational rollback, deployment, publication | Not established by this directory | `UNKNOWN` or `HOLD` until owning surfaces provide exact-revision evidence |

### Bounded executable evidence currently documented

The no-network runbook identifies three substantive, synthetic, coordinate-free profiles:

1. Archaeological Volume Measurement Assessment.
2. Three-Dimensional Documentation paradata validation.
3. Three-Dimensional Visibility Assumption Disclosure.

Only the Three-Dimensional Documentation profile is wired into the dedicated Archaeology workflow at the pinned revision. The rollback runbook separately identifies a generic `RollbackCard` candidate validator and a marker-protected synthetic-workspace rehearsal. The promotion runbook identifies a bounded A–G readiness validator. None of these is equivalent to live cultural authority, source admission, evidence closure, policy activation, operational transition, public invalidation, release, deployment, or publication.

[Back to top](#top)

---

<a id="direct-child-map"></a>

## Direct-child map

```text
docs/runbooks/archaeology/
├── README.md
├── NO_NETWORK_TEST_RUNBOOK.md
├── PROMOTION_RUNBOOK.md
├── ROLLBACK_RUNBOOK.md
└── SOURCE_REFRESH_RUNBOOK.md
```

| Child | Primary question | Current posture | Use boundary |
|---|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Which checks can run deterministically without network or sensitive payload access? | Repository-grounded v0.2 | Named synthetic profiles only |
| [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | How should an already-admitted source vintage be refreshed? | Repository-grounded v1.0.0; live execution held | Preparation, inspection, and candidate handoff only until prerequisites close |
| [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Which gates must close before accountable release review? | Repository-grounded v2.0; policy/candidate/proof/release held | Readiness preparation only |
| [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | How should a suspected release defect be classified and rehearsed safely? | Repository-grounded v0.2; operational rollback held | Candidate preparation and synthetic rehearsal only |

[Back to top](#top)

---

<a id="start-here"></a>

## Start here

| Situation | Start with | Required boundary |
|---|---|---|
| Reproduce a named synthetic validator profile | [`NO_NETWORK_TEST_RUNBOOK.md`](./NO_NETWORK_TEST_RUNBOOK.md) | Stop at the declared fixture result; do not infer site truth or public permission |
| Prepare a refresh for an already-admitted source | [`SOURCE_REFRESH_RUNBOOK.md`](./SOURCE_REFRESH_RUNBOOK.md) | `HOLD` live retrieval until admission, rights, sensitivity, cultural review, connector, fixtures, and rollback prerequisites close |
| Evaluate a public-safe candidate for accountable release review | [`PROMOTION_RUNBOOK.md`](./PROMOTION_RUNBOOK.md) | Require separate evidence, policy, cultural/sensitivity review, release, correction, and rollback closure |
| Classify a suspected released-carrier defect | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Prepare a public-safe candidate and governed handoff; do not execute production rollback |
| Rehearse rollback mechanics | [`ROLLBACK_RUNBOOK.md`](./ROLLBACK_RUNBOOK.md) | Use only the marker-protected temporary synthetic root |
| Respond to a suspected sensitive leak | Restricted incident and sensitivity escalation path | Do not put sensitive detail in a public issue, PR, log, or screenshot |
| Publish a map, 3D scene, export, search result, API response, or AI answer | Governed release and public-delivery authorities | No direct path from this directory to publication |

[Back to top](#top)

---

<a id="lifecycle-and-state-separation"></a>

## Lifecycle and state separation

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

| State axis | Example | What it cannot prove |
|---|---|---|
| File presence | A runbook, schema, or source YAML is tracked | Acceptance or operational admission |
| Fixture or validator state | A synthetic profile returns a finite outcome | Cultural review, source authority, evidence closure, policy approval, or release |
| Workflow state | Exact-head job succeeds | Independent review, promotion, deployment, or publication |
| Readiness state | Bounded packet is ready for accountable review | Applied transition or public state |
| Synthetic rehearsal state | Marked temporary workspace behaves deterministically | Production rollback or public invalidation |
| Release state | Accountable authority approves an immutable release | Deployment unless separately applied |
| Publication state | Governed public-safe carrier is exposed | Truth beyond its evidence, scope, time, policy, and correction lineage |

Receipts, proofs, evidence bundles, policy decisions, review records, promotion decisions, release manifests, correction notices, withdrawal notices, rollback cards, redaction or representation receipts, catalogs, and published carriers remain distinct object families.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

### Belongs

- Human-readable Archaeology procedures for no-network validation, admitted-source refresh, promotion readiness, correction/withdrawal handoff, and rollback preparation or synthetic rehearsal.
- Archaeology-specific sensitivity, cultural-review, source-role, candidate-versus-confirmed, and cross-carrier exposure checkpoints.
- Exact commands only when tied to current repository files and bounded validation claims.
- Finite result interpretation, escalation, audit keys, maintenance triggers, and documentation rollback.

### Does not belong

- Source payloads, exact coordinates, site identifiers, burial or human-remains records, sacred-site detail, oral-history transcripts, consent tokens, cultural-review substance, private landowner data, collection-security detail, or looting-risk detail.
- Normative contracts, JSON Schema, Rego policy, redaction profiles, source registry entries, fixtures, validator implementation, tests, pipeline code, connectors, lifecycle instances, evidence bundles, proofs, review records, release decisions, or published artifacts.
- Credentials, private endpoints, signed URLs, operational secrets, or restricted-system access instructions.
- A direct public path to `RAW`, `WORK`, `QUARANTINE`, candidates, proof internals, restricted stores, or model runtimes.
- A procedure that converts a candidate anomaly, model output, remote-sensing feature, or 3D reconstruction into a confirmed site without evidence and review.

[Back to top](#top)

---

<a id="inputs-outputs-and-permitted-actors"></a>

## Inputs, outputs, and permitted actors

A procedure may begin only with the inputs appropriate to its scope:

| Input class | Minimum requirement |
|---|---|
| Repository identity | Exact repository, base/head revision, target path, and current bytes |
| Procedure identity | Runbook version, declared profile, current command or handoff path |
| Source identity | Admitted `SourceDescriptor`, source role, rights, sensitivity, cadence, citation, and content identity for live-source work |
| Evidence and policy | Resolvable support plus accepted policy profile, evaluator, outcome, and obligations where required |
| Cultural or sovereignty review | Verified scope and authority record appropriate to the material and audience |
| Validation | Named profile, fixture identity, expected finite outcomes, and revision |
| Release support | Candidate identity, review state, correction path, invalidation plan, and rollback target where public state is implicated |
| Actor and environment | Authenticated actor in a verified role; approved no-network, synthetic, review, or operational environment; least privilege; public-safe logs |

Missing a required input produces `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` according to the owning contract. It does not produce an implied default allow.

Expected outputs may include a public-safe run record, validation report, review request, candidate `RollbackCard`, correction or release handoff, rollback target reference, or documentation drift item. Every output must state its authority limit.

The only verified GitHub route is `@bartytime4life`. Archaeology, source/evidence, cultural/sovereignty, rights-holder, sensitivity, policy, validation, independent-review, release, correction, rollback, and operator assignments remain roles to verify—not identities to invent. When required authority or separation cannot be established, use `HOLD`.

[Back to top](#top)

---

<a id="archaeology-specific-safety-rules"></a>

## Archaeology-specific safety rules

1. **Location protection is cross-carrier.** A place can be narrowed through tiles, labels, identifiers, joins, search facets, graph edges, timestamps, caches, screenshots, errors, exports, terrain, point clouds, meshes, 3D scenes, or generated language. Styling and client-side filters are not security transforms.
2. **Cultural and sovereignty authority cannot be inferred.** File ownership, agency publication, generic consent, a public URL, or absence of objection does not establish disclosure authority.
3. **Human remains, burials, sacred places, and restricted knowledge fail closed.** No generic transform automatically makes them public-safe.
4. **Candidate and confirmed states remain distinct.** Remote-sensing anomalies, LiDAR features, geophysical signals, model classifications, historical-map hints, 3D interpretations, and AI suggestions remain candidates or interpretations until evidence and review support more.
5. **Representation is a claim.** Maps, 3D scenes, reconstructions, volume estimates, visibility analyses, chronologies, and generalized geometries must preserve source role, method, uncertainty, scale, time, limitations, and lineage.
6. **Rights and terms are checked per source and use.** Public availability does not settle redistribution, derivative-display, model-training, commercial use, attribution, embargo, or culturally appropriate use.
7. **AI remains evidence-subordinate.** AI does not decide site identity, affiliation, cultural authority, consent, sensitivity, policy, release, or exact-location disclosure.
8. **KFM is not a field-response, law-enforcement, excavation, access, or emergency authority.** Redirect to the accountable authority and preserve only a public-safe audit trail.

[Back to top](#top)

---

<a id="finite-outcomes-and-stop-conditions"></a>

## Finite outcomes and stop conditions

Use the vocabulary owned by the operation:

| Context | Finite outcomes | Boundary |
|---|---|---|
| Synthetic Archaeology validators | `PASS`, `ABSTAIN`, `DENY`, `ERROR` | Named fixture profile only |
| Source refresh | `ADMIT`, `QUARANTINE`, `DENY`, `NO_CHANGE`, `SKIP`, `RATE_LIMITED`, `ERROR`, `HOLD` | Does not imply downstream answer or release |
| Readiness/work coordination | `PASS`, `HOLD`, `FAIL`, `ERROR` as declared | `PASS` may mean ready for review only |
| Governed outward response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Evidence and policy still govern |
| Review, release, correction, rollback | Accepted family-specific states | Separate from validation and merge |

Stop and create a public-safe handoff when:

- protected location or restricted knowledge appears in a public artifact, log, fixture, or review surface;
- source identity, role, rights, terms, sensitivity, citation, time, or content identity is missing or stale;
- cultural, sovereignty, rights-holder, consent, or required independent authority is absent or conflicted;
- a candidate or reconstruction is presented as a confirmed site or observation;
- `EvidenceRef` cannot resolve to support appropriate to the claim;
- policy profile, evaluator, obligations, or consumer binding is missing;
- a named path, command, schema, fixture, validator, workflow, or release object does not match current repository evidence;
- a public client would read internal, candidate, restricted, proof-internal, or direct-model state;
- a public-safe transform lacks an attributable profile, receipt, review, or reverse-inference assessment;
- correction, invalidation, or rollback support is missing where public state may change;
- the operation would weaken a no-network or synthetic-workspace guard;
- overlapping active work has no survivor or dependency order;
- repository identity, target bytes, or review scope drifted after preflight.

Never include the sensitive detail that caused an escalation in the public escalation record.

[Back to top](#top)

---

<a id="validation-and-rehearsal-boundary"></a>

## Validation and rehearsal boundary

A documentation change should verify metadata, H1/navigation, fences, tables, alerts, UTF-8/LF/final newline, relative links, direct-child inventory, evidence labels, no sensitive records or credentials, no invented authority, and reversible scope.

Executable validation remains child-specific:

- no-network: three substantive synthetic profiles, one dedicated CI binding;
- source refresh: repository-grounded procedure, but live execution remains `HOLD`;
- promotion: bounded A–G readiness, with policy, candidate, proof, release, and transition authority separate;
- rollback: candidate validation and marker-protected synthetic rehearsal, while operational rollback remains `HOLD`.

A hosted result must belong to the exact head SHA and event before citation. A green workflow does not authenticate cultural authority, prove independent review, admit a source, create an EvidenceBundle, approve policy, promote lifecycle state, release, deploy, or publish.

Synthetic rollback rehearsal is permitted only in the marker-protected temporary workspace described by the current rollback runbook and helper. Do not point it at real `data/`, `release/`, storage, cache, deployment, or public paths.

[Back to top](#top)

---

<a id="maintenance-review-and-correction-triggers"></a>

## Maintenance, review, and correction triggers

Update this README when a child runbook, source-admission posture, validator profile, CI binding, policy profile, candidate lane, proof producer, release dry run, transition executor, rollback authority, cultural-review route, exact-location decision, public surface, or stewardship assignment changes materially.

Changes need the verified GitHub route plus applicable accountable roles. The author or generator is not the sole approver for policy-significant work. Correct documentation through a reviewable commit or forward fix; public correction, withdrawal, invalidation, and rollback follow their owning procedures.

[Back to top](#top)

---

<a id="open-verification-backlog"></a>

## Open verification backlog

| Item | Current status | Evidence required |
|---|---|---|
| Accountable Archaeology and cultural/sovereignty review routes | `UNKNOWN / HOLD` | Verified assignments, authority intervals, scope, confidentiality, and revocation process |
| Independent review capacity | `UNKNOWN / HOLD` where required | Verified route separate from author/generator and release authority |
| Live source admission and refresh | `HOLD` | Complete admitted descriptors, rights, policy, connector, fixtures, no-network proof, operator, receipts, and rollback |
| Broad direct-domain test suite | `PARTIAL / HOLD` | Replace placeholder and vacuous modules with substantive negative proof |
| CI coverage for all three substantive no-network profiles | `PARTIAL` | Deliberate workflow wiring and exact-head results |
| EvidenceBundle and proof closure | `HOLD` | Accepted producer/resolver, fixtures, policy, review, correction, and rollback |
| Archaeology policy bundle and evaluator | `HOLD` | Accepted input profile, evaluator binding, obligations, negative fixtures, and governed consumer |
| Candidate dossier and release dry run | `HOLD` | Immutable candidate, evidence, policy, review, proof, manifest, correction, and rollback support |
| Exact-location and public-safe transform decision | `PROPOSED / HOLD` | Accepted decision and accountable sensitivity, cultural, and rights-holder review |
| Operational rollback and domain-schema conflict | `CONFLICTED / HOLD` | Selected contract/schema authority, production-safe executor, invalidation, rehearsal evidence, and release authority |
| Domain-side runbook lineage | `NEEDS VERIFICATION` | No-loss reconciliation with the canonical lane and current executable evidence |
| Parent runbook inventory | `STALE / NEEDS VERIFICATION` | Full current subtree recomputation |
| Deployment and publication state | `UNKNOWN` | Current runtime, release, deployment, public endpoint, and monitoring evidence |

[Back to top](#top)

---

<a id="related-surfaces"></a>

## Related surfaces

### Governing and domain documentation

- Parent index: [`docs/runbooks/README.md`](../README.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted adoption decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- Domain README: [`docs/domains/archaeology/README.md`](../../domains/archaeology/README.md)
- Architecture: [`ARCHITECTURE.md`](../../domains/archaeology/ARCHITECTURE.md)
- Lifecycle: [`DATA_LIFECYCLE.md`](../../domains/archaeology/DATA_LIFECYCLE.md)
- Sensitivity: [`SENSITIVITY.md`](../../domains/archaeology/SENSITIVITY.md)
- Cultural review: [`CULTURAL_REVIEW.md`](../../domains/archaeology/CULTURAL_REVIEW.md)
- Publication and policy: [`PUBLICATION_AND_POLICY.md`](../../domains/archaeology/PUBLICATION_AND_POLICY.md)
- Release index: [`RELEASE_INDEX.md`](../../domains/archaeology/RELEASE_INDEX.md)
- Verification backlog: [`VERIFICATION_BACKLOG.md`](../../domains/archaeology/VERIFICATION_BACKLOG.md)
- Domain-side orientation: [`docs/domains/archaeology/runbooks/README.md`](../../domains/archaeology/runbooks/README.md)
- Domain-side rollback-drill lineage: [`rollback-drill.md`](../../domains/archaeology/runbooks/rollback-drill.md)

### Semantic, machine, operational, and release boundaries

- Contracts: [`contracts/domains/archaeology/README.md`](../../../contracts/domains/archaeology/README.md)
- Schemas: [`schemas/contracts/v1/domains/archaeology/README.md`](../../../schemas/contracts/v1/domains/archaeology/README.md)
- Fixtures: [`fixtures/domains/archaeology/README.md`](../../../fixtures/domains/archaeology/README.md)
- Policy: [`policy/domains/archaeology/README.md`](../../../policy/domains/archaeology/README.md)
- Tests: [`tests/domains/archaeology/README.md`](../../../tests/domains/archaeology/README.md)
- Validators: [`tools/validators/domains/archaeology/README.md`](../../../tools/validators/domains/archaeology/README.md)
- Proof boundary: [`data/proofs/archaeology/README.md`](../../../data/proofs/archaeology/README.md)
- Candidate boundary: [`release/candidates/archaeology/README.md`](../../../release/candidates/archaeology/README.md)
- Domain workflow: [`.github/workflows/domain-archaeology.yml`](../../../.github/workflows/domain-archaeology.yml)
- Review routing: [`.github/CODEOWNERS`](../../../.github/CODEOWNERS)

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Evidence | What it supports | What it cannot prove |
|---|---|---|
| `main@b1964d5f70834195c4e7d6c2824bdc35a409b697` | Immutable repository checkpoint | Runtime or public behavior by commit alone |
| Prior target blob `8b137891…` | Target was tracked but blank in substance | Why it was blank or external reliance |
| Direct child blobs in metadata | Exact child inventory and document bytes | Live operation or authority beyond their support |
| No-network blob `6a57abe6…` | Three synthetic profiles, one CI binding, broader holds | Archaeological truth or public permission |
| Source-refresh blob `0166f478…` | Current fail-closed procedure and live-execution hold | Source admission or live retrieval |
| Promotion blob `6c746a4f…` | Readiness procedure and policy/candidate/release holds | Applied promotion or publication |
| Rollback blob `9e59120c…` | Candidate validation, schema conflict, synthetic rehearsal | Operational rollback or public invalidation |
| Domain workflow blob `d51ba3b1…` | One executable profile and proof/release holds | Broad correctness or release |
| ADR-0029 and Directory Rules | Placement and non-authority rules | Operational approval |
| CODEOWNERS blob `dd2a84aa…` | Verified GitHub review route and its limitation | Cultural, sovereignty, independent-review, policy, or release authority |
| Domain-side runbook blobs | Orientation and rollback-drill lineage | Canonical procedure authority or production recovery proof |

Memory, generic best practice, document length, repeated proposal language, badges, and file names are not implementation evidence.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This file is documentation-only and has no source, evidence, policy, cultural-review, lifecycle, release, deployment, promotion, rollback-execution, or publication side effect.

- **Before merge:** close or abandon the draft pull request.
- **After merge:** revert the implementation commit or submit a smaller forward fix against the actual merged head; do not rewrite shared history.
- **Historical preimage:** blob `8b137891791fe96927ad78e64b0aad7bded08bdc` restores the exact prior one-byte file.

A Git revert of this README would not correct any separate source, sensitive record, evidence, policy, review, release, deployment, or publication state. Those transitions require their own owning correction and rollback paths.

[Back to top](#top)
