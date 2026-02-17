# 🧭 KFM Story Tools (`tools/story/`)

![Governed](https://img.shields.io/badge/Governed-yes-2b6cb0)
![Evidence-first](https://img.shields.io/badge/Evidence--first-required-0f766e)
![Contract-first](https://img.shields.io/badge/Contract--first-required-7c3aed)
![Trust membrane](https://img.shields.io/badge/Trust%20membrane-non--negotiable-111827)

This folder contains **developer tools** for KFM’s **Story Nodes / Story Mode** workflow—authoring support, validation, packaging, and CI-friendly gates that keep narrative artifacts **machine-ingestible, provenance-linked, and safe to publish**.

> ✅ Goal: make it easy to build story content that is **auditable**, **policy-governed**, and **UI-ready** (map + timeline + citations drawer), without bypassing KFM governance.

---

## 📌 What belongs here

`tools/story` is for *tooling* (CLI scripts, validators, transformers, packagers) that help authors and CI systems:

- **Validate Story Nodes** (structure, front matter, citations, entity references, sensitivity flags).
- **Transform or migrate Story Nodes** between template versions (e.g., legacy → v3).
- **Package story artifacts** for offline/field playback (packaging format is TBD) *(not confirmed in repo)*.
- **Generate or verify manifests** that tie narrative scenes to evidence bundles (STAC/DCAT/PROV + graph IDs).
- **Run “governance lint” checks** locally the same way CI does (fail closed).

**Not** in scope for this folder:
- Runtime Story Mode services
- Direct database access
- UI components
- “Freeform” narrative generation without evidence linkage

---

## 🧱 Non‑negotiable invariants

These are the guardrails that every tool in this folder must preserve:

### 1) Evidence-first (no black boxes)
- Story Nodes are governed narrative artifacts: **every factual claim must trace to evidence** (catalog entry or cataloged external source).
- Tools should **refuse** (fail) rather than “guess” if evidence references are missing.

### 2) Contract-first (schemas/specs are first-class)
- Treat **schemas and contracts** as the starting point for implementation.
- Tools must validate against the canonical templates/schemas (see links below).

### 3) Trust membrane (no DB from tools)
- Tools **must not** connect directly to PostGIS/Neo4j/etc.  
  Use governed APIs or pre-exported snapshots/fixtures only. *(If a tool truly needs data, it should consume a versioned export produced by the pipeline.)*

### 4) Governance & CARE/FAIR safety
- Tools must detect/flag sensitive content (precise locations, living persons, culturally restricted info) and route to governance review rather than silently passing.

---

## 🔗 Canonical references (don’t re-invent)

These are the repo-level “sources of truth” this folder should rely on:

- **Story Node template (v3):** `../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- **API contract extension template:** `../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- **KFM catalog profiles:**  
  - `../../docs/standards/KFM_STAC_PROFILE.md`  
  - `../../docs/standards/KFM_DCAT_PROFILE.md`  
  - `../../docs/standards/KFM_PROV_PROFILE.md`
- **Repo structure + doc workflow:** `../../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(if present)*

> If these paths differ in your repo, update this README to match the canonical locations. *(not confirmed in repo)*

---

## 🧠 Story Nodes & Focus Mode: mental model

Story Nodes are KFM’s method for turning narrative into **governed data**: Markdown + semantic annotations + citations + stable IDs.

```mermaid
flowchart LR
  A[Author Story Node (Markdown + front matter)] --> B[Validate schema + links + citations]
  B --> C[Resolve references: graph IDs + STAC/DCAT/PROV IDs]
  C --> D[Package / Publish (versioned)]
  D --> E[Consume in UI: map + timeline + citation drawer]
  E --> F[Focus Mode Q&A: cite or abstain + audit log]
```

---

## ✅ What “valid” Story Node content means (tooling must enforce)

A **valid Story Node** must:

- Include **provenance for every claim** (footnotes or inline citations that resolve to catalog entries).  
- Reference **graph entities** using stable IDs for people/places/events/documents.  
- Clearly distinguish **fact vs interpretation** (especially for AI-assisted text).  

Tools in this folder should treat these as *hard validation rules*, not “best effort.”

---

## 🧪 Toolchain entrypoints (expected)

> These command names are illustrative *(not confirmed in repo)*.  
> Pick one CLI surface and keep it stable (CI depends on it).

### Common operations
- `kfm-story validate <path>`  
  Validate Story Node(s): structure, front matter, citations, entity refs, sensitivity flags.

- `kfm-story migrate --from v2 --to v3 <path>`  
  Transform legacy Story Nodes to `TEMPLATE__STORY_NODE_V3.md`.

- `kfm-story bundle <story_slug>`  
  Create/verify an evidence bundle manifest (STAC/DCAT/PROV IDs + graph IDs).

- `kfm-story pack <story_slug>`  
  Build an offline package (story markdown + assets + manifests) *(pack format TBD; not confirmed in repo)*.

### Example (illustrative)
```bash
# Validate a single Story Node
kfm-story validate ../../docs/reports/story_nodes/draft/my_story/story.md

# Validate everything under published/
kfm-story validate ../../docs/reports/story_nodes/published/

# Migrate legacy → v3
kfm-story migrate --from v2 --to v3 ../../docs/reports/story_nodes/draft/
```

---

## 📦 Inputs & outputs

| Artifact | Input/Output | What it is | Must be true |
|---|---:|---|---|
| Story Node Markdown | Input | Narrative + front matter + citations | Every factual claim is cited; graph IDs present |
| Evidence bundle refs | Input | STAC/DCAT/PROV IDs + graph IDs | IDs resolve; versions pinned |
| Validation report | Output | Machine-readable validation results | CI can fail on errors (non-zero exit) |
| Packaged story bundle | Output | Offline/portable story package | Contains only approved assets + manifests |

---

## 🗂️ Directory layout (recommended)

This folder may evolve, but keep it **boring and predictable**:

```text
tools/story/
  README.md                      # you are here
  bin/                           # CLI entrypoints (if using a single CLI)
  src/                           # implementation
  fixtures/                      # test fixtures: known-good + known-bad Story Nodes
  rules/                         # policy packs / lint rules (e.g., Rego) (optional)
  reports/                       # local tool outputs (gitignored) (optional)
```

> If your repo already has a different structure, align to the repo standard and update this map. *(not confirmed in repo)*

---

## 🧰 How to add a new tool (contributor checklist)

When adding or changing tooling under `tools/story/`:

- [ ] Define the **contract first** (schema / expected outputs / CLI interface)
- [ ] Add fixtures:
  - [ ] `fixtures/valid/` examples that pass
  - [ ] `fixtures/invalid/` examples that fail for the right reason
- [ ] Add tests that run in CI (unit + contract-style)
- [ ] Ensure fail-closed behavior:
  - [ ] missing citation → fail
  - [ ] unresolved ID → fail
  - [ ] sensitive marker without required fields → fail *(policy-defined)*
- [ ] Document usage in this README
- [ ] Add/extend CI wiring (if needed) under `.github/workflows/`

---

## 🛡️ Governance & sensitivity triggers

Tools must surface (not bury) risk:

- **Sensitive locations**: prefer generalized geometry / bounding boxes when policy requires.
- **Living persons / PII**: redact or coarsen; require explicit authorization to publish.
- **Culturally restricted knowledge**: must route to governance review before publishing.

If policy is uncertain: **fail closed**.

---

## 🔌 CI/CD expectations (minimum)

Your CI workflow should include checks that call tools from this folder to:

- validate Story Nodes + governed Markdown structure
- validate STAC/DCAT/PROV artifacts for new datasets
- run policy tests (OPA/Rego)  
- (optional but recommended) create SBOM + build provenance attestations

---

## 📎 Related docs (starting points)

- Story Node template: `../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Master guide: `../../docs/MASTER_GUIDE_v13.md` *(if present)*
- Governance: `../../docs/governance/ROOT_GOVERNANCE.md` *(if present)*
- Story Mode architecture notes: see `docs/` and `schemas/storynodes/`

---

## 🧭 “Definition of Done” for this folder

This folder is “ready” when:

- [ ] A single **stable CLI** exists (or clearly documented equivalents)
- [ ] `validate` is deterministic and CI-safe
- [ ] Fixtures cover common pass/fail cases
- [ ] Migration path to Story Node v3 is automated (legacy → v3) *(if legacy exists; not confirmed in repo)*
- [ ] Tool outputs are machine-readable (JSON) + human-readable summaries
- [ ] All tooling respects the trust membrane and governance rules