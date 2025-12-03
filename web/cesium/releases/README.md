---
title: "📦 KFM v11.2.3 — CesiumJS Web Release Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index of CesiumJS release integrations for the Kansas Frontier Matrix web stack, including version history, compatibility, and telemetry/governance links."
path: "web/cesium/releases/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web Visualization Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Cesium 1.120 → 1.136 web-integration-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:doc:web-cesium-releases-index-v11-2-3"
semantic_document_id: "kfm-web-cesium-releases-index-v11.2.3"
event_source_id: "ledger:kfm:web:cesium:releases:index:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-cesium-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-cesium-release-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"
status: "Active / Enforced"
doc_kind: "Release Index"
intent: "web-cesium-releases-index"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — CesiumJS Web Release Index**  
`web/cesium/releases/README.md`

**Purpose:**  
Serve as the **governed index** of CesiumJS versions integrated into the KFM web stack, with links to per-version release notes, tests, artifacts, and upstream references.

</div>

---

## 📘 1. Overview

This index tracks **all CesiumJS releases** that have been:

- Evaluated for use in KFM  
- Documented with **KFM-governed release notes**  
- Covered by **smoke tests**, **artifacts**, and **telemetry hooks**  

For the subsystem-level overview of Cesium integration, see:

- `web/cesium/README.md`

This file focuses on **per-version** status and directory layout.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
web/cesium/releases/
│
├── 📄 README.md                         # This file — CesiumJS web release index
│
└── 1.136/                               # CesiumJS v1.136 (current governed release)
    ├── 📄 README.md                     # KFM-governed v1.136 release notes
    │
    ├── 🧪 tests/                        # Smoke tests for rendering, picking, terrain, glyphs
    │   ├── 📄 README.md                 # Test suite overview
    │   └── 📄 rendering-smoke.md        # Scenario-by-scenario smoke tests
    │
    ├── 🗄️ artifacts/                    # Screenshots, metrics, optional logs (non-sensitive)
    │   ├── 📄 README.md                 # Artifact layout & usage
    │   ├── 📸 terrain-picking.png
    │   ├── 📸 billboard-scaling.png
    │   └── 🧾 metrics.json
    │
    └── 📚 references/                   # Upstream docs & KFM integration notes
        ├── 📄 README.md                 # Reference directory overview
        ├── 📄 upstream-release-notes.md # Curated upstream release summary
        ├── 📄 api-links.md              # Key API references used by KFM
        └── 📄 integration-notes.md      # Deeper KFM-specific integration notes
~~~

**Layout contract:**

- Each Cesium version integrated into KFM gets its **own subdirectory** under `web/cesium/releases/`.  
- Each version **must** have a `README.md` with:
  - Front matter aligned to **KFM-MDP v11.2.3**  
  - Links to tests, artifacts, and references  

Future versions (e.g., `1.137/`, `1.138/`) must follow the **same structure**.

---

## 🧩 3. Release Catalog

### 3.1 Current Governed Release

| Cesium Version | Status              | KFM Version | Notes                                                      | Entry Point                                                |
|----------------|--------------------|------------|------------------------------------------------------------|-----------------------------------------------------------|
| **1.136**      | 🟢 Stable / Governed | v11.2.3    | Async pick, terrain sampling improvements, glyph fixes, and performance updates validated in KFM. | `web/cesium/releases/1.136/README.md`                     |

**Highlights for v1.136 in KFM:**

- Adoption of `scene.pickAsync` as the **preferred picking API**.  
- Terrain sampling performance improvements aligned with KFM hydrology & archaeology tools.  
- Billboard/label rendering fixes improving glyph stacks and readability.  
- Telemetry + smoke tests defined for regression detection.

---

### 3.2 Deprecated / Historical Releases

> **Note:** Prior Cesium versions (e.g., `1.120–1.135`) may have been used historically but do not carry full KFM v11.2.3 documentation.  
> If/when these versions require archival documentation, they should be added under versioned directories (e.g., `web/cesium/releases/1.120/`) with at least:

