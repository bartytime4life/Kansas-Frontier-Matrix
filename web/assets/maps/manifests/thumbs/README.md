---
title: "KFM Web — Map Manifest Thumbnails (thumbs/)"
path: "web/assets/maps/manifests/thumbs/README.md"
version: "v0.1.0"
last_updated: "2026-01-17"
status: "active"
doc_kind: "Runbook"
license: "CC-BY-4.0"
markdown_protocol_version: "v13"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"
review_gates_ref: "docs/governance/REVIEW_GATES.md"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"
doc_uuid: "urn:kfm:doc:web:assets:maps:manifests:thumbs:readme:v0.1.0"
commit_sha: "<commit_sha>"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

# 🖼️ Thumbnails for Map Manifests (`thumbs/`)

![KFM](https://img.shields.io/badge/KFM-web%20map%20ui-2b6cb0?style=flat&logo=leaflet&logoColor=white)
![Static Assets](https://img.shields.io/badge/static-assets-in%20repo-lightgrey?style=flat)
![Governed](https://img.shields.io/badge/provenance-first-success?style=flat)

Quick-preview images for the **layer browser / catalog** in the `web/` Map UI 🌐🗺️.[^web-ui][^web-static]

---

## ✅ What belongs in this folder

- 🖼️ **Thumbnail images** (fast previews for dataset/layer cards)
- 📄 **This README** (rules + conventions)

### 🚫 What does *not* belong here
- ❌ Source rasters (COGs), tiles, GeoJSON, GeoParquet, etc.
- ❌ “Hidden data files” that bypass the governed pipeline and API boundaries.[^pipeline-order][^api-boundary]

> KFM is built around **contract-first + provenance-first** data flow, so UI assets stay “decorative,” while the real layer data stays governed and traceable.[^contract-first][^provenance-first]

---

## 🧭 Directory layout

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 manifests/
        📁 thumbs/           👈 you are here
          📄 README.md
          🖼️ <layer_id>.webp
          🖼️ <layer_id>.png
```

---

## 🚦 Quick rules (TL;DR)

- ✅ **File name MUST match** the manifest `id` (exact slug match)
- ✅ Prefer **WebP** (PNG only when needed)
- ✅ **Square** thumbs (1:1), readable at ~120px
- ✅ Keep file size **small** (fast layer browsing)
- 🚫 No orphan thumbs (every file must be referenced by a manifest)
- 🔒 No sensitive/restricted content leaks through previews (classification propagates)[^classification]

---

## 🔗 Naming & linking rules (non-negotiable)

| Rule | Why it matters |
|---|---|
| **`<layer_id>.<ext>` must match manifest `id`** | Prevents “mystery layers” and keeps traceability tight.[^no-mystery] |
| Only **lowercase + digits + `_` + `-`** | Stable URLs, predictable imports |
| One canonical thumb per layer | Consistent UX + avoids drift |
| No orphan files | Keeps the repo clean and the UI trustworthy |

**Recommended slug shape:**  
`<domain>__<dataset>__<variant>` (double underscore splits “namespace chunks”)

Examples:
- `historical__atlas_1880__plate_12.webp`
- `environment__precip_normals_1991_2020.webp`

---

## 🧩 How a manifest should reference a thumb

Use **relative paths** so it works in GitHub, local dev, and production builds.

```jsonc
{
  "id": "historical__atlas_1880__plate_12",
  "title": "Atlas Plate 12 (1880)",
  "thumbnail": {
    "src": "./thumbs/historical__atlas_1880__plate_12.webp",
    "w": 512,
    "h": 512,
    "alt": "Preview of Atlas Plate 12 (1880)"
  }

  // Optional but encouraged cross-links:
  // "stac_item": "data/stac/items/…",
  // "dcat_dataset": "data/catalog/dcat/…",
  // "prov_bundle": "data/prov/…"
}
```

> ℹ️ Those optional cross-links align with KFM’s expectation that catalogs/provenance stay connected (STAC/DCAT/PROV/graph).[^cross-layer]

---

## 🖌️ Thumbnail specs (recommended defaults)

These defaults are tuned for **fast browsing**, **mobile**, and **accessibility**:

- 📐 **Canvas:** 1:1 square
- 🧱 **Resolution:** 512×512 px (or 256×256 if you need ultra-small)
- 🗜️ **Format:** WebP preferred; PNG as fallback
- ⚡ **Weight target:** ≤ 150 KB (≤ 80 KB ideal)
- 🧭 **Content:** show the layer’s character (symbology + region); avoid tiny labels
- ♿ **Accessibility:** provide `alt` text in the manifest; the UI should honor high-contrast needs.[^ui-accessibility]

---

## 🧾 Provenance, licensing, and governance

KFM is **provenance-first**: map layers (and anything the UI presents as “real”) should stay traceable to sources and processing steps.[^provenance-first]

**Therefore:**
- ✅ Treat thumbs as **derived UI assets**, not evidence.
- ✅ Ensure the layer’s real data is cataloged + lineage tracked before it becomes user-facing.[^pipeline-order]
- ✅ If thumbs are regenerated, update any integrity fields you track (size, sha256, pipeline version) in the relevant contract/metadata.[^pipeline-metadata]
- 🚫 Do **not** include previews that reveal restricted/sensitive content; classification must not be “downgraded” through derivatives.[^classification]
- ⚖️ Respect dataset/map licenses (thumbnails are still derivative reproductions).[^license-care]

---

## 🔁 Updating / regenerating thumbs

Pipelines in KFM are intended to be **deterministic and reproducible**.[^deterministic]

When a layer’s styling, extent, or appearance changes:

1. Regenerate the thumb from the canonical rendering flow used for that layer (COG/tiles → render → thumb).[^pipeline-cog][^historic-map-pipeline]
2. Replace the old file **in-place** (same name) unless the manifest `id` changed.
3. Update metadata (where applicable): checksum, size, generation timestamp, pipeline version.[^pipeline-metadata]

> 🧰 If/when a generator script exists, keep it in `tools/` or `src/pipelines/` (not inside `web/`) and document it here.[^repo-structure]

---

## ✅ Definition of Done (thumbs)

- [ ] File name matches manifest `id` exactly
- [ ] Square thumb renders well at ~120px in a layer card
- [ ] File size within target (≤ 150 KB)
- [ ] Manifest includes `thumbnail.alt`
- [ ] No sensitive/restricted information leaks via preview
- [ ] Metadata updated if integrity fields are tracked (sha256, size, pipeline version)

---

## 📚 References (project grounding)

[^web-ui]: KFM’s UI lives under `web/` and targets a React + MapLibre map UI.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^web-static]: The `web/` folder is treated as a static front-end (MapLibre/Leaflet) and can include precomputed JSON configuration needed by the app.  [oai_citation:1‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
[^repo-structure]: Canonical subsystem layout (pipelines in `src/pipelines/`, tools in `tools/`, UI in `web/`).  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^pipeline-order]: Pipeline ordering is explicit: ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^api-boundary]: UI must not bypass the API layer (e.g., no direct graph access).  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^contract-first]: Contract-first + deterministic pipeline behavior is a core invariant.  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^deterministic]: Deterministic, idempotent ETL is a stated goal (stable outputs for stable inputs).  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^pipeline-metadata]: Pipelines update metadata/provenance, including integrity info (file size, checksum, thumbnail preview if applicable).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^historic-map-pipeline]: Example pipeline work includes georeferencing historical maps and producing COGs/tiles and metadata outputs.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^pipeline-cog]: Processing pipeline converts and georeferences map imagery and produces web-friendly outputs (COGs, tiles) with traceable metadata.  [oai_citation:10‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)
[^provenance-first]: KFM treats citations + metadata as first-class and avoids black boxes.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^no-mystery]: “No mystery layers” is supported by required metadata contracts and validation.  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^cross-layer]: KFM enforces/encourages cross-references among STAC, DCAT, PROV, and graph entries.  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^classification]: Classification/sensitivity must propagate end-to-end; UI may blur/generalize sensitive locations.  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^ui-accessibility]: UI should follow cartographic best practices and accessibility (contrast, ARIA, semantic HTML).  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^license-care]: KFM emphasizes careful licensing to build trust and avoid legal pitfalls.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
