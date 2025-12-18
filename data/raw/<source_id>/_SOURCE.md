---
title: "SOURCE — <source_id> (Upstream Provenance & Licensing Notes)"
path: "data/raw/<source_id>/_SOURCE.md"
version: "v0.1.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Source Notes"
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

doc_uuid: "urn:kfm:doc:data:raw:<source_id>:source-notes:v0.1.0"
semantic_document_id: "kfm-data-raw-<source_id>-source-notes-v0.1.0"
event_source_id: "ledger:kfm:doc:data:raw:<source_id>:source-notes:v0.1.0"
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

# SOURCE — `<source_id>`

This file captures **upstream provenance pointers**, **licensing/attribution notes**, and **acquisition context** for the raw artifacts stored under:

- `data/raw/<source_id>/`

It is intentionally human-readable. It should complement (not replace) a machine-readable manifest under `data/sources/` (**not confirmed in repo**: exact schema/filename).

> Replace `<source_id>` everywhere in this file with the canonical source ID used by your `data/sources/` manifest (if applicable).

## 📘 Overview

### Purpose
- Provide a stable “source-of-truth” note for:
  - Where the data came from (provider + publication reference)
  - License terms and attribution expectations
  - How raw artifacts were acquired (what, when, how)
  - What *not* to do in `data/raw/` (no transformations; no sensitive data leakage)

### Scope
| In Scope | Out of Scope |
|---|---|
| Provider identity + references | Data cleaning/normalization (belongs in `data/work/`) |
| License + attribution notes | Full legal analysis (defer to upstream terms) |
| Acquisition events (date-stamped) | Graph modeling + API contract behavior |
| Known limitations of upstream data | UI presentation decisions |

### Audience
- Primary: Contributors adding/updating this source.
- Secondary: Maintainers reviewing provenance + compliance.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- **source_id**: Canonical identifier for an upstream source.
- **acquisition**: A specific retrieval event resulting in a dated raw bundle folder.
- **raw artifact**: Source-faithful file as acquired (no transformation).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Per-source raw folder | `data/raw/<source_id>/` | Data maintainers | This source’s landing zone |
| Per-source raw README | `data/raw/<source_id>/README.md` | Data maintainers | Folder usage + layout |
| Source notes (this doc) | `data/raw/<source_id>/_SOURCE.md` | Data maintainers | Provenance + license notes |
| Optional license summary | `data/raw/<source_id>/_LICENSE.md` | Data maintainers | Human summary only (no new policy) |
| Machine manifest | `data/sources/<source_id>.*` | Data maintainers | **not confirmed in repo** (schema/ext) |

### Definition of done (for this document)
- [ ] Provider/publisher identity recorded
- [ ] Upstream publication reference recorded (URL/citation string, release/version if available)
- [ ] License name + reference recorded (and any constraints summarized)
- [ ] Attribution statement captured (if required)
- [ ] At least one acquisition event recorded (date, method, integrity approach)
- [ ] Sensitivity + sovereignty considerations stated (even if “none known”)

## 🗂 Directory Layout

### This document
- `path`: `data/raw/<source_id>/_SOURCE.md`

### Expected local structure (recommended)
~~~text
📁 data/
└─📁 raw/
  └─📁 <source_id>/
    ├─📄 README.md
    ├─📄 _SOURCE.md
    ├─📄 _LICENSE.md                 # optional
    ├─📁 <YYYY-MM-DD>/               # acquisition bundle(s)
    │  ├─📄 <original_filename>.<ext>
    │  ├─📄 <original_filename>.<ext>.sha256   # optional
    │  └─📄 _ACQUISITION_NOTES.md     # optional
    └─📁 _inventory/                 # optional
       └─📄 inventory_<YYYY-MM-DD>.csv
~~~

## 🧭 Context

### Background
Fill in:

| Field | Value |
|---|---|
| Source name | `<human-readable source name>` |
| Provider / publisher | `<organization>` |
| Provider reference | `<provider portal / archive ref / DOI / citation string>` |
| Coverage (spatial) | `<statewide / region / county / bbox>` |
| Coverage (temporal) | `<start–end>` |
| What this supports in KFM | `<1–3 sentences: layers/entities/questions enabled>` |

### License & attribution
Record upstream licensing here. Do not invent new policy language.

| Field | Value |
|---|---|
| License name | `<e.g., CC-BY 4.0 / ODbL / Public Domain / custom>` |
| License reference | `<citation string or link placeholder>` |
| Attribution required | `<yes/no + required text if provided>` |
| Redistribution limits | `<none known / describe succinctly>` |
| Commercial use | `<allowed / restricted / unknown>` |
| Derivatives | `<allowed / restricted / unknown>` |
| Notes | `<anything special: share-alike, no-endorsement, etc.>` |

**Attribution statement (if required by provider):**
~~~text
<insert provider-required attribution statement verbatim or paraphrase with citation reference>
~~~

### Acquisition method
| Field | Value |
|---|---|
| Acquisition type | `<API / bulk download / manual export / scan / other>` |
| Authentication required | `<none / yes (DO NOT store tokens here)>` |
| Data format(s) received | `<GeoJSON / SHP / CSV / TIFF / PDF / etc.>` |
| Expected cadence | `<one-time / monthly / annual / irregular>` |
| Integrity approach | `<sha256 sidecars / DVC / other>` (**not confirmed in repo** if unknown) |

