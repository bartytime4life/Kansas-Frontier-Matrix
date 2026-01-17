# 3D Map Schemas 🧊🗺️  
![status](https://img.shields.io/badge/status-governed%20contracts-6f42c1) ![jsonschema](https://img.shields.io/badge/JSON%20Schema-2020--12-blue) ![3dtiles](https://img.shields.io/badge/3D%20Tiles-streaming%20ready-orange) ![cesium](https://img.shields.io/badge/CesiumJS-3D%20viewer-0b7285) ![provenance](https://img.shields.io/badge/provenance-first-✅-2ea44f)

This folder contains **JSON Schemas** for **KFM’s 3D map “configuration + asset manifest” contracts** used by the web app’s 3D viewer stack (typically Cesium + 3D Tiles).

**Goal:** make every 3D layer/scene *machine-validated*, *attributable*, and *safe to render* — before it ever reaches the UI.

> ✅ **Contract-first**: config formats are treated like APIs (versioned, validated, backwards-compatible by default).  
> 🔎 **Provenance-first**: no “mystery layers” — every 3D thing shown must have source + license + lineage references.  
> 🔒 **Governance-aware**: classification and sovereignty tags travel with configs so the UI can enforce redaction rules.

---

## 📍 Where you are

```text
web/
└─ 📁 assets/
   └─ 🗺️ maps/
      └─ 🧊 3d/
         └─ 📐 _schemas/        👈 you are here 📌
            ├─ 📄 README.md
            └─ 📐🧾 …           # (schema files live here)
```

---

## 🧭 What belongs here (and what doesn’t)

### ✅ Belongs here
- **UI-facing JSON Schemas** for:
  - 3D layer *manifest* files (what to load + how to style it)
  - 3D scene config (terrain/imagery/camera defaults)
  - 3D story “steps” (how narratives trigger 3D actions)
  - security/governance metadata required at the UI boundary (classification, redaction hints)

### ❌ Does *not* belong here
- **Canonical platform schemas** for STAC/DCAT/PROV (those live in the repo’s main `schemas/` directory)
- **API contracts** (OpenAPI / GraphQL SDL) — those belong under the server contract home
- **Actual 3D data** (3D Tiles tilesets, b3dm/i3dm/pnts, glTF, textures, etc.) — store/serve those from a tile server or the designated 3D assets directory, and reference them by URL/ID in manifests

---

## 🧾 Schema inventory (recommended set)

> If your repo already has schema files here, treat this section as the *index* and update names/paths accordingly.

| Schema file 📄 | Status | Validates ✅ | Typical target file(s) |
|---|---:|---|---|
| `kfm.3d-layer.v1.schema.json` | 🚧 | A single 3D “layer manifest” (tileset reference + styling + attribution + governance) | `**/*.layer.json` |
| `kfm.3d-scene.v1.schema.json` | 🚧 | A reusable 3D scene preset (terrain + imagery + camera defaults) | `**/*.scene.json` |
| `kfm.3d-story-step.v1.schema.json` | 🚧 | A story step that drives 3D actions (flyTo, toggle tileset, time sync) | `**/*.step.json` or story config JSON |
| `kfm.classification.v1.schema.json` | 🚧 | A shared governance block (classification, sovereignty tags, redaction policy) | embedded in the above |

**Naming convention (recommended):**
- `kfm.<area>.<thing>.v<major>.schema.json`
- Keep schemas **immutable** once published; breakages = new major file.

---

## 🧪 Validation (local + CI)

Any standards-compliant JSON Schema validator works.

### Option A — AJV (Node) ⚡
```bash
# one-off validate a file against a schema
npx ajv-cli validate \
  -s web/assets/maps/3d/_schemas/kfm.3d-layer.v1.schema.json \
  -d web/assets/maps/3d/**/*.layer.json
```

### Option B — Python (jsonschema) 🐍
```bash
python -m jsonschema \
  -i path/to/example.layer.json \
  web/assets/maps/3d/_schemas/kfm.3d-layer.v1.schema.json
```

### CI expectation ✅
- Any change to structured config/metadata should trigger schema validation.
- CI should fail on:
  - missing required fields
  - invalid URLs/IDs
  - governance downgrade (e.g., output marked `public` when inputs were restricted)

---

## 🔖 Versioning rules (non-negotiable)

### ✅ Do
- Embed an `$id` in every schema (stable + unique)
- Include a **major version** in the filename (e.g., `v1`, `v2`)
- Use `additionalProperties: false` by default in UI-facing contracts (tight interfaces)
- Treat new required fields as breaking changes unless defaults are safely inferable

### ❌ Don’t
- Edit a published schema in-place in a way that breaks previously-valid files
- Add ad-hoc fields “just for one dataset” — extend the schema properly

---

## 🧱 Minimal contract: what a 3D layer manifest should include

At minimum, a 3D layer manifest should carry:

- **identity**: `id`, `title`, `description`
- **type + pointers**: e.g., `kind: "3d-tiles"`, `tilesetUrl`
- **time semantics** (if applicable): `temporalExtent`, `timeBehavior`
- **attribution + licensing**: `source`, `license`, `attributionText`
- **provenance references**: references/IDs/URLs pointing to cataloged evidence (STAC/DCAT/PROV)
- **governance block**: classification + sovereignty + redaction hints

---

## 📦 Example: 3D layer manifest (`example.layer.json`)

<details>
<summary><b>Click to expand JSON</b> 👇</summary>

```json
{
  "schemaVersion": "1.0.0",
  "id": "kfm.demo.kansas-from-above",
  "title": "Kansas From Above (Demo)",
  "description": "Showcase 3D terrain + streamed 3D Tiles for demo storytelling.",
  "kind": "3d-tiles",
  "tilesetUrl": "https://tiles.example.org/kfm/kansas-from-above/tileset.json",

  "appearance": {
    "opacity": 1.0,
    "pointSize": 2.0,
    "heightOffsetMeters": 0
  },

  "temporalExtent": {
    "start": "2020-01-01",
    "end": "2020-12-31"
  },

  "provenance": {
    "stacItem": "stac:item:kfm.demo.kansas-from-above",
    "dcatDataset": "dcat:dataset:kfm.demo.kansas-from-above",
    "provBundle": "prov:bundle:kfm.demo.kansas-from-above:v1"
  },

  "attribution": {
    "source": "KFM pipeline output",
    "license": "CC-BY-4.0",
    "attributionText": "© Contributors — see dataset record for full attribution."
  },

  "governance": {
    "classification": "public",
    "sovereigntyTags": [],
    "redaction": {
      "mode": "none",
      "notes": "No redaction required for this demo layer."
    }
  }
}
```

</details>

---

## 🧩 Example: 3D story step (`example.step.json`)

<details>
<summary><b>Click to expand JSON</b> 👇</summary>

```json
{
  "schemaVersion": "1.0.0",
  "action": "flyTo",
  "target": {
    "lon": -98.0,
    "lat": 38.5,
    "heightMeters": 12000,
    "headingDeg": 0,
    "pitchDeg": -35,
    "rollDeg": 0
  },
  "layerToggles": [
    { "layerId": "kfm.demo.kansas-from-above", "visible": true }
  ],
  "notes": "Transition from 2D map to a tilted 3D view and enable the demo tileset."
}
```

</details>

---

## 🛡️ Governance & safety checklist (for every new 3D layer)

- [ ] Layer has a **license** and **attribution** (human-readable + machine-readable)
- [ ] Layer has **provenance references** (IDs/URLs back to cataloged sources)
- [ ] Layer has **classification + sovereignty tags** and does not downgrade restrictions
- [ ] Any sensitive geometry is **generalized/blurred** or excluded (as required)
- [ ] Manifest passes schema validation locally and in CI

---

## 🧰 Adding a new schema (quick recipe)

1. **Create** `kfm.3d-<thing>.v1.schema.json`
2. Add:
   - `$schema`, `$id`, `title`, `description`
   - strict `required` fields
   - `additionalProperties: false`
3. Add **one example** config file under the relevant assets folder
4. Wire validation into CI (or the repo’s validation tooling)
5. If you change a schema in a breaking way:
   - create `v2`
   - keep `v1` for backwards compatibility

---

## 🔗 Related (recommended reading inside the repo)

- 📘 KFM Master Guide (contracts + pipeline ordering): `../../../../../docs/MASTER_GUIDE_v13.md`
- 🧾 Canonical JSON Schemas (source of truth): `../../../../../schemas/`
- 🗺️ 3D assets root: `../`
