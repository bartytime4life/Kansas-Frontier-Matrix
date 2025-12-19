---
title: "KFM Data Archive"
path: "data/archive/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:archive:readme:v1.0.0"
semantic_document_id: "kfm-data-archive-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:archive:readme:v1.0.0"
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

# KFM Data Archive

## 📘 Overview

### Purpose
`data/archive/` is the repository location for **frozen, read-only archival bundles** that support reproducibility, auditability, and long-term reference of KFM inputs and outputs.

This directory is intended to hold **snapshotted artifacts** that should not be edited in-place after creation (e.g., “the exact files used for a published Story Node or catalog release”).

### Scope

| In Scope | Out of Scope |
|---|---|
| Immutable snapshots of source bundles, derived products, or release bundles | Active ETL work-in-progress |
| Manifests and integrity metadata that allow later verification | Day-to-day working files (`data/work/`) |
| Versioned exports used for citation or external publication | Ad-hoc scratch outputs or experiments (use `mcp/` for experiments) |

### Audience
- Primary: Data maintainers, pipeline maintainers, catalog/graph maintainers
- Secondary: Reviewers, auditors, historians/editors validating provenance, release managers

### Definitions
- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Archive bundle**: A read-only snapshot of data + metadata required to reproduce or validate a downstream artifact.
  - **Manifest**: A machine-readable inventory of a bundle (filenames, sizes, hashes, identifiers).
  - **Integrity**: The ability to verify that a bundle’s content has not changed (typically via checksums).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Archive bundles | `data/archive/…` | Data maintainers | Should be immutable once committed |
| Checksums / hash manifests | `data/checksums/…` | CI + maintainers | See `data/checksums/README.md` (if present) |
| Provenance bundles | `data/prov/…` | Pipeline maintainers | Archive may copy or reference PROV artifacts |
| Catalog snapshots | `data/stac/…` + `data/catalog/dcat/…` | Catalog maintainers | Archive may store a release snapshot |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Archive intent clearly stated (read-only / immutable expectation)
- [ ] Recommended structure does not imply non-existent folders (“not confirmed in repo” used when needed)
- [ ] Validation and reproducibility steps described without inventing repo commands

## 🗂️ Directory Layout

### This document
- `path`: `data/archive/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/raw/`, `data/work/`, `data/processed/` | Active ingestion/normalization and derived datasets |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV outputs |
| Checksums | `data/checksums/` | Integrity artifacts (hash lists/manifests) |
| Documentation | `docs/` | Canonical governed docs and templates |
| Pipelines | `src/pipelines/` | ETL + catalog + graph build logic |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
> The following layout is **recommended** for clarity and reproducibility. Subfolders beyond `README.md` are **not confirmed in repo** unless they already exist.

~~~text
📁 data/
└── 📁 archive/
    ├── 📄 README.md
    ├── 📁 manifests/              # not confirmed in repo
    ├── 📁 bundles/                # not confirmed in repo
    ├── 📁 releases/               # not confirmed in repo
    └── 📁 notes/                  # not confirmed in repo
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline produces artifacts (datasets, catalogs, graph extracts, story nodes) that may need to be **referenced exactly as they existed at a point in time** for:
- provenance verification,
- reproducibility,
- releases and citations,
- rollback and audit investigations.

This archive directory is a stable place to store those time-frozen bundles without mixing them into active pipeline staging.

### Assumptions
- Archived artifacts are treated as **read-only** after creation.
- Any “update” to an archived artifact is done by creating a **new archive bundle** (new version / new timestamp), not by editing in place.
- Large binaries may require special handling (e.g., external object storage or Git LFS) depending on repo policy (not confirmed in repo).

### Constraints / invariants
- The canonical pipeline ordering is preserved:
  - **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- Archive is **supporting infrastructure**, not a shortcut:
  - do not run UI/graph workloads directly from `data/archive/`
  - do not bypass API contracts using archived copies

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the official archive naming convention (date, semver, or both)? | TBD | TBD |
| Are archive bundles permitted to include restricted/sensitive material? | TBD | TBD |
| What size limits apply to committed archive bundles? | TBD | TBD |

