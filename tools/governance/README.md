---
title: "KFM Governance Tooling — README"
path: "tools/governance/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:tools:governance:readme:v1.0.0"
semantic_document_id: "kfm-tools-governance-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:governance:readme:v1.0.0"
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

# KFM Governance Tooling — README

## 📘 Overview

This directory is the **implementation home for automated governance checks** (validators, linters, and “review gate” detectors) that keep Kansas Frontier Matrix contributions compliant with:

- The canonical pipeline ordering (**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**)
- The “contract-first / evidence-first” constraints (schemas, API contracts, provenance, redaction)
- FAIR+CARE requirements and sovereignty safeguards

**Important boundary rule:** governance *policy* lives under `docs/governance/`. This folder exists to make those policies **executable** (CI gates, pre-commit checks, and local developer commands).

## 🗂️ Directory Layout

### Current

~~~text
📁 tools/
└── 📁 governance/
    └── 📄 README.md
~~~

### Recommended structure (add as needed)

~~~text
📁 tools/
└── 📁 governance/
    ├── 📄 README.md
    ├── 📁 runners/                   # entrypoints that CI / devs call
    ├── 📁 checks/                    # individual checks grouped by subsystem
    │   ├── 📁 markdown/              # Markdown protocol + front-matter validation
    │   ├── 📁 schemas/               # STAC/DCAT/PROV/telemetry schema validation
    │   ├── 📁 graph/                 # ontology + import constraint checks
    │   ├── 📁 api/                   # OpenAPI/GraphQL contract checks
    │   ├── 📁 ui/                    # layer-registry schema checks
    │   └── 📁 security_sovereignty/  # scanning gates + redaction rules
    ├── 📁 configs/                   # machine-readable rule configs/allowlists (no policy prose)
    └── 📁 fixtures/                  # deterministic test fixtures for validation
~~~

## 🧭 Context

Governance checks are cross-cutting: they do **not** introduce new product features, but they **prevent** breaking the governed architecture.

### What governance tooling protects

- **Pipeline order** stays intact: artifacts flow ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode.
- **Contract boundaries** stay intact: UI reads via API contracts; catalogs and schemas are machine-validated.
- **Provenance requirements** are enforced: Story Nodes and Focus Mode must only surface provenance-linked content.
- **Sovereignty and sensitivity** rules are enforced: redact/generalize restricted locations and honor CARE triggers.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL / Pipelines] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Layer]
  D --> E[Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph "Governance Tooling (tools/governance/)"
    M1[Markdown protocol validation]
    M2[Schema validation]
    M3[Graph integrity]
    M4[API contract tests]
    M5[UI registry schema checks]
    M6[Security + sovereignty scanning]
  end

  M1 -. gates .-> A
  M1 -. gates .-> F
  M2 -. gates .-> B
  M3 -. gates .-> C
  M4 -. gates .-> D
  M5 -. gates .-> E
  M6 -. gates .-> A
  M6 -. gates .-> B
  M6 -. gates .-> C
  M6 -. gates .-> D
  M6 -. gates .-> E
  M6 -. gates .-> F
  M6 -. gates .-> G
~~~

## 📦 Data & Metadata

Governance tooling may generate **reports**, but should not become a new canonical data home.

- Preferred write targets for derived artifacts:
  - run logs / validation outputs → `mcp/runs/` (or `mcp/experiments/`)
  - build reports (optional) → `data/reports/`
- Avoid committing generated outputs unless explicitly versioned and referenced.

## 🌐 STAC, DCAT & PROV Alignment

This folder is expected to host validators that check:

- **STAC**: `data/stac/collections/` and `data/stac/items/`
- **DCAT**: `data/catalog/dcat/` (JSON-LD outputs)
- **PROV**: `data/prov/` (run/dataset lineage bundles)

Validation should be **deterministic** and fail with actionable errors.

## 🧱 Architecture

### Minimum CI gates (what these tools should enable)

The governance toolchain should support (directly or via wrappers):

- Markdown protocol validation
- Schema validation (STAC/DCAT/PROV/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates (where applicable)

### “Validate / fail / skip” behavior

Checks should follow deterministic CI semantics:

- **Validate if present**
- **Fail if invalid**
- **Skip if not applicable** (optional subsystems not yet present)

## 🧠 Story Node & Focus Mode Integration

Governance checks should enforce:

- Every Story Node claim is traceable to a dataset/record/asset ID.
- Focus Mode only consumes provenance-linked content.
- Any predictive or AI-generated content is:
  - opt-in,
  - labeled as such, and
  - carries uncertainty/confidence metadata (where applicable).

## 🧪 Validation & CI/CD

### Local reproduction (placeholders)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Markdown protocol validation
# ./tools/governance/runners/validate_markdown.sh

# 2) Schema validation (STAC/DCAT/PROV/telemetry)
# ./tools/governance/runners/validate_schemas.sh

# 3) Graph integrity checks
# ./tools/governance/runners/validate_graph.sh

# 4) API contract tests
# ./tools/governance/runners/validate_api_contracts.sh

# 5) UI layer registry schema checks
# ./tools/governance/runners/validate_ui_registry.sh

# 6) Security + sovereignty scanning gates
# ./tools/governance/runners/scan_security_and_sovereignty.sh
~~~

### Repo lint rules (target gates)

Governance tooling is expected to enforce repo-level lint rules such as:

- No YAML front-matter in code files
- No `README.me`
- No duplicate canonical homes without explicit deprecation markers

### Suggested CI integration points

- Pre-commit: fast format + Markdown/front-matter checks
- Pull request: full validation suite + review-gate detection
- Release: full validation + release artifacts checks (e.g., SBOMs) when present

## ⚖ FAIR+CARE & Governance

### Review gates

Escalate to governance review (and ensure the PR/doc explicitly flags it) when changes introduce:

- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints or tools

### CARE / sovereignty considerations

- Identify impacted communities.
- Apply redaction/generalization rules for restricted locations.
- Ensure access controls and UI presentation follow sovereignty policy.

### AI usage constraints

- AI should not be used to “invent policy”.
- AI outputs must not infer sensitive locations.
- Documentation front-matter must reflect allowed vs prohibited AI transforms.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README scaffold for governance tooling | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`