---
title: "KFM Master Guides — README"
path: "docs/master_guides/README.md"
version: "v0.1.0"
last_updated: "2026-02-18"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"

# Profile versions (optional; keep for tooling)
markdown_protocol_version: "1.0"

# Governance metadata (keep fields; use TBD if unknown)
governance_ref: "TBD"
ethics_ref: "TBD"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

doc_uuid: "urn:kfm:doc:master-guides:readme:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# KFM Master Guides (docs/master_guides)

![Governed](https://img.shields.io/badge/Governed-Yes-success)
![Evidence-first](https://img.shields.io/badge/Evidence--first-Required-informational)
![Policy](https://img.shields.io/badge/Policy-Fail--closed-critical)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Aligned-blueviolet)

Master Guides are **cross-cutting, stable** documents that keep Kansas Frontier Matrix (KFM) coherent end-to-end:

> **data → pipeline → catalogs/provenance → APIs → UI / Focus Mode / Story Nodes**

They are the “glue layer” between specs, contracts, and implementation.

---

## Overview

### Purpose

- Provide a **single index** for KFM’s system-level guides.
- Preserve **non-negotiable invariants** (trust membrane, governance gates, evidence-first behavior).
- Reduce “truth drift” by keeping core patterns centralized and reviewable.

### Scope

| In Scope (Master Guides) | Out of Scope (Belongs Elsewhere) |
|---|---|
| Architecture invariants & boundaries (clean layers, trust membrane) | One-off investigations, brainstorming notes |
| Cross-pipeline contracts (IDs, receipts, catalogs, provenance, policy inputs) | Pipeline-specific step-by-step recipes (put in `docs/pipelines/**`) |
| System-wide governance rules, review lanes, “fail closed” posture | Operational incident response runbooks (put in `docs/runbooks/**`) |
| Story Node + Focus Mode behavioral contracts and evidence UX expectations | Raw research literature dumps (put in `docs/research/**`) |

### Audience

- **Primary:** platform/backend/data engineers, governance & security maintainers.
- **Secondary:** researchers, storytellers, UI engineers, reviewers.

### Definitions

| Term | Meaning (KFM usage) |
|---|---|
| **Truth Path** | The canonical lifecycle: acquire → validate → enrich → catalog → serve → explain. |
| **Trust membrane** | UI/clients **never** access data stores directly; all access goes through governed APIs + policy boundary. |
| **Fail-closed** | When policy/validation is uncertain, deny by default; prefer abstention over unsafe outputs. |
| **Evidence bundle** | The resolvable artifacts (catalog/provenance/receipts) that support a claim, layer, or narrative. |
| **Story Node** | A machine-ingestible narrative artifact tied to evidence references and governance constraints. |
| **Focus Mode** | A governed, evidence-first query experience that must cite or abstain and emit audit context. |

### Key Artifacts

| Artifact | Why it matters | Typical location |
|---|---|---|
| Policy bundles (OPA/Rego) + fixtures | Enforces governance at CI + runtime | `policy/**` (or equivalent) |
| Catalogs (STAC/DCAT) + provenance (PROV) | Discovery + lineage + evidence resolution | `data/**/catalog/**` (pattern) |
| Receipts / run records | Auditable transformation history | `data/**/receipts/**` (pattern) |
| API contracts | Trust membrane surface | `src/**`, `docs/api/**` (pattern) |
| UX evidence drawers | “Show your work” for layers/claims | `web/**` (pattern) |

### Definition of Done (for this README)

- [x] Has front-matter (metadata + governance fields).
- [x] Defines what “Master Guides” are and what they are not.
- [x] Includes a registry and contribution workflow.
- [ ] Linked master guides exist (as this folder grows).
- [ ] CI checks for Markdown lint + link integrity are enabled.

---

## Directory layout

### Suggested repository “shape” (target state)

> Use this as a map. If the repo diverges, update this README to match reality.

```text
.
├─ data/                 # raw/work/processed + catalogs + provenance (truth artifacts)
├─ docs/
│  ├─ master_guides/     # ← YOU ARE HERE (system-level guides)
│  ├─ pipelines/         # pipeline specs (per dataset family / connector)
│  ├─ runbooks/          # ops/reliability runbooks
│  ├─ research/          # governed research drafts + evaluations
│  ├─ standards/         # standards profiles (STAC/DCAT/PROV overlays), conventions
│  └─ templates/         # doc templates (Universal Doc, Story Node v3, etc.)
├─ src/                  # backend (domain/usecases/adapters/infrastructure)
├─ web/                  # UI (React/TS + map + Story/Focus experiences)
├─ policy/               # OPA/Rego policies (CI + runtime)
└─ .github/              # CI workflows (merge-blocking governance)
```

### How Master Guides map to the KFM “Truth Path”

| Truth Path step | What to document here | Where it becomes “real” |
|---|---|---|
| 1) Acquire | Source onboarding rules, licensing requirements, ingestion patterns | connectors/watchers, pipeline specs |
| 2) Validate | Schema/QA gates, materiality rules, test fixtures | CI validators + pipeline validators |
| 3) Enrich | Geocoding/time normalization/entity linking standards | enrich jobs + graph/search builders |
| 4) Catalog | STAC/DCAT/PROV profile overlays, evidence IDs | catalog emitters + registries |
| 5) Serve | API boundary + auth + policy contract, rate limits, audit | API gateway + policy PDP |
| 6) Explain | Story Nodes + Focus Mode citation/abstention + evidence UX | UI + retrieval + policy + audit |

