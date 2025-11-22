---
title: "🛰️ OpenLineage v2.5 Governance Test Plan — Unified Dataset/Model/Pipeline Lineage Compliance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/tests/plans/lineage/openlineage/README.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Quarterly • Provenance Governance Board • FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/openlineage-testplan-v11.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Lineage-Test-Plan"
intent: "openlineage-governance-testplan"
semantic_document_id: "kfm-lineage-testplan-openlineage"
doc_uuid: "urn:kfm:lineage:testplan:openlineage:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Moderate-Risk (lineage domain)"
immutability_status: "version-pinned"
---

<div align="center">

# 🛰️ **OpenLineage v2.5 Governance Test Plan**  
`docs/pipelines/validation-observability/tests/plans/lineage/openlineage/README.md`

**Purpose:**  
Define the **authoritative v11 test plan** for validating **OpenLineage v2.5** compliance across all lineage-emitting components of the Kansas Frontier Matrix:  
- ETL pipelines  
- AI model training & evaluation  
- Story Node v3 + Focus Mode v3 narrative generation  
- Telemetry emission  
- STAC/DCAT dataset processing  
- AI anomaly jobs (bias/drift/OOD/reasoning/etc.)

This plan ensures ALL lineage emitted by KFM is unified, traceable, PROV-O aligned, FAIR+CARE aware, and promotion-safe.

</div>

---

# 📘 Overview

This test plan validates that every pipeline or AI component emitting lineage through **OpenLineage** produces:

### ✔ Complete and valid OpenLineage events  
### ✔ Correct `run`, `job`, `dataset`, and `facet` structure  
### ✔ Compatible PROV-O translation  
### ✔ STAC/DCAT metadata enrichment for dataset nodes  
### ✔ Correct linkage to telemetry bundles  
### ✔ CARE-S sovereignty protections  
### ✔ Story Node v3 + Focus Mode lineage mapping  
### ✔ Promotion Gate v11 lineage guarantees  

The plan is **blocking** for all deployments and model promotions.

---

# 🗂 Directory Layout

```text
docs/pipelines/validation-observability/tests/plans/lineage/openlineage/
│
├── README.md                                       # This file
│
├── cases/                                          # Individual OpenLineage compliance tests
│   ├── structure/                                  # Event structure correctness
│   ├── datasets/                                   # Dataset lineage correctness
│   ├── jobs/                                       # Job hierarchy & IDs
│   ├── runs/                                       # Run lifecycle tests
│   ├── facets/                                     # Core & custom facet validation
│   │   ├── data_quality/
│   │   ├── schema/
│   │   ├── lineage_propagation/
│   │   ├── column_lineage/
│   │   └── ownership/
│   ├── prov_translation/                           # PROV-O equivalence tests
│   ├── stac_dcat/                                  # STAC/DCAT mapping validation
│   ├── sovereignty/                                # CARE-S lineage boundaries
│   ├── telemetry/                                  # OpenLineage ←→ telemetry linkage
│   └── promotion_gate/                             # Gate aggregation rules
│
├── configs/                                        # Execution configs for the test suite
│   ├── openlineage_testplan_v11.yaml
│   └── lineage_facet_rules_v11.yaml
│
└── reports/                                        # Auto-generated lineage evaluation reports
    ├── latest.json
    └── history/
```

---

# 🧩 OpenLineage v2.5 Governance Domains (Mandatory)

Each domain MUST pass for lineage to be considered promotion-safe.

---

## 1. 🧬 Event Structure & Schema Compliance  
Validates:

- Required fields (`eventType`, `eventTime`, `run`, `job`)  
- Valid UUIDs and URIs  
- Correct dataset URIs  
- Conformance to v2.5 schema  

**Fail → BLOCK**

---

## 2. 📦 Dataset Lineage Correctness  
Ensures:

- `inputDataset` / `outputDataset` nodes exist  
- Dataset namespace URIs valid  
- STAC/DCAT metadata attached  
- Geographic + temporal metadata present  

