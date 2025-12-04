---
title: "📜 KFM v11.2.3 — NRCS Soils Citations & Usage Guidance (SSURGO · gNATSGO) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Canonical citation patterns and usage guidance for NRCS SSURGO/gNATSGO soils datasets and KFM-derived annual refresh products."
path: "docs/data/soils/annual-refresh/provenance/citations.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Geospatial Systems · FAIR+CARE Oversight"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "v10.x → v11.x soils-citations-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/soils-refresh-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/soils-refresh-v1.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Citation & Usage Guide"
intent: "nrcs-soils-annual-refresh-citations"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "CreativeWork"
  cidoc: "E31 Document"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/data-soils-annual-refresh-citations-readme-v1.json"
shape_schema_ref: "../../../../../schemas/shacl/data-soils-annual-refresh-citations-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "Permanent"
sunset_policy: "Never (citation guidance is historically cumulative; superseded statements must be versioned, not deleted)"
---

<div align="center">

# 📜 NRCS Soils Citations & Usage Guidance  
**SSURGO · gNATSGO · KFM Annual Soils Refresh**  
`docs/data/soils/annual-refresh/provenance/citations.md`

**Purpose:**  
Provide **canonical citation patterns** and **usage guidance** for:

- Upstream NRCS soils datasets (**SSURGO** and **gNATSGO**)  
- KFM’s **Annual Soils Refresh** derivatives (diffs, STAC catalogs, web layers)  

so that all downstream KFM work (papers, reports, Story Nodes, web maps) cites soils data in a **consistent, FAIR+CARE-aligned, and provenance-accurate** way.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

This document covers:

- How to **cite NRCS** soils datasets by year.  
- How to **cite KFM**-derived soils products (deltas, STAC catalogs, overlays).  
- How to describe soils **usage terms & disclaimers** in KFM outputs.

It is the human-facing companion to:

- `prov-ssurgo-YYYY.jsonld` / `prov-gnatsgo-YYYY.jsonld` — machine-readable PROV-O lineage.  
- `../README.md` — soils provenance overview.  
- `../../README.md` — annual soils refresh pipeline overview.  
- KFM STAC/DCAT standards under `docs/standards/catalogs/`.

All example citations below are templates; KFM outputs (papers, reports, Story Nodes) SHOULD replace `{PLACEHOLDERS}` with real years, access dates, and DOIs/URLs as available.

---

## 🧾 2. Canonical NRCS Citations (Templates)

These patterns MUST be used (with correct year & details) when **directly citing NRCS data** as the source.

### 2.1 SSURGO (Template)

Short template (KFM-neutral):

~~~text
Natural Resources Conservation Service (NRCS). {YEAR}. "Soil Survey Geographic (SSURGO) Database." United States Department of Agriculture.
Accessed {ACCESS_DATE}. {NRCS_URL_OR_DOI}
~~~

Example (illustrative; replace URL/DOI with actual NRCS reference):

~~~text
Natural Resources Conservation Service (NRCS). 2025. "Soil Survey Geographic (SSURGO) Database." United States Department of Agriculture.
Accessed 2025-10-15. https://www.nrcs.usda.gov/...
~~~

### 2.2 gNATSGO (Template)

~~~text
Natural Resources Conservation Service (NRCS). {YEAR}. "Gridded National Soil Survey Geographic (gNATSGO) Database." United States Department of Agriculture.
Accessed {ACCESS_DATE}. {NRCS_URL_OR_DOI}
~~~

Example (illustrative):

~~~text
Natural Resources Conservation Service (NRCS). 2025. "Gridded National Soil Survey Geographic (gNATSGO) Database." United States Department of Agriculture.
Accessed 2025-10-15. https://www.nrcs.usda.gov/...
~~~

### 2.3 Requirements

- `{YEAR}` MUST match the NRCS release year used in the KFM **Annual Soils Refresh** (e.g., 2024, 2025).  
- `{ACCESS_DATE}` SHOULD be the date on which KFM (or the downstream author) accessed the NRCS data.  
- `{NRCS_URL_OR_DOI}` SHOULD be a stable NRCS URL or DOI, taken from upstream metadata (`raw/metadata/`).

If NRCS updates citation guidance in future, **new guidance MUST be appended in a separate section** with version history updated at the bottom.

---

## 🧬 3. KFM-Derived Soils Citations (Diffs, STAC, Overlays)

KFM adds value via:

- Schema & topology validation.  
- Year-over-year diff computation (geometry & tabular).  
- STAC cataloging and provenance graph integration.  
- Derived overlays & Story Node narratives.

Citations MUST distinguish between **NRCS source** and **KFM derivatives**.

### 3.1 KFM Annual Soils Refresh (Pipeline-Level) — Template

~~~text
Kansas Frontier Matrix (KFM). {YEAR}. "Annual NRCS Soils Refresh (SSURGO · gNATSGO) for Kansas."
Version {PIPELINE_VERSION}. Lawrence, Kansas.
Derived from NRCS SSURGO/gNATSGO {YEAR} datasets. {KFM_DOI_OR_URL}
~~~

Example (illustrative):

~~~text
Kansas Frontier Matrix (KFM). 2025. "Annual NRCS Soils Refresh (SSURGO · gNATSGO) for Kansas."
Version v11.2.3. Lawrence, Kansas.
Derived from NRCS SSURGO/gNATSGO 2025 datasets. https://kfm.example.org/soils/annual-refresh/2025
~~~

