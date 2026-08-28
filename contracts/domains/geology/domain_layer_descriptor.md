<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-domain-layer-descriptor
title: Domain Layer Descriptor Contract — Geology
type: semantic-contract
version: v0.2
status: draft; PROPOSED; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public-with-gates; semantic-contract; geology; layer-descriptor; map-ui-profile; evidence-bound; policy-aware; release-gated; rollback-ready
tags: [kfm, contracts, geology, domain_layer_descriptor, layer-descriptor, layer-manifest, maplibre, public-safe-geometry, evidence-ref, evidence-bundle, release-manifest, policy-decision, source-role, catalog-closure, artifact-digest, rollback, correction]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./GeologicUnit.md
  - ./GeologyBoundaryVersion.md
  - ./StructureFeature.md
  - ./BoreholeReference.md
  - ./WellLogReference.md
  - ./MineralOccurrence.md
  - ./ResourceDeposit.md
  - ./ResourceEstimate.md
  - ../../../docs/domains/geology/MAP_UI_CONTRACTS.md
  - ../../../docs/domains/geology/API_CONTRACTS.md
  - ../../../docs/domains/geology/RELEASE_INDEX.md
  - ../../../docs/domains/geology/CANONICAL_PATHS.md
  - ../../../packages/domains/geology/layer_manifest/README.md
  - ../../../schemas/contracts/v1/domains/geology/domain_layer_descriptor.schema.json
  - ../../../fixtures/domains/geology/domain_layer_descriptor/
  - ../../../tools/validators/domains/geology/validate_domain_layer_descriptor.py
  - ../../../policy/domains/geology/
  - ../../../data/registry/sources/geology/
  - ../../../release/manifests/geology/
notes:
  - "Expanded from a greenfield scaffold into a Geology domain_layer_descriptor semantic contract."
  - "The paired schema exists at schemas/contracts/v1/domains/geology/domain_layer_descriptor.schema.json, but it is still a PROPOSED stub with only id, version, and spec_hash fields; field-level enforcement remains NEEDS VERIFICATION."
  - "This contract defines a Geology profile/support descriptor for released or release-candidate map layers. It does not replace cross-cutting LayerManifest, StyleManifest, TileArtifactManifest, MapReleaseManifest, EvidenceDrawerPayload, ReleaseManifest, EvidenceBundle, PolicyDecision, SourceDescriptor, or public API contracts."
  - "Layer descriptors are downstream carriers. They must point to release, evidence, catalog, policy, source-role, artifact digest, geometry role, warning, correction, and rollback support rather than becoming canonical truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Layer Descriptor — Geology

> Semantic contract for `domain_layer_descriptor`: the Geology profile that describes a released or release-candidate map layer's purpose, artifact binding, geometry role, evidence lookup, policy posture, source caveats, UI warnings, correction state, and rollback target without turning the layer into canonical truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-2e7d32">
  <img alt="Object: domain_layer_descriptor" src="https://img.shields.io/badge/object-domain__layer__descriptor-blue">
  <img alt="Schema: stub" src="https://img.shields.io/badge/schema-stub%20%2F%20NEEDS__VERIFICATION-orange">
  <img alt="Truth: downstream carrier" src="https://img.shields.io/badge/truth-downstream__carrier-informational">
  <img alt="Boundary: not release authority" src="https://img.shields.io/badge/boundary-not__release__authority-critical">
</p>

`contracts/domains/geology/domain_layer_descriptor.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Layer descriptor vs manifest families](#layer-descriptor-vs-manifest-families) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended semantics](#recommended-semantics) · [Layer classes](#layer-classes) · [Geometry roles](#geometry-roles) · [Source-role and warning rules](#source-role-and-warning-rules) · [Anti-collapse rules](#anti-collapse-rules) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/geology/domain_layer_descriptor.md`  
> **Schema path:** `schemas/contracts/v1/domains/geology/domain_layer_descriptor.schema.json`  
> **Schema posture:** paired schema exists, but is still a `PROPOSED` stub. It currently defines only `spec_hash`, `id`, and `version`, requires only `id`, and permits additional properties.  
> **Truth posture:** Geology map/UI and layer-manifest doctrine support this document's boundary rules. Field-level schema enforcement, fixtures, validator behavior, policy runtime, release workflow, API behavior, UI behavior, artifact inventory, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> `domain_layer_descriptor` is a Geology layer profile / support contract. It does **not** replace canonical object-family truth, cross-cutting `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `MapReleaseManifest`, `ReleaseManifest`, `EvidenceBundle`, `PolicyDecision`, `SourceDescriptor`, governed API behavior, or AI/UI truth.

