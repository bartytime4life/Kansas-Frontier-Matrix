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

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalog-metadata-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../faircare/FAIRCARE-GUIDE.md"
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

json_schema_ref: "../../../schemas/json/catalogs-index-v1.json"
shape_schema_ref: "../../../schemas/shacl/catalogs-index-v1.shape.ttl"

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

- **STAC (SpatioTemporal Asset Catalog)** standards and KFM STAC profiles.  
- **DCAT / GeoDCAT** profiles used for catalogs and federation.  
- **STAC → DCAT crosswalks**, including the KFM **STAC-first, DCAT-derived** model.  
- Validation, telemetry, and governance expectations for catalog metadata.

It complements:

- `docs/standards/kfm_markdown_protocol_v11.md` — Markdown / documentation protocol.  
- `docs/standards/faircare/FAIRCARE-GUIDE.md` — FAIR+CARE data governance guide.  
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

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 standards/
        ├── 📁 catalogs/                           📚
        │   ├── 📄 README.md                       📚 Catalog & metadata standards index (this file)
        │   │
        │   ├── 🧩 stac/                           🛰️ STAC standards & KFM profiles
        │   │   ├── 📄 stac-kfm-profile.md         — KFM STAC profile (Collections, Items, extensions, kfm:* fields)
        │   │   └── 📄 stac-best-practices.md      — Naming, versioning, tiling & asset patterns
        │   │
        │   ├── 🧩 dcat/                           🗄️ DCAT / GeoDCAT profiles
        │   │   ├── 📄 dcat-kfm-profile.md         — KFM DCAT profile for catalogs & federation
        │   │   └── 📄 dcat-examples.md            — Example DCAT JSON-LD / Turtle records
        │   │
        │   ├── 🔁 crosswalks/                     🔀 STAC ↔ DCAT (and optional CKAN) mappings
        │   │   ├── 📄 stac-dcat-crosswalk.md      — Canonical STAC ↔ DCAT crosswalk (field-level)
        │   │   └── 📄 stac-ckan-crosswalk.md      — Optional STAC → CKAN / portal mapping notes
        │   │
        │   └── 📄 stac-dcat-derivation.md         🧬 STAC-first → DCAT-derived standard
        │
        ├── 📁 governance/                         ⚖️ Global governance & approvals
        ├── 📁 faircare/                           💛 FAIR+CARE policies
        └── 📁 sovereignty/                        🪶 Indigenous data protection
~~~

**Directory contract**

- Every Markdown in `docs/standards/catalogs/` must:
  - follow **KFM-MDP v11.2.4** front-matter and heading rules  
  - be machine-extractable (tables, crosswalks, and sections clearly structured)  
  - align with FAIR+CARE and sovereignty policies where applicable  
- Implementation code and CI workflows live outside this directory, but MUST reference these standards by path and version.

---

## 📦 STAC Standards

KFM treats **STAC as the spatially authoritative metadata layer**.

### 1. `stac-kfm-profile.md` — KFM STAC Profile

Defines:

- Required STAC fields for **Collections** and **Items** (core STAC + KFM extensions).  
- KFM `kfm:*` properties for:
  - ingest state, QC, SLO state, mission tags, event references  
- Naming & ID patterns:
  - collection and item IDs  
  - versioning fields (`kfm:version`, `kfm:processing_level`)  
- Link structure (`self`, `parent`, `root`, `license`, `derived-from`, etc.).  
- Constraints on `geometry`, `bbox`, `datetime`, and temporal ranges.

### 2. `stac-best-practices.md` — Asset & Layout Guidance

Defines:

- Asset roles (e.g., `data`, `thumbnail`, `metadata`, `quality`, `mask`).  
- Media types and expected file extensions.  
- Rules for tiling, mosaics, and collection-level vs item-level assets.  
- Expectations around checksums, sizes, and integrity fields.  
- Conventions for:
  - Kansas-wide layers vs localized tiles  
  - time-bucketed collections vs continuously appended collections.

**Policy**

- All KFM spatial datasets must have a STAC representation compliant with this profile.  
- STAC is the **authoritative starting point** for any DCAT derivative or portal projection.

---

## 📚 DCAT Standards

DCAT represents the **discovery and federation** view for catalogs.

### 1. `dcat-kfm-profile.md` — KFM DCAT Profile

Defines:

- Required DCAT fields:
  - `dct:identifier`, `dct:title`, `dct:description`  
  - `dct:spatial`, `dct:temporal`  
  - `dcat:distribution`, `dcat:DataService` where applicable  
- FAIR+CARE and sovereignty alignment:
  - capturing rights, consent, and usage constraints at the dataset and distribution level  
- Relationship to STAC:
  - which STAC properties map into `dcat:Dataset` and `dcat:Distribution` fields  
  - how STAC collections show up as catalog entries.

### 2. `dcat-examples.md` — DCAT Example Library

Provides:

- Example `dcat:Dataset`/`dcat:Distribution` records derived from real KFM STAC Collections and Items.  
- JSON-LD examples for usage in portals and linked-data environments.  
- Templates for:
  - environmental datasets  
  - heritage-aware catalogs  
  - space/weather and remote-sensing catalogs.

**Policy**

- Production DCAT is **derived** from STAC using governed crosswalks.  
- Handwritten DCAT is allowed only for:
  - documentation  
  - testing / fixtures  
  and **must not** be treated as authoritative.

---

## 🔁 Crosswalks & Derivation

The **crosswalks** and derivation documents define how KFM keeps catalogs consistent.

### 1. `stac-dcat-crosswalk.md` — Canonical Crosswalk

