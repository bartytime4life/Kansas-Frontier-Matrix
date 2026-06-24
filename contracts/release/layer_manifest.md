<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-layer-manifest
title: contracts/release/layer_manifest.md — Release LayerManifest Bridge Contract
type: contract
version: v0.2
status: draft; PROPOSED; compatibility-bridge; release-aware; schema-home-unresolved
owners: OWNER_TBD — Release steward · Layer steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Map/UI steward · Rollback steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; layer-manifest; compatibility-bridge; release-gated; map-aware; evidence-aware; rollback-aware; no-parallel-authority
tags: [kfm, contracts, release, layer-manifest, release-manifest, map-layer, layer-payload, bridge-contract, schema-home-unresolved, release-gated, rollback-aware, no-parallel-authority]
related:
  - ./README.md
  - ./release_manifest.md
  - ./promotion_decision.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
  - ../data/layer_manifest.md
  - ../data/layer_descriptor.md
  - ../data/layer_catalog_item.md
  - ../map/layer_manifest/README.md
  - ../../schemas/contracts/v1/data/layer_manifest.schema.json
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../policy/release/
  - ../../policy/data/
  - ../../release/
  - ../../data/registry/layers/
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../docs/architecture/release-discipline.md
  - ../../docs/standards/RELEASE_MANIFEST.md
notes:
  - "Expanded from a scaffold created from a domain-document inventory reference."
  - "The inspected canonical LayerManifest semantic contract currently lives at `contracts/data/layer_manifest.md`."
  - "This release-lane file is a compatibility bridge for release inclusion semantics; it must not duplicate or supersede the canonical data-layer LayerManifest contract."
  - "No `schemas/contracts/v1/release/layer_manifest.schema.json` was verified in this session; schema home remains NEEDS VERIFICATION."
  - "This contract does not store release artifacts, tiles, PMTiles/COG files, manifests, proofs, receipts, public API payloads, UI state, or AI output."
  - "Rollback target for this expansion is previous blob SHA `472a4fcc061493494791cdad51c224bc9b153566`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Release LayerManifest Bridge Contract

> Semantic bridge for `LayerManifest` when a layer payload participates in a release. The canonical inspected layer-manifest meaning is [`../data/layer_manifest.md`](../data/layer_manifest.md). This release-lane contract only explains how a governed layer manifest relates to `ReleaseManifest`, promotion, rollback, correction, and publication gates.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: release bridge" src="https://img.shields.io/badge/family-release__bridge-0a7ea4">
  <img alt="Layer authority: data contract" src="https://img.shields.io/badge/layer__authority-data__contract-blueviolet">
  <img alt="Schema: unresolved" src="https://img.shields.io/badge/schema-unresolved-orange">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
</p>