---

## Master guide registry

> This is a **registry**, not a wish-list: only add a guide topic here if you intend to keep it current.

| Topic | What it standardizes | Proposed filename | Owner role | Status |
|---|---|---|---|---|
| Architecture & trust membrane | Clean layers, interface boundaries, “no direct DB access” | `architecture_trust_membrane.md` | Platform Eng | planned |
| Governance & fail-closed policy | CI gates, runtime policy inputs, review lanes | `governance_fail_closed.md` | Governance/Security | planned |
| Catalogs & provenance | STAC/DCAT/PROV overlays, evidence resolver conventions | `catalogs_provenance.md` | Data Steward | planned |
| IDs & immutability | Canonical IDs, versioning, release immutability | `ids_versioning.md` | Platform Eng | planned |
| Focus Mode contract | Cite-or-abstain, audit references, policy checks | `focus_mode_contract.md` | Product + Security | planned |
| Story Node contract | Schema rules, evidence bundle binding, sensitivity handling | `story_node_contract.md` | Story/Research | planned |
| Sensitivity & CARE handling | Generalization/redaction rules, authority-to-control tags | `sensitivity_care.md` | Governance Council | planned |
| Serving formats | “processed is truth” formats (COG/GeoParquet/PMTiles, etc.) | `serving_formats.md` | Data + Platform | planned |
| Observability & audit | Audit ledger events, correlation IDs, telemetry minimums | `audit_observability.md` | Platform/SRE | planned |

---

## How to add or update a master guide

### 1) Start from the Universal Doc structure

Master Guides must be **template-aligned** and machine-checkable.

Minimum recommended structure:

- Front-matter (YAML)
- `## Overview` (Purpose / Scope / Audience / Definitions)
- `## Directory layout` (how it fits in repo/system)
- Main guide content sections
- `## Definition of Done` checklist
- `## References`

### 2) Front-matter rules (governed docs)

- Keep required fields even if unknown (use `TBD`).
- Keep `path`, `version`, `last_updated`, `status`, `doc_uuid`.
- If the guide defines a contract that would break consumers, bump `version`.

### 3) Add the guide to the registry table

- Add a row under **Master guide registry** (above).
- Use a stable filename.
- Assign an **owner role** (not an individual) to avoid “orphaned docs”.

### 4) Validate before merge (expected)

At minimum, guides should pass:

- Markdown lint (style + consistency)
- Link integrity (no broken internal references)
- Governance scan (no sensitive leakage, correct care_label)
- If the guide affects policy/contracts, it should be reviewed by governance/security

---

## Governance and safety notes

### Non-negotiables (system invariants)

- **Evidence-first:** every claim should trace to evidence or be labeled “not confirmed.”
- **Fail-closed:** deny/abstain is a valid outcome when policy/evidence is insufficient.
- **Trust membrane:** clients do not bypass the governed API boundary.
- **Auditability:** important decisions and outputs should be traceable.

### Sensitivity handling (CARE-aligned)

- Do **not** publish precise locations for sensitive sites in public artifacts.
- Use `care_label` to signal additional review requirements (e.g., “Tribal Sensitive”).
- When in doubt, generalize/redact and escalate to governance review.

---

## Appendix: minimal “new guide” skeleton

```markdown
---
title: "TEMPLATE — Master Guide Title"
path: "docs/master_guides/TEMPLATE__MASTER_GUIDE.md"
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"
markdown_protocol_version: "1.0"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US"
doc_uuid: "urn:kfm:doc:master-guides:<slug>:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# Master Guide — <Title>

## Overview
### Purpose
### Scope
### Audience
### Definitions

## Directory layout

## Main content

## Definition of Done
- [ ] Front-matter complete & valid
- [ ] Required sections present
- [ ] Claims trace to evidence or clearly marked
- [ ] No broken links
- [ ] Governance review if care_label != Public

## References
```

---

## References

- **KFM Masterpiece Vision** (generated 2026-02-16)
- **KFM Blueprint & Ideas / Integration Pack** (governance + policy-as-code concepts)
- **Comprehensive Markdown Guide** (KFM-inspired templates and metadata patterns)
