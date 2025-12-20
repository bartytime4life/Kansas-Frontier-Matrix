---
title: "Source Summaries — Web (README)"
path: "docs/research/source_summaries/by_type/web/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:research:source-summaries:web:readme:v1.0.0"
semantic_document_id: "kfm-research-source-summaries-web-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:research:source-summaries:web:readme:v1.0.0"
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

# Source Summaries — Web

## 📘 Overview

### Purpose
This directory holds **governed summaries of web-based sources** (web pages, online articles, project docs, standards pages, institutional pages).
These summaries are used to:
- capture evidence and constraints (license/terms, definitions, key claims),
- drive implementation decisions (ETL, catalogs, graph modeling, APIs, UI),
- preserve provenance so downstream Story Nodes and Focus Mode can remain source-linked.

### Scope
| In Scope | Out of Scope |
|---|---|
| Web pages (HTML), online documentation, blog posts, institutional pages, standards pages | Books (use `../books/`), journal papers (use the relevant by_type folder if present), datasets as primary artifacts (use the relevant by_type folder if present) |
| Web sources used to justify pipeline/architecture decisions | “Opinion-only” sources with no extractable constraints/evidence for KFM (unless explicitly tracked for rationale) |
| Web sources that may later be snapshotted/ingested into `data/raw/` | Sources requiring prohibited handling (e.g., sensitive location inference) |

### Audience
- Primary: contributors writing/maintaining source summaries; maintainers reviewing research inputs
- Secondary: ETL/catalog/graph/API/UI implementers who need traceable rationale

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: source summary, provenance, snapshot, license/terms, extraction cues

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `docs/research/source_summaries/by_type/web/README.md` | TBD | Scope + conventions for web summaries |
| Web source summaries | `docs/research/source_summaries/by_type/web/*.md` | TBD | One governed doc per web source |
| Canonical pipeline | `docs/MASTER_GUIDE_v12.md` | TBD | Ordering + invariants |

### Definition of done (for this document)
- [x] Front-matter complete + valid
- [x] Pipeline relationship documented
- [x] Mermaid diagram uses renderer-safe labels (no HTML tags)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (as applicable)

## 🗂️ Directory Layout

