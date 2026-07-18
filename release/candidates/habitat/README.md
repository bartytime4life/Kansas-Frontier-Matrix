<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-habitat-readme
title: Habitat Release Candidate Review Lane
type: per-domain-release-candidate-index
version: v2
status: draft; repository-grounded; deny-by-default; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
domain: habitat
lane_role: habitat candidate dossier index, child-lane router, and pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 7b9c4592fc53ec6ac5182782bd62225816e86a6c
  prior_blob: bd0ccc0dfaaee950d0ca3e42f0395d391a50e0fc
  bounded_candidate_inventory: parent README plus two child README indexes; no non-README candidate record established
related:
  - ../README.md
  - ../../README.md
  - ../../manifests/README.md
  - ../../promotion_decisions/README.md
  - ../../correction_notices/README.md
  - ../../rollback_cards/README.md
  - ../../withdrawal_notices/README.md
  - ../../changelog/README.md
  - ./ecoregions/README.md
  - ./habitat_fauna_thin_slice/README.md
  - ../../../docs/domains/habitat/RELEASE_INDEX.md
  - ../../../docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md
  - ../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/runbooks/habitat/PROMOTION_RUNBOOK.md
  - ../../../docs/runbooks/habitat/ROLLBACK_RUNBOOK.md
  - ../../../data/processed/habitat/README.md
  - ../../../data/published/habitat/README.md
  - ../../../data/registry/sources/habitat/README.md
  - ../../../data/proofs/habitat/README.md
  - ../../../contracts/domains/habitat/README.md
  - ../../../schemas/contracts/v1/domains/habitat/README.md
  - ../../../policy/domains/habitat/README.md
  - ../../../fixtures/domains/habitat/README.md
  - ../../../tests/domains/habitat/README.md
  - ../../../tools/validators/domains/habitat/README.md
  - ../../../tools/validators/habitat/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-habitat.yml
  - ../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, habitat, ecoregions, habitat-fauna, evidence, sensitivity, geoprivacy, correction, rollback]
notes:
  - "This README indexes Habitat release-candidate dossiers and routes specialized candidates to governed child lanes. It is not Habitat truth, source admission, policy, proof, stewardship, regulatory interpretation, release approval, or publication authority."
  - "Bounded repository inspection establishes the parent README and two child README indexes, but no non-README candidate record or active Habitat release candidate."
  - "The literal sentence 'A candidate is not a release.' is retained for the current domain-habitat readiness workflow; it is a compatibility signal, not release proof."
  - "Habitat sensitivity is frequently join-induced. A benign Habitat object can become restricted through association with Fauna, Flora, archaeology, private-land, infrastructure, cultural, or other controlled context."
  - "CODEOWNERS routing is not stewardship assignment, sensitivity review, independent approval, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/habitat/` — Habitat Release Candidate Review Lane

