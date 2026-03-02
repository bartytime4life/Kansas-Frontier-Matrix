<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/2a0c2a76-1d6c-4d21-8ddf-2d0f2b1fe5fd
title: UI Diagram Exports (Generated)
type: standard
version: v1
status: draft
owners: KFM maintainers
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/diagrams/out/ui/
tags: [kfm, diagrams, ui, generated]
notes:
  - This directory is intended for generated diagram exports used in UI documentation and reviews.
  - Do not hand-edit generated exports; update the diagram sources and re-export.
[/KFM_META_BLOCK_V2] -->

# UI Diagram Exports (Generated)

Generated **SVG/PNG/PDF** exports for **KFM UI** diagrams (Map Explorer, Story Nodes, Focus Mode), meant to be embedded in docs, ADRs, and review threads.

![status](https://img.shields.io/badge/status-draft-yellow)
![artifact](https://img.shields.io/badge/artifact-generated-blue)
![scope](https://img.shields.io/badge/scope-ui-informational)
![policy](https://img.shields.io/badge/policy-public-success)

> **IMPORTANT:** This folder is for **outputs**. If you need to change a diagram, update the **source** (wherever your repo keeps diagram sources) and regenerate the export(s).

---

## Quick links

- [What this directory is](#what-this-directory-is)
- [Directory contract](#directory-contract)
- [Expected structure](#expected-structure)
- [Naming convention](#naming-convention)
- [UI invariants the diagrams must reflect](#ui-invariants-the-diagrams-must-reflect)
- [How to add or update a diagram](#how-to-add-or-update-a-diagram)
- [Diagram registry](#diagram-registry)
- [Governance and safety](#governance-and-safety)
- [Troubleshooting](#troubleshooting)

---

## What this directory is

This directory is the **published, embeddable diagram output** surface for UI documentation:

- use in markdown docs via relative links like:
  - `![alt text](./map-explorer__evidence-drawer__flow.svg)`
- use in PRs / code reviews as stable artifacts
- keep diagrams consistent across Map Explorer, Story Node v3, and Focus Mode UX docs

If your repo distinguishes **diagram sources** vs **exports**, this folder is the “exports” side.

---

## Directory contract

### ✅ Acceptable inputs (what belongs here)

Generated, embeddable artifacts such as:

- `*.svg` (preferred)
- `*.png` (only when SVG is impractical)
- `*.pdf` (only when needed for printing / external sharing)
- `*.txt` (rare: export logs or manifest summaries, if your tooling emits them)

### ❌ Exclusions (what must not go here)

- diagram **sources** (e.g., Mermaid source, Draw.io source, Figma exports-as-source)
- screenshots with unreadable text
- anything containing secrets (tokens, credentials, internal URLs with credentials)
- diagrams that leak restricted/sensitive locations or operational details

> If a diagram meaningfully changes data-access boundaries or policy behavior, treat it like a governed change: update the appropriate architecture/governance doc and/or ADR, not just the image.

---

## Expected structure

This is a **recommended** layout pattern (adapt to your repo if different):

```text
docs/diagrams/
├── out/
│   ├── ui/
│   │   ├── README.md                 # you are here
│   │   ├── map-explorer__*.svg
│   │   ├── story-node__*.svg
│   │   └── focus-mode__*.svg
│   └── ...
└── (sources live elsewhere in your repo)
```

**Rule of thumb:** outputs here should be **safe to link** from any doc that needs UI diagrams.

---

## Naming convention

Use names that are stable, greppable, and sortable.

**Recommended pattern:**

`<surface>__<topic>__<diagram-kind>__vYYYYMMDD.<ext>`

Examples:

- `map-explorer__evidence-drawer__flow__v20260301.svg`
- `story-node__publish-gate__sequence__v20260301.svg`
- `focus-mode__cite-or-abstain__state__v20260301.svg`

### Surface prefixes

| Prefix         | Meaning |
|---------------|---------|
| `map-explorer`| Map Explorer UI surface |
| `story-node`  | Story Node v3 rendering/publishing UI |
| `focus-mode`  | Focus Mode UI + response flow |

---

## UI invariants the diagrams must reflect

Diagrams in this folder should be consistent with KFM’s non-negotiable UX/architecture posture:

- **Trust membrane:** UI clients do **not** fetch directly from databases or object storage; access goes through the governed API boundary.
- **Evidence-first UX:** user interactions must be explainable with resolvable evidence (e.g., Evidence Drawer patterns).
- **Cite-or-abstain posture (Focus Mode):** if evidence can’t support a claim, the system abstains.

### Reference diagram: UI trust membrane + evidence resolution

```mermaid
flowchart LR
  U[User] --> UI[Web UI: Map Explorer / Story / Focus]
  UI -->|HTTPS| API[Governed API Boundary (PEP)]
  API --> POL[Policy Engine]
  API --> CAT[Catalog Triplet: DCAT + STAC + PROV]
  API --> EVD[Evidence Resolver]
  EVD --> ART[Artifact Stores (RAW/WORK/PROCESSED)]
  API -->|policy-filtered response| UI

  %% Non-goal: direct client-to-storage access
  UI -. "NO: direct DB/object store access" .-> ART
```

---

## How to add or update a diagram

### 1) Update the diagram source (do not edit exports)

Because this folder is “`out/`”, edits should happen in your **diagram source location** (repo-specific).

**Minimum verification steps to find the source-of-truth:**

```bash
# Find references to the diagram build pipeline
git grep -n "diagram" .
git grep -n "mermaid" .
git grep -n "drawio" .
git grep -n "plantuml" .

# Find tasks/scripts that emit into docs/diagrams/out
git grep -n "docs/diagrams/out" .
```

### 2) Regenerate the export(s)

Run your repo’s diagram/export build step (repo-specific).

> TODO: Wire this README to the *actual* script/command once confirmed in-repo.

### 3) Sanity-check before committing

- [ ] SVG text is legible at typical doc widths
- [ ] File size is reasonable (avoid multi‑MB exports unless necessary)
- [ ] Names follow the naming convention
- [ ] Diagram matches trust-membrane posture (no direct UI → storage)
- [ ] No restricted details are present

---

## Diagram registry

Keep a lightweight index so reviewers can quickly find the right artifact.

| Diagram | Surface | Purpose | Output file(s) | Owner | Status |
|--------|---------|---------|----------------|-------|--------|
| Evidence Drawer flow | map-explorer | Explain click → evidence resolution | `map-explorer__evidence-drawer__flow__vYYYYMMDD.svg` | TODO | draft |
| Story publish gate | story-node | Explain “citations must resolve” gate | `story-node__publish-gate__sequence__vYYYYMMDD.svg` | TODO | draft |
| Focus cite-or-abstain | focus-mode | Explain evidence-required responses | `focus-mode__cite-or-abstain__state__vYYYYMMDD.svg` | TODO | draft |

> TIP: If you find yourself duplicating UI diagrams in multiple docs, prefer adding the diagram here once, then linking it everywhere.

---

## Governance and safety

These exports are documentation artifacts, but they still have **governance impact**:

- If a diagram implies a **policy bypass** (client-to-storage access), it’s wrong by definition.
- If a diagram includes sensitive locations, internal-only endpoints, or restricted operational details:
  - move it to an appropriate restricted location (repo policy-dependent),
  - or generalize/redact it before exporting.

---

## Troubleshooting

### Diagram renders but looks “off” in GitHub

- Prefer **SVG** exports.
- Avoid tiny font sizes.
- Avoid excessively wide canvases; break one giant diagram into 2–3 smaller diagrams.

### “Where do the sources live?”

Search the repo for the generator pipeline:

```bash
git grep -n "docs/diagrams/out/ui" .
git grep -n "out/ui" .
```

---

_Back to top:_ [Quick links](#quick-links)
