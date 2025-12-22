---
title: "MCP SOPs — README"
path: "mcp/sops/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:mcp:sops:readme:v1.0.0"
semantic_document_id: "kfm-mcp-sops-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:mcp:sops:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# MCP SOPs — README

## 📘 Overview

### Purpose
This README defines how to create, review, and maintain **Standard Operating Procedures (SOPs)** under `mcp/sops/` so that recurring workflows are **repeatable, auditable, and architecture-synced**.

SOPs are MCP evidence products: step-by-step guides for recurring tasks that help contributors replicate processes consistently and correctly. Each SOP should include (at minimum) **Purpose, Tools Needed or Prerequisites, Steps or Procedure, Verification or Expected Outcome, and Troubleshooting or Notes**.

### Scope
**In scope**
- Repeatable procedures for tasks that touch the KFM pipeline: ingestion and ETL, catalog generation, graph updates, API boundary work, UI layer updates, Story Node publication flows, and operational verification.
- “How to” documentation that must be reproducible and safe to run.

**Out of scope**
- API contract definitions (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`).
- Narrative content intended for end users (use Story Node templates under `docs/reports/story_nodes/`).

### Audience
- Contributors performing operational work (DataOps, GraphOps, API/UI maintainers, curators).
- Reviewers validating reproducibility, governance compliance, and downstream integrity.

### Definitions
- Glossary: `docs/glossary.md`
- **SOP**: A step-by-step guide for a recurring task (runbook-quality, reproducible).
- **MCP**: “Master Coder Protocol” evidence and documentation products (experiments, model cards, SOPs).
- **Run manifest**: A recorded, repeatable run description tying inputs → outputs (often paired with PROV).

### Key artifacts
| Artifact | Location | Purpose | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + invariants | Source of truth for stage boundaries |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Default template for governed Markdown docs | Use unless a dedicated SOP template exists |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative artifacts for Focus Mode | Story Nodes must be provenance-linked |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Review gates + governance rules | Follow for sensitive content + redaction |
| This index | `mcp/sops/README.md` | SOP entrypoint + conventions | Keep updated when SOPs are added |

### Definition of done
A new SOP is “done” when:
- [ ] It lives under `mcp/sops/` and its front-matter `path:` matches the file path.
- [ ] It declares which pipeline stage(s) it affects and respects canonical ordering.
- [ ] It lists prerequisites (tools, access, environment assumptions, versions).
- [ ] It provides step-by-step procedure that is deterministic where possible.
- [ ] It specifies inputs, outputs, and where outputs must be placed (`data/`, `schemas/`, `src/`, `web/`, etc.).
- [ ] It includes verification checks and explicit success criteria.
- [ ] It includes troubleshooting notes for common failure modes.
- [ ] This README’s SOP index is updated with a link and basic metadata.

---

## 🗂️ Directory Layout

### This document
- `path`: `mcp/sops/README.md` (must match front-matter)

### Related repository paths
| Area | Canonical path | What it is |
|---|---|---|
| MCP SOPs | `mcp/sops/` | This SOP library |
| MCP experiments | `mcp/experiments/` | Experiment reports / logs (if present) |
| MCP model cards | `mcp/model_cards/` | Model documentation (if present) |
| Data staging | `data/raw/`, `data/work/`, `data/processed/` | Source → work → derived outputs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV artifacts |
| Pipelines | `src/pipelines/` | Deterministic ETL / transforms |
| Graph | `src/graph/` | Ontology, ingest, migrations |
| API boundary | `src/server/` | REST/GraphQL contracts + redaction layer |
| UI | `web/` | Map layers + Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts + assets |
| Schemas | `schemas/` | JSON Schema / validation contracts |
| Tests | `tests/` | Validation + regression checks |

### Expected file tree for this sub-area
~~~text
📁 mcp/
└── 📁 sops/
    ├── 📄 README.md
    ├── 📄 <sop_name>.md
    ├── 📄 <sop_name>__v2.md
    └── 📁 assets/
        └── 🖼️ <optional_screenshots_or_diagrams>.png
~~~

### SOP index
Add each SOP here as it lands.

| SOP | Pipeline stage(s) | Status | Notes |
|---|---|---|---|
| _No SOPs indexed yet_ | — | — | Add first SOP and update this table |

### Authoring workflow
1. Create a new file under `mcp/sops/` (use `snake_case` names, short but specific).
2. Start from the **Universal Doc Template** and adjust values for `title`, `path`, `doc_uuid`, and `semantic_document_id`.
3. In the SOP body:
   - State what stage(s) you are touching.
   - List prerequisites (tools + versions, access, required datasets).
   - Provide the procedure steps.
   - Provide verification and troubleshooting.
4. If the SOP changes catalogs, graph, API contracts, or UI layer registry, link the relevant artifacts and include validation steps.
5. Update the SOP index table in this README.

### Required SOP content and where it belongs
SOPs should include the following concepts; the recommended mapping to the Universal Doc structure is:

| SOP requirement | Recommended location in Universal Doc | Notes |
|---|---|---|
| Purpose | `## 📘 Overview → Purpose` | What problem this SOP solves |
| Tools Needed / Prerequisites | `## 🧭 Context → Assumptions` and/or `## ✅ Validation & CI/CD → Reproduction` | Include versions and environment assumptions |
| Steps / Procedure | `## ✅ Validation & CI/CD → Reproduction` | Prefer idempotent steps; use explicit paths |
| Expected outcome | `## 📦 Data & Metadata → Outputs` + `## ✅ Validation & CI/CD → Validation steps` | Define success criteria |
| Verification | `## ✅ Validation & CI/CD → Validation steps` | Include concrete checks |
| Troubleshooting / Notes | `## ✅ Validation & CI/CD` (add a Troubleshooting subsection) | Document common failure modes |

---

## 🧭 Context

### Background
MCP SOPs exist to ensure recurring workflows remain reproducible and consistent across contributors. SOPs are particularly important when a task has multiple interdependent steps across the pipeline, or when mistakes could create downstream integrity issues.

### Assumptions
- The canonical KFM pipeline ordering is followed when writing and executing SOPs.
- Outputs are placed in the correct canonical homes (data vs code vs docs) and are schema-validated where applicable.
- SOP steps are written to be verifiable (someone else can run them and confirm success).

### Constraints and invariants
- Maintain canonical ordering: ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode.
- No unsourced narrative for end-user contexts (Story Nodes / Focus Mode).
- Provenance is first-class: if the SOP produces an evidence artifact, it must be traceable via catalog + lineage.
- Do not place derived datasets under `src/`; derived outputs belong under `data/processed/` and related catalog roots.
- Do not include credentials, tokens, secrets, or personally identifying information in SOPs.
- For culturally sensitive content or precise locations requiring protection, follow sovereignty and redaction rules.

### Open questions
| Question | Owner | Notes |
|---|---|---|
| Do we want a dedicated SOP template file under `docs/templates/` | TBD | Currently using Universal Doc template |
| Should SOP index be generated automatically | TBD | Could be a CI doc check in future |

### Future extensions
- Add a linter or CI step that validates:
  - front-matter `path` matches file path
  - internal links resolve
  - required SOP sections exist
  - sensitive strings are not present

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["SOP author / contributor"] --> B["SOP in mcp/sops"]
  B --> C["ETL and transforms"]
  C --> D["STAC/DCAT/PROV catalogs"]
  D --> E["Neo4j graph build"]
  E --> F["API boundary"]
  F --> G["Map and Focus Mode UI"]
  G --> H["Story Nodes"]
~~~

---

## 📦 Data & Metadata

This README is documentation-only. However, SOPs must explicitly document inputs and outputs so that procedures can be reproduced safely.

### Inputs
For each SOP, include a table like:

| Input | Expected location | Format | Sensitivity | Validation | Notes |
|---|---|---|---|---|---|
| Example: raw source map scan | `data/raw/<domain>/...` | TIFF / PDF | public / restricted | checksum, metadata completeness | cite source URL in catalog docs |

### Outputs
For each SOP, include a table like:

| Output | Expected location | Format | Validation | Downstream consumer | Notes |
|---|---|---|---|---|---|
| Example: processed raster | `data/processed/<domain>/...` | COG | gdalinfo checks, projection | STAC + UI tiles | record processing parameters |

### Sensitivity and redaction
SOPs must state whether their procedure touches:
- Sensitive locations (precise coordinates).
- Culturally sensitive datasets or materials requiring sovereignty review.
- Restricted or licensed materials.

If sensitivity is present, the SOP must document redaction/generalization rules and required reviews.

### Quality signals
SOPs should describe:
- Schema validation gates (e.g., STAC JSON schema checks, DCAT validation, PROV bundle validation).
- Geospatial validity checks (CRS, geometry validity, bbox/time range sanity).
- Regression checks when updating graph or APIs.

---

## 🌐 STAC, DCAT & PROV Alignment

SOPs must declare which standard artifacts are created or updated.

### STAC
- State whether the SOP adds or modifies:
  - a STAC Collection (`data/stac/collections/...`)
  - STAC Items (`data/stac/items/...`)
- Include validation steps (schema + integrity + broken links).

### DCAT
- State whether the SOP updates:
  - dataset entries in `data/catalog/dcat/`
- Declare the mapping between the dataset and its STAC representation where relevant.

### PROV-O
- If the SOP creates derived artifacts, capture lineage:
  - Entities (inputs/outputs)
  - Activities (transforms)
  - Agents (people/tools)
- Store PROV bundles under `data/prov/` (or the canonical lineage location used by the repo).

### Versioning
- SOPs must increment their own `version:` when steps change materially.
- If an SOP changes a data product, ensure the relevant dataset/catalog versioning is handled in the appropriate subsystem.

---

## 🧱 Architecture

### Components
| Component | Canonical home | Responsibility | SOP touchpoints |
|---|---|---|---|
| ETL / pipelines | `src/pipelines/` | Deterministic transforms | SOPs may reference run commands + configs |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Discoverability + lineage | SOPs must describe updates + validation |
| Graph | `src/graph/` | Ontology-governed semantics | SOPs may add ingest fixtures/migrations |
| API boundary | `src/server/` | Contracted access layer | SOPs must not bypass contracts |
| UI | `web/` | Map layers + Focus Mode | SOPs must update layer registries safely |
| Story Nodes | `docs/reports/story_nodes/` | Provenance-linked narrative | SOPs may describe publishing steps |
| MCP SOPs | `mcp/sops/` | Repeatable procedures | This library |

### Interfaces and contracts
| Interface | Location | Contract | Notes |
|---|---|---|---|
| SOP docs | `mcp/sops/*.md` | KFM Markdown protocol + linting | Front-matter required |
| STAC | `data/stac/**` | STAC profile + schema validation | Items ↔ collections integrity |
| DCAT | `data/catalog/dcat/**` | DCAT profile + validation | Dataset registry |
| PROV | `data/prov/**` | PROV profile + validation | Lineage bundles |
| Graph ingest | `src/graph/**` | Ontology protocol | Labels/relations must conform |
| API endpoints | `src/server/**` | REST/GraphQL contracts | Redaction enforced here |
| UI layer registry | `web/**` | UI registry schema | Used for layer availability + metadata |

### Extension points checklist
When adding a new SOP, confirm:
- [ ] The SOP states which pipeline stage(s) it touches.
- [ ] The SOP indicates where outputs land and how they are validated.
- [ ] The SOP includes verification and troubleshooting.
- [ ] The SOP is indexed in `mcp/sops/README.md`.
- [ ] Any new schema, contract, or governance rule changes are routed to their canonical docs.

---

## 📚 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
SOPs are internal operational documentation and do not typically surface directly in the UI. However, SOP-driven outputs may feed Story Nodes and Focus Mode via:
- new datasets or layers
- new evidence artifacts
- updated provenance and citations

### Provenance-linked narrative rule
If an SOP produces or changes evidence used in Story Nodes, ensure:
- every narrative claim can be tied back to a dataset/document ID
- provenance artifacts (STAC/DCAT/PROV and graph lineage) exist and validate

### Potential structured narrative controls
Not applicable for this README. If an SOP produces a new narrative UX control, document it in the relevant Story Node or UI subsystem docs.

---

## ✅ Validation & CI/CD

### Validation steps
Each SOP should include relevant checks, such as:
- Markdown front-matter and link validation.
- STAC/DCAT/PROV schema validation if catalogs are updated.
- Graph ingestion test fixtures or migration checks if graph is updated.
- API contract validation if endpoints or schemas change.
- UI build / layer registry validation if UI configuration changes.

### Reproduction
Each SOP should include a reproducible command sequence. Example placeholder:

~~~bash
# 1) Fetch or stage inputs
# <replace with repo-specific command>

# 2) Run the pipeline step
# <replace with repo-specific command>

# 3) Validate outputs
# <replace with repo-specific command>
~~~

### Troubleshooting
SOPs should document:
- common failure modes (schema mismatch, CRS errors, missing assets)
- how to diagnose (logs, validation outputs)
- safe rollback strategy (revert catalog change, revert migration, etc.)

### Telemetry signals
If the repo captures run metadata, SOPs should note where those logs/manifests live and what constitutes a successful run signature.

---

## ⚖ FAIR+CARE & Governance

### Review gates
SOP changes require review when they:
- add a new external data source or change licensing interpretation
- touch sensitive locations or sovereignty-protected material
- modify redaction logic or boundary rules
- change API contracts consumed by UI
- alter provenance expectations for narrative contexts

### CARE and sovereignty considerations
- Follow sovereignty rules for culturally sensitive content and protected sites.
- Prefer generalization/redaction when required, and document the decision.

### AI usage constraints
- SOPs should not direct contributors to infer or publish sensitive locations.
- Align the SOP’s front-matter AI permissions with the repo governance stance.

---

## 🧾 Version History

| Version | Date | Change summary | Author | Review status |
|---|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial SOP README scaffold | TBD | draft |

---

## Footer refs
- `docs/MASTER_GUIDE_v12.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/glossary.md`