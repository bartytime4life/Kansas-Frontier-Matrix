---
title: "🗂️ Kansas Frontier Matrix — Web Public Assets Architecture (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/ARCHITECTURE.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-architecture-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "web-public-architecture"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/public/ARCHITECTURE.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E31 Document"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "N/A"
json_schema_ref: "../../schemas/json/web-public-architecture.schema.json"
shape_schema_ref: "../../schemas/shacl/web-public-architecture-shape.ttl"
doc_uuid: "urn:kfm:doc:web-public-architecture-v10.4.0"
semantic_document_id: "kfm-doc-web-public-architecture"
event_source_id: "ledger:web/public/ARCHITECTURE.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major web/public architecture update"
---

<div align="center">

# 🗂️ **Kansas Frontier Matrix — Web Public Assets Architecture**  
`web/public/ARCHITECTURE.md`

**Purpose:**  
Define the **complete static assets architecture** for `web/public/**` in the Kansas Frontier Matrix (KFM) Web
Platform — including HTML shell, PWA manifest, robots configuration, icons, images, and their integration into the
build pipeline, governance, accessibility, and Focus Mode–aware UI.

</div>

---

## 📘 Overview

The `web/public/` directory contains **all static assets** that are served directly by the web server or CDN
without going through the React/TypeScript build step. These assets participate in:

- React SPA bootstrapping (`index.html`)  
- Progressive Web App behavior (`manifest.json`, icons, favicon)  
- Search engine and crawler behavior (`robots.txt`)  
- Shared imagery for the UI (logos, hero art, simple map thumbnails)  

Although these assets are not compiled TypeScript, they are part of the **Web Platform architecture** and must comply
with KFM’s FAIR+CARE, governance, and accessibility rules. This document describes how `web/public/**` fits into
the overall system and how contributions to public assets are governed.

---

## 🎯 Purpose

This specification:

- Describes the structure and responsibilities of `web/public/**`.  
- Explains how public assets integrate with:
  - The React SPA in `web/src/**`  
  - The build system (Vite)  
  - PWA behavior and metadata  
  - Governance and FAIR+CARE requirements  
- Provides clear guidance for adding or modifying public assets (images, icons, HTML shell).

---

## 📍 Scope

### In Scope

- All files under `web/public/**`, including:
  - `index.html`  
  - `manifest.json`  
  - `robots.txt`  
  - `favicon.ico`  
  - `icons/**`  
  - `images/**` (and other static asset subfolders)  
- How these assets are referenced from `web/src/**` and the build system.  
- Governance, licensing, and accessibility expectations for static resources.

### Out of Scope

- Frontend source code in `web/src/**` (covered by `web/src/ARCHITECTURE.md`).  
- Backend APIs and data pipelines.  
- CDN and edge cache configuration (documented at infra level).

---

## 🧱 Directory Structure

Static assets are arranged as follows:

~~~text
web/public/                      # Static assets served directly
├── index.html                   # SPA entry HTML shell for React
├── manifest.json                # Web App Manifest (PWA metadata)
├── robots.txt                   # Crawler and indexing directives
├── favicon.ico                  # Primary favicon
├── icons/                       # Platform/App icons (various sizes)
│   ├── icon-192.png             # PWA icon (192×192)
│   ├── icon-512.png             # PWA icon (512×512)
│   └── ...                      # Additional platform-specific icons
└── images/                      # Shared images used by the UI
    ├── logo-full.png            # KFM logo used on landing/splash
    ├── logo-mark.png            # Compact logo mark
    ├── hero-*.jpg               # Hero/cover imagery
    └── ...                      # Other non-sensitive static imagery
~~~

**Rule:** Any new static asset must be placed in an appropriate subdirectory under `web/public/` and referenced
using the correct public path (e.g., `/images/...`, `/icons/...`) according to the build system.

---

## 🧩 Role in the Web Platform

`web/public/` plays these architectural roles:

- **Bootstrap Shell**  
  - `index.html` is the base document loaded by browsers.  
  - It includes the root `<div>` where React mounts (`#root` or similar).  
  - Global `<meta>` tags (charset, viewport, theme-color, basic SEO) reside here.

- **PWA & Installability**  
  - `manifest.json` declares app name, icons, theme colors, and start URL.  
  - References icons in `icons/` and drives “install to home screen” behavior.  

- **Branding & Visual Identity**  
  - `favicon.ico`, icons, and `images/` maintain a consistent KFM brand across pages and devices.  

- **Crawling & Indexing**  
  - `robots.txt` controls indexing and crawling, aligning with governance decisions (what is meant to be discoverable).  

- **Performance & Caching**  
  - Public assets are typically cached by the CDN or browser with long-lived headers, so modifications can have broad
    impact. Filenames and hash-based naming should be used where appropriate.

---

## 🧱 Index HTML Architecture

Key architectural aspects of `index.html`:

