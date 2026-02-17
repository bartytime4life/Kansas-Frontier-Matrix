# 🛰️ STAC Catalog Templates (KFM)

![Governed](https://img.shields.io/badge/Governed-Yes-success)
![Contract-first](https://img.shields.io/badge/Contract--first-Yes-blue)
![Schema-validated](https://img.shields.io/badge/Schema--validated-Required-orange)

**Path:** `data/registry/catalog-templates/stac/`

This folder contains **governed STAC templates** used by KFM’s catalog layer emitters to generate STAC **Collections** and **Items** for promoted geospatial assets (rasters/tiles/vectors/etc.).

These templates encode:
- the **minimum required STAC fields** needed for promotion
- **deterministic identity** (stable IDs)
- **provenance + run metadata hooks** so every asset is traceable (evidence-first)

> [!IMPORTANT]
> **Generated STAC artifacts are outputs, not inputs.**  
> Do not hand-edit `data/stac/**` in normal operation—review and modify generation logic/templates instead.

---

## Scope

✅ In scope:
- STAC Collection & Item skeletons (minimum required fields)
- KFM-required `properties` keys for run/digest/attestation/sensitivity
- Link conventions to PROV bundles
- CI/validation expectations (fail-closed promotion gates)

❌ Out of scope:
- Dataset-specific mapping logic (belongs in domain mapping docs + pipeline code)
- Storage/index implementation details (PostGIS/Neo4j/search/object store)
- UI rendering rules (MapLibre/Cesium/Story Nodes)

---

## Where templates sit in the KFM truth path

```mermaid
flowchart LR
  subgraph Z1["Data lifecycle zones"]
    Raw[Raw] --> Work[Work] --> Processed[Processed]
  end

  Processed --> Catalog[Catalog layer emitters\n(STAC/DCAT/PROV)]
  Catalog --> Validation[Schema + policy validation\n(fail-closed)]
  Validation --> Stores[Stores & indexes]
  Stores --> API[Governed API boundary]
  API --> UI[UI / Stories / Focus Mode]
```

---

## Directory layout

```text
data/
  registry/
    catalog-templates/
      stac/
        README.md

        # Recommended conventions (create if missing):
        collection.template.json
        item.template.json
        item.kfm-provenance.snippet.json
```

> [!NOTE]
> The filenames above are conventions.  
> The requirement is that **templates here represent governed contracts** and that catalog emitters + CI enforce the minimum required keys and rules documented below.

---

## Generated outputs live elsewhere

KFM’s canonical generated STAC outputs are expected under:

```text
data/stac/
  collections/
  items/
```

Recommended nesting (keeps PR diffs tidy and paths predictable):

```text
data/stac/collections/<domain>/<collection_id>.json
data/stac/items/<domain>/<collection_id>/<item_id>.json
```

---

## Minimum required fields

These are the **minimum** fields KFM expects for promotion. Optional STAC extensions can be added incrementally once the baseline is stable and validated.

### STAC Collection minimum

| Field | Required | Notes |
|---|:---:|---|
| `id` | ✅ | Stable ID referenced by Items |
| `title` | ✅ | Human-friendly name |
| `description` | ✅ | What assets are in the collection |
| `license` | ✅ | SPDX identifier or URL |
| `extent.spatial.bbox` | ✅ | Spatial coverage |
| `extent.temporal.interval` | ✅ | Temporal coverage |
| `keywords` | ✅ | Search keywords |
| `providers` | ✅ | Attribution + provider roles |

### STAC Item minimum

| Field | Required | Notes |
|---|:---:|---|
| `id` | ✅ | Deterministic per asset slice |
| `geometry` | ✅* | *May be generalized/redacted by policy* |
| `bbox` | ✅* | *May be generalized/redacted by policy* |
| `properties.datetime` | ✅ | Temporal anchor (RFC 3339) |
| `assets.data` | ✅ | Primary artifact link |
| `assets.thumbnail` | ⭕ | Quicklook (optional) |
| `assets.metadata` | ⭕ | Sidecar JSON, QA report, etc. |
| `links` | ✅ | Must include `self` and `collection`; provenance link required |

#### Optional (recommended) Item properties

Use when known:

- `properties.platform`
- `properties.instruments`
- `properties["proj:epsg"]`
- `properties.gsd`
- `properties["eo:bands"]`

---

## KFM-required provenance + run metadata hooks

KFM’s evidence-first workflow requires each promoted Item to carry **small, query-friendly run metadata** and to link to the full PROV bundle.

### Required KFM keys on every promoted STAC Item

| Field | Required | Why it exists |
|---|:---:|---|
| `properties["kfm:run_id"]` | ✅ | Join point to run logs/receipts and replay safety |
| `properties["kfm:artifact_digest"]` | ✅ | Integrity checks and reproducibility |
| `properties["kfm:attestation_uri"]` | ✅ | Where to verify build provenance (SLSA/in-toto/cosign/etc.) |
| `properties["kfm:source_license"]` | ✅ | License-first policy gates depend on this |
| `properties["kfm:data_sensitivity"]` | ✅ | Policy gating + redaction logic |
| `links[]` with `rel: "prov"` | ✅ | Link to PROV JSON-LD bundle for this run |

> [!TIP]
> Keep the Item lightweight: store **URIs** to heavy manifests/logs; don’t inline large manifests.

### Embedded minimal PROV profile (recommended)

<details>
<summary>Example: minimal <code>properties.prov</code> object</summary>

```json
{
  "prov:activity": "ingest_run",
  "prov:generatedAtTime": "2026-02-17T00:00:00Z",
  "prov:wasAssociatedWith": ["kfm:agent/pipeline"],
  "prov:used": [
    { "id": "raw:sha256:…", "href": "../../../raw/<source>.tif" }
  ],
  "prov:wasGeneratedBy": "kfm:run/<kfm:run_id>",
  "prov:evidence": [
    { "href": "../../../prov/runs/<kfm:run_id>.jsonld", "type": "application/ld+json" }
  ]
}
```

</details>

### `stac_extensions` guidance

If you adopt a KFM provenance extension/profile for STAC, add it to `stac_extensions` for governed datasets (the concrete URI/definition is owned by KFM standards).

Common extensions KFM may use:
- Projection (`proj`)
- Electro-Optical (`eo`)

---

## Deterministic identity

Promotion diffs should be reviewable, and replays should be stable.

### Recommended ID patterns

- **Item ID:** `<domain>-<source>-<yyyymmdd>-<geohash5>-<sha8(fingerprint)>`
- **Collection ID:** `<domain>-<theme>-<version>`

### Fingerprint guidance

Derive the fingerprint from a stable set of canonical fields (URIs, extents, bbox, checksums). Prefer deterministic canonicalization for hashing.

---

## Asset conventions

KFM favors a predictable asset key set to reduce downstream coupling:

| Asset key | Required | Typical media type(s) | Typical roles |
|---|:---:|---|---|
| `data` | ✅ | COG, PMTiles, GeoParquet, GeoJSON | `data`, `primary` |
| `thumbnail` | ⭕ | `image/png`, `image/jpeg` | `thumbnail` |
| `metadata` | ⭕ | `application/json`, `application/ld+json` | `metadata` |

Recommended extras (when extension schemas exist and are enabled): checksums, file sizes, and projection metadata.

---

## Governance & sensitivity handling

> [!CAUTION]
> **STAC is part of the narrative surface.** If you put it in STAC, it may be discoverable and citable.
>
> - Always populate `kfm:data_sensitivity`.
> - For restricted datasets, **generalize or redact** `geometry` / `bbox` according to policy.
> - Default-deny: if sensitivity is unknown, block promotion until classified.

---

## Validation gates

Use this checklist when adding/changing templates or onboarding a dataset family:

- [ ] Schema validation passes for Collection and Item JSON (+ extension schemas as applicable)
- [ ] Minimum required keys present (Collection + Item minimums)
- [ ] Cross-links are resolvable (`self`, `collection`, `prov` at minimum)
- [ ] Assets use stable hrefs and known roles; digest metadata present where required
- [ ] Deterministic ID rules validated (same inputs → same IDs)
- [ ] Policy gates pass (license, providers, sensitivity, provenance)
- [ ] Link-check is clean (no broken relative paths)

---

## Change control

- Treat changes here as **governed contract changes**.
- Keep templates minimal; add optional fields incrementally.
- Breaking changes should be versioned (and may require migration of existing catalogs).

---

## Related (repo) references

| Area | Path | What it is |
|---|---|---|
| STAC profile | `docs/standards/KFM_STAC_PROFILE.md` | KFM rules for STAC (may be placeholder) |
| PROV profile | `docs/standards/KFM_PROV_PROFILE.md` | KFM rules for lineage |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | KFM rules for dataset catalog metadata |
| Schema registry | `schemas/` | JSON Schemas for validation |
| Generated STAC outputs | `data/stac/` | Generated Collections + Items |
| Domain mappings | `data/<domain>/mappings/` | Optional dataset → catalog mapping docs |