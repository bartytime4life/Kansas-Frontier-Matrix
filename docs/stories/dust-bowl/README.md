# 🌪️ Dust Bowl in Kansas (1930s) — Story Node

![KFM](https://img.shields.io/badge/KFM-Story%20Node-2b6cb0) ![Status](https://img.shields.io/badge/Status-Draft-f59e0b) ![Era](https://img.shields.io/badge/Era-1930s-6b7280) ![Region](https://img.shields.io/badge/Region-Western%20Kansas-10b981)

> [!IMPORTANT]
> **Evidence-first story node.** This story is designed for KFM’s citation-gated workflows (🧠 *“No Source, No Answer”*). Every factual claim should be backed by a dataset, document, or archival record — and cited in `story.md`.

---

## 📦 What’s in this folder?

```text
docs/
└─ stories/
   └─ dust-bowl/
      ├─ README.md        👈 you are here
      ├─ story.md         📖 narrative + citations + media callouts
      ├─ story.json       🧩 scroll → map-state bindings (camera/layers/time/annotations)
      └─ media/           🖼️ images/audio/video + attribution files
```

### 🔗 Quick links
- 📖 Narrative: `./story.md`
- 🧩 Scroll bindings: `./story.json`
- 🖼️ Media vault: `./media/`
- 🧰 Template (recommended): `../../templates/TEMPLATE__STORY_NODE_V3.md` *(if present in repo)*

---

## 🎯 Story purpose

This node documents how drought + land conditions + wind erosion combined into **Dust Bowl-era impacts in Kansas**, using:
- 🗺️ **Spatial data** (soils, wind erodibility, drought/climate indicators)
- 🧾 **Archival evidence** (reports, newspapers, photographs)
- 🕰️ **Time-aware storytelling** (section-by-section map states you can scroll)

The goal is to let a reader *see* the relationships — not just read about them.

---

## 🧭 Scope

### 🗺️ Geography
- Primary focus: **Western Kansas** (county-level views, with optional deep-dives to selected counties/towns).
- Secondary context (optional): adjacent High Plains regions for cross-border continuity.

### 🕰️ Timeline
- Core narrative: **1930s**, with interactive “snapshots” on key dates/events (see outline below).
- Optional epilogue: “legacy layers” comparing **then vs now** (modern land cover, erosion risk, conservation footprints).

---

## 🧵 Narrative outline (draft)

> Keep these **section slugs** stable — they should match `story.json.sections[].slug` exactly ✅

1. **`before-the-dust`** 🌾  
   - Set conditions: land use pressure, soil exposure, and vulnerability “primers”.
2. **`drought-arrives-early-1930s`** ☀️  
   - Climate signals + drought severity layers and station-based context.
3. **`black-sunday-1935`** 🌀  
   - Event-centric view (map toggles + timeline jump) with 1935 drought context + dust storm reporting.
4. **`liberal-ks-1936`** 📸  
   - Primary-source spotlight: geolocated photos and local accounts (visual evidence on the map).
5. **`why-here-wind-x-soil`** 🧪  
   - “Mechanism explainer”: overlay **wind erodibility** + **drought** + **soil** to show *why impacts clustered where they did*.
6. **`response-conservation`** 🌲  
   - Soil conservation actions, shelterbelts, and institutional response layers.
7. **`aftermath-migration-1940`** 🚚  
   - Population change / displacement indicators (where available) + documented social impacts.
8. **`legacy-today`** 🧭  
   - Modern echoes: land management, erosion risk, and memory (archives + maps).

---

## 🧩 Story Node contract (how KFM reads this)

### 1) `story.md` (narrative)
- Markdown narrative with **YAML front matter** for machine-ingestible metadata.
- Contains citations and media callouts.
- Uses headings that can be matched by slug/anchor.

**Recommended front matter**
```yaml
---
title: "Dust Bowl in Kansas (1930s)"
slug: "dust-bowl"
status: "draft"   # draft | review | published
era:
  start: "1930-01-01"
  end: "1939-12-31"
region:
  name: "Western Kansas"
  bbox: [-102.5, 36.9, -98.5, 39.0]  # example bbox (lon/lat)
authors:
  - name: "TBD"
    role: "Story author"
sources:
  - "TBD: dataset-id-or-archive-record"
licenses:
  - "TBD"
tags: ["drought", "wind erosion", "Dust Bowl", "Kansas", "1930s"]
---
```

> ✍️ Write like a documentary editor: short scenes, strong captions, and citations close to the claim.

---

### 2) `story.json` (scroll → map bindings)
This file is the **controller**: as the reader scrolls, the map updates.

**Minimal skeleton (draft)**
```json
{
  "id": "dust-bowl",
  "title": "Dust Bowl in Kansas (1930s)",
  "version": 1,
  "sections": [
    {
      "slug": "black-sunday-1935",
      "headline": "Black Sunday (April 14, 1935)",
      "map": {
        "camera": { "center": [-100.9, 37.0], "zoom": 6.2 },
        "time": "1935-04-14",
        "layers_on": ["drought_severity_1935", "wind_erodibility_index", "dust_storm_reports"],
        "annotations": [
          { "type": "note", "text": "Illustrative view — replace with sourced event geometry when available." }
        ]
      }
    }
  ]
}
```

> [!NOTE]
> `story.json` should never “invent” geometry. If an event location is uncertain, use **clearly marked approximations** (and prioritize sourcing event footprints over point guesses).

---

## 🧱 Draft data layers plan

> This table is a planning surface. Replace “TBD” with **real dataset IDs** from the KFM catalog once ingested.

| Layer (proposed id) | What it shows 🗺️ | Candidate sources 📚 | Notes 🧠 | KFM Dataset ID |
|---|---|---|---|---|
| `drought_severity_1930s` | Drought intensity by time slice | NDMC-style analyses + NOAA climate archives | Prefer time-enabled rasters or county stats w/ dates | `TBD` |
| `drought_severity_1935` | Highlight year 1935 | Same as above | Used for the “Black Sunday” scene | `TBD` |
| `wind_erodibility_index` | Susceptibility to wind erosion | Derived from soils (document derivation!) | Key explanatory overlay (wind × soil) | `TBD` |
| `soils_ssurgo` | Soil type / texture / organic matter | USDA SSURGO (or Kansas soil surveys) | Add simplified styling for readability | `TBD` |
| `dust_storm_reports` | Documented dust storm sightings | NOAA archives, SCS reports, newspapers | Store as Events w/ dates + citations | `TBD` |
| `loc_photos_dustbowl` | Geolocated archival photos | Library of Congress / Kansas archives | Each point should include rights + caption | `TBD` |
| `shelterbelt_projects` | Conservation / shelterbelt actions | Kansas institutions / documented projects | Tie to “Response” section | `TBD` |
| `population_change_1930_1940` | Migration / population shifts | Census aggregates (county) | Use careful language + avoid causal leaps | `TBD` |

---

## 🧠 Focus Mode test prompts (for this story)

Use these to validate the node supports grounded Q&A:

- “What evidence supports severe drought impacts in **Finney County** in the mid-1930s, and which sources are cited?”  
- “Show the relationship between **wind erodibility** and **drought severity** in southwest Kansas — what layers back this up?”  
- “Which archival photos are tied to dust conditions near **Liberal, Kansas (1936)**, and what do their captions say?”  
- “What changed by **1940** in the counties most affected — population, land use, or conservation activity — and what datasets support that?”

> ✅ A good Focus Mode answer should return with citations, or refuse if evidence is missing.

---

## 🎨 Cartography & UX guardrails (don’t skip)

### 🧩 Classification & pattern clarity
- Keep choropleth class counts **reader-friendly** (avoid “legend soup”).
- Reclassify and compare multiple schemes during drafting.
- If you can’t justify the classification, simplify.

### 🔤 Typography & labels
- Keep label blocks readable: consistent spacing, avoid cramped “set solid” text, and avoid spacing so large it looks like separate labels.
- Prefer ragged-right blocks for narrative text; avoid hyphenation for map labels.

### 🎬 Storytelling with maps
Cartography isn’t only measurement — it’s narrative. This story should treat maps + captions + photos as a **sequenced documentary** (each scene has a purpose).

---

## 🧪 Definition of Done checklist ✅

- [ ] `story.md` has YAML front matter filled out (title, authors, sources, licenses)
- [ ] Each narrative section has **at least one** map state in `story.json`
- [ ] Every factual claim has a citation (dataset/document ID or archive ref)
- [ ] Each layer referenced in `story.json` exists in the catalog (or is explicitly marked `TBD`)
- [ ] Media in `media/` includes attribution + license notes
- [ ] Maps pass readability checks (legend clarity, label collisions, color contrast)
- [ ] Approximations are marked as approximations (no silent guessing)
- [ ] Governance check: sensitive data is flagged and handled appropriately

---

## 🤝 Contributing

1. Create or update `story.md` + `story.json`
2. Add or reference datasets (with provenance + license)
3. Attach media with attribution
4. Open a PR for review 🧾

> [!TIP]
> Keep PRs small: one narrative improvement or one layer addition per PR is easier to review and validate.

---

## 📜 Credits & licensing (placeholders)

- **Narrative text:** © contributors (see repo license)
- **Datasets:** see dataset metadata (license varies)
- **Archival media:** follow source-specific rights (LOC/archives/public domain varies)

---

### 🧭 Maintainers
- `TBD` (add GitHub handles)