---
title: "TEMPLATE — Story Node Title 🗺️✨"
path: "docs/reports/story_nodes/<story_slug>/story.md"
doc_kind: "StoryNode"
status: "draft" # draft | review | published | deprecated
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
language: "en"

# Identity (stable + machine-ingestible)
story_node_id: "kfm:story_node:<story_slug>:v0.1.0"   # ✅ stable URN-style ID (update when version bumps)
slug: "<story_slug>"                                  # e.g., dust-bowl-1934
display_title: "<Story Node Title>"
subtitle: "<Optional subtitle>"

# Summary cards / galleries
summary: "<1–3 sentences. What will the reader learn?>"
cover_image: "assets/cover.jpg"
thumbnail_image: "assets/thumbnail.jpg"
estimated_read_time_minutes: "TBD"

# FAIR+CARE / governance ⚖️
license: "CC-BY-4.0"
jurisdiction: "US-KS"
fair_category: "FAIR+CARE"
care_label: "n/a"               # e.g., "indigenous_sensitive" | "community_restricted" | "n/a"
sensitivity: "public"           # public | restricted | sensitive
classification: "open"          # open | controlled | embargoed
sovereignty_notice: "n/a"       # add if Indigenous/community governance applies
redaction_notes: "n/a"          # describe any intentional redactions/generalization (coords, names, etc.)

# Authorship & attribution 👥
authors:
  - name: "TBD"
    role: "author"              # author | editor | reviewer | data_steward
    affiliation: "TBD"
    contact: "TBD"
    orcid: "TBD"
review:
  reviewers: []
  approval_required: false
  review_ticket: "TBD"          # e.g., GitHub issue/PR number
  published_by: "TBD"
  published_on: "YYYY-MM-DD"

# UI presentation defaults 🖥️📱
ui:
  default_layout: "split"       # split | overlay | story-only
  panel_position: "left"        # left | right | bottom
  scroll_driven: false          # true = scroll triggers steps (if supported)
  allow_free_explore: true
  map_mode_default: "2d"        # 2d | 3d
  renderer_hint: "maplibre"     # maplibre | cesium | hybrid
  show_citations_panel: true
  show_evidence_button: true
  show_ai_disclosure: true

# Coverage 🧭
coverage:
  spatial:
    bbox_wgs84: [ -102.05, 36.99, -94.59, 40.00 ]   # [minLon, minLat, maxLon, maxLat] (Kansas default)
    places:
      - label: "<Place name>"
        graph_id: "kfm:place:<id>"                  # link to KG entity
  temporal:
    start: "YYYY-MM-DD"
    end: "YYYY-MM-DD"
    key_instants: []                                 # e.g., ["1934-05-01", "1935-04-14"]

# Linkage to governed artifacts 🔗
links:
  node_config: "node.config.json"                    # JSON config that drives map/timeline steps
  evidence_manifest: "evidence/EM-XXXX.yaml"          # machine-readable evidence list
  prov_bundle: "evidence/SN-XXXX.prov.jsonld"         # PROV JSON-LD snippet/bundle for lineage
  related_story_nodes: []                             # ["kfm:story_node:..."]
  related_pulse_threads: []                           # optional live narrative links
  related_concepts: []                                # Conceptual Attention Nodes IDs
  related_datasets: []                                # DCAT/STAC IDs
  related_graph_entities: []                          # KG entity IDs referenced in text

# AI disclosure 🤖 (required if any AI contributed)
ai_assistance:
  used: false
  model: "n/a"                                       # e.g., "gpt-5.x" (or internal)
  tools: []                                          # e.g., ["FocusMode-RAG", "Summarizer", "OCR"]
  generated_sections: []                              # list of headings/anchors AI contributed to
  human_verification_notes: "n/a"                     # describe what was verified and how
  confidence_notes: "n/a"                             # if applicable

# Integrity (optional but recommended) 🧾
integrity:
  commit_sha: "<commit-hash>"
  content_checksum: "sha256:<to-be-filled>"
  config_checksum: "sha256:<to-be-filled>"
  evidence_checksum: "sha256:<to-be-filled>"
  prov_checksum: "sha256:<to-be-filled>"
---

