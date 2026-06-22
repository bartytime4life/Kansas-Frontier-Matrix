<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-structure-feature
title: StructureFeature Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Structural geology steward
  - OWNER_TBD — Spatial steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; structure-feature; fault-structure; structural-context; source-role-aware; release-gated; hazards-boundary
tags: [kfm, contracts, geology, StructureFeature, FaultStructure, structure-feature, fault, fold, joint, lineament, structural-geology, geometry-fingerprint, map-provenance, evidence, source-role, hazards-boundary, policy, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicUnit.md
  - ./GeologyBoundaryVersion.md
  - ./CrossSection.md
  - ./GeophysicalObservation.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../docs/domains/geology/sublanes/bedrock_geology.md
  - ../../../docs/domains/geology/sublanes/geophysics.md
  - ../../../schemas/contracts/v1/domains/geology/structure_feature.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../policy/sensitivity/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology StructureFeature semantic contract."
  - "A lower-case schema scaffold exists at schemas/contracts/v1/domains/geology/structure_feature.schema.json, while this requested contract path uses PascalCase. The schema's x-kfm.contract_doc points to contracts/domains/geology/structure_feature.md, creating a casing/path drift that remains CONFLICTED / NEEDS VERIFICATION."
  - "Object-family docs explicitly surface Fault Structure ↔ StructureFeature spelling drift. This contract preserves StructureFeature by requested path and records FaultStructure as the unresolved alternate family spelling."
  - "StructureFeature supplies structural geology context. It does not assert Hazards risk, rupture probability, hazard zoning, public alert status, ownership/title, or AI/UI truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# StructureFeature — Geology

> Semantic contract for Geology `StructureFeature`: the evidence-bound object for faults, folds, joints, lineaments, structural surfaces, geometry fingerprints, map provenance, source role, public-safe derivatives, correction, and rollback — explicitly distinct from Hazards risk, public alerts, and generated UI/AI claims.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: StructureFeature" src="https://img.shields.io/badge/object-StructureFeature-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: structure not hazard risk" src="https://img.shields.io/badge/boundary-structure__not__hazard__risk-critical">
</p>

`contracts/domains/geology/StructureFeature.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Feature classes](#feature-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/StructureFeature.md`  
> **Schema posture:** a lower-case scaffold exists at `schemas/contracts/v1/domains/geology/structure_feature.schema.json`; its `x-kfm.contract_doc` points to lower-case `contracts/domains/geology/structure_feature.md`, while the current requested contract path is PascalCase  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies the family through a naming drift pair: §10.B says `Fault Structure`, while §E uses `StructureFeature`. Field-level schema shape, casing, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `StructureFeature` is structural geology context. It does **not** prove Hazards risk, rupture probability, landslide/subsidence risk, hazard zoning, public alert status, ownership/title, lease/permit status, emergency guidance, or AI/UI truth by itself.

---

## Meaning

`StructureFeature` is the Geology semantic object for a mapped or interpreted structural geology element such as a fault, fold, joint, lineament, fracture zone, structural surface, contact-like structural trace, shear zone, or source-native structure feature.

It answers:

- Which structural feature is being asserted?
- Which feature class, geometry, source map, map provenance, interpretation version, confidence, source role, and evidence support apply?
- Which geologic units, boundary versions, cross-sections, geophysical observations, boreholes/logs, or source records may cite or support the structure without collapsing identity?
- What public-safe geometry, label, layer dependency, graph claim, or derivative may be shown?
- Which validation report, policy decision where material, review record, release manifest, correction notice, and rollback target govern downstream use?

A structural feature can supply geologic context to Hazards. Hazards owns risk, warning, alert, probability, and life-safety claims. Geology does not become a hazards authority by publishing structural geometry.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Structure-feature meaning | `contracts/domains/geology/StructureFeature.md` | Owned here by request; naming/casing drift remains open |
| Machine schema shape | `schemas/contracts/v1/domains/geology/structure_feature.schema.json` | CONFIRMED scaffold; field shape still empty / PROPOSED |
| Schema/contract casing drift | `StructureFeature.md` vs `structure_feature.schema.json` and lower-case `x-kfm.contract_doc` | CONFLICTED / NEEDS VERIFICATION |
| Object-family naming drift | `Fault Structure` vs `StructureFeature` | CONFLICTED / ADR-class; do not treat as two identities without ADR/schema decision |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms §10.B `Fault Structure` as structural lines/surfaces with sense-of-slip and confidence, and confirms Hazards boundary |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms StructureFeature/FaultStructure purpose, proposed keys, material times, sensitivity posture, and Hazards boundary |
| Boundary version support | `contracts/domains/geology/GeologyBoundaryVersion.md` | Geometry lineage and replacement history; not structure identity itself |
| Cross-section support | `contracts/domains/geology/CrossSection.md` | Interpretive panels may show structures; cross-section identity remains separate |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy | `policy/domains/geology/`, `policy/sensitivity/geology/` | Allow/deny/abstain and public-safe exposure decisions where material |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, source-role, geometry, hazards-boundary, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

A paired schema exists only as a lower-case scaffold and does not yet enforce fields.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/StructureFeature.md` |
| Confirmed schema path | `schemas/contracts/v1/domains/geology/structure_feature.schema.json` |
| Schema status | `PROPOSED` scaffold with empty `properties` and `additionalProperties: true` |
| Schema title | `Structure Feature` |
| Schema contract pointer | `contracts/domains/geology/structure_feature.md` |
| Casing/path posture | CONFLICTED / NEEDS VERIFICATION; requested PascalCase contract exists, schema points lower-case contract path |
| Family-name posture | `Fault Structure` in §10.B vs `StructureFeature` in §E / schema scaffold |
| Field-level enforcement | NEEDS VERIFICATION |

Until the casing, naming, and schema-field decision is resolved, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `StructureFeature` should semantically assert:

1. **Feature identity** — deterministic identity for the structural feature, source, geometry fingerprint, feature class, temporal scope, and normalized digest.
2. **Feature class** — fault, fold, joint, lineament, fracture, shear zone, structural surface, source-native class, candidate, or public derivative.
3. **Geometry support** — geometry ref, geometry fingerprint, CRS, line/polygon/surface/trace type, topology state, scale, precision, and public-safe derivative where released.
4. **Structural semantics** — sense of slip, confidence, dip/strike/orientation, displacement, certainty, activity/source label, or source-native descriptors where supported.
5. **Source identity** — SourceDescriptor, source record ID, map provenance, source role, source time, rights, cadence, and attribution.
6. **Evidence linkage** — source map, report, cross-section, geophysical observation, borehole/log evidence, field note, remote-sensing product, EvidenceRef, or EvidenceBundle.
7. **Interpretation support** — interpretation version, method, confidence, inferred/observed posture, and uncertainty/caveats.
8. **Hazards boundary** — explicit separation from rupture probability, hazard zoning, risk classification, emergency guidance, and alert authority.
9. **Temporal discipline** — source time, valid time, observed time where material, retrieval time, release time, and correction time remain distinct.
10. **Governance state** — validation, policy, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a fault trace as hazards risk | Hazards owns risk. Geology supplies structural context only. |
| Treating a structure as rupture probability | Probability and life-safety claims require Hazards authority and policy gates. |
| Treating structure geometry as public alert | KFM is not an alert authority; public alerts are outside this contract. |
| Treating source-native structure label as normalized class without review | Feature-class vocabulary and source semantics must be explicit. |
| Treating inferred lineaments as observed faults | Inferred/modeled features must retain source-role and confidence labels. |
| Treating cross-section display as source geometry | CrossSection is an interpretive carrier; source/evidence geometry remains separately governed. |
| Treating structure as land/title/permit proof | People/Land or regulatory/legal sources own those claims. |
| Treating a rendered tile/layer as canonical structure truth | Delivery artifacts are downstream carriers and must cite governed source/release state. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM structure-feature identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `StructureFeature`, `FaultStructure`, or accepted canonical spelling after ADR/schema reconciliation. |
| `feature_id` | Source-native or KFM structural feature identifier. |
| `feature_class` | Fault, fold, joint, lineament, fracture zone, shear zone, structural surface, contact-like trace, source-native, candidate, or public derivative. |
| `source_feature_class` | Source-native class label retained for audit. |
| `feature_name` | Public-safe feature name or label, where supported. |
| `source_feature_name` | Source-native feature name retained for audit. |
| `feature_vocabulary_ref` | Feature-class vocabulary, legend, code list, or source-native classification ref. |
| `map_provenance_id` | Source map / map edition / provenance ref. |
| `interpretation_version` | Source or KFM interpretation version. |
| `geometry_ref` | Internal line, polygon, surface, or trace geometry reference. |
| `public_geometry_ref` | Public-safe released geometry reference, if released. |
| `geometry_fingerprint` | Stable geometry fingerprint for identity and drift detection. |
| `crs` | Coordinate reference system / projection metadata. |
| `topology_state` | Valid, repaired, simplified, clipped, dissolved, invalid, or NEEDS VERIFICATION. |
| `precision_state` | Source precision, reviewed exact, generalized, aggregate, public-safe, withheld, or unknown. |
| `orientation_summary` | Strike/dip/plunge/orientation summary where source-supported. |
| `sense_of_slip` | Normal, reverse, strike-slip, oblique, unknown, source-native, or not applicable. |
| `confidence_state` | Observed, concealed, inferred, queried, approximate, modeled, unknown, or source-native confidence class. |
| `activity_context` | Source-native activity/age/recency context where supported; not hazards risk. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, regulatory, candidate, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native map feature, report, linework, layer, table, figure, or dataset record. |
| `geologic_unit_refs` | Linked GeologicUnit or SurficialUnit context. |
| `boundary_version_refs` | Linked GeologyBoundaryVersion refs for geometry lineage. |
| `cross_section_refs` | Linked CrossSection refs where feature appears. |
| `geophysical_observation_refs` | Linked GeophysicalObservation evidence. |
| `borehole_refs` | Linked BoreholeReference evidence where relevant. |
| `well_log_refs` | Linked well-log evidence where relevant. |
| `hazards_context_refs` | Hazards-owned refs only as downstream/adjacent context; no risk ownership. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Field/observation/acquisition time, where known and material. |
| `valid_time` | Time interval the structural interpretation claims to represent. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `policy_decision_ref` | Policy result governing use or public projection where material. |
| `review_record_ref` | Source, geology, structural-geology, spatial, hazards-boundary, or release review. |
| `validation_report_ref` | Validation report for schema, geometry, topology, feature vocabulary, source-role, hazards-boundary, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, feature reclass, geometry correction, confidence update, rights update, and rollback lineage. |
| `quality_flags` | Feature-class conflict, geometry invalid, confidence missing, source-role conflict, hazard-collapse risk, rights unknown, stale source, or incomplete evidence. |

---

## Feature classes

| Class | Meaning | Default posture |
|---|---|---|
| `fault` | Fault trace, surface, zone, or source-native fault feature. | Public-safe as geology context when rights allow; not risk. |
| `fold` | Anticline, syncline, fold axis, fold surface, or source-native fold feature. | Public-safe when source rights allow. |
| `joint` | Joint/fracture set or mapped joint feature. | Often local/detail-sensitive; review precision. |
| `lineament` | Linear feature or interpreted lineament. | Usually inferred/model-like; source-role and confidence required. |
| `fracture_or_shear_zone` | Fracture zone, shear zone, deformation zone. | Source role/confidence material. |
| `structural_surface` | Plane/surface/horizon with structural meaning. | May be interpreted/model-derived; version and uncertainty required. |
| `source_native_label` | Source structure class not yet normalized. | Preserve source label and mark normalization state. |
| `candidate_record` | Unreviewed import or unresolved feature. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical feature. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released public-safe feature geometry/label. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | StructureFeature posture |
|---|---|---|
| Mapped fault/fold/contact-like structural line from geologic map | `observed` with interpretation caveat | Evidence-bearing structural context; preserve source scale/version. |
| Concealed/inferred/queried fault or lineament | `modeled` or source-native inferred posture | Must retain inferred/confidence labels; never relabel as observed. |
| Regional compiled structural map | `aggregate` | Compiled support; preserve scale, version, and caveats. |
| Structural feature vocabulary/legend row | `administrative` | Defines labels/codes; not observation by itself. |
| Cross-section interpretation or reconstructed surface | `modeled` | Interpretation/reconstruction with version and reality-boundary caveats. |
| Hazards layer or risk classification | Hazards-owned source role | May be context only; Geology does not restate risk. |
| Unreviewed import, fuzzy geometry, unresolved feature class | `candidate` | Quarantine until identity, source role, geometry, vocabulary, and rights resolve. |
| AI-generated or hypothetical structure | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`StructureFeature` is geologic structure context, not downstream risk or alert authority.

```text
StructureFeature != Hazards risk
StructureFeature != rupture probability
StructureFeature != hazard zoning
StructureFeature != public alert
StructureFeature != GeologyBoundaryVersion
StructureFeature != GeologicUnit
StructureFeature != CrossSection
StructureFeature != GeophysicalObservation
StructureFeature != land / title / lease / permit proof
StructureFeature != AI summary
```

Any linkage must preserve source role, feature class, geometry lineage, confidence, evidence, rights, policy state, release state, and correction lineage.

---

## Sensitivity and release

StructureFeature geometry is generally public-safe at map feature scale when source rights allow. It can become policy-sensitive when it is interpreted as risk, when exact infrastructure/security context is exposed, when source rights restrict redistribution, or when inferred/model features are displayed without confidence caveats.

Rules:

- A structural feature is not automatically a released public layer.
- Public derivatives require validation, source rights, release manifest, correction path, and rollback target.
- Public outputs must preserve source role, source time, valid time, interpretation version, geometry precision, feature class, confidence, and caveats.
- Inferred/concealed/modelled features must not be visually or textually represented as observed.
- StructureFeature must not be used to imply hazards risk, rupture probability, public safety, emergency guidance, or alert status.
- Candidate, synthetic, rights-unknown, feature-class-conflicted, geometry-invalid, confidence-missing, stale, or evidence-incomplete features must not enter public outputs as authoritative structural facts.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native structural linework, polygons, surfaces, legends, confidence labels, reports, and metadata remain source-bound. |
| WORK / QUARANTINE | Candidate features are normalized, feature-class mapped, source-role checked, confidence labels preserved, geometry/topology checked, rights-screened, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, feature class, geometry fingerprint, source/valid times, interpretation version, evidence refs, rights state, and correction posture. |
| CATALOG / TRIPLET | Claims may be cataloged only with source role, source time, valid time, geometry lineage, confidence, evidence, and Hazards-boundary caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, review where material, release manifest, and rollback target. |
| PUBLISHED | Only released public-safe structure geometries, labels, graph claims, or API/UI payloads appear in public clients. |
| CORRECTION | Source update, feature reclass, geometry correction, confidence update, interpretation supersession, rights update, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Resolve naming drift between `Fault Structure`, `FaultStructure`, and `StructureFeature`.
- [ ] Resolve casing/path drift between `StructureFeature.md`, lower-case schema file, and lower-case schema `contract_doc` pointer.
- [ ] Expand `structure_feature.schema.json` from scaffold into field-level validation, or record the accepted schema path via ADR/schema PR.
- [ ] Add valid fixtures for fault, fold, joint, lineament, fracture/shear zone, structural surface, source-native label, candidate import, synthetic example, and public derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing feature class, missing geometry fingerprint, invalid geometry, inferred feature relabeled observed, structure treated as hazards risk/public alert, structure treated as title/permit proof, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, feature class, geometry fingerprint, CRS/topology, confidence state, source role, interpretation version, evidence refs, release refs, correction refs, and hazards-boundary constraints.
- [ ] Add policy/access tests proving public clients consume released public-safe derivatives only.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source revision, feature reclassification, geometry repair, confidence-label update, inferred/observed relabeling, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, feature class/geometry/source role validate, derivative is released | `ANSWER` / public-safe structural context may be shown |
| Evidence, source role, feature class, confidence, geometry, rights, or release support is incomplete | `ABSTAIN` |
| Claim would imply hazard risk/alert, expose restricted detail, relabel inferred as observed, or bypass release | `DENY` |
| Schema, validator, source-read, geometry, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Confirmed schema scaffold | Confirms lower-case schema file exists, is PROPOSED, and currently has empty properties. | Does not prove field validation; also exposes casing/path drift. |
| Geology scope doc | Confirms `Fault Structure` is Geology-owned for structural lines/surfaces with sense-of-slip and confidence, while Hazards owns risk. | Does not prove schema or implementation enforcement. |
| Geology object-family doc | Confirms StructureFeature/FaultStructure purpose, proposed key fields, material times, sensitivity posture, and Hazards boundary. | Field realization remains PROPOSED. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized StructureFeature weakens source integrity, misstates source role, collapses structure into Hazards risk, hides confidence, or depends on superseded source, geometry, rights, or release evidence.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source structural feature corrected, withdrawn, merged, split, or reclassified;
- geometry, topology, feature class, confidence state, or interpretation version corrected;
- inferred/concealed/modelled feature was presented as observed;
- structure was presented as rupture probability, hazard zoning, public alert, emergency guidance, or public-safety statement;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate features as public truth;
- public derivative lacks release manifest, correction path, or rollback target.

Rollback artifacts should include affected StructureFeature IDs, source record IDs, feature-class refs, geometry refs, confidence labels, boundary-version refs, public derivative refs, release IDs, evidence refs, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical family name `Fault Structure`, `FaultStructure`, or `StructureFeature`? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| Should the contract file be PascalCase `StructureFeature.md` or lower-case `structure_feature.md` to match the schema scaffold pointer? | CONFLICTED / NEEDS VERIFICATION | ADR, schema PR, or drift-register resolution. |
| Which feature-class vocabulary is canonical for faults, folds, joints, lineaments, and structural surfaces? | NEEDS VERIFICATION | Schema, source registry, and structural-geology steward review. |
| How should concealed/inferred/queried source labels be normalized without hiding confidence? | NEEDS VERIFICATION | Fixture and validator design. |
| What relationship predicates connect StructureFeature to Hazards without copying risk truth into Geology? | NEEDS VERIFICATION | Hazards/Geology cross-lane ADR and policy tests. |
| How should MapLibre/AI surfaces display structural context without implying risk or alert authority? | NEEDS VERIFICATION | API/UI/AI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/GeologicUnit.md` — mapped unit context that may cite structural features.
- `contracts/domains/geology/GeologyBoundaryVersion.md` — geometry lineage and boundary replacement history.
- `contracts/domains/geology/CrossSection.md` — interpretive panels that may show structures.
- `contracts/domains/geology/GeophysicalObservation.md` — geophysical evidence that may support structural interpretation.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary and Hazards exclusion.
- `docs/domains/geology/OBJECT_FAMILIES.md` — object-family reference, naming drift, and StructureFeature semantics.
- `schemas/contracts/v1/domains/geology/structure_feature.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `policy/sensitivity/geology/` — expected sensitivity policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Resolve Fault Structure / FaultStructure / StructureFeature naming drift.
- [ ] Resolve PascalCase vs lower-case contract/schema path drift.
- [ ] Expand paired schema and fixtures.
- [ ] Add validation for feature class, source role, geometry fingerprint, CRS/topology, confidence state, interpretation version, and evidence refs.
- [ ] Add anti-collapse tests for structure/hazards-risk/public-alert/unit/boundary/cross-section/UI-summary distinctions.
- [ ] Add source profiles and SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe structural derivatives and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved casing/path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