- Provides a minimal HTML shell.  
- Contains no application logic; all behavior comes from the compiled React bundle.  
- Must include:

  - `<meta charset="utf-8">`  
  - `<meta name="viewport" content="width=device-width, initial-scale=1">`  
  - `<meta name="theme-color" content="#000000">` (kept in sync with theming)  
  - `<link rel="manifest" href="/manifest.json">`  
  - `<link rel="icon" type="image/x-icon" href="/favicon.ico">`  
  - A root mount container for React, e.g.:

    - `<div id="root"></div>`

- Must not embed secrets or privileged configuration; any configuration is obtained by the SPA at runtime (e.g., via
  environment variables baked into the bundle, not public HTML).

---

## 📱 Manifest & Icons Architecture

The **Web App Manifest** (`manifest.json`) specifies:

- `name` and `short_name` for KFM.  
- `start_url` (usually `/` or a specific route).  
- `display` mode (e.g., `standalone`).  
- `theme_color` and `background_color` (must be visually and A11y-aligned with React theming).  
- `icons` array referencing `icons/**`.

Architectural rules:

- All icons referenced in `manifest.json` must exist under `web/public/icons/`.  
- Icon sizes must satisfy platform recommendations (e.g., 192×192, 512×512).  
- Icons should have adequate contrast on various device backgrounds.  
- Where symbols appear in contexts related to Indigenous or sensitive data, governance guidance must be followed for
  iconography (no misappropriation of symbols).

---

## 🔐 Governance & FAIR+CARE Expectations

Although `web/public/` typically holds non-sensitive resources, the same **governance principles** apply:

- All images and icons must have clear licensing and provenance:
  - Prefer original KFM assets or open-licensed assets with attribution tracked in `manifest_ref` or in a per-asset log.  
- No sensitive or restricted imagery (e.g., photographs of protected sites) should be placed in `web/public/images/`
  without CARE review.  
- For imagery illustrating Indigenous history or sacred sites:
  - CARE considerations must be reviewed by the FAIR+CARE Council before inclusion.  
  - Images may be generalized, stylized, or replaced with neutral illustrations when appropriate.  

The architecture assumes that all content in `web/public/` is **public-safe** and consistent with the declared
`care_label` and `classification`.

---

## ♿ Accessibility Architecture

Accessibility for public assets focuses on:

- **Logo and imagery usage**  
  - React components using images in `web/public/images/` must supply appropriate `alt` text.  
  - Decorative images should explicitly use empty `alt` attributes (and be styled via CSS) to avoid noisy screen reader
    output.  

- **Icons**  
  - Icons used purely as decoration can rely on CSS background images and be hidden from assistive tech where needed.  
  - Icons carrying semantic meaning (e.g., warning, info) must be paired with text or ARIA labeling; the icon alone is
    not considered sufficient.

- **Color & Contrast**  
  - Icons and branding images must be chosen to work with the high-contrast modes offered by the SPA.  
  - Theme color in `manifest.json` should not cause text/icons to become illegible in browser UI or OS surfaces.

No standalone A11y behavior lives in `web/public/**`, but its contents must support the A11y story implemented in
`web/src/**`.

---

## 📈 Integration with Build & Runtime

From a build/runtime perspective:

- Vite serves `index.html` as the SPA entry and injects built JS/CSS bundles.  
- Paths like `/images/...` and `/icons/...` are resolved relative to the public root.  
- When new assets are added:
  - They should be referenced from React components via `/images/...` or `/icons/...` (not relative `../public/...`).
  - Rebuilds of the web app should ensure no broken links (GitHub Actions can run asset existence checks).

Public assets are versioned along with the rest of KFM via the same Git history and SBOM manifests.

---

## 🔒 Security & Privacy

The public assets architecture must:

- Avoid embedding any secrets, keys, or sensitive endpoints in `index.html`, `manifest.json`, or image metadata.  
- Ensure that any pre-configured URLs in the manifest are non-sensitive and safe to expose.  
- Treat all content in `web/public/` as world-readable; security controls are applied at other layers (e.g., backend).

---

## 📁 Directory Layout Summary

For quick reference, here is the `web/public/` layout with roles:

~~~text
web/public/
├── ARCHITECTURE.md               # This architecture document for public assets
├── index.html                    # Static SPA shell, React mount point
├── manifest.json                 # PWA metadata, icons, and display preferences
├── robots.txt                    # Crawler directives for search engines
├── favicon.ico                   # Default site favicon
├── icons/                        # App/platform icons referenced by manifest
│   ├── icon-192.png              # PWA icon (192×192)
│   ├── icon-512.png              # PWA icon (512×512)
│   └── ...                       # Additional icon sizes/variants
└── images/                       # Non-sensitive UI imagery
    ├── logo-full.png             # Primary KFM logo
    ├── logo-mark.png             # Compact icon-like logo
    ├── hero-*.jpg                # Hero images for landing sections
    └── ...                       # Other shared illustrations/graphics
~~~

---

## 🕰 Version History

| Version | Date       | Summary                                                                                   |
|--------:|------------|-------------------------------------------------------------------------------------------|
| v10.4.0 | 2025-11-15 | Initial `web/public` static assets architecture for KFM v10.4; aligned with KFM-MDP v10.4 |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Validated under MCP-DL v6.3 and KFM-MDP v10.4 · FAIR+CARE Certified · Public Document · Version-Pinned  

</div>