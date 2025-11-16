---
title: "🗑️ Kansas Frontier Matrix — Deprecated Features & Removal Map (v9.7 → v10) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/upgrade/deprecated-features.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Release / Postmortem · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/upgrade-deprecated-features-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Upgrade Report"
intent: "deprecated-features-v10"
care_label: "C2-A2-R2-E1"
fair_category: "F1-A1-I1-R1"
sensitivity_level: "None"
machine_extractable: true
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
semantic_document_id: "kfm-doc-upgrade-deprecated"
doc_uuid: "urn:kfm:doc:deprecated-features-v10.4.2"
---

<div align="center">

# 🗑️ **Kansas Frontier Matrix — Deprecated Features & Removal Map (v9.7 → v10)**  
`docs/guides/upgrade/deprecated-features.md`

**Purpose**  
Document all **retired, removed, replaced, or superseded features** in the migration from **KFM v9.7.x → v10**, including:  
- API endpoints  
- pipelines  
- STAC/DCAT assets  
- legacy UI modules  
- old Focus Mode architecture  
- deprecated governance & FAIR+CARE v1 features  
- obsolete directory structures  

Ensures clean v10 deployments, removes dead weight, and enforces **MCP-DL v6.3** + **FAIR+CARE v2** governance.

</div>

---

# 🗂️ Repository Context (Upgrade Directory)

~~~text
docs/guides/upgrade/
├── README.md
├── v10-readiness.md
├── v10-inventory.md
├── migration-checklist.md
├── repository-refactor-map.md
├── upgrade-validation-suite.md
├── deprecated-features.md        # ← THIS FILE
└── breaking-changes.md
~~~

---

# ❌ What "Deprecated" Means in KFM v10

A feature is **deprecated** when:
- It violates **FAIR+CARE v2**  
- It conflicts with **Lineage v2**, **STAC/DCAT v3**, or new ETL architecture  
- It duplicates v10 functionality  
- It breaks governance automation  
- It prevents Predictive ETL or Streaming ingestion  
- It is replaced by a new subsystem  

Deprecated items are:

1. **Removed immediately**  
2. **Blocked in CI**  
3. **Disallowed in new pipelines**  
4. **Never published to STAC/DCAT**  
5. **Marked as incompatible with Focus Mode v2.5**

---

# 🗃️ v9.7 → v10 Deprecation Map (Lined Style)

~~~text
# ─────────────────────────────────────────────────────────────────────────────
#  v9.7 → v10 Deprecated Features Map
# ─────────────────────────────────────────────────────────────────────────────

