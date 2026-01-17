# 🧩 Kansas Frontier Matrix (KFM) — Logo Assets

![Status](https://img.shields.io/badge/status-draft-orange)
![Formats](https://img.shields.io/badge/formats-SVG%20%7C%20PNG-blue)
![Accessibility](https://img.shields.io/badge/accessibility-colorblind--aware-brightgreen)
![Principle](https://img.shields.io/badge/principle-provenance--first-purple)

> 📌 **Path:** `web/assets/media/branding/logo/`  
> 🧠 **Goal:** Keep KFM’s logo assets **clean, consistent, accessible, and versionable**.

---

## 🧭 Why the logo matters (project-aligned)

KFM is built to make Kansas’s spatial truth **searchable, mappable, auditable, and modelable**, with a **provenance-first** approach where **citations and metadata are first-class** and nothing is treated like a “black box.”[^kfm_mission]  
That same spirit applies to branding assets: the logo is a *trust cue*—it should feel **clear, honest, and readable** across UI contexts (maps, dashboards, story panels, print exports).[^kfm_mission]

---

## 📦 What belongs in this folder

✅ **Do keep here**
- **Production-ready** logo exports for the web UI and docs:
  - `*.svg` (preferred)
  - `*.png` (fallback / social / legacy)
- Variants (primary / mono / mark-only / wordmark-only)
- Light/dark-safe exports if needed

🚫 **Do not keep here**
- Raw design working files (Figma exports, Illustrator `.ai`, etc.) → place in a `source/` folder *outside* runtime assets (or in a dedicated design repo).
- Random screenshots, mockups, or ad-hoc edits
- Third-party logos unless explicitly permitted + documented

---

## 🗂️ Expected layout

```text
📁 web/
└─ 📁 assets/
   └─ 📁 media/
      └─ 📁 branding/
         └─ 📁 logo/
            ├─ 📄 README.md
            ├─ 🖼️ kfm_logo_primary.svg
            ├─ 🖼️ kfm_logo_primary.png
            ├─ 🖼️ kfm_logo_mark.svg
            ├─ 🖼️ kfm_logo_wordmark.svg
            ├─ 🖼️ kfm_logo_mono_black.svg
            ├─ 🖼️ kfm_logo_mono_white.svg
            └─ 📄 kfm_logo.manifest.json   (optional, recommended)
```

---

## 🏷️ Naming conventions

Keep names **lower_case_with_underscores** and **no spaces**.[^kfm_naming]

**Recommended pattern**
- `kfm_logo_<variant>.<ext>`
- `kfm_logo_<variant>_<theme>.<ext>` (when needed)

**Examples**
- `kfm_logo_primary.svg`
- `kfm_logo_mark.svg`
- `kfm_logo_wordmark.svg`
- `kfm_logo_mono_black.svg`
- `kfm_logo_mono_white.svg`

---

## 🧩 Logo variants (define the “contract”)

| Variant | File | Use it when… | Notes |
|---|---|---|---|
| **Primary** | `kfm_logo_primary.svg` | Most UI headers, docs cover areas | Preferred default |
| **Mark-only** | `kfm_logo_mark.svg` | Favicons/app icons/map UI controls | Needs to be legible at small sizes |
| **Wordmark-only** | `kfm_logo_wordmark.svg` | Narrow horizontal headers | Avoid tiny text in-map overlays |
| **Mono (black/white)** | `kfm_logo_mono_black.svg` / `..._white.svg` | Single-color environments | Great for overlays + stamps |

> 🧠 Tip: Treat these variants like **API contracts** for the UI: stable names + predictable behavior reduce churn (and broken imports).[^kfm_contract_ui]

---

## 🎨 Color & accessibility rules (map-aware)

KFM’s cartographic conventions emphasize **colorblind-friendly, intuitive palettes** and explicitly avoiding problematic combinations like **red–green**.[^kfm_cartography]  
This matters for the logo because it will frequently sit on top of map tiles, legends, and data layers.

### ✅ Color guidance
- Prefer **high-contrast** brand colors that remain legible on:
  - light basemaps
  - dark basemaps
  - satellite imagery
- Avoid “meaningful contrast” that relies on red vs green differences (many users won’t see it).[^maps_colorblind]

### 🔎 Quick checks (recommended)
- Test the logo at **16px / 24px / 32px / 48px**
- Test on:
  - white background
  - near-black background
  - a busy satellite tile
  - a medium-gray UI panel

> Background variation can make identical colors appear different—verify the logo reads consistently across contexts.[^maps_background]

---

## 📐 Clear space & minimum sizes

Because the logo often appears in dense, information-rich map UIs:

- **Clear space:** keep at least **0.5× the mark width** on all sides (baseline rule; tighten only when necessary).
- **Minimum size (baseline defaults):**
  - Mark-only: **≥ 20px** (UI), **≥ 16px** (favicon variants)
  - Primary logo: **≥ 120px wide** (headers)
  - Wordmark: **≥ 140px wide** (headers)

> 🧩 If the mark becomes ambiguous at small sizes, ship a **simplified small-size mark** (separate file) rather than letting the primary mark degrade.

---

## 🧾 Provenance, licensing, and metadata (yes—even for logos)

KFM treats anything shown in the UI as something that should be **traceable** and governed.[^kfm_contract_ui]  
For data, this is enforced via **metadata contracts** including **source + license** and rules like “no mystery layers.”[^kfm_contract_metadata]

Logos should follow the same *spirit*:
- Every production logo asset should have an **explicit license** and **source provenance** (where it came from, who created it, when it changed).

### Recommended: a tiny manifest (optional but strong)
Create `kfm_logo.manifest.json`:

```json
{
  "brand": "Kansas Frontier Matrix",
  "asset_kind": "logo",
  "preferred": "kfm_logo_primary.svg",
  "variants": [
    { "name": "primary", "file": "kfm_logo_primary.svg" },
    { "name": "primary_png", "file": "kfm_logo_primary.png" },
    { "name": "mark", "file": "kfm_logo_mark.svg" },
    { "name": "wordmark", "file": "kfm_logo_wordmark.svg" },
    { "name": "mono_black", "file": "kfm_logo_mono_black.svg" },
    { "name": "mono_white", "file": "kfm_logo_mono_white.svg" }
  ]
}
```

### Recommended: per-asset sidecar metadata (if you want max rigor)
Example `kfm_logo_primary.meta.yml` (keep short):

```yaml
asset: "kfm_logo_primary.svg"
asset_kind: "logo"
variant: "primary"
created_by: "TBD"
last_updated: "TBD"
source_design: "TBD (e.g., Figma file/link or repo path)"
license: "TBD"
notes: "Exported + optimized for web"
```

> If your CI later validates docs and metadata for completeness, you can extend these checks to brand assets too (same governance mindset).[^md_ci_checks]

---

## 🛠️ Export & optimization workflow (recommended)

```mermaid
flowchart LR
  A[🎨 Source design] --> B[📤 Export SVG/PNG]
  B --> C[🧹 Optimize assets]
  C --> D[🧾 Update manifest + metadata]
  D --> E[🧪 Visual QA (light/dark/map)]
  E --> F[✅ Commit + PR]
```

### SVG export rules
- Must include a proper `viewBox`
- Avoid editor junk (hidden layers, gigantic canvases)
- Prefer **paths** (outlined text) for portability
- No embedded rasters inside SVG unless absolutely necessary

<details>
  <summary>🧹 Optimization ideas (tool-agnostic)</summary>

- SVG: run through an optimizer (e.g., SVGO)  
- PNG: use lossless compression where possible (do not destroy sharp edges)

</details>

---

## 👩‍💻 Usage examples (web)

### HTML
```html
<img
  src="/assets/media/branding/logo/kfm_logo_primary.svg"
  alt="Kansas Frontier Matrix"
/>
```

### React
```tsx
export function KfmLogo() {
  return (
    <img
      src="/assets/media/branding/logo/kfm_logo_primary.svg"
      alt="Kansas Frontier Matrix"
      width={160}
      height={40}
      loading="eager"
    />
  );
}
```

### Dark mode swap (simple pattern)
```css
.kfm-logo--dark { display: none; }
@media (prefers-color-scheme: dark) {
  .kfm-logo--light { display: none; }
  .kfm-logo--dark { display: inline; }
}
```

```html
<img class="kfm-logo--light" src="/assets/media/branding/logo/kfm_logo_primary.svg" alt="KFM" />
<img class="kfm-logo--dark"  src="/assets/media/branding/logo/kfm_logo_mono_white.svg" alt="KFM" />
```

---

## ✅ Definition of Done (PR checklist) 🧪

Inspired by the project’s governed-doc mindset: complete metadata, validated references, and reviewable changes.[^md_dod][^md_ci_checks]

- [ ] Exported **SVG** is clean (`viewBox`, no editor noise)
- [ ] Added **PNG fallback** where needed
- [ ] Added/updated **manifest** (`kfm_logo.manifest.json`) if used
- [ ] License/provenance info is present (manifest or sidecar)
- [ ] Tested in **light/dark** and on a **busy map** background
- [ ] Confirmed **colorblind-aware** (no red/green-only distinctions)[^kfm_cartography][^maps_colorblind]
- [ ] README updated if conventions changed

---

## 📚 Sources & rationale (project files)

[^kfm_mission]: KFM mission, provenance-first transparency, and evidence-backed UI philosophy are stated in the technical documentation. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm_contract_ui]: “Anything that shows up in the UI… must be traceable” is a guiding architectural rule. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm_contract_metadata]: KFM’s contract-first approach and the “no mystery layers” trust model are described here. [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm_cartography]: KFM cartographic conventions emphasize colorblind-friendly palettes and avoiding red-green combinations. [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm_naming]: KFM naming guidance includes lower_case_with_underscores and avoiding spaces. [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^maps_colorblind]: Map-design guidance notes that color-blind viewers often see red and green as the same, and recommends using alternatives like reds+blues or greens+blues. [oai_citation:5‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)
[^maps_background]: Map-design guidance warns that varying backgrounds can change perceived symbol colors; verify consistency across backgrounds. [oai_citation:6‡making-maps-a-visual-guide-to-map-design-for-gis.pdf](file-service://file-51FgWTn7uFXenxztXw29bP)
[^md_dod]: The docs guide recommends using Definition of Done checklists (front-matter complete, citations present, reviewed). [oai_citation:7‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
[^md_ci_checks]: The v13 markdown governance approach includes CI checks for front-matter and link/reference validity (preventing broken references). [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
