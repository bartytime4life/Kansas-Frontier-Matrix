---
title: "🧩 KFM v11.2.3 — STAC Extensions Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for KFM-specific STAC extensions and domain profiles used in the Kansas Frontier Matrix STAC metadata layer."
path: "docs/standards/catalogs/stac/extensions/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x extension-profile compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-stac-extensions-index-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-stac-extensions-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:stac:extensions:index:v11.2.3"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Standards Index"
intent: "catalogs-stac-extensions-index"
status: "Active / Enforced"

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
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/catalogs-stac-extensions-index-v1.json"
shape_schema_ref: "../../../../schemas/shacl/catalogs-stac-extensions-index-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major STAC extension standards overhaul"
---

<div align="center">

# 🧩 Kansas Frontier Matrix — STAC Extensions Index  
`docs/standards/catalogs/stac/extensions/README.md`

**Purpose:**  
Serve as the **governed index** for all **KFM-specific STAC extensions and domain profiles**, defining how KFM augments core STAC to capture FAIR+CARE, sovereignty, provenance, and domain metadata (climate, hydrology, archaeology, etc.) while remaining **STAC 1.0.x–compatible**.

</div>

---

## 📘 1. Scope

This index covers all **non-core STAC metadata** that KFM uses via:

- KFM **STAC extensions** (namespaces, additional fields).  
- Domain-specific profiles that **build on core STAC** (e.g., climate, archaeology, hydrology).  
- FAIR+CARE and sovereignty-related extension fields wired into:
  - Catalogs,  
  - web applications, and  
  - downstream DCAT derivation.

It sits under:

- `docs/standards/catalogs/README.md` — catalog standards index  
- `docs/standards/catalogs/stac/README.md` — STAC standards index  
- `docs/standards/catalogs/stac-dcat-derivation.md` — STAC-first → DCAT-derived model  

**KFM position:**  
> STAC extensions are **strict, versioned contracts**; they must remain compatible with core STAC 1.0.x and be documented, validated, and governed.

---

## 🗂️ 2. Directory Layout (v11.2.3)

~~~text
docs/standards/catalogs/stac/extensions/
├── 📄 README.md                          # This file — STAC extensions index
│
├── 🧩 stac-ext-kfm-core.md               # Core KFM STAC extension (shared fields across domains)
├── 🧩 stac-ext-faircare.md               # FAIR+CARE + sovereignty extension for KFM datasets
│
├── 🧩 stac-ext-climate.md                # Climate / atmosphere / weather-specific fields
├── 🧩 stac-ext-hydrology.md              # Hydrology / rivers / lakes-specific fields
├── 🧩 stac-ext-archaeology.md            # Archaeology / heritage-specific fields
│
└── 🧩 stac-ext-*.md                      # Additional domain extensions (landcover, geology, etc.)
~~~

**Directory contract:**

- Each `stac-ext-*.md` describes **one extension**:
  - Namespace, field names, datatypes, and semantics.  
  - JSON schema (or link to schema).  
  - Usage examples on STAC Items and Collections.  

- Extensions must be:
  - **Versioned** (e.g., `v1`, `v1.1` profiles within the doc).  
  - **Compatible** with STAC 1.0.x schemas and best practices defined in `stac-kfm-profile.md`.

---

## 🧩 3. Core KFM STAC Extension (`stac-ext-kfm-core.md`)

The **core KFM extension** is expected to define shared fields that appear across many domains, such as:

- KFM identifiers and classification:
  - `kfm:dataset_id`  
  - `kfm:domain` (e.g., `climate`, `hydrology`, `archaeology`)  
  - `kfm:subdomain`  

- Region and geometry context:
  - `kfm:region_slug` (linking to region registries)  
  - `kfm:crs` (if relevant for derived products)  

- Governance and lifecycle:
  - `kfm:release_stage`  
  - `kfm:lifecycle`  
  - `kfm:review_cycle`  

This extension should **not duplicate** functionality from existing STAC or community extensions (e.g., `eo`, `sar`) unless carefully justified.

---

## 🛡️ 4. FAIR+CARE & Sovereignty STAC Extension (`stac-ext-faircare.md`)

The **FAIR+CARE extension** codifies governance metadata at the STAC level:

Expected fields (illustrative):

