---
title: "KFM Data Archive — Releases"
path: "data/archive/releases/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:data:archive:releases:readme:v1.0.0"
semantic_document_id: "kfm-data-archive-releases-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:archive:releases:readme:v1.0.0"
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

# KFM Data Archive — Releases

## 📘 Overview

### Purpose
This directory stores **versioned “release snapshots”** of KFM archival bundles and their associated
release metadata. A *release* is intended to represent a stable point-in-time packaging of archival
artifacts that can be referenced by provenance (PROV), catalogs (STAC/DCAT), and downstream consumers
(e.g., API/UI deployments) without ambiguity.

> Note: The exact release mechanics (signing, publishing, CI jobs, semantic versioning scheme) are **not confirmed in repo**.
> This README defines a recommended structure that keeps the canonical pipeline ordering intact.

### Scope

| In Scope | Out of Scope |
|---|---|
| Release folders (version/date keyed) | ETL logic and transforms (owned by `src/pipelines/`) |
| Release metadata + pointers to manifests/bundles | Neo4j graph schema/migrations |
| Checksums + integrity expectations for packaged artifacts | Public API endpoint definitions (owned by `src/server/` + docs) |
| Provenance-friendly, immutable release conventions | Any policy requiring legal/security approval (tracked elsewhere) |

### Audience
- Primary: Data maintainers, archivists, release engineers
- Secondary: CI/CD maintainers, catalog/graph/API integrators

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: **release**, **bundle**, **manifest**, **checksum**, **immutability**, **provenance**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Archive root README | `data/archive/README.md` | Data | Explains archive philosophy + boundaries |
| Bundle manifests | `data/archive/manifests/` | Data | Machine-readable list of bundles/assets |
| Bundles | `data/archive/bundles/` | Data | Packaged payloads (zips/tars/dirs) |
| Archive notes | `data/archive/notes/` | Data | Human notes: release rationale, caveats |
| Checksums | `data/checksums/` | Data/CI | Repository-level checksums (cross-cutting) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Explains *what a release is* and *how releases relate to manifests/bundles/checksums*
- [ ] Lists a clear, lintable directory convention for releases
- [ ] Identifies provenance (STAC/DCAT/PROV) expectations at a high level
- [ ] States governance and sensitivity assumptions (no sensitive locations inferred)

## 🗂️ Directory Layout