v9.7/legacy/                               →   REMOVED (non-compliant)
v9.7/src/ai/focus_mode_v1/                 →   REPLACED by ai/focus_transformer_v2/
v9.7/src/etl/release/                      →   REPLACED by pipelines/reliable_auto_release/
v9.7/src/rs/hillshade.py                   →   REPLACED by remote_sensing/svf/ + lrm/
v9.7/src/rs/visualization/                 →   MERGED into docs/guides/visualization/
v9.7/src/etl/stac_lite/                    →   REMOVED (v10 STAC/DCAT unified)
v9.7/docs/pipelines/overview.md            →   SPLIT into multiple v10 pipeline guides
v9.7/docs/rs/methods.md                    →   MERGED into lidar-relief-visualization.md
v9.7/docs/governance/CARE_v1.md            →   REPLACED by faircare.md (CARE v2)
v9.7/data/stac/lite/                       →   REMOVED (v10 auto-publish STAC)
v9.7/data/work/temp/                       →   RELOCATED to data/work/tmp/
v9.7/web/src/focus/                        →   REPLACED by components/FocusMode/
v9.7/web/src/map/                          →   REPLACED by components/MapView/
v9.7/web/src/timeline/                     →   REPLACED by components/TimelineView/
v9.7/tests/legacy/                         →   REMOVED (incompatible with v10)
v9.7/.github/workflows/deprecated/*.yml    →   REMOVED (v10 CI requires 11 validators)
~~~

---

# 🛠️ Deprecated Pipeline Components

### ❌ **Focus Mode v1**
- Prompt-only model  
- No SHAP/LIME explainability  
- No sovereignty/CARE controls  
- No subgraph reasoning  

**Replacement:** `src/ai/focus_transformer_v2/`

---

### ❌ **STAC Lite Publisher**
- Removed due to:
  - Lack of DCAT parity  
  - Missing provenance  
  - Invalid checksums  
  - No STAC extensions  

**Replacement:**  
`src/pipelines/publishing/stac/` (v10-compliant)

---

### ❌ **ETL Release v9**
- Shell-based release scripts  
- No idempotency  
- No SemVer automation  

**Replacement:**  
`pipelines/reliable_auto_release/`

---

### ❌ **Hillshade-Only Terrain Viz**
- Directionally biased  
- Not FAIR+CARE reviewed  
- Deprecated in favor of SVF + LRM  

**Replacement:**  
`remote_sensing/svf/`  
`remote_sensing/lrm/`

---

# 🧭 Deprecated API Endpoints

| v9.7 Endpoint | Status | Replacement |
|---------------|--------|-------------|
| `/focus/v1/{id}` | ❌ Removed | `/focus/v2/entity/{id}` |
| `/etl/release/run` | ❌ Removed | `/pipeline/auto-release/run` |
| `/stac/lite/{item}` | ❌ Removed | `/stac/v10/items/{id}` |
| `/graph/deprecated/query` | ❌ Removed | GraphQL endpoint |
| `/rs/hillshade` | ❌ Removed | `/terrain/svf` |

---

# 🗺️ Deprecated UI Modules (Web Platform)

~~~text
# ──────────────────────────────────────────────────────────────
#  v9.7 → v10 Web Client Deprecations
# ──────────────────────────────────────────────────────────────

web/src/focus/                              →   replaced by FocusMode/
web/src/map/                                →   replaced by MapView/
web/src/timeline/                           →   replaced by TimelineView/
web/src/components/legacy/                  →   removed
web/src/utils/date-old/                     →   removed (moved to utils/date/)
web/src/styles/old-tokens/                  →   removed (replaced with A11y Tokens v2)
~~~

All legacy modules fail CI automatically under v10.

---

# 🧬 Deprecated Lineage & Telemetry Features

### ❌ **Lineage v1**
- Missing PROV-O agent linking  
- Missing CARE records  
- No GeoSPARQL geometries  
- No telemetry binding  

**Replacement:**  
`Lineage v2` (validated via `lineage-validate.yml`)

---

### ❌ **Telemetry v1**
- Missing A11y data  
- Missing energy/carbon  
- No inference logs  

**Replacement:**  
Telemetry v2 (JSONL, aggregated, governance-linked)

---

# 🛡️ Governance Deprecations (FAIR+CARE v2)

### Removed:
- CARE v1  
- CARE “soft warning” system  
- Manual provenance notes  
- Unversioned audit logs  

### Required replacements:
- CARE v2 + sovereignty detection  
- Masking strategies (H3 R7/R5)  
- Automated governance ledger entries  
- Required hashes: `sha256`, `multihash`, `ledger_sig`  

---

# 🧪 CI/CD Deprecations

All these v9.7 workflows are now invalid:

~~~text
.github/workflows/rs-validate.yml
.github/workflows/stac-lite.yml
.github/workflows/basic-lint.yml
.github/workflows/focus-v1-tests.yml
.github/workflows/legacy-etl.yml
~~~

Replaced by v10’s required 11 validators.

---

# 🛠 Developer Action Required

To finalize v10 migration:

- [ ] Remove all deprecated directories shown above  
- [ ] Delete deprecated endpoints from backend code  
- [ ] Update imports to new v10 structures  
- [ ] Remove any remaining Focus Mode v1 logic  
- [ ] Update docs links to v10 equivalents  
- [ ] Re-run the Upgrade Validation Suite  

---

# 📜 Version History

| Version | Date | Summary |
|--------:|-------------|---------------------------------------------|
| v10.4.2 | 2025-11-16 | Full deprecated-features rewrite with new lined directory style |
| v10.0.0 | 2025-11-08 | Initial deprecation mapping |
| v9.7.x | 2025-05-01 | Pre-migration baseline |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
Master Coder Protocol v6.3 · FAIR+CARE v2 Certified  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Upgrade Index](./README.md)

</div>
