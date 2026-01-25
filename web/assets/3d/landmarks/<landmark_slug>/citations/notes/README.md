<!--
📍 Path:
web/assets/3d/landmarks/<landmark_slug>/citations/notes/README.md

🧠 Purpose:
This is the per-landmark “evidence pack” README that explains how to keep this landmark’s
3D asset + facts + UI narrative fully provenance-backed (KFM-style).
-->

# 🧾 Landmark Citations & Notes — `<landmark_slug>`

**Evidence-first notes + citations pack** for a single 3D landmark in the Kansas Frontier Matrix (KFM).  
This folder exists so the landmark **never becomes a “mystery layer”** in the UI, and so AI/Focus Mode can answer questions **with receipts** (citations + provenance + licensing).

---

## 🧭 Landmark Snapshot (fill these in)

- **Display name:** `<Landmark Display Name>`
- **Slug (folder name):** `<landmark_slug>` *(kebab-case, stable)*
- **Canonical ID (recommended):** `kfm.ks.landmark.<landmark_slug>`
- **Primary location (public-safe):** `<lat, lon>` *(use generalized location if sensitive)*
- **3D asset type:** `3D Tiles | glTF | other`
- **Model version:** `<semver-or-date>`
- **Classification:** `public | internal | restricted`
- **Last reviewed:** `<YYYY-MM-DD>`
- **Owner / steward:** `<name or team>`

> [!IMPORTANT]
> If the slug changes, **links break** and provenance chains get messy. Treat the slug as **immutable** once published.

---

## 🎯 What lives here (and why)

This `citations/notes/` area is the **human + machine-readable provenance hub** for the landmark’s 3D representation and any claims shown in the UI.

### This folder enables
- 🧬 **Provenance-first UI**: layer panels can show **source, license, confidence, and “how it was made.”**
- 🤖 **Focus Mode / AI answers**: responses should be able to cite **specific evidence items**.
- 🧾 **Policy gates**: automated checks can ensure **licenses exist**, required metadata is present, and sensitive content is handled correctly.
- 🧩 **Story Nodes / Pulse Threads hooks**: short narratives anchored to this landmark can point to the same evidence pack.

### This folder is *not*
- ❌ the place for large raw datasets (those belong in the canonical data pipeline directories)
- ❌ a “pretty description” with no supporting sources
- ❌ a dumping ground for unlicensed images/scans/textures

---

## 🧱 How this fits the KFM pipeline

KFM’s “boundary artifacts” idea is: **nothing is “published” without metadata + lineage**.  
For a 3D landmark, that means the *visual* asset may live in `web/assets/...`, but the *truth* (sources + provenance + license) must be traceable.

```mermaid
flowchart LR
  A[📥 Raw Sources\n(data/raw...)] --> B[🧪 Processing\n(data/work...)]
  B --> C[📦 Processed Outputs\n(data/processed...)]
  C --> D[🗂️ Catalogs\nSTAC/DCAT/PROV]
  D --> E[🧠 Graph + API\nNeo4j + PostGIS]
  E --> F[🗺️ UI + 3D View\n(web/...)]
  F --> G[🧾 This folder\ncitations/notes]
  G -. "feeds" .-> F
  G -. "feeds" .-> E
```

> [!NOTE]
> KFM’s architecture pattern expects **PostGIS** to stay authoritative for geometry operations, while **Neo4j** stores relationships + narrative context. The UI should consume governed results via API (for redaction/classification), not directly query the graph.

---

## 📁 Expected folder structure

Here’s the recommended structure around this README (adjust if your landmark uses different subfolders):

```text
web/
└─ assets/
   └─ 3d/
      └─ landmarks/
         └─ <landmark_slug>/
            ├─ 📦 model/                 # 3D Tiles / glTF / textures (implementation-defined)
            ├─ 🖼️ preview/               # thumbnails, posters, turntable renders
            └─ 🧾 citations/
               ├─ sources/               # optional: small source PDFs/images used for citations
               └─ notes/
                  ├─ README.md           # ✅ you are here
                  ├─ CITATIONS.md        # ✅ compact human citation block (3–7 lines)
                  ├─ NOTES.md            # ✅ longform research notes + decisions
                  ├─ evidence/
                  │  └─ EM-<id>.yaml     # ✅ machine-readable evidence manifest
                  ├─ prov/
                  │  └─ prov.jsonld      # ✅ provenance bundle tying model + facts to evidence
                  ├─ LICENSES.md         # ✅ license + attribution notes (if not embedded elsewhere)
                  └─ CHANGELOG.md        # optional: notes-only changelog (not model versioning)
```

---

## ✅ Minimum required artifacts (Definition of “done”)

Before a landmark is considered **publishable**, ensure:

- [ ] `CITATIONS.md` exists and is **short + readable** (3–7 lines)
- [ ] `evidence/EM-<id>.yaml` exists with **all sources referenced**
- [ ] `prov/prov.jsonld` exists linking:
  - sources → transformations → outputs → this landmark
