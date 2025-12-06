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

doc_uuid: "urn:kfm:doc:standards:catalogs:index:v11.2.3"
semantic_document_id: "kfm-standards-catalogs-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:index:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../schemas/telemetry/catalog-metadata-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../faircare.md"
sovereignty_ref: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_kind: "Standards Index"
intent: "catalogs-standards-index"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
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
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "12 Months"
sunset_policy: "Superseded by next major catalog standards overhaul"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "timeline-generation"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "governance-override"
  - "narrative-fabrication"

transform_registry:
  allowed:
    - "summary"
    - "semantic-highlighting"
    - "metadata-extraction"
    - "timeline-generation"
    - "a11y-adaptations"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "governance-override"
    - "narrative-fabrication"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "📦 STAC Standards"
    - "📚 DCAT Standards"
    - "🔁 Crosswalks & Derivation"
    - "📊 Telemetry, Validation & Governance"
    - "✅ Implementation Checklist"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Catalog & Metadata Standards Index (v11.2.3)**  
`docs/standards/catalogs/README.md`

**Purpose**  
Serve as the **governed index** for all **catalog and metadata standards** in KFM — including **STAC**, **DCAT**, KFM profiles, crosswalks, and validation patterns that keep spatial catalogs, discovery portals, and external federations consistent, FAIR+CARE-compliant, and provenance-aligned.

</div>

---

## 📘 Overview

This index covers the **catalog layer** of the Kansas Frontier Matrix (KFM):

- **STAC (SpatioTemporal Asset Catalog)** standards and KFM profiles.  
- **DCAT / GeoDCAT** profiles used for catalogs and federation.  
- **STAC → DCAT crosswalks**, including the KFM **STAC-first, DCAT-derived** model.  
- Validation, telemetry, and governance expectations for catalog metadata.

It complements:

- `docs/standards/kfm_markdown_protocol_v11.md` — Markdown / docs protocol.  
- `docs/standards/faircare.md` — FAIR+CARE data governance.  
- `docs/standards/governance/ROOT-GOVERNANCE.md` — global governance charter.  
- `docs/standards/data-contracts.md` — dataset metadata & contracts standard.

### Who Should Read This

| Role / Team              | Why this index matters                                      |
|--------------------------|-------------------------------------------------------------|
| Catalog / metadata WG    | Defines authoritative STAC/DCAT profiles and crosswalks.    |
| Pipeline & ETL engineers | Specifies how outputs must be cataloged and validated.      |
| Portal & API developers  | Clarifies DCAT views derived from STAC for discovery.       |
| Governance & FAIR+CARE   | Shows where catalog governance and telemetry hooks attach.  |
| External integrators     | Provides crosswalks for federation with KFM catalogs.       |

---

## 🗂️ Directory Layout (v11.2.3)

~~~text
📂 docs/standards/catalogs/
├── 📄 README.md                         — ← This file (catalog & metadata standards index)
│
├── 🧩 stac/                             — STAC profiles & guidance
│   ├── 📄 stac-kfm-profile.md           — KFM STAC profile (Items, Collections, extensions)
│   └── 📄 stac-best-practices.md        — Naming, versioning, tiling & asset patterns
│
├── 🧩 dcat/                             — DCAT / GeoDCAT profiles & guidance
│   ├── 📄 dcat-kfm-profile.md           — KFM DCAT profile for portals & federation
│   └── 📄 dcat-examples.md              — Example DCAT JSON-LD / Turtle records
│
├── 🔁 crosswalks/                       — STAC ↔ DCAT (& optional CKAN) crosswalk documentation
│   ├── 📄 stac-dcat-crosswalk.md        — Field-level mappings & edge cases
│   └── 📄 stac-ckan-crosswalk.md        — (Optional) STAC → CKAN / portal mapping notes
│
└── 📦 stac-dcat-derivation.md           — STAC-first → DCAT-derived KFM standard
~~~

**Directory contract**

- All standards in this tree MUST:
  - Use **KFM-MDP v11.2.4**-compliant front-matter.  
  - Be **machine-extractable** (headings, tables, crosswalks).  
  - Align with FAIR+CARE and sovereignty rules where applicable.  
- Implementation code and CI workflows live outside this tree, but **must reference** these standards by path and version.

---

## 📦 STAC Standards (Authoritative Layer)

KFM treats **STAC as the spatially authoritative metadata layer**.

### Key STAC Standards (expected documents)

| File                        | Scope |
|-----------------------------|-------|
| `stac/stac-kfm-profile.md`  | Defines the KFM STAC profile: required properties, extensions, naming and versioning rules, collection/item conventions, and link structure. |
| `stac/stac-best-practices.md` | Asset patterns, geometry and bbox handling, temporal fields (`datetime`, `start_datetime`, `end_datetime`), checksum and size fields, collection vs item semantics. |

**KFM position**

- All geospatial/spatiotemporal datasets in KFM are represented **STAC first**.  
- STAC assets are:
  - Versioned with clear IDs.  
  - Validated via `stac-validator` + custom rules.  
  - Used as the **source of truth** for DCAT and other catalog layers.

---

## 📚 DCAT Standards (Derived Discovery Layer)

DCAT is used primarily for:

- Catalog discovery (search portals & APIs).  
- Federation with external catalogs.  
- Semantic web / Linked Data integration (JSON-LD, Turtle, RDF graphs).

### Key DCAT Standards (expected documents)

