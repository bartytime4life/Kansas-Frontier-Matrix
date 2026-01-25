# 🎨 Shared 3D Material Schema (KFM)

![Status](https://img.shields.io/badge/status-draft-yellow)
![Schema](https://img.shields.io/badge/schema-JSON%20Schema-blue)
![Targets](https://img.shields.io/badge/targets-CesiumJS%20%7C%20glTF%20%7C%20Three.js-informational)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE%20%2B%20Policy%20Gates-brightgreen)
![Scope](https://img.shields.io/badge/scope-web%2Fassets%2F3d-lightgrey)

This directory documents the **material definition contract** for KFM’s shared 3D materials — meant to be **configuration-driven**, **auditable**, and **portable across viewers** (notably the KFM web UI’s 2D/3D toggle with CesiumJS, and future AR/offline packaging).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🧭 Why this exists

KFM’s architecture leans hard into:

- **Configuration + schemas** as the backbone for extensibility (layers, stories, UI behavior, etc.).:contentReference[oaicite:3]{index=3}
- **2D ↔ 3D parity**, where many layers can have a “3D equivalent” in Cesium (3D globe, terrain, 3D Tiles).:contentReference[oaicite:4]{index=4}:contentReference[oaicite:5]{index=5}
- **Provenance-first publishing + policy gates** (“fail closed”) so nothing enters the system without licensing, classification, and provenance metadata.:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

A **material pack** is “just another artifact” that should follow those same rules: schema-valid, licensed, attributable, and linked into provenance (especially if it is derived from imagery, scans, or culturally-sensitive sources).:contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

---

## 🗂️ Expected layout

> The schema lives here (📁 `web/assets/3d/shared/materials/schema/`).  
> Individual materials live elsewhere (recommended: 📁 `web/assets/3d/shared/materials/packs/`).

Example structure (recommended):

```text
web/assets/3d/shared/materials/
├─ 📁 schema/
│  ├─ 📄 README.md   👈 you are here
│  ├─ 📄 material.schema.json           (single material spec)
│  ├─ 📄 material-pack.schema.json      (folder-level manifest)
│  └─ 📄 materials.catalog.schema.json  (UI-friendly index)
└─ 📁 packs/
   └─ 📁 kfm.mat.prairie.grassland/
      ├─ 📄 material.json
      ├─ 📄 provenance.jsonld          (optional but strongly encouraged)
      ├─ 🖼️ preview.jpg                (optional, for catalogs/UI)
      └─ 📁 textures/
         ├─ 🧱 baseColor.(png|ktx2)
         ├─ 🧲 normal.(png|ktx2)
         ├─ ⚙️ metallicRoughness.(png|ktx2)
         ├─ 🌫️ occlusion.(png|ktx2)
         └─ ✨ emissive.(png|ktx2)
```

---

## 🧱 Concepts & terminology

### MaterialSpec
A **single JSON document** describing:
- PBR-ish intent (baseColor, roughness, metalness, normal, etc.)
- required governance metadata (license, attribution, classification)
- optional engine hints (Cesium/Three/glTF mappings)

### Material Pack
A **folder** that bundles:
- `material.json` (the spec)
- textures (and optional preview)
- provenance stub (optional but recommended; required if derived from restricted/sensitive sources)

### Catalog
A UI-friendly index of available materials:
- minimal metadata
- points to pack paths
- can be used by Story Nodes / editors / UI pickers

> KFM Story Nodes are narrative markdown + config JSON; treating materials as “IDs you can reference” fits the existing pattern.:contentReference[oaicite:11]{index=11}

---

## 📐 MaterialSpec v1 (proposed contract)

### ✅ Required fields (KFM governance minimum)

| Field | Type | Why it matters |
|---|---:|---|
| `schema_version` | string | Safe evolution of the contract |
| `id` | string | Stable reference from layers/stories |
| `version` | string (semver) | Deterministic evolution of visuals |
| `name` | string | Human readable |
| `license` | string (SPDX-ish) | Policy gate requirement (“no data without license”):contentReference[oaicite:12]{index=12} |
| `attribution` | string | UI credit + legal hygiene:contentReference[oaicite:13]{index=13} |
| `classification` | enum | Sovereignty/sensitivity propagation in policy gates:contentReference[oaicite:14]{index=14} |
| `provenance` | object | Provenance-first publishing (even if stub):contentReference[oaicite:15]{index=15} |
| `pbr` | object | Rendering intent |
| `textures` | object | Texture slot URIs (if any) |

### 🧾 Suggested governance enums

```json
{
  "classification": "public | internal | restricted | confidential"
}
```

> Note: KFM policy expects **most restrictive input classification propagates to outputs** (so “public” cannot be derived from “confidential” without an explicit governance process).:contentReference[oaicite:16]{index=16}

---

## 🧪 Minimal example: `material.json`

```json
{
  "schema_version": "kfm.material.v1",
  "id": "kfm.mat.prairie.grassland",
  "version": "1.0.0",
  "name": "Prairie Grassland",
  "description": "Neutral prairie ground cover material intended for mid-distance terrain-adjacent meshes.",
  "tags": ["prairie", "kansas", "ground"],

  "license": "CC-BY-4.0",
  "attribution": "Textures derived from public-domain reference photography; see provenance link.",
  "classification": "public",

  "provenance": {
    "prov_ref": "data/prov/materials/kfm.mat.prairie.grassland@1.0.0.prov.jsonld",
    "source_summary": "Derived texture set; see PROV for source URLs, checksums, and processing steps."
  },

  "pbr": {
    "model": "metallicRoughness",
    "baseColorFactor": [1, 1, 1, 1],
    "metallicFactor": 0.0,
    "roughnessFactor": 0.9,
    "doubleSided": false,
    "alphaMode": "OPAQUE"
  },

  "textures": {
    "baseColor": { "uri": "textures/baseColor.ktx2", "colorSpace": "sRGB" },
    "normal": { "uri": "textures/normal.ktx2", "colorSpace": "linear", "scale": 1.0 },
    "metallicRoughness": { "uri": "textures/metallicRoughness.ktx2", "colorSpace": "linear" },
    "occlusion": { "uri": "textures/occlusion.ktx2", "colorSpace": "linear", "strength": 1.0 }
  }
}
```

---

## 🧩 Optional: variants (seasonal/time-based)

KFM has strong temporal storytelling and expects “time-aware” experiences (timelines, story steps, etc.).:contentReference[oaicite:17]{index=17}

Use variants to keep the base material stable while enabling seasonal “skins”:

<details>
<summary><strong>🌦️ Variant example</strong> (click to expand)</summary>

```json
{
  "variants": [
    {
      "id": "summer",
      "name": "Summer (lush)",
      "overrides": {
        "pbr": { "roughnessFactor": 0.85 },
        "textures": {
          "baseColor": { "uri": "textures/variants/summer_baseColor.ktx2", "colorSpace": "sRGB" }
        }
      }
    },
    {
      "id": "winter",
      "name": "Winter (dry)",
      "overrides": {
        "pbr": { "roughnessFactor": 0.95 },
        "textures": {
          "baseColor": { "uri": "textures/variants/winter_baseColor.ktx2", "colorSpace": "sRGB" }
        }
      }
    }
  ]
}
```

</details>

---

## 🛰️ Engine targets (optional hints)

KFM’s web viewers include **CesiumJS** for 3D (3D globe + 3D Tiles) and MapLibre for 2D.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

This schema stays **engine-agnostic**, but you can add `engines.*` blocks when you need deterministic behavior per renderer:

### `engines.cesium`
- Intended for Cesium-specific quirks (e.g., fabric materials, classification, translucency behavior)

### `engines.three`
- Useful for lightweight local scenes or analysis tooling (e.g., Three.js-based overlays, previews)
- Example patterns exist in the project’s WebGL reference materials and geospatial cookbook notes (Three.js materials, textures, wireframes).

---

## 🔐 Governance & policy gates (non-negotiable)

KFM enforces automated “policy gates” at multiple points (ingestion, publication, AI outputs). These gates are **fail-closed** and include schema validation, STAC/DCAT/PROV completeness, license checks, sensitivity/classification rules, etc.:contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}

### ✅ Material policy checklist

**A material pack SHOULD NOT MERGE unless:**

- ✅ `material.json` validates against the schema (CI gate)
- ✅ `license` is present and allowed (CI gate):contentReference[oaicite:23]{index=23}
- ✅ `attribution` is present (UI/legal):contentReference[oaicite:24]{index=24}
- ✅ `classification` is present and consistent (propagation rules apply):contentReference[oaicite:25]{index=25}
- ✅ `provenance` is present (at least a stub ref) — provenance-first publishing:contentReference[oaicite:26]{index=26}
- ✅ no secrets / credentials are committed in JSON (policy-as-code scanning):contentReference[oaicite:27]{index=27}

### 🧾 Optional but strongly recommended: canonical digest

KFM proposes canonical JSON hashing (RFC 8785) to compute a stable SHA-256 `canonical_digest` for manifests and idempotency keys.:contentReference[oaicite:28]{index=28}

For materials, this enables:
- stable cache keys
- tamper detection
- reproducible builds
- offline pack verification

---

## 📦 Offline packs + AR readiness

KFM plans for:
- **Offline data packs** (pre-rendered tiles, layers, story nodes, and 3D assets):contentReference[oaicite:29]{index=29}
- **AR mode** (subset of layers, simplified geometry, cached assets):contentReference[oaicite:30]{index=30}

### Recommendations for material authors
- Prefer **local relative URIs** (no runtime network fetch).
- Provide **LOD texture variants** (e.g., 4k, 2k, 1k) if the material will ship in offline/AR packs.
- Keep a small `preview.jpg` for catalog browsing and story editors.

---

## 🧵 Story Nodes integration pattern (recommended)

Story Nodes combine markdown narrative with a configuration JSON that drives map state and layers.:contentReference[oaicite:31]{index=31}

If a story step uses a 3D layer, it can reference materials by ID:

```json
{
  "step_id": "prairie-3d-context",
  "viewer": "cesium",
  "layers": ["kfm.layer.settlements.1870s.3d"],
  "material_overrides": [
    {
      "target": { "type": "tileset", "tileset_id": "settlements_1870s" },
      "material_id": "kfm.mat.prairie.grassland",
      "variant": "summer"
    }
  ]
}
```

> The story config format is intentionally editable by domain experts (markdown + JSON), reinforcing the need for stable IDs and schema validation.:contentReference[oaicite:32]{index=32}

---

## 🛠️ Authoring workflow (human or agent-assisted)

KFM supports “safe, auditable” agent workflows where automation proposes/executes changes but never bypasses review or CI/policy gates.:contentReference[oaicite:33]{index=33}

### 1) Create the pack folder
- `web/assets/3d/shared/materials/packs/<material_id>/`

### 2) Add textures
- Place in `textures/`
- Use consistent naming (`baseColor`, `normal`, `metallicRoughness`, `occlusion`, `emissive`)

### 3) Write `material.json`
- Fill required governance fields (license, classification, provenance)

### 4) Add provenance stub (recommended)
- Link to a PROV JSON-LD record or at minimum list source URLs/checksums in a structured way.
- KFM’s broader system ties STAC/DCAT/PROV together and mirrors the evidence graph in Neo4j, so keeping refs structured pays off later.:contentReference[oaicite:34]{index=34}

### 5) Validate
- Schema validation + policy gates must pass (fail closed).:contentReference[oaicite:35]{index=35}

---

## 🧪 “Definition of Done” checklist ✅

A PR adding or modifying a material pack is **done** when:

- [ ] `material.json` passes JSON Schema validation
- [ ] `license`, `attribution`, `classification`, `provenance` are present and accurate
- [ ] any sensitive/culturally restricted source material has correct classification + governance notes
- [ ] preview asset exists (if the pack is intended for UI selection)
- [ ] if derived assets were processed, PROV points to sources + method (reproducibility mindset):contentReference[oaicite:36]{index=36}:contentReference[oaicite:37]{index=37}

---

## 🧭 Ethics & cultural protocols (don’t skip this)

KFM explicitly anticipates culturally sensitive knowledge workflows (e.g., Mukurtu CMS-inspired approaches and sensitivity-aware handling).:contentReference[oaicite:38]{index=38}

If a texture/material is derived from:
- restricted imagery
- culturally sensitive artifacts
- site-specific scans
- Indigenous knowledge materials

…then **classification + provenance must reflect that**, and the pack must follow the same governance posture as any other dataset or story artifact.

---

## 📚 Project references (all source files)

<details>
<summary><strong>📖 Primary KFM design & architecture docs</strong></summary>

- :contentReference[oaicite:39]{index=39} Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf  
- :contentReference[oaicite:40]{index=40} Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf  
- :contentReference[oaicite:41]{index=41} Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf  
- :contentReference[oaicite:42]{index=42} Kansas Frontier Matrix – Comprehensive UI System Overview.pdf  
- :contentReference[oaicite:43]{index=43} 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf  
- :contentReference[oaicite:44]{index=44} 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf  
- :contentReference[oaicite:45]{index=45} Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf  
- :contentReference[oaicite:46]{index=46} Additional Project Ideas.pdf  

</details>

<details>
<summary><strong>🧰 Supporting technical references & libraries (some are PDF portfolios)</strong></summary>

- :contentReference[oaicite:47]{index=47} Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf  
- :contentReference[oaicite:48]{index=48} KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf  
- :contentReference[oaicite:49]{index=49} Data Mining Concepts &amp; applictions.pdf  
- :contentReference[oaicite:50]{index=50} Scientific Method _ Research _ Master Coder Protocol Documentation.pdf  
- :contentReference[oaicite:51]{index=51} Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf (PDF portfolio)  
- :contentReference[oaicite:52]{index=52} AI Concepts &amp; more.pdf (PDF portfolio)  
- :contentReference[oaicite:53]{index=53} Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf (PDF portfolio)  
- :contentReference[oaicite:54]{index=54} Various programming langurages &amp; resources 1.pdf (PDF portfolio)  

</details>

---

## 🗺️ Roadmap (next upgrades)

- 🧾 Add the actual `material.schema.json` + catalog schemas to this folder.
- 🧪 Add CI validation + policy gates for material packs (license/classification/provenance).
- 📦 Add offline-pack manifest support for materials (LOD texture selection).
- 🧰 Add a small “material preview generator” so every pack gets a deterministic thumbnail.
- 🔏 Add optional signing/attestation for published material packs (aligned with KFM’s supply-chain security direction).:contentReference[oaicite:55]{index=55}:contentReference[oaicite:56]{index=56}

