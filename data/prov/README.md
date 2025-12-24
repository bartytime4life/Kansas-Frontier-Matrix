---
title: "KFM PROV Directory Lineage Bundles"
path: "data/prov/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:prov:readme:v1.0.1"
semantic_document_id: "kfm-data-prov-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:data:prov:readme:v1.0.1"
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

# KFM PROV Directory — Lineage Bundles (`data/prov/`)

This directory is the **canonical repository location** for **machine-readable provenance outputs** (lineage bundles) produced by KFM pipelines and catalog stages.

**Pipeline position (non-negotiable):** **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose

`data/prov/` exists to keep KFM **auditable** and **traceable**.

It stores provenance that lets any downstream consumer (Graph/API/UI/Story/Focus Mode) answer:

- **What is this artifact?**
- **Where did it come from?**
- **How was it produced?**
- **Who/what produced it?**
- **Was anything redacted/generalized and why?** (without leaking protected details)

### Scope

| In Scope | Out of Scope |
|---|---|
| PROV bundles emitted by ETL, transforms, catalog builds, and graph ingest | Raw source data (belongs under `data/<domain>/raw/`) |
| Run manifests and integrity metadata (checksums, content inventory) | Pipeline implementation code (belongs under `src/pipelines/`) |
| Safe redaction/generalization notices for provenance artifacts | STAC catalogs (belongs under `data/stac/`) |
| Stable cross-links (by ID) to STAC/DCAT outputs and graph entities | DCAT catalogs (belongs under `data/catalog/dcat/`) |
| Minimal, non-sensitive run diagnostics for reproducibility | Secrets, credentials, PII, or sensitive location details |

### Audience

- Primary: pipeline maintainers, catalog maintainers
- Secondary: graph/ontology maintainers, API developers, UI/Focus Mode implementers, auditors/curators, Story Node authors

### Definitions

- Glossary: `docs/glossary.md` *(if missing, treat as **not confirmed in repo** and repair link)*
- Terms used in this doc:
  - **PROV-O**: W3C provenance model (Entities, Activities, Agents)
  - **Bundle**: a serialized package of PROV statements for a single run and/or product
  - **run_id**: stable identifier for a pipeline/catalog activity
  - **product_id**: stable identifier for a versioned dataset/evidence product
  - **agent**: script/service/person responsible for the activity (as captured in PROV)

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| PROV bundles | `data/prov/**` | Pipelines + catalog maintainers | Generated outputs; avoid hand-edits |
| PROV schema/profile | `schemas/prov/**` | Schema/catalog maintainers | Contract for validation (KFM-PROV profile) |
| STAC catalogs | `data/stac/**` | Catalog stage | Evidence artifacts should reference PROV IDs where profile requires |
| DCAT records | `data/catalog/dcat/**` | Catalog stage | Discovery records should reference PROV IDs where profile requires |
| Graph ingest fixtures | `data/graph/**` | Graph build | Import fixtures should carry provenance IDs for traceability |

### Non-negotiables (folder contract)

1. **Provenance is evidence, not narrative.** Keep bundles machine-first and minimal.
2. **No secrets.** Never write API keys, tokens, credentials, private endpoints, or internal hostnames into provenance artifacts.
3. **No sensitive location leakage.** Provenance must not reconstruct restricted locations (see sovereignty policy).
4. **Deterministic + reproducible.** Re-runs with the same inputs and pinned versions should yield diffable, stable bundles.
5. **Generated, not hand-edited.** Treat bundles as build artifacts. If a manual edit is unavoidable, record it in `manifest.json`.

### Definition of done (for this README)

- [ ] Front-matter complete + valid and `path` matches file location
- [ ] Folder contract is explicit (in scope/out of scope + non-negotiables)
- [ ] Directory layout + naming expectations documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + FAIR+CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `data/prov/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/{raw,work,processed}/` | Source snapshots → transforms → normalized outputs |
| PROV outputs | `data/prov/` | Lineage bundles + run manifests + integrity metadata |
| STAC catalogs | `data/stac/` | STAC Collections + Items |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset records |
| Pipelines | `src/pipelines/` | ETL + transforms that emit PROV |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/UI/telemetry) |
| Graph | `src/graph/` + `data/graph/` | Graph build + ontology bindings + import fixtures |
| API boundary | `src/server/` | Contracted access to graph + catalogs |
| UI | `web/` | React/Map clients |
| Story Nodes | `docs/reports/story_nodes/` | Provenance-linked narratives |

### Canonical target layout (v13+)

If the repository already has an established layout, **align to it** and treat this as the target end-state.

~~~text
📁 data/
└── 📁 prov/
    ├── 📄 README.md
    │
    ├── 📁 runs/
    │   └── 📁 <run_id>/
    │       ├── 📄 prov.jsonld           # PROV bundle for the run/activity
    │       ├── 📄 manifest.json         # inventory, run metadata, version pins
    │       └── 📄 integrity.json        # checksums, sizes, and link integrity
    │
    └── 📁 products/
        └── 📁 <product_id>/
            ├── 📄 prov.jsonld           # PROV bundle for the product/entity
            ├── 📄 manifest.json
            └── 📄 integrity.json
