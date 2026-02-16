# KFM Catalog Minimums Contract (DCAT / STAC / PROV)

![Contract](https://img.shields.io/badge/contract-governed-blue)
![Gate](https://img.shields.io/badge/promotion-fail--closed-critical)
![Catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-informational)

> [!IMPORTANT]
> This directory defines the **minimum machine-checkable metadata** required for a dataset/version to be **promoted to `Processed`**.
>
> **Missing required catalog fields, broken cross-links, or invalid structure ⇒ promotion MUST fail (fail-closed).**

---

## Governance metadata

| Field | Value |
|---|---|
| Contract name | `catalog-minimums` |
| Location | `infra/contracts/catalog-minimums/` |
| Primary purpose | Merge-/promotion-gate criteria for **catalog emitters + validators** |
| Applies to | Dataset promotion (`Raw → Work → Processed`) and any publishable artifact |
| Compatibility anchors | DCAT v3, STAC (Collections/Items), W3C PROV |
| Change policy | **Contract-first**: changes require fixtures + validators updates; breaking changes require versioning + migration notes |

> [!NOTE]
> The “minimum fields” listed here are derived from KFM’s integration blueprint templates and catalog integrity rules.
> Full KFM profiles live elsewhere (see **Related specs & docs**).

---

## Why this exists

KFM’s trust model requires that promoted data is:
- **Discoverable** (DCAT for dataset-level interoperability),
- **Renderable / mappable** (STAC for spatial assets),
- **Explainable** (PROV for lineage and auditability),
- **Policy-governed** (rights + sensitivity labels enforced at the API boundary).

This contract exists so those requirements are **testable** and **merge-blocking**, not “docs-only.”

---

## Where this sits in the lifecycle

```mermaid
flowchart LR
  SRC[Source APIs / Files] --> RAW[Raw zone<br/>immutable capture]
  RAW --> WORK[Work zone<br/>normalize + QA]
  WORK --> PROC[Processed zone<br/>query-ready + publishable]

  PROC --> DCAT[DCAT<br/>dataset catalog]
  PROC --> STAC[STAC<br/>asset catalog]
  PROC --> PROV[PROV<br/>lineage graph]

  DCAT --> API[Governed API + Policy<br/>(trust membrane)]
  STAC --> API
  PROV --> API

  API --> UI[UI / Stories / Focus Mode]
```

---

## Directory layout

> [!TIP]
> Keep this folder **schema-first** and **fixture-backed**. Validators should be able to run locally and in CI with no network dependency beyond fetching the generated artifacts.

```text
infra/
└─ contracts/
   └─ catalog-minimums/
      ├─ README.md  ← you are here
      ├─ dcat/      ← DCAT minimum validation (schema/shapes) + examples
      ├─ stac/      ← STAC collection/item minimum validation + examples
      ├─ prov/      ← PROV minimum validation + examples
      └─ examples/  ← end-to-end “small” bundles used as regression fixtures
```

*(Exact filenames/tools are implementation-defined; the contract is the **requirements + tests**, not the validator technology.)*

---

## Normative language

This document uses RFC-style keywords:
- **MUST / MUST NOT** = hard gate (promotion fails)
- **SHOULD / SHOULD NOT** = strongly recommended; may be required by specific domains
- **MAY** = optional, but allowed when policy permits

---

## Minimum catalog requirements

### DCAT minimum fields (Dataset-level)

A promoted dataset/version **MUST** emit a DCAT Dataset record with at least the following fields:

| DCAT/DC Terms field | Requirement | Why it’s required in KFM |
|---|---:|---|
| `dct:title` | MUST | Human-readable identification |
| `dct:description` | MUST | Enables evidence-first UI to describe “what is this?” |
| `dct:publisher` (org id) | MUST | Stewardship + accountability |
| `dct:license` (SPDX id or URL) | MUST | Rights enforcement + compliance |
| `dct:spatial` (bbox or admin coverage) | MUST | Spatial discovery + map defaults |
| `dct:temporal` (start/end) | MUST | Time filtering + timeline UI |
| `dct:accrualPeriodicity` (update cadence) | MUST | Operational expectations + refresh policy |
| `dcat:distribution` (download/API endpoints) | MUST | Access paths; supports policy-gated delivery |
| `prov:wasGeneratedBy` (link to PROV activity) | MUST | Provenance linkage for “how do we know?” |

> [!IMPORTANT]
> DCAT is **always required** for promotion (even when the dataset has no spatial assets).

---

### STAC minimum fields (Asset-level; when spatial assets exist)

If a dataset/version publishes **spatial assets** (vectors/rasters/tiles), it **MUST** also emit STAC.

#### STAC Collection (minimum)

| STAC field | Requirement |
|---|---:|
| `id` | MUST |
| `title` | MUST |
| `description` | MUST |
| `license` | MUST |
| `extent.spatial.bbox` | MUST |
| `extent.temporal.interval` | MUST |
| `keywords` | MUST |
| `providers` | MUST |

#### STAC Item (minimum)

| STAC field | Requirement |
|---|---:|
| `id` | MUST |
| `geometry` | MUST |
| `bbox` | MUST |
| `datetime` | MUST |
| `assets` (at least `{data, thumbnail, metadata}` where applicable) | MUST |
| `links` includes `self`, `collection` | MUST |
| `links` includes `derived_from` (PROV linkage) | MUST |

**Item `properties` guidance**
- `proj:epsg` SHOULD be present for spatial consistency (set to canonical CRS when known).
- `gsd` SHOULD be included when known.
- `platform` / `instruments` SHOULD be included when applicable.
- `eo:bands` MAY be included (optional).

> [!NOTE]
> STAC validation MUST include required fields **and** link graph integrity (see **Cross-link integrity**).

---

### PROV minimum fields (Lineage)

A promoted artifact set **MUST** have a PROV representation that includes at least:

**Core node types**
- **Entity**: e.g., `raw_asset`, `normalized_table`, `derived_tile`, `ocr_text`, etc.
- **Activity**: e.g., `ingest_run`, `transform_job`, `redaction_job`
- **Agent**: connector/service identity; steward approval identity when required

**Minimum relations**
- `wasGeneratedBy(entity, activity)` MUST exist for promoted outputs
- `used(activity, entity)` MUST exist for key inputs
- `wasDerivedFrom(derived, source)` MUST exist for derivatives
- `wasAssociatedWith(activity, agent)` MUST exist for responsibility attribution

> [!IMPORTANT]
> “Provenance completeness” in KFM means: **every promoted artifact has a PROV chain and a deterministic checksum** (checksums live in run manifests/receipts and/or referenced entities).  

---

## Cross-link integrity contract (STAC ↔ DCAT ↔ PROV)

Catalog artifacts **MUST** be mutually navigable or resolvable through stable IDs:

- DCAT Dataset record MUST link to a PROV activity (`prov:wasGeneratedBy`).
- STAC Items MUST link to provenance (`derived_from`).
- STAC Collections/Items and DCAT Distributions SHOULD provide a resolvable path to each other:
  - e.g., DCAT Distribution points to STAC Collection root, or STAC Collection includes a link to the DCAT landing page.
- All `href`/IDs used for these cross-links MUST be **resolvable** under the configured object store and/or the governed API.

> [!WARNING]
> “Looks right” is not acceptable. Cross-links are **validated** (link-check clean) and failures must block promotion.

---

## Validation gates this contract expects

The minimum CI/promotion gates implied by this contract include:

- **Schema validation**: DCAT/STAC/PROV outputs validate against their minimum requirements.
- **Geospatial validation**:
  - GeoJSON validity + bbox rules where applicable (RFC 7946).
  - GeoParquet: required geo metadata + geometry encoding constraints.
  - COG rasters: cloud-optimized structure expectations consistent with OGC COG.
- **Temporal sanity**: no invalid intervals; no impossible timestamps for the domain.
- **License + attribution present**: DCAT license is mandatory; missing rights metadata fails closed.
- **Policy labels attached**: `public | restricted | sensitive-location | …` (enforced at API boundary).
- **Determinism**:
  - checksums exist for raw inputs and promoted outputs,
  - catalogs and manifests are generated deterministically (stable ordering; canonical hashing where used).

---

## Sensitivity and CARE handling

> [!CAUTION]
> Some KFM domains include **restricted cultural or archaeology location data**. Catalogs must not become a leakage channel.

Minimum expectations:
- Sensitive datasets/fields MUST be labeled (policy label) and handled fail-closed by default.
- If generalization/redaction is applied, provenance MUST record the redaction activity (PROV) and outputs must remain linkable without exposing restricted coordinates.

---

## Change management

Any change to “minimum fields” is a **contract change**.

### Definition of Done for contract changes

- [ ] Update schema/shapes for DCAT/STAC/PROV minimums
- [ ] Update/extend example fixtures in `examples/`
- [ ] Update validators to enforce the new rule(s)
- [ ] Add/adjust CI tests (merge-blocking)
- [ ] If breaking: document migration path + bump contract version (and update changelog where applicable)

---

## Related specs & docs

Internal (repo-local paths may vary):
- `docs/standards/KFM_DCAT_PROFILE.md` (KFM DCAT profile)
- `docs/standards/KFM_STAC_PROFILE.md` (KFM STAC profile)
- `docs/standards/KFM_PROV_PROFILE.md` (KFM PROV profile)

External (normative references):
- DCAT v3: https://www.w3.org/TR/vocab-dcat-3/
- PROV overview: https://www.w3.org/TR/prov-overview/
- GeoJSON RFC 7946: https://www.rfc-editor.org/rfc/rfc7946
- OGC Cloud Optimized GeoTIFF: https://www.ogc.org/standards/ogc-cloud-optimized-geotiff/
- GeoParquet: https://geoparquet.org/
- RFC 8785 JSON Canonicalization Scheme (JCS): https://www.rfc-editor.org/rfc/rfc8785

---

## Appendix: minimal examples (illustrative)

<details>
<summary><strong>Minimal DCAT Dataset (illustrative JSON-LD skeleton)</strong></summary>

```json
{
  "@type": "dcat:Dataset",
  "dct:title": "Example Dataset Title",
  "dct:description": "What this dataset is and why it exists.",
  "dct:publisher": { "@id": "kfm:org/example-publisher" },
  "dct:license": "CC-BY-4.0",
  "dct:spatial": { "bbox": [-102.0, 36.9, -94.6, 40.0] },
  "dct:temporal": { "start": "1850-01-01", "end": "1900-12-31" },
  "dct:accrualPeriodicity": "irregular",
  "dcat:distribution": [
    { "accessURL": "https://kfm.example/api/datasets/example" }
  ],
  "prov:wasGeneratedBy": { "@id": "kfm:prov/activity/example-ingest-run" }
}
```

</details>

<details>
<summary><strong>Minimal STAC Item (illustrative skeleton)</strong></summary>

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "example-item-001",
  "geometry": { "type": "Polygon", "coordinates": [] },
  "bbox": [-102.0, 36.9, -94.6, 40.0],
  "properties": { "datetime": "1885-01-01T00:00:00Z" },
  "assets": {
    "data": { "href": "https://kfm.example/obj/...", "roles": ["data"] },
    "metadata": { "href": "https://kfm.example/obj/...", "roles": ["metadata"] }
  },
  "links": [
    { "rel": "self", "href": "https://kfm.example/stac/items/example-item-001" },
    { "rel": "collection", "href": "https://kfm.example/stac/collections/example-collection" },
    { "rel": "derived_from", "href": "https://kfm.example/prov/activities/example-ingest-run" }
  ]
}
```

</details>
