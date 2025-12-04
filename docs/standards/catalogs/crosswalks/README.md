---
title: "🔁 KFM v11.2.3 — Catalog Crosswalks Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for STAC ↔ DCAT and related catalog crosswalk standards in the Kansas Frontier Matrix."
path: "docs/standards/catalogs/crosswalks/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 2.x/3.0 crosswalk-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-crosswalks-index-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-crosswalks-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:crosswalks:index:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Standards Index"
intent: "catalogs-crosswalks-index"
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

json_schema_ref: "../../../schemas/json/catalogs-crosswalks-index-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-crosswalks-index-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major crosswalk standards overhaul"
---

<div align="center">

# 🔁 Kansas Frontier Matrix — Catalog Crosswalks Index  
`docs/standards/catalogs/crosswalks/README.md`

**Purpose:**  
Serve as the **governed index** for all **catalog crosswalk standards** in KFM — including **STAC → DCAT**, optional **STAC → CKAN/portal** mappings, and any future crosswalks — under the **STAC-first → DCAT-derived** model and FAIR+CARE + sovereignty governance.

</div>

---

## 📘 1. Scope & Relationship to Other Docs

This index covers **crosswalk documentation**, not implementation code:

- STAC → DCAT (primary, normative crosswalk).  
- Optional STAC → other catalog formats (CKAN, proprietary portals, etc.).  
- Any **KFM-specific crosswalk profiles** that describe how internal fields map to external catalog vocabularies.

It must be read alongside:

- `../README.md` — catalog standards index.  
- `../stac/README.md` — STAC standards index.  
- `../dcat/README.md` — DCAT standards index.  
- `../stac-dcat-derivation.md` — STAC-first → DCAT-derived model.  
- `../dcat/dcat-kfm-profile.md` — normative KFM DCAT profile.

**KFM position:**

- Crosswalks are **governed contracts**.  
- Crosswalk docs describe how **authoritative STAC** is transformed into **derived DCAT and other catalog forms**, with FAIR+CARE and sovereignty constraints preserved.

---

## 🗂️ 2. Directory Layout (v11.2.3)

~~~text
docs/standards/catalogs/crosswalks/
├── 📄 README.md                         # This file — crosswalk standards index
│
├── 🔁 stac-dcat-crosswalk.md            # STAC → DCAT field-level crosswalk (primary)
└── 🔁 stac-ckan-crosswalk.md            # (Optional) STAC → CKAN/portal crosswalk guidance
~~~

**Directory contract:**

- **`stac-dcat-crosswalk.md`** is the **primary, normative crosswalk** for the KFM STAC-first → DCAT-derived model.  
- Additional crosswalk docs (e.g. `stac-ckan-crosswalk.md`) MUST:
  - Clearly identify themselves as **secondary** and **derived from STAC**.  
  - Respect the same governance and FAIR+CARE requirements as the STAC → DCAT crosswalk.

Implementation code and CI pipelines live elsewhere (e.g., `pipelines/catalogs/stac-dcat/`), but must reference these documents by path and version.

---

## 📦 3. STAC → DCAT Crosswalk (`stac-dcat-crosswalk.md`)

This document is expected to define:

### 3.1 Dataset-Level Mapping

Field-level mapping from:

- **STAC Item/Collection** → **`dcat:Dataset`**:

Examples (conceptual):

- `STAC.id` / `kfm:dataset_id` → `dct:identifier`  
- `properties.title` / Collection `title` → `dct:title`  
- `properties.description` / Collection `description` → `dct:description`  
- `bbox` / `extent.spatial.bbox` → `dct:spatial` (as `dct:Location`)  
- `datetime` / temporal intervals → `dct:temporal` (`dct:PeriodOfTime`)  
- `keywords` / domain & extension tags → `dcat:keyword`  
- `providers` → `dct:publisher`, `dct:creator`  
- STAC Catalog/Collection links → `dcat:landingPage` or related link properties

### 3.2 Distribution-Level Mapping

From **STAC Assets** → **`dcat:Distribution`**:

- `assets.*.href` → `dcat:downloadURL` or `dcat:accessURL`  
- `assets.*.type` → `dct:format`  
- `assets.*.roles` → `dcat:role` (or profile-specific extension)  
- `checksum:sha256` → `spdx:Checksum`  

### 3.3 Governance & FAIR+CARE

The crosswalk must define:

- How `kfmfc:*` (FAIR+CARE extension) and domain sensitivities are:

  - Used to **filter** which STAC records are eligible for public DCAT.  
  - Reflected in DCAT (e.g., as `dcat:keyword` or via extended profile fields).

- How **internal-only fields** (e.g., `kfmarch:site_code_internal`) are excluded from DCAT.

### 3.4 Edge Cases & Domain-Specific Handling

For climate, hydrology, archaeology, etc., the crosswalk must document:

- How domain fields:
  - Map to DCAT keywords, descriptions, or theme/taxonomy codes.  
  - Are dropped or generalized when necessary.

---

## 🌐 4. STAC → CKAN / Portal Crosswalk (`stac-ckan-crosswalk.md`)

This optional document is expected to describe:

- How KFM maps STAC (or derived DCAT) into:

  - CKAN dataset and resource fields.  
  - Other portal-specific metadata fields.

Key concerns:

- Mapping of:

  - Titles, descriptions, tags/keywords.  
  - Spatial/temporal fields into portal-specific structures.  
  - Resource URLs, formats, checksums.

- Preservation of FAIR+CARE and sovereignty semantics:
  - Which datasets and fields are allowed in external portals.  
  - How to express governance information consistently, even in non-DCAT-native systems.

**KFM rule:**

- CKAN/portal metadata must be **derived from STAC (via DCAT or direct mapping)**, NOT maintained as an independent authoritative layer.

---

## 🧬 5. Provenance & Crosswalk Lineage

Crosswalks are **transformations** with their own provenance:

- STAC source (Items, Collections) — `prov:Entity`.  
- Crosswalk code / pipeline — `prov:Activity`.  
- DCAT / CKAN / portal artifacts — `prov:Entity` derived from STAC.

Crosswalk docs should:

- Reference where PROV-O models are defined (e.g., in provenance standards).  
- Encourage implementers to:
  - Record crosswalk version and config used.  
  - Capture derivation timestamps and result counts.

This ensures that:

- DCAT and portal catalogs can always be traced back to STAC.  
- Regression or divergence can be detected and corrected.

---

## 🧪 6. Validation & CI Expectations

Crosswalk behavior must be enforced in CI:

- **Crosswalk tests** (e.g., `catalog-crosswalk-validate.yml`) should:

  - Use example STAC records as fixtures.  
  - Generate DCAT (and optional CKAN/portal metadata).  
  - Validate outputs against:

    - KFM DCAT profile.  
    - Partner/portal profiles (where applicable).  
    - Expected governance rules (e.g., no internal-only datasets in public export).

- **Round-trip sanity checks** (where appropriate):

  - Verify that DCAT `dct:identifier`, spatial/temporal coverage, and distribution URLs still match STAC source.  

- **Governance checks**:

  - Confirm that crosswalk filters out datasets with `kfmfc:sensitivity = "restricted-internal"` for public exports.  
  - Confirm that visibility rules (e.g., `h3-only`) are honored in terms of what distributions are exposed.

Telemetry from crosswalk CI should be recorded in:

- `catalog-metadata-telemetry.json` with metrics such as:
  - Number of STAC records processed.  
  - Number of DCAT datasets produced.  
  - Number and type of crosswalk validation failures.

---

## ✅ 7. Implementation Checklist (Crosswalks)

When implementing or modifying a crosswalk:

1. **Document the mapping**  
   - Update `stac-dcat-crosswalk.md` (and others) with any field-level changes.  
   - Ensure docs and implementation stay synchronized.

2. **Respect STAC-first model**  
   - Confirm that **all fields** used in DCAT or portal outputs are derived from STAC or clearly documented supplemental logic.  
   - No “DCAT-only” primary fields without STAC backing.

3. **Apply FAIR+CARE & sovereignty filters**  
   - Use `kfmfc:*` and domain sensitivity fields to include/exclude or generalize datasets.

4. **Validate in CI**  
   - Add/update fixtures and tests in crosswalk CI.  
   - Ensure crosswalk changes cannot be merged with failing tests.

5. **Update telemetry and governance references**  
   - Track crosswalk jobs and export runs.  
   - Ensure governance docs referenced in STAC/ DCAT are up-to-date.

---

## 🕰️ 8. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created crosswalk standards index; documented directory structure for STAC → DCAT and STAC → CKAN crosswalk docs; aligned with STAC-first catalog model, DCAT profile, and KFM-MDP v11.2.3. |

