---
title: "FONT SUBSET — <family-slug> / <version>"
path: "web/assets/media/_sources/fonts/<family-slug>/<version>/SUBSET.md"
version: "<version>"
status: "active" # draft | active | deprecated
doc_kind: "Asset Spec"
asset_kind: "font"
subset_id: "kfm-ui-latin" # rename per your actual subset strategy
last_updated: "YYYY-MM-DD"

# Governance / traceability
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13" # align with repo major (if used)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

# Provenance
license: "SEE LICENSE.md"
upstream:
  name: "TBD (foundry / provider)"
  url: "TBD"
  version: "TBD (upstream release / tag)"
  retrieved_on: "YYYY-MM-DD"
  files:
    - "original/<family-slug>-<version>.ttf" # or .otf / variable font

build:
  tool: "fonttools (pyftsubset)"
  tool_version: "TBD (pin for determinism)"
  woff2_tool: "TBD (if separate)"
  build_host: "TBD (os/arch)"
  command_ref: "#-regeneration-command"

# Integrity
commit_sha: "<commit-hash>"
doc_uuid: "urn:kfm:asset:font:<family-slug>:<version>:subset"
doc_integrity_checksum: "sha256:<to-be-filled>"
---

# ✂️ Font Subset — `<family-slug>` (`<version>`)

