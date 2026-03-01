<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8d7e66f4-6a7b-44d8-8f7a-6a3dc5b8e9c2
title: ADR: Map surfaces and access rules by lifecycle zone
type: adr
version: v1
status: draft
owners: kfm-platform
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - kfm://doc/kfm-blueprint-vnext
  - kfm://doc/tooling-kfm-pipeline
  - kfm://doc/promotion-contract-v1
  - kfm://doc/trust-membrane
  - kfm://doc/evidence-resolver-contract
  - kfm://doc/story-node-v3
  - kfm://doc/focus-mode
  - kfm://vocab/artifact.zone
  - kfm://vocab/policy_label
  - kfm://vocab/citation.kind
tags:
  - kfm
  - adr
  - maps
  - governance
notes:
  - Defines which map capabilities are permitted in each truth-path zone.
  - Prevents accidental policy bypass and keeps “preview” experiences safe.
[/KFM_META_BLOCK_V2] -->

# ADR: Map surfaces and access rules by lifecycle zone

![Status](https://img.shields.io/badge/status-draft-yellow)
![Type](https://img.shields.io/badge/type-ADR-blue)
![Area](https://img.shields.io/badge/area-maps%20%2B%20governance-purple)

**Decision date:** 2026-03-01  
**Owners:** `kfm-platform` (with `kfm-governance` review)

## Quick links
- [Context](#context)
- [Decision](#decision)
- [Zone-by-zone contract](#zone-by-zone-contract)
- [Implementation notes](#implementation-notes)
- [Consequences](#consequences)
- [Alternatives considered](#alternatives-considered)
- [Roll-back plan](#roll-back-plan)
- [Open questions](#open-questions)
- [Verification (minimum)](#verification-minimum)

---

## Context

**Where this lives:** `docs/adr/maps/by-zone.md` (map governance decisions).

KFM’s credibility depends on two coupled ideas:
1) a **truth path** (RAW → WORK/QUARANTINE → PROCESSED → CATALOG → PUBLISHED), and
2) a **trust membrane** (clients do not touch storage or DBs directly; policy is enforced at a governed API boundary).

Maps are the most “leaky” surface in geospatial systems: a single tile, feature popup, or export can accidentally reveal restricted coordinates, attributes, or rights-protected media. This ADR standardizes which map surfaces are allowed in each zone, and how “preview” works without breaking governance.

---

## Decision

### D1. Map surfaces MUST be gated by **zone** and **policy_label**

- **Zone** controls *lifecycle* and what is eligible to be served at all.
- **policy_label** controls *who can see what* and what redaction/generalization obligations apply.

A dataset version may only be shown in public map UI when:
- it is in **PUBLISHED**, and
- its **policy_label** allows the requesting principal’s action.

Additionally:
- Any dataset version in **QUARANTINE** is treated as *not eligible* for map serving (fail closed), even for stewards, unless an explicit override is approved and recorded.

### D2. Only PROCESSED + CATALOG artifacts are eligible inputs to map serving

- RAW and WORK artifacts are never served into public-facing map surfaces.
- Preview map rendering (if needed) must either:
  - use PROCESSED artifacts in a “preview channel”, or
  - be a local/dev-only workflow that never reaches shared endpoints.

### D3. “Preview” is a first-class capability, but it is **still governed**

Preview is permitted to support QA, cartographic iteration, and steward review, but:
- it must flow through the same policy semantics as runtime,
- it must be explicitly labeled in UX (watermark/badge), and
- it must not widen access beyond what would be allowed after promotion.

---

## Zone-by-zone contract

### Contract table (normative)

| Zone | Primary goal | Allowed map surfaces | Not allowed | Notes |
|---|---|---|---|---|
| **RAW** | Immutable acquisition | none | tiles, feature queries, UI browsing, exports | RAW exists for reproducibility and audits; not for interaction. |
| **WORK** | Normalization + QA | steward-only preview *if* policy allows | public UI; public tiles; shareable links | Treat as unstable + potentially sensitive. |
| **QUARANTINE** | Fail-closed holding | none (default) | all public surfaces; all exports | Only governance/steward access; used when license/sensitivity/QA unclear. |
| **PROCESSED** | Publishable artifacts | steward preview; limited internal UI | public UI (unless promoted to PUBLISHED) | First zone where “delivery formats” should exist (e.g., GeoParquet/COG/PMTiles). |
| **CATALOG** | Evidence + discovery metadata | catalog-only browsing (metadata) | raw artifact download (unless policy allows) | DCAT/STAC/PROV must cross-link and be resolvable. |
| **PUBLISHED** | Governed runtime | public UI + governed API | direct storage/DB access | This is the only zone eligible for general users. |

### Map surfaces defined

- **Tiles**: vector tiles (PMTiles or z/x/y endpoints) and raster tiles (COG-derived tiles).
- **Feature query**: query-by-bbox / identify-on-click.
- **Catalog browsing**: discovery UI with dataset extents, versions, license, provenance, and “open evidence” actions.
- **Exports**: any bulk download, clip, or “download this selection”.

### Controlled vocabulary notes

**This ADR assumes the following controlled vocabulary exists (or will exist) and is enforced by schema + CI:**

- `artifact.zone`: `raw | work | processed | catalog | published`
- `policy_label` (starter set): `public | public_generalized | restricted | restricted_sensitive_location | internal | embargoed | quarantine`

`policy_label` *must* drive both authorization decisions and any required obligations (e.g., geometry generalization notices).

### UX requirements (normative)

- Any surface that can lead to a public-facing claim (feature popups, layer description panels, exports, story embeds) MUST provide an “open evidence” affordance that resolves to an inspectable evidence view.
- Preview surfaces MUST be visually distinct from published surfaces (badge + watermark) to prevent screenshots being mistaken for publication.

---

## Implementation notes

### Reference architecture (conceptual)

~~~mermaid
flowchart LR
  subgraph Zones[Truth path zones]
    RAW[RAW\n(immutable acquisition)] --> WORK[WORK\n(normalize + QA)]
    WORK --> PROC[PROCESSED\n(publishable artifacts)]
    PROC --> CAT[CATALOG\n(DCAT + STAC + PROV)]
    CAT --> PUB[PUBLISHED\n(governed runtime)]
  end

  subgraph Serving[Map surfaces]
    UI[Map Explorer / Story / Focus] -->|only| API[Governed API (PEP)]
    API -->|policy-checked| Tiles[Tiles]
    API -->|policy-checked| Features[Feature queries]
    API -->|policy-checked| Evidence[Evidence resolve]
  end

  RAW -. not served .-> Serving
  WORK -. steward preview only .-> API
  PROC --> API
  CAT --> API
  PUB --> API
~~~

### Policy + evidence requirements

- Every map interaction that can surface facts (feature popup, layer metadata, export) must be able to open an **EvidenceBundle** view.
- Story publishing and Focus Mode must hard-gate on “citations resolve + policy allows”.

### CRS and reprojection (PROPOSED default)

- Canonical storage CRS for vector artifacts: **EPSG:4326**.
- Web map tile rendering: derive **EPSG:3857** tiles from PROCESSED artifacts.

> If a different standard is already adopted in the repo, this ADR must be updated to match it (and the choice should be enforced by schema + CI).

---

## Consequences

### Benefits
- Prevents “accidental publication” from RAW/WORK.
- Makes preview safe and explicit.
- Keeps evidence-first UX coherent (every surfaced claim routes to evidence).

### Costs
- Requires extra “preview channel” plumbing (policy-aware) for stewards.
- Adds discipline: cartography iteration must be done against PROCESSED artifacts (or local-only).

---

## Alternatives considered

1) **Allow UI to browse WORK/RAW directly in dev**
   - Rejected: creates habits and tooling that later bypass policy.

2) **Serve everything as long as policy_label blocks it**
   - Rejected: zone still matters. RAW/WORK artifacts are unstable and may embed unreviewed licensing/sensitivity problems.

3) **No preview at all**
   - Rejected: stewards and cartographers need a workflow for QA and symbology iteration before promotion.

---

## Roll-back plan

This ADR is additive. If preview gating introduces friction or breaks workflows:

1) Temporarily disable preview mode at the API layer (feature flag) while keeping the zone rules intact.
2) Fall back to local-only preview for cartography iteration (no shared endpoints) until preview plumbing is corrected.
3) Keep CI promotion gates unchanged.

Any rollback must preserve: (a) trust membrane, and (b) “PUBLISHED-only for public UI” invariant.

## Open questions

- Should CATALOG metadata for restricted datasets be visible to public users (metadata-only), or hidden entirely?
- Do we need explicit “public extent only” rendering for restricted datasets (e.g., show statewide bbox but not geometry)?
- What is the repo’s current canonical CRS convention (if any), and is it enforced by validators?

---

## Verification (minimum)

- [ ] Confirm CI gate(s) prevent promotion without DCAT/STAC/PROV + run receipt.
- [ ] Confirm no UI path exists that hits object storage or PostGIS directly (static analysis + runtime network checks).
- [ ] Confirm EvidenceRefs resolve end-to-end from: feature click → evidence drawer.
- [ ] Confirm policy fixture tests cover at least: public, public_generalized, restricted, restricted_sensitive_location, quarantine.

---

## References

- KFM vNext: truth path zones, promotion contract, and controlled vocabularies.
- Tooling plan: evidence resolver contract; Map Explorer acceptance criteria (evidence drawer shows license + dataset version).
