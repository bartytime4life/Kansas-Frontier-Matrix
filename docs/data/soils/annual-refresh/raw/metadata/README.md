---
title: "📑 KFM v11.2.3 — NRCS Soils Upstream Metadata (SSURGO · gNATSGO) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed storage and usage rules for original NRCS metadata (FGDC/ISO XML, release notes, checksums) associated with annual SSURGO/gNATSGO raw bundles in the KFM soils refresh pipeline."
path: "docs/data/soils/annual-refresh/raw/metadata/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-refresh-raw-metadata-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Raw Metadata Index"
intent: "nrcs-soils-annual-refresh-raw-metadata"

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
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../schemas/json/data-soils-annual-refresh-raw-metadata-readme-v1.json"
shape_schema_ref: "../../../../../../schemas/shacl/data-soils-annual-refresh-raw-metadata-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (upstream metadata is an immutable audit record)"
---

<div align="center">

# 📑 NRCS Soils Upstream Metadata  
**SSURGO + gNATSGO · FGDC/ISO XML · Release Notes · Checksums**  
`docs/data/soils/annual-refresh/raw/metadata/README.md`

**Purpose:**  
Define the **governed storage and usage rules** for original NRCS metadata (FGDC/ISO XML, release notes, checksums, readme files) associated with annual SSURGO/gNATSGO raw bundles used by the KFM **Annual Soils Refresh** pipeline.

</div>

---

## 📘 1. Scope

This directory contains **only upstream metadata** shipped by NRCS alongside soils bundles, including:

- FGDC/ISO XML metadata documents.  
- NRCS readme files and technical documentation.  
- Release notes (PDF/TXT).  
- Official checksum files (MD5/SHA, etc.), when provided.  

These artifacts:

- Provide **authoritative descriptions** of each annual soils release.  
- Anchor **citation and licensing** obligations.  
- Support **integrity verification and provenance** for the soils-refresh pipeline.  
- Are treated as **immutable reference records** — all parsing, extraction, or transformation happens downstream.

---

## 🗂️ 2. Directory Layout

~~~text
docs/data/soils/annual-refresh/raw/metadata/
│
├── 📄 README.md                        # This file — upstream metadata governance & layout
│
├── 📄 ssurgo-2025-metadata.xml         # FGDC/ISO XML or equivalent for SSURGO 2025
├── 📄 gnatsgo-2025-metadata.xml        # FGDC/ISO XML or equivalent for gNATSGO 2025
├── 📄 release-notes-2025.pdf           # NRCS release notes / tech docs (if provided)
├── 📄 checksums-2025.txt               # Official NRCS checksums (MD5/SHA, if provided)
│
└── 📁 archive/                         # Older or superseded metadata files
    ├── 📄 ssurgo-2024-metadata.xml
    ├── 📄 gnatsgo-2024-metadata.xml
    └── 📄 checksums-2024.txt
~~~

**Directory contract:**

- Year-specific files MUST follow a `*-YYYY.*` naming convention.  
- The `archive/` subdirectory is used when NRCS reissues metadata for the same year or when older formats are retained for audit purposes.  
- No derived or edited metadata belongs here — all **derived metadata** (e.g., KFM JSON-LD, STAC fields) lives in `processing/` and `provenance/`.

---

## 🔐 3. Ingestion & Integrity Rules

### 3.1 Placement Workflow

For each annual NRCS soils refresh:

1. Download NRCS metadata artifacts alongside the raw bundles:
   - FGDC/ISO XML.  
   - Readme, technical docs.  
   - Checksum files (if provided).

2. Place them in this directory as:

   - `ssurgo-YYYY-metadata.xml`  
   - `gnatsgo-YYYY-metadata.xml`  
   - `release-notes-YYYY.pdf` (or `.txt`)  
   - `checksums-YYYY.txt`  

3. If NRCS reissues metadata for a year:
   - Move the superseded file into `archive/` with a suffix (e.g., `-v1`, `-v2`) and log the change in:
     - `processing/diff-report-YYYY.md`  
     - `provenance/prov-*-YYYY.jsonld`.

### 3.2 Immutability & Editing Rules

- Files in this directory represent **upstream truth** from NRCS.  
- They MUST NOT be:
  - Manually edited.  
  - Machine-modified in place (e.g., search/replace).  
- Any parsing or conversion (e.g., XML → JSON-LD) must:
  - Create **new, derived artifacts** under `processing/` or `provenance/`.  
  - Capture transformation details in PROV-O.

---

## 🧬 4. Relationship to Downstream Components

Metadata in this directory feeds:

- **Provenance generation** (`provenance/prov-*.jsonld`):
  - Source metadata documents are referenced as `prov:Entity` inputs.  

- **STAC catalog production** (`stac/`):
  - Selected fields (spatial/temporal extents, credits, usage constraints) may be extracted and mapped into STAC properties or KFM extensions.

- **Citation & documentation** (`provenance/citations.md`):
  - Citation strings and references are derived based on NRCS-authoritative text.

Downstream processes MUST:

- Treat these files as **source-of-record for descriptive metadata**, not as plain text to be casually edited.  
- Capture any mapping logic in standards (e.g. STAC/DCAT crosswalk guidance) where appropriate.

---

## 📊 5. Telemetry & Verification for Metadata Stage

While this directory is static, the **metadata fetch and verification stage** is instrumented:

- Telemetry reported via:
  - `../../../../../../releases/v11.2.3/soils-refresh-telemetry.json`  
  - Schema: `../../../../../../schemas/telemetry/soils-refresh-v1.json`

Tracked metrics for metadata ingestion:

- Number of metadata artifacts fetched per year.  
- Success/failure of checksum verification.  
- Parsing/validation success of XML/structured metadata.  
- Detected discrepancies between NRCS checksums and KFM-computed hashes for the corresponding raw bundles.

---

## 🧭 6. Governance & FAIR+CARE Context

NRCS soils metadata generally:

- Relates to **public-domain government data** (subject to NRCS terms of use).  
- Does not contain **PII** or sensitive site-level data.  

Nevertheless, KFM must:

- Respect any **usage constraints** or disclaimers expressed in these files.  
- Incorporate such constraints in:
  - STAC licensing and usage notes.  
  - Downstream DCAT and portal metadata.  
  - User-facing disclosures where soils data is visualized.

Any change in NRCS usage terms detected across years MUST be:

- Called out in `processing/diff-report-YYYY.md`.  
- Reflected in `provenance/citations.md` and licensing fields for derived products.

---

## 🕰️ 7. Version History (Metadata Index)

| Version  | Date       | Author                                  | Summary                                                                 |
|----------|------------|-----------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial upstream metadata README; defined naming, immutability, and downstream usage rules for NRCS soils metadata artifacts. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Raw Bundles](../README.md) · [⬅ Back to Annual Soils Refresh](../../README.md) · [📜 Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

