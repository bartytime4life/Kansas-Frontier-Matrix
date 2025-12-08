---
title: "💧 Kansas Frontier Matrix — KDHE 2026 §303(d) Water-Quality Data Submission Node (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/domains/hydrology/kdhe/303d-2026-submission.md"
version: "v11.2.5"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council · Hydrology Governance Board"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Domain Submission Guide"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<prev-sha256-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.5/sbom.spdx.json"
manifest_ref: "releases/v11.2.5/manifest.zip"
telemetry_ref: "releases/v11.2.5/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/domains-hydrology-kdhe303d-v4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-SOVEREIGNTY.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "hydrology"
  applies_to:
    - "etl"
    - "validation"
    - "stac"
    - "provenance"
    - "telemetry"
    - "story-nodes"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed · Requires Sovereignty Review"
classification: "Public / Restricted-Context (environmental monitoring)"
sensitivity_level: "Low–Medium (spatial joins with Tribal/sovereign data possible)"
public_exposure_risk: "Low"
risk_category: "Regulatory Submission / Water Quality"
indigenous_rights_flag: true
redaction_required: true

json_schema_ref: "schemas/json/domains-hydrology-kdhe-303d-2026-v1.schema.json"
shape_schema_ref: "schemas/shacl/domains-hydrology-kdhe-303d-2026-v1-shape.ttl"

doc_uuid: "urn:kfm:doc:domains:hydrology:kdhe:303d-2026-submission:v11.2.5"
semantic_document_id: "kfm-domains-hydrology-kdhe-303d-2026-submission"
event_source_id: "ledger:docs/domains/hydrology/kdhe/303d-2026-submission.md"
immutability_status: "version-pinned"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "fabricated historical events"
  - "unverified regulatory claims"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded upon KDHE 2028 §303(d) submission pattern approval"
---

<div align="center">

# 💧 **KDHE 2026 §303(d) Water-Quality Data Submission Node**  
### *Kansas Frontier Matrix — Hydrology Domain Integration*  

`docs/domains/hydrology/kdhe/303d-2026-submission.md`

</div>

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 domains/
    └── 📁 hydrology/
        └── 📁 kdhe/
            📄 303d-2026-submission.md      # ← This document (domain submission guide)

📁 data/
└── 📁 hydrology/
    └── 📁 kdhe_2026/
        📁 raw/                             # Raw multi-source water-quality data (immutable commits)
        📁 validated/                       # QA/QC-passed measurements
        📁 standardized/                    # KDHE-aligned parameter/units schema
        📁 exports/                         # Final KDHE-ready bundles (CSV/JSON/GeoJSON)

📁 src/
└── 📁 pipelines/
    └── 📁 hydrology/
        └── 📁 kdhe_2026/
            📄 ingest.py                    # Deterministic, WAL-safe ingest
            📄 validate.py                  # Validation + QA/QC checks
            📄 standardize.py               # Schema + units harmonization
            📄 export_kdhe.py               # KDHE export emitter + STAC/PROV wiring
