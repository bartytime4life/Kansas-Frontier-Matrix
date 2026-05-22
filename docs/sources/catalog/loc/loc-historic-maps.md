<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-loc-loc-historic-maps
title: LOC Geography and Map Division Historic Maps
type: product-page
version: v0.2
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward for `loc` family>
created: 2026-05-20
updated: 2026-05-22
policy_label: public
related:
  - docs/sources/catalog/loc/README.md
  - docs/sources/catalog/loc/IDENTITY.md
  - docs/sources/catalog/loc/RIGHTS-AND-SENSITIVITY-MAP.md
  - docs/sources/catalog/loc/LCNAF.md
  - docs/sources/catalog/loc/LCSH.md
  - docs/sources/catalog/loc/CHRONICLING-AMERICA.md
  - docs/sources/catalog/loc/_examples/stac-item-example.json
  - docs/sources/catalog/loc/_examples/historic-map-overlay-manifest-example.json
  - docs/sources/catalog/README.md
  - docs/standards/STAC_KFM_PROFILE.md
  - docs/standards/PROV.md
  - docs/standards/PLUGIN_ALLOWLIST.md
  - docs/doctrine/directory-rules.md
  - data/registry/sources/loc/historic-maps/
  - schemas/contracts/v1/source/source-descriptor.schema.json
  - schemas/contracts/v1/map/historic_map_overlay_manifest.schema.json
  - connectors/loc/historic-maps/
  - pipeline_specs/cross-domain/loc-historic-maps/
tags: [kfm, docs, sources, catalog, loc, historic-maps, iiif, allmaps, georeference, warped-overlay, representation, story-node]
notes:
  - "PROPOSED product-page scaffold; the docs/sources/catalog/loc/ tree itself is PROPOSED until repo verification."
  - "Historic-map overlays are INTERPRETIVE REPRESENTATIONS, not direct geometry evidence — Representation Receipt + Reality Boundary Note are required."
  - "Doctrine grounded in KFM-P9-FEAT-0016, KFM-P9-PROG-0074, ML-064-036/037, ML-064-103 (analog GLO RMS pattern)."
  - "Owners, badge targets, and example links are explicit placeholders — not fabricated."
[/KFM_META_BLOCK_V2] -->

# LOC Geography and Map Division — Historic Maps

> Historic maps served via **IIIF**, rendered as **warped overlays** through **Allmaps georeference annotations** for Story-Node context — treated as *interpretive representations* requiring source rights, ground-control-point (GCP) provenance, RMS uncertainty disclosure, and **plugin governance** before any MapLibre display.