---

## Meaning

`domain_layer_descriptor` records the Geology-specific semantics needed to describe a map-ready layer **after** upstream governance has supplied release, evidence, catalog, policy, artifact, source, sensitivity, warning, and rollback support.

It answers:

- Which Geology layer is being described?
- Which released or release-candidate artifact may a governed API expose?
- What geometry role does the layer carry: exact internal, source-scale, generalized public, aggregate public, withheld, restricted, or synthetic representation?
- Which EvidenceRef/EvidenceBundle, SourceDescriptor, PolicyDecision, catalog closure, release manifest, artifact digest, receipt, and rollback target support it?
- Which user-facing warnings must follow the layer into MapLibre, Evidence Drawer, Focus Mode, API payloads, exports, and downstream reports?
- Which finite outcome applies when evidence, policy, geometry role, artifact digest, source role, release state, or rollback support is missing?

A layer descriptor is a delivery-support object. It may tell a client what to load and how to warn users. It must never become the source dataset, the canonical Geology object, the proof object, the release decision, the public publication approval, or the AI explanation.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Geology layer-descriptor meaning | `contracts/domains/geology/domain_layer_descriptor.md` | Owned here |
| Machine schema shape | `schemas/contracts/v1/domains/geology/domain_layer_descriptor.schema.json` | CONFIRMED stub; field-level enforcement NEEDS VERIFICATION |
| Layer-manifest helper implementation | `packages/domains/geology/layer_manifest/` | May build/validate payloads from governed inputs; not release authority |
| Map/UI doctrine | `docs/domains/geology/MAP_UI_CONTRACTS.md` | Explains cross-cutting MapLibre/UI families and Geology profile obligations |
| API doctrine | `docs/domains/geology/API_CONTRACTS.md` | Explains governed API surfaces and finite outcomes |
| Release doctrine | `docs/domains/geology/RELEASE_INDEX.md` | Human index only; actual release authority belongs to release artifacts |
| Semantic contracts | `contracts/domains/geology/` | Object-family meanings referenced by layer descriptors |
| Source registry | `data/registry/sources/geology/` | Source identity, source role, rights, cadence, citation, caveats |
| Evidence/proofs/catalog | `data/proofs/`, `data/catalog/`, or accepted repo homes | EvidenceBundle, ValidationReport, catalog closure, proof support |
| Policy and sensitivity | `policy/domains/geology/`, `policy/sensitivity/geology/` | Public exposure, redaction, restriction, denial, and abstention decisions |
| Release and rollback | `release/manifests/`, `release/candidates/geology/`, accepted release homes | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal support |
| Public consumers | governed API, MapLibre, Evidence Drawer, Focus Mode | Consume released descriptors; do not read internal lifecycle stores directly |

---

## Schema posture