**Fail → BLOCK**

---

## 3. 🛠 Job & Run Continuity  
Checks:

- Run lifecycle (`START`, `RUNNING`, `COMPLETE`, `FAIL`)  
- Job version alignment  
- Correct job namespace (KFM prefix)  
- Deterministic reproducibility metadata  

**Fail → BLOCK**

---

## 4. 🧩 Facet Validation (Core + Custom)  
Includes:

- `dataQualityMetrics`  
- `schema`  
- `columnLineage`  
- `ownership`  
- `sourceCodeLocation`  
- `parentRun`  
- `errorMessage`  

All must be:

- Valid  
- Sufficient  
- Versioned  

**Fail → BLOCK**

---

## 5. 🧬 PROV-O Translation Consistency  
Checks:

- OpenLineage `Dataset` ↔ PROV `Entity`  
- OpenLineage `Run` ↔ PROV `Activity`  
- OpenLineage `Job` ↔ PROV `Plan/ActivityClass`  
- Facet provenance ↔ PROV attributes  

**Fail → BLOCK**

---

## 6. 🌐 STAC/DCAT Lineage Mapping  
Ensures:

- Dataset metadata enriched with STAC/DCAT fields  
- Valid spatial/temporal extents  
- Correct dataset rights/license  

**Fail → BLOCK**

---

## 7. 🪶 CARE-S Sovereignty Constraints  
Ensures:

- No disclosure of sensitive cultural datasets  
- Correct tribal data sovereignty annotations  
- Zero propagation of forbidden sites/narratives  

**Fail → BLOCK immediately**

---

## 8. ♻ Telemetry + OpenLineage Chain Linkage  
Validates:

- Telemetry bundles correctly linked to runs  
- Energy/compute/carbon data present  
- ISO 50001/14064 alignment  

**Fail → BLOCK**

---

## 9. 🧠 Narrative Lineage (Story Node v3 + Focus Mode v3)  
Ensures:

- Narrative outputs mapped to correct OpenLineage runs  
- Inputs, intermediate reasoning steps, and outputs documented  
- No hallucinated lineage nodes  

**Fail → BLOCK**

---

## 10. 🚦 Promotion Gate v11 Lineage Aggregation  
Final enforcement:

- All lineage domains pass  
- No unresolved IDs  
- No broken chains  
- No sovereignty violations  
- Telemetry complete  
- Full PROV-O equivalence  

**Any failure → promotion BLOCKED**

---

# 🛠 Example Test Config

```yaml
openlineage_testplan:
  version: "v11.0.0"
  required_domains:
    - structure
    - datasets
    - jobs
    - runs
    - facets
    - prov_translation
    - stac_dcat
    - sovereignty
    - telemetry
    - promotion_gate

rules:
  require_prov_chain: true
  require_stac_dcat: true
  require_telemetry: true
  block_on_care_s: true
  block_on_unresolved_urn: true
```

---

# 🧪 CI Integration

Executed by:

- `openlineage-governance-testplan.yml`  
- `prov-lineage-audit.yml`  
- `model-promotion-gate.yml`  
- `ai-lineage-testplan.yml`  
- `stac-dcat-lineage-validate.yml`  
- `telemetry-lineage-validate.yml`  
- `faircare-sovereignty-review-gate.yml`  

**Any failure** → merge + promotion **BLOCKED**.

---

# 🕰 Version History

| Version | Date | Author | Summary |
|---------:|------|--------|---------|
| v11.0.0 | 2025-11-21 | `@kfm-governance` | Initial creation of OpenLineage Governance Test Plan for KFM v11. |

---

<div align="center">

**Kansas Frontier Matrix — OpenLineage Governance Test Plan**  
*Unified Provenance · Ethical Lineage · FAIR+CARE Sovereignty-Compliant Intelligence*

[Back to Lineage Test Plans](../README.md) •  
[FAIR+CARE Charter](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>