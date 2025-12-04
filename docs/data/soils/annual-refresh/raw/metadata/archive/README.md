---
title: "🗃️ KFM v11.2.3 — NRCS Soils Upstream Metadata Archive (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Archive of superseded NRCS metadata (FGDC/ISO XML, release notes, checksums) for annual SSURGO/gNATSGO bundles in the KFM soils refresh pipeline."
path: "docs/data/soils/annual-refresh/raw/metadata/archive/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-refresh-raw-metadata-archive-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Raw Metadata Archive Index"
intent: "nrcs-soils-annual-refresh-raw-metadata-archive"

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

json_schema_ref: "../../../../../../../schemas/json/data-soils-annual-refresh-raw-metadata-archive-readme-v1.json"
shape_schema_ref: "../../../../../../../schemas/shacl/data-soils-annual-refresh-raw-metadata-archive-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (archived upstream metadata are immutable audit records)"
---

<div align="center">

# 🗃️ NRCS Soils Upstream Metadata Archive  
**SSURGO + gNATSGO · Superseded FGDC/ISO XML · Legacy Release Notes · Checksums**  
`docs/data/soils/annual-refresh/raw/metadata/archive/README.md`

**Purpose:**  
Maintain an **immutable archive** of superseded NRCS soils metadata (FGDC/ISO XML, release notes, checksums) for the **Annual Soils Refresh** pipeline, ensuring that all historical upstream descriptions remain **auditable and traceable** even when NRCS reissues or updates metadata.

</div>

---

## 📘 1. Scope

This directory contains **older or superseded upstream metadata** for NRCS soils releases, including:

- Prior-year metadata (e.g., SSURGO/gNATSGO 2024).  
- Earlier versions of metadata for the *same year* (e.g., `-v1`, `-v2`), when NRCS reissues XML or documentation.  
- Historical checksum files and release notes that have since been replaced.

These artifacts are:

- **Never edited or removed**, once archived.  
- Referenced by provenance and diff reports when NRCS metadata changes across time.  
- Used to understand:
  - How NRCS definitions and documentation evolved.  
  - Why KFM behavior or soils interpretation might differ between refreshes.

---

## 🗂️ 2. Directory Layout (Archive)

~~~text
docs/data/soils/annual-refresh/raw/metadata/archive/
│
├── 📄 README.md                          # This file — archive governance & layout
│
├── 📄 ssurgo-2024-metadata.xml           # FGDC/ISO XML or equivalent (SSURGO 2024)
├── 📄 gnatsgo-2024-metadata.xml          # FGDC/ISO XML or equivalent (gNATSGO 2024)
├── 📄 checksums-2024.txt                 # Official NRCS checksums for 2024 bundles
│
├── 📄 ssurgo-2025-metadata-v1.xml        # Superseded 2025 metadata (v1, if reissued)
├── 📄 ssurgo-2025-metadata-v2.xml        # Current 2025 metadata still mirrored in parent dir
├── 📄 gnatsgo-2025-metadata-v1.xml       # Superseded 2025 gNATSGO metadata (if any)
└── 📄 checksums-2025-v1.txt              # Superseded checksum set, if reissued by NRCS
~~~

> **Note:** Filenames above are illustrative; actual names MUST follow the conventions described below.

---

## 🧱 3. Naming & Versioning Rules

To keep the archive coherent and machine-usable:

- **Year-only entries** use:
  - `ssurgo-YYYY-metadata.xml`  
  - `gnatsgo-YYYY-metadata.xml`  
  - `checksums-YYYY.txt`  

- If NRCS reissues metadata during the same year:

  - First version (original) is archived as:
    - `ssurgo-YYYY-metadata-v1.xml`  
    - `gnatsgo-YYYY-metadata-v1.xml`  
    - `checksums-YYYY-v1.txt`  

  - Subsequent versions follow `-v2`, `-v3`, … as needed.

- The “active” metadata for the pipeline will be in the **parent directory**:
  - `../ssurgo-YYYY-metadata.xml`  
  - `../gnatsgo-YYYY-metadata.xml`  
  - `../checksums-YYYY.txt`  

When upgrading metadata for a year:

1. Move previous metadata into `archive/` and rename with appropriate `-vN` suffix.  
2. Update the parent directory with the new NRCS-provided files.  
3. Document the change in:
   - `processing/diff-report-YYYY.md`  
   - `provenance/prov-ssurgo-YYYY.jsonld` and `provenance/prov-gnatsgo-YYYY.jsonld`.

---

## 🔐 4. Immutability & Editing Rules

Archive files MUST be treated as **immutable**:

- No manual edits.  
- No machine rewrites in place.  
- No deletion of historical versions.

If a file is found to be corrupted or incorrect due to an operational mistake:

- Keep the incorrect file in the archive but annotate:
  - The correction and its rationale in:
    - `processing/diff-report-YYYY.md`.  
    - PROV-O logs for that year.  

This ensures that **all historical states** (including mistakes) remain visible for audit, while corrected versions are clearly identified.

---

## 🧬 5. Relationship to Provenance & Diff Reports

The archive is tightly coupled to:

- `docs/data/soils/annual-refresh/provenance/`  
  - PROV-O JSON-LD records refer to **specific metadata versions** when describing upstream entities.  

- `docs/data/soils/annual-refresh/processing/`  
  - `diff-report-YYYY.md` should:
    - Note when metadata is reissued or significantly changed.  
    - Refer to archived metadata filenames and versions.

When interpreting differences:

- If soils interpretations or schema expectations change between years, the archive:
  - Provides the upstream **“as-documented”** context for each year/version.  
  - Enables forensic analysis on why KFM’s behavior or outputs differ across soils refreshes.

---

## 📊 6. Telemetry for Metadata Version Changes

While archive content itself is static, metadata version changes should trigger telemetry events at the **processing** stage:

- Record:
  - Year and dataset (`SSURGO` / `gNATSGO`).  
  - Old vs new metadata filenames.  
  - Reason for change (e.g., NRCS erratum, updated definitions).  

- Telemetry is written to:
  - `../../../../../../../releases/v11.2.3/soils-refresh-telemetry.json`  
  - Under the `metadata_version_changes` or analogous dimension, per `soils-refresh-v1.json` schema.

This permits:

- Tracking frequency of upstream metadata corrections.  
- Detecting cascading impacts on downstream pipelines.

---

## 🧭 7. Governance & FAIR+CARE Context

Even though this directory contains metadata for **public-domain government data**, KFM still:

- Tracks changes in **usage terms, disclaimers, and constraints** across years.  
- Ensures that:
  - Licensing/terms updates are propagated to derived STAC, DCAT, and portal metadata.  
  - Any new restrictions or disclaimers are **respected** in KFM’s own distribution and visualization of soils data.

Any significant governance or licensing change detected in archived metadata MUST be:

- Called out explicitly in:
  - `processing/diff-report-YYYY.md`.  
  - `provenance/citations.md` (for citations and usage guidance).  

---

## 🕰️ 8. Version History (Metadata Archive Index)

| Version  | Date       | Author                                  | Summary                                                                 |
|----------|------------|-----------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial upstream metadata archive README; defined naming, immutability, and provenance rules for superseded NRCS soils metadata artifacts. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Upstream Metadata](../README.md) · [⬅ Back to Raw Bundles](../../README.md) · [⬅ Back to Annual Soils Refresh](../../../README.md) · [📜 Governance Charter](../../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

