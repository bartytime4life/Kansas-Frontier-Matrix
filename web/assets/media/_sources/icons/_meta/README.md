---
title: "README — Icons Meta (Source Governance)"
path: "web/assets/media/_sources/icons/_meta/README.md"
version: "v0.1.0"
last_updated: "2026-01-18"
status: "draft"
doc_kind: "README"
system: "Kansas Frontier Matrix (KFM)"
area: "Web UI • Media • Icons"
license: "MIT"
markdown_protocol_version: "v13-draft"
classification: "open"
care_label: "Public"
doc_uuid: "urn:kfm:doc:web:assets:icons:meta:readme:v0.1.0"
commit_sha: "<set-on-merge>"
---

<div align="center">

# 🧩 Icons Meta — Sources, Licenses & Build Contracts

<!-- Optional badges. Remove if your CI forbids external images. -->
![status](https://img.shields.io/badge/status-draft-orange)
![format](https://img.shields.io/badge/assets-SVG-informational)
![governance](https://img.shields.io/badge/policy-contract--first-blue)
![provenance](https://img.shields.io/badge/policy-provenance--first-blueviolet)

</div>

> 🎯 **Goal**: keep every icon in KFM *traceable*, *licensed*, and *reproducible* — the same way we treat datasets and story evidence.[^kfm-contract]

---

## 🎯 Overview

This folder (`web/assets/media/_sources/icons/_meta/`) is the **governance layer** for UI icons:

- ✅ **Provenance**: where each icon came from (source, author, URL, version, retrieval date)
- ✅ **License**: what we’re allowed to do with it (license ID, attribution text, restrictions)
- ✅ **Build contract**: how raw assets become shippable assets (optimization + packaging)
- ✅ **Auditability**: enough metadata for automated validation and “credit lists”

KFM’s core rule is **contract-first + provenance-first**: if something appears in the UI, it must be traceable to cataloged sources and provable processing — and “mystery assets” are not acceptable.[^kfm-contract]

---

## 🗂️ Directory Layout

This README follows the KFM docs convention of including **Overview** and **Directory Layout** and keeping **YAML front-matter** up top.[^kfm-md-protocol]

Typical layout (exact file names may evolve, but the intent stays):

```text
📁 web/assets/media/_sources/icons/
├─ 📁 svg/                      # raw, editable SVGs (source-of-truth)
├─ 📁 png/                      # optional fallbacks (avoid if possible)
└─ 📁 _meta/                    # ✅ governance + contracts (this folder)
   ├─ 📄 README.md
   ├─ 📄 icons.manifest.json     # per-icon records (source/license/attribution/usage)
   ├─ 📄 iconset.contract.json   # iconset-level rules (schema/tool versions, outputs)
   ├─ 📄 THIRD_PARTY_NOTICES.md  # aggregated attributions for UI builds/releases
   └─ 📁 schemas/                # optional JSON Schemas (if not stored elsewhere)
```

### 🧠 What counts as “source-of-truth”?

- `_sources/icons/**` is the **authoritative input** (human-editable, reviewed).
- Anything generated from these files (sprites, optimized SVGs, icon fonts, hashes) should live in a **build output** location and be treated as **derived** artifacts.

> If you’re unsure where something belongs: if it’s **edited by hand**, it’s likely a source. If it’s **generated**, it’s likely an output. 🙂

---

## 🔒 Provenance & License Policy

### ✅ Non-negotiables

1. **No icon ships without a source + license record.**  
2. **No icon ships with “unknown license.”**  
3. **No icon ships if we can’t confidently generate correct attribution.**  
4. **No icon “implies” something the data doesn’t support** (e.g., an icon that labels something as “verified” without evidence).

KFM explicitly treats careful license handling as a trust & collaboration enabler.[^kfm-licensing]

### 🧾 Third-party icon packs

If we import a whole pack (even if we only use a subset), track:

- pack name + version (or commit/tag)
- official URL + download URL
- pack license (and per-icon differences, if any)
- attribution requirements
- any modifications we made

---

## 🧾 Icon Metadata Contract

KFM uses “data contracts” (metadata JSON) to enforce provenance and usage rules, validated by automated checks.[^kfm-contract] The same approach applies here: treat icons as **UI assets with contracts**.

### 🧱 Required fields (per icon)

| Field | Type | Why it exists |
|---|---:|---|
| `icon_id` | string | Stable identifier used by code (`kebab-case`) |
| `source.name` | string | Human-readable source (project/site) |
| `source.url` | string | Where we got it (or canonical upstream) |
| `source.license` | string | SPDX-like license ID (or explicit custom license label) |
| `source.attribution` | string | Text we must display in credits/NOTICE |
| `source.retrieved` | date | When it was fetched (important for audits) |
| `files.svg` | string | Relative path to raw SVG under `_sources/icons/` |
| `build.outputs[]` | array | Which generated assets depend on it (sprite, bundle, etc.) |
| `changes[]` | array | Notes on modifications (optimize, simplify paths, recolor) |
| `checksum.sha256` | string | Integrity tracking (optional but recommended) |

### 📄 Example: `icons.manifest.json`

```json
{
  "schema_version": "1.0",
  "icons": [
    {
      "icon_id": "map-marker-town",
      "files": {
        "svg": "svg/map/map-marker-town.svg"
      },
      "source": {
        "name": "Upstream Icon Pack Name",
        "url": "https://example.com/icons",
        "license": "CC-BY-4.0",
        "license_url": "https://example.com/license",
        "author": "Upstream Author or Org",
        "retrieved": "2026-01-18",
        "attribution": "© Upstream Author — used under CC-BY-4.0"
      },
      "usage": {
        "contexts": ["map", "legend", "focus-mode"],
        "decorative_default": true
      },
      "changes": [
        "Normalized viewBox to 0 0 24 24",
        "SVGO optimized (IDs/namespaces stripped)"
      ],
      "build": {
        "outputs": [
          "web/assets/media/icons/icons.sprite.svg",
          "web/assets/media/icons/icons.index.json"
        ]
      },
      "checksum": {
        "sha256": "sha256:<fill-me>"
      }
    }
  ]
}
```

### 🧪 Validation & CI expectations

KFM’s CI philosophy: **schemas + links + front-matter** are validated, and failures block merges.[^kfm-ci-gates] For icons, we want the same guardrails:

- `icons.manifest.json` validates against a JSON Schema (if/when defined)
- each `files.svg` path must exist
- licenses must match allowed list (or include explicit custom license text)
- `THIRD_PARTY_NOTICES.md` must be up to date (generated or reviewed)

---

## 🎨 SVG Technical Standard

SVG is the preferred icon format because it scales cleanly and is typically smaller than raster alternatives for simple artwork.[^svg-resolution]

### ✅ SVG must-haves

- `viewBox` defined and correct
- shapes fit inside the viewBox (no off-canvas stray points)
- no editor-only namespaces/metadata unless required (they’re often safe to remove)[^svg-namespaces]
- prefer `fill="currentColor"` for theming (unless multi-color icon is intentional)
- keep strokes/paths simple; avoid filters unless you **really** need them

### ♿ Accessibility

SVG can be made highly accessible with `<title>` and `<desc>`; these describe the content when it can’t be seen.[^svg-title-desc]

- If the icon is **informative**, prefer inline SVG with a meaningful title/desc (or `aria-label`).
- If the icon is **purely decorative**, mark it as decorative (`aria-hidden="true"`) and omit verbose labels.

> ⚠️ Note: if SVGs are used purely as CSS backgrounds, the title/desc may be stripped in optimization to reduce size.[^svg-title-desc]

### 🧩 Re-use via sprite symbols

For sprite-based workflows, define icons once and re-use with `<use …>`:

```html
<svg class="icon-map-marker-town" aria-hidden="true">
  <use xlink:href="#icon-map-marker-town"></use>
</svg>
```

This pattern is commonly used for re-using SVG symbols efficiently.[^svg-use]

### 🛠️ Optimization & repeatability

Two practical guidelines we follow:

- **Automate the asset pipeline** to reduce human error and keep outputs predictable.[^svg-automation]
- Prefer **one delivery mechanism** for static icons (sprite vs data URI vs inline) to avoid maintenance drift.[^svg-automation]

---

## 🔠 Naming & Organization Rules

### 📛 File names

- ✅ `kebab-case.svg`
- ✅ semantic and stable: `map-marker-town.svg`, not `pin2.svg`
- ❌ no spaces, no camelCase, no “final-final-v3.svg”

### 🧩 IDs

- `icon_id` should match filename (minus `.svg`) unless there’s a strong reason not to.
- Once published, treat `icon_id` as **API surface area** (backwards compatibility matters).

Suggested pattern:

- `map-…` for map markers, layer glyphs
- `ui-…` for buttons, panels, menus
- `data-…` for dataset/file type glyphs
- `alert-…` for warnings/errors/status

---

## ⚙️ Build Workflow (Recommended)

Exact scripts depend on the UI toolchain, but the **contract-first** approach is consistent:

1. **Add/modify SVG** in `_sources/icons/svg/…`
2. **Update** `icons.manifest.json`
3. **Run icon build** (optimize + generate sprite/index)
4. **Review** diffs visually (icons, sprite, NOTICE)
5. **Commit** source + metadata together

If you add tooling, aim for a deterministic pipeline: same inputs → same outputs, logged and reproducible.[^kfm-deterministic]

---

## ✅ Definition of Done

When adding or updating an icon, check:

- [ ] SVG meets technical standard (viewBox, clean paths, no junk)
- [ ] `icon_id` and filename follow naming rules
- [ ] Source + license + attribution captured in `icons.manifest.json`
- [ ] Any modifications documented in `changes[]`
- [ ] Generated outputs updated (sprite/index/whatever the build produces)
- [ ] `THIRD_PARTY_NOTICES.md` updated (or regenerated)
- [ ] No broken references (paths, IDs, build outputs)

---

## 🧠 Focus Mode Notes

Icons used in Focus Mode should not introduce “new claims.” Focus Mode is built around the principle: **no new narrative without sources, no data without provenance**.[^kfm-focus-mode]

---

## 📚 References (Project Files)

[^kfm-contract]: Contract-first & provenance-first rule (metadata JSON “data contract”, enforced by validators/CI). [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-licensing]: KFM notes that careful license handling avoids legal pitfalls and fosters collaboration. [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
[^kfm-md-protocol]: KFM Markdown Protocol: docs use YAML front-matter + required sections (e.g., Overview, Directory Layout); missing sections fail builds. [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^kfm-ci-gates]: CI gates include link/reference validation and JSON Schema validation for structured outputs. [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^kfm-deterministic]: Deterministic pipeline principle: idempotent, config-driven, logged, reproducible outputs. [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^kfm-focus-mode]: Focus Mode principle: “no new narrative without sources, no data without provenance.” [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
[^svg-namespaces]: SVG generator namespaces are often unnecessary and can be stripped during optimization. [oai_citation:6‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
[^svg-title-desc]: `<title>` and `<desc>` improve accessibility; may be removed for background SVGs to reduce file size. [oai_citation:7‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
[^svg-use]: Example of re-using SVG symbols via `<use xlink:href="…">` and sizing with CSS. [oai_citation:8‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
[^svg-automation]: Implementation tips: automate asset creation; stick to a single delivery mechanism for maintainability/performance. [oai_citation:9‡responsive-web-design-with-html5-and-css3.pdf](file-service://file-4pQLNMB3Rk5n5vUPTqxpNa)
[^svg-resolution]: SVGs can be smaller than bitmap formats for icon-like artwork while staying resolution independent. [oai_citation:10‡O-R programming Books.pdf](file-service://file-M6zCNBGmJbot7A2aaUUy9M)
