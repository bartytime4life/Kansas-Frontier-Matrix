# 🧳 04 — Offline Packs (MCP Gate Example)

![Example](https://img.shields.io/badge/example-04--offline--packs-blue)
![MCP](https://img.shields.io/badge/MCP-Master%20Coder%20Protocol-6e40c9)
![Gates](https://img.shields.io/badge/gates-fail--closed-critical)
![Formats](https://img.shields.io/badge/formats-PMTiles%20%7C%20MBTiles%20%7C%20GeoParquet%20%7C%20COG-informational)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%7C%20DCAT%20%7C%20PROV-success)
![Supply%20Chain](https://img.shields.io/badge/supply%20chain-OCI%20%2B%20Cosign-success)

> [!NOTE]
> **Offline Packs** are a first-class KFM feature idea: a **self-contained bundle** for a region/theme (e.g., a county) containing **pre-rendered tiles + curated layers + story content + an embedded mini-app** for use in low/no connectivity settings (field work, classrooms, museum kiosks). 🗺️📦

---

## 📍 Where you are

`mcp/gates/examples/04-offline-packs/README.md`

This example shows how to treat an **Offline Pack** as an **evidence-first, policy-gated artifact** — not “a zip file someone made on a laptop.”

---

## 🎯 What this example builds

An **Offline Pack** that can be:

- **Downloaded once**, then used **fully offline**
- Opened as:
  - a **mini web app** (static site / PWA) 🧩
  - or packaged into a **standalone desktop/mobile shell** (e.g., Electron) 🖥️📱
- Verified via:
  - **policy gates** (fail-closed)
  - **provenance** (STAC/DCAT/PROV)
  - **supply-chain signatures** (OCI + Cosign)

> [!TIP]
> KFM’s UI architecture (React + MapLibre/Cesium) is intentionally **config-driven + API-decoupled**, which makes it realistic to point the same UI at **local** tile/data sources inside a pack.

---

## 🧠 Core idea: Offline Pack == “Distribution Artifact” (not a one-off export)

Offline packs inherit KFM’s non-negotiables:

- ✅ **Provenance-first**: every dataset/story/model in the pack has traceable lineage (STAC/DCAT/PROV)
- ✅ **Catalog-driven**: pack contents are selected by *IDs* (datasets, story nodes, artifacts), not ad-hoc files
- ✅ **Fail-closed governance**: if anything is missing (license, sensitivity tag, provenance), the **gate closes**
- ✅ **Reproducible**: pack build generates a **run manifest**, canonicalized + hashed (deterministic identity)
- ✅ **Signed distribution**: the final pack is published as a content-addressed artifact (OCI) and signed (Cosign)

---

## 📦 Pack anatomy

| What’s inside 🧩 | Typical format(s) 📄 | Why it exists ✅ |
|---|---|---|
| Map tiles (vector) | **PMTiles** (preferred), MBTiles | Fast offline map rendering without a tile server |
| Map tiles (raster) | COG tiles, MBTiles | Offline basemaps / imagery |
| Feature data | GeoParquet, GeoJSON, CSV snapshots | Analytics + filtering, reproducible exports |
| Story Nodes | Markdown + JSON config | Guided narratives that work offline |
| Citations & evidence | “evidence manifest” JSON, source pointers | Enforce “map behind the map” transparency |
| Catalog | STAC Collection(s) + DCAT record(s) | Make contents searchable + federatable |
| Provenance | PROV (e.g., JSON-LD) | Trace how assets were produced |
| Mini-app UI | static site / PWA bundle | Browse everything without a backend |
| Policy metadata | classification / CARE flags | Prevent unsafe sharing + enforce ethics |

---

## 🗂️ Example folder layout

```text
mcp/
  gates/
    examples/
      04-offline-packs/
        README.md                # 👈 you are here
        pack.spec.yaml           # 🧾 what to include (region/layers/stories/limits)
        policies/
          offline-pack.rego      # 🚦 OPA/Rego checks (fail-closed)
        scripts/
          build-pack.ts          # 🛠️ example builder (or python equivalent)
          verify-pack.ts         # 🔍 verify signature + policy + manifests
        dist/
          <pack-id>/
            pack.manifest.json   # 📌 pack identity + contents index
            run.manifest.json    # ♻ reproducibility ledger record
            catalog/
              stac.collection.json
              dcat.dataset.json
              prov.jsonld
            assets/
              tiles/
              data/
              media/
            ui/
              index.html
              assets/...
```

> [!IMPORTANT]
> `dist/` should typically be **gitignored** — packs are *built artifacts* and published via OCI, not committed.

---

## 🧾 Pack spec (the “protocol”)

In MCP terms, this spec is your **experiment protocol**: it states the **objective**, **materials**, **methods**, and **expected outputs** (and becomes part of provenance). 🧪🧠

### `pack.spec.yaml` (example)

```yaml
pack:
  id: kfm-offline-county-douglas-v1
  name: "KFM Education Pack — Douglas County (v1)"
  description: "Offline classroom/field bundle: key layers + story nodes + map tiles."
  version: "1.0.0"
  created_by: "kfm-bot|human-maintainer"
  created_at: "2026-01-23"

scope:
  region:
    type: "county"
    name: "Douglas"
    state: "KS"
    bbox: [-95.6, 38.8, -95.0, 39.2]
  time:
    start: "1850-01-01"
    end: "1950-12-31"

contents:
  layers:
    - dataset_id: "kfm.dataset.surficial_geology.ks.v1"
      modes: ["map", "download", "analysis"]
      formats: ["pmtiles", "geoparquet"]
    - dataset_id: "kfm.dataset.railroads_historic.ks.v2"
      modes: ["map"]
      formats: ["pmtiles"]
  stories:
    - story_id: "kfm.story.settlement_patterns_douglas"
    - story_id: "kfm.story.rail_expansion_1880_1920"
  media:
    include_thumbnails: true
    include_story_images: true

map:
  renderer: "maplibre"
  vector_tiles:
    format: "pmtiles"
    zoom_min: 5
    zoom_max: 12
  styles:
    - "styles/kfm-default.json"

ai:
  focus_mode:
    enabled: true
    offline_behavior:
      mode: "restricted"   # options: restricted | disabled | on_device
      on_device_model_ref: null # optional OCI ref if using on-device model

governance:
  license_required: true
  sensitivity:
    enforce: true
    allowed_levels: ["public", "low_risk"]
  care:
    enforce: true
    require_authority_to_control_flag: true
  secrets_scan: true

build:
  ui:
    mode: "pwa"           # pwa | static | electron
    entry_route: "/offline"
  publish:
    method: "oci"
    registry: "ghcr.io/<org>/kfm-offline-packs"
    sign_with_cosign: true
```

---

## 🚦 Gate chain overview

This example models Offline Pack creation as a **sequence of gates** — each gate produces auditable outputs and can **fail-closed**.

```mermaid
flowchart LR
  A[🧾 Spec In] --> B[🔎 Resolve IDs → immutable artifact digests]
  B --> C[🚦 Policy Gate (OPA/Rego)]
  C --> D[📦 Materialize assets (tiles/data/media)]
  D --> E[🗂️ Build catalog (STAC/DCAT/PROV)]
  E --> F[🧩 Bundle mini-app (static/PWA/Electron)]
  F --> G[🧾 Run Manifest + Hash (deterministic)]
  G --> H[📤 Publish to OCI registry]
  H --> I[🔏 Sign (Cosign) + attach attestations]
  I --> J[✅ Verify (signature + policy + integrity)]
```

### Gates in plain language 🧱

- **Resolve**: convert dataset/story IDs → exact immutable digests (so “what’s inside” is unambiguous)
- **Policy**: enforce license/sensitivity/provenance requirements (**gate closes** if missing)
- **Materialize**: build or fetch PMTiles/MBTiles/GeoParquet/COGs for the region + time range
- **Catalog**: generate STAC + DCAT + PROV (+ evidence manifests)
- **Bundle UI**: produce a local mini-app pointing at pack-local assets
- **Run manifest**: canonicalize + hash the build record (reproducibility identity)
- **Publish & sign**: treat the pack as a distributable artifact (OCI + Cosign)
- **Verify**: consumers verify before use (especially in sensitive contexts)

---

## ▶️ Quickstart (developer flow)

> [!WARNING]
> Commands below are **reference commands**. Wire them to your repo’s actual CLI (Node/TS or Python), but keep the **gate semantics** the same.

### 1) Build the pack

```bash
# from repo root
mcp gate run offline-pack \
  --spec mcp/gates/examples/04-offline-packs/pack.spec.yaml \
  --out  mcp/gates/examples/04-offline-packs/dist
```

### 2) Run the mini-app locally (offline)

```bash
# any static server works
npx http-server mcp/gates/examples/04-offline-packs/dist/kfm-offline-county-douglas-v1/ui -p 4173
```

Open: `http://localhost:4173`

✅ You should see:
- Map loads from **local tiles**
- Story nodes render from **pack content**
- Provenance/metadata panels still work (because they’re local)

### 3) Verify integrity + governance (consumer-side)

```bash
mcp gate verify offline-pack \
  --pack mcp/gates/examples/04-offline-packs/dist/kfm-offline-county-douglas-v1
```

---

## 📤 Publishing (OCI) + 🔏 Signing (Cosign)

Offline packs should ship like software:

- **OCI registry** for distribution (versioned, digest-pinned)
- **Cosign signatures** for chain-of-custody
- Optional referrers:
  - SBOM
  - provenance attestation
  - policy attestation

### Publish (example)

```bash
oras push ghcr.io/<org>/kfm-offline-packs/kfm-offline-county-douglas-v1:1.0.0 \
  ./dist/kfm-offline-county-douglas-v1:application/vnd.kfm.offlinepack.v1+dir
```

### Sign (example)

```bash
cosign sign ghcr.io/<org>/kfm-offline-packs/kfm-offline-county-douglas-v1:1.0.0
```

### Verify (example)

```bash
cosign verify ghcr.io/<org>/kfm-offline-packs/kfm-offline-county-douglas-v1:1.0.0
```

> [!TIP]
> Prefer pulling by **digest** in automation (immutable), and use tags only for humans.

---

## 🧾 Run manifest (reproducibility ledger)

Each build should generate something like:

- `run.manifest.json` (canonicalized)
- `canonical_digest` = SHA-256 of the canonical form
- tool versions
- input digests
- output digests
- errors/warnings

This enables:

- idempotency (“did we already build this exact pack?”)
- provenance linking (PROV Activity ↔ run manifest digest)
- policy checks on the build itself (“was this produced by CI?”)

---

## 🔐 Governance & safety (Offline is *higher risk*)

Offline distribution increases the “blast radius” of mistakes. This example treats governance as **mandatory**:

### Minimum policy checks (suggested)

- ✅ License present for every dataset/story
- ✅ STAC/DCAT/PROV present for every artifact
- ✅ Sensitivity classification present and within allowed set
- ✅ CARE flags (Authority to Control, Ethics constraints) enforced
- ✅ “No secrets” scan (don’t embed tokens/keys in config)
- ✅ Size/zoom limits (avoid accidental 40GB packs)
- ✅ Geo-obfuscation required for sensitive sites (if permitted at all)

> [!IMPORTANT]
> If data includes culturally sensitive locations (e.g., heritage sites) the policy should enforce **generalization/obfuscation** or require **Council approval** before pack publication.

---

## 🤖 Focus Mode offline behavior

Offline packs can include Focus Mode in three modes:

1. **disabled** 🚫 (UI hides it)
2. **restricted** 🧭 (no live model; only pre-indexed, evidence-backed retrieval + citations)
3. **on_device** 📱 (bundle a small on-device model — treated as an artifact with model card + signatures)

> [!NOTE]
> The KFM AI design explicitly expects offline packs to support offline browsing, while **Focus Mode may be limited offline unless an on-device model is packaged**.

---

## ✅ Acceptance checklist (what “done” looks like)

- [ ] Pack builds from spec without manual edits
- [ ] Policy gate fails closed when:
  - [ ] license missing
  - [ ] provenance missing
  - [ ] sensitivity tag missing
- [ ] UI loads offline with:
  - [ ] local PMTiles/MBTiles
  - [ ] story nodes + media
- [ ] Pack includes:
  - [ ] STAC Collection(s)
  - [ ] DCAT Dataset record(s)
  - [ ] PROV record
  - [ ] run manifest + digest
- [ ] OCI publish works
- [ ] Cosign verify passes
- [ ] Consumer verify blocks unsigned/invalid packs

---

## 🧩 Extensions (easy upgrades)

### 🧊 “Dual-format” packaging everywhere
Follow the “analysis-friendly + visualization-friendly” pattern:

- **GeoParquet** for analytics
- **PMTiles** for fast rendering

…and register both via STAC/DCAT with hashes.

### 🌍 3D + terrain offline (Cesium)
Add:
- 3D tilesets
- offline terrain bundles
- local imagery

### 📸 Field capture + sync later
Extend the mini-app to capture:
- geotagged photos
- notes
- annotations

Store locally (indexed) and sync when back online (through normal gated intake).

### 🕶️ AR “in the field”
Use offline packs as the substrate for AR overlays:
- local features + story context
- device-based positioning
- careful privacy controls

---

## 📚 Related docs & patterns

This example is designed to align with:

- 🗺️ **UI Offline Data Packs & Field Use** (React UI, provenance-first UX)
- 🧭 **AI System Overview** (offline pack support, offline Focus Mode constraints)
- 🧱 **Architecture & Design** (MapLibre local tiles, Cesium offline terrain options)
- ♻ **Data Intake Guide** (policy packs, provenance-first, CI gates, run manifests)
- 🔏 **Supply-chain concepts** (OCI + Cosign signatures)
- 🧪 **MCP documentation** (protocols, reproducibility, experiment logs, QA)
- 🧩 **Design audit recommendations** (modular docs, model cards, experiment reports)

---

## 🧯 Troubleshooting

<details>
<summary>Tiles don’t load offline</summary>

- Ensure tile URLs are **relative** inside the pack (no `https://...`)
- Confirm the style JSON points to `pmtiles://./assets/tiles/...`
- Serve the UI via a local server (file:// can break fetch/CORS)

</details>

<details>
<summary>Policy gate fails unexpectedly</summary>

- Inspect `policies/offline-pack.rego` output
- Check that each dataset/story has:
  - license
  - classification
  - provenance references
  - catalog entries (STAC/DCAT)

</details>

<details>
<summary>Pack is too large</summary>

- Reduce `zoom_max`
- Reduce region size (bbox/county)
- Switch heavy rasters to lower-res
- Exclude nonessential media

</details>

---

## ✅ Next step

If you implement this example for real, add a **Pack Card** (like a Model Card) to every published pack:

- what it contains
- intended use
- excluded use
- sensitivity & CARE notes
- how to verify signatures
- how to cite it

That turns offline packs into trustworthy, shareable “mini-atlases.” 🧭📦✨