The paired schema exists but is intentionally thin.

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/geology/domain_layer_descriptor.schema.json` |
| Schema status | `PROPOSED` |
| Schema description | Greenfield placeholder; fields to be defined per contract document and ADR |
| Defined properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Schema-linked fixtures root | `fixtures/domains/geology/domain_layer_descriptor/` |
| Schema-linked validator | `tools/validators/domains/geology/validate_domain_layer_descriptor.py` |
| Validator implementation | NEEDS VERIFICATION; schema references the path, but runtime/file behavior was not verified here |

Until the schema is expanded, this contract is the semantic authority for review and fixture design, but not proof of field-level validation.

---

## Layer descriptor vs manifest families

KFM already uses cross-cutting map/UI contract families. The Geology lane profiles those families; it does not redefine them.

| Thing | Owner/home | What this contract may say | What this contract must not do |
|---|---|---|---|
| `domain_layer_descriptor` | `contracts/domains/geology/` + paired Geology schema stub | Geology-specific meaning, required support refs, warning posture, anti-collapse rules | Become release authority or map schema authority |
| `LayerManifest` | Cross-cutting map contract/schema home | Geology-specific profile/fill obligations | Be redefined as a Geology-only family |
| `StyleManifest` | Cross-cutting map contract/schema home | Required legend/uncertainty/source-role warning behavior | Treat style as evidence or certainty |
| `TileArtifactManifest` | Cross-cutting map contract/schema home | Artifact digest/media/bounds support expected by Geology | Treat PMTiles/MVT/GeoParquet/COG as evidence by itself |
| `MapReleaseManifest` / `ReleaseManifest` | Release/map/release homes | Must be referenced before public exposure | Be replaced by this descriptor |
| `EvidenceDrawerPayload` | Cross-cutting UI contract home | Must be resolvable from layer features | Be treated as canonical truth |
| `FocusModeResponse` / `AIReceipt` | Governed AI/UI homes | May cite layer context only after evidence resolution | Authorize or fill evidence/policy/release fields |

> [!WARNING]
> A layer descriptor can be complete enough for rendering and still be insufficient for publication. Public readiness requires release, evidence, policy, catalog closure, digest, geometry-role, receipt where needed, and rollback support.

---

## Assertions

A reviewed `domain_layer_descriptor` should semantically assert:

1. **Layer identity** — stable layer descriptor ID, layer ID, domain, version, purpose, and `spec_hash`.
2. **Artifact binding** — released or release-candidate artifact ref, digest, media type, bounds, CRS, min/max zoom or equivalent render envelope.
3. **Release binding** — ReleaseManifest, PromotionDecision, release state, supersession, correction, withdrawal, and rollback refs.
4. **Evidence binding** — EvidenceRef/EvidenceBundle lookup refs and proof/catalog closure refs for layer claims and feature-level inspection.
5. **Source binding** — SourceDescriptor refs, source roles, attribution, source time, source scale, rights, caveats, and source limitations.
6. **Policy binding** — PolicyDecision refs, sensitivity state, public exposure decision, redaction/aggregation/representation receipts where material.
7. **Geometry-role clarity** — exact/internal, source-scale, generalized-public, aggregate-public, centroid-public, withheld, restricted, or synthetic representation state.
8. **UI warning obligations** — required warnings for source scale, generalized geometry, rights, stale state, supersession, modeled/synthetic status, uncertainty, or restricted detail.
9. **Interaction constraints** — which interactions are allowed: click-to-evidence, hover label, download, export, Focus Mode context, or no interaction.
10. **Finite outcome support** — deterministic `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `RESTRICT`, `WITHHOLD_GEOMETRY`, or `ALLOW_WITH_WARNINGS` style outcomes where applicable.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Treating a layer as canonical geology truth | Layers are downstream carriers; object-family contracts and EvidenceBundles carry support. |
| Treating an artifact path as evidence | PMTiles/MVT/GeoParquet/COG/JSON must have evidence and release support. |
| Treating a style as certainty | Styling can communicate uncertainty; it must not erase it. |
| Treating generalized geometry as exact geometry | Public-safe geometry is a derivative and must carry geometry role and receipt/caveat. |
| Treating a layer descriptor as ReleaseManifest | Release authority belongs to release artifacts, not this contract. |
| Treating a layer descriptor as PolicyDecision | Policy owns allow/restrict/deny/abstain. |
| Treating a MapLibre popup as claim authority | Popups must resolve evidence; UI is not evidence. |
| Treating AI text as manifest data | AI can summarize released evidence; it cannot fill release/evidence/policy fields. |
| Treating RAW/WORK/QUARANTINE/candidate artifacts as public | Public clients consume governed API/released artifacts only. |
| Treating administrative layers as physical geology | Source role must constrain claim scope. |

---

## Recommended semantics

The following fields are **PROPOSED** targets for future schema expansion. Only `id`, `version`, and `spec_hash` are currently visible in the confirmed schema stub.

