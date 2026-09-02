# `release/candidates/roads-rail-trade/` — Candidate Review Lane

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-roads-rail-trade-readme
title: release/candidates/roads-rail-trade/ — Candidate Review Lane
version: v2
status: draft
policy_label: public
owners:
  - <domain-steward>
  - <release-steward>
  - <data-steward>
updated: 2026-07-20
tags: [kfm, release, candidates, roads-rail-trade, pre-publication, evidence, sensitivity, review, rollback]
truth_posture: "CONFIRMED repository paths and bounded implementation evidence; PROPOSED dossier guidance; CONFLICTED schema and contract topology; NEEDS VERIFICATION for semantic owners, accepted machine contracts, end-to-end enforcement, release inventory, and public adoption"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9a29f659be82af7acbed4a2563ab8f96c1f84046
  prior_blob: 8ad3ee353ed42b2191ed8a7e09229dadde8ef505
notes:
  - "This README is release guidance. It is not a candidate, PromotionDecision, ReleaseManifest, PolicyDecision, proof, released artifact, or publication authority."
  - "The roads-rail-trade segment is canonical for this release lane. Repository documentation also exposes unresolved roads-rail-trade versus transport and domains-versus-flat schema/contract topology; this README does not resolve or mirror that drift."
  - "The inspected domain workflow performs bounded static readiness checks and intentionally records holds. It does not establish semantic validation, proof production, release approval, or public readiness."
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v2-informational)
![root](https://img.shields.io/badge/root-release%2F-blue)
![domain](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![publication](https://img.shields.io/badge/publication-not__authorized-orange)
![validation](https://img.shields.io/badge/semantic__validation-HOLD-red)
![truth](https://img.shields.io/badge/truth-cite__or__abstain-success)

> [!IMPORTANT]
> A candidate is not a release. A file, directory, passing shape check, pull request, merge, deployment, or generated summary does not promote or publish Roads/Rail/Trade material. Promotion requires a separately governed decision, evidence and policy closure, review, manifest readiness, correction support, and rollback support.

> [!CAUTION]
> KFM transportation context is not turn-by-turn navigation, dispatch, traffic control, emergency routing, railroad operating authority, legal-access advice, or a guarantee that a road, rail line, bridge, crossing, ferry, facility, route, or corridor is open, safe, passable, lawful, current, or complete.

**Quick links:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed)

## Purpose

`release/candidates/roads-rail-trade/` is the pre-publication review lane for proposed Roads/Rail/Trade release dossiers.

It helps reviewers decide whether a bounded candidate should remain in assembly, enter review, move toward manifest preparation, be repaired, be deferred, be blocked, be withdrawn, or be superseded. It holds review records and pointers; the candidate payload remains in its owning lifecycle path.

This lane may cover dossiers for road and rail segments, route and corridor membership, crossings and transport facilities, time-bound restriction or status context, freight-corridor context, historic route claims, generalized trade-route corridors, and derived network views. Each dossier must preserve the owning domain's object boundaries, source roles, time semantics, evidence, sensitivity, and cross-domain dependencies.

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move.

## Authority level

**Release-guidance lane; pre-publication; non-authoritative for transport truth, policy, proof, released artifacts, or public behavior.**

| Concern | Authority home | Boundary for this lane |
|---|---|---|
| Directory placement | [`docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) and accepted ADRs | This existing path follows `release/candidates/<domain>/`. |
| Domain meaning | [`docs/domains/roads-rail-trade/`](../../../docs/domains/roads-rail-trade/README.md) and accepted semantic contracts | A dossier cites meaning; it does not redefine roads, rail, routes, crossings, facilities, restrictions, or graphs. |
| Machine shape | Accepted files under `schemas/` | A dossier cannot make a stub or path candidate authoritative. |
| Source identity, role, rights, and cadence | [`data/registry/sources/roads-rail-trade/`](../../../data/registry/sources/roads-rail-trade/README.md) and governing policy | A dossier references admitted sources; it does not admit or upgrade them. |
| Lifecycle payloads | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, and `data/triplets/` | Payloads do not belong in this directory. |
| Evidence and proof | `data/proofs/` and the governing evidence contracts | Candidate prose, generated text, screenshots, and validator summaries are not sovereign evidence. |
| Process receipts | `data/receipts/` | A receipt records process memory; it is not proof or release approval by itself. |
| Admissibility and sensitivity | `policy/`, source-rights records, and required reviewers | This README preserves fail-closed expectations; it does not issue a `PolicyDecision`. |
| Release decisions | `release/promotion_decisions/`, `release/manifests/`, `release/rollback_cards/`, `release/correction_notices/`, and `release/withdrawal_notices/` | A dossier may point to these records but cannot replace them. |
| Released artifacts | `data/published/` | Only reviewed public-safe artifacts belong there; release records remain under `release/`. |
| Public API, map, export, search, graph, and AI surfaces | Governed interfaces bound to released artifacts | Public clients must not read this candidate lane or internal lifecycle stores directly. |

### Repository fit

```text
release/
├── candidates/
│   └── roads-rail-trade/       # you are here: candidate dossiers and review notes
├── manifests/                  # ReleaseManifest records
├── promotion_decisions/        # PromotionDecision records
├── rollback_cards/             # rollback artifacts
├── correction_notices/         # correction records
├── withdrawal_notices/         # withdrawal records
├── signatures/                 # signing artifacts
└── changelog/                  # release-level history

data/
├── receipts/                   # process memory
├── proofs/                     # evidence/proof closure
└── published/                  # released public-safe artifacts
```

### Domain-segment and authority conflict

`roads-rail-trade` is the canonical domain segment for this release lane under current Directory Rules and Domain Placement Law.

The repository also contains documentation and implementation-shaped surfaces under both `contracts/domains/roads-rail-trade/` and `contracts/transport/`, and under multiple `schemas/.../roads-rail-trade/` and `schemas/.../transport/` forms. Domain documents label this `OQ-RRT-01`; current repository evidence does not establish an accepted migration that resolves it.

**CONFLICTED / NEEDS VERIFICATION:** a candidate may cite the relevant paths, but this lane must not select a winner, create a mirror, rename a segment, or treat parallel files as mutually interchangeable without an accepted authority decision and migration plan.

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Directly observed at the pinned repository commit or established by governing doctrine. |
| `PROPOSED` | Review guidance or future behavior; not established implementation. |
| `NEEDS VERIFICATION` | Checkable, but not closed by the inspected evidence. |
| `UNKNOWN` | The bounded inspection did not establish an answer. |
| `CONFLICTED` | Repository or doctrine surfaces disagree or expose parallel authority candidates. |
| `INFERRED` | A reasoned interpretation that must not be upgraded to observed fact. |

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Visibility | Public |
| Base ref | `main` |
| Pinned evidence commit | `9a29f659be82af7acbed4a2563ab8f96c1f84046` |
| Prior target blob | `8ad3ee353ed42b2191ed8a7e09229dadde8ef505` |
| Path owner route | `/release/ @bartytime4life` in `.github/CODEOWNERS` |
| Documentation state | Existing compact draft; parent candidate index explicitly calls for expansion |
| Change scope | This README plus the required generated provenance receipt only |

### Maturity matrix

| Surface | State at the pinned commit | Safe conclusion |
|---|---|---|
| Candidate lane | `CONFIRMED` | The canonical release-candidate path exists. Candidate instances below it were not exhaustively inventoried. |
| Candidate dossier vocabulary | `PROPOSED` | The parent candidate README supplies workflow labels; no accepted machine enum was established for them. |
| Domain contracts and schemas | `CONFLICTED / NEEDS VERIFICATION` | Multiple `roads-rail-trade` and `transport` homes are surfaced; acceptance, pairing, and migration remain unresolved. |
| Domain schemas and fixtures | `CONFIRMED` structurally present | The domain workflow parses their JSON shape and status metadata; this is not semantic or release validation. |
| Domain tests | `CONFIRMED` known assert-true smoke scaffold | The domain workflow intentionally detects that scaffold and reports no substantive domain test suite. |
| Validator implementation | `NEEDS VERIFICATION / HOLD` | The inspected workflow reports no accepted executable validator body in the checked transport validator lanes. |
| Domain policy | `CONFIRMED` proposed scaffold | Policy presence does not establish complete rights, sensitivity, legal-access, current-status, or release enforcement. |
| Domain workflow | `CONFIRMED` bounded static readiness workflow | It uses read-only repository permissions, performs boundary checks, and intentionally records semantic-validation, proof, and publish-readiness holds. |
| `PromotionDecision` schema | `PROPOSED`, fielded, finite | It requires `APPROVE`, `DENY`, or `ABSTAIN` plus evidence, rollback, policy, time, and review fields. Runtime wiring remains `NEEDS VERIFICATION`. |
| `ReleaseManifest` schema | `PROPOSED` thin stub | It requires only `id` and permits additional properties; shape acceptance is not release closure. |
| Roads/Rail/Trade release inventory | `UNKNOWN` in this bounded review | No claim is made that a candidate or public release exists, is current, or is complete. |
| Human review | `PENDING` | CODEOWNERS routing is not semantic approval, sensitivity approval, release approval, or publication authority. |

Repository presence and a passing structural check do not establish public readiness:

```text
README + schemas + fixtures + static readiness checks
!= semantic validation
!= EvidenceBundle closure
!= PolicyDecision
!= PromotionDecision APPROVE
!= ReleaseManifest closure
!= publication
```

## What belongs here

- This folder-level README.
- Bounded candidate dossiers and readiness notes.
- Review checklists and safe reviewer dispositions.
- Immutable pointers to candidate artifacts in their owning lifecycle paths.
- References to source descriptors, EvidenceRefs, EvidenceBundles, validation reports, policy and rights review, and human review records.
- Manifest-handoff notes after a separate governed `PromotionDecision` permits advancement.
- Correction, withdrawal, supersession, and rollback references.
- Truth-labeled records of unresolved source-role, identity, time, geometry, sensitivity, schema, contract, validation, or ownership questions.

### Candidate lifecycle

The parent candidate index uses the following review vocabulary. Treat it as **documentation guidance**, not an accepted machine enum, unless a governing contract and schema say otherwise.

| Candidate status | Meaning |
|---|---|
| `PROPOSED` | Candidate is named but not ready for review. |
| `ASSEMBLING` | The dossier and its references are being gathered. |
| `READY_FOR_REVIEW` | Required review material is present; no approval is implied. |
| `APPROVED_FOR_MANIFEST` | A review disposition allows manifest preparation to begin; publication is not authorized. |
| `PROMOTED` | A separately governed release path records the completed transition. Do not infer this from a file move or merge. |
| `DEFERRED` | Candidate remains in consideration but is not ready now. |
| `REPAIR_REQUIRED` | Named deficiencies must be corrected before advancement. |
| `BLOCKED` | A named blocker prevents advancement. |
| `WITHDRAWN` | Candidate was removed from consideration while its audit history remains. |
| `SUPERSEDED` | A newer candidate replaces it through explicit lineage. |

`HOLD` may be used as a human review or workflow disposition. Do not add it to a machine enum without contract and schema authority.

### Candidate dossier contract

Every dossier should answer each field below or record `UNKNOWN`, `NEEDS VERIFICATION`, `NOT APPLICABLE`, or a blocking reason.

| Field | Required content |
|---|---|
| Candidate identity | Stable candidate ID, version, domain, immutable run/build reference, and content digest where available |
| Scope | Included and excluded object families, geography, time interval, intended audience, and intended release surface |
| Artifact pointer | Immutable reference to the candidate artifact in its owning lifecycle path; never the payload itself |
| Proposed target | Exact proposed released artifact family; no floating `latest` alias |
| Object boundaries | Separation among segments, routes, memberships, crossings, facilities, events, restrictions, historic claims, trade corridors, and graph derivatives |
| Source closure | SourceDescriptor references, fixed source roles, source vintage/cadence, rights, attribution, and retrieval context |
| Evidence closure | Resolvable EvidenceRef and EvidenceBundle references, claim scope, integrity digest, and citation-validation state |
| Identity and time | Object identity, route membership, geography version, geometry lineage, valid/source/retrieval/build/release/correction times, and stale-state posture |
| Uncertainty and geometry | Precision basis, uncertainty representation, generalization/redaction receipts, and prohibition on inferred precision |
| Cross-domain dependencies | Owned references to Hydrology, Settlements/Infrastructure, Hazards, Archaeology, People/Land, Agriculture, or other lanes without authority collapse |
| Rights and sensitivity | Restricted terms, cultural/sovereignty review, critical-infrastructure review, exact-harm-coordinate handling, and public-safe transform references |
| Validation | Schema, semantic, source-role, temporal, spatial, topology, evidence, policy, sensitivity, negative-test, and citation results, with explicit gaps |
| Review | Author, reviewer roles, conflicts, independence requirements, ticket/review record, and current disposition |
| Manifest handoff | PromotionDecision reference, manifest-readiness state, exact blockers, and intended manifest family |
| Correction and rollback | Correction/invalidation path, rollback target, supersession or withdrawal reference, and safe prior state |

### Source-role and knowledge-character separation

Source role is fixed at admission and must not be upgraded because a candidate advanced. The repository doctrine uses the role vocabulary `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`.

For this domain, reviewers should specifically reject:

- observational or candidate map edits presented as legal, regulatory, or current-operational authority;
- administrative names presented as proof of route designation, membership, ownership, access, restriction, or condition;
- live event feeds silently converted into historical truth;
- modeled, inferred, reconstructed, synthetic, or generated route geometry presented as observed alignment;
- a graph edge presented as a canonical segment, route, crossing, or safe path; and
- a narrative or AI summary presented as evidence without resolving the cited EvidenceBundle.

### Roads/Rail/Trade review safeguards

| Candidate concern | Minimum posture | Blocking condition |
|---|---|---|
| Modern road or rail geometry | Preserve source, vintage, identity, route membership, geometry lineage, and legal/current-status limits. | Missing source role, time, lineage, or evidence closure. |
| Restriction, closure, work-zone, operator, or status context | Carry valid/source/retrieval time, cadence, stale-state behavior, and owning authority. | Stale or unknown state presented as current; KFM presented as operational authority. |
| Historic route claim | Preserve source conflict, temporal scope, uncertainty, and generalized public geometry where required. | Coarse or interpretive evidence converted into a precise line or confirmed membership. |
| Indigenous, cultural, treaty, or steward-controlled corridor | Apply the most restrictive rights and sensitivity posture; obtain required sovereignty/cultural review before any public-safe derivative. | Missing rights-holder review, unsafe precision, or unresolved source rights. |
| Bridge, crossing, ferry, yard, depot, or other facility | Separate transport-side claims from infrastructure condition, vulnerability, hydrology, access, and safety authority. | Public exposure of restricted condition/vulnerability detail or unsupported safe-passage claim. |
| Freight or trade corridor | Preserve designation source, role, time, scope, and whether the representation is administrative, observed, modeled, or interpretive. | Designation or activity inferred from proximity, geometry, or generated text alone. |
| Derived network or graph view | Mark as derivative, bind every edge to supported objects and time, and preserve graph rollback. | Graph projection replaces source-bound domain records or becomes operational routing truth. |
| Cross-domain join | Preserve each neighboring lane's identity, evidence, policy, sensitivity, and correction authority. | Join reveals restricted data or absorbs another domain's truth. |

### Illustrative candidate dossier

This example is documentation only. It is not a schema, a real candidate, a release record, or permission to publish.

```markdown
# <candidate-id> — Roads/Rail/Trade candidate dossier

## Status

ASSEMBLING

## Identity and scope

- Candidate version: <immutable version>
- Run/build reference: <immutable reference>
- Object families: <included families>
- Exclusions: <explicit exclusions>
- Geography version: <immutable reference>
- Valid/source/retrieval/build time: <explicit values>
- Intended public surface: <bounded public-safe surface>

## Candidate artifact

- Immutable artifact ref: <owning lifecycle path + digest>
- Proposed released target: <artifact family + stable ID>

## Sources and evidence

- Source descriptors and fixed roles: <refs>
- Rights and attribution: <status + refs>
- EvidenceRef: <ref>
- EvidenceBundle: <resolved ref + digest>
- Citation validation: <report ref + outcome>

## Geometry, time, and sensitivity

- Geometry lineage and uncertainty: <refs + findings>
- Freshness and stale-state behavior: <status>
- Public-safe transforms: <receipt refs or not applicable>
- Cultural, infrastructure, exact-location, and combination risks: <findings>
- Remaining blockers: <named blockers>

## Validation and review

- Schema and semantic checks: <refs + outcomes>
- Source-role, temporal, spatial, topology, evidence, policy, sensitivity, and negative checks: <refs + outcomes>
- Author and reviewer roles: <bindings>
- Review state: <pending / changes requested / approved>

## Release handoff

- PromotionDecision: <ref + APPROVE / DENY / ABSTAIN>
- Manifest readiness: <state + blockers>
- Correction path: <ref>
- Rollback target: <ref>
- Supersession or withdrawal: <ref or not applicable>
```

## What does NOT belong here

- Raw, work, quarantine, processed, catalog, triplet, or published data payloads.
- Bulk datasets, GeoJSON, Parquet, PMTiles, STAC items, graph exports, models, map tiles, screenshots, API responses, or AI outputs.
- SourceDescriptor instances, registry rows, contracts, schemas, policy rules, validator code, fixtures, tests, workflows, packages, or pipeline implementations.
- PromotionDecision, ReleaseManifest, PolicyDecision, CorrectionNotice, WithdrawalNotice, RollbackCard, signature, proof, or receipt instances that belong in their own authority paths.
- Live traffic, closure, detour, train movement, dispatch, signal, switching, warrant, emergency, legal-access, right-of-way, bridge-condition, flood/ford-condition, ferry-operation, or safe-passage instructions.
- Credentials, tokens, private endpoints, restricted source payloads, private operating material, or critical-infrastructure vulnerabilities.
- Exact protected cultural, archaeological, private-land, or otherwise harm-enabling coordinates.
- Generated language, model confidence, map styling, proximity, route snapping, graph connectivity, or repeated assertion used as proof.
- Final release approval, direct publication, or public-client access to this directory.
- A README-only resolution of the `roads-rail-trade` versus `transport` schema/contract conflict.

If material in this lane would be unsafe in a public pull request, store only a safe identifier and access-controlled reference; do not copy the sensitive value into the dossier, filename, receipt, log, review comment, or commit message.

## Inputs

A candidate dossier may be assembled only from reviewable references to material in its owning roots.

### Admission checklist

Before marking a dossier `READY_FOR_REVIEW`, verify or explicitly block on:

1. stable candidate, run, object, route/membership, geography, and version identities;
2. immutable artifact references and digests;
3. admitted source descriptors with fixed roles, rights, attribution, vintage, cadence, and retrieval context;
4. resolvable EvidenceRefs and EvidenceBundles with matching claim scope;
5. explicit valid, source, retrieval, build, and correction times where applicable;
6. geometry lineage, CRS/geography version, precision basis, and uncertainty/generalization posture;
7. object-family and cross-domain ownership boundaries;
8. schema and contract references with any path conflict recorded rather than normalized away;
9. semantic, temporal, spatial, topology, evidence, policy, sensitivity, rights, citation, and negative-test outcomes;
10. public-safe transform receipts for generalization, redaction, aggregation, or withholding where required;
11. required domain, rights-holder, sensitivity, infrastructure/security, evidence, data, and release reviewers;
12. correction, invalidation, supersession/withdrawal, and rollback targets; and
13. exact remaining `UNKNOWN`, `NEEDS VERIFICATION`, `CONFLICTED`, and blocking findings.

### Fail-closed intake

Keep the candidate in assembly, quarantine, repair, or blocked state when any required source, evidence, rights, sensitivity, identity, time, geometry, validation, review, correction, or rollback reference is missing, stale, conflicted, unsafe, or unresolved.

Do not improve an apparent outcome by silently dropping failing records, downcasting source roles, smoothing uncertainty, replacing precise restricted geometry with an unreviewed transform, or treating absence from a search result as proof of absence.

## Outputs

This lane supports only review and controlled handoff outputs:

- a maintained candidate dossier;
- a reviewer disposition such as continue assembly, review, repair, defer, block, withdraw, or supersede;
- safe references to validation, evidence, policy, rights, sensitivity, correction, and rollback records;
- a separately governed `PromotionDecision` with `APPROVE`, `DENY`, or `ABSTAIN`; and
- when approved and otherwise closed, an input packet for ReleaseManifest preparation.

### Decision vocabulary

Keep candidate status, promotion decision, workflow disposition, release state, and public response separate.

| Vocabulary | Values established by inspected evidence | Boundary |
|---|---|---|
| Candidate status | Parent README guidance listed above | Documentation workflow; machine authority `NEEDS VERIFICATION`. |
| Promotion decision | `APPROVE`, `DENY`, `ABSTAIN` | Defined by the paired proposed schema; `APPROVE` is not publication by itself. |
| Workflow/review disposition | `HOLD`, `REPAIR_REQUIRED`, or named findings | Human/CI coordination only unless an owning machine contract says otherwise. |
| Release state | `CONFLICTED / NEEDS VERIFICATION` across domain documentation profiles | Do not invent or normalize a release-state enum in this lane. |
| Governed public response | Commonly `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Request-time interface result; distinct from promotion and release state. |

### Manifest handoff

A dossier may move toward manifest preparation only after a separately governed `PromotionDecision` records `APPROVE` and all applicable gates are satisfied.

The handoff should identify immutable candidate and run IDs, exact inputs, evidence-bundle digests, source-rights state, sensitivity and transform records, validation reports, policy-bundle identity, reviewer bindings, proposed released-artifact hashes, and correction/rollback targets.

The inspected common `ReleaseManifest` schema is a thin `PROPOSED` stub that requires only `id` and permits additional properties. Passing that schema alone is not manifest closure and must not be described as release readiness.

### Public handoff boundary

Released artifacts belong under `data/published/`; release decisions belong under `release/`. Public clients bind to governed interfaces and released artifacts, never to this directory, a candidate payload, a floating `latest` pointer, or an internal lifecycle store.

## Validation

### Current executable boundary

The inspected [domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml) is a bounded static readiness workflow with read-only repository permissions. It currently:

- checks required responsibility-boundary paths;
- confirms the known assert-true smoke scaffold and detects substantive test changes that require deliberate graduation;
- parses current domain JSON Schemas and fixtures for structural integrity and status metadata;
- detects executable bodies in inspected transport validator lanes;
- checks that the current domain policy remains explicitly proposed; and
- records explicit holds for semantic validation, proof production, and publish readiness.

It does **not** establish route or network truth, legal access, live closure, bridge condition, rail status, safe passage, semantic correctness, EvidenceBundle closure, policy correctness, proof production, release approval, or publication readiness.

### Candidate review gates

| Gate | Minimum question | Fail-closed result |
|---|---|---|
| Placement | Is the dossier under the canonical release candidate lane with payloads and authority objects kept elsewhere? | `HOLD` or `REPAIR_REQUIRED`. |
| Identity | Are candidate, run, dataset, object, route/membership, geography, version, and digests stable and collision-aware? | `REPAIR_REQUIRED` or `ABSTAIN`. |
| Source and evidence | Do source roles remain fixed, rights current, and consequential references resolve to scoped EvidenceBundles? | `ABSTAIN` or `DENY`. |
| Time and freshness | Are valid/source/retrieval/build times and stale-state behavior explicit for time-sensitive claims? | `HOLD`, `ABSTAIN`, or `DENY`. |
| Geometry and uncertainty | Is precision evidence-backed, uncertainty visible, and any public transform reviewed and receipted? | `REPAIR_REQUIRED` or `DENY`. |
| Cross-domain ownership | Do Hydrology, Settlements/Infrastructure, Hazards, Archaeology, People/Land, and other lanes retain their truth and policy authority? | `HOLD` or `DENY`. |
| Rights and sensitivity | Are restricted terms, cultural sovereignty, critical infrastructure, exact-harm coordinates, private access, and combination risks resolved? | `DENY`, `HOLD`, or restricted review. |
| Validation | Did applicable schema, semantic, temporal, spatial, topology, evidence, policy, sensitivity, citation, and negative checks run and pass? | `REPAIR_REQUIRED`, `ABSTAIN`, or `DENY`. |
| Review | Are required roles identified, conflicts visible, and separation requirements met where applicable? | `HOLD`. |
| Release readiness | Are PromotionDecision, manifest inputs, immutable targets, correction path, and rollback support complete? | `ABSTAIN` or `DENY`. |
| Public-surface safety | Is the proposed derivative released, current enough, appropriately generalized, and served only through governed interfaces? | `DENY`. |

### Verification checklist

#### Placement and authority

- [ ] Candidate dossier is under `release/candidates/roads-rail-trade/`.
- [ ] Payload, proof, receipt, source, contract, schema, policy, and release-decision instances remain in their owning roots.
- [ ] No schema/contract path conflict was silently normalized or mirrored.
- [ ] No domain segment was renamed and no parallel release authority was created.

#### Candidate closure

- [ ] Candidate identity, version, geography, scope, object families, and time are explicit.
- [ ] Artifact pointers are immutable and digest-bound.
- [ ] Sources are admitted, rights-aware, and assigned fixed non-collapsed roles.
- [ ] Every consequential EvidenceRef resolves to the intended EvidenceBundle.
- [ ] Route membership, geometry lineage, uncertainty, precision, and stale-state posture are supported.
- [ ] Modern, historic, modeled, reconstructed, candidate, synthetic, generated, and graph-derived knowledge remain distinguishable.
- [ ] Cultural/sovereignty, infrastructure, exact-location, legal-access, and combination risks were reviewed where applicable.
- [ ] Neighboring domains retain identity, evidence, policy, sensitivity, and correction authority.
- [ ] Applicable schema, semantic, temporal, spatial, topology, citation, policy, sensitivity, and negative checks are recorded.
- [ ] Required reviewers and independence constraints are identified without treating CODEOWNERS as approval.
- [ ] PromotionDecision, ReleaseManifest inputs, correction path, and rollback target are separately reachable.
- [ ] Candidate and internal material remains unavailable to public clients and ordinary AI/UI/map surfaces.

#### Documentation and provenance

- [ ] Repository-relative links resolve at the reviewed commit.
- [ ] Truth labels distinguish confirmed facts, proposals, unknowns, inferences, and conflicts.
- [ ] No credential, private endpoint, restricted payload, operational instruction, vulnerability detail, or exact sensitive location appears in the dossier or review metadata.
- [ ] Generated text, maps, graphs, screenshots, and receipts are not treated as sovereign evidence.
- [ ] AI-authored substantive changes carry a schema-valid generated receipt with independent human review pending or completed.
- [ ] A future behavior change updates this README or records why no documentation change is required.

### Receipt, proof, and release separation

- A `RunReceipt`, validation receipt, or generated receipt records what a process did.
- A proof record or EvidenceBundle supports claims and integrity closure.
- A `PromotionDecision` records a finite governed transition decision.
- A `ReleaseManifest` binds a release after required closure.
- A merge, workflow success, or receipt does not substitute for any of the others.

## Review burden

`.github/CODEOWNERS` routes `/release/` and `/data/receipts/` changes to `@bartytime4life`. That route does not prove semantic ownership, human approval, rights-holder approval, sensitivity approval, infrastructure/security review, release approval, or publication authority.

Review roles depend on the candidate:

| Role | Review burden |
|---|---|
| Roads/Rail/Trade domain steward | Object boundaries, identity, route membership, source roles, time, uncertainty, and domain claims |
| Data/source steward and rights reviewer | Source admission, rights, attribution, cadence, provenance, and redistribution |
| Evidence/validation steward | Evidence resolution, integrity, deterministic validation, negative cases, and unresolved findings |
| Sensitivity or security reviewer | Cultural corridors, exact-harm coordinates, critical infrastructure, restricted operational detail, and combination risk |
| Rights-holder or cultural/sovereignty reviewer | Indigenous, treaty, oral-history, or steward-controlled corridor claims where applicable |
| Adjacent-domain steward | Hydrology, Settlements/Infrastructure, Hazards, Archaeology, People/Land, or other owned claims reached by joins |
| Release steward | Promotion decision, manifest readiness, correction, withdrawal, supersession, and rollback support |

The proposed [release separation-of-duties ADR](../../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md) describes stronger independence for material and sensitive releases. Its accepted status and enforcement remain `NEEDS VERIFICATION`; do not claim that CODEOWNERS or a merged pull request satisfies it.

## Related folders

### Governing and domain guidance

- [Release candidate parent index](../README.md)
- [Release governance root](../../README.md)
- [Directory Rules](../../../docs/doctrine/directory-rules.md)
- [Domain Placement Law](../../../docs/architecture/domain-placement-law.md)
- [Roads/Rail/Trade domain dossier](../../../docs/domains/roads-rail-trade/README.md)
- [Roads/Rail/Trade sensitivity posture](../../../docs/domains/roads-rail-trade/SENSITIVITY.md)
- [Historic routes guidance](../../../docs/domains/roads-rail-trade/HISTORIC_ROUTES.md)
- [Source guidance](../../../docs/domains/roads-rail-trade/SOURCES.md)
- [Domain release index](../../../docs/domains/roads-rail-trade/RELEASE_INDEX.md)
- [Roads/Rail/Trade promotion runbook](../../../docs/runbooks/roads-rail-trade/PROMOTION_RUNBOOK.md)

### Contracts, schemas, policy, and validation

- [Domain contract index](../../../contracts/domains/roads-rail-trade/README.md)
- [`transport` contract compatibility/index lane](../../../contracts/transport/README.md)
- [Domain schema index](../../../schemas/contracts/v1/domains/roads-rail-trade/README.md)
- [`transport` schema compatibility/index lane](../../../schemas/contracts/v1/transport/README.md)
- [PromotionDecision contract](../../../contracts/release/promotion_decision.md)
- [ReleaseManifest contract](../../../contracts/release/release_manifest.md)
- [Proposed PromotionDecision schema](../../../schemas/contracts/v1/release/promotion_decision.schema.json)
- [Thin proposed ReleaseManifest schema](../../../schemas/contracts/v1/release/release_manifest.schema.json)
- [Domain policy scaffold](../../../policy/domains/roads-rail-trade/README.md)
- [Domain fixtures](../../../fixtures/domains/roads-rail-trade/README.md)
- [Domain tests](../../../tests/domains/roads-rail-trade/README.md)
- [Domain validator index](../../../tools/validators/domains/roads-rail-trade/README.md)
- [Domain CI readiness workflow](../../../.github/workflows/domain-roads-rail-trade.yml)
- [Pipeline specification boundary](../../../pipeline_specs/roads-rail-trade/README.md)

### Release records

- [Promotion decisions](../../promotion_decisions/README.md)
- [Release manifests](../../manifests/README.md)
- [Rollback cards](../../rollback_cards/README.md)
- [Correction notices](../../correction_notices/README.md)

## ADRs

- [ADR-0018 — Promotion gate sequence](../../../docs/adr/ADR-0018-promotion-gate-sequence.md) is `PROPOSED` in the inspected repository. This README uses its gate concepts as review guidance and does not claim full enforcement.
- [ADR-0024 — Steward separation of duties for release](../../../docs/adr/ADR-0024-steward-separation-of-duties-for-release.md) is `PROPOSED` in the inspected repository. This README preserves the review burden without claiming acceptance or automation.
- `OQ-RRT-01` in the Roads/Rail/Trade documentation records the unresolved `roads-rail-trade` versus `transport` schema/contract topology. It is an open question, not an accepted migration decision.

This documentation revision does not create or accept an ADR. A later change requires ADR or migration review if it renames the domain segment, selects or retires a canonical schema/contract home, changes object identity, adds parallel release authority, changes lifecycle or release semantics, alters public-store access, or weakens the trust membrane.

### Maintenance

Review this README when any of the following occurs:

- the first verified candidate dossier is added or the candidate-lane inventory changes;
- `OQ-RRT-01` is resolved or a schema/contract migration begins;
- substantive domain validators, tests, policy, proof producers, or workflow gates are accepted;
- PromotionDecision or ReleaseManifest contracts, schemas, validators, fixtures, or required checks materially change;
- a candidate reaches manifest handoff, promotion, correction, withdrawal, supersession, or rollback;
- source rights, cadence, current-status behavior, sensitivity, or public-surface rules change; or
- six months pass without review.

### Documentation rollback

Before merge, leave or close the unmerged review route and abandon only the scoped branch with appropriate repository authority. After merge, create a transparent revert commit or revert pull request for this README and its generated receipt; do not rewrite shared history.

Reverting this documentation does not roll back data, a candidate, a policy decision, a release manifest, or a published artifact. If repository or public state changed separately, use the applicable governed CorrectionNotice, WithdrawalNotice, RollbackCard, invalidation, supersession, and release procedures.

## Last reviewed

| Field | Value |
|---|---|
| Date | 2026-07-20 |
| Repository | `bartytime4life/Kansas-Frontier-Matrix` |
| Base ref | `main` |
| Pinned evidence commit | `9a29f659be82af7acbed4a2563ab8f96c1f84046` |
| Prior target blob | `8ad3ee353ed42b2191ed8a7e09229dadde8ef505` |
| Review type | Repository-grounded candidate-lane revision; no candidate, payload, schema, contract, policy, validator, fixture, test, workflow, manifest, release, or publication state changed |
| Next review trigger | First verified candidate dossier, manifest handoff, accepted validator/policy graduation, slug-topology decision, correction/rollback event, or 2027-01-20, whichever occurs first |