### This document
- `path`: `docs/research/source_summaries/by_type/web/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs + research notes |
| Source summaries | `docs/research/source_summaries/` | External-source evidence captured as governed docs |
| Data lifecycle | `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` | Standard staging for ingested assets |
| Graph | `src/graph/` | Ontology bindings + graph build |
| APIs | `src/server/` + docs | Contracted access layer |
| UI | `web/` | React + map clients |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 research/
    └── 📁 source_summaries/
        └── 📁 by_type/
            └── 📁 web/
                ├── 📄 README.md
                ├── 📄 <source-summary-1>.md
                └── 📄 <source-summary-2>.md
~~~

## 🧭 Context

### Background
Web sources are often:
- the fastest way to capture evolving standards, implementation notes, and institutional guidance,
- ephemeral (content changes, links rot), and
- licensing/terms-sensitive.

Therefore, KFM treats web sources as **inputs that must be summarized with provenance** before they can influence contracts, schemas, or narrative outputs.

### Assumptions
- Web sources may change after the summary is written; summaries should record an **access date** and (if applicable) a **stable snapshot reference**.
- Source summaries are **research artifacts** that can drive downstream work but do not bypass governance/PR review.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No unsourced narrative in Focus Mode contexts; web sources must be traceable through summaries and then into catalogs/graph as applicable.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we require durable web snapshots for any source used in public narrative? | TBD | TBD |
| Where do we store web snapshots (if required) and how do we link them into STAC/PROV? | TBD | TBD |

### Future extensions
- Optional: add a standardized “web snapshot” ingestion pattern (to `data/raw/` + STAC asset linkage).
- Optional: add automated “link rot” checks for summarized URLs.

## 🗺️ Diagrams

### How web source summaries relate to the KFM pipeline
~~~mermaid
flowchart LR
  W["Web source"] --> SS["Source summary (web)"]
  SS --> D["Governed docs and standards"]
  SS --> ETL["ETL ingestion plan"]
  ETL --> CAT["STAC/DCAT/PROV catalogs"]
  CAT --> G["Neo4j graph"]
  G --> API["API layer"]
  API --> UI["React/Map UI"]
  UI --> SN["Story Nodes"]
  SN --> FM["Focus Mode"]
~~~

## 📦 Data & Metadata

### Minimum fields a web source summary should capture
| Field | Why it matters | Notes |
|---|---|---|
| Canonical URL | Identity + reproducibility | Prefer canonical permalink when available |
| Title + publisher | Citation + credibility context | Record organization/site owner |
| Author(s) | Attribution | If unknown, record as unknown |
| Published / last-updated date | Currency | If absent, note “not stated” |
| Accessed date | Reproducibility | Required for web sources |
| License / terms | Reuse constraints | Record what is stated; do not guess |
| Summary (neutral) | Shared understanding | Keep factual and concise |
| KFM relevance | Pipeline linkage | Which stage(s) it informs |
| Extractable constraints | Engineering value | e.g., required fields, definitions, invariants |
| Risks / caveats | Governance | e.g., changing content, bias, paywall, sensitive info |

### Sensitivity & redaction
- If a web source includes sensitive locations, vulnerable populations, or personal data, the summary must:
  - avoid reproducing sensitive details beyond what governance allows,
  - note the sensitivity risk explicitly,
  - include any required generalization/redaction expectations.

### Quality signals
- Does the source provide primary evidence or only commentary?
- Is it an official standard / institutional page vs. a personal blog?
- Are claims supported by references or data?

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If the web source is captured as a durable artifact (e.g., HTML/PDF snapshot), the summary should note:
  - the expected STAC Item(s) and assets (TBD per repo conventions),
  - the spatial/temporal relevance (if any),
  - how it will be discovered downstream.

### DCAT
- If the web source describes a dataset or service that will be cataloged:
  - record the dataset identifier (if available),
  - record publisher/license keywords needed for DCAT mapping.

### PROV-O
- Web summaries should anticipate provenance linkage:
  - `prov:wasDerivedFrom`: the canonical URL and/or snapshot ID
  - `prov:wasGeneratedBy`: the ETL/catalog activity/run ID (once ingestion exists)

### Versioning
- When a web source changes materially, prefer creating a new summary version or a new summary doc that links back to the earlier one (exact mechanism: TBD per repo conventions).

## 🧱 Architecture

### How this content is served
- These summaries are **documentation-layer artifacts** that:
  - inform implementation work (`src/`, `schemas/`, `data/`),
  - support Story Node authoring (evidence trail),
  - help Focus Mode remain provenance-linked.

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Source summary doc (this area) | `docs/research/source_summaries/` | Semver in front-matter + version history |
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| UI registry | `web/` | Schema-validated (details TBD) |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- A web source summary may be referenced by:
  - Story Nodes (as justification for narrative structure or claims),
  - Focus Mode evidence panels (only when it is permissible and provenance-linked).

### Provenance-linked narrative rule
- Any claim that reaches Story Nodes / Focus Mode must trace back to:
  - a source summary, and
  - a stable dataset/document ID where applicable (STAC/DCAT/PROV and/or graph references).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Links are well-formed and use canonical URLs where possible
- [ ] License/terms are recorded (not inferred)
- [ ] No prohibited AI actions implied (e.g., sensitive location inference)
- [ ] If used for public narrative: references can be mapped into catalogs/graph where required

### Reproduction
~~~bash
# Suggested checks (repo-specific commands TBD):
# 1) markdown lint / protocol validator
# 2) link checker (optional)
# 3) schema validation (if summary references schemas/assets)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Any web source used to justify:
  - public-facing endpoints,
  - new sensitive layers,
  - narrative claims in Story Nodes,
  should be reviewed under the referenced governance/ethics/sovereignty docs.

### CARE / sovereignty considerations
- Identify impacted communities and protection rules when sources concern culturally sensitive content.

### AI usage constraints
- This doc permits summarization/structuring/translation/keyword indexing.
- This doc prohibits generating new policy and inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for web source summaries | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

