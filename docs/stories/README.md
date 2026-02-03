# 🧭 KFM Stories — Story Nodes & Interactive Narratives

![KFM](https://img.shields.io/badge/KFM-Story%20Nodes-2ea44f)
![Provenance](https://img.shields.io/badge/Provenance-Required-blue)
![Governance](https://img.shields.io/badge/Governance-FAIR%2BCARE-purple)
![Format](https://img.shields.io/badge/Format-Markdown%20%2B%20JSON-orange)
![UX](https://img.shields.io/badge/Experience-Map%20%2B%20Timeline%20%2B%20Reader-informational)

Welcome to `docs/stories/` 🗺️📚  
This directory contains **KFM Story Packages** — **versioned**, **evidence-first** narratives that can be read as plain Markdown **and** played as an interactive “map + timeline + reader” experience (Focus Mode / Story Player).

> **Core principle:** “the map behind the map” ✅  
> Stories are **not** freeform blog posts. Every factual claim must be traceable to evidence (cataloged datasets, documents, archives, or other governed sources).

---

## 📌 What lives here?

A story is typically **two parts**:

1. **`story.md`** 📝  
   The narrative (human-readable, reviewable, diffable).
2. **`story.json`** 🎛️  
   The “director track” that binds sections of the narrative to UI states:
   - map camera movements 🗺️
   - timeline highlights 🕰️
   - layer toggles 🧩
   - annotations/markers 📍
   - optional media cues 🖼️🔊

Optional extras:
- `media/` folder for images/audio/video
- `refs/` folder for citation exports, transcripts, or supporting files (when licensing allows)

---

## 🗂️ Recommended directory conventions

### ✅ Preferred: **folder-per-story** (clean + scalable)

```text
docs/stories/
├── README.md
├── index.json                # optional (curated list + ordering)
├── media/                    # optional (shared assets; use sparingly)
└── dust-bowl/
    ├── story.md              # required
    ├── story.json            # required
    ├── media/                # optional
    │   ├── black-sunday.jpg
    │   └── crop-dust.webp
    └── refs/                 # optional (if permitted)
        └── bibliography.bib
```

### ⚠️ Alternate: “flat files” (OK for small prototypes)

```text
docs/stories/
├── dust-bowl.md
├── dust-bowl.json
└── media/
    └── ...
```

**Rule of thumb:** if the story has **any assets**, use folder-per-story. 🧰

---

## 🧱 Story Node requirements (Markdown)

### 1) YAML front matter ✅ (required)

At the top of `story.md`, include **governance + discovery metadata**:

```yaml
---
id: dust-bowl
title: "Dust Bowl in Kansas"
status: draft            # draft | review | published | archived
version: 0.1.0
authors:
  - name: "Your Name"
    role: "researcher"
created: "2026-02-03"
updated: "2026-02-03"

summary: "An evidence-backed narrative linking drought, land practices, and migration with interactive map states."
tags: ["climate", "agriculture", "migration", "1930s"]

# Spatial/temporal bounds (helps search + UI defaults)
time_range:
  start: "1930-01-01"
  end: "1941-12-31"
bbox: [-102.05, 36.99, -94.59, 40.00]   # [minLon, minLat, maxLon, maxLat]

# Governance / sensitivity
care_label: public       # public | sensitive | restricted
sensitivity_notes: "No precise coordinates for culturally sensitive sites."

# Evidence anchors (high-level)
datasets:
  - "kfm:dataset:ks_drought_severity_1930s"
  - "kfm:dataset:us_census_county_1930_1940"
sources:
  - "kfm:doc:chronicling-america:xxxx"
  - "kfm:archive:kansas-memory:yyyy"

# Knowledge graph linkage (stable IDs, if available)
entities:
  - "kfm:place:western-kansas"
  - "kfm:event:black-sunday-1935"
---
```

### 2) Structure that plays well in Focus Mode 🧠

A strong default layout:

- **Context** (what/where/when)
- **Evidence** (what sources show)
- **Interpretation** (your analysis; clearly labeled)
- **Uncertainty / Open questions** (what is not confirmed yet)
- **References** (full citations)

Example skeleton:

```md
## Context
...

## Evidence
...

## Interpretation (Author Analysis)
...

## Open Questions / Not Confirmed
> [not confirmed in repo] This paragraph needs a primary source.

## References
- [^1]: ...
```

---

## 🔎 Citations & evidence rules (non‑negotiable)

### ✅ Every factual claim must be backed
Use one of these styles consistently:

**Option A: Markdown footnotes (recommended)**  
```md
Black Sunday occurred on April 14, 1935.[^black-sunday-date]

[^black-sunday-date]: KFM catalog entry: kfm:doc:... (plus original archive link if allowed)
```

**Option B: Numbered references**
```md
The drought severity peaked in 1934–1936.[1]

[1] KFM dataset: kfm:dataset:...
```

### 🧭 Evidence should be *catalog-addressable*
Prefer citing:
- `kfm:dataset:*` (DCAT/STAC-backed datasets)
- `kfm:doc:*` (documents indexed with provenance)
- `kfm:place:*`, `kfm:event:*` (graph entities)
- stable public archive identifiers (only if policy allows)

> If it’s not in catalogs/graph **with provenance**, it shouldn’t appear as a “fact” in a published story. 🛑

### 🧠 Fact vs interpretation must be explicit
If you infer something, label it:

- **Fact** ✅ (source-backed)
- **Interpretation** 🧩 (your analysis)
- **Hypothesis** 🧪 (testable claim not yet proven)
- **Unknown** ❓ (open question)

---

## 🎛️ Story JSON (binding narrative → map/timeline)

`story.json` is the “director track” that tells the UI what to do at each section.

### 🧩 Key idea: sections are the join key
Your JSON should reference **stable section anchors** from the Markdown.

✅ Recommended: add explicit anchors in Markdown:

```md
## Black Sunday (April 14, 1935)
<a id="black-sunday-1935"></a>
...
```

### Minimal JSON example

```json
{
  "id": "dust-bowl",
  "title": "Dust Bowl in Kansas",
  "version": "0.1.0",
  "steps": [
    {
      "anchor": "context",
      "ui": {
        "timeline": { "year": 1933 },
        "map": { "center": [-100.5, 38.5], "zoom": 5.8 },
        "layers": [
          { "id": "base_counties", "visible": true },
          { "id": "drought_severity", "visible": true, "time": "1933-06-01" }
        ]
      }
    },
    {
      "anchor": "black-sunday-1935",
      "ui": {
        "timeline": { "date": "1935-04-14" },
        "map": { "center": [-101.2, 38.0], "zoom": 6.2, "pitch": 25 },
        "annotations": [
          { "type": "marker", "lon": -101.2, "lat": 38.0, "label": "Black Sunday" }
        ],
        "layers": [
          { "id": "dust_storm_reports", "visible": true, "time": "1935-04-01" }
        ],
        "media": [
          { "type": "image", "src": "media/black-sunday.jpg", "caption": "Archive photo (see story citations)." }
        ]
      }
    }
  ]
}
```

### 🧠 Design notes (for the UI contract)
- `steps[].anchor` should match a Markdown anchor (stable over time).
- `layers[].id` should reference a known layer registry ID (or a dataset-backed layer mapping).
- Use **time-aware layer toggles** where possible (the story is a time machine 🕰️✨).

---

## ➕ Adding a new story (contributor workflow)

1. 🍴 Fork the repo (or create a feature branch).
2. 📁 Create a folder: `docs/stories/<story-slug>/`
3. 📝 Add `story.md` using the Story Node template.
4. 🎛️ Add `story.json` with at least:
   - `id`, `title`, `version`
   - a `steps[]` list
5. 🖼️ Add media (if needed) and ensure:
   - you have rights to include it
   - you include attribution in the narrative and/or metadata
6. 🧪 Self-review with the checklist below.
7. 🔁 Open a PR for maintainers + subject-matter review.

---

## ✅ Definition of Done (Story Node PR checklist)

### Governance & provenance 🛡️
- [ ] YAML front matter is complete (id/title/status/version/authors/dates)
- [ ] `care_label` is set correctly (and notes explain any sensitivity)
- [ ] No restricted/sensitive coordinates are exposed (if applicable)
- [ ] Every factual claim has a citation
- [ ] Sources are catalog-addressable (preferred) or clearly attributable

### Narrative quality ✍️
- [ ] Clear separation of **Evidence** vs **Interpretation**
- [ ] No speculative language presented as fact
- [ ] Dates/places are explicit and consistent
- [ ] The story can be read meaningfully **without** the map (graceful degradation)

### Interactive UX 🎚️
- [ ] `story.json` anchors match the Markdown
- [ ] Steps progress logically (no whiplash zooms 😵‍💫)
- [ ] Layers referenced exist (or are clearly TODO with issue link)
- [ ] Media loads and is optimized for web delivery

### Accessibility ♿
- [ ] Images have alt text (and captions when useful)
- [ ] Headings are hierarchical (no skipped levels)
- [ ] Avoid “color-only” meaning; describe patterns in text too

---

## 🖼️ Media guidelines

- Prefer **web-friendly formats**:
  - photos: `.webp` (or optimized `.jpg`)
  - diagrams: `.svg` or `.png`
- Keep files small:
  - aim for < 500KB per image unless there’s a compelling reason
- Always include attribution:
  - in caption, references, or front matter `sources`

---

## 🧩 Notes on “published” vs “draft” stories

- `status: draft` → safe to iterate; still must cite claims if shared.
- `status: review` → maintainers/SMEs verify accuracy + governance.
- `status: published` → eligible for UI listing + Focus Mode consumption.
- `status: archived` → kept for provenance/history; not surfaced by default.

> Optional pattern: `index.json` can be used to control ordering and visibility (curated list). 🗂️

---

## 🔗 Related docs (in-repo)

- `docs/templates/TEMPLATE__STORY_NODE_V3.md` 🧾  
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` 📘  
- `docs/governance/` ⚖️  
- `docs/standards/` 📏  

---

## 🧯 Troubleshooting

**My story renders in GitHub but not in the app**
- Check anchors: does `story.json.steps[].anchor` match the Markdown anchor exactly?
- Check unsupported Markdown features: avoid renderer-specific extensions unless the UI supports them.

**A claim is hard to cite**
- Move it to **Interpretation** or **Open Questions** until a primary source is cataloged.
- Use the `[not confirmed in repo]` marker to flag it for review.

**A story includes sensitive cultural information**
- Set `care_label: sensitive` or `restricted`
- Remove/blur precise spatial details
- Add `sensitivity_notes` explaining handling expectations

---

## 🧾 License & attribution

Stories are governed content. Ensure:
- citations are complete
- embedded media is legally includable
- attribution is present and unambiguous ✅

Happy storytelling — let’s keep it evidence-first. 🧭🗺️✨