### This document
- `path`: `data/archive/releases/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Archive releases | `data/archive/releases/` | Versioned release snapshots + metadata |
| Manifests | `data/archive/manifests/` | Bundle inventories + file lists |
| Bundles | `data/archive/bundles/` | Actual packaged data artifacts |
| Notes | `data/archive/notes/` | Human-readable release notes / decisions |
| Checksums | `data/checksums/` | Hash inventories (optionally per release) |
| STAC outputs | `data/stac/` | STAC collections/items for discoverability |
| PROV outputs | `data/prov/` | Lineage bundles to support traceability |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 archive/
    ├── 📁 releases/
    │   ├── 📄 README.md
    │   ├── 📁 <release_id>/
    │   │   ├── 📄 release.json
    │   │   ├── 📄 release_notes.md
    │   │   ├── 📄 manifest.ref
    │   │   └── 📄 checksums.ref
    │   └── 📁 <release_id>/
    │       └── 📄 ...
    ├── 📁 manifests/
    │   └── 📄 README.md
    ├── 📁 bundles/
    │   └── 📄 README.md
    └── 📁 notes/
        └── 📄 README.md
~~~

**Conventions (recommended; not confirmed in repo):**
- `<release_id>` SHOULD be one of:
  - `v<semver>` (e.g., `v1.2.0`), or
  - `YYYY-MM-DD` (e.g., `2025-12-20`), or
  - `YYYY-MM-DD__<short-label>` (e.g., `2025-12-20__baseline-stac-refresh`)
- Release directories SHOULD be treated as **immutable** once published. If something must change, create a new release.

## 🧭 Context

### Background
KFM’s canonical flow requires deterministic, provenance-linked outputs from ETL through catalogs, graph, APIs, UI, and story nodes.
Releases provide a stable **distribution boundary** for archived artifacts (bundles/manifests/checksums) so that:
- CI can validate integrity and reproducibility,
- catalogs and provenance can reference a known snapshot,
- downstream deployments can pin to an exact archival state.

### Assumptions
- Releases are **pointers** to bundles/manifests/checksums rather than duplicating them (preferred to avoid repository bloat).
- Release metadata is structured (JSON) and can be validated in CI (**not confirmed in repo**).
- No sensitive location inference is performed as part of release packaging.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- UI/clients do not read Neo4j directly; releases do not bypass the API boundary.
- No secrets, credentials, or personal data are stored in release metadata.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should `<release_id>` be semver or date-based (or both)? | TBD | TBD |
| Do we sign releases (e.g., Sigstore/cosign) or only hash them? | TBD | TBD |
| Should `release.json` embed STAC/DCAT/PROV references or only point to them? | TBD | TBD |
| Where do “published” releases live (repo-only vs GitHub Releases vs external storage)? | TBD | TBD |

### Future extensions
- Add a CI gate that validates `release.json` structure, and checks that `manifest.ref` and `checksums.ref` resolve.
- Add an optional “release index” file for discovery across releases (e.g., `releases.index.json`).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL Outputs] --> B[Archive Bundles]
  B --> C[Bundle Manifests]
  C --> D[Release Snapshot Metadata]
  D --> E[STAC/DCAT/PROV references]
  E --> F[Graph & API consumers]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Bundle payloads | zip/tar/dir | `data/archive/bundles/` | checksum match, optional schema checks |
| Bundle manifest(s) | JSON/YAML | `data/archive/manifests/` | schema + referential integrity |
| Checksums | txt/JSON | `data/checksums/` | hash verification |
| Human notes | Markdown | `data/archive/notes/` | doc lint |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Release metadata | JSON | `data/archive/releases/<release_id>/release.json` | **not confirmed in repo** (recommend JSON Schema) |
| Release notes | Markdown | `data/archive/releases/<release_id>/release_notes.md` | Markdown lint |
| Manifest pointer | text | `data/archive/releases/<release_id>/manifest.ref` | must resolve |
| Checksums pointer | text | `data/archive/releases/<release_id>/checksums.ref` | must resolve |

### Sensitivity & redaction
- Release metadata SHOULD NOT contain:
  - restricted coordinates
  - personally identifying information (PII)
  - secrets/tokens/credentials
- If any archival bundle includes sensitive content, the release must reference the applicable governance controls (**not confirmed in repo**).

### Quality signals
- Checksums verified
- Manifests resolve to actual bundle assets
- No broken references to STAC/DCAT/PROV outputs

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Releases MAY include references to STAC Collection/Item IDs that correspond to archived assets (preferred: references, not copies).

### DCAT
- Releases MAY reference DCAT dataset identifiers for the snapshot boundary (e.g., “dataset version X”).

### PROV-O
- Releases SHOULD be attributable to a `prov:Activity` (e.g., “archive-release-build”) and list `prov:wasDerivedFrom` pointers (manifests, checksums, bundle IDs).

### Versioning
- A new release should supersede prior releases via explicit predecessor/successor links in metadata (**not confirmed in repo**).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Bundles | Store packaged payloads | File paths + checksums |
| Manifests | Inventory what’s in bundles | JSON/YAML + schema |
| Releases | Snapshot metadata + pointers | release.json + *.ref |
| Catalogs | Discoverability + metadata | STAC/DCAT/PROV outputs |
| CI | Validate integrity | actions/workflows (**not confirmed in repo**) |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Release metadata schema | `schemas/` (**not confirmed in repo**) | semver + changelog |
| Manifest schema | `schemas/` (**not confirmed in repo**) | semver + changelog |
| Checksums format | `data/checksums/` | stable + backward compatible |

### Extension points checklist (for future work)
- [ ] Add `schemas/archive/release.schema.json` (**not confirmed in repo**)
- [ ] Add CI validation action to enforce schema + referential integrity
- [ ] Add a release index for browsing/automation

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Releases are not a narrative artifact themselves, but they enable reproducible story-node inputs by pinning archival source bundles.

### Provenance-linked narrative rule
Any Story Node referencing archival content should be able to cite the release (directly or indirectly via PROV/STAC asset IDs).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks for `release_notes.md`
- [ ] `release.json` validates against schema (**not confirmed in repo**)
- [ ] `manifest.ref` resolves to an existing manifest
- [ ] `checksums.ref` resolves to an existing checksum inventory
- [ ] Bundle files referenced in manifests exist and match checksums
- [ ] No sensitive content leakage in metadata

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate release schema
# 2) validate manifest references
# 3) verify checksums
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| release_build_id | CI | `mcp/runs/` or `docs/telemetry/` (**not confirmed in repo**) |

## ⚖ FAIR+CARE & Governance

### Review gates
- If a release includes or points to sensitive materials:
  - FAIR+CARE council review: **TBD**
  - Security council review: **TBD**
  - Historian/editor review: **TBD**

### CARE / sovereignty considerations
- If archival bundles include culturally sensitive sites or materials, apply generalization/redaction controls and document them.

### AI usage constraints
- No release process should infer or enrich sensitive locations beyond what is explicitly present in governed source data.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for archive releases directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
