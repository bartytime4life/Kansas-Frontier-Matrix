<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-habitat-patch-contract
title: HabitatPatch Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — HabitatPatch steward
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
policy_label: public-with-gates; semantic-contract; habitat; habitat-patch; polygonal-unit; source-role-aware; evidence-bound; sensitivity-aware; release-gated; anti-collapse
tags: [kfm, contracts, habitat, HabitatPatch, habitat-patch, patch, polygon, public-safe-geometry, source-role, evidence, policy, sensitivity, geoprivacy, release, correction, rollback, anti-collapse]
related:
  - ./README.md
  - ./habitat_patch.md
  - ./domain_observation.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./domain_validation_report.md
  - ./ecological_system.md
  - ./SuitabilityModel.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./land_cover/observation.md
  - ./land_cover/class_scheme.md
  - ./land_cover/crosswalk.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/sublanes/biotopes.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../schemas/contracts/v1/domains/habitat/habitat_patch.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/habitat_patch/
  - ../../../tests/domains/habitat/habitat_patch/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a scaffold at contracts/domains/habitat/habitat-patch.contract.md."
  - "CONFLICTED / NEEDS VERIFICATION: the requested file is habitat-patch.contract.md, while the paired schema's x-kfm.contract_doc points to contracts/domains/habitat/habitat_patch.md, and that sibling file also exists as a scaffold. This update preserves the requested path and does not delete or merge the sibling scaffold."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/habitat_patch.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "HabitatPatch is a discrete polygonal habitat unit and one of the Habitat lane's canonical object families. It is not species occurrence truth, not Flora vegetation-community ownership, not regulatory critical habitat, not modeled suitability, not a connectivity edge/corridor, and not release authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# HabitatPatch Contract — Habitat

> Semantic contract for `HabitatPatch`: the governed Habitat object for a discrete habitat unit or public-safe patch geometry, preserving source role, spatial/temporal scope, evidence, sensitivity posture, release state, correction lineage, and rollback support.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: HabitatPatch" src="https://img.shields.io/badge/object-HabitatPatch-blue">
  <img alt="Geometry: public-safe required" src="https://img.shields.io/badge/geometry-public--safe__required-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: patch not occurrence" src="https://img.shields.io/badge/boundary-patch__not__occurrence-critical">
</p>

`contracts/domains/habitat/habitat-patch.contract.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Naming conflict](#naming-conflict) · [Schema posture](#schema-posture) · [HabitatPatch vs nearby objects](#habitatpatch-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Patch sources](#patch-sources) · [Source-role rules](#source-role-rules) · [Geometry and sensitivity](#geometry-and-sensitivity) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Requested contract path:** `contracts/domains/habitat/habitat-patch.contract.md`  
> **Conflicting sibling path:** `contracts/domains/habitat/habitat_patch.md` — also exists as a scaffold.  
> **Schema path:** `schemas/contracts/v1/domains/habitat/habitat_patch.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine confirms `HabitatPatch` as a canonical object family for discrete polygonal habitat units. Field-level schema shape, fixtures, validators, source registry activation, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A `HabitatPatch` is not a species occurrence, not a plant specimen/vegetation-community ownership record, not a regulatory critical-habitat designation, not a modeled suitability surface, not a connectivity edge, not a corridor, not a management instruction, and not release authority.

---

## Meaning

`HabitatPatch` represents a discrete habitat unit: a declared patch geometry, raster-derived polygon, inventory polygon, stewardship-bounded habitat area, or public-safe generalized habitat unit that KFM can cite, validate, review, publish, correct, and roll back.

It answers:

- What habitat unit is being referenced?
- Which source, source role, classification, geometry, time scope, and artifact digest support it?
- Which land-cover observation, ecological-system classification, vegetation context, hydrology/soil context, regulatory context, or model output informs the patch?
- Which exact geometry is internal/restricted, and which public-safe geometry may be released?
- Which EvidenceRefs, EvidenceBundles, validation reports, policy decisions, review records, release manifests, correction notices, and rollback targets govern consequential use?

