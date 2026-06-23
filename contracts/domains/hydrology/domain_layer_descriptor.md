<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hydrology-domain-layer-descriptor
title: Domain Layer Descriptor Contract — Hydrology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Governed API steward
  - OWNER_TBD — Contracts steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hydrology; layer-descriptor; map-ui-profile; source-role-aware; evidence-bound; release-gated; rollback-aware; not-for-life-safety
tags: [kfm, contracts, hydrology, domain-layer-descriptor, LayerManifest, MapReleaseManifest, MapLibre, EvidenceDrawerPayload, source-role, NFHL, regulatory-context, observed-flood, hydrograph, release-manifest, rollback]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./domain_feature_identity.md
  - ./domain_observation.md
  - ./domain_validation_report.md
  - ./huc_unit.md
  - ./hydrograph.md
  - ./nfhl_zone.md
  - ./aquifer_observation.md
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json
  - ../../../policy/domains/hydrology/
  - ../../../fixtures/domains/hydrology/domain_layer_descriptor/
  - ../../../tests/domains/hydrology/test_domain_layer_descriptor.*
  - ../../../data/published/layers/hydrology/
  - ../../../release/candidates/hydrology/
notes:
  - "Expanded from a greenfield scaffold at contracts/domains/hydrology/domain_layer_descriptor.md."
  - "The paired schema exists at schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json, but it remains a PROPOSED stub with only spec_hash, id, and version properties; only id is required and additionalProperties=true."
  - "Hydrology API doctrine confirms a Hydrology layer manifest resolver returning LayerManifest/domain layer descriptor with ANSWER / DENY / ERROR, but route names, mounts, DTO field shapes, and enforcement remain PROPOSED / NEEDS VERIFICATION."
  - "This descriptor profiles public/release layer delivery. It is not source truth, EvidenceBundle proof, PolicyDecision, ReleaseManifest, RunReceipt, public API implementation, emergency warning, or life-safety instruction."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Layer Descriptor Contract — Hydrology

> Semantic contract for `domain_layer_descriptor`: the Hydrology layer/view descriptor that binds a public or release-candidate map/API layer to released artifacts, source-role posture, evidence, policy, release state, UI obligations, correction lineage, and rollback support without turning a layer into source truth, evidence proof, or flood-warning authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hydrology" src="https://img.shields.io/badge/domain-Hydrology%20%5BDOM--HYD%5D-1f9eda">
  <img alt="Object: domain_layer_descriptor" src="https://img.shields.io/badge/object-domain__layer__descriptor-blue">
  <img alt="Boundary: layer not truth" src="https://img.shields.io/badge/boundary-layer__not__truth-critical">
  <img alt="NFHL: regulatory not observed" src="https://img.shields.io/badge/NFHL-regulatory__not__observed-critical">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
</p>

`contracts/domains/hydrology/domain_layer_descriptor.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Layer descriptor vs trust objects](#layer-descriptor-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Layer classes](#layer-classes) · [Display obligations](#display-obligations) · [Source-role rules](#source-role-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/hydrology/domain_layer_descriptor.md`  
> **Schema path:** `schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json`  
> **Schema posture:** paired schema exists, but remains a `PROPOSED` stub with only `spec_hash`, `id`, and `version` visible. Only `id` is required and `additionalProperties: true` is still allowed.  
> **Truth posture:** Hydrology API doctrine confirms the layer manifest resolver and public-layer release gates. Field-level schema shape, validators, fixtures, policy enforcement, runtime route implementation, layer artifacts, release manifests, and UI behavior remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A Hydrology layer descriptor is not a layer's proof, source feed, release approval, or emergency guidance. It is a downstream descriptor for governed delivery of released or release-candidate Hydrology views.

---

## Meaning

`domain_layer_descriptor` records how a Hydrology map/API/UI layer may be presented safely once it is bound to evidence, policy, release, correction, and rollback controls.

It answers:

- Which Hydrology layer is being described?
- Which released artifact or release-candidate artifact may be served?
- Which object family and source role does the layer represent?
- Does the layer include observed readings, regulatory context, modeled derivatives, aggregate summaries, administrative context, candidates, or synthetic content?
- Which EvidenceRefs, EvidenceBundles, PolicyDecisions, ReleaseManifests, CorrectionNotices, and RollbackCards must resolve before public use?
- Which UI obligations must be displayed: regulatory badge, provisional-status notice, generalized-geometry notice, citation/Evidence Drawer link, stale-source badge, release/correction state, or not-for-life-safety warning?

