<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/stac-eo
title: STAC EO — KFM Conformance Profile
type: standard
version: v0.1
status: draft
owners: <TBD — standards stewards>
created: 2026-05-14
updated: 2026-05-14
policy_label: public
related: [docs/standards/README.md, docs/standards/STAC_KFM_PROFILE.md, docs/standards/DCAT.md, docs/standards/PROV.md, docs/architecture/contract-schema-policy-split.md, docs/adr/README.md, schemas/contracts/v1/, policy/]
tags: [kfm, standards, stac, eo, remote-sensing]
notes:
  - "PROPOSED-status conformance profile; depends on kfm-stac-profile-v1 namespace ADR."
  - "All repo path claims marked PROPOSED until repo inspection lands."
[/KFM_META_BLOCK_V2] -->

# STAC EO — KFM Conformance Profile

How KFM uses the SpatioTemporal Asset Catalog (STAC) **Electro-Optical (EO) extension** to catalog remote-sensing imagery while keeping evidence, provenance, sensitivity, review state, and release state inspectable.

![Status](https://img.shields.io/badge/status-draft-orange)
![Authority](https://img.shields.io/badge/authority-standards--profile-blue)
![STAC](https://img.shields.io/badge/STAC-1.0.0%20core-informational)
![Profile](https://img.shields.io/badge/profile-kfm--stac--profile--v1-success)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)
![Lifecycle](https://img.shields.io/badge/lifecycle-governed-informational)
![Last Updated](https://img.shields.io/badge/updated-2026--05--14-lightgrey)

> [!IMPORTANT]
> This profile is **PROPOSED**. It documents how KFM intends to apply STAC core + EO extension. The `kfm:` namespace, the `kfm-stac-profile-v1` schema home, and CI gate wiring remain **NEEDS VERIFICATION** until a mounted repository and an accepted ADR confirm them.

---

## Quick links

- [Purpose](#purpose)
- [Scope and non-scope](#scope-and-non-scope)
- [How this fits in KFM standards](#how-this-fits-in-kfm-standards)
- [STAC core requirements KFM observes](#stac-core-requirements-kfm-observes)
- [Required and companion extensions for EO assets](#required-and-companion-extensions-for-eo-assets)
- [KFM property namespace](#kfm-property-namespace)
- [KFM-required Item properties](#kfm-required-item-properties)
- [Asset roles and integrity](#asset-roles-and-integrity)
- [Link relations](#link-relations)
- [Provenance threading](#provenance-threading)
- [Validation gates](#validation-gates)
- [Example STAC EO Item (illustrative)](#example-stac-eo-item-illustrative)
- [Anti-patterns](#anti-patterns)
- [Open questions and verification backlog](#open-questions-and-verification-backlog)
- [Related docs](#related-docs)

---

## Purpose

CONFIRMED doctrine. STAC is the de facto JSON catalog vocabulary for spatiotemporal assets, and threading KFM's provenance through STAC keeps KFM portable across the broader geospatial tooling ecosystem (`pgstac`, `stac-fastapi`, `pystac-client`, STAC Browser, TiTiler, Planetary Computer). The EO extension covers electro-optical sensor characteristics — bands, cloud cover, view geometry — that imagery products require to be useful and inspectable.

This document specifies how the **EO surface of KFM's STAC profile** is constructed: which STAC extensions accompany EO, which KFM-namespaced properties are required, which link relations carry provenance, and which gates a record must pass before it can be promoted to `data/catalog/stac/` or published.

> [!NOTE]
> KFM does **not fork STAC**. It remains STAC 1.0.0 compliant and extends via namespaced properties and a profile schema (`kfm-stac-profile-v1`). Governance lives in the profile and in policy bundles, not in altered core fields.

---

## Scope and non-scope

| In scope | Out of scope |
|---|---|
| EO-extension fields KFM uses on Items and Collections | DCAT distributions for non-spatial datasets (see `docs/standards/DCAT.md`) |
| Companion extensions for imagery: `projection`, `raster`, `view`, `processing`, `checksum`, `scientific`, `version` | The Darwin Core hybrid for biodiversity occurrences (see `docs/standards/STAC-DwC.md` — PROPOSED) |
| Required KFM governance fields on EO records | The full `kfm-stac-profile-v1` schema definition (see `docs/standards/STAC_KFM_PROFILE.md` — PROPOSED) |
| Provenance threading via `kfm:provenance`, `links[]`, and signed receipts | Tile-publication pipelines (PMTiles, COG-tiling release path) |
| Asset roles, integrity, and naming for EO products | Authoritative semantic truth — that remains in `EvidenceBundle`, `DecisionEnvelope`, claim graph, and `ReleaseManifest` |

---

## How this fits in KFM standards

````mermaid
flowchart TB
  A[STAC Core 1.0.0]:::core --> B[Projection]
  A --> C[Raster]
  A --> D[EO ← this document]:::focus
  A --> E[View]
  A --> F[Processing]
  A --> G[Checksum]
  A --> H[Scientific]
  A --> I[Version]
  A --> J["kfm-stac-profile-v1
  (governance overlay)"]:::kfm

  J --> K[EvidenceRef / EvidenceBundle]
  J --> L[Policy posture]
  J --> M[Release state]
  J --> N[Correction lineage]
  J --> O[Review gates]
  J --> P[Public-safe exposure]

  classDef core fill:#eef,stroke:#446,stroke-width:1px
  classDef focus fill:#fec,stroke:#a60,stroke-width:2px
  classDef kfm fill:#efe,stroke:#262,stroke-width:1px
````

CONFIRMED doctrine. The EO extension is one slice of the recommended **KFM STAC stack**. The KFM governance overlay rides alongside core and standard extensions; it does not replace them. Conformance to this EO profile implies conformance to STAC core and to `kfm-stac-profile-v1`.

[Back to top](#stac-eo--kfm-conformance-profile)

---

## STAC core requirements KFM observes

CONFIRMED doctrine. Every STAC Item KFM publishes — EO or otherwise — must carry the core fields. KFM enforces these as part of the shape gate before any EO-specific or KFM-specific field is checked.

| Core surface | Required fields | KFM relevance |
|---|---|---|
| Identity | `id`, `type`, `stac_version` | Stable `EvidenceRef` anchoring; validator/API behavior |
| Spatial | `geometry`, `bbox` | Map-first query integrity |
| Temporal | `properties.datetime` **or** `start_datetime` / `end_datetime` | Time-aware claims |
| Assets | `assets.*.href`, `assets.*.type` | Durable artifact resolution |
| Navigation | `links[]` | Traversable lineage |
| Collection scoping | `collection` (on Items) | Governance scoping per dataset family |
| Extensions | `stac_extensions[]` | Validator compatibility |
| Lifecycle posture | `properties.license`, `properties.created`, `properties.updated` | Rights and freshness |

> [!TIP]
> When EO Items represent a single acquisition, use `properties.datetime`. When the EO Item aggregates a window (e.g., a daily mosaic, a multi-pass composite), use `start_datetime` and `end_datetime` together with `datetime: null` rather than collapsing to a single timestamp.

---

## Required and companion extensions for EO assets

PROPOSED. EO Items in KFM SHOULD declare the EO extension and the companion extensions that imagery products need to be honestly described. Inclusion of an extension URL in `stac_extensions[]` is what tells validators and STAC API servers to apply the extension's schemas.

| Extension | Role on EO items | Status in KFM |
|---|---|---|
| `eo` | Bands (name, common name, wavelength), `eo:cloud_cover`, snow cover | **Required** for any optical-imagery Item |
| `projection` | Native CRS, transform, `proj:shape`, `proj:bbox` | **Required** for raster assets |
| `raster` | Per-band data type, nodata, statistics, scale/offset | **Required** for raster assets |
| `view` | Sun/sensor geometry: azimuth, zenith, off-nadir | Recommended where relevant |
| `processing` | `processing:facility`, `processing:version`, `processing:lineage` | Recommended; mirrors KFM run metadata |
| `checksum` | `checksum:multihash` (BLAKE3 preferred; SHA-256 compatibility) | **Required** on every asset |
| `scientific` | DOIs, citations for scientific products | Recommended when applicable |
| `version` | Versioning of the Item itself | Recommended |

> [!NOTE]
> **NEEDS VERIFICATION** — exact pinned versions of each extension schema URL (e.g., `eo/v1.1.0/schema.json`) MUST be resolved against the upstream `stac-extensions` registry at the time the profile is cut, and frozen in `kfm-stac-profile-v1`. Do not pin versions from memory.

[Back to top](#stac-eo--kfm-conformance-profile)

---

## KFM property namespace

> [!CAUTION]
> **Open governance question — PROPOSED.** The KFM corpus is split between two candidate namespace prefixes for STAC properties and link relations:
>
> - `kfm:` — short, KFM-global, aligns with STAC extension conventions
> - `ks-kfm:` — Kansas-scoped, more explicit
>
> This profile **proposes `kfm:`** as the working namespace, on the strength of compactness, stability, and convention. The final binding requires an accepted ADR (e.g., `docs/adr/ADR-NNNN-kfm-stac-namespace.md`, PROPOSED) and must be declared in Collection `summaries` and in the `kfm-stac-profile-v1` schema. Until then, all `kfm:*` field names below are subject to namespace migration.

All KFM-specific properties on STAC Items and Collections live under a single namespace. Custom fields must be either (a) declared as part of an extension referenced in `stac_extensions[]`, or (b) carried as `Link` objects, to avoid being silently dropped by strict STAC clients.

---

## KFM-required Item properties

PROPOSED. The fields below are the governance-posture fields that `kfm-stac-profile-v1` requires for any EO Item that is a candidate for catalog promotion or release.

| Property | Type | Meaning |
|---|---|---|
| `kfm:spec_hash` | string (`sha256:…` or `blake3:…`) | Deterministic semantic integrity of the canonicalized record |
| `kfm:evidence_ref` | URI (`kfm://evidence/…`) | Pointer that resolves to an `EvidenceBundle` |
| `kfm:evidence_bundle` | URI (`kfm://bundle/…`) | Direct bundle reference where pre-resolved |
| `kfm:run_receipt` | URI (`kfm://run/…` or `dsse://sha256:…`) | Signed `RunReceipt` that produced this record |
| `kfm:source_role` | enum (below) | What kind of input this Item represents |
| `kfm:rights_status` | enum (below) | Rights posture for downstream gates |
| `kfm:sensitivity` | enum (below) | Sensitivity disposition |
| `kfm:review_state` | enum (below) | Review gate state |
| `kfm:release_state` | enum (below) | Release-lifecycle position |
| `kfm:provenance` | object | Provenance join point (see [Provenance threading](#provenance-threading)) |

### Enumerations

CONFIRMED doctrine in source materials. These enumerations mirror the wider KFM object family; preserve casing exactly.

<details>
<summary><strong>Click to expand: enumerations for source_role, rights_status, sensitivity, review_state, release_state</strong></summary>

**`kfm:source_role`**

````text
observation
derived
simulation
regulatory
interpretation
ai_generated
reference
````

**`kfm:rights_status`**

````text
public
open
controlled
restricted
unknown
````

**`kfm:sensitivity`**

````text
public
generalize
restricted
review_required
````

**`kfm:review_state`**

````text
draft
in_review
approved
rejected
````

**`kfm:release_state`**

````text
unreleased
candidate
released
withdrawn
corrected
superseded
````

</details>

> [!IMPORTANT]
> Records with `kfm:release_state: released` and `kfm:sensitivity: restricted` MUST be denied at the policy gate. This combination is one of the four canonical fail-closed conditions in the publication policy bundle.

[Back to top](#stac-eo--kfm-conformance-profile)

---

## Asset roles and integrity

CONFIRMED doctrine. STAC asset `roles` tell consumers — including the MapLibre shell, the Evidence Drawer, and external clients — what each asset is *for*. EO Items typically carry several assets per scene; each must declare its roles and integrity.

| Common role | Used for | Notes |
|---|---|---|
| `data` | The primary observation (e.g., surface-reflectance GeoTIFF / COG) | One per band group or per stacked product |
| `thumbnail` | Quicklook image (PNG/JPG) | Should not be the only asset with a thumbnail role |
| `overview` | Lower-resolution preview | Optional |
| `metadata` | Sidecar metadata documents (XML, JSON) | Carries upstream provider metadata |
| `qa` | Cloud/QA mask | Required when the EO product ships a QA layer |
| `visual` | Web-friendly RGB rendering | Distinct from `data` rasters |

PROPOSED additional asset properties:

| Asset property | Purpose |
|---|---|
| `checksum:multihash` | Per-file integrity (BLAKE3 preferred; SHA-256 for compatibility) |
| `kfm:spec_hash` | Optional — per-asset spec_hash when the asset has its own deterministic descriptor |
| `kfm:temporal` | Optional asset-level `{start, end}` when an asset's valid time differs from `properties.datetime` |
| `alternate` | Mirror locations (e.g., S3 canonical + HTTPS edge URL) |

> [!WARNING]
> Asset `href` values MUST NOT resolve to `data/raw/`, `data/work/`, or `data/quarantine/`. Public STAC clients consume governed surfaces only. A released STAC Item pointing into RAW or WORK is a trust-membrane violation regardless of whether the asset bytes are technically reachable.

---

## Link relations

PROPOSED. KFM extends standard STAC link relations with a small set of governance-bearing relations. Standard `rel` values (`self`, `parent`, `root`, `collection`, `item`) are preserved unchanged.

| `rel` | Purpose |
|---|---|
| `derived_from` | Source lineage — input Items, scenes, or RunReceipts |
| `prov` | Pointer to provenance bundle (`EvidenceBundle`) |
| `evidence` | Direct `EvidenceBundle` resolution |
| `receipt` | Signed `RunReceipt` (DSSE/cosign envelope) |
| `correction` | `CorrectionNotice` (if this Item has been corrected) |
| `rollback` | `RollbackCard` |
| `policy` | Governing `PolicyDecision` record |
| `release-manifest` | `ReleaseManifest` controlling this record's release |

> [!TIP]
> Prefer `Link` objects over free-form top-level properties for cross-Item provenance. STAC API search backends (`/search`) traverse `links[]`; unknown top-level keys are silently dropped by strict clients.

[Back to top](#stac-eo--kfm-conformance-profile)

---

## Provenance threading

CONFIRMED doctrine. EO Items carry a `properties.kfm:provenance` block that is the **join point** between the STAC item and the rest of KFM's evidence machinery. The block contains the small set of references that allow a validator, a reviewer, or a downstream consumer to reconstruct what made this record.

````json
"kfm:provenance": {
  "spec_hash": "sha256:…",
  "evidence_bundle_ref": "kfm://bundle/7f9a…",
  "run_record_ref": "kfm://run/aa31…",
  "audit_ref": "kfm://audit/SLSA-OPA/2c17…",
  "policy_digest": "sha256:…"
}
````

| Field | Resolves to |
|---|---|
| `spec_hash` | The canonicalized-record fingerprint; recomputed and checked by the spec-hash-match gate |
| `evidence_bundle_ref` | Content-addressed JSON-LD `EvidenceBundle` containing receipts and validations |
| `run_record_ref` | The `RunReceipt` (or pre-RAW `event_run_receipt`) that produced this record |
| `audit_ref` | Signed SLSA / OPA attestations |
| `policy_digest` | The policy bundle digest applied at promotion |

Per-asset integrity is recorded separately via `checksum:multihash` on each asset. The provenance block governs the Item; the checksum entries govern the bytes.

````mermaid
flowchart LR
  I[STAC EO Item] -- kfm:provenance --> P[(provenance block)]
  P -- evidence_bundle_ref --> EB[EvidenceBundle<br/>JSON-LD, content-addressed]
  P -- run_record_ref --> RR[RunReceipt<br/>DSSE-signed]
  P -- audit_ref --> AA[SLSA / OPA attestations]
  P -- policy_digest --> PD[Policy bundle digest]
  I -- assets[].checksum:multihash --> CK[Per-asset integrity]
  I -- links[rel=prov] --> EB
  I -- links[rel=receipt] --> RR
  EB -. resolves .-> Claims[Reconstructable claims]
````

> [!IMPORTANT]
> The STAC Item is the **discovery envelope**. The `EvidenceBundle` is the **reconstructable truth object**. If the catalog disagrees with the bundle, the bundle wins; that is the cite-or-abstain posture of KFM applied to spatial data.

[Back to top](#stac-eo--kfm-conformance-profile)

---

## Validation gates

PROPOSED gate architecture. EO records pass through three validation layers in order. Each layer fails closed; downstream layers do not execute if an upstream layer denies.

````mermaid
flowchart LR
  Author([EO Item authored]) --> L1
  L1[Layer 1 — STAC core + extension validation] --> L2
  L2[Layer 2 — KFM profile schema validation] --> L3
  L3[Layer 3 — Policy validation OPA / Conftest] --> Promote([Catalog promotion])

  L1 -. fail .-> Q1[Quarantine - shape]
  L2 -. fail .-> Q2[Quarantine - profile]
  L3 -. deny .-> Q3[Quarantine - policy]
````

| Layer | Checks | Default failure outcome |
|---|---|---|
| **1 — STAC** | Core fields, extension schemas, `stac_extensions[]` consistency, asset media types | ERROR → quarantine |
| **2 — KFM profile** | Required `kfm:*` fields present, enums valid, `kfm:spec_hash` format, URI shapes, release/review consistency | ERROR → quarantine |
| **3 — Policy** | Admissibility, sensitivity, release-state legality, source-role rules, EvidenceRef resolution | DENY → fail-closed; never silently promoted |

### Example deny conditions (Layer 3)

PROPOSED policy rules drawn from KFM doctrine. Final wording lives in `policy/stac/publication.rego`.

````rego
# Restricted content cannot be in 'released' state
DENY if:
  input.properties["kfm:sensitivity"] == "restricted"
  and input.properties["kfm:release_state"] == "released"

# Missing evidence pointer
DENY if:
  missing(input.properties["kfm:evidence_bundle"])

# Asset path leaks into raw lifecycle phase
DENY if:
  input.assets[_].href startswith "s3://kfm/raw/"

# AI-generated record without lineage link
DENY if:
  input.properties["kfm:source_role"] == "ai_generated"
  and not any_link(input, "derived_from")
````

> [!NOTE]
> **NEEDS VERIFICATION** — actual policy paths, the Rego function `any_link`, and the precise asset-path prefixes depend on the mounted repo's `data/raw/` storage convention. Treat the snippets above as illustrative until `policy/stac/publication.rego` lands.

[Back to top](#stac-eo--kfm-conformance-profile)

---

## Example STAC EO Item (illustrative)

The example below is **illustrative**. It is sketched from KFM doctrine, not extracted from a released catalog record. Field values are placeholders.

<details>
<summary><strong>Click to expand: minimal KFM-flavored STAC EO Item (illustrative)</strong></summary>

````json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "stac_extensions": [
    "https://stac-extensions.github.io/eo/v1.1.0/schema.json",
    "https://stac-extensions.github.io/projection/v1.1.0/schema.json",
    "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
    "https://stac-extensions.github.io/checksum/v1.0.0/schema.json",
    "https://stac-extensions.github.io/processing/v1.1.0/schema.json",
    "https://kfm.example.org/stac/kfm-stac-profile-v1/schema.json"
  ],
  "id": "kfm-landsat-c2l2-LC09-2025-07-01-029033",
  "collection": "kfm-landsat-c2l2-sr",
  "geometry": { "type": "Polygon", "coordinates": [[[/* … */]]] },
  "bbox": [-99.50, 38.10, -98.20, 39.30],
  "properties": {
    "datetime": "2025-07-01T16:22:09Z",
    "license": "PDDL-1.0",
    "created": "2025-07-02T03:11:42Z",
    "updated": "2025-07-02T03:11:42Z",

    "eo:cloud_cover": 12,
    "eo:snow_cover": 0,

    "proj:epsg": 32614,
    "proj:shape": [7821, 7691],

    "processing:facility": "kfm-eo-watchers",
    "processing:version": "veg-anomaly@0.4.0",

    "kfm:spec_hash": "sha256:<placeholder>",
    "kfm:evidence_ref": "kfm://evidence/0b4c…",
    "kfm:evidence_bundle": "kfm://bundle/7f9a…",
    "kfm:run_receipt": "kfm://run/aa31…",
    "kfm:source_role": "observation",
    "kfm:rights_status": "open",
    "kfm:sensitivity": "public",
    "kfm:review_state": "approved",
    "kfm:release_state": "released",
    "kfm:provenance": {
      "spec_hash": "sha256:<placeholder>",
      "evidence_bundle_ref": "kfm://bundle/7f9a…",
      "run_record_ref": "kfm://run/aa31…",
      "audit_ref": "kfm://audit/SLSA-OPA/2c17…",
      "policy_digest": "sha256:<placeholder>"
    }
  },
  "assets": {
    "sr_red": {
      "href": "s3://kfm/published/eo/landsat/2025/029033/LC09_…/sr_red.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "reflectance"],
      "eo:bands": [{ "name": "B4", "common_name": "red", "center_wavelength": 0.654 }],
      "checksum:multihash": "blake3-256-u:<placeholder>"
    },
    "sr_nir": {
      "href": "s3://kfm/published/eo/landsat/2025/029033/LC09_…/sr_nir.tif",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "reflectance"],
      "eo:bands": [{ "name": "B5", "common_name": "nir", "center_wavelength": 0.865 }],
      "checksum:multihash": "blake3-256-u:<placeholder>"
    },
    "qa_cloud": {
      "href": "s3://kfm/published/eo/landsat/2025/029033/LC09_…/qa_cloud.tif",
      "type": "image/tiff; application=geotiff",
      "roles": ["qa"],
      "checksum:multihash": "blake3-256-u:<placeholder>"
    },
    "thumbnail": {
      "href": "https://cdn.example.org/kfm/.../thumb.jpg",
      "type": "image/jpeg",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    { "rel": "self", "href": "./LC09_2025-07-01_029033.json" },
    { "rel": "collection", "href": "../collection.json" },
    { "rel": "parent", "href": "../collection.json" },
    { "rel": "derived_from", "href": "kfm://run/aa31…", "type": "application/json", "title": "RunReceipt (signed)" },
    { "rel": "prov", "href": "kfm://bundle/7f9a…", "type": "application/json" },
    { "rel": "evidence", "href": "kfm://bundle/7f9a…", "type": "application/ld+json" },
    { "rel": "policy", "href": "kfm://policy/decision/eo-publish/2c17…", "type": "application/json" }
  ]
}
````

</details>

[Back to top](#stac-eo--kfm-conformance-profile)

---

## Anti-patterns

> [!CAUTION]
> Each of the following is a fail-closed condition in the publication policy. Avoid them by construction; do not patch around them at the gate.

| Anti-pattern | Why it fails |
|---|---|
| Inventing free-form top-level fields (outside an extension or `Link`) | Strict STAC clients drop unknown keys; provenance silently lost |
| Pointing asset `href` into `data/raw/`, `data/work/`, or `data/quarantine/` | Trust-membrane violation; bypasses promotion gates |
| Omitting `stac_extensions[]` entries for KFM or companion extensions | Validators cannot apply the right schemas; profile claims unverifiable |
| Collapsing observation and derivation under the same `kfm:source_role` | Loses the distinction between sensor measurement and downstream interpretation |
| Setting `kfm:release_state: released` while `kfm:sensitivity: restricted` | Default-deny gate; sensitive geometry must not default to full public exposure |
| Treating STAC records as the sovereign truth source | STAC is the discovery envelope; `EvidenceBundle` is the reconstructable truth |
| Renaming a Collection `id` post-release | Breaks every Item link in the catalog and every external reference |
| Using rasterized WMS pixels as a regulatory analytic input | WMS is visualization-only; analytics must run against canonical assets |
| Quoting a model's text answer in `properties` instead of resolving via Focus Mode | AI is interpretive; map popups and properties are not citation surfaces |

---

## Open questions and verification backlog

PROPOSED tracking. Items below MUST be carried in `docs/registers/VERIFICATION_BACKLOG.md` or `control_plane/verification_backlog.yaml`.

| ID | Question | Status |
|---|---|---|
| Q-STAC-EO-001 | `kfm:` versus `ks-kfm:` namespace — which is canonical? | OPEN — needs ADR |
| Q-STAC-EO-002 | Exact pinned versions of `eo`, `projection`, `raster`, `view`, `processing`, `checksum`, `scientific`, `version` extension schemas for `kfm-stac-profile-v1` | NEEDS VERIFICATION |
| Q-STAC-EO-003 | Live home for `kfm-stac-profile-v1` schema URL (where is the profile JSON Schema hosted?) | UNKNOWN |
| Q-STAC-EO-004 | Hash function preference for `kfm:spec_hash` — `sha256` vs `blake3` mandated form | NEEDS VERIFICATION |
| Q-STAC-EO-005 | Whether Collections also carry `kfm:promotion_state` summarizing the highest lifecycle phase any Item has reached | OPEN |
| Q-STAC-EO-006 | Whether `kfm:care` namespace fields (CARE/sovereignty) overlap with `kfm:sensitivity` here or sit alongside | OPEN |
| Q-STAC-EO-007 | Final asset-prefix conventions (`s3://kfm/published/eo/...`) for the policy `startswith` checks | NEEDS VERIFICATION |
| Q-STAC-EO-008 | Whether `kfm-stac-profile-v1` is submitted upstream to the `stac-extensions` registry or remains KFM-local | OPEN |

---

## Related docs

- [`docs/standards/README.md`](./README.md) — index of external standards KFM conforms to (PROPOSED)
- [`docs/standards/STAC_KFM_PROFILE.md`](./STAC_KFM_PROFILE.md) — the full KFM STAC profile across all asset families (PROPOSED)
- [`docs/standards/DCAT.md`](./DCAT.md) — non-spatial dataset catalog standard (PROPOSED)
- [`docs/standards/PROV.md`](./PROV.md) — W3C PROV-O for graph-layer provenance (PROPOSED)
- [`docs/standards/STAC-DwC.md`](./STAC-DwC.md) — STAC × Darwin Core hybrid for biodiversity (PROPOSED)
- [`docs/architecture/contract-schema-policy-split.md`](../architecture/contract-schema-policy-split.md) — how shape, meaning, and admissibility are split
- [`docs/doctrine/lifecycle-law.md`](../doctrine/lifecycle-law.md) — RAW → PUBLISHED invariant
- [`docs/doctrine/trust-membrane.md`](../doctrine/trust-membrane.md) — public-path discipline
- `docs/adr/ADR-NNNN-kfm-stac-namespace.md` — namespace decision (PROPOSED, not yet authored)
- `schemas/contracts/v1/stac/kfm-profile-v1.schema.json` — profile JSON Schema (PROPOSED placement)
- `policy/stac/publication.rego` — Layer-3 policy bundle (PROPOSED placement)

---

<sub>**Last reviewed:** 2026-05-14 · **Maintainers:** standards stewards (TBD) · **Authority level:** standards profile · **Status:** PROPOSED draft · [Back to top](#stac-eo--kfm-conformance-profile)</sub>
