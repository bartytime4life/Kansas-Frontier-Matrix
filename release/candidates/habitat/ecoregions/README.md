<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/release-candidates-habitat-ecoregions-readme
title: Habitat Ecoregions Release Candidate Review Lane
type: per-sublane-release-candidate-index
version: v2
status: draft; repository-grounded; context-boundary-aware; pre-publication
contract_version: "3.0.0"
owners: [bartytime4life]
created: 2026-07-03
updated: 2026-07-18
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: release/
domain: habitat
sublane: ecoregions
lane_role: ecoregion candidate dossier index and regionalization-context pre-publication review boundary
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: d68cc7344d50e3d739dee555ca3dbe28960369fc
  prior_blob: b233c15f31ea235a0c578fc8b415af56ac654d01
  bounded_candidate_inventory: parent README only; no child candidate dossier established
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../manifests/README.md
  - ../../../promotion_decisions/README.md
  - ../../../correction_notices/README.md
  - ../../../rollback_cards/README.md
  - ../../../withdrawal_notices/README.md
  - ../../../changelog/README.md
  - ../../../../docs/domains/habitat/RELEASE_INDEX.md
  - ../../../../docs/domains/habitat/sublanes/ecoregions.md
  - ../../../../pipeline_specs/habitat/ecoregions/README.md
  - ../../../../pipelines/domains/habitat/ecoregions/README.md
  - ../../../../contracts/domains/habitat/ecoregions/README.md
  - ../../../../schemas/contracts/v1/domains/habitat/ecoregions/README.md
  - ../../../../data/registry/sources/habitat/ecoregions/README.md
  - ../../../../data/proofs/habitat/README.md
  - ../../../../data/catalog/domain/habitat/ecoregions/README.md
  - ../../../../data/processed/habitat/ecoregions/README.md
  - ../../../../data/published/layers/habitat/ecoregions/README.md
  - ../../../../fixtures/domains/habitat/ecoregions/README.md
  - ../../../../tests/domains/habitat/ecoregions/README.md
  - ../../../../policy/domains/habitat/README.md
  - ../../../../tools/validators/domains/habitat/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../.github/CODEOWNERS
  - ../../../../.github/workflows/domain-habitat.yml
  - ../../../../.github/workflows/release-dry-run.yml
tags: [kfm, release, candidates, habitat, ecoregions, regionalization, context, hierarchy, evidence, sensitivity, rollback]
notes:
  - "This README indexes Habitat ecoregion release-candidate dossiers and defines their pre-publication review boundary. It is not an ecoregion source, semantic contract, schema, pipeline specification, evidence object, policy decision, habitat-quality claim, occurrence record, regulatory designation, release decision, or publication authority."
  - "The bounded repository search establishes no child candidate dossier under this lane."
  - "The literal sentence 'A candidate is not a release.' is retained as a cross-lane compatibility invariant; it is not release proof."
  - "Ecoregions are regionalization context. They classify places by a named framework, hierarchy, source version, and boundary version; they do not prove species presence, plant presence, habitat-patch quality, critical-habitat status, hydrologic truth, land/title truth, or release state."
  - "CODEOWNERS routing is not source admission, framework equivalence, steward review, independent approval, release approval, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `release/candidates/habitat/ecoregions/` — Habitat Ecoregions Release Candidate Review Lane

