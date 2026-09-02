<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-boundary-version
title: GeologyBoundaryVersion Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Spatial steward
  - OWNER_TBD — Boundary-version steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; boundary-version; geometry-lineage; source-role-aware; metadata-public; release-gated
tags: [kfm, contracts, geology, GeologyBoundaryVersion, boundary-version, geometry-lineage, map-units, geologic-unit, surficial-unit, topology, provenance, evidence, source-role, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicUnit.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../docs/domains/geology/sublanes/surficial.md
  - ../../../docs/domains/geology/sublanes/bedrock_geology.md
  - ../../../schemas/contracts/v1/domains/geology/GeologyBoundaryVersion.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a GeologyBoundaryVersion semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/GeologyBoundaryVersion.schema.json was not found in this session. Object-family docs explicitly ask whether this warrants its own schema or remains metadata on GeologicUnit; schema shape remains NEEDS VERIFICATION."
  - "GeologyBoundaryVersion is a lineage/version object for geology boundary geometry and topology. It does not replace GeologicUnit, SurficialUnit, source maps, tiles, release manifests, correction notices, or public layer truth."
  - "Public-safe metadata posture is supported by doctrine, but public artifacts still require evidence, validation, rights, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GeologyBoundaryVersion — Geology

> Semantic contract for Geology `GeologyBoundaryVersion`: the evidence-bound lineage object for versioned geology boundary geometries, topology state, source-map provenance, replacement relationships, public-safe metadata, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: GeologyBoundaryVersion" src="https://img.shields.io/badge/object-GeologyBoundaryVersion-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: lineage metadata not release approval" src="https://img.shields.io/badge/boundary-lineage__metadata__not__release__approval-critical">
</p>

`contracts/domains/geology/GeologyBoundaryVersion.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Boundary classes](#boundary-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/GeologyBoundaryVersion.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/GeologyBoundaryVersion.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine places `GeologyBoundaryVersion` in the lineage/cross-lane group and flags an open question: it may be its own schema, or it may be metadata on `GeologicUnit`. Field-level schema shape, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `GeologyBoundaryVersion` records boundary geometry/version lineage. It does **not** replace `GeologicUnit`, `SurficialUnit`, source maps, topology validators, release manifests, correction notices, map tiles, public layers, or AI/UI truth by itself.

---

## Meaning

`GeologyBoundaryVersion` is the Geology semantic object for tracking a versioned geology boundary snapshot or boundary-lineage state. It may apply to bedrock units, surficial units, contacts, map editions, generalized public geometries, topology repairs, source-map revisions, or replacement versions.

It answers:

- Which boundary geometry or boundary set is being versioned?
- Which source map, map edition, source record, unit family, interpretation version, geometry fingerprint, CRS, topology state, and evidence support apply?
- Which earlier boundary version does this supersede, replace, repair, generalize, dissolve, clip, or publish as a public-safe derivative?
- Which downstream GeologicUnit, SurficialUnit, StructureFeature, CrossSection, layer, tile, catalog, or graph projection depends on it?
- What release/correction state and rollback target govern downstream use?

A boundary version is lineage and provenance support. It is not the geologic unit itself, not the source map itself, not a rendered tile, and not a release decision.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Boundary-version meaning | `contracts/domains/geology/GeologyBoundaryVersion.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/GeologyBoundaryVersion.schema.json` or metadata on accepted companion schema | NEEDS VERIFICATION; exact path not found |
| Geologic unit contract | `contracts/domains/geology/GeologicUnit.md` | Unit identity and interpretation; boundary version is lineage support |
| Surficial unit context | `docs/domains/geology/sublanes/surficial.md` and future contract homes | Surficial boundary-version use; not a separate release by itself |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms lineage grouping, T0 metadata posture, and schema-open question |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms Geology-owned families and adjacent-lane exclusions |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy | `policy/domains/geology/` | Allow/deny/abstain and public projection decisions where material |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Version, topology, supersession, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/GeologyBoundaryVersion.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/GeologyBoundaryVersion.schema.json` |
| Exact schema result | Not found in this session |
| Object-family roster | `GeologyBoundaryVersion` appears in the §E / lineage roster, not the §10.B owns-list |
| Schema open question | Doctrine explicitly asks whether it warrants its own schema or is metadata on `GeologicUnit` |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema decision is resolved, this contract is semantic guidance for boundary-version meaning and review gates only.

---

## Assertions

A reviewed `GeologyBoundaryVersion` should semantically assert:

1. **Boundary-version identity** — deterministic identity for the boundary snapshot, lineage state, geometry fingerprint, source, role, and normalized digest.
2. **Bound object support** — linked GeologicUnit, SurficialUnit, StructureFeature, map unit, contact, source map, or public derivative that the boundary version applies to.
3. **Source provenance** — SourceDescriptor, source record ID, source map/edition, source role, rights, cadence, and attribution.
4. **Geometry support** — geometry ref, geometry fingerprint, CRS, topology state, scale/generalization, and precision/caveat posture.
5. **Lineage support** — supersedes, replaces, repairs, splits, merges, clips, dissolves, simplifies, generalizes, or withdraws another version.
6. **Temporal support** — source time, valid time, retrieval time, release time, correction time, and stale/supersession state remain distinct.
7. **Validation support** — topology/CRS checks, geometry integrity checks, identity checks, diff checks, and release-readiness checks.
8. **Release posture** — public-safe derivative status, release manifest, correction path, rollback target, and caveats.
9. **Downstream dependency support** — catalog/triplet, published layers, tiles, API/UI, AI summaries, and graph projections identify which boundary version they use.
10. **Governance state** — validation, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating boundary version as unit truth | GeologicUnit / SurficialUnit own unit meaning; boundary version records geometry lineage. |
| Treating boundary version as source map truth | Source maps remain source records with rights/provenance; boundary version is a KFM lineage projection. |
| Treating topology repair as scientific reinterpretation | Geometry repair must be distinguished from interpretation update. |
| Treating simplification/generalization as exact geometry | Public-safe derivatives must preserve precision and transform caveats. |
| Treating a tile/layer as boundary authority | Delivery artifacts are downstream carriers and must cite boundary version/release. |
| Treating correction notice as boundary version | Correction notices document changes; boundary versions are geometry lineage objects. |
| Treating release manifest as boundary version | Release manifests govern publication; boundary versions are inputs or dependencies. |
| Treating scaffold presence as release approval | Publication requires release manifest, validation, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM boundary-version identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `GeologyBoundaryVersion` or accepted metadata form after schema decision. |
| `boundary_class` | Source boundary, reviewed boundary, topology repair, interpretation update, generalized derivative, public derivative, candidate, or withdrawn version. |
| `bound_object_type` | GeologicUnit, SurficialUnit, StructureFeature, source map, contact, layer, or accepted companion object. |
| `bound_object_ref` | Object or source record this boundary version applies to. |
| `boundary_version_id` | Stable source/KFM boundary version key. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, candidate, regulatory, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native map, polygon, contact, boundary, unit, or layer record. |
| `map_provenance_id` | Source map / map edition / provenance ref. |
| `interpretation_version` | Source or KFM interpretation version if boundary change is interpretive. |
| `geometry_ref` | Internal geometry reference for this version. |
| `public_geometry_ref` | Public-safe released geometry reference, if released. |
| `geometry_fingerprint` | Stable geometry fingerprint for identity and drift detection. |
| `previous_geometry_fingerprint` | Prior version fingerprint, when superseding/replacing. |
| `crs` | Coordinate reference system / projection metadata. |
| `topology_state` | Valid, repaired, simplified, clipped, dissolved, invalid, or NEEDS VERIFICATION. |
| `precision_state` | Source precision, reviewed exact, generalized, aggregate, public-safe, withheld, or unknown. |
| `lineage_action` | Created, superseded, repaired, split, merged, clipped, dissolved, generalized, withdrawn, or replaced. |
| `supersedes_ref` | Prior boundary version ref. |
| `superseded_by_ref` | Later boundary version ref, if known. |
| `diff_summary_ref` | Geometry/topology/source diff report ref. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the boundary version claims to represent. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `policy_decision_ref` | Policy result governing use or public projection where material. |
| `review_record_ref` | Source, geology, spatial, topology, vocabulary, or release review. |
| `validation_report_ref` | Validation report for schema, geometry, topology, source-role, lineage, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, geometry repair, topology fix, rights update, supersession, and rollback lineage. |
| `quality_flags` | Missing source, topology invalid, CRS missing, ambiguous lineage, stale source, rights unknown, transform unreceipted, release missing, or incomplete evidence. |

---

## Boundary classes

| Class | Meaning | Default posture |
|---|---|---|
| `source_boundary` | Source-native polygon/contact/boundary version. | Preserve source provenance and scale. |
| `reviewed_boundary` | KFM-reviewed geometry snapshot. | Requires validation report and lineage refs. |
| `topology_repair` | Geometry/topology repair without scientific reinterpretation. | Must carry repair method and diff summary. |
| `interpretation_update` | Boundary change based on new source or interpretation. | Requires source/evidence/review and supersession. |
| `generalized_derivative` | Simplified/generalized geometry for release or display. | Requires transform/precision caveat and release gate. |
| `public_derivative` | Released public-safe geometry/metadata. | Requires release manifest and rollback target. |
| `candidate_record` | Unreviewed import or unresolved boundary row. | WORK/QUARANTINE until reviewed. |
| `withdrawn_version` | Boundary version withdrawn or superseded. | Retain lineage and rollback/correction records. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | GeologyBoundaryVersion posture |
|---|---|---|
| Source map polygon/contact from published geology map | `observed` with interpretation caveat | Boundary snapshot of source interpretation; preserve source scale and version. |
| Compiled state map or generalized regional map | `aggregate` | Compiled boundary support; preserve scale and generalization caveats. |
| Interpolated/model-derived boundary | `modeled` | Must remain modeled/inferred with uncertainty and method. |
| Topology repair, clipping, projection repair, tiling preparation | `administrative` or derived processing posture | Geometry processing lineage, not scientific reinterpretation unless evidence says so. |
| Unreviewed import, invalid geometry, unresolved source polygon | `candidate` | Quarantine until source, topology, CRS, and lineage resolve. |
| AI-generated or hypothetical boundary | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`GeologyBoundaryVersion` is lineage, not the downstream or upstream truth object.

```text
GeologyBoundaryVersion != GeologicUnit
GeologyBoundaryVersion != SurficialUnit
GeologyBoundaryVersion != source map
GeologyBoundaryVersion != topology validator
GeologyBoundaryVersion != ReleaseManifest
GeologyBoundaryVersion != CorrectionNotice
GeologyBoundaryVersion != published tile/layer
GeologyBoundaryVersion != AI summary
```

Any linkage must preserve object identity, source role, evidence, topology state, geometry fingerprint, release state, and correction lineage.

---

## Sensitivity and release

Boundary-version metadata is generally public-safe at unit/line scale when source rights allow. Public geometry or layers still require governed release and must preserve precision, scale, source, topology, and interpretation caveats.

Rules:

- A boundary version is not automatically a public layer.
- Public derivatives require validation, source rights, release manifest, correction path, and rollback target.
- Generalized, clipped, dissolved, simplified, or tiled geometries must not be presented as source exact geometry.
- Map/API/UI/AI surfaces must cite or carry the boundary version, source, interpretation version, geometry precision, and stale/supersession state where material.
- Candidate, synthetic, rights-unknown, topology-invalid, stale, or evidence-incomplete boundary versions must not enter public outputs as authoritative boundary facts.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native polygons, contacts, layers, map editions, topology, CRS, and metadata remain source-bound. |
| WORK / QUARANTINE | Candidate boundary versions are normalized, CRS/topology checked, source-role checked, lineage-matched, rights-screened, and evidence-linked. |
| PROCESSED | Reviewed versions receive deterministic identity, geometry fingerprint, topology state, source/valid times, evidence refs, and correction posture. |
| CATALOG / TRIPLET | Boundary claims may be cataloged only with source role, source time, valid time, geometry lineage, topology state, evidence, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, review where material, release manifest, and rollback target; generalized derivatives also require transform/precision caveats. |
| PUBLISHED | Only released public-safe boundary metadata/layers/API payloads appear in public clients. |
| CORRECTION | Source update, topology repair, boundary replacement, geometry simplification bug, rights update, stale-state change, or release bug triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve whether `GeologyBoundaryVersion` has its own schema or is metadata on `GeologicUnit` / `SurficialUnit` / boundary-bearing objects.
- [ ] Create or locate the accepted paired schema path, or record the accepted metadata placement.
- [ ] Add valid fixtures for source boundary, reviewed boundary, topology repair, interpretation update, generalized derivative, public derivative, candidate record, and withdrawn version.
- [ ] Add invalid fixtures for missing source descriptor, missing geometry fingerprint, missing CRS, invalid topology, ambiguous lineage, generalized geometry presented as exact, boundary version treated as unit truth, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, bound object ref, source map provenance, interpretation version where material, geometry fingerprint, CRS, topology state, lineage action, evidence refs, release refs, and correction refs.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source map revision, geometry repair, simplification bug, topology repair, boundary replacement, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, geometry/topology validates, lineage is clear, derivative is released | `ANSWER` / public-safe boundary metadata may be shown |
| Evidence, source role, geometry, topology, CRS, lineage, rights, or release state is incomplete | `ABSTAIN` |
| Claim would bypass release, misstate exactness, or collapse boundary lineage into unit/source/tile truth | `DENY` |
| Schema, validator, source-read, topology, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology object-family map | Places `GeologyBoundaryVersion` in lineage/cross-lane object group. | Does not prove schema enforcement. |
| Geology object-family quick reference | Confirms T0 metadata posture, source/valid/correction times, observed source-role default, and open question about whether it warrants its own schema. | Field realization remains PROPOSED. |
| Geology scope doc | Confirms Geology owned families and adjacent-domain boundaries. | Does not list `GeologyBoundaryVersion` in §10.B owns-list; membership is roster-drift context. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized GeologyBoundaryVersion weakens source integrity, misstates exactness, hides topology state, breaks lineage, or depends on superseded source, geometry, rights, validation, or release evidence.

Rollback triggers include:

- schema/metadata placement is superseded by ADR or schema decision;
- source map or boundary layer corrected, withdrawn, or superseded;
- geometry fingerprint, CRS, topology, or precision state corrected;
- topology repair is mistaken for scientific reinterpretation;
- generalized/simplified geometry is presented as source exact geometry;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate boundary versions as public truth;
- published layer/tile lacks boundary-version dependency, release manifest, correction path, or rollback target.

Rollback artifacts should include affected GeologyBoundaryVersion IDs, geometry refs, fingerprints, bound object refs, source map refs, diff reports, public derivative refs, release IDs, evidence refs, validation reports, correction notices, rollback cards, replacement versions, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Does `GeologyBoundaryVersion` warrant its own schema, or is it metadata on `GeologicUnit` / boundary-bearing objects? | NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| What is the accepted paired schema path and casing if it is its own object? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which geometry fingerprint algorithm and normalization rules are canonical? | NEEDS VERIFICATION | Spatial/schema/validator review. |
| What counts as topology repair versus interpretation update? | NEEDS VERIFICATION | Geology steward + spatial steward review. |
| Should generalized public geometry require a RedactionReceipt, RepresentationReceipt, transform receipt, or release-only metadata? | NEEDS VERIFICATION | Policy/release/receipt-family review. |
| How should downstream map tiles, APIs, and graph triples pin a boundary version without treating it as the unit truth? | NEEDS VERIFICATION | API/UI/release projection design. |

---

## Related contracts and docs

- `contracts/domains/geology/GeologicUnit.md` — mapped unit meaning and unit identity.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference, lineage group, sensitivity table, and schema-open question.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/sublanes/surficial.md` — surficial boundary context.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home or companion metadata home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve own-schema vs metadata-on-unit placement.
- [ ] Create or verify paired schema/metadata fields and fixtures.
- [ ] Add validation for geometry fingerprint, CRS, topology state, lineage action, bound object, source role, and release refs.
- [ ] Add anti-collapse tests for boundary-version/unit/source-map/release/tile/AI-summary distinctions.
- [ ] Add source profiles or SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe boundary dependencies and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved schema/metadata/path drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
