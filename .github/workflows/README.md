---
title: "KFM — GitHub Actions Workflows (CI/CD) README"
path: ".github/workflows/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:ci:workflows-readme:v1.0.1"
semantic_document_id: "kfm-ci-workflows-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:ci:workflows-readme:v1.0.1"
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

# .github/workflows — GitHub Actions for KFM

## 📘 Overview

### Purpose

This README documents how KFM uses GitHub Actions to enforce repository-wide contracts, validation gates, and “repo lint” rules across the canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

The goal is to keep CI aligned with KFM’s **contract-first**, **evidence-first**, **provenance-first** architecture.

### Scope

| In Scope | Out of Scope |
|---|---|
| GitHub Actions workflows in `.github/workflows/*.yml` (CI checks, validations, scans, scheduled jobs) | Cloud deployment specifics and infra provisioning (belongs under `tools/` and/or separate ops repos) |
| CI gate alignment to KFM contracts and canonical paths | Implementing ETL/domain pipelines (tracked in subsystem docs/runbooks) |
| Workflow determinism rules (skip vs fail behavior) | Adding datasets or story content (handled under `data/` / `docs/`) |

### Audience

- Primary: repo maintainers + contributors authoring/editing CI workflows.
- Secondary: data/catalog/graph/API/UI/story maintainers who depend on CI guarantees.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **CI gate**, **repo lint**, **canonical path**, **schema validation**, **Story Node validation**, **API contract tests**, **security/sovereignty scans**, **deterministic runs**.

### Key artifacts (what this doc points to)

> Paths below are **expected**. If a referenced path is missing, treat it as **not confirmed in repo** and avoid hard-coding CI assumptions without a deprecation/migration note.

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Canonical pipeline ordering + invariants |
| Redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Canonical roots + v13 readiness gates (draft; if adopted) |
| This README | `.github/workflows/README.md` | CI maintainers | Documents workflow expectations |
| Local actions README | `.github/actions/README.md` | CI maintainers | Reusable repo-local CI “gate” actions (if present) |
| Tests README | `tests/README.md` | Test owners | Test taxonomy + determinism rules (if present) |
| Schema registry | `schemas/README.md` | Contract owners | Schemas for STAC/DCAT/PROV/story/ui/telemetry (if present) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] CI gate expectations align to Master Guide v12 and (if adopted) the v13 blueprint
- [ ] Gate behavior is explicit: **validate if present**, **fail if invalid**, **skip if not applicable**
- [ ] No stale workflow references (don’t list file names that aren’t present in-repo)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] No secrets, tokens, or sensitive locations embedded in this README

---

## 🗂️ Directory Layout

### This document

