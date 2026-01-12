---
title: "⚖️ Kansas Frontier Matrix — FAIR+CARE Data Governance Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/faircare.md"

version: "v13.0.0"
last_updated: "2026-01-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual + Release Gate / FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
signature_ref: "releases/v13.0.0/signature.sig"
attestation_ref: "releases/v13.0.0/slsa-attestation.json"
sbom_ref: "releases/v13.0.0/sbom.spdx.json"
manifest_ref: "releases/v13.0.0/manifest.zip"
telemetry_ref: "releases/v13.0.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/docs-faircare-v13.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
review_gates_ref: "docs/governance/REVIEW_GATES.md"
master_guide_ref: "docs/MASTER_GUIDE_v13.md"
redesign_blueprint_ref: "docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "faircare-governance"

header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "governance-faircare"
  applies_to:
    - "all-datasets"
    - "all-evidence-artifacts"
    - "all-models"
    - "all-story-nodes"
    - "focus-mode"
    - "governance-ledgers"
    - "telemetry"
    - "federated-hubs"

semantic_document_id: "kfm-doc-faircare"
doc_uuid: "urn:kfm:docs:standards:faircare-v13.0.0"
event_source_id: "ledger:kfm:doc:standards:faircare:v13.0.0"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium-Sensitivity"
sensitivity: "Governance & ethics guidance (non-PII)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
lifecycle_stage: "stable"
ttl_policy: "36 months"
sunset_policy: "None (current)"

provenance_chain:
  - "docs/standards/faircare.md@v11.0.0"
  - "docs/MASTER_GUIDE_v13.md"
  - "docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md"
  - "Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx"
  - "Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx"
  - "Audit of the Kansas Frontier Matrix (KFM) Repository.pdf"
  - "docs/standards/KFM_STAC_PROFILE.md"
  - "docs/standards/KFM_DCAT_PROFILE.md"
  - "docs/standards/KFM_PROV_PROFILE.md"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"

metadata_profiles:
  - "FAIR"
  - "CARE"
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "representation"
  - "metadata-extraction"
  - "anomaly-flagging"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-ethical-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "declassification"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - representation
    - metadata-extraction
    - anomaly-flagging
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-ethical-claims
    - narrative-fabrication
    - governance-override
    - declassification

policy_as_code:
  enabled: true
  engine: "OPA/Conftest (Policy Pack)"
  policies_path: "policies/faircare/"

json_schema_ref: "schemas/json/kfm-faircare-v13.0.0.schema.json"
shape_schema_ref: "schemas/shacl/kfm-faircare-v13.0.0-shape.ttl"
story_node_refs: []

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 FAIR Principles"
    - "🤝 CARE Principles"
    - "🧱 FAIR+CARE Metadata Requirements"
    - "🧬 FAIR+CARE Data Lifecycle"
    - "🧪 Validation & CI/CD"
    - "🔐 Governance Ledger Compliance"
    - "📖 Narrative Governance (Story Nodes & Focus Mode)"
    - "📊 Audits & Scoring"
    - "🧾 Examples"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "faircare-check"
  - "diagram-check"
  - "provenance-check"
  - "policy-pack-check"
  - "footer-check"
  - "accessibility-check"

ci_integration:
  workflow: ".github/workflows/faircare-governance.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Technical Integrity × Ethical Responsibility × Community Sovereignty"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "legacy_faircare_standard_v10"
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — FAIR+CARE Data Governance Framework (v13.0.0)**  
`docs/standards/faircare.md`

**Purpose**  
Define the **ethical, procedural, and technical governance framework** for applying  
**FAIR (Findable, Accessible, Interoperable, Reusable)** and  
**CARE (Collective Benefit, Authority to Control, Responsibility, Ethics)**  
principles across the entire Kansas Frontier Matrix (KFM) ecosystem. 🧭

This standard governs all **datasets**, **catalogs (STAC/DCAT/PROV)**, **models & simulations**, **AI pipelines**,  
**scientific workflows**, **Story Node v3 narratives**, and **Focus Mode** contexts—ensuring an integrated approach to  
open science, community sovereignty, cultural protection, and ethical AI.