The descriptor is the bridge between Hydrology object contracts and the public renderer/API surface. It does not replace either side.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable layer meaning | `contracts/domains/hydrology/domain_layer_descriptor.md` | This file; semantic contract for Hydrology layer descriptors. |
| Machine schema | `schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json` | Confirmed stub; full layer descriptor shape is not enforced yet. |
| Hydrology API doctrine | `docs/domains/hydrology/API_CONTRACTS.md` | Defines the layer manifest resolver, finite outcomes, trust membrane, deny rules, DTO families, and release gates. |
| Contract root | `contracts/domains/hydrology/README.md` | Directory root and object-family boundaries. |
| Feature identity | `contracts/domains/hydrology/domain_feature_identity.md` | Stable identity, source role, time, geography/version, digest companion. |
| Decision envelope | `contracts/domains/hydrology/decision_envelope.md` | Runtime finite-outcome wrapper. |
| Observation envelope | `contracts/domains/hydrology/domain_observation.md` | Observation/source-role boundary, if present/expanded. |
| Source registry | `data/registry/sources/hydrology/` | Expected SourceDescriptor instances and role/rights/cadence. |
| Published artifacts | `data/published/layers/hydrology/` | Expected public-safe artifacts, never release authority by themselves. |
| Policy | `policy/domains/hydrology/` | Expected deny/restrict/abstain and sensitivity gates. |
| Release | `release/candidates/hydrology/` and release roots | ReleaseManifest, MapReleaseManifest, CorrectionNotice, RollbackCard. |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_layer_descriptor` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Contract pointer | `contracts/domains/hydrology/domain_layer_descriptor.md` |
| Fixtures pointer | `fixtures/domains/hydrology/domain_layer_descriptor/` |
| Validator pointer | `tools/validators/domains/hydrology/validate_domain_layer_descriptor.py` |
| Policy pointer | `policy/domains/hydrology/` |
| Full layer descriptor enforcement | NEEDS VERIFICATION |

The current schema does not prove enforcement of layer ID, artifact refs, release refs, evidence refs, source role, UI obligations, geometry posture, or rollback linkage.

---

## Layer descriptor vs trust objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `domain_layer_descriptor` | Layer meaning, source-role posture, artifact binding, display duties, and public-delivery constraints. | This contract. |
| `LayerManifest` | Cross-cutting layer manifest payload returned by a layer manifest resolver. | Descriptor profiles Hydrology requirements; does not redefine shared manifest. |
| `MapReleaseManifest` | Active map/layer release set and version lock. | Required for public layer load; descriptor does not publish. |
| `EvidenceBundle` | Evidence support for claims. | Descriptor cites it; descriptor is not proof. |
| `PolicyDecision` | Allow/restrict/deny/abstain. | Descriptor cites policy; descriptor does not decide policy. |
| `ReleaseManifest` | Publication authority and rollback target. | Descriptor cites it; descriptor is not release approval. |
| `RunReceipt` | Build/tile/pipeline generation memory. | Descriptor may cite artifacts from a run; it is not the run receipt. |
| `CorrectionNotice` | Public correction/supersession. | Descriptor must expose correction state where material. |
| Map tiles/styles | Delivery artifacts. | Never evidence, proof, release, source truth, or redaction policy by themselves. |
| Evidence Drawer payload | UI projection of evidence. | Descriptor must make drawer resolution possible, but drawer owns projection. |

---

## Assertions

A reviewed `domain_layer_descriptor` should assert:

1. **Layer identity** — stable descriptor ID, layer ID, Hydrology domain, layer class, version, and `spec_hash`.
2. **Artifact binding** — artifact refs, digests, media type, CRS, bounds, zoom/resolution, temporal extent, and public-safe flag.
3. **Source-role binding** — observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain visible and do not collapse.
4. **Evidence binding** — EvidenceRefs/EvidenceBundles are resolvable for layer claims and Evidence Drawer inspection.
5. **Policy binding** — PolicyDecision refs and exposure/restriction state travel with the descriptor.
6. **Release binding** — ReleaseManifest / MapReleaseManifest, correction path, and rollback target exist before public layer loading.
7. **Temporal posture** — source, observed, valid, retrieval, release, correction, and stale/freshness states are not collapsed.
8. **Display duties** — NFHL/regulatory, provisional, modeled, aggregate, generalized, sensitive, stale, correction, and not-for-life-safety badges/notes are machine-inspectable where material.
9. **Public path safety** — layer loads only through governed APIs and released artifacts; no direct RAW/WORK/source endpoint path.
10. **Correction/rollback readiness** — changed source, artifact, policy, or release state can invalidate the descriptor and all downstream surfaces.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Layer descriptor as source truth | SourceDescriptor and source payloads own source authority. |
| Layer descriptor as evidence proof | EvidenceBundle/proof support remains separate. |
| Layer descriptor as release authority | ReleaseManifest/MapReleaseManifest own publication. |
| Tile URL as public release | Tile artifacts require release, digest, policy, evidence, and rollback refs. |
| Map style as sensitivity control | Style is delivery; redaction/generalization needs policy and receipt support. |
| NFHL layer as observed flood extent | Regulatory context is not observed inundation. |
| Modeled hydrograph layer as observed series | Modeled source role must remain visible. |
| Aggregate HUC layer as per-place truth | Aggregation scope must remain visible. |
| Candidate layer as public layer | WORK/QUARANTINE/release-candidate material is not public. |
| Emergency warning or life-safety instruction layer | Hydrology is not an alert authority. |
| AI/focus answer inferred from layer alone | AI answers require released EvidenceBundle support and AIReceipt/citation closure. |

---

## Recommended fields

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the current schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical Hydrology layer descriptor ID. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic digest over normalized layer descriptor semantics. |
| `domain` | Must resolve to `hydrology`. |
| `layer_id` | Stable layer identifier used by governed API/UI. |
| `layer_class` | HUC/watershed, reach, gauge, observation, NFHL regulatory, hydrograph, upstream trace, groundwater, cross-link, aggregate, or accepted enum. |
| `object_family_refs` | Hydrology object families represented in the layer. |
| `artifact_refs` | Released artifact refs such as PMTiles, vector tiles, COG, GeoParquet, API payload, or report/export artifact. |
| `artifact_digests` | Content digests for layer artifacts. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, authority, citation. |
| `source_role_summary` | Role set represented in the layer. |
| `temporal_extent` | Source/observed/valid/retrieval/release/correction time coverage. |
| `freshness_state` | current, historical, stale_source, superseded, withdrawn, provisional, unknown, or accepted enum. |
| `geometry_role` | exact_internal, source_scale, generalized_public, aggregate_public, withheld, restricted, or accepted enum. |
| `evidence_ref_ids` | EvidenceRefs available for feature/drawer resolution. |
| `evidence_bundle_ids` | EvidenceBundles supporting public layer claims. |
| `policy_decision_refs` | Policy decisions controlling exposure. |
| `release_refs` | ReleaseManifest, MapReleaseManifest, or PromotionDecision refs. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | RollbackCard/rollback target refs. |
| `ui_obligations` | Required legend badges, caveats, disclaimers, drawer links, and export notes. |
| `interaction_policy` | view, click, drawer, focus_context, export, download, denied, or accepted enum. |
| `quality_flags` | missing_evidence, missing_release, stale_source, source_role_conflict, nfhl_observed_collapse, modeled_as_observed, aggregate_as_per_place, sensitive_join, schema_stub. |

---

## Layer classes

| Layer class | Publishable posture | Required display behavior |
|---|---|---|
| `huc_unit` / `watershed` | Boundary/accounting context. | Snapshot/vintage and source role visible. |
| `hydro_feature` / `reach_identity` | Hydrographic network context. | Source version, ambiguity/ABSTAIN state, and evidence support visible. |
| `gauge_site` | Monitoring site identity. | Site metadata separate from observations. |
| `flow_observation` / `water_level_observation` | Observed reading layer. | Unit, qualifier/provisional status, observed/source time, evidence drawer. |
| `water_quality_observation` | Observed parameter layer. | Parameter, unit, qualifier, sampling window. |
| `groundwater_well` / `aquifer_observation` | Groundwater context or observation. | Private-property/sensitive geometry review; generalized public geometry where needed. |
| `nfhl_zone` / `flood_context` | Regulatory flood-hazard context. | Regulatory badge; never observed flooding. |
| `observed_flood_event` | Observed inundation evidence. | Event time, source evidence, and distinction from NFHL. |
| `hydrograph` | Observed or modeled time-series view. | Role badge; model/run/uncertainty for modeled outputs. |
| `upstream_trace` | Derived network traversal result. | Source graph/version, algorithm, evidence/receipt. |
| `water_use_link` / `drought_link` / `irrigation_link` | Cross-domain relation layer. | Both lanes' source roles and evidence; sensitive joins reviewed. |

---

## Display obligations

Every public Hydrology layer descriptor should make these duties machine-inspectable before a public client can render it as `ANSWER`:

- release state and ReleaseManifest / MapReleaseManifest reference;
- EvidenceBundle or EvidenceRef resolution path;
- source-role badges for observed/regulatory/modeled/aggregate/administrative/candidate/synthetic content;
- NFHL regulatory caveat where NFHL or flood-regulatory context is present;
- provisional/final status for USGS/NWIS observations where material;
- model/run/uncertainty caveat for modeled hydrograph or derived surfaces;
- generalized/restricted geometry notice where public geometry differs from source/internal geometry;
- stale, superseded, withdrawn, or correction state when material;
- rollback target for published layer artifacts;
- not-for-life-safety notice when a Hydrology layer could be mistaken for emergency flood guidance.

A layer that cannot provide these duties may still be useful internally, but it is not public-ready.

---

## Source-role rules

| Source role | Layer descriptor behavior |
|---|---|
| `observed` | May support observed readings/events when time, unit, qualifier, evidence, and release resolve. |
| `regulatory` | May support NFHL/FloodContext as regulatory context only; observed-flood framing is denied. |
| `modeled` | May support modeled hydrograph or derived surfaces with run/receipt/uncertainty; observed framing is denied. |
| `aggregate` | May support HUC/watershed/county rollups with aggregation scope; per-place framing is denied. |
| `administrative` | May support registry/allocation/accounting context; not an observation unless separately evidenced. |
| `candidate` | No public layer serving before governed promotion. |
| `synthetic` | Never observed reality; representation/AI boundaries required. |

---

## Lifecycle

| Phase | Layer descriptor handling |
|---|---|
| RAW | Source metadata/artifact references may be captured, but no public descriptor is served. |
| WORK / QUARANTINE | Candidate descriptor is normalized; missing source role, evidence, release, sensitivity, or role-collapse issues are held. |
| PROCESSED | Descriptor can bind candidate artifact, digest, temporal extent, source-role summary, EvidenceRefs, ValidationReport, and quality flags. |
| CATALOG / TRIPLET | Descriptor may support catalog/discovery and release candidates, but not public serving without release closure. |
| RELEASE CANDIDATE | ReleaseManifest, MapReleaseManifest, EvidenceBundle, PolicyDecision, correction path, rollback target, and UI obligations are checked. |
| PUBLISHED | Governed API may return layer descriptor / LayerManifest for released public-safe artifacts only. |
| CORRECTED / SUPERSEDED | Source update, policy change, artifact digest change, correction, withdrawal, or rollback invalidates the descriptor and downstream caches. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json` beyond `spec_hash`, `id`, and `version`.
- [ ] Decide whether this domain descriptor is a profile of shared `LayerManifest` or an independent Hydrology DTO.
- [ ] Define canonical `layer_class`, `geometry_role`, `freshness_state`, `interaction_policy`, `ui_obligations`, and `quality_flags` values.
- [ ] Add positive fixtures for HUCUnit boundary, gauge-site, provisional flow observation, NFHL regulatory context, observed flood event, modeled hydrograph, upstream trace, and generalized groundwater/aquifer layer.
- [ ] Add negative fixtures for NFHL-as-observed-flood, modeled-hydrograph-as-observed, aggregate-as-per-place, unreleased-layer-load, RAW/WORK path exposure, candidate-as-public, missing ReleaseManifest, missing EvidenceBundle, missing rollback target, and life-safety layer framing.
- [ ] Confirm policy can DENY or RESTRICT sensitive groundwater/private-property, infrastructure, and cross-lane joins.
- [ ] Confirm governed API layer manifest resolver returns `ANSWER`, `DENY`, or `ERROR` for layer loads and never silently falls through to source endpoints.
- [ ] Confirm MapLibre/public UI surfaces render negative states rather than blank/generic error states.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Descriptor, artifact, evidence, source role, policy, release, correction, rollback, and display obligations resolve | `ANSWER` / public-safe layer manifest |
| Release, policy, sensitivity, role-collapse, source-rights, or public-path rule blocks layer | `DENY` |
| Schema, artifact, evidence, policy, release, or resolver failure prevents evaluation | `ERROR` |
| Feature/drawer/focus question against the layer lacks evidence/citation support | `ABSTAIN` on that surface, not necessarily layer manifest resolver |

