<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-corridor
title: Corridor Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Connectivity steward
  - OWNER_TBD — Corridor steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Sensitivity reviewer
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; habitat; corridor; Corridor; derived-product; connectivity-spatialization; public-safe-geometry; evidence-bound; release-gated; sensitive-movement-deny-default
tags: [kfm, contracts, habitat, corridor, Corridor, connectivity, connectivity-edge, derived-product, corridor-geometry, least-cost, resistance, public-safe-geometry, geoprivacy, redaction-receipt, model-run-receipt, uncertainty-surface, source-role, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./connectivity_edge.md
  - ./SuitabilityModel.md
  - ./suitability_model.md
  - ./land_cover/observation.md
  - ./land_cover/model_run_receipt.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/sublanes/connectivity.md
  - ../../../docs/domains/habitat/sublanes/suitability.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../schemas/contracts/v1/domains/habitat/corridor.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/corridor/
  - ../../../tests/domains/habitat/corridor/
  - ../../../pipelines/domains/habitat/
  - ../../../pipeline_specs/habitat/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a scaffold at contracts/domains/habitat/corridor.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/corridor.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "Corridor is a derived Habitat spatialization of connectivity. It is not an observed animal MigrationRoute, not a transport corridor, not a regulatory designation, not a management instruction, not a ConnectivityEdge relation by itself, and not release authority."
  - "Public corridor geometry is sensitive by default when derived from sensitive movement, occurrence, den/nest/roost/hibernacula/spawning, stewardship, or protected-resource context. Public release requires governed generalization/redaction, evidence, policy, review, release, correction, and rollback support."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Corridor — Habitat

> Semantic contract for `Corridor`: the Habitat object that spatializes a derived connectivity relationship into a line, polygon, swath, least-cost path, resistance corridor, or public-safe generalized corridor under explicit source support, model-run receipt, uncertainty, sensitivity, release, correction, and rollback controls.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: Corridor" src="https://img.shields.io/badge/object-Corridor-blue">
  <img alt="Product: derived" src="https://img.shields.io/badge/product-derived-6f42c1">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: not observed route" src="https://img.shields.io/badge/boundary-not__observed__route-critical">
</p>

`contracts/domains/habitat/corridor.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Corridor vs nearby objects](#corridor-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Corridor classes](#corridor-classes) · [Geometry and derivation rules](#geometry-and-derivation-rules) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/corridor.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/corridor.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine names `Corridor` as a canonical Habitat-owned object family and the connectivity sublane defines it as a derived spatial product related to `ConnectivityEdge`. Field-level schema shape, fixtures, validators, geoprivacy enforcement, model-run enforcement, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `Corridor` is derived Habitat geometry. It is **not** an observed animal route, not a Fauna `MigrationRoute`, not a Roads/Rail/Trade transport corridor, not a regulatory designation, not a management instruction, and not a public layer or release manifest by itself.

---

## Meaning

`Corridor` represents a derived spatial expression of Habitat connectivity. It may be a line, polygon, raster-derived swath, least-cost path, resistance corridor, generalized public corridor, or candidate corridor produced from patch, suitability, land-cover, resistance, uncertainty, and context inputs.

It answers:

- Which `ConnectivityEdge`, patch pair, habitat nodes, or connectivity run does this corridor spatialize?
- Which model/run, resistance assumptions, suitability surfaces, land-cover observations, context layers, and source vintages produced it?
- Which internal geometry is restricted, generalized, withheld, or public-safe?
- Which uncertainty, model-run receipt, EvidenceBundle, policy decision, review record, release manifest, correction notice, and rollback target govern its use?
- How should maps, APIs, Focus Mode, reports, and AI label the corridor so users do not read it as observed movement, transport infrastructure, regulatory designation, or emergency/management instruction?

A corridor is useful only when its derivation and uncertainty stay attached. A corridor with detached provenance is a risk surface, not a reliable Habitat object.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Corridor meaning | `contracts/domains/habitat/corridor.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/corridor.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Connectivity relation | `contracts/domains/habitat/connectivity_edge.md` | Corridor may spatialize one or more edges; it is not the edge relation itself |
| Connectivity doctrine | `docs/domains/habitat/sublanes/connectivity.md` | Defines ConnectivityEdge/Corridor scope, derived posture, inputs, sensitivity, lifecycle, and proposed tests |
| Parent Habitat contracts | `contracts/domains/habitat/README.md` | Contract-root orientation; not a substitute for this object contract |
| Suitability input | `contracts/domains/habitat/SuitabilityModel.md` | Modeled suitability/resistance input may support corridor derivation |
| Land-cover input | `contracts/domains/habitat/land_cover/observation.md` | Observed/context input; does not become corridor truth |
| Run receipt | `contracts/domains/habitat/land_cover/model_run_receipt.md` or future Habitat-wide receipt contract | Required companion concept; exact cross-sublane home NEEDS VERIFICATION |
| Uncertainty | `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide uncertainty contract | Required uncertainty support; exact cross-sublane home NEEDS VERIFICATION |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Expected sensitivity/release gates; contents NEEDS VERIFICATION |
| Release | `release/` / `release/manifests/habitat/` | Expected release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/corridor.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Corridor` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## Corridor vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `Corridor` | Spatial expression of modeled Habitat connectivity. | This contract. |
| `ConnectivityEdge` | Graph edge or linkage relation between Habitat nodes. | Edge is relation; corridor is spatialized derivative. |
| `HabitatPatch` | Patch/node geometry and habitat unit identity. | Corridor may connect patches; it does not become the patch. |
| `SuitabilityModel` | Modeled suitability/resistance surface or score family. | Corridor may consume it; corridor is not suitability. |
| `ModelRunReceipt` | Run inputs, params, digests, time, method. | Required derivation support; not proof or release. |
| `UncertaintySurface` | Confidence, footprint, and uncertainty support. | Corridor must carry uncertainty. |
| Fauna `MigrationRoute` | Observed/curated animal movement route. | Habitat corridor must not be presented as observed movement. |
| Roads/Rail/Trade corridor | Transport route/corridor. | Habitat corridor is ecological, not transport infrastructure. |
| `LayerManifest` | Public serving/rendering metadata. | Layer may show released corridor; it is not corridor truth. |

---

## Assertions

A reviewed `Corridor` should semantically assert:

1. **Corridor identity** — deterministic identity from source/support refs, corridor role, geometry fingerprint, method profile, temporal scope, and normalized digest.
2. **Connectivity linkage** — source `ConnectivityEdge` refs, patch-pair refs, or node/edge group refs that the corridor spatializes.
3. **Geometry posture** — internal geometry, public-safe generalized geometry, withheld geometry, or aggregate-only geometry state.
4. **Derivation method** — least-cost, resistance/circuit, graph-to-geometry, expert/steward rule, model-specific method, or scenario method.
5. **Input support** — suitability/resistance surfaces, land cover, patch geometry, context layers, public-safe Fauna/Flora context, and source vintages are cited.
6. **Model-run support** — model-run receipt, config digest, input digest, output digest, method parameters, CRS/resolution, and run time are linked.
7. **Uncertainty support** — corridor uncertainty, confidence, geometry generalization caveats, and weakest-input support are visible.
8. **Source-role preservation** — observed, modeled, regulatory, context, aggregate, candidate, and synthetic roles do not collapse.
9. **Sensitivity posture** — sensitive occurrence, movement, den/nest/roost/hibernacula/spawning, or stewardship-sensitive detail is generalized, restricted, withheld, or denied before public exposure.
10. **Release support** — validation report, policy decision, review record, release manifest, correction path, and rollback target exist before public use.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating corridor as observed animal movement | Fauna owns observed/curated movement routes. |
| Treating corridor as transport corridor | Roads/Rail/Trade owns transport corridors and route graphs. |
| Treating corridor as regulatory designation | Habitat corridor is derived unless an admitted authority source separately says otherwise. |
| Treating corridor as emergency or management instruction | KFM is not an alert, command, or land-management authority. |
| Treating corridor as `ConnectivityEdge` relation | Corridor is spatialized geometry; edge is graph relation. |
| Treating exact internal geometry as public-safe | Public release requires governed generalization/redaction/review. |
| Treating model receipt as proof | Receipt records process; EvidenceBundle/proof support remains separate. |
| Dropping uncertainty | Overstates connectivity confidence. |
| Letting AI infer precise movement paths | AI is interpretive and cannot reconstruct sensitive routes. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM corridor ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized corridor digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `Corridor`. |
| `corridor_id` | Source/KFM corridor identifier. |
| `corridor_kind` | Least-cost path, resistance corridor, circuit corridor, graph-spatialization, expert-rule corridor, seasonal/conditional, candidate, public derivative, or accepted enum. |
| `connectivity_edge_refs` | ConnectivityEdge refs the corridor spatializes. |
| `node_refs` | HabitatPatch, aggregate, or habitat-unit refs connected by the corridor. |
| `directionality` | Undirected, directed, asymmetric, seasonal, conditional, unknown. |
| `geometry_role` | internal-exact, public-generalized, aggregate-only, withheld, denied, or accepted enum. |
| `geometry_ref_internal` | Access-controlled exact/working geometry, if retained. |
| `public_geometry_ref` | Released public-safe generalized/aggregate geometry. |
| `geometry_fingerprint` | Digest/fingerprint for corridor geometry. |
| `generalization_method_ref` | Method/receipt for public-safe geometry transformation. |
| `redaction_receipt_ref` | Required when sensitive detail is generalized/redacted. |
| `method_profile_ref` | Derivation method, algorithm, expert rule, or model profile. |
| `resistance_surface_refs` | Resistance/cost/suitability surfaces used. |
| `suitability_model_refs` | SuitabilityModel refs used as input. |
| `habitat_patch_refs` | Input patch/node refs. |
| `land_cover_observation_refs` | LandCoverObservation refs used. |
| `context_refs` | Ecoregion, Soil, Hydrology, Roads/Rail/Trade, Hazards, or other governed context refs. |
| `public_safe_fauna_context_refs` | Public-safe Fauna movement/occurrence context refs, if used. |
| `model_run_receipt_ref` | Required derivation receipt. |
| `uncertainty_surface_refs` | Required uncertainty support. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_role_summary` | Source roles preserved across inputs and output. |
| `source_time` | Source publication/assertion time for inputs. |
| `observed_time` | Observation/acquisition time for observed inputs, if applicable. |
| `valid_time` | Time/season/condition interval for corridor claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `run_time` | Corridor derivation run time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the corridor claim. |
| `validation_report_ref` | ValidationReport for schema, derivation, geometry, evidence, sensitivity, and release readiness. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement corridor refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing edge, missing receipt, missing uncertainty, unresolved input role, sensitive geometry, method gap, stale input, overconfident corridor, release missing. |

---

## Corridor classes

| Class | Meaning | Default posture |
|---|---|---|
| `least_cost_corridor` | Spatial corridor from least-cost path/cost-distance assumptions. | Derived; method and inputs required. |
| `resistance_corridor` | Corridor from resistance/conductance/circuit-style analysis. | Derived; uncertainty required. |
| `graph_spatialization` | Spatialization of one or more `ConnectivityEdge` records. | Derived relation-to-geometry product. |
| `suitability_weighted_corridor` | Corridor weighted by suitability or habitat quality surface. | Modeled input stays modeled. |
| `seasonal_or_conditional_corridor` | Corridor valid under declared season/condition/scenario. | Valid-time/condition required. |
| `barrier_adjusted_corridor` | Corridor adjusted by roads, land cover, hazards, or other context barriers. | Owning-lane truth preserved. |
| `sensitive_join_corridor` | Corridor influenced by sensitive occurrence/movement/stewardship context. | Deny-by-default until public-safe transform exists. |
| `candidate_corridor` | Unreviewed derivation output. | WORK/QUARANTINE; no public edge. |
| `public_derivative_corridor` | Released public-safe generalized corridor. | Requires release manifest and rollback target. |

---

## Geometry and derivation rules

- `Corridor` is derived, not observed.
- Corridor geometry must carry a geometry role: internal exact, public generalized, aggregate-only, withheld, or denied.
- Public geometry must be generalized/redacted before release when sensitive detail is possible.
- Every corridor must link a model/run receipt and preserve input refs unless a later ADR defines a different proof pattern.
- Every corridor must carry uncertainty support or abstain from public use.
- Corridor confidence must not exceed the weakest relevant input support.
- Resistance/cost assumptions and generalization parameters are part of corridor identity; changing them creates a new version or correction lineage.
- Input source vintages and temporal scope must stay distinct from run time and release time.
- Watcher recompute output is a candidate, not publication.

---

## Source-role rules

| Source pattern | Required handling |
|---|---|
| `ConnectivityEdge` input | Edge relation remains separate; corridor spatializes it. |
| HabitatPatch input | Patch geometry/classification stays Habitat-owned input; public-safe geometry required. |
| SuitabilityModel input | Modeled role stays visible; corridor does not become observed or regulatory. |
| LandCoverObservation input | Observation/context role preserved; crosswalks remain explicit. |
| Soil/Hydrology context | Owning-lane source truth preserved; Habitat consumes context only. |
| Roads/Rail/Trade barrier context | Transport corridor remains RRT-owned; Habitat may use as resistance/barrier context. |
| Hazards/disturbance context | Context only; KFM is not alert/management authority. |
| Fauna movement/occurrence context | Public-safe only; Fauna owns movement/occurrence truth. |
| Sensitive or restricted input | Derived corridor fails closed until redaction/generalization/review/release support exists. |
| AI-proposed corridor | Synthetic/candidate only; cannot become evidence or release. |

---

## Sensitivity and release

Corridors are sensitive by default when they might reveal movement paths, habitat linkage routes, dens, nests, roosts, hibernacula, spawning areas, rare species, private stewardship zones, protected resources, or exact conservation opportunity geography.

Rules:

- Public exact corridor geometry denies by default when it can expose sensitive movement or occurrence context.
- A single sensitive input taints the whole corridor until generalized, redacted, aggregated, delayed, restricted, or denied.
- Public derivatives require RedactionReceipt or equivalent transform receipt where geometry/detail is generalized.
- Public maps must label derived status, uncertainty, source roles, stale/correction state, and public-safe geometry posture.
- Style filters are not sensitivity controls.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate corridor records.
- AI must not infer precise movement paths or claim management/emergency instruction from a derived corridor.

---

## Lifecycle

| Phase | Corridor handling |
|---|---|
| RAW | Input objects are referenced by identity/hash; no raw corridor is public truth. |
| WORK / QUARANTINE | Derivation runs produce candidate corridors, receipts, uncertainty, geometry fingerprints, method assumptions, and quarantine reasons for unresolved inputs/sensitivity. |
| PROCESSED | Reviewed corridors bind connectivity refs, geometry role, method, input refs, receipt, uncertainty, evidence refs, validation report, policy posture, and correction state. |
| CATALOG / TRIPLET | Corridor claims may be projected only with EvidenceBundle refs, source-role caveats, temporal scope, geometry role, and sensitivity posture. |
| RELEASE CANDIDATE | Public corridor/layer/API payloads require validation, policy/review, public-safe geometry, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe corridor artifacts appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Input update, method change, resistance assumption change, uncertainty update, sensitive review, or geometry/generalization correction triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/corridor.schema.json` beyond empty scaffold.
- [ ] Confirm whether `Corridor` schema requires `connectivity_edge_refs`, `geometry_role`, `geometry_fingerprint`, `model_run_receipt_ref`, `uncertainty_surface_refs`, and `redaction_receipt_ref` where sensitive.
- [ ] Add valid fixtures for least-cost, resistance, graph-spatialized, suitability-weighted, barrier-adjusted, candidate, sensitive-denied, public-generalized, and superseded corridors.
- [ ] Add invalid fixtures for missing connectivity refs, missing receipt, missing uncertainty, exact sensitive geometry public, unresolved input role, corridor-as-Fauna-route, transport-corridor collapse, corridor-as-regulatory, missing EvidenceBundle, and missing rollback target.
- [ ] Add tests proving derived-as-observed and derived-as-regulatory claims are denied.
- [ ] Add sensitivity tests proving exact sensitive movement/corridor detail fails closed.
- [ ] Add release tests proving public clients consume released public-safe derivatives only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Connectivity refs, geometry role, method, inputs, receipt, uncertainty, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe corridor explanation may proceed |
| Evidence, role, method, receipt, uncertainty, geometry posture, sensitivity, or release support is missing | `ABSTAIN` / `HOLD` |
| Corridor is framed as observed movement, regulatory designation, transport corridor, management instruction, or exact sensitive linkage | `DENY` |
| Schema, validator, source read, model run, geometry transform, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current target scaffold | Confirms target existed as scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat README | Confirms `Corridor` is a Habitat canonical object family and temporal handling stays distinct. | Field realization remains PROPOSED. |
| Connectivity sublane doc | Defines `ConnectivityEdge` / `Corridor` derived posture, input constraints, source-role preservation, sensitive-deny behavior, lifecycle, tests, and AI behavior. | Sublane file itself marks some placement and implementation claims PROPOSED. |
| ConnectivityEdge contract | Adjacent semantic contract for graph-edge relation that corridors may spatialize. | Recent contract content is semantic documentation, not schema enforcement. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `Corridor` weakens derived-status integrity, hides method or geometry assumptions, leaks sensitive movement detail, or makes a modeled corridor appear observed, regulatory, transport-related, or authoritative beyond its evidence.

Rollback triggers include:

- connectivity edge, patch, suitability surface, resistance layer, source vintage, method profile, or geometry transform is corrected;
- model-run receipt, uncertainty support, evidence support, policy decision, release manifest, or rollback target is missing or invalid;
- exact or over-precise sensitive geometry was published;
- sensitive input taint was missed;
- corridor was shown as observed animal `MigrationRoute` or transport corridor;
- corridor was treated as regulatory, management, emergency, or access instruction;
- public layer dropped derived/uncertainty/public-safe-geometry badges;
- AI inferred precise movement path or sensitive location from the corridor;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate corridor records as public truth.

Rollback artifacts should include affected corridor IDs, connectivity edge refs, node refs, geometry refs/fingerprints, method refs, source/input refs, model-run receipt refs, uncertainty refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement corridors, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `corridor.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which corridor methods are admitted first: least-cost, circuit/resistance, graph spatialization, or another method? | NEEDS VERIFICATION | Habitat steward + model/validator review. |
| Should `ConnectivityEdge` and `Corridor` share one contract family or remain separate files? | NEEDS VERIFICATION | Contract/schema placement review. |
| Where should Habitat-wide `ModelRunReceipt` and `UncertaintySurface` contracts live outside land-cover-specific paths? | NEEDS VERIFICATION | Habitat object-family placement review. |
| Which public corridor geometry generalization rules are implemented in policy/tests? | NEEDS VERIFICATION | Policy root and fixture inspection. |
| How should public maps badge derived corridor versus observed movement and transport corridors? | NEEDS VERIFICATION | Map/UI contract and release fixture review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./connectivity_edge.md`](./connectivity_edge.md) — graph-edge connectivity relation.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — modeled suitability input contract.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation inputs.
- [`./land_cover/model_run_receipt.md`](./land_cover/model_run_receipt.md) — model/run receipt semantics.
- [`./land_cover/uncertainty.md`](./land_cover/uncertainty.md) — uncertainty support semantics.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/sublanes/connectivity.md`](../../../docs/domains/habitat/sublanes/connectivity.md) — connectivity sublane doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/corridor.schema.json`](../../../schemas/contracts/v1/domains/habitat/corridor.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