![asset](https://img.shields.io/badge/asset-font-2b6cb0)
![format](https://img.shields.io/badge/format-WOFF2-111827)
![subset](https://img.shields.io/badge/subset-kfm--ui--latin-047857)
![status](https://img.shields.io/badge/status-active-16a34a)

> ✅ **Goal:** ship only the glyphs KFM actually needs (faster loads, fewer bytes) while keeping licensing + provenance crystal clear. 🧾

---

## 📘 Overview

### Purpose
This document is the **source-of-truth** for:
- which glyphs/Unicode ranges are included in the web subset(s)
- how to regenerate the subset deterministically
- what files are expected to exist in this directory for audits & CI ✅

### Scope
| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Subset character coverage + rationale | Choosing the project’s typography system |
| Reproducible build commands | App-level CSS architecture |
| Output file inventory + hashes | CDN/cache configuration (handled elsewhere) |
| License + upstream provenance | Non-font media assets |

### Audience
- **Primary:** Web/UI maintainers, build/tooling maintainers
- **Secondary:** Reviewers validating provenance + licensing, performance-minded contributors

### Definitions
- **Subset:** A reduced font file containing only a selected set of glyphs.
- **Glyph:** The actual shape(s) used to render a character.
- **WOFF2:** Modern compressed webfont format (preferred).
- **Unicode Range:** A range of code points (e.g., U+0020–007E) used by CSS `unicode-range`.

---

## 🗂️ Directory Layout

> 📌 Keep this folder self-contained and reviewable. One canonical home per asset/version. 🧱

```text
web/assets/media/_sources/fonts/<family-slug>/<version>/
├── 📄 SUBSET.md                 # this file ✅
├── 📄 LICENSE.md                # font license / OFL / etc.
├── 📄 SOURCE.md                 # where the upstream font came from (URL, tag, hash)
├── 📁 original/                 # upstream files as obtained (read-only)
│   └── <family-slug>-<version>.ttf
└── 📁 subset/                   # derived build outputs (what the web app actually serves)
    ├── <family-slug>-ui-latin-400.woff2
    ├── <family-slug>-ui-latin-600.woff2
    └── manifest.json            # sizes + hashes (recommended)
```

---

## 📦 Subset Inventory

Fill this table in with what you actually ship.

| Subset Tag | Weights / Styles | Unicode Coverage | Output(s) | Notes |
|---|---|---|---|---|
| `ui-latin` | `400, 600` (example) | Basic Latin + punctuation + UI symbols | `subset/*.woff2` | Default KFM UI subset |
| `ui-latin-ext` (optional) | TBD | Latin Extended (if needed) | `subset/*.woff2` | Add only if required |

---

## 🔤 Character Coverage

### Minimal “KFM UI” text set (starter)
Use this only as a baseline; the ideal approach is **extract actual characters from the UI + docs**.

- **Basic Latin:** `U+0020–007E`
- **Latin-1 Supplement:** `U+00A0–00FF` (optional; use if you need accent support)
- **Punctuation & UI symbols (common):**
  - “ ” ‘ ’ … – — •
  - ° ′ ″ (maps/coordinates)
  - → ← ↑ ↓ (navigation hints)
  - ✓ ✕ (status icons, if you render as glyphs instead of SVG)

### Recommended: maintain an explicit charset file ✅
Create/keep a text file (suggested name: `subset/charset.txt`) that contains **every character** you intend to support.
- One simple approach: paste representative UI text + Story Node punctuation here.
- Your build command can use `--text-file=subset/charset.txt` for deterministic subsetting.

<details>
  <summary><strong>🧠 Tip: How to find missing glyphs fast</strong></summary>

- In the browser: look for tofu (□) boxes.
- In dev tools: inspect which font-face is being used.
- Expand the charset minimally, regenerate, and re-test.
</details>

---

## 🧾 Provenance & Licensing

### Upstream source
- **Provider / foundry:** `TBD`
- **Upstream URL:** `TBD`
- **Upstream version/tag:** `TBD`
- **Retrieved on:** `YYYY-MM-DD`
- **Upstream file hash:** `sha256:TBD`

> ⚠️ Do not proceed if licensing is unclear. Put the full license text in `LICENSE.md` and record upstream in `SOURCE.md`.

---

## 🛠️ Regeneration Command

> ✅ Keep commands deterministic: pin tool versions, prefer `--text-file`, and record hashes in `manifest.json`.

### Example (static font → WOFF2 subset)
```bash
# from: web/assets/media/_sources/fonts/<family-slug>/<version>/

# 1) Ensure you have fonttools installed (pin version in your tooling)
# pip install "fonttools==X.Y.Z"

# 2) Subset
pyftsubset "original/<family-slug>-<version>.ttf" \
  --output-file="subset/<family-slug>-ui-latin-400.woff2" \
  --flavor=woff2 \
  --layout-features='*' \
  --name-IDs='*' \
  --name-legacy \
  --glyph-names \
  --symbol-cmap \
  --no-hinting \
  --text-file="subset/charset.txt"

# 3) Record hashes + sizes (recommended)
# sha256sum subset/*.woff2 > subset/SHA256SUMS.txt
# wc -c subset/*.woff2 > subset/SIZES.txt
```

### Example (variable font)
```bash
# Variable fonts may need axis handling; keep the exact source and command recorded.
pyftsubset "original/<family-slug>-<version>-variable.ttf" \
  --output-file="subset/<family-slug>-ui-latin-variable.woff2" \
  --flavor=woff2 \
  --layout-features='*' \
  --text-file="subset/charset.txt"
```

---

## 🧩 Web Integration Notes

### CSS `@font-face` (example)
```css
@font-face {
  font-family: "<Family Name>";
  src: url("/assets/media/fonts/<family-slug>/<version>/<family-slug>-ui-latin-400.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
  /* If using unicode-range splitting: */
  /* unicode-range: U+0020-007E, U+00A0-00FF; */
}
```

### Font stack suggestion (example)
```css
:root {
  --font-ui: "<Family Name>", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}
```

---

## 🧪 Validation Checklist

### Visual QA
- [ ] UI renders without tofu (□) anywhere in primary flows
- [ ] Map-related strings render correctly (° ′ ″ and coordinate formatting)
- [ ] Bold/semibold weights render (if shipped)

### Technical QA
- [ ] `woff2` loads successfully in target browsers
- [ ] Output file(s) are smaller than upstream font(s)
- [ ] Subset is deterministic (same inputs → same hashes)
- [ ] `subset/SHA256SUMS.txt` (or manifest) updated

<details>
  <summary><strong>🔬 Optional deeper validation</strong></summary>

- Run OpenType sanitizers (if available in your toolchain)
- Run a font QA suite (e.g., FontBakery) in CI for upstream changes
</details>

---

## 🕰️ Change Log

| Date | Change | Author | Notes |
|---|---|---|---|
| YYYY-MM-DD | Initial subset doc | TBD | Baseline `ui-latin` |

---

## ✅ Definition of Done (for this SUBSET.md)

- [ ] Front-matter complete & valid
- [ ] `LICENSE.md` present and matches upstream licensing
- [ ] `SOURCE.md` records upstream URL, version/tag, and hash
- [ ] `subset/charset.txt` present (or clear alternative documented)
- [ ] Build command is repeatable and recorded (this doc)
- [ ] Output file inventory table updated
- [ ] Hashes + sizes recorded for outputs
- [ ] UI smoke test confirms no missing glyphs