# 🗺️ <Story Node Title>  
![KFM](https://img.shields.io/badge/KFM-Story%20Node-blue) ![Status](https://img.shields.io/badge/status-draft-lightgrey) ![Evidence](https://img.shields.io/badge/evidence-first-success)

> ⚠️ **Template Notice**: Replace all `<placeholders>` and `TBD` fields.  
> ✅ **Evidence-first**: every factual claim must have a citation that maps to the Evidence Manifest (`links.evidence_manifest`).  
> 🧠 **Fact vs. interpretation**: clearly label interpretation/hypothesis vs. sourced facts.

---

## 📘 Overview

### Purpose
- <Why does this story exist? What decision/learning does it support?>

### Scope (In / Out)
| ✅ In scope | 🚫 Out of scope |
|---|---|
| <What is covered?> | <What is explicitly not covered?> |
| <Time span?> | <Other regions?> |
| <Data domains?> | <Speculative claims without evidence?> |

### Audience
- Primary: <e.g., educators, historians, analysts, land managers>
- Secondary: <e.g., general public, students>

---

## 🗂️ Story Node Bundle Layout (recommended)

> KFM Story Nodes are typically shipped as a small “bundle” folder with narrative + config + evidence.

```text
📁 docs/reports/story_nodes/<story_slug>/
├─ 📄 story.md                ✅ (this file)
├─ ⚙️ node.config.json        ✅ map/timeline steps
├─ 📁 assets/
│  ├─ 🖼️ cover.jpg
│  ├─ 🖼️ step-01.jpg
│  └─ 🎞️ optional.mp4
└─ 📁 evidence/
   ├─ 🧾 EM-XXXX.yaml          ✅ evidence manifest (machine-readable)
   └─ 🧬 SN-XXXX.prov.jsonld   ✅ PROV bundle (machine-readable)
```

---

## 🧠 Semantic Links (Knowledge Graph-ready)

When you mention a key entity (place/person/event/dataset/document), link it to the knowledge graph.  
Use one of these patterns (pick **one** convention and stick to it):

- **Link style**: `[Fort Riley](kfm://graph/place/kfm:place:fort_riley)`  
- **Tag style**: `<!-- kfm:entity type="place" id="kfm:place:fort_riley" label="Fort Riley" -->`

> Tip: If the entity doesn’t exist yet, create a stub request in `related_graph_entities` + open a governance ticket.

---

## 🧭 Key Takeaways (TL;DR)

- **Takeaway 1:** <one sentence>[^E1]  
- **Takeaway 2:** <one sentence>[^E2]  
- **Takeaway 3:** <one sentence>[^E3]

---

## 🕰️ Timeline at a Glance

| Year / Date | What happened? | Evidence |
|---|---|---|
| <YYYY> | <event summary> | [^E1] |
| <YYYY-MM-DD> | <event summary> | [^E2] |

---

## 🗺️ Story Steps (slides / chapters)

> Each step should align with a `steps[]` entry in `node.config.json`.  
> Keep steps tight: **1 core idea + 1 map change + 1–2 pieces of evidence**.

---

<!-- KFM_STEP: step-01 -->
### 1) <Step Title 01> 🧭

**Context:** <Set the scene. Where/when are we?>[^E1]

**Claim (fact):** <A factual statement backed by evidence.>[^E1]  
**Claim (fact):** <Another factual statement backed by evidence.>[^E2]

> 🧠 **Interpretation (label clearly):** <Your analysis/interpretation/hypothesis — still cite what informed it.>[^E3]

<details>
<summary>🧩 Step 01 — Map & timeline intent (human-readable)</summary>

- **Map mode:** 2D / 3D  
- **Camera:** center `<lon, lat>`, zoom `<z>`, bearing `<deg>`, pitch `<deg>`  
- **Time:** `<year>` or `<start,end>`  
- **Layers ON:** `<layer_a>`, `<layer_b>`  
- **Layers OFF:** `<layer_x>`  
- **Highlight:** `<feature_id>` (optional)  
- **Media:** `assets/step-01.jpg` (alt text + caption required)  

</details>

---

<!-- KFM_STEP: step-02 -->
### 2) <Step Title 02> 🗺️

**What changes now:** <Describe the map/time/layer change.>[^E2]

**Claim (fact):** <Sourced statement.>[^E2]  
**Claim (fact):** <Sourced statement.>[^E4]

<details>
<summary>🧩 Step 02 — Map & timeline intent (human-readable)</summary>

- **Map mode:** 2D / 3D  
- **Camera:** center `<lon, lat>`, zoom `<z>`  
- **Time:** `<year>` or `<start,end>`  
- **Layers ON/OFF:** `<...>`  
- **Compare mode:** optional (before/after, swipe, split)  

</details>

---

<!-- KFM_STEP: step-03 -->
### 3) <Step Title 03> 🧪

**Method snapshot (if chart/analysis appears):**  
- Metric: `<name>`  
- Aggregation: `<mean/max/percentile>`  
- Geography: `<county/region/grid>`  
- Time window: `<...>`  
- Repro steps: see **Methods** below.  

**Claim (fact):** <Sourced statement.>[^E5]

> 🤖 **AI-assisted text (ONLY if used):**  
> Mark AI-drafted passages clearly, and ensure every sentence is cited or explicitly marked as uncertain.

---

<!-- KFM_STEP: step-04 -->
### 4) <Step Title 04> 📍

**Local focus:** <Zoom into a place/site and connect evidence.>[^E3]

---

<!-- KFM_STEP: step-05 -->
### 5) <Step Title 05> ✅

**Conclusion:** <What should the reader remember?>[^E1]  
**Open questions:** <What still needs research?>  
**Next recommended exploration:** <Link to layers, datasets, or related stories.>

---

## 🔎 Methods (Reproducible & Auditable)

> If the story includes calculations, summaries, or derived charts, record how they were produced.  
> The **Evidence Manifest** should include parameters, queries, and checksums for reproducibility.

### Data inputs
- Dataset A: `<DCAT id or STAC id>`[^E1]  
- Dataset B: `<DCAT id or STAC id>`[^E2]

### Query / computation (example)
```sql
-- REPLACE_ME: query used for a statistic shown in Step 03
SELECT
  county_id,
  AVG(value) AS mean_value
FROM some_table
WHERE year BETWEEN 1930 AND 1939
GROUP BY county_id;
```

### Output artifacts
- Chart/table shown in Step 03: `<path or UI component id>`
- Derived layer (if any): `<STAC item id>` (must be cataloged if published)

---

## 🧾 Citations (keep this block short: 3–7 lines)

1. **[E1]** <Primary dataset/document reference>  
2. **[E2]** <Primary dataset/document reference>  
3. **[E3]** <Primary dataset/document reference>  
4. **[E4]** <Optional supporting source>  
5. **[E5]** <Optional supporting source>

---

## ✅ QA / Definition of Done (DoD)

### Evidence & trust 🧾
- [ ] Every factual claim has a citation (`[^E#]`)  
- [ ] Every `[^E#]` maps to an entry in `evidence/EM-XXXX.yaml`  
- [ ] Any AI-generated content is clearly labeled and cited  
- [ ] Facts vs interpretation are visually separated

### Governance ⚖️
- [ ] Sensitivity/classification fields are set correctly  
- [ ] Sovereignty/CARE notes included if applicable  
- [ ] Media licenses + credits documented (images, video, audio)

### UI integrity 🗺️
- [ ] `node.config.json` validates against schema (if available)  
- [ ] Step IDs match between markdown and config  
- [ ] Map states are reproducible (camera, layers, time)  
- [ ] Layers referenced exist in the layer registry and have provenance

### Accessibility ♿
- [ ] All images have alt text + captions  
- [ ] Color-dependent charts have text labels or patterns  
- [ ] Any audio/video has captions or transcript link

---

## 🧩 Appendices (copy out into separate files)

<details>
<summary>⚙️ Appendix A — node.config.json (copy → <code>node.config.json</code>)</summary>

```json
{
  "schema_version": "1.0",
  "story_node_id": "kfm:story_node:<story_slug>:v0.1.0",
  "title": "<Story Node Title>",
  "ui": {
    "layout": "split",
    "panel_position": "left",
    "scroll_driven": false,
    "renderer": "maplibre"
  },
  "steps": [
    {
      "id": "step-01",
      "title": "<Step Title 01>",
      "anchor": "kfm_step_step-01",
      "map": {
        "mode": "2d",
        "camera": { "center": [-96.5, 38.5], "zoom": 6.2, "bearing": 0, "pitch": 0 },
        "time": { "kind": "year", "value": 1934 },
        "layers": { "on": ["<layer_id_a>"], "off": ["<layer_id_b>"] },
        "highlights": []
      },
      "media": [
        {
          "type": "image",
          "src": "assets/step-01.jpg",
          "alt": "<REQUIRED alt text>",
          "caption": "<Caption>",
          "credit": "<Creator / institution>",
          "license": "<License>"
        }
      ],
      "focus_mode": {
        "suggested_questions": [
          "<What does this layer show?>",
          "<What changed between step 01 and 02?>"
        ],
        "concepts": ["<concept_id_optional>"]
      }
    },
    {
      "id": "step-02",
      "title": "<Step Title 02>",
      "anchor": "kfm_step_step-02",
      "map": {
        "mode": "2d",
        "camera": { "center": [-98.0, 38.5], "zoom": 6.6, "bearing": 0, "pitch": 0 },
        "time": { "kind": "range", "start": "1930-01-01", "end": "1939-12-31" },
        "layers": { "on": ["<layer_id_c>"], "off": ["<layer_id_a>"] },
        "highlights": []
      },
      "media": []
    }
  ],
  "exports": {
    "share_url_enabled": true,
    "offline_pack_hint": "optional"
  },
  "notes": {
    "governance": "Do not bypass API. Respect redaction rules."
  }
}
```

</details>

<details>
<summary>🧾 Appendix B — Evidence Manifest (copy → <code>evidence/EM-XXXX.yaml</code>)</summary>

```yaml
schema_version: "1.0"
evidence_manifest_id: "kfm:evidence_manifest:EM-XXXX"
story_node_id: "kfm:story_node:<story_slug>:v0.1.0"
generated: "YYYY-MM-DD"
generated_by:
  agent_type: "human"     # human | ai | hybrid
  agent_id: "TBD"
  notes: "TBD"

evidence:
  - id: "E1"
    kind: "dataset"       # dataset | document | image | web | code | analysis
    title: "<Dataset or document title>"
    kfm_catalog_ref:
      dcat_dataset_id: "<dcat:...>"
      stac_item_id: "<stac:...>"   # optional
    source:
      uri: "<source URL or repo path>"
      version: "<version/date>"
      checksum: "sha256:<...>"     # REQUIRED for reproducibility if possible
    extraction:
      method: "<sql_query|manual_quote|clip|aggregation|geoprocess>"
      parameters: {}
      query: |
        -- optional
        SELECT ...
    used_in:
      steps: ["step-01", "step-03"]
      claims: ["C1", "C2"]
    license: "<license>"
    sensitivity: "public"
    notes: "TBD"

  - id: "E2"
    kind: "document"
    title: "<Archive / paper / report title>"
    source:
      uri: "<repo path or stable URL>"
      checksum: "sha256:<...>"
    extraction:
      method: "manual_quote"
      locator: "p.12, lines 4–10"
      excerpt: "<short excerpt (avoid long quotes)>"
    used_in:
      steps: ["step-01"]
      claims: ["C1"]
    license: "<license>"
    sensitivity: "public"
    notes: "TBD"
```

</details>

<details>
<summary>🧬 Appendix C — PROV JSON-LD (copy → <code>evidence/SN-XXXX.prov.jsonld</code>)</summary>

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "kfm": "https://kansasfrontiermatrix.org/ns#"
  },
  "@id": "kfm:prov_bundle:SN-XXXX",
  "@type": "prov:Bundle",
  "kfm:storyNode": {
    "@id": "kfm:story_node:<story_slug>:v0.1.0",
    "@type": ["prov:Entity", "kfm:StoryNode"],
    "dct:title": "<Story Node Title>",
    "prov:wasAttributedTo": { "@id": "kfm:agent:<author_or_team_id>" },
    "prov:wasDerivedFrom": [
      { "@id": "kfm:evidence:E1" },
      { "@id": "kfm:evidence:E2" }
    ]
  },
  "kfm:authoringActivity": {
    "@id": "kfm:activity:story_authoring:<uuid>",
    "@type": "prov:Activity",
    "prov:used": [
      { "@id": "kfm:evidence:E1" },
      { "@id": "kfm:evidence:E2" }
    ],
    "prov:wasAssociatedWith": [
      { "@id": "kfm:agent:<author_or_team_id>" },
      { "@id": "kfm:agent:<ai_agent_id_optional>" }
    ],
    "prov:generated": { "@id": "kfm:story_node:<story_slug>:v0.1.0" }
  },
  "kfm:agents": [
    {
      "@id": "kfm:agent:<author_or_team_id>",
      "@type": "prov:Agent",
      "dct:title": "<Author name or team>"
    }
  ]
}
```

</details>

---

## 🕰️ Change Log

| Version | Date | Change | Author |
|---|---:|---|---|
| v0.1.0 | YYYY-MM-DD | Initial draft | <name> |

---

## Footnotes (placeholders)

[^E1]: <Evidence reference that maps to Evidence Manifest E1>  
[^E2]: <Evidence reference that maps to Evidence Manifest E2>  
[^E3]: <Evidence reference that maps to Evidence Manifest E3>  
[^E4]: <Evidence reference that maps to Evidence Manifest E4>  
[^E5]: <Evidence reference that maps to Evidence Manifest E5>