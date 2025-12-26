---
title: "KFM Raw Data"
path: "data/raw/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:data:raw:readme:v1.0.0"
semantic_document_id: "kfm-data-raw-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:raw:readme:v1.0.0"

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

# KFM Raw Data

> **Purpose (required):** Define what belongs in the **raw landing layer** (`data/raw/`), the **immutability + provenance rules** for storing source artifacts, and how raw inputs connect to downstream **work → processed → STAC/DCAT/PROV → Graph/API → UI → Story Nodes → Focus Mode**.

## 📘 Overview

### Purpose

- `data/raw/` is the **landing zone for source artifacts “as received”** from external providers (downloads, dumps, exports, archives, API responses).

- This layer is **append-only** and **must not be hand-edited**; corrections happen by adding a new snapshot/version while retaining prior inputs for auditability.

- Raw is **evidence**, not a product: it supports provenance, reproducibility, and governance review, while user-facing outputs come from `data/processed/` and catalogs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Raw source snapshots (“as received”) and pointer files for large assets | Data cleaning/normalization (belongs in `data/work/`) |
| Minimum metadata to reproduce ingestion (source, retrieval time, license/terms, checksums) | Certified/public datasets (belongs in `data/processed/`) |
| Provenance linkage expectations (PROV references to raw entities) | STAC/DCAT authoring details (belongs in catalog docs + schemas) |
| Governance and sensitivity expectations for raw inputs | API/UI behaviors and contracts (documented under `src/server/` + `web/`) |

### Audience

- Primary: ETL/pipeline contributors, data maintainers, release managers.

- Secondary: governance reviewers, auditors, story authors who need evidence lineage.

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**).

- Terms used in this doc:

  - **Raw**: landed artifacts as received from a source.

  - **Work**: intermediate, reproducible transformation outputs; safe to delete/rebuild.

  - **Processed**: certified, schema-aligned outputs suitable for catalog + graph + UI.

  - **Snapshot**: a time/version-bounded raw capture of a source.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM Maintainers | Canonical pipeline ordering + invariants |
| Data root README | `data/README.md` | Data Maintainers | Repository-wide data layout conventions (may reflect v13 target layout) |
| v13 redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Target directory layout and migration direction |
| Universal template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governs this README structure |
| Domain ingestion docs | `data/<domain>/ingestion/README.md` (**not confirmed in repo**) | Domain Owners | Domain-level landing/processing rules (if present) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path` matches file location.

- [ ] Raw layer invariants stated (immutability, checksums, license capture, no hand edits).

- [ ] Directory layout reflects KFM staging semantics and avoids broken internal links.

- [ ] Validation + governance expectations listed (secrets/PII scanning, sensitivity propagation).

- [ ] Version history included.

## 🗂️ Directory Layout

### This document

- `path`: `data/raw/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data (root) | `data/` | Domains + staging + catalogs |
| Raw stage | `data/raw/` | Landed source artifacts (this document governs) |
| Work stage | `data/work/` | Intermediate artifacts (rebuildable) |
| Processed stage | `data/processed/` | Certified artifacts (schema-aligned) |
| STAC catalogs | `data/stac/` | STAC Collections/Items + assets |
| DCAT catalogs | `data/catalog/dcat/` | DCAT datasets/distributions |
| Provenance | `data/prov/` | PROV bundles (activities/entities/agents) |
| ETL/pipelines | `src/pipelines/` | Ingest + transform code/config |
| Graph ingest | `src/graph/` | Ontology + ingest/build steps |
| API boundary | `src/server/` | Contracted access (UI never reads Neo4j directly) |
| UI | `web/` | Map/narrative front end (React/MapLibre per architecture) |

### Supported layout patterns

KFM documents describe two common staging layouts:

1) **Stage-scoped (this folder):** `data/raw/<domain>/...`

2) **Domain-scoped (v13 target pattern):** `data/<domain>/raw/...`

If the repository migrates to domain-scoped staging, update this README (or replace it with the domain-scoped equivalent) to avoid ambiguity.

### Expected file tree for this sub-area

> Note: Example domain folders below are illustrative; presence/absence is **not confirmed in repo**.

