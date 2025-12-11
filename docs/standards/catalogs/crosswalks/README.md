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

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/catalog-metadata-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/catalog-metadata-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

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

json_schema_ref: "../../../../schemas/json/catalogs-crosswalks-index-v1.json"
shape_schema_ref: "../../../../schemas/shacl/catalogs-crosswalks-index-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

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
- Domain-specific crosswalk profiles that extend the core mappings.  
- Crosswalk documentation structure, validation rules, and CI/CD integration.  

It is a child of:

- `docs/standards/catalogs/README.md` — catalog & metadata standards index.  
- `docs/standards/catalogs/stac-dcat-derivation.md` — authoritative STAC → DCAT derivation model.

Crosswalk docs under this tree are **normative** for KFM pipelines: if a pipeline maps between catalog models, it must implement one of the governed crosswalk standards defined here.

---

## 🗂️ Directory Layout

~~~text
📁 Kansas-Frontier-Matrix/
└── 📁 docs/
    └── 📁 standards/
        └── 📁 catalogs/
            ├── 📄 README.md                       📚 Catalog & metadata standards index
            ├── 📦 stac-dcat-derivation.md         📦 STAC → DCAT derivation model
            │
            └── 📁 crosswalks/                     🔀 Catalog crosswalk standards subtree
                ├── 📄 README.md                    📚 This file (crosswalks index)
                │
                ├── 📄 stac-dcat-crosswalk.md       📦 STAC → DCAT field-level mapping (canonical)
                ├── 📄 stac-ckan-crosswalk.md       📦 Optional STAC → CKAN / portal mapping notes
                │
                └── 📁 profiles/                    🧩 Domain-specific crosswalk profiles
                    ├── 📄 stac-dcat-hydro-profile.md    💧 Hydrology-focused crosswalk profile
                    └── 📄 stac-dcat-archaeo-profile.md  🏺 Archaeology / heritage crosswalk profile
~~~

**Directory contract**

- Every document under `docs/standards/catalogs/crosswalks/` MUST:
  - follow **KFM-MDP v11.2.4** front-matter and heading conventions  
  - be **machine-extractable** (clear tables and code blocks)  
  - declare its source and target models (e.g., “STAC → DCAT v3”)  
  - align with the STAC-first, DCAT-derived model in `stac-dcat-derivation.md`  
  - respect FAIR+CARE and sovereignty rules, especially for sensitive domains (e.g., heritage)

---

## 🔁 Crosswalk Types

KFM catalog crosswalks fall into three main categories:

1. **Core STAC ↔ DCAT crosswalk**  
   - Defines the **base, version-stable mapping** required for all KFM catalogs.  
   - Normative and enforced by CI and metadata tooling.  

2. **Portal-oriented crosswalks (STAC → CKAN / other)**  
   - Used to integrate with CKAN-like or national portals that rely on specific schemas.  
   - Non-authoritative, but must not contradict core STAC ↔ DCAT semantics.  

3. **Domain-specific crosswalk profiles**  
   - Hydrology, archaeology/heritage, atmospheric science, etc.  
   - Extend the core crosswalk with domain-specific fields and constraints.  

All crosswalk docs MUST:

- Specify:
  - source model and version (e.g., STAC 1.0.0 + KFM-STAC v11 profile)  
  - target model and version (e.g., DCAT 3.0 + KFM-DCAT v11 profile)  
- Describe:
  - field-level mappings (including type/unit conversions)  
  - edge cases and lossy transformations  
  - required and optional fields on both sides  
- Include:
  - worked examples (STAC in → derivation out)  
  - notes on FAIR+CARE and sovereignty impacts where applicable  

---

## 📦 STAC → DCAT Crosswalk

The **canonical STAC → DCAT crosswalk** is defined in:

- `docs/standards/catalogs/crosswalks/stac-dcat-crosswalk.md`

and is paired with the architectural model in:

- `docs/standards/catalogs/stac-dcat-derivation.md`

**KFM position**

- STAC is the **authoritative spatial/temporal metadata layer**.  
- DCAT is a **derived discovery and federation layer**, never the source of truth.  
- The STAC → DCAT crosswalk is **binding** for all KFM catalog pipelines.

The `stac-dcat-crosswalk.md` standard MUST:

- Cover mappings from:
  - STAC Collections/Items → `dcat:Dataset`  
  - STAC Assets → `dcat:Distribution`  

