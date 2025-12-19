---
title: "KFM — Archive Bundle Payloads"
path: "data/archive/bundles/bundles/README.md"
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

doc_uuid: "urn:kfm:doc:data:archive:bundles:bundle-payloads-readme:v1.0.0"
semantic_document_id: "kfm-data-archive-bundles-bundle-payloads-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:archive:bundles:bundle-payloads-readme:v1.0.0"
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

# KFM — Archive Bundle Payloads

## 📘 Overview

### Purpose
This directory holds the *payload artifacts* for KFM archive bundles (i.e., the actual bundle files that can be transported, stored, or restored).
It is intended to support reproducible handoffs across the canonical pipeline (ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode) by preserving “snapshot-like” distribution units.

### Scope
| In Scope | Out of Scope |
|---|---|
| Bundle payload files (e.g., compressed archives) | Raw source ingestion inputs (`data/raw/`) |
| Bundle payload directory layout and conventions | Working / scratch build outputs (`data/work/`) |
| Links to manifests + checksums that describe/verify payloads | Any runtime caches or temp files |

### Audience
- Primary: data/pipeline maintainers; CI/CD maintainers
- Secondary: release engineers; auditors verifying provenance & integrity

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc: “bundle”, “payload”, “manifest”, “checksum”, “restore”

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Archive root | `data/archive/` | Data Ops | Archive system root |
| Bundle manifests | `data/archive/manifests/` | Data Ops | Describes bundle contents + metadata |
| Checksums | `data/checksums/` | Data Ops | Integrity verification for payload files |
| Bundle system docs | `data/archive/bundles/README.md` | Data Ops | Higher-level bundle overview (sibling README) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are explicit
- [ ] Expected file tree included
- [ ] Validation steps are listed and repeatable
- [ ] Sensitivity & governance cautions are stated

## 🗂️ Directory Layout

### This document
- `path`: `data/archive/bundles/bundles/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Archive | `data/archive/` | Immutable-ish preservation of build outputs |
| Bundle payloads | `data/archive/bundles/bundles/` | The bundle files themselves |
| Bundle manifests | `data/archive/manifests/` | Machine-readable “what’s inside” |
| Checksums | `data/checksums/` | Hashes for integrity checks |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 archive/
    └── 📁 bundles/
        └── 📁 bundles/
            ├── 📄 README.md
            ├── 📦 <bundle_id>.<ext>
            ├── 📦 <bundle_id>.<ext>
            └── 📁 <bundle_id>/
                ├── 📄 README.md
                └── 📦 <payload_parts_if_split>
~~~

**Notes:**
- `<bundle_id>` is a stable identifier for a specific bundle payload.
- `<ext>` is an archive format (e.g., `zip`, `tar`, `tar.gz`, `tar.zst`) — exact formats are *not confirmed in repo*.
- This directory can support either:
  - **single-file bundles** (`<bundle_id>.<ext>`), or
  - **bundle-as-directory** (`<bundle_id>/...`) if the payload must be split.

## 🧭 Context

### Background
KFM uses a strict pipeline ordering with governed artifacts and provenance. Archive bundles are a practical way to preserve and distribute “frozen” outputs of key stages (catalogs, derived datasets, evidence products) without changing the meaning of the canonical sources.

### Assumptions
- Bundle payloads are paired with:
  - a manifest record (under `data/archive/manifests/`), and
  - checksum material (under `data/checksums/`).
- Bundle payloads are treated as **append-only artifacts** (replace-by-new-version rather than edit-in-place) — *not confirmed in repo*.

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The UI must not read Neo4j directly; it consumes contracted API outputs (bundle payloads are not UI-facing by default).
- No sensitive locations should be inferred or “filled in” during bundling or documentation.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical bundle payload format (zip vs tar.*)? | TBD | TBD |
| Do we require content-addressed filenames (sha256) or human IDs? | TBD | TBD |
| Are payloads stored in Git, Git LFS, or external object storage? | TBD | TBD |

### Future extensions
- Add a machine-readable index of bundles (if needed) — *not confirmed in repo*.
- Add restore automation tooling under `tools/` — *not confirmed in repo*.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL outputs] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Bundle build activity]
  C --> D[Bundle manifest]
  C --> E[Bundle payload files]
  D --> F[Restore / verification]
  E --> F[Restore / verification]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Bundle manifest | JSON/YAML (TBD) | `data/archive/manifests/` | Schema + link integrity (TBD) |
| Checksums | text/JSON (TBD) | `data/checksums/` | Hash verification |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Bundle payload file(s) | archive file(s) | `data/archive/bundles/bundles/` | Manifest-defined (TBD) |

### Sensitivity & redaction
Bundle payloads may package artifacts that include restricted/sensitive content depending on the domain.
Before placing payloads here, ensure the *upstream* artifacts have applied any required redaction/generalization rules per:
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
*(All governance paths referenced here are not confirmed in repo.)*

### Quality signals
Recommended checks (implementations may live in CI/CD):
- Payload has a corresponding manifest entry.
- Payload hash matches the recorded checksum.
- Manifest references resolve to existing repo paths or external stable identifiers (as applicable).
- No “work-in-progress” artifacts included (e.g., temp files).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Bundle payloads may include STAC JSON (Collections/Items) or STAC-exported subsets.
If so, ensure:
- Items ↔ Collections integrity is maintained.
- Asset links inside the bundle remain valid *within the bundle context* (or are rewritten deterministically) — *not confirmed in repo*.

### DCAT
If bundle payloads include DCAT views (JSON-LD/Turtle), ensure dataset identifiers are stable and match the canonical catalog layer.

### PROV-O
If a bundling step is tracked, it should be representable as a PROV Activity, and the payload should trace back to source artifact IDs:
- `prov:wasDerivedFrom`: source catalog and/or dataset artifact IDs
- `prov:wasGeneratedBy`: bundling activity/run ID
*(Exact PROV recording strategy is not confirmed in repo.)*

### Versioning
Preferred behavior (TBD / not confirmed in repo):
- Bundle payloads are immutable; produce a new bundle for changes.
- Manifests reference predecessor/successor bundles when representing versions.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Run logs + deterministic outputs |
| Catalogs | STAC/DCAT/PROV | JSON/LD + validators |
| Bundling | Package selected outputs | Manifest + payload + checksums |
| Restore | Verify + unpack | Manifest-driven |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Bundle manifest contract | `data/archive/manifests/` | Semver (TBD) |
| Checksum format | `data/checksums/` | Semver (TBD) |

## 🧠 Story Node & Focus Mode Integration

This directory is not a Story Node surface. If bundle payloads contain Story Node markdown or Focus Mode evidence artifacts, the bundle manifest should list them explicitly and preserve provenance identifiers so the API/UI layers can continue to enforce citation and sensitivity rules.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Bundle payload exists and is readable
- [ ] Matching manifest exists and references the payload
- [ ] Checksums exist and verify successfully
- [ ] No sensitive locations are exposed beyond allowed classification
- [ ] If catalog artifacts are included, STAC/DCAT/PROV validation passes (where applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) verify payload checksums
# 2) validate manifest schema
# 3) (optional) unpack to a temp location and run STAC/DCAT/PROV validators
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Human review required when:
  - packaging new external sources
  - packaging restricted/sensitive domains
  - changing bundling format or manifest contract (backward compatibility)

### CARE / sovereignty considerations
- Ensure culturally sensitive content and restricted locations remain protected at rest and during distribution.
- Avoid embedding “more precise than allowed” geometry or place resolution.

### AI usage constraints
- This document prohibits:
  - generating new policy
  - inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README scaffolding for bundle payload directory | TBD |

