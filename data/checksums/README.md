---
title: "KFM Data Checksums — README"
path: "data/checksums/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:checksums:readme:v1.0.0"
semantic_document_id: "kfm-data-checksums-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:checksums:readme:v1.0.0"
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

# KFM Data Checksums — README

## 📘 Overview

### Purpose
This directory is the canonical home for checksum manifests that support **integrity verification** of data artifacts in the KFM repository.

Checksums are used to:
- Detect accidental corruption or unintended changes to data files.
- Support reproducible pipelines by enabling “verify inputs/outputs match expected bytes”.
- Provide an auditable integrity signal that can be referenced by ETL logs, catalogs, and validation gates.

### Scope
| In Scope | Out of Scope |
|---|---|
| Checksums for files under `data/` (raw/work/processed/stac outputs, reports, etc.) | Dependency/SBOM hashes (handled elsewhere) |
| Manifests intended for CI verification | Secret material, credentials, or private keys |
| Dataset-level or run-level checksum bundles | Checksums for external systems not stored in this repo |

### Audience
- Primary: Data pipeline maintainers, catalog maintainers, CI maintainers
- Secondary: Reviewers, historians/editors verifying provenance bundles, downstream consumers mirroring KFM data

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: checksum, manifest, integrity, deterministic, provenance

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/checksums/README.md` | TBD | Orientation + conventions |
| Checksum manifests | `data/checksums/...` | TBD | See “Directory Layout” + “Conventions” |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are explicit
- [ ] Naming + format conventions documented (with “not confirmed in repo” clearly marked where applicable)
- [ ] Validation steps are listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `data/checksums/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs per domain |
| Catalog outputs | `data/stac/` | STAC collections + items |
| Lineage outputs | `data/prov/` | PROV bundles (if present) |
| Pipelines | `src/pipelines/` | ETL/catalog generation code (not confirmed in repo) |
| CI | `.github/` | Validation actions/workflows (not confirmed in repo) |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 checksums/
    └── 📄 README.md
~~~

> Reserved expansion (not confirmed in repo): per-domain or per-stage manifests (e.g., `raw/`, `processed/`, `stac/`) and/or per-release manifests.

## 🧭 Context

### Background
KFM’s pipeline is designed to be reproducible and provenance-forward. Checksums are a lightweight, tool-agnostic integrity mechanism that can be referenced by:
- ETL runs (to prove which bytes were ingested and produced),
- catalog artifacts (to validate that referenced assets haven’t drifted),
- CI gates (to prevent silent corruption).

### Assumptions
- Checksum files are treated as **derived artifacts** and are updated when the corresponding data artifacts change.
- The repository may include both human-curated and pipeline-generated data; checksum practices must work for both.

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes data through API contracts; checksums do **not** introduce direct UI → graph coupling.
- No secrets/credentials in checksum manifests.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical checksum algorithm (SHA-256 recommended; confirm actual) | TBD | TBD |
| Are manifests generated in CI, locally, or by ETL runs (or all three)? | TBD | TBD |
| Should manifests be per-domain, per-run, or per-release? | TBD | TBD |

### Future extensions
- Add a validator that ensures checksum manifests:
  - cover all required artifacts for a dataset release,
  - have no orphan entries,
  - match the canonical algorithm and formatting.
- Align checksum values with STAC asset metadata where applicable (not confirmed in repo).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL outputs under data/] --> B[Checksum manifest generation]
  B --> C[CI verifies manifests]
  A --> D[STAC/DCAT/PROV catalogs]
  D --> C
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Data files to checksum | any (binary/text) | `data/**` | File exists + stable path |
| Manifest rules | documented conventions | this README | Lint + deterministic ordering |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Checksum manifest(s) | text | `data/checksums/**` | This README (format rules below) |

### Sensitivity & redaction
- Checksums are typically non-sensitive, but **filenames/paths can be sensitive** if they reveal restricted site locations or culturally sensitive material.
- If a dataset contains restricted/sensitive location identifiers, prefer:
  - opaque IDs in file naming, and/or
  - storing restricted bundles outside public distribution channels (requires human review).

### Quality signals
- Completeness: required files are covered by a manifest.
- Determinism: manifest ordering is stable (e.g., lexical sort by path).
- Verifiability: a standard tool can verify the manifest without custom code.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If STAC Items reference assets stored in-repo, checksum manifests can serve as an integrity backstop for those assets.
- If the repo adopts a STAC checksum mechanism/extension, manifest values should match (not confirmed in repo).

### DCAT
- Dataset releases may link to checksum manifests as “distribution integrity metadata” (implementation not confirmed in repo).

### PROV-O
- Where PROV bundles exist, checksum manifests can be referenced as evidence of the exact bytes used/produced by an activity.
  - `prov:wasDerivedFrom`: input data identifiers
  - `prov:wasGeneratedBy`: run/activity identifier
  - (How/where run IDs are recorded is not confirmed in repo.)

### Versioning
- When data artifacts change, update checksum manifests in the same change set.
- Prefer stable IDs/paths; avoid churn that breaks downstream mirroring.

## 🧱 Architecture

### Recommended manifest format (not confirmed in repo)
A plain-text format compatible with common tooling is recommended:

- One line per file:
  - `<hex-digest><two-spaces><relative-path>`
- Relative paths are from repo root (use forward slashes).
- Use a deterministic sort order by path.

Example (illustrative only):
~~~text
<sha256-hex>  data/processed/example-dataset/example.parquet
<sha256-hex>  data/stac/items/example-item.json
~~~

## 🧠 Story Node & Focus Mode Integration

Checksums are an **integrity layer**, not narrative content. They may indirectly support Focus Mode by:
- preventing drift between narrative references and underlying artifacts,
- enabling auditors/reviewers to validate that cited evidence assets match expected bytes.

## 🧪 Validation & CI/CD

### Validation steps (examples; tooling not confirmed in repo)
~~~bash
# Example: generate SHA-256 checksums (POSIX)
# sha256sum data/processed/... > data/checksums/<manifest>.sha256

# Example: verify a manifest (POSIX)
# sha256sum -c data/checksums/<manifest>.sha256
~~~

### Validation checklist
- [ ] Manifest uses the canonical algorithm (confirm which)
- [ ] Manifest paths are relative + repo-stable
- [ ] Manifest is deterministically ordered
- [ ] Verification step succeeds in CI (if configured)

## ⚖ FAIR+CARE & Governance

### Review gates
- If manifests include or reveal sensitive location identifiers:
  - FAIR+CARE council review: TBD
  - Security council review: yes (recommended)
  - Historian/editor review: yes (recommended)

### CARE / sovereignty considerations
- Avoid leaking sensitive sites via filenames/paths embedded in manifests.
- Apply redaction/generalization rules when required (requires human review).

### AI usage constraints
- AI must not infer or reconstruct sensitive locations from checksum or filename patterns.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `data/checksums/` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`