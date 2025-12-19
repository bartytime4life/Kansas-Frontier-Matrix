---
title: "KFM — Data Archive Bundles (README)"
path: "data/archive/bundles/README.md"
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

doc_uuid: "urn:kfm:doc:data:archive:bundles:readme:v1.0.0"
semantic_document_id: "kfm-data-archive-bundles-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:archive:bundles:readme:v1.0.0"
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

# Data Archive Bundles

## 📘 Overview

### Purpose
This directory stores **archive bundles**: immutable, portable snapshots of KFM data products and their associated metadata needed for reproducibility, transfer, and long-term retention.

Bundles are intended to **complement** (not replace) the canonical KFM data pipeline and catalogs:
ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.

### Scope

| In Scope | Out of Scope |
|---|---|
| Immutable archives of data products (and/or pointers to them) tied to a specific dataset/version/run | Day-to-day working files in `data/work/` |
| Bundles that can be verified via checksums + manifests | Rewriting/overwriting existing bundles |
| Bundles that preserve provenance linkages (STAC/DCAT/PROV references) | Storing secrets/credentials; leaking restricted locations |

### Audience
- Primary: data engineering / pipeline maintainers
- Secondary: release managers, auditors, researchers needing reproducible snapshots

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used here:
  - **Bundle**: an immutable packaged snapshot (or pointer set) representing a coherent archival unit.
  - **Manifest**: machine-readable record describing bundle contents + checksums + provenance refs.
  - **Run ID**: identifier for a specific pipeline execution that generated the bundle contents.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Archive root README | `data/archive/README.md` | DataOps | Parent conventions |
| Manifests README | `data/archive/manifests/README.md` | DataOps | Manifest format + rules |
| Checksums README | `data/checksums/README.md` | DataOps | Hash conventions + verification |

## 🗂️ Directory Layout

