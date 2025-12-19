---
title: "KFM — Archive Manifests (data/archive/manifests)"
path: "data/archive/manifests/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:data:archive:manifests:readme:v1.0.0"
semantic_document_id: "kfm-data-archive-manifests-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:archive:manifests:readme:v1.0.0"
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

# KFM — Archive Manifests

## 📘 Overview

### Purpose
This directory holds **machine-readable manifest files** that describe archived data bundles (snapshots/releases) tracked under `data/archive/`. Manifests exist to make archives **auditable, reproducible, and integrity-checkable** without requiring inference or “tribal knowledge”.

### Scope
| In Scope | Out of Scope |
|---|---|
| Manifest file conventions (naming, minimum fields, validation expectations) | The full archive creation procedure (documented elsewhere) |
| How manifests relate to checksums + PROV lineage | Where large/binary archive payloads are hosted/stored |
| Guidance for linking manifests to STAC/DCAT/PROV outputs | Any policy creation beyond referenced governance docs |

### Audience
- Primary: Data/pipeline maintainers, release managers
- Secondary: Researchers/analysts validating reproducibility; reviewers auditing provenance

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Archive bundle**: An immutable snapshot of a dataset/domain output (and/or inputs) at a known point in time.
  - **Manifest**: A machine-readable inventory of an archive bundle’s contents + identifiers + integrity hashes.
  - **Archive ID**: A stable identifier used to relate an archive bundle, its manifest, and lineage records.
  - **Content hash**: Cryptographic digest (e.g., sha256) used to detect tampering or accidental changes.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Archive root | `data/archive/` | DataOps (TBD) | Archived bundles + supporting materials |
| This manifests directory | `data/archive/manifests/` | DataOps (TBD) | One manifest per archived bundle (recommended) |
| Checksums store | `data/checksums/` | DataOps (TBD) | Repository-wide integrity artifacts (see its README) |
| PROV outputs | `data/prov/` | Pipeline owners (TBD) | W3C PROV-O exports for lineage alignment |
| STAC outputs | `data/stac/` | Catalog build owners (TBD) | Collections/items for geospatial assets |
| DCAT outputs | `data/catalog/dcat/` | Catalog build owners (TBD) | DCAT dataset-level catalogs |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Conventions clearly state what belongs here vs. elsewhere
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/archive/manifests/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Archive root | `data/archive/` | Archived bundle materials + readme(s) |
| Manifests | `data/archive/manifests/` | Manifests describing archived bundles |
| Checksums | `data/checksums/` | Hash inventories and checksum references |
| Raw/work/processed | `data/<domain>/{raw,work,processed}/` | Domain-scoped datasets by lifecycle stage |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | STAC/DCAT/PROV exports |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 archive/
    ├── 📄 README.md
    └── 📁 manifests/
        ├── 📄 README.md
        ├── 📄 <archive_id>.manifest.json
        └── 📄 <archive_id>.manifest.json.sha256   (optional; see data/checksums/)
~~~

## 🧭 Context

### Background
Archives are only useful if they can be validated later. A manifest provides the “index card” for an archive: *what it contains, what identifiers it corresponds to, how to verify integrity, and how it ties back to provenance and catalogs*.

### Assumptions
- This repository maintains (or will maintain) a stable notion of **archive IDs**.
- A manifest schema is **not confirmed in repo** at the time this README is authored; this document defines *minimum expectations* and a *recommended structure* until a formal schema is added under `schemas/`.

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend/UI must consume data through **API contracts** (no direct graph reads).
- Manifests must not include secrets, credentials, or unnecessary PII. Redact/generalize sensitive locations per governance/sovereignty rules.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should manifests be validated by a JSON Schema under `schemas/`? | TBD | TBD |
| Where are large/binary archive payloads stored (git/LFS/external)? | TBD | TBD |
| What is the canonical `archive_id` format? | TBD | TBD |

