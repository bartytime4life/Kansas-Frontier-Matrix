# 🪨 Monument Rocks — Sources QA (Evidence Locker)

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-0b7285?style=for-the-badge)
![3D](https://img.shields.io/badge/3D-Model%20QA-2f9e44?style=for-the-badge)
![Provenance](https://img.shields.io/badge/Provenance-First-f59f00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active%20QA%20Spec-5c7cfa?style=for-the-badge)

> 📍 **Path:** `web/assets/3d/shared/models/monument-rocks/sources/qa/`  
> 🧾 **Purpose:** This folder is the **QA + provenance evidence locker** for everything we claim about the **Monument Rocks** 3D model — validation outputs, checksums, render proofs, performance notes, licensing proof, and reviewer sign‑off artifacts.

---

## 🧭 Why this exists (KFM alignment)

KFM’s architecture is **contract-first + provenance-first**: anything shown in the UI (including 3D) should be traceable back to **cataloged sources** and **provable processing** — no “mystery layers.”:contentReference[oaicite:0]{index=0}

This is especially important for 3D because KFM’s 3D experience is designed as a **toggleable Cesium 3D mode** (vs 2D MapLibre mode), and it’s intentionally **opt‑in** due to cost/performance constraints.:contentReference[oaicite:1]{index=1}:contentReference[oaicite:2]{index=2}

---

## 🗺️ Runtime context for this specific asset

Monument Rocks is explicitly called out as an example of a story-driven 3D experience (e.g., a “Kansas From Above” flyover that can include **Monument Rocks with a 3D model**).:contentReference[oaicite:3]{index=3}

That means QA must cover **both**:
- ✅ “Is the model correct and legally usable?”  
- ✅ “Does it behave correctly inside KFM’s 2D/3D UX and performance expectations?”

---

## 📦 What belongs in `sources/qa/`

This folder should store **evidence artifacts**, not raw working files. Keep it **reviewable** and **auditable**.

### ✅ Recommended layout (create as needed)
```text
📁 sources/qa/
  📄 README.md                 👈 you are here
  📄 qa-manifest.yml           (what was tested, when, by whom, tool versions)
  📄 checksums.sha256          (hashes for key inputs/outputs)
  📁 license/                  (license text, attribution screenshots, source proof)
  📁 validation/
    📄 gltf-validator.json
    📄 tileset-validator.json  (if applicable)
  📁 renders/
    📁 baseline/               (golden screenshots)
    📁 current/                (new screenshots for comparison)
  📁 perf/
    📄 perf-report.md          (triangles, textures, load time notes)
  📁 review/
    📄 reviewer-notes.md       (human QA notes + acceptance sign-off)
```

> 💡 **Rule of thumb:** if it justifies trust, it belongs here. If it’s just intermediate work, it belongs elsewhere.

---

## ✅ Definition of Done (DoD)

A model update is “done” when:

### 🧾 Provenance & Governance (non-negotiable)
- [ ] Source(s) documented with enough detail to reproduce/verify  
- [ ] License is present + compatible + attribution text is clear  
- [ ] Sensitivity classification reviewed (even if “public”)  
- [ ] Evidence artifacts committed here (hashes, reports, screenshots)  
- [ ] Nothing “mystery” ships into UI/Stories without traceability:contentReference[oaicite:4]{index=4}

### 🧱 Geometry & Packaging
- [ ] glTF/GLB validates (no critical errors)  
- [ ] Units, orientation, pivot/origin, and scale are documented  
- [ ] Materials/textures are consistent and web-friendly (no missing references)

### 🌍 Geospatial fit (KFM standard)
- [ ] Position/anchor metadata uses **WGS84 (EPSG:4326)** or is clearly transformable to it  
- [ ] Any reprojection/transform is explicitly recorded (don’t silently distort):contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

### ⚡ Performance & UX
- [ ] Loads reliably in **KFM 3D (Cesium)**  
- [ ] Doesn’t break **2D ⇄ 3D toggle** flows  
- [ ] Performance notes captured (tri count, texture sizes, load time)  
- [ ] Degrades gracefully (3D is opt‑in; avoid “mandatory heavy mode”):contentReference[oaicite:7]{index=7}

---

## 🧪 QA Gates (practical checklist)

> KFM QA is meant to be **multi-layered**: prevention → detection → response → continuous improvement.:contentReference[oaicite:8]{index=8}

### Gate 0 — “Can we legally ship this?” 🧾
- [ ] Source URL(s) recorded (or archive reference)  
- [ ] License text saved in `license/` (or screenshot evidence if needed)  
- [ ] Attribution string finalized (what the UI/story should display)  
- [ ] If license/sensitivity metadata is missing, **stop** — KFM QA should fail for missing essentials.:contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

### Gate 1 — Integrity & tamper evidence 🔐
- [ ] Create/refresh `checksums.sha256` for:
  - key inputs (source downloads or source manifests)
  - final model artifact(s)
  - textures/tileset bundles
- [ ] Record tooling + versions in `qa-manifest.yml`

This mirrors KFM’s intake approach: compute checksums + record them as tamper-evidence.:contentReference[oaicite:11]{index=11}

### Gate 2 — Spec validation (automated) ✅
**Suggested tools (pick what the repo/CI supports):**
- glTF Validator (for `.gltf/.glb`)
- 3D Tiles validation (if you ship `tileset.json`)

**Example CLI patterns (adapt to your toolchain):**
```bash
# glTF / GLB validation (Node-based example)
npx gltf-validator -i monument-rocks.glb -o sources/qa/validation/gltf-validator.json

# 3D Tiles validation (tooling varies; store output in sources/qa/validation/)
# <tileset-validator> tileset.json > sources/qa/validation/tileset-validator.json
```

### Gate 3 — Geospatial correctness 🧭🌍
- [ ] Confirm the anchor location/orientation is correct in-world  
- [ ] Confirm vertical placement (altitude/terrain) is correct for Cesium  
- [ ] Document assumptions (terrain drape? absolute height? local offsets?)

> KFM standardizes serving in WGS84 for web consistency.:contentReference[oaicite:12]{index=12}

### Gate 4 — Visual sanity (human) 👀
Capture screenshots and store them as regression evidence:
- [ ] `renders/baseline/` (golden)  
- [ ] `renders/current/` (new)  
- [ ] Notes: lighting differences, texture seams, normals, z-fighting, LOD pops, etc.

### Gate 5 — Performance sanity ⚡
Record at least:
- triangles / primitives
- texture count + max dimensions
- compressed/uncompressed sizes
- “first render” time on a typical dev machine (rough is fine)

KFM treats QA as more than correctness — **metrics matter** and should be tracked over time.:contentReference[oaicite:13]{index=13}

---

## 🧑‍⚖️ Governance & sensitivity (yes, even for rocks)

KFM includes sensitivity classification and UI behaviors for sensitive content (hide by default, warnings, access control, generalized coordinates, etc.).:contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

For Monument Rocks, the expected label is likely **public**, but still record:
- [ ] `sensitivity: public` (explicit > implicit)
- [ ] any usage constraints (photography license, commercial restrictions, etc.)

---

## 🔒 Security & supply-chain notes (lightweight, but real)

KFM’s automation vision includes supply-chain integrity signals (e.g., attestations, signed artifacts, tracked dependencies).:contentReference[oaicite:16]{index=16}

**Recommended minimum for 3D assets:**
- [ ] checksums recorded
- [ ] only known-safe file types committed
- [ ] no embedded executables/scripts in “asset” archives
- [ ] validate external downloads via pinned hashes where possible

### 🧰 Advanced (optional): OCI artifact packaging + signing
KFM proposes storing large/immutable artifacts in OCI registries using ORAS + Cosign, attaching provenance/attestations, improving rollback and tamper resistance.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

If the Monument Rocks model or textures become too large for Git, this is a clean future path.

---

## 🚀 Promotion rule (don’t ship half-baked)

KFM’s managed promotion principle: data/artifacts should only be “promoted” after validation/QA passes, preventing broken states and partial updates.:contentReference[oaicite:20]{index=20}

**Apply the same here:**
- keep work-in-progress outside the shipped artifact path
- only update the final served model when QA evidence is present in this folder

---

## 🧯 Rollback plan (because mistakes happen)

If a problematic model slips through (license issue, misplacement, broken tileset):
- revert to the last known good artifact
- add a QA test/check so it can’t recur (QA culture improvement):contentReference[oaicite:21]{index=21}
- document the incident and the fix in `review/reviewer-notes.md`

KFM explicitly emphasizes rollback readiness and governance logging for safety and trust.:contentReference[oaicite:22]{index=22}

---

## 🧷 PR checklist (copy/paste)

> Inspired by KFM’s contributor patterns: update source manifests, run tests, keep documentation current.:contentReference[oaicite:23]{index=23}

- [ ] Updated source reference(s) / manifest(s) (and/or `sources.json` pattern if used)
- [ ] Added/updated license & attribution proof in `sources/qa/license/`
- [ ] Updated `checksums.sha256`
- [ ] Added validation reports in `sources/qa/validation/`
- [ ] Added before/after renders in `sources/qa/renders/`
- [ ] Added perf notes in `sources/qa/perf/`
- [ ] Verified in KFM 3D mode (Cesium)
- [ ] Verified 2D ⇄ 3D toggle does not break the scene

---

## 📎 (Optional) QA Doc Metadata (machine-friendly)

KFM documentation practices encourage standardized metadata blocks for governance + integrity tracking.:contentReference[oaicite:24]{index=24}

```yaml
title: "Monument Rocks — 3D Model QA Evidence"
path: "web/assets/3d/shared/models/monument-rocks/sources/qa/README.md"
status: "active"
model_id: "monument-rocks"
asset_kind: "3d-model"
sensitivity: "public"
license: "TBD"
last_reviewed: "TBD"
doc_integrity_checksum: "sha256:TBD"
```

---

## 📚 KFM source references that informed this QA design

- **Monument Rocks appears as a 3D story example** and 3D is treated as powerful but heavy/opt‑in.:contentReference[oaicite:25]{index=25}
- **2D/3D mode design:** MapLibre for 2D + Cesium for 3D + 3D Tiles, with a user toggle that keeps context consistent.:contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}
- **WGS84 standardization** for serving geospatial data and explicit reprojection logging expectations.:contentReference[oaicite:28]{index=28}:contentReference[oaicite:29]{index=29}
- **Multi-layer QA philosophy** (catch coordinate misalignment, missing license; improve continuously).:contentReference[oaicite:30]{index=30}:contentReference[oaicite:31]{index=31}
- **Governance + sensitivity behaviors** and metadata QA expectations (OPA/policy checks; missing required fields should fail).:contentReference[oaicite:32]{index=32}:contentReference[oaicite:33]{index=33}
- **Checksums + ingestion gatekeeping** as a baseline integrity pattern to reuse for 3D assets too.:contentReference[oaicite:34]{index=34}
- **Future AR/3D layers still cataloged via STAC/DCAT** (so 3D assets benefit from the same governance stack).:contentReference[oaicite:35]{index=35}
- **Optional advanced artifact discipline:** OCI/ORAS/Cosign for signed, versioned binary artifacts with provenance attachments.:contentReference[oaicite:37]{index=37}

---

## 📚 Extra reference packs (PDF portfolios)

Some project reference PDFs are distributed as **PDF portfolios** (open in Acrobat/Reader for full browsing):
- `AI Concepts & more.pdf`
- `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf`
- `Various programming langurages & resources 1.pdf`
- `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf`:contentReference[oaicite:41]{index=41}

They’re useful for background research, but not ideal as “directly citeable” QA requirements without extracting their embedded docs first.

---

🧱 **Bottom line:** If we can’t prove it, we don’t ship it. ✅

