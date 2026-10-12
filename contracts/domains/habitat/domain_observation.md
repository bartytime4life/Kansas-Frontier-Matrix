<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-habitat-domain-observation
title: Domain Observation Contract — Habitat
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Observation steward
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
policy_label: public-with-gates; semantic-contract; habitat; observation; source-role-aware; temporal-scope-aware; evidence-bound; release-gated; anti-collapse
tags: [kfm, contracts, habitat, domain_observation, DomainObservation, observation, observed, modeled, regulatory, aggregate, candidate, synthetic, source-role, temporal-scope, evidence, policy, sensitivity, release, correction, rollback]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./domain_layer_descriptor.md
  - ./SuitabilityModel.md
  - ./connectivity_edge.md
  - ./corridor.md
  - ./land_cover/observation.md
  - ./land_cover/uncertainty.md
  - ../../../docs/domains/habitat/README.md
  - ../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/sublanes/land_cover.md
  - ../../../schemas/contracts/v1/domains/habitat/domain_observation.schema.json
  - ../../../policy/domains/habitat/
  - ../../../policy/sensitivity/habitat/
  - ../../../fixtures/domains/habitat/domain_observation/
  - ../../../tests/domains/habitat/domain_observation/
  - ../../../data/registry/sources/habitat/
  - ../../../release/manifests/habitat/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/habitat/domain_observation.md."
  - "The paired schema exists at schemas/contracts/v1/domains/habitat/domain_observation.schema.json, but it is still a PROPOSED scaffold that only defines spec_hash, id, and version, requires id, and allows additionalProperties=true; field-level enforcement remains NEEDS VERIFICATION."
  - "DomainObservation is a Habitat-wide observation envelope/support contract. It does not replace specific object-family contracts such as LandCoverObservation, HabitatPatch, EcologicalSystem, SuitabilityModel, ConnectivityEdge, Corridor, or UncertaintySurface."
  - "Role spelling drift remains NEEDS VERIFICATION: docs/domains/habitat/README.md uses modeled, while MODEL_VS_OBSERVATION.md uses model. This contract uses modeled as the lane-facing spelling and treats model as an alias pending schema/policy review."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Observation — Habitat

> Semantic contract for Habitat `DomainObservation`: the domain-wide observation envelope that preserves source role, object family, temporal scope, evidence linkage, policy posture, sensitivity, release state, correction lineage, and anti-collapse rules for Habitat observations and observation-backed objects.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Object: DomainObservation" src="https://img.shields.io/badge/object-DomainObservation-blue">
  <img alt="Role: source-role aware" src="https://img.shields.io/badge/role-source--role--aware-6f42c1">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Boundary: observation not release" src="https://img.shields.io/badge/boundary-observation__not__release-critical">
</p>

`contracts/domains/habitat/domain_observation.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Observation vs nearby objects](#observation-vs-nearby-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Observation classes](#observation-classes) · [Source-role rules](#source-role-rules) · [Temporal rules](#temporal-rules) · [Sensitivity and release](#sensitivity-and-release) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/habitat/domain_observation.md`  
> **Schema path:** `schemas/contracts/v1/domains/habitat/domain_observation.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` scaffold that defines only `spec_hash`, `id`, and `version`, requires only `id`, and allows `additionalProperties: true`.  
> **Truth posture:** Habitat doctrine defines the lane as landscape-focused and source-role-bound: observed, modeled, regulatory, aggregate, administrative, candidate, and synthetic roles are not interchangeable. Field-level schema shape, fixtures, validators, source registries, policy runtime, release artifacts, map/UI behavior, Focus Mode behavior, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `DomainObservation` is not a generic proof object, not a release decision, and not an excuse to flatten Habitat object families. It is an observation-support envelope that keeps source role, evidence, time, sensitivity, and correction visible before any Habitat observation is used downstream.

---

## Meaning

`DomainObservation` records the shared observation semantics for Habitat objects that are grounded in a source observation, inventory, regulatory source record, admitted context source, or reviewed observation-derived artifact.

It answers:

- What kind of source claim is this: observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, derivative, or context?
- Which Habitat object family is being observed or observation-backed?
- Which source, source descriptor, source role, source vintage, rights, sensitivity, and citation support it?
- Which temporal scope is material: source, observed, valid, retrieval, release, and correction time?
- Which EvidenceRefs, EvidenceBundles, policy decisions, validation reports, review records, release refs, correction notices, and rollback targets govern consequential use?