> Index Habitat ecoregion release-candidate dossiers, preserve blockers and safe support pointers, and prevent regionalization polygons, hierarchy records, crosswalks, public layers, or context joins from being treated as occurrence, habitat-quality, regulatory, hydrologic, land-title, evidence, or release truth before source, framework, hierarchy, time, geometry, rights, evidence, sensitivity, policy, validation, review, correction, and rollback gates close.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-orange)
![root](https://img.shields.io/badge/root-release%2F-blue)
![domain](https://img.shields.io/badge/domain-habitat-2E7D32)
![sublane](https://img.shields.io/badge/sublane-ecoregions-1B5E20)
![publication](https://img.shields.io/badge/publication-not_yet-red)
![truth](https://img.shields.io/badge/truth-context__not__occurrence-critical)
![posture](https://img.shields.io/badge/posture-cite--or--abstain-success)
![contract](https://img.shields.io/badge/contract-v3.0.0-1f6feb)

> [!IMPORTANT]
> **Safe conclusion at `main@d68cc7344d…`:** bounded repository search establishes this README as the only directly indexed file under `release/candidates/habitat/ecoregions/`. No child candidate dossier, candidate payload, accepted ecoregion specification, concrete ecoregion schema, emitted proof, release manifest, published ecoregion artifact, or successful ecoregion-specific release path was verified. The Habitat release index contains illustrative or proposed release material rather than a verified ecoregion release, and the current Habitat workflow is an explicit maturity-hold workflow.
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
[Identity](#ecoregion-identity-hierarchy-and-source-role) ·
[Anti-collapse](#regionalization-context-anti-collapse) ·
[Space and time](#space-time-vintage-and-stale-state) ·
[Sensitivity](#sensitivity-cross-lane-joins-and-public-safe-representation) ·
[Gates](#ecoregion-release-gates) ·
[Dossier](#required-dossier-structure) ·
[Validation](#validation-proof-fixture-and-schema-posture) ·
[Automation](#automation-posture) ·
[Handoff](#review-and-release-handoff) ·
[Correction](#correction-withdrawal-supersession-and-rollback) ·
[Public boundary](#public-api-map-export-and-ai-boundary) ·
[Maintenance](#maintenance-and-definition-of-done) ·
[Evidence](#evidence-ledger) ·
[Open items](#open-verification) ·
[Rollback](#rollback-for-this-readme)

---

## Purpose

`release/candidates/habitat/ecoregions/` is the Habitat ecoregions pre-publication review lane under the `release/` responsibility root.

It exists to answer bounded release-readiness questions:

1. Which ecoregion candidate dossiers are currently indexed?
2. Which framework, source version, hierarchy level, boundary version, extent, CRS, scale, and public representation does each candidate claim?
3. Which admitted sources, evidence, rights, policy, validation, review, catalog, correction, and rollback records support it?
4. Does the candidate preserve the rule that ecoregions are regionalization context rather than species, plant, patch-quality, regulatory, hydrologic, soil, hazard, agricultural, parcel, or title truth?
5. Do public fields and geometry avoid leaking sensitive information introduced through cross-lane joins?
6. Which shared release record owns the next governed state transition?

**A candidate is not a release.**

A dossier in this lane is a review packet. It does not create an active source, accepted framework equivalence, validated object, EvidenceBundle, public-safe transform, PromotionDecision, ReleaseManifest, published layer, or public API authority.

The lifecycle boundary remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, branch merge, successful render, catalog entry, generated receipt, or documentation claim.

[Back to top](#top)

---

## Status and evidence boundary

| Question | Repository-grounded answer |
|---|---|
| Does this path exist? | **CONFIRMED.** |
| Does the direct lane contain a child candidate dossier? | **No verified child dossier surfaced in bounded indexed search.** |
| Is an ecoregion candidate active? | **UNKNOWN / not established.** |
| Is there an active ecoregion pipeline specification? | **No.** The directly inspected spec lane is README-only and states that no active specification is established. |
| Are concrete ecoregion semantic contracts established? | **No.** The contract lane contains a README and proposed contract names. |
| Are concrete ecoregion schemas established? | **No.** The schema lane is an index and reports no confirmed concrete schema inventory. |
| Are admitted ecoregion source records established? | **UNKNOWN.** The source-registry README defines admission posture but does not establish concrete admitted descriptors. |
| Are executable ecoregion tests established? | **No direct test module surfaced.** The test lane is README-backed and implementation remains unverified. |
| Are fixture payloads established? | **No verified payload inventory.** The fixture README states that none were verified. |
| Are emitted ecoregion proofs established? | **No.** The Habitat proof lane states implementation depth remains unknown. |
| Is a published ecoregion layer established? | **No emitted artifact surfaced in bounded search.** The published lane is guidance only. |
| Is release automation established? | **No.** `domain-habitat` is an explicit maturity hold; the general release dry run is TODO-only. |

### Truth labels used here

- **CONFIRMED** — verified from current repository files, workflow definitions, comparisons, or generated artifacts in this session.
- **PROPOSED** — intended behavior, contract, field, placement, or control not established as implemented.
- **UNKNOWN** — not verified strongly enough to make a claim.
- **NEEDS VERIFICATION** — checkable, but not sufficiently checked or accepted.
- **CONFLICTED** — repository evidence exposes incompatible or unresolved vocabularies, paths, or authority descriptions.
- **LINEAGE** — historically useful planning or documentation evidence that is not current implementation proof.

This README narrows claims to current evidence. It does not infer maturity from filenames, planned trees, prose, or generic best practice.

[Back to top](#top)

---

## Authority and repository fit

### Directory Rules basis

The requested path already exists beneath the `release/` responsibility root:

```text
release/
└── candidates/
    └── habitat/
        └── ecoregions/
            └── README.md
```

This placement is appropriate because the file governs **candidate review**. It does not own source data, semantic meaning, machine shape, policy, execution, fixtures, tests, proofs, catalog records, published bytes, or final release decisions.

| Responsibility | Owning path | Relationship to this lane |
|---|---|---|
| Habitat candidate parent | [`../README.md`](../README.md) | Parent candidate index and shared Habitat candidate posture. |
| Cross-domain candidate guidance | [`../../README.md`](../../README.md) | Candidate-family orientation. |
| Release authority | [`../../../README.md`](../../../README.md) and shared release record lanes | Owns governed release transitions and record-family separation. |
| Human ecoregion doctrine | [`docs/domains/habitat/sublanes/ecoregions.md`](../../../../docs/domains/habitat/sublanes/ecoregions.md) | Explains ecoregion meaning and domain boundaries. |
| Declarative run intent | [`pipeline_specs/habitat/ecoregions/`](../../../../pipeline_specs/habitat/ecoregions/README.md) | May declare accepted run intent after activation; does not release. |
| Executable processing | [`pipelines/domains/habitat/ecoregions/`](../../../../pipelines/domains/habitat/ecoregions/README.md) | Owns processing behavior when implemented. |
| Semantic meaning | [`contracts/domains/habitat/ecoregions/`](../../../../contracts/domains/habitat/ecoregions/README.md) | Defines ecoregion concepts and invariants. |
| Machine shape | [`schemas/contracts/v1/domains/habitat/ecoregions/`](../../../../schemas/contracts/v1/domains/habitat/ecoregions/README.md) | Owns accepted JSON Schema files when established. |
| Source admission | [`data/registry/sources/habitat/ecoregions/`](../../../../data/registry/sources/habitat/ecoregions/README.md) | Owns source identity, role, rights, cadence, and activation pointers. |
| Processed candidates | [`data/processed/habitat/ecoregions/`](../../../../data/processed/habitat/ecoregions/README.md) | Holds validated upstream artifacts; not public by presence. |
| Proof support | [`data/proofs/habitat/`](../../../../data/proofs/habitat/README.md) | Owns inspectable proof support; not release authority. |
| Catalog closure | [`data/catalog/domain/habitat/ecoregions/`](../../../../data/catalog/domain/habitat/ecoregions/README.md) | Owns discovery/provenance projections after closure. |
| Published carriers | [`data/published/layers/habitat/ecoregions/`](../../../../data/published/layers/habitat/ecoregions/README.md) | Holds released public-safe bytes only after promotion. |
| Policy | [`policy/domains/habitat/`](../../../../policy/domains/habitat/README.md) | Owns admissibility rules; current README is a scaffold. |
| Fixtures | [`fixtures/domains/habitat/ecoregions/`](../../../../fixtures/domains/habitat/ecoregions/README.md) | Holds synthetic public-safe examples, not lifecycle truth. |
| Tests | [`tests/domains/habitat/ecoregions/`](../../../../tests/domains/habitat/ecoregions/README.md) | Owns enforceability tests when implemented. |
| Validators | [`tools/validators/domains/habitat/`](../../../../tools/validators/domains/habitat/README.md) | Owns accepted validator code when established. |

### Authority boundary

This lane may record review state and route pointers. It must not:

- admit or activate a source;
- decide that one ecoregion framework is equivalent to another;
- define a canonical ecoregion schema or contract;
- execute a pipeline or geometry transform;
- decide policy or sensitivity;
- create evidence or proof closure;
- certify a hierarchy, topology, or crosswalk;
- authorize public fields, tiles, or APIs;
- create a PromotionDecision or ReleaseManifest;
- publish, correct, withdraw, supersede, or roll back an artifact.

[Back to top](#top)

---

## Current candidate inventory

### Direct inventory

| Candidate | Status | Evidence | Public effect |
|---|---|---|---|
| _None established_ | `NO_ACTIVE_CANDIDATE` | Bounded indexed search surfaced this README only in the direct lane. | None |

The parent Habitat candidate index confirms this sublane exists, but existence of a sublane is not existence of a candidate.

### Inventory limits

The inventory is bounded by current indexed repository evidence. It does not prove the absence of:

- ignored or generated files;
- unindexed history;
- external review systems;
- restricted stores;
- runtime-only objects;
- differently named records;
- unmerged branches;
- local-only artifacts.

Any such material remains **UNKNOWN** until directly inspected and admitted into the governed repository flow.

### Empty-lane behavior

When no candidate is established:

- do not invent a placeholder candidate ID;
- do not populate an illustrative release row as real;
- do not treat a pipeline spec, fixture, catalog note, published-lane README, or generated receipt as a candidate;
- keep automation in an explicit hold posture;
- keep public clients on existing governed released surfaces only;
- report `NO_ACTIVE_CANDIDATE`, `ABSTAIN`, or another accepted finite non-release state.

[Back to top](#top)

---

## Candidate lifecycle

A useful finite candidate state vocabulary is:

| State | Meaning | Public effect |
|---|---|---|
| `PROPOSED` | A public-safe dossier shell exists, but admission checks are incomplete. | None |
| `ASSEMBLING` | Pointers and support records are being gathered. | None |
| `READY_FOR_REVIEW` | Required fields are present for bounded review. | None |
| `RESTRICTED_REVIEW` | Review requires non-public evidence or sensitive join context. | None |
| `BLOCKED` | A hard gate is unresolved or failed. | None |
| `STALE` | Source, framework, boundary, evidence, or review freshness exceeded tolerance. | None |
| `REPAIR_REQUIRED` | Candidate can continue only after a documented correction. | None |
| `DEFERRED` | Review intentionally paused without approval. | None |
| `APPROVED_FOR_MANIFEST` | Independent review permits manifest preparation; release has not occurred. | None |
| `PROMOTED` | A separate accepted PromotionDecision and ReleaseManifest establish release state. | Governed downstream effect only |
| `SUPERSEDED` | A newer governed candidate or release replaces it. | Historical only |
| `WITHDRAWN` | Candidate was removed from consideration. | None |

`PROMOTED` must never be inferred from the dossier text itself.

### Explicit hold outcomes

Use the narrowest applicable hold:

- `HOLD_FOR_CANDIDATE_IDENTITY`
- `HOLD_FOR_ARTIFACT`
- `HOLD_FOR_FRAMEWORK`
- `HOLD_FOR_SOURCE_VERSION`
- `HOLD_FOR_HIERARCHY`
- `HOLD_FOR_BOUNDARY_VERSION`
- `HOLD_FOR_SOURCE_ADMISSION`
- `HOLD_FOR_SOURCE_ROLE`
- `HOLD_FOR_RIGHTS`
- `HOLD_FOR_TIME`
- `HOLD_FOR_CRS`
- `HOLD_FOR_TOPOLOGY`
- `HOLD_FOR_CROSSWALK`
- `HOLD_FOR_EVIDENCE`
- `HOLD_FOR_PUBLIC_FIELDS`
- `HOLD_FOR_SENSITIVE_JOIN`
- `HOLD_FOR_POLICY`
- `HOLD_FOR_VALIDATION`
- `HOLD_FOR_REVIEW`
- `HOLD_FOR_CATALOG_CLOSURE`
- `HOLD_FOR_RELEASE_TOPOLOGY`
- `HOLD_FOR_CORRECTION_PATH`
- `HOLD_FOR_ROLLBACK`

A hold is safer than silently filling an unknown field or upgrading context into truth.

[Back to top](#top)

---

## What belongs here

This lane may contain public-safe candidate review material such as:

- child candidate dossier READMEs;
- compact machine-readable candidate indexes after a schema and producer are accepted;
- candidate identity and version notes;
- immutable pointers and digests for upstream processed artifacts;
- proposed public target and artifact-family notes;
- source, framework, hierarchy, rights, and vintage closure summaries;
- evidence, validation, policy, review, catalog, correction, and rollback pointers;
- public-field allowlist and public-safe geometry review summaries;
- cross-lane join risk summaries that reveal no protected detail;
- explicit finite outcomes and blockers;
- handoff notes to shared release record lanes.

Keep the dossier pointer-based. Do not duplicate source payloads, geometry packages, proof packs, receipts, or release objects.

[Back to top](#top)

---

## What does not belong here

Do not place these materials in this lane:

| Excluded material | Correct authority home |
|---|---|
| RAW source downloads, shapefiles, geodatabases, archives, rasters, or API payloads | `data/raw/`, `data/work/`, or `data/quarantine/` |
| Processed ecoregion polygons or crosswalk outputs | `data/processed/habitat/ecoregions/` |
| STAC, DCAT, PROV, domain catalog, or triplet records | `data/catalog/` and `data/triplets/` |
| PMTiles, GeoParquet, GeoJSON, MVT, styles, allowlist files, or public exports | `data/published/layers/habitat/ecoregions/` after release |
| SourceDescriptor or activation records | accepted source-registry lane |
| Semantic contracts or JSON Schemas | `contracts/` and `schemas/` |
| Pipeline code or active declarative specs | `pipelines/` and `pipeline_specs/` |
| Policy rules or sensitivity decisions | `policy/` and accepted decision-record lanes |
| Fixtures, tests, or validator code | `fixtures/`, `tests/`, and `tools/validators/` |
| EvidenceBundle, ProofPack, validation proof, or receipt objects | `data/proofs/` and `data/receipts/` |
| PromotionDecision, ReleaseManifest, CorrectionNotice, WithdrawalNotice, or RollbackCard | shared `release/` record lanes |
| Species or plant occurrence records | Fauna or Flora lifecycle and evidence lanes |
| HabitatPatch, suitability, restoration, or critical-habitat truth | owning Habitat sibling sublane or regulatory lane |
| Hydrologic-unit, soil-map, parcel, title, administrative, or jurisdiction truth | owning domain |
| Credentials, private review substance, or sensitive join details | approved restricted systems only |
| AI-generated prose presented as evidence, policy, validation, or approval | governed AI output with citations and finite status only |

[Back to top](#top)

---

## Candidate admission contract

A child dossier must not enter `READY_FOR_REVIEW` until the following fields are explicit or marked with a blocking status.

### Candidate identity

- stable `candidate_id`;
- candidate version and digest;
- owner and review contacts;
- creation, update, and supersession times;
- current finite state;
- parent Habitat candidate reference;
- proposed release family and audience.

### Artifact identity

- immutable processed or staging artifact pointer;
- artifact format and byte digest;
- object count or feature count where safe;
- geometry family;
- proposed published target;
- expected layer, export, API, or report carriers;
- artifact-manifest reference when accepted.

### Ecoregion identity

- framework identifier;
- framework authority/source family;
- native framework version;
- hierarchy level;
- region code and label semantics;
- parent/child hierarchy rules;
- boundary version;
- spatial extent;
- crosswalk posture;
- identity conflict or unresolved-equivalence posture.

### Source and rights

- admitted SourceDescriptor references;
- accepted canonical source roles;
- source head and retrieval identity;
- rights, attribution, redistribution, and derivative-use posture;
- source cadence and stale tolerance;
- authority limits;
- activation and supersession state.

### Space, scale, and time

- source CRS;
- processing CRS;
- tiling CRS where relevant;
- datum and axis-order posture;
- scale, resolution, simplification, and topology rules;
- valid time;
- source/publication vintage;
- retrieval time;
- processing time;
- candidate time;
- release and correction time expectations.

### Public representation

- proposed public geometry;
- public-field allowlist reference;
- excluded internal fields;
- source and framework attribution;
- safe evidence resolver keys;
- zoom and scale limits where tiled;
- cross-lane join posture;
- sensitive-join review and transform references;
- reconstruction, crosswalk-loss, or uncertainty notes.

### Governance support

- EvidenceRef and EvidenceBundle pointers;
- validation report and receipt pointers;
- policy decision and obligations;
- review records;
- catalog closure;
- correction and invalidation plan;
- withdrawal and supersession plan;
- rollback target;
- release-manifest readiness.

Missing consequential fields block review rather than being guessed.

[Back to top](#top)

---

## Ecoregion identity, hierarchy, and source role

### Identity tuple

Treat an ecoregion identity as at least:

```text
framework
+ framework_version
+ hierarchy_level
+ native_region_code
+ boundary_version
+ spatial_extent
+ valid_time
```

A matching label or overlapping geometry is not identity equivalence.

### Hierarchy rules

A candidate must preserve:

- the native hierarchy level;
- parent and child identifiers;
- one documented hierarchy source;
- boundary/version lineage;
- code and label changes;
- splits, merges, retirements, and supersessions;
- uncertainty or unresolved crosswalks.

Do not silently map Level III to Level IV, EPA/Omernik to USFS/Bailey, or any local crosswalk to canonical equivalence.

### Source-role posture

The Habitat release index records the current seven-role vocabulary:

```text
observed
regulatory
modeled
aggregate
administrative
candidate
synthetic
```

Current ecoregion docs also use words such as `authority` and `context`. Those words describe authority scope or use character; they are **not automatically accepted source-role values**.

This produces a current repository conflict:

- the ecoregion charter describes EPA/Omernik as `authority`;
- the source-registry README suggests `administrative` or `aggregate`, depending on descriptor evidence;
- the canonical Habitat release vocabulary lists seven accepted roles and does not include `authority` or `context`.

Therefore, source-role assignment is **NEEDS VERIFICATION** for every candidate. Preserve the source's actual authority scope, but do not invent or upgrade a canonical role.

[Back to top](#top)

---

## Regionalization-context anti-collapse

The candidate must keep these distinctions explicit:

| Material | Must not become |
|---|---|
| Ecoregion polygon | Species occurrence or plant occurrence |
| Ecoregion polygon | HabitatPatch, habitat quality, suitability, corridor, or restoration priority |
| Ecoregion framework | Regulatory critical-habitat designation |
| Ecoregion code or label | Stable KFM identity without an accepted mapping |
| Level III region | Level IV region |
| EPA/Omernik framework | USFS/Bailey framework |
| Crosswalk | Lossless identity equivalence |
| Land-cover observation | Ecoregion identity |
| WBD/HUC boundary | Ecoregion or hydrologic truth owned by Habitat |
| PLSS or parcel context | Ecological or land-title truth |
| Aggregate summary | Per-place observation |
| Modeled regionalization | Observed occurrence |
| Tile, style, or renderer output | Canonical geometry |
| Catalog record | Evidence closure or release approval |
| Successful pipeline run | Policy clearance or publication |
| Generated explanation | Evidence, source authority, or release state |

### Crosswalk posture

Crosswalks must record:

- source and target frameworks;
- source and target versions;
- mapping method;
- one-to-one, one-to-many, many-to-one, or unresolved relation;
- known loss;
- geometry or attribute transforms;
- reviewer;
- evidence support;
- correction and rollback path.

When equivalence cannot be established, preserve both identities and return `ABSTAIN`, `CONFLICTED`, or another accepted finite outcome.

[Back to top](#top)

---

## Space, time, vintage, and stale state

### Spatial support

A candidate must state:

- source geometry and authoritative CRS;
- processing CRS;
- tiling/rendering CRS;
- topology and geometry-validity expectations;
- simplification and generalization profile;
- scale or zoom range;
- extent and clipping behavior;
- boundary precision and uncertainty;
- coordinate transformation lineage.

Reprojection for rendering does not replace source geometry or provenance.

### Time kinds

Keep these time kinds distinct where material:

| Time | Meaning |
|---|---|
| `source_time` | Date or edition asserted by the source. |
| `valid_time` | Period when the boundary/classification applies. |
| `retrieval_time` | When KFM captured the source. |
| `processing_time` | When the candidate was produced. |
| `candidate_time` | When the review packet was assembled. |
| `release_time` | When a separate release decision took effect. |
| `correction_time` | When a correction or withdrawal changed public posture. |
| `supersession_time` | When a newer framework/boundary replaced the prior version. |

### Stale-state rules

A candidate becomes `STALE` when:

- source cadence or review tolerance is exceeded;
- a framework or boundary version is superseded;
- source rights or terms expire or change;
- an upstream correction invalidates the artifact;
- evidence or catalog closure no longer resolves;
- public fields or transform profiles are no longer accepted;
- a crosswalk is invalidated by version drift.

Stale is not the same as wrong, but stale candidates do not silently remain release-ready.

[Back to top](#top)

---

## Sensitivity, cross-lane joins, and public-safe representation

Ecoregion polygons are generally low intrinsic sensitivity. Their joins can create high sensitivity or reconstruction risk.

### Join-induced sensitivity

Fail closed when a candidate joins or exposes:

- sensitive fauna occurrence, nests, dens, roosts, hibernacula, or spawning sites;
- rare or culturally sensitive Flora records;
- critical-habitat or stewardship detail whose public posture differs from ecoregion context;
- archaeology, cultural-resource, or sovereign-community-sensitive material;
- private land, living-person, owner, parcel, or access-route information;
- precise restoration, monitoring, or management sites;
- infrastructure-sensitive locations;
- small-cell aggregates that permit re-identification;
- internal crosswalks or fields that reconstruct withheld geometry.

### Public-safe requirements

A public candidate requires:

- an explicit public-field allowlist;
- a public geometry profile;
- removal of internal IDs and sensitive join keys;
- source/framework/version attribution;
- safe EvidenceRef resolver keys;
- reviewed aggregation/generalization when joins raise risk;
- receipt and review references where a transform occurs;
- no hidden sensitive attributes in tiles, metadata, logs, screenshots, or error messages.

Style-only hiding is not access control. Fields omitted from a popup but retained in PMTiles or exports remain exposed.

### Audience classes

A dossier should distinguish:

- public web map;
- public API;
- public download/export;
- reviewer-only artifact;
- steward-only evidence;
- internal QA.

Approval for one audience is not approval for all audiences.

[Back to top](#top)

---

## Ecoregion release gates

A candidate cannot advance to `APPROVED_FOR_MANIFEST` until all applicable gates close.

| Gate | Minimum support | Fail-closed outcome |
|---|---|---|
| Candidate identity | Stable ID, version, owner, digest, state | `HOLD_FOR_CANDIDATE_IDENTITY` |
| Artifact identity | Immutable pointer, format, digest, proposed target | `HOLD_FOR_ARTIFACT` |
| Framework identity | Named framework, authority scope, version | `HOLD_FOR_FRAMEWORK` |
| Hierarchy | Explicit level, codes, labels, parent/child rules | `HOLD_FOR_HIERARCHY` |
| Boundary identity | Boundary version, extent, lineage | `HOLD_FOR_BOUNDARY_VERSION` |
| Source admission | Admitted descriptors and activation state | `HOLD_FOR_SOURCE_ADMISSION` |
| Source role | Accepted role without truth upgrade | `HOLD_FOR_SOURCE_ROLE` |
| Rights | Terms, attribution, redistribution, derivative use | `HOLD_FOR_RIGHTS` |
| Time | Source, valid, retrieval, processing, candidate, stale posture | `HOLD_FOR_TIME` |
| Spatial support | CRS, scale, resolution, topology, transform lineage | `HOLD_FOR_CRS` or `HOLD_FOR_TOPOLOGY` |
| Crosswalk | Method, loss, versions, review, rollback | `HOLD_FOR_CROSSWALK` |
| Evidence | Consequential claims resolve to EvidenceBundle | `HOLD_FOR_EVIDENCE` |
| Public fields | Reviewed allowlist and excluded-field proof | `HOLD_FOR_PUBLIC_FIELDS` |
| Sensitive joins | Join inventory, policy, transform, review, no-leak support | `HOLD_FOR_SENSITIVE_JOIN` |
| Policy | Accepted finite policy result and obligations | `HOLD_FOR_POLICY` |
| Validation | Deterministic schema/semantic/hierarchy/topology/no-leak checks | `HOLD_FOR_VALIDATION` |
| Catalog closure | Catalog and provenance references resolve | `HOLD_FOR_CATALOG_CLOSURE` |
| Review | Habitat, ecoregion, source/rights, spatial, sensitivity, release reviewers | `HOLD_FOR_REVIEW` |
| Correction | Derivative inventory and invalidation route | `HOLD_FOR_CORRECTION_PATH` |
| Rollback | Verified prior target or safe withdrawal strategy | `HOLD_FOR_ROLLBACK` |
| Release topology | PromotionDecision and ReleaseManifest homes resolved | `HOLD_FOR_RELEASE_TOPOLOGY` |

No single passing gate compensates for another missing gate.

[Back to top](#top)

---

## Required dossier structure

A child candidate dossier should remain public-safe and pointer-based.

```markdown
# <candidate title>

## KFM metadata
- candidate_id:
- candidate_version:
- owner:
- state:
- created_at:
- updated_at:
- supersedes:
- digest:

## Candidate artifact
- artifact_ref:
- artifact_sha256:
- artifact_format:
- feature_count:
- proposed_public_targets:

## Framework and hierarchy
- framework_id:
- framework_version:
- hierarchy_level:
- native_region_code_field:
- native_region_label_field:
- parent_relation:
- boundary_version:
- extent:
- crosswalk_refs:

## Sources and rights
- source_descriptor_refs:
- source_roles:
- authority_scope:
- rights_state:
- attribution:
- redistribution_state:
- activation_state:
- stale_after:

## Space and time
- source_crs:
- processing_crs:
- tiling_crs:
- scale_or_resolution:
- topology_profile:
- valid_time:
- retrieval_time:
- processing_time:
- candidate_time:

## Claim character
- regionalization_context:
- prohibited_truth_upgrades:
- uncertainty_and_loss:
- reality_or_reconstruction_notes:

## Public representation
- public_geometry_profile:
- field_allowlist_ref:
- excluded_fields:
- audience_classes:
- evidence_resolver_keys:
- sensitive_join_posture:

## Evidence and validation
- evidence_refs:
- evidence_bundle_refs:
- validation_report_refs:
- receipt_refs:
- catalog_refs:
- finite_outcomes:
- blockers:

## Policy and review
- policy_decision_ref:
- obligations:
- habitat_review_ref:
- source_rights_review_ref:
- spatial_review_ref:
- sensitivity_review_ref:
- independent_release_review_ref:

## Release handoff
- promotion_decision_target:
- release_manifest_target:
- published_artifact_target:
- correction_notice_target:
- withdrawal_notice_target:
- rollback_card_target:

## Decision
- recommendation:
- reason_codes:
- unresolved_items:
```

The template is **PROPOSED** until a machine contract is accepted. It does not authorize creating candidate-local copies of shared release records.

[Back to top](#top)

---

## Validation, proof, fixture, and schema posture

### Current repository posture

| Surface | Confirmed evidence | Current limit |
|---|---|---|
| Candidate lane | This README exists; no child dossier surfaced | No active candidate established |
| Ecoregion doctrine | Detailed draft sublane charter exists | Some implementation and source-role claims remain proposed or conflicted |
| Pipeline specification | Repository-grounded README exists | Direct lane is README-only; no active spec established |
| Semantic contracts | README exists | Proposed contract candidates only |
| Schemas | README index exists | No concrete schema inventory confirmed |
| Source registry | Grounded README exists | Concrete descriptors, activation records, rights, and topology unresolved |
| Tests | Detailed README exists | No direct executable test module surfaced |
| Fixtures | Detailed README exists | No payload files verified by its own inventory |
| Proofs | Habitat proof README exists | Implementation depth remains unknown; no ecoregion proof inventory established |
| Published layer | Detailed README exists | No emitted release-linked artifact surfaced |
| Policy | Habitat policy README exists | Greenfield scaffold; executable enforcement not established |
| Validators | Habitat validator indexes exist | Accepted ecoregion validator command not established |
| Automation | `domain-habitat` workflow exists | Explicit maturity holds, not ecoregion validation or release proof |
| Release dry run | General workflow exists | TODO-only echo jobs |

### Minimum positive cases

Future deterministic tests should prove:

- a synthetic ecoregion snapshot preserves framework, version, hierarchy, boundary version, source role, CRS, time, and evidence;
- a valid parent/child hierarchy is accepted;
- an approved public field allowlist excludes internal and sensitive fields;
- public geometry preserves source lineage and accepted simplification;
- a public candidate with closed evidence, policy, review, catalog, correction, and rollback references can advance to manifest review;
- context joins preserve the owning domain's truth.

### Minimum negative cases

Future tests should deny, abstain, restrict, or fail when:

- framework, level, source version, or boundary version is missing;
- source role is unaccepted or upgraded;
- EPA/Omernik and USFS/Bailey identities are collapsed;
- Level III and Level IV are treated as equivalent;
- a crosswalk omits method or known loss;
- an ecoregion is used as species or plant occurrence evidence;
- an ecoregion is used as HabitatPatch quality, suitability, or critical-habitat proof;
- WBD/HUC or PLSS context is treated as ecoregion identity;
- EvidenceRef does not resolve;
- rights or source activation is unresolved;
- a sensitive join leaks through fields, tiles, metadata, logs, or exports;
- a public layer lacks an allowlist, release state, correction path, or rollback target;
- a stale source is presented as current;
- generated prose or renderer output is treated as evidence.

### Validation does not equal truth

A schema-valid, topology-valid, or renderable polygon may still be:

- the wrong framework;
- the wrong hierarchy level;
- stale;
- rights-restricted;
- unsupported by evidence;
- unsafe after a cross-lane join;
- unreleased;
- unsuitable for a consequential claim.

[Back to top](#top)

---

## Automation posture

### `domain-habitat`

The current Habitat workflow:

- checks required Habitat boundary paths;
- uses AST inspection to detect executable tests;
- uses AST and content checks to detect executable validator implementations;
- holds validation when no accepted suite is wired;
- holds proof production when no accepted producer is wired;
- holds release dry-run behavior when no candidate record or accepted command exists.

The workflow's candidate check operates at the parent Habitat candidate tree and treats non-README files as a signal that release automation must graduate. This README does not satisfy or bypass that graduation burden.

A green held result means only that the documented maturity assumptions remain true. It does not mean:

- the candidate is valid;
- the source is admitted;
- the framework/hierarchy is correct;
- evidence closes;
- sensitive joins are safe;
- a release exists;
- public use is approved.

### General release dry run

The general `release-dry-run` workflow currently uses TODO echo steps for candidate assembly, promotion-gate checking, and rollback-card presence. Green results from those jobs are not release governance.

### Watchers and generators

A watcher or generator may propose changed source/framework/version state. It must not:

- activate a source;
- create a candidate as approved;
- decide framework equivalence;
- perform unreviewed sensitive joins;
- promote or publish;
- silently rewrite correction or rollback state.

[Back to top](#top)

---

## Review and release handoff

### Required review roles

A mature candidate may require:

- Habitat domain steward;
- ecoregions sublane steward;
- source and rights steward;
- Spatial Foundation / CRS / topology reviewer;
- evidence and validation reviewer;
- sensitivity and geoprivacy reviewer;
- Fauna or Flora reviewer when joined occurrence context is involved;
- Hydrology, Soil, Hazards, Agriculture, Archaeology, or People/Land reviewer when their truth is referenced;
- release steward;
- independent approver where significance warrants separation of duties.

CODEOWNERS routing does not prove that any role reviewed or approved the candidate.

### Handoff routing

| Review result | Next authority lane |
|---|---|
| Candidate needs repair | Upstream processed/work/quarantine owner plus this dossier |
| Candidate blocked | This dossier with explicit hold and reason codes |
| Candidate approved for promotion review | `release/promotion_decisions/` |
| Candidate approved for manifest assembly | `release/manifests/` |
| Public artifacts emitted after release | `data/published/layers/habitat/ecoregions/` |
| Correction required | `release/correction_notices/` |
| Withdrawal required | `release/withdrawal_notices/` |
| Rollback required | `release/rollback_cards/` |
| Release history update | `release/changelog/` |

Candidate-local `PromotionDecision`, `ReleaseManifest`, `CorrectionNotice`, or `RollbackCard` copies would create parallel authority unless an accepted migration or ADR explicitly permits them.

[Back to top](#top)

---

## Correction, withdrawal, supersession, and rollback

### Correction triggers

Correction review is required when:

- a framework, version, hierarchy, code, label, or boundary is wrong;
- a crosswalk is revised or invalidated;
- source rights or attribution change;
- an upstream source is corrected or withdrawn;
- hierarchy or topology validation changes;
- a public field is found unsafe;
- a sensitive join or reconstruction path is discovered;
- an evidence or catalog reference breaks;
- a public artifact digest differs from its release record;
- stale-state or supersession was omitted.

### Derivative inventory

A correction plan must identify affected:

- processed artifacts;
- catalogs and triplets;
- proofs and receipts;
- candidate dossiers;
- release manifests;
- public PMTiles, GeoParquet, GeoJSON, and exports;
- layer registry entries;
- caches and CDN objects;
- API responses and search indexes;
- Evidence Drawer and Focus Mode references;
- reports, screenshots, and generated summaries.

### Rollback requirements

A rollback must:

1. identify the affected candidate or release;
2. bind to a verified prior target or safe withdrawal state;
3. invalidate derivatives;
4. remove or supersede public pointers;
5. update correction and changelog records;
6. preserve audit lineage;
7. avoid restoring a stale, rights-invalid, or sensitive-leaking artifact.

Rollback is not a hidden file copy or manual alias change.

[Back to top](#top)

---

## Public API, map, export, and AI boundary

### Public clients

Public clients use governed interfaces and released carriers. They must not read:

- RAW, WORK, or QUARANTINE stores;
- processed candidates directly;
- candidate dossiers as data APIs;
- source-registry internals;
- proofs or receipts as public truth stores;
- unreleased tiles or exports;
- internal join keys or sensitive fields.

### Map and tile behavior

A public ecoregion layer should expose only:

- released geometry;
- approved framework/version/level attribution;
- public labels and codes;
- public-safe source and evidence references;
- released time and correction state;
- approved uncertainty or boundary notes.

The renderer must not imply:

- species presence;
- habitat quality;
- critical-habitat status;
- hydrologic authority;
- land ownership;
- currentness beyond source vintage;
- equivalence between frameworks or levels.

### Exports

Exports require independent review of:

- included fields;
- geometry precision;
- metadata sidecars;
- source and rights obligations;
- evidence resolver keys;
- release and correction state;
- join-induced sensitivity;
- reconstruction risk.

### Governed AI

AI may summarize released, policy-admitted, citation-closed ecoregion evidence. It may not:

- infer species or plant occurrence from an ecoregion;
- convert context into habitat-quality or regulatory truth;
- silently equate frameworks;
- fill missing hierarchy, source role, rights, or evidence;
- expose protected join context;
- treat candidate or catalog state as release state.

Use finite outcomes:

```text
ANSWER
ABSTAIN
DENY
ERROR
```

Every non-`ANSWER` should carry an accepted reason code.

[Back to top](#top)

---

## Maintenance and definition of done

### Maintenance triggers

Update this README when:

- the first child candidate dossier is added;
- a machine-readable candidate index is accepted;
- a concrete contract or schema is added;
- a source descriptor is admitted;
- an active pipeline specification or executable consumer is accepted;
- fixture payloads or executable tests appear;
- an ecoregion proof producer is wired;
- a candidate enters review;
- a PromotionDecision or ReleaseManifest is created;
- public artifacts are emitted;
- a correction, withdrawal, supersession, or rollback occurs;
- framework, hierarchy, source-role, or path conflicts are resolved.

### Definition of done for this lane

This lane becomes implementation-backed when:

- exhaustive candidate inventory is deterministic and reviewable;
- candidate identity and artifact-manifest contracts are accepted;
- framework, hierarchy, boundary, crosswalk, source-role, time, CRS, topology, and public-field contracts are machine-checkable;
- admitted source records and rights decisions exist;
- concrete schemas, fixtures, validators, and deterministic no-network tests are wired;
- EvidenceRef-to-EvidenceBundle and catalog closure are enforced;
- sensitive-join no-leak tests pass;
- policy results and reviewer obligations are machine-resolvable;
- candidate-to-PromotionDecision-to-ReleaseManifest routing is accepted;
- correction, withdrawal, supersession, cache invalidation, and rollback drills are tested;
- public clients consume only governed released carriers;
- human review and branch protection requirements are verified.

Until then, this README remains a repository-grounded governance contract, not proof of implementation.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | Supports | Limitation |
|---|---|---|---|
| This target README | `CONFIRMED prior file` | Existing candidate sublane path and prior minimal guidance | Prior file did not establish candidate inventory or implementation maturity |
| Parent Habitat candidate README | `CONFIRMED` | Parent path, sibling sublanes, lifecycle and candidate boundary | Parent remains draft and does not establish child candidates |
| Habitat ecoregions charter | `CONFIRMED file / draft doctrine` | Regionalization context, hierarchy, time, CRS, joins, public-safe rules | Several implementation and source-role details remain proposed or conflicted |
| Ecoregions pipeline-spec README | `CONFIRMED repository-grounded` | README-only direct spec lane, no active specification, finite gates | No parser, consumer, activation, or runtime proof established |
| Ecoregion contracts README | `CONFIRMED file / proposed contracts` | Semantic boundary and proposed object families | Direct contract inventory is README-only |
| Ecoregion schema README | `CONFIRMED file / index` | Proposed schema home and candidate names | No concrete schema inventory confirmed |
| Ecoregion source-registry README | `CONFIRMED file / draft registry guidance` | Admission, rights, cadence, role, framework/version controls | Concrete descriptors and canonical topology unresolved |
| Ecoregion tests README | `CONFIRMED file / proposed test lane` | Expected invariant and negative cases | No direct executable module surfaced |
| Ecoregion fixture README | `CONFIRMED file` | Synthetic/public-safe fixture rules | Its inventory says no payload files were verified |
| Habitat proof README | `CONFIRMED file / proposed proof lane` | Proof closure requirements | Implementation depth remains unknown |
| Habitat release index | `CONFIRMED navigational draft` | Shared release records, sensitivity, stale/correction/rollback posture | Illustrative entries are not proof of releases |
| Published ecoregion layer README | `CONFIRMED carrier guidance` | Public layer fields, allowlist, map and release boundaries | No emitted artifact surfaced in bounded search |
| Habitat policy README | `CONFIRMED scaffold` | Policy home | Does not establish executable rules |
| `domain-habitat` workflow | `CONFIRMED definition` | Explicit maturity holds and detector logic | Held outcomes are not domain validation or release proof |
| General release dry run | `CONFIRMED TODO scaffold` | Workflow presence | Echo jobs are not candidate assembly or gate enforcement |
| CODEOWNERS | `CONFIRMED routing surface` | GitHub review routing | Not proof of review, stewardship, or release authority |

No external web research is required for this repository-state documentation update.

[Back to top](#top)

---

## Open verification

- [ ] Confirm exhaustive recursive inventory under `release/candidates/habitat/ecoregions/`.
- [ ] Confirm candidate naming, stable identity, versioning, and digest conventions.
- [ ] Confirm accepted ecoregion object-family and claim-character vocabularies.
- [ ] Confirm canonical framework IDs, hierarchy levels, native code rules, and boundary-version contract.
- [ ] Resolve the `authority` / `context` terminology against the accepted seven-role source vocabulary.
- [ ] Confirm admitted EPA/Omernik, USFS/Bailey, NatureServe, GAP/LANDFIRE, NLCD, NWI, PLSS, WBD/HUC, and crosswalk source records as applicable.
- [ ] Confirm source rights, terms, attribution, redistribution, cadence, and stale tolerance.
- [ ] Resolve subtype-first versus domain-first Habitat source-registry topology.
- [ ] Confirm accepted semantic contracts and concrete JSON Schemas.
- [ ] Confirm parser, registry, activation, executable consumer, scheduler, and pipeline-spec schema.
- [ ] Confirm time-kind, CRS, datum, axis-order, scale, simplification, topology, and boundary-lineage profiles.
- [ ] Confirm public-field allowlists and no-leak validation.
- [ ] Confirm crosswalk method, loss, evidence, review, correction, and rollback contracts.
- [ ] Confirm synthetic fixture payload inventory and direct executable tests.
- [ ] Confirm accepted ecoregion validator ownership and deterministic no-network command.
- [ ] Confirm EvidenceRef-to-EvidenceBundle resolution and ecoregion proof producer.
- [ ] Confirm catalog closure and layer-registry integration.
- [ ] Confirm candidate-to-PromotionDecision-to-ReleaseManifest handoff.
- [ ] Confirm CorrectionNotice, WithdrawalNotice, supersession, RollbackCard, cache invalidation, and derivative invalidation flows.
- [ ] Confirm public API, MapLibre, export, search, graph, Evidence Drawer, and AI no-truth-upgrade tests.
- [ ] Confirm branch protection, required checks, immutable action pinning, and independent reviewer assignments.
- [ ] Confirm candidate inventory generation does not make generated output sovereign truth.

[Back to top](#top)

---

## Changelog

### v2 — 2026-07-18

- Replaced minimal candidate notes with a repository-grounded ecoregion candidate index and pre-publication review contract.
- Recorded that no child candidate dossier or active ecoregion candidate is established by bounded inspection.
- Added finite states and holds, candidate admission requirements, framework/hierarchy/source-role rules, regionalization anti-collapse, time/vintage/stale-state controls, crosswalk and sensitive-join posture, release gates, a public-safe dossier template, validation and automation maturity, review handoff, correction and rollback discipline, public-client boundaries, evidence ledger, definition of done, and open verification.
- Preserved the exact candidate-not-release sentence and added `publication-not_yet`.
- Added `CONTRACT_VERSION = "3.0.0"` and commit-pinned evidence metadata.

### v1 — prior state

- Minimal README replacing a blank file.

[Back to top](#top)

---

## Rollback for this README

This revision changes documentation only.

Before merge, close the pull request or delete the scoped branch.

After merge, revert the generated-receipt commit and README commit in reverse order and restore the prior README blob:

```text
b233c15f31ea235a0c578fc8b415af56ac654d01
```

No Habitat candidate, ecoregion framework, hierarchy, source record, boundary, crosswalk, processed artifact, EvidenceBundle, policy decision, validation result, release manifest, public layer, correction, withdrawal, supersession, or rollback state requires restoration.

[Back to top](#top)
