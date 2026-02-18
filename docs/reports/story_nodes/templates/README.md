# Story Node Templates (KFM)

This folder contains **authoring templates** for KFM Story Nodes: governed, evidence-first narrative artifacts that can be parsed, indexed, cited, and replayed in Map UI / Story Mode / Focus Mode.

> **Goal:** a Story Node should be readable by humans *and* reliably usable by software (indexing, search, entity linking, map-state playback, provenance display).

---

## What belongs in this folder

- Templates (Markdown) used to author new Story Nodes and related artifacts.
- Small helper snippets (YAML/JSON examples) for citations, entity references, and map-state “keyframes”.
- Checklists for review and publishing.

**What does *not* belong here:** completed Story Nodes. Put finished nodes in the Story Nodes library (typically `docs/reports/story_nodes/...`) and keep this directory limited to reusable templates.

---

## Suggested folder layout (template-only)

```text
docs/
└─ reports/
   └─ story_nodes/
      ├─ templates/
      │  ├─ README.md  ← you are here
      │  ├─ story_node_v3.template.md
      │  ├─ story_node_minimal.template.md
      │  ├─ scene_keyframe.template.yaml
      │  ├─ citation_record.template.yaml
      │  └─ review_checklist.template.md
      └─ (published Story Nodes live elsewhere)
```

> If your repo already uses different filenames, keep them — just update the **Template Index** below so authors can find the right starting point.

---

## Template index

| Template file | Use when… | Output artifact type |
|---|---|---|
| `story_node_v3.template.md` | You’re creating a Story Node intended for Story Mode playback (chapters/scenes, map states, tasks). | Story Node (full) |
| `story_node_minimal.template.md` | You need a fast, narrative-only note, but still governed (citations + provenance). | Story Node (minimal) |
| `scene_keyframe.template.yaml` | You want a reusable “map state” snippet: bbox, time window, layers, camera. | Scene / keyframe |
| `citation_record.template.yaml` | You’re adding a new citation record tied to a dataset/asset and want a consistent shape. | Citation record |
| `review_checklist.template.md` | You’re reviewing a Story Node for publication (governance + UX). | QA checklist |

---

## Authoring workflow (happy path)

1. **Pick the right template** from the table above.
2. **Copy it** into the Story Nodes library (example: `docs/reports/story_nodes/2026/<slug>.md`).
3. Fill in:
   - required metadata
   - narrative
   - citations
   - entity references
   - map/timeline states (if applicable)
4. **Run validation** (if your repo has CI checks), or do the manual checklist in `review_checklist.template.md`.
5. **Publish** by merging via PR so CI can fail-closed on broken structure.

---

## Story Node contract (the non-negotiables)

A Story Node is valid for KFM when it satisfies all of the following:

### 1) Evidence-first claims

- Any **factual** statement that is not common knowledge must have a citation.
- Quotes must have citations (and ideally a stable page/section pointer).
- If a claim cannot be supported, label it clearly as **(not confirmed)**.

### 2) Entity linking (for the knowledge graph)

- Important *people / places / events / sources / datasets* should reference stable IDs.
- IDs must be stable across edits (avoid “incremental numbers” that drift).

### 3) Fact vs. interpretation

- Separate **observations** (what sources say) from **interpretation** (analysis, inference, hypothesis).
- If AI assistance was used for synthesis, make that explicit in metadata and keep citations intact.

### 4) Map + time replay (when used in Story Mode)

If the Story Node is intended for Story Mode playback, it must define:

- a time window for each scene
- a spatial window (bbox or named region)
- the layers/overlays used
- citations associated with each scene (not just at the end)

### 5) Sensitivity handling (CARE + safety)

- Treat precise coordinates as sensitive when dealing with:
  - archaeology, culturally restricted knowledge, endangered species, private individuals, etc.
- Prefer **generalized geometry** (coarser bbox, grid cell, county) when sensitivity is non-trivial.
- Record any redaction/generalization decision in the node metadata (and ideally in provenance).

---

## Recommended metadata (YAML front matter)

> This is a *recommended* baseline. If your repo already has a canonical Story Node schema, follow that instead and update the template.

```yaml
---
kfm:
  artifact_type: story_node
  template_version: v3
  status: draft # draft|review|published|deprecated
  title: "Example: Railroads and Town Growth (1870–1910)"
  summary: "How rail expansion reshaped settlement patterns in central Kansas."
  authors:
    - name: "Your Name"
      role: "author" # author|reviewer|curator
  created: "2026-02-18"
  updated: "2026-02-18"
  time_range:
    start: "1870-01-01"
    end: "1910-12-31"
  region:
    type: bbox
    bbox: [-102.05, 36.99, -94.59, 40.00] # KS-ish
  sensitivity:
    classification: public # public|internal|restricted|embargoed
    notes: "If restricted, remove precise coordinates and explain why."
  evidence:
    required: true
    citations_required: true
  links:
    datasets: []
    assets: []
    entities: []
---
```

---

## Citation guidance (practical)

**Preferred pattern:** cite each claim *close to where it appears*, then maintain a references section with stable keys.

Example inline markers:

- `...[CIT-001]`
- `...[CIT-railroad-map-1878]`

Example reference section:

```md
## References

- **[CIT-railroad-map-1878]** Title, creator, year. Dataset: `kfm.dataset.<id>`; Asset: `stac.item.<id>`; Notes: page/plate 3.
- **[CIT-census-1900]** U.S. Census, 1900. Dataset: `kfm.dataset.<id>`.
```

> Keep citation IDs stable. Changing a citation ID is a breaking change for any indexer, UI deep-link, or audit reference.

---

## Review checklist (minimum)

Before a Story Node can be labeled `published`:

- [ ] Title, summary, status, dates filled in
- [ ] Time range present and sane (start ≤ end; no mixed calendars)
- [ ] Region present (bbox or named region) and matches narrative
- [ ] Every non-trivial claim has a citation (or is marked **(not confirmed)**)
- [ ] Interpretations are clearly labeled as analysis (not presented as fact)
- [ ] Sensitive locations are generalized/redacted (if applicable)
- [ ] Entity references included for primary actors/places/events
- [ ] References section contains complete citation records
- [ ] Spellcheck + linkcheck (if your repo enforces them)
- [ ] PR reviewer sign-off recorded (who/when)

---

## Appendix: “Hello world” Story Node stub

```md
---
kfm:
  artifact_type: story_node
  template_version: v3
  status: draft
  title: "Hello Story Node"
  created: "2026-02-18"
  updated: "2026-02-18"
  time_range: { start: "1900-01-01", end: "1900-12-31" }
  region: { type: bbox, bbox: [-98.0, 38.0, -97.0, 39.0] }
  sensitivity: { classification: public }
---

# Hello Story Node

## Claim

This is a cited claim about Kansas. [CIT-001]

## Analysis

This is an interpretation based on the cited claim.

## References

- **[CIT-001]** Source title. Dataset: `kfm.dataset.example`; Notes: "p. 12".
```