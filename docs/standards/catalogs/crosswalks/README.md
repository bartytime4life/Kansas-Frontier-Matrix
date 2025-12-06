---
title: "📚 KFM v11.2.3 — Catalog Crosswalks Standards Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index for STAC ↔ DCAT and related catalog crosswalk standards in the Kansas Frontier Matrix, including mappings, edge cases, and validation rules."
path: "docs/standards/catalogs/crosswalks/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata & Catalogs · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "STAC 1.0.x → DCAT 3.0 crosswalk compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:doc:standards:catalogs:crosswalks-index:v11.2.3"
semantic_document_id: "kfm-standards-catalogs-crosswalks-index-v11.2.3"
event_source_id: "ledger:kfm:standards:catalogs:crosswalks:index:v11.2.3"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/catalog-metadata-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_kind: "Standards Index"
intent: "catalogs-crosswalks-index"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_rights_flag: false
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
sunset_policy: "Superseded by next major catalog crosswalks standards update"

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
  - "narrative-fabrication"
  - "governance-override"

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
    - "narrative-fabrication"
    - "governance-override"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🔁 Crosswalk Types"
    - "📦 STAC → DCAT Crosswalk"
    - "📦 STAC → CKAN / Portal Crosswalk"
    - "🧪 Validation & CI/CD"
    - "🧠 Focus Mode & Metadata Extraction"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

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

# 📚 **KFM v11.2.3 — Catalog Crosswalks Standards Index**  
`docs/standards/catalogs/crosswalks/README.md`

**Purpose**  
Serve as the **governed index** for all **catalog crosswalk standards** in the Kansas Frontier Matrix (KFM), with a focus on **STAC ↔ DCAT** and related patterns that keep spatial catalogs, discovery portals, and external federations **consistent, FAIR+CARE-compliant, and provenance-aligned**.

</div>

---

## 📘 Overview

This index defines how KFM documents and governs:

- **STAC → DCAT** crosswalks (KFM’s canonical pattern — STAC-first, DCAT-derived).  
- Optional **STAC → CKAN / portal** crosswalks for legacy or external systems.  
- Crosswalk documentation structure, validation rules, and CI/CD integration.  
- How crosswalk specs are used by pipelines, governance, and Focus Mode for safe, explainable metadata behavior.

It is a child of:

- `docs/standards/catalogs/README.md` — Catalog & metadata standards index.  
- `docs/standards/catalogs/stac-dcat-derivation.md` — Authoritative STAC → DCAT derivation model.

---

## 🗂️ Directory Layout

~~~text
📂 docs/standards/catalogs/
└── 📂 crosswalks/
    ├── 📄 README.md                      — ← This file (crosswalks index)
    │
    ├── 📄 stac-dcat-crosswalk.md         — STAC → DCAT field-level mapping (canonical)
    ├── 📄 stac-ckan-crosswalk.md         — Optional STAC → CKAN/portal mapping notes
    │
    └── 📂 profiles/                      — (Optional) domain-specific crosswalk profiles
        ├── 📄 stac-dcat-hydro-profile.md — Hydrology-focused crosswalk details
        └── 📄 stac-dcat-archaeo-profile.md — Archaeology / heritage-focused crosswalk details
~~~

**Directory contract**

- Every document under this tree MUST:
  - Use **KFM-MDP v11.2.4** front-matter and heading patterns.  
  - Be **machine-extractable** (tables, headings, code blocks) for crosswalk tooling.  
  - Align with `stac-dcat-derivation.md` and the catalog standards index.  
  - Respect FAIR+CARE and sovereignty requirements, especially when mapping sensitive fields.

---

## 🔁 Crosswalk Types

KFM crosswalk docs fall into three main categories:

1. **Core STAC ↔ DCAT crosswalk**  
   - Defines the **base, version-stable mapping** all pipelines must implement.  
   - Normative; used by CI, validators, and metadata tooling.

2. **Portal-oriented crosswalks**  
   - STAC → CKAN / GeoNetwork / other portal models.  
   - Non-authoritative; supported where external systems require specific fields.

3. **Domain-specific crosswalk profiles**  
   - Hydrology, archaeology, climatology, etc.  
   - Build on the core STAC ↔ DCAT mapping with domain-specific semantics (e.g., `eo:*` extensions, cultural sensitivity flags).

All crosswalks MUST:

- Declare their **source** and **target** models.  
- Describe **field-level mappings**, including type conversions and units.  
- Document **edge cases** and **lossy transformations**.  
- Provide **examples** (STAC in → DCAT/portal out).

---

## 📦 STAC → DCAT Crosswalk

The core crosswalk is fully specified in:

- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`  
- Together with the architecture and rationale in `docs/standards/catalogs/stac-dcat-derivation.md`.

**Normative KFM position**

- STAC is the **authoritative spatial and temporal metadata layer**.  
- DCAT is a **derived discovery and federation layer**, never the source of truth.  
- Crosswalk logic MUST be **deterministic** and **versioned**.

Key expectations of the `stac-dcat-crosswalk.md` standard:

- Mapping of:
  - STAC Item/Collection → `dcat:Dataset`.  
  - STAC Assets → `dcat:Distribution`.  

- Coverage of:
  - Identifiers and titles.  
  - Temporal intervals (`datetime`, `start_datetime`, `end_datetime`).  
  - Bounding boxes and spatial footprint handling.  
  - Providers, licenses, checksums, and roles.  
  - Provenance (PROV-O) and FAIR+CARE indicators.

Implementation pipelines MUST treat `stac-dcat-crosswalk.md` as **binding** for all STAC → DCAT transformations.

---

## 📦 STAC → CKAN / Portal Crosswalk

Where KFM integrates with CKAN-like portals or national data portals, the optional crosswalk is documented in:

- `docs/standards/catalogs/crosswalks/stac-ckan-crosswalk.md`.

This document SHOULD:

- Define how STAC fields map into:
  - CKAN `package` fields (e.g., `name`, `title`, `notes`, `extras`).  
  - Portal-specific metadata extensions (e.g., tags, organizations).  

- Highlight:
  - Where information may be **lost or flattened** (e.g., multi-asset Items).  
  - How to handle **spatial/temporal fields** that lack native equivalents.  
  - How to avoid exposing **sensitive fields** in public-facing portals (e.g., generalized locations for cultural sites).

KFM rule:

> Portal crosswalks MUST NOT bypass the STAC → DCAT model or weaken FAIR+CARE protections.

---

## 🧪 Validation & CI/CD

Crosswalks are enforced via CI workflows and telemetry.

### 1. Recommended CI Workflows

- `catalog-stac-validate.yml`  
  - Validates STAC Items/Collections against:
    - STAC 1.0.x schemas.  
    - KFM-STAC v11 profile.  

- `catalog-dcat-validate.yml`  
  - Validates derived DCAT JSON-LD against:
    - DCAT 3.0.  
    - KFM-DCAT v11 profile.

- `catalog-crosswalk-validate.yml`  
  - Ensures STAC ↔ DCAT consistency:
    - IDs, temporal ranges, spatial extents.  
    - License and publisher consistency.  
    - Asset/Distribution counts and checksums.

All workflows MUST emit Unified Telemetry Objects into:

- `../../../releases/v11.2.3/catalog-metadata-telemetry.json`  
  conforming to `../../../schemas/telemetry/catalog-metadata-v1.json`.

### 2. Governance Rules

- No DCAT in production without **traceable STAC provenance**.  
- Changes to crosswalk standards MUST:
  - Bump version and `last_updated`.  
  - Update this index and referenced docs.  
  - Be recorded in governance/audit logs.  
  - Pass FAIR+CARE review if they affect visibility of sensitive fields.

---

## 🧠 Focus Mode & Metadata Extraction

Crosswalk docs are used by Focus Mode and other AI tools to:

- Explain how a STAC record becomes a DCAT dataset or portal entry.  
- Clarify why a field appears (or does not appear) in an external catalog.  
- Surface potential **lossy transformations** or **generalizations** (e.g., geometry simplification, sensitive field masking).

Under this index’s AI rules:

- Focus Mode MAY:
  - Summarize crosswalk behavior.  
  - Highlight which fields map where.  
  - Explain differences between STAC, DCAT, and portal metadata.  

- Focus Mode MUST NOT:
  - Invent new crosswalk rules.  
  - Override or reinterpret normative mapping tables.  
  - Claim legal or governance authority outside of what is stated in these docs.

Crosswalk docs MUST remain:

- Plain, unambiguous, and table-driven.  
- Friendly to machine parsing (no deeply nested formatting tricks).

---

## 🕰️ Version History

| Version  | Date       | Author                                      | Summary                                                                                                 |
|----------|------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created crosswalks standards index; aligned with catalog standards index and STAC → DCAT derivation model; defined directory layout, crosswalk types, CI/governance expectations, and Focus Mode usage. |

<div align="center">

📚 **Kansas Frontier Matrix — Catalog Crosswalks Standards Index (v11.2.3)**  
STAC-first catalogs · DCAT-derived discovery · Governed crosswalks.

© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Aligned · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Catalog Standards Index](../README.md) ·  
[📦 STAC → DCAT Derivation Model](../stac-dcat-derivation.md) ·  
[⚖ Root Governance Charter](../../governance/ROOT-GOVERNANCE.md)

</div>