Contains:

- Field-by-field mappings from STAC Collections / Items to DCAT Datasets / Distributions.  
- Edge cases:
  - multiple STAC assets → multiple DCAT distributions  
  - STAC events or mission tags mapped into DCAT keywords and subjects  
- Rules for:
  - handling missing or partial fields  
  - deriving default values from STAC when needed.

Examples of mappings:

- STAC `id` → DCAT `dct:identifier`  
- STAC `properties.title` → DCAT `dct:title`  
- STAC `properties.description` → DCAT `dct:description`  
- STAC `bbox` & `geometry` → DCAT `dct:spatial` (GeoJSON → GeoSPARQL / WKT)  
- STAC temporal fields → DCAT `dct:temporal`  
- STAC `assets.*.href` → DCAT `dcat:downloadURL` / `dcat:accessURL`  
- STAC `properties.license` → DCAT `dct:license`  
- STAC provenance fields → DCAT/PROV fields (`dct:source`, `prov:wasDerivedFrom`).

### 2. `stac-ckan-crosswalk.md` — Optional Portal Mapping

Documents:

- Optional projections of STAC-derived DCAT into CKAN-like schemas (if used by KFM portals).  
- Field truncation rules and limitations of the CKAN model.  
- Warnings where important provenance or FAIR+CARE fields cannot be fully represented.

### 3. `stac-dcat-derivation.md` — STAC-first → DCAT-derived

Defines the KFM **derivation standard**:

- **Authoring** happens in STAC.  
- **Derivation** uses crosswalk scripts/configs to emit DCAT JSON-LD.  
- **Validation** ensures:
  - STAC passes KFM profile checks  
  - DCAT passes KFM DCAT profile checks  
  - crosswalk metrics (coverage, mapping completeness) remain within governed thresholds.

Derivation invariants:

- No DCAT entry without a valid STAC parent.  
- Changes in STAC that affect discovery fields must be reflected in regenerated DCAT before release.  
- Crosswalk and derivation configs are versioned with this index.

---

## 📊 Telemetry, Validation & Governance

Catalog standards are enforced via CI and telemetry.

### 1. Validation

Workflows (indicative names):

- `catalog-stac-validate.yml`  
  - Runs STAC schema validation + KFM STAC profile rules.  

- `catalog-dcat-validate.yml`  
  - Validates DCAT JSON-LD against KFM DCAT profile.  

- `catalog-crosswalk-validate.yml`  
  - Executes crosswalk logic on fixture sets and checks mapping completeness.

All must be wired into `.github/workflows/kfm-ci.yml` and run for:

- changes in `docs/standards/catalogs/**`  
- changes in crosswalk / derivation tooling  
- changes to STAC/ DCAT source catalogs.

### 2. Telemetry

Telemetry records (per release):

- counts of Collections and Items with valid STAC and DCAT.  
- crosswalk success and failure counts.  
- distribution of validation error categories.  
- percentage of KFM datasets that:
  - have STAC only  
  - have STAC + DCAT  
  - are missing from catalogs and need remediation.

Stored at:

- `releases/v11.2.3/catalog-metadata-telemetry.json` (relative from repo root)  
  accessed in this document via `telemetry_ref`.

### 3. Governance

Any change to:

- the KFM STAC profile,  
- the KFM DCAT profile, or  
- the STAC ↔ DCAT crosswalk rules  

is a **governance event** and must:

- be reviewed by the Metadata & Catalogs WG and FAIR+CARE Council.  
- result in:
  - updated docs in `docs/standards/catalogs/**`  
  - updated tooling configurations  
  - a version bump in this index (and possibly dependent standards).  
- be logged into a governance ledger file (e.g., `reports/audit/governance-ledger.json`).

---

## ✅ Implementation Checklist

Before a dataset is considered **catalog-compliant** in KFM:

1. **STAC Representation**
   - [ ] Collection and Items exist for the dataset.  
   - [ ] They conform to `stac-kfm-profile.md` and `stac-best-practices.md`.  
   - [ ] STAC validation passes (schema + KFM rules).

2. **DCAT Projection**
   - [ ] DCAT is generated from STAC using approved crosswalk tooling.  
   - [ ] DCAT JSON-LD validates against `dcat-kfm-profile.md`.  
   - [ ] Any domain-specific fields are either:
     - mapped into DCAT, or  
     - explicitly documented as not mapped.

3. **Crosswalk Integrity**
   - [ ] `stac-dcat-crosswalk.md` covers all fields used in this dataset’s STAC profile.  
   - [ ] Crosswalk tests pass in CI for representative fixtures.

4. **CI Wiring**
   - [ ] STAC, DCAT, and crosswalk validation workflows are referenced from `.github/workflows/kfm-ci.yml`.  
   - [ ] Validation failures block merges to protected branches.

5. **Telemetry & Governance**
   - [ ] `catalog-metadata-telemetry.json` is updated with derived metrics.  
   - [ ] Any profile or crosswalk change is documented and approved as a governance event.

---

## 🕰️ Version History

| Version | Date       | Author                       | Summary                                                                                             |
|--------:|------------|-----------------------------|-----------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-03 | Metadata & Catalogs WG · KFM | Initial catalogs standards index; added emoji layout; codified STAC-first → DCAT-derived pattern; aligned with KFM-MDP v11.2.4 and catalog telemetry v1. |

---

<div align="center">

📚 **Kansas Frontier Matrix — Catalog & Metadata Standards Index (v11.2.3)**  
**“STAC first. DCAT derived. Provenance everywhere.”**

© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[📖 Standards Index](../README.md) · [🏛 Root Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>