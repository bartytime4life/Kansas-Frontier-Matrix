<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-geologic-unit
title: GeologicUnit Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Bedrock geology steward
  - OWNER_TBD — Stratigraphy steward
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
policy_label: public-with-gates; semantic-contract; geology; geologic-unit; map-unit; bedrock; interpretation-versioned; source-role-aware; release-gated
tags: [kfm, contracts, geology, GeologicUnit, geologic-unit, map-unit, bedrock, polygon, lithology, geologic-age, stratigraphic-interval, boundary-version, evidence, source-role, policy, release, correction, rollback]
related:
  - ./README.md
  - ./GeologicAge.md
  - ./CrossSection.md
  - ../../../docs/domains/geology/SCOPE.md
  - ../../../docs/domains/geology/OBJECT_FAMILIES.md
  - ../../../docs/domains/geology/sublanes/bedrock_geology.md
  - ../../../docs/domains/geology/sublanes/stratigraphy.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/geology/GeologicUnit.schema.json
  - ../../../schemas/contracts/v1/domains/geology/
  - ../../../policy/domains/geology/
  - ../../../fixtures/domains/geology/
  - ../../../tests/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a thin scaffold into a Geology GeologicUnit semantic contract."
  - "The exact paired schema path schemas/contracts/v1/domains/geology/GeologicUnit.schema.json was not found in this session; schema shape and casing remain NEEDS VERIFICATION."
  - "GeologicUnit is a mapped bedrock geologic-unit assertion, usually polygonal and interpretation-versioned. It does not replace Lithology, GeologicAge, StratigraphicInterval, GeologyBoundaryVersion, CrossSection, Soil, Hazards, Hydrology, People/Land, or release state."
  - "Public use requires evidence, rights, validation, policy/review where material, release manifest, correction path, and rollback target."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# GeologicUnit — Geology

> Semantic contract for Geology `GeologicUnit`: the evidence-bound object for mapped bedrock geologic-unit assertions, map-unit symbols, unit polygons, interpretation versions, lithology and age references, boundary lineage, public-safe derivatives, correction, and rollback.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: GeologicUnit" src="https://img.shields.io/badge/object-GeologicUnit-blue">
  <img alt="Schema: needs verification" src="https://img.shields.io/badge/schema-NEEDS__VERIFICATION-orange">
  <img alt="Boundary: unit not release approval" src="https://img.shields.io/badge/boundary-unit__not__release__approval-critical">
</p>

`contracts/domains/geology/GeologicUnit.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Unit classes](#unit-classes) · [Source-role rules](#source-role-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/GeologicUnit.md`  
> **Schema posture:** exact paired schema path `schemas/contracts/v1/domains/geology/GeologicUnit.schema.json` was **not found** in this session  
> **Truth posture:** the target contract path exists as a scaffold and is now expanded. Geology doctrine identifies `Geologic Unit` / `GeologicUnit` as a foundational owned object family for mapped lithostratigraphic / chronostratigraphic bedrock bodies and their attribution. Field-level schema shape, fixtures, validators, source registry records, policy runtime, release workflow, API behavior, UI behavior, and test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `GeologicUnit` is a mapped-unit assertion. It does **not** replace `Lithology`, `GeologicAge`, `StratigraphicInterval`, `GeologyBoundaryVersion`, `CrossSection`, `SurficialUnit`, Soil objects, Hydrology measurements, Hazards risk, land/title claims, or public release approval by itself.

---

## Meaning

`GeologicUnit` is the Geology semantic object for a mapped bedrock geologic unit or source map-unit assertion. It may represent a polygonal map unit, unit symbol, source-native legend row, normalized KFM unit record, map-edition-specific unit, or public-safe derivative.

It answers:

- Which geologic map unit is being asserted?
- Which source map, source version, map-unit symbol, unit name, interpretation version, geometry, and evidence support apply?
- Which lithology, geologic age, stratigraphic interval, boundary version, structure context, or cross-section interpretation may be linked without collapsing identity?
- What source role, source time, valid time, retrieval time, release time, and correction time govern the claim?
- What public-safe polygon or derivative may be shown, and which caveats must travel with it?
- Which validation report, policy decision where material, release manifest, correction notice, and rollback target govern downstream use?