- `kfm:care_sensitivity` — e.g., `"general"`, `"restricted-generalized"`.  
- `kfm:care_label` — FAIR+CARE label associated with the dataset.  
- `kfm:sovereignty_flag` — whether Indigenous or sovereignty-governed data is present.  
- `kfm:sovereignty_notes` — short explanation for reviewers.  

Usage:

- On **Items** and **Collections** to:
  - Drive **governance hooks** in web/ETL.  
  - Inform **STAC → DCAT** derivations (e.g., which datasets appear in public catalogs).  
  - Feed into regional / domain governance dashboards.

This extension must align with:

- `docs/standards/faircare/FAIRCARE-GUIDE.md`  
- `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

---

## 🌦️ 5. Domain Extensions (Climate, Hydrology, Archaeology, …)

Domain-specific extension docs (e.g., `stac-ext-climate.md`, `stac-ext-hydrology.md`, `stac-ext-archaeology.md`) are expected to define:

### 5.1 Climate / Atmosphere (`stac-ext-climate.md`)

Possible fields:

- `kfm:variable` (e.g., `temperature`, `precipitation`, `wind_speed`).  
- `kfm:vertical_level` (pressure levels or height).  
- `kfm:model_run_time` vs `properties.datetime` (forecast vs observation).  
- Coverage / resolution attributes relevant to climate models.

### 5.2 Hydrology (`stac-ext-hydrology.md`)

Possible fields:

- `kfm:watershed_id` / `kfm:river_id`.  
- Flow metrics (e.g., `kfm:discharge_cms` for snapshots).  
- Vertical datum or reference (e.g., `NAVD88`).

### 5.3 Archaeology & Heritage (`stac-ext-archaeology.md`)

Possible fields:

- `kfm:site_code` (internal; may be redacted in public catalogs).  
- `kfm:period` / `kfm:culture_phase` (linked to archaeology ontology).  
- `kfm:sensitivity_class` (for governance, generalization, and masking).

Each domain extension must:

- Clearly distinguish **internal-only** vs **public** fields.  
- Document any fields that must be **removed or generalized** when producing public STAC or DCAT.

---

## 🧪 6. Validation & Schema Requirements

Each extension must have:

- A **JSON Schema**:
  - Either local (e.g., `schemas/stac-ext-archaeology-v1.schema.json`), or  
  - Hosted in a shared KFM schema directory (`schemas/stac/`), referenced from the doc.

- Validation pathways:
  - Integration with `stac-validator` via `--extensions` or custom checks.  
  - CI jobs that ensure:
    - Only allowed fields are used under each extension namespace.  
    - Required fields are present when an extension is declared active.

CI jobs (names illustrative):

- `catalog-stac-extensions-validate.yml`  
  - Validates that extension fields match schema.  
  - Checks Items/Collections for declared extension usage.

---

## 🔁 7. Interaction with Crosswalks & DCAT

Extensions must be designed so that:

- **STAC → DCAT** crosswalks can interpret them:
  - Some extension fields map to DCAT/PROV-O (e.g., governance fields → DCAT metadata).  
  - Others remain STAC-only but should not conflict with derived DCAT.

The **crosswalk documents** (e.g., `crosswalks/stac-dcat-crosswalk.md`) should:

- Reference extensions here when relevant.  
- Document how extension fields are:
  - Propagated,  
  - Transformed, or  
  - Omitted from DCAT.

---

## ✅ 8. Implementation Checklist for New Extensions

When proposing a new STAC extension:

1. **Justify the need**:
   - Confirm it cannot be covered by existing STAC/community extensions.  

2. **Draft the extension doc**:
   - Create `stac-ext-<domain>.md` with:
     - Namespaces, fields, types, semantics, examples.  
     - FAIR+CARE & sovereignty implications.

3. **Create schema and tests**:
   - Add a JSON schema and sample STAC Items/Collections for validation.  

4. **Wire into CI**:
   - Update STAC validation workflows to include the extension schema.  
   - Add regression tests using example records.

5. **Review & approve**:
   - FAIR+CARE + sovereignty review (if applicable).  
   - Metadata & Catalogs WG review for semantic clarity.  

6. **Align crosswalks**:
   - Decide how (or if) extension fields map into DCAT or other formats.  
   - Update crosswalk docs and code accordingly.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created STAC extensions index; defined directory layout and governance expectations for KFM core and domain-specific STAC extensions; aligned with STAC-first catalog model and KFM-MDP v11.2.3. |