~~~

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/prov/runs/<run_id>/` | Provenance about one execution/activity | ETL/catalog/graph build | Auditors, graph ingest, API “evidence” endpoints |
| `data/prov/products/<product_id>/` | Provenance about one data product/entity | Catalog build / release packaging | UI/Focus Mode evidence panels, Story Node citations |
| `manifest.json` | Stable inventory + version pins | Pipelines | CI + debugging + audits |
| `integrity.json` | Checksums + reference/link checks | Pipelines/CI | CI + release packaging |

---

## 🧭 Context

### Background

KFM is **contract-first** and **provenance-first**. PROV bundles are required so that:

- catalog artifacts (STAC/DCAT/PROV) remain machine-validatable evidence,
- graph entities can carry references to the evidence that created them,
- Focus Mode can enforce “provenance-linked only” narrative behavior.

### Assumptions

- PROV outputs represent **Activities** (runs/builds), **Entities** (inputs/outputs), and **Agents** (pipelines/services/people).
- Bundles are treated as **build artifacts**; most changes should come from pipeline code/config, not by editing PROV directly.
- PROV artifacts validate against `schemas/prov/**` (KFM-PROV profile).

### Constraints / invariants

- **Pipeline order is preserved:** **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- **API boundary is enforced:** UI does not read Neo4j directly; it consumes contracted APIs.
- Pipelines must not write STAC/DCAT/PROV artifacts into `docs/`.
- Provenance must be safe to publish under the doc’s classification (no secrets; no protected locations).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Canonical `run_id` format and stability rules | TBD | TBD |
| Accepted serialization formats beyond JSON-LD (if any) | TBD | TBD |
| Required fields enforced by `schemas/prov/**` in this repo | TBD | TBD |

### Future extensions

- Bundle signing and/or checksum enforcement at release packaging time.
- Recording container image digests and SBOM identifiers for reproducibility.
- “Redaction justification” logging that is safe for public distribution.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL / Pipeline Run] --> P[PROV Bundle]
  A --> S[STAC Items + Collections]
  A --> D[DCAT Dataset Records]
  S --> G[Neo4j Graph]
  D --> G
  P --> G
  G --> API[API Boundary]
  API --> UI[React/Map UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

### Optional sequence diagram (evidence resolution)

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  participant Catalog as STAC/DCAT/PROV

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  API->>Catalog: resolve STAC/DCAT/PROV IDs
  Graph-->>API: entities + evidence IDs
  Catalog-->>API: catalog + provenance payloads
  API-->>UI: narrative + citations + provenance panel data
~~~

---

## 📦 Data & Metadata

### Accepted serialization formats

The repo’s authoritative accepted formats should be enforced by `schemas/prov/**`:

- **Preferred:** JSON-LD (`prov.jsonld`)
- **Optional:** RDF/Turtle (`.ttl`) *(only if supported by repo schemas/profile; otherwise treat as **not confirmed in repo**)*

### Minimum required PROV content (conceptual)

A bundle should include:

- **Activities**
  - ETL run
  - catalog build
  - graph ingest
- **Entities**
  - inputs: raw/work/processed artifacts and external sources (by stable reference)
  - outputs: processed artifacts + STAC/DCAT outputs + graph ingest fixtures
- **Agents**
  - pipeline/service identity
  - operator identity (if policy allows; avoid PII)

Expected core relations:

- `prov:used` (Activity → Entity input)
- `prov:wasGeneratedBy` (Entity output → Activity)
- `prov:wasAssociatedWith` (Activity → Agent)
- `prov:wasDerivedFrom` (Entity output → Entity input)

### `manifest.json` (recommended)

`manifest.json` should be stable, diffable, and safe to publish.

Recommended (repo-defined) fields:

~~~json
{
  "run_id": "string",
  "job_name": "string",
  "started_at": "ISO-8601",
  "ended_at": "ISO-8601",
  "inputs": [{"id": "string", "uri": "string", "sha256": "string"}],
  "outputs": [{"id": "string", "uri": "string", "sha256": "string"}],
  "profiles": {
    "kfm_mdp": "KFM-MDP v11.2.6",
    "kfm_ppc": "KFM-PPC v11.0.0",
    "kfm_prov": "KFM-PROV v11.0.0"
  },
  "code": {"commit_sha": "<latest-commit-hash>"},
  "environment": {"container_image": "optional", "python": "optional"},
  "redactions": [{"type": "optional", "scope": "optional", "justification": "optional"}]
}
~~~

### `integrity.json` (recommended)

`integrity.json` is intended for CI and release packaging.

Recommended (repo-defined) fields:

- SHA-256 digests for `prov.jsonld` and referenced in-repo artifacts
- File sizes/byte counts (truncation detection)
- Link integrity results (referenced STAC/DCAT IDs resolve)

---

## 🌐 STAC, DCAT & PROV Alignment

### Alignment rule

Each dataset or evidence product is expected to have:

- STAC catalog entry (Collection + Item(s)) where applicable
- DCAT dataset record(s) where applicable
- PROV activity describing lineage

This enables “follow the evidence” navigation in Graph/API/UI and supports Focus Mode auditability.

### Identifier linkage expectations

Downstream systems should be able to resolve:

- PROV activity IDs ↔ ETL/catalog `run_id`s
- PROV entity IDs ↔ STAC Item IDs and/or DCAT dataset IDs
- PROV IDs ↔ graph entities (via properties on nodes/edges)

> Exact field/property names are governed by the KFM profiles and schemas. Use `schemas/prov/**`, `schemas/stac/**`, and `schemas/dcat/**` as the contract source of truth.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Output that links to PROV |
|---|---|---|
| ETL | ingest + normalize | `data/<domain>/{raw,work,processed}/` + run provenance |
| Catalog build | publish STAC/DCAT/PROV | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` |
| Graph build | ingest evidence into Neo4j | `data/graph/**` with provenance IDs |
| API boundary | enforce contracts + redaction | API payloads include evidence/provenance refs |
| UI | map + narrative | consumes provenance-linked content via API only |
| Story Nodes | curated narrative | cite STAC/DCAT/PROV evidence IDs |
| Focus Mode | contextual synthesis | shows provenance panel and citations |

### Interfaces / contracts

| Contract | Canonical location | Notes |
|---|---|---|
| PROV schemas | `schemas/prov/**` | Semver + changelog (repo-defined) |
| STAC schemas | `schemas/stac/**` | Used to validate `data/stac/**` |
| DCAT schemas | `schemas/dcat/**` | Used to validate `data/catalog/dcat/**` |
| API contracts | `src/server/` | REST/OpenAPI or GraphQL SDL (repo-defined) |

### Extension points checklist

- [ ] New dataset added under `data/<domain>/...`
- [ ] STAC Collections and Items generated and validated
- [ ] DCAT dataset record created or updated
- [ ] PROV activity/bundle recorded under `data/prov/`
- [ ] Graph ingest updated (if applicable) and carries provenance IDs
- [ ] API endpoints expose provenance refs
- [ ] UI/Story Nodes updated only via API contracts

---

## 🧠 Story Node & Focus Mode Integration

### What Focus Mode needs from `data/prov/`

For any displayed claim, Focus Mode should be able to retrieve:

- the **PROV activity/run** that produced the evidence,
- the **input sources** used,
- the **output artifacts** (STAC/DCAT IDs, files, graph entities),
- any **redaction/generalization notices** (without exposing protected details).

### Provenance-linked narrative rule

- Story Nodes and Focus Mode content must cite evidence IDs that resolve to STAC/DCAT/PROV artifacts.
- Predictive or AI-generated content must be opt-in and include uncertainty metadata (where used).

---

## 🧪 Validation & CI/CD

### Minimum validation checks (folder-level)

- [ ] PROV bundles validate against `schemas/prov/**`
- [ ] No orphan references: any STAC/DCAT IDs referenced by PROV resolve to artifacts under `data/stac/**` and `data/catalog/dcat/**`
- [ ] Deterministic outputs: repeated runs produce diffable, stable bundles (where stable IDs are defined)
- [ ] No secrets/PII: repository scanners pass (CI gate)
- [ ] Sovereignty/ethics gates: provenance does not expose restricted locations or sensitive fields

### Reproduction

~~~bash
# Placeholder: replace with repo-specific commands.
# 1) Run ETL/catalog build to generate PROV
# 2) Validate PROV bundles against schemas
# 3) Run link integrity checks across STAC/DCAT/PROV
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates

Human review is required when changes:

- introduce new provenance fields or schemas (`schemas/prov/**`),
- introduce new external data sources or new run agents,
- affect redaction/generalization behavior,
- change how provenance links to STAC/DCAT/Graph are represented.

### CARE / sovereignty considerations

- Provenance must not leak protected locations or culturally sensitive knowledge.
- Where redaction is required, provenance may record the *fact of redaction* and a justification category without disclosing protected details.
- Apply any additional controls required by `docs/governance/SOVEREIGNTY.md` (if present).

### AI usage constraints

- AI must not infer sensitive locations from provenance artifacts.
- AI transformation permissions/prohibitions must match the front-matter of this document.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `data/prov/` | TBD |
| v1.0.1 | 2025-12-24 | Aligned to universal template; clarified folder contract and linkage expectations | TBD |

---

## ⚖ Footer

- Master Guide: `docs/MASTER_GUIDE_v12.md` *(if missing, treat as **not confirmed in repo** and repair link)*
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`