| Field | Meaning |
|---|---|
| `id` | Canonical domain layer descriptor ID. |
| `version` | Contract/object version. |
| `spec_hash` | Normalized descriptor digest. |
| `domain` | Must resolve to `geology`. |
| `layer_id` | Stable layer identity. |
| `layer_slug` | Human-readable stable slug, if used. |
| `layer_title` | User-facing title. |
| `layer_purpose` | Public context map, evidence locator, review layer, restricted steward layer, aggregate summary, or synthetic representation. |
| `layer_class` | Bedrock, surficial, structure, boundary, borehole, well-log, sample, geophysics, geochemistry, occurrence, deposit, estimate, extraction, reclamation, cross-section, hydrostratigraphy, or mixed profile. |
| `object_family_refs` | Geology contracts/object families represented by the layer. |
| `domain_feature_identity_refs` | Identity refs for layer features where applicable. |
| `artifact_ref` | Released or candidate artifact ref. |
| `artifact_digest` | Digest binding display to artifact bytes. |
| `artifact_media_type` | PMTiles, MVT, GeoParquet, COG, JSON, image, vector tile, or accepted media type. |
| `artifact_bounds` | Public-safe bounds/envelope. |
| `crs` | Coordinate reference system / projection metadata. |
| `min_zoom` | Minimum intended zoom. |
| `max_zoom` | Maximum intended zoom. |
| `scale_warning` | Source-scale or display-scale warning. |
| `geometry_role` | Exact internal, source scale, generalized public, aggregate public, centroid public, withheld, restricted, synthetic representation, or unknown. |
| `public_exposure` | Public, public-with-caveat, restricted, withheld, review-only, steward-only, or unknown. |
| `redaction_receipt_ref` | Required when detail/geometry is generalized, redacted, downgraded, or withheld. |
| `aggregation_receipt_ref` | Required when layer is aggregate public. |
| `representation_receipt_ref` | Required for synthetic/reconstructed/3D/cross-section representation layers where material. |
| `release_ref` | ReleaseManifest / MapReleaseManifest / PromotionDecision / release candidate ref. |
| `release_state` | Candidate, review, approved, published, restricted, withdrawn, superseded, corrected, or unknown. |
| `rollback_target_ref` | Required rollback/withdrawal target for public-ready descriptors. |
| `correction_notice_ref` | Correction notice ref where applicable. |
| `supersession_ref` | Superseded-by or supersedes ref where applicable. |
| `evidence_lookup_ref` | Evidence lookup handle for features/layer support. |
| `evidence_bundle_refs` | EvidenceBundle refs behind claims. |
| `validation_report_refs` | ValidationReport refs for schema, artifact digest, geometry, policy, release, and evidence closure. |
| `catalog_refs` | STAC/DCAT/PROV/domain catalog closure refs. |
| `policy_decision_ref` | PolicyDecision governing layer exposure. |
| `sensitivity_state` | Public, generalized, restricted, withheld, source-limited, rights-limited, sensitive, or unknown. |
| `source_refs` | SourceDescriptor refs. |
| `source_roles` | Source roles represented by the layer. |
| `source_caveats` | Source scale, rights, completeness, model, administrative, or temporal caveats. |
| `attribution` | User-visible attribution text or ref. |
| `legend_ref` | Legend/style token/ref. |
| `style_ref` | StyleManifest/style token/ref. |
| `ui_warning_refs` | Warning refs that must render with the layer. |
| `allowed_interactions` | Click, hover, drawer, focus, export, download, search, inspect, none, or steward-only. |
| `denied_interactions` | Interactions explicitly denied for policy or sensitivity reasons. |
| `finite_outcome` | ANSWER, ABSTAIN, DENY, ERROR, RESTRICT, WITHHOLD_GEOMETRY, ALLOW_WITH_WARNINGS, or accepted enum. |
| `quality_flags` | Missing release, missing evidence, missing policy, missing rollback, stale, superseded, digest mismatch, geometry-role conflict, source-role conflict, restricted-detail risk. |

---

## Layer classes

