<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-land-cover-class-scheme
title: Land Cover Class Scheme Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Land-cover steward
  - OWNER_TBD — Classification-scheme steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; habitat; land-cover; class-scheme; ClassSchemeProfile; source-vintage-aware; evidence-bound; crosswalk-aware; release-gated
tags: [kfm, contracts, habitat, land_cover, class_scheme, ClassSchemeProfile, land-cover-legend, classification-scheme, source-vintage, nlcd, landfire, gap, nwi, cdl-adjacency, crosswalk, evidence, source-role, policy, release, correction, rollback]
related:
  - ../../README.md
  - ./change_summary.md
  - ../../../../docs/domains/habitat/README.md
  - ../../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json
  - ../../../../schemas/contracts/v1/domains/habitat/land_cover/
  - ../../../../policy/domains/habitat/land_cover/
  - ../../../../fixtures/domains/habitat/land_cover/class_scheme/
  - ../../../../tests/domains/habitat/land_cover/class_scheme/
  - ../../../../data/registry/sources/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "Expanded from a thin scaffold into a Habitat land-cover class-scheme semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "The land-cover sublane uses ClassSchemeProfile for the object-family concept, while this requested file path is class_scheme.md and the paired schema title is Class Scheme. This contract treats class_scheme.md as the semantic contract for ClassSchemeProfile unless a later ADR/schema decision says otherwise."
  - "Class schemes name and pin versioned land-cover legends/classification systems. They do not perform crosswalks, reclassifications, source activation, observation truth, change summaries, public layer release, or HabitatPatch/SuitabilityModel claims by themselves."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Cover Class Scheme — Habitat

> Semantic contract for `ClassSchemeProfile`: the Habitat land-cover object that names, versions, and governs a source classification scheme or legend before `LandCoverObservation`, crosswalk, change-summary, public layer, or downstream Habitat reasoning can use its classes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Sublane: land cover" src="https://img.shields.io/badge/sublane-land__cover-6a5acd">
  <img alt="Object: ClassSchemeProfile" src="https://img.shields.io/badge/object-ClassSchemeProfile-blue">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: scheme not crosswalk" src="https://img.shields.io/badge/boundary-scheme__not__crosswalk-critical">
</p>

`contracts/domains/habitat/land_cover/class_scheme.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Scheme classes](#scheme-classes) · [Source-role rules](#source-role-rules) · [Crosswalk and change-summary boundaries](#crosswalk-and-change-summary-boundaries) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/land_cover/class_scheme.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Naming posture:** the land-cover sublane names the object family `ClassSchemeProfile`; the requested path and schema title use `Class Scheme`. This file treats `class_scheme.md` as the current semantic contract for `ClassSchemeProfile`, pending schema/ADR confirmation.  
> **Truth posture:** Habitat land-cover doctrine defines class schemes as named, versioned classification systems whose versions are immutable once published. Field-level schema shape, fixtures, validators, source registry records, policy files, release artifacts, API behavior, UI behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A class scheme names and pins a classification vocabulary. It is **not** a `LandCoverObservation`, not a `CoverClassCrosswalk`, not a `LandCoverChangeSummary`, not a source activation decision, not a raster, not a HabitatPatch, not a species/plant occurrence claim, not a critical-habitat designation, and not a public release artifact by itself.

---

## Meaning

`ClassSchemeProfile` records the meaning, provenance, version, class codes, labels, hierarchy, nodata/unknown handling, and allowed use posture of a land-cover classification scheme.

It answers:

- Which source family and classification system is being used?
- Which version, edition, legend, source vintage, or source-native scheme ID is pinned?
- Which class codes and class labels are valid, deprecated, reserved, nodata, unknown, aggregate, or source-native only?
- Which source descriptor, source role, rights posture, evidence refs, and citation rules apply?
- Which `LandCoverObservation` records may cite this scheme?
- Which crosswalks or change summaries depend on this scheme without silently recoding it?
- Which validation, correction, release, and rollback records govern downstream use?

A class scheme is a vocabulary anchor. It makes source labels inspectable. It does not itself assert land-cover presence anywhere.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Class-scheme meaning | `contracts/domains/habitat/land_cover/class_scheme.md` | Owned here by request; object-family naming needs verification |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Land-cover doctrine | `docs/domains/habitat/sublanes/land_cover.md` | Defines class scheme term, object identity, source families, source-role separations, and lifecycle context |
| Source registry | `data/registry/sources/habitat/` | Source identity, source role, rights, cadence, activation |
| Crosswalk contracts | `contracts/domains/habitat/land_cover/` or accepted future path | Crosswalk meaning belongs outside this file unless an ADR consolidates it |
| Threshold policy | `policy/domains/habitat/land_cover/` | Materiality/crosswalk/change-summary policy home; contents NEEDS VERIFICATION |
| Fixtures and tests | `fixtures/domains/habitat/land_cover/class_scheme/`, `tests/domains/habitat/land_cover/class_scheme/` | PROPOSED / NEEDS VERIFICATION |
| Executable logic | `pipelines/domains/habitat/land_cover/` | Expected processing home; not this contract |
| Declarative specs | `pipeline_specs/habitat/land_cover/` | Expected config home; not this contract |
| Release | `release/manifests/habitat/` | Expected release/correction/rollback home; release instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Class Scheme` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/sublanes/land_cover.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Assertions