- [ ] licensing is explicit for:
  - source materials
  - derived model/tiles
  - textures/images
- [ ] sensitivity classification is set and respected (see below)

---

## 🧾 Citation model used by KFM-style content

We keep three layers of “proof”:

### 1) Human-readable citations (fast trust)
Used in popups, panels, Story Nodes, and footers.

✅ File: `./CITATIONS.md`  
Goal: a **tiny citation block** that a human can scan quickly.

### 2) Evidence Manifest (machine trust)
A structured inventory of every evidence item with identifiers/checksums and “how used.”

✅ File: `./evidence/EM-<id>.yaml`

### 3) PROV bundle (lineage trust)
A compact provenance graph linking the landmark model + claims to the evidence items and processing activities.

✅ File: `./prov/prov.jsonld`

> [!TIP]
> If you write a claim in `NOTES.md`, you should be able to point to **at least one evidence item ID** in the EM file.

---

## 🧩 Templates you can copy/paste

<details>
<summary>📄 <strong>Template: CITATIONS.md</strong> (3–7 lines only)</summary>

```md
# Citations (verify)

[1] <Source title> — <Author/Org>, <Year>. <Identifier or archive ref>
[2] <Dataset / map / survey> — <Publisher>, <Version/Date>. <Dataset ID or accession>
[3] <Photo / scan / field note> — <Creator>, <Date>. <Collection / local file ref>

> Verification note: Each citation maps to an entry in `evidence/EM-<id>.yaml`.
```
</details>

<details>
<summary>🧾 <strong>Template: evidence/EM-&lt;id&gt;.yaml</strong></summary>

```yaml
# Evidence Manifest (EM)
# Keep this small, explicit, and machine-parsable.

em_id: "EM-<id>"
landmark:
  id: "kfm.ks.landmark.<landmark_slug>"
  slug: "<landmark_slug>"
  name: "<Landmark Display Name>"
  classification: "public"   # public | internal | restricted
  location_public:
    lat: <float>
    lon: <float>

outputs:
  # What this evidence supports/produces
  - output_id: "model-<version>"
    type: "3d_asset"
    path: "web/assets/3d/landmarks/<landmark_slug>/model/<...>"
    format: "3d-tiles"       # 3d-tiles | gltf | other
    sha256: "<optional-if-stored>"
    notes: "Main landmark model used in UI."

evidence:
  - evidence_id: "EV-001"
    type: "document"         # document | dataset | image | field_note | scan | lidar | photogrammetry | etc
    title: "<Title>"
    creator: "<Author/Org>"
    date: "<YYYY-MM-DD or YYYY>"
    license: "<SPDX-or-text>"
    local_path: "../sources/<filename.ext>"     # optional if stored here
    external_ref: "<accession/dataset-id/etc>"  # avoid raw URLs in prose; keep refs as IDs when possible
    checksum:
      sha256: "<sha256-if-available>"
    used_for:
      - "historical_fact:founding_date"
      - "model_reference:geometry"
    excerpt:
      # optional: how to re-find the key portion
      locator: "<page/figure/table/line-range>"
      note: "<why it matters>"

transformations:
  - activity_id: "ACT-<id>"
    type: "3d_model_build"
    agent: "<person|team|pipeline>"
    toolchain:
      - "<tool>@<version>"
      - "<tool>@<version>"
    inputs:
      - "EV-001"
      - "EV-002"
    outputs:
      - "model-<version>"
    parameters:
      coordinate_system: "<EPSG/definition>"
      scale_units: "meters"
      notes: "Any critical settings that affect reproducibility."

quality:
  confidence: "medium"       # low | medium | high
  review:
    reviewer: "<name>"
    date: "<YYYY-MM-DD>"
    notes: "<what was checked>"
```
</details>

<details>
<summary>🧬 <strong>Template: prov/prov.jsonld</strong> (compact PROV bundle)</summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://example.invalid/kfm#"
  },
  "@graph": [
    {
      "@id": "kfm:kfm.ks.landmark.<landmark_slug>",
      "@type": "prov:Entity",
      "prov:label": "<Landmark Display Name>",
      "kfm:classification": "public"
    },
    {
      "@id": "kfm:activity:ACT-<id>",
      "@type": "prov:Activity",
      "prov:label": "3D model build for <landmark_slug>",
      "prov:used": [
        { "@id": "kfm:evidence:EV-001" },
        { "@id": "kfm:evidence:EV-002" }
      ],
      "prov:generated": { "@id": "kfm:output:model-<version>" }
    },
    {
      "@id": "kfm:output:model-<version>",
      "@type": "prov:Entity",
      "prov:label": "3D asset for <landmark_slug>"
    }
  ]
}
```
</details>

<details>
<summary>📝 <strong>Template: NOTES.md</strong> (research notes + decisions)</summary>

```md
# Notes — <Landmark Display Name> (<landmark_slug>)

## Summary (2–5 bullets)
- …
- …

## Key Facts (with evidence IDs)
- Fact: … (Evidence: EV-001)
- Fact: … (Evidence: EV-003)