### This document
- `path`: `data/archive/bundles/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Archive bundles | `data/archive/bundles/` | Bundle artifacts (archives and/or pointers) |
| Bundle manifests | `data/archive/manifests/` | Manifests that describe bundles |
| Checksums | `data/checksums/` | Checksum files / hash registries |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical metadata + provenance |

### Expected file tree for this sub-area
~~~text
📁 data/
├── 📁 archive/
│   ├── 📄 README.md
│   ├── 📁 manifests/
│   │   ├── 📄 README.md
│   │   └── 🧾 <bundle_id>.manifest.(json|yaml)
│   └── 📁 bundles/
│       ├── 📄 README.md
│       ├── 📦 <bundle_id>.(tar|tar.gz|tar.zst|zip)
│       └── 🧾 <bundle_id>.bundle-metadata.(json|yaml)   # optional adjunct
└── 📁 checksums/
    ├── 📄 README.md
    └── 🔐 <bundle_id>.sha256
~~~

> Note: If this repository uses an external artifact store (or Git LFS), the `📦 <bundle_id>...` entry may be a pointer/metadata file instead of the full binary.

## 🧭 Context

### Background
KFM’s canonical pipeline emphasizes:
- deterministic, replayable ETL,
- first-class provenance (STAC/DCAT/PROV),
- and governed delivery into graph/APIs/UI.

Bundles exist to make it easier to:
- freeze “what we shipped” (data + metadata),
- reproduce a release or analysis result,
- transfer a coherent dataset slice to another environment,
- and support auditability without rewriting history.

### Assumptions
- Bundles are **immutable** once published (new bundles are new versions).
- A bundle can be validated using checksums and a manifest.
- Bundles must not bypass governance or sensitivity requirements.

### Constraints / invariants
- The canonical ordering ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Bundles do not become a shortcut around STAC/DCAT/PROV; they must reference (or include) catalog/provenance artifacts rather than replace them.
- Frontend consumes contracts via APIs (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What archive formats are allowed/preferred (e.g., `tar.zst` vs `zip`)? | TBD | TBD |
| Are binary bundles stored in-repo, via Git LFS, or external storage? | TBD | TBD |
| What is the canonical manifest schema and required fields? | TBD | TBD |

### Future extensions
- Extension point A: “release bundles” aligned with `releases/` tags.
- Extension point B: “evidence bundles” that package model/evidence artifacts with explicit uncertainty + provenance.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL Outputs / Processed Data] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Bundle Manifest]
  C --> D[Archive Bundle Artifact]
  D --> E[Restore / Verify / Reproduce]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Data products to archive | files (varies) | `data/processed/` and/or evidence outputs | domain checks + integrity |
| STAC metadata | JSON | `data/stac/` | STAC validation |
| DCAT metadata | JSON-LD/Turtle (or project format) | `data/catalog/dcat/` | schema validation |
| PROV bundle | JSON/JSON-LD (or project format) | `data/prov/` | schema validation |
| Bundle manifest | JSON/YAML | `data/archive/manifests/` | schema validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Bundle archive (or pointer) | `.tar*` / `.zip` / pointer metadata | `data/archive/bundles/` | bundle policy (this doc) |
| Bundle checksum(s) | `.sha256` (or equivalent) | `data/checksums/` | checksum policy (see README) |
| Manifest | JSON/YAML | `data/archive/manifests/` | manifest schema (TBD) |

### Sensitivity & redaction
- Do **not** include secrets, credentials, or private keys in any bundle.
- If an asset is restricted/sensitive, the bundle must either:
  - exclude it, or
  - store a redacted/generalized derivative (with clear provenance and redaction notes).
- Ensure sovereignty rules are followed before publishing bundles.

### Quality signals
- Checksums match expected values.
- Catalog artifacts validate (STAC/DCAT/PROV).
- Manifest content matches the bundle contents (file list, sizes, hashes).
- Bundle build is deterministic for a given run/config when feasible.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If the bundle contains geospatial assets, it should include or reference the relevant:
  - STAC Collection(s)
  - STAC Item(s)
- Bundle manifests should list associated STAC IDs.

### DCAT
- Bundle manifests should list DCAT dataset identifiers (where applicable) to support discovery and reuse.

### PROV-O
- Bundle manifests should reference:
  - `prov:wasDerivedFrom` source IDs (datasets/assets)
  - `prov:wasGeneratedBy` pipeline activity/run ID
  - agent/tool identifiers if available

### Versioning
- Publish a new bundle for every new dataset version or materially different run output.
- Use stable bundle IDs and do not mutate existing bundles.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | produce normalized data artifacts | configs + run logs |
| Catalogs | produce STAC/DCAT/PROV | validator outputs |
| Bundler | package artifacts into an immutable bundle | manifest + archive |
| Verifier | validate bundle integrity | checksum/manifest checks |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Bundle manifest schema | `schemas/` (recommended) | Semver + changelog |
| Bundle creation conventions | `data/archive/**/README.md` | update with version |
| Checksums conventions | `data/checksums/README.md` | update with version |

### Extension points checklist (for future work)
- [ ] Bundle manifest JSON schema added under `schemas/`
- [ ] Bundler implemented under `src/pipelines/` or `tools/`
- [ ] Verification script + CI gate added
- [ ] Storage policy documented (in-repo vs external)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Bundles may package Story Nodes or evidence products used by Focus Mode, but **Focus Mode should still consume provenance-linked content via APIs**.
- If Story Nodes are bundled, manifests should list their document IDs and linked entity IDs.

### Provenance-linked narrative rule
- Bundling narrative artifacts does not waive the requirement that all claims trace to dataset/asset IDs.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Verify checksum file(s) for the bundle
- [ ] Verify manifest is present and schema-valid
- [ ] Validate included/referenced STAC items + collections
- [ ] Validate included/referenced DCAT records
- [ ] Validate included/referenced PROV bundles
- [ ] Run security scanning rules on bundle contents (no secrets)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands once bundling tooling exists.

# 1) Verify bundle checksums
# <verify-checksums-command> data/checksums/<bundle_id>.sha256

# 2) Validate manifest schema
# <validate-manifest-command> data/archive/manifests/<bundle_id>.manifest.json

# 3) Validate STAC/DCAT/PROV artifacts referenced by the manifest
# <stac-validate-command>
# <schema-validate-command>
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If the bundle contains potentially sensitive locations, restricted cultural material, or personal data:
  - requires human review before publication.
- If the bundle is intended for public release, confirm license mapping and attribution fields are complete.

### CARE / sovereignty considerations
- Ensure bundling does not inadvertently increase the precision of sensitive locations beyond what is permitted.

### AI usage constraints
- Bundles may include AI-generated artifacts only when they are:
  - explicitly permitted by governance,
  - provenance-linked,
  - and labeled with uncertainty/confidence where applicable.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for archive bundle conventions | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