A reviewed `ClassSchemeProfile` should semantically assert:

1. **Scheme identity** — deterministic identity from `scheme_namespace + scheme_id + scheme_version`.
2. **Source family** — NLCD, LANDFIRE, GAP, NWI, NatureServe, state inventory, remote-sensing-derived scheme, or accepted source family.
3. **Source role** — observation product, cross-reference authority, controlled-distribution source, adjacency-only context, modeled output, administrative scheme, or candidate.
4. **Version pin** — class-scheme versions are immutable once published; changes create new versions or correction lineage.
5. **Class inventory** — valid class codes, labels, descriptions, hierarchy/parent classes, nodata/unknown/reserved classes, deprecated classes, and source-native values.
6. **Citation and rights** — source descriptor, attribution, rights, terms, license, cadence, source vintage, and access state.
7. **Use constraints** — what observation types may cite the scheme and what crosswalk/change-summary operations require review.
8. **Evidence binding** — source legend, documentation, source table, PDF, API response, raster attribute table, EvidenceRef/EvidenceBundle refs, and artifact digests.
9. **Temporal discipline** — source time, valid time, retrieval time, release time, and correction time remain distinct.
10. **Governance state** — validation report, policy decision where material, review record, release/correction/rollback refs.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating class scheme as observed land cover | Schemes define labels; `LandCoverObservation` applies them to space/time. |
| Treating class scheme as a crosswalk | Crosswalks map between schemes and need separate review/versioning. |
| Treating class scheme version changes as in-place edits | Published scheme versions are immutable; corrections require lineage. |
| Treating NLCD/LANDFIRE/GAP/NWI classes as interchangeable | Each scheme has its own source, vocabulary, hierarchy, and caveats. |
| Treating CDL as Habitat land-cover scheme | CDL is Agriculture-owned adjacency unless governed join rules say otherwise. |
| Treating NWI as regulatory wetland delineation | NWI may be wetland observation/context; regulatory determinations are separate. |
| Treating source legend as source activation | SourceDescriptor, rights, role, fixtures, validators, and activation decision are separate gates. |
| Treating scheme as public release | ReleaseManifest and public layer artifacts own publication. |
| Treating UI legend as canonical scheme | UI legends are downstream carriers and must cite the scheme. |
| Treating schema scaffold as implementation readiness | Current schema is a scaffold; validation enforcement remains unverified. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM class-scheme profile ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized scheme digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `ClassSchemeProfile`, pending naming confirmation. |
| `scheme_namespace` | Source namespace such as `nlcd`, `landfire`, `gap`, `nwi`, `nass_cdl`, or accepted enum. |
| `scheme_id` | Stable scheme identifier. |
| `scheme_version` | Version, edition, year, release, or source-native legend version. |
| `scheme_title` | Human-readable title. |
| `scheme_kind` | Categorical, continuous-binned, fractional, wetland-class, vegetation-type, crop-adjacency, ecological-system, modeled, source-native, or candidate. |
| `source_family` | NLCD, LANDFIRE, GAP, NWI, NatureServe, state inventory, remote-sensing index, CDL adjacency, or accepted source family. |
| `source_descriptor_ref` | Source identity, rights, cadence, attribution, authority limits. |
| `source_role` | Observation product, cross-reference, controlled distribution, adjacency, modeled, administrative, candidate, or accepted KFM enum. |
| `legend_artifact_ref` | Source legend/table/report/API artifact ref. |
| `legend_artifact_digest` | Digest for source legend artifact. |
| `class_table_ref` | Structured table of codes/labels/descriptions. |
| `class_count` | Count of active classes. |
| `nodata_codes` | Values that mean nodata. |
| `unknown_codes` | Values that mean unknown/unclassified. |
| `reserved_codes` | Values reserved by source scheme. |
| `deprecated_codes` | Values deprecated/superseded by source scheme. |
| `hierarchy_ref` | Parent/child class hierarchy or grouping ref, if any. |
| `color_table_ref` | Optional source color table; style is not truth. |
| `valid_source_vintages` | Source vintages that may cite this scheme. |
| `valid_observation_types` | Observation types allowed to use the scheme. |
| `crosswalk_policy_ref` | Policy/review rules for mapping to/from other schemes. |
| `allowed_crosswalk_refs` | Reviewed CoverClassCrosswalk refs. |
| `release_ref` | ReleaseManifest or PromotionDecision ref where the scheme is publicly surfaced. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the scheme. |
| `validation_report_ref` | Validation report for scheme shape, source role, class inventory, and rights. |
| `policy_decision_ref` | Policy decision where material. |
| `review_record_ref` | Steward review record. |
| `source_time` | Source publication/assertion time. |
| `valid_time` | Scheme validity interval. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `correction_refs` | CorrectionNotice, supersession, replacement scheme refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source descriptor, rights unknown, class collision, label conflict, nodata ambiguity, hierarchy conflict, source-vintage mismatch, unreviewed crosswalk, stale source. |

