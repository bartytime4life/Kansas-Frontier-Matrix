---
title: "Kansas Frontier Matrix — Contributing Guide"
path: "CONTRIBUTING.md"
version: "v1.0.0-draft"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:contributing:v1.0.0-draft"
semantic_document_id: "kfm-contributing-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:contributing:v1.0.0-draft"
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

# Contributing to Kansas Frontier Matrix

Thanks for helping build **Kansas Frontier Matrix (KFM)**. This repo is **contract-first** and **evidence-first**: changes should preserve the canonical ordering and the “no unsourced narrative” rule.

**Canonical flow (do not break):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 🧭 What kinds of contributions we accept

- **Docs & standards:** clarify guidance, templates, runbooks, ADRs.
- **Data / domain packs:** add a new dataset (or domain) with provenance and catalog artifacts.
- **ETL / pipelines:** deterministic transforms that write to `data/**`.
- **Catalog outputs:** STAC / DCAT / PROV creation and validation.
- **Graph / ontology:** ingest fixtures, ontology-aligned mappings.
- **API boundary:** endpoints, query services, redaction rules, API contracts.
- **UI:** map layers, focus mode UI, citation rendering.
- **Story Nodes:** sourced, provenance-linked narrative nodes (draft → published).

If you’re unsure where your change belongs, open a small PR that adds an ADR proposal under `docs/architecture/adr/` describing what you want to do and where it should live.

---

## ✅ Non‑negotiables (architectural invariants)

These are enforced by design and/or CI gates.

1. **No UI direct-to-graph reads**  
   - `web/` must never query Neo4j directly; all graph access is via `src/server/`.

2. **No unsourced narrative**  
   - Published Story Nodes must be provenance-linked and must validate.

3. **Contracts are canonical**  
   - Schemas/specs live in `schemas/`.  
   - API contracts live in `src/server/contracts/`.  
   - Contracts must validate in CI.

4. **Data outputs are not code**  
   - Derived datasets belong under `data/<domain>/processed/`, not under `src/`.

5. **STAC/DCAT/PROV are first-class**  
   - STAC, DCAT, and PROV remain required for datasets and evidence products.

---

## 🗂️ Directory layout

### Top-level overview (target)

~~~text
📁 .
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
├── 📁 releases/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 CITATION.cff
├── 📄 CHANGELOG.md
├── 📄 CONTRIBUTING.md
├── 📄 SECURITY.md
├── 📄 .editorconfig
├── 📄 .pre-commit-config.yaml
├── 📄 docker-compose.yml
└── 📄 .env.example
~~~

### Canonical homes by stage

| Stage | Canonical home | What belongs here |
|---|---|---|
| ETL / pipelines | `src/pipelines/` | deterministic transforms; run manifests; outputs in `data/**` |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections; DCAT datasets; PROV bundles |
| Graph | `src/graph/` + `data/graph/` | ontology-governed ingest; import fixtures/CSVs |
| API boundary | `src/server/` | contracts; redaction; query services |
| UI | `web/` | map layers; focus mode UI; citation rendering |
| Story Nodes | `docs/reports/story_nodes/` | templates; draft; published; assets |
| Releases | `releases/` | manifests; SBOMs; signed bundles; telemetry snapshots |

---

## 🧑‍💻 Local development expectations

This repository supports multiple subsystems (pipelines, server, web UI). The exact commands may differ by environment; the expectations below are *contract-level*:

1. **Run the pre-commit hooks** configured in `.pre-commit-config.yaml` before you open a PR.  
2. **Run tests** relevant to your change (pipelines / server / web).  
3. **Run validators** relevant to your change:
   - Markdown protocol validation (docs)
   - Schema validation (`schemas/…`)
   - Story Node validation (`docs/reports/story_nodes/…`)
   - API contract tests (`src/server/contracts/…`)
   - Security and sovereignty scanning (where applicable)

> Repo lint reminder: do **not** add YAML front-matter to code files. YAML front-matter is for Markdown documents only.

---

## 🧩 Change-type guidance

### 1) Documentation changes
- Use a governed template:
  - General documentation → `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
  - Story Nodes / Focus Mode narratives → `docs/templates/TEMPLATE__STORY_NODE_V3.md`
  - API contract additions/changes → `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Keep YAML front-matter keys intact (no ad-hoc fields).

### 2) Data + catalog contributions (new dataset or update)
When you add or update a dataset, include:
- **Data placement**
  - Raw sources → `data/<domain>/raw/`
  - Working files → `data/<domain>/work/`
  - Derived outputs → `data/<domain>/processed/`
- **Catalog outputs**
  - STAC items/collections → `data/stac/…`
  - DCAT record(s) → `data/catalog/dcat/…`
  - PROV bundle(s) → `data/prov/…`
- **Determinism**
  - Pipelines should be idempotent and produce stable outputs given the same inputs/config.

### 3) Graph / ontology contributions
- Put ingest logic and transforms under `src/graph/`.
- Put import fixtures/exports under `data/graph/`.
- Align changes with the repo’s ontology protocol and relevant schemas/shapes.

### 4) API boundary contributions
- API code and contracts live under `src/server/`.
- Put new/changed contracts under `src/server/contracts/` and add/adjust contract tests.
- Ensure UI uses the API boundary (no direct graph access from `web/`).

### 5) UI contributions
- UI lives under `web/`.
- UI must render citations and provenance links where required (especially in Focus Mode views).
- UI must never query Neo4j directly.

### 6) Story Node contributions
- Draft story nodes go under `docs/reports/story_nodes/draft/`.
- Published story nodes go under `docs/reports/story_nodes/published/<story_slug>/`.
- Published nodes must be provenance-linked and pass validation.

---

## 🧪 Validation & CI expectations (what your PR should pass)

Minimum CI gates for v13 readiness:

- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

Repo lint rules to respect:

- No YAML front-matter in code files
- No `README.me`
- No duplicate canonical homes without explicit deprecation markers

---

## ⚖ FAIR+CARE & Governance

Before submitting changes, check:

- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/governance/REVIEW_GATES.md`

Some changes may require extra review (examples: sensitive content, redaction behavior, narrative/AI behaviors, or sovereignty constraints).

---

## ✅ PR checklist (copy into your PR description)

- [ ] My change fits a single pipeline stage (or clearly explains cross-stage impact).
- [ ] I used the correct canonical home(s) and did not create duplicate subsystem roots.
- [ ] I ran the pre-commit hooks and fixed any failures.
- [ ] I ran relevant tests and validators (schemas/contracts/story nodes/etc.).
- [ ] If I added/updated data, I included STAC/DCAT/PROV outputs and provenance.
- [ ] If I changed the API or contracts, I updated `src/server/contracts/` and tests.
- [ ] If I changed the UI, it still relies only on `src/server/` for graph data.
- [ ] If I changed Story Nodes, they remain provenance-linked and validate.

---

## 🧾 Version History

| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-21 | Initial CONTRIBUTING guide aligned to v13 blueprint | <your-name> |

---

## Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Templates: `docs/templates/`
- Standards: `docs/standards/`
- Governance: `docs/governance/`
