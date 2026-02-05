<!--
📄 Path: web/src/assets/_meta/licenses/README.md
🎯 Purpose: License + attribution registry for anything that ships in the web client bundle.
-->

![KFM](https://img.shields.io/badge/KFM-Kansas%20Frontier%20Matrix-0b7285)
![Governance](https://img.shields.io/badge/governance-policy--as--code-6f42c1)
![Licensing](https://img.shields.io/badge/licenses-tracked%20%26%20auditable-1f883d)

# 📜 Licenses & Attribution Registry (Web Assets)

This directory is the **source-of-truth** for licensing + attribution metadata for **static assets that are bundled and shipped** with the KFM web client.

KFM is built around transparency and traceability — “the map behind the map.” If an asset ends up inside the client build, we must be able to answer:

- **Where did it come from?** 🧭
- **What license governs it?** 📄
- **What attribution is required (and where do we show it)?** 🏷️
- **Did we modify it?** ✍️
- **When was its license last verified?** 🗓️

> [!IMPORTANT]
> **No License, No Launch 🚫🚀**  
> If we can’t clearly document an asset’s origin + license + required attribution, it **does not ship**.

---

## 🧭 Table of Contents

- [Why this exists](#-why-this-exists)
- [What belongs here](#-what-belongs-here)
- [What does not belong here](#-what-does-not-belong-here)
- [Recommended layout](#-recommended-layout)
- [License record schema](#-license-record-schema)
- [Attribution surfaces in the UI](#-attribution-surfaces-in-the-ui)
- [Review checklist](#-review-checklist)
- [Governance hooks](#-governance-hooks)
- [Common pitfalls](#-common-pitfalls)
- [FAQ](#-faq)

---

## 🧠 Why this exists

Licensing is not a “paperwork later” item — it is **part of provenance**.

In GIS and mapping, it’s easy to accidentally violate rights by copying *representation* (symbols, line styles, color ramps, labels, screenshots) even when the *facts* are public. The web bundle is also the highest-risk distribution channel because it is public and easily redistributed.

This folder makes licenses **visible, reviewable, and enforceable** (ideally via policy-as-code + CI gates).

---

## ✅ What belongs here

This folder is for **static artifacts shipped by the web client**, including:

- 🧩 UI media: icons, illustrations, photos, audio snippets
- 🗺️ Map UI assets: style JSON, sprites, glyph ranges, textures
- 🧱 Embedded sample files: small GeoJSON examples, demo datasets (only if allowed)
- 🎨 Design resources: fonts (if bundled), background patterns, logos (if permitted)

> [!NOTE]
> If the asset is fetched at runtime from the server/API, it **should be licensed in the dataset/catalog layer**, not here (unless you also bundle a copy in `web/src/assets`).

---

## 🚫 What does not belong here

Keep this directory focused. These items typically belong elsewhere:

- 📦 **npm / JS dependencies** (licenses come from their packages; track with tooling that reads `package-lock.json` / `pnpm-lock.yaml`)
- 🧠 **Research PDFs / internal references** (do not bundle into the client)
- 🗃️ **Server-served datasets** (license lives in the dataset catalog/DCAT metadata, returned by the API)
- 🔐 **Restricted / sensitive data** (never ship in `web/src/assets`)

---

## 🗂️ Recommended layout

You can organize this directory like this (suggested, not mandatory):

```text
📁 web/src/assets/_meta/licenses/
├─ 📄 README.md                     ← you are here
├─ 📁 texts/                        ← full license texts when we must redistribute them
│  ├─ 📄 MIT.txt
│  ├─ 📄 Apache-2.0.txt
│  ├─ 📄 BSD-3-Clause.txt
│  ├─ 📄 CC-BY-4.0.txt
│  └─ 📄 ODbL-1.0.txt
├─ 📁 records/                      ← one record per shipped asset (or per asset pack)
│  ├─ 📄 <asset-id>.license.json
│  └─ 📄 <asset-pack-id>.license.json
└─ 📁 attributions/                 ← UI-ready attribution blocks/snippets
   ├─ 📄 <asset-id>.md
   └─ 📄 <provider-id>.md
```

---

## 🧾 License record schema

KFM uses metadata-first thinking: we record license and provenance in a **machine-readable** way (JSON), and optionally a **human-friendly** attribution snippet (Markdown).

### Minimum fields (required)

| Field | Type | Why |
|------|------|-----|
| `id` | string | Stable identifier for CI + UI attribution |
| `artifact` | string | Path to shipped asset (or a glob/prefix) |
| `upstream.name` | string | Creator/org name |
| `upstream.url` | string | Source/provenance URL |
| `license.spdx` **or** `license.name` | string | SPDX preferred; else human readable |
| `license.url` | string | Link to canonical license |
| `attribution` | string | Required UI attribution text (if applicable) |
| `redistribution` | `"required" \| "recommended" \| "not_required" \| "unknown"` | Whether we should bundle the license text |
| `last_verified` | `YYYY-MM-DD` | Keep license audits fresh |

### Full example

<details>
<summary>📦 Example: <code>records/example-icon-pack.license.json</code></summary>

```json
{
  "id": "example-icon-pack",
  "type": "media/icon",
  "artifact": "web/src/assets/icons/example/*.svg",
  "title": "Example Icon Pack",
  "upstream": {
    "name": "Example Author",
    "url": "https://example.com/icon-pack",
    "retrieved_at": "2026-02-05"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "url": "https://creativecommons.org/licenses/by/4.0/"
  },
  "attribution": "Icons © Example Author (CC BY 4.0)",
  "redistribution": "recommended",
  "changes": "Optimized SVG paths for web bundle size (no visual changes).",
  "last_verified": "2026-02-05",
  "notes": [
    "Attribution must appear in About → Credits and (if used on map UI) in the map attribution footer.",
    "If upstream changes license terms, update record + lock to a specific version/commit if possible."
  ]
}
```

</details>

### Attribution snippet (optional but encouraged)

If a license requires specific wording, keep it in `attributions/<id>.md` so the UI can render it consistently:

```md
**Example Icon Pack** — Icons © Example Author  
License: CC BY 4.0 • Source: https://example.com/icon-pack
```

---

## 🏷️ Attribution surfaces in the UI

Different asset types require attribution in different places. When adding a record, also declare where we surface attribution.

Recommended UI surfaces:

- 🧾 **About → Credits / Licenses** page (always safe)
- 🗺️ **Map attribution control** (required for many map/data sources)
- 📥 **Download / Export panel** (when exporting assets or derived outputs)
- 🧠 **Focus Mode / AI citations UI** (for facts/data sources; *not* for static icons, unless relevant)

> [!TIP]
> If an asset affects map rendering (styles, tiles, imagery, labels), assume it needs **map attribution** until proven otherwise.

---

## 🔍 Review checklist

Before merging an asset into the web bundle:

### 1) Provenance ✅
- [ ] Do we have a stable source URL (not a random image search result)?
- [ ] Can we re-download or reproduce the asset from upstream?
- [ ] If derived from a dataset or map, do we have the original dataset reference?

### 2) License clarity ✅
- [ ] Is the license explicitly stated?
- [ ] If unclear, treat as **all rights reserved** → do not ship.
- [ ] If it’s copyleft/share-alike, do we understand the obligations?

### 3) Distribution rules ✅
- [ ] Does the license require bundling the license text?
- [ ] Does it require attribution in a specific place?
- [ ] Does it restrict commercial use or derivatives?

### 4) Modification disclosure ✅
- [ ] If we modified it: did we record what changed?
- [ ] If we transformed it (crop, recolor, vectorize): does the license allow that?

---

## 🧱 Governance hooks

KFM’s broader system design emphasizes **policy-as-code** and **automated enforcement**. This folder is designed to support that model.

### Suggested CI rules (policy-as-code ready)

These are the kinds of checks we should enforce automatically:

- Every file under `web/src/assets/**` (except `_meta/**`) must match **exactly one** license record.
- Every license record must include:
  - `upstream.url`
  - `license.spdx|name`
  - `license.url`
  - `last_verified`
- Any record with `redistribution: "required"` must have a corresponding file in `texts/`.
- No record may be `unknown` at merge time (unless explicitly waived by maintainers).

> [!NOTE]
> KFM governance is intended to be enforced through CI + policy checks (OPA/Rego, Conftest-style gating). This folder is structured to make those checks straightforward.

---

## ⚠️ Common pitfalls

### “It’s on the internet so it’s free”
Nope. Many works are copyrighted by default unless a license explicitly grants reuse rights.

### “The data is public domain, so the map image is too”
Not necessarily. The **facts** may be free; the **representation** (cartography, styling, labeling, screenshots) can still be protected.

### “Screenshots are harmless”
Screenshots of proprietary platforms or restricted imagery can trigger licensing violations. Prefer:
- public domain sources
- open data portals
- permissive/open imagery providers
- datasets with clear reuse terms

---

## ❓ FAQ

### Do we need a record for our own original assets?
Yes — if it ships, it should be recorded. Use:
- `license.spdx: "Proprietary"` (if project-private)
- or the repository’s open-source license (if applicable)

### What about server/API datasets?
Those should have a license in their dataset metadata (catalog/DCAT), and the API should expose it. Only add a record here if the dataset (or part of it) is bundled into the client.

### What if an upstream license changes?
Update:
- the license record
- the attribution snippet (if needed)
- and ideally pin to a specific upstream version (tag/commit/hash)

---

## 🧩 TODOs (nice upgrades)

- [ ] Add a script to generate a **Credits/Licenses** UI page from `records/*.license.json`
- [ ] Add CI validation (policy-as-code) for asset ↔ record coverage
- [ ] Add a small “Attribution registry viewer” dev route for quick audits

---

**Last updated:** 2026-02-05 ✅  
**Maintainers:** KFM Web + Governance owners 🛡️