### Constraints / invariants
- Do **not** transform/clean data in `data/raw/<source_id>/`.
- Do **not** commit secrets, credentials, or sensitive personal information.
- If the source may include sensitive locations (cultural sites, private addresses, etc.):
  - Avoid repeating precise coordinates in notes.
  - Ensure downstream generalization/redaction is applied before publication.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical manifest schema/filename for this source under `data/sources/`? | TBD | TBD |
| Are raw artifacts stored in Git, or tracked via a large-file mechanism? | TBD | TBD |
| Are there any explicit sensitivity constraints from the provider or governance? | TBD | TBD |

### Future extensions
- Add standardized acquisition metadata sidecar (JSON/YAML) per bundle (**not confirmed in repo**).
- Add CI checks for integrity (hash verification + file counts) for this source.

## 🗺 Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  U["Upstream provider<br/>System of record"] --> R["data/raw/<source_id><br/>Raw artifacts"]
  R --> W["data/work/<source_id><br/>Staging + QA"]
  W --> P["data/processed<br/>Validated outputs"]
  P --> C["data/stac<br/>Catalogs: STAC · DCAT · PROV"]
  C --> G["Neo4j graph"]
  G --> A["APIs"]
  A --> UI["UI"]
  UI --> S["Story Nodes"]
  S --> F["Focus Mode"]
~~~

## 📦 Data & Metadata

### Acquisition record
Add one row per acquisition bundle folder.

| Acquisition date | Provider release/version | Method | Folder | Integrity notes | Operator |
|---|---|---|---|---|---|
| `<YYYY-MM-DD>` | `<vX.Y / unknown>` | `<download/api/export>` | `data/raw/<source_id>/<YYYY-MM-DD>/` | `<hashes recorded? file count?>` | `<name/role>` |

### Inputs (what arrives into `data/raw/<source_id>/`)
| Input | Format | Where from | Validation |
|---|---|---|---|
| `<dataset name>` | `<ext>` | `<provider>` | `<hash/size + completeness>` |
| `<ancillary metadata>` | `<ext>` | `<provider>` | `<sanity check>` |

### Outputs (what this source produces downstream)
(These are typically created outside raw.)

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed dataset | `<ext>` | `data/processed/<domain>/...` | `<schema id>` (**not confirmed in repo**) |
| STAC collection/items | JSON | `data/stac/...` | STAC 1.0 |
| DCAT dataset | RDF/JSON-LD | `data/stac/...` | DCAT 3 |
| PROV lineage | RDF/JSON-LD | `data/stac/...` | PROV-O |

### Sensitivity & redaction
| Category | Applies? | Notes |
|---|---:|---|
| PII risk | `<yes/no/unknown>` | `<what fields might include PII?>` |
| Sensitive locations | `<yes/no/unknown>` | `<generalize before publishing?>` |
| Cultural sensitivity | `<yes/no/unknown>` | `<sovereignty handling?>` |
| Restricted access | `<yes/no/unknown>` | `<license/security constraints?>` |

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Upstream provider | Publishes source data | Portal / API / archive reference |
| Raw store | Holds source-faithful artifacts | `data/raw/<source_id>/...` |
| Work store | Transform + QA staging | `data/work/<source_id>/...` |
| Processed store | Canonical outputs | `data/processed/...` |
| Catalog builder | STAC/DCAT/PROV | `data/stac/...` |
| Graph + APIs | Query + serve | API layer |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Source manifest schema | `schemas/` | Semver (**not confirmed in repo**) |
| Processed output schema | `schemas/` | Semver (**not confirmed in repo**) |
| Catalog validation | STAC/DCAT/PROV | Validator-pinned |

## 🧠 Story Node & Focus Mode Integration

### How this source surfaces
- Expected entities/layers enabled: `<boundaries / parcels / events / imagery / etc.>`
- Provenance expectation: Focus Mode should reference **processed** IDs (STAC + graph), with trace-back to raw acquisition folders/hashes.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID, not solely to a raw filename.

### Optional structured controls
~~~yaml
focus_layers:
  - "<collection_or_layer_id>"
focus_time: "<YYYY or range>"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] License/attribution compliance verified against provider reference
- [ ] No secrets or sensitive personal data present in raw notes/filenames
- [ ] Integrity signals present (hashes and/or large-file tooling) per repo standard (**not confirmed in repo**)
- [ ] If processed outputs exist: schema validation + catalog validation is green

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) validate manifest schema for <source_id>
# 2) fetch/verify raw artifacts for <source_id>
# 3) run pipeline: raw -> work -> processed -> stac
# 4) validate catalogs (STAC/DCAT/PROV)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| acquisition_date | operator/pipeline | `mcp/runs/` (**not confirmed in repo**) |
| sha256 | sidecar/tooling | alongside artifacts or inventory |
| processed_build_id | pipeline run | `mcp/runs/` (**not confirmed in repo**) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Approver(s): `<TBD>` (follow `docs/governance/*`)
- Extra review required if: `<sensitivity / sovereignty / restricted license>`

### CARE / sovereignty considerations
- Communities potentially impacted: `<TBD>`
- Handling constraints: `<TBD>`
- If culturally sensitive information exists, ensure downstream generalization/redaction before public release.

### AI usage constraints
- Do not use AI to infer or reconstruct sensitive locations from this source.
- Keep AI transforms limited to allowed modes in front-matter.

## 🕰 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-18 | Initial `_SOURCE.md` template for `<source_id>` | TBD |