A patch is the spatial carrier for Habitat reasoning. It may carry class, quality, suitability, connectivity, stewardship, and restoration context, but those concerns remain separate object families when they make distinct claims.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| HabitatPatch meaning | `contracts/domains/habitat/habitat-patch.contract.md` | Owned here for requested path; naming conflict noted below |
| Sibling scaffold | `contracts/domains/habitat/habitat_patch.md` | CONFIRMED scaffold; disposition NEEDS VERIFICATION |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/habitat_patch.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Habitat object-family doctrine | `docs/domains/habitat/README.md` | Names `HabitatPatch` as discrete polygonal habitat unit |
| Habitat-type grouping | `docs/domains/habitat/sublanes/biotopes.md` | Groups HabitatPatch, LandCoverObservation, EcologicalSystem as evidence-backed habitat-type objects |
| Land-cover support | `contracts/domains/habitat/land_cover/observation.md` | May support patch class/vintage/geometry; does not replace patch identity |
| Ecological-system support | `contracts/domains/habitat/ecological_system.md` | May classify patch ecological type; not the patch geometry itself |
| Identity support | `contracts/domains/habitat/domain_feature_identity.md` | Shared deterministic identity and anti-collapse rules |
| Observation support | `contracts/domains/habitat/domain_observation.md` | Shared observation envelope, if patch is observation-backed |
| Layer support | `contracts/domains/habitat/domain_layer_descriptor.md` | Public layer descriptor semantics; not patch truth |
| Validation support | `contracts/domains/habitat/domain_validation_report.md` | Validation findings; not proof/release authority |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Expected sensitivity/release gates; contents NEEDS VERIFICATION |
| Release | `release/` / `release/manifests/habitat/` | Expected release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Naming conflict

