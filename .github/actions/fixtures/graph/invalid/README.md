---
title: "Fixtures — Graph — Invalid"
path: ".github/actions/fixtures/graph/invalid/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:github-actions:fixtures:graph:invalid-readme:v1.0.0"
semantic_document_id: "kfm-github-actions-fixtures-graph-invalid-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github-actions:fixtures:graph:invalid-readme:v1.0.0"
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

# Fixtures — Graph — Invalid

## 📘 Overview

### Purpose

- This directory holds **intentionally invalid** graph fixture inputs used for **negative testing** of graph validation / integrity checks in CI.
- These fixtures exist to ensure CI behavior is **deterministic**: invalid inputs must be rejected (i.e., treated as a failure by the validator), and regressions where invalid inputs are accepted must be caught.

### Scope

| In Scope | Out of Scope |
|---|---|
| Negative/invalid graph fixture data used to confirm validators reject broken inputs | Production datasets, curated domain data, or any “real” graph exports |
| Small, synthetic examples that isolate one failure mode | Valid fixtures (keep elsewhere) |
| Documentation for adding/updating invalid fixtures | Defining the full graph ontology/contract (belongs in `docs/graph/` + `src/graph/`) |

### Audience

- Primary: CI/workflow maintainers; graph ingestion/validation maintainers
- Secondary: contributors adding or updating fixture cases

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: **fixture**, **negative test**, **graph integrity check**, **validator**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Invalid graph fixtures (this directory) | `.github/actions/fixtures/graph/invalid/` | Maintainers | Inputs here must be rejected by the graph validator |
| Graph subsystem (code) | `src/graph/` | Maintainers | Ontology bindings, ingest/validation logic |
| Graph artifact formats (reference) | `data/graph/` (e.g., `csv/`, `cypher/`) | Maintainers | If fixtures mirror import formats, keep them minimal |
| Master Guide (canonical pipeline + locations) | `docs/MASTER_GUIDE_v12.md` | Project | Pipeline ordering + canonical homes |
| v13 redesign blueprint (CI determinism principle) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Project | “fail if invalid; skip if not applicable” guidance |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Purpose and scope make it clear these fixtures are **invalid on purpose**
- [ ] Adding a new fixture case has a documented expectation (“what should fail and why”)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (synthetic; no sensitive content)

## 🗂️ Directory Layout

### This document

- `path`: `.github/actions/fixtures/graph/invalid/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub Actions | `.github/workflows/` | Workflow definitions that run CI gates |
| Action fixtures | `.github/actions/fixtures/` | Test fixtures used by custom/composite actions |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Graph artifacts | `data/graph/` | Import exports (e.g., CSV) and optional scripts (e.g., Cypher) |
| Schemas | `schemas/` | Contract schemas (JSON Schema, etc.) |
| Documentation | `docs/` | Governed docs and standards |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 graph/
            └── 📁 invalid/
                └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM’s canonical pipeline includes a governed graph stage, and CI is expected to enforce repeatable validation gates. Invalid fixtures provide a controlled way to ensure the validator rejects broken graph inputs rather than silently accepting them.

### Assumptions

- A CI workflow or action consumes these fixtures as part of a **negative test** harness (i.e., it expects the validator to fail on these inputs).
- The exact command/entrypoint that reads these fixtures is **not confirmed in this document**; reference the workflow(s) under `.github/workflows/`.

### Constraints / invariants

- **Determinism:** Invalid fixtures must reliably trigger rejection in the same way across environments.
- **Isolation:** Prefer fixture cases that break **one** rule at a time to make regressions diagnosable.
- **No sensitive content:** Fixtures must be synthetic and must not encode restricted locations, culturally sensitive knowledge, or PII.

### Open questions

- Which workflow/action is the canonical consumer of `fixtures/graph/*`?
- Do we standardize case metadata (e.g., expected error codes/messages), and if so, where does that manifest live?

### Future extensions

- Add a minimal “case manifest” (format TBD) so each invalid case declares:
  - what rule is being violated, and
  - what rejection signal is expected (exit code, error substring, etc.).

## 🗺️ Diagrams

### Process flow

~~~mermaid
flowchart LR
  A[Invalid graph fixture<br/>.github/actions/fixtures/graph/invalid] --> B[Graph validator / integrity checks]
  B -->|rejects (non-zero / error)| C[Negative test passes]
  B -->|accepts unexpectedly| D[CI fails (regression)]
~~~

### Optional sequence diagram

(Not required for this directory; include only if the consuming action/workflow needs a step-by-step contract.)

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Invalid graph fixture(s) | Graph-ingest artifacts (e.g., CSV/Cypher or repo-specific formats) | Hand-authored, synthetic | Must be rejected by graph integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validator rejection | Non-zero exit + log output | CI logs | N/A (behavioral expectation) |
| Regression signal | CI failure when invalid is accepted | CI logs | N/A |

### Sensitivity & redaction

- Fixtures should be synthetic and avoid any real-world sensitive or restricted locations.
- If a fixture needs to resemble real data, generalize and de-identify it (and treat it as review-gated).

### Quality signals

- Each fixture case should document:
  - the **intended failure mode** (what is invalid), and
  - the **expected validator behavior** (what signal proves the validator caught it).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: N/A (fixtures only)
- Items involved: N/A (fixtures only)
- Extension(s): N/A

### DCAT

- Dataset identifiers: N/A (fixtures only)
- License mapping: N/A
- Contact / publisher mapping: N/A

### PROV-O

- `prov:wasDerivedFrom`: N/A (fixtures are hand-authored test inputs)
- `prov:wasGeneratedBy`: N/A
- Activity / Agent identities: N/A

### Versioning

- Keep fixtures small and stable; changes should be accompanied by updates to the consuming test harness (if applicable).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Graph | Ontology-governed ingest + validation | `src/graph/` |
| CI harness | Executes validator against fixtures | `.github/workflows/` (consumer not named here) |
| Fixtures | Provide known-bad inputs | `.github/actions/fixtures/graph/invalid/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Graph contract / ontology bindings | `src/graph/` + `docs/graph/` | Governed changes; migration plan if needed |
| CI expectations | `.github/workflows/` | Deterministic behavior required |

### Extension points checklist (for future work)

- [ ] Graph: add a new invalid fixture case and ensure it is exercised by the negative-test harness
- [ ] CI: ensure behavior is deterministic (invalid → reject; optional roots → skip when absent)
- [ ] Governance: ensure fixtures remain synthetic (no sensitive content)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- N/A — fixtures are CI-only and do not surface directly.

### Provenance-linked narrative rule

- N/A — fixtures are not narrative content.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (for this README)
- [ ] Graph integrity checks (consumer workflow should reject these fixtures)
- [ ] Security and sovereignty checks (ensure fixtures contain no sensitive content)

### Reproduction

~~~bash
# Locate the workflow/action that consumes graph fixtures:
#   .github/workflows/*.yml
#
# Then run the underlying graph validator locally.
# (Exact command is not confirmed in this document; it should mirror CI.)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes to fixture data should be reviewed by maintainers of the graph validator / CI workflows.
- Any fixture that resembles real data should be treated as review-gated and checked for sensitivity risks.

### CARE / sovereignty considerations

- Fixtures must not include culturally sensitive knowledge, restricted site locations, or information requiring community consent/controls.

### AI usage constraints

- This README inherits the front-matter AI permissions/prohibitions and must not be used to infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for invalid graph fixtures | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
