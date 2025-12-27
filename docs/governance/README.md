---
title: "KFM Governance — README"
path: "docs/governance/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:governance:readme:v1.0.0"
semantic_document_id: "kfm-governance-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:governance:readme:v1.0.0"
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

# KFM Governance — README

## 📘 Overview

### Purpose

This directory is the **canonical home for project-wide governance** in KFM. It exists to:

- define **FAIR+CARE-aligned** governance rules that apply across the pipeline (data → catalogs → graph → APIs → UI → story),
- document **review gates** and change-control expectations for sensitive or high-impact modifications,
- ensure KFM stays **architecture-synced** (no bypassing contracts, provenance, or access policy),
- provide a single starting point for contributors who need to understand **what requires governance review** and how approvals are tracked.

### Scope

| In Scope | Out of Scope |
|---|---|
| Project-wide governance policies and their change-control expectations | Domain-specific governance (belongs under `data/<domain>/governance/`) |
| Ethics and sovereignty policy references and review triggers | Writing new policy text without an approved governance process |
| Review gates and exception logging mechanisms (if adopted) | Implementing ETL/API/UI code (belongs under `src/**` or `web/**`) |
| Classification / sensitivity invariants that must hold across the pipeline | Legal advice or jurisdiction-specific requirements beyond what is explicitly governed in-repo |

### Audience

- Primary: maintainers, governance reviewers/owners, DataOps, security reviewers
- Secondary: contributors adding/modifying datasets, schemas, graph mappings, APIs, UI layers, or Story Nodes

### Definitions

- Link: `docs/glossary.md` *(if missing, add via governance process)*
- Terms used in this doc (non-exhaustive):
  - **Governance gate**: a review or CI validation step that must pass before merge/release.
  - **Sensitivity**: content-based risk label that can require redaction/generalization and governance review.
  - **Classification**: distribution/access label that controls publishing and API authorization behavior.
  - **Redaction / generalization**: techniques used to prevent leakage of sensitive locations/knowledge.
  - **Provenance-linked narrative**: narrative claims traceable to evidence identifiers (STAC/DCAT/PROV).
  - **CARE**: governance principles for Indigenous data (Collective benefit, Authority, Responsibility, Ethics).
  - **FAIR**: Findable, Accessible, Interoperable, Reusable.
  - **Story Node / Focus Mode**: governed narrative artifacts and UI mode that surface provenance-linked context.

### Key artifacts (what this README points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `docs/governance/README.md` | Repo maintainers | Index + process guidance |
| Root governance policy | `docs/governance/ROOT_GOVERNANCE.md` | Governance owners | Canonical definitions (labels, approvals, exceptions) |
| Ethics policy | `docs/governance/ETHICS.md` | Governance owners | AI/ML transparency + bias + disclosure requirements |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance owners | Indigenous data sovereignty + culturally sensitive handling |
| Review gates list | `docs/governance/REVIEW_GATES.md` | Governance owners | *(not confirmed in repo; roadmap suggests adding)* |
| Exception log | `docs/governance/exceptions.yaml` | Governance owners | *(not confirmed in repo; roadmap suggests adding)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline + baseline gates |
| Templates | `docs/templates/` | KFM maintainers | Required doc structures + front matter |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (all required keys present)
- [ ] Directory layout reflects actual governance files (unknowns marked **not confirmed in repo**)
- [ ] Review-gate guidance is consistent with governed pipeline ordering (no “skip the API boundary”)
- [ ] Describes how governance affects Story Nodes / Focus Mode (provenance-linked narrative rule)
- [ ] Validation/CI expectations are stated at least at “minimum gates” level
- [ ] Footer refs present and point to canonical governance documents

## 🗂️ Directory Layout

### This document

- `docs/governance/README.md` — navigation + process summary for governance in KFM

### Related repository paths

- `docs/MASTER_GUIDE_v12.md` — canonical pipeline ordering and baseline CI gates
- `docs/templates/` — governed doc templates (Universal / Story Node / API Contract Extension)
- `docs/standards/` — work protocol and standards *(not confirmed in repo)*
- `.github/` — CI workflows and automation that enforce gates *(not confirmed in repo; repo-dependent)*
- `data/**` — domain modules and datasets (domain governance lives under `data/<domain>/governance/`)
- `schemas/**` — schema constraints for STAC/DCAT/PROV/story/UI/telemetry *(not confirmed in repo)*
- `src/**` — ETL/catalog/graph/API code (policy is documented here, not implemented here)
- `web/**` — UI (must not read Neo4j directly; API boundary is mandatory)

### Expected file tree

~~~text
docs/
└── 📁 governance/
    ├── 📄 README.md
    ├── 📄 ROOT_GOVERNANCE.md
    ├── 📄 ETHICS.md
    ├── 📄 SOVEREIGNTY.md
    ├── 📄 REVIEW_GATES.md            # not confirmed in repo (roadmap suggests adding/maintaining)
    └── 📄 exceptions.yaml            # not confirmed in repo (roadmap suggests adding)
~~~