A geologic unit can be public-safe at map-unit scale when rights and release gates allow. It remains source-bound, interpretation-versioned, evidence-bound, and correctable.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Geologic-unit meaning | `contracts/domains/geology/GeologicUnit.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/GeologicUnit.schema.json` or accepted variant | NEEDS VERIFICATION; exact path not found |
| Geology scope | `docs/domains/geology/SCOPE.md` | Confirms owned family and adjacent-lane exclusions |
| Object-family reference | `docs/domains/geology/OBJECT_FAMILIES.md` | Confirms purpose, key fields, source roles, sensitivity posture, and interpretation-version need |
| Bedrock / stratigraphy doctrine | `docs/domains/geology/sublanes/bedrock_geology.md`, `docs/domains/geology/sublanes/stratigraphy.md` | Expected context; path/content status may need verification |
| Source registry | `data/registry/sources/geology/` | Source identity, rights, cadence, authority limits |
| Policy | `policy/domains/geology/` | Allow/deny/abstain and public projection decisions |
| Fixtures and tests | `fixtures/domains/geology/`, `tests/domains/geology/` | Valid, invalid, source-role, geometry, release, and rollback proof cases |
| Release | `release/candidates/geology/`, `release/manifests/geology/` | Promotion decisions and rollback targets |

---

## Schema posture

No exact paired schema was confirmed for this casing/path in this session.

| Schema fact | Current posture |
|---|---|
| Requested contract path | `contracts/domains/geology/GeologicUnit.md` |
| Exact schema tried | `schemas/contracts/v1/domains/geology/GeologicUnit.schema.json` |
| Exact schema result | Not found in this session |
| Naming posture | `GeologicUnit` preserved because the user requested this path and Geology docs use this object-family spelling |
| Field-level enforcement | NEEDS VERIFICATION |

Until the schema is created or located under an accepted name, this contract is semantic guidance only.

---

## Assertions

A reviewed `GeologicUnit` should semantically assert:

1. **Unit identity** — deterministic identity for the source map unit, normalized unit, interpretation version, geometry fingerprint, and normalized digest.
2. **Source identity** — SourceDescriptor, source record ID, source map/legend ID, source role, source time, rights, cadence, and attribution.
3. **Unit label** — source-native unit symbol, source-native unit name, normalized KFM label, map-edition context, and alias/correlation caveats.
4. **Geometry support** — source polygon, boundary lineage, CRS, geometry fingerprint, topology state, and public-safe derivative geometry where released.
5. **Interpretation support** — interpretation version, map provenance, basis, evidence refs, and confidence/caveats.
6. **Lithology support** — linked Lithology refs or descriptor summaries without replacing the Lithology object.
7. **Age and interval support** — linked GeologicAge and StratigraphicInterval refs without collapsing age/interval identity into the unit.
8. **Temporal discipline** — source time, valid time, retrieval time, release time, correction time, and stale/supersession state remain distinct.
9. **Cross-lane boundary** — Soil, Hydrology, Hazards, People/Land, and UI/AI surfaces remain downstream or adjacent authority classes.
10. **Governance state** — validation, review, release, correction, supersession, and rollback references.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a unit polygon as soil truth | Geology may supply parent-material context; Soil owns soil objects. |
| Treating unit geometry as hazards risk | Hazards owns risk and alert posture. Geology supplies structural/map context only. |
| Treating a unit as a stratigraphic interval | StratigraphicInterval owns interval names and bounds. |
| Treating a unit as lithology itself | Lithology is a linked material characterization, not the unit identity. |
| Treating a unit as geologic age itself | GeologicAge is a linked age binding and vocabulary-versioned claim. |
| Treating a unit as a boundary history object | GeologyBoundaryVersion carries boundary lineage and replacement history. |
| Treating a rendered tile as canonical unit truth | Tiles are delivery artifacts; EvidenceBundle/source/release state carry authority. |
| Treating scaffold presence as release approval | Publication requires release manifest, validation, correction path, and rollback target. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema work. They are not enforced by any verified schema in this session.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM geologic-unit identity. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic content hash or integrity pin. |
| `domain` | Must resolve to `geology`. |
| `object_family` | `GeologicUnit`. |
| `unit_class` | Bedrock unit, source map unit, legend row, correlation unit, composite unit, candidate, synthetic, or public derivative. |
| `unit_code` | Normalized unit code or source map-unit symbol. |
| `source_unit_code` | Source-native map-unit symbol retained for audit. |
| `unit_name` | Normalized public-safe unit label. |
| `source_unit_name` | Source-native legend name retained for audit. |
| `map_provenance_id` | Source map / map edition / provenance ref. |
| `interpretation_version` | Explicit source or KFM interpretation version. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observed, modeled, aggregate, administrative, candidate, regulatory, or synthetic posture as accepted by KFM source-role rules. |
| `source_record_ref` | Source-native map, polygon, legend, or unit record. |
| `geometry_ref` | Internal polygon or multipolygon geometry reference. |
| `public_geometry_ref` | Public-safe released geometry reference, if released. |
| `geometry_fingerprint` | Stable geometry fingerprint for identity and drift detection. |
| `crs` | Coordinate reference system / projection metadata. |
| `topology_state` | Valid, repaired, simplified, clipped, dissolved, invalid, or NEEDS VERIFICATION. |
| `boundary_version_refs` | Linked GeologyBoundaryVersion refs for boundary lineage. |
| `lithology_refs` | Linked Lithology refs or descriptor set refs. |
| `age_refs` | Linked GeologicAge refs. |
| `stratigraphic_interval_refs` | Linked StratigraphicInterval refs. |
| `structure_feature_refs` | Linked structure/fault context refs, where applicable. |
| `cross_section_refs` | Linked CrossSection refs where the unit appears. |
| `surficial_context_refs` | Linked SurficialUnit or parent-material context refs when applicable; do not replace Soil. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Time interval the unit interpretation claims to represent. |
| `retrieval_time` | Time KFM retrieved the source. |
| `release_time` | Time a public-safe derivative was released. |
| `correction_time` | Time correction/supersession was applied. |
| `stale_state` | Current, historical, stale, superseded, withdrawn, or unknown. |
| `evidence_refs` | EvidenceRef/EvidenceBundle links. |
| `rights_state` | Rights, redistribution, attribution, access, and source-term posture. |
| `policy_decision_ref` | Policy result governing use or public projection where material. |
| `review_record_ref` | Source, geology, spatial, vocabulary, or release review. |
| `validation_report_ref` | Validation report for schema, geometry, topology, vocabulary, source-role, or release candidate. |
| `release_ref` | Release candidate, ReleaseManifest, PromotionDecision, or publication linkage. |
| `correction_refs` | CorrectionNotice, source update, boundary replacement, unit rename, geometry repair, rights update, and rollback lineage. |
| `quality_flags` | Missing provenance, topology invalid, source-role conflict, lithology missing, age missing, vocabulary conflict, rights unknown, stale source, or incomplete evidence. |

---

## Unit classes

| Class | Meaning | Default posture |
|---|---|---|
| `bedrock_unit` | Mapped bedrock geologic unit. | Public-safe when rights, source role, and release allow. |
| `source_map_unit` | Source-native unit row/polygon/legend entry. | Preserve source symbol/name/provenance. |
| `correlation_unit` | Unit correlated across sources/editions. | Requires evidence and review. |
| `composite_unit` | Composite or grouped unit. | Requires grouping semantics and caveats. |
| `candidate_record` | Unreviewed import or unresolved source unit. | WORK/QUARANTINE until reviewed. |
| `synthetic` | Generated/hypothetical unit label or panel-only simplification. | Reality-boundary disclosure; not source evidence. |
| `public_derivative` | Released public-safe unit geometry/label. | Requires release manifest and rollback target. |