```

Implementations may add extra helpers (config, tests, notebooks), but the **raw → validated → standardized → exports** tiering must remain intact.

---

## 📘 Overview

This document defines the **authoritative KFM pattern** for integrating, validating, transforming, and preparing water-quality datasets intended for submission to the **Kansas Department of Health and Environment (KDHE)** for inclusion in the **2026 Clean Water Act §303(d) List of Impaired Waters**.

KDHE accepts “all existing and readily available” data collected from **2000‑01‑01 → 2025‑09‑30** with a submission deadline of **2025‑12‑08**.

The KFM hydrology pipelines:

- Aggregate and standardize multi-source water-quality data into a KDHE‑compatible schema.  
- Enforce deterministic ETL with **idempotent, WAL-backed** runs.  
- Emit **STAC/PROV/telemetry artifacts** suitable for regulatory handoff and internal Story Nodes.  
- Respect **FAIR+CARE** and **Indigenous data sovereignty** via masking and generalization rules.

Outputs may be provided directly to KDHE or surfaced through Kansas‑focused Story Nodes representing water-quality and impairment narratives.

---

## 📅 Submission Timeline Requirements

### KDHE Coverage Window

- **Start:** 2000‑01‑01  
- **End:** 2025‑09‑30  
- **Submission deadline:** 2025‑12‑08  

### Internal KFM Deadlines (for v11.2.5 submission cycle)

| Stage                | Deadline     | System / Branch              |
|----------------------|-------------|------------------------------|
| Raw data freeze      | 2025-11-20  | lakeFS branch `kdhe_2026`   |
| QC / Validation lock | 2025-11-25  | Great Expectations + GE-X   |
| PROV lineage lock    | 2025-11-27  | OpenLineage + Neo4j         |
| Final KDHE export    | 2025-12-05  | `data/hydrology/kdhe_2026/exports/` |

After **raw data freeze**, only:

- Deterministic reprocessing (no new sources),  
- Validation rule tuning (governance-approved), and  
- Export formatting adjustments

are permitted.

---

## 🔬 Technical Requirements (KDHE-Aligned)

### Accepted Measurements (Non-Exhaustive)

- **Nutrients:**  
  - Nitrate, Nitrite, TKN, Total Nitrogen, Dissolved Phosphorus, Total Phosphorus (TP).  
- **Physical:**  
  - Temperature, Dissolved Oxygen (DO), pH, Specific Conductance/Conductivity, Turbidity.  
- **Biological:**  
  - *E. coli*, cyanotoxin indicators, algal biomass metrics (e.g., chlorophyll‑a where accepted).  
- **Hydrologic context:**  
  - Flow/Stage via USGS gauges and KGS crosswalks, attached in Neo4j as contextual nodes.

### Required Metadata Fields (KFM → KDHE Mapping)

| KFM Field          | KDHE Equivalent   | Required            |
|--------------------|-------------------|---------------------|
| `sampling_event_id`| Unique ID         | Yes                 |
| `location_id`      | Station ID        | Yes                 |
| `lat`, `lon`       | Coordinates       | Yes (or station xref) |
| `sample_datetime`  | Date/time         | Yes                 |
| `analyte`          | Parameter code    | Yes                 |
| `value`, `uq`, `units` | Measurement data | Yes              |
| `censored_flag`    | Censored/LOD flag | Strongly recommended |
| `method_id`        | Analytical method | Strongly recommended |
| `qa_flag`          | QA/QC status      | Required            |
| `source_system`    | Origin system     | Required (KFM-only field, mapped in metadata) |

The **standardization node** is responsible for mapping `analyte`, `units`, and `method_id` fields into KDHE‑compatible codes and canonical units.

---

## 🛠️ Deterministic ETL Pattern for KDHE 2026

The KDHE 2026 pipeline instantiates the **Idempotent Node** and **Event‑Driven Deterministic Ingestion** patterns for the hydrology domain.

### 1. Ingest Node

- Sources (illustrative, subject to licensing and agreements):
  - KGS, USGS NWIS, EPA STORET, KDHE internal feeds (where permitted),
  - Tribal datasets (subject to sovereignty- and CARE-aligned generalization rules).

- Guarantees:
  - All raw payloads stored under `data/hydrology/kdhe_2026/raw/` in lakeFS with:
    - **Immutable commits**,  
    - **WAL replay** metadata,  
    - Checksums and upstream identifiers.

### 2. Validation Node

- Core checks (Great Expectations / equivalent):

  - **Temporal validity:**
    - All `sample_datetime` within `[2000-01-01, 2025-09-30]`.  

  - **Spatial validity:**
    - Coordinates within Kansas + configured buffer (e.g., 5km) or mapped via station indices.  

  - **Value checks:**
    - Outlier detection using HYDRO-ZScore v3 / domain rules,  
    - Non‑negative for parameters that cannot be negative,  
    - Detection limits and censored flags consistent.

- Output:
  - `data/hydrology/kdhe_2026/validated/` plus:
    - Validation report (JSON/MD),
    - PROV activities for validation steps,
    - Telemetry metrics for validation cost.

### 3. Standardization Node

- Applies **KFM Hydrology Standard v4**:

  - Parameter normalization to KDHE code system (e.g., STORET-style codes or KDHE-specific codes).  
  - Unit conversion to KDHE‑accepted canonical units.  
  - Station/study area crosswalk to KDHE station identifiers where possible.  
  - CARE / sovereignty masking:
    - Generalized coordinates or station‑level abstraction where required.

- Output:
  - `data/hydrology/kdhe_2026/standardized/` with:
    - A uniform tabular schema ready for export,
    - STAC Collection / Item metadata stubs for later cataloging.

### 4. Export Node

Creates deterministic, KDHE-ready artifacts under:

```text
📁 data/
└── 📁 hydrology/
    └── 📁 kdhe_2026/
        📁 exports/
            📄 kfm_2026_kdhe_measurements.csv
            📄 kfm_2026_kdhe_metadata.json
            📄 kfm_2026_kdhe_prov.json
            📄 kfm_2026_kdhe_station_index.geojson