- `path`: `.github/workflows/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub workflows | `.github/workflows/` | GitHub Actions workflows for tests, validations, and scans |
| Local actions (optional) | `.github/actions/` | Repo-local composite actions invoked by workflows |
| Schemas (optional root) | `schemas/` | JSON Schemas and constraint bundles used by CI + runs |
| Data domains | `data/<domain>/` | `raw/`, `work/`, `processed/` per domain |
| STAC | `data/stac/` | `collections/` + `items/` outputs |
| DCAT (optional root) | `data/catalog/dcat/` | dataset catalog records |
| PROV (optional root) | `data/prov/` | lineage bundles |
| Graph import (optional) | `data/graph/` | CSV + Cypher outputs for Neo4j ingest |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Graph build | `src/graph/` | ontology bindings + build scripts |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) |
| UI | `web/` | React/MapLibre UI; layer registry under `web/**/layers/**` (if used) |
| Story Nodes (optional root) | `docs/reports/story_nodes/` | governed narrative artifacts + metadata |

### Expected file tree for this sub-area

~~~text
📁 .github/
└── 📁 workflows/
    ├── 📄 README.md
    └── 📄 *.yml
~~~

> Note: This README intentionally avoids enumerating workflow file names unless they are confirmed present in-repo. Keep this document synchronized with the actual `.yml` files.

---

## 🧭 Context

KFM’s CI is a **pipeline contract enforcement layer**, not just “unit tests.” It exists to keep the system aligned to:

- canonical pipeline ordering and invariants,
- contract-first API boundaries (**UI must not query Neo4j directly**),
- provenance-first content rules (no unsourced narrative),
- schema-valid catalogs and story outputs.

### Repo drift and “optional roots”

Some canonical roots may be absent in a given repository snapshot (“not confirmed in repo”). CI should be written to handle this safely:

- **Validate if present**: if a canonical root exists (or changes), validate its artifacts.
- **Fail deterministically if invalid**: schema errors, missing links, orphan references fail the job.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

> This “validate / fail / skip” contract is the safest default when the repository is evolving toward v13 readiness.

### Canonical homes and consolidation note

KFM guidance expects **one canonical home per subsystem**. If the repo contains overlapping/duplicated homes (e.g., both `src/api/` and `src/server/`), workflows must not “paper over” the conflict by validating both indefinitely. Instead:

- treat duplication as drift,
- require a deprecation/consolidation plan,
- update workflows and docs once the canonical home is chosen.

---

## 🗺️ Diagrams

### Canonical pipeline and where CI gates apply

~~~mermaid
flowchart LR
  A["ETL (src/pipelines)"] --> B["Catalogs (data/stac + data/catalog/dcat + data/prov)"]
  B --> C["Graph (data/graph + src/graph)"]
  C --> D["API Boundary (src/server + contracts)"]
  D --> E["UI (web)"]
  E --> F["Story Nodes (docs/reports/story_nodes)"]
  F --> G["Focus Mode (provenance-linked only)"]

  CI["CI Gates (.github/workflows)"] -. validates .-> A
  CI -. validates .-> B
  CI -. validates .-> C
  CI -. validates .-> D
  CI -. validates .-> E
  CI -. validates .-> F
~~~

### CI gate flow on Pull Requests

~~~mermaid
flowchart TB
  PR["Pull Request"] --> CI["GitHub Actions"]
  CI --> MD["Markdown protocol validation"]
  CI --> SC["Schema validation"]
  CI --> SN["Story Node validation"]
  CI --> API["API contract tests"]
  CI --> SEC["Security + sovereignty scanning"]
  MD --> OK["Merge allowed"]
  SC --> OK
  SN --> OK
  API --> OK
  SEC --> OK
~~~

### Workflows → (optional) local actions → gates

> Mermaid rendering note:
> - Avoid unquoted `*` (wildcards) inside node labels.
> - Prefer quoted labels: `NODE["text with / and ( )"]`.

~~~mermaid
flowchart LR
  PR["PR / Push / Schedule"] --> WF[".github/workflows (workflow files)"]
  WF --> ACT[".github/actions (local actions, optional)"]

  ACT --> G1["Docs: Markdown protocol validation"]
  ACT --> G2["Schemas: STAC/DCAT/PROV + Story/UI/Telemetry schemas"]
  ACT --> G3["Graph: integrity checks (no broken refs)"]
  ACT --> G4["API: contract tests (OpenAPI/GraphQL)"]
  ACT --> G5["UI: registry/schema checks"]
  ACT --> G6["Security + sovereignty scans (as applicable)"]
~~~

---

## 📦 Data & Metadata

### CI inputs

- The repository content under canonical roots (e.g., `schemas/`, `data/`, `src/`, `web/`, `docs/`).
- A PR diff or branch tip on push.
- Optional: cached dependencies and/or precomputed validation artifacts.

### CI outputs

- Status checks on PRs/branches.
- Optional artifacts (test reports, schema validation reports, lint summaries).

### Artifact handling and redaction

- Treat workflow logs as potentially public. Never print secrets, tokens, or sensitive location details.
- Prefer **summary outputs** (counts, pass/fail) over uploading raw restricted data as artifacts.
- If a scan/validator produces sensitive detail, either:
  - redact before upload, or
  - store only pointers/IDs and keep restricted outputs out of public CI artifacts.

### Quality signals

CI should provide (at minimum) signals that:

- STAC/DCAT/PROV artifacts validate against schemas in `schemas/` (if the root exists).
- No orphan references (entity refs, evidence refs, Story Node refs resolve where applicable).
- Runs are deterministic and outputs are diffable.

---

## 🌐 STAC, DCAT & PROV Alignment

CI workflows are expected to validate that catalog and lineage outputs adhere to KFM’s canonical layout:

- STAC outputs in `data/stac/**`
- DCAT outputs in `data/catalog/dcat/**` *(optional root; may be absent depending on repo snapshot)*
- PROV outputs in `data/prov/**` *(optional root; may be absent depending on repo snapshot)*

Schemas for these typically live under `schemas/stac/`, `schemas/dcat/`, and `schemas/prov/` (plus additional schema families for Story Nodes, UI, telemetry).

---

## 🧱 Architecture

### CI gates required for v13 readiness

Minimum CI gates (v13 readiness) should include:

- Markdown protocol validation
- Schema validation
- Story Node validation
- API contract tests
- Security and sovereignty scanning gates

CI should also enforce basic “repo lint” rules:

- No duplicate canonical homes for the same subsystem without explicit deprecation markers.
- No typo-paths or shadow directories that bypass governance checks.

### CI behavior contract (skip vs fail)

CI workflows must be deterministic in “skip vs fail” behavior:

- **Skip** when an optional root is absent.
- **Fail** when the root exists but artifacts are invalid (schema errors, broken refs, missing required metadata).

> Keep this behavior consistent so contributor expectations match CI outcomes.

### Gate taxonomy (conceptual map)

This table describes “what CI is responsible for,” without assuming specific workflow file names.

| Gate category | What it protects | Canonical roots | Typical trigger | Skip condition | Fail condition |
|---|---|---|---|---|---|
| Docs / Markdown protocol | Governed docs + front-matter integrity | `docs/**`, selected `README.md` files | PRs touching docs | N/A | Invalid front-matter, missing required sections, broken required footer refs |
| Schemas | Contract correctness | `schemas/**` | PRs touching schemas | Root absent | Invalid schema bundles, breaking changes without version bump (if enforced) |
| Catalog validation | Evidence artifacts | `data/stac/**`, `data/catalog/dcat/**` | PRs touching data catalogs | Root absent | STAC/DCAT validation failures, broken links |
| Provenance validation | Lineage integrity | `data/prov/**` | PRs touching prov bundles | Root absent | Orphan refs, missing required links (prov:wasDerivedFrom / prov:wasGeneratedBy) |
| Graph integrity | Graph ingest correctness | `src/graph/**`, `data/graph/**` | PRs touching graph build/import | Root absent | Broken constraints, invalid mappings, missing required fixtures |
| API contract tests | API boundary stays canonical | `src/server/contracts/**` | PRs touching API/contracts | Root absent | Contract test failures, breaking API changes without coordination |
| UI registry checks | UI doesn’t bypass contracts | `web/**` (esp. `web/**/layers/**`) | PRs touching UI/layers | Root absent | Registry/schema validation failures, a11y checks (if configured) |
| Security + sovereignty | No leaks, no unsafe policy bypass | repo-wide | PRs, scheduled | N/A | Secrets/PII/sensitive-location disclosure, policy gate violations (when applicable) |

### Workflow security baseline (recommended)

- Use least-privilege `permissions:` per workflow/job.
- Avoid patterns that execute untrusted code with elevated permissions.
- Prefer repo-local actions (`.github/actions/**`) for core gates so contract logic is:
  - versioned,
  - reviewable,
  - and consistent across workflows.

> If any workflow change increases permissions, broadens token access, or modifies security/sovereignty gates, treat it as **requires human review**.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes are governed artifacts and must live at:

- `docs/reports/story_nodes/` *(canonical; may be absent in some repo snapshots)*

Design rules that CI should enforce for published Story Nodes (when the root exists):

- validate front-matter, citations, entity references, redaction compliance.
- Focus Mode consumes only provenance-linked content.
- Predictive/AI-generated content is opt-in and includes uncertainty metadata; it must never appear as unmarked fact.

---

## 🧪 Validation & CI/CD

### What CI must enforce (conceptual checklist)

- [ ] Markdown protocol validation for governed docs that require it
- [ ] Schema validation for any STAC/DCAT/PROV outputs present
- [ ] Story Node validation for published nodes
- [ ] API contract tests for `src/server/contracts/**`
- [ ] Security + sovereignty scanning gates (especially for sensitive locations, restricted knowledge, and redaction expectations)

### Local validation

Not confirmed in repo: the exact local commands/scripts/Make targets. If local tooling exists, document it here (and keep it in sync with CI).

~~~bash
# not confirmed in repo — replace with repo’s actual validation commands
# make lint-docs
# make validate-schemas
# make validate-catalogs
# make validate-prov
# make test-graph
# make test-api-contracts
# make validate-ui
# make scan-security
~~~

### Workflow change checklist (for reviewers)

When reviewing a workflow PR:

- [ ] Does the workflow follow **skip vs fail** determinism?
- [ ] Are `permissions:` scoped to the minimum required?
- [ ] Are artifacts/logs non-sensitive and appropriately redacted?
- [ ] Are canonical roots referenced correctly (no duplication drift)?
- [ ] If new gates are introduced: is ownership clear (CODEOWNERS, review rules, doc updates)?

---

## ⚖ FAIR+CARE & Governance

### Sensitivity and redaction enforcement

Any restricted locations or culturally sensitive knowledge must be protected via:

- generalization of geometry where required,
- API-level redaction,
- Story Node asset review gates.

CI should treat sensitivity and redaction violations as **blocking** for merges when the relevant artifacts are present.

### Governance approvals required (if any)

- FAIR+CARE council review: yes/no
- Security council review: yes/no
- Historian/editor review: yes/no

### AI usage constraints

This README’s AI transform permissions/prohibitions are defined in front-matter and should remain aligned with repo governance.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial workflows README scaffold | TBD |
| v1.0.1 | 2025-12-24 | Clarified optional roots + deterministic skip/fail contract; added local-actions linkage; removed stray external citation marker | TBD |

---

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