## 3D Model Provenance
- Source geometry: … (EV-…)
- Capture method: …
- Toolchain + versions: …
- Coordinate system + units: …
- Known limitations: …

## Modeling Decisions (why we did it this way)
- Decision: … (Reason: …, Evidence: EV-…)
- Decision: …

## Sensitivity / Ethics
- Classification: …
- Redactions/generalization applied: …
- Notes: …

## Open Questions / TODO
- …
```
</details>

---

## 🗺️ 3D + geospatial metadata checklist (don’t skip)

When the landmark is visualized in 3D, small metadata mistakes become *big* UX bugs. Capture:

- [ ] **Coordinate reference system** for sources and final asset
- [ ] **Scale units** (meters vs feet) and any scaling applied
- [ ] **Orientation** (north alignment, up axis) and any transforms
- [ ] **Bounding box / footprint** (public-safe if sensitive)
- [ ] **Capture date(s)** (photogrammetry flights, LiDAR acquisitions, surveys)
- [ ] **LOD strategy** (if 3D Tiles): LOD levels, tile sizing, simplification approach
- [ ] **Textures**: resolution, compression, provenance/licensing for each texture source
- [ ] **Performance notes**: triangle count, draw calls, known hotspots

---

## 🔐 Sensitivity, CARE, and “do no harm”

Some landmarks (especially archaeological/cultural sites) should not expose precise locations or revealing details.

- **Classification** must be explicit: `public | internal | restricted`
- If sensitive:
  - generalize or fuzz coordinates in public-facing metadata
  - avoid publishing high-resolution scans that enable looting/vandalism
  - document *why* restrictions exist and who the steward is

> [!WARNING]
> “Cool to share” is not the same as “ethical to publish.”  
> If you’re unsure, default to **restricted** and add a TODO to consult the proper steward/community.

---

## 📜 Licensing & attribution (UI-ready)

Every 3D landmark should have a clear attribution string and license posture.

✅ Include in either `LICENSES.md` or in the EM file:

- Source licenses (per evidence item)
- Derived model license
- Texture/image licenses
- Any required attribution language

**Recommended UI attribution string (copy/paste):**
> `<Landmark Display Name> 3D model derived from <sources>; processed by KFM; license: <...>.`

---

## 🤖 AI / Focus Mode support (make answers citeable)

To help the AI stay evidence-backed:

- Prefer **atomic facts** with evidence IDs (in `NOTES.md`)
- Keep citations resolvable via `EM-<id>.yaml`
- Mark uncertain claims explicitly:
  - `confidence: low`
  - `assumption: …`
  - `needs verification: …`

> [!NOTE]
> In KFM, analysis outputs and AI-generated artifacts should be treated as first-class datasets with provenance.
> If AI generated *any* part of this landmark representation (text, classification, derived metrics), capture it as a transformation/activity with toolchain details.

---

## 🧪 QA & policy-gate checklist (pre-merge)

- [ ] No missing licenses
- [ ] No “naked claims” (claims without evidence IDs)
- [ ] Evidence manifest enumerates all sources used
- [ ] PROV bundle links evidence → activity → output
- [ ] Sensitive info reviewed and properly classified
- [ ] Reproducibility notes included (tool versions, parameters, environment hints)
- [ ] Second set of eyes review (when possible) ✅

---

## 🧠 Optional: Story Node / Pulse Thread hooks for this landmark

If this landmark has time-sensitive updates or narrative threads (restoration, discovery, events), record **seeds** here so they can be promoted into Story Nodes or Pulse Threads later:

- **Pulse candidate:** `<short headline>`
  - Why it matters: …
  - Evidence: `EV-…`, `EV-…`
  - Suggested map anchor: `<region/place>`
  - Status: `draft | reviewed | published`

---

## ✍️ Editing rules (keep it clean)

- Use **plain Markdown** (headings, bullets, short paragraphs)
- Prefer **evidence IDs** over raw links in prose
- Keep `CITATIONS.md` short (3–7 lines)
- Put long discussion in `NOTES.md`
- Avoid storing large binaries here unless unavoidable

---

## ✅ “Good” looks like this

- A user clicks the landmark → sees **source + license + confidence**
- A story references the landmark → has a **tiny citation block** + “View Evidence”
- A maintainer audits a claim → can open **EM + PROV** and trace inputs
- Policy gates pass because metadata + licensing + classification are explicit

---

## 📚 Project references that define this contract (read when in doubt)

- KFM technical standards + repo conventions
- KFM architecture: PostGIS + Neo4j roles, catalog-driven design
- KFM data intake: STAC/DCAT/PROV alignment, evidence-first pipeline expectations
- KFM UI overview: provenance visibility + user trust patterns
- KFM AI overview: Focus Mode citation discipline and governance rules
- Pulse Threads / evidence manifests: compact citations + machine-readable manifests + PROV bundles
- Markdown authoring guides: structure + conventions for long-lived docs
- Supporting geospatial/3D resources: WebGL, geospatial processing, data management patterns

