<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-hazards-domain-layer-descriptor
title: Domain Layer Descriptor Contract — Hazards
type: semantic-contract
version: v0.2
status: draft; PROPOSED; CONFLICTED schema-home/path form; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Governed API steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-22
updated: 2026-06-22
policy_label: public-with-gates; semantic-contract; hazards; layer-descriptor; map-ui-profile; not-for-life-safety; source-role-aware; stale-aware; evidence-bound; release-gated; rollback-aware
tags: [kfm, contracts, hazards, domain_layer_descriptor, layer-descriptor, layer-manifest, map-ui, maplibre, evidence-drawer, not-for-life-safety, official-source-referral, source-role, stale-state, expiry, release-manifest, rollback, correction, anti-collapse]
related:
  - ./README.md
  - ./domain_feature_identity.md
  - ./domain_validation_report.md
  - ./hazards_decision_envelope.md
  - ../../../docs/domains/hazards/README.md
  - ../../../docs/domains/hazards/API_CONTRACTS.md
  - ../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md
  - ../../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hazards/IDENTITY_MODEL.md
  - ../../../docs/domains/hazards/CANONICAL_PATHS.md
  - ../../../docs/architecture/hazards-trust-membrane.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json
  - ../../../policy/domains/hazards/
  - ../../../fixtures/domains/hazards/domain_layer_descriptor/
  - ../../../tests/domains/hazards/test_domain_layer_descriptor.*
  - ../../../data/registry/sources/hazards/
  - ../../../release/manifests/
notes:
  - "Expanded from a thin scaffold at contracts/domains/hazards/domain_layer_descriptor.md."
  - "The paired schema exists at schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json, but remains a PROPOSED scaffold with only spec_hash, id, and version fields plus additionalProperties=true."
  - "CONFLICTED path form: current mounted repo evidence uses contracts/domains/hazards/ and schemas/contracts/v1/domains/hazards/, while docs/domains/hazards/CANONICAL_PATHS.md argues for flat contracts/hazards/ and schemas/contracts/v1/hazards/ pending ADR-S-01 / ADR-0001. This file follows the mounted target path and preserves the conflict."
  - "Hazards layer descriptors are downstream delivery-support objects. They are not source truth, not EvidenceBundle proof, not ReleaseManifest authority, not emergency-alert authority, and not life-safety instructions."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Domain Layer Descriptor Contract — Hazards

> Semantic contract for `domain_layer_descriptor`: the Hazards profile that describes a released or release-candidate map/UI layer's purpose, artifact binding, source-role posture, evidence lookup, policy/release state, not-for-life-safety disclaimer obligations, stale/expiry behavior, correction state, and rollback target without turning the layer into source truth or emergency guidance.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts%2F-0a7ea4">
  <img alt="Domain: Hazards" src="https://img.shields.io/badge/domain-Hazards%20%5BDOM--HAZ%5D-orange">
  <img alt="Object: domain_layer_descriptor" src="https://img.shields.io/badge/object-domain__layer__descriptor-blue">
  <img alt="Boundary: layer not truth" src="https://img.shields.io/badge/boundary-layer__not__truth-critical">
  <img alt="Alert authority: never" src="https://img.shields.io/badge/alert__authority-never-critical">
  <img alt="Schema: scaffold" src="https://img.shields.io/badge/schema-scaffold%20%2F%20NEEDS__VERIFICATION-orange">
</p>

