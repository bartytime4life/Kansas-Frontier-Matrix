# docs/reports 🧾 — Governed Reports & Story Nodes

![Governed](https://img.shields.io/badge/governed-yes-blue)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-success)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-required-informational)

This folder contains **governed, human-readable reports** that ship with the Kansas Frontier Matrix (KFM) repository—especially **Story Nodes** (curated narrative units that are machine-ingestible and provenance-linked).

> [!IMPORTANT]
> **Trust membrane rule (documentation edition):**
> reports here must reference **stable IDs and governed evidence** (catalog entries, documents, provenance records) — not direct database state, ad-hoc screenshots without provenance, or private/unreviewed materials.

---

## What belongs in `docs/reports/`

Use `docs/reports/` for **readable artifacts meant to be rendered and reviewed**:

- ✅ **Story Nodes** (governed narrative content)
- ✅ Narrative bundles that are *reviewable* and *traceable* (with citations + provenance links)
- ✅ Human-facing “explainers” that point to *cataloged evidence artifacts* (STAC/DCAT/PROV + documents)

### What does *not* belong here

- ❌ Pipeline run outputs (put these under `data/work/`, `receipts/`, `data/prov/`, etc.)
- ❌ Large raw datasets / binaries (use governed data paths + catalogs)
- ❌ Anything that bypasses governance (uncited claims, sensitive coordinates, private info)

---

## Directory layout

~~~text
docs/reports/
├── README.md
└── story_nodes/
    ├── templates/
    │   └── (optional local helper templates for story packages; canonical template lives in docs/templates/)
    ├── draft/
    │   └── <story_slug>/
    │       ├── story.md
    │       └── assets/
    └── published/
        └── <story_slug>/
            ├── story.md
            └── assets/
~~~

### Folder meanings

| Folder | Purpose | Editing rules |
|---|---|---|
| `story_nodes/templates/` | Optional “starter kits” for this subtree | Should not diverge from canonical templates without governance review |
| `story_nodes/draft/` | Work-in-progress stories | Editable; must still follow template + cite evidence |
| `story_nodes/published/` | Reviewed stories ready for UI consumption | **Edit via PR only**; changes should trigger validation + review |

---

## Story Nodes

Story Nodes are the core “report” artifact under `docs/reports/`. They are designed to be:

- **Machine-ingestible** (structured format; consistent sections)
- **Evidence-linked** (every factual claim traceable)
- **Governed** (review gates + sensitivity handling)

### Create a new Story Node (author workflow)

1. Choose a stable story slug:
   - recommended: `kebab-case`
   - keep it short and specific (e.g., `bleeding-kansas-overview`, `santa-fe-trail-trade`, `drought-1930s-dust-bowl`)

2. Create the folder structure:

~~~bash
mkdir -p docs/reports/story_nodes/draft/<story_slug>/assets
~~~

3. Copy the canonical template into place:

~~~bash
cp docs/templates/TEMPLATE__STORY_NODE_V3.md \
  docs/reports/story_nodes/draft/<story_slug>/story.md
~~~

4. Author the story:
   - Replace placeholders
   - Add citations for **every factual claim**
   - Link datasets using stable IDs (DCAT/STAC/PROV) rather than local-only paths

5. Add assets (optional):
   - Put images/media under `assets/`
   - Prefer small, reviewable files (optimize images; avoid huge binaries)
   - Record attribution and license in the story or adjacent notes (as required by governance)

---

## Publishing workflow

A Story Node is “published” when it has passed:

- automated validation (template completeness + citation checks)
- peer review (accuracy + clarity)
- governance review (when sensitivity/rights triggers apply)

### Recommended publish path (conceptual)

~~~mermaid
flowchart TD
  A[Author in draft/] --> B[Automated validation]
  B -->|pass| C[Peer review]
  B -->|fail| A
  C -->|approve| D{Governance review needed?}
  D -->|yes| E[Governance review]
  D -->|no| F[Publish to published/]
  E -->|approve| F
  E -->|changes requested| A
  F --> G[Update bundle index + checksums + provenance refs (if used)]
~~~

> [!NOTE]
> Some repos implement the “publish step” as a script that:
> - copies `draft/<story_slug>/` → `published/<story_slug>/`
> - writes or updates an index/manifest with checksums and provenance references  
> If your repo has such a script, prefer it over manual moves.

---

## Citation and evidence rules

### Non-negotiables

- **No uncited factual claims.**
- **Every citation must be resolvable to evidence** (dataset/doc/provenance/graph reference).
- **Sensitive content must be handled fail-closed**:
  - generalize or redact location details when needed
  - trigger governance review when required

### Practical guidance

- Prefer citing:
  - dataset catalog entries (DCAT)
  - geospatial assets (STAC collections/items)
  - provenance bundles (PROV)
  - source documents (doc references) with stable locators (page/span)
  - graph entities (graph references)

> [!TIP]
> If you can’t cite it, either:
> - rewrite it as a question/uncertainty, **or**
> - move it to a “hypotheses” section clearly labeled as non-assertive, **or**
> - do not include it until evidence is ingested/citable.

---

## Sensitivity and CARE handling

Some historical/geospatial content can be harmful if over-specific (e.g., culturally restricted knowledge, sensitive sites, private individuals).

**If in doubt:**
- redact precise coordinates
- aggregate to a safer spatial resolution
- label the story as requiring review
- ensure public/published artifacts cannot leak restricted detail

> [!WARNING]
> Do not “smuggle” sensitive details into images, captions, or embedded metadata.

---

## Definition of Done ✅

Use this checklist before requesting review or publishing:

- [ ] Story Node uses the **v3 template** (`docs/templates/TEMPLATE__STORY_NODE_V3.md`)
- [ ] All required sections are present and complete
- [ ] Every factual claim has a citation
- [ ] Citations are resolvable to governed evidence (DCAT/STAC/PROV/doc/graph refs)
- [ ] Rights/license/attribution are recorded for any included media/assets
- [ ] Sensitivity/CARE labeling is present (and governance review requested if triggered)
- [ ] Links are valid; no broken internal references
- [ ] Local validation (if available) passes; CI should pass the same checks
- [ ] Peer review completed (accuracy + clarity)

---

## Adding new report categories

If you need additional report types beyond Story Nodes:

1. Create a new subfolder under `docs/reports/<report_kind>/`
2. Add a **README.md** inside that folder documenting:
   - purpose
   - required template
   - validation gates
   - provenance/citation expectations
   - how it’s used by API/UI

3. If the report kind becomes UI-consumed, add:
   - a schema under `schemas/`
   - a validator in CI
   - a stable resolver path (so citations remain clickable)

---

## Quick links

- Story Node template (canonical): `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Review gates: `docs/governance/REVIEW_GATES.md`
- Ethics / CARE: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
