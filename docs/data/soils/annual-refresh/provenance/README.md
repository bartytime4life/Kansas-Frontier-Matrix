---
title: "📜 KFM v11.2.3 — Annual NRCS Soils Provenance & Citations (SSURGO · gNATSGO) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "PROV-O lineage, citations, and governance anchors for the annual NRCS SSURGO/gNATSGO soils refresh pipeline in the Kansas Frontier Matrix."
path: "docs/data/soils/annual-refresh/provenance/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-provenance-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Provenance Overview"
intent: "nrcs-soils-annual-refresh-provenance"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-provenance-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-provenance-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (provenance records are immutable audit artifacts)"
---

<div align="center">

# 📜 Annual NRCS Soils Provenance & Citations  
`docs/data/soils/annual-refresh/provenance/README.md`

**Purpose:**  
Define the **PROV-O lineage, citation anchors, and governance metadata** for the KFM **Annual NRCS Soils Refresh** (SSURGO & gNATSGO), connecting:

- Raw NRCS bundles (`raw/`)  
- Processing & diff engine (`processing/`, `deltas/`)  
- Soils STAC catalogs (`stac/`)  
- External citations and usage guidance  

into a **coherent soils provenance graph**.

</div>

---

## 📘 1. Scope

This directory contains **provenance and citation artifacts** for each annual soils refresh:

- PROV-O JSON-LD documents describing fetch, validation, diff, and publication activities.  
- Citation documents for NRCS soils datasets and KFM-derived representations.  
- The canonical link between annual soils refresh operations and the KFM **provenance graph**.

This README is the provenance-specific companion to:

- `../README.md` — Annual Soils Refresh pipeline overview.  
- `../processing/README.md` — Processing & diff engine.  
- `../stac/README.md` — Soils STAC catalogs.  

---

## 🗂️ 2. Directory Layout (Provenance Layer)

~~~text
docs/data/soils/annual-refresh/provenance/
│
├── 📄 README.md                      # This file — soils provenance overview
│
├── 📄 prov-ssurgo-2025.jsonld        # PROV-O lineage for SSURGO 2025 refresh
├── 📄 prov-gnatsgo-2025.jsonld       # PROV-O lineage for gNATSGO 2025 refresh
│
└── 📄 citations.md                   # NRCS + KFM citation blocks & usage guidance
~~~

**Directory contract:**

- Each refresh year MUST have at least one **PROV-O JSON-LD file per product**:
  - `prov-ssurgo-YYYY.jsonld`  
  - `prov-gnatsgo-YYYY.jsonld`  
- `citations.md` contains a maintained list of:
  - NRCS source citations.  
  - KFM soils-refresh citation patterns.  
  - Known DOIs / identifiers and any usage constraints.

If additional provenance splits are introduced (e.g., per-subset), their naming and structure MUST be documented here.

---

## 🧬 3. PROV-O Model Overview

Each `prov-*.jsonld` file encodes the soils refresh as a **PROV-O graph**:

- **Entities (`prov:Entity`)**:
  - `raw` NRCS bundles (SSURGO/gNATSGO ZIPs, metadata XML, checksums).  
  - Derived tables and intermediate data (if modeled at this level).  
  - STAC Collections & Items for a given year.  
  - Geometry/tabular diff Parquet files (`deltas/`).  

- **Activities (`prov:Activity`)**:
  - `fetch` — NRCS bundle acquisition.  
  - `schema_validation` — schema & topology checks.  
  - `diff` — geometry/tabular diff computation.  
  - `stac_publish` — STAC soils catalog creation for that year.  
  - `telemetry_export` — summarizing metrics into `soils-refresh-telemetry.json`.

- **Agents (`prov:Agent`)**:
  - NRCS (as upstream data provider).  
  - KFM Geospatial Systems WG (as processor).  
  - KFM infrastructure (e.g., pipelines or services) modeled as software agents, if desired.

This structure allows:

- Querying “what data and operations produced SSURGO/gNATSGO 20XX in KFM?”  
- Understanding changes in KFM behavior when upstream NRCS schemas/definitions change.  
- Driving visualization of soils lineage in the KFM provenance graph.

---

## 🧾 4. `prov-ssurgo-YYYY.jsonld` & `prov-gnatsgo-YYYY.jsonld`

### 4.1 Required Content

Each per-year, per-product provenance document MUST encode:

- A **fetch activity**:
  - Start/end time, NRCS URLs, KFM storage locations (`raw/`).  
  - Input `prov:Entity` for NRCS bundles and metadata.  