~~~text
📁 data/
├── 📁 raw/
│   ├── 📄 README.md                         # This file (raw layer rules)
│   ├── 📁 <domain>/                         # e.g., air-quality/, hydrology/, landcover/, terrain/ (examples)
│   │   ├── 📄 README.md                     # Domain raw index (recommended)
│   │   └── 📁 <dataset_or_source>/          # Dataset/source grouping (recommended)
│   │       ├── 📁 <snapshot>/               # Date/version bucket (recommended)
│   │       │   ├── 📄 <source_artifact>     # “As received” file(s) or pointer(s)
│   │       │   ├── 📄 checksums.sha256      # Checksums for artifacts (recommended)
│   │       │   └── 📄 snapshot.meta.yml     # Minimal capture metadata (recommended)
│   │       └── 📄 README.md                 # Dataset/source-level notes (recommended)
│   └── 📁 _quarantine/                      # Optional: fails validation / pending review (not confirmed in repo)
└── 📁 (siblings: work/, processed/, stac/, catalog/dcat/, prov/)
~~~

## 🧭 Context

### Why raw exists in KFM

- KFM’s pipeline is designed to be **deterministic and explainable**, with traceable lineage from inputs to outputs.

- Raw is where we preserve the **original evidence** so downstream:

  - transformations can be rerun,

  - provenance can be validated, and

  - governance can verify that no public output becomes “less restricted” than its inputs.

### Raw-layer invariants

These invariants are treated as “must not break” unless the Master Guide is updated accordingly:

- **Append-only:** do not mutate or overwrite raw snapshots.

- **No hand edits:** any “fix” must be represented as a new snapshot/version with its own metadata + checksums.

- **Capture the minimum to reproduce:** at least source identity, retrieval time, license/terms (or best-known terms), and checksums.

- **No secrets:** credentials, API keys, tokens must never be committed; use secure runtime configuration.

- **Sensitivity propagation:** if a raw input is sensitive/restricted, downstream outputs must not reduce restriction without governance review.

### When to add something to raw vs sources vs work

- Put in **raw**:

  - immutable snapshots (files, exports, dumps) and/or *pointer files* to externally stored large assets.

- Put in **work**:

  - normalized tables, reprojected rasters, cleaned joins—anything derived from raw.

- Put in **sources** (if present; **not confirmed in repo**):

  - registries/manifests describing upstream sources and access patterns (not the raw bytes themselves).

## 🗺️ Diagrams

### Canonical data flow with raw landing

~~~mermaid
flowchart LR

  S["External Source Systems"] --> R["data/raw/ (landed snapshots)"]
  R --> W["data/work/ (normalize/clean)"]
  W --> P["data/processed/ (certified outputs)"]

  P --> STAC["data/stac/ (STAC)"]
  P --> DCAT["data/catalog/dcat/ (DCAT)"]
  P --> PROV["data/prov/ (PROV)"]

  STAC --> G["Graph (Neo4j ingest)"]
  DCAT --> G
  PROV --> G

  G --> API["APIs (contract boundary)"]
  API --> UI["UI (React/MapLibre)"]
  UI --> SN["Story Nodes"]
  SN --> FM["Focus Mode"]
~~~

## 🧠 Story Node & Focus Mode Integration

### How raw should (and should not) surface

- Raw artifacts are primarily **internal evidence**.

- Story Nodes and Focus Mode should cite:

  - certified datasets (`data/processed/**`),

  - catalog records (`data/stac/**`, `data/catalog/dcat/**`), and

  - provenance (`data/prov/**`) that links back to raw.

- Avoid exposing raw directly in UI/Focus Mode unless explicitly approved by governance, and only with sensitivity-aware generalization/redaction.

### Provenance-linked narrative rule

- Any narrative claim must trace to an identifiable dataset/record/asset ID.

- Raw snapshots support this by providing stable checksums/identifiers that PROV can reference.

## 🧪 Validation & CI/CD

### Validation steps (recommended for any raw additions)

- [ ] Raw snapshot is added as a new directory/version (no overwrite).

- [ ] Checksums exist for all new artifacts (or pointer targets) and are recorded.

- [ ] Source license/terms are captured (or explicitly marked unknown with a follow-up ticket).

- [ ] Minimal capture metadata exists (retrieval time, source ID, method, parameters).

- [ ] Secret scan passes (no tokens/keys in files).

- [ ] PII / sensitive-location risk is assessed (especially if raw contains precise coordinates or personal data).

### CI expectations (if configured)

- Markdown protocol validation for this README (front-matter, required sections, footer refs).

- Secret scanning / PII scanning (if enabled in CI).

