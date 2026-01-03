# 🌐 `web/public/` — Static Public Assets (UI “surface area”)

![path](https://img.shields.io/badge/path-web%2Fpublic-informational)
![ui](https://img.shields.io/badge/UI-React%20%2B%20Map%20UI-blue)
![maps](https://img.shields.io/badge/maps-MapLibre%20%7C%20Leaflet%20%7C%20Cesium-success)
![policy](https://img.shields.io/badge/policy-public%20means%20public-red)

> [!IMPORTANT]
> Everything in `web/public/` is **served directly to the browser**.  
> Treat this folder as the project’s **public interface** 🧭 — if it’s here, assume it can be fetched by anyone in production.

---

## 🔗 Quick links

- 🔙 Back to Web App: `../README.md`
- 🏠 Repo Root: `../../README.md`
- 📚 Canonical project rules / architecture: `../../docs/MASTER_GUIDE_v13.md` (if present)

---

## 🎯 Purpose

This folder is for **non-secret, non-sensitive** files that must be available at runtime **without** going through JS/TS module imports.

Typical use-cases ✅
- 🧷 Favicons + app icons
- 🪪 PWA/metadata files (e.g., `manifest.json`)
- 🖼️ Social preview images (OpenGraph / Twitter cards)
- 🧩 Runtime JSON config that is safe to ship (e.g., UI feature flags, a “layer catalog” index)
- 🧪 Tiny demo GeoJSON for local development (only if it’s explicitly public-safe)

---

## 🧠 Where `web/public/` sits in the KFM-style pipeline

```mermaid
flowchart LR
  U[🌍 Browser UI] -->|HTTPS| A[🧰 API Gateway / Backend]
  A --> D[(🗄️ Data Stores / Catalogs / Graph)]
  D --> A
  A --> U

  P[📁 web/public (static assets)] -. served as-is .-> U
```

### The core rule 🧷
**Static assets are for presentation + harmless runtime configuration.**  
Anything that “looks like data” (indexes, catalogs, tiles, story nodes, etc.) should be treated as governed output and **served via the API**, not hard-coded as public files.

> [!NOTE]
> If a user can see it in the UI, we should be able to answer: **where did it come from, how was it generated, what version is it, and what governance rules apply?** ✅

---

## 📁 Suggested layout (recommended)

> This is a *convention*, not a hard requirement. Keep it boring and predictable.

```text
📁 web/
  📁 public/
    📄 README.md            👈 you are here
    📄 robots.txt           (optional)
    📄 manifest.json        (optional)
    🖼️ favicon.ico          (optional)
    📁 icons/               🧷 app icons + PWA icons
    📁 images/              🖼️ OG images, logos, UI illustrations
    📁 fonts/               🔤 self-hosted fonts (if allowed/licensed)
    📁 config/              🧩 non-secret runtime JSON config
    📁 demo/                🧪 tiny public-safe sample data only
```

---

## ✅ Allowed here

- **Brand/UI assets**: logos, icons, favicons, OG images 🖼️
- **Non-sensitive runtime config** (small JSON only) 🧩
  - feature flags (e.g., enable/disable 3D)
  - UI defaults (e.g., timeline start/end, default layer)
  - “catalog stubs” *only if* they do not contain sensitive details
- **Small demo content** for local dev 🧪
  - Keep it tiny, anonymized, and explicitly “safe to publish”.

---

## ⛔ Not allowed here

- 🔑 **Secrets**: API keys, tokens, service credentials, signed URLs
- 🧬 **Sensitive datasets** (even if “just JSON”)
- 🗺️ **Raw or large geospatial assets** (big GeoJSON, rasters, tiles, scans)
- 🧾 **Anything requiring governance** (restricted locations, protected sites, private notes)
- 🧨 **Build outputs** committed accidentally (e.g., `dist/`, `build/`) unless the repo explicitly requires it

> [!TIP]
> If you’re unsure whether something is sensitive: assume it is, and route it through the governed pipeline + API instead. 🛡️

---

## 🧪 Local preview (quick checks)

### Option A — super simple (Python)
From `web/public/`:
```bash
python -m http.server 8000
```
Then open: `http://localhost:8000/` 🌍

### Option B — Express static server (Node)
A minimal dev server example:
```js
const express = require("express");
const app = express();

// serve ./public at the site root
app.use(express.static("public"));

app.listen(3000, () => console.log("http://localhost:3000"));
```

> [!NOTE]
> Your actual dev workflow may be Vite/Next/CRA/etc. The point here is: **static files should load correctly** and **paths should resolve**.

---

## 🗺️ Map UI expectations (how public assets typically support the viewer)

Even though application logic lives in `web/src/…`, `web/public/` commonly provides:
- 🧷 Icons for map controls (timeline, layers, 2D/3D toggle)
- 🖼️ Layer thumbnails / legends
- 🧩 Safe “bootstrap config” (e.g., default layer, default year)
- 🧪 Demo datasets for UI prototyping

Common KFM-style interactions this folder may support:
- 🗓️ **Timeline slider** with tick marks + step controls
- 🧭 **2D Map ↔ 3D Globe toggle** (lazy-load heavier 3D resources for performance)
- 🧾 **Popups / side panels** showing contextual info and linked document references
- 📈 **Charts** (time-series / trend views) driven by API-returned data, not embedded public blobs

---

## 📱 Responsive + accessibility rules of thumb

- 📐 Design for *side panel + main map panel* layouts (desktop), and *collapsible overlays* (mobile)
- ⌨️ Keyboard navigation matters for:
  - timeline stepping
  - layer toggles
  - popup focus management
- 🏷️ Always add `alt` text for meaningful images
- 🎨 Don’t encode meaning with color alone (legends + labels + patterns help)

> [!IMPORTANT]
> Accessibility is not “nice to have” — it’s part of human-centered design. ❤️

---

## 🔐 Security & governance guardrails (read this twice)

### 1) Public folder = “DMZ mindset” 🧱
Assume production deployments serve static assets from hardened edge infrastructure (HTTPS only).  
So: **never** treat `web/public/` as a safe place to stash “temporary” files.

### 2) Don’t bypass the API 🧰
If a file represents governed data, it should be:
- produced deterministically by the pipeline
- versioned
- served by the API
- referenced by the UI via API calls

### 3) Track provenance + licensing 🧾
Every third‑party asset (icons, fonts, images) must have:
- a license ✅
- a source reference ✅
- attribution text ✅

**Suggested pattern:** maintain a simple `web/public/ATTRIBUTION.md` (create it if missing).

---

## 🧰 Adding or updating an asset (checklist)

1. 📦 Put the file in the right subfolder (`icons/`, `images/`, `fonts/`, `config/`)
2. 🧼 Optimize it (size + compression)
3. 🏷️ Add attribution + license info (if not created by us)
4. 🔗 Update references in UI code (prefer predictable paths)
5. 🧪 Verify locally (preview server + in-app)
6. 🛡️ Sanity check: “Would I be OK with this file being on the open internet forever?”

---

## 🧯 Troubleshooting

- **404 on asset**
  - Check leading slash vs relative path
  - Confirm the build/deploy tool copies `public/` to the output
- **Old icon/image won’t update**
  - Browser caching: rename with a version suffix (`logo.v2.svg`) or use hashed filenames
- **Works locally but not on GitHub Pages**
  - Base paths differ; prefer relative URLs when possible

---

## 📚 Reference shelf (project library)

If you want deeper background on the design choices that inform this folder, see the project’s reference docs (PDF/library) such as:
- 📘 *Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation*
- 🧾 *MARKDOWN_GUIDE_v13* (contract-first, deterministic pipeline, governance rules)
- 🗺️ *Kansas-Frontier-Matrix — Open-Source Geospatial Historical Mapping Hub Design*
- 🧱 *Node.js Notes for Professionals* (static hosting patterns)
- 📐 *Responsive Web Design with HTML5 and CSS3*
- 🧭 *WebGL Programming Guide* (3D rendering concepts)

---

### ✅ Definition of Done for changes in `web/public/`

- [ ] No secrets added 🔑❌
- [ ] Asset optimized (size + format) 🧼
- [ ] Attribution included (if applicable) 🧾
- [ ] Verified paths load in dev + prod-like build 🧪
- [ ] Governance check passed (public-safe) 🛡️