| File                      | Scope |
|---------------------------|-------|
| `dcat/dcat-kfm-profile.md` | KFM DCAT profile: required `dct:*` and `dcat:*` fields, use of `dct:spatial`, `dct:temporal`, `dcat:distribution`, `dcat:DataService`, FAIR+CARE and provenance fields. |
| `dcat/dcat-examples.md`  | Example `dcat:Dataset` / `dcat:Distribution` / `dcat:DataService` records derived from real KFM STAC Items and Collections. |

**KFM position**

- Production DCAT is **never manually curated** as the primary source.  
- DCAT is **derived from STAC** via governed crosswalks and tooling.  
- Hand-authored DCAT MAY exist for testing or documentation but is not authoritative.

---

## 🔁 Crosswalks & Derivation

The **crosswalks** directory documents field-level mappings and derivation rules.

### 1. STAC ↔ DCAT Crosswalk

| File                            | Scope |
|---------------------------------|-------|
| `crosswalks/stac-dcat-crosswalk.md` | Canonical field-level mapping between STAC Items/Collections and DCAT Datasets/Distributions, including edge cases. |

Typical mappings:

- STAC `id` → `dct:identifier`  
- STAC `properties.title` → `dct:title`  
- STAC `properties.description` → `dct:description`  
- STAC `bbox` / `geometry` → `dct:spatial`  
- STAC temporal fields → `dct:temporal`  
- STAC `assets.*` → `dcat:Distribution` records  
- STAC `links` (providers, license) → `dct:publisher`, `dct:license`, `dct:rights`

### 2. STAC → CKAN / Portal Crosswalk (Optional)

| File                           | Scope |
|--------------------------------|-------|
| `crosswalks/stac-ckan-crosswalk.md` | Notes and examples for projecting STAC-derived DCAT into CKAN-like portal schemas, if needed. |

---

## 📦 STAC → DCAT Derivation Standard

The document `stac-dcat-derivation.md` defines the **STAC-first → DCAT-derived** pattern:

- **Authoritative STAC**  
  - Human and pipeline authors work in STAC.  
  - STAC is validated and versioned.  

- **DCAT as a projection**  
  - DCAT JSON-LD is generated from STAC via crosswalk tooling.  
  - Optional RDF/Turtle representations produced for linked-data contexts.  

- **Core derivation rules** (examples)

  - `stac.id` → `dct:identifier`  
  - `stac.properties.license` → `dct:license`  
  - `stac.properties.provenance` → `prov:wasDerivedFrom` or `dct:source`  
  - `stac.assets[x].href` → `dcat:downloadURL` (or `accessURL`)  
  - `stac.collection` → `dct:isPartOf` (for `dcat:Dataset`)

- **CI constraints**

  - No DCAT record may be emitted unless its STAC source passes validation.  
  - Crosswalk tooling must succeed without critical mapping errors.  
  - Any change in crosswalk semantics is a governance event (review + version bump).

---

## 📊 Telemetry, Validation & Governance

Catalog metadata is subject to **strict validation and observability**.

### 1. Validation CI

Recommended workflows:

- `catalog-stac-validate.yml`  
  - STAC schema and KFM STAC profile checks.  

- `catalog-dcat-validate.yml`  
  - DCAT profile validation, JSON-LD structure checks.  

- `catalog-crosswalk-validate.yml`  
  - Ensures DCAT outputs are consistent with their STAC sources per crosswalk rules.

### 2. Telemetry

Telemetry (per release) includes:

- Count of STAC Items and Collections by domain.  
- DCAT derivation success/failure counts.  
- Top validation error categories and trends over time.  
- Coverage (percentage of datasets with both STAC and DCAT views).  

Stored at:

- `../../releases/v11.2.3/catalog-metadata-telemetry.json`  
- Validated with: `../../schemas/telemetry/catalog-metadata-v1.json`

### 3. Governance Hooks

- Changes to:
  - STAC profile,  
  - DCAT profile, or  
  - Crosswalk rules  

  MUST be treated as **governance events** and:

  - Logged to the governance ledger (`reports/audit/governance-ledger.json`).  
  - Reviewed by the Metadata & Catalogs WG and FAIR+CARE Council.  
  - Reflected in a version bump for the affected docs and tooling.  

---

## ✅ Implementation Checklist

When onboarding or updating catalog pipelines:

1. **STAC Contract**  
   - Dataset has a STAC Item/Collection compliant with `stac-kfm-profile.md`.  
   - Spatial and temporal coverage correctly defined.  

2. **DCAT Projection**  
   - DCAT records are generated **from STAC**, not hand-authored.  
   - DCAT validates against `dcat-kfm-profile.md`.  

3. **Crosswalk Compliance**  
   - `stac-dcat-crosswalk.md` covers all required mappings.  
   - Any domain-specific fields have crosswalk entries (or are explicitly excluded).  

4. **CI Integration**  
   - STAC, DCAT, and crosswalk validation workflows are wired into `.github/workflows/kfm-ci.yml`.  
   - Validation failures block merges for affected datasets or catalogs.  

5. **Telemetry & Governance**  
   - Telemetry entries emitted into `catalog-metadata-telemetry.json`.  
   - Governance ledger updated when profiles/crosswalks change.  

---

## 🕰️ Version History

| Version | Date       | Author                          | Summary                                                                                             |
|--------:|------------|---------------------------------|-----------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-03 | Metadata & Catalogs WG · KFM    | Created catalogs index; formalized directory layout; codified STAC-first → DCAT-derived model; aligned with KFM-MDP v11.2.4 and telemetry v1. |

---

<div align="center">

📚 **Kansas Frontier Matrix — Catalog & Metadata Standards Index (v11.2.3)**  
“STAC first. DCAT derived. Provenance everywhere.”

© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Standards Index](../README.md) ·  
[🏛 Root Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>