| Layer class | Meaning | Default posture |
|---|---|---|
| `bedrock_public` | Bedrock geologic units/contacts as public context. | Public-with-caveats; source scale and evidence drawer required. |
| `surficial_public` | Surficial/unconsolidated geology context. | Public-with-caveats; Soil truth remains outside Geology. |
| `structure_public` | Faults/folds/lineaments/structural features. | Geology context only; not Hazards risk. |
| `boundary_version` | Released boundary/version lineage layer. | Requires version/correction/rollback support. |
| `borehole_reference` | Borehole/well reference availability. | Exact points restricted/generalized by default. |
| `well_log_reference` | Well-log/LAS availability or reference layer. | Reference-only public by default; payloads withheld unless rights-cleared. |
| `sample_or_geochemistry` | Sample/geochemistry localities or summaries. | Generalized/restricted where sensitive. |
| `geophysical_observation` | Survey footprints/products. | Public generalized unless rights/sensitivity restrict. |
| `mineral_occurrence` | Occurrence context. | Generalized/aggregate by default where sensitivity applies. |
| `resource_deposit` | Deposit context. | Restricted/generalized by default; not estimate or economic proof. |
| `resource_estimate` | Estimate/model/aggregate context. | Restricted or aggregate public; never observed truth. |
| `extraction_or_reclamation` | Extraction/reclamation context layers. | Physical/status context only; not title/permit/compliance proof. |
| `cross_section_or_3d` | Cross-section, subsurface, synthetic/reconstructed representation. | Representation/Reality Boundary receipt required where material. |
| `review_only` | Steward/review layer for candidates or restricted detail. | Not public. |
| `public_derivative` | Released public-safe layer descriptor. | Requires release, evidence, policy, catalog, artifact digest, and rollback support. |

---

## Geometry roles

| Geometry role | Meaning | Public behavior |
|---|---|---|
| `exact_internal` | Exact source/internal geometry behind trust membrane. | Never normal public path. |
| `source_scale_boundary` | Source map-scale geometry intended for context. | Public with scale warning and release support. |
| `generalized_public` | Public-safe generalized geometry. | Public only with receipt/caveat where transformed. |
| `aggregate_public` | Aggregated geography or summary. | Public only with aggregation receipt and anti-per-place caveat. |
| `centroid_public` | Public centroid or approximate location. | Must not be treated as exact. |
| `withheld` | Geometry deliberately omitted. | Layer may expose non-spatial/context metadata only. |
| `restricted` | Controlled-access geometry. | Public route must deny or return restricted outcome. |
| `synthetic_representation` | Rendered/reconstructed/synthetic display geometry. | Requires representation/reality-boundary receipt. |
| `unknown` | Geometry posture unresolved. | `ABSTAIN` or `DENY`; never public-ready. |

---

## Source-role and warning rules

Layer descriptors must carry source role and warnings into every public display.

| Condition | Required warning / behavior |
|---|---|
| Source map scale is coarse | Display scale warning; prevent over-zoom certainty. |
| Geometry is generalized | Show generalized-location warning and receipt ref. |
| Geometry is aggregate | Show aggregate-not-per-place warning. |
| Source role is administrative/regulatory | Do not style as observed physical geology. |
| Source role is modeled | Label modeled/derived; never observed. |
| Source role is candidate | No public layer unless promotion/review resolves. |
| Source role is synthetic | Show reality-boundary / representation receipt. |
| Resource estimate layer | Label as estimate/model/aggregate; never occurrence/deposit/observed truth. |
| Structure layer | Label as structural context; not Hazards risk or alert. |
| Borehole/well-log/sample layer | Restrict or generalize exact point detail by default. |
| Stale or superseded release | Show stale/superseded state and correction/rollback link. |

---

## Anti-collapse rules

```text
domain_layer_descriptor != LayerManifest schema authority
domain_layer_descriptor != ReleaseManifest
domain_layer_descriptor != EvidenceBundle
domain_layer_descriptor != PolicyDecision
domain_layer_descriptor != SourceDescriptor
domain_layer_descriptor != catalog closure
domain_layer_descriptor != map tile / artifact bytes
domain_layer_descriptor != style authority
domain_layer_descriptor != AI summary
```

Geology-specific denials:

```text
Layer != canonical GeologicUnit / Lithology / StructureFeature truth
Generalized geometry != exact geometry
Aggregate layer != per-place record
Administrative layer != observed geology
Modeled layer != observed measurement
Structure layer != Hazards risk or alert
ResourceEstimate layer != occurrence / deposit / reserve / economic proof
Borehole / WellLog / Sample layer != public exact point release
Candidate layer != public-ready layer
Synthetic layer != observed reality
```

Any layer descriptor that encourages one of these collapses must return `DENY`, `ABSTAIN`, or `ERROR` instead of a public-ready descriptor.

---

## Lifecycle

