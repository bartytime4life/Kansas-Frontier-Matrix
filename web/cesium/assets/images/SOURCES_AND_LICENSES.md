---
title: "Cesium UI Images — Sources and Licenses"
path: "web/cesium/assets/images/SOURCES_AND_LICENSES.md"
version: "v1.0.0"
last_updated: "2025-12-24"
status: "draft"
doc_kind: "Governance"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:images:sources-and-licenses:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-images-sources-and-licenses-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:images:sources-and-licenses:v1.0.0"
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

# Cesium UI Images — Sources and Licenses

## 📘 Overview

### Purpose

- Maintain a **complete attribution + license register** for every image asset under `web/cesium/assets/images/`.
- Prevent accidental inclusion of assets with unclear redistribution rights and ensure required notices are preserved in UI builds/releases.

### Scope

| In Scope | Out of Scope |
|---|---|
| Raster/vector image files in `web/cesium/assets/images/` (including UI icons, textures, overlays, screenshots used in UI) | Cesium models (`web/cesium/assets/models/`), CZML fixtures (`web/cesium/assets/fixtures/czml/`), JS/CSS deps, datasets and map layers sourced via APIs |
| Derivative/optimized variants stored in this directory (resized/compressed) | Runtime data fetched from external services |
| Attribution text required in app/about screens or release notes | Legal counsel guidance (handled via governance review) |

### Audience

- **Primary:** Frontend contributors maintaining Cesium UI assets.
- **Secondary:** Governance reviewers, release managers, and auditors verifying compliance.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: **asset**, **source**, **license**, **attribution**, **derivative**, **trademark**, **redistribution**, **terms-of-service**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This license register | `web/cesium/assets/images/SOURCES_AND_LICENSES.md` | Frontend | Must be updated with every asset change |
| Image assets directory | `web/cesium/assets/images/` | Frontend | Files referenced by Cesium UI |
| Root governance | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review triggers + process |
| Ethics + sovereignty policy | `docs/governance/ETHICS.md` + `docs/governance/SOVEREIGNTY.md` | Governance | Sensitive-content handling rules |

### Definition of done (for this document)

- [ ] Front-matter complete + valid and `path` matches file location
- [ ] Every file in `web/cesium/assets/images/` has an entry in the register table (or is explicitly excluded with a reason)
- [ ] Each entry includes: **source**, **license**, **attribution requirements**, and **last_verified_date**
- [ ] Any trademarks / restricted-to-use assets are clearly marked with handling notes
- [ ] Validation steps are listed and repeatable (even if tooling is “not confirmed in repo”)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/images/SOURCES_AND_LICENSES.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/Map UI (including Cesium) |
| Cesium assets | `web/cesium/assets/` | Local assets used by Cesium-based UI features |
| Image assets | `web/cesium/assets/images/` | Images requiring attribution/license tracking |
| Governance | `docs/governance/` | Root governance + ethics + sovereignty |

## 🧭 Context

### Background

UI image assets can carry **copyright**, **license obligations**, and **trademark restrictions**. This register ensures:
- the project can lawfully redistribute assets (including in packaged releases),
- required attribution is not lost during optimization/minification,
- governance review is triggered when an asset’s terms are unclear or restrictive.

### Assumptions

- Licenses and terms can change over time; each source should be periodically re-verified.
- Derived images inherit the original’s license obligations unless the upstream license explicitly states otherwise.
- If the license is unclear, treat the asset as **restricted** until reviewed.

### Constraints / invariants

- Do **not** add assets with unknown provenance or ambiguous reuse rights.
- Do **not** remove or obscure required attribution (including “©” notices) in derived variants.
- Preserve the canonical pipeline boundaries: UI assets are part of the UI layer and must not bypass governance expectations.

### Open questions

| Question | Owner | Status | Notes |
|---|---|---|---|
| Where should full license texts be stored when a license requires bundling? | Maintainer | open | Suggested: `web/cesium/assets/images/licenses/` (not confirmed in repo) |
| Should we add a CI check ensuring every file has a row in this register? | Maintainer | open | Suggested tooling is “not confirmed in repo” |

## 📦 Data & Metadata

### Asset register

**Rule:** If you add, rename, or delete a file in `web/cesium/assets/images/`, you must update this table in the same PR.

| Asset (relative path) | Purpose / Usage | Source | License | Attribution required | Modifications | Last verified (YYYY-MM-DD) | Notes / Restrictions |
|---|---|---|---|---|---|---:|---|
| `TBD` | `TBD` | `TBD (URL / internal provenance)` | `TBD (SPDX or named license)` | `TBD (exact text or “none”)` | `TBD (resized/compressed/edited)` | `TBD` | `TBD` |

### Minimum required fields per entry

- **Source:** canonical URL and/or upstream publisher (and, if applicable, internal procurement/permission reference).
- **License:** SPDX identifier when possible (e.g., `CC-BY-4.0`, `CC0-1.0`, `MIT`) or a named license with a pointer to the full text location.
- **Attribution required:** the exact text that must appear (if applicable), plus where it is displayed (e.g., “About”, “Credits”, “Docs”).
- **Modifications:** describe transforms (crop, recolor, resize, convert PNG→WebP, etc.).
- **Last verified date:** when the license/source page was last checked.

## 🧱 Architecture

### Where this fits

- These assets support the **UI layer** (`web/`) and must remain compatible with build and release packaging.
- If a UI surface requires attribution display, ensure the UI implements it via approved UX patterns (not specified here).

## 🧪 Validation & CI/CD

### Recommended validation steps

- [ ] Confirm no image in `web/cesium/assets/images/` lacks a row in the register table.
- [ ] Confirm every non-original asset includes an unambiguous license and a source.
- [ ] Confirm attribution requirements are satisfied (UI, docs, or release notes), where applicable.
- [ ] Confirm no asset includes restricted/sensitive content that could violate sovereignty or ethics policies.

### Optional automation (not confirmed in repo)

~~~text
- Script to diff directory listing vs table rows.
- Lint rule to require Last verified date and license field presence.
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when:
- introducing a new third-party image source,
- an asset has unclear or restrictive terms (including “non-commercial”, “no-derivatives”, or trademark-only usage),
- an asset depicts or reveals sensitive locations/communities in a way that creates ethical or sovereignty risk.

### CARE / sovereignty considerations

Even “just images” can leak sensitive information (e.g., photos of restricted sites or culturally sensitive places). If an image could:
- identify a sensitive location,
- depict sovereignty-controlled lands or culturally sensitive knowledge,
- or be interpreted as endorsing a political/cultural position,

then apply conservative handling and request governance review per `docs/governance/SOVEREIGNTY.md` and `docs/governance/ETHICS.md`.

### AI usage constraints

- Allowed AI use: summarization/formatting of this register.
- Prohibited AI use: generating new license claims or inferring license terms from the asset itself.

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-24 | Initial register scaffold for Cesium image assets | TBD | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

---

