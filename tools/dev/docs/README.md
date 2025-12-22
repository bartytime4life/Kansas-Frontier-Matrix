---
title: "KFM Dev Tooling Docs — README"
path: "tools/dev/docs/README.md"
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

doc_uuid: "urn:kfm:doc:tools:dev-docs-readme:v1.0.0"
semantic_document_id: "kfm-tools-dev-docs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:dev-docs-readme:v1.0.0"
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

# 🛠️ tools/dev/docs

## 📘 Overview

### Purpose
This folder holds **developer-facing documentation** for the `tools/dev/` area: runbooks, local workflows, troubleshooting notes, and “how-to” guides that support development and CI work.

This directory is **not** the canonical home for KFM architecture, standards, pipeline contracts, or public-facing documentation. Those belong under `docs/` and must follow the governed templates and review gates.

### Scope
Include docs here when they:
- Explain how to use or maintain **developer tooling** under `tools/dev/`
- Document **local development workflows** and debugging steps
- Describe how to build/refresh **dev fixtures** (see `tools/dev/fixtures/README.md`)
- Provide “operator notes” that don’t redefine canonical contracts or standards

### Out of scope
Do **not** put the following here:
- Canonical pipeline definitions, ontology rules, catalog standards, or API contracts (go in `docs/`).
- Any “second copy” of a canonical doc that already exists elsewhere (avoid “mystery duplicates”).
- Sensitive knowledge or restricted locations that have not been redacted/generalized.

### Audience
- Maintainers and contributors working on: ETL, catalogs (STAC/DCAT/PROV), graph ingest, API, UI, Story Nodes, Focus Mode.
- CI / repo-lint troubleshooters.

### Canonical references (authoritative)
- `docs/MASTER_GUIDE_v12.md`
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`

---

## 🗂️ Directory Layout

### This directory (expected)
~~~text
📁 tools/
└── 📁 dev/
    ├── 📁 docs/
    │   └── 📄 README.md
    └── 📁 fixtures/
        └── 📄 README.md
~~~

### What to add here
Recommended organization for additional dev docs (create only as needed):
~~~text
📁 tools/dev/docs/
├── 📄 README.md
├── 📁 runbooks/               # step-by-step operational guides (local + CI)
│   └── 📄 <topic>.md
├── 📁 troubleshooting/        # common errors and fixes
│   └── 📄 <topic>.md
└── 📁 howto/                  # short "do X" docs (dev-only)
    └── 📄 <topic>.md
~~~

Notes:
- If a document becomes canonical (defines contracts/standards), move it to `docs/` and conform it to the correct governed template.

---

## 🧭 Context

### The non-negotiable flow
KFM work is organized around the canonical pipeline ordering:
**ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → UI → Story Nodes → Focus Mode**

Dev tooling should support this ordering and must not short-circuit it (e.g., UI code should not depend on direct graph access; use API contracts).

### “One canonical home” rule (practical interpretation)
Use this folder for **how to work on the repo** (developer experience), not for **what the system is** (canonical documentation).

If you find yourself writing:
- “the official schema is…”
- “the pipeline contract says…”
- “this is the canonical path for…”

…you likely need `docs/` instead of `tools/dev/docs/`.

---

## 🗺️ Diagrams

### Tooling docs in relation to the pipeline
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs] --> C[Neo4j Graph] --> D[API Layer] --> E[UI] --> F[Story Nodes] --> G[Focus Mode]
  T[tools/dev/*] -. supports dev + CI .-> A
  T -. supports dev + CI .-> B
  T -. supports dev + CI .-> C
  T -. supports dev + CI .-> D
  T -. supports dev + CI .-> E
  T -. supports dev + CI .-> F
  T -. supports dev + CI .-> G
~~~

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Developer knowledge / runbook steps | Markdown | Maintainers | Markdown protocol checks (if enforced) |
| Tooling behavior descriptions | Markdown | `tools/dev/*` scripts/config | Keep references accurate; avoid duplicating canonical docs |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Dev docs (runbooks/how-to) | Markdown | `tools/dev/docs/**` | Governed doc template (recommended) |
| Links to fixture docs | Markdown links | `tools/dev/fixtures/README.md` | N/A |

### Sensitivity & redaction
- Do not include sensitive locations, credentials, tokens, or private identifiers.
- If a dev fixture contains restricted geospatial detail, document the required generalization/redaction approach and route it through governance review.

---

## 🌐 STAC, DCAT & PROV Alignment

This directory does not define STAC/DCAT/PROV standards. If a dev doc explains how to generate fixtures, it must:
- Point to the canonical profiles in `docs/standards/` (if present)
- Emphasize machine validation of generated artifacts against `schemas/`
- Avoid inventing schema rules inside runbooks

---

## 🧱 Architecture

### What this folder *can* do
- Explain how to run local or CI tooling that supports:
  - deterministic ETL runs,
  - catalog validation,
  - graph ingest fixture generation,
  - contract tests,
  - Story Node validation.

### What this folder must *not* do
- Establish alternative subsystem boundaries or “new canonical homes”
- Publish “official contracts” outside their canonical locations

---

## 🧠 Story Node & Focus Mode Integration

If a dev doc touches Story Nodes or Focus Mode, treat these as hard rules:
- Story Nodes must be provenance-linked (claims trace to evidence IDs).
- Focus Mode consumes provenance-linked content only; unsourced narrative is prohibited.
- Any predictive/AI-generated content must be clearly marked, opt-in, and carry uncertainty metadata.

(Authoritative details belong in `docs/`—dev docs should link, not redefine.)

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)
- [ ] Markdown protocol validation (if enabled in CI)
- [ ] Link checks for referenced local paths
- [ ] Ensure no duplicated canonical docs (no “mystery duplicates”)
- [ ] Ensure no secrets/credentials are present
- [ ] If referencing fixtures, ensure fixtures documentation exists and is up to date

### Reproduction (placeholders)
~~~bash
# Replace placeholders with repo-specific commands / scripts.

# 1) run markdown lint / protocol check (if applicable)
# <command>

# 2) run schema validators (if applicable)
# <command>

# 3) run unit/integration tests (if applicable)
# <command>
~~~

---

## ⚖ FAIR+CARE & Governance

### Review triggers
Escalate to governance review when dev docs introduce or expose:
- New external data sources
- New sensitive layers or restricted locations
- New public-facing endpoints / behaviors
- Any AI narrative behavior changes (even if “dev only”)

### Sovereignty safety
If you are unsure whether a location, dataset, or narrative is sensitive:
- treat it as sensitive until reviewed,
- generalize or remove the detail,
- link to governance policy docs above.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for `tools/dev/docs/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
