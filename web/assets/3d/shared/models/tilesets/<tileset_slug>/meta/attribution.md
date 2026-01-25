<!--
KFM Tileset Attribution (human-readable)
📍 Path: web/assets/3d/shared/models/tilesets/<tileset_slug>/meta/attribution.md

✅ Fill every <...> placeholder before publishing.
🧬 KFM principle: provenance-first publishing — no “mystery layers.”
🧾 Intended surfaces: KFM UI “Layer Info” / “Layer Provenance” + exports + offline packs.
-->

# 🧱 `<tileset_title>` — 3D Tileset Attribution & License

![Format](https://img.shields.io/badge/format-3D%20Tiles-blue) ![Viewer](https://img.shields.io/badge/viewer-CesiumJS-1f6feb) ![Provenance](https://img.shields.io/badge/provenance-STAC%2FDCAT%2FPROV-8250df) ![License](https://img.shields.io/badge/license-<spdx_or_custom>-f59e0b)

> 🧭 **What this is:** the human-friendly attribution + licensing summary for this tileset.  
> 🧠 **What it connects to:** machine metadata (STAC/DCAT/PROV) + a reproducible build/run manifest.

---

## ✅ Quick facts

- **Tileset slug:** `<tileset_slug>`
- **Title:** `<tileset_title>`
- **One-liner:** `<1–2 sentence description of what this 3D tileset represents>`
- **Coverage:** `<Kansas / county / bbox / AOI name>`
- **Time range:** `<YYYY–YYYY or YYYY-MM-DD>`
- **Format:** `3D Tiles` (`tileset.json`)  
- **Primary viewer:** `CesiumJS` (KFM 3D view)
- **KFM build:** `<pipeline_id>` • run `<run_id>` • generated `<YYYY-MM-DD>`
- **Sensitivity label:** `<public | internal | restricted | sovereign_review_required>`
- **KFM dataset ID (optional):** `<kfm_dataset_id>`

---

## 🧾 Recommended attribution (copy/paste)

### ⭐ Short (UI footer / export footer)

```text
<tileset_title> — Source(s): <source_short_list>. Processed by Kansas Frontier Matrix (KFM) on <YYYY-MM-DD>. License: <output_license>.
```

### 📚 Long (reports / publications)

```text
<tileset_title> (3D Tiles). Produced by Kansas Frontier Matrix (KFM) from the following source datasets: <full_source_list_with_publishers_and_dates>. Processing: <short_processing_summary>. Generated: <YYYY-MM-DD> (run <run_id>). Output license: <output_license>. See STAC/DCAT/PROV links for full lineage and distributions.
```

### 🧩 If you only have room for one line

```text
Data: <primary_source> • Processing: KFM • <YYYY-MM-DD> • <output_license>
```

---

## 🔗 Upstream sources (what this tileset is built from)

> 💡 **Rule:** list every upstream dataset that contributed *bytes or meaning* to the tileset (geometry, textures, elevation, attributes, classifications, labels, etc.).

| Role / Use | Publisher / Provider | Dataset / Product | Version / Date | License | Required credit text | Source URL |
|---|---|---|---|---|---|---|
| `<role_1>` | `<provider_1>` | `<dataset_name_1>` | `<YYYY-MM-DD or vX.Y>` | `<SPDX or custom>` | `<required attribution text>` | <https://example.com> |
| `<role_2>` | `<provider_2>` | `<dataset_name_2>` | `<YYYY-MM-DD or vX.Y>` | `<SPDX or custom>` | `<required attribution text>` | <https://example.com> |
| `<role_3>` | `<provider_3>` | `<dataset_name_3>` | `<YYYY-MM-DD or vX.Y>` | `<SPDX or custom>` | `<required attribution text>` | <https://example.com> |

✅ **If OpenStreetMap contributed:** include ODbL attribution + share-alike notes.  
✅ **If imagery/orthos/textures contributed:** include provider + terms for derivative textures.  
✅ **If LiDAR/point clouds contributed:** include provider + year + any redistribution constraints.

---

## ⚖️ License & usage terms

### Output license (this tileset)

- **Output license:** `<output_license_spdx_or_custom>`
- **Output attribution requirement:** `<what users must do when using this tileset>`
- **Commercial use:** `<allowed | disallowed | conditional>`
- **Share-alike / copyleft:** `<none | yes (explain)>`
- **Warranty / liability:** provided “as-is” unless stated otherwise.

### License stacking (combined layers)

> 🧷 **KFM licensing rule of thumb:** when multiple source licenses apply, treat the combined output as the **most restrictive** applicable license (e.g., `CC-BY` + `Public Domain` ⇒ `CC-BY`).  
> If anything is non-commercial / share-alike / education-only, that constraint must be reflected here *and* in machine metadata.

### Special constraints (if any)

- `<constraint_1>`
- `<constraint_2>`

---

## 🛠️ What KFM changed (processing summary)

> 🔁 **KFM principle:** transformations must be traceable via code/config — no hidden manual edits.

- **Raw intake:** `<where the original inputs live: data/raw/... or external reference>`
- **Normalization:** `<reprojection / schema harmonization / unit normalization>`
- **Cleaning:** `<dedupe / geometry fixes / topology repairs / outlier removal>`
- **Derivation:** `<extrusions / meshing / classification / texturing / decimation>`
- **Tiling:** `<3D Tiles pipeline details: LOD strategy, geometric error target, tile size, etc.>`
- **QA/QC:** `<validation checks run + results summary>`
- **Output artifacts:** `web/assets/3d/shared/models/tilesets/<tileset_slug>/tileset.json` (+ tile content)

<details>
<summary>🔧 Toolchain (fill in what you actually used)</summary>

- **Core geospatial:** `<GDAL | PROJ | PostGIS | Tippecanoe | …>`
- **Point clouds:** `<PDAL | Entwine | …>`
- **3D:** `<Cesium tools | glTF pipeline | mesh optimizer | …>`
- **Build environment:** `<container image / lockfile / versions>`
- **Determinism note:** `<how this pipeline is repeatable>`

</details>

---

## 🧬 Provenance & machine metadata (STAC / DCAT / PROV)

> 🧠 These are the “source of truth” references that Focus Mode + the UI can cite and verify.

- **DCAT dataset:** `<relative_path_or_url_to_dcat_dataset.jsonld>`
- **STAC collection / item(s):** `<relative_path_or_url_to_stac_collection_or_items>`
- **PROV record:** `<relative_path_or_url_to_prov.jsonld>`
- **Data contract / schema (if applicable):** `<relative_path_or_id>`
- **Run manifest (hashes + inputs + steps):** `<relative_path_or_url_to_run_manifest.json>`

<details>
<summary>🗂️ Suggested repo linkage (optional, but recommended)</summary>

```text
📁 data/
├── 🧾 raw/                          (immutable upstream evidence; keep pristine + read-only mindset)
├── 🧪 processed/                    (derived datasets; reproducible outputs from pipelines)
├── 🗺️ catalog/
│   ├── 🏷️ dcat/                     (discoverability: dataset metadata + publishers + themes)
│   └── 🛰️ stac/                     (spatiotemporal index + distributions: items, assets, collections)
├── 🧬 provenance/
│   └── 🧾 prov/                     (lineage + activities: entities/activities/agents; trace inputs→outputs)
└── 🔍 audits/
    └── 🆔 <run_id>/                 (execution receipts: run_manifest.json, checksums, QA logs, gate results)
```

</details>

---

## 🔐 Artifact integrity & distribution (optional but 🔥 for trust)

> If this tileset is shipped via an OCI registry (ORAS) and signed (Cosign), record it here.

- **OCI reference:** `oci://<registry>/<repo>:<tag>`
- **Digest (immutable):** `sha256:<digest>`
- **Cosign signature:** `<yes/no>` • `<verification instructions or reference>`
- **Referrers (PROV/attestations):** `<links or descriptions>`

---

## 🧭 FAIR+CARE & sensitivity (non-negotiable)

- **Sensitivity classification:** `<public | internal | restricted | sovereign_review_required>`
- **CARE / sovereignty notes:** `<if indigenous/community-governed or culturally sensitive, specify oversight + allowed representations>`
- **PII policy:** `<confirm none, or describe aggregation/redaction>`
- **Location masking (if needed):** `<generalization, jitter, omission, bounding-only, etc.>`

---

## ⚠️ Known limitations & accuracy notes

- **Resolution / scale:** `<LOD limits, minimum feature size>`
- **Completeness:** `<what’s missing / coverage gaps>`
- **Positional accuracy:** `<known error ranges or references>`
- **Rendering caveats:** `<texture seams, LOD popping, precision issues, etc.>`

---

## 🗺️ Where this shows up in KFM

- **Layer Info dialog:** this file should provide the *source, license, and “how prepared” summary* in plain language.
- **Layer Provenance (planned):** supports listing active layers with citations/metadata.
- **Exports & share links:** enables automatic attribution footnotes/snippets.
- **Offline packs:** include this file alongside the tileset so attribution travels offline too.

---

## 📌 Changelog

- `v<tileset_version>` — `<YYYY-MM-DD>` — `<what changed + why>`
- `v<tileset_version>` — `<YYYY-MM-DD>` — `<what changed + why>`

---

## 🤝 Contacts

- **Data steward / maintainer:** `<name or team>` • `<contact method>`
- **Issues / tracking:** `<repo issue link or internal tracker>`
- **Last reviewed:** `<YYYY-MM-DD>`

---

## ✅ Maintainer checklist (ship-blocking)

- [ ] All upstream datasets listed with **provider**, **version/date**, **license**, and **URL**
- [ ] Output license is set + consistent with the most restrictive input license
- [ ] STAC / DCAT / PROV links are filled and resolve
- [ ] Run manifest / hashes recorded (or explicitly marked “not yet available”)
- [ ] Sensitivity label is set + CARE/sovereignty notes completed (if applicable)
- [ ] Attribution snippets tested in UI + included in export flows

<!-- END -->