### Future extensions
- Add `schemas/archive/archive-manifest.schema.json` and a CI gate to validate manifests.
- Add a generator tool that outputs: manifest + checksum refs + PROV activity stub.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL run outputs] --> B[data/archive/ bundle]
  B --> C[data/archive/manifests/ manifest.json]
  A --> D[STAC/DCAT/PROV catalogs]
  D --> C
  D --> E[Neo4j Graph]
  E --> F[APIs]
  F --> G[UI / Story Nodes]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Archive bundle (snapshot) | directory / tar / zip (TBD) | `data/archive/` | Existence + integrity via hashes |
| Checksums | sha256 text (recommended) | `data/checksums/` or local to archive | Hash matches manifest inventory |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Archive manifest | JSON | `data/archive/manifests/<archive_id>.manifest.json` | **Not confirmed in repo** (recommended structure below) |

### Sensitivity & redaction
- Do **not** embed secrets, tokens, credentials, or private access URLs in a manifest.
- If a file path reveals a sensitive location or protected site, generalize or omit as required by:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`

### Quality signals
- Each inventory entry has: stable relative path, size (bytes), sha256, and a role/category.
- No duplicate paths.
- Manifest references (where applicable) the relevant STAC/DCAT/PROV identifiers used elsewhere in the pipeline.

### Recommended manifest structure (until schema exists)
> This is a recommended shape only; update once a formal schema is added under `schemas/`.

~~~json
{
  "manifest_version": "1.0",
  "archive_id": "urn:kfm:archive:<tbd>",
  "created_at": "YYYY-MM-DD",
  "created_by": "TBD",
  "description": "TBD",
  "bundle": {
    "path_or_uri": "data/archive/<tbd>",
    "byte_size_total": 0
  },
  "integrity": {
    "hash_algorithm": "sha256",
    "checksums_ref": "data/checksums/<tbd>.sha256"
  },
  "inventory": [
    {
      "path": "data/<domain>/processed/<file>",
      "bytes": 0,
      "sha256": "<hex>",
      "media_type": "application/json",
      "role": "processed"
    }
  ],
  "catalog_refs": {
    "stac_collections": [],
    "stac_items": [],
    "dcat_datasets": [],
    "prov_entities": [],
    "prov_activities": []
  },
  "build_context": {
    "commit_sha": "<latest-commit-hash>",
    "pipeline_run_id": "TBD"
  },
  "notes": []
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: **TBD**
- Items involved: **TBD**
- Extension(s): **TBD**

### DCAT
- Dataset identifiers: **TBD**
- License mapping: **TBD**
- Contact / publisher mapping: **TBD**

### PROV-O
- `prov:wasDerivedFrom`: **TBD**
- `prov:wasGeneratedBy`: **TBD**
- Activity / Agent identities: **TBD**

### Versioning
- Prefer stable identifiers (archive_id, dataset IDs) and immutable integrity hashes.
- If version chains exist, link them via catalog/provenance records (STAC versioning links; PROV relations).

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Manifests can serve as audit artifacts when a Story Node cites a dataset version/archive.
- If used, reference the **archive_id** and any catalog/provenance identifiers, not ad-hoc filenames.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (and the manifest can support auditability for those assets).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (formatting, links)
- [ ] If/when a schema exists: validate `*.manifest.json` against `schemas/...`
- [ ] Verify referenced `checksums_ref` exists (if used)
- [ ] Verify each `inventory.path` exists in the referenced archive bundle context
- [ ] Verify `inventory.sha256` matches actual file digest (tooling TBD)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands/tools
# 1) validate manifest JSON (if schema exists)
# 2) verify sha256 inventory
# 3) verify referenced catalogs/prov IDs exist (optional)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Requires human review if a manifest change:
  - alters integrity hashes
  - changes archive identity/version
  - includes/risks sensitive or sovereignty-protected information

### CARE / sovereignty considerations
- Identify impacted communities and protection rules (see governance refs).
- Do not “reconstruct” or infer sensitive locations; store only approved/generalized representations.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use (no policy generation; no sensitive location inference).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for archive manifests directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