## 🧭 Context

### Background

KFM is a governed knowledge system. Governance exists because:

- KFM integrates **external sources**, **geospatial data**, and **narratives** that can include sensitive or culturally protected knowledge.
- KFM’s architecture is contract- and provenance-first: changes must remain consistent with the canonical pipeline ordering:
  - **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- Governance is a cross-cutting concern: it constrains **what can be ingested**, **how it can be represented**, **what can be served**, and **what can be narrated/published**.

### Assumptions

- Contributions happen via PRs and are reviewed before merge.
- All governed docs use the template front-matter (sensitivity/classification/jurisdiction included).
- “Allowed values” for sensitivity/classification and their ordering are governed globally (see `ROOT_GOVERNANCE.md`).

### Constraints / invariants

- **API boundary is mandatory**: UI must not read Neo4j directly; all access is via contracted APIs.
- **No unsourced narrative**: published Story Nodes must be provenance-linked (dataset/asset IDs).
- **Classification propagation**: outputs must not have lower restriction than any input used to generate them (exact ordering is governed in `ROOT_GOVERNANCE.md`).
- **Restricted location protection**: if data could reveal protected locations, redaction/generalization is required and must be enforceable at API/UI layers.
- **No secrets/PII**: governance docs must not embed credentials, private URLs, personal data, or disallowed sensitive details.

### Open questions (track here until resolved)

- What is the canonical sensitivity/classification taxonomy and ordering? *(see `ROOT_GOVERNANCE.md`; not restated here)*
- Which roles/groups are the designated governance reviewers (ethics / sovereignty / security)? *(not confirmed in repo)*
- Is `docs/governance/REVIEW_GATES.md` adopted as the canonical gate registry? *(not confirmed in repo)*
- Is an exception registry (e.g., `docs/governance/exceptions.yaml`) adopted and CI-enforced? *(not confirmed in repo)*

### Future extensions (optional)

- Add machine-readable governance gates (YAML) for CI enforcement.
- Add automated reviewer-request rules based on touched paths (e.g., sovereignty paths, story node paths).
- Add an exception process with expirations and CI suppression semantics for known temporary deviations.

## 🗺️ Diagrams

### Governance decision flow (PR → gates → review)

~~~mermaid
flowchart TD
  A["Change proposed (PR)"] --> B["Run CI gates (contracts + policy checks)"]
  B --> C{"Governance trigger hit?"}
  C -- "No" --> D["Standard review + merge (maintainers)"]
  C -- "Yes" --> E["Request governance review (ethics/sovereignty/security as applicable)"]
  E --> F["Address findings / approvals recorded"]
  F --> D
  D --> G["Release/publish (if applicable)"]
  G --> H["Audit trail + telemetry (if applicable)"]
~~~

## 🧠 Story Node & Focus Mode Integration

### Provenance-linked narrative rule

- Story Nodes must ensure every factual claim can trace to a dataset/record/asset identifier.
- If a Story Node depends on restricted inputs, it must inherit the appropriate classification and must not be published as open.

### Focus Mode behavior expectations

- Focus Mode should surface **provenance-linked context only**:
  - narrative + citations + audit/governance flags
  - no leakage of exact restricted locations (even if stored internally)
- If “AI explanation” or generated narrative exists anywhere in the system, it must be:
  - opt-in,
  - clearly labeled,
  - accompanied by uncertainty metadata where applicable,
  - reviewed per ethics policy.

### Optional structured controls (illustrative only)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
governance:
  allow_public_render: true
  location_precision: "coarse"   # coarse | exact (exact requires governance review)
~~~

## ⚙️ Validation & CI/CD

### Minimum CI gates (baseline expectations)

Workflows should enforce a baseline set of gates for governed contributions:

- [ ] Markdown protocol validation (template + front matter + links)
- [ ] Schema validation (STAC/DCAT/PROV + story node schemas, where applicable)
- [ ] Graph integrity tests (where applicable)
- [ ] API contract tests (OpenAPI/GraphQL), where applicable
- [ ] UI registry schema checks, where applicable
- [ ] Security + sovereignty scanning where applicable

### CI behavior principle

- If a gate depends on a root that does not exist in the current repo snapshot, the workflow should **skip** that gate.
- If the root exists, validation must be **strict** and must **fail deterministically** when invalid.

### Reproduction (placeholders)

~~~bash
# Example placeholders — replace with repo-specific commands/scripts.

# 1) Markdown protocol checks
# <TBD>

# 2) Schema validation (STAC/DCAT/PROV/storynodes/ui/telemetry)
# <TBD>

# 3) Graph integrity tests
# <TBD>

# 4) API contract tests
# <TBD>

# 5) Security + sovereignty scanning
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| CI gate results | GitHub Actions | CI logs + artifacts (location TBD) |
| Pipeline run signals | ETL/catalog runs | `data/prov/` and/or run manifests |
| Governance review approvals | Review process | PR history and/or governed registry (TBD; not confirmed in repo) |

## 📦 Data & Metadata

### Required metadata fields (governed docs)

