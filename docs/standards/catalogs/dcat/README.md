---
title: "📚 KFM v11.2.3 — DCAT Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for DCAT-based catalog and discovery standards in the Kansas Frontier Matrix, including KFM DCAT profiles, examples, and STAC → DCAT crosswalk integration."
path: "docs/standards/catalogs/dcat/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "DCAT 2.x / 3.0 profile-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-dcat-index-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-dcat-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:dcat:index:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../schemas/telemetry/catalog-metadata-v1.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Standards Index"
intent: "catalogs-dcat-standards-index"
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

json_schema_ref: "../../schemas/json/catalogs-dcat-index-v1.json"
shape_schema_ref: "../../schemas/shacl/catalogs-dcat-index-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major DCAT standards overhaul"
---

<div align="center">

# 📚 Kansas Frontier Matrix — DCAT Standards Index  
`docs/standards/catalogs/dcat/README.md`

**Purpose:**  
Serve as the **governed index** for all **DCAT (Data Catalog Vocabulary)**–based standards used in KFM — including KFM DCAT profiles, examples, and their relationship to the **STAC-first → DCAT-derived** catalog model.

</div>

---

## 📘 1. Scope & Relationship to STAC

This index covers the **DCAT layer** in KFM:

- DCAT / DCAT-AP / GeoDCAT profiles used for:
  - Search & discovery portals.  
  - Interoperability with external catalogs (e.g., CKAN, national portals).  
  - Semantic web / Linked Data exports (JSON-LD, Turtle, RDF/XML).

It must be read alongside:

- `../README.md` — catalog standards root index.  
- `../stac/README.md` — STAC standards index.  
- `../stac-dcat-derivation.md` — **STAC-first → DCAT-derived** model.  
- `../crosswalks/stac-dcat-crosswalk.md` — field-level STAC → DCAT mappings.

**KFM position:**

- **STAC is authoritative.**  
- **DCAT is a derived discovery/federation layer**, generated from validated STAC via governed crosswalks.

---

## 🗂️ 2. Directory Layout (v11.2.3)

~~~text
docs/standards/catalogs/dcat/
├── 📄 README.md                         # This file — DCAT standards index
│
├── 📘 dcat-kfm-profile.md               # KFM DCAT profile (Dataset, Distribution, DataService rules)
├── 📘 dcat-examples.md                  # Example DCAT JSON-LD / Turtle records derived from STAC
│
└── 📘 dcat-federation-guidelines.md     # (Optional) DCAT guidance for external portals & federation
~~~

**Directory contract:**

- All DCAT standards docs here must:
  - Use **KFM-MDP v11.2.3** metadata.  
  - Be **machine-extractable** (clear headings, tables, crosswalks).  
  - Explicitly state that DCAT is **derived from STAC**, never the other way around.

Implementation code (generation pipelines, SHACL shapes, validators) lives outside this tree, but must reference these docs by path/version.

---

## 📦 3. KFM DCAT Profile (`dcat-kfm-profile.md`)

The KFM DCAT profile document is expected to define:

### 3.1 Core DCAT Classes

- `dcat:Dataset`  
- `dcat:Distribution`  
- `dcat:DataService` (for APIs and dynamic services)  
- Optionally `dcat:Catalog` and `dcat:CatalogRecord` if needed for portal integrations.

### 3.2 Required Dataset Fields

At minimum:

- `dct:identifier` — derived from STAC Item/Collection `id` or `kfm:dataset_id`.  
- `dct:title` — from STAC titles.  
- `dct:description` — summary description.  
- `dct:spatial` — bounding boxes / locations derived from STAC `bbox` / `geometry`.  
- `dct:temporal` — derived from STAC `datetime` / intervals.  
- `dcat:keyword` — from STAC `keywords`, domains, and extensions.  
- `dct:publisher`, `dct:creator` — from STAC `providers`.  
- `dcat:distribution` — mapping from STAC Assets.

### 3.3 Required Distribution Fields

Each `dcat:Distribution` MUST have:

- `dcat:downloadURL` or `dcat:accessURL` — from STAC Asset `href`.  
- `dct:format` — from STAC Asset `type`.  
- `dct:title` — from STAC Asset `title` (if present).  
- Optional `spdx:Checksum` from STAC Asset `checksum:*`.

### 3.4 Governance-Aware Fields

DCAT profile should describe:

- Where `kfmfc:*` FAIR+CARE concepts are surfaced in DCAT:
  - As `dcat:keyword`, custom properties, or in a DCAT profile extension.  
- How to ensure that DCAT distributions do **not leak** sensitive internal-only STAC assets.

---

## 📚 4. DCAT Examples (`dcat-examples.md`)

This document is expected to include:

- JSON-LD and Turtle examples of:

  - `dcat:Dataset` representing a single STAC Collection.  
  - `dcat:Dataset` + multiple `dcat:Distribution`s representing STAC multi-asset Items.  
  - Optional `dcat:DataService` record for KFM APIs (e.g., feature services, visualization services).

Each example should:

- Clearly annotate which STAC fields produced which DCAT fields.  
- Demonstrate FAIR+CARE / governance fields where applicable.  
- Show correct usage of `@context` and prefixes.

---

## 🌐 5. Federation & External Catalogs (`dcat-federation-guidelines.md`)

If present, this document should define:

- How KFM DCAT is **shared with external catalogs**:

  - National or state data portals.  
  - Research data exchanges.  
  - Partner CKAN instances.

- Required DCAT shapes or profiles for each partner.  
- How to avoid:

  - Leakage of internal-only datasets.  
  - Publishing derived DCAT that diverges from upstream STAC.

Topics may include:

- Use of **DCAT-AP** or **GeoDCAT-AP** when needed.  
- Preferred mechanisms: periodic dumps, federated SPARQL endpoints, or APIs.  
- Provenance of exported DCAT (linking back to KFM STAC).

---

## 🔁 6. Relationship to STAC & Crosswalks

This DCAT standards index is tightly coupled to:

- `../stac/README.md` — STAC is the **authoritative source**.  
- `../stac-dcat-derivation.md` — defines the STAC-first → DCAT-derived architecture.  
- `../crosswalks/stac-dcat-crosswalk.md` — field-level mapping between STAC and DCAT.

**Key rules:**

- DCAT **must never be maintained independently** of STAC for production catalogs.  
- Any change to the DCAT profile requires review of:
  - STAC → DCAT crosswalk logic.  
  - STAC profile and extensions, if impacted.

---

## 🧪 7. Validation, SHACL & CI

DCAT artifacts (JSON-LD, Turtle, RDF/XML) are validated via:

- JSON Schema (if used) and, primarily, **SHACL** shapes:

  - For `dcat:Dataset`, `dcat:Distribution`, `dcat:DataService`, etc.  

- CI workflows (names illustrative):

  - `catalog-dcat-validate.yml` — run RDF/JSON-LD validation (SHACL).  
  - `catalog-crosswalk-validate.yml` — ensure STAC ↔ DCAT consistency.

CI MUST:

- Fail if DCAT artifacts:

  - Violate KFM DCAT profile or SHACL shapes.  
  - Lack required fields mapped from STAC.  
  - Reference `dcat:downloadURL`s not present in STAC Assets.

- Confirm that:

  - No DCAT record exists without upstream STAC.  
  - FAIR+CARE-sensitive datasets appear only in DCAT exports where governance permits.

Telemetry from these checks is recorded in:

- `catalog-metadata-telemetry.json` with DCAT-specific stats (validation failures, export counts, etc.).

---

## ✅ 8. Implementation Checklist (DCAT Layer)

When building or updating catalog pipelines:

1. **Confirm STAC coverage:**
   - Ensure all datasets exist in STAC and pass KFM STAC profile validation.

2. **Use crosswalks:**
   - Generate DCAT JSON-LD from STAC using governed crosswalk code.  
   - Avoid hand-editing DCAT in production.

3. **Validate DCAT:**
   - Run SHACL/JSON-LD validation against KFM DCAT profile shapes.  
   - Fix any discrepancies in the crosswalk or STAC source (not just DCAT).

4. **Apply FAIR+CARE rules:**
   - Ensure DCAT exports do not include:
     - Internal-only datasets (`kfmfc:sensitivity = "restricted-internal"`).  
     - Sensitive distributions that should remain private.

5. **Document & monitor:**
   - Update `dcat-kfm-profile.md` and `dcat-examples.md` if profile changes.  
   - Monitor telemetry for DCAT validation and export runs.

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created DCAT standards index; defined directory structure for KFM DCAT profile, examples, and federation guidelines; aligned with STAC-first → DCAT-derived model and KFM-MDP v11.2.3. |