[![Standard · FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Governance-gold)]() ·
[![Pipeline · Evidence-first](https://img.shields.io/badge/Pipeline-Evidence--First-0a7)]() ·
[![Catalogs · STAC/DCAT/PROV](https://img.shields.io/badge/Catalogs-STAC%2FDCAT%2FPROV-5865F2)]() ·
[![Policy-as-Code · OPA](https://img.shields.io/badge/Policy--as--Code-OPA%2FConftest-111)]() ·
[![MCP · v6.3](https://img.shields.io/badge/MCP-v6.3-blue)]()

</div>

---

## 📘 Overview

KFM is built around a **non-negotiable, evidence-first pipeline**:

> **ETL → STAC/DCAT/PROV catalogs → Graph → APIs (contracts + redaction) → UI → Story Nodes → Focus Mode**

That ordering matters because FAIR+CARE is not a “policy PDF”—it’s a **machine-enforced contract** and a **human-governed process**.

### ✅ What this standard guarantees

- **FAIR** — data is discoverable, retrievable, interoperable, and reusable via open standards (STAC/DCAT/PROV) 🌍  
- **CARE** — data about communities (especially Indigenous communities) is handled with sovereignty, protection, and benefit in mind 🪶  
- **Evidence before interpretation** — narratives and AI must be downstream of cataloged evidence (no “freeform” facts) 🧾  
- **No declassification by accident** — *no output may be less restricted than its inputs* 🔒  
- **Review gates** — sensitive domains trigger required review steps and ledger logging 🧿  
- **Auditability** — decisions, redactions, validations, and releases are recorded (ledger + telemetry + attestation) 🧾📈  

<details>
<summary><strong>🧭 Quick Index</strong> (click to expand)</summary>

- **FAIR**: persistent IDs, standardized metadata, licensing, provenance  
- **CARE**: sovereignty, review triggers, redaction/generalization, ethics  
- **Catalog alignment**: STAC/DCAT/PROV cross-linking as a hard requirement  
- **Narrative governance**: Story Nodes + Focus Mode are evidence-bound  
- **CI/CD**: schema validation + policy-as-code + release attestation  

</details>

---

## 🗂️ Directory Layout

> This reflects the **v13 repo structure** where catalogs and provenance are first-class artifacts.

~~~text
📂 KansasFrontierMatrix/
├── 📂 docs/
│   ├── 📂 standards/
│   │   ├── 📄 README.md                         # 📚 Standards index
│   │   ├── 📄 faircare.md                       # ⚖️ FAIR+CARE Governance (this file)
│   │   ├── 📄 KFM_STAC_PROFILE.md               # 🛰️ STAC profile (KFM extensions)
│   │   ├── 📄 KFM_DCAT_PROFILE.md               # 🌐 DCAT profile (KFM extensions)
│   │   ├── 📄 KFM_PROV_PROFILE.md               # 🧾 PROV profile (KFM extensions)
│   │   ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md     # 📝 Markdown authoring rules
│   │   ├── 📄 licensing.md                      # 📜 Licensing & IP standards
│   │   └── 📄 telemetry_standards.md            # 📈 Telemetry standards
│   ├── 📂 governance/
│   │   ├── 📄 ROOT_GOVERNANCE.md                # 🏛️ Root governance charter
│   │   ├── 📄 ETHICS.md                         # 🧠 Ethics baseline
│   │   ├── 📄 SOVEREIGNTY.md                    # 🪶 Sovereignty + Indigenous data protection
│   │   └── 📄 REVIEW_GATES.md                   # 🧿 Review triggers + approvals
│   ├── 📂 architecture/
│   │   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md     # 🧱 v13 redesign blueprint
│   │   └── 📂 decisions/                        # 🧾 ADRs (architecture decision records)
│   ├── 📂 templates/
│   │   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md    # 🧩 Universal doc template
│   │   └── 📄 TEMPLATE__STORY_NODE_V3.md        # 🎬 Story Node governed template
│   └── 📂 reports/
│       └── 📂 story_nodes/
│           ├── 📂 draft/                        # 📝 Under review
│           └── 📂 published/                    # ✅ Approved & published
├── 📂 data/
│   ├── 📂 raw/                                  # 📥 Ingested sources
│   ├── 📂 work/                                 # 🧪 Intermediate processing
│   ├── 📂 processed/                            # 🗃️ Final outputs (authoritative)
│   ├── 📂 stac/                                 # 🛰️ STAC collections + items
│   ├── 📂 catalog/
│   │   └── 📂 dcat/                             # 🌐 DCAT dataset discovery
│   └── 📂 prov/                                 # 🧾 PROV lineage bundles
├── 📂 schemas/                                   # 📐 JSON Schema + SHACL
├── 📂 src/                                       # 🧠 pipelines + graph + server
├── 📂 web/                                       # 🗺️ UI (React/MapLibre/optional Cesium)
├── 📂 reports/
│   └── 📂 audit/                                 # 🧾 governance-ledger + scorecards
└── 📂 releases/                                  # 📦 versioned release bundles + attestations
~~~

### ✍️ Author rules

- This file is the **root FAIR+CARE governance standard** for KFM.  
- Any domain-specific governance doc MUST:
  - live under `docs/` (typically `docs/data/<domain>/`), and  
  - explicitly link back to this standard in a **FAIR+CARE Alignment** section.  
- **No narrative** (Story Nodes, Focus Mode text, UI “explainers”) may cite uncataloged evidence.

---

## 🧭 FAIR Principles

| Principle | Meaning | KFM Implementation (evidence-first) |
|---|---|---|
| **F1 — Findable** | Persistent IDs + searchable metadata | STAC `id`, DCAT dataset identifiers, globally unique IDs, stable catalog paths |
| **F2 — Accessible** | Retrievable through standard protocols | HTTPS, Range-GET (COGs), tiered access controls at API boundary |
| **F3 — Interoperable** | Shared vocabularies / ontologies | STAC 1.0.0 + KFM extensions, DCAT 3.0 JSON-LD, PROV-O, CIDOC/Schema.org where relevant |
| **F4 — Reusable** | Clear licensing + provenance | SPDX where possible, explicit license fields, checksums, PROV lineage bundles, reproducible configs |

### 🔁 FAIR “Evidence Before Narrative” rule

FAIR in KFM includes **ordering**:

- **Catalog metadata (STAC/DCAT/PROV)** must exist *before* any downstream usage (graph/UI/story).  
- Every dataset and evidence artifact must be **traceable** (raw → work → processed, with lineage).

### ✅ FAIR CI enforcement (minimum)

- STAC validation (schema + required KFM fields)  
- DCAT validation (JSON-LD shape + required distributions)  
- PROV bundle validation (required entities/activities/agents)  
- Provenance link checks (STAC ↔ DCAT ↔ PROV ↔ graph refs)

Core outputs:

~~~text
reports/self-validation/stac_validation.json
reports/self-validation/dcat_validation.json
reports/self-validation/prov_validation.json
reports/fair/faircare_summary.json
~~~

---

## 🤝 CARE Principles

| Principle | Meaning | KFM Implementation (sovereignty-first) |
|---|---|---|
| **C1 — Collective Benefit** | Data should provide shared value | Education layers, community-informed narratives, transparent decision support |
| **C2 — Authority to Control** | Communities control data about them | CARE blocks, sovereignty policy enforcement, approvals + restrictions |
| **C3 — Responsibility** | Stewards must prevent harm | Generalization/suppression, access controls, redaction logs, audits |
| **C4 — Ethics** | Prioritize rights + context | Cultural protocols, restricted handling, narrative safeguards, review gates |

### 🧿 Governance review triggers (hard gate)

A FAIR+CARE review is required when a dataset/model/story involves or may imply:

- Indigenous communities, treaties, culturally sensitive knowledge 🪶  
- Sacred sites, burial sites, ceremonial practices (even inferred)  
- Minors, schools, family/household-level topics  
- Personal addresses, phone numbers, identifying attributes (PII)  
- Law-enforcement sensitive details or operational security  
- Any dataset labeled `restricted`, `embargoed`, or `community-controlled`

> Review gates are defined in `docs/governance/REVIEW_GATES.md` and must be logged in the ledger.

### 🛡️ Sovereignty & safety measures (non-negotiable)

- **Redaction + generalization at every layer**:  
  **catalog → graph → API → UI → narrative** (never “UI-only masking”)  
- **No declassification**: outputs cannot be less restricted than inputs  
- **Audit trails are mandatory**:
  - governance ledger entries (who/what/why/when)  
  - telemetry signals indicating user-visible redaction notices (e.g., Focus Mode)  
- **Federation-safe sharing**: when KFM interoperates with other regional hubs, the *original access level and CARE constraints must travel with the data* (no “policy drop” during replication)

---

## 🧱 FAIR+CARE Metadata Requirements

All datasets and evidence artifacts MUST carry FAIR+CARE-aligned metadata across:

- **STAC** (asset-level + spatial/temporal)  
- **DCAT** (discovery + distributions)  
- **PROV** (lineage + responsibility)  

> Profiles: `docs/standards/KFM_STAC_PROFILE.md`, `KFM_DCAT_PROFILE.md`, `KFM_PROV_PROFILE.md`

### Core metadata (minimum) ✅

~~~json
{
  "id": "kfm--<domain>--<dataset>--<version>",
  "title": "Human title",
  "description": "What this is and why it exists",
  "license": "CC-BY-4.0",
  "checksum": "sha256-...",
  "links": [
    { "rel": "self", "href": "data/stac/items/<id>.json" },
    { "rel": "derived_from", "href": "data/prov/<prov_bundle>.jsonld" }
  ]
}
~~~

### KFM access classification (required) 🔒

KFM uses an explicit access label so policy-as-code can enforce it:

- `public` — safe for open publication  
- `internal` — visible to maintainers/partners only  
- `restricted` — sensitive; requires approval workflow  
- `embargoed` — time-delayed release  
- `community-controlled` — authority-to-control external to KFM (treat as restricted unless explicitly approved)

> Exact fields and allowed values are defined in the STAC/DCAT profile extensions.

### CARE block (required when culturally/community sensitive) 🪶

~~~json
{
  "care": {
    "status": "approved | revision | restricted | rejected",
    "authority_to_control": "Tribal/Community Authority",
    "reviewer": "FAIR+CARE Council",
    "statement": "Ethical review notes (non-sensitive summary)",
    "constraints": [
      "no_precise_coordinates",
      "no_sensitive_inference",
      "no_ai_training"
    ],
    "date_reviewed": "2026-01-05"
  },
  "kfm:access_level": "restricted"
}
~~~

### Evidence artifact rule (AI/model outputs) 🧠🧪

Any derived output (simulation result, OCR corpus, AI-predicted layer, anomaly flags) is treated as a **first-class dataset**:

- stored in `data/processed/...`  
- cataloged in STAC/DCAT  
- traced in PROV  
- linked to inputs + method + parameters + uncertainty  
- gated through API (redaction + access enforcement)

Minimum additional fields:

~~~json
{
  "kfm:evidence_type": "simulation | ocr | ai_inference | analysis_output",
  "kfm:uncertainty": {
    "type": "qualitative | quantitative",
    "summary": "Confidence notes / error bounds"
  },
  "prov:wasGeneratedBy": "prov:Activity/<run_id>",
  "kfm:inputs": ["stac:item/<id1>", "stac:item/<id2>"]
}
~~~

---

## 🧬 FAIR+CARE Data Lifecycle

~~~mermaid
flowchart TD
  A["📥 Data Submission (raw)"] --> B["🧪 ETL + Normalization (work → processed)"]
  B --> C["🛰️ STAC + 🌐 DCAT + 🧾 PROV (boundary artifacts)"]
  C --> D{"🔎 FAIR checks pass?"}
  D -->|No| X["⛔ Quarantine + remediation"]
  D -->|Yes| E{"🪶 CARE review required?"}
  E -->|Yes| F["🧿 Review Gates (Council + Community)"]
  F --> G{"✅ Approved?"}
  G -->|No| X
  G -->|Yes| H["🧠 Graph references catalogs (no duplication)"]
  E -->|No| H
  H --> I["🔌 API layer (contracts + redaction)"]
  I --> J["🗺️ UI consumption (access enforced)"]
  J --> K["🎬 Story Nodes (governed narratives)"]
  K --> L["🔎 Focus Mode (evidence-linked context bundle)"]
  L --> M["📈 Telemetry + 🧾 Ledger + ✅ Attestation"]
~~~

Key stages:

1. **Submission** — raw sources registered + licensing captured  
2. **Processing** — deterministic ETL produces `data/processed/...`  
3. **Boundary artifacts** — STAC/DCAT/PROV generated (required)  
4. **FAIR validation** — schema + linkage checks  
5. **CARE gates** — triggered reviews + redaction/generalization rules  
6. **Graph/API/UI/Narrative** — downstream usage only after compliance  
7. **Telemetry/Audit** — every decision is recorded and reviewable  

---

## 🧪 Validation & CI/CD

Validation is structured as **composable gates**. Failure at any gate is a **governance event**.

| Stage | Tool / Workflow | Output |
|---|---|---|
| FAIR+CARE checks | `faircare-governance.yml` | `reports/fair/faircare_summary.json` |
| Policy-as-code | OPA/Conftest policy pack | `reports/policy/policy_decisions.json` |
| Sensitive scan | PII + sensitive-geo heuristics | `reports/security/sensitivity_scan.json` |
| STAC validation | `stac-validate.yml` | `reports/self-validation/stac_validation.json` |
| DCAT validation | `dcat-validate.yml` | `reports/self-validation/dcat_validation.json` |
| PROV validation | `prov-validate.yml` | `reports/self-validation/prov_validation.json` |
| Docs integrity | `docs-lint.yml` | `reports/self-validation/docs_lint_summary.json` |
| Release integrity | SLSA/SBOM/signature checks | `releases/<ver>/slsa-attestation.json` |

### ✅ Governance “Definition of Done” checklist

- [ ] STAC/DCAT/PROV artifacts exist and validate  
- [ ] Access level (`kfm:access_level`) set correctly  
- [ ] CARE block included when required  
- [ ] Redaction/generalization documented (if applicable)  
- [ ] Ledger entry recorded for publish/restrict decisions  
- [ ] Story Nodes (if any) reference only cataloged evidence  
- [ ] Release bundle includes SBOM + attestation + signature  

---

## 🔐 Governance Ledger Compliance

All FAIR+CARE decisions MUST be logged in a machine-readable ledger:

~~~text
reports/audit/governance-ledger.jsonl
~~~

### Example ledger entry (publish decision)

~~~json
{
  "event": "faircare_review",
  "dataset_id": "kfm--historic--hydrography--1890--v1",
  "decision": "approved",
  "access_level": "public",
  "care_required": false,
  "reviewer": "FAIR+CARE Council",
  "evidence": {
    "stac_item": "data/stac/items/kfm--historic--hydrography--1890--v1.json",
    "dcat_entry": "data/catalog/dcat/kfm--historic--hydrography--1890--v1.jsonld",
    "prov_bundle": "data/prov/kfm--historic--hydrography--1890--v1.jsonld"
  },
  "reports": {
    "faircare_summary": "reports/fair/faircare_summary.json",
    "policy_decisions": "reports/policy/policy_decisions.json"
  },
  "timestamp": "2026-01-12T00:00:00Z",
  "commit_sha": "<latest-commit-hash>"
}
~~~

### Example ledger entry (redaction applied)

~~~json
{
  "event": "redaction_applied",
  "dataset_id": "kfm--heritage--cultural-sites--1870--v2",
  "decision": "restricted",
  "access_level": "restricted",
  "care_required": true,
  "care_status": "restricted",
  "redaction": {
    "type": "spatial_generalization",
    "rule": "no_precise_coordinates",
    "method": "grid_10km + centroid_noise",
    "notes": "Generalized geometry to prevent site inference."
  },
  "timestamp": "2026-01-10T18:42:00Z"
}
~~~

---

## 📖 Narrative Governance (Story Nodes & Focus Mode)

Narratives are **governed artifacts**, not blog posts.

### 🎬 Story Nodes (governed narrative artifacts)

Story Nodes MUST:

- live under `docs/reports/story_nodes/` (`draft/` or `published/`)  
- follow `docs/templates/TEMPLATE__STORY_NODE_V3.md`  
- link every claim, image, and figure to cataloged evidence (STAC/DCAT/PROV)  
- respect `kfm:access_level` and CARE constraints

### 🔎 Focus Mode (evidence-linked context bundle)

Focus Mode MUST:

- use only provenance-linked content (no unsourced text)  
- clearly label AI-generated suggestions as suggestions  
- provide citations or catalog references for all factual claims  
- show a visible notice when content is redacted or generalized (telemetry logged)

### 🚫 Forbidden narrative content (CARE-protected)

- Precise coordinates for **sensitive cultural or sacred sites**  
- Unreviewed or speculative cultural knowledge  
- Detailed ritual/ceremonial/burial information  
- Naming communities/tribes without approval when flagged  
- Any attempt to infer restricted content from non-sensitive layers

### ✅ Required narrative safeguards

- Use generalized spatial language (“regional”, “county-level”) when CARE applies  
- Include a “CARE status” disclosure (approved/restricted) at the top of sensitive stories  
- Omit or mask content entirely when `care.status = restricted` or `access_level ≠ public`  
- Apply the rule: **no output may be less restricted than its input** 🔒

---

## 📊 Audits & Scoring

### 📆 Audit cadence

- **Quarterly**: FAIR+CARE scorecards + policy deviations  
- **Annual**: Council review of governance rules, access taxonomy, and incident summaries  

Published to:

~~~text
docs/reports/telemetry/governance_scorecard.json
reports/audit/governance-ledger.jsonl
~~~

### FAIR+CARE Composite Score (FCS v13)

~~~text
FCS = (FAIR_score * 0.7) + (CARE_score * 0.3)
~~~

Ranges:

| Score | Label | Meaning |
|---:|---|---|
| 95–100 | ✔ Excellent | Fully compliant |
| 80–94 | ⚙ Strong | Minor gaps, monitored |
| 65–79 | ⚠ Review | Publication delayed pending fix |
| <65 | 🚫 Blocked | Not eligible for release |

---

## 🧾 Examples

### Example dataset metadata (non-sensitive, v13-aligned)

~~~json
{
  "id": "kfm--historic--hydrography--1890--v1",
  "title": "Historic Hydrography of Kansas (1890)",
  "description": "Digitized hydrography layer compiled from archival sources.",
  "license": "Public Domain",
  "checksum": "sha256-aaaabbbbcccc",
  "kfm:access_level": "public",
  "care": {
    "status": "approved",
    "reviewer": "FAIR+CARE Council",
    "statement": "No cultural sensitivity identified.",
    "date_reviewed": "2026-01-05"
  },
  "prov:wasGeneratedBy": "prov:Activity/digitization_pipeline_v3.2",
  "links": [
    { "rel": "stac_item", "href": "data/stac/items/kfm--historic--hydrography--1890--v1.json" },
    { "rel": "dcat_dataset", "href": "data/catalog/dcat/kfm--historic--hydrography--1890--v1.jsonld" },
    { "rel": "prov_bundle", "href": "data/prov/kfm--historic--hydrography--1890--v1.jsonld" }
  ]
}
~~~

### Example dataset metadata (culturally sensitive → restricted)

~~~json
{
  "id": "kfm--heritage--cultural-sites--1870--v2",
  "title": "Documented Cultural Sites in Kansas (circa 1870) — Generalized",
  "description": "Sensitive heritage locations generalized to prevent inference. Restricted access.",
  "license": "CC-BY-4.0",
  "checksum": "sha256-ddddeeeeffff",
  "kfm:access_level": "restricted",
  "care": {
    "status": "restricted",
    "authority_to_control": "Example Tribal Nation",
    "reviewer": "FAIR+CARE Council",
    "statement": "Contains culturally sensitive location information. Restricted to approved research contexts.",
    "constraints": ["no_precise_coordinates", "no_ai_training"],
    "date_reviewed": "2026-01-10"
  },
  "prov:wasGeneratedBy": "prov:Activity/heritage_mapping_pipeline_v2.1"
}
~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---:|---|---|---|
| v13.0.0 | 2026-01-12 | KFM Governance Council | Aligned governance with v13 evidence-first pipeline: catalogs-before-narrative, review gates, policy-as-code, redaction-at-every-layer, updated directory structure for Story Nodes + catalogs. |
| v11.0.0 | 2025-11-20 | KFM Governance Council | Upgraded FAIR+CARE framework for KFM v11; added ontology mappings, narrative governance rules, telemetry integration, and protocol alignment. |
| v10.2.2 | 2025-11-12 | A. Barta | Updated SBOM/manifest references; added DCAT and STAC alignment; extended composite FAIR+CARE scoring. |
| v10.0.0 | 2025-11-10 | A. Barta | Major improvements; added telemetry and governance ledger integration; clarified CARE review flows. |

---

<div align="center">

⚖️ **Kansas Frontier Matrix — FAIR+CARE Governance Framework (v13.0.0)**  
“Technical integrity × Ethical responsibility × Community sovereignty.”

© 2026 Kansas Frontier Matrix — CC-BY 4.0  
Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Standards Index](README.md) ·  
[🏛 Root Governance Charter](../governance/ROOT_GOVERNANCE.md) ·  
[🧠 Ethics](../governance/ETHICS.md) ·  
[🪶 Sovereignty](../governance/SOVEREIGNTY.md) ·  
[🧿 Review Gates](../governance/REVIEW_GATES.md) ·  
[🛰️ STAC Profile](KFM_STAC_PROFILE.md) ·  
[📜 Licensing Standard](licensing.md)

</div>