> Index Habitat release-candidate dossiers, route specialized candidates to governed child lanes, preserve blockers and safe support pointers, and prevent habitat observations, patches, classifications, scores, models, corridors, restoration opportunities, stewardship context, regionalization layers, or cross-domain joins from being treated as released, legally authoritative, ecologically proven, management-approved, or public-safe before source, evidence, rights, sensitivity, policy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![lane](https://img.shields.io/badge/lane-candidates-blueviolet)
![domain](https://img.shields.io/badge/domain-habitat-2E7D32)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![sensitivity](https://img.shields.io/badge/sensitivity-join--induced%20fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@7b9c4592fc…`:** bounded repository inspection establishes this parent README plus two governed child README indexes:
>
> - `release/candidates/habitat/ecoregions/README.md`
> - `release/candidates/habitat/habitat_fauna_thin_slice/README.md`
>
> No non-README Habitat candidate record, child dossier, accepted candidate-manifest contract, approved PromotionDecision, ReleaseManifest, or released Habitat artifact was established. Both child indexes explicitly report no active child candidate. The Habitat release index remains a documentation mirror with illustrative or proposed material, the Habitat proof lane reports implementation depth as unknown, Habitat policy remains a scaffold, and current domain automation is a readiness/maturity workflow rather than Habitat validation or release authority.
>
> Differently named, unindexed, generated, history-only, external, restricted-system, or runtime-only material remains **UNKNOWN** until directly verified.

## Quick navigation

[Purpose](#purpose) ·
[Status](#status-and-evidence-boundary) ·
[Authority](#authority-and-repository-fit) ·
[Inventory](#current-candidate-inventory) ·
[Routing](#child-lane-routing) ·
[Lifecycle](#candidate-lifecycle) ·
[Contents](#what-belongs-here) ·
[Exclusions](#what-does-not-belong-here) ·
[Admission](#candidate-admission-contract) ·
[Identity](#habitat-identity-object-family-and-source-role) ·
[Anti-collapse](#habitat-anti-collapse-rules) ·
[Sensitivity](#sensitivity-geoprivacy-rights-and-public-safe-representation) ·
[Time](#time-vintage-model-and-stale-state) ·
[Gates](#habitat-release-gates) ·
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

`release/candidates/habitat/` is the Habitat domain's pre-publication review and candidate-routing lane under the `release/` responsibility root.

It exists to answer bounded questions:

1. Which Habitat candidate dossiers are indexed?
2. Which Habitat object families, source roles, model roles, joins, representations, and audience classes are in scope?
3. Which candidates belong in this parent lane and which require a specialized child lane?
4. Which admitted sources, EvidenceBundles, rights decisions, sensitivity decisions, validations, reviews, catalogs, and receipts support each candidate?
5. Does the proposed public representation preserve Habitat's ownership boundary and avoid upgrading context, models, regulatory material, or joined evidence into stronger truth?
6. Does the candidate remain safe across files, tiles, API payloads, popups, exports, search, graph projections, caches, logs, screenshots, and AI summaries?
7. Which release record owns the next governed state transition?
8. Can the candidate be corrected, withdrawn, superseded, and rolled back without restoring unsafe or unsupported material?

**A candidate is not a release.**

A dossier in this lane is a review packet. It does not create a Habitat observation, public-safe transform, EvidenceBundle, PolicyDecision, ReviewRecord, PromotionDecision, ReleaseManifest, published layer, legal designation, ecological conclusion, management recommendation, or governed API authority.

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, schema pass, model run, proof pass, catalog entry, branch merge, map render, graph edge, successful workflow, or generated narrative.

[Back to top](#top)

---

## Status and evidence boundary

| Question | Repository-grounded answer |
|---|---|
| Does this parent README exist? | **CONFIRMED.** It existed at the pinned base with blob `bd0ccc0dfaaee950d0ca3e42f0395d391a50e0fc`. |
| Which direct child lanes are established? | **CONFIRMED:** `ecoregions/` and `habitat_fauna_thin_slice/`, each currently represented by a repository-grounded README index. |
| Are there non-README candidate records under the bounded Habitat candidate tree? | **Not established.** The current domain workflow is designed to hold while only README files and `.gitkeep` files exist. |
| Is an active Habitat candidate established? | **No.** No child index establishes an active candidate or dossier. |
| Is a candidate approved for manifest assembly? | **No.** No `APPROVED_FOR_MANIFEST` candidate was established. |
| Is a Habitat ReleaseManifest established by this lane? | **No.** Release manifests remain shared release records and none was established by this candidate inventory. |
| Is a published Habitat artifact established by this README? | **No.** Documentation, processed data, catalog guidance, proof guidance, workflow holds, or published-lane READMEs do not establish emitted released bytes. |
| Is executable Habitat policy established? | **No.** `policy/domains/habitat/README.md` remains a greenfield scaffold in inspected evidence. |
| Is accepted Habitat proof production established? | **No.** `data/proofs/habitat/README.md` says implementation depth remains unknown; the domain workflow retains an explicit proof hold. |
| Are executable tests and validators mature? | **NEEDS VERIFICATION.** Placeholder and scaffold files exist, and the current validation readiness evaluator has recently failed; exact accepted suite and detector behavior remain unresolved. |
| Are public clients allowed to read this lane? | **No.** Normal public clients use governed APIs and released public-safe artifacts only. |
| Does CODEOWNERS prove review or release approval? | **No.** Routing is not stewardship, sensitivity review, independent approval, or publication authority. |

### Truth labels used here

- **CONFIRMED** — directly supported by the current repository inspection, file content, workflow definition, or generated artifacts.
- **PROPOSED** — a recommended contract, field, state, path use, or control not yet accepted as implementation.
- **UNKNOWN** — not resolved strongly enough to state.
- **NEEDS VERIFICATION** — checkable but not yet sufficiently verified.
- **CONFLICTED** — competing repository evidence or terminology requires resolution.
- **LINEAGE** — historical or supersession context that must remain auditable.

### Safe interpretation

The safest current conclusion is:

```text
Habitat candidate parent index: present
Governed child indexes: ecoregions, habitat_fauna_thin_slice
Non-README candidate record: not established
Active candidate: none established
Approved candidate: none established
Release manifest: none established by this inventory
Published Habitat release: none established by this inventory
```

Absence of an indexed candidate is not proof that no Habitat material exists elsewhere. It means this governed candidate lane does not currently establish release readiness for such material.

[Back to top](#top)

---

## Authority and repository fit

### Owning root

This file remains under:

```text
release/candidates/habitat/README.md
```

Directory Rules basis:

- `release/` owns promotion, candidate review, manifest, correction, withdrawal, supersession, and rollback decision surfaces.
- `release/candidates/` owns pre-publication dossiers and readiness indexes.
- Habitat is a domain segment inside the release responsibility root, not a new repository root.
- Child lanes narrow review responsibilities without creating new release, policy, proof, schema, source, or lifecycle authorities.
- Candidate payload bytes remain in the appropriate lifecycle lane and are referenced immutably from the dossier.
- Public clients do not read candidate folders as a normal data path.

### Authority separation

| Concern | Authority home | Relationship to this README |
|---|---|---|
| Habitat doctrine and object scope | `docs/domains/habitat/` | Referenced; not redefined here. |
| Semantic object meaning | `contracts/domains/habitat/` | Candidate records cite accepted contracts. |
| Machine shape | `schemas/contracts/v1/domains/habitat/` or accepted successor | Candidate records cite accepted schema versions. |
| Source identity, role, rights, cadence, and admission | `data/registry/sources/habitat/` or ADR-selected source registry | Candidate records reference admitted sources. |
| Habitat policy and sensitivity decisions | `policy/domains/habitat/`, sensitivity policy, and emitted policy records | Candidate dossiers carry results; this README does not decide them. |
| RAW / WORK / QUARANTINE / PROCESSED bytes | corresponding `data/` lifecycle lanes | Candidate dossiers point to immutable artifacts. |
| Catalog and triplet projection | `data/catalog/` and `data/triplets/` | Candidate dossiers require closure; catalogs do not approve release. |
| Evidence and proof | accepted `data/proofs/` and EvidenceBundle homes | Candidate claims resolve support; proof is not promotion. |
| Process memory and receipts | `data/receipts/` | Candidate dossiers reference receipts; this lane does not replace them. |
| Tests, validators, fixtures, and pipelines | `tests/`, `tools/validators/`, `fixtures/`, `pipelines/` | Candidate review consumes outcomes; it does not own implementations. |
| Promotion decision | `release/promotion_decisions/` | Separate authoritative state-transition record. |
| Release manifest | `release/manifests/` | Separate release authority record. |
| Correction / withdrawal / rollback | shared release record families | Separate post-publication authority. |
| Published public-safe bytes | `data/published/` | Downstream only after release. |
| Public API/UI/AI behavior | governed application and runtime surfaces | Must consume released, policy-safe projections only. |

### This README cannot establish

This README cannot establish that:

- a source is admitted, current, authoritative, rights-cleared, or safe;
- a Habitat feature or model is ecologically correct;
- a candidate has passed schema, semantic, geometry, temporal, evidence, policy, review, or release gates;
- a regulatory designation exists;
- modeled suitability is observation;
- an ecoregion proves occurrence;
- a sensitive join is public-safe;
- a restoration or management recommendation is approved;
- a release exists;
- public bytes are deployed;
- rollback has been tested;
- a workflow result is release approval.

[Back to top](#top)

---

## Current candidate inventory

### Bounded direct inventory

| Path | Role | Current safe status |
|---|---|---|
| `release/candidates/habitat/README.md` | Parent Habitat candidate index and router | Present; documentation only. |
| `release/candidates/habitat/ecoregions/README.md` | Ecoregion candidate index | Present; no child candidate dossier established. |
| `release/candidates/habitat/habitat_fauna_thin_slice/README.md` | Cross-domain Habitat × Fauna candidate index | Present; no child candidate dossier established. |

### Candidate register

| Candidate ID | Sublane | State | Artifact pointer | Evidence closure | Policy / sensitivity | Review | Release handoff |
|---|---|---|---|---|---|---|---|
| _none established_ | — | `NO_ACTIVE_CANDIDATE` | — | — | — | — | — |

Do not add placeholder rows that resemble active release records. Add a candidate row only when a child dossier exists with stable identity, immutable artifact support, declared state, and reviewable gate status.

### Inventory interpretation

A child README is a lane index, not a candidate. A candidate exists only when a dossier or accepted candidate record:

- has deterministic identity;
- identifies immutable inputs and intended outputs;
- records object families and claim character;
- cites admitted source descriptors;
- resolves EvidenceBundle support for consequential claims;
- records rights, sensitivity, policy, validation, and review status;
- states correction, withdrawal, and rollback paths;
- carries a finite candidate state;
- remains separate from PromotionDecision and ReleaseManifest authority.

### Inventory update triggers

Update this section when:

- a governed child candidate dossier is added;
- a child candidate changes finite state;
- a child lane is added, renamed, moved, deprecated, or superseded;
- a candidate receives a PromotionDecision;
- a release manifest is issued;
- a candidate is corrected, withdrawn, denied, superseded, or rolled back;
- repository evidence invalidates the current no-active-candidate conclusion.

[Back to top](#top)

---

## Child-lane routing

Use the narrowest accepted candidate lane that preserves ownership and review burden.

| Candidate character | Candidate lane | Required boundary |
|---|---|---|
| General Habitat candidate not governed by a narrower accepted sublane | Parent lane or an ADR-approved child dossier path | Preserve Habitat object, source role, evidence, sensitivity, model, and release boundaries. |
| Ecoregion or biophysical-regionalization candidate | `ecoregions/` | Regionalization context is not occurrence, habitat-patch quality, critical-habitat, hydrology, parcel, or title truth. |
| Habitat × Fauna public-safe thin-slice candidate | `habitat_fauna_thin_slice/` | Habitat and Fauna ownership remain separate; most-restrictive sensitivity wins; geoprivacy and no-leak controls apply. |
| Land-cover candidate | **NEEDS VERIFICATION** | Do not invent a release child lane from docs or pipeline names without Directory Rules and repository evidence. |
| Suitability / connectivity / corridor candidate | **NEEDS VERIFICATION** | Models, observations, uncertainty, scale, and sensitive endpoints require explicit review. |
| Restoration or stewardship candidate | **NEEDS VERIFICATION** | Planning, recommendation, rights, parcel, named-party, sovereignty, and management authority must remain separate. |
| Regulatory critical-habitat candidate | **NEEDS VERIFICATION** | Regulatory source role and legal authority must not collapse into modeled Habitat. |
| Multi-domain candidate beyond the accepted thin slice | Lowest common responsibility root after ADR/review | Do not bury cross-domain authority inside Habitat by convenience. |

### Routing rules

1. Do not create a child folder merely because a topic appears in Habitat docs.
2. Check Directory Rules, current repository evidence, and visible ADRs before naming a path.
3. A child lane narrows review responsibility; it does not create new domain, release, policy, proof, or data authority.
4. Cross-domain candidates preserve owner-publishes / consumer-cites discipline.
5. Sensitive or sovereignty-bearing joins route through the most restrictive applicable review path.
6. If ownership is ambiguous, hold the candidate and resolve placement before adding a dossier.
7. Do not keep parallel candidate records in multiple child lanes.

[Back to top](#top)

---

## Candidate lifecycle

Candidate state is finite, explicit, and reviewable.

### Candidate states

| State | Meaning | Public effect |
|---|---|---|
| `PROPOSED` | Candidate identity or scope has been drafted. | None. |
| `ASSEMBLING` | Support pointers and gate evidence are being collected. | None. |
| `READY_FOR_REVIEW` | Required dossier fields are present and review can begin. | None. |
| `RESTRICTED_REVIEW` | Candidate contains or depends on controlled information and is limited to authorized reviewers. | None. |
| `BLOCKED` | One or more release gates cannot close. | None. |
| `REPAIR_REQUIRED` | Correctable validation, evidence, rights, sensitivity, or lineage defects exist. | None. |
| `DEFERRED` | Review is intentionally postponed without approval. | None. |
| `APPROVED_FOR_MANIFEST` | Independent review supports manifest assembly, subject to final shared release checks. | None by itself. |
| `PROMOTED` | A separate PromotionDecision and ReleaseManifest completed the governed transition. | Only released public-safe artifacts may become public. |
| `STALE` | Source, model, evidence, review, or candidate age exceeded declared tolerance. | No new promotion; public derivatives require stale-state handling. |
| `SUPERSEDED` | A newer candidate or release replaces this one. | Retain lineage; do not silently overwrite. |
| `WITHDRAWN` | Candidate was withdrawn before or after review. | No promotion. |
| `DENIED` | Candidate was rejected under policy, evidence, rights, sensitivity, or review rules. | No promotion. |

### Explicit hold reasons

Use machine- and human-readable hold reasons such as:

```text
HOLD_FOR_ARTIFACT
HOLD_FOR_IDENTITY
HOLD_FOR_SOURCE_ADMISSION
HOLD_FOR_SOURCE_ROLE
HOLD_FOR_RIGHTS
HOLD_FOR_SENSITIVITY
HOLD_FOR_GEOPRIVACY
HOLD_FOR_EVIDENCE
HOLD_FOR_MODEL_SUPPORT
HOLD_FOR_UNCERTAINTY
HOLD_FOR_PUBLIC_REPRESENTATION
HOLD_FOR_POLICY
HOLD_FOR_VALIDATION
HOLD_FOR_CATALOG_CLOSURE
HOLD_FOR_REVIEW
HOLD_FOR_RELEASE_TOPOLOGY
HOLD_FOR_CORRECTION_PATH
HOLD_FOR_WITHDRAWAL_PATH
HOLD_FOR_ROLLBACK
HOLD_FOR_STALE_DEPENDENCY
HOLD_FOR_CROSS_DOMAIN_OWNERSHIP
HOLD_FOR_SOVEREIGNTY_OR_CULTURAL_REVIEW
```

A hold is not a failure to document. It is a governed outcome that prevents unsupported promotion.

### State transition rules

- State changes require a recorded reason and actor or reviewing authority.
- `READY_FOR_REVIEW` does not imply gate success.
- `APPROVED_FOR_MANIFEST` does not publish bytes.
- `PROMOTED` requires separate authoritative release records.
- `STALE` is distinct from wrong, withdrawn, or denied.
- `SUPERSEDED` preserves the prior dossier and lineage.
- Corrections never silently rewrite historical decision records.
- Withdrawal and denial are not deletion instructions.
- A branch merge cannot set a candidate state by implication.

[Back to top](#top)

---

## What belongs here

Accepted material is limited to candidate indexes, dossiers, and review support that belongs in the release decision plane.

### Parent-lane material

- this parent README;
- child-lane routing and bounded candidate indexes;
- candidate-state summaries sourced from actual dossiers;
- safe review checklists;
- links to immutable candidate artifacts;
- links to SourceDescriptors, EvidenceBundles, validation reports, policy decisions, review records, catalogs, receipts, manifests, correction notices, withdrawal notices, and rollback cards;
- safe summaries of blockers and finite outcomes;
- migration, deprecation, supersession, and correction notes for candidate records;
- public-safe review templates that do not embed protected content.

### Candidate dossier material

A dossier may contain or reference:

- deterministic candidate identity and version;
- candidate owner and owning Habitat sublane;
- immutable artifact pointers and digests;
- object-family and claim-character declarations;
- source descriptor and source-role references;
- rights, license, terms, attribution, and redistribution status;
- evidence and citation closure;
- model identity, version, inputs, assumptions, support, and uncertainty where applicable;
- spatial support, CRS, precision, scale, resolution, and topology;
- temporal support and stale tolerance;
- sensitivity tier and audience class;
- named public-safe representation profile references;
- validation reports and finite outcomes;
- policy and review records;
- catalog and proof closure references;
- proposed public artifact and governed consumer surfaces;
- correction, withdrawal, supersession, and rollback paths;
- candidate state and decision rationale.

### Pointer-first rule

Keep dossiers compact and pointer-based. Do not copy canonical payloads, sensitive data, proof bundles, policy rules, or release records into candidate Markdown.

[Back to top](#top)

---

## What does not belong here

Do not place these materials under `release/candidates/habitat/`:

| Excluded material | Correct responsibility |
|---|---|
| RAW source downloads, archives, rasters, vectors, tables, media, or API dumps | `data/raw/` |
| Work products, temporary joins, model experiments, QA scratch, or transformation trials | `data/work/` |
| Rights-unclear, malformed, disputed, over-precise, or unsafe material | `data/quarantine/` |
| Normalized Habitat artifacts | `data/processed/habitat/` |
| STAC, DCAT, PROV, domain catalog, or triplet records | catalog and triplet roots |
| SourceDescriptor or activation records | source-registry authority |
| EvidenceBundle, ProofPack, or proof payloads | accepted proof/evidence homes |
| Run, transform, aggregation, model, redaction, policy, validation, review, AI, or release receipts as primary records | `data/receipts/` |
| Semantic contracts | `contracts/` |
| JSON Schemas | `schemas/` |
| Policy rules or sensitivity matrices | `policy/` |
| Validator, test, fixture, pipeline, connector, package, application, or workflow implementation | owning implementation roots |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, or RollbackCard as primary records | shared `release/` object-family homes |
| Public PMTiles, COG, GeoParquet, GeoJSON, API snapshots, reports, or exports | released `data/published/` lanes |
| Credentials, tokens, private agreements, restricted review substance, or secrets | approved secret/restricted systems |
| Exact sensitive occurrence, rare-plant, archaeology, cultural, stewardship, private-land, or infrastructure-sensitive detail | restricted lifecycle/review systems |
| Geoprivacy seeds, offsets, masks, thresholds, suppression logic, reversal keys, or hidden precision parameters | protected transform/policy implementation and receipts |
| Unreviewed generated Habitat claims | governed AI/review paths; never release evidence by themselves |

### Forbidden shortcuts

```text
README -> candidate truth
child folder -> active candidate
candidate -> release
processed artifact -> public artifact
catalog record -> release approval
proof pass -> PromotionDecision
schema-valid -> semantically valid
model output -> observation
suitability -> species occurrence
ecoregion -> habitat patch
critical-habitat label -> modeled suitability
regulatory record -> observed Habitat event
public style hiding a field -> redaction
generalized display -> source geometry safe
map tile -> canonical truth
graph edge -> evidence
AI summary -> EvidenceBundle
CODEOWNERS routing -> independent review
green workflow hold -> release readiness
```

[Back to top](#top)

---

## Candidate admission contract

A candidate should not enter `READY_FOR_REVIEW` until every applicable field is supplied or explicitly held.

### Identity and placement

- [ ] `candidate_id` is stable and deterministic.
- [ ] `candidate_version` is immutable.
- [ ] owning domain is `habitat`.
- [ ] owning sublane or cross-domain relationship is explicit.
- [ ] placement was checked against Directory Rules, current repository evidence, and visible ADRs.
- [ ] candidate is not duplicated in another release lane.
- [ ] supersession and prior-candidate refs are explicit where applicable.

### Artifact and lifecycle support

- [ ] candidate artifacts are stored in the correct upstream lifecycle lane.
- [ ] immutable artifact URIs or repository paths are present.
- [ ] digests identify exact reviewed bytes.
- [ ] source, processing, catalog, proof, and release-stage artifacts remain distinct.
- [ ] intended public artifacts and audience are declared.
- [ ] no candidate bytes are treated as public merely because a path is visible.

### Habitat scope

- [ ] object families are declared.
- [ ] claim character is declared for every material output.
- [ ] Habitat-owned and adjacent-domain objects remain distinguishable.
- [ ] observation, model, aggregate, administrative, regulatory, candidate, and synthetic content remain labeled.
- [ ] uncertainty and limitations are explicit.
- [ ] legal, regulatory, management, ecological, and life-safety non-authority is explicit where material.

### Source and rights

- [ ] every source resolves to an admitted SourceDescriptor.
- [ ] source role is canonical and preserved.
- [ ] rights, license, terms, attribution, redistribution, and derivative-use posture are resolved.
- [ ] source vintage, cadence, supersession, and stale tolerance are recorded.
- [ ] controlled or terms-limited sources remain fail-closed.
- [ ] watchers or source freshness checks do not promote or publish.

### Evidence and citations

- [ ] consequential claims resolve `EvidenceRef -> EvidenceBundle`.
- [ ] evidence identifies source, claim, time, scope, and limitations.
- [ ] evidence does not rely solely on generated language, maps, models, or aggregate summaries.
- [ ] conflicting evidence is surfaced rather than silently flattened.
- [ ] missing support returns hold, abstain, deny, or error as appropriate.

### Spatial and temporal support

- [ ] geometry type, CRS, datum, scale, resolution, precision, extent, and topology are explicit.
- [ ] source geometry and public representation are distinct.
- [ ] observed, valid, retrieval, processing, model-run, review, release, correction, and supersession times remain separate where material.
- [ ] stale state is deterministic and reviewable.
- [ ] crosswalks, resampling, classification changes, and generalization are named and receipted.

### Sensitivity and public representation

- [ ] base-object sensitivity is declared.
- [ ] resulting-product sensitivity is recalculated after every join.
- [ ] most-restrictive applicable posture wins.
- [ ] exact or inferential sensitive exposure is denied by default.
- [ ] public-safe transforms are named and versioned.
- [ ] required RedactionReceipt, AggregationReceipt, RepresentationReceipt, or equivalent exists.
- [ ] public field allowlists are explicit.
- [ ] no-leak checks cover files, tiles, APIs, popups, exports, search, graph, logs, caches, screenshots, and AI.
- [ ] restricted transform parameters do not appear in public review material.

### Model and uncertainty support

- [ ] model identity, version, inputs, parameters, spatial/temporal support, and assumptions are recorded.
- [ ] observation and model output remain distinct.
- [ ] training, calibration, validation, and release datasets remain distinguishable.
- [ ] uncertainty surfaces and limitations travel with the public representation.
- [ ] model output does not acquire legal, regulatory, occurrence, or management authority.
- [ ] corrections to model inputs trigger downstream review.

### Validation, policy, and review

- [ ] semantic, schema, source-role, geometry, temporal, evidence, sensitivity, public-representation, and release checks have finite outcomes.
- [ ] policy result is linked.
- [ ] review record is linked where required.
- [ ] independent review is separated from authoring where materiality or sensitivity requires it.
- [ ] unresolved findings are represented as holds, not hidden in prose.
- [ ] workflow success is not substituted for gate evidence.

### Release and reversibility

- [ ] proposed public artifacts and audiences are explicit.
- [ ] candidate-to-PromotionDecision handoff is defined.
- [ ] candidate-to-ReleaseManifest handoff is defined.
- [ ] correction path is actionable.
- [ ] withdrawal path is actionable.
- [ ] supersession lineage is explicit.
- [ ] rollback target is immutable and verified.
- [ ] derivative invalidation includes tiles, caches, search, graphs, embeddings, previews, exports, and AI indexes where applicable.
- [ ] rollback does not restore unsafe precision or revoked content.

### Admission outcomes

```text
ADMIT_FOR_ASSEMBLY
READY_FOR_REVIEW
RESTRICTED_REVIEW
HOLD
REPAIR_REQUIRED
DEFER
DENY
WITHDRAW
```

No admission outcome publishes anything.

[Back to top](#top)

---

## Habitat identity, object family, and source role

### Habitat object families

Candidate dossiers should preserve the accepted or currently documented Habitat families rather than use generic “habitat data” labels:

| Object family | Candidate-review concern |
|---|---|
| `HabitatPatch` | Boundary basis, source support, classification, time, uncertainty, joins, and public precision. |
| `LandCoverObservation` | Observation date, classification scheme, source role, resolution, crosswalk, and change semantics. |
| `EcologicalSystem` | Classification authority, source version, crosswalk support, uncertainty, and controlled-source posture. |
| `HabitatQualityScore` | Method, inputs, weights, scale, uncertainty, interpretation limits, and non-authority. |
| `SuitabilityModel` | Model identity, inputs, assumptions, validation, uncertainty, sensitive training/support data, and model-not-observation boundary. |
| `ConnectivityEdge` | Endpoint identity, cost/impedance method, scale, sensitive-site inference, uncertainty, and graph projection boundary. |
| `Corridor` | Model/support basis, endpoint sensitivity, precision, uncertainty, planning posture, and public generalization. |
| `RestorationOpportunity` | Planning-not-approval posture, model support, rights, parcel/named-party sensitivity, review, and uncertainty. |
| `StewardshipZone` | Administrative/stewardship role, rights, sovereignty, named-party detail, audience, and public-safe representation. |
| `ModelRunReceipt` | Process memory, input/output digests, model version, uncertainty, and no embedded sensitive payload. |
| `UncertaintySurface` | Method, scale, resolution, semantics, sensitivity, and required paired display. |

This table is review guidance, not an assertion that all families have accepted machine contracts or active candidate instances.

### Canonical source-role posture

Use the repository's documented seven-role Habitat release vocabulary where accepted:

```text
observed
regulatory
modeled
aggregate
administrative
candidate
synthetic
```

### Terminology conflict

Habitat and source documents may also use terms such as:

```text
authority
context
model
representation
compiled
derived
```

Those terms may describe authority scope, use case, product character, or legacy vocabulary. They must not silently become source-role values in claim-bearing candidates.

Until an accepted crosswalk exists:

- preserve the native or legacy term as metadata;
- map to an accepted canonical role only with evidence and review;
- record the mapping version and reason;
- hold ambiguous mappings;
- never upgrade source authority through a label change.

### Deterministic identity expectations

A candidate should distinguish:

- canonical Habitat object ID;
- source-native ID;
- source version;
- candidate ID;
- candidate version;
- model/run ID;
- artifact digest;
- public representation ID;
- catalog ID;
- release ID;
- correction and supersession IDs.

Human-readable names are labels, not identity.

[Back to top](#top)

---

## Habitat anti-collapse rules

Habitat is especially vulnerable to plausible-looking authority upgrades. Keep these distinctions explicit.

### Object and claim distinctions

```text
land-cover observation != habitat patch
habitat patch != ecological system
ecoregion != habitat patch
habitat quality score != observed condition
suitability model != species occurrence
corridor != legal access or management approval
restoration opportunity != restoration decision
stewardship zone != land ownership
administrative context != ecological observation
regulatory critical habitat != modeled habitat
aggregate result != per-feature observation
candidate layer != released layer
uncertainty surface != evidence of absence
```

### Cross-domain distinctions

```text
Habitat context != Fauna occurrence truth
Habitat context != Flora occurrence truth
Habitat context != Hydrology truth
Habitat context != Soil truth
Habitat context != Hazard authority
Habitat context != Agriculture truth
Habitat context != Archaeology truth
Habitat context != parcel/title truth
Habitat relation != ownership transfer
joined product != permission to expose either input
```

### Evidence and representation distinctions

```text
map display != canonical geometry
style omission != redaction
generalized tile != proof source is safe
catalog record != EvidenceBundle
EvidenceBundle != PolicyDecision
proof pass != ReviewRecord
ReviewRecord != PromotionDecision
PromotionDecision != ReleaseManifest
ReleaseManifest != deployed bytes
generated explanation != source evidence
```

### Model, observation, and regulatory separation

Every model-bearing candidate must make clear:

- what is observed;
- what is regulatory;
- what is modeled;
- what is administrative;
- what is aggregated;
- what is candidate or synthetic;
- which claims are interpretation only;
- which evidence supports each claim;
- which uncertainty and limitations apply.

A model cannot become observation by validation score, map rendering, or repeated citation. A regulatory layer cannot become observed habitat condition. An observation cannot create legal designation.

### Regulatory critical-habitat rule

Where critical-habitat material is in scope:

- preserve `regulatory` source role;
- cite the authoritative regulatory source;
- keep modeled suitability and regulatory designation separate;
- do not imply legal effect from Habitat modeling;
- keep effective dates, amendments, withdrawals, and jurisdiction explicit;
- route legal interpretation outside this candidate lane;
- fail closed when status or source authority is unresolved.

[Back to top](#top)

---

## Sensitivity, geoprivacy, rights, and public-safe representation

### Join-induced sensitivity

Habitat's dominant sensitivity risk is often the resulting product, not the base Habitat object.

A public Habitat patch can become restricted when joined, co-rendered, summarized, indexed, or inferred with:

- sensitive Fauna occurrences, nests, dens, roosts, hibernacula, spawning sites, migration bottlenecks, or disease/mortality records;
- rare or culturally sensitive Flora records;
- archaeology or cultural-resource locations;
- private parcel, owner, operator, partner, or access information;
- sovereignty-controlled or stewardship-restricted material;
- vulnerable infrastructure or security-sensitive context;
- other controlled evidence whose location can be reconstructed.

The resulting product inherits the most restrictive applicable posture.

### Default outcomes

| Condition | Default outcome |
|---|---|
| Exact sensitive or reverse-engineerable location | `DENY` public exposure. |
| Sensitive join with unresolved policy or review | `HOLD_FOR_SENSITIVITY` or `DENY`. |
| Rights or terms unclear | `HOLD_FOR_RIGHTS` or `DENY`. |
| Public-safe derivative is possible but not yet produced | `HOLD_FOR_GEOPRIVACY`. |
| Transform exists but receipt or review is missing | `HOLD_FOR_PUBLIC_REPRESENTATION`. |
| Evidence is insufficient | `ABSTAIN` or `HOLD_FOR_EVIDENCE`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`; never fail open. |
| Safe representation and all gates close | Candidate may advance to review; still not released. |

### Public-safe transform requirements

A candidate may reference a public-safe representation only when:

- the transform/profile is named and versioned;
- the source and derived geometry remain distinct;
- the transformation is reproducible by authorized tooling;
- the transform emits the required receipt;
- public fields are allowlisted;
- hidden/internal fields cannot leak through alternate carriers;
- sensitive joins are re-evaluated after transformation;
- the output is tested for direct and inferential reconstruction;
- authorized reviewers approve the audience class;
- correction and rollback can invalidate every derivative.

Do not put operational transform parameters, random seeds, offsets, masks, suppression thresholds, hidden precision logic, or reversal aids in this public README or public candidate dossier.

### All-surface no-leak rule

Review must cover:

- source and derivative files;
- PMTiles, MVT, COG, GeoParquet, GeoJSON, CSV, and report exports;
- governed API payloads;
- map popups and hover state;
- Evidence Drawer payloads;
- search indexes and snippets;
- graph/triplet projections;
- vector indexes and embeddings;
- caches and CDNs;
- logs, traces, metrics, and error messages;
- screenshots, previews, and thumbnails;
- AI prompts, context windows, summaries, and citations;
- correction and rollback artifacts.

A safe map layer with an unsafe search index is an unsafe release.

### Rights and sovereignty

- rights and source terms travel with the candidate;
- controlled sources remain controlled after transformation;
- public-source status does not waive joined sensitivity;
- lack of response is not consent;
- sovereignty, cultural authority, consent, embargo, and revocation remain governed outside this README;
- a candidate cannot downgrade restrictions through aggregation or narrative;
- revoked or expired permission fails closed and triggers derivative review.

[Back to top](#top)

---

## Time, vintage, model, and stale state

Habitat candidates must distinguish time kinds rather than use one generic timestamp.

### Time fields

| Time kind | Meaning |
|---|---|
| `source_time` | Time represented or published by the upstream source. |
| `observed_time` | Time an observation or survey applies to. |
| `valid_time` | Time interval during which a claim or model output is intended to apply. |
| `retrieval_time` | Time KFM retrieved the source. |
| `processing_time` | Time a transform or pipeline ran. |
| `model_run_time` | Time a model was executed. |
| `review_time` | Time a review decision was recorded. |
| `release_time` | Time a release becomes authoritative for its audience. |
| `correction_time` | Time a correction is issued. |
| `supersession_time` | Time a successor replaces a candidate or release. |

### Vintage and stale rules

A candidate becomes `STALE` or blocked when:

- an admitted source exceeds its declared cadence or tolerance;
- a source is superseded or withdrawn;
- a model depends on stale inputs;
- an EvidenceBundle is invalidated;
- a related domain issues a correction that affects the candidate;
- rights, terms, consent, or access conditions expire;
- a review expires or becomes inapplicable;
- a public representation no longer matches its source or policy profile;
- a rollback target is no longer valid.

Stale does not automatically mean false. It means the candidate cannot be represented as current without explicit stale labeling and review.

### Model-specific time

Model candidates must preserve:

- training-data vintage;
- calibration and validation periods;
- model version;
- model-run time;
- prediction or validity interval;
- input source versions;
- stale tolerance;
- correction and rerun triggers.

A newer model does not silently supersede an older candidate or release. Supersession requires explicit lineage and review.

### Correction propagation

Time or vintage corrections must propagate to:

- candidate state;
- evidence and catalog references;
- public artifacts if released;
- tiles and caches;
- search and graph projections;
- summaries and reports;
- AI indexes and generated-answer context;
- derivative cross-domain products.

[Back to top](#top)

---

## Habitat release gates

A candidate cannot advance to `APPROVED_FOR_MANIFEST` until all applicable gates close.

### Gate A — identity and placement

- deterministic candidate identity;
- correct parent or child lane;
- no duplicate authority;
- object families and claim character declared;
- supersession lineage explicit.

### Gate B — source and rights closure

- admitted SourceDescriptors;
- canonical source roles;
- authority limits;
- rights, terms, attribution, and redistribution resolved;
- source cadence, vintage, and stale tolerance recorded.

### Gate C — semantic and model closure

- accepted contract refs;
- observation/model/regulatory/administrative/aggregate distinctions;
- crosswalk and classification semantics;
- uncertainty and limitations;
- adjacent-domain ownership preserved.

### Gate D — spatial and temporal closure

- CRS, datum, geometry, precision, scale, resolution, topology, and extent;
- source versus public representation;
- time kinds and valid intervals;
- generalization or aggregation receipts;
- stale-state evaluation.

### Gate E — evidence and catalog closure

- all material claims resolve EvidenceBundles;
- citations are safe and inspectable;
- catalog/triplet records resolve;
- digests bind reviewed artifacts;
- graph and search projections preserve claim character and sensitivity.

### Gate F — sensitivity, policy, and public-representation closure

- resulting-product sensitivity evaluated;
- rights and audience class resolved;
- geoprivacy/public-safe representation validated;
- public field allowlist approved;
- all-surface no-leak checks completed;
- PolicyDecision and required review records linked.

### Gate G — validation and independent review

- deterministic tests and validators completed;
- finite outcomes recorded;
- unresolved findings held;
- reviewer separation applied where required;
- workflow or tool limitations surfaced;
- generated summaries are not used as primary support.

### Gate H — release, correction, and rollback closure

- proposed public artifacts declared;
- candidate-to-PromotionDecision handoff defined;
- candidate-to-ReleaseManifest handoff defined;
- correction and withdrawal paths actionable;
- supersession lineage explicit;
- rollback target verified;
- derivative invalidation and safe restoration tested.

### Gate outcomes

```text
PASS
HOLD
RESTRICT
ABSTAIN
DENY
ERROR
REPAIR_REQUIRED
```

A green held workflow is not a gate pass unless the workflow contract explicitly produces and validates the required authoritative artifacts.

[Back to top](#top)

---

## Required dossier structure

Use a child directory or accepted candidate-record format only after placement is verified.

### Public-safe Markdown template

```markdown
<!-- [KFM_META_BLOCK_V2_TEMPLATE]
doc_id: kfm://release/candidate/habitat/<candidate-id>
title: <candidate title>
type: habitat-release-candidate-dossier
version: <immutable candidate version>
status: PROPOSED
domain: habitat
sublane: <verified sublane or none>
candidate_id: <stable id>
artifact_digest: <digest or manifest ref>
policy_label: <safe review label>
[/KFM_META_BLOCK_V2_TEMPLATE] -->

# <Candidate title>

## Candidate state

`PROPOSED | ASSEMBLING | READY_FOR_REVIEW | RESTRICTED_REVIEW | BLOCKED | REPAIR_REQUIRED | DEFERRED | APPROVED_FOR_MANIFEST | STALE | SUPERSEDED | WITHDRAWN | DENIED`

## Scope and authority boundary

- Habitat object families:
- claim character:
- owning sublane:
- adjacent-domain refs:
- non-authority statement:

## Artifact identity

- immutable artifact refs:
- digests:
- schema/contract refs:
- prior/superseded candidate refs:
- intended public artifacts:

## Sources, roles, rights, and time

- admitted SourceDescriptor refs:
- canonical roles:
- rights / terms / attribution:
- source and valid times:
- cadence / stale tolerance:

## Model and uncertainty support

- model/run refs:
- observation/model/regulatory separation:
- uncertainty refs:
- limitations:
- rerun/correction triggers:

## Evidence and catalog closure

- EvidenceBundle refs:
- validation refs:
- catalog/triplet refs:
- unresolved conflicts:

## Sensitivity and public representation

- base sensitivity:
- resulting-product sensitivity:
- audience:
- public-safe profile refs:
- receipt refs:
- public field allowlist:
- no-leak summary:
- restricted detail location: <pointer only; do not embed>

## Policy and review

- PolicyDecision ref:
- ReviewRecord refs:
- independent reviewer:
- finite outcomes:
- open holds:

## Release handoff

- proposed PromotionDecision ref:
- proposed ReleaseManifest ref:
- release target:
- release state: not_released

## Correction, withdrawal, and rollback

- correction path:
- withdrawal path:
- supersession path:
- rollback target:
- derivative invalidation:
- safe restoration rule:

## Decision

- current state:
- reason:
- decided by:
- decision time:
```

### Template restrictions

The public dossier must not include:

- exact sensitive locations;
- restricted source payloads;
- private names, parcel details, agreements, or access routes;
- source credentials;
- geoprivacy reversal parameters;
- internal join keys that reconstruct controlled records;
- unredacted logs or evidence;
- generated claims presented as facts;
- approval language unsupported by authoritative records.

[Back to top](#top)

---

## Validation, proof, fixture, schema, and policy posture

### Current maturity boundary

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Habitat candidate parent | Present | Index and router only. |
| Ecoregions child | Repository-grounded README | No child candidate dossier established. |
| Habitat × Fauna thin-slice child | Repository-grounded README | No child candidate dossier established. |
| Habitat release index | Draft docs mirror | Illustrative/proposed entries do not establish releases. |
| Habitat proof lane | Draft guide; implementation depth stated unknown | No accepted proof producer or proof inventory established. |
| Habitat policy | Greenfield scaffold | Executable policy enforcement not established. |
| Habitat tests | Documentation plus placeholder/scaffold modules | Accepted deterministic suite and pass rate need verification. |
| Habitat validators | Documentation plus placeholder/scaffold modules | Accepted validator ownership and command need verification. |
| Habitat workflow | Explicit validation, proof, and release-readiness logic | Maturity detection only; not Habitat truth or release authority. |
| General release dry run | Existing TODO steps | Not candidate assembly, promotion enforcement, or rollback proof. |

### Required validation families

A mature candidate should have deterministic, no-network, synthetic/public-safe tests for:

- object-family identity;
- source-role preservation;
- model-versus-observation separation;
- regulatory-versus-modeled separation;
- schema and semantic contract conformance;
- evidence resolution and citation safety;
- time, vintage, and stale-state behavior;
- geometry, CRS, topology, scale, and uncertainty;
- sensitive-join inheritance;
- geoprivacy and no-leak behavior;
- public field allowlists;
- catalog closure;
- public trust-membrane behavior;
- candidate-state transitions;
- correction, withdrawal, supersession, and rollback;
- cross-domain owner-publishes / consumer-cites behavior;
- AI evidence-before-model and cite-or-abstain behavior.

### Fixture rules

Fixtures must be:

- synthetic and public-safe;
- deterministic and no-network;
- compact and reviewable;
- explicit about object family, source role, model role, evidence, time, sensitivity, audience, release state, and expected outcome;
- free of real protected locations, private details, credentials, or restricted payloads;
- paired with expected outputs where practical;
- incapable of being mistaken for live evidence or released data.

### Proof rules

A proof or proof-harness result:

- demonstrates bounded behavior;
- does not create EvidenceBundle truth by itself;
- does not decide policy;
- does not approve release;
- does not authorize public exposure;
- must bind exact inputs, outputs, contracts, policy state, and receipts;
- must remain correctable and rollback-aware.

### Schema rules

Schema validity proves shape only. It does not prove:

- semantic validity;
- source admission;
- evidence closure;
- rights clearance;
- sensitivity safety;
- model validity;
- ecological truth;
- review approval;
- release state.

### Policy rules

Policy is fail-closed. Missing or unavailable policy support returns a finite non-public outcome. Candidate prose cannot substitute for machine or steward decisions.

[Back to top](#top)

---

## Automation posture

### Current domain workflow

`.github/workflows/domain-habitat.yml` is a read-only readiness workflow. Its documented authority boundary says it does not:

- validate Habitat truth;
- establish species presence;
- issue legal or regulatory interpretations;
- build EvidenceBundles or ProofPacks;
- admit sources;
- apply policy;
- perform geoprivacy transforms;
- promote lifecycle artifacts;
- approve release;
- write published data;
- deploy or publish.

It currently contains:

- `validate-habitat`;
- `build-proof-habitat`;
- `publish-dry-run-habitat`.

The workflow preserves explicit hold behavior while accepted executable validation, proof production, and release-dry-run contracts remain unestablished.

### Compatibility marker

The current release-readiness job checks for this exact sentence:

```text
A candidate is not a release.
```

Retaining the sentence is workflow compatibility only. It is not proof that:

- the candidate inventory is complete;
- a release gate passed;
- policy approved;
- evidence closed;
- rollback is ready;
- public output is safe.

### Candidate-record detector

The current release-readiness job searches recursively for non-README, non-`.gitkeep` files under `release/candidates/habitat/`.

Therefore:

- adding a non-README candidate record should deliberately trigger workflow graduation or review;
- hiding a candidate in Markdown to avoid the detector is not acceptable;
- adding a candidate payload to satisfy documentation is not acceptable;
- changing the workflow to ignore a real candidate merely to make CI green is not acceptable.

### Validation detector posture

The validation job inspects test and validator trees for executable bodies. Placeholder and scaffold growth has already created detector ambiguity and failures in recent workflow runs.

Safe posture:

- do not represent a failing maturity detector as a candidate failure without exact evidence;
- do not suppress the detector simply to make CI green;
- inspect the exact triggering file or AST node;
- distinguish placeholder files from accepted executable coverage;
- graduate the workflow only with accepted contracts, fixtures, no-network behavior, ownership, policy, evidence, and reviewer support.

### General release dry run

The shared `.github/workflows/release-dry-run.yml` currently contains TODO-only jobs for candidate assembly, promotion gate checking, and rollback-card presence.

A green result from those TODO steps is not:

- candidate assembly;
- promotion enforcement;
- manifest validation;
- rollback verification;
- release proof.

### Automation cannot approve

No workflow result can replace:

- SourceDescriptor admission;
- EvidenceBundle closure;
- PolicyDecision;
- required human or steward review;
- PromotionDecision;
- ReleaseManifest;
- CorrectionNotice;
- WithdrawalNotice;
- RollbackCard.

[Back to top](#top)

---

## Review and release handoff

### Review roles

Depending on candidate scope, review may require:

- Habitat domain steward;
- owning sublane steward;
- source and rights steward;
- evidence/proof steward;
- model and uncertainty reviewer;
- spatial/CRS/topology reviewer;
- sensitivity/geoprivacy reviewer;
- Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Archaeology, People/Land, or other adjacent-domain reviewer;
- cultural or sovereignty authority where applicable;
- policy steward;
- validation/QA steward;
- release steward;
- independent reviewer for material or sensitive changes.

### Separation of duties

At minimum:

- candidate authoring is separate from final release authority;
- transform authoring is separate from required sensitivity review where practical;
- source admission is separate from release approval;
- model authoring is separate from consequential model review where practical;
- proof production is separate from PromotionDecision;
- CODEOWNERS routing does not satisfy independent review automatically.

### Handoff sequence

```text
candidate dossier
  -> source / rights / evidence / sensitivity / validation review
  -> child-lane and cross-domain review where applicable
  -> READY_FOR_REVIEW or finite hold
  -> independent review
  -> APPROVED_FOR_MANIFEST or DENIED / DEFERRED / REPAIR_REQUIRED
  -> PromotionDecision
  -> ReleaseManifest
  -> released public-safe artifact
  -> governed API / map / export / search / graph / AI surfaces
```

### Shared release routes

Candidate dossiers should hand off by reference to existing shared release object families:

| Record | Shared route |
|---|---|
| PromotionDecision | `release/promotion_decisions/` |
| ReleaseManifest | `release/manifests/` |
| CorrectionNotice | `release/correction_notices/` |
| WithdrawalNotice | `release/withdrawal_notices/` |
| RollbackCard | `release/rollback_cards/` |
| Release changelog | `release/changelog/` |

Do not create Habitat-specific parallel homes for shared release records without an accepted ADR or migration plan.

### Handoff denial conditions

Do not advance when:

- candidate identity is unstable;
- artifact bytes are mutable or unbound;
- source roles are ambiguous;
- rights or terms are unresolved;
- evidence does not close;
- model/observation/regulatory distinctions are unclear;
- resulting sensitivity is unresolved;
- public representation is not validated;
- review is missing;
- correction or rollback is not actionable;
- candidate placement conflicts with Directory Rules;
- a workflow is green only because it is held or TODO-only.

[Back to top](#top)

---

## Correction, withdrawal, supersession, and rollback

### Correction

A correction is required when:

- source or evidence is wrong;
- source role or claim character was misclassified;
- geometry, CRS, topology, scale, or precision is wrong;
- model inputs, assumptions, outputs, uncertainty, or labels are wrong;
- sensitivity or public-safe representation is wrong;
- public fields leak controlled context;
- a related domain correction invalidates a join;
- rights, terms, consent, sovereignty, or access posture changes;
- release lineage or digest references are wrong.

Correction must identify:

- affected candidate and release IDs;
- prior and corrected claims;
- evidence and source changes;
- impacted artifacts and audience;
- derivative invalidation;
- review requirements;
- whether withdrawal or rollback is required.

### Withdrawal

Withdraw a candidate when:

- rights or terms prohibit continued use;
- sensitive exposure cannot be made safe;
- evidence is retracted or inadequate;
- source authority is invalidated;
- consent, agreement, or authority is revoked;
- the candidate is abandoned;
- correction cannot preserve trustworthy lineage.

Withdrawal is a recorded state, not deletion of history.

### Supersession

A successor candidate must state:

- `supersedes`;
- reason;
- changed sources, models, contracts, schemas, policy, evidence, or representation;
- migration and compatibility effect;
- stale and correction implications;
- rollback relationship.

Do not silently edit a prior candidate into a successor.

### Rollback

A rollback plan must identify:

- target prior release;
- exact artifacts and digests;
- release records;
- tiles, caches, APIs, search, graph, embeddings, previews, reports, and exports to invalidate;
- public notices or correction state;
- sensitive material that must remain suppressed;
- verification that rollback will not restore revoked, stale, unsupported, or over-precise data.

### Candidate-only rollback

Before promotion, rollback usually means:

- close the review;
- withdraw or supersede the candidate;
- retain audit history;
- revert documentation or candidate-index changes;
- leave canonical source, evidence, policy, and release histories intact.

### Post-release rollback

After release, use authoritative CorrectionNotice and RollbackCard paths. Do not implement rollback as a hidden file copy or pointer edit.

[Back to top](#top)

---

## Public API, map, export, search, graph, and AI boundary

### Normal public path

```text
released public-safe artifact
  -> release and catalog resolution
  -> governed API / layer resolver
  -> map, export, search, graph, Evidence Drawer, or AI surface
```

### Forbidden public paths

```text
release/candidates/habitat/
  -> public API

data/raw|work|quarantine|processed/
  -> public UI

candidate artifact
  -> map layer without ReleaseManifest

model output
  -> public claim without EvidenceBundle and policy

proof result
  -> public artifact

graph or vector index
  -> canonical truth
```

### Map boundary

MapLibre and other map clients:

- render released public-safe representations only;
- do not read candidate, proof, policy, registry, or canonical stores directly;
- preserve source role, model role, time, uncertainty, sensitivity, stale state, and release state;
- cannot hide sensitive fields merely through styling;
- must resolve evidence and correction state through governed interfaces.

### Export boundary

Exports must preserve:

- release ID;
- schema/contract version;
- source and evidence refs;
- audience and policy state;
- time and stale state;
- sensitivity and public-representation posture;
- correction and rollback refs;
- artifact digest.

### Search and graph boundary

Search and graph projections:

- remain derived carriers;
- cannot strengthen claim authority;
- must preserve owner domain and source role;
- must not reconstruct sensitive locations through joins or facets;
- must be invalidated on correction, withdrawal, supersession, or rollback;
- must not index candidate or restricted material for public use.

### AI boundary

Governed AI may:

- summarize released EvidenceBundles;
- compare released support;
- explain limitations, uncertainty, stale state, and correction history;
- draft non-authoritative review notes.

Governed AI may not:

- treat candidate prose as evidence;
- read candidate or restricted payloads as the normal public path;
- create source admission, policy, review, or release state;
- infer sensitive locations;
- upgrade models or context into observations;
- issue legal, regulatory, ecological-management, or life-safety authority;
- answer without citation when evidence is required.

Finite runtime outcomes remain:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

[Back to top](#top)

---

## Maintenance and definition of done

### Maintenance rules

Update this README when:

- a candidate or child lane is added;
- child-lane placement changes;
- a candidate state changes;
- source-role vocabulary changes;
- Habitat object-family contracts change;
- sensitivity or public-representation policy changes;
- a test, validator, proof producer, or release command graduates;
- release record topology changes;
- correction or rollback procedures change;
- current evidence invalidates the no-active-candidate conclusion.

### Definition of done for this parent lane

The parent lane is mature when:

- [ ] candidate inventory is generated deterministically from governed records;
- [ ] each child lane has accepted placement and ownership;
- [ ] candidate identity and manifest contracts are accepted;
- [ ] SourceDescriptor, rights, evidence, sensitivity, model, and public-representation contracts are accepted;
- [ ] finite states and holds validate machine-readably;
- [ ] deterministic no-network fixtures and tests exist;
- [ ] validators are owned and wired;
- [ ] policy enforcement is executable and fail-closed;
- [ ] EvidenceRef-to-EvidenceBundle resolution is proven;
- [ ] catalog closure is enforced;
- [ ] candidate-to-PromotionDecision and candidate-to-ReleaseManifest handoffs are tested;
- [ ] correction, withdrawal, supersession, and rollback paths are exercised;
- [ ] public API/map/export/search/graph/AI no-leak behavior is tested;
- [ ] branch protection and required checks are verified;
- [ ] independent review assignments are explicit;
- [ ] generated indexes remain mirrors, not sovereign truth.

### Documentation quality checks

- one rendered H1;
- one closed KFM Meta Block;
- balanced code fences;
- valid internal navigation;
- no duplicate rendered anchors;
- no trailing whitespace;
- final newline;
- repository-relative references resolve;
- truth labels match current evidence;
- no protected details or reversal aids;
- rollback target is explicit.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Prior `release/candidates/habitat/README.md` blob `bd0ccc0d…` | **CONFIRMED** | Parent lane existed with two named child lanes and candidate-not-release posture. | Generic and stale relative to current child indexes. |
| Current `main@7b9c4592fc…` | **CONFIRMED** | Pinned repository snapshot for this revision. | Repository may advance after branch creation. |
| `release/candidates/habitat/ecoregions/README.md` blob `d8946a71…` | **CONFIRMED** | Ecoregions child lane is repository-grounded and reports no child candidate dossier. | Does not establish exhaustive hidden/runtime inventory. |
| `release/candidates/habitat/habitat_fauna_thin_slice/README.md` blob `d5c3990b…` | **CONFIRMED** | Thin-slice child lane is repository-grounded and reports no child candidate dossier. | Does not establish proof execution or release. |
| Bounded candidate-path search | **CONFIRMED / search-limited** | Surfaced the parent and two child indexes. | Search is not a complete filesystem or restricted-system inventory. |
| `.github/workflows/domain-habitat.yml` blob `edf20c99…` | **CONFIRMED** | Defines read-only readiness checks, candidate-not-release marker, recursive non-README candidate detector, proof hold, and release hold. | Workflow logic is not Habitat truth, policy, review, or release authority. |
| `docs/domains/habitat/RELEASE_INDEX.md` | **CONFIRMED draft docs mirror** | Documents release object families, correction, rollback, stale state, source-role, and sensitivity posture. | Illustrative/proposed rows do not establish releases. |
| `docs/domains/habitat/HABITAT_SENSITIVITY_PROFILE.md` | **CONFIRMED draft profile** | Documents join-induced sensitivity and most-restrictive-result posture. | Profiles doctrine; does not itself decide or enforce policy. |
| `data/proofs/habitat/README.md` | **CONFIRMED draft guide** | States implementation depth remains unknown and separates proof from release. | No accepted proof producer or inventory established. |
| `policy/domains/habitat/README.md` | **CONFIRMED scaffold** | Identifies policy responsibility lane. | Does not establish executable Habitat policy. |
| Habitat test and validator surfaces | **CONFIRMED mixed docs/placeholders; NEEDS VERIFICATION** | Demonstrate planned enforceability and current detector inputs. | Accepted suite, ownership, pass rate, and exact workflow failure triggers remain unresolved. |
| `.github/workflows/release-dry-run.yml` | **CONFIRMED TODO-only behavior in recent runs** | Shows shared release automation exists. | Green TODO steps are not release proof. |
| `.github/CODEOWNERS` | **CONFIRMED routing evidence** | Routes repository review. | Not stewardship, independent review, or release approval. |
| Directory Rules | **CONFIRMED governing doctrine** | Supports responsibility-root placement and separation of release, data, policy, proof, schema, and public-client authority. | Does not prove runtime implementation. |

### Evidence precedence

When materials conflict:

1. authoritative current release, policy, review, and evidence records;
2. current repository implementation, tests, workflows, and generated outputs;
3. governing doctrine and accepted ADRs;
4. this parent index;
5. generated summaries.

This README must be corrected when higher-authority evidence changes.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive recursive Habitat candidate inventory through a repository tree or governed index.
- [ ] Confirm deterministic candidate-index generation.
- [ ] Confirm canonical candidate ID, version, dossier, and artifact-manifest contracts.
- [ ] Confirm parent-versus-child routing rules and ownership.
- [ ] Confirm accepted Habitat object-family contracts and schema topology.
- [ ] Confirm canonical source-role vocabulary and legacy-term crosswalks.
- [ ] Confirm source-registry topology and admitted Habitat SourceDescriptors.
- [ ] Confirm rights, terms, attribution, redistribution, cadence, and stale tolerances.
- [ ] Confirm observation/model/regulatory/aggregate/administrative distinctions in machine contracts.
- [ ] Confirm geometry, CRS, scale, topology, uncertainty, and public-representation profiles.
- [ ] Confirm resulting-product sensitivity and most-restrictive inheritance.
- [ ] Confirm named geoprivacy profiles, receipts, reviewer obligations, and no-leak tests.
- [ ] Confirm public field allowlists for each artifact family.
- [ ] Confirm policy engine behavior and finite outcomes.
- [ ] Confirm EvidenceRef-to-EvidenceBundle resolution and proof production.
- [ ] Confirm deterministic synthetic fixtures and accepted test suites.
- [ ] Confirm validator ownership and no-network commands.
- [ ] Confirm exact current Habitat workflow validation failure triggers.
- [ ] Confirm candidate-to-PromotionDecision and candidate-to-ReleaseManifest handoff.
- [ ] Confirm correction, withdrawal, supersession, and rollback record contracts.
- [ ] Confirm derivative invalidation across files, tiles, APIs, caches, search, graph, embeddings, previews, exports, and AI.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewers.
- [ ] Confirm public routes consume released governed surfaces only.
- [ ] Confirm generated indexes and summaries cannot become sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced the generic Habitat candidate README with a repository-grounded parent candidate index and child-lane router.
- Recorded the bounded three-README inventory and no-active-candidate posture.
- Indexed the governed `ecoregions/` and `habitat_fauna_thin_slice/` child lanes.
- Added finite states and holds, routing rules, admission fields, Habitat identity and source-role controls, model/observation/regulatory anti-collapse, join-induced sensitivity, geoprivacy and all-surface no-leak rules, time and stale-state discipline, release gates, a public-safe dossier template, validation and automation posture, review handoff, correction and rollback discipline, public-client boundaries, evidence ledger, definition of done, and open verification.
- Preserved the exact candidate-not-release workflow sentence and `publication-not_yet`.
- Added `CONTRACT_VERSION = "3.0.0"` and commit-pinned evidence metadata.

### v1 — prior state

- Draft parent README with general candidate guidance and two named child lanes.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge:

- close the pull request; or
- delete the scoped branch.

After merge:

1. revert the generated-receipt commit;
2. revert the README commit;
3. restore prior README blob:

```text
bd0ccc0dfaaee950d0ca3e42f0395d391a50e0fc
```

No Habitat object, source, evidence, policy decision, proof, candidate payload, PromotionDecision, ReleaseManifest, public artifact, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