> [!WARNING]
> **CONFLICTED / NEEDS VERIFICATION:** this repository currently has two scaffold paths for the same likely concept:
>
> - `contracts/domains/habitat/habitat-patch.contract.md` — the path requested here.
> - `contracts/domains/habitat/habitat_patch.md` — the path referenced by `schemas/contracts/v1/domains/habitat/habitat_patch.schema.json`.
>
> This update preserves the requested `.contract.md` path and documents the conflict. A steward should decide whether to keep both, redirect one, supersede one, or migrate links/schema pointers through an ADR or migration note. No file was deleted or renamed.

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/habitat_patch.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Habitat Patch` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Contract doc pointer | `contracts/domains/habitat/habitat_patch.md` — not the requested `.contract.md` path |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added and the contract-doc pointer is reconciled, this file is semantic guidance and review vocabulary only.

---

## HabitatPatch vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `HabitatPatch` | Discrete habitat unit identity and patch geometry. | This contract. |
| `LandCoverObservation` | Land-cover class evidence over place/time. | May support patch class; not the patch itself. |
| `EcologicalSystem` | Ecological-system classification. | May classify patch type; not species presence. |
| `Habitat Quality Score` | Scalar/categorical quality assessment. | Describes patch quality under rules/model; not management instruction. |
| `SuitabilityModel` | Modeled suitability surface. | May score or inform patch; not patch identity. |
| `ConnectivityEdge` | Graph relation between patches. | Derived relation; not patch polygon. |
| `Corridor` | Linear or area corridor derived from connectivity. | Derived geometry; not the same as a patch unless explicitly modeled as such. |
| `Restoration Opportunity` | Candidate restoration site. | May overlap patch; not the same claim. |
| `StewardshipZone` | Administrative/stewardship context. | May constrain access/use; not habitat truth. |
| Fauna/Flora occurrence | Species occurrence truth. | HabitatPatch may join as context only under policy/geoprivacy. |
| Flora `Vegetation Community` | Plant-community object. | Flora-owned; Habitat may cite context only. |
| Regulatory critical habitat | Authority designation. | Distinct regulatory role; not generic patch type. |

---

## Assertions

A reviewed `HabitatPatch` should semantically assert:

1. **Patch identity** — stable patch ID, object role, source role, temporal scope, spatial scope, and digest basis.
2. **Geometry role** — exact internal geometry, public-safe generalized geometry, or aggregate-only scope is explicit.
3. **Source support** — SourceDescriptor refs, source record refs, rights, citation, source role, source vintage, and authority limits are visible.
4. **Classification support** — land-cover observation refs, ecological-system refs, class scheme refs, crosswalk refs, and uncertainty refs are linked where material.
5. **Temporal support** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
6. **Evidence support** — EvidenceRef/EvidenceBundle refs are present before consequential use.
7. **Policy support** — sensitivity, rights, source-role, geometry exposure, and release policy decisions are linked where material.
8. **Review support** — steward review and validation support are visible before promotion.
9. **Release support** — ReleaseManifest, public artifact refs, correction path, and rollback target are present before public use.
10. **Correction support** — supersession, replacement patch, stale-state, and rollback lineage are auditable.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating patch as species occurrence | Fauna/Flora own occurrence truth. |
| Treating patch as Flora vegetation community | Flora owns plant-community semantics. |
| Treating patch as regulatory critical habitat | Regulatory designation has distinct source role and authority burden. |
| Treating patch as suitability score | SuitabilityModel / Habitat Quality Score owns modeled scoring. |
| Treating patch as connectivity edge or corridor | Connectivity/corridor are derived graph/geometric objects. |
| Treating style-filtered geometry as redacted | Sensitive geometry must be transformed before public serving. |
| Treating candidate patch as public | Candidate material remains WORK/QUARANTINE or review-only. |
| Treating AI-drawn polygon as source truth | AI is interpretive and must be labeled/reviewed. |
| Treating schema scaffold as implemented validator | Current schema is only a scaffold. |
| Treating patch as management instruction | KFM is not an emergency, regulatory, or management authority. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM habitat patch ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest over patch-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `HabitatPatch`. |
| `patch_id` | Stable patch identifier. |
| `patch_kind` | observed, derived, modeled-support, regulatory-context, stewardship-context, aggregate, public-safe, or accepted enum. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_record_refs` | Source-native raster/vector/table/report/API refs. |
| `source_role` | observed, modeled/model, regulatory, aggregate, administrative, candidate, synthetic, derivative, context, or accepted enum. |
| `exact_geometry_ref` | Restricted/internal exact geometry, when retained. |
| `public_geometry_ref` | Public-safe generalized, aggregated, or redacted geometry. |
| `geometry_role` | exact-internal, public-generalized, aggregate-only, withheld, or accepted enum. |
| `geometry_fingerprint` | Hash/fingerprint for identity and correction. |
| `spatial_scope_ref` | County, HUC, ecoregion, grid, project, patch set, or other declared scope. |
| `land_cover_observation_refs` | LandCoverObservation evidence used to form/support patch. |
| `ecological_system_refs` | EcologicalSystem classification refs. |
| `vegetation_community_context_refs` | Flora-owned context refs, if admitted. |
| `soil_context_refs` | Soil-owned context refs, if admitted. |
| `hydrology_context_refs` | Hydrology-owned context refs, if admitted. |
| `occurrence_context_refs` | Fauna/Flora context refs, public-safe and policy-gated only. |
| `quality_score_refs` | Habitat Quality Score refs. |
| `suitability_model_refs` | SuitabilityModel refs that inform but do not define patch truth. |
| `connectivity_edge_refs` | Connectivity relations using this patch. |
| `corridor_refs` | Corridor relations using this patch. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/acquisition time where applicable. |
| `valid_time` | Valid interval for patch claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `uncertainty_refs` | UncertaintySurface or uncertainty summary refs. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind consequential use. |
| `validation_report_ref` | ValidationReport for schema, geometry, time, identity, evidence, sensitivity, and release readiness. |
| `policy_decision_ref` | PolicyDecision where material. |
| `redaction_receipt_refs` | Generalization/redaction/aggregation receipts for public-safe geometry. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement patch refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source, unresolved role, invalid geometry, sensitive exact exposure, rights unknown, stale source, missing evidence, release missing. |

---

## Patch sources

