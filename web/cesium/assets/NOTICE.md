---
title: "KFM Cesium Assets — NOTICE"
path: "web/cesium/assets/NOTICE.md"
version: "v1.0.0"
last_updated: "2025-12-24"
status: "draft"
doc_kind: "Notice"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:notice:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-notice-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:notice:v1.0.0"
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

# Cesium Assets — NOTICE

## 📘 Overview

### Purpose

This file records **third-party attribution notices** for **bundled/static runtime assets** distributed under:

- `web/cesium/assets/`

It is intended to support license compliance when shipping the KFM web UI that includes Cesium-based rendering.

> This is **not legal advice**. It is a practical attribution ledger for build/distribution hygiene.

### Scope

| In Scope | Out of Scope |
|---|---|
| Files physically present under `web/cesium/assets/` | NPM/PNPM transitive dependencies (track via package manager + SBOM tooling) |
| Static images, icons, fonts, shaders, sample models, etc. that are shipped with the web build | Remote services/content (e.g., hosted imagery/terrain/3D content) |
| Attribution requirements that must travel with redistributions of these bundled assets | Project-wide licensing (root `LICENSE*` files) |

### Maintenance rules

- When adding, replacing, or deleting any third-party asset under `web/cesium/assets/`, you **must**:
  - add/update an entry in **“Bundled third-party inventory”** below, and
  - keep any required copyright, license, and attribution text intact.
- If an upstream asset requires shipping a license text file alongside it, store that text adjacent to the asset **or** in a clearly named sibling file in this directory.

## 🧾 Third-Party Notices

### CesiumJS (library + distributed runtime assets)

If this directory contains assets originating from the CesiumJS distribution (e.g., packaged widget imagery, default UI resources, etc.), attribution is:

- Upstream project: **CesiumJS**
- Copyright: **Copyright 2011–2022 CesiumJS Contributors**
- License: **Apache License 2.0**
- Upstream repository: `https://github.com/CesiumGS/cesium`
- License text (upstream): `https://raw.githubusercontent.com/CesiumGS/cesium/main/LICENSE.md`

Notes:

- CesiumJS distributions may include third-party components whose notices are included in the upstream CesiumJS license materials. Where applicable, consult upstream `LICENSE.md` and related third-party listings and ensure required attribution notices remain included in KFM redistributions.

### Remote services and hosted content (not bundled)

KFM deployments may be configured to use remote services/content when rendering a globe (for example, terrain/imagery/geocoding). These are **not shipped from this directory**, but may still carry separate terms depending on configuration.

- If the deployment uses **Cesium ion** services or content, those services/content may have separate terms and licensing requirements.
- If the deployment uses other imagery/terrain providers, ensure their attribution and terms are satisfied per provider requirements.

## 📦 Bundled third-party inventory

Add entries here for any third-party assets that are physically shipped under `web/cesium/assets/`.

| Asset path (relative) | Upstream / Author | License | Copyright / Attribution | Source / URL | Notes |
|---|---|---|---|---|---|
| *(TBD — populate based on actual contents)* |  |  |  |  |  |

## 🧪 Validation & CI/CD

### Recommended checks (may be enforced by CI)

- [ ] This file exists at `web/cesium/assets/NOTICE.md`
- [ ] Any newly added third-party asset has:
  - [ ] a corresponding entry in “Bundled third-party inventory”
  - [ ] license/attribution text included as required
- [ ] No secrets/PII embedded in distributed assets or in this notice
- [ ] If a license/SBOM scanning gate exists for `web/`, it passes (not confirmed in repo)

## ⚖ FAIR+CARE & Governance

- This notice is **public** and should not include sensitive locations, PII, or restricted cultural information.
- If an asset relates to culturally sensitive content, apply the repo sovereignty and ethics requirements before publication.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial NOTICE scaffold for `web/cesium/assets/` | TBD |

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
