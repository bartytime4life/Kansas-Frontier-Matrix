---
title: "🧰 Kansas Frontier Matrix — STAC Pipeline Utility Library (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/utils/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-stac-utils-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧰 **Kansas Frontier Matrix — STAC Pipeline Utility Library**  
`src/pipelines/stac/utils/README.md`

**Purpose:**  
Provide **shared, deterministic, FAIR+CARE-aligned utility modules** used across all STAC ingestion pipelines (monitoring, validation, transformation, publishing, telemetry).  
These utilities supply **safe geospatial helpers, metadata augmentation tools, STAC/EO/PROJ/SAR validators, provenance builders, and asset normalization logic** required for KFM’s Diamond⁹ Ω / Crown∞Ω ETL architecture.

<img alt="STAC Utils" src="https://img.shields.io/badge/STAC_Utils-Core_Toolset-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Deterministic" src="https://img.shields.io/badge/Deterministic-Yes-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Stable-success"/>

</div>

---

## 📘 Overview

`src/pipelines/stac/utils/` provides:

- **Metadata normalization tools** for STAC Items & Collections  
- **Asset inspection utilities** (roles, MIME types, projections, href checks)  
- **CARE-aware masking helpers** for sensitive datasets  
- **Checksum tools** for immutable artifact verification  
- **STAC filtering and grouping logic**  
- **Provenance chain construction** (PROV-O, CIDOC, STAC/DCAT alignment)  
- **Datetime/geospatial validators**  
- **JSON Schema guards**  

These utilities are imported by:

- `monitor.py`  
- `transform.py`  
- `publish.py`  
- GE expectation suites  
- Telemetry aggregation jobs  
- Graph hydration modules  

All utilities must be:

- Pure functions (unless explicitly telemetry-emitting)  
- Reproducible  
- Type-annotated  
- FAIR+CARE-compliant  
- Validated under MCP-DL v6.3

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/stac/utils/
├── README.md
│
├── stac_helpers.py          # General STAC utilities (filtering, grouping, link resolution)
├── asset_tools.py           # Asset role/MIME checks, extension inference, EO/PROJ/SAR helpers
└── metadata_tools.py        # Provenance, checksum, CARE masking, datetime normalization
~~~~~

---

## 🧩 Module Responsibilities

### 1. `stac_helpers.py`
Provides generalized helpers for:

- Filtering STAC Items by:
  - collection_id  
  - datetime window  
  - geometry intersection  
- Building STAC link relations consistently  
- Flattening nested STAC search results  
- Validating Item vs. Collection consistency  

**Used by:** `monitor.py`, `transform.py`, tests

---

### 2. `asset_tools.py`
Provides tools for inspecting and validating STAC **assets**:

- Detect incorrect MIME types  
- Ensure proper asset roles  
- Infer EO/PROJ/SAR extensions  
- Validate band metadata  
- Resolve relative vs. absolute `href`s  
- Flag missing asset-level metadata required by KFM  

**Used by:** `transform.py`, GE validation, publish routines

---

### 3. `metadata_tools.py`
Handles:

- `kfm:*` metadata insertion:
  - `kfm:checksum`
  - `kfm:ingest_version`
  - `kfm:care_label`
  - `kfm:provenance`
- CARE masking (H3 resolution, bbox generalization, centroid fuzzing)  
- Sovereignty flag detection (tribal overlays)  
- JSON-LD provenance chain construction  
- Datetime normalization helpers  
- File-level checksum verification  

**Used by:** `transform.py`, `publish.py`, governance engines

---

## 🔒 FAIR+CARE Compliance Requirements

All utilities MUST:

- Enforce metadata completeness  
- Reject unsafe/missing CARE labels  
- Apply masking logic when required  
- Maintain provenance chain integrity  
- Never leak precise coordinates from protected sites  
- Never override published metadata  
- Log governance-relevant signals when called from orchestrator contexts

Governance logs reference:

~~~~~text
../../../docs/reports/audit/data_provenance_ledger.json
~~~~~

---

## 🧪 Utility Workflow (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Raw STAC Item"] --> B["stac_helpers.py<br/>Filter · Normalize · Links"]
  B --> C["asset_tools.py<br/>MIME · Roles · Extensions"]
  C --> D["metadata_tools.py<br/>CARE · Provenance · Checksums"]
  D --> E["Validated Output"]
  E --> F["Publish / Graph Hydration / Telemetry"]
~~~~~

---

## 📦 Tests & Validation

Each utility module must include:

- **Unit tests** (`pytest`)  
- **Schema/DTO validation tests**  
- **CARE masking tests**  
- **Sovereignty intersection tests**  
- **Checksum reproducibility tests**  
- **Datetime normalization tests**  

CI enforcement:

- `docs-lint.yml`  
- `stac-validate.yml` (indirect)  
- `codeql.yml`  
- `telemetry-export.yml`  
- `faircare-validate.yml`

---

## 📡 Telemetry Integration

Utility calls may optionally emit telemetry signals (pure functions must not):

Telemetry captures:

- Care masking events  
- Extension inference frequencies  
- Asset-role corrections  
- Datetime normalization failures  
- Checksum mismatches  

Telemetry aggregated into:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧾 Example Provenance Utility Usage

~~~~~python
from stac.utils.metadata_tools import add_provenance

item = json.load(open("item.json"))
item = add_provenance(
    item,
    lineage_path="data/lineage/landsat/v10.3.1/lineage.json",
    checksum="sha256:abcd1234..."
)
~~~~~

~~~~~json
{
  "kfm:provenance": "data/lineage/landsat/v10.3.1/lineage.json",
  "kfm:checksum": "sha256:abcd1234..."
}
~~~~~

---

## 🧭 Local Development

~~~~~bash
pytest src/pipelines/stac/utils/
python -m stac.utils.stac_helpers
python -m stac.utils.asset_tools
python -m stac.utils.metadata_tools
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Created full STAC utility library documentation with FAIR+CARE, provenance, masking, and telemetry contracts. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Utility Library**  
Deterministic Tools × FAIR+CARE Compliance × Provenance Enforcement  
© 2025 Kansas Frontier Matrix — MIT License  

</div>