`contracts/domains/hazards/domain_layer_descriptor.md`

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema posture](#schema-posture) · [Path conflict](#path-conflict) · [Layer descriptor vs trust objects](#layer-descriptor-vs-trust-objects) · [Assertions](#assertions) · [Exclusions](#exclusions) · [Recommended fields](#recommended-fields) · [Layer classes](#layer-classes) · [Hazards display obligations](#hazards-display-obligations) · [Lifecycle](#lifecycle) · [Validation](#validation) · [Rollback](#rollback) · [Evidence basis](#evidence-basis) · [Open questions](#open-questions)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / semantic contract  
> **Contract path:** `contracts/domains/hazards/domain_layer_descriptor.md`  
> **Schema path:** `schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json`  
> **Schema posture:** paired schema exists, but remains a `PROPOSED` scaffold with only `spec_hash`, `id`, and `version` visible and `additionalProperties: true`.  
> **Truth posture:** Hazards publication and API doctrine define strong layer/public-surface obligations, but route names, field-level schema shape, validator enforcement, fixtures, policy runtime, UI behavior, release artifacts, and CI/test coverage remain **NEEDS VERIFICATION**.

> [!CAUTION]
> A Hazards layer descriptor is not a warning, not a source feed, not a proof object, not a release decision, not a policy decision, not a live alert, and not life-safety advice. It is a bounded descriptor for public-safe delivery through governed surfaces.

---

## Meaning

`domain_layer_descriptor` records the Hazards-specific semantics a public map, Evidence Drawer, API payload, Focus Mode card, export, or report needs in order to display a Hazards layer without weakening KFM's trust membrane.

It answers:

- Which Hazards layer is being described?
- Which released or release-candidate artifact may be exposed through a governed API?
- Which source roles are present: observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, or unresolved?
- Does the layer include operational warning/advisory/watch context, and if so, are issue/expiry/freshness and `not_for_life_safety` obligations visible?
- Which EvidenceRefs, EvidenceBundles, SourceDescriptors, PolicyDecisions, ReleaseManifest, CorrectionNotice, and RollbackCard support the layer?
- Which UI behaviors are allowed: visible layer, click-to-evidence, time slider, drawer detail, Focus Mode context, export, or denied interaction?

A layer descriptor is a delivery-support object. It can help a client load a released layer safely. It must never become the canonical Hazards object, the source authority, the evidence bundle, the release approval, or the user's safety instruction.

---

## Repo fit

| Responsibility | Path or root | This contract's role |
|---|---|---|
| Human-readable layer meaning | `contracts/domains/hazards/domain_layer_descriptor.md` | This file; semantic contract for Hazards layer descriptors. |
| Machine schema | `schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json` | CONFIRMED scaffold; field-level shape still thin. |
| Hazards API doctrine | `docs/domains/hazards/API_CONTRACTS.md` | Defines layer manifest resolver, Evidence Drawer payload, Focus Mode envelope, and finite outcomes. |
| Publication boundary | `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` | Defines publishable families, release gates, UI/public boundaries, expiry/stale rules, and deny register. |
| Hazards domain doctrine | `docs/domains/hazards/README.md` | Defines object families, source-role anti-collapse, validation, AI, publication/rollback posture. |
| Identity contract | `contracts/domains/hazards/domain_feature_identity.md` | Stable IDs and role/time/geography identity support. |
| Decision envelope | `contracts/domains/hazards/hazards_decision_envelope.md` | Planned bounded runtime envelope; currently scaffold unless separately expanded. |
| Trust membrane | `docs/architecture/hazards-trust-membrane.md` | Defines never-alert-authority posture, official-source deferral, and no imperative UI language. |
| Source registry | `data/registry/sources/hazards/` | Expected SourceDescriptor and activation records; implementation NEEDS VERIFICATION. |
| Policy | `policy/domains/hazards/` and possibly `policy/release/hazards/` | Expected layer allow/deny/restrict/abstain and life-safety gates. |
| Release | `release/` | ReleaseManifest, CorrectionNotice, RollbackCard, PromotionDecision. |

---

## Schema posture

| Schema fact | Current posture |
|---|---|
| Confirmed schema path | `schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json` |
| Schema status | `PROPOSED` |
| Schema title | `domain_layer_descriptor` |
| Visible properties | `spec_hash`, `id`, `version` |
| Required fields | `id` only |
| Additional properties | `true` |
| Contract pointer | `contracts/domains/hazards/domain_layer_descriptor.md` |
| Fixtures root | `fixtures/domains/hazards/domain_layer_descriptor/` |
| Validator pointer | `tools/validators/domains/hazards/validate_domain_layer_descriptor.py` |
| Policy pointer | `policy/domains/hazards/` |
| Field-level enforcement | NEEDS VERIFICATION |

This means the Markdown contract defines intended semantics, while the schema does not yet enforce the full layer descriptor tuple.

---

## Path conflict

> [!WARNING]
> **CONFLICTED / NEEDS VERIFICATION:** current mounted repo evidence uses `contracts/domains/hazards/` and `schemas/contracts/v1/domains/hazards/`, while `docs/domains/hazards/CANONICAL_PATHS.md` argues the canonical Hazards crosswalk should be the flat `contracts/hazards/` and `schemas/contracts/v1/hazards/` form pending ADR-S-01 / ADR-0001. This file follows the user's requested mounted path and paired schema pointer. It does not resolve the ADR.

Do not create a second `contracts/hazards/domain_layer_descriptor.md` without a migration note or ADR. Doing so would create parallel contract authority.

---

## Layer descriptor vs trust objects

| Object / artifact | What it owns | Boundary |
|---|---|---|
| `domain_layer_descriptor` | Hazards layer purpose, artifact linkage, disclaimers, interaction limits, and public-delivery posture. | This contract. |
| `LayerManifest` | Cross-cutting layer manifest payload for released layer serving. | Layer descriptor profiles it; does not redefine it. |
| `EvidenceBundle` | Admissible evidence support. | Descriptor cites it; descriptor is not proof. |
| `PolicyDecision` | Allow/restrict/deny/abstain for exposure. | Descriptor cites it; descriptor does not decide policy. |
| `ReleaseManifest` | Publication authority and rollback target. | Required before public `ANSWER`; descriptor does not publish. |
| `CorrectionNotice` | Correction/supersession notice. | Descriptor must expose correction state where material. |
| `SourceDescriptor` | Source authority, rights, role, cadence, citation. | Descriptor must cite source role and authority limits. |
| `HazardsDecisionEnvelope` | Runtime finite-outcome envelope. | Descriptor supports layer surface; envelope answers requests. |
| Evidence Drawer payload | UI projection of evidence, caveats, policy, release, correction. | Descriptor must make drawer resolution possible. |
| Map tiles / styles | Delivery artifacts. | Never evidence, proof, release, or source truth. |

---

## Assertions

A reviewed `domain_layer_descriptor` should assert:

1. **Layer identity** — stable descriptor ID, layer ID, domain, version, layer class, and `spec_hash`.
2. **Artifact binding** — released artifact refs, digests, media type, bounds, CRS, temporal extent, zoom/render envelope, and public-safe flag.
3. **Source-role binding** — source roles and hazards knowledge-character labels for layer contents remain visible and do not collapse.
4. **Evidence binding** — EvidenceRefs/EvidenceBundles are resolvable for feature claims and drawer inspection.
5. **Policy binding** — PolicyDecision refs and sensitivity/restriction state travel with the descriptor.
6. **Release binding** — ReleaseManifest, release state, correction path, supersession state, rollback target, and cache invalidation expectations exist before public serving.
7. **Temporal posture** — issue/expiry, event/observed, valid, source, retrieval, release, correction, and stale state are not collapsed.
8. **Operational boundary** — operational warning/advisory/watch context never displays as KFM current authority or instruction.
9. **Display obligations** — not-for-life-safety disclaimer, official-source referral, source-vintage/freshness labels, source-role badges, and correction/stale markers are present where required.
10. **Finite outcomes** — layer resolving can return only governed outcomes such as `ANSWER`, `DENY`, or `ERROR`; feature/drawer/focus surfaces carry their own finite outcomes.

---

## Exclusions

| Misuse | Why it is denied or abstained |
|---|---|
| Layer descriptor as source truth | SourceDescriptor and source payloads own source authority. |
| Layer descriptor as evidence proof | EvidenceBundle/proof support remains separate. |
| Layer descriptor as release authority | ReleaseManifest/PromotionDecision owns publication. |
| Layer descriptor as policy decision | Policy bundles decide allow/restrict/deny/abstain. |
| Tile URL as public release | Tile artifacts require release, digest, policy, and rollback refs. |
| UI style as redaction or disclaimer | Style is delivery; policy/disclaimer must be explicit data/contract state. |
| Warning layer as active safety alert | KFM is never an alert authority. |
| Expired warning rendered current | Expiry/stale-state denial applies. |
| Regulatory flood layer as observed flood | Source-role collapse. |
| Modeled smoke/drought layer as observation | Model-vs-observation collapse. |
| Candidate layer public serving | WORK/QUARANTINE/CATALOG candidates cannot be public layers. |
| AI/focus answer inferred from layer alone | AI answers require released EvidenceBundle support and AIReceipt. |

---

## Recommended fields

The following fields are **PROPOSED** targets for future schema expansion. They are not enforced by the confirmed scaffold schema.

| Field | Meaning |
|---|---|
| `id` | Canonical Hazards layer descriptor ID. |
| `version` | Contract/object version. |
| `spec_hash` | Deterministic hash over normalized layer descriptor semantics. |
| `domain` | Must resolve to `hazards`. |
| `layer_id` | Stable public or release-candidate layer identifier. |
| `layer_class` | hazard_event, warning_context, advisory_context, regulatory_context, detection, modeled_context, aggregate_summary, exposure, resilience, timeline, impact_area, or accepted enum. |
| `artifact_refs` | Released artifact refs such as PMTiles, vector tiles, COG, GeoParquet, API layer payload, or summary card artifact. |
| `artifact_digests` | Content digests for layer artifacts. |
| `source_descriptor_refs` | Source identity, role, rights, cadence, authority, citation. |
| `source_role_summary` | Role set present in the layer. |
| `knowledge_character_summary` | Hazards-specific labels present in the layer. |
| `temporal_extent` | Event/observed/valid/issue/expiry range and public time-slider bounds. |
| `freshness_state` | current, historical, expired_operational_context, stale_source, superseded, unknown, or accepted enum. |
| `not_for_life_safety` | Required marker for operational or public Hazards layers. |
| `official_source_referral` | Official-source link/reference or source family referral. |
| `evidence_ref_ids` | EvidenceRefs available for feature/drawer resolution. |
| `evidence_bundle_ids` | Resolved or release-bound EvidenceBundle IDs. |
| `policy_decision_refs` | Policy decisions controlling exposure. |
| `release_ref` | ReleaseManifest/PromotionDecision ref. |
| `correction_refs` | CorrectionNotice/supersession refs. |
| `rollback_refs` | RollbackCard/rollback target refs. |
| `ui_warning_obligations` | Badges/caveats/disclaimers/legend warnings required in public UI. |
| `interaction_policy` | Allowed interactions: view, click, drawer, focus_context, export, download, denied. |
| `quality_flags` | Missing evidence, missing release, stale source, expired operational context, unresolved source role, restricted geometry, direct-source risk. |

---

## Layer classes

| Layer class | Publishable posture | Required display behavior |
|---|---|---|
| `hazard_event` | Historical event context. | Evidence/citation, event time, source role. |
| `hazard_observation` | Observation layer. | Observation ≠ authority; freshness visible. |
| `warning_context` / `advisory_context` | Historical/operational context only. | `not_for_life_safety`, issue/expiry, freshness, official-source referral. |
| `regulatory_context` | Regulatory layer, such as NFHL. | Regulatory badge; never observed inundation or forecast. |
| `remote_sensing_detection` | Detection layer. | Detection ≠ confirmation; sensor/source/vintage/confidence. |
| `modeled_context` | Modeled derivative. | Model/run/uncertainty badge; never observation. |
| `aggregate_summary` | Aggregate/rollup. | Aggregation unit/window; never per-place truth. |
| `exposure_summary` / `resilience_summary` | Aggregate or model-derived public-safe rollup. | Upstream sensitivity tier check; infrastructure detail denied/restricted. |
| `hazard_timeline` | Time-aware derivative. | Member roles preserved; operational items retain expiry. |
| `impact_area` | Impact polygon or derivative geometry. | Input-tier check; geometry/exposure role visible. |

---

## Hazards display obligations

Every public Hazards layer descriptor must make the following obligations machine-inspectable before a public client can render it as `ANSWER`:

- `not_for_life_safety` marker where operational or public Hazards context is present;
- official-source referral for warning/advisory/watch or current-safety-adjacent contexts;
- source-role badges preserving observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic distinctions;
- issue/expiry/freshness/stale state where operational context is present;
- Evidence Drawer link or reason why drawer access is denied;
- released artifact digest and ReleaseManifest reference;
- policy/restriction and public-safe geometry posture;
- correction/supersession state and rollback target;
- denial reason when a layer cannot be served.

> [!IMPORTANT]
> A layer that cannot supply these obligations may still be useful internally, but it is not public-ready. It must remain in WORK, QUARANTINE, PROCESSED, CATALOG, or release-candidate HOLD state rather than silently entering a public map.

---

## Lifecycle

| Phase | Layer descriptor handling |
|---|---|
| RAW | Source layer metadata, source role, source refs, source time, issue/expiry, rights, sensitivity, and artifact refs are captured but not public. |
| WORK / QUARANTINE | Candidate layer descriptors are normalized; missing source role, missing evidence, missing disclaimer, missing expiry, rights gaps, and source-role collapse are held or denied. |
| PROCESSED | Descriptor binds candidate artifacts, digests, temporal extent, source-role summary, EvidenceRefs, validation results, and policy posture. |
| CATALOG / TRIPLET | Descriptor can support catalog/discovery and evidence projection, but remains non-public until release closure. |
| RELEASE CANDIDATE | Public-safe descriptor must resolve ReleaseManifest, EvidenceBundle, PolicyDecision, correction path, and rollback target. |
| PUBLISHED | Governed API serves descriptor-backed layer manifests to public UI; public clients do not read raw/source/internal stores. |
| CORRECTED / SUPERSEDED | Source refresh, stale state, expiry, upstream correction, artifact digest change, policy change, or release withdrawal updates descriptor and linked release/correction/rollback objects. |

---

## Validation

Before this contract is promoted beyond draft:

- [ ] Expand `schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json` beyond the three visible scaffold fields.
- [ ] Resolve the flat-vs-`domains/` path conflict or record an accepted compatibility rule.
- [ ] Define canonical `layer_class`, `freshness_state`, `interaction_policy`, `not_for_life_safety`, and `official_source_referral` field names.
- [ ] Add positive fixtures for historical event, NFHL regulatory context, earthquake event, remote-sensing detection, modeled smoke, drought indicator, exposure summary, and expired historical warning context.
- [ ] Add negative fixtures for layer without ReleaseManifest, direct source endpoint, missing disclaimer, expired warning-as-current, NFHL-as-observed, model-as-observed, aggregate-as-per-place, candidate-as-public, missing EvidenceBundle, and missing rollback target.
- [ ] Add validator coverage for artifact digest, source role, issue/expiry, stale state, release refs, evidence refs, policy refs, correction refs, rollback refs, public-safe geometry, and official-source referral.
- [ ] Confirm layer manifest resolver returns `ANSWER`, `DENY`, or `ERROR` only, and denies any layer without a release manifest.
- [ ] Confirm Evidence Drawer and Focus Mode surfaces preserve source roles and not-for-life-safety posture.

Recommended finite outcomes:

| Condition | Outcome |
|---|---|
| Released layer descriptor resolves artifact, evidence, policy, release, correction, rollback, disclaimer, and source-role support | `ANSWER` |
| Layer is unreleased, missing release/evidence/disclaimer, or blocked by policy | `DENY` |
| Layer query malformed or descriptor cannot be evaluated due to schema/runtime failure | `ERROR` |
| Feature/drawer/focus query has insufficient evidence or stale context | `ABSTAIN` on that surface, not layer manifest resolver |

---

## Rollback

Rollback is required when a Hazards layer descriptor weakens the trust membrane, source-role separation, life-safety boundary, evidence closure, release governance, or public-safe display obligations.

Rollback triggers include layer served without ReleaseManifest; missing rollback target; missing not-for-life-safety disclaimer; missing official-source referral; warning/advisory shown current after expiry; regulatory context rendered as observed event; modeled derivative rendered as observation; aggregate rendered as per-place truth; candidate layer exposed publicly; tile/style used as redaction; public UI reads source endpoint directly; AI/Focus Mode answers from layer without EvidenceBundle; artifact digest mismatch; source refresh/stale-state change; policy/release withdrawal; or path migration causing descriptor/schema mismatch.

Rollback artifacts should include affected layer IDs, descriptor IDs, artifact refs/digests, source descriptors, source-role summaries, EvidenceRefs/EvidenceBundles, validation reports, policy decisions, release manifests, correction notices, rollback cards, replacement descriptors, invalidated tiles/styles/caches, and public UI cache invalidation instructions.

---

## Evidence basis

| Source | Status | Supports | Limits |
|---|---|---|---|
| `contracts/domains/hazards/domain_layer_descriptor.md` scaffold | CONFIRMED | Target existed as a greenfield scaffold. | Did not contain authoritative layer semantics. |
| `schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json` | CONFIRMED | Schema pointer, current scaffold fields, fixtures/validator/policy pointers. | Does not enforce full layer descriptor semantics. |
| `docs/domains/hazards/API_CONTRACTS.md` | CONFIRMED | Layer manifest resolver, Evidence Drawer, Focus Mode, finite outcomes, not-for-life-safety API posture. | Many DTO/route shapes remain PROPOSED / NEEDS VERIFICATION. |
| `docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md` | CONFIRMED | Publishable layer families, governed publication path, UI obligations, expiry/stale rules, deny register, validators. | It states many route/policy paths as PROPOSED where implementation was not proven. |
| `docs/domains/hazards/README.md` | CONFIRMED | Source-role anti-collapse, validator expectations, governed AI, publication/correction/rollback, risks. | Some implementation claims remain verification-bound. |
| `docs/domains/hazards/CANONICAL_PATHS.md` | CONFIRMED | Path-law doctrine and flat-vs-segment conflict. | Conflicts with mounted `contracts/domains/` and `schemas/contracts/v1/domains/` paths for this file/schema. |
| `docs/architecture/hazards-trust-membrane.md` | CONFIRMED | Never-alert-authority boundary, official-source deferral, no imperative UI language, source-role vocabulary. | Architecture note marks some path claims as proposed. |
| `contracts/domains/geology/domain_layer_descriptor.md` | CONFIRMED | Adjacent expanded contract pattern for layer-descriptor structure and downstream-carrier boundary. | Geology-specific semantics do not transfer directly to Hazards. |
| User-provided authoring role | CONFIRMED user instruction | Requires evidence-grounded, repo-ready Markdown and visible verification boundaries. | Authoring rule, not implementation proof. |

---

## Open questions

| Question | Status | Resolution path |
|---|---|---|
| Should Hazards contracts/schemas ultimately use flat `contracts/hazards/` and `schemas/contracts/v1/hazards/` or current mounted `contracts/domains/hazards/` and `schemas/contracts/v1/domains/hazards/`? | CONFLICTED / NEEDS VERIFICATION | ADR-S-01 / ADR-0001 / migration note. |
| Which fields must be required in `domain_layer_descriptor.schema.json`? | NEEDS VERIFICATION | Schema PR with valid/invalid fixtures. |
| Which layer classes and freshness-state values are canonical? | NEEDS VERIFICATION | Contract/schema/policy review. |
| Is the Hazards life-safety disclaimer required on every Hazards layer or only operational-context layers? | NEEDS VERIFICATION | Policy and UI review; safer default is every public Hazards surface. |
| Which validator proves public UI never reads NWS/FIRMS/NFHL/OpenFEMA directly? | NEEDS VERIFICATION | UI/governed API tests. |
| Where should layer manifest schemas live: runtime cross-cutting home, hazards schema home, or both via profile? | NEEDS VERIFICATION | Schema/Map/UI ADR review. |

---

## Related contracts and docs

- [`./README.md`](./README.md) — Hazards contract-root README.
- [`./domain_feature_identity.md`](./domain_feature_identity.md) — Hazards feature identity contract.
- [`./domain_validation_report.md`](./domain_validation_report.md) — planned validation-report contract scaffold.
- [`./hazards_decision_envelope.md`](./hazards_decision_envelope.md) — planned bounded runtime envelope scaffold.
- [`../../../docs/domains/hazards/API_CONTRACTS.md`](../../../docs/domains/hazards/API_CONTRACTS.md) — governed API surfaces and layer manifest resolver doctrine.
- [`../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md`](../../../docs/domains/hazards/PUBLICATION_AND_BOUNDARY.md) — publication and not-for-life-safety boundary.
- [`../../../docs/domains/hazards/README.md`](../../../docs/domains/hazards/README.md) — Hazards domain operating doctrine.
- [`../../../docs/domains/hazards/CANONICAL_PATHS.md`](../../../docs/domains/hazards/CANONICAL_PATHS.md) — canonical path map and path conflict.
- [`../../../docs/architecture/hazards-trust-membrane.md`](../../../docs/architecture/hazards-trust-membrane.md) — hazards trust-membrane architecture note.
- [`../../../schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json`](../../../schemas/contracts/v1/domains/hazards/domain_layer_descriptor.schema.json) — confirmed scaffold schema, pending expansion.

[Back to top](#top)