| Source / support family | Likely role | HabitatPatch handling |
|---|---|---|
| NLCD / land-cover observations | observed / context | May delineate or classify patch; source vintage and class scheme must remain visible. |
| GAP / LANDFIRE / NatureServe ecological systems | modeled / observed / aggregate / context depending SourceDescriptor | May classify patch type; does not assert occurrence truth. |
| NWI wetlands / hydrology context | observed / regulatory/context depending SourceDescriptor | May inform wetland/riparian patch context; Hydrology owns water truth. |
| Soil / SSURGO context | context | May inform substrate; Soil owns soil truth. |
| Fauna/Flora public-safe occurrence context | context | Used only through governed, geoprivacy-safe joins. |
| Regulatory critical habitat | regulatory | May overlap or contextualize patch; not the same object. |
| Suitability / model outputs | model / derivative | May score or derive candidate patch; requires model receipt and uncertainty. |
| Stewardship / administrative boundaries | administrative/context | May constrain access/release; not habitat truth by itself. |
| AI/synthetic patch proposal | synthetic/candidate | Never source truth; requires review, evidence, and validation. |

---

## Source-role rules

| Role | HabitatPatch handling | Failure mode |
|---|---|---|
| `observed` | Patch derives from direct observation/inventory/remote-sensing with source vintage and scheme. | Misclassification or stale source. |
| `modeled` / `model` | Patch is generated or scored by model under stated assumptions. | Modeled-as-observed or modeled-as-regulatory. |
| `regulatory` / `authority` | Patch overlaps or represents authority designation only when source supports it. | Regulatory-as-biological-truth. |
| `aggregate` | Patch is a public-safe summary or generalized unit. | Aggregate-as-exact. |
| `administrative` | Patch is stewardship/management context. | Administrative-as-title or instruction. |
| `candidate` | Unreviewed pipeline/watcher/model output. | Candidate-as-public. |
| `synthetic` | AI/simulated/reconstructed proposal. | Synthetic-as-observed. |
| `derivative` | Derived from observations, crosswalks, model outputs, or public-safe transforms. | Derived-as-primary source. |
| `context` | Consumed from another lane through governed join. | Habitat adopts neighboring-lane truth. |

---

## Geometry and sensitivity

Patch geometry is often the most policy-significant part of a HabitatPatch.

Rules:

- Exact internal patch geometry and public-safe patch geometry must be distinguishable.
- Public exact exposure fails closed when geometry would reveal sensitive species context, rare habitat, private stewardship context, protected resources, or occurrence-linked habitat.
- Public derivatives may require generalized geometry, aggregated grids, watershed/county/ecoregion rollups, delayed publication, or steward-only exact access.
- Redaction/generalization transforms need receipts with input class, output class, reason, policy, reviewer, residual risk, and rollback target.
- Public map/style filters are not a sensitivity control; sensitive geometry must be transformed before tile generation or public serving.
- A patch geometry used in public UI must carry stale/correction state and evidence/citation paths.

---

## Lifecycle