[![Status: PROPOSED](https://img.shields.io/badge/status-PROPOSED-orange)]() &nbsp;
[![Family: loc](https://img.shields.io/badge/family-loc-blue)](./README.md) &nbsp;
[![Source role: context · representation](https://img.shields.io/badge/source--role-context%20%C2%B7%20representation-purple)]() &nbsp;
[![Carries: Representation Receipt](https://img.shields.io/badge/carries-Representation%20Receipt-9cf)]() &nbsp;
[![Reality Boundary: required](https://img.shields.io/badge/reality%20boundary-required-orange)]() &nbsp;
[![Policy: public](https://img.shields.io/badge/policy-public-green)]() &nbsp;
[![Rights: NEEDS%20VERIFICATION](https://img.shields.io/badge/rights-NEEDS%20VERIFICATION-yellow)](./RIGHTS-AND-SENSITIVITY-MAP.md) &nbsp;
[![Doctrine: KFM v1.1](https://img.shields.io/badge/doctrine-KFM%20v1.1-lightgrey)](../../../doctrine/directory-rules.md) &nbsp;
[![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)]()

**Status:** PROPOSED — scaffold only · **Source family:** [`loc`](./README.md) · **Source role (PROPOSED):** **`context`** with mandatory **`Representation Receipt`** (the warped overlay is interpretive, not observed positional truth)  
**Anchored object families (CONFIRMED doctrine):** `HistoricMapOverlayManifest` (PROPOSED), `Representation Receipt`, `Reality Boundary Note`, `LayerManifest`, `TileArtifactManifest`  
**Owners:** `<PLACEHOLDER — Docs steward + Source steward for loc>` · **Last reviewed:** 2026-05-22

---

## Contents

- [1. Overview](#1-overview)
- [2. Where this product fits in the KFM corpus](#2-where-this-product-fits-in-the-kfm-corpus)
- [3. Source authority (no descriptor fields here)](#3-source-authority-no-descriptor-fields-here)
- [4. The interpretive-representation frame](#4-the-interpretive-representation-frame)
- [5. Catalog profiles used](#5-catalog-profiles-used)
- [6. Collection identity](#6-collection-identity)
- [7. Provenance fields (`kfm:provenance` + georeference provenance)](#7-provenance-fields-kfmprovenance--georeference-provenance)
- [8. Temporal handling](#8-temporal-handling)
- [9. Geometry, projection, and georeference uncertainty](#9-geometry-projection-and-georeference-uncertainty)
- [10. Rights, sensitivity, and CARE posture](#10-rights-sensitivity-and-care-posture)
- [11. Plugin governance (Allmaps WarpedMapLayer)](#11-plugin-governance-allmaps-warpedmaplayer)
- [12. Validation and catalog closure](#12-validation-and-catalog-closure)
- [13. Related contracts and schemas](#13-related-contracts-and-schemas)
- [14. Related connectors and pipelines](#14-related-connectors-and-pipelines)
- [15. Examples (illustrative only)](#15-examples-illustrative-only)
- [16. Open questions](#16-open-questions)
- [17. Related docs](#17-related-docs)
- [Appendix · Field expectations and disposition matrix](#appendix--field-expectations-and-disposition-matrix)

---

## 1. Overview

CONFIRMED (`KFM-P9-FEAT-0016`, MAP category): KFM treats *"historic-map overlays from IIIF/Allmaps or similar systems as **interpretive georeferenced artifacts requiring source rights, control points, and uncertainty metadata**."* The overlay is **not direct geometry evidence**; it is a representation choice with disclosed georeferencing error.

CONFIRMED (`KFM-P9-PROG-0074`): KFM historic-map overlays must **preserve IIIF rights, georeferencing annotation provenance, and plugin governance before MapLibre display**.

CONFIRMED (`ML-064-036`, `ML-064-037` from the MapLibre master): IIIF + Allmaps overlays warp historic maps into MapLibre/Leaflet **without rehosting**; the Allmaps **`WarpedMapLayer`** belongs in **Story Node map panels** and **must** be governed via a plugin allowlist with attribution/rights tests.

PROPOSED (this product): The page records how LOC Geography and Map Division (G&M) holdings — delivered as IIIF — flow through Allmaps georeference annotations into a KFM **`HistoricMapOverlayManifest`** and the Story-Node UI. No live repository is mounted in this session.

> [!WARNING]
> **Synthetic-as-observed is a CONFIRMED anti-pattern** (CDB cross-domain object/receipt table). A warped historic map is a **representation**, not an observation. Any KFM surface that uses these overlays MUST carry a **`Representation Receipt`** and a **`Reality Boundary Note`** in the Evidence Drawer; AI surfaces MUST `ABSTAIN` on questions that would treat the warped overlay's positions as modern positional truth.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 2. Where this product fits in the KFM corpus

CONFIRMED (Directory Rules §0, §5, §6, §6.4, §6.5, §7.3, §7.4, §9.1): KFM uses **responsibility roots**, not topic roots. A product page belongs in `docs/`; the source descriptor belongs in `data/registry/sources/`; schemas live under `schemas/contracts/v1/source/` (and `schemas/contracts/v1/map/` for map-side manifests) per **ADR-0001**; policy lives in `policy/`; connectors live in `connectors/`; pipelines live in `pipelines/`; declarative specs live in `pipeline_specs/`.

PROPOSED (path of this file): `docs/sources/catalog/loc/HISTORIC-MAPS.md`. NEEDS VERIFICATION — the `docs/sources/catalog/loc/` tree itself is PROPOSED.

```mermaid
flowchart LR
    A[LoC G and M<br/>IIIF Presentation Manifest] -->|fetch IIIF| B[connectors/loc/<br/>historic-maps/]
    A2[Allmaps<br/>Georeference Annotation] -->|fetch annotation| B
    B -->|raw IIIF bytes + GCPs<br/>+ receipts| C[data/raw/cross-domain/<br/>loc-historic-maps/]
    C --> D[data/work/<br/>RMS check · uncertainty model]
    D -->|RMS threshold + rights gate| E[data/processed/]
    E --> F[data/catalog/<br/>stac/ · dcat/ · prov/]
    E --> G[HistoricMapOverlayManifest<br/>+ Representation Receipt<br/>+ Reality Boundary Note]
    G --> H[release/]
    F --> H
    H -->|MapReleaseManifest| I[data/published/<br/>layers/ · pmtiles/]
    I -.->|governed API| J[Story Node map panel<br/>Allmaps WarpedMapLayer<br/>via plugin allowlist]
    J -.-> K[Public UI · Focus Mode]
    style A fill:#eef,stroke:#88a
    style A2 fill:#eef,stroke:#88a
    style G fill:#fef,stroke:#a8a
    style J fill:#eff,stroke:#8aa
    style K fill:#efe,stroke:#8a8
    style D fill:#fee,stroke:#a88
```

> [!IMPORTANT]
> The diagram reflects **CONFIRMED doctrine** (RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED; IIIF + Allmaps overlay pattern per `ML-064-036` / `ML-064-037`; Representation Receipt + Reality Boundary Note required per §1) — not a verified implementation. Box paths are **PROPOSED**; presence in the live repo is NEEDS VERIFICATION.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 3. Source authority (no descriptor fields here)

CONFIRMED (doctrine, Directory Rules §9.1): The **authoritative `SourceDescriptor`** for this product lives under [`data/registry/sources/`](../../../../data/registry/sources/) (PROPOSED leaf: `data/registry/sources/loc/historic-maps/`). The schema home is `schemas/contracts/v1/source/source-descriptor.schema.json` per **ADR-0001**.

> [!WARNING]
> **Do not duplicate descriptor fields here.** A product page explains; the **registry owns identity, role, rights, cadence, steward, sensitivity, and access method**.

| Descriptor responsibility | Home (CONFIRMED) | Authored here? |
|---|---|---|
| Identity, role, access, cadence, rights | `data/registry/sources/loc/historic-maps/` | **No** — registry owns |
| Machine shape of the descriptor | `schemas/contracts/v1/source/` (ADR-0001) | **No** — schemas owns |
| HistoricMapOverlayManifest shape | `schemas/contracts/v1/map/historic_map_overlay_manifest.schema.json` (PROPOSED) | **No** — schemas owns |
| Allow / deny / restrict / abstain | `policy/sensitivity/` and `policy/release/` | **No** — policy owns |
| Plugin allowlist | `policy/plugins/` (PROPOSED — see §11) | **No** — policy owns |
| Human-facing orientation, georeference frame, examples | this product page (`docs/`) | **Yes** |

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 4. The interpretive-representation frame

CONFIRMED (CDB §24.7 receipts table — Master Receipt Register, included in the consolidated atlas): KFM defines a **`RepresentationReceipt`** specifically for *"a representation step where surface fidelity differs from evidence fidelity — e.g., 3D scene from 2D evidence, synthetic terrain, tile downsampling."* Required fields (PROPOSED shape): `evidence_ref`, `representation_method`, `parameters`, `reality_boundary_note_ref`. **A warped historic-map overlay is the canonical 2D analogue.**

CONFIRMED (Planetary/3D domain ubiquitous language, §17): **`Reality Boundary Note`** is a CONFIRMED term — *"public-facing or steward-facing statement that a carrier is synthetic or reconstructed and not direct evidence."* PROPOSED extension: the same vocabulary applies to 2D georeferenced overlays whose positions are interpretive.

CONFIRMED (`KFM-P9-FEAT-0016` dependencies): **`HistoricMapOverlayManifest`** is named as a PROPOSED object family; `GCP provenance` and `plugin allowlist` are required dependencies.

| Frame element | Role | Status |
|---|---|---|
| **`HistoricMapOverlayManifest`** | Binds IIIF manifest URL + Allmaps annotation URL + GCP set + RMS + warp method to a `LayerManifest` | PROPOSED (`KFM-P9-FEAT-0016`) |
| **`RepresentationReceipt`** | Records that the overlay is a representation, what method warped it, and the parameters | CONFIRMED concept (CDB §24.7); shape PROPOSED |
| **`Reality Boundary Note`** | Public-facing statement that the overlay is interpretive, not observed positional truth | CONFIRMED term (§17 Planetary/3D); applies here by parallel |
| **GCP provenance** | Source of each ground control point (Allmaps annotator, KFM editor, automated match) + confidence | CONFIRMED dependency (`KFM-P9-FEAT-0016`) |
| **RMS receipt** | Root-mean-square georeferencing error against threshold (parallel to `ML-064-103` GLO RMS pattern) | PROPOSED — see §15 OPEN-HM-01 |
| **Plugin allowlist** | Governance for Allmaps `WarpedMapLayer` and any other overlay plugin | CONFIRMED requirement (`ML-064-037`) |

> [!CAUTION]
> The corpus explicitly asks (NEEDS VERIFICATION in `KFM-P9-FEAT-0016`): *"Should historic overlays default to **contextual evidence** rather than **direct geometry evidence**?"* Until that question is answered by ADR, this product defaults to **contextual** — overlays may inform Story Nodes and Focus Mode context but may not anchor positional claims about modern features.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 5. Catalog profiles used

CONFIRMED (Pass 10 C4): KFM publishes through **STAC** (spatiotemporal), **DCAT** (dataset-level), and **PROV-O / PAV** (lineage). Unlike LCNAF / LCSH (authority sources) and unlike Chronicling America (page-level documents), **historic-map overlays are spatiotemporal raster assets** — STAC participation is **Yes**.

| Profile | Lane (CONFIRMED canonical home) | Used by this product? | Basis |
|---|---|---|---|
| STAC (Items + Collection) | `data/catalog/stac/` | **PROPOSED — Yes**. Each warped overlay is a STAC Item with `geometry` (warped bbox), `datetime` (original map date or interval), and a `kfm:provenance` block. The IIIF manifest, Allmaps annotation, and PMTiles render are STAC assets. | `KFM-P14-PROG-0009` (LoC IIIF STAC PROV ingestor); Pass 10 C4-01 |
| DCAT | `data/catalog/dcat/` | **PROPOSED — Yes** (dataset-level row for the LoC G&M snapshot KFM consumes) | Pass 10 C4-05; `KFM-P26-PROG-0025` |
| PROV-O / PAV | `data/catalog/prov/` | **PROPOSED — Yes** (`wasDerivedFrom` chain: IIIF manifest → Allmaps annotation → warped overlay → PMTiles render) | Pass 10 C8-03 |
| Domain projection | `data/catalog/domain/cross-domain/` | **PROPOSED — Yes** (cross-domain; used by Settlements, Roads/Rail/Trade, Archaeology, People/Land, Hydrology context, etc.) | Directory Rules §9.1 |
| `kfm:care` extension on STAC / DCAT | as above | **PROPOSED — Yes** when overlays touch Indigenous places, vernacular naming, or culturally-sensitive cartography | Pass 10 C15-02 |

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 6. Collection identity

PROPOSED (Pass 10 C4-02): Collection id pattern is `kfm-<org>-<product>`; the exact form for this product is left to [`IDENTITY.md`](./IDENTITY.md). Collection ids are **stable handles** — renaming a Collection breaks links throughout the catalog.

PROPOSED (Pass 10 C4-01 open question, tracked as **OPEN-DSC-03**): The vendor namespace for KFM extension fields is **unresolved between `kfm:` (KFM-global) and `ks-kfm:` (Kansas-scoped)**. This page does not pin the choice.

| Identity item | Status | Notes |
|---|---|---|
| Collection id pattern | PROPOSED | `kfm-<org>-<product>` (Pass 10 C4-02) |
| Namespace | UNKNOWN | `kfm:` vs `ks-kfm:` — pending **OPEN-DSC-03** ADR |
| Asset roles | NEEDS VERIFICATION | Likely `["iiif", "metadata"]` for the IIIF manifest; `["data", "georeference"]` for the Allmaps annotation; `["data", "tiles"]` for the PMTiles render — confirm against `schemas/contracts/v1/source/` |
| Provider block | NEEDS VERIFICATION | Library of Congress as `publisher` (IIIF manifest); Allmaps as `processor` (georeference annotation); KFM as `processor` (warp + tile) |

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 7. Provenance fields (`kfm:provenance` + georeference provenance)

CONFIRMED (Pass 10 C4-01): STAC Items carry `item.properties.kfm:provenance` with:

| Field | Role | Resolves to |
|---|---|---|
| `spec_hash` | Deterministic identity of the canonical record (JCS + SHA-256) | n/a — opaque digest |
| `evidence_bundle_ref` | Truth-bearing JSON-LD bundle (claims + citations + receipts) | `kfm://evidence/<digest>` |
| `run_record_ref` | The run that produced this artifact | `kfm://run/<run-id>` |
| `audit_ref` | SLSA / OPA attestation chain | `kfm://audit/<attestation-id>` |
| `policy_digest` | The policy bundle at promotion time | sha256 of the policy set |

**Per-asset integrity:** `file:checksum` applies to each IIIF manifest snapshot, Allmaps annotation snapshot, and PMTiles render.

PROPOSED (this product's georeference-provenance extension, grounded in `KFM-P9-FEAT-0016`, `ML-064-036` validation requirements, and the parallel `ML-064-103` GLO RMS pattern): a **`kfm:georeference`** block on the STAC Item / `HistoricMapOverlayManifest`:

| Field | Role | Status |
|---|---|---|
| `iiif_manifest_digest` | sha256 of the IIIF Presentation Manifest at fetch time | PROPOSED — required |
| `allmaps_annotation_digest` | sha256 of the Allmaps georeference annotation | PROPOSED — required (`ML-064-036` validation) |
| `gcps[]` | Array of `{pixel, world, source, confidence}` GCPs | PROPOSED — required (`KFM-P9-FEAT-0016`) |
| `gcp_source_breakdown` | Counts by annotator: Allmaps community / KFM editor / automated | PROPOSED |
| `warp_method` | e.g., `helmert`, `polynomial-1`, `polynomial-2`, `tps` | PROPOSED |
| `rms_error_pixels` / `rms_error_meters` | Residual error against held-out points | PROPOSED — required, with threshold per **OPEN-HM-01** |
| `representation_receipt_ref` | `kfm://receipt/representation/<digest>` | PROPOSED — required |
| `reality_boundary_note_ref` | `kfm://note/reality-boundary/<digest>` | PROPOSED — required |

> [!TIP]
> The georeference block is **stricter than the default catalog provenance** because the overlay's positions are **derived**, not observed. Every consequential downstream claim that uses the overlay must resolve to *both* the `evidence_bundle_ref` *and* the `representation_receipt_ref`.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 8. Temporal handling

CONFIRMED (doctrine §24.8 + repeated multi-temporal discipline): KFM keeps source / observed / valid / retrieval / release / correction times distinct where material. For historic-map overlays the relevant times are:

| Time field | Meaning for this product | Status |
|---|---|---|
| `source_time` | The **date printed on the historic map** (or an interval, if survey-date and publish-date differ) | PROPOSED — required where the IIIF manifest exposes it |
| `valid_time` | Interval over which the overlay's depicted state is asserted to apply (typically the **survey date**, not the publication date) | NEEDS VERIFICATION per map; often imprecise — encode as an interval with uncertainty |
| `retrieval_time` | When KFM fetched the IIIF manifest + Allmaps annotation | **MUST** — required by the georeference receipt |
| `release_time` | When the KFM cached overlay entered PUBLISHED | PROPOSED — required (set by `MapReleaseManifest`) |
| `correction_time` | When LoC re-released, Allmaps re-annotated, or KFM re-warped | PROPOSED — required when applicable |
| `annotation_revision_time` *(Allmaps-specific)* | When the Allmaps georeference annotation was last revised by its annotator | PROPOSED — surface as a stale-state badge per §24.8 |

CONFIRMED (§24.8 stale-state markers): When the underlying IIIF manifest or Allmaps annotation is revised, KFM must show a **schema-or-source-drift** badge and trigger re-warp on dependent overlays; otherwise the overlay is **stale**, not wrong.

> [!NOTE]
> Historic-map dating is **structurally imprecise**: a map "published 1879" may depict survey work from 1875–1878, with hand-drawn annotations through 1881. Encode `source_time` as an interval where the manifest supports it; do not collapse to a single year just to fit a UI badge.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 9. Geometry, projection, and georeference uncertainty

This is the **largest substantive section** of this page because historic-map overlays are defined by their georeferencing properties.

CONFIRMED (`KFM-P9-FEAT-0016`): Historic-map overlays *"require source rights, **control points**, and **uncertainty metadata**."*

CONFIRMED (`ML-064-103` parallel for GLO plats): *"GLO plat georeferencing requires **RMS and control-point receipts**."* The same discipline applies to LoC historic-map overlays.

PROPOSED rules for this product:

| Concern | Rule | Status |
|---|---|---|
| **CRS for the original raster** | The original IIIF tiles have no CRS; only pixel space | CONFIRMED (IIIF property) |
| **CRS for the warped overlay** | `EPSG:4326` for provenance and Allmaps annotation; `EPSG:3857` only at tile time, per `ML-E-062` doctrine | PROPOSED |
| **Warp method disclosure** | The method (`helmert` / `polynomial-N` / `tps`) MUST appear in the `kfm:georeference` block; the Evidence Drawer MUST surface it | PROPOSED — required |
| **RMS threshold** | A per-collection or per-Item RMS-error threshold (in pixels and meters) MUST exist; overlays exceeding the threshold are quarantined or downgraded to "preview only" | PROPOSED — see OPEN-HM-01 for the threshold value |
| **Control-point completeness** | A minimum number of GCPs (per warp method) MUST be enforced; warps with fewer than the minimum are denied | PROPOSED |
| **Uncertainty surface** | An optional `kfm:uncertainty_surface` raster (per-pixel positional error) MAY be emitted alongside the overlay | PROPOSED — see OPEN-HM-02 |
| **Generalization at scale** | Overlay opacity, zoom-range gating, and styling MUST be set so users cannot read modern positional facts from the warped raster | PROPOSED — see §11 plugin governance |

> [!CAUTION]
> Even a well-georeferenced 19th-century township plat is **not** a substitute for modern survey data. A KFM surface that lets a user pin a 21st-century parcel claim to a 1879 LoC overlay is collapsing **representation** into **observation** — the exact anti-pattern the Representation Receipt and Reality Boundary Note are designed to prevent.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 10. Rights, sensitivity, and CARE posture

NEEDS VERIFICATION (default for this product): defer to [`policy/sensitivity/`](../../../../policy/sensitivity/) and [`./RIGHTS-AND-SENSITIVITY-MAP.md`](./RIGHTS-AND-SENSITIVITY-MAP.md). **Do not restate policy here.**

CONFIRMED (`KFM-P9-PROG-0074`): KFM historic-map overlays MUST *"preserve **IIIF rights, georeferencing annotation provenance, and plugin governance** before MapLibre display."* This implies **two parallel rights streams** that must both clear:

| Rights stream | Holder (typical) | KFM treatment |
|---|---|---|
| **IIIF rights** | Library of Congress (host); rights statement varies per item | CONFIRMED requirement (`KFM-P9-PROG-0074`); MUST be preserved as a STAC asset on the Item and surfaced in the Evidence Drawer |
| **Allmaps annotation rights** | Allmaps community / individual annotator (typically open) | PROPOSED — confirm per snapshot; annotation provenance is required by `KFM-P9-FEAT-0016` |

CONFIRMED (Master MapLibre Q section): the anti-pattern *"Assuming all mirrors inherit federal public domain rights"* applies. LoC G&M items have varying rights postures (some U.S. government works; some donated collections with separate rights). **Rights must be checked per item, not assumed federal-domain.**

PROPOSED (sensitivity tier baseline):

- **T0** for an overlay whose underlying LoC item carries no use restriction, whose Allmaps annotation is openly licensed, and whose depicted content is not culturally sensitive.
- **T1+** escalation when the overlay depicts:
  - Indigenous places with vernacular / historically-imposed names (CARE applicability — Pass 10 C15-02 / C15-03);
  - Burial grounds, sacred sites, or sites identified to KFM stewards as restricted regardless of LoC's public posture;
  - Living-person or sensitive-property detail (rare on historic maps, but plat books can show occupancy);
  - Infrastructure detail that, even historic, falls under a current-day sensitivity policy.

> [!WARNING]
> Historic maps frequently encode **outdated or harmful place-naming, racial classifications, and sovereignty erasures**. When such content is present, the overlay must carry a CARE flag, a steward review, and a public-facing **interpretive caveat** in the Evidence Drawer. Do not silently render such content as if it were neutral cartography.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 11. Plugin governance (Allmaps WarpedMapLayer)

CONFIRMED (`ML-064-037`): The Allmaps `WarpedMapLayer` *"belongs in Story Node map panels"* and is to be *"used as a **conditional overlay plugin with dependency governance**."* Validation: **plugin allowlist** and **attribution/rights test**.

CONFIRMED (`KFM-P9-PROG-0074`): Plugin governance is one of three things that MUST be preserved before MapLibre display (alongside IIIF rights and georeference annotation provenance).

PROPOSED (operational rules for this product):

| Concern | Rule |
|---|---|
| Allowlist | The Allmaps `WarpedMapLayer` and any dependency must appear in `policy/plugins/` (PROPOSED path) with pinned versions and digests |
| SRI / version pinning | Browser-loaded plugin assets must be SRI-pinned or shipped as in-tree packages; out-of-band plugin loading is denied |
| Attribution test | A CI test must verify that every Story Node consuming a warped overlay surfaces the LoC IIIF attribution and the Allmaps attribution |
| Sandboxing | The plugin runs only inside the Story Node map panel; it does not gain access to other governed UI surfaces |
| Update governance | A new plugin version must enter via an ADR or per-root README update — never as a silent dependency bump |

> [!IMPORTANT]
> The plugin allowlist is **policy**, not a build-time convenience. A new `WarpedMapLayer` version landing without an allowlist update is grounds for the catalog-closure gate to fail closed.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 12. Validation and catalog closure

CONFIRMED (`KFM-P1-IDEA-0020`, "Catalog closure before public release"): Public release requires **catalog closure** linking evidence, source role, policy, proof, release state, and rollback target.

| Gate | Reference | Status for this product |
|---|---|---|
| Catalog closure (STAC + DCAT + PROV + evidence) | `KFM-P1-IDEA-0020` | **Required** before publication |
| IIIF manifest rights validated | `ML-064-036` validation | **Required** |
| Allmaps annotation digest validated | `ML-064-036` validation | **Required** |
| GCP completeness and RMS threshold | `KFM-P9-FEAT-0016` + parallel `ML-064-103` | **Required** — see OPEN-HM-01 |
| Plugin allowlist + attribution test | `ML-064-037` | **Required** |
| Representation Receipt present | CDB §24.7 receipts table | **Required** for any KFM surface using the overlay |
| Reality Boundary Note attached to the Evidence Drawer payload | §17 Planetary/3D term; parallel for 2D overlays | **Required** for public surfaces |
| STAC Projection lint | `KFM-P27-FEAT-0003` | PROPOSED |
| Catalog QA surface | `KFM-P27-FEAT-0004` | PROPOSED |
| Dataset promotion MetaBlock v2 checklist | `KFM-P14-PROG-0033` | PROPOSED — fail-closed |
| SPDX license guard | `KFM-P10-PROG-0014` | PROPOSED — required |
| AI surface ABSTAIN on positional questions about modern features | CDB anti-pattern register (synthetic-as-observed) | **Required** behavior in Focus Mode |

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 13. Related contracts and schemas

| Object family | Home (CONFIRMED doctrine) | Status |
|---|---|---|
| `SourceDescriptor` (meaning) | [`contracts/source/`](../../../../contracts/source/) | NEEDS VERIFICATION |
| `SourceDescriptor` (shape) | [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — per **ADR-0001** | CONFIRMED schema-home rule |
| `HistoricMapOverlayManifest` (shape) | `schemas/contracts/v1/map/historic_map_overlay_manifest.schema.json` (PROPOSED) | PROPOSED — see OPEN-HM-03 |
| `LayerManifest` | `schemas/contracts/v1/map/layer_manifest.schema.json` | CONFIRMED in Master MapLibre object table |
| `TileArtifactManifest` (warped PMTiles render) | `schemas/contracts/v1/map/tile_artifact_manifest.schema.json` | CONFIRMED in Master MapLibre object table |
| `MapReleaseManifest` | `schemas/contracts/v1/map/map_release_manifest.schema.json` | CONFIRMED in Master MapLibre object table |
| `EvidenceBundle` (shape) | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | CONFIRMED in Master MapLibre object table |
| `RepresentationReceipt` (shape) | PROPOSED home under `schemas/contracts/v1/receipts/` or `schemas/contracts/v1/<domain>/receipts/` per **ADR-S-03** | PROPOSED — schema home pending ADR-S-03 |
| `Reality Boundary Note` (shape) | PROPOSED home, likely under `schemas/contracts/v1/ui/` or `schemas/contracts/v1/evidence/` | PROPOSED |
| Plugin allowlist | [`policy/plugins/`](../../../../policy/plugins/) (PROPOSED) | PROPOSED |

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 14. Related connectors and pipelines

CONFIRMED (Directory Rules §7.3, §7.4): Connectors fetch and admit; pipelines transition lifecycle phases.

| Stage | Path (CONFIRMED canonical home) | Status for this product |
|---|---|---|
| Source fetch + admission (IIIF + Allmaps) | `connectors/loc/historic-maps/` | **PROPOSED** — uses conditional GET (Pass 10 C3-01); cache keyed by IIIF manifest IRI + Allmaps annotation IRI |
| Ingest | `pipelines/ingest/` | PROPOSED — IIIF manifest + Allmaps annotation byte capture + digests |
| Normalize | `pipelines/normalize/` | PROPOSED — extract GCPs from Allmaps annotation; compute initial RMS |
| Validate | `pipelines/validate/` | PROPOSED — RMS threshold, GCP completeness, rights presence, attribution test |
| Catalog | `pipelines/catalog/` | PROPOSED — STAC Item + DCAT row + PROV chain |
| Tile | `pipelines/publish/` (warped PMTiles render) | PROPOSED — deterministic PMTiles build per `ML-064-038` / `ML-064-039` |
| Triplets / graph projection | `pipelines/triplets/` | PROPOSED — bind to E55 Type (`map: historic`) and to Place E53 via warped-bbox context |
| Watchers | `pipelines/watchers/` | PROPOSED — periodic re-harvest for IIIF / Allmaps annotation revisions |
| Declarative spec | `pipeline_specs/cross-domain/loc-historic-maps/` | PROPOSED — cross-domain because consumers span Settlements, Roads, Archaeology, People/Land |

NEEDS VERIFICATION (Directory Rules §13.5 anti-pattern *Source alias drift risk*): the connector folder name must align with the source id under `data/registry/sources/`.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 15. Examples (illustrative only)

> [!NOTE]
> Examples below are **illustrative**, not authoritative. Authoritative samples live under [`_examples/`](./_examples/) and the fixture lanes — do not treat any block on this page as a contract.

See [`_examples/stac-item-example.json`](./_examples/stac-item-example.json) and [`_examples/historic-map-overlay-manifest-example.json`](./_examples/historic-map-overlay-manifest-example.json).

<details>
<summary><strong>Illustrative STAC Item sketch with georeference provenance (DO NOT COPY VERBATIM)</strong></summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "<PROPOSED collection-id>/<map-item-id>",
  "collection": "<PROPOSED kfm-<org>-loc-historic-maps>",
  "geometry": { "type": "Polygon", "coordinates": [/* warped bbox in EPSG:4326 */] },
  "bbox": [/* warped bbox */],
  "properties": {
    "datetime": null,
    "start_datetime": "<source_time_lower YYYY-MM-DDTHH:MM:SSZ>",
    "end_datetime": "<source_time_upper YYYY-MM-DDTHH:MM:SSZ>",
    "title": "<map title>",
    "license": "<SPDX or rights statement IRI — NEEDS VERIFICATION per item>",
    "kfm:provenance": {
      "spec_hash": "sha256:<...>",
      "evidence_bundle_ref": "kfm://evidence/<digest>",
      "run_record_ref": "kfm://run/<run-id>",
      "audit_ref": "kfm://audit/<attestation-id>",
      "policy_digest": "sha256:<...>"
    },
    "kfm:georeference": {
      "iiif_manifest_digest": "sha256:<...>",
      "allmaps_annotation_digest": "sha256:<...>",
      "warp_method": "polynomial-1",
      "gcps_count": 0,
      "gcp_source_breakdown": { "allmaps_community": 0, "kfm_editor": 0, "automated": 0 },
      "rms_error_pixels": 0.0,
      "rms_error_meters": 0.0,
      "representation_receipt_ref": "kfm://receipt/representation/<digest>",
      "reality_boundary_note_ref": "kfm://note/reality-boundary/<digest>"
    }
  },
  "assets": {
    "iiif_manifest": {
      "href": "<IIIF Presentation Manifest URL>",
      "type": "application/json",
      "roles": ["metadata", "iiif"],
      "file:checksum": "sha256:<...>"
    },
    "allmaps_annotation": {
      "href": "<Allmaps annotation URL>",
      "type": "application/ld+json",
      "roles": ["data", "georeference"],
      "file:checksum": "sha256:<...>"
    },
    "warped_pmtiles": {
      "href": "<PMTiles render URL>",
      "type": "application/vnd.pmtiles",
      "roles": ["data", "tiles", "visual"],
      "file:checksum": "sha256:<...>"
    }
  },
  "links": [
    { "rel": "attestation", "href": "kfm://evidence/<digest>", "title": "EvidenceBundle (KFM)" },
    { "rel": "kfm:representation-receipt", "href": "kfm://receipt/representation/<digest>" },
    { "rel": "kfm:reality-boundary-note", "href": "kfm://note/reality-boundary/<digest>" }
  ]
}
```

</details>

<details>
<summary><strong>Illustrative HistoricMapOverlayManifest sketch (PROPOSED — DO NOT COPY VERBATIM)</strong></summary>

```json
{
  "@context": "<kfm:historic-map-overlay-manifest JSON-LD context — PROPOSED>",
  "overlay_id": "<canonical id>",
  "version": "v1",
  "spec_hash": "sha256:<...>",
  "iiif_manifest_url": "<IIIF Presentation Manifest URL>",
  "iiif_manifest_digest": "sha256:<...>",
  "iiif_rights_statement": "<rights statement IRI or text — NEEDS VERIFICATION>",
  "allmaps_annotation_url": "<Allmaps annotation URL>",
  "allmaps_annotation_digest": "sha256:<...>",
  "allmaps_annotation_rights": "<rights — NEEDS VERIFICATION>",
  "gcps": [
    { "pixel": [0, 0], "world": [0.0, 0.0], "source": "allmaps_community", "confidence": null }
  ],
  "warp": {
    "method": "polynomial-1",
    "parameters": { /* method-specific */ },
    "rms_error_pixels": 0.0,
    "rms_error_meters": 0.0,
    "threshold_pixels": null,
    "threshold_meters": null,
    "passes_threshold": null
  },
  "rendered_artifact_ref": {
    "tile_artifact_manifest": "<TileArtifactManifest URL>",
    "digest": "sha256:<...>"
  },
  "representation_receipt_ref": "kfm://receipt/representation/<digest>",
  "reality_boundary_note_ref": "kfm://note/reality-boundary/<digest>",
  "plugin_allowlist_ref": "kfm://policy/plugins/<digest>",
  "release_state": "candidate"
}
```

</details>

<details>
<summary><strong>Illustrative Evidence Drawer payload fragment (DO NOT COPY VERBATIM)</strong></summary>

```json
{
  "feature_id": "<...>",
  "layer_id": "<historic-overlay layer id>",
  "evidence_bundle_refs": ["kfm://evidence/<digest>"],
  "source_summary": {
    "publisher": "Library of Congress — Geography and Map Division",
    "annotator": "Allmaps community",
    "iiif_rights_statement": "<...>",
    "map_date": "<source_time interval>"
  },
  "citations": [/* ... */],
  "policy_state": "ALLOW",
  "release_state": "PUBLISHED",
  "limitations": [
    "Warped overlay — interpretive representation, not modern positional truth.",
    "RMS error: <X> meters; warp method: polynomial-1; GCPs: <N>."
  ],
  "kfm:reality_boundary_note": "<note text shown to user>",
  "kfm:representation_receipt_ref": "kfm://receipt/representation/<digest>"
}
```

</details>

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 16. Open questions

- **OPEN-HM-01** — Set the **RMS-error threshold** (pixels and/or meters) for promotion. Above-threshold overlays go to "preview only" or quarantine. The corpus names the requirement (`KFM-P9-FEAT-0016`, `ML-064-103`) but does not pin a value. Candidate ADR.
- **OPEN-HM-02** — Should an explicit **per-pixel uncertainty surface** be rendered alongside the warped overlay, or is the per-Item RMS sufficient?
- **OPEN-HM-03** — Confirm the **`HistoricMapOverlayManifest`** schema home: `schemas/contracts/v1/map/` is the default per ADR-0001; alternative is `schemas/contracts/v1/representation/` if a new receipt-class lane lands per ADR-S-03.
- **OPEN-HM-04** — Resolve the corpus's own NEEDS-VERIFICATION question (`KFM-P9-FEAT-0016`): *"Should historic overlays default to **contextual** evidence rather than **direct geometry** evidence?"* This page defaults to contextual; an ADR should pin the answer.
- **OPEN-HM-05** — Resolve the corpus's own NEEDS-VERIFICATION question (`KFM-P9-FEAT-0016`): *"How should KFM disclose georeferencing error for warped historic maps?"* — UI vocabulary, badge thresholds, Evidence Drawer text.
- **OPEN-HM-06** — Pin the **plugin allowlist** policy file (`policy/plugins/` PROPOSED) and the SRI / version-pin convention for Allmaps `WarpedMapLayer`.
- **OPEN-HM-07** — Confirm re-harvest cadence and the policy for handling **Allmaps annotation revisions** (a community-edited annotation can change without notice).
- **OPEN-HM-08** — Confirm domain lane: `pipeline_specs/cross-domain/loc-historic-maps/` (PROPOSED) vs. per-consuming-domain scoping.
- **OPEN-HM-09** — Confirm rights status — both LoC G&M item rights and Allmaps annotation rights — per snapshot. Federal-domain default MUST NOT be applied silently.
- **OPEN-HM-10** — Confirm whether this product warrants its own **STAC Collection** or shares one with sibling `loc` products.
- **OPEN-HM-11** — Pin namespace choice (`kfm:` vs `ks-kfm:`) — tracked as **OPEN-DSC-03**.
- **OPEN-HM-12** — Resolve docs filename naming (`PROV.md` vs `PROVENANCE.md`) — tracked as **ADR-S-06**.
- **OPEN-HM-13** — Confirm whether `docs/sources/catalog/loc/` is the established docs convention for source product pages, or whether they live under `docs/dossiers/sources/`.

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## 17. Related docs

- [`./README.md`](./README.md) — `loc` source family overview
- [`./IDENTITY.md`](./IDENTITY.md) — collection-id pattern, namespace decisions for the `loc` family
- [`./RIGHTS-AND-SENSITIVITY-MAP.md`](./RIGHTS-AND-SENSITIVITY-MAP.md) — rights and sensitivity disposition for `loc` products
- [`./LCNAF.md`](./LCNAF.md) — sibling LoC product (name authority); LCNAF anchors creators / cartographers of historic maps
- [`./LCSH.md`](./LCSH.md) — sibling LoC product (subject headings); LCSH classifies the topical / geographic subject of a historic map
- [`./CHRONICLING-AMERICA.md`](./CHRONICLING-AMERICA.md) — sibling LoC product (recall-layer newspapers)
- [`./_examples/stac-item-example.json`](./_examples/stac-item-example.json) — minimal STAC + `kfm:provenance` + `kfm:georeference` shape
- [`./_examples/historic-map-overlay-manifest-example.json`](./_examples/historic-map-overlay-manifest-example.json) — `HistoricMapOverlayManifest` shape
- [`../README.md`](../README.md) — `docs/sources/catalog/` overview
- [`../../../standards/STAC_KFM_PROFILE.md`](../../../standards/STAC_KFM_PROFILE.md) — KFM STAC profile (namespace, extensions, attestation hook)
- [`../../../standards/PROV.md`](../../../standards/PROV.md) — PROV-O / PAV provenance profile *(filename pending ADR-S-06)*
- [`../../../standards/PLUGIN_ALLOWLIST.md`](../../../standards/PLUGIN_ALLOWLIST.md) — plugin-allowlist convention *(path PROPOSED)*
- [`../../../doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement law
- [`../../../adr/ADR-0001-schema-home.md`](../../../adr/ADR-0001-schema-home.md) — schema-home rule *(path PROPOSED)*

[↑ Back to top](#loc-geography-and-map-division--historic-maps)

---

## Appendix · Field expectations and disposition matrix

<details>
<summary><strong>Expand: per-field expectations summary</strong></summary>

| Concern | Field / artifact | Required? | Status |
|---|---|---|---|
| Identity | STAC `id`, `collection`; overlay `overlay_id` | MUST | PROPOSED pattern: `kfm-<org>-<product>` |
| Time | `start_datetime` / `end_datetime` (source interval), `retrieval_time` | MUST | PROPOSED |
| Geometry | `geometry`, `bbox` (warped) | MUST | PROPOSED |
| Warp method | `kfm:georeference.warp_method` | MUST | PROPOSED |
| GCPs | `kfm:georeference.gcps[]`, `gcp_source_breakdown` | MUST | PROPOSED (`KFM-P9-FEAT-0016`) |
| RMS error | `rms_error_pixels`, `rms_error_meters` against threshold | MUST | PROPOSED (`KFM-P9-FEAT-0016`, `ML-064-103`) |
| IIIF rights | preserved as STAC asset metadata | MUST | CONFIRMED (`KFM-P9-PROG-0074`) |
| Allmaps rights | preserved as STAC asset metadata | MUST | CONFIRMED (`KFM-P9-PROG-0074`) |
| License | DCAT `dct:license` (SPDX or rights statement IRI) | MUST | NEEDS VERIFICATION per item |
| Provenance | `kfm:provenance.{spec_hash, evidence_bundle_ref, run_record_ref, audit_ref, policy_digest}` | MUST | CONFIRMED shape (Pass 10 C4-01) |
| Asset integrity | `file:checksum` on IIIF manifest, Allmaps annotation, PMTiles render | MUST | CONFIRMED shape (Pass 10 C4-01) |
| **Representation Receipt** | `representation_receipt_ref` | MUST | CONFIRMED concept (CDB §24.7); shape PROPOSED |
| **Reality Boundary Note** | `reality_boundary_note_ref` | MUST | CONFIRMED term (§17 Planetary/3D term, applied here) |
| Plugin governance | allowlist entry + SRI / version pin | MUST | CONFIRMED requirement (`ML-064-037`) |
| Attribution test | CI test for LoC + Allmaps attribution in Story Node | MUST | CONFIRMED requirement (`ML-064-037`) |
| CARE handling | `kfm:care` block on STAC / DCAT for sensitive overlays | when applicable | CONFIRMED extension (Pass 10 C15-02) |
| Catalog closure | STAC + DCAT + PROV + EvidenceBundle + receipt + rollback target | MUST before publish | CONFIRMED gate (`KFM-P1-IDEA-0020`) |
| AI behavior | ABSTAIN on modern positional questions about the warped overlay | MUST | CONFIRMED anti-pattern register (synthetic-as-observed) |

</details>

<details>
<summary><strong>Expand: disposition by source-role family</strong></summary>

| KFM source role | Applies to this product? | Notes |
|---|---|---|
| `observed` | **No** | The original map was an observed product in its day, but the warped overlay is interpretive |
| `regulatory` | No | Not a regulatory authority |
| `modeled` | **Marginal** | The warp is a geometric model with parameters; `RepresentationReceipt` is the correct receipt, not `ModelRunReceipt` (see OPEN-HM-04) |
| `aggregate` | No | Not aggregate |
| `administrative` | **Sometimes** | Plat books and General Land Office maps were administrative artifacts; flag where applicable |
| `candidate` | **Yes** during admission | New harvests / re-annotations are candidates until validated |
| `synthetic` | **Marginal** | The warped overlay is "synthetic" in the Reality-Boundary sense; the `Reality Boundary Note` is the controlling artifact |
| **`context`** *(KFM-specific role, PROPOSED default)* | **Yes — primary role** | Until OPEN-HM-04 is settled, overlays default to **contextual** evidence (Story Node, Focus Mode context) and do not anchor positional claims |

</details>

<details>
<summary><strong>Expand: worked rows for overlay outcomes (illustrative)</strong></summary>

| Case | Outcome | Required artifact |
|---|---|---|
| IIIF rights clear, Allmaps annotation clear, RMS below threshold, GCPs sufficient | Promote to PUBLISHED; surface in Story Node panel | full `HistoricMapOverlayManifest` + Representation Receipt + Reality Boundary Note |
| IIIF rights clear, RMS **above threshold** | Downgrade to "preview only" or quarantine; do not render in public Story Nodes | quarantine record + steward review |
| IIIF rights uncertain | Deny publication; route to rights-clearance review | `PolicyDecision` (DENY) + `ReviewRecord` |
| Allmaps annotation revised after KFM cache | Trigger re-warp watcher; mark dependent overlays stale until re-validated | stale-state badge per §24.8 |
| Plugin version bump without ADR | Catalog-closure gate fails closed | block release; require ADR or per-root README update |
| Overlay depicts Indigenous places with outdated naming | CARE flag + steward review + interpretive caveat in Evidence Drawer; retain for context with explicit caveat | `kfm:care` block + `ReviewRecord` |
| User asks Focus Mode for modern positional claim sourced to the overlay | Focus Mode returns **ABSTAIN** with reason "interpretive overlay; not modern positional truth" | `AIReceipt` with abstain reason |

</details>

---

> [!NOTE]
> **Truth posture:** Every implementation-shaped claim on this page is **PROPOSED** or **NEEDS VERIFICATION** until a mounted-repo inspection, an accepted ADR, and the relevant per-root README review confirm the placements. Doctrine references (Directory Rules §§0, 5–9; ADR-0001; CDB §16; §24.7 receipts; §24.8 stale-state; §17 Planetary/3D ubiquitous language; Pass 10 C4-01, C4-05, C8-03, C15-02 / C15-03; `KFM-P9-FEAT-0016`; `KFM-P9-PROG-0074`; `ML-064-036`; `ML-064-037`; `ML-064-103`; `KFM-P14-PROG-0033`; `KFM-P1-IDEA-0020`) are **CONFIRMED** as doctrinal references; their implementation in this repo is **NEEDS VERIFICATION**.

---

**Related docs:** [loc family README](./README.md) · [IDENTITY](./IDENTITY.md) · [RIGHTS-AND-SENSITIVITY-MAP](./RIGHTS-AND-SENSITIVITY-MAP.md) · [LCNAF](./LCNAF.md) · [LCSH](./LCSH.md) · [Chronicling America](./CHRONICLING-AMERICA.md) · [STAC KFM Profile](../../../standards/STAC_KFM_PROFILE.md) · [Plugin Allowlist](../../../standards/PLUGIN_ALLOWLIST.md) · [Directory Rules](../../../doctrine/directory-rules.md)

*Last updated: 2026-05-22 · Doc version: v0.2 · Status: PROPOSED scaffold*

[↑ Back to top](#loc-geography-and-map-division--historic-maps)
