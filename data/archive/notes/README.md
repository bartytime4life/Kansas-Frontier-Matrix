---
title: "KFM — Data Archive Notes (README)"
path: "data/archive/notes/README.md"
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

doc_uuid: "urn:kfm:doc:data:archive:notes:readme:v1.0.0"
semantic_document_id: "kfm-data-archive-notes-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:archive:notes:readme:v1.0.0"
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

# Data Archive Notes

## 📘 Overview

### Purpose
`data/archive/notes/` holds **human-authored, lightweight Markdown notes** that accompany archived
materials (bundles + manifests). These notes capture *context* that is important for reviewers and future
maintainers but does **not** belong in machine-readable artifacts (e.g., manifests, checksums, STAC/DCAT,
or PROV records).

Typical reasons for a note:
- Explaining *why* something was archived (retention, snapshotting, de-duplication, migration).
- Recording review outcomes (e.g., “license verified”, “geometry generalized”, “redaction applied”).
- Linking together bundle IDs, manifest IDs, checksum files, and provenance/run identifiers.

### Scope
| In Scope | Out of Scope |
|---|---|
| Short Markdown notes linked to a specific archived bundle/manifest | Primary data, derived datasets, or STAC/DCAT/PROV JSON-LD/Turtle |
| Rationale for curation decisions (normalization, redaction, exclusions) | Secrets/credentials/tokens, private keys, auth configs |
| Human review outcomes and caveats | Personally identifying information (PII) or sensitive location inference |
| Pointers to stable IDs (bundle IDs, manifest IDs, STAC item IDs, PROV activity IDs) | Anything the UI or API should consume directly |

### Audience
- Primary: data curators, ETL maintainers, catalog maintainers
- Secondary: security/governance reviewers, historians/editors validating provenance

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: archive, bundle, manifest, checksum, provenance, redaction/generalization

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Archive overview | `data/archive/README.md` | Data maintainers | Explains the archive subsystem at a high level |
| Bundles | `data/archive/bundles/` | Data maintainers | Archived payloads (structure defined by repo conventions) |
| Manifests | `data/archive/manifests/` | Data maintainers | Index of archived contents + stable IDs |
| Checksums | `data/checksums/` | Data maintainers | Cryptographic checksums used for integrity checks |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Notes directory purpose is explicit (what belongs here / what does not)
- [ ] Cross-links to bundles/manifests/checksums are present
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations are explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/archive/notes/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Archive (root) | `data/archive/` | Archived materials + index/structure |
| Bundles | `data/archive/bundles/` | Archived payload directories/files |
| Manifests | `data/archive/manifests/` | Machine-readable inventory describing bundles |
| Notes (this folder) | `data/archive/notes/` | Human-readable context + review notes |
| Checksums | `data/checksums/` | Integrity hashes for artifacts |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 archive/
    └── 📁 notes/
        ├── 📄 README.md
        ├── 📄 <bundle_id>.md
        └── 📄 <bundle_id>--<short-title>.md
~~~

## 🧭 Context

### Background
The archive subsystem preserves snapshots of inputs/outputs and supporting artifacts over time. Machine
contracts (manifests, checksums, catalogs) are necessary but often insufficient to explain *why* a snapshot
exists or what caveats apply. This notes folder provides that missing human context while keeping the
canonical pipeline clean.

### Assumptions
- Bundles and manifests are the **source of truth** for machine consumption.
- Notes are **advisory** and must reference stable IDs rather than duplicating data.
- Any sensitive information must be handled via governance/sovereignty rules and redaction.

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend/UI must not read these notes directly; any surfaced narrative must go through APIs and governed
  story nodes (no direct data/graph coupling).
- No secrets/credentials/PII in archive notes.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should notes adopt a standardized per-note mini-template (e.g., required header fields)? | TBD | TBD |
| Should notes be referenced in PROV as `prov:Entity` documentation links? | TBD | TBD |

### Future extensions
- Add an optional note template (e.g., `NOTE_TEMPLATE.md`) if consistency becomes a problem.
- Add lightweight link checks ensuring every note references an existing bundle/manifest ID.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Archive Bundle] --> B[Archive Manifest]
  B --> C[Checksums]
  B --> D[Archive Note]
  D --> E[Reviewer context]
  B --> F[Catalog/PROV references]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Bundle identifier(s) | string | `data/archive/bundles/` | Must exist and be stable |
| Manifest identifier(s) | JSON/YAML/etc. | `data/archive/manifests/` | Must parse + link to bundle |
| Checksum reference(s) | text | `data/checksums/` | Hash file exists + matches artifact |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Archive note | Markdown | `data/archive/notes/<bundle_id>*.md` | Governed by this README (human-readable) |

### Sensitivity & redaction
- Do not record restricted locations at high precision if they are considered sensitive.
- If a note must refer to sensitive content, describe it at an abstract level and point to the governed
  artifact that applies redaction/generalization.

### Quality signals
- Notes should include:
  - the bundle ID (required)
  - the manifest ID or filename (recommended)
  - any known issues and their impact
  - review status (e.g., “license verified”, “pending historian review”) when relevant

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Notes may reference STAC Collection/Item IDs when the archived material corresponds to catalog entries.
- Notes must not replace STAC metadata.

### DCAT
- Notes may reference DCAT dataset identifiers where applicable.
- Notes must not replace DCAT records.

### PROV-O
- Notes should, when relevant, record:
  - `prov:wasDerivedFrom` identifiers (sources referenced by the archive)
  - `prov:wasGeneratedBy` pipeline activity/run IDs (if known)
- Notes are supplementary; PROV lineage bundles remain authoritative for provenance.

### Versioning
- Notes are versioned via Git.
- If a bundle is superseded, notes should reference the successor/predecessor relationship as described in
  the manifest/canonical lineage docs.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Archive bundles | Preserve snapshots | File system paths under `data/archive/bundles/` |
| Archive manifests | Inventory + identifiers | Files under `data/archive/manifests/` |
| Archive notes | Human context + review | Markdown under `data/archive/notes/` |
| Checksums | Integrity verification | Files under `data/checksums/` |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Archive manifests | `data/archive/manifests/` | Stable IDs; changes must be reviewed |
| Checksums | `data/checksums/` | Recomputed only when artifact content changes |
| Notes | `data/archive/notes/` | Free-form but must reference stable IDs |

### Extension points checklist (for future work)
- [ ] Add note template if needed
- [ ] Add CI check: every note references an existing bundle/manifest ID
- [ ] Link notes to PROV entities (requires review)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- This folder is **not** a narrative delivery mechanism.
- If content in a note becomes user-facing, it should be promoted into a governed Story Node document
  with explicit provenance links.

### Provenance-linked narrative rule
- Any promoted narrative must trace back to dataset/record/asset IDs in catalogs and manifests.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (format + structure)
- [ ] Link integrity checks (paths to bundles/manifests/checksums resolve)
- [ ] Secret scanning / security scanning (no credentials, tokens, or private keys)
- [ ] Sovereignty/sensitivity review if notes mention restricted content

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run markdown lint
# 2) run link checker (docs/data paths)
# 3) run secret scan
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- If notes reference sensitive sources or restricted geographies: requires governance + sovereignty review.
- If notes document a redaction/generalization decision: requires reviewer sign-off as defined by governance.

### CARE / sovereignty considerations
- Avoid disclosing culturally sensitive locations or information.
- Prefer generalized descriptions and cite governed artifacts that implement redaction.

### AI usage constraints
- Notes must not be used to justify unsourced narrative.
- Any AI summarization must respect the prohibitions in the front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for archive notes directory | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

