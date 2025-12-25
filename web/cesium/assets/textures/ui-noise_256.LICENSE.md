---
title: "KFM UI Texture License Record — ui-noise_256"
path: "web/cesium/assets/textures/ui-noise_256.LICENSE.md"
version: "v0.1.0-draft"
last_updated: "2025-12-24"
status: "draft"
doc_kind: "License"
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
care_label: "Low-Risk / Public UI Asset"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:assets:textures:ui-noise_256:license:v0.1.0-draft"
semantic_document_id: "kfm-web-cesium-texture-ui-noise_256-license-v0.1.0-draft"
event_source_id: "ledger:kfm:web:cesium:assets:textures:ui-noise_256:license:v0.1.0-draft"
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

# KFM UI Texture License Record — ui-noise_256

## 📘 Overview

### Purpose

Provide **license + attribution** metadata for the `ui-noise_256` texture used by the KFM Cesium-based UI, ensuring redistribution and downstream packaging remain compliant.

### Scope

| In Scope | Out of Scope |
|---|---|
| License + attribution for the `ui-noise_256` texture and any format variants with the same basename | Licensing for unrelated Cesium assets, datasets, or UI code |

### Audience

- Primary: Web/UI maintainers, release managers
- Secondary: Governance/compliance reviewers

### Definitions

- Glossary link: `docs/glossary.md` (not confirmed in repo)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Texture asset | `web/cesium/assets/textures/ui-noise_256.*` | UI | `*` = actual extension(s); keep this record aligned to what exists in-repo |
| License record | `web/cesium/assets/textures/ui-noise_256.LICENSE.md` | UI | This document |
| Upstream provenance evidence | TBD | TBD | Not confirmed in repo |

### Asset license and attribution

> **Status:** Not confirmed in repo  
> This record is intentionally created as a **draft** until upstream origin and licensing are verified.

| Field | Value |
|---|---|
| Asset covered | `ui-noise_256.*` |
| Upstream source | **TBD** (not confirmed in repo) |
| Upstream author / owner | **TBD** (not confirmed in repo) |
| Upstream license | **TBD** (not confirmed in repo) |
| SPDX identifier | **TBD** |
| Modifications in KFM | **TBD** (e.g., resize, recompress, rename) |
| Attribution requirements | **TBD** (e.g., credit line, NOTICE retention) |
| Redistribution notes | Do not assume redistributable until “Upstream license” is filled and reviewed |

### Definition of done

- [ ] Identify the upstream source (repo/page/file) for `ui-noise_256`
- [ ] Record upstream license and SPDX identifier (or “No SPDX” + citation)
- [ ] Record attribution text required by upstream terms
- [ ] Record any modifications done in KFM (if any)
- [ ] Set `status: active` once verified
- [ ] Fill `doc_integrity_checksum` (CI-calculated)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/textures/ui-noise_256.LICENSE.md` (must match front-matter)

### Local layout

~~~text
🌐 web/
└── 🧭 cesium/
    └── 🎛️ assets/
        └── 🧵 textures/
            ├── 🖼️ ui-noise_256.<ext>
            └── 📄 ui-noise_256.LICENSE.md
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/MapLibre/Cesium UI surface |
| Cesium UI assets | `web/cesium/assets/` | Static assets used by Cesium UI |
| Textures | `web/cesium/assets/textures/` | WebGL/UI textures |
| Governance | `docs/governance/` | Governance/Ethics/Sovereignty docs (paths referenced by templates) |

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| `ui-noise_256.*` | image texture | `web/cesium/assets/textures/` | Confirm upstream origin + license |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| License record | Markdown | `web/cesium/assets/textures/ui-noise_256.LICENSE.md` | KFM Universal Governed Doc |

### Sensitivity and redaction

- None expected (public UI texture). No PII.

### Quality signals

- License fields completed (source, license, attribution, changes)
- SPDX identifier provided where possible
- Any required NOTICE/credit text retained in-repo

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Not applicable (UI static asset)

### DCAT

- Not applicable unless this texture is distributed as part of a cataloged dataset distribution (not confirmed in repo)

### PROV-O

- Not applicable (not a data transform artifact)

### Versioning

- Use this file’s `version` + `last_updated`.
- If upstream asset changes materially (new source/derivative), bump version and update attribution.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| UI | Rendering and user interaction | Static assets loaded by UI build/runtime |
| Governance | Licensing hygiene | Review + documentation references |

### Interfaces and contracts

- UI must not directly access graph; this file is a static asset compliance record (no API impact).

## 🧠 Story Node & Focus Mode Integration

- Not applicable (UI texture only)

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (lint + required sections)
- [ ] Secret/PII scan (should be clean)
- [ ] Human license verification step (required before `status: active`)

### Reproduction

~~~bash
# Repo-specific commands not confirmed in repo.
# Suggested checks (adapt to your CI tooling):
# 1) markdown lint
# 2) link / footer validation (if enforced)
# 3) repo-wide license scan (if present)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

- Any third-party asset or derivative must have:
  - documented upstream source,
  - license identifier or full license terms,
  - required attribution/NOTICE text.

### CARE / sovereignty considerations

- None expected (non-cultural, non-location-bearing UI noise texture)

### AI usage constraints

- Do not use AI to infer licensing; licensing must be verified from authoritative upstream sources.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0-draft | 2025-12-24 | Initial license record scaffold for `ui-noise_256` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