- A minimal `README.md`  
- Status: `"Deprecated"` or `"Internal-Only"`  
- Upgrade guidance pointing to 1.136 or later

Until then, the **single source of truth** for active KFM web deployments is the **current governed release** row above.

---

## 🧪 4. Release Governance & CI Expectations

For each Cesium release directory (e.g., `1.136/`), KFM expects:

1. **Release Notes**  
   - `1.136/README.md`  
   - Includes:
     - High-impact changes  
     - KFM integration notes  
     - Telemetry and governance references  

2. **Tests**  
   - `1.136/tests/README.md` and `1.136/tests/rendering-smoke.md`  
   - Define:
     - Smoke scenarios  
     - Acceptance criteria  
     - Manual & CI-friendly steps  

3. **Artifacts**  
   - `1.136/artifacts/README.md`  
   - Optional, but recommended:
     - Screenshots  
     - Metrics JSON  
     - Summarized logs  

4. **References**  
   - `1.136/references/README.md`  
   - Curated:
     - Upstream release note summaries  
     - Key API links  
     - Integration notes

CI checks should:

- Validate **markdown structure** and **front matter** for all `README.md` and test files.  
- Ensure all release directories follow the **directory layout contract**.  
- Optionally verify that `metrics.json` (if present) is valid JSON and ***telemetry_ref*** is consistent.

---

## 📊 5. Telemetry & Performance Tracking

All Cesium releases integrated at KFM v11.2.3 share:

- Telemetry schema:  
  `../../schemas/telemetry/web-cesium-release-v1.json`  

- Default telemetry location:  
  `../../releases/v11.2.3/web-cesium-telemetry.json`  

Per-release telemetry expectations:

- Track:
  - Picking latency distributions  
  - Terrain sampling latency  
  - Basic FPS / frame-time metrics under representative scenes  

- Telemetry should be:
  - **Opt-in** and redacted  
  - Focused on performance & reliability, not user behavior  

Each release’s `README.md` may add additional telemetry details as needed.

---

## ⚖ 6. FAIR+CARE & Sovereignty Requirements

Cesium releases in KFM must comply with the same governance as other spatial tools:

- **Sensitive locations** must be:
  - Generalized or masked (e.g., H3 regions)  
  - Controlled by CARE visibility rules in layer registries and Cesium components  

- **Release notes, tests, and artifacts** must:
  - Avoid revealing coordinates or views that violate these constraints.  
  - Ensure screenshots and metrics are non-sensitive and properly redacted where necessary.

Governance path:

- Web Visualization Systems WG  
- FAIR+CARE Council  
- Sovereignty / heritage reviewers as appropriate for any specific content

---

## 🧭 7. Adding a New Cesium Release

When integrating a new Cesium version (e.g., `1.137`):

1. **Create directory**

   - `web/cesium/releases/1.137/`

2. **Add core docs**

   - `web/cesium/releases/1.137/README.md`  
   - `web/cesium/releases/1.137/tests/README.md`  
   - `web/cesium/releases/1.137/tests/rendering-smoke.md`  
   - `web/cesium/releases/1.137/artifacts/README.md` (optional but recommended)  
   - `web/cesium/releases/1.137/references/README.md`  
   - Any of:
     - `api-links.md`  
     - `integration-notes.md`  
     - `upstream-release-notes.md`

3. **Wire CI**

   - Ensure new release directory participates in documentation and lint checks.  
   - Optionally add scenarios to automated test harnesses.

4. **Update this index**

   - Add a new row in the **Release Catalog** section.  
   - Update status of previous releases if they become `Deprecated` or `Legacy`.

5. **Governance review**

   - Run smoke tests and record artifacts.  
   - Present results to Web Visualization Systems WG + FAIR+CARE Council.  
   - Only then mark the new version as **Stable / Governed**.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Web Visualization Systems WG · FAIR+CARE Council | Created CesiumJS web release index; documented directory layout, current governed release (1.136), CI expectations, telemetry wiring, and governance flow for future releases. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT (Cesium Release Index & Docs)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Cesium Web Integration Overview](../README.md) · [⬅ Back to Web Root](../..//README.md)

</div>