| Phase | HabitatPatch handling |
|---|---|
| RAW | Source geometry, source refs, source role, rights, sensitivity, citation, time, and hashes are captured but not public truth. |
| WORK / QUARANTINE | Candidate patch is normalized; invalid geometry, time collapse, unresolved source role, missing evidence, rights gaps, and sensitivity failures are held with reasons. |
| PROCESSED | Reviewed patch binds identity, source role, geometry role, spatial/temporal scope, artifact digests, evidence refs, validation report, policy posture, and correction state. |
| CATALOG / TRIPLET | Patch claims may be projected only with EvidenceBundle refs, source-role caveats, and public-safe geometry posture. |
| RELEASE CANDIDATE | Public patch layers/API payloads require policy/review, public-safe geometry, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe patch objects or derivatives appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source update, geometry correction, role correction, evidence correction, policy change, sensitivity review, or release withdrawal triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Decide whether `habitat-patch.contract.md` or `habitat_patch.md` is canonical; update schema `x-kfm.contract_doc` accordingly.
- [ ] Expand `schemas/contracts/v1/domains/habitat/habitat_patch.schema.json` beyond an empty scaffold.
- [ ] Confirm canonical source-role enum spelling, including `model` vs `modeled` and `authority` vs `regulatory`.
- [ ] Add valid fixtures for observed patch, land-cover-derived patch, ecological-system-classified patch, public-safe generalized patch, model-derived candidate patch, regulatory-context patch, and aggregate patch.
- [ ] Add invalid fixtures for missing source, missing evidence, invalid geometry, exact sensitive geometry released publicly, modeled-as-observed, modeled-as-regulatory, species-occurrence-as-patch-truth, vegetation-community-as-Habitat-owned, style-only redaction, candidate-as-public, missing release, and missing rollback target.
- [ ] Add validator checks for geometry validity, geometry role, source role, spatial/temporal scope, artifact digest, evidence refs, policy refs, redaction receipt refs, release refs, and correction lineage.
- [ ] Add tests proving public map/UI/AI surfaces cannot treat patch tiles, popups, graph projections, vector indexes, or generated text as source truth.
- [ ] Confirm release tests proving public clients consume released public-safe patch artifacts only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, geometry, role, scope, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe patch may support a claim |
| Evidence, role, geometry, rights, sensitivity, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, sensitive leak, candidate public path, style-only redaction, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Requested target scaffold | Confirms `habitat-patch.contract.md` existed as scaffold before replacement. | Does not prove contract maturity. |
| Sibling scaffold | Confirms `habitat_patch.md` also exists as scaffold. | Does not resolve canonical naming. |
| Paired schema scaffold | Confirms `habitat_patch.schema.json` path and schema/contract-doc pointer drift. | Does not prove field-level validation. |
| Habitat README | Confirms HabitatPatch as a canonical object family, lifecycle, sensitivity, source-role anti-collapse, map/UI, AI, and validation doctrine. | Some implementation paths remain PROPOSED / NEEDS VERIFICATION. |
| Biotopes sublane | Confirms HabitatPatch as Habitat-owned typed polygon/cell context in the habitat-type grouping. | `Biotope` remains a proposed docs grouping, not a new object family. |
| Model-vs-observation doc | Confirms role separation and anti-collapse behavior. | Role spelling and exact schema/policy enforcement remain NEEDS VERIFICATION. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized patch weakens geometry integrity, source-role separation, evidence support, sensitivity posture, or release integrity.

Rollback triggers include:

- exact or public geometry changes;
- source, source role, source vintage, class scheme, ecological-system classification, crosswalk, temporal scope, artifact digest, evidence ref, policy decision, or release ref changes;
- modeled or candidate patch was presented as observed or regulatory;
- patch was presented as species occurrence, Flora vegetation-community ownership, regulatory critical habitat, suitability score, corridor, or management instruction;
- sensitive exact patch or occurrence-linked habitat leaked publicly;
- style-only redaction was used instead of pre-publication transformation;
- candidate patch appeared in public API/UI/AI path;
- public map tile, popup, AI answer, graph projection, or vector index was treated as patch truth;
- release, correction, or rollback refs were missing for public use.

Rollback artifacts should include affected patch IDs, exact/public geometry refs, geometry fingerprints, source refs, source-role refs, temporal-scope refs, artifact digests, evidence refs, validation reports, policy decisions, redaction receipts, release refs, correction notices, rollback cards, replacement patches, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `habitat-patch.contract.md` or `habitat_patch.md` the canonical HabitatPatch contract path? | CONFLICTED / NEEDS VERIFICATION | Contract/schema steward review; ADR or migration note. |
| Which fields must be required in `habitat_patch.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which source-role spelling is canonical: `model` or `modeled`; `authority` or `regulatory`? | NEEDS VERIFICATION | Source-role/schema/policy review. |
| Which geometry roles are allowed for internal vs public patch geometry? | NEEDS VERIFICATION | Policy, redaction, and release review. |
| Which source families are activated first for HabitatPatch? | NEEDS VERIFICATION | Source activation decision and SourceDescriptor review. |
| How should public patch layers link to restricted exact geometry and redaction receipts? | NEEDS VERIFICATION | Geoprivacy, policy, release, and UI review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./habitat_patch.md`](./habitat_patch.md) — sibling scaffold; canonical disposition NEEDS VERIFICATION.
- [`./domain_observation.md`](./domain_observation.md) — domain observation envelope.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — deterministic identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — layer/view descriptor support.
- [`./domain_validation_report.md`](./domain_validation_report.md) — validation-report support.
- [`./ecological_system.md`](./ecological_system.md) — ecological-system classification contract.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation contract.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/sublanes/biotopes.md`](../../../docs/domains/habitat/sublanes/biotopes.md) — habitat-type / patch grouping.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/habitat_patch.schema.json`](../../../schemas/contracts/v1/domains/habitat/habitat_patch.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