All governed docs (including governance docs) should include in front-matter:

- identifiers: `doc_uuid`, `semantic_document_id`, `event_source_id`, `commit_sha`
- governance labels: `sensitivity`, `classification`, `jurisdiction`, `fair_category`, `care_label`
- references: `governance_ref`, `ethics_ref`, `sovereignty_policy`
- AI constraints: `ai_transform_permissions`, `ai_transform_prohibited`
- integrity fields: `doc_integrity_checksum`

### Sensitivity & redaction (project-wide invariant)

- Provenance artifacts, catalogs, and docs must not leak restricted locations or culturally sensitive knowledge.
- If uncertain, default to **more restrictive** handling until reviewed.
- Do not attempt to infer protected locations from indirect fields (device IDs, unique timestamps, sparse metadata).

### Common governance “inputs” and “outputs”

| Category | Inputs | Outputs |
|---|---|---|
| Policy change | PR text + governed markdown | Updated policy doc(s) + version history |
| Review gate change | Proposed trigger list + CI implications | Updated `REVIEW_GATES.md` (if adopted) + automation changes |
| Exception request | Justification + approver + expiry | Entry in `exceptions.yaml` (if adopted) + audit trail |
| Domain expansion | Domain governance doc + licensing summary | Domain acceptance decision + required constraints recorded |

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements (minimum)

- `prov:wasDerivedFrom`: list upstream source IDs / dataset IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Confidence/uncertainty fields when predictive content is included (ethics review may be required)

### Governance expectations for catalogs/lineage

- STAC items/collections should encode governance labels where the KFM profile allows (e.g., sensitivity/classification/redaction notes).
- DCAT records should reflect access level (e.g., access rights) and must not misrepresent restricted assets.
- PROV should record where and when redaction/generalization occurred (if applicable).

### Classification propagation rule (invariant)

- Outputs must not have “lower restriction” than any input used to generate them.
- Exact allowed values and ordering are governed in `docs/governance/ROOT_GOVERNANCE.md`.

## 🧱 Architecture

### Governance enforcement points across the canonical pipeline

| Component | Responsibility | Enforcement point for governance |
|---|---|---|
| ETL ingest | Acquire + normalize sources | Assign initial labels; default conservative when unsure |
| Work/staging | Intermediate transforms + QA | Run governance scans; block promotion if violations |
| Processed | Certified outputs | Only store publishable artifacts after passing checks |
| Catalog builder | STAC/DCAT/PROV emission | Encode labels; build redacted catalogs if applicable |
| Graph ingest | Neo4j load | Store governance labels for query-time filtering (via APIs) |
| API boundary | Serve data to UI/clients | Authorize + redact/generalize responses by classification |
| UI / Focus Mode | Present layers + narratives | Display governance flags; avoid exposing sensitive locations |

### API boundary reminder (non-negotiable)

- UI must not consume Neo4j directly.
- All access to graph and catalog content must flow through contracted APIs that apply authorization and redaction/generalization.

## ⚖ FAIR+CARE & Governance

### Review gates (examples; canonical list belongs in `REVIEW_GATES.md` if adopted)

The roadmap indicates governance reviews should trigger for conditions like:

- Adding a dataset with `sensitivity: restricted` or culturally sensitive info → sovereignty review.
- Introducing/modifying any AI/ML component generating or summarizing narrative → ethics review (transparency/bias).
- Adding a new external data source API → license/FAIR review (rights + metadata mapping).
- New major UI/API feature affecting security posture (e.g., file downloads, public query endpoints) → security review.

*(For the canonical list, see `docs/governance/REVIEW_GATES.md` if present; otherwise treat these as guidance and record triggers in PR descriptions.)*

### PR template updates (recommended)

- Add a governance checklist to the PR template (not confirmed in repo), e.g.:
  - “Does this change add/modify data with sensitivity concerns? If yes, has approval been obtained?”
  - “If adding a new dataset, confirm PROV + metadata are included.”
  - “If adding story content, confirm every claim is provenance-linked.”

### Automated notifications (recommended)

- Auto-request governance review if a PR touches:
  - `docs/governance/**`
  - sovereignty-sensitive domains (example path: `data/historical/indigenous/**`)
  - Story Nodes (`docs/reports/story_nodes/**`)

### Exception logging (recommended, time-bounded)

- For temporary deviations (e.g., staleness waivers, incomplete upstream availability), consider a governed exception registry:
  - `docs/governance/exceptions.yaml` *(not confirmed in repo)*
- Each entry should include:
  - what is waived,
  - who approved,
  - why,
  - an expiry date,
  - any mitigations.

### CARE / sovereignty considerations

- Identify impacted communities and protection rules for sensitive/restricted locations.
- Ensure provenance and audit logs don’t re-expose restricted geometry or identifiers.
- If in doubt, escalate to sovereignty review before publishing or promoting a dataset/story.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited:
  - generating new policy text (“generate_policy”),
  - inferring sensitive locations (“infer_sensitive_locations”).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial governance README scaffold | TBD |

---

## Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

---
