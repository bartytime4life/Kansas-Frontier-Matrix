---
title: "📦 KFM v11.2.3 — Annual NRCS Soils Raw Bundles (SSURGO · gNATSGO) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Raw, verbatim NRCS SSURGO/gNATSGO annual bundles used as the authoritative upstream source for the KFM soils refresh pipeline."
path: "docs/data/soils/annual-refresh/raw/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-refresh-raw-contract compatible"

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

doc_kind: "Raw Data Index"
intent: "nrcs-soils-annual-refresh-raw"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "DataFeed"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-raw-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-raw-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (raw upstream artifacts are immutable audit records)"
---

<div align="center">

# 📦 Annual NRCS Soils Raw Bundles  
**SSURGO + gNATSGO · Verbatim Upstream Artifacts**  
`docs/data/soils/annual-refresh/raw/README.md`

**Purpose:**  
Define the **governed storage rules** for **raw NRCS SSURGO/gNATSGO bundles** that serve as the upstream source for the KFM **Annual Soils Refresh** pipeline.

</div>

---

## 📘 1. Scope

This directory holds **only**:

- **Verbatim annual NRCS soils bundles** (SSURGO + gNATSGO).  
- **Original NRCS metadata** (FGDC/ISO XML, readme files, change logs).  

These artifacts are:

- The **authoritative upstream inputs** for the soils provenance-diff pipeline.  
- Never modified in place — all transformations happen downstream (`processing/`, `deltas/`, `stac/`).  
- Used to compute:
  - Geometry & attribute diffs.  
  - STAC Collections & Items.  
  - PROV-O lineage and telemetry.

---

## 🗂️ 2. Directory Layout (Raw Bundles)

~~~text
docs/data/soils/annual-refresh/raw/
│
├── 📄 README.md                      # This file — raw data governance & layout
│
├── 📦 ssurgo-2025.zip                # Verbatim NRCS SSURGO 2025 bundle
├── 📦 gnatsgo-2025.zip               # Verbatim NRCS gNATSGO 2025 bundle
│
└── 📂 metadata/                      # Original NRCS metadata artifacts
    ├── 📄 ssurgo-2025-metadata.xml   # FGDC/ISO XML or equivalent
    ├── 📄 gnatsgo-2025-metadata.xml  # FGDC/ISO XML or equivalent
    ├── 📄 release-notes-2025.pdf     # NRCS release notes (if provided)
    └── 📄 checksums-2025.txt         # Official NRCS checksums (if provided)
~~~

**Directory contract:**

- Filenames MUST reflect:
  - Dataset (`ssurgo` / `gnatsgo`).  
  - Year (`YYYY`).  
  - Optional suffix indicating source or variant if NRCS changes naming (documented in this README when used).  
- Files must remain **byte-for-byte identical** to NRCS downloads.  
- No derived/processed content is allowed here (that belongs in `processing/`, `deltas/`, `stac/`).

---

## 🔐 3. Ingestion & Integrity Rules

### 3.1 Download & Placement

For each refresh year:

1. Download NRCS soils bundles from official URLs.  
2. Store them under `raw/` as:

   - `ssurgo-YYYY.zip`  
   - `gnatsgo-YYYY.zip`

3. store **all accompanying NRCS metadata** (XML, PDFs, TXT) in `raw/metadata/`.

### 3.2 Checksums & Verification

- For each ZIP and metadata artifact, compute a **SHA-256 checksum** and record it in:

  - `provenance/prov-ssurgo-YYYY.jsonld`  
  - `provenance/prov-gnatsgo-YYYY.jsonld`

- If NRCS publishes its own checksums:

  - Save them as `metadata/checksums-YYYY.txt`.  
  - Ensure KFM-computed SHA-256 values match the upstream references where possible.

### 3.3 Immutability

Once placed:

- Files in `raw/` MUST NOT be:
  - Edited.  
  - Recompressed.  
  - Partially replaced.

If a file is discovered to be corrupted or incorrectly named:

- Keep the corrupted/misnamed version in an **archive/incident** log (elsewhere).  
- Re-download and clearly document corrective actions in `processing/diff-report-YYYY.md` and `provenance` logs.

---

## 🧪 4. Relationship to Downstream Pipeline

`raw/` feeds:

- **Schema & topology validation** (documented in `processing/schema-validation.md`).  
- **Diff computation** (outputs stored in `deltas/`).  
- **STAC publication** (catalogs stored in `stac/`).  
- **Provenance generation** (records stored in `provenance/`).

Downstream processes MUST:

- Treat these ZIPs as **read-only sources**.  
- Use **copy-on-read** workflows (e.g., decompress to a temporary working area).  
- Capture all derived artifacts in non-raw directories.

---

## 📊 5. Telemetry Hooks (Raw Stage)

Although `raw/` is data-only, the **fetch and verification stage** emits telemetry to:

- `../../../../../releases/v11.2.3/soils-refresh-telemetry.json`  
- As defined in `../../../../../schemas/telemetry/soils-refresh-v1.json`

Tracked metrics (for the raw stage):

- Number of bundles fetched per year.  
- Download duration and size metrics.  
- Integrity check counts (pass/fail).  
- Number of retry attempts per URL.

This telemetry allows KFM to:

- Track upstream reliability.  
- Understand bandwidth and energy consumption for raw acquisitions.

---

## 🧭 6. Governance & FAIR+CARE Considerations

NRCS soils bundles are:

- Public-domain / open government data (subject to NRCS conditions of use).  
- Not inherently sensitive in the same way as PII or site-level archaeology data.

Nevertheless:

- All upstream usage must respect NRCS **citation and usage requirements**.  
- Governance decisions about **how soils are re-distributed** (e.g., as STAC or map services) are documented in:

  - `docs/data/soils/annual-refresh/README.md`  
  - `provenance/citations.md`  

Changes in NRCS licensing or usage terms MUST be recorded in:

- `processing/diff-report-YYYY.md`  
- `provenance` records for that year

---

## 🕰️ 7. Version History (Raw Bundles Index)

| Version  | Date       | Author                               | Summary                                                                 |
|----------|------------|--------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial governed raw bundles README; defined naming, integrity, and immutability rules for SSURGO/gNATSGO annual bundles. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Annual Soils Refresh](../README.md) · [⬅ Back to Soils Data Index](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

