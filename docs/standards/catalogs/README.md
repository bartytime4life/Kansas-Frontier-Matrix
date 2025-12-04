---
title: "📚 KFM v11.2.3 — Catalog & Metadata Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for STAC, DCAT, and catalog metadata standards in the Kansas Frontier Matrix, including profiles, crosswalks, and validation rules."
path: "docs/standards/catalogs/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 3.0 crosswalk-compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards-catalogs-index-v11.2.3"
semantic_document_id: "kfm-standards-catalogs-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:index:v11.2.3"

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
intent: "catalogs-standards-index"
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

json_schema_ref: "../../schemas/json/catalogs-index-v1.json"
shape_schema_ref: "../../schemas/shacl/catalogs-index-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major catalog standards overhaul"
---

<div align="center">

# 📚 Kansas Frontier Matrix — Catalog & Metadata Standards Index  
`docs/standards/catalogs/README.md`

**Purpose:**  
Serve as the **governed index** for all **catalog and metadata standards** in KFM — including **STAC**, **DCAT**, profiles, crosswalks, and validation patterns that keep spatial catalogs, discovery portals, and external federations consistent, FAIR+CARE-compliant, and provenance-aligned.

</div>

---

## 📘 1. Scope

This index covers:

- **STAC (SpatioTemporal Asset Catalog)** standards and KFM profiles.  
- **DCAT / DCAT-AP / GeoDCAT** profiles used for catalogs and federation.  
- **STAC → DCAT crosswalks**, including KFM’s STAC-first, DCAT-derived model.  
- Validation, telemetry, and governance expectations for catalog metadata.

It complements:

- `docs/standards/kfm_markdown_protocol_v11.2.2.md` — Markdown / docs protocol.  
- `docs/standards/governance/ROOT-GOVERNANCE.md` — global governance.  
- `docs/standards/faircare/FAIRCARE-GUIDE.md` — FAIR+CARE policy.

---

## 🗂️ 2. Directory Layout (v11.2.3)

~~~text
docs/standards/catalogs/
├── 📄 README.md                                   # This file — catalog standards index
│
├── 🧩 stac/                                       # STAC profiles & guidance
│   ├── 📄 stac-kfm-profile.md                     # KFM STAC profile (items, collections, extensions)
│   └── 📄 stac-best-practices.md                  # Naming, versioning, tiling & asset patterns
│
├── 🧩 dcat/                                       # DCAT / GeoDCAT profiles & guidance
│   ├── 📄 dcat-kfm-profile.md                     # KFM DCAT profile for portals & federation
│   └── 📄 dcat-examples.md                        # Example DCAT JSON-LD / Turtle records
│
├── 🔁 crosswalks/                                 # STAC ↔ DCAT crosswalk documentation
│   ├── 📄 stac-dcat-crosswalk.md                  # Field-level mappings & edge cases
│   └── 📄 stac-ckan-crosswalk.md                  # (Optional) STAC → CKAN/portal mapping notes
│
└── 📦 stac-dcat-derivation.md                     # STAC-first → DCAT-derived KFM standard
~~~

**Directory contract:**

- All **standards documents** under this tree must:
  - Use **KFM-MDP v11.2.3** metadata.  
  - Be **machine-extractable** (headings, tables, crosswalks).  
  - Align with KFM governance and FAIR+CARE requirements.  

- Implementation code and CI workflows live outside this tree, but **must reference** these standards by path and version.

---

## 📦 3. STAC Standards (Authoritative Layer)

KFM treats **STAC as the spatially authoritative metadata layer**.

Key documents (expected):

- `stac/stac-kfm-profile.md`  
  - Defines the KFM STAC profile: required fields, extensions, naming, versioning.  
  - Covers Items, Collections, Catalogs, and recommended link structures.

- `stac/stac-best-practices.md`  
  - Patterns for:
    - Geometry & bbox handling  
    - Asset naming and roles  
    - Temporal fields (`datetime`, `start_datetime`, `end_datetime`)  
    - Checksums and size fields  
    - Collection-level vs item-level semantics  

**KFM position:**

- All **geospatial datasets** in KFM are represented as **STAC first**.  
- STAC files are:
  - Version-controlled.  
  - Validated with `stac-validator` and additional checks.  
  - The **source of truth** for DCAT, CKAN, and other catalog layers.

---

## 📚 4. DCAT Standards (Derived Discovery Layer)

DCAT is used in KFM primarily for:

- Catalog discovery (portals, search interfaces).  
- Machine-to-machine federation with external catalogs.  
- Semantic web / Linked Data integration (JSON-LD, Turtle).

Key documents (expected):