```

Each export bundle:

- Is reproducible from the same raw commits and config.  
- Carries:
  - Derivation hash,  
  - SLSA attestation,  
  - SBOM compatibility reference,  
  - Energy/carbon telemetry.

Optional (recommended):

- Emit a KDHE‑focused **STAC Collection** for the export, with Items referencing:
  - Measurements CSV, metadata JSON, station index GeoJSON, and PROV bundles.

---

## 🧠 Story Node Integration (Hydrology Domain)

Hydrology Story Nodes that discuss impaired or candidate waters can reference KDHE 2026 data via:

- Neo4j relationships:

  - `(:Waterbody)-[:HAS_MEASUREMENT]->(:Measurement)`,  
  - `(:Waterbody)-[:HAS_IMPAIRMENT_CANDIDATE {parameter, cycle:'2026'}]->(:KDHEImpairmentTag)`.

- Time-series visual layers:
  - MapLibre/Cesium overlays, timeline charts, and Focus Mode timelines built from standardized measurements.

Story Nodes may include:

- Localized historical context about a waterbody’s use, impairments, and interventions.  
- Overlays involving Tribal or sovereign lands, generalized per **CARE + sovereignty** rules.  
- Explicit links to KDHE submission snapshots for transparency:
  - e.g., `data/hydrology/kdhe_2026/exports/kfm_2026_kdhe_measurements.csv`.

Narratives must not:

- Promise regulatory outcomes,  
- Interpret KDHE policy decisions,  
- Fabricate or speculate beyond what data and KDHE documentation support.

---

## 🔗 Provenance & Lineage Guarantees

Each dataset in the KDHE export bundle is paired with:

- **OpenLineage event chain**:
  - From raw ingest → validation → standardization → export.  
- **Neo4j `DatasetVersion` node**:
  - Tied to KDHE 2026 cycle (`cycle: '2026'`, `domain: 'hydrology'`).  
- **Deterministic job hash**:
  - Including config, code version, and input content hashes.  
- **Immutable lakeFS commit**:
  - Representing the raw and standardized states.  
- **Telemetry snapshot**:
  - Energy (kWh), CO₂e, and cost for the ETL cycle.

These guarantees ensure that KDHE and downstream researchers can:

1. Trace any value back to its raw source and ingest commit.  
2. Re-run the pipeline and obtain bit‑identical exports for the same inputs and config.  
3. Audit all validation and masking steps via PROV/Ontology-aligned records.

---

## 🧩 Example PROV Snippet

```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "kfm:dataset:kfmx_hydro_2026_export": {
      "type": ["prov:Entity", "kfm:DatasetVersion"],
      "generatedAtTime": "2025-12-05T03:22:41Z",
      "kfm:derivation_hash": "sha256:<hash>",
      "kfm:cycle": "2026",
      "kfm:domain": "hydrology"
    }
  },
  "activity": {
    "kfm:pipeline:hydrology/kdhe_2026/export": {
      "type": ["prov:Activity", "kfm:ExportActivity"],
      "startedAtTime": "2025-12-05T03:00:00Z",
      "endedAtTime": "2025-12-05T03:22:41Z"
    }
  },
  "wasGeneratedBy": {
    "_:gen1": {
      "prov:entity": "kfm:dataset:kfmx_hydro_2026_export",
      "prov:activity": "kfm:pipeline:hydrology/kdhe_2026/export"
    }
  },
  "agent": {
    "kfm:system": {
      "type": ["prov:SoftwareAgent"],
      "kfm:component": "KFM Hydrology Pipelines v11.2.5"
    }
  },
  "wasAssociatedWith": {
    "_:assoc1": {
      "prov:activity": "kfm:pipeline:hydrology/kdhe_2026/export",
      "prov:agent": "kfm:system"
    }
  }
}
```

Concrete PROV bundles for each run must conform to `telemetry_schema` and `prov_profile`.

---

## 📝 Responsibilities & Governance

- **Hydrology Domain Stewards**  
  - Curate source manifest for KDHE 2026,  
  - Approve validation and standardization rules,  
  - Own the `kdhe_2026` pipeline configs.

- **FAIR+CARE Council**  
  - Review ethical and sovereignty alignment of data sources and masking rules,  
  - Approve any use of Tribal data in submissions or public narratives.

- **Reliability Engineering Guild**  
  - Enforce deterministic ETL behavior and SLO gates,  
  - Maintain CI/CD checks for idempotency, replay, and telemetry completeness.

- **Story Node Board**  
  - Review and approve hydrology Story Nodes that reference KDHE 2026 exports,  
  - Ensure narratives remain factual, contextual, and sovereignty‑aware.

Any changes to:

- Coverage window,  
- Source inclusion/exclusion,  
- Validation logic, or  
- Export schema

must be reviewed through governance and reflected in **version history** and PROV.

---

## 📈 Version History

| Version | Date       | Summary                                                                                  |
|--------:|------------|------------------------------------------------------------------------------------------|
| v11.2.5 | 2025-12-08 | Initial governed KDHE 2026 submission node pattern; integrated with idempotent/event-driven pipeline standards. |
| v11.2.4 | 2025-12-04 | Global MDP v11.2.4 alignment of hydrology domain docs and telemetry schema references.  |
| v10.x   | 2024-xx-xx | Earlier hydrology metadata structures and pre‑KDHE 2026 preparation guidance.           |

---

<div align="center">

💧 **Kansas Frontier Matrix — KDHE 2026 §303(d) Submission Node**  

[🌊 Hydrology Domain Index](../README.md) ·  
[📜 Project History Archive](../../../history/README.md) ·  
[⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>