<!--
File: web/public/images/README.md
Scope: Public static image assets for the KFM web app.
-->

# `web/public/images` 🖼️

![Scope](https://img.shields.io/badge/scope-public%20static%20assets-brightgreen)
![Governance](https://img.shields.io/badge/governance-evidence--first%20%7C%20FAIR%2BCARE-blue)
![Security](https://img.shields.io/badge/security-no%20secrets%20here-critical)

> [!IMPORTANT]
> Anything placed in `web/public/**` is treated as **publicly readable** once deployed.  
> If an asset includes sensitive locations, private individuals, or restricted knowledge, **do not put it here**.

## What lives here

This folder holds image assets that the frontend can reference directly:

- UI icons (SVG)
- UI illustrations (empty states, hints)
- Non-sensitive static diagrams/legends
- Logos (KFM + partners, with permission)

## What must NOT live here

- Raw datasets, scans, or “source” imagery (use the governed pipeline + object storage instead).
- Any image that reveals **sensitive site locations** (exact coordinates, identifiable landmarks, etc.).
- Any image containing secrets (API keys, tokens), internal screenshots, or credentials.
- Anything without a clear reuse license / permission.

> [!WARNING]
> If it’s not safe to tweet, it’s not safe for `web/public/`.

## Directory layout

```text
web/public/images/
├─ icons/        # small UI icons (prefer SVG)
├─ logos/        # KFM + partner logos (license/permission required)
├─ ui/           # UI illustrations, empty-state graphics
├─ story/        # Story Node cover art & inline illustrations (public-safe only)
├─ maps/         # non-sensitive map legends, symbology, static explainers
├─ tmp/          # scratch during dev; do not ship to production
└─ README.md     # this file
```

> [!NOTE]
> Create subfolders as needed, but keep the intent obvious and keep assets public-safe.

## Naming conventions

Use **kebab-case**, keep names stable, and avoid ambiguous `final` / `new` / `v2`.

Recommended patterns:

- `icon-<verb>-<modifier>.svg`  
  (example: `icon-search.svg`, `icon-zoom-in.svg`)
- `logo-<org>.svg|png`  
  (example: `logo-kfm.svg`)
- `ui-<purpose>.<ext>`  
  (example: `ui-empty-state-search.webp`)
- `story-<story-id>-cover.<ext>`  
  (example: `story-snode-012-cover.webp`)

## Formats & performance guidelines

| Use case | Preferred format | Why |
|---|---|---|
| Icons | **SVG** | Crisp at any scale; small payload |
| Photos / raster art | **WebP** (or PNG/JPG if needed) | Better compression; fast loads |
| Diagrams with transparency | **PNG** or **SVG** | Cleaner edges; predictable rendering |

**Performance targets (guidelines):**
- Icons (SVG): aim for **< 10 KB**
- UI illustrations: aim for **< 200 KB**
- Photos / cover art: aim for **< 500 KB** (or provide multiple sizes)

### SVG safety (required)

SVG can embed scripts and external references. Before committing an SVG:

- ✅ Remove `<script>` tags and event handlers (e.g., `onload=...`)
- ✅ Avoid external references (`<image href="http...">`, remote fonts)
- ✅ Run an optimizer (example: `svgo`)
- ✅ Prefer basic shapes + paths; avoid unnecessary metadata

## Provenance & licensing metadata

For any asset that is not “trivial” (anything beyond tiny hand-made icons), add a sidecar:

- `my-asset.ext`
- `my-asset.meta.yml`

Example schema:

```yaml
# my-asset.meta.yml
title: "KFM Logo (Horizontal)"
kind: "logo"              # icon | logo | photo | illustration | map | other
source:
  origin: "created"       # created | commissioned | partner-provided | public-domain | purchased | unknown
  url: ""                 # if applicable
  retrieved_at: ""        # ISO-8601 date, if applicable
license:
  spdx: ""                # e.g., CC-BY-4.0, CC0-1.0, proprietary, partner-permission
  notes: ""               # constraints, attribution text, etc.
attribution:
  author: ""
  required_text: ""       # copy/paste attribution line (if required)
governance:
  sensitivity: "public"   # public | internal | restricted (restricted MUST NOT be in this folder)
  notes: ""               # redactions/generalizations performed, if any
derivations:
  - description: "optimized + stripped metadata"
    tool: "svgo"
    when: "YYYY-MM-DD"
```

> [!TIP]
> If you can’t state the license and source confidently, treat the asset as **not shippable**.

## How to add an image (PR checklist)

- [ ] Asset is appropriate for **public** distribution (no sensitive locations, no private data).
- [ ] License/permission is known and recorded (`*.meta.yml` for non-trivial assets).
- [ ] Image is optimized (SVG optimized; raster compressed; EXIF stripped).
- [ ] Filename follows conventions and is placed in the right subfolder.
- [ ] The UI uses meaningful `alt` text (or `aria-label` for purely decorative icons).

## Using images in the web app

General pattern (framework-dependent):

- File: `web/public/images/icons/icon-search.svg`
- URL: `/images/icons/icon-search.svg`

> [!NOTE]
> If your framework does not auto-serve `public/` at the web root, adjust accordingly. (Implementation detail)

## When you should NOT put an image here

Use a governed, access-controlled store + API when an image is:

- tied to a restricted dataset,
- derived from partner data with distribution constraints,
- or could expose sensitive locations/subjects.

---

### Owners

This directory is owned by the **Web/UI** layer, but governance rules apply to every commit.