| Phase | Descriptor handling |
|---|---|
| RAW | No public layer descriptor. Source artifact, source role, and rights remain unpromoted. |
| WORK / QUARANTINE | Candidate descriptor may be assembled for review only. Public exposure is denied. |
| PROCESSED | Artifact digest, source refs, geometry role, evidence refs, and validation refs may be prepared. |
| CATALOG / TRIPLET | Catalog closure and EvidenceBundle support become resolvable. |
| RELEASE CANDIDATE | Descriptor can be evaluated with policy, receipts, warnings, rollback, and release refs. |
| PUBLISHED | Only governed API/released-artifact surfaces can expose a public-safe descriptor. |
| CORRECTED / WITHDRAWN / SUPERSEDED | Descriptor must expose correction, withdrawal, supersession, stale state, and rollback target. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `domain_layer_descriptor.schema.json` beyond `id`, `version`, and `spec_hash`.
- [ ] Decide whether this schema is a Geology profile of cross-cutting `LayerManifest` or a separate support object with references to `LayerManifest`.
- [ ] Verify or create `tools/validators/domains/geology/validate_domain_layer_descriptor.py`.
- [ ] Add valid fixtures for bedrock public, surficial public, structure public, boundary version, generalized borehole, reference-only well-log, mineral occurrence aggregate, resource estimate restricted/aggregate, cross-section representation, and public derivative cases.
- [ ] Add invalid fixtures for missing `release_ref`, missing `artifact_digest`, missing `geometry_role`, missing `evidence_lookup_ref`, missing `policy_decision_ref`, missing rollback target, digest mismatch, public exact sensitive geometry, AI-filled evidence field, candidate layer published, and generalized geometry displayed as exact.
- [ ] Add tests proving public clients consume descriptors only through governed API/released artifacts.
- [ ] Add no-network fixtures so CI can validate without live source access.
- [ ] Add non-regression tests for correction, supersession, rollback, stale-state display, source-role warning preservation, and geometry-role downgrade.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Release, artifact digest, evidence, catalog, policy, source role, geometry role, warnings, and rollback all resolve | `ANSWER` / descriptor may be served through governed API |
| Support is incomplete, stale, ambiguous, or not yet reviewed | `ABSTAIN` |
| Restricted detail would be exposed, release/policy is absent, source role is collapsed, or descriptor would mislead | `DENY` |
| Schema, validator, digest, evidence lookup, artifact read, release lookup, or policy lookup fails | `ERROR` |

---

## Evidence basis

| Evidence class | Use | Limit |
|---|---|---|
| Current repo scaffold | Confirms this target file existed as a greenfield scaffold before replacement. | Does not prove contract maturity. |
| Confirmed paired schema stub | Confirms schema path, `$id`, `x-kfm` pointers, and current minimal fields. | Does not prove field-level validation or validator implementation. |
| Geology layer-manifest package README | Confirms layer manifests are downstream carriers, require release/evidence/policy/catalog/artifact/geometry/rollback support, and must not replace trust objects. | Package implementation remains NEEDS VERIFICATION in that source. |
| Geology Map/UI contracts | Confirms renderer is not truth and cross-cutting manifest families do not live in the Geology lane. | Route/schema implementation is PROPOSED in that source. |
| Geology API contracts | Confirms governed API surfaces, finite outcomes, evidence closure, lifecycle membrane, and public-safe release-only layer manifest resolver as PROPOSED API design. | Exact routes and runtime behavior remain UNKNOWN / NEEDS VERIFICATION. |
| Geology Release Index | Confirms release index is not release authority; release decisions require ReleaseManifest with supporting artifacts. | Release artifact instances remain PROPOSED / NEEDS VERIFICATION. |
| KFM Markdown authoring role | Requires evidence-grounded, repo-ready Markdown, truth labels, and no invented implementation claims. | It is an authoring rule, not repo implementation proof. |

---

## Rollback

Rollback is required when a released or review-authorized `domain_layer_descriptor` weakens the trust membrane, hides missing support, leaks restricted geometry/payloads, or makes a layer look more authoritative than its evidence/release state allows.

Rollback triggers include:

