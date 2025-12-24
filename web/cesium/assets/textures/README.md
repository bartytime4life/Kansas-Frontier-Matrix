---
title: "Cesium — Texture Assets"
path: "web/cesium/assets/textures/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:assets:textures:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-textures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:textures:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Cesium — Texture Assets

## 📘 Overview

### Purpose

- Define what belongs in `web/cesium/assets/textures/` and how to add/update textures safely.
- Establish lightweight, directory-local conventions (naming, formats, licensing notes) so UI assets remain reviewable and deterministic.

### Scope

| In Scope | Out of Scope |
|---|---|
| Committed texture files used by the Cesium client (e.g., billboards/sprites, repeating materials, UI effects, normal maps). | Runtime data imagery served via APIs; STAC-managed data products; anything requiring STAC/DCAT/PROV publication. |

### Audience

- Primary: UI engineers working on the Cesium client under `web/`
- Secondary: Reviewers validating performance, licensing, and governance

### Definitions (link to glossary)

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Texture**: an image used as GPU input for rendering (color, normal, mask, etc.).
  - **Sprite**: a texture used for 2D billboards/icons.
  - **POT (power-of-two)**: 64/128/256/512/1024… dimensions (often preferred for mipmaps/repeating patterns).
  - **sRGB vs linear**: color textures are usually sRGB; data textures (normals/masks) are usually linear.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Textures directory | `web/cesium/assets/textures/` | UI | This directory |
| UI root | `web/` | UI | Client app(s), including Cesium integration |
| Governance baseline | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Review rules for sensitive/licensed content |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path:` matches file location)
- [ ] Directory intent is clear (what belongs here vs. what does not)
- [ ] Conventions for naming/formats/licensing are stated
- [ ] Governance and CARE/sovereignty considerations are explicitly stated (when relevant)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/textures/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React + map clients, UI assets, viewer code |
| Cesium assets | `web/cesium/assets/` | Static assets for Cesium integration (not fully enumerated here) |
| Textures | `web/cesium/assets/textures/` | Texture image assets used by Cesium client |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 textures/
            ├── 📄 README.md                      # 📘 This document
            ├── 🖼️ ui-noise_256.png               # Example placeholder
            ├── 🖼️ terrain-normal_1024.png        # Example placeholder (data/linear)
            └── 📄 ui-noise_256.LICENSE.md         # Optional per-asset source/license notes (recommended)
~~~

## 🧭 Context

This directory is for **static texture assets** that are bundled and shipped with the Cesium UI. These textures should be:
- small enough for web delivery,
- named predictably for reuse,
- safe to publish (no restricted imagery; licenses recorded for any third-party sources).

### What belongs here

- Reusable UI textures (noise patterns, subtle overlays)
- Billboards / sprite sheets used in Cesium visualizations
- Material textures used by custom shaders/materials (if applicable)
- Normal maps / masks used for rendering (if applicable)

### What does NOT belong here

- Any **data product** imagery that is generated from sources and should be tracked in STAC/DCAT/PROV
- Any texture that materially encodes “facts” (e.g., annotated maps with claims) without a provenance pathway
- Sensitive imagery that could reveal restricted locations (requires governance review before inclusion)

### Conventions for adding/updating textures

**File formats**
- Prefer **PNG** for transparency (UI sprites, masks, normal maps).
- Prefer **JPG** only for photographic textures with no alpha channel.
- Avoid embedding unnecessary metadata (EXIF/XMP); strip metadata when possible.

**Dimensions**
- Prefer **POT** dimensions (e.g., 256/512/1024) for repeating patterns and mipmapped textures.
- Non-POT is acceptable for UI sprites/icons if needed (keep file size small).

**Naming**
- Use lowercase with `-` and `_` only.
- Include intent + size where helpful.
- Examples:
  - `ui-noise_256.png`
  - `pin-sprite_64.png`
  - `terrain-normal_1024.png`

**Licensing (recommended)**
- If a texture is third-party or derived from a third-party source, add a sibling note:
  - `<texture_name>.<ext>.LICENSE.md` (e.g., `ui-noise_256.png.LICENSE.md`)
- Include at minimum:
  - Source (URL or internal origin)
  - License name/identifier
  - Retrieval date
  - Modifications (if any)

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Texture file<br/>web/cesium/assets/textures/*] --> B[Web build / static asset pipeline<br/>(not confirmed in repo)]
  B --> C[Cesium client runtime]
  C --> D[Rendered sprites / materials / overlays]
~~~

## 🧠 Story Node & Focus Mode Integration

- Textures are typically “presentation assets,” but they can still affect interpretation.
- If a texture includes **labels, boundaries, or claims**, treat it as content:
  - ensure any claims are supported elsewhere (e.g., Story Nodes with provenance-linked sources),
  - avoid embedding unverified or sensitive assertions into imagery.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Confirm the new/updated file is appropriately sized (avoid oversized textures for web delivery).
- [ ] Confirm the filename follows naming conventions.
- [ ] Confirm no embedded sensitive content (restricted imagery, precise sensitive locations).
- [ ] Confirm third-party textures have license/source notes (recommended).
- [ ] Confirm links in this README resolve (if any are added later).

## 📦 Data & Metadata

### Per-asset metadata (recommended)

For third-party or derived textures, add `*.LICENSE.md` with:
- **Source:** where the asset came from
- **License:** terms for redistribution/modification
- **Date:** retrieval/creation date
- **Edits:** what was changed (resize, color correction, compression, etc.)

## 🌐 STAC, DCAT & PROV Alignment

- This directory is **UI assets only**.
- If an image/texture is actually a **dataset artifact** (generated output that should be discoverable or provenance-linked), store it under the appropriate `data/**` domain and publish via the normal STAC/DCAT/PROV pipeline.

## 🧱 Architecture

This directory sits in the **UI layer** of the canonical architecture. UI assets should remain decoupled from graph storage (i.e., no direct graph access from the UI; access should be via APIs).  

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is recommended when:
- adding third-party textures (license verification),
- adding textures that could reveal sensitive locations (e.g., high-resolution map imagery),
- adding textures containing culturally sensitive symbols or context-specific markings.

### CARE / sovereignty considerations

- If a texture depicts culturally sensitive knowledge or sovereignty-controlled places/symbols, follow the sovereignty policy and governance review rules before publication.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not use AI workflows to infer sensitive locations or generate new policy beyond governed standards.

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium texture asset directory | TBD | TBD |

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