---

## Source-role rules

| Source pattern | Canonical source-role posture | GeologicUnit posture |
|---|---|---|
| Field-mapped geologic map/contact/unit polygon | `observed` with interpretation caveat | Supports map-unit claim when provenance, geometry, and interpretation version resolve. |
| Generalized state map, compiled map, atlas, regional synthesis | `aggregate` | Compiled support; preserve scale/source version and caveats. |
| Interpolated/model-derived unit surface or inferred contact | `modeled` | Must remain modeled/inferred with uncertainty. |
| Source legend row, administrative unit code, catalog row | `administrative` | Defines labels/metadata, not observed geometry by itself. |
| Unreviewed import, unresolved map-unit symbol, invalid polygon | `candidate` | Quarantine until source, geometry, and vocabulary resolve. |
| AI-generated or hypothetical unit | `synthetic` | Reality-boundary disclosure; not source evidence. |

---

## Anti-collapse rules

`GeologicUnit` is a map-unit assertion, not its linked support objects.

```text
GeologicUnit != Lithology
GeologicUnit != GeologicAge
GeologicUnit != StratigraphicInterval
GeologicUnit != GeologyBoundaryVersion
GeologicUnit != CrossSection
GeologicUnit != SurficialUnit
GeologicUnit != Soil mapunit
GeologicUnit != Hazards risk
GeologicUnit != Hydrology measurement
GeologicUnit != public tile/layer release
GeologicUnit != AI summary
```

Any linkage must preserve object identity, source role, interpretation version, evidence, rights, validation, release, and correction state.

---

## Sensitivity and release

Geologic unit polygons are generally public-safe at unit/line scale when source rights allow, but public use still requires governed release. Interpretation version, source scale, rights, geometry lineage, topology, and caveats must travel with the public derivative.

Rules:

- A source map-unit polygon is not automatically a released KFM public layer.
- Public derivatives require validation, source rights, release manifest, correction path, and rollback target.
- Map/API/UI/AI surfaces must preserve source role, source time, valid time, interpretation version, geometry precision, and caveats.
- Candidate, synthetic, rights-unknown, topology-invalid, stale, or evidence-incomplete records must not enter public outputs as authoritative unit facts.
- Cross-lane use must not harden Geology context into Soil, Hydrology, Hazards, People/Land, or UI/AI truth.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native map units, polygons, legends, metadata, unit labels, CRS, and rights remain source-bound. |
| WORK / QUARANTINE | Candidate units are normalized, source-role checked, geometry/topology checked, vocabulary-mapped, rights-screened, and evidence-linked. |
| PROCESSED | Reviewed records receive deterministic identity, interpretation version, geometry fingerprint, unit/label refs, evidence refs, rights state, and correction posture. |
| CATALOG / TRIPLET | Unit claims may be cataloged only with source role, source time, valid time, interpretation version, evidence, geometry lineage, and caveats preserved. |
| RELEASE CANDIDATE | Public derivatives require validation report, review where material, release manifest, and rollback target. |
| PUBLISHED | Only released public-safe unit layers, labels, graph claims, or API/UI payloads appear in public clients. |
| CORRECTION | Source update, boundary replacement, unit rename, geometry repair, vocabulary correction, rights update, or stale-state update triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Create or locate the accepted paired schema path.
- [ ] Add valid fixtures for bedrock unit, source map unit, correlation unit, composite unit, candidate record, synthetic display label, and public derivative.
- [ ] Add invalid fixtures for missing source descriptor, missing unit code, missing map provenance, invalid topology, missing interpretation version, source role collapse, unit treated as lithology/age/interval/boundary, unit treated as soil/hazards/hydrology truth, missing release manifest, and missing rollback target.
- [ ] Add validator checks for deterministic identity, source unit code, source map provenance, interpretation version, geometry fingerprint, CRS/topology, lithology refs, age refs, interval refs, evidence refs, release refs, and correction refs.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for source map revision, unit rename, geometry repair, boundary replacement, vocabulary update, public derivative rebuild, and rollback.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Evidence resolves, geometry validates, rights allow, derivative is released | `ANSWER` / public-safe unit claim may be shown |
| Evidence, source role, geometry, interpretation version, rights, or provenance is incomplete | `ABSTAIN` |
| Claim would bypass release, misstate source role, or collapse adjacent-domain truth | `DENY` |
| Schema, validator, source-read, topology, transform, or release-runtime failure | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms the target file existed and was a scaffold before replacement. | Does not prove contract maturity. |
| Geology scope doc | Confirms Geology owns Geologic Unit and preserves adjacent-domain ownership boundaries. | Records broader naming drift and field realization remains PROPOSED. |
| Geology object-family doc | Confirms GeologicUnit purpose, proposed key fields, material times, sensitivity posture, typical source roles, and interpretation-version requirement. | Does not prove schema or validator enforcement. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized GeologicUnit weakens source integrity, misstates source role, hides interpretation version, breaks geometry lineage, collapses linked object identity, or depends on superseded source, geometry, vocabulary, rights, or release evidence.

