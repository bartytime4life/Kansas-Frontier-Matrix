<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-connectivity-edge
title: ConnectivityEdge Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Connectivity steward
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
policy_label: public-with-gates; semantic-contract; habitat; connectivity; ConnectivityEdge; derived-product; patch-graph; resistance-aware; evidence-bound; release-gated; sensitive-movement-deny-default
tags: [kfm, contracts, habitat, connectivity_edge, ConnectivityEdge, connectivity, patch-graph, least-cost, resistance, corridor, model-run-receipt, uncertainty-surface, habitat-patch, suitability-model, source-role, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
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
  - ../../../schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/connectivity_edge/
  - ../../../tests/domains/habitat/connectivity_edge/
  - ../../../pipelines/domains/habitat/
  - ../../../pipeline_specs/habitat/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a scaffold at contracts/domains/habitat/connectivity_edge.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json, but it is still a PROPOSED scaffold with empty properties and additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "ConnectivityEdge is a derived Habitat patch-graph edge. It is not an observed animal route, not a transport corridor, not a regulatory designation, not a HabitatPatch, not a Corridor geometry by itself, and not release authority."
  - "Connectivity products inherit the weakest source role, rights, sensitivity, vintage, evidence, uncertainty, and release posture of their inputs unless governed derivation, review, and public-safe transformation prove otherwise."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ConnectivityEdge — Habitat

> Semantic contract for `ConnectivityEdge`: the Habitat object that represents a derived graph edge between habitat patches or habitat units under declared connectivity assumptions, source support, model-run receipt, uncertainty, policy, release, correction, and rollback controls.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: ConnectivityEdge" src="https://img.shields.io/badge/object-ConnectivityEdge-blue">
  <img alt="Product: derived" src="https://img.shields.io/badge/product-derived-6f42c1">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: not movement route" src="https://img.shields.io/badge/boundary-not__movement__route-critical">
</p>

`contracts/domains/habitat/connectivity_edge.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [ConnectivityEdge vs nearby objects](#connectivityedge-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Edge classes](#edge-classes) · [Derivation rules](#derivation-rules) · [Source-role rules](#source-role-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/connectivity_edge.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold with empty `properties` and `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine names `ConnectivityEdge` as a canonical Habitat-owned object family and the connectivity sublane defines it as a derived product linking habitat areas. Field-level schema shape, fixtures, validators, model-run enforcement, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `ConnectivityEdge` is derived Habitat graph evidence. It is **not** observed animal movement, not a Fauna `MigrationRoute`, not a Roads/Rail/Trade transport corridor, not a regulatory designation, not a public layer, not a management instruction, and not release authority by itself.

---

## Meaning

`ConnectivityEdge` represents a modeled or derived linkage between two Habitat units, usually patches, habitat nodes, ecological-system units, or public-safe habitat aggregates.

It answers:

- Which two Habitat nodes are linked?
- Which suitability, resistance, land-cover, ecoregion, patch, uncertainty, or public-safe Fauna/Flora context supported the linkage?
- Which method produced the edge: least-cost, resistance/circuit, graph adjacency, corridor candidate, expert/steward review, or another governed method?
- Which model-run receipt, input EvidenceRefs, uncertainty support, policy decision, release manifest, correction notice, and rollback target govern downstream use?
- How should public surfaces label the edge so users do not read it as observed animal movement, a transport route, a regulatory corridor, or an emergency/management instruction?

A connectivity edge is an evidence-bounded relationship. It is useful for Habitat reasoning, but it must remain visibly **derived**.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| ConnectivityEdge meaning | `contracts/domains/habitat/connectivity_edge.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Connectivity doctrine | `docs/domains/habitat/sublanes/connectivity.md` | Defines ConnectivityEdge/Corridor sublane, derived posture, inputs, sensitivity, lifecycle, and tests |
| Parent Habitat contracts | `contracts/domains/habitat/README.md` | Contract-root orientation; not a substitute for this object contract |
| Suitability input | `contracts/domains/habitat/SuitabilityModel.md` | Modeled suitability/resistance input may support edge derivation |
| Land-cover input | `contracts/domains/habitat/land_cover/observation.md` | Observed/context input; does not become the edge truth |
| Run receipt | `contracts/domains/habitat/land_cover/model_run_receipt.md` or future Habitat-wide receipt contract | Required companion concept; exact cross-sublane home NEEDS VERIFICATION |
| Uncertainty | `contracts/domains/habitat/land_cover/uncertainty.md` or future Habitat-wide uncertainty contract | Required uncertainty support; exact cross-sublane home NEEDS VERIFICATION |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, cadence, activation |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Expected source-role/sensitivity/release gates; contents NEEDS VERIFICATION |
| Release | `release/` / `release/manifests/habitat/` | Expected release/correction/rollback authority; instances NEEDS VERIFICATION |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `Connectivity Edge` |
| Schema properties | Empty object |
| Required fields | None visible in the scaffold |
| Additional properties | `true` |
| Source doc | `docs/domains/habitat/MISSING_OR_PLANNED_FILES.md` |
| Field-level validation | NEEDS VERIFICATION |

Until schema fields are added, this contract is semantic guidance and review vocabulary only.

---

## ConnectivityEdge vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `ConnectivityEdge` | Graph edge or linkage relation between Habitat nodes. | This contract. |
| `Corridor` | Spatial corridor geometry or released corridor derivative. | Edge is relation; corridor is spatialization of linkage. |
| `HabitatPatch` | Patch/node geometry and habitat unit identity. | Edge references patches; it does not become the patch. |
| `SuitabilityModel` | Modeled suitability/resistance surface or score family. | Edge may consume it; edge is not suitability. |
| `ModelRunReceipt` | Run inputs, params, digests, time, method. | Required derivation support; not proof or release. |
| `UncertaintySurface` | Confidence and uncertainty support. | Edge must not claim more confidence than uncertainty supports. |
| Fauna `MigrationRoute` | Observed/curated animal movement route. | Habitat edge/corridor must not be presented as observed movement. |
| Roads/Rail/Trade corridor | Transport route/corridor. | Habitat corridor is ecological, not transport infrastructure. |
| `LayerManifest` | Public serving/rendering metadata. | Layer may show released edge; it is not edge truth. |

---

## Assertions

A reviewed `ConnectivityEdge` should semantically assert:

1. **Edge identity** — deterministic identity from source/support refs, node pair, edge role, method profile, temporal scope, and normalized digest.
2. **Node pair** — `from_node_ref` and `to_node_ref` identify Habitat patches, units, or public-safe aggregates.
3. **Directionality** — undirected, directed, asymmetric, seasonal, or conditional connectivity is explicit.
4. **Derivation method** — least-cost, resistance/circuit, graph adjacency, expert/steward rule, or model-specific method is recorded.
5. **Input support** — suitability/resistance surfaces, land cover, patch geometry, context layers, public-safe Fauna/Flora context, and source vintages are cited.
6. **Model-run support** — model-run receipt, config digest, input digest, output digest, and method parameters are linked.
7. **Uncertainty support** — edge uncertainty, confidence, sensitivity to input assumptions, and weakest-input support are visible.
8. **Source-role preservation** — observed, modeled, regulatory, context, aggregate, candidate, and synthetic roles do not collapse.
9. **Sensitivity posture** — sensitive occurrence, movement, den/nest/roost/hibernacula/spawning, or stewardship-sensitive detail is generalized, restricted, withheld, or denied before public exposure.
10. **Release support** — validation report, policy decision, review record, release manifest, correction path, and rollback target exist before public use.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating edge as observed animal movement | Fauna owns movement routes; Habitat edge is derived habitat structure. |
| Treating edge as transport corridor | Roads/Rail/Trade owns transport corridors and route graphs. |
| Treating edge as regulatory designation | Connectivity is derived/modelled unless an authority source separately says otherwise. |
| Treating edge as HabitatPatch | Patch/node identity remains separate. |
| Treating edge as Corridor geometry | Corridor spatialization is a separate object/derivative. |
| Treating resistance surface as edge | Resistance may support derivation; edge is relation output. |
| Treating model receipt as proof | Receipt records process; EvidenceBundle/proof support remains separate. |
| Dropping uncertainty | Overstates connectivity confidence. |
| Publishing precise sensitive linkage | Sensitive movement/corridor detail denies by default. |
| Letting AI infer exact movement paths | AI is interpretive and cannot reconstruct sensitive routes. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM connectivity edge ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized edge digest. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | `ConnectivityEdge`. |
| `edge_id` | Source/KFM edge identifier. |
| `edge_kind` | Least-cost, resistance, circuit, graph-adjacency, expert-rule, seasonal, candidate, public-derivative, or accepted enum. |
| `from_node_ref` | Source Habitat node/patch/aggregate ref. |
| `to_node_ref` | Target Habitat node/patch/aggregate ref. |
| `node_family` | HabitatPatch, ecoregion aggregate, restoration unit, public-safe grid, or accepted node family. |
| `directionality` | Undirected, directed, asymmetric, seasonal, conditional, unknown. |
| `edge_weight` | Cost, resistance, conductance, adjacency score, suitability-weighted score, or accepted metric. |
| `weight_units` | Units or dimensionless score. |
| `threshold_profile_ref` | Edge admission/visibility threshold profile, if used. |
| `method_profile_ref` | Derivation method, algorithm, expert rule, or model profile. |
| `resistance_surface_refs` | Resistance/cost/suitability surfaces used. |
| `suitability_model_refs` | SuitabilityModel refs used as input. |
| `habitat_patch_refs` | Input patch/node refs. |
| `land_cover_observation_refs` | LandCoverObservation refs used. |
| `context_refs` | Ecoregion, Soil, Hydrology, Roads/Rail/Trade, Hazards, or other governed context refs. |
| `public_safe_fauna_context_refs` | Public-safe Fauna movement/occurrence context refs, if used. |
| `model_run_receipt_ref` | Required derivation receipt. |
| `uncertainty_surface_refs` | Required uncertainty support. |
| `corridor_ref` | Corridor geometry/derivative ref if spatialized. |
| `geometry_ref_internal` | Access-controlled geometry, if any. |
| `public_geometry_ref` | Public-safe generalized/aggregate edge or corridor geometry, if released. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_role_summary` | Source roles preserved across inputs and output. |
| `source_time` | Source publication/assertion time for inputs. |
| `observed_time` | Observation/acquisition time for observed inputs, if applicable. |
| `valid_time` | Time/season/condition interval for edge claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `run_time` | Connectivity derivation run time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind the edge claim. |
| `validation_report_ref` | ValidationReport for schema, derivation, evidence, sensitivity, and release readiness. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `redaction_receipt_ref` | Required if sensitive geometry/detail is generalized or redacted. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement edge refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing receipt, missing uncertainty, unresolved input role, sensitive-input taint, method gap, stale input, overconfident edge, release missing. |

---

## Edge classes

| Class | Meaning | Default posture |
|---|---|---|
| `least_cost_edge` | Edge produced from least-cost path or cost-distance assumptions. | Derived; method and inputs required. |
| `resistance_edge` | Edge derived from resistance/conductance/circuit-style analysis. | Derived; uncertainty required. |
| `graph_adjacency_edge` | Edge from patch adjacency/proximity/network topology. | Derived/contextual; not movement proof. |
| `suitability_weighted_edge` | Edge weighted by suitability or habitat quality surface. | Modeled input stays modeled. |
| `seasonal_or_conditional_edge` | Edge valid under declared season/condition/scenario. | Valid-time/condition required. |
| `barrier_adjusted_edge` | Edge adjusted by Roads/Rail/Trade, land cover, hazards, or other context barriers. | Owning-lane truth preserved. |
| `sensitive_join_edge` | Edge influenced by sensitive occurrence/movement/stewardship context. | Deny-by-default until public-safe transform exists. |
| `candidate_edge` | Unreviewed derivation output. | WORK/QUARANTINE; no public edge. |
| `public_derivative_edge` | Released public-safe generalized edge summary. | Requires release manifest and rollback target. |

---

## Derivation rules

- `ConnectivityEdge` is derived, not observed.
- Every edge must link a model/run receipt and preserve input refs unless a later ADR defines a different proof pattern.
- Every edge must carry uncertainty support or abstain from public use.
- Edge confidence must not exceed the weakest relevant input support.
- Resistance/cost assumptions are part of edge identity; changing them creates a new edge version or correction lineage.
- Input source vintages and temporal scope must stay distinct from run time and release time.
- Sensitive-input taint follows the edge until a governed public-safe derivative is produced.
- Watcher recompute output is a candidate, not publication.

---

## Source-role rules

| Source pattern | Required handling |
|---|---|
| HabitatPatch input | Patch geometry/classification stays Habitat-owned input; public-safe geometry required. |
| SuitabilityModel input | Modeled role stays visible; edge does not become observed or regulatory. |
| LandCoverObservation input | Observation/context role preserved; crosswalks remain explicit. |
| Soil/Hydrology context | Owning-lane source truth preserved; Habitat consumes context only. |
| Roads/Rail/Trade barrier context | Transport corridor remains RRT-owned; Habitat may use as resistance/barrier context. |
| Hazards/disturbance context | Context only; KFM is not alert/management authority. |
| Fauna movement/occurrence context | Public-safe only; Fauna owns movement/occurrence truth. |
| Sensitive or restricted input | Derived edge fails closed until redaction/generalization/review/release support exists. |
| AI-proposed edge | Synthetic/candidate only; cannot become evidence or release. |

---

## Sensitivity and release

Connectivity is high-risk when it can reveal sensitive movement, nesting, denning, roosting, hibernacula, spawning, rare-species, private stewardship, or protected-resource context.

Rules:

- Public exact connectivity exposure denies by default if it can expose sensitive movement or occurrence context.
- A single sensitive input taints the whole edge until generalized, redacted, aggregated, delayed, restricted, or denied.
- Public derivatives require RedactionReceipt or equivalent transform receipt where geometry/detail is generalized.
- Public maps must label derived status, uncertainty, source roles, stale/correction state, and public-safe geometry posture.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate edge records.
- AI must not infer precise movement paths or claim management/emergency instruction from a derived edge.

---

## Lifecycle

| Phase | ConnectivityEdge handling |
|---|---|
| RAW | Input objects are referenced by identity/hash; no raw connectivity edge is public truth. |
| WORK / QUARANTINE | Derivation runs produce candidate edges, receipts, uncertainty, method assumptions, and quarantine reasons for unresolved inputs/sensitivity. |
| PROCESSED | Reviewed edges bind node pair, method, input refs, receipt, uncertainty, evidence refs, validation report, policy posture, and correction state. |
| CATALOG / TRIPLET | Edge claims may be projected only with EvidenceBundle refs, source-role caveats, temporal scope, and sensitivity posture. |
| RELEASE CANDIDATE | Public edge/layer/API payloads require validation, policy/review, public-safe geometry, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe connectivity artifacts appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Input update, method change, resistance assumption change, uncertainty update, sensitive review, or geometry correction triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json` beyond empty scaffold.
- [ ] Confirm whether `ConnectivityEdge` schema requires `from_node_ref`, `to_node_ref`, `method_profile_ref`, `model_run_receipt_ref`, and `uncertainty_surface_refs`.
- [ ] Add valid fixtures for least-cost, resistance, graph-adjacency, suitability-weighted, barrier-adjusted, candidate, sensitive-denied, and public-derivative edges.
- [ ] Add invalid fixtures for missing node refs, missing receipt, missing uncertainty, unresolved input role, sensitive input without redaction, corridor-as-Fauna-route, transport-corridor collapse, edge-as-regulatory, missing EvidenceBundle, and missing rollback target.
- [ ] Add tests proving derived-as-observed and derived-as-regulatory claims are denied.
- [ ] Add sensitivity tests proving exact sensitive movement/corridor detail fails closed.
- [ ] Add release tests proving public clients consume released public-safe derivatives only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Node pair, method, inputs, receipt, uncertainty, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe connectivity explanation may proceed |
| Evidence, role, method, receipt, uncertainty, sensitivity, or release support is missing | `ABSTAIN` / `HOLD` |
| Edge is framed as observed movement, regulatory designation, transport corridor, management instruction, or exact sensitive linkage | `DENY` |
| Schema, validator, source read, model run, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current target scaffold | Confirms target existed as scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current empty schema posture. | Does not prove field-level validation. |
| Habitat README | Confirms `ConnectivityEdge` is a Habitat canonical object family and temporal handling stays distinct. | Field realization remains PROPOSED. |
| Connectivity sublane doc | Defines derived posture, input constraints, source-role preservation, sensitive-deny behavior, lifecycle, tests, and AI behavior for connectivity. | Sublane file itself marks some placement and implementation claims PROPOSED. |
| Suitability / land-cover / uncertainty contracts | Adjacent semantic support for common inputs and companions. | Recent contract content is semantic documentation, not schema enforcement. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `ConnectivityEdge` weakens derived-status integrity, hides method assumptions, leaks sensitive movement detail, or makes a modeled linkage appear observed, regulatory, or authoritative beyond its evidence.

Rollback triggers include:

- input node, patch, suitability surface, resistance layer, source vintage, or method profile is corrected;
- model-run receipt, uncertainty support, evidence support, policy decision, release manifest, or rollback target is missing or invalid;
- sensitive input taint was missed;
- edge was shown as observed animal `MigrationRoute` or transport corridor;
- edge was treated as regulatory, management, emergency, or access instruction;
- public layer dropped derived/uncertainty badges;
- AI inferred precise movement path or sensitive location from the edge;
- public API/UI/AI used RAW/WORK/QUARANTINE/candidate edge records as public truth.

Rollback artifacts should include affected edge IDs, node refs, method refs, source/input refs, model-run receipt refs, uncertainty refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement edges, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `connectivity_edge.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which connectivity methods are admitted first: least-cost, circuit/resistance, graph adjacency, or another method? | NEEDS VERIFICATION | Habitat steward + model/validator review. |
| Should `ConnectivityEdge` and `Corridor` share a contract family or remain separate files? | NEEDS VERIFICATION | Contract/schema placement review. |
| Where should Habitat-wide `ModelRunReceipt` and `UncertaintySurface` contracts live outside land-cover-specific paths? | NEEDS VERIFICATION | Habitat object-family placement review. |
| Which sensitive-input taint rules are implemented in policy/tests? | NEEDS VERIFICATION | Policy root and fixture inspection. |
| How should public maps badge derived connectivity versus observed movement and transport corridors? | NEEDS VERIFICATION | Map/UI contract and release fixture review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — modeled suitability input contract.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation inputs.
- [`./land_cover/model_run_receipt.md`](./land_cover/model_run_receipt.md) — model/run receipt semantics.
- [`./land_cover/uncertainty.md`](./land_cover/uncertainty.md) — uncertainty support semantics.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/sublanes/connectivity.md`](../../../docs/domains/habitat/sublanes/connectivity.md) — connectivity sublane doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json`](../../../schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