- A **validation activity**:
  - Inputs: fetched ZIPs & metadata.  
  - Outputs: validation logs (summarized in `processing/schema-validation.md`).  
  - Status: success/warnings/errors.

- A **diff activity**:
  - Inputs: current-year raw/baseline; prior-year baseline.  
  - Outputs:
    - `geometry-diff-YYYY-prev.parquet`  
    - `tabular-diff-YYYY-prev.parquet`  

- A **STAC publication activity**:
  - Inputs: processed soils data & diff results.  
  - Outputs:
    - `stac/ssurgo-YYYY/collection.json` and Items.  
    - `stac/gnatsgo-YYYY/collection.json` and Items.

- A **telemetry export activity**:
  - Inputs: processing metrics.  
  - Outputs:
    - `releases/v11.2.3/soils-refresh-telemetry.json` entries for that year.

### 4.2 Identifier & URI Patterns

Entities and activities SHOULD use stable URIs/IRIs based on:

- KFM dataset IDs (`urn:kfm:dataset:ssurgo-ks-YYYY`, `gnatsgo-ks-YYYY`).  
- Relative paths to artifacts within the repo (STAC, deltas, logs).  
- NRCS canonical URLs where appropriate.

Patterns MUST be consistent across years to enable longitudinal queries.

---

## 📚 5. Citations & Usage Guidance (`citations.md`)

`citations.md` provides:

- **Canonical citation strings** for:
  - NRCS SSURGO and gNATSGO (by year).  
  - KFM-added value (diff engine, STAC catalogs, derived products).

- **Usage guidance**:
  - Under what terms KFM redistributes soils data.  
  - How to cite KFM in downstream science & publications.  
  - Any NRCS-provided disclaimers that affect KFM use.

This file is the **human-facing counterpart** to licensing and provenance fields encoded in:

- STAC Collections & Items (via `license`, `providers`, etc.).  
- DCAT Datasets (via `dct:license` and related fields).  
- Internal documentation and Story Node metadata.

---

## 🔗 6. Relationships to Other Layers

Provenance is the **glue** between layers in the soils-refresh pipeline:

- **Raw data (`../raw/`)**:
  - PROV-O `prov:used` points to NRCS ZIPs, metadata, and checksums.  

- **Processing (`../processing/`)**:
  - Activities in `lineage-events.json` are often a **lower-level source** used to build `prov-*.jsonld`.  
  - `diff-report-YYYY.md` and `schema-validation.md` are cited as `prov:Entity` or via `prov:wasDerivedFrom` when needed.

- **Deltas (`../deltas/`)**:
  - Diff Parquet files are `prov:Entity` outputs of the **diff activity**.

- **STAC (`../stac/`)**:
  - STAC Collections & Items are `prov:Entity` outputs of the **stac_publish** activity.  
  - STAC `links` may include provenance references back to `prov-*.jsonld`.

Downstream components (graph, web, analytics) MUST treat these provenance docs as:

- The primary **truth source** for soils-refresh lineage.  
- The basis for any “why am I seeing this soils version?” UI or analysis.

---

## 📊 7. Telemetry & Provenance Alignment

Telemetry and provenance must be consistent:

- Telemetry metrics in `soils-refresh-telemetry.json` SHOULD be referenced in PROV-O as:
  - Properties of activities or derived performance entities (e.g., “2025 soils refresh run metrics”).  

- `telemetry_schema` ensures soils-refresh telemetry is:
  - Machine-validated.  
  - Alignable with PROV-O and KFM sustainability reporting.

Any significant anomalies (e.g., unusually large diff magnitude, prolonged processing times) MUST be:

- Visible in both telemetry and PROV-O.  
- Summarized in `processing/diff-report-YYYY.md` where relevant.

---

## 🛡️ 8. Governance & FAIR+CARE Context

While NRCS soils data is generally public and low-sensitivity:

- The **usage context** can have ethical implications (e.g., zoning, land-use decisions).  
- Provenance MUST accurately:
  - Attribute NRCS as the upstream source.  
  - Represent KFM’s processing steps and added-value layers.  
  - Provide transparency about limitations and assumptions.

Any changes to NRCS usage terms or KFM redistribution policies MUST be:

- Recorded in:
  - `citations.md` (usage guidance).  
  - Corresponding year’s diff report and schema-validation summary, if relevant.  
- Reflected in:
  - STAC/DCAT licensing fields.  
  - User-facing documentation.

---

## 🕰️ 9. Version History (Provenance Overview)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial soils provenance README; defined PROV-O structure, per-year per-product provenance docs, citations anchor, and relationships to raw/processing/deltas/STAC layers. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annual Soils Refresh](../README.md) · [⬅ Back to Soils Data Index](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