### Future extensions
- Add a standard archive manifest schema under `schemas/` (not confirmed in repo).
- Add CI validation that archive bundles include checksums + provenance references (not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL Outputs] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Graph + APIs + UI Artifacts]
  C --> D[Published/Referenced Release]
  D --> E[data/archive Snapshot Bundle]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source bundle snapshot | files/zip/tar (TBD) | `data/raw/` or external sources | checksums + manifest |
| Catalog snapshot | JSON / JSON-LD / Turtle | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | schema validation (where applicable) |
| Release notes | Markdown / YAML (TBD) | release process | lint + required fields |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Archive bundle | folder or compressed artifact | `data/archive/<bundle_id>/...` | manifest (recommended) |
| Manifest | JSON/YAML/TXT (TBD) | `data/archive/manifests/...` (recommended) | not confirmed in repo |
| Integrity hashes | SHA256 list (recommended) | `data/checksums/...` | not confirmed in repo |
| Provenance reference | PROV IDs/links | manifest fields | PROV-O alignment |

### Sensitivity & redaction
- If archived bundles include any restricted locations or culturally sensitive content:
  - ensure they follow sovereignty and governance rules,
  - avoid publishing precise sensitive coordinates in public artifacts,
  - do not add new inferences (especially about sensitive locations).

### Quality signals
Recommended (not confirmed in repo):
- checksums for every archived file,
- a manifest containing:
  - stable identifiers (dataset IDs, STAC item IDs),
  - the generating pipeline run/activity ID,
  - input references (prov:wasDerivedFrom).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
If archiving catalog outputs:
- Archive should include the exact STAC Collection/Item JSON used or released.
- Prefer storing STAC as plain JSON to preserve discoverability and diffability.

### DCAT
If archiving dataset catalog views:
- Archive should include the DCAT record and the referenced distribution assets (or clear pointers to them).

### PROV-O
Archive bundles should preserve lineage by recording:
- `prov:wasDerivedFrom`: source dataset/document IDs
- `prov:wasGeneratedBy`: pipeline activity / run ID
- `prov:wasAttributedTo`: agent (pipeline/maintainer identity) where appropriate

### Versioning
Recommended (not confirmed in repo):
- Use an archive bundle identifier that includes:
  - a timestamp (e.g., `YYYY-MM-DD`),
  - a semver tag for the bundle schema/content.
- Never “rewrite history” — add a successor bundle instead.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | configs + run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON/JSON-LD/Turtle + validators |
| Graph | Neo4j graph build | via API layer only |
| APIs | Contracted access | REST/GraphQL |
| Archive | Immutable snapshots | bundle + manifest + checksums |

### Interfaces / contracts
- Archive is not an API surface. It is a storage location that supports:
  - reproduction,
  - auditing,
  - release packaging.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode should reference **catalog + provenance identifiers**, not raw archive file paths.
- Archive bundles are supporting evidence for:
  - “what was used to generate this story node”
  - “what catalog version was current”

### Provenance-linked narrative rule
- Archived narrative artifacts must remain consistent with:
  - the STAC/DCAT/PROV identifiers they cite,
  - the graph entities they reference.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Bundle immutability convention followed (no edits-in-place after publish)
- [ ] Manifest exists and includes stable identifiers (recommended)
- [ ] Checksums exist for all archived files (recommended)
- [ ] No secrets/credentials included
- [ ] Restricted/sensitive content handled per governance rules

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate catalogs (STAC/DCAT/PROV)
# 2) verify checksums for the archived bundle
# 3) run doc lint / markdown protocol checks
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Archive bundle creation event | CI / release pipeline | `docs/telemetry/` (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates
- If an archive bundle is intended to support a public release or a Story Node:
  - historian/editor review: recommended
  - security review: required if sensitive material is included

### CARE / sovereignty considerations
- Ensure archive content does not expose sensitive locations or culturally restricted data.
- Avoid adding derived coordinates, inferred identities, or other prohibited inferences.

### AI usage constraints
- AI may summarize or structure-extract from archived materials when allowed,
  but must not introduce new claims or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/archive/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md` (not confirmed in repo)
- Ethics: `docs/governance/ETHICS.md` (not confirmed in repo)
- Sovereignty: `docs/governance/SOVEREIGNTY.md` (not confirmed in repo)
