---
title: "KFM — docs/reports (Governed Reports & Story Nodes)"
path: "docs/reports/README.md"
version: "v1.0.0"
last_updated: "2026-02-14"
status: "active"
doc_kind: "README"
license: "CC-BY-4.0"
sensitivity: "public"
care_label: "Public"
markdown_protocol_version: "1.0"
governance:
  root: "../governance/ROOT_GOVERNANCE.md"
  review_gates: "../governance/REVIEW_GATES.md"
  ethics: "../governance/ETHICS.md"
  sovereignty: "../governance/SOVEREIGNTY.md"
---

# docs/reports — Governed Reports & Story Nodes 🧭🧾

![Governed](https://img.shields.io/badge/Governed-Yes-blue)
![Evidence-First](https://img.shields.io/badge/Evidence--First-Required-brightgreen)
![CI](https://img.shields.io/badge/CI-Validated-informational)
![Trust Membrane](https://img.shields.io/badge/Trust%20Membrane-Enforced-important)

This directory contains **governed narrative + report artifacts** intended to be consumed by KFM’s **Story Mode** and/or **Focus Mode**. Every claim must be traceable to evidence, and every artifact must remain compatible with the repo’s **contract-first / evidence-first** pipeline.

> **Hard rule:** If a report or Story Node can’t cite evidence, it must **abstain** from making the factual claim.  
> This is not “nice to have” — it is a system guardrail.

---

## Quick links

- 📘 Master Guide: `../MASTER_GUIDE_v13.md`
- 🧩 Templates:
  - Universal doc template: `../templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
  - Story Node template (v3): `../templates/TEMPLATE__STORY_NODE_V3.md`
  - API contract extension template: `../templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- ⚖️ Governance & review gates:
  - Root governance: `../governance/ROOT_GOVERNANCE.md`
  - Review gates: `../governance/REVIEW_GATES.md`
  - Ethics: `../governance/ETHICS.md`
  - Sovereignty: `../governance/SOVEREIGNTY.md`
- 🧾 Evidence catalogs (authoritative evidence lives here — reports link *to* these):
  - STAC: `../../data/stac/`
  - DCAT: `../../data/catalog/dcat/`
  - PROV: `../../data/prov/`
- 🧪 Methods & computational runs (code / run receipts do **not** live in docs): `../../mcp/`

---

## Table of contents

- [Purpose](#purpose)
- [Trust membrane + evidence-first rules](#trust-membrane--evidence-first-rules)
- [Directory layout](#directory-layout)
- [Story Nodes](#story-nodes)
  - [Lifecycle: draft → review → published](#lifecycle-draft--review--published)
  - [Story folder structure](#story-folder-structure)
  - [Citations & Evidence Bundle rules](#citations--evidence-bundle-rules)
  - [Story authoring checklist](#story-authoring-checklist)
- [Non-story reports](#non-story-reports)
  - [Where should this document live](#where-should-this-document-live)
  - [Report naming conventions](#report-naming-conventions)
  - [Report metadata](#report-metadata)
- [Sensitivity & redaction guidance](#sensitivity--redaction-guidance)
- [Validation & CI gates](#validation--ci-gates)
- [Definition of Done](#definition-of-done)
- [Common failures & fixes](#common-failures--fixes)

---

## Purpose

`docs/reports/` is the governed home for:

1. **Story Nodes** — curated, machine-ingestible narratives used by Story Mode and referenced by Focus Mode.
2. **Governed reports** — analysis or design reports that support decisions or narratives *and* are safe to ship as documentation.

### What belongs here

- ✅ Story Nodes (draft/review/published)
- ✅ Research/analysis memos that:
  - cite evidence (STAC/DCAT/PROV/graph/doc),
  - state assumptions and limitations,
  - are safe to render for intended audiences, and
  - follow governance + sensitivity rules.

### What does *not* belong here

- ❌ Raw or processed data files (those belong under `data/…`)
- ❌ Pipeline run receipts / experiment logs (those belong under `mcp/…` and/or pipeline outputs)
- ❌ Secrets or credentials (ever)
- ❌ Unreviewed “fact dumps” with no citations
- ❌ Anything that bypasses the governed API boundary (e.g., “run this SQL directly on prod”)

---

## Trust membrane + evidence-first rules

KFM enforces a strict “trust membrane” and provenance discipline. For content in `docs/reports/`, that means:

- **Do not instruct** readers (or the UI) to access databases directly.
- **Do not embed** restricted datasets or sensitive coordinates inside narrative docs.
- **Do not cite** “floating” URLs or screenshots as primary evidence if the evidence is already represented in KFM catalogs.

Instead, Story Nodes and reports should reference:

- `dcat://…` dataset identifiers (discovery / dataset-level provenance)
- `stac://…` items/collections (spatial asset-level evidence)
- `prov://…` lineage bundles (how it was produced, checksums, agents, transforms)
- `graph://…` references when you need semantic context (still must link back to catalogs)

> **Rule of thumb:**  
> If it affects a claim, you should be able to point to an evidence bundle that can be resolved through the governed system.

---

## Directory layout

The **canonical** layout for story content is governed and should not drift.

```text
docs/
└── reports/                                   # Long-form, governed narrative outputs (human-readable, citation-backed)
    ├── README.md                              # (This file) — how reports/story nodes work, rules, and publishing flow
    │
    └── story_nodes/                           # Story Nodes: auditable narratives tied to evidence + datasets
        ├── templates/                         # Optional: starter bundles/snippets for authors (frontmatter, sections, ADR refs)
        │
        ├── draft/                             # Work-in-progress Story Nodes (not authoritative; may change without notice)
        │   └── river-trade-1850s/             # Story Node slug (kebab-case; stable identifier once published)
        │       ├── story.md                   # Draft narrative (must include citations + evidence links where possible)
        │       └── assets/                    # Supporting artifacts referenced by story.md (keep small; prefer derived outputs)
        │           ├── overview-map.png        # Visual summary for the story (rendered/derived, not raw source data)
        │           └── river-corridor.geojson  # Spatial overlay used in figures/maps (derived; include provenance notes in story)
        │
        └── published/                         # Reviewed + released Story Nodes (authoritative; versioned + stable)
            └── river-trade-1850s/             # Published slug matches draft slug (enables diff + traceability)
                ├── story.md                   # Final narrative (passes policy: cite-or-abstain, sensitivity, licensing)
                └── assets/                    # Published assets (frozen; must match story references exactly)
                    ├── overview-map.png        # Released figure (immutable unless version bump / republish)
                    └── river-corridor.geojson  # Released overlay (immutable; changes require republish + new provenance)
```

### Optional subfolders (create only when needed)

If you need to store non-story reports here, prefer a small, explicit structure:

```text
docs/reports/
├── research/         # investigation memos supporting stories/features
├── audits/           # governance/security/privacy audits (sanitized as needed)
└── decisions/        # narrative decision records that are not ADRs (ADRs remain in docs/architecture/adr/)
```

If a document is truly architecture/design, it probably belongs under `docs/architecture/` instead.

---

## Story Nodes

Story Nodes are **structured narrative artifacts** with a strict template (v3) and schema validation. They are designed to be:

- human-readable,
- machine-ingestible,
- evidence-linked,
- safe for governed rendering.

### Lifecycle: draft → review → published

| Status | Where it lives | Who can change it | Expectations |
|---|---|---:|---|
| `draft` | `docs/reports/story_nodes/draft/<slug>/story.md` | author(s) | may be incomplete, but **no unsourced facts** |
| `review` | `draft/` (or a review branch) | reviewers + author | citations complete; governance review triggered as needed |
| `published` | `docs/reports/story_nodes/published/<slug>/story.md` | restricted via review gates | stable story_id; high bar for edits |

> Recommended practice: Only move a story into `published/` via PR, with the required governance approvals defined in `docs/governance/REVIEW_GATES.md`.

### Story folder structure

Each story lives in a folder named with a stable **slug**:

- Use **kebab-case**: `river-trade-1850s`, `kansas-dust-bowl`, `rail-expansion-1880s`
- Avoid spaces, punctuation, or date prefixes in the folder name.
- A published story’s slug should be treated as stable (do not rename without a migration plan).

Minimum files:

- `story.md` — the governed narrative
- `assets/` — local story assets (images, small GeoJSON, diagrams, etc.)

### Citations & Evidence Bundle rules

Every Story Node must:

- include a YAML front matter block with `story_id`, `template_version`, `status`, and `evidence_bundle` references,
- include an **Evidence & Citations** section with footnote-style citations,
- ensure citations are **resolvable** (by ID/path) inside the repo or through governed evidence endpoints.

#### Minimal Story Node skeleton (v3-compatible)

> Canonical template lives at: `../templates/TEMPLATE__STORY_NODE_V3.md`  
> This skeleton is provided for convenience and must match the template/schema in-repo.

```markdown
---
story_id: "urn:kfm:story:river-trade-1850s"
title: "River Trade Corridors in the 1850s"
summary: "How river travel shaped early Kansas settlement patterns."
template_version: "v3"
status: "draft"
tags: ["transport", "rivers", "settlement"]
time_range: ["1850-01-01", "1859-12-31"]
bbox: [-102.051, 36.993, -94.588, 40.003] # Kansas-ish bbox example
evidence_bundle:
  stac: ["stac://kfm.hydro.rivers/1850s_corridor"]
  dcat: ["dcat://kfm.dataset.river_trade_corridors"]
  prov: ["prov://kfm.prov.run.2026-02-01T12:00:00Z"]
  graph: ["graph://kfm.story_context.river_trade_1850s"]
---

# Overview
Narrative overview text... [^c1]

# Step 1: Why rivers mattered
Step text... [^c2]

# Evidence & Citations
[^c1]: kind=dcat ref="dcat://kfm.dataset.river_trade_corridors" locator="dct:description" note="Dataset overview + scope."
[^c2]: kind=prov ref="prov://kfm.prov.run.2026-02-01T12:00:00Z" locator="activity:derive_corridor" note="Lineage for corridor derivation; includes parameters + checksum."
```

### Story authoring checklist

- [ ] Story is placed under `docs/reports/story_nodes/draft/<slug>/`
- [ ] `story_id` is **stable** and unique
- [ ] `template_version: "v3"` and required front matter fields are present
- [ ] Every factual claim has at least one citation
- [ ] Evidence bundle references exist (STAC/DCAT/PROV/graph/doc as appropriate)
- [ ] Asset files are referenced with **relative paths**, have descriptive filenames, and images include alt text
- [ ] Sensitivity is handled (see [Sensitivity & redaction guidance](#sensitivity--redaction-guidance))
- [ ] Link checks pass (no broken internal references)
- [ ] CI validations pass locally / in PR

---

## Non-story reports

Story Nodes are the primary “report” type expected under `docs/reports/`. When you need additional documentation here, keep it **clearly categorized** and governed.

### Where should this document live?

Use this decision guide:

| Document type | Best home |
|---|---|
| Story narrative meant for UI playback | `docs/reports/story_nodes/…` |
| Architecture design, ADR, system blueprint | `docs/architecture/…` |
| Domain ETL runbook / dataset notes | `docs/data/<domain>/README.md` |
| Experiments, notebooks, model cards, run receipts | `mcp/…` |
| Report supporting a story or governance review | `docs/reports/research/` or `docs/reports/audits/` |

### Report naming conventions

For Markdown reports under `docs/reports/` (non-story):

- Use date + topic prefix for sorting and auditability:

```text
YYYY-MM-DD__topic__short-title.md
```

Example:

```text
docs/reports/research/2026-02-14__evidence-resolver__citation-resolution-gaps.md
```

### Report metadata

All non-story reports in this folder **should** include YAML front matter (so CI can enforce protocol requirements).

Recommended minimum:

```yaml
---
title: "Report — Citation Resolution Gaps (Evidence Resolver)"
path: "docs/reports/research/2026-02-14__evidence-resolver__citation-resolution-gaps.md"
version: "v1.0.0"
last_updated: "2026-02-14"
status: "draft"
doc_kind: "Report"
license: "CC-BY-4.0"
sensitivity: "public"
care_label: "Public"
evidence_bundle:
  dcat: ["dcat://kfm.dataset.evidence_resolver_logs"]
  prov: ["prov://kfm.prov.run.2026-02-14T18:00:00Z"]
---
```

---

## Sensitivity & redaction guidance

KFM treats sensitivity as a first-class concern. As an author:

- **Do not publish sensitive locations at high precision** in Story Nodes or reports.
- **Do not include personal identifiers** unless policy explicitly allows it.
- **When redaction occurs**, it must be traceable as a transformation (and reflected in PROV / dataset versioning).

Recommended sensitivity classes (align your reporting behavior to the strictest applicable class):

| Class | What it means | Authoring guidance |
|---|---|---|
| Public | Safe to publish | Normal citation discipline still required |
| Restricted | Requires role-based access | Avoid embedding the data; cite governed dataset IDs and describe at high level |
| Sensitive-location | Coordinates must be generalized/suppressed | Use coarse geometry (bbox/county-level) or omit coordinates; explain why |
| Aggregate-only | Publish only above thresholds | Use aggregation; avoid small counts; document aggregation rule |

If you suspect a report/story could introduce risk (re-identification, sacred sites, endangered species locations, etc.):

- mark it clearly in front matter (`sensitivity: "restricted"` or `"sensitive-location"`),
- trigger governance review per `docs/governance/REVIEW_GATES.md`,
- prefer publishing a redacted derivative dataset and citing that.

---

## Validation & CI gates

KFM CI enforces documentation quality and governance. Expect checks such as:

- Markdown protocol & front matter validation (required sections + metadata present)
- Link/reference validation (no broken links or unresolved reference tags)
- Story Node schema validation (template_version + required structure)
- Security & governance scans (secrets, PII, sensitive locations, classification drift)

> If CI fails, fix the artifact — do not “work around” validations. These checks are part of KFM’s governance model.

---

## Definition of Done

### DoD — Story Node (draft → publish)

- [ ] YAML front matter valid and complete (v3 template)
- [ ] All factual statements cite evidence (no orphan claims)
- [ ] Evidence bundle references are resolvable and appropriate
- [ ] Sensitivity handled (no precise sensitive locations; restricted content not embedded)
- [ ] Links valid; assets present; no missing files
- [ ] Governance review completed if triggered
- [ ] CI validations pass
- [ ] Story moved into `published/` only via PR + required approvals

### DoD — Non-story report

- [ ] YAML front matter valid and complete
- [ ] Claims cite evidence or clearly marked as assumptions/analysis
- [ ] Any computations referenced are reproducible (link to `mcp/…` run or PROV)
- [ ] Sensitivity handled and labeled
- [ ] Link-check clean; no missing references
- [ ] CI validations pass

---

## Common failures & fixes

| Failure | Why it happens | Fix |
|---|---|---|
| “Missing YAML front matter” | doc protocol requires metadata | add/repair the top `--- … ---` block |
| “Missing required section” | template enforcement | add the required section headings (Overview/Directory Layout/etc. as applicable) |
| “Broken internal link” | moved/renamed file, wrong relative path | update link; prefer relative links; rerun link checker |
| “Unresolvable citation ref” | citation points to non-existent evidence | replace with valid STAC/DCAT/PROV/doc reference |
| “Sensitive location flagged” | coordinates exposed | generalize geometry; cite redacted derivative; escalate review |
| “Classification drift” | output labeled more public than input | correct labels; document transformation + redaction provenance |

---

## Maintenance note

This README is itself a governed artifact. Changes to conventions, layout, or required fields may impact CI and downstream rendering (Story/Focus). Treat edits as production changes.