### 3.2 KFM Soils Deltas (Geometry & Tabular) — Template

When citing **diff artifacts** (Parquet deltas):

~~~text
Kansas Frontier Matrix (KFM). {YEAR}. "NRCS Soils Deltas {YEAR_PREV}–{YEAR} (Geometry and Tabular)."
Version {PIPELINE_VERSION}. Lawrence, Kansas.
Derived from NRCS SSURGO/gNATSGO {YEAR_PREV} and {YEAR} datasets. {KFM_DOI_OR_URL}
~~~

Example:

~~~text
Kansas Frontier Matrix (KFM). 2025. "NRCS Soils Deltas 2024–2025 (Geometry and Tabular)."
Version v11.2.3. Lawrence, Kansas.
Derived from NRCS SSURGO/gNATSGO 2024 and 2025 datasets. https://kfm.example.org/soils/deltas/2024-2025
~~~

### 3.3 KFM Soils STAC Collections — Template

When referencing **STAC-level soils catalogs**:

~~~text
Kansas Frontier Matrix (KFM). {YEAR}. "NRCS Soils STAC Catalog ({PRODUCT} {YEAR}, Kansas AOI)."
Version {PIPELINE_VERSION}. Lawrence, Kansas.
STAC Collection: {STAC_COLLECTION_ID}. {KFM_STAC_URL}
~~~

Example:

~~~text
Kansas Frontier Matrix (KFM). 2025. "NRCS Soils STAC Catalog (SSURGO 2025, Kansas AOI)."
Version v11.2.3. Lawrence, Kansas.
STAC Collection: ssurgo-2025-ks. https://kfm.example.org/stac/ssurgo-2025-ks
~~~

---

## 🔗 4. Combined Citations (NRCS + KFM)

Many KFM outputs (papers, Story Nodes, maps) will rely on both NRCS source data and KFM derivatives. A combined style is recommended:

~~~text
Natural Resources Conservation Service (NRCS). {YEAR}. "Soil Survey Geographic (SSURGO) Database." United States Department of Agriculture. Accessed {ACCESS_DATE}. {NRCS_URL_OR_DOI}

Kansas Frontier Matrix (KFM). {YEAR}. "Annual NRCS Soils Refresh (SSURGO · gNATSGO) for Kansas."
Version {PIPELINE_VERSION}. Lawrence, Kansas. Derived from NRCS SSURGO/gNATSGO {YEAR} datasets. {KFM_DOI_OR_URL}
~~~

For works that also use deltas or specific STAC collections, add:

- A citation for **deltas** (geometry/tabular).  
- A citation for **the specific STAC Collection** used (e.g., SSURGO 2025 Kansas AOI).

This two-part (NRCS + KFM) pattern makes clear:

- Who produced the original soils data.  
- What KFM added (processing, diffing, cataloging, governance).

---

## ⚖️ 5. Usage Guidance & Disclaimers

All KFM soils-related outputs (STAC, DCAT, maps, notebooks, Story Nodes) MUST:

- Respect NRCS **conditions of use** and disclaimers.  
- Avoid representing KFM derivatives as **official NRCS products**.  
- Distinguish clearly between:
  - NRCS source datasets (SSURGO, gNATSGO).  
  - KFM processing (e.g., soils deltas, derived overlays, AI narratives).

Recommended language for KFM outputs (template):

~~~text
This work uses soil survey data from the USDA Natural Resources Conservation Service (SSURGO/gNATSGO {YEAR}).
Data have been processed and re-published by the Kansas Frontier Matrix (KFM) as part of its annual soils refresh pipeline.
Any interpretations or derived products presented here are the responsibility of KFM and do not represent official USDA or NRCS positions.
~~~

Where soils are combined with other layers (e.g., archaeological sensitivity, infrastructure):

- Additional FAIR+CARE or sovereignty language may be required.  
- If soils derivatives contribute to risk or sensitivity overlays, those overlays MUST also be cited and governed per their own standards (outside the scope of this file).

---

## 🧩 6. Where Citations Are Used in KFM

KFM components that MUST follow these citation patterns:

- **STAC → DCAT crosswalks**:
  - `dct:title`, `dct:description`, `dct:publisher`, `dct:creator`, `dct:license` fields.  

- **Story Nodes & Focus Mode**:
  - Context panels, metadata chips, and “About this dataset” views.

- **Web maps & overlays**:
  - Legend/info modals for soils layers.  
  - Download/citation panels.

- **Static documentation**:
  - Reports in `docs/`, `reports/`, or generated PDFs.  
  - Jupyter notebooks, whitepapers, and technical appendices.

Implementation details (how these templates map into UI text or DCAT fields) may be further specified in:

- `docs/standards/catalogs/stac-dcat-derivation.md`  
- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`  

---

## 🕰️ 7. Version History (Citations & Usage Guidance)

| Version  | Date       | Author                                   | Summary                                                                 |
|----------|------------|------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Geospatial Systems WG · FAIR+CARE Council | Initial NRCS + KFM soils citation and usage guidance; defined templates for SSURGO/gNATSGO, KFM annual refresh, deltas, and STAC catalogs; aligned with KFM-MDP v11.2.3 and soils provenance model. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0 (Citation Templates)**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Soils Provenance Overview](README.md) · [⬅ Back to Annual Soils Refresh](../README.md) · [📜 Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