- `dcat/dcat-kfm-profile.md`  
  - KFM’s DCAT profile:
    - Required `dct:*` and `dcat:*` fields.  
    - Use of `dct:spatial`, `dct:temporal`, `dcat:distribution`, `dcat:DataService`.  
    - FAIR+CARE and provenance alignment.

- `dcat/dcat-examples.md`  
  - Example `dcat:Dataset` and `dcat:Distribution` records derived from real STAC Items & Collections.  
  - Example `dcat:DataService` entries for APIs and live services.

**KFM position:**

- DCAT is **never authoritatively edited by hand** for production catalogs.  
- DCAT is always **derived from STAC** via governed crosswalks.

---

## 🔁 5. Crosswalks & Derivation (STAC → DCAT)

The **crosswalks** subdirectory documents field-level mappings:

- `crosswalks/stac-dcat-crosswalk.md`  
  - Detailed mapping table:
    - STAC Item/Collection → `dcat:Dataset`  
    - STAC Assets → `dcat:Distribution`  
  - Handling of:
    - Multi-asset items  
    - Collections with multiple temporal/spatial extents  
    - Provider and licensing information  
    - Checksums (`spdx:Checksum`) and roles

- Optional: `crosswalks/stac-ckan-crosswalk.md`  
  - Additional guidance for integration with CKAN-like portals (if in scope).

The **core normative statement** is implemented in:

- `stac-dcat-derivation.md`  
  - **STAC-first → DCAT-derived** pattern:  
    - STAC is edited & validated.  
    - DCAT is generated, never hand-crafted.  
    - CI enforces alignment.

---

## 🧱 6. STAC → DCAT Derivation Standard (Summary)

The document `stac-dcat-derivation.md` is the **canonical KFM standard** for this model and defines:

- Why STAC is **spatially authoritative**.  
- Why DCAT is **discovery/federation-focused** and thus derived.  
- The recommended architecture:

  - Authoritative STAC  
  - Validation (`stac-validator`, `stac-check`)  
  - Transform to DCAT JSON-LD via crosswalk scripts  
  - Optional export to Turtle / RDF/XML

- Minimal, stable STAC → DCAT crosswalk:
  - `id` → `dct:identifier`  
  - `bbox` → `dct:spatial`  
  - `datetime` / intervals → `dct:temporal`  
  - `assets.*` → `dcat:Distribution` fields

- Tooling recommendations and CI rules:
  - No orphan DCAT.  
  - No hand-edited DCAT in production.  
  - Crosswalk validation required.

This README should always be read **together with** `stac-dcat-derivation.md` for implementation.

---

## 📊 7. Telemetry, Validation & Governance Expectations

Catalog metadata is subject to:

- **Validation CI**:
  - `catalog-stac-validate.yml` — STAC schema & semantics.  
  - `catalog-dcat-validate.yml` — DCAT profile validation.  
  - `catalog-crosswalk-validate.yml` — STAC ↔ DCAT consistency.

- **Telemetry**:
  - Metrics on:
    - Number of STAC Items/Collections per domain.  
    - DCAT derivation frequency and success/failure counts.  
    - Validation error types and trends.

Telemetry configuration:

- Schema: `../../schemas/telemetry/catalog-metadata-v1.json`  
- Data: `../../releases/v11.2.3/catalog-metadata-telemetry.json`

**Governance rules:**

- Any change to:
  - STAC profile,  
  - DCAT profile, or  
  - Crosswalk rules  
  is a **governance event** that must:

  - Trigger review by Metadata & Catalogs WG + FAIR+CARE Council.  
  - Bump version numbers and update this README and related docs.

---

## ✅ 8. Implementation Checklist

When onboarding a new dataset or revising a catalog pipeline, ensure:

1. **STAC presence**  
   - STAC Item/Collection exists in the KFM STAC tree.  
   - It passes STAC validation and best-practices linting.

2. **Crosswalk coverage**  
   - Fields required by DCAT are present or derivable from STAC.  
   - Any domain-specific fields are mapped and documented in crosswalk docs.

3. **DCAT derivation**  
   - DCAT JSON-LD is generated from STAC via governed tools.  
   - Optional Turtle/RDF/XML exports are produced if needed for federation.

4. **CI integration**  
   - STAC, DCAT, and crosswalk validations are wired into CI.  
   - Telemetry is updated to capture validation and derivation metrics.

5. **Governance review**  
   - FAIR+CARE & sovereignty considerations are respected in metadata fields (e.g., not over-exposing sensitive content in public catalogs).

---

## 🕰️ 9. Version History

| Version  | Date       | Author                                      | Summary                                                                 |
|----------|------------|---------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created catalog standards index; documented STAC-first → DCAT-derived model and directory structure for STAC, DCAT, and crosswalk standards; aligned with KFM-MDP v11.2.3. |


