---
title: "🗺️ Map Legend Manifests (Web UI)"
path: "web/assets/maps/manifests/legends/README.md"
version: "v0.1.0"
last_updated: "2026-01-17"
status: "draft"
doc_kind: "README"
markdown_protocol_version: "KFM-MP(v13)-compatible"
license: "See repo LICENSE"
sensitivity: "public"
---

# 🧭 Legend Manifests (KFM Web Map UI)

![Status](https://img.shields.io/badge/status-draft-orange)
![Config](https://img.shields.io/badge/config-manifest--driven-brightgreen)
![UI](https://img.shields.io/badge/ui-React%20%2B%20MapLibre-blue)
![Contracts](https://img.shields.io/badge/contracts-contract--first-informational)
![Evidence](https://img.shields.io/badge/trust-evidence--first-purple)
![A11y](https://img.shields.io/badge/a11y-ARIA%20%2B%20High%20Contrast-blue)

> [!IMPORTANT]
> Legends are not “decoration.” In KFM they are **part of the evidence surface**: if a layer can’t be explained and attributed, it shouldn’t ship.

---

## 🎯 Overview

This folder is the **canonical home** for **legend manifests** consumed by the KFM web map UI. A *legend manifest* is a small, governed JSON document that:

- ✅ Describes **how a map layer should be explained** to users (symbols, colors, ramps, units)
- ✅ Provides **human-readable labels** (including “No Data”, “Unknown”, etc.)
- ✅ Embeds **provenance hooks** (so the UI can cite the governed dataset & processing lineage)
- ✅ Enables **accessible** legends (screen reader text, not color-only meaning, compact mobile-friendly layout)

---

## 🧱 Non‑Negotiables (KFM Contracts)

### ✅ 1) Contract‑first
Legend manifests are **contracts**. If you change the shape of a manifest, you must:
- Update the **JSON Schema** (recommended location: `schemas/ui/`)
- Version the schema + manifests
- Ensure UI compatibility (or bump a major version)

### ✅ 2) Evidence‑first (no “mystery layers”)
Every legend must link to a governed data source and lineage (via IDs/refs). If you can’t trace it back to **cataloged metadata**, it’s not eligible for Focus Mode / official UI.

### ✅ 3) No sensitive leakage
If a layer is subject to sovereignty / CARE / redaction rules, the legend must not become a side-channel (e.g., implying exact locations via category names). Keep legend labels **policy-safe**.

---

## 🗂️ Directory Layout

```text
📁 web/
  📁 assets/
    📁 maps/
      📁 manifests/
        📁 legends/
          📄 README.md
          📄 <layer-id>.legend.json
          📄 <layer-id>.legend.json
          📄 ... (one per layer, as needed)
```

**Rule of thumb:**  
➡️ **One layer = one legend manifest** (unless multiple layers intentionally share a legend, in which case share a single manifest and reference it from each layer).

---

## 🧩 File Naming & IDs

### 📄 Filename
Use this convention:

- `kebab-case.layer-id.legend.json` **OR** `<layer-id>.legend.json`

Recommended (simple + predictable):
- `ks-counties.legend.json`
- `ogallala-aquifer-extent.legend.json`
- `dust-bowl-1930s.legend.json`

### 🆔 Manifest `id`
- Must be **stable**
- Must be **kebab-case**
- Should match the filename stem

Example:
- Filename: `ks-counties.legend.json`
- Manifest `id`: `ks-counties`

---

## 🧾 Legend Manifest Shape (Recommended Contract)

> [!NOTE]
> The UI can *sometimes* infer symbols from MapLibre style JSON, but this manifest is the **source of truth** for labels, grouping, units, and provenance refs.

### ✅ Minimum fields (recommended)
| Field | Type | Required | Purpose |
|------|------|:--------:|---------|
| `schemaVersion` | string | ✅ | Legend schema version (semver) |
| `id` | string | ✅ | Stable legend ID |
| `title` | string | ✅ | Legend title in UI |
| `layerRef` | string | ✅ | Points to the UI layer registry / layer manifest ID |
| `dataRefs` | object | ✅ | Provenance hooks (DCAT/STAC/PROV IDs) |
| `groups` | array | ✅ | Grouping for legend items |
| `a11y` | object | ✅ | Accessibility labels & notes |
| `updatedAt` | string | ✅ | ISO date for auditing |

---

## 🧱 Legend Groups & Items

A legend can have **multiple groups**, each with one or more **items**.

### Common item types
| `symbol.type` | Typical geometry | Use case |
|---|---|---|
| `fill` | polygon | choropleths, regions |
| `line` | line | boundaries, rivers, routes |
| `circle` | point | stations, events, settlements |
| `icon` | point | specific pictographic symbols |
| `ramp` | raster/continuous | temperature, precipitation, index values |

---

## ✅ Examples

<details>
<summary><strong>🟦 Example A — Categorical legend (polygon boundary)</strong></summary>

```json
{
  "schemaVersion": "1.0.0",
  "id": "ks-counties",
  "title": "Kansas Counties",
  "layerRef": "ks-counties",
  "dataRefs": {
    "dcatDatasetId": "dcat:ks:admin:counties",
    "stacCollectionId": "stac:ks:admin-boundaries",
    "provActivityId": "prov:etl:ks-counties:v1"
  },
  "groups": [
    {
      "title": "Administrative Boundaries",
      "items": [
        {
          "label": "County boundary",
          "symbol": {
            "type": "line",
            "paint": {
              "line-color": "#2b2b2b",
              "line-width": 1.5,
              "line-opacity": 0.85
            }
          }
        },
        {
          "label": "County fill",
          "symbol": {
            "type": "fill",
            "paint": {
              "fill-color": "#d9d9d9",
              "fill-opacity": 0.15
            }
          }
        }
      ]
    }
  ],
  "a11y": {
    "ariaLabel": "Legend for Kansas Counties",
    "notes": "County boundaries are dark gray lines. County fills are light gray and semi-transparent."
  },
  "updatedAt": "2026-01-17"
}
```

</details>

<details>
<summary><strong>🌈 Example B — Continuous ramp legend (index / raster)</strong></summary>

```json
{
  "schemaVersion": "1.0.0",
  "id": "drought-index",
  "title": "Drought Index (Example)",
  "layerRef": "drought-index",
  "dataRefs": {
    "dcatDatasetId": "dcat:ks:climate:drought-index",
    "stacCollectionId": "stac:ks:climate-indices",
    "provActivityId": "prov:etl:drought-index:v2"
  },
  "groups": [
    {
      "title": "Severity",
      "items": [
        {
          "label": "Index value",
          "symbol": {
            "type": "ramp",
            "units": "index",
            "domain": [-6, 6],
            "stops": [
              { "value": -6, "color": "#7f0000", "label": "Extreme dry" },
              { "value": -3, "color": "#d7301f", "label": "Severe dry" },
              { "value":  0, "color": "#f7f7f7", "label": "Neutral" },
              { "value":  3, "color": "#2b8cbe", "label": "Wet" },
              { "value":  6, "color": "#08306b", "label": "Very wet" }
            ]
          }
        },
        {
          "label": "No data",
          "symbol": {
            "type": "fill",
            "paint": {
              "fill-color": "#bdbdbd",
              "fill-opacity": 0.4
            }
          }
        }
      ]
    }
  ],
  "a11y": {
    "ariaLabel": "Legend for drought index layer",
    "notes": "The color ramp represents increasing wetness from red (dry) to blue (wet)."
  },
  "updatedAt": "2026-01-17"
}
```

</details>

---

## 🎨 Cartographic Rules of Thumb (Legend Quality)

> [!TIP]
> A legend is successful when a user can interpret the map **without guessing** and with **minimum interpretive effort**.

### ✅ Do
- Keep labels **short**, **specific**, and **unit-aware** (e.g., `Population density (people/km²)`)
- Include **No data / Unknown / Masked** where applicable
- Group items by meaning (e.g., *Boundaries*, *Transportation*, *Hydrology*)
- Prefer **consistency** across layers (same “boundary” symbol style across the app)
- Use **redundant encoding** when possible (pattern + color, icon + label) for accessibility

### ❌ Don’t
- Don’t rely on color alone to encode meaning
- Don’t put long narratives in legend labels (use layer “Info” panels for depth)
- Don’t create “nearly identical” categories (users can’t distinguish them)
- Don’t include symbols that are self-evident *unless required for clarity*

---

## ♿ Accessibility Checklist

Each legend manifest should include:

- `a11y.ariaLabel` → clear and descriptive
- `a11y.notes` → how to interpret the legend without color cues
- Item labels that can stand alone in screen readers
- Avoid phrases like “shown in red” **without** also stating the meaning (“Dry conditions”)

> [!NOTE]
> If the UI supports a high-contrast mode, ensure the legend remains interpretable (e.g., add pattern/dash hints or alternate symbols).

---

## 🧪 Validation & CI Expectations

Legend manifests should be machine-validated:

- ✅ JSON must parse
- ✅ Conforms to the `schemas/ui/...` legend schema (recommended)
- ✅ `layerRef` must resolve to a known UI layer
- ✅ `dataRefs.*` must resolve to governed catalog IDs (DCAT/STAC/PROV)
- ✅ Any referenced assets (icons/sprites) must exist

> [!WARNING]
> If you add a new legend schema field, treat it like a **contract change**. Update schema + tests.

---

## ✅ Definition of Done (DoD)

- [ ] Legend manifest exists in this folder and follows naming conventions
- [ ] `id` is stable, kebab-case, matches filename stem
- [ ] `layerRef` points to a real UI layer
- [ ] `dataRefs` points to governed catalog records (DCAT/STAC/PROV)
- [ ] Labels include units and “No data” where applicable
- [ ] `a11y` is complete (aria label + interpretation notes)
- [ ] Manifest passes JSON Schema validation
- [ ] Visual check: legend matches layer symbology in the UI
- [ ] Governance check: no sensitive leakage, CARE/FAIR aligned

---

## 🧾 Version History

| Version | Date | Notes |
|---|---|---|
| v0.1.0 | 2026-01-17 | Initial README + recommended legend contract |

---