- schema field names or descriptor/LayerManifest relationship are superseded by ADR/schema PR;
- descriptor emits without release, evidence, policy, catalog, source-role, artifact digest, geometry role, or rollback refs;
- public descriptor points at RAW/WORK/QUARANTINE, unpublished candidates, internal exact geometry, or direct source systems;
- artifact digest mismatch or stale artifact remains visible;
- generalized geometry is displayed as exact;
- aggregate layer is queried as per-place truth;
- administrative/regulatory/model/synthetic source role is styled or narrated as observed geology;
- resource layer implies occurrence/deposit/estimate/reserve/economic proof collapse;
- structure layer implies Hazards risk, alert, or life-safety guidance;
- AI text populates descriptor fields requiring evidence, policy, release, or source authority;
- public API/UI/AI consumes the descriptor outside governed release interfaces.

Rollback artifacts should include affected descriptor IDs, layer IDs, artifact refs/digests, source IDs, geometry-role refs, evidence refs, policy decisions, catalog refs, receipts, release refs, correction notices, rollback cards, replacement descriptors, and cache/style invalidation instructions.

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Is `domain_layer_descriptor` a Geology profile of cross-cutting `LayerManifest` or a separate support object that references it? | NEEDS VERIFICATION | Map/UI + schema ADR or schema PR. |
| Which fields must be required in `domain_layer_descriptor.schema.json` beyond `id`? | NEEDS VERIFICATION | Schema PR and fixture review. |
| Which canonical schema home owns cross-cutting `LayerManifest`, `StyleManifest`, `TileArtifactManifest`, and `MapReleaseManifest`? | NEEDS VERIFICATION | Map/UI schema inspection and ADR confirmation. |
| What exact finite outcome enum should this descriptor use? | NEEDS VERIFICATION | API/validator outcome contract. |
| Which geometry-role enum is canonical across Geology and map/UI surfaces? | NEEDS VERIFICATION | Policy + map schema review. |
| How should descriptors handle stale/superseded layer caches and style invalidation? | NEEDS VERIFICATION | Release/runtime/cache invalidation design. |
| Which public layer interactions are allowed for restricted Geology object families? | NEEDS VERIFICATION | Policy, UI, and fixture review. |

---

## Related contracts and docs

- `contracts/domains/geology/domain_feature_identity.md` — identity support for feature/object claims.
- `contracts/domains/geology/GeologicUnit.md` — object-family meaning for bedrock unit layers.
- `contracts/domains/geology/StructureFeature.md` — structure context; not hazards risk.
- `contracts/domains/geology/BoreholeReference.md` — restricted/generalized point context.
- `contracts/domains/geology/WellLogReference.md` — reference-only public well-log/LAS posture.
- `contracts/domains/geology/MineralOccurrence.md` — occurrence context; not deposit/estimate.
- `contracts/domains/geology/ResourceDeposit.md` — deposit body; not estimate/economic proof.
- `contracts/domains/geology/ResourceEstimate.md` — modeled/aggregate estimate; not observed truth.
- `docs/domains/geology/MAP_UI_CONTRACTS.md` — Map/UI contract profile.
- `docs/domains/geology/API_CONTRACTS.md` — governed API contract profile.
- `docs/domains/geology/RELEASE_INDEX.md` — release surface index, not release authority.
- `packages/domains/geology/layer_manifest/README.md` — implementation-helper boundary document.
- `schemas/contracts/v1/domains/geology/domain_layer_descriptor.schema.json` — confirmed schema stub, pending expansion.
- `policy/domains/geology/` — expected policy home, pending verification.
- `release/manifests/geology/` — expected release/rollback home, pending verification.

---

## Maintainer checklist

- [ ] Expand paired schema with required layer-descriptor fields.
- [ ] Decide descriptor-vs-LayerManifest relationship and record it in schema/ADR.
- [ ] Verify or create validator and fixtures referenced by the schema `x-kfm` block.
- [ ] Add anti-collapse tests for layer/truth, style/evidence, artifact/evidence, generalized/exact geometry, aggregate/per-place, source-role, structure/hazards, and resource-class failures.
- [ ] Confirm EvidenceRef/EvidenceBundle lookup is available before feature interactions and Focus Mode claims.
- [ ] Confirm public map/API/UI surfaces use only released public-safe descriptors through governed interfaces.
- [ ] Confirm correction, supersession, cache invalidation, rollback, and withdrawal behavior before promotion.
- [ ] Record unresolved descriptor/schema/map-ui/release/geometry-role drift in `docs/registers/DRIFT_REGISTER.md`.

[Back to top](#top)
