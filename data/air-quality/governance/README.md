---
title: "Air Quality — Data Domain Governance README"
path: "data/air-quality/governance/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:data:air-quality:governance:readme:v0.1.0-draft"
semantic_document_id: "kfm-data-air-quality-governance-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:data:air-quality:governance:readme:v0.1.0-draft"
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

# Air Quality — Data Domain Governance

## 📘 Overview

### Purpose
- Provide the governance entrypoint for the **Air Quality** data domain.
- Define *domain-local* expectations for classification, provenance, validation, and review gates before any air-quality artifacts are published to catalogs, graph, APIs, or UI.

### Scope
| In Scope | Out of Scope |
|---|---|
| Governance artifacts for the air-quality domain (this folder), and the “rules of the road” for ingest → transform → catalog of air-quality datasets | Implementing ETL jobs, designing API endpoints, UI layer styling, or defining new ontology terms without review |

### Audience
- Primary: data engineers, catalog maintainers, governance reviewers
- Secondary: analysts, Story Node authors, UI layer maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive): Domain, Dataset, Asset, STAC, DCAT, PROV, Station/Sensor, Observation/Timeseries, Derived Product

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Domain governance README (this doc) | `data/air-quality/governance/README.md` | TBD | Entry point for domain-local rules |
| Domain classification notes | `data/air-quality/governance/DATA_CLASSIFICATION.md` | TBD | Planned; records any sensitive-location handling |
| Source + license ledger | `data/air-quality/governance/SOURCES_AND_LICENSES.md` | TBD | Planned; **do not** publish data without license clarity |
| QA checklist | `data/air-quality/governance/QA_CHECKLIST.md` | TBD | Planned; minimum validation gates |
| Domain change log | `data/air-quality/governance/CHANGELOG.md` | TBD | Planned; record changes that affect downstream outputs |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All domain-specific claims clearly marked as **confirmed** vs **not confirmed in repo**
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “not applicable”)
- [ ] File tree reflects the intended domain organization and is visually aligned

---

## 🗂️ Directory Layout

### This document
- `path` (must match front-matter): `data/air-quality/governance/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Domain governance (this area) | `data/air-quality/governance/` | Domain-local governance docs, checklists, and decision logs |
| Data staging (required) | `data/raw/`, `data/work/`, `data/processed/` | Raw inputs → intermediate artifacts → canonical processed outputs |
| Catalog outputs | `data/stac/` + `docs/data/` | STAC collections/items + DCAT mappings + PROV bundles |
| Graph integration | `src/graph/` + `docs/graph/` | Ontology, label mappings, migrations, constraints |
| ETL / transforms | `src/pipelines/` + `docs/pipelines/` | Deterministic pipelines + docs |
| UI layer registry | `web/` + `docs/design/` | Map layers, UI configs, and governed UI rules |
| Story Nodes (narrative outputs) | `docs/reports/**/story_nodes/` | Evidence-led narrative artifacts with provenance |

### File tree
> Notes:
> - Items marked **(planned)** may not exist yet (not confirmed in repo).
> - The staging folders (`data/raw|work|processed|stac`) are canonical; air-quality content should be organized *within* them by domain.

~~~text
📁 data/
├── 📁 air-quality/
│   ├── 📁 governance/
│   │   ├── 📄 README.md
│   │   ├── 📄 DATA_CLASSIFICATION.md (planned)
│   │   ├── 📄 SOURCES_AND_LICENSES.md (planned)
│   │   ├── 📄 QA_CHECKLIST.md (planned)
│   │   └── 📄 CHANGELOG.md (planned)
│   └── 📄 DOMAIN_NOTES.md (planned)
├── 📁 raw/
│   └── 📁 air-quality/                 # raw ingests (append-only; never “hand edited”)
├── 📁 work/
│   └── 📁 air-quality/                 # intermediate artifacts (reproducible; safe to delete/rebuild)
├── 📁 processed/
│   └── 📁 air-quality/                 # canonical outputs (schema-validated; versioned)
├── 📁 stac/
│   └── 📁 air-quality/                 # STAC Collections/Items for this domain
└── 📁 reports/
    └── 📁 air-quality/                 # optional evidence products / analysis outputs
~~~

---

## 📦 Data & Metadata

### Data lifecycle (required staging)
- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/reports/` outputs as needed)

### Domain expansion pattern
- New domains go under `data/<domain>/.`
- New domain docs go under `docs/<domain>/.` or `docs/data/<domain>/.` (**choose one canonical location and link**)

### Domain-local governance rules
- **Default classification:** This domain is currently labeled `sensitivity: public`, `classification: open` in front-matter.
- **If any asset requires elevated handling** (e.g., precise locations that could be sensitive), document the decision in:
  - `data/air-quality/governance/DATA_CLASSIFICATION.md` (planned)
  - and ensure downstream catalogs and UI layers apply the same restriction.

> Air-quality-specific sensitivity guidance is **not confirmed in repo**. Until confirmed, treat any location-bearing records conservatively:
> - avoid inferring private locations,
> - and require explicit review before publishing high-precision point data.

### Minimal metadata required for any dataset entering this domain
- Stable dataset identifier (domain + source + vintage/version)
- Spatial extent (bbox/geometry) and temporal coverage
- License + attribution requirements
- Processing lineage (at minimum: inputs + transform activity + timestamps)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy (how to document)
Every new dataset in this domain must have:
- **STAC**: Collection + Item(s)
- **DCAT**: minimum title/description/license/keywords
- **PROV**: at least one Activity describing the transform that generated the processed artifact(s)

> Exact schema locations and validators are **not confirmed in repo** for the air-quality domain specifically; follow the repo-wide STAC/DCAT/PROV profiles referenced in front-matter and the root governance docs.

### Versioning expectations
- New dataset versions:
  - must link predecessor/successor (e.g., via STAC `links`, DCAT versioning fields, and/or PROV derivation)
  - must keep identifiers stable and append a new version token rather than overwriting history
- Graph should mirror dataset version lineage (if/when graph integration is added for this domain)

---

## 🧩 Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Not confirmed in repo for this domain.
- Intended pattern:
  - Air-quality datasets become selectable map layers (via UI registry)
  - Narrative claims about air quality must cite dataset + item IDs

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "air_quality:<TBD-layer-id>"
focus_time: "<TBD-iso8601>"
focus_center: [-98.0000, 38.0000]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (if graph is extended)
- [ ] API contract tests (if APIs are extended)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate STAC/DCAT/PROV
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol checks
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

---

## ⚖ FAIR+CARE & Governance

### Review gates
- Any of the following changes should trigger review:
  - adding a **new upstream source** (license + provenance verification)
  - publishing **location-bearing** datasets at higher precision than previously used
  - changing STAC/DCAT/PROV schema mappings for this domain
  - exposing new layers in the UI registry

### CARE / sovereignty considerations
- Domain-specific CARE rules are **not confirmed in repo**.
- Apply repo-wide sovereignty rules per `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use.
- Do not use AI to infer sensitive locations from air-quality records.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0-draft | 2025-12-17 | Initial domain governance README scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