- Provenance checks downstream: any promotion from raw → processed should be accompanied by PROV linkage.

> Repo-specific commands and validators are **not confirmed in repo**; document them here once tool paths are finalized (e.g., under `tools/` or `src/pipelines/`).

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source artifacts | mixed (CSV/JSON/GeoJSON/NetCDF/TIFF/etc.) | External providers | Checksums; format sanity; license recorded |
| Source docs/metadata | text/PDF/web exports | Provider documentation | Capture title, publisher, license/terms, retrieval date |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Landed raw artifacts | mixed | `data/raw/**` | Immutable snapshot + checksums |
| Minimal capture metadata | YAML/JSON/MD | `data/raw/**` | Must be sufficient to reproduce retrieval |
| Pointer files (large assets) | text | `data/raw/**` | Must include stable external URI + checksum (recommended) |

### Minimal snapshot metadata (recommended)

This is a recommended sidecar schema to keep raw “reproducible enough” without over-engineering:

~~~yaml
source_id: "<domain>:<provider>:<dataset>"
retrieved_at: "YYYY-MM-DDTHH:MM:SSZ"
retrieval_method: "http_download | api_export | manual_archive | other"
upstream_terms:
  license: "<SPDX id or URL or 'unknown'>"
  attribution: "<required attribution text if known>"
artifacts:
  - path: "<filename-or-pointer>"
    sha256: "<sha256>"
notes: "<anything important: auth used? pagination? query params?>"
~~~

If your domain uses a richer per-source registry JSON, ensure it at least contains:

- `id`, `title`, `description`, `license`, `providers`, `assets` (URLs/formats/checksums), `spatial`, `temporal`, `provenance`, `stac_version`.

### What does *not* belong in raw

- Any transformed/reprojected/cleaned output.

- Any derived aggregate that is intended for UI use.

- Any credentials, tokens, secrets, or private keys.

- Any “fixed” version of a raw file (instead: add a new snapshot and document why).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- STAC should represent **certified outputs** (usually `data/processed/**`) as Collections/Items with Assets.

- Raw artifacts may be referenced as supporting assets only if appropriate for licensing and sensitivity.

### DCAT

- DCAT dataset/distributions should be derived from the same authoritative metadata used for STAC.

- Raw sources are typically not published as public DCAT distributions unless governance explicitly approves.

### PROV-O

- Provenance must link:

  - certified entities back to raw entities (checksums enable stable identity), and

  - transformation activities (ETL runs) that used/generate them.

### Versioning

- Prefer versioned snapshot folders and checksum manifests so downstream PROV can reference exact inputs.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Configs + run logs + provenance |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j | Ingest fixtures + API layer |
| APIs | Serve contracts; enforce redaction | REST/GraphQL |
| UI | Map + narrative | API calls only (no direct graph access) |
| Story Nodes | Curated narrative | Evidence/provenance-linked |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Raw-layer contract to downstream stages

- Downstream stages may assume:

  - raw snapshots are immutable once committed,

  - snapshot metadata exists for reproducibility,

  - checksums are present (or explicitly waived with justification).

- Downstream stages must ensure:

  - classification/sensitivity does not get relaxed in derived outputs without governance review,

  - provenance is emitted and points back to raw snapshot inputs.

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review should occur when:

- a new raw source is introduced (license/terms and sensitivity must be evaluated),

- a source changes its terms or access pattern (may impact publication),

- any raw input contains (or could imply) restricted locations, culturally sensitive knowledge, or PII,

- any change would expand what is exposed through catalogs, APIs, or UI.

(Approver roles/process are **not confirmed in repo**; follow `docs/governance/ROOT_GOVERNANCE.md`.)

### CARE / sovereignty considerations

- Treat culturally sensitive or sovereignty-controlled information as **high-risk by default**.

- Prefer aggregation/generalization in downstream products; do not publish precise sensitive coordinates.

- Ensure `docs/governance/SOVEREIGNTY.md` is consulted for any affected communities/jurisdictions.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.

- Prohibited: generating new policy; inferring sensitive locations from raw artifacts (directly or indirectly).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `data/raw/` README defining raw-layer rules and linkage to downstream catalogs | TBD |

---

### Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`

- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`

- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`

- Governance: `docs/governance/ROOT_GOVERNANCE.md`

- Ethics: `docs/governance/ETHICS.md`

- Sovereignty: `docs/governance/SOVEREIGNTY.md`