- Address:
  - identifiers (`id` → `dct:identifier`)  
  - titles and descriptions  
  - spatial footprint (`bbox`, `geometry` → `dct:spatial`)  
  - temporal intervals (`datetime`, `start_datetime`, `end_datetime` → `dct:temporal`)  
  - providers, licenses, and rights  
  - keywords, mission tags, and KFM `kfm:*` properties  
  - provenance and derivation (`dct:source`, `prov:wasDerivedFrom`)  

Pipelines implementing STAC → DCAT transformations MUST be traceable back to this crosswalk.

---

## 📦 STAC → CKAN / Portal Crosswalk

For CKAN-like or external portal integrations, the optional crosswalk is documented in:

- `docs/standards/catalogs/crosswalks/stac-ckan-crosswalk.md`

This document SHOULD describe:

- Field mappings from STAC (and/or DCAT) into:
  - CKAN `package`-level fields (`name`, `title`, `notes`, `tags`, `extras`, etc.)  
  - portal-specific organizational and access metadata  

- Handling of:
  - spatial/temporal fields where portal support is limited  
  - multi-asset Items that must be flattened into portal concepts  
  - sensitive fields that must be masked, generalized, or omitted (e.g., heritage locations)

KFM rule:

> Portal crosswalks MUST NOT bypass STAC → DCAT governance or weaken FAIR+CARE protections.

Portal crosswalks are **adapters** on top of the STAC-first, DCAT-derived architecture; they do not redefine authoritative metadata.

---

## 🧪 Validation & CI/CD

Crosswalk standards are enforced via CI, schemas, and telemetry.

### 1. CI Workflows

Recommended workflows:

- `catalog-stac-validate.yml`  
  - Validates STAC against STAC 1.0.x and KFM-STAC v11.  

- `catalog-dcat-validate.yml`  
  - Validates derived DCAT JSON-LD against DCAT 3.0 and KFM-DCAT v11.  

- `catalog-crosswalk-validate.yml`  
  - Applies crosswalk logic to fixture STAC/portal inputs and asserts:
    - identifier consistency  
    - temporal/spatial consistency  
    - license and publisher consistency  
    - asset/distribution count checks  

All workflows MUST run as part of:

- `.github/workflows/kfm-ci.yml`  
- the `dev → staging → production` promotion pipeline.

### 2. Telemetry

Crosswalk-related telemetry (referenced via `telemetry_ref`) SHOULD include:

- counts of STAC records evaluated  
- counts of DCAT (and optional portal) records generated  
- mapping coverage statistics (e.g., fields mapped vs ignored)  
- error and warning categories over time  

Telemetry MUST conform to:

- `catalog-metadata-telemetry.json` schema (`catalog-metadata-v1.json`)  
- KFM energy/carbon schemas for crosswalk-heavy workflows.

### 3. Governance

Any changes to:

- the core STAC ↔ DCAT crosswalk  
- portal crosswalk definitions  
- domain-specific crosswalk profiles  

MUST:

- bump version and `last_updated` in the changed docs  
- update this index if new crosswalks or profiles are added/removed  
- record changes in governance/audit logs  
- pass FAIR+CARE review when they affect visibility of sensitive information.

---

## 🧠 Focus Mode & Metadata Extraction

Crosswalk docs are **first-class inputs** for Focus Mode and other AI tooling.

Under this index’s AI rules:

- Focus Mode MAY:
  - summarize crosswalk behavior and mapping rules  
  - highlight where data may be generalized, flattened, or dropped  
  - generate **explanations** for why specific DCAT or portal fields appear (or do not appear)  

- Focus Mode MUST NOT:
  - invent crosswalk rules that are not present in these docs  
  - override, contradict, or “fix” crosswalk tables autonomously  
  - claim governance authority beyond what is explicitly encoded here  

Authors SHOULD:

- keep crosswalk sections table-driven and stable  
- use clear headings and short, structured lists so extraction is deterministic  
- annotate lossy transforms and FAIR+CARE impacts explicitly to aid interpretability.

---

## 🕰️ Version History

| Version | Date       | Author                                      | Summary                                                                                                 |
|--------:|------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-03 | Metadata & Catalogs WG · FAIR+CARE Council | Created catalog crosswalks standards index; aligned with catalog standards index and STAC → DCAT derivation model; defined directory layout, crosswalk types, CI/governance expectations, and Focus Mode usage. |

---

<sub>© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.4</sub>

<br/>

<div align="center">

📚 **KFM v11.2.3 — Catalog Crosswalks Standards Index**  
STAC-First Catalogs · DCAT-Derived Discovery · Governed Crosswalks  

[📚 Catalog Standards Index](../README.md) · [📦 STAC → DCAT Derivation](../stac-dcat-derivation.md) · [⚖ Governance Charter](../../governance/ROOT-GOVERNANCE.md)

</div>