Rollback triggers include:

- schema/name/casing is superseded by ADR or schema decision;
- source map or unit legend corrected, withdrawn, or superseded;
- boundary geometry repaired or replaced;
- unit symbol/name/vocabulary corrected;
- lithology, age, interval, boundary, or cross-section refs corrected;
- public API/UI/AI uses RAW/WORK/QUARANTINE or candidate units as public truth;
- public derivative lacks release manifest, correction path, or rollback target.

Rollback artifacts should include affected GeologicUnit IDs, source map refs, unit codes, geometry refs, boundary-version refs, linked lithology/age/interval refs, public derivative refs, release IDs, evidence refs, validation reports, correction notices, rollback cards, replacement records, and suppression/rebuild instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| What is the accepted paired schema path and casing for `GeologicUnit`? | NEEDS VERIFICATION | Schema-home inspection and ADR-0001 alignment. |
| Which source map/provenance fields define deterministic unit identity? | NEEDS VERIFICATION | Source registry, schema, and fixture review. |
| How should unit grouping/correlation across map editions be represented? | NEEDS VERIFICATION | Stratigraphy/bedrock steward review. |
| Should public derivatives be separate contract objects or release projections? | PROPOSED / NEEDS VERIFICATION | Release and schema review. |
| How should GeologicUnit link to GeologyBoundaryVersion without duplicating boundary lineage? | NEEDS VERIFICATION | Boundary-version contract/schema review. |
| How should MapLibre/AI surfaces display interpretation version without clutter? | NEEDS VERIFICATION | API/UI projection review. |

---

## Related contracts and docs

- `contracts/domains/geology/GeologicAge.md` — age binding and vocabulary-versioned geologic-time claims.
- `contracts/domains/geology/CrossSection.md` — interpretive panels that may display unit labels.
- `docs/domains/geology/SCOPE.md` — Geology owns/does-not-own boundary.
- `docs/domains/geology/OBJECT_FAMILIES.md` — Geology object-family reference and unit semantics.
- `schemas/contracts/v1/domains/geology/` — expected machine-shape home, pending verification.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Create or verify paired schema and fixtures.
- [ ] Add validation for unit code, map provenance, geometry fingerprint, topology, interpretation version, source role, and linked refs.
- [ ] Add anti-collapse tests for unit/lithology/age/interval/boundary/soil/hazards/hydrology/UI-summary distinctions.
- [ ] Add source profiles or SourceDescriptor records before activation.
- [ ] Confirm public map/API/UI surfaces use only released public-safe unit layers and caveats.
- [ ] Confirm EvidenceBundle resolution before public or AI claims.
- [ ] Confirm correction and rollback targets before promotion.
- [ ] Record unresolved path/schema/source-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