**Status:** draft / PROPOSED / compatibility bridge  
**Path:** `contracts/release/layer_manifest.md`  
**Canonical inspected layer contract:** [`../data/layer_manifest.md`](../data/layer_manifest.md)  
**Release manifest companion:** [`./release_manifest.md`](./release_manifest.md)  
**Current inspected layer schema:** `schemas/contracts/v1/data/layer_manifest.schema.json`  
**Release-lane layer schema:** NEEDS VERIFICATION — no verified `schemas/contracts/v1/release/layer_manifest.schema.json` in this session  
**Policy authority:** `policy/release/`, `policy/data/`, and sensitivity/rights policy roots, not this contract  
**Release artifact authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED target scaffold replaced · CONFIRMED inspected canonical data-layer contract exists · CONFIRMED release README allows release semantic contracts but not release artifacts · PROPOSED release-bridge semantics until ADR/schema/fixture/validator/release integration resolves placement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Boundary with data LayerManifest](#boundary-with-data-layermanifest) · [Release-facing semantics](#release-facing-semantics) · [Proposed fields](#proposed-fields) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Exclusions](#exclusions) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`contracts/release/layer_manifest.md` defines the release-side meaning of a layer manifest when a map layer payload is included in, withheld from, superseded by, or rolled back within a KFM release.

It answers release-facing questions:

- Which canonical `LayerManifest` is being considered for release?
- Which `ReleaseManifest` includes or references it?
- Which layer artifact digests, tile archives, style dependencies, or renderer-facing descriptors are in scope?
- What evidence, rights, sensitivity, policy, review, and rollback posture applies at publication time?
- What changes when the released layer is corrected, superseded, withdrawn, or rolled back?

It does **not** define the full canonical layer manifest object. That meaning is already inspected under `contracts/data/layer_manifest.md`.

---

## Meaning

A release-side `LayerManifest` bridge is the release relationship between a governed versioned layer manifest and the release package that may expose it to public or restricted clients.

It is release-aware context, not layer truth by itself.

It may be used to record:

- a `LayerManifest` reference included in a `ReleaseManifest`;
- release-time artifact digests for tile payloads, PMTiles, COGs, sprites, glyphs, style fragments, or sidecars;
- release eligibility status for map/UI exposure;
- sensitivity and rights posture at the time of release;
- rollback target for the published layer representation;
- correction or supersession lineage when a layer release changes.

A release-side layer manifest must not bypass the canonical layer contract, the release manifest, promotion decisions, policy decisions, review records, evidence bundles, proofs, receipts, or release gates.

---

## Repo fit

| Responsibility | Correct home | Relationship to this contract |
|---|---|---|
| Canonical layer manifest meaning | `contracts/data/layer_manifest.md` | Inspected canonical layer semantic contract. |
| Release-side layer inclusion semantics | `contracts/release/layer_manifest.md` | This bridge contract; PROPOSED until placement is resolved. |
| Release manifest meaning | `contracts/release/release_manifest.md` | Release package object that may include layer manifests. |
| Promotion decision meaning | `contracts/release/promotion_decision.md` | Approve/deny/abstain decision for state transition. |
| Rollback target semantics | `contracts/release/rollback_card.md` | Rollback object; currently scaffold-level. |
| Layer descriptor/catalog companions | `contracts/data/layer_descriptor.md`, `contracts/data/layer_catalog_item.md` | Renderer/discovery companions; do not replace LayerManifest. |
| Machine shape | `schemas/contracts/v1/data/layer_manifest.schema.json` currently inspected; release schema unresolved | Shape authority remains schemas, not this file. |
| Release policy | `policy/release/`, `policy/data/`, sensitivity/rights policy roots | Admissibility and gate authority. |
| Release artifacts | `release/` | Stores release records/artifacts, not contracts. |
| Layer registry/catalog | `data/registry/layers/`, `data/catalog/` or accepted homes | Layer lookup/discovery state. |
| Proofs and receipts | `data/proofs/`, `data/receipts/` or accepted homes | Auditable trust artifacts. |
| Public surfaces | governed API/UI/map/AI roots | Downstream consumers only. |

---

## Boundary with data LayerManifest

The inspected `contracts/data/layer_manifest.md` contract defines `LayerManifest` as the governed manifest for a versioned layer payload, binding identity, data lineage, evidence posture, integrity references, valid time, freshness, source roles, rights, sensitivity, policy posture, review state, release relationship, correction, supersession, and rollback lineage.

This release-lane contract must therefore stay narrower:

| Question | Canonical data-layer contract | Release bridge contract |
|---|---|---|
| What is a layer manifest? | `contracts/data/layer_manifest.md` | Points back to data contract. |
| What data/source/evidence/freshness context defines the layer? | `contracts/data/layer_manifest.md` | References the approved manifest state. |
| Which release includes this layer? | Release bridge + `release_manifest.md` | In scope. |
| Which tile/archive artifacts were published? | Release bridge + release artifact records | In scope as references/digests, not payloads. |
| What rollback target applies to this released layer? | Both, depending on lifecycle scope | Release-specific rollback relation in scope. |
| Does this bridge approve publication? | No | No; release gates and policy decide. |

> [!IMPORTANT]
> If a maintainer changes the meaning of `LayerManifest`, change [`../data/layer_manifest.md`](../data/layer_manifest.md), not this release bridge. This file only defines release-facing relationships.

---

## Release-facing semantics

A release-side layer manifest bridge SHOULD identify or reference:

- the canonical layer manifest id/ref;
- the release id/ref that includes or evaluates the layer;
- the artifact set included in the release, by digest/ref only;
- the source EvidenceBundle refs needed for public layer claims;
- policy decision refs for release, render, sensitivity, rights, export, and AI interaction where applicable;
- sensitivity labels and redaction/generalization state at release time;
- rights/license/export posture at release time;
- review state and release authority;
- rollback target and correction/supersession lineage;
- valid time, publish time, superseded time, and stale/degraded flags where applicable.

---

## Proposed fields

No release-specific schema was verified in this session. These fields are therefore PROPOSED semantic targets only:

| Field | Meaning | Required posture |
|---|---|---|
| `release_layer_manifest_id` | Stable id for this release-layer bridge object. | Deterministic where practical. |
| `layer_manifest_ref` | Ref to canonical `LayerManifest`. | Must resolve before release. |
| `release_manifest_ref` | Ref to the containing `ReleaseManifest`. | Must resolve for PUBLISHED release use. |
| `artifact_refs` | Tile/archive/style/glyph/sprite/sidecar refs or digests. | Digest/ref only; no payload storage. |
| `evidence_refs` | Evidence refs supporting release-visible claims. | Must resolve to EvidenceBundle where claims depend on evidence. |
| `policy_decision_refs` | Policy decisions for release/render/sensitivity/rights. | Must include gate-relevant decisions. |
| `sensitivity_label_refs` | Sensitivity posture applied to layer or artifacts. | Fail closed when unresolved. |
| `rights_refs` | Rights/license/terms refs. | Unknown rights block or restrict release. |
| `review_refs` | ReviewRecord/steward approval refs. | Required for material/sensitive release. |
| `rollback_target_ref` | Prior release/layer target for rollback. | Required unless explicitly waived with reason. |
| `correction_lineage_refs` | Corrections/supersessions/withdrawals. | Must preserve public audit trail. |
| `release_state` | candidate, held, released, superseded, withdrawn, rolled_back, stale. | Finite state recommended. |
| `evaluated_at` | Time this bridge was evaluated for release. | UTC/date-time recommended. |

---

## Invariants

PROPOSED semantic invariants:

- A release-side layer manifest bridge must point to a canonical layer manifest; it must not duplicate it.
- It must not store tile/archive payloads, release artifacts, proofs, receipts, or public render state.
- Public release requires a `ReleaseManifest`, release policy decision, evidence closure, rights/sensitivity checks, review where required, and rollback target.
- A layer can be catalog-visible without being public-release-safe.
- A public map/UI/client must not read RAW, WORK, QUARANTINE, unpublished candidates, canonical/internal stores, or direct model output through this bridge.
- Sensitive geometry, rare-species locations, archaeology, living-person/DNA-derived joins, infrastructure risks, and rights-uncertain layers fail closed unless redacted/generalized/restricted by policy.
- Supersession and rollback must preserve prior release references and correction lineage.
- If the canonical layer manifest changes materially, a new release-side bridge or supersession must be emitted rather than silently mutating the old release relationship.

---

## Lifecycle role

This bridge participates only at governed release-facing boundaries:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical use:

| Lifecycle point | Role of this bridge |
|---|---|
| PROCESSED → CATALOG/TRIPLET | May remain absent; layer can be prepared without release inclusion. |
| CATALOG/TRIPLET → PUBLISHED | Binds the canonical layer manifest to release eligibility and artifact refs. |
| PUBLISHED → PUBLISHED′ correction | Links correction notice and superseding layer/release state. |
| PUBLISHED → prior release rollback | Identifies layer-specific rollback target and invalidation path. |
| PUBLISHED → withdrawn | Preserves withdrawal notice and public-safe explanation. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Canonical full LayerManifest meaning | `contracts/data/layer_manifest.md` | Avoids duplicate layer authority. |
| JSON Schema | `schemas/contracts/v1/...` accepted schema home | Schemas own machine shape. |
| Release manifest JSON instances | `release/` or accepted release artifact roots | Contracts do not store release records. |
| Tile archives, PMTiles, COGs, sprites, glyphs, styles | `release/`, lifecycle artifact roots, or accepted artifact stores | Payloads are artifacts, not contract prose. |
| Proofs, receipts, attestations, signatures | `data/proofs/`, `data/receipts/`, signing/release roots | Trust artifacts remain separately auditable. |
| Rego/OPA/equivalent policy rules | `policy/release/`, `policy/data/`, sensitivity/rights roots | Policy owns admissibility. |
| Runtime renderer code or MapLibre UI | `apps/`, `ui/`, `web/`, packages | Public/render surfaces are downstream. |
| AI summaries or direct model outputs | Governed AI envelopes with evidence/policy/release checks | AI is interpretive, not release authority. |

---

## Validation expectations

NEEDS VERIFICATION before treating this bridge as canonical:

- accepted home decision: keep release bridge here, move to `contracts/data/`, move to `contracts/layers/`, or replace with a README pointer;
- schema home decision and paired schema creation or compatibility rule;
- fixture home and minimum fixtures for valid release inclusion, held release, sensitive generalized release, rights-denied release, stale layer, superseded layer, withdrawal, and rollback;
- validator path and CI wiring;
- release policy rules for layer artifacts;
- proof/receipt binding to ReleaseManifest and layer artifact digests;
- public API/UI/map/AI tests proving no pre-PUBLISHED or sensitive layer leakage.

---

## Open questions

- Should this file remain a release-side bridge, or should it be replaced by an object-folder pointer to `contracts/data/layer_manifest.md`?
- Should a future `ReleaseLayerManifest` object have a distinct name to avoid collision with canonical `LayerManifest`?
- Should release-specific layer fields live inside `ReleaseManifest.contents[]` instead of a standalone contract?
- Which schema home is authoritative: `schemas/contracts/v1/data/`, `schemas/contracts/v1/layers/`, or `schemas/contracts/v1/release/`?
- How should PMTiles/COG sidecars, style fragments, and layer digests be represented without making this contract an artifact store?

---

## Rollback

Rollback is required if this file is used to duplicate the canonical `LayerManifest` contract, publish a layer, store artifacts, bypass release gates, bypass sensitivity/rights policy, hide correction/rollback lineage, or authorize public map/UI/AI exposure directly.

Rollback target for this expansion: previous scaffold blob SHA `472a4fcc061493494791cdad51c224bc9b153566`.

<p align="right"><a href="#top">Back to top</a></p>