A domain observation is evidence-bearing context. It can support HabitatPatch, LandCoverObservation, EcologicalSystem, quality, suitability, connectivity, corridor, restoration, or stewardship reasoning, but it does not become those objects by itself.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Habitat observation semantics | `contracts/domains/habitat/domain_observation.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/habitat/domain_observation.schema.json` | CONFIRMED scaffold; field shape not enforced |
| Habitat domain doctrine | `docs/domains/habitat/README.md` | Defines lane scope, source-role enum, object families, lifecycle, sensitivity, cross-lane rules |
| Source-role doctrine | `docs/domains/habitat/MODEL_VS_OBSERVATION.md` | Defines observed/modeled/regulatory separation and publication-class defect posture |
| Land-cover observation detail | `contracts/domains/habitat/land_cover/observation.md` | Specific object-family contract for `LandCoverObservation` |
| Identity support | `contracts/domains/habitat/domain_feature_identity.md` | Shared deterministic identity and anti-collapse rules |
| Layer support | `contracts/domains/habitat/domain_layer_descriptor.md` | Public layer/descriptor semantics; not observation truth |
| Source registry | `data/registry/sources/habitat/` | Source identity, role, rights, cadence, activation |
| Policy | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Allow/restrict/deny/abstain behavior and sensitivity posture |
| Release | `release/` / `release/manifests/habitat/` | Publication, correction, rollback authority; not owned here |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/habitat/domain_observation.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_observation` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Field-level validation | NEEDS VERIFICATION |
| Contract pointer | `contracts/domains/habitat/domain_observation.md` |
| Fixtures root pointer | `fixtures/domains/habitat/domain_observation/` |
| Validator pointer | `tools/validators/domains/habitat/validate_domain_observation.py` |
| Policy pointer | `policy/domains/habitat/` |

Until the schema expands and validators/fixtures are confirmed, this contract is semantic guidance and review vocabulary only.

---

## Observation vs nearby objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `DomainObservation` | Shared observation envelope and source-role posture. | This contract. |
| `LandCoverObservation` | Observed land-cover classification over place/time. | Specific object-family contract. |
| `HabitatPatch` | Habitat unit/patch identity and geometry. | May cite observations; not replaced by observation envelope. |
| `EcologicalSystem` | Classified ecological-system unit. | May be observed/modelled/classified; role must be explicit. |
| `SuitabilityModel` | Modeled suitability surface. | Not an observation; consumes observations/context. |
| `ConnectivityEdge` / `Corridor` | Derived connectivity relation/geometry. | Not observed movement. |
| `UncertaintySurface` | Confidence/coverage/uncertainty. | Explains support; does not assert observation truth. |
| `EvidenceBundle` | Evidence support. | Observation may cite it; observation is not proof by itself. |
| `PolicyDecision` / `ReleaseManifest` | Decision and publication authority. | Observation cannot publish itself. |

---

## Assertions

A reviewed `DomainObservation` should semantically assert:

1. **Observation identity** — stable observation ID, object family, object role, source role, temporal scope, and digest basis.
2. **Source identity** — SourceDescriptor refs, source family, source record, rights, cadence, attribution, authority limits, and source vintage.
3. **Source role** — observed, modeled/model, regulatory/authority, aggregate, administrative, candidate, synthetic, derivative, or context, with aliases resolved by policy/schema review.
4. **Object-family binding** — Habitat object family or support object that the observation informs.
5. **Temporal scope** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
6. **Spatial scope** — point, polygon, raster extent, grid, tile set, analysis unit, or public-safe geometry posture where material.
7. **Evidence support** — EvidenceRef/EvidenceBundle refs required before consequential claims.
8. **Validation support** — ValidationReport refs for schema, source role, geometry/time, evidence, sensitivity, and release readiness.
9. **Policy support** — PolicyDecision refs where rights, sensitivity, source-role ambiguity, or release posture is material.
10. **Release/correction support** — release refs, correction refs, and rollback refs before public use.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating observation as regulatory designation | Only admitted authority sources can carry regulatory role. |
| Treating modeled output as observed | Hides assumptions, model card, receipt, and uncertainty. |
| Treating regulatory source record as biological truth | KFM records the designation; it does not assert the rule's correctness. |
| Treating aggregate as exact per-place evidence | Aggregates are public-safe rollups, not exact locations. |
| Treating candidate as published | Candidate records stay WORK/QUARANTINE or review-only. |
| Treating observation as EvidenceBundle | Observation can cite evidence; it is not proof. |
| Treating observation as layer or popup | UI surfaces are downstream carriers. |
| Treating occurrence context as Habitat-owned truth | Fauna/Flora own occurrence and plant-record truth. |
| Treating style filters as sensitivity controls | Sensitive transforms happen before public serving. |
| Letting AI infer missing source role or confidence | AI must abstain or deny when support is incomplete. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical KFM domain observation ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized digest over observation-relevant content. |
| `domain` | Must resolve to `habitat`. |
| `object_family` | Habitat object family being observed or supported. |
| `object_role` | Role inside Habitat trust model. |
| `observation_id` | Observation-local stable identifier. |
| `observation_kind` | Field survey, remote-sensing observation, inventory record, regulatory record, aggregate summary, modeled input, derivative support, candidate, synthetic, or accepted enum. |
| `source_id` | Stable source/source-derived handle. |
| `source_descriptor_ref` | Source identity, role, rights, cadence, attribution, authority limits. |
| `source_record_ref` | Source-native record, raster, vector, table, report, API object, or scene ref. |
| `source_family` | NLCD, NWI, GAP, LANDFIRE, ECOS, KDWP, NatureServe, PAD-US, remote sensing, field survey, or accepted enum. |
| `source_role` | Observed, modeled/model, regulatory/authority, aggregate, administrative, candidate, synthetic, derivative, context, or accepted enum. |
| `source_role_alias_status` | Notes unresolved alias drift such as `model` vs `modeled`. |
| `source_vintage` | Source product vintage/year/version. |
| `spatial_scope_ref` | Geometry, raster extent, grid, tile set, county/HUC/ecoregion/project ref, or public-safe scope. |
| `temporal_scope_ref` | Structured time-scope object or refs. |
| `source_time` | Source publication/assertion time. |
| `observed_time` | Observation/acquisition time where applicable. |
| `valid_time` | Valid interval of the object claim. |
| `retrieval_time` | KFM retrieval/harvest time. |
| `release_time` | Public-safe release time, if released. |
| `correction_time` | Correction/supersession time, if corrected. |
| `artifact_refs` | Source or processed artifacts supporting the observation. |
| `artifact_digests` | Digests for source/processed artifacts. |
| `identity_ref` | DomainFeatureIdentity ref. |
| `uncertainty_refs` | UncertaintySurface or uncertainty summary refs. |
| `evidence_refs` | EvidenceRef links. |
| `evidence_bundle_refs` | EvidenceBundle refs behind consequential use. |
| `validation_report_ref` | ValidationReport for schema, source role, geometry, time, evidence, sensitivity, and release. |
| `policy_decision_ref` | PolicyDecision where material. |
| `review_record_ref` | Steward review record. |
| `release_ref` | ReleaseManifest or PromotionDecision ref. |
| `correction_refs` | CorrectionNotice, supersession, replacement observation refs. |
| `rollback_refs` | Rollback target refs. |
| `quality_flags` | Missing source, unresolved role, time collapse, rights unknown, sensitivity unresolved, missing evidence, stale source, release missing. |

---

## Observation classes

| Class | Means | Public posture |
|---|---|---|
| `land_cover_observation` | Observed land cover/classification over place and time. | Public only after source, rights, evidence, validation, policy, release. |
| `field_survey_observation` | Steward/field survey context. | Rights/sensitivity review required. |
| `remote_sensing_observation` | Observed imagery/index/product. | Source vintage, resolution, footprint, uncertainty required. |
| `regulatory_observation_record` | Record of an authority designation. | Regulatory badge; not biological truth. |
| `aggregate_observation_summary` | Public-safe rollup/summary. | Must not imply exact geometry. |
| `context_observation` | Neighbor-lane context admitted through governed join. | Ownership remains with source lane. |
| `candidate_observation` | Unreviewed connector/watcher/model/import output. | No public edge. |
| `synthetic_observation_candidate` | AI/simulated/reconstructed content. | Not observed reality; requires strong labeling and review. |

---

## Source-role rules

| Role | DomainObservation rule | Failure mode |
|---|---|---|
| `observed` | Record the observed value with source vintage, class/source system, spatial scope, and uncertainty. | Misclassification or stale source. |
| `modeled` / `model` | Keep as model support/output with model card, receipt, and uncertainty when material. | Modeled-as-observed or modeled-as-regulatory. |
| `regulatory` / `authority` | Record that the competent authority designated something. | Treating designation as broader biological fact. |
| `aggregate` | Preserve aggregation scope and generalization receipt. | Aggregate-as-exact. |
| `administrative` | Preserve administrative/stewardship authority and limits. | Administrative-as-title or management instruction. |
| `candidate` | Hold until reviewed and promoted. | Candidate-as-public. |
| `synthetic` | Label as synthetic/AI/simulation; not source reality. | Synthetic-as-observed. |
| `derivative` | Preserve method, receipt, inputs, and weakest-input support. | Derived-as-primary observation. |
| `context` | Preserve owning-domain truth and join policy. | Habitat adopts neighboring-lane truth. |

---

## Temporal rules

Habitat observations must not collapse time dimensions.

| Time kind | Meaning | Observation risk if collapsed |
|---|---|---|
| `source_time` | When the source asserted or published the record. | Stale source appears current. |
| `observed_time` | When the landscape, image, survey, or phenomenon was observed. | Acquisition and publication are confused. |
| `valid_time` | Interval during which the observation is valid for analysis. | Past condition appears current. |
| `retrieval_time` | When KFM acquired the source artifact. | Harvest time is mistaken for observation. |
| `release_time` | When public-safe artifact was released. | Processing appears like publication. |
| `correction_time` | When correction/supersession happened. | Superseded observation remains authoritative. |

---

## Sensitivity and release

Observations can be sensitive when they reveal exact habitat, occurrence-linked context, rare species, stewardship-sensitive locations, private land context, or rights-limited source detail.

Rules:

- Sensitive joins fail closed until geoprivacy/redaction, policy, review, release, correction, and rollback support exist.
- Public-safe observation derivatives may need generalized geometry, aggregate scope, delayed publication, or steward-only exact access.
- Source-role, rights, sensitivity, validation, review, release, correction, and rollback refs must resolve before public clients use observation-bearing objects.
- Public UI/AI must show role labels and cannot infer stronger authority than evidence supports.
- Public clients use governed APIs and released artifacts, not RAW/WORK/QUARANTINE/candidate observation records.

---

## Lifecycle

| Phase | Observation handling |
|---|---|
| RAW | Source records, source terms, source time, observed time, rights, sensitivity, and hashes are captured but not public truth. |
| WORK / QUARANTINE | Candidate observations are normalized; role conflicts, time collapse, geometry/digest mismatch, rights gaps, and sensitivity failures are held with reasons. |
| PROCESSED | Reviewed observations bind source role, object family, temporal scope, artifact digests, evidence refs, validation report, policy posture, and correction state. |
| CATALOG / TRIPLET | Observation claims may be projected only with EvidenceBundle refs and source-role caveats. |
| RELEASE CANDIDATE | Public observation derivatives, API payloads, layer refs, and Focus Mode references require policy/review, release manifest, correction path, and rollback target. |
| PUBLISHED | Only released public-safe observations or derivatives appear through governed APIs, map surfaces, Evidence Drawer, Focus Mode, or reports. |
| CORRECTED / SUPERSEDED | Source update, role correction, geometry correction, digest correction, time correction, policy change, or sensitivity review triggers correction and possible rollback. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/habitat/domain_observation.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Confirm accepted source-role enum values and aliases such as `model` vs `modeled` and `authority` vs `regulatory`.
- [ ] Add valid fixtures for observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, and context observations.
- [ ] Add invalid fixtures for modeled-as-observed, modeled-as-regulatory, regulatory-as-biological-truth, aggregate-as-exact, candidate-as-published, synthetic-as-observed, context-with-ownership-collapse, time-collapse, digest mismatch, sensitive-exact public observation, and missing rollback target.
- [ ] Add validator checks for source role, object family, temporal scope, artifact digest, evidence refs, policy refs, sensitivity posture, release refs, and correction lineage.
- [ ] Add tests proving public map/UI/AI surfaces cannot treat tiles, popups, vector indexes, graph projections, or generated text as observation truth.
- [ ] Confirm release tests proving public clients consume released public-safe observations or derivatives only.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Source, role, object family, temporal scope, digest, evidence, policy, release, and rollback all resolve | `ANSWER` / public-safe observation may support a claim |
| Evidence, role, schema, rights, sensitivity, release, or rollback support is incomplete | `ABSTAIN` / `HOLD` |
| Role collapse, sensitive leak, candidate public path, or release bypass would occur | `DENY` |
| Schema, validator, source read, digest, evidence lookup, policy lookup, or release lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current target scaffold | Confirms target existed as greenfield scaffold before replacement. | Does not prove contract maturity. |
| Paired schema scaffold | Confirms schema path and current limited schema posture. | Does not prove field-level validation. |
| Habitat README | Confirms lane scope, source-role enum, object families, lifecycle gates, sensitivity, cross-lane rules, map/AI boundaries, and proposed tests. | Some implementation claims remain PROPOSED. |
| Model-vs-observation doc | Confirms observed/modeled/regulatory role separation and publication-class defect posture. | Role spelling and policy/schema enforcement remain NEEDS VERIFICATION. |
| Adjacent Habitat contracts | Provide object-family observation, identity, layer, model, corridor, and uncertainty patterns. | Recent contract content is semantic documentation, not schema enforcement. |
| User-provided authoring role | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized Habitat observation weakens source-role separation, temporal discipline, sensitivity, evidence integrity, or release integrity.

Rollback triggers include:

- observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, derivative, or context role is corrected;
- source, source vintage, geometry, temporal scope, artifact digest, evidence ref, policy decision, or release ref changes;
- modeled output was presented as observed or regulatory;
- regulatory designation was presented as biological fact beyond the designation;
- sensitive exact observation or occurrence-linked context leaked publicly;
- candidate observation appeared in public API/UI/AI path;
- public map tile, popup, AI answer, graph projection, or vector index was treated as observation truth;
- release, correction, or rollback refs were missing for public observation use.

Rollback artifacts should include affected observation IDs, object refs, source refs, source-role refs, temporal-scope refs, artifact digests, geometry refs, evidence refs, validation reports, policy decisions, release refs, correction notices, rollback cards, replacement observations, and public-cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Which fields must be required in `domain_observation.schema.json`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Should source-role values use `model` or `modeled`, and should `authority` alias `regulatory`? | NEEDS VERIFICATION | Source-role/schema/policy review. |
| Should `DomainObservation` be a concrete persisted object or a shared envelope inherited by object-family contracts? | NEEDS VERIFICATION | Contract steward + Habitat steward review. |
| How should public-safe observation IDs link to restricted exact observations? | NEEDS VERIFICATION | Policy, redaction, and release design review. |
| Which tests prove candidate observations cannot become public truth? | NEEDS VERIFICATION | Fixture/test inspection. |
| How should observation correction invalidate public layers, graph edges, and Focus Mode cards? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Habitat contracts root.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — deterministic identity and anti-collapse support.
- [`./domain_layer_descriptor.md`](./domain_layer_descriptor.md) — domain layer/view descriptor support.
- [`./SuitabilityModel.md`](./SuitabilityModel.md) — modeled suitability contract.
- [`./connectivity_edge.md`](./connectivity_edge.md) — derived connectivity contract.
- [`./corridor.md`](./corridor.md) — derived corridor geometry contract.
- [`./land_cover/observation.md`](./land_cover/observation.md) — land-cover observation contract.
- [`../../../docs/domains/habitat/README.md`](../../../docs/domains/habitat/README.md) — Habitat lane doctrine.
- [`../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md`](../../../docs/domains/habitat/MODEL_VS_OBSERVATION.md) — source-role anti-collapse doctrine.
- [`../../../schemas/contracts/v1/domains/habitat/domain_observation.schema.json`](../../../schemas/contracts/v1/domains/habitat/domain_observation.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
