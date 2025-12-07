---
title: "⚖️ Kansas Frontier Matrix — Historical Methods Governance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/analyses/historical/methods/governance.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Historical Governance Working Group"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Methods Governance Guide"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/analyses-historical-methods-governance-v1.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "Public · High-Sensitivity Historical & Cultural"
sensitivity: "High (culturally sensitive and sovereignty-linked methods and outputs possible)"
sensitivity_level: "High"
public_exposure_risk: "Moderate"
classification: "Internal / Methods-Governance"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Historical Team · FAIR+CARE Council · Historical Governance Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - version: "v11.2.4"
    date: "2025-12-07"
    activity: "Initial Historical Methods Governance guide; aligned with Historical Methods README, Historical Governance, KFM-MDP v11.2.4, and CI/lineage standards."
    is_root: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "a11y-adaptations"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - diagram-extraction
    - metadata-extraction
    - a11y-adaptations
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override
---

<div align="center">

# ⚖️ **Kansas Frontier Matrix — Historical Methods Governance**  
`docs/analyses/historical/methods/governance.md`

**Purpose**  
Define the **governance, approval, and risk framework** for all **historical methods** in the Kansas Frontier Matrix (KFM) — including archival correlation, population dynamics, and cultural landscape analysis — so that:

- Methods are **reviewed, versioned, and ethically constrained** before use.  
- Pipelines and Story Nodes **declare which methods they implement**.  
- Historical methods remain **FAIR+CARE-aligned, sovereignty-respecting, and PROV-traceable** across the entire KFM stack.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../README.md)  
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Historical_Methods-orange)](../../../standards/faircare.md)  
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](../../../../releases/)

</div>

---

## 📘 Overview

This document governs **how methods themselves** (not just datasets) are:

- Proposed and designed.  
- Reviewed for **ethical, historical, and sovereignty implications**.  
- Linked to **pipelines, datasets, and Story Nodes**.  
- Maintained, versioned, and decommissioned.

It complements:

- `docs/analyses/historical/README.md` – domain overview.  
- `docs/analyses/historical/governance.md` – data & narrative governance.  
- `docs/analyses/historical/methods/README.md` – methods index.  
- `docs/analyses/historical/validation.md` – validation framework.

In short: this file answers **“What does it mean for a historical method to be allowed and in good standing?”**

---

## 🗂️ Directory Layout

Governance for historical methods is embedded in the following structure:

```text
📁 Kansas-Frontier-Matrix/
├── 📁 docs/
│   └── 📁 analyses/
│       └── 📁 historical/
│           ├── 📄 README.md                         # Historical Analyses Overview
│           ├── 📄 governance.md                     # Historical data & narrative governance
│           ├── 📄 validation.md                     # Historical validation & CI rules
│           ├── 📁 methods/
│           │   ├── 📄 README.md                     # Methods index (this directory's entrypoint)
│           │   ├── 📄 governance.md                 # This methods governance guide
│           │   ├── 📄 archival-correlation.md       # Archival correlation methods
│           │   ├── 📄 population-dynamics.md        # Demography & migration methods
│           │   └── 📄 cultural-landscapes.md        # Cultural & environmental landscape methods
│           └── 📁 datasets/
│               └── 📄 risk-register.json            # Dataset-level risk & governance registry
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 historical/
│           ├── 📄 archival_pipeline.py              # Implements archival methods (governed here)
│           ├── 📄 population_pipeline.py            # Implements population methods
│           ├── 📄 landscapes_pipeline.py            # Implements landscape methods
│           └── 📄 config_historical.yml             # Method + dataset selection, parameters
└── 📁 dist/
    └── 📁 historical/
        ├── 📁 provenance/                           # PROV-O bundles for historical pipelines
        └── 📁 validation/                           # Validation reports for methods/datasets
```

**Directory-level governance rules:**

- Every method doc under `docs/analyses/historical/methods/` is treated as a **governed method spec** (CIDOC E29 / PROV `prov:Plan`).  
- Pipelines in `src/pipelines/historical/` **must** reference one or more governed methods by doc path or `method_id`.  
- Method governance decisions (e.g., “not approved for sovereign data”) **must** be documented here and reflected in:
  - Pipeline configs (`config_historical.yml`).  
  - STAC/DCAT metadata for datasets generated using that method.  
  - Story Node metadata for narratives built on those methods.

---

## 🧭 Context

Historical methods can introduce risk even when datasets are individually permitted. Examples:

- Aggregating multiple low-risk datasets into a **sensitive inference** about a community.  
- Applying methods that **overstate certainty** or **erase alternative interpretations**.  
- Generating outputs that **reveal patterns** (e.g., persecution, land loss) in ways that communities request be contextualized or constrained.

This governance guide sits **between**:

- **Data governance** (`../governance.md`) — what data is allowed and how it must be generalized.  
- **Validation** (`../validation.md`) — what tests must pass before results are accepted.  

It focuses on:

- **Method approval & lifecycle** – when a method is allowed, experimental, or deprecated.  
- **Sovereignty & ethics for methods** – which methods are barred or restricted for certain datasets.  
- **Mapping methods to provenance** – linking methods to OpenLineage runs, PROV bundles, and catalog metadata.

---

## 🧱 Architecture

### 🧩 Method Governance Flow

```mermaid
flowchart LR
    A["Method Proposal\n(New or Revised)"]
        --> B["Preliminary Review\nHistorical Team"]
    B --> C{"Risk / Sovereignty Impact?"}
    C -->|High| D["Deep Review\nFAIR+CARE Council · Sovereignty Board"]
    C -->|Low/Moderate| E["Standard Review\nHistorical Governance WG"]
    D --> F["Governance Decision\nApprove · Conditional · Reject"]
    E --> F
    F --> G["Update Method Doc\n& Methods Index"]
    G --> H["Update Pipelines & Configs\nsrc/pipelines/historical/*"]
    H --> I["Update Catalog & PROV\nSTAC/DCAT · PROV-O · OpenLineage"]
```

### 🧬 Method States

Each historical method must be tagged with one of:

- **`approved`** – may be used in production pipelines and Story Nodes, subject to dataset-level governance.  
- **`approved-conditional`** – may be used only with specified constraints (e.g., **aggregated outputs only**, **no coordinate-level display**).  
- **`experimental`** – allowed in research branches and internal experiments; not surfaced via public Story Nodes without explicit review.  
- **`deprecated`** – not recommended for new analyses; may exist for legacy compatibility, but must not underpin new Story Nodes.  
- **`rejected`** – must not be used in any production or public context; kept only for archival reasons, if at all.

These states should be recorded:

- In each method doc’s front-matter (`method_status`, if present) or  
- In a shared **method registry** (see below), and  
- In pipeline configs indicating which methods are runnable in which environments (dev / staging / production).

---

## 📦 Data & Metadata

### 🧾 Method Registry (Conceptual)

Alongside this Markdown guide, KFM should maintain a machine-readable **method registry**, e.g.:

- `docs/analyses/historical/methods/method-registry.json`

Each method entry might include:

```json
{
  "method_id": "hist-archival-correlation-v1",
  "doc_path": "docs/analyses/historical/methods/archival-correlation.md@v11.2.4",
  "status": "approved-conditional",
  "allowed_risk_tiers": [0, 1, 2],
  "sovereignty_constraints": "requires-sovereignty-review-for-tier-2",
  "notes": "Can be applied to treaty and land cession datasets only with H3 generalization and donut masking.",
  "approving_body": "Historical Governance WG · Sovereignty Board",
  "decision_timestamp": "2025-12-06T22:30:00Z"
}
```

Pipelines, catalogs, and Story Nodes can query this registry to ensure that their method usage is **legitimate and in-bounds**.

---

## 🌐 STAC, DCAT & PROV Alignment

Methods governance must be visible in catalogs and provenance.

### STAC

Historical STAC Items that implement governed methods should include:

```json
{
  "kfm:method_id": "hist-archival-correlation-v1",
  "kfm:method_doc": "docs/analyses/historical/methods/archival-correlation.md@v11.2.4",
  "kfm:method_status": "approved-conditional"
}
```

These properties:

- Allow users and tools to see **which methods shaped which datasets**.  
- Help Focus Mode explain **how** historical outputs were generated.  
- Provide quick checks to ensure deprecated or rejected methods are not active in current catalogs.

### DCAT

In DCAT:

- `dct:conformsTo` can point to method docs or this governance guide.  
- `dct:provenance` can link to PROV bundles that include the method’s `prov:Plan`.

### PROV-O

In PROV:

- Each governed method is modeled as a `prov:Plan`.  
- Each pipeline run is a `prov:Activity` that:
  - `prov:used` the method plan.  
  - `prov:generated` historical datasets or Story Node bundles.  

Governance decisions can be represented as PROV entities and activities:

- Decision records as `prov:Entity`.  
- Review meetings as `prov:Activity`.  
- Councils and boards as `prov:Agent`.

---

## 🧠 Story Node, AI & Focus Mode Integration

Methods governance shapes **how narratives and AI transforms** are permitted to use methods.

### Story Nodes

Story Nodes must declare:

- Which method(s) they rely on (`method_id` or doc path).  
- Any constraints applied (e.g., **spatial generalization**, **aggregation**, **redaction of names**).

Story Nodes are **not allowed** to:

- Imply that experimental or rejected methods are authoritative.  
- Present method-driven inferences as direct archival “facts.”  
- Ignore conditions like “aggregated-only” or “don’t display certain place-names.”

Example Story Node metadata fragment:

```json
{
  "method_ids": ["hist-archival-correlation-v1", "hist-population-dynamics-v2"],
  "method_governance_ref": "docs/analyses/historical/methods/governance.md@v11.2.4"
}
```

### AI Transform Governance

Per front-matter:

- **Allowed transforms (Focus Mode / AI):**
  - `summary`, `timeline-generation`, `semantic-highlighting`,  
  - `diagram-extraction`, `metadata-extraction`, `a11y-adaptations`.

- **Prohibited transforms:**
  - `content-alteration`, `speculative-additions`,  
  - `unverified-architectural-claims`, `narrative-fabrication`,  
  - `governance-override`.

AI systems:

- May **summarize**, index, or adapt content for accessibility.  
- Must **not change** normative governance text, invent new policy, or reinterpret methods as more permissive than documented.  
- Must defer to this document and associated standards (`governance_ref`, `ethics_ref`, `sovereignty_policy`) as the **source of truth**.

---

## 🧪 Validation & CI/CD

Method governance is enforced via CI alongside historical validation.

### CI Responsibilities

A dedicated workflow (e.g., `.github/workflows/historical-methods-governance.yml`) must:

- Validate that **all method IDs** referenced in:
  - Pipelines (`src/pipelines/historical/*`).  
  - STAC/DCAT metadata (`data/stac/historical/**`).  
  - Story Node bundles (`dist/historical/storynode/**`).  
  correspond to entries in the method registry and/or real docs.

- Check that:
  - `status` of methods is compatible with the target environment (e.g., `experimental` methods not used in production).  
  - `allowed_risk_tiers` intersect correctly with datasets’ risk tiers from `risk-register.json`.  
  - Sovereignty constraints are respected for high-sensitivity datasets (`indigenous_rights_flag: true`).

### CI Gate Examples

- **Block merge** if:
  - A pipeline uses a `method_id` with `status = "rejected"`.  
  - A Story Node uses a method **not present** in the registry.  
  - A `approved-conditional` method is used with incompatible risk tiers or without required masking/generalization.

- **Require human approval** (FAIR+CARE Council or Sovereignty Board) if:
  - New methods are introduced with `status = "approved-conditional"`.  
  - Existing methods change status (e.g., `approved` → `experimental` or `deprecated`) while still underpinning active datasets/Story Nodes.

Validation results and governance warnings related to methods should be written into:

- `dist/historical/validation/validation-<sha>.json`, and  
- Telemetry artifacts referenced by `telemetry_ref`.

---

## ⚖ FAIR+CARE & Governance

This methods governance document applies FAIR+CARE to **how** historical analyses are done, not just **what** data they use.

### FAIR

- **Findable** – Methods are discoverable via:
  - This governance guide,  
  - The methods index, and  
  - STAC/DCAT `kfm:method_id` fields.

- **Accessible** – Method docs are CC-BY licensed and available in the repo.

- **Interoperable** – Methods are aligned with:
  - CIDOC CRM, PROV-O, DCAT, STAC, OWL-Time, and GeoSPARQL,  
  - Internal ontologies defined in KFM-OP v11.

- **Reusable** – Governance constraints, assumptions, and caveats are explicitly documented, allowing others to safely reuse or audit methods.

### CARE

- **Collective Benefit**  
  Methods are prioritized when they support community goals (heritage, education, resilience) rather than only technical novelty.

- **Authority to Control**  
  For methods impacting Indigenous or sovereignty-linked data:
  - Sovereignty Board and Indigenous partners must review and approve.  
  - Conditions (e.g., minimum generalization) are binding.

- **Responsibility**  
  Method authors must:
  - Document potential harms, biases, and limits.  
  - Propose mitigations and alternatives when risks are high.

- **Ethics**  
  Methods that inherently sensationalize, decontextualize, or erase marginalized perspectives can be **rejected outright**, regardless of technical sophistication.

If a method cannot be reconciled with FAIR+CARE or sovereignty policies, it must be:

- Marked `rejected` or kept `experimental` and blocked from production.  
- Clearly labeled in:
  - Its method doc,  
  - The method registry, and  
  - Any pipeline configs in which it appears.

---

## 🕰️ Version History

| Version   | Date       | Author / Steward                              | Summary                                                                                                 |
|----------:|-----------:|-----------------------------------------------|---------------------------------------------------------------------------------------------------------|
| v11.2.4   | 2025-12-07 | FAIR+CARE Council · Historical Governance WG | Initial Historical Methods Governance guide; aligned with KFM-MDP v11.2.4, Historical Methods README, Historical Governance, and CI/lineage standards; defined method lifecycle, registry structure, STAC/DCAT/PROV mappings, AI/Focus Mode constraints, and CI enforcement. |

---

<div align="center">

⚖️ **Kansas Frontier Matrix — Historical Methods Governance**  
Scientific Insight · FAIR+CARE · Sovereignty-Respecting · CI-Enforced  

[📜 Historical Methods Index](./README.md) · [⚖ Historical Governance (Domain)](../governance.md) · [✅ Historical Validation](../validation.md) · [📘 Markdown Protocol v11.2.4](../../../standards/kfm_markdown_protocol_v11.2.4.md)

</div>