---

## Scheme classes

| Scheme class | Meaning | Default posture |
|---|---|---|
| `nlcd_legend` | NLCD categorical land-cover legend. | Public source-family candidate; activation still needs SourceDescriptor and validation. |
| `landfire_evt` | LANDFIRE Existing Vegetation Type scheme. | Observation/context scheme; preserve version and source caveats. |
| `landfire_bps` | LANDFIRE Biophysical Settings scheme. | Context/model-related caveats required. |
| `gap_land_cover` | USGS GAP/NVC-aligned land-cover classification. | Source-family candidate; sparse update cadence caveat. |
| `nwi_wetland_class` | NWI wetland classification scheme. | Wetland observation/context; not regulatory delineation by itself. |
| `ecological_system_ref` | NatureServe/ecological-system controlled-distribution or cross-reference scheme. | Rights and sensitive joins fail closed until reviewed. |
| `remote_sensing_bins` | Derived class bins from continuous remote-sensing indices. | Modeled/derived; not direct categorical source scheme unless reviewed. |
| `cdl_adjacency` | USDA NASS CDL classes used as Agriculture-owned adjacency. | Context only; not Habitat scheme unless ADR/policy allows. |
| `state_inventory_scheme` | State ecological inventory class scheme. | Authority/rights vary; review required. |
| `candidate_scheme` | Unreviewed or imported source-native scheme. | WORK/QUARANTINE; no public edge. |

---

## Source-role rules

| Source family / scheme | Required handling |
|---|---|
| NLCD | Observation product, not regulatory law or critical habitat. Preserve version/source vintage. |
| LANDFIRE EVT/BPS/FDist | Vegetation/fuel/ecological context. Do not convert into fire prediction or observed species presence. |
| USGS GAP | Land-cover/NVC-aligned context. Preserve sparse update cadence and source version. |
| NWI | Wetland observation/context, not a regulatory wetlands delineation under §404. |
| NatureServe / ecological systems | Controlled-distribution or rights-sensitive cross-reference. Rights and joins NEED VERIFICATION. |
| State inventories | Authority class varies. Preserve source-specific role and review state. |
| Remote-sensing bins/models | Derived/modeled unless source evidence supports a narrower role. |
| USDA NASS CDL | Agriculture-owned crop observation adjacency; do not silently reclassify as Habitat cover. |

---

## Crosswalk and change-summary boundaries

Class schemes are the input vocabulary for crosswalks and summaries; they are not the transform.

```text
ClassSchemeProfile != CoverClassCrosswalk
ClassSchemeProfile != LandCoverObservation
ClassSchemeProfile != LandCoverChangeSummary
ClassSchemeProfile != LayerManifest
ClassSchemeProfile != ReleaseManifest
```

Rules:

- Any mapping between two class schemes must be a reviewed, versioned, citable crosswalk.
- Crosswalks must not be hidden inside renderers or notebooks.
- Change summaries must reference the schemes and crosswalks used, not just final class labels.
- Class-scheme versions are immutable once published; corrections create new lineage.
- UI legends and color tables may render class schemes, but they do not define them.

---

## Sensitivity and release

Class schemes are usually public-safe, but not always public-ready.

Rules:

- Public display requires source attribution, rights posture, source version, evidence refs, and release support where material.
- Controlled-distribution or rights-restricted schemes must not be copied into public artifacts without rights review.
- Source labels that imply sensitive habitats or rare ecological communities must not be joined to sensitive occurrence detail without policy/review/geoprivacy support.
- Public layers and Focus Mode cards must expose enough scheme/version context to prevent misleading comparisons.
- Public clients use governed APIs and released artifacts, not source legends or internal stores directly.

---

## Lifecycle