---

## Rollback

Rollback is required when a Hydrology layer descriptor weakens source-role integrity, evidence closure, policy/release state, sensitivity posture, correction lineage, or the public trust membrane.

Rollback triggers include descriptor serving without ReleaseManifest or MapReleaseManifest; missing artifact digest; missing EvidenceBundle; missing rollback target; NFHL regulatory layer rendered as observed flood extent; modeled hydrograph rendered as observation; aggregate HUC rollup rendered as per-place observation; private-property or sensitive infrastructure join exposed without review; public client reading RAW/WORK/QUARANTINE/source endpoints directly; Focus Mode answer derived from a layer without CitationValidationReport; tile/style used as redaction or proof; correction/withdrawal not propagated; or schema/contract drift after migration.

Rollback artifacts should include affected descriptor IDs, layer IDs, artifact refs/digests, object-family refs, source descriptors, source-role summaries, temporal extents, geometry roles, EvidenceRefs/EvidenceBundles, ValidationReports, PolicyDecisions, ReleaseManifests, MapReleaseManifests, CorrectionNotices, RollbackCards, invalidated decision envelopes, invalidated exports, and public-cache/style invalidation instructions.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hydrology/domain_layer_descriptor.md` scaffold | CONFIRMED | Target existed as a greenfield scaffold. | Did not contain Hydrology-specific layer semantics. |
| `schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json` | CONFIRMED | Schema pointer, current stub fields, fixtures/validator/policy pointers. | Does not enforce full layer descriptor fields. |
| `docs/domains/hydrology/API_CONTRACTS.md` | CONFIRMED | Layer manifest resolver, trust-membrane posture, finite outcomes, DTO/object-family map, deny rules, lifecycle gates, anti-patterns, validation fixture families. | Route names, DTO shapes, policy runtime, and implementation remain PROPOSED / NEEDS VERIFICATION. |
| `contracts/domains/hydrology/README.md` | CONFIRMED | Contract-root object families, trust flow, source-role rules, validation and rollback expectations. | Orientation doc, not schema enforcement. |
| `contracts/domains/hydrology/domain_feature_identity.md` | CONFIRMED | Identity/source-role/time/digest companion semantics. | Identity contract, not layer schema enforcement. |
| `contracts/domains/hydrology/decision_envelope.md` | CONFIRMED | Runtime finite-outcome alias and Hydrology deny/obligation profile. | Runtime envelope, not layer descriptor schema. |
| `docs/domains/hydrology/CANONICAL_PATHS.md` | CONFIRMED | Responsibility-root doctrine and schema-home rule. | Some path-as-applied claims in that doc are PROPOSED, though this target path is directly verified. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `domain_layer_descriptor` a Hydrology profile of shared `LayerManifest` or a separate domain DTO? | NEEDS VERIFICATION | Schema/API steward review. |
| Which fields must be required in `domain_layer_descriptor.schema.json`? | NEEDS VERIFICATION | Schema PR with valid/invalid fixtures. |
| Which layer classes and geometry roles are canonical? | NEEDS VERIFICATION | Contract/schema/policy review. |
| Which public UI badges are required for NFHL, provisional observations, modeled hydrographs, generalized geometry, and stale sources? | NEEDS VERIFICATION | Map/UI + policy fixture review. |
| Which validator proves a layer cannot load without ReleaseManifest and rollback target? | NEEDS VERIFICATION | Validator/test implementation. |
| Which MapReleaseManifest contract is canonical for Hydrology layer sets? | NEEDS VERIFICATION | Release/schema review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hydrology contract-root README.
- [`./decision_envelope.md`](./decision_envelope.md) — Hydrology runtime decision-envelope alias.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hydrology feature identity contract.
- [`./domain_observation.md`](./domain_observation.md) — Hydrology observation envelope, if present/expanded.
- [`./domain_validation_report.md`](./domain_validation_report.md) — Hydrology validation report, if present/expanded.
- [`../../../docs/domains/hydrology/API_CONTRACTS.md`](../../../docs/domains/hydrology/API_CONTRACTS.md) — Hydrology governed API and layer-manifest doctrine.
- [`../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md`](../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md) — source-role anti-collapse matrix.
- [`../../../docs/domains/hydrology/IDENTITY_MODEL.md`](../../../docs/domains/hydrology/IDENTITY_MODEL.md) — identity and deterministic hash doctrine.
- [`../../../docs/domains/hydrology/CANONICAL_PATHS.md`](../../../docs/domains/hydrology/CANONICAL_PATHS.md) — responsibility-root path map.
- [`../../../schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json`](../../../schemas/contracts/v1/domains/hydrology/domain_layer_descriptor.schema.json) — current schema stub.

[Back to top](#top)
