<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-ecological-system
title: EcologicalSystem Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Ecological systems steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; habitat; ecological-system; classification; source-role-aware; evidence-bound; release-gated; anti-collapse
tags: [kfm, contracts, habitat, ecological_system, EcologicalSystem, ecological-system, classification, habitat-patch, land-cover, biotope, NatureServe, GAP, LANDFIRE, source-role, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./land_cover/observation.md
  - ./land_cover/class_scheme.md
  - ./land_cover/crosswalk.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/sublanes/biotopes.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../schemas/contracts/v1/domains/habitat/ecological_system.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/ecological_system/
  - ../../../tests/domains/habitat/ecological_system/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a scaffold at contracts/domains/habitat/ecological_system.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/ecological_system.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "The paired schema $id currently includes schemas/contracts/v1 in the URL path; confirm whether that is intended before treating schema IDs as stable external identifiers."
  - "EcologicalSystem is a Habitat-owned ecological classification object. It is not Flora Vegetation Community, not species occurrence truth, not regulatory critical habitat, not land-cover observation itself, not suitability, not connectivity/corridor, and not release authority."
  - "Land-cover docs mark EcologicalSystem as partial/upstream in the land-cover sublane: cover-class inputs and crosswalk material may originate there, while the synthesized EcologicalSystem object belongs to the ecological systems / biotopes slice of Habitat."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# EcologicalSystem — Habitat

> Semantic contract for Habitat `EcologicalSystem`: the governed classification object that records a source-role-bounded ecological-system label over a declared spatial and temporal scope, with classification scheme, evidence, uncertainty, sensitivity, release, correction, and rollback controls.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: EcologicalSystem" src="https://img.shields.io/badge/object-EcologicalSystem-blue">
  <img alt="Role: classification" src="https://img.shields.io/badge/role-classification-6f42c1">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: not occurrence truth" src="https://img.shields.io/badge/boundary-not__occurrence__truth-critical">
</p>

`contracts/domains/habitat/ecological_system.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [EcologicalSystem vs nearby objects](#ecologicalsystem-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Classification sources](#classification-sources) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/ecological_system.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/ecological_system.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine confirms `EcologicalSystem` as a canonical Habitat object family and the biotopes sublane treats ecological-system classification as Habitat-owned classification context. Field-level schema shape, fixtures, validators, source registry activation, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `EcologicalSystem` is a source-role-bounded classification object. It is **not** species occurrence truth, not Flora `Vegetation Community`, not regulatory critical habitat, not a land-cover observation by itself, not modeled suitability, not connectivity/corridor, not a management instruction, and not release authority.

---

## Meaning

`EcologicalSystem` records that a place, patch, cell, polygon, raster unit, or public-safe aggregate has been classified as an ecological system under a declared source, classification scheme, source role, temporal scope, and evidence basis.

It answers:

- Which ecological-system label is being asserted?
- Which classification scheme, source family, source record, source role, and source vintage support the label?
- Which spatial scope and temporal scope make the label valid?
- Which land-cover observation, class scheme, crosswalk, ecological inventory, or public-safe derivative supports the classification?
- Which EvidenceRefs, EvidenceBundles, uncertainty artifacts, policy decisions, review records, release manifests, correction notices, and rollback targets govern consequential use?

An ecological-system classification is useful for Habitat reasoning, but it is never a shortcut to species presence, plant taxonomy, regulatory designation, or management action.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| EcologicalSystem meaning | `contracts/domains/habitat/ecological_system.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/ecological_system.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Habitat object-family doctrine | `docs/domains/habitat/README.md` | Names `EcologicalSystem` in Habitat object-family spine |
| Biotopes / habitat-type grouping | `docs/domains/habitat/sublanes/biotopes.md` | Groups HabitatPatch, LandCoverObservation, and EcologicalSystem for habitat-type classification discussion |
| Land-cover inputs | `docs/domains/habitat/sublanes/land_cover.md` and `contracts/domains/habitat/land_cover/*` | May supply cover-class inputs and crosswalk material; does not own synthesized EcologicalSystem object |
| Source-role doctrine | `docs/domains/habitat/MODEL_VS_OBSERVATION.md` | Defines observed/model/regulatory/derivative/context anti-collapse behavior |
| Identity support | `contracts/domains/habitat/domain_feature_identity.md` | Shared deterministic identity and anti-collapse rules |
| Observation support | `contracts/domains/habitat/domain_observation.md` | Shared observation envelope, if the classification is observation-backed |
| Layer support | `contracts/domains/habitat/domain_layer_descriptor.md` | Public layer descriptor semantics; not classification truth |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Expected sensitivity/release gates; contents NEEDS VERIFICATION |
| Release | `release/` / `release/manifests/habitat/` | Expected release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/ecological_system.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Ecological System` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/ecological_system.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## EcologicalSystem vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `EcologicalSystem` | Ecological-system classification over a declared scope. | This contract. |
| `HabitatPatch` | Discrete habitat unit/patch identity and geometry. | Patch may carry or cite ecological-system classification; it is not the class itself. |
| `LandCoverObservation` | Land-cover class observation over place/time. | May support ecological-system classification, but stays land-cover evidence. |
| `ClassSchemeProfile` | Named/versioned class scheme. | EcologicalSystem must point to a scheme; it does not define the whole scheme alone. |
| `CoverClassCrosswalk` | Mapping between class schemes. | Crosswalk may support classification; it is not the classified place. |
| Flora `Vegetation Community` | Plant-community object owned by Flora. | Habitat may cite it as context; it does not own it. |
| Fauna/Flora occurrence record | Species occurrence truth. | EcologicalSystem is habitat context only. |
| `SuitabilityModel` | Modeled suitability surface. | May consume ecological-system classification; not the same object. |
| `ConnectivityEdge` / `Corridor` | Derived connectivity relation/geometry. | May consume ecological-system context; not classification truth. |
| Regulatory critical habitat | Authority designation. | EcologicalSystem is not a regulatory designation. |

---

## Assertions

A reviewed `EcologicalSystem` should semantically assert:

1. **Classification identity** — stable ID, source, classification scheme, object role, temporal scope, spatial scope, and digest basis.
2. **Classification label** — ecological-system code, name, rank, version, namespace, and scheme ref.
3. **Source role** — observed, modeled/model, regulatory, aggregate, administrative, candidate, synthetic, derivative, or context posture is explicit.
4. **Source support** — SourceDescriptor refs, source record refs, rights, citation, source vintage, and authority limits are visible.
5. **Spatial support** — geometry, raster/cell footprint, patch ref, analysis unit, or public-safe aggregate geometry role is declared.
6. **Temporal support** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
7. **Evidence support** — EvidenceRef/EvidenceBundle refs are present before consequential use.
8. **Uncertainty support** — accuracy, confidence, class ambiguity, model uncertainty, or classification caveat is linked where material.
9. **Policy support** — sensitivity, rights, source-role, and release policy decisions are linked where material.
10. **Correction support** — corrections, supersession, replacement classifications, stale state, and rollback targets are auditable.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating ecological-system class as species occurrence | Fauna/Flora own occurrence truth. |
| Treating it as Flora `Vegetation Community` | Flora owns plant-community semantics; Habitat may cite context only. |
| Treating it as regulatory critical habitat | Regulatory designation has distinct source role and authority burden. |
| Treating it as land-cover observation | LandCoverObservation owns land-cover class evidence. |
| Treating modeled classification as observed | Hides assumptions and uncertainty. |
| Treating classification as management instruction | KFM is not a management or emergency authority. |
| Reclassifying through renderer/style only | Crosswalks are first-class evidence artifacts, not silent styling. |
| Publishing sensitive occurrence-linked habitat type | Sensitive joins require fail-closed geoprivacy/redaction/release. |
| Treating AI label as source | AI is interpretive and evidence-subordinate. |
| Treating schema scaffold as implemented validator | Current schema is only a scaffold. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM ecological-system ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest over classification-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `EcologicalSystem`. |
| `ecological_system_id` | Source/KFM ecological-system identifier. |
| `system_namespace` | Classification namespace, e.g., NatureServe, GAP, LANDFIRE, state inventory, or accepted enum. |
| `system_code` | Ecological-system code. |
| `system_name` | Ecological-system display name. |
| `classification_rank` | Level/rank in classification hierarchy. |
| `classification_scheme_ref` | ClassSchemeProfile or external scheme ref. |
| `classification_scheme_version` | Version/vintage of scheme. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_record_refs` | Source-native record, raster, vector, table, API, or report refs. |
| `source_role` | Observed, modeled/model, regulatory, aggregate, administrative, candidate, synthetic, derivative, context, or accepted enum. |
| `supporting_land_cover_observation_refs` | LandCoverObservation refs used. |
| `supporting_crosswalk_refs` | Class/crosswalk refs used. |
| `habitat_patch_refs` | HabitatPatch refs carrying or using the system label. |
| `vegetation_community_context_refs` | Flora-owned context refs, if admitted. |
| `spatial_scope_ref` | Geometry, raster extent, patch, grid, analysis unit, or public-safe scope. |
| `geometry_fingerprint` | Internal geometry fingerprint, if geometry is identity-relevant. |
| `public_geometry_ref` | Public-safe generalized/aggregate geometry, if released. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/acquisition time where applicable. |
| `valid_time` | Valid interval for the classification claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `uncertainty_refs` | UncertaintySurface or classification-confidence refs. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind consequential use. |
| `validation_report_ref` | ValidationReport for schema, source role, scheme, geometry, time, evidence, sensitivity, and release readiness. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement class refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing scheme, unresolved source role, rights unknown, ambiguous class, stale source, crosswalk gap, sensitivity unresolved, release missing. |

---

## Classification sources

| Source family | Likely role | Required posture |
|---|---|---|
| NatureServe ecological systems | aggregate / authority context / controlled biodiversity context | Rights and terms NEEDS VERIFICATION; sensitive joins fail closed. |
| USGS GAP land cover / NVC-aligned products | modeled or observed depending source descriptor | Preserve source role and class-system version. |
| LANDFIRE EVT / BPS / vegetation layers | observed/model/context depending product | Preserve version, method, and uncertainty/caveat. |
| State ecological inventories | observed / aggregate / administrative depending source | Rights, steward review, and sensitivity required. |
| NLCD / land-cover observations | observed land-cover support | May support, but does not become ecological-system truth by itself. |
| Flora vegetation-community context | context only | Flora owns the plant-community object. |
| Fauna/Flora occurrence context | context only, public-safe | Species occurrence truth stays with source lane and geoprivacy applies. |
| AI/synthetic classification | synthetic/candidate only | Not source truth; requires review and evidence support. |

---

## Source-role rules

| Role | EcologicalSystem handling | Failure mode |
|---|---|---|
| `observed` | Direct inventory/observation classification with source vintage and class scheme. | Misclassification or stale source. |
| `modeled` / `model` | Classification produced by model or derived raster/product under assumptions. | Modeled-as-observed or modeled-as-regulatory. |
| `regulatory` / `authority` | Only if a competent authority designated a classification. | Treating designation as broader ecological truth. |
| `aggregate` | Public-safe summary or controlled biodiversity context. | Aggregate-as-exact. |
| `administrative` | Stewardship or agency context. | Administrative-as-title or management instruction. |
| `candidate` | Unreviewed classifier/crosswalk/watcher output. | Candidate-as-public. |
| `synthetic` | AI/simulated/reconstructed label. | Synthetic-as-observed. |
| `derivative` | Derived from land cover/crosswalk/model inputs. | Derived-as-primary source. |
| `context` | Consumed from Flora/Fauna/Soil/Hydrology/Agriculture through governed join. | Habitat adopts neighboring-lane truth. |

---

## Sensitivity and release

Ecological-system labels are often generally public at broad scale, but become sensitive when joined to rare species, precise occurrences, private stewardship, protected resources, or sensitive habitat corridors.

Rules:

- Public exact exposure fails closed when classification would reveal sensitive occurrence-linked habitat or stewardship context.
- Public derivatives may require generalized geometry, aggregate scope, delayed publication, or steward-only exact access.
- Source-role, rights, sensitivity, validation, review, release, correction, and rollback refs must resolve before public clients use ecological-system objects.
- Public UI/AI must show classification source role, scheme/version, uncertainty/caveat, public-safe geometry posture, stale/correction state, and evidence support.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate classification records.

---

## Lifecycle

| Phase | EcologicalSystem handling |
|---|---|
| RAW | Source records, classification schemes, rasters/vectors/tables, rights, sensitivity, and hashes are captured but not public truth. |
| WORK / QUARANTINE | Candidate classifications are normalized; role conflicts, scheme gaps, rights gaps, crosswalk errors, geometry/time issues, and sensitivity failures are held with reasons. |
| PROCESSED | Reviewed classifications bind source role, scheme/version, spatial scope, temporal scope, artifact digests, evidence refs, validation report, policy posture, and correction state. |
| CATALOG / TRIPLET | Classification claims may be projected only with EvidenceBundle refs, source-role caveats, and scheme/version context. |
| RELEASE CANDIDATE | Public ecological-system layers/API payloads require policy/review, public-safe geometry, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe classifications or derivatives appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source update, scheme update, crosswalk correction, geometry correction, role correction, policy change, or sensitivity review triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/ecological_system.schema.json` beyond an empty scaffold.
- [ ] Confirm canonical source-role enum spelling, including `model` vs `modeled` and `authority` vs `regulatory`.
- [ ] Add valid fixtures for NatureServe, GAP, LANDFIRE, state inventory, land-cover-supported, crosswalk-supported, public-aggregate, and sensitive-denied examples.
- [ ] Add invalid fixtures for missing scheme, missing source descriptor, missing evidence, unresolved rights, stale source, modeled-as-observed, modeled-as-regulatory, vegetation-community-as-Habitat-owned, species-occurrence-as-classification, silent renderer recode, sensitive exact public geometry, and missing rollback target.
- [ ] Add validator checks for scheme/version, source role, spatial/temporal scope, crosswalk refs, evidence refs, policy refs, sensitivity posture, release refs, and correction lineage.
- [ ] Add tests proving public map/UI/AI surfaces cannot treat ecological-system labels as species occurrence, regulatory designation, management instruction, or source-free truth.
- [ ] Confirm release tests proving public clients consume released public-safe classifications only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, scheme, role, scope, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe classification may support a claim |
| Evidence, role, scheme, rights, sensitivity, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, sensitive leak, candidate public path, silent recode, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current target scaffold | Confirms target existed as scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and empty-schema posture. | Does not prove field-level validation. |
| Habitat README | Confirms Habitat lane scope, source-role enum, source-family roster, object-family spine, lifecycle, sensitivity, exclusions, and cross-lane rules. | Some implementation paths remain PROPOSED / NEEDS VERIFICATION. |
| Land-cover sublane | Confirms land-cover slice treats `EcologicalSystem` as partial/upstream there and routes synthesized object responsibility elsewhere. | It is a sublane doc; field realization remains PROPOSED. |
| Biotopes sublane | Confirms the habitat-type grouping over HabitatPatch, LandCoverObservation, EcologicalSystem, and Flora-owned Vegetation Community. | `Biotope` itself is not KFM ubiquitous language and remains PROPOSED as a docs grouping. |
| Model-vs-observation doc | Confirms role separation and anti-collapse behavior. | Role spelling and exact schema/policy enforcement remain NEEDS VERIFICATION. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized ecological-system classification weakens source-role separation, classification-scheme integrity, evidence support, sensitivity posture, or release integrity.

Rollback triggers include:

- classification scheme, source record, source role, source vintage, crosswalk, geometry, temporal scope, artifact digest, evidence ref, policy decision, or release ref changes;
- modeled or derivative classification was presented as observed or regulatory;
- ecological-system label was presented as species occurrence, Flora vegetation-community ownership, regulatory critical habitat, or management instruction;
- sensitive exact classification or occurrence-linked habitat leaked publicly;
- candidate classification appeared in public API/UI/AI path;
- silent renderer/style reclassification replaced a reviewed crosswalk;
- public map tile, popup, AI answer, graph projection, or vector index was treated as classification truth;
- release, correction, or rollback refs were missing for public use.

Rollback artifacts should include affected ecological-system IDs, classification scheme refs, source refs, source-role refs, temporal-scope refs, artifact digests, geometry refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement classifications, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `ecological_system.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Is the schema `$id` path with `/schemas/contracts/v1/...` intentional? | NEEDS VERIFICATION | Schema steward review. |
| Which source-role spelling is canonical: `model` or `modeled`; `authority` or `regulatory`? | NEEDS VERIFICATION | Source-role/schema/policy review. |
| Which source families are activated first for EcologicalSystem: NatureServe, GAP, LANDFIRE, state inventories, or another source? | NEEDS VERIFICATION | Source activation decision and SourceDescriptor review. |
| Should this object live under a future Ecological Systems sublane doc distinct from biotopes? | NEEDS VERIFICATION | Habitat steward/docs steward review. |
| How should public ecological-system labels link to restricted exact geometry and public-safe generalized layers? | NEEDS VERIFICATION | Geoprivacy, policy, and release design review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./domain_observation.md`](./domain_observation.md) — domain observation envelope.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — deterministic identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./domain_validation_report.md`](./domain_validation_report.md) — validation-report support.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation contract.
- [`./land_cover/class_scheme.md`](./land_cover/class_scheme.md) — class scheme contract.
- [`./land_cover/crosswalk.md`](./land_cover/crosswalk.md) — cover-class crosswalk contract.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/sublanes/biotopes.md`](../../../docs/domains/habitat/sublanes/biotopes.md) — habitat-type / ecological-classification grouping.
- [`../../../docs/domains/habitat/sublanes/land_cover.md`](../../../docs/domains/habitat/sublanes/land_cover.md) — land-cover source/input boundary.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/ecological_system.schema.json`](../../../schemas/contracts/v1/domains/habitat/ecological_system.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