| Phase | Expected handling |
|---|---|
| RAW | Source-native legends, class tables, PDFs, API responses, raster attribute tables, and color tables remain source-bound. |
| WORK / QUARANTINE | Candidate schemes are normalized, source-role checked, rights reviewed, class inventory parsed, nodata/unknown handling reviewed, and evidence-linked. |
| PROCESSED | Reviewed scheme profiles receive deterministic identity, source refs, class table refs, evidence refs, validation report refs, and correction posture. |
| CATALOG / TRIPLET | Scheme claims may be cataloged with source role, version, class inventory, EvidenceBundle refs, and crosswalk caveats. |
| RELEASE CANDIDATE | Public scheme references, legends, API payloads, or layer legends require validation, policy/review where material, release refs, correction path, and rollback target. |
| PUBLISHED | Only released public-safe scheme references and legends appear in public clients. |
| CORRECTED / SUPERSEDED | Source legend update, class label correction, code deprecation, hierarchy change, rights change, or crosswalk correction triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand the paired schema beyond an empty scaffold.
- [ ] Decide whether `ClassSchemeProfile` or `ClassScheme` is the accepted object-family name.
- [ ] Add valid fixtures for NLCD, LANDFIRE EVT, GAP, NWI, NatureServe/ecological-system reference, remote-sensing bins, CDL adjacency, state inventory, candidate scheme, and public derivative examples.
- [ ] Add invalid fixtures for missing source descriptor, missing scheme version, duplicate class code, label conflict, nodata ambiguity, unreviewed crosswalk, source-vintage mismatch, rights unknown, controlled-distribution public leak, and class scheme used as observation truth.
- [ ] Add validator checks for deterministic identity, class inventory integrity, nodata/unknown handling, source-role preservation, rights state, evidence refs, immutable versioning, and correction lineage.
- [ ] Add tests proving UI legends, layers, change summaries, and crosswalks cannot silently redefine schemes.
- [ ] Add release tests proving public clients consume released scheme metadata only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, version, class inventory, rights, evidence, validation, and release support all resolve | `ANSWER` / public-safe scheme reference may be shown |
| Evidence, source role, rights, version, class inventory, or release support is incomplete | `ABSTAIN` / `HOLD` |
| Scheme would be used as observation/crosswalk/release truth, rights-restricted labels would leak, or source role would collapse | `DENY` |
| Schema, validator, source read, legend parse, evidence lookup, policy, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current contract scaffold | Confirms the target file existed as a scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat land-cover sublane doc | Defines `ClassSchemeProfile`, class scheme, crosswalk, source families, identity rule, source-role separations, lifecycle, and map product boundaries. | Many field realizations and paths remain PROPOSED. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | It is an authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized class scheme weakens source integrity, silently changes class meaning, collapses crosswalk/observation truth, or lets public outputs compare incompatible schemes.

Rollback triggers include:

- class scheme renamed, corrected, withdrawn, or superseded by source;
- scheme version changed in place instead of creating a corrected/superseded lineage;
- class code/label collision discovered;
- nodata/unknown/reserved class handling corrected;
- source role, rights, or controlled-distribution status corrected;
- a crosswalk or change summary used the wrong scheme version;
- UI legend, color table, or public layer rendered classes without scheme/version context;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate scheme as public truth.

Rollback artifacts should include affected scheme IDs, scheme version refs, source descriptor refs, source legend refs, class table refs, crosswalk refs, observation refs, change-summary refs, public layer refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement schemes, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is the canonical object name `ClassSchemeProfile` or `ClassScheme`? | NEEDS VERIFICATION | Habitat contract/schema naming review. |
| Which fields must be required in `class_scheme.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which source-family schemes should be activated first? | NEEDS VERIFICATION | SourceDescriptor activation review. |
| Which class-code tables are rights-cleared for public display? | NEEDS VERIFICATION | Source rights and release review. |
| How should color tables be handled without making style canonical truth? | NEEDS VERIFICATION | Map/UI style contract review. |
| Which crosswalk relationships are allowed before full ecological-system synthesis exists? | NEEDS VERIFICATION | Land-cover + ecological-systems steward review. |

---

## Related contracts and docs

- `contracts/domains/habitat/land_cover/change_summary.md` — change summaries that must reference schemes and crosswalks.
- `docs/domains/habitat/sublanes/land_cover.md` — land-cover sublane doctrine and object-family context.
- `docs/domains/habitat/SOURCE_FAMILIES.md` — Habitat source-family role, rights, and sensitivity posture.
- `schemas/contracts/v1/domains/habitat/land_cover/class_scheme.schema.json` — confirmed scaffold schema, pending expansion.
- `policy/domains/habitat/land_cover/` — expected source-role/materiality/crosswalk policy home, pending verification.
- `release/manifests/habitat/` — expected release/rollback home, pending verification.

[Back to top